"""The reward's sorts on an accelerator.  Same numbers as ``partura.steer.reward`` -- that one stays the reference.

Why this exists: in a short search every candidate costs a panel (AlphaCube, on the GPU, about 5 s on the full
market) and then a reward.  The reference reward is numpy on the CPU and costs as much again -- 4 s for the level
rewards, 8-12 s for the bucket and the paired ones (six (half-life, direction) combinations, each with one or two
full-width sorts of a 1362 x 5220 panel).  Half of a search's wall clock was the yardstick, not the search.

What is moved: the per-(half-life, direction) work -- the bucket rank, the z-rank, the tie-block band, the decile
book and its daily net excess.  What is not: the EMA (numpy, sequential over days, cheap) and the two final
``books.book_row`` calls on the chosen signal, so the statistics that are RECORDED come from the same numpy code as
everywhere else in Partura.  Every sort is stable and every rank is integer arithmetic, so the chosen signal is
bit-identical to the reference's; the only floating-point difference is the order of summation inside a Sharpe or an
information ratio used to CHOOSE between combinations (about 1e-13 relative).

Switched on by ``PARTURA_REWARD_DEVICE`` (``cuda`` / ``cpu``); unset = the reference.  ``steer.reward`` falls back to
the reference if anything here raises: the fast path never decides the answer.  Locked by tests/test_steer_fast.py.
"""
from __future__ import annotations

from typing import Dict

import numpy as np

from . import books as bk
from .steer import PAIRED, PAIRED_FLOOR, REWARDS, _sized

SQRT252 = float(np.sqrt(252))


def _t(x, dev):
    import torch
    return torch.as_tensor(np.ascontiguousarray(x, dtype=np.float64), device=dev)


def _cached(ctx, name, dev, make):
    """Context tensors live on the context, one copy per device."""
    store = ctx.__dict__.setdefault("_fast", {})
    key = (name, str(dev))
    if key not in store:
        store[key] = make()
    return store[key]


def long_net(sm, tgt, cost: float = bk.COST, top: float = bk.TOP_FRAC):
    """Daily net excess of the pure long book of ``sm`` (rows = the days of one period; the book starts empty).
    ``alphacube.metrics.long_short_weights`` + ``books.long_book``, long leg only: equal weight on the top
    ``top`` of the finite names (ties at the boundary by symbol order -- a stable sort), minus the equal weight of
    the names with a signal and a label, minus ``cost`` per unit traded."""
    import torch
    D, S = sm.shape
    fin = torch.isfinite(sm)
    n = fin.sum(1)
    order = torch.argsort(torch.where(fin, sm, torch.full_like(sm, float("inf"))), dim=1, stable=True)   # non-finite last
    k = torch.clamp(torch.floor(n.to(torch.float64) * top).to(torch.int64), min=1)
    pos = torch.arange(S, device=sm.device)[None, :]
    long_ = (n >= 2)[:, None] & (pos >= (n - k)[:, None]) & (pos < n[:, None])
    w_sorted = torch.where(long_, (0.5 / k.to(torch.float64))[:, None].expand(D, S), torch.zeros((), dtype=torch.float64, device=sm.device))
    wl = torch.zeros((D, S), dtype=torch.float64, device=sm.device).scatter_(1, order, w_sorted) * 2.0
    ok = fin & torch.isfinite(tgt)
    r = torch.where(ok, tgt, torch.zeros_like(tgt))
    cnt = ok.sum(1)
    nan = torch.full((D,), float("nan"), dtype=torch.float64, device=sm.device)
    ew = torch.where(cnt > 0, r.sum(1) / cnt.clamp(min=1).to(torch.float64), nan)
    gross = torch.where(wl.sum(1) > 0, (wl * r).sum(1) - ew, nan)
    traded = (wl - torch.cat([torch.zeros((1, S), dtype=torch.float64, device=sm.device), wl[:-1]], 0)).abs().sum(1)
    return gross - cost * traded


