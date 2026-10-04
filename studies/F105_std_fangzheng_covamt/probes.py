"""Probes this tree needs: ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5).

The tree is "a positive, heavy-tailed, scale-carrying daily quantity (intraday variance of Amt)
-> 3-day max -> a ONE-YEAR hard-window statistic (mean + std) -> the 5-day std of that slow level".
The built-in probes run on a 40-row sample, which is shorter than the 241-day window, so they cannot
see what a 241-day window does (the built-in ``effective_memory`` reads 27 for cross_fangzheng only
because 40 - 13 = 27 rows are left after the impulse).  Four questions the built-ins do not answer:

* ``window_exit_echo`` -- a hard rolling window forgets a value abruptly d days later.  How big is the
  output's step when an impulse LEAVES the window, relative to the step when it ENTERS?  If the ratio
  is ~1, anything that reads the *change* of this node (the outer ts_stddev does) fires twice: once on
  the event and once on its d-day anniversary.
* ``chain_impulse_profile`` -- the same question for the whole chain of this tree, built from the real
  kernels: on which lags after an impulse is the root non-zero, and how large is the anniversary echo
  against the entry response?  Also on a noisy lognormal background (does the echo survive noise?).
* ``tail_dominance`` -- mean + std of a heavy-tailed positive series: is it a level (follows the
  window mean / median) or an extreme-value statistic (follows the window max)?
* ``std_reads_change`` -- what does a short rolling std read on a slow level: a step of size J, a ramp
  of slope s, and does it keep the direction of the change?

Every probe carries a self-check on a kernel whose answer is known analytically (cross_mean,
cross_decay_linear, cross_max, ts_delta); a probe whose self-check fails must not be used.
"""

import math

import torch

from partura.probes import ProbeContext, probe


def _kernel(name):
    from alphacube.catalog import default_registry
    return default_registry()._ops[name].fn


def _rolling_unary_d(s):
    return bool(s.requires_window) and s.compute_axis == "D" and s.arity == 1


def _impulse(days: int, t0: int, size: float = 50.0, cols: int = 3) -> torch.Tensor:
    x = torch.ones((days, cols), dtype=torch.float64)
    x[t0] += size
    return x


def _steps(fn, w: int, size: float = 50.0):
    """(entry step, exit step) of ``fn(x, w)`` for a single impulse on a constant background,
    measured where the window is full."""
    days, t0 = 3 * w + 40, w + 10
    y = fn(_impulse(days, t0, size), w).double().reshape(days, -1)[:, 0]
    return float(y[t0] - y[t0 - 1]), float(y[t0 + w] - y[t0 + w - 1])


@probe("window_exit_echo",
       question="脉冲滑出硬窗口那天,输出的跳变相对于进入那天有多大?(≈1 说明读这个节点『变化』的外层会在 d 天后再响一次)",
       applies=_rolling_unary_d)
def _exit_echo(ctx: ProbeContext):
    w = int(ctx.window)
    ent, ext = _steps(lambda x, d: ctx.call([x], window=d), w)
    # known answers at the same window: a flat mean steps +X/w then -X/w (ratio 1);
    # a linearly-decaying mean steps +2X/(w+1) and loses only 2X/(w(w+1)) at the exit (ratio 1/w).
    m_ent, m_ext = _steps(_kernel("cross_mean"), w)
    d_ent, d_ext = _steps(_kernel("cross_decay_linear"), w)
    return {"window": w, "entry_step": round(ent, 5), "exit_step": round(ext, 5),
            "exit_over_entry": round(abs(ext) / abs(ent), 4) if abs(ent) > 1e-12 else None,
            "selfcheck": {"cross_mean_entry_is_X/w": abs(m_ent - 50.0 / w) < 1e-9,
                          "cross_mean_ratio_is_1": abs(abs(m_ext) / abs(m_ent) - 1.0) < 1e-9,
                          "decay_linear_entry_is_2X/(w+1)": abs(d_ent - 100.0 / (w + 1)) < 1e-9,
                          "decay_linear_ratio_is_1/w": abs(abs(d_ext) / abs(d_ent) - 1.0 / w) < 1e-6}}


def _ranges(lags):
    """[0,1,2,241,242] -> ['0..2', '241..242']"""
    out, start, prev = [], None, None
    for v in lags:
        if start is None:
            start = prev = v
        elif v == prev + 1:
            prev = v
        else:
            out.append(f"{start}..{prev}")
            start = prev = v
    if start is not None:
        out.append(f"{start}..{prev}")
    return out


def _chain(x: torch.Tensor, mid: str = "cross_fangzheng", w_max: int = 3, w_mid: int = 241, w_out: int = 5):
    b = _kernel("cross_max")(x, w_max)
    c = _kernel(mid)(b, w_mid)
    return _kernel("ts_stddev")(c, w_out).double(), c.double()


@probe("chain_impulse_profile",
       question="整条链 ts_stddev(fangzheng(max(x,3),241),5):脉冲之后根节点在哪些滞后上非零?一年后的回声相对进入时多大?",
       applies=lambda s: s.name == "cross_fangzheng")
