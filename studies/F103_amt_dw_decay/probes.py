"""Probes this tree needs:

    cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)

The tree is "a 30-day average of the intraday Amt CURVE (minute slot by minute slot) -> a
roughness statistic of that average curve -> cubed -> times today's last-bar Amt -> 5-day max".
The built-in probes say DW is scale-free and order-dependent; they do not say what one needs to
know to read it when the operand is a non-negative, averaged volume curve:

* ``isolated_spike_response`` -- a flat curve with ONE spike of height h (an auction bar, a block
  print): what does a day reducer return, and does it matter whether the spike is the last bar or
  an interior one?  For DW the analytic answer is (h-1)^2/(M-1+h^2) at the end and twice that in
  the middle (an interior spike has two jumps, an end spike one).
* ``noise_averaging_exponent`` -- average N independent noisy curves FIRST, then reduce: output
  ~ N^p.  p = -1 means "averaging first removes day-to-day independent noise at rate 1/N", which
  is the whole difference between DW(decay30(Amt)) and decay30(DW(Amt)).
* ``impulse_footprint`` -- an impulse at (day i, column j) of a day-axis rolling operator: which
  columns and which lags respond, with what weights, and what is the effective sample size
  (sum w)^2 / sum w^2?  On the dt face a "column" is a MINUTE slot, so this is what shows that
  cross_decay_linear(Amt, 30) averages each minute slot over days and never mixes minutes.
* ``window_one_is_identity`` -- is f(x, 1) == x?  (`ts_min(., 1)` sits in the middle of the tree.)
* ``trailing_nan_fallback`` -- when the last bars of the day are NaN, which bar does the reducer read?

Every probe carries a self-check on kernels whose answer is known, reported under "selfcheck";
a probe whose self-check fails must not be used to read this tree.
"""

import math

import torch

from partura.probes import ProbeContext, is_day_reducer, probe

M = 241


def _kernel(name):
    from alphacube.catalog import default_registry
    return default_registry()._ops[name].fn


def _day_unary(s):
    return is_day_reducer(s) and s.arity == 1 and not s.requires_window


def _day_rolling_unary(s):
    return bool(s.requires_window) and s.arity == 1 and s.compute_axis == "D"


def _first(t: torch.Tensor) -> float:
    return float(t.double().flatten()[0])


def _spiked(pos: int, h: float, rows: int = 3) -> torch.Tensor:
    x = torch.ones((rows, M), dtype=torch.float64)
    x[:, pos] = h
    return x


@probe("isolated_spike_response",
       question="水平为 1 的平坦曲线上放一个高度 h 的孤立尖峰(集合竞价那一根/一笔大单):输出多少?尖峰在末端还是中间有没有区别?",
       applies=_day_unary)
