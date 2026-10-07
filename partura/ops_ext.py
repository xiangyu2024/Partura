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


@op("dt", "day", arity=1, real_valued=True)
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
    x32 = _f(x)
    # In float64: inside a block the terms are scaled by q**-k (up to 1e30), and a float32 input of the size of a
    # traded amount (1e8 and more, 1e16 once squared) overflowed there -- the EMA of any amount-level quantity came
    # back NaN on most cells (found by the F105 lead: coverage 0.49 at d = 5).  Bounded inputs were never affected.
    x = x32.to(torch.float64)
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
    # a block is as long as q**-(B-1) <= 1e30 allows, i.e. ~100 days at half-life 1, everything at 60
    B = int(min(x.shape[0], max(8.0, 69.0 / max(-math.log(q), 1e-9))))
    for s0 in range(0, x.shape[0], B):
        vb, mb = v[s0:s0 + B], m[s0:s0 + B]
        k = torch.arange(vb.shape[0], device=x.device, dtype=x.dtype)
        up, dn = (q ** (-k)).view(shape), (q ** k).view(shape)
        n_t = dn * (q * cn + a * torch.cumsum(vb * up, 0))
        d_t = dn * (q * cd + a * torch.cumsum(mb * up, 0))
        out[s0:s0 + B] = torch.where(d_t > 1e-12, n_t / d_t.clamp(min=1e-12), torch.full_like(n_t, NAN))
        cn, cd = n_t[-1], d_t[-1]
    return out.to(x32.dtype)


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
    # The same within-bucket ranks repeat in all ten buckets, i.e. ten-way ties everywhere; break them by
    # the overall rank of y (weight 1e-4 << one within-bucket step), so no decile book hangs on symbol order.
    return out + 1e-4 * _pct_rank(y, ok)


@op("nd", "cs", arity=1)
def cs_winsor(x: torch.Tensor) -> torch.Tensor:
    """Clip each day's cross-section at its own 1% and 99% quantiles (NaN stays NaN).
    For heavy-tailed inputs feeding a mean, a regression or an EMA: the EMA of a raw
    heavy-tailed value is a peak memory, the EMA of the clipped value is a level."""
    x = _f(x)
    lo = torch.nanquantile(x, 0.01, dim=-1, keepdim=True)
    hi = torch.nanquantile(x, 0.99, dim=-1, keepdim=True)
    return torch.where(torch.isfinite(x), torch.minimum(torch.maximum(x, lo), hi), x)


# ----------------------------------------------------------------------------- asked for by the studies

@op("dt", "day", arity=1, real_valued=True)
def day_zero_ratio(x: torch.Tensor) -> torch.Tensor:
    """Share of the day's finite minutes with ``x == 0`` exactly.

    On Ret: the mass of the point at zero -- minutes in which the price did not move
    (locked at the limit, suspended, no trade).  ``day_flat_ratio`` on Ret would mix
    'did not move twice' with 'moved by the same amount twice'; this does not.
    (Requested by the F114 study: its tree turned out to be reading this atom.)"""
    x = _f(x)
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    r = ((x == 0) & ok).sum(-1).to(x.dtype) / n.clamp(min=1).to(x.dtype)
    return _day(r, n > 0)


@op("dt", "cross", arity=1, requires_window=True)
def cross_valid_count(x: torch.Tensor, d: int) -> torch.Tensor:
    """Number of the last ``d`` trading days (today included) on which ``x`` is finite:
    an integer in 0..d, never NaN.

    The cube has no listing date and no suspension flag; both show up only as NaN
    patterns.  ``cross_valid_count(day_last(Close), 241) < 241`` = listed (or resumed)
    within the last year; a small count on a short window = recently suspended.
    (Requested by F114: the largest segment effect in its anatomy was listing age.)"""
    x = _f(x)
    return torch.isfinite(rolling_windows(x, int(d), 0)).sum(-1).to(x.dtype)


def _tail_mean(x: torch.Tensor, d: int, q: float, low: bool) -> torch.Tensor:
    w = rolling_windows(_f(x), int(d), 0)
    ok = torch.isfinite(w)
    n = ok.sum(-1)
    thr = torch.nanquantile(torch.where(ok, w, torch.full_like(w, NAN)), q, dim=-1, keepdim=True)
    sel = ok & ((w <= thr) if low else (w >= thr))
    m = torch.where(sel, w, torch.zeros_like(w)).sum(-1) / sel.sum(-1).clamp(min=1).to(w.dtype)
    return torch.where((n >= 2) & (sel.sum(-1) > 0), m, torch.full_like(m, NAN))


