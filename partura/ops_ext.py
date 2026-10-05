"""Partura's operator extension: kernels added while doing research.

They are registered into AlphaCube's own ``OPERATOR_REGISTRY`` through its ``op``
decorator, so the parser, the engine, the probes and ``study.sh ops / src`` see
them exactly like built-ins -- without touching the AlphaCube checkout (other
sessions mine with it).  Upstreaming one = copying the function into the matching
``alphacube/operators/*.py`` module.

**The docstring of each kernel is its definition.  Read that, not the name.**

Conventions (the same as AlphaCube's kernels):
* ``dt`` kernels see a 2-D tensor whose LAST axis is the minute axis (``in`` /
  ``day`` families) or whose FIRST axis is the trading-day axis (``cross``);
  a ``day`` kernel returns ``(..., 1)``.
* ``nd`` kernels see ``(days, stocks)``: ``cs`` works along the last axis.
* NaN = missing; a kernel never invents a value for a missing input.

Why each one exists is recorded in ``docs/new_operators.md``.
"""
from __future__ import annotations

import math

import torch

from alphacube.operators.common import EPS, op, rolling_windows

NAN = float("nan")


def _f(x: torch.Tensor) -> torch.Tensor:
    return x if x.is_floating_point() else x.float()


# ----------------------------------------------------------------------------- minute axis (in_*)

@op("dt", "in", arity=1, requires_window=True)
def in_pct(x: torch.Tensor, d: int) -> torch.Tensor:
    """Relative change over ``d`` minutes: ``x[t] / x[t-d] - 1``.

    NaN for the first ``d`` minutes and wherever the base ``x[t-d]`` is NaN or 0.
    On Close with d=1 this is the minute return (~ the ``Ret`` field); on Volume or
    Amt it is the minute *volume change rate* -- the same shape of quantity, which
    is why the two can be swapped inside a tree.  Scale-free (degree 0)."""
    x = _f(x)
    d = int(d)
    out = torch.full_like(x, NAN)
    T = x.shape[-1]
    if d < T:
        base = x[..., : T - d]
        out[..., d:] = torch.where(base != 0, x[..., d:] / base - 1.0, torch.full_like(base, NAN))
    return out


@op("dt", "in", arity=1, requires_window=True)
def in_logchg(x: torch.Tensor, d: int) -> torch.Tensor:
    """Log change over ``d`` minutes: ``log(x[t] / x[t-d])`` for positive x (NaN otherwise
    and for the first ``d`` minutes).  Symmetric in up/down moves, unlike ``in_pct``,
    whose right tail is unbounded and left tail stops at -1 -- that asymmetry matters
    for volume, which jumps by multiples."""
    x = _f(x)
    d = int(d)
    out = torch.full_like(x, NAN)
    T = x.shape[-1]
    if d < T:
        a, b = x[..., d:], x[..., : T - d]
        ok = (a > 0) & (b > 0)
        out[..., d:] = torch.where(ok, torch.log(a.clamp(min=1e-30) / b.clamp(min=1e-30)), torch.full_like(a, NAN))
    return out


# ----------------------------------------------------------------------------- day collapse (day_*)

def _day(v: torch.Tensor, ok: torch.Tensor) -> torch.Tensor:
    """(...,) values, NaN where ``ok`` is False, returned as (..., 1)."""
    return torch.where(ok, v, torch.full_like(v, NAN)).unsqueeze(-1)


@op("dt", "day", arity=1)
def day_flat_ratio(x: torch.Tensor) -> torch.Tensor:
    """Share of minutes (2nd to last) whose value equals the previous minute's:
    ``mean(x[t] == x[t-1])`` over minutes where both are finite.

    On a price field: 1.0 = the quote never moved (suspended, or locked at the limit
    all day); a liquid stock sits near 0.2-0.5.  It names the 'frozen book' state
    directly instead of reading it off a kurtosis that saturates there."""
    x = _f(x)
    a, b = x[..., 1:], x[..., :-1]
    ok = torch.isfinite(a) & torch.isfinite(b)
    n = ok.sum(-1)
    r = ((a == b) & ok).sum(-1).to(x.dtype) / n.clamp(min=1).to(x.dtype)
    return _day(r, n > 0)


@op("dt", "day", arity=1)
def day_pos_ratio(x: torch.Tensor) -> torch.Tensor:
    """Share of finite minutes with ``x > 0`` (zeros count as not positive).
    On Ret: the fraction of up-minutes.  Unlike a mean or a skew it ignores sizes."""
    x = _f(x)
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    r = ((x > 0) & ok).sum(-1).to(x.dtype) / n.clamp(min=1).to(x.dtype)
    return _day(r, n > 0)