def _ratio(d, min_n: int) -> float:
    """mean / std * sqrt(252) of the finite entries (population std, as numpy's default); NaN when it cannot be."""
    import torch
    f = d[torch.isfinite(d)]
    if f.numel() < min_n:
        return float("nan")
    sd = float(torch.sqrt(((f - f.mean()) ** 2).mean()))
    if not sd > 0:
        return float("nan")
    return float(f.mean()) / sd * SQRT252


def sharpe(net) -> float:          # books.stats: at least 3 finite days
    return _ratio(net, 3)


def ir(d) -> float:                # steer._ir: at least 30 finite days
    return _ratio(d, 30)


def ann(d) -> float:               # steer._ann: annualised mean of the finite days
    import torch
    f = d[torch.isfinite(d)]
    return float(f.mean()) * 252 if f.numel() else float("nan")


def bucket_rank(sm, bucket, n: int = 10):
    """``steer._bucket_rank``: rank inside each liquidity bucket, mapped to (0, 1]; ties inside a bucket by symbol
    order.  Two stable sorts (value, then bucket) are the lexicographic sort of the reference."""
    import torch
    D, S = sm.shape
    fin = torch.isfinite(sm) & (bucket >= 0)
    b = torch.where(fin, bucket, torch.full_like(bucket, n))
    o1 = torch.argsort(torch.where(fin, sm, torch.full_like(sm, float("inf"))), dim=1, stable=True)
    o2 = torch.argsort(torch.gather(b, 1, o1), dim=1, stable=True)
    order = torch.gather(o1, 1, o2)                                    # bucket first, value second, symbol third
    ar = torch.arange(S, device=sm.device)[None, :].expand(D, S)
    pos = torch.empty_like(order).scatter_(1, order, ar)
    cnt = torch.stack([(b == k).sum(1) for k in range(n + 1)], 1)
    start = torch.cumsum(cnt, 1) - cnt
    within = pos - torch.gather(start, 1, b)
    out = (within.to(torch.float64) + 1.0) / torch.gather(cnt, 1, b).clamp(min=1).to(torch.float64)
    return torch.where(fin, out, torch.full_like(out, float("nan")))


def zrank(x):
    """``diagnose._zrank``: per-row average ranks of the finite cells, mapped to [-0.5, 0.5]; NaN elsewhere."""
    import torch
    fin = torch.isfinite(x)
    s, order = torch.sort(torch.where(fin, x, torch.full_like(x, float("inf"))), dim=1, stable=True)
    s = s.contiguous()
    lo, hi = torch.searchsorted(s, s, right=False), torch.searchsorted(s, s, right=True)
    r = torch.empty_like(x).scatter_(1, order, (lo + hi + 1).to(torch.float64) / 2.0)
    n = fin.sum(1, keepdim=True).to(torch.float64)
    u = (r - 1.0) / torch.clamp(n - 1.0, min=1.0) - 0.5
    return torch.where(fin, u, torch.full_like(u, float("nan")))


def top_band(x, frac: float = 0.2):
    """``steer._top_band``: the names whose whole tie block lies in the top ``frac`` of the day's finite values."""
    import torch
    ok = torch.isfinite(x)
    v = torch.where(ok, x, torch.full_like(x, float("-inf")))
    s_, order = torch.sort(v, dim=-1, stable=True)
    s_ = s_.contiguous()
    first = torch.searchsorted(s_, s_, right=False)
    n = ok.sum(-1, keepdim=True)
    below = (first - (x.shape[-1] - n)).to(torch.float64) / n.clamp(min=1).to(torch.float64)
    return torch.zeros_like(ok).scatter_(-1, order, below >= (1.0 - frac) - 1e-12) & ok