def _chain_profile(ctx: ProbeContext):
    days, t0, size = 620, 300, 50.0
    x = _impulse(days, t0, size)
    d, _ = _chain(x)
    d = d.reshape(days, -1)[:, 0]
    lags = [int(i) - t0 for i in torch.nonzero(d > 1e-9).flatten()]
    entry = float(d[t0:t0 + 20].max())
    echo = float(d[t0 + 241:t0 + 261].max())
    # known answer: with cross_mean in the middle the level is a 3-step staircase of height X/241 each,
    # and the 5-day population std of [0,a,2a,3a,3a] is sqrt(6.8/5)*a.
    dm, _ = _chain(x, mid="cross_mean")
    dm = dm.reshape(days, -1)[:, 0]
    a = size / 241.0
    mean_ok = abs(float(dm[t0:t0 + 20].max()) - math.sqrt(6.8 / 5.0) * a) < 1e-9
    mean_echo_ok = abs(float(dm[t0 + 241:t0 + 261].max()) - float(dm[t0:t0 + 20].max())) < 1e-9
    # no-echo reference: a linearly-decaying mean in the middle
    dd, _ = _chain(x, mid="cross_decay_linear")
    dd = dd.reshape(days, -1)[:, 0]
    # noisy background: lognormal day values (sigma 1), a spike of k x the median on one day
    g = torch.Generator().manual_seed(11)
    noisy = {}
    for k in (10.0, 100.0):
        xb = torch.exp(torch.randn((days, 200), generator=g, dtype=torch.float64))
        base, _ = _chain(xb)
        xs = xb.clone()
        xs[t0] += k
        dn, _ = _chain(xs)
        bg = float(base[260:].median())
        noisy[f"spike_{k:g}x_median"] = {
            "entry_peak_over_background_median": round(float(dn[t0:t0 + 8].max(dim=0).values.median()) / bg, 1),
            "echo_peak_over_background_median": round(float(dn[t0 + 241:t0 + 249].max(dim=0).values.median()) / bg, 1)}
    return {"nonzero_lag_ranges": _ranges(lags), "n_nonzero_days": len(lags), "entry_peak": round(entry, 4), "echo_peak": round(echo, 4),
            "echo_over_entry": round(echo / entry, 4),
            "decay_linear_mid_echo_over_entry": round(float(dd[t0 + 241:t0 + 261].max()) / float(dd[t0:t0 + 20].max()), 4),
            "noisy_background": noisy,
            "selfcheck": {"mean_chain_entry_peak_is_sqrt(6.8/5)X/241": mean_ok,
                          "mean_chain_echo_equals_entry": mean_echo_ok}}


@probe("tail_dominance",
       question="喂重尾正值序列(对数正态,σ 越大尾越重):输出跟着窗口最大值走,还是跟着窗口均值/中位数走?",
       applies=_rolling_unary_d)
def _tail(ctx: ProbeContext):
    w = int(ctx.window)
    out = {}
    for sigma in (0.5, 1.0, 1.5, 2.5):
        g = torch.Generator().manual_seed(int(sigma * 10))
        x = torch.exp(sigma * torch.randn((w, 600), generator=g, dtype=torch.float64))
        y = ctx.call([x], window=w).double().reshape(w, -1)[-1]
        out[f"sigma_{sigma:g}"] = {"vs_window_max": round(ctx.spearman(y, x.max(dim=0).values), 3),
                                   "vs_window_mean": round(ctx.spearman(y, x.mean(dim=0)), 3),
                                   "vs_window_median": round(ctx.spearman(y, x.median(dim=0).values), 3)}
    g = torch.Generator().manual_seed(15)
    x = torch.exp(1.5 * torch.randn((w, 600), generator=g, dtype=torch.float64))
    mx = _kernel("cross_max")(x, w).double().reshape(w, -1)[-1]
    mn = _kernel("cross_mean")(x, w).double().reshape(w, -1)[-1]
    return {"window": w, **out,
            "selfcheck": {"cross_max_reads_max": ctx.spearman(mx, x.max(dim=0).values) > 0.9999,
                          "cross_mean_reads_mean": ctx.spearman(mn, x.mean(dim=0)) > 0.9999}}


@probe("std_reads_change",
       question="短窗滚动标准差作用在一个慢变水平上读出什么?(阶跃 J、斜坡 s 各读多少;升和降分不分)",
       applies=lambda s: s.name in ("ts_stddev", "ts_std", "cross_stddev"))
def _std_change(ctx: ProbeContext):
    w = int(ctx.window)
    days = 60
    step = {}
    for k in range(1, w):                      # k = days since the step, inside a w-day window
        x = torch.zeros((days, 2), dtype=torch.float64)
        x[40:] = 1.0
        y = ctx.call([x], window=w).double().reshape(days, -1)[:, 0]
        step[k] = round(float(y[40 + k - 1]), 4)
    analytic = {k: round(math.sqrt(k * (w - k)) / w, 4) for k in range(1, w)}
    ramp = torch.arange(days, dtype=torch.float64).reshape(-1, 1).repeat(1, 2)
    r_up = float(ctx.call([ramp], window=w).double().reshape(days, -1)[-1, 0])
    r_dn = float(ctx.call([-ramp], window=w).double().reshape(days, -1)[-1, 0])
    after = torch.zeros((days, 2), dtype=torch.float64)
    after[40:] = 1.0
    gone = float(ctx.call([after], window=w).double().reshape(days, -1)[40 + w - 1, 0])
    # known answer for direction: ts_delta keeps the sign of a ramp, a std cannot
    dl = _kernel("ts_delta")
    return {"window": w, "step_response_by_days_since": step, "analytic_sqrt(k(w-k))/w": analytic,
            "ramp_slope1": round(r_up, 4), "ramp_slope-1": round(r_dn, 4),
            "analytic_ramp_sqrt((w^2-1)/12)": round(math.sqrt((w * w - 1) / 12.0), 4),
            "w_days_after_step": round(gone, 6),
            "selfcheck": {"step_matches_analytic": all(abs(step[k] - analytic[k]) < 1e-4 for k in step),
                          "ramp_matches_analytic": abs(r_up - math.sqrt((w * w - 1) / 12.0)) < 1e-6,
                          "ts_delta_is_signed": float(dl(ramp, w)[-1, 0]) == -float(dl(-ramp, w)[-1, 0])}}