@op("dt", "day", arity=2)
def day_wmean(x: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
    """Weighted mean over the day's minutes: ``sum(x * |w|) / sum(|w|)`` where both are
    finite; NaN when the weights sum to 0.  ``day_wmean(Ret, Amt)`` is the
    turnover-weighted minute return -- what the money actually experienced, as opposed
    to ``day_mean(Ret)``, which weights a dead minute like a busy one."""
    x, w = _f(x), _f(w).abs()
    ok = torch.isfinite(x) & torch.isfinite(w)
    xw = torch.where(ok, x * w, torch.zeros_like(x)).sum(-1)
    sw = torch.where(ok, w, torch.zeros_like(w)).sum(-1)
    return _day(xw / sw.clamp(min=1e-30), sw > 0)


@op("dt", "day", arity=2)
def day_signed_ratio(x: torch.Tensor, y: torch.Tensor) -> torch.Tensor:
    """``sum(|y| * sign(x)) / sum(|y|)`` over minutes where both are finite, in [-1, 1].

    ``day_signed_ratio(Ret, Amt)``: share of the day's turnover traded in up-minutes
    minus the share traded in down-minutes -- a net buying-pressure proxy that needs
    no tick data.  Minutes with x == 0 count in the denominator only."""
    x, y = _f(x), _f(y).abs()
    ok = torch.isfinite(x) & torch.isfinite(y)
    num = torch.where(ok, y * torch.sign(x), torch.zeros_like(y)).sum(-1)
    den = torch.where(ok, y, torch.zeros_like(y)).sum(-1)
    return _day(num / den.clamp(min=1e-30), den > 0)


@op("dt", "day", arity=1)
def day_gini(x: torch.Tensor) -> torch.Tensor:
    """Gini coefficient of ``|x|`` across the day's finite minutes: 0 = spread evenly,
    -> 1 = everything in a few minutes.  Scale-free and bounded, so unlike
    ``day_kurt`` / max-share it cannot be dominated by one print, and unlike
    ``day_std / day_mean`` it does not explode on thin days."""
    x = _f(x).abs()
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    v = torch.where(ok, x, torch.full_like(x, float("inf")))          # missing minutes sort last
    v, _ = torch.sort(v, dim=-1)
    v = torch.where(torch.isfinite(v), v, torch.zeros_like(v))
    idx = torch.arange(1, x.shape[-1] + 1, device=x.device, dtype=x.dtype)
    tot = v.sum(-1)
    nf = n.to(x.dtype)
    g = (2.0 * (v * idx).sum(-1) / (nf.clamp(min=1) * tot.clamp(min=1e-30))) - (nf + 1.0) / nf.clamp(min=1)
    return _day(g, (n > 1) & (tot > 0))


@op("dt", "day", arity=1)
def day_centroid(x: torch.Tensor) -> torch.Tensor:
    """Centre of mass of ``|x|`` along the minute axis, scaled to [0, 1]:
    ``sum(t * |x[t]|) / sum(|x|) / (T - 1)``.  0 = all at the open, 1 = all at the
    close, 0.5 = symmetric.  On Volume / Amt: *when* in the day the trading happened --
    information that every order-free statistic (std, kurt, gini) throws away."""
    x = _f(x).abs()
    ok = torch.isfinite(x)
    v = torch.where(ok, x, torch.zeros_like(x))
    T = x.shape[-1]
    t = torch.arange(T, device=x.device, dtype=x.dtype) / max(T - 1, 1)
    tot = v.sum(-1)
    return _day((v * t).sum(-1) / tot.clamp(min=1e-30), tot > 0)


# ----------------------------------------------------------------------------- day axis (cross_*)

@op("dt", "cross", arity=1, requires_window=True)
def cross_ema(x: torch.Tensor, d: int) -> torch.Tensor:
    """Causal exponential moving average along the trading-day axis with HALF-LIFE ``d``
    days: ``y[t] = sum_k a(1-a)^k x[t-k] / sum_k a(1-a)^k`` over the days where x is
    finite, ``a = 1 - 0.5 ** (1/d)``.  A missing day is skipped (its weight is dropped),
    not treated as 0.  It lets an expression carry its own smoothing instead of leaving
    it to the book's half-life -- and, unlike ``cross_mean``, an old spike fades instead
    of dropping out of a hard window."""
    x = _f(x)
    a = 1.0 - 0.5 ** (1.0 / max(float(d), 1e-6))
    q = 1.0 - a
    ok = torch.isfinite(x)
    v = torch.where(ok, x, torch.zeros_like(x))
    m = ok.to(x.dtype)
    out = torch.empty_like(x)
    cn = torch.zeros_like(x[0])
    cd = torch.zeros_like(x[0])
    shape = (-1,) + (1,) * (x.dim() - 1)
    # exact recursion, done block-wise so the engine pays for a handful of Python steps instead of one per day:
    # a block is as long as q**-(B-1) <= 1e30 allows (float32), i.e. ~100 days at half-life 1, everything at 60
    B = int(min(x.shape[0], max(8.0, 69.0 / max(-math.log(q), 1e-9))))
    for s0 in range(0, x.shape[0], B):
        vb, mb = v[s0:s0 + B], m[s0:s0 + B]
        k = torch.arange(vb.shape[0], device=x.device, dtype=x.dtype)
        up, dn = (q ** (-k)).view(shape), (q ** k).view(shape)
        n_t = dn * (q * cn + a * torch.cumsum(vb * up, 0))
        d_t = dn * (q * cd + a * torch.cumsum(mb * up, 0))
        out[s0:s0 + B] = torch.where(d_t > 1e-12, n_t / d_t.clamp(min=1e-12), torch.full_like(n_t, NAN))
        cn, cd = n_t[-1], d_t[-1]
    return out


@op("dt", "cross", arity=1, requires_window=True)
def cross_zscore(x: torch.Tensor, d: int) -> torch.Tensor:
    """Today's value relative to its own last ``d`` days: ``(x[t] - mean_d) / (std_d + EPS)``,
    mean and std over the finite days of the window (today included).  Turns a level
    (amount, volatility) into 'unusual for THIS stock', removing the persistent
    cross-sectional level that makes level factors all look like the same factor."""
    x = _f(x)
    w = rolling_windows(x, int(d), 0)
    ok = torch.isfinite(w)
    n = ok.sum(-1)
    w0 = torch.where(ok, w, torch.zeros_like(w))
    m = w0.sum(-1) / n.clamp(min=1).to(x.dtype)
    var = (torch.where(ok, (w - m.unsqueeze(-1)) ** 2, torch.zeros_like(w))).sum(-1) / n.clamp(min=1).to(x.dtype)
    z = (x - m) / (torch.sqrt(var) + EPS)
    return torch.where((n > 1) & torch.isfinite(x), z, torch.full_like(x, NAN))


# ----------------------------------------------------------------------------- cross-section (cs_*)

def _pct_rank(x: torch.Tensor, ok: torch.Tensor) -> torch.Tensor:
    v = torch.where(ok, x, torch.full_like(x, torch.finfo(x.dtype).max))
    r = (torch.argsort(torch.argsort(v, dim=-1, stable=True), dim=-1, stable=True) + 1).to(x.dtype)
    n = ok.sum(-1, keepdim=True).to(x.dtype)
    return torch.where(ok, r / n.clamp(min=1), torch.full_like(x, NAN))


@op("nd", "cs", arity=2)
def cs_bucket_rank(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """Percentile rank of ``y`` among the stocks in the SAME DECILE of ``x`` that day
    (deciles of x by rank; NaN where either is missing).

    'y, neutral to x' without a regression: within every x-decile the output is
    uniform on (0, 1], so its top decile holds the same share of every x-bucket --
    which a linear rank residual (``cs_regres(cs_rank(y), cs_rank(x))``) does not
    guarantee in the tails."""
    y, x = _f(y), _f(x)
    ok = torch.isfinite(y) & torch.isfinite(x)
    bx = torch.ceil(_pct_rank(x, ok) * 10.0).clamp(1, 10)              # 1..10, NaN where missing
    out = torch.full_like(y, NAN)
    for b in range(1, 11):
        m = ok & (bx == b)
        out = torch.where(m, _pct_rank(y, m), out)
    return out


@op("nd", "cs", arity=1)
def cs_winsor(x: torch.Tensor) -> torch.Tensor:
    """Clip each day's cross-section at its own 1% and 99% quantiles (NaN stays NaN).
    For heavy-tailed inputs feeding a mean, a regression or an EMA: the EMA of a raw
    heavy-tailed value is a peak memory, the EMA of the clipped value is a level."""
    x = _f(x)
    lo = torch.nanquantile(x, 0.01, dim=-1, keepdim=True)
    hi = torch.nanquantile(x, 0.99, dim=-1, keepdim=True)
    return torch.where(torch.isfinite(x), torch.minimum(torch.maximum(x, lo), hi), x)


NEW_OPERATORS = ("in_pct", "in_logchg", "day_flat_ratio", "day_pos_ratio", "day_wmean", "day_signed_ratio",
                 "day_gini", "day_centroid", "cross_ema", "cross_zscore", "cs_bucket_rank", "cs_winsor")


def install() -> None:
    """Make the registry and the legacy name tables pick the new kernels up, whatever was built before."""
    import alphacube.catalog as catalog
    import alphacube.operators as ops
    from alphacube.operators.common import OPERATOR_REGISTRY
    for name in NEW_OPERATORS:
        meta = OPERATOR_REGISTRY[name]
        if meta["mode"] in ("dt", "shared"):
            ops.operator_dict_DT[name] = meta["fn"]
        if meta["mode"] in ("nd", "shared"):
            ops.operator_dict_ND[name] = meta["fn"]
    catalog._DEFAULT = None            # rebuilt, with the extensions, on next use


install()