def _spike(ctx: ProbeContext):
    fn = lambda x: ctx.call([x])
    out = {}
    formula_ok = True
    for h in (5.0, 20.0, 80.0):
        e, mid = _first(fn(_spiked(M - 1, h))), _first(fn(_spiked(M // 2, h)))
        dw_end = (h - 1.0) ** 2 / (M - 1 + h * h)
        formula_ok &= abs(e - dw_end) < 1e-6 and abs(mid - 2 * dw_end) < 1e-6
        out[f"h={h:g}"] = {"end": round(e, 5), "middle": round(mid, 5),
                           "middle/end": round(mid / e, 3) if e not in (0.0,) and math.isfinite(e) else None}
    out["equals_(h-1)^2/(M-1+h^2)_end_and_twice_that_in_middle"] = bool(formula_ok)
    sd, dl = _kernel("day_std"), _kernel("day_last")
    ok_std = abs(_first(sd(_spiked(M - 1, 20.0))) / _first(sd(_spiked(M // 2, 20.0))) - 1.0) < 1e-9
    ok_last = _first(dl(_spiked(M - 1, 20.0))) == 20.0 and _first(dl(_spiked(M // 2, 20.0))) == 1.0
    return {**out, "selfcheck": {"day_std_is_position_free": bool(ok_std), "day_last_reads_the_end_only": bool(ok_last)}}


def _avg_exponent(fn, sigma: float = 0.3, rows: int = 96):
    g = torch.Generator().manual_seed(7)
    ns, vals = (1, 4, 16, 64), []
    for n in ns:
        x = (1.0 + sigma * torch.randn((rows, n, M), generator=g, dtype=torch.float64)).clamp(min=1e-6)
        vals.append(float(fn(x.mean(1)).double().nanmean()))
    lx = [math.log(n) for n in ns]
    ly = [math.log(abs(v)) if v != 0 and math.isfinite(v) else float("nan") for v in vals]
    if any(not math.isfinite(v) for v in ly):
        return None, vals
    mx, my = sum(lx) / len(lx), sum(ly) / len(ly)
    p = sum((a - mx) * (b - my) for a, b in zip(lx, ly)) / sum((a - mx) ** 2 for a in lx)
    return p, vals


@probe("noise_averaging_exponent",
       question="把 N 条独立带噪曲线(均值 1、噪声 0.3)先平均再喂进去,输出 ∝ N^p 的 p 是多少?(先平均能压掉多少逐日独立的噪声)",
       applies=_day_unary)
def _avg(ctx: ProbeContext):
    p, vals = _avg_exponent(lambda x: ctx.call([x]))
    checks = {}
    for name, expect in (("day_mean", 0.0), ("day_std", -0.5), ("day_var", -1.0)):
        q, _ = _avg_exponent(_kernel(name))
        checks[f"{name}_p≈{expect:g}"] = bool(q is not None and abs(q - expect) < 0.05)
    return {"p": None if p is None else round(p, 3),
            "value_at_N=1,4,16,64": [round(v, 5) for v in vals], "selfcheck": checks}


def _footprint(fn, w: int, cols: int = 6):
    D = 2 * w + 12
    g = torch.Generator().manual_seed(11)
    base = torch.rand((D, cols), generator=g, dtype=torch.float64) + 1.0
    i, j, amp = w + 2, cols // 2, 30.0
    x = base.clone()
    x[i, j] += amp
    diff = (fn(x, w).double() - fn(base, w).double())
    diff = torch.where(torch.isfinite(diff), diff, torch.zeros_like(diff))
    hit_cols = [int(c) for c in torch.nonzero(diff.abs().sum(0) > 1e-9).flatten()]
    lags = [int(r) - i for r in torch.nonzero(diff.abs().sum(1) > 1e-9).flatten()]
    wts = (diff[i:, j] / amp)
    wts = wts[wts.abs() > 1e-12]
    neff = float(wts.sum() ** 2 / (wts ** 2).sum()) if wts.numel() else float("nan")
    return {"columns_hit": hit_cols, "impulse_column": j, "lags_hit": [min(lags), max(lags)] if lags else [],
            "weight_at_lag0": round(float(wts[0]), 4) if wts.numel() else None,
            "weight_at_last_lag": round(float(wts[-1]), 4) if wts.numel() else None,
            "effective_n": round(neff, 2)}


@probe("impulse_footprint",
       question="在 (第 i 天, 第 j 列) 打一个脉冲:哪些列、哪些滞后天有响应,权重怎么分布,有效样本数 (Σw)²/Σw² 是多少?"
                "(dt 面上列 = 分钟槽位:日轴滚动是不是逐分钟各滚各的)",
       applies=_day_rolling_unary)
def _foot(ctx: ProbeContext):
    w = int(ctx.window or 5)
    res = _footprint(lambda x, d: ctx.call([x], window=d), w)
    ref = _footprint(_kernel("cross_mean"), 10)
    ok = (ref["columns_hit"] == [ref["impulse_column"]] and ref["lags_hit"] == [0, 9]
          and abs(ref["effective_n"] - 10.0) < 1e-6 and abs(ref["weight_at_lag0"] - 0.1) < 1e-9)
    return {**res, "window": w, "selfcheck": {"cross_mean(10)_same_column_lags_0..9_flat_0.1_neff_10": bool(ok)}}


def _w1_identity(fn) -> bool:
    g = torch.Generator().manual_seed(31)
    x = torch.randn((20, 7), generator=g, dtype=torch.float64)
    x[3, 2] = float("nan")
    out = fn(x, 1).double()
    same_nan = bool((torch.isnan(out) == torch.isnan(x)).all())
    m = torch.isfinite(x) & torch.isfinite(out)
    return bool(same_nan and (out[m] - x[m]).abs().max() < 1e-12)


@probe("window_one_is_identity", question="窗口取 1 时是不是恒等变换?(数值和 NaN 位置都不变)",
       applies=_day_rolling_unary)
def _w1(ctx: ProbeContext):
    val = _w1_identity(lambda x, d: ctx.call([x], window=d))
    return {"identity_at_window_1": val,
            "selfcheck": {"ts_max(x,1)_is_identity": _w1_identity(_kernel("ts_max")),
                          "ts_delay(x,1)_is_not": not _w1_identity(_kernel("ts_delay"))}}


@probe("trailing_nan_fallback", question="当天最后 3 根是 NaN 时,输出等于哪一根?(读的是'最后一个有效分钟'还是固定的最后一列)",
       applies=_day_unary)
def _trail(ctx: ProbeContext):
    x = torch.arange(M, dtype=torch.float64).reshape(1, -1).repeat(3, 1) + 1.0      # bar m holds m+1
    x[:, -3:] = float("nan")
    v = _first(ctx.call([x]))
    y = x.clone()
    y[:, :2] = float("nan")
    ok_first = _first(_kernel("day_first")(y)) == 3.0                              # first valid bar is index 2
    return {"output": v, "equals_last_valid_bar(M-3)": bool(v == float(M - 3)),
            "selfcheck": {"day_first_reads_first_valid_bar": bool(ok_first)}}