@op("dt", "cross", arity=1, requires_window=True)
def cross_tail_mean_q25(x: torch.Tensor, d: int) -> torch.Tensor:
    """Mean of the values at or below the 25% quantile of the last ``d`` days (the lower
    tail's conditional mean); NaN with fewer than 2 finite days.  Same tail as
    ``cross_quantile_q25`` but averaged over the tail instead of read at one order
    statistic, so 'which tail' and 'how noisily it is estimated' can be told apart."""
    return _tail_mean(x, d, 0.25, True)


@op("dt", "cross", arity=1, requires_window=True)
def cross_tail_mean_q75(x: torch.Tensor, d: int) -> torch.Tensor:
    """Mean of the values at or above the 75% quantile of the last ``d`` days (upper-tail
    conditional mean); NaN with fewer than 2 finite days."""
    return _tail_mean(x, d, 0.75, False)


def _lexi(y: torch.Tensor, x: torch.Tensor, lo: float, hi: float, shift: float) -> torch.Tensor:
    """rank(y) in (0, 1], shifted by ``shift`` for the stocks whose x-rank is in (lo, hi]."""
    y, x = _f(y), _f(x)
    ok = torch.isfinite(y) & torch.isfinite(x)
    rx, ry = _pct_rank(x, ok), _pct_rank(y, ok)
    return torch.where(ok, ry + shift * ((rx > lo) & (rx <= hi)).to(y.dtype), torch.full_like(y, NAN))


