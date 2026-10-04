"""The tradable-book metrics, in exactly the convention the user's tables use.

AlphaCube's current single-factor ranking (``scripts/pick_single_factors.py``)
judges a factor by two books built from a causally EMA-smoothed signal:

* a **decile long/short book** (gross 1), after 15 bp per unit turnover, and
* a **pure long book**: the long leg of that same decile book rescaled to
  weight 1, minus the equal-weight return of every stock that has both a
  signal and a label that day.  A holding whose label is missing (it opened
  locked at limit-up and could not have been bought) earns 0.

The half-life is chosen from {0, 1, 2, 3, 5, 10, 20} on the FIT period only,
by that book's own after-cost Sharpe, and then held fixed.

``stats`` and ``long_book`` are vendored from that script rather than imported
(the script lives in another session's working tree and changes under us); the
vendoring is guarded by a reproduction check against the user's published
table (``scripts/reproduce_table.py``), which is the only thing that makes a
Partura number comparable with one of theirs.

On top of that convention this module adds the two views a distillation needs:

* ``leg_anatomy`` -- how much of the spread is the long leg and how much is the
  short leg.  In A-shares the short leg cannot be traded, and a book whose
  spread is 80% short leg is a different object from one that is 80% long leg
  even when the two Sharpe ratios agree.
* ``quantile_profile`` -- mean next-day excess by signal quantile.  A decile
  book assumes "more signal is better"; the profile says whether that is true.
"""

from __future__ import annotations

from typing import Dict, List, Optional, Sequence

from .bridge import ensure_alphacube_on_path

ensure_alphacube_on_path()

import numpy as np  # noqa: E402

from alphacube.metrics import ema_rows, long_short_weights, portfolio_returns  # noqa: E402

HALFLIVES = (0.0, 1, 2, 3, 5, 10, 20)
TOP_FRAC = 0.10
COST = 0.0015


def stats(net: np.ndarray) -> Dict[str, float]:
    f = net[np.isfinite(net)]
    if f.size < 3 or f.std() == 0:
        return {"sharpe": float("nan"), "ann": float("nan"), "mdd": float("nan")}
    eq = np.cumsum(f)
    return {"sharpe": float(f.mean() / f.std() * np.sqrt(252)),
            "ann": float(f.mean() * 252),
            "mdd": float((eq - np.maximum.accumulate(eq)).min())}


def long_book(w: np.ndarray, sig: np.ndarray, target: np.ndarray, cost: float = COST):
    """(net excess, gross excess, one-sided turnover) of the long leg as a pure long book."""
    wl = np.clip(w, 0.0, None) * 2.0
    ok = np.isfinite(sig) & np.isfinite(target)
    r = np.where(ok, target, 0.0)
    n = ok.sum(1)
    ew = np.where(n > 0, r.sum(1) / np.maximum(n, 1), np.nan)
    gross = np.where(wl.sum(1) > 0, (wl * r).sum(1) - ew, np.nan)
    traded = np.abs(np.diff(wl, axis=0, prepend=np.zeros((1, wl.shape[1])))).sum(1)
    return gross - cost * traded, gross, 0.5 * traded


def short_leg_excess(w: np.ndarray, sig: np.ndarray, target: np.ndarray) -> np.ndarray:
    """Gross daily excess EARNED by being short the bottom decile: equal-weight
    universe minus the short basket (positive = the shorts underperformed)."""
    ws = np.clip(-w, 0.0, None) * 2.0
    ok = np.isfinite(sig) & np.isfinite(target)
    r = np.where(ok, target, 0.0)
    n = ok.sum(1)
    ew = np.where(n > 0, r.sum(1) / np.maximum(n, 1), np.nan)
    return np.where(ws.sum(1) > 0, ew - (ws * r).sum(1), np.nan)


def smoothed(sig: np.ndarray, halflife: float) -> np.ndarray:
    return ema_rows(sig, halflife) if halflife else np.asarray(sig, dtype=np.float64)


def fit_halflives(sig: np.ndarray, target: np.ndarray, fit: slice, cost: float = COST,
                  top_frac: float = TOP_FRAC, halflives: Sequence[float] = HALFLIVES) -> Dict[str, object]:
    """Choose the L/S and the long-book half-life on ``fit`` only (first maximum wins)."""
    best: Dict[str, tuple] = {}
    sweep: List[dict] = []
    for hl in halflives:
        sm = smoothed(sig, hl)[fit]
        w = long_short_weights(sm, top_frac)
        ls_net, _, ls_turn = portfolio_returns(w, target[fit], cost)
        ls = stats(ls_net)
        net, gross, turn = long_book(w, sm, target[fit], cost)
        lo = stats(net)
        sweep.append({"halflife": float(hl), "ls_sharpe": ls["sharpe"], "ls_turnover": float(np.nanmean(ls_turn)),
                      "long_sharpe": lo["sharpe"], "long_ann": lo["ann"], "long_turnover": float(np.nanmean(turn))})
        for name, s in (("ls", ls["sharpe"]), ("long", lo["sharpe"])):
            key = float(np.nan_to_num(s, nan=-9e9))
            if name not in best or key > best[name][0]:
                best[name] = (key, float(hl))
    return {"hl_ls": best["ls"][1], "hl_long": best["long"][1], "sweep": sweep}


