"""Probes this study needs and F001 did not.

F001 was a tree of day-collapsers, a day-axis extremum and an elementwise
power, so the useful questions were about scale, location and path dependence.
This tree is different: its middle node is a PAIR operator rolling along the
day axis (`cross_cov(x, y, 15)`), and its outer node is an order statistic
(`ts_quantile_q75(·, 5)`).  None of the built-in probes answer what one
actually needs to know about those:

* Does a pair operator treat its two arguments symmetrically, or is one of
  them privileged?  (If it is symmetric, "x explains y" is not a reading the
  expression supports.)
* Does it relate the two series contemporaneously, or across a lag?  A
  covariance over a rolling window is contemporaneous by construction -- but
  that is a claim about the implementation, and this measures it: put an
  impulse in x at day i and in y at day j and see which (i, j) pairs move the
  output.
* For an order statistic, WHICH order statistic?  Feed a known ramp and read
  off where the output lands.

These live here, not in partura/probes.py, because they are questions about
this tree.  The next study loads its own file.
"""

import torch

from partura.probes import ProbeContext, probe


def _is_pair_rolling(s):
    return s.category == "pair_rolling" and s.compute_axis == "D"


@probe("argument_symmetric", question="f(x, y) 与 f(y, x) 是否相同?(两个操作数是否对称)",
       applies=lambda s: s.arity == 2)
def _symmetric(ctx: ProbeContext):
    xs = ctx.operands(101, positive=False)
    return ctx.close(ctx.call(xs), ctx.call(list(reversed(xs))))


@probe("cross_lag_response", question="x 在第 i 天、y 在第 i+L 天各打一个脉冲,交互项随 L 怎么衰减?"
                                      "(同期配对,还是真的跨期配对)",
       applies=_is_pair_rolling)
def _cross_lag(ctx: ProbeContext):
    """Interaction magnitude as a function of the lag L between the two impulses,
    normalised by L = 0.

    Read it carefully: a rolling covariance pairs x_t with y_t only, so a
    genuine lead-lag pairing would show a peak away from L = 0.  A nonzero but
    much smaller response at L != 0 is NOT lead-lag -- it is the window's means
    moving, since an impulse anywhere in the window shifts x-bar and y-bar and
    therefore every deviation.  The first run of this probe returned a flat
    "lags [-3..3]" and that is exactly the mistake it was rewritten to avoid.
    """
    D = ctx.shape[0]
    base_x, base_y = ctx.sample(111), ctx.sample(112)
    ref = ctx.call([base_x, base_y]).double()
    i = D // 2
    prof = {}
    for lag in range(-3, 4):
        j = i + lag
        if not (0 <= j < D):
            continue
        x, y = base_x.clone(), base_y.clone()
        x[i] += 30.0
        y[j] += 30.0
        xo = base_x.clone(); xo[i] += 30.0
        yo = base_y.clone(); yo[j] += 30.0
        inter = (ctx.call([x, y]).double() - ctx.call([xo, base_y]).double()
                 - ctx.call([base_x, yo]).double() + ref).abs()
        m = torch.isfinite(inter)
        prof[lag] = float(inter[m].max()) if m.any() else float("nan")
    z = prof.get(0) or 1.0
    return {"peak_lag": max(prof, key=lambda k: prof[k]),
            "profile_vs_lag0": {k: round(v / z, 4) for k, v in sorted(prof.items())}}


@probe("effective_quantile", question="喂一段已知的斜坡,输出落在第几分位?(这个顺序统计量到底取的是哪一位)",
       applies=lambda s: s.requires_window and s.arity == 1 and s.compute_axis in ("D",))
def _effective_quantile(ctx: ProbeContext):
    w = ctx.window or 5
    D = max(ctx.shape[0], w * 4)
    ramp = torch.arange(D, dtype=torch.float64).reshape(-1, 1).repeat(1, ctx.shape[1])
    out = ctx.call([ramp]).double()[-1, 0]
    lo, hi = float(D - w), float(D - 1)          # the last window holds [D-w, D-1]
    if hi <= lo:
        return None
    return round(float((out - lo) / (hi - lo)), 3)