@op("nd", "cs", arity=2)
def cs_first_low40(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """Rank of ``y`` (in (0, 1]) with every stock in the LOWEST 40% of ``x`` placed above
    every other stock: ``rank(y) + 1`` there, ``rank(y)`` elsewhere.

    'Trade y only where x is low' as an expression: the top of the output is drawn from
    the low-x segment, ordered by y, while every stock keeps a distinct value (no NaN,
    no ties), so the book is still measured against the whole market.  Use it when the
    anatomy says a signal selects only inside one segment (small / illiquid names)."""
    return _lexi(y, x, -1.0, 0.4, 1.0)


@op("nd", "cs", arity=2)
def cs_first_high40(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_first_low40`` but the HIGHEST 40% of ``x`` come first."""
    return _lexi(y, x, 0.6, 1.0, 1.0)


@op("nd", "cs", arity=2)
def cs_last_high20(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """Rank of ``y`` with every stock in the HIGHEST 20% of ``x`` placed BELOW every other
    stock (``rank(y) - 1`` there).  An exclusion screen: those names can never reach the
    long book, the rest keep their order.  'y, but never the names x flags'."""
    return _lexi(y, x, 0.8, 1.0, -1.0)


@op("nd", "cs", arity=2)
def cs_last_low20(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_last_high20`` but it is the LOWEST 20% of ``x`` that are pushed to the bottom."""
    return _lexi(y, x, -1.0, 0.2, -1.0)


@op("dt", "day", arity=1, real_valued=True)
def day_flat_run_max(x: torch.Tensor) -> torch.Tensor:
    """Longest RUN of consecutive minutes whose value equals the previous minute's, divided
    by the number of finite minutes: in [0, 1].

    ``day_flat_ratio`` only counts: a stock locked at the limit for 240 minutes and a thin
    stock whose quote is still half the time, scattered, can share a ratio; they do not
    share a longest run.  (Requested by F108: its kurtosis reads '29 still minutes then
    one print', which is a statement about runs.)"""
    x = _f(x)
    a, b = x[..., 1:], x[..., :-1]
    eq = (a == b) & torch.isfinite(a) & torch.isfinite(b)
    c = torch.cumsum(eq.to(x.dtype), dim=-1)
    reset = torch.cummax(torch.where(eq, torch.zeros_like(c), c), dim=-1).values     # count at the last break
    run = (c - reset).max(dim=-1).values
    n = torch.isfinite(x).sum(-1)
    return _day(run / n.clamp(min=1).to(x.dtype), n > 1)


@op("dt", "in", arity=1, requires_window=True)
def in_madz(x: torch.Tensor, d: int) -> torch.Tensor:
    """Robust 'how isolated is this minute' score along the minute axis:
    ``(x[t] - median_d) / (1.4826 * MAD_d + 1e-6 * |median_d|)`` over the last ``d`` minutes
    (t included); NaN until ``d`` finite minutes are available and where the window does
    not move at all (MAD = 0).

    Scale-free with a RELATIVE epsilon, unlike a rolling kurtosis whose absolute epsilon
    (1e-9 on var**2) crushes low-priced stocks and any return-sized input to a constant.
    (Requested by F108.)"""
    x = _f(x)
    w = rolling_windows(x, int(d), -1)
    ok = torch.isfinite(w)
    full = ok.sum(-1) >= int(d)
    med = torch.nanmedian(w, dim=-1).values
    mad = torch.nanmedian((w - med.unsqueeze(-1)).abs(), dim=-1).values
    z = (x - med) / (1.4826 * mad + 1e-6 * med.abs())
    return torch.where(full & (mad > 0) & torch.isfinite(x), z, torch.full_like(x, NAN))


# ----------------------------------------------------------------------------- third batch: asked for by several studies

def _buckets(x: torch.Tensor, ok: torch.Tensor) -> torch.Tensor:
    return torch.ceil(_pct_rank(x, ok) * 10.0).clamp(1, 10)


@op("nd", "cs", arity=2, real_valued=True)
def cs_bucket_demean(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """``y`` minus the mean of ``y`` over the stocks in the same decile of ``x`` that day.
    Keeps y's units and magnitude (``cs_bucket_rank`` throws them away), so a fold
    ``abs_(cs_bucket_demean(y, x))`` measures 'distance from what is typical FOR ITS OWN
    x-bucket' instead of from the whole-market mean.  NaN where either is missing or the
    bucket has fewer than 2 names.  (Requested by F101, F107, F110.)"""
    y, x = _f(y), _f(x)
    ok = torch.isfinite(y) & torch.isfinite(x)
    bx = _buckets(x, ok)
    out = torch.full_like(y, NAN)
    for b in range(1, 11):
        m = ok & (bx == b)
        n = m.sum(-1, keepdim=True)
        mu = torch.where(m, y, torch.zeros_like(y)).sum(-1, keepdim=True) / n.clamp(min=1).to(y.dtype)
        out = torch.where(m & (n >= 2), y - mu, out)
    return out


@op("nd", "cs", arity=2, real_valued=True)
def cs_bucket_zscore(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_bucket_demean`` but divided by the bucket's own population std (+EPS):
    comparable across buckets whose dispersion differs severalfold.  (F101, F106.)"""
    y, x = _f(y), _f(x)
    ok = torch.isfinite(y) & torch.isfinite(x)
    bx = _buckets(x, ok)
    out = torch.full_like(y, NAN)
    for b in range(1, 11):
        m = ok & (bx == b)
        n = m.sum(-1, keepdim=True)
        nf = n.clamp(min=1).to(y.dtype)
        mu = torch.where(m, y, torch.zeros_like(y)).sum(-1, keepdim=True) / nf
        var = torch.where(m, (y - mu) ** 2, torch.zeros_like(y)).sum(-1, keepdim=True) / nf
        out = torch.where(m & (n >= 2), (y - mu) / (torch.sqrt(var) + EPS), out)
    return out


@op("nd", "cs", arity=1)
def cs_robust_z(x: torch.Tensor) -> torch.Tensor:
    """Cross-sectional robust z-score: ``(x - median) / (1.4826 * MAD + EPS)`` per day."""
    x = _f(x)
    med = torch.nanmedian(x, dim=-1, keepdim=True).values
    mad = torch.nanmedian((x - med).abs(), dim=-1, keepdim=True).values
    return (x - med) / (1.4826 * mad + EPS)


@op("nd", "cs", arity=2)
def cs_first_low20(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_first_low40`` with the lowest 20% of ``x`` first."""
    return _lexi(y, x, -1.0, 0.2, 1.0)


@op("nd", "cs", arity=2)
def cs_first_high20(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_first_high40`` with the highest 20% of ``x`` first."""
    return _lexi(y, x, 0.8, 1.0, 1.0)


@op("nd", "cs", arity=2)
def cs_last_high40(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_last_high20`` with the highest 40% of ``x`` pushed to the bottom."""
    return _lexi(y, x, 0.6, 1.0, -1.0)


@op("nd", "cs", arity=2)
def cs_last_low40(y: torch.Tensor, x: torch.Tensor) -> torch.Tensor:
    """As ``cs_last_low20`` with the lowest 40% of ``x`` pushed to the bottom."""
    return _lexi(y, x, -1.0, 0.4, -1.0)


def _market_series(g: torch.Tensor) -> torch.Tensor:
    """(days,) cross-sectional mean of a (days, stocks) panel."""
    return torch.nanmean(_f(g), dim=-1)


def _trailing_rank(m: torch.Tensor, d: int) -> torch.Tensor:
    """Percentile of m[t] among the finite values of m[t-d+1..t], in (0, 1]; NaN where m[t] is."""
    w = rolling_windows(m.unsqueeze(-1), int(d), 0).squeeze(1)           # (days, d)
    ok = torch.isfinite(w)
    n = ok.sum(-1)
    le = (ok & (w <= m.unsqueeze(-1))).sum(-1)
    return torch.where(torch.isfinite(m) & (n > 0), le.to(m.dtype) / n.clamp(min=1).to(m.dtype), torch.full_like(m, NAN))


@op("nd", "ts", arity=1, requires_window=True)
def cs_state_rank(x: torch.Tensor, d: int) -> torch.Tensor:
    """A MARKET state, the same number for every stock on a day: take the day's
    cross-sectional mean of ``x``, then its percentile within its own last ``d`` days
    (in (0, 1]).  ``cs_state_rank(day_sum(Amt), 60)`` near 1 = the whole market is
    trading heavily relative to the last quarter.

    A per-day constant does nothing to a cross-sectional rank on its own; it becomes
    useful as a weight between two signals, e.g. ``add(mul(s, a), mul(sub(1, s), b))``,
    or as the condition of ``select_where``.  (F107, F112, F115 asked for a way to write
    'only in this kind of market'.)"""
    r = _trailing_rank(_market_series(x), d)
    return r.unsqueeze(-1).expand_as(x).clone()


@op("nd", "cs", arity=2)
def cs_flip_by_state(y: torch.Tensor, g: torch.Tensor) -> torch.Tensor:
    """``+rank(y)`` on days when the market-level state is HIGH and ``-rank(y)`` when it is
    low: state = the day's cross-sectional mean of ``g`` compared with the median of that
    series over the last 241 days; rank(y) is centred on 0 (percentile - 0.5).

    The minimal way to say 'y works in one kind of market and reverses in the other'
    inside an expression.  If y simply stops working in the other state, the flipped
    version will be clearly WORSE than y -- which is itself the test.  (F104.)"""
    y = _f(y)
    m = _market_series(g)
    hi = _trailing_rank(m, 241) > 0.5
    ok = torch.isfinite(y)
    r = _pct_rank(y, ok) - 0.5
    sgn = torch.where(hi, torch.ones_like(m), -torch.ones_like(m)).unsqueeze(-1)
    return torch.where(ok, r * sgn, torch.full_like(y, NAN))


@op("dt", "day", arity=1, real_valued=True)
def day_at_max_ratio(x: torch.Tensor) -> torch.Tensor:
    """Share of the day's finite minutes whose value equals the day's maximum.
    On Close / High: time spent pinned at the day's high -- a limit-up lock reads near 1,
    a normal day near 1/240.  (F106, F110: 'locked at the top' vs 'locked at the bottom'
    are different events and ``day_flat_ratio`` cannot tell them apart.)"""
    x = _f(x)
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    mx = torch.where(ok, x, torch.full_like(x, float("-inf"))).max(dim=-1, keepdim=True).values
    r = ((x == mx) & ok).sum(-1).to(x.dtype) / n.clamp(min=1).to(x.dtype)
    return _day(r, n > 1)


@op("dt", "day", arity=1, real_valued=True)
def day_at_min_ratio(x: torch.Tensor) -> torch.Tensor:
    """Share of the day's finite minutes whose value equals the day's minimum."""
    x = _f(x)
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    mn = torch.where(ok, x, torch.full_like(x, float("inf"))).min(dim=-1, keepdim=True).values
    r = ((x == mn) & ok).sum(-1).to(x.dtype) / n.clamp(min=1).to(x.dtype)
    return _day(r, n > 1)


@op("dt", "day", arity=1, real_valued=True)
def day_distinct_ratio(x: torch.Tensor) -> torch.Tensor:
    """Number of DISTINCT values among the day's finite minutes, divided by their count:
    1/n = one price all day, 1 = every minute different.  On a price: how many price
    levels the day visited -- coarse for low-priced stocks on a one-tick grid.  (F107.)"""
    x = _f(x)
    ok = torch.isfinite(x)
    n = ok.sum(-1)
    v, _ = torch.sort(torch.where(ok, x, torch.full_like(x, float("inf"))), dim=-1)
    new = (v[..., 1:] != v[..., :-1]) & torch.isfinite(v[..., 1:])
    k = new.sum(-1) + (n > 0).to(new.sum(-1).dtype)
    return _day(k.to(x.dtype) / n.clamp(min=1).to(x.dtype), n > 1)


@op("dt", "day", arity=2)
def day_wstd(x: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
    """Weighted population std over the day's minutes: ``sqrt(sum(|w| (x - m)^2) / sum(|w|))``,
    ``m = day_wmean(x, w)``.  ``day_wstd(Ret, Amt)``: volatility as the traded money saw
    it; dead minutes (zero turnover, zero return) no longer dilute it.  (F101.)"""
    x, w = _f(x), _f(w).abs()
    ok = torch.isfinite(x) & torch.isfinite(w)
    w0 = torch.where(ok, w, torch.zeros_like(w))
    sw = w0.sum(-1)
    m = (torch.where(ok, x, torch.zeros_like(x)) * w0).sum(-1) / sw.clamp(min=1e-30)
    var = (w0 * torch.where(ok, (x - m.unsqueeze(-1)) ** 2, torch.zeros_like(x))).sum(-1) / sw.clamp(min=1e-30)
    return _day(torch.sqrt(var), sw > 0)


@op("dt", "day", arity=2)
def day_topw_mean(y: torch.Tensor, w: torch.Tensor) -> torch.Tensor:
    """Mean of ``y`` over the 10% of the day's minutes with the largest ``|w|`` (ties
    included): ``day_topw_mean(Ret, Volume)`` = the average return of the heaviest
    minutes.  An event study in one node, without a trigger mask.  (F115.)"""
    y, w = _f(y), _f(w).abs()
    ok = torch.isfinite(y) & torch.isfinite(w)
    thr = torch.nanquantile(torch.where(ok, w, torch.full_like(w, NAN)), 0.9, dim=-1, keepdim=True)
    sel = ok & (w >= thr)
    k = sel.sum(-1)
    return _day(torch.where(sel, y, torch.zeros_like(y)).sum(-1) / k.clamp(min=1).to(y.dtype), k > 0)


def _es_ratio(x: torch.Tensor, q: float, hi: bool) -> torch.Tensor:
    x = _f(x)
    ok = torch.isfinite(x)
    v = torch.nanquantile(torch.where(ok, x, torch.full_like(x, NAN)), q, dim=-1, keepdim=True)
    sel = ok & ((x > v) if hi else (x < v))
    k = sel.sum(-1)
    es = torch.where(sel, x, torch.zeros_like(x)).sum(-1) / k.clamp(min=1).to(x.dtype)
    v = v.squeeze(-1)
    good = (k > 0) & (v.abs() > 1e-8)
    return _day(es / torch.where(good, v, torch.ones_like(v)), good)


@op("dt", "day", arity=1)
def day_es_ratio_hi(x: torch.Tensor) -> torch.Tensor:
    """Right-tail shape: mean of the minutes ABOVE the day's 95% quantile, divided by that
    quantile; **NaN** when the quantile is (near) zero or no minute exceeds it.
    The hand-written ``erm_*`` factors compute this with ``+1e-6`` in the denominator,
    which turns every locked / dead day (quantile = 0) into a value near 1e4 -- the
    factor then reads 'was there a locked day', not tail shape.  This is the same
    quantity with that day left missing.  (F106, F109.)"""
    return _es_ratio(x, 0.95, True)


@op("dt", "day", arity=1)
def day_es_ratio_lo(x: torch.Tensor) -> torch.Tensor:
    """Left-tail shape: mean of the minutes BELOW the day's 5% quantile, divided by that
    quantile (so it is >= 1 for a negative quantile); NaN when the quantile is (near)
    zero or no minute is below it."""
    return _es_ratio(x, 0.05, False)


@op("dt", "in", arity=1)
def in_index(x: torch.Tensor) -> torch.Tensor:
    """The minute's position in the day, ``t / (T - 1)`` in [0, 1], wherever ``x`` is finite
    (NaN elsewhere).  Lets a tree weight or compare by time of day, e.g.
    ``day_corr(in_index(Volume), Volume)`` = is volume back-loaded.  (F115.)"""
    x = _f(x)
    T = x.shape[-1]
    t = torch.arange(T, device=x.device, dtype=x.dtype) / max(T - 1, 1)
    return torch.where(torch.isfinite(x), t.expand_as(x), torch.full_like(x, NAN))


@op("dt", "in", arity=1)
def in_zscore_expand(x: torch.Tensor) -> torch.Tensor:
    """Expanding-window z-score along the minute axis: ``(x[t] - mean(x[0..t])) /
    (std(x[0..t]) + EPS)`` over the finite minutes so far; NaN until 5 are available.
    'Unusual relative to today so far' -- causal within the day, unlike a full-day
    z-score, which knows the close at the open.  (F110.)"""
    x = _f(x)
    ok = torch.isfinite(x)
    v = torch.where(ok, x, torch.zeros_like(x))
    n = torch.cumsum(ok.to(x.dtype), -1)
    s1, s2 = torch.cumsum(v, -1), torch.cumsum(v * v, -1)
    mu = s1 / n.clamp(min=1)
    var = (s2 / n.clamp(min=1) - mu * mu).clamp(min=0)
    return torch.where(ok & (n >= 5), (x - mu) / (torch.sqrt(var) + EPS), torch.full_like(x, NAN))


@op("dt", "cross", arity=1, requires_window=True)
def cross_madz(x: torch.Tensor, d: int) -> torch.Tensor:
    """Robust version of ``cross_zscore``: ``(x[t] - median_d) / (1.4826 * MAD_d + 1e-6 *
    |median_d|)`` over the last ``d`` days; NaN with fewer than d/2 finite days or MAD = 0.
    A heavy-tailed daily statistic drags a mean / std z-score around with one spike;
    this tells 'standardising is the wrong idea' from 'the estimator was fragile'.  (F104.)"""
    x = _f(x)
    w = rolling_windows(x, int(d), 0)
    n = torch.isfinite(w).sum(-1)
    med = torch.nanmedian(w, dim=-1).values
    mad = torch.nanmedian((w - med.unsqueeze(-1)).abs(), dim=-1).values
    z = (x - med) / (1.4826 * mad + 1e-6 * med.abs())
    return torch.where((n * 2 >= int(d)) & (mad > 0) & torch.isfinite(x), z, torch.full_like(x, NAN))


@op("dt", "cross", arity=1, requires_window=True, real_valued=True)
def cross_flat_ratio(x: torch.Tensor, d: int) -> torch.Tensor:
    """Share of the last ``d`` days on which ``x`` equals the previous day's value exactly
    (over day pairs where both are finite); NaN with fewer than 2 such pairs.  On a daily
    price: how often the stock did not move day to day.  (F111.)"""
    x = _f(x)
    prev = torch.cat([torch.full_like(x[:1], NAN), x[:-1]], dim=0)
    pair = torch.isfinite(x) & torch.isfinite(prev)
    same = torch.where(pair, (x == prev).to(x.dtype), torch.full_like(x, NAN))
    w = rolling_windows(same, int(d), 0)
    ok = torch.isfinite(w)
    n = ok.sum(-1)
    r = torch.where(ok, w, torch.zeros_like(w)).sum(-1) / n.clamp(min=1).to(x.dtype)
    return torch.where(n >= 2, r, torch.full_like(r, NAN))


def _semistd(x: torch.Tensor, d: int, neg: bool) -> torch.Tensor:
    x = _f(x)
    prev = torch.cat([torch.full_like(x[:1], NAN), x[:-1]], dim=0)
    ok = (x > 0) & (prev > 0)
    g = torch.where(ok, torch.log(x.clamp(min=1e-30) / prev.clamp(min=1e-30)), torch.full_like(x, NAN))
    part = torch.where(torch.isfinite(g), (g.clamp(max=0) if neg else g.clamp(min=0)) ** 2, torch.full_like(g, NAN))
    w = rolling_windows(part, int(d), 0)
    okw = torch.isfinite(w)
    n = okw.sum(-1)
    v = torch.where(okw, w, torch.zeros_like(w)).sum(-1) / n.clamp(min=1).to(x.dtype)
    return torch.where(n >= 3, torch.sqrt(v), torch.full_like(v, NAN))


@op("dt", "cross", arity=1, requires_window=True)
def cross_semistd_neg(x: torch.Tensor, d: int) -> torch.Tensor:
    """Downside semi-deviation of the daily log change of a positive ``x`` over the last
    ``d`` days: ``sqrt(mean(min(log(x[t]/x[t-1]), 0)^2))``; NaN with fewer than 3 days.
    Splits a volatility into the half that hurts.  (F112.)"""
    return _semistd(x, d, True)


@op("dt", "cross", arity=1, requires_window=True)
def cross_semistd_pos(x: torch.Tensor, d: int) -> torch.Tensor:
    """Upside semi-deviation of the daily log change of a positive ``x`` over ``d`` days."""
    return _semistd(x, d, False)


@op("dt", "cross", arity=1)
def cross_age(x: torch.Tensor) -> torch.Tensor:
    """Trading days since ``x`` first had a finite value: 0 on that day, +1 every trading
    day after (suspensions included); NaN before.  A stock that is already finite on the
    first day of the data is treated as old (its age starts at 10000), because the data
    cannot say when it listed.  Unlike ``cross_valid_count`` it does not saturate at the
    window.  (F105.)"""
    x = _f(x)
    seen = torch.cummax(torch.isfinite(x).to(x.dtype), dim=0).values
    age = torch.cumsum(seen, dim=0) - 1.0
    old = torch.isfinite(x[:1]).to(x.dtype) * 10000.0
    return torch.where(seen > 0, age + old, torch.full_like(x, NAN))


NEW_OPERATORS = ("in_pct", "in_logchg", "day_flat_ratio", "day_pos_ratio", "day_wmean", "day_signed_ratio",
                 "day_gini", "day_centroid", "cross_ema", "cross_zscore", "cs_bucket_rank", "cs_winsor",
                 "day_zero_ratio", "cross_valid_count", "cross_tail_mean_q25", "cross_tail_mean_q75",
                 "cs_first_low40", "cs_first_high40", "cs_last_high20", "cs_last_low20",
                 "day_flat_run_max", "in_madz",
                 "cs_bucket_demean", "cs_bucket_zscore", "cs_robust_z", "cs_first_low20", "cs_first_high20",
                 "cs_last_high40", "cs_last_low40", "cs_state_rank", "cs_flip_by_state", "day_at_max_ratio",
                 "day_at_min_ratio", "day_distinct_ratio", "day_wstd", "day_topw_mean", "day_es_ratio_hi",
                 "day_es_ratio_lo", "in_index", "in_zscore_expand", "cross_madz", "cross_flat_ratio",
                 "cross_semistd_neg", "cross_semistd_pos", "cross_age")


def install_kernels() -> None:
    """Make the legacy name tables (``operators.operator_dict_DT`` /
    ``operator_dict_ND``) pick the kernels above up, so ``fullcatalog`` /
    ``parse_legacy`` resolve them by name exactly like a built-in.

    The ``@op(...)``-decorated kernels above already land in
    ``operators.common.OPERATOR_REGISTRY`` -- with their ``real_valued`` flag
    already set -- the moment this module is imported; that part needs no
    call.  What used to ALSO need a call, before WP11, was clearing the nine
    boolean-mis-flagged kernels' flags through a ``catalog.build_registry``
    monkeypatch: ``real_valued=True`` on those nine ``@op(...)`` decorators
    above now does that at the definition site instead (see
    docs/alphacube_steering_design.md, "丙 Migration"), so this function is
    left with only the one thing nothing else does for it.

    Called from a plugin's ``register()`` (see ``partura.ac_plugin``), before
    the registry is (re)built -- ``alphacube.plugins.load_plugins`` is what
    resets ``catalog._DEFAULT`` afterwards; this module does not reset it
    itself any more."""
    import alphacube.operators as ops
    from alphacube.operators.common import OPERATOR_REGISTRY
    for name in NEW_OPERATORS:
        meta = OPERATOR_REGISTRY[name]
        if meta["mode"] in ("dt", "shared"):
            ops.operator_dict_DT[name] = meta["fn"]
        if meta["mode"] in ("nd", "shared"):
            ops.operator_dict_ND[name] = meta["fn"]