def book_row(sm: np.ndarray, target: np.ndarray, days: slice, cost: float = COST,
             top_frac: float = TOP_FRAC) -> Dict[str, float]:
    """Both books on ``days`` (each started from an empty book), from one smoothed signal."""
    s, t = sm[days], target[days]
    w = long_short_weights(s, top_frac)
    ls_net, ls_gross, ls_turn = portfolio_returns(w, t, cost)
    net, gross, turn = long_book(w, s, t, cost)
    short = short_leg_excess(w, s, t)
    lo, ls = stats(net), stats(ls_net)
    lg, sg = stats(gross), stats(short)
    tot = (lg["ann"] or 0.0) + (sg["ann"] or 0.0)
    return {
        "ls_sharpe": ls["sharpe"], "ls_ann": ls["ann"], "ls_mdd": ls["mdd"],
        "ls_gross_sharpe": stats(ls_gross)["sharpe"], "ls_turnover": float(np.nanmean(ls_turn)),
        "long_sharpe": lo["sharpe"], "long_ann": lo["ann"], "long_mdd": lo["mdd"],
        "long_gross_ann": lg["ann"], "long_turnover": float(np.nanmean(turn)),
        "short_gross_ann": sg["ann"],
        # share of the gross decile spread that comes from the leg one can actually hold
        "long_share": float(lg["ann"] / tot) if tot and np.isfinite(tot) and tot != 0 else float("nan"),
        "n_days": int(np.isfinite(ls_net).sum()),
    }


def books(sig: np.ndarray, target: np.ndarray, fit: slice, evals: Dict[str, slice], *,
          cost: float = COST, top_frac: float = TOP_FRAC, rank_by: str = "long") -> Dict[str, object]:
    """``sig`` is already sign-aligned.  Two half-lives are fitted on ``fit``:

    * ``long`` -- by the pure long book's after-cost excess Sharpe.  This is the
      selection convention (and the default of the user's own
      ``pick_single_factors --rank long``): in A-shares only the long leg can be
      held, so the half-life that matters is the one that is best FOR that book.
      A longer half-life that turns a 5% net long-leg excess into 8% is a real,
      tradable improvement, not an artefact to be controlled away.
    * ``ls`` -- by the decile long/short book's after-cost Sharpe; the convention
      of the table the user first published, kept so every number stays
      comparable with it.

    Every split in ``evals`` is scored under BOTH (``by_rank``); ``splits`` /
    ``hl_used`` are the view named by ``rank_by``.
    """
    fitd = fit_halflives(sig, target, fit, cost, top_frac)
    views: Dict[str, dict] = {}
    for name, hl in (("ls", fitd["hl_ls"]), ("long", fitd["hl_long"])):
        if name == "long" and hl == fitd["hl_ls"]:
            views[name] = {"hl": hl, "splits": views["ls"]["splits"]}
            continue
        sm = smoothed(sig, hl)
        views[name] = {"hl": hl, "splits": {k: book_row(sm, target, d, cost, top_frac) for k, d in evals.items()}}
    out = {"hl_ls": fitd["hl_ls"], "hl_long": fitd["hl_long"], "hl_used": views[rank_by]["hl"],
           "rank_by": rank_by, "sweep": fitd["sweep"], "splits": views[rank_by]["splits"], "by_rank": views}
    return out


def views_of(b: Dict[str, object]) -> Dict[str, dict]:
    """{"ls": {hl, splits}, "long": {hl, splits}} for a ``books`` result of ANY vintage.
    Runs from before ``by_rank`` scored at the L/S half-life and kept the long
    view under ``splits_at_hl_long`` only when the two half-lives differed."""
    if "by_rank" in b:
        return b["by_rank"]
    return {"ls": {"hl": b["hl_ls"], "splits": b["splits"]},
            "long": {"hl": b["hl_long"], "splits": b.get("splits_at_hl_long") or b["splits"]}}


def quantile_profile(sm: np.ndarray, target: np.ndarray, days: slice, n: int = 10) -> List[Dict[str, float]]:
    """Mean next-day EXCESS return (vs the equal-weight universe of scored names)
    of each signal quantile, annualised, plus how often it is positive."""
    s = np.asarray(sm[days], dtype=np.float64)
    t = np.asarray(target[days], dtype=np.float64)
    ok = np.isfinite(s) & np.isfinite(t)
    order = np.argsort(np.where(ok, s, np.inf), axis=1, kind="stable")
    cnt = ok.sum(1)
    pos = np.empty_like(order)
    np.put_along_axis(pos, order, np.arange(s.shape[1])[None, :].repeat(s.shape[0], 0), axis=1)
    with np.errstate(invalid="ignore", divide="ignore"):
        q = np.floor(pos / np.maximum(cnt, 1)[:, None] * n)
    q = np.where(ok, q, np.nan)
    r = np.where(ok, t, 0.0)
    ew = np.where(cnt > 0, r.sum(1) / np.maximum(cnt, 1), np.nan)
    rows = []
    for k in range(n):
        sel = (q == k)
        m = sel.sum(1)
        with np.errstate(invalid="ignore", divide="ignore"):
            ex = np.where(m > 0, (r * sel).sum(1) / np.maximum(m, 1) - ew, np.nan)
        f = ex[np.isfinite(ex)]
        rows.append({"quantile": k + 1, "excess_ann": float(f.mean() * 252) if f.size else float("nan"),
                     "sharpe": float(f.mean() / f.std() * np.sqrt(252)) if f.size > 2 and f.std() > 0 else float("nan"),
                     "win": float((f > 0).mean()) if f.size else float("nan")})
    return rows


__all__ = ["HALFLIVES", "TOP_FRAC", "COST", "stats", "long_book", "short_leg_excess", "smoothed",
           "fit_halflives", "book_row", "books", "views_of", "quantile_profile"]