def _spread(sm) -> float:
    """numpy's nanmedian(nanstd(sm, axis=1)): the median over days of the cross-sectional (population) std."""
    import torch
    fin = torch.isfinite(sm)
    n = fin.sum(1)
    x = torch.where(fin, sm, torch.zeros_like(sm))
    mean = x.sum(1) / n.clamp(min=1).to(torch.float64)
    var = (torch.where(fin, (sm - mean[:, None]) ** 2, torch.zeros_like(sm))).sum(1) / n.clamp(min=1).to(torch.float64)
    sd = torch.sqrt(var)[n > 0]
    if sd.numel() == 0:
        return float("nan")
    v = torch.sort(sd).values
    m = v.numel()
    return float((v[(m - 1) // 2] + v[m // 2]) / 2.0)


def reward_fast(panel, ctx, kind: str = "long", *, both_periods: bool = True, device: str = "cuda") -> Dict[str, object]:
    """``partura.steer.reward`` with the sorts on ``device``.  See that docstring for what is scored."""
    import torch

    if kind not in REWARDS:
        raise ValueError(f"unknown reward {kind!r}; choose from {REWARDS}")
    dev = torch.device(device)
    raw = np.asarray(panel, dtype=np.float64)
    use_mask = ctx.untradable is not None and kind in ("long_tradable", "long_bucket", "long_marginal")
    keep = ("long_ann", "long_sharpe", "long_turnover", "long_mdd")
    tr_, va_ = ctx.train, ctx.valid
    tgt = _cached(ctx, "tgt", dev, lambda: _t(ctx.tgt, dev))
    mask = _cached(ctx, "mask", dev, lambda: torch.as_tensor(np.ascontiguousarray(ctx.untradable, dtype=bool), device=dev)) if use_mask else None
    nan = torch.tensor(float("nan"), dtype=torch.float64, device=dev)
    best, extra = None, {}

    if kind not in PAIRED:
        bucket = _cached(ctx, "bucket", dev, lambda: torch.as_tensor(np.ascontiguousarray(ctx.bucket(), dtype=np.int64), device=dev)) if kind == "long_bucket" else None
        Q = _cached(ctx, "neutral_Q", dev, lambda: torch.as_tensor(ctx.neutral_Q, device=dev)) if kind == "long_neutral" else None
        for hl in ctx.halflives:
            sm0 = _t(bk.smoothed(raw, hl), dev)              # the EMA is linear: one pass serves both directions
            if mask is not None:
                sm0 = torch.where(mask, nan, sm0)
            if Q is not None:                                # C03: the residual on the style controls (steer.neutral_residual)
                z = zrank(sm0)
                fin = torch.isfinite(z) & (Q.abs().sum(2) > 0)
                y = torch.where(fin, z, torch.zeros_like(z)).to(torch.float32)
                r = y - torch.einsum("dsk,dk->ds", Q, torch.einsum("dsk,ds->dk", Q, y))
                rs = torch.sqrt((torch.where(fin, r, torch.zeros_like(r)) ** 2).sum(1) / fin.sum(1).clamp(min=1))
                fin = fin & (rs > 1e-4)[:, None]          # float32 here: a residual this small is the controls themselves
                sm0 = torch.where(fin, r.to(torch.float64), nan)
            for sign in (1.0, -1.0):
                sm = sign * sm0
                if bucket is not None:
                    sm = bucket_rank(sm, bucket)
                s = sharpe(long_net(sm[tr_], tgt[tr_]))
                key = -9e9 if s != s else s
                if best is None or key > best[0]:
                    best = (key, sign, float(hl), sm)
        _, sign, hl, sm = best
        sm = sm.cpu().numpy()
        tr, va = bk.book_row(sm, ctx.tgt, ctx.train), bk.book_row(sm, ctx.tgt, ctx.valid)
        s_tr, s_va = tr["long_sharpe"], va["long_sharpe"]
        score = min(s_tr, s_va) if both_periods else s_tr
    else:
        if kind == "long_marginal":
            pu = _cached(ctx, "pool_u", dev, lambda: _t(ctx.pool_in_universe(), dev))
            cells = torch.isfinite(_t(raw, dev)) & torch.isfinite(pu)
            if mask is not None:
                cells = cells & ~mask
            ref = torch.where(cells, pu, nan)                # the pool, on exactly the cells the blend can use
            ref_tr, ref_va = long_net(ref[tr_], tgt[tr_]), long_net(ref[va_], tgt[va_])
            ref_fin = None
        else:
            ref = _cached(ctx, "base", dev, lambda: _t(ctx.base, dev))
            ref_tr, ref_va = _cached(ctx, "base_rows", dev, lambda: (long_net(ref[tr_], tgt[tr_]), long_net(ref[va_], tgt[va_])))
            ref_fin = torch.isfinite(ref)
            n_ref = max(int(ref_fin[tr_].sum()), 1)
        for hl in ctx.halflives:
            sm0 = _t(bk.smoothed(raw, hl), dev)
            z0 = zrank(torch.where(cells, sm0, nan)) if kind == "long_marginal" else None
            for sign in (1.0, -1.0):
                if kind == "long_marginal":
                    sm = torch.where(cells, 0.5 * sign * z0 + 0.5 * pu, nan)     # rank(-x) = -rank(x): one ranking per half-life
                    share = float("nan")
                else:
                    band = top_band(torch.where(ref_fin, sign * sm0, nan))
                    sm = torch.where(ref_fin, torch.where(band, ref - 2.0, ref), nan)   # below every unscreened name, order kept
                    share = float(band[tr_].sum()) / n_ref
                if not _spread(sm[tr_]) > 1e-12:             # no cross-section, no book
                    continue
                d = long_net(sm[tr_], tgt[tr_]) - ref_tr
                r = _sized(ir(d), ann(d))                    # reliable AND worth something
                key = 0.0 if r != r else r                   # NaN = the book IS the reference book: worth exactly nothing
                if best is None or key > best[0]:
                    best = (key, sign, float(hl), sm, r, share)
        if best is None or best[4] != best[4]:               # the best this candidate can do is to change nothing
            nanrow = {k: float("nan") for k in keep}
            return {"score": float("-inf"), "sign": 1.0, "hl": float(ctx.halflives[0]), "kind": kind, "score_train": float("nan"),
                    "score_valid": float("nan"), "score_all": float("nan"), "no_effect": True, "train": nanrow, "valid": nanrow}
        _, sign, hl, sm, s_tr, share = best
        d_tr = long_net(sm[tr_], tgt[tr_]) - ref_tr
        d_va = long_net(sm[va_], tgt[va_]) - ref_va
        d_all = torch.cat([d_tr, d_va])
        size = {"ir_train": ir(d_tr), "ir_valid": ir(d_va), "ir_all": ir(d_all),
                "dann_train": ann(d_tr), "dann_valid": ann(d_va), "dann_all": ann(d_all)}
        s_va, s_all = _sized(size["ir_valid"], size["dann_valid"]), _sized(size["ir_all"], size["dann_all"])
        worst = min(s_tr, s_va) if (s_tr == s_tr and s_va == s_va) else float("nan")
        score = worst if not worst >= PAIRED_FLOOR else s_all            # NaN (a no-op) falls through to -inf below
        if not both_periods:
            score = s_tr
        sm = sm.cpu().numpy()
        tr, va = bk.book_row(sm, ctx.tgt, ctx.train), bk.book_row(sm, ctx.tgt, ctx.valid)
        extra = {"score_all": float(s_all), **size, **({"screened_share": share} if kind == "long_screen" else {})}
    return {"score": float(score) if score == score else float("-inf"), "sign": sign, "hl": hl, "kind": kind,
            "score_train": float(s_tr), "score_valid": float(s_va), **extra,
            "train": {k: tr[k] for k in keep}, "valid": {k: va[k] for k in keep}}


__all__ = ["reward_fast", "long_net", "sharpe", "ir", "bucket_rank", "zrank", "top_band"]
