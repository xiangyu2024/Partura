"""Probes this tree needs and neither F001 nor F002 did.

The tree is  cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15).

Read by name it says "kurtosis of the intraday autocorrelation of returns".
Read by kernel it is something else, and three questions decide what:

* `nt_ts_autocorr_s1(x, 3)` is a Pearson correlation over THREE pairs with an
  `+EPS` in the denominator.  What does it return when the window is constant
  (a stock whose price did not tick for four minutes)?  NaN, or exactly 0?
  And what does ONE isolated price change in a flat stretch produce?
  -> `constant_input_value`, `impulse_in_zeros`.
* With only three pairs the estimator is far from its population value even on
  iid noise.  Where does its null distribution sit?  -> `iid_null_location`.
* The denominator is `sqrt(var_x * var_y) + 1e-9`.  The homogeneity probe says
  degree 0, but it feeds O(1) numbers; minute returns are 1e-4 .. 1e-3, where
  `sqrt(var_x * var_y)` is itself 1e-9 .. 1e-6.  -> `eps_shrink_at_scale`.
* (added after x1) In the bulk of the data K is NOT explained by how many
  minutes moved (daily Spearman with the share of non-zero minutes: -0.05).
  A local simulation suggested the other candidate: with three pairs the sample
  correlation is so skewed that its SHAPE moves with the true first-order
  autocorrelation of the input.  -> `ar1_response` (self-check: at window 60
  the mean of the rolling autocorrelation must read phi itself).
* `day_kurt` collapses the 241 per-minute values.  If its input is mostly one
  repeated value (0) with a few exceptions, kurtosis stops measuring "tail
  shape" and becomes a SPARSITY meter: for a two-point input with a fraction w
  of exceptions it is 1/(w(1-w)) - 6.  -> `two_point_response`.

Self-checks (operators whose answer is known analytically) are in
`selfcheck()` at the bottom; `x1_anatomy.py` runs them on the server before
any of these probes is used to read the tree.
"""

import math

import torch

from partura.probes import ProbeContext, probe


def _rolls_rows(s):          # a rolling kernel whose window runs along the rows of its 2-D view
    return bool(s.requires_window) and s.arity == 1 and s.face in ("nt", "nd") and s.family == "ts"


def _reduces(s):
    return bool(getattr(s, "reduces_m", False)) and s.arity == 1


@probe("constant_input_value", question="输入是常数(窗口内方差为 0)时输出什么?NaN、0,还是别的?",
       applies=lambda s: s.arity == 1 and s.compute_axis is not None)
def _const(ctx: ProbeContext):
    x = torch.full(ctx.shape, 0.0, dtype=torch.float64)
    out = ctx.call([x]).double()
    tail = out[-1] if out.shape[0] == ctx.shape[0] and out.shape[-1] != 1 else out.flatten()
    tail = tail.flatten()
    if bool(torch.isnan(tail).all()):
        return "nan"
    v = tail[torch.isfinite(tail)]
    return round(float(v.mean()), 6) if float(v.std() if v.numel() > 1 else 0.0) < 1e-9 else "varies"


@probe("impulse_in_zeros", question="全 0 序列里放一个孤立脉冲(一次价格跳动),输出在脉冲之后各行是多少?",
       applies=_rolls_rows)
def _impulse(ctx: ProbeContext):
    R = ctx.shape[0]
    i = R // 2
    x = torch.zeros(ctx.shape, dtype=torch.float64)
    x[i] = 1.0
    out = ctx.call([x]).double()[:, 0]
    return {f"+{k}": (None if not math.isfinite(float(out[i + k])) else round(float(out[i + k]), 4))
            for k in range(0, (ctx.window or 3) + 2) if i + k < R}


@probe("iid_null_location", question="iid 高斯输入下输出的均值 / 中位数 / |值|>0.9 的比例(小窗口估计量的零分布在哪)",
       applies=_rolls_rows)
def _null(ctx: ProbeContext):
    g = torch.Generator().manual_seed(5)
    x = torch.randn((400, 200), generator=g, dtype=torch.float64)
    out = ctx.call([x]).double()[(ctx.window or 3) + 1:].flatten()
    out = out[torch.isfinite(out)]
    return {"mean": round(float(out.mean()), 3), "median": round(float(out.median()), 3),
            "frac_abs_gt_0.9": round(float((out.abs() > 0.9).double().mean()), 3)}


@probe("two_point_response", question="输入是两点分布(M 个 0 里有 k 个 1)时输出随 k 怎么变?(是不是稀疏度计)",
       applies=_reduces)
def _two_point(ctx: ProbeContext):
    M = 240
    res = {}
    for k in (1, 2, 6, 24, 60, 120):
        x = torch.zeros((2, M), dtype=torch.float64)
        x[:, :k] = 1.0
        v = float(ctx.call([x]).double().flatten()[0])
        res[f"k={k}"] = None if not math.isfinite(v) else round(v, 3)
    return res


@probe("eps_shrink_at_scale",
       question="把 iid 输入缩到分钟收益的真实量级时,输出相对 O(1) 输入还剩多少?(分母里的 +EPS 是不是隐藏的尺度门槛)",
       applies=_rolls_rows)
def _eps(ctx: ProbeContext):
    g = torch.Generator().manual_seed(7)
    x = torch.randn((400, 50), generator=g, dtype=torch.float64)
    base = ctx.call([x]).double()
    res = {}
    for c in (1e-3, 3e-4, 1e-4, 3e-5):
        out = ctx.call([x * c]).double()
        m = torch.isfinite(base) & torch.isfinite(out) & (base.abs() > 1e-6)
        res[f"{c:g}"] = round(float((out[m] / base[m]).median()), 3)
    return res


@probe("ar1_response",
       question="输入是 AR(1) 序列时,输出沿时间的均值 / 超额峰度随真实系数 phi 怎么变?(小窗口相关的分布**形状**是不是在量 phi)",
       applies=_rolls_rows)
def _ar1(ctx: ProbeContext):
    """241 'minutes' x 400 independent 'days' of x_t = phi * x_{t-1} + e_t.  For each
    day: the mean and the excess kurtosis of the kernel's output along time; the
    median over days is reported.  Self-check built in: at window 60 the MEAN of a
    rolling lag-1 autocorrelation must read phi itself (minus the usual small-sample
    bias), otherwise the probe is not measuring what it claims."""
    w0 = ctx.window or 3

    def read(window):
        out = {}
        for phi in (-0.4, -0.2, 0.0, 0.2, 0.4):
            g = torch.Generator().manual_seed(11)
            e = torch.randn((241, 400), generator=g, dtype=torch.float64)
            x = torch.empty_like(e)
            x[0] = e[0]
            for t in range(1, 241):
                x[t] = phi * x[t - 1] + e[t]
            o = ctx.call([x], window=window).double()[window + 1:]
            m = o.nanmean(dim=0)
            d = o - m
            k = (d ** 4).nanmean(dim=0) / (d ** 2).nanmean(dim=0) ** 2 - 3.0
            out[f"{phi:+.1f}"] = (round(float(m.median()), 3), round(float(k.median()), 3))
        return out

    here = read(w0)
    res = {f"phi={k}": {"mean": v[0], "kurt": v[1]} for k, v in here.items()}
    if "autocorr" in ctx.spec.name:
        ref = read(60)
        res["selfcheck_w60_mean_reads_phi"] = {k: v[0] for k, v in ref.items()}
        res["selfcheck"] = "PASS" if all(abs(v[0] - float(k)) < 0.06 for k, v in ref.items()) else "FAIL"
    return res


def selfcheck(reg) -> None:
    """Run each probe on an operator whose answer is known, print PASS/FAIL."""
    from partura.probes import run_probes, values

    def val(name, probe_name, window=None):
        return values(run_probes(reg._ops[name], window=window, only=[probe_name])).get(probe_name)

    w = lambda k: k / 240.0
    exp_kurt = {f"k={k}": round(1.0 / (w(k) * (1 - w(k))) - 6.0, 3) for k in (1, 2, 6, 24, 60, 120)}
    exp_mean = {f"k={k}": round(w(k), 3) for k in (1, 2, 6, 24, 60, 120)}
    checks = [
        ("constant_input_value", "day_mean", None, 0.0),              # mean of zeros is 0
        ("constant_input_value", "day_kurt", None, "nan"),            # 0/0
        ("impulse_in_zeros", "nt_ts_mean", 3, {"+0": 0.3333, "+1": 0.3333, "+2": 0.3333, "+3": 0.0, "+4": 0.0}),
        ("two_point_response", "day_mean", None, exp_mean),           # fraction of ones
        ("two_point_response", "day_kurt", None, exp_kurt),           # analytic Bernoulli excess kurtosis
    ]
    for pname, op, win, expect in checks:
        got = val(op, pname, win)
        print(f"[selfcheck] {pname:<22} on {op:<12} expect {expect}  got {got}  -> {'PASS' if got == expect else 'FAIL'}")
    one = {"0.001": 1.0, "0.0003": 1.0, "0.0001": 1.0, "3e-05": 1.0}
    got = val("nt_ts_rank", "eps_shrink_at_scale", 5)                # a rank has no denominator: scale-free at any scale
    print(f"[selfcheck] eps_shrink_at_scale    on nt_ts_rank   expect {one}  got {got}  -> {'PASS' if got == one else 'FAIL'}")
    got = val("nt_ts_autocorr_s1", "iid_null_location", 60)
    print(f"[selfcheck] iid_null_location      on nt_ts_autocorr_s1(w=60) expect mean≈-1/60, few |r|>0.9  got {got}  -> "
          f"{'PASS' if got and abs(got['mean'] + 1 / 60) < 0.02 and got['frac_abs_gt_0.9'] < 0.001 else 'FAIL'}")
