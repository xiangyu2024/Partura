"""Diagnostics that turn a panel into evidence about a hypothesis.

AlphaCube already answers "how good is it" (IC, ICIR, turnover, net Sharpe).
Partura needs to answer "where does it come from", so this module adds the
discriminating measurements AlphaCube has no reason to own:

* ``neutralise``        -- daily cross-sectional residual after regressing the
  factor on control panels (size / price / volatility / reversal / momentum).
  If the alpha survives, the controls do not explain it; if it dies, they do.
* ``conditional_ic``    -- the IC of A inside quantile buckets of B.  This is
  what separates "B is a regime gate" from "B is a second, additive signal".
* ``decay``             -- IC across forward horizons: when the alpha starts,
  peaks and dies.
* ``by_year``           -- one row per calendar year, after cost.
* ``extreme_day_dependence`` -- net Sharpe after dropping the biggest P&L days.
* ``pair_rank_corr``    -- mean daily Spearman between two panels, i.e. whether
  a "variant" is actually a different factor or the same one rewritten.

Every metric that involves money is reported after cost.  The direction of a
factor is never re-chosen out of sample: ``metric_row`` takes the sign as an
argument so a sign fitted on train can be applied unchanged to valid/holdout.
"""

from __future__ import annotations

import warnings
from typing import Dict, List, Optional, Sequence, Tuple

from .bridge import ensure_alphacube_on_path

ensure_alphacube_on_path()

import numpy as np  # noqa: E402

import os  # noqa: E402

from alphacube.metrics import (apply_turnover_cap, cs_pearson, ema_rows, long_short_weights,  # noqa: E402
                               nanmean_quiet, portfolio_returns)
from alphacube.metrics import rank_rows as _rank_rows_pandas  # noqa: E402


def _rank_rows_torch(x: np.ndarray, device: str, rows: int = 512) -> np.ndarray:
    """``rank_rows`` on an accelerator: per-row average ranks (ties averaged) of
    the finite cells, NaN elsewhere -- the same answer as the pandas version
    (locked by tests/test_partura.py), without the CPU.  The server's CPU quota
    is usually taken by a neighbouring job while its GPU sits idle, and ranking
    a 1400 x 5200 panel is the single hottest call in a study."""
    import torch
    x = np.asarray(x, dtype=np.float64)
    out = np.empty(x.shape, dtype=np.float64)
    for a in range(0, x.shape[0], rows):
        t = torch.as_tensor(x[a:a + rows], device=device)
        fin = torch.isfinite(t)
        s, order = torch.sort(torch.where(fin, t, torch.full_like(t, float("inf"))), dim=1, stable=True)
        lo = torch.searchsorted(s, s, right=False)
        hi = torch.searchsorted(s, s, right=True)
        avg = (lo + hi + 1).to(torch.float64) / 2.0
        r = torch.empty_like(t).scatter_(1, order, avg)
        r[~fin] = float("nan")
        out[a:a + rows] = r.cpu().numpy()
    return out


def rank_rows(x: np.ndarray) -> np.ndarray:
    dev = os.environ.get("PARTURA_RANK_DEVICE", "")
    if dev:
        try:
            return _rank_rows_torch(x, dev)
        except Exception as exc:                         # never let the fast path decide the answer
            print(f"[diagnose] rank on {dev} failed ({type(exc).__name__}: {exc}); using pandas", flush=True)
    return _rank_rows_pandas(x)

COST_PER_SIDE = 0.0015          # 15 bp, AlphaCube's production assumption
TURNOVER_CAP = 0.30
TOP_FRAC = 0.10


# ---------------------------------------------------------------- basics
def ic_series(panel: np.ndarray, target: np.ndarray) -> np.ndarray:
    return cs_pearson(np.asarray(panel, dtype=np.float64), target)


def rank_ic_series(panel: np.ndarray, target: np.ndarray, *, panel_ranks: Optional[np.ndarray] = None,
                   target_ranks: Optional[np.ndarray] = None) -> np.ndarray:
    """``rank_rows`` is pandas' ``rank(axis=1)`` -- correct (ties averaged, inf
    skipped) but slow on a 1000 x 5000 panel, and this is the single hottest
    call in a run.  Pre-computed ranks may be passed in; a correlation is
    invariant to an affine map, so a flipped factor can reuse the unflipped
    ranks with a sign."""
    pr = rank_rows(np.asarray(panel, dtype=np.float64)) if panel_ranks is None else panel_ranks
    tr = rank_rows(target) if target_ranks is None else target_ranks
    return cs_pearson(pr, tr)


def _ir(x: np.ndarray) -> float:
    f = x[np.isfinite(x)]
    return float(f.mean() / f.std()) if f.size > 1 and f.std() > 0 else float("nan")


def _tstat(x: np.ndarray) -> float:
    f = x[np.isfinite(x)]
    return float(f.mean() / f.std() * np.sqrt(f.size)) if f.size > 1 and f.std() > 0 else float("nan")


def sign_from(panel: np.ndarray, target: np.ndarray, use: str = "rank_ic",
              target_ranks: Optional[np.ndarray] = None) -> float:
    s = (rank_ic_series(panel, target, target_ranks=target_ranks) if use == "rank_ic"
         else ic_series(panel, target))
    m = nanmean_quiet(s)
    return -1.0 if (np.isfinite(m) and m < 0) else 1.0


def ic_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
           target_ranks: Optional[np.ndarray] = None) -> Dict[str, float]:
    """Prediction metrics only (no book): what a stage needs for every variant
    when the money side is reported by ``partura.books``."""
    raw = np.asarray(panel, dtype=np.float64)
    p = sign * raw
    ic = ic_series(p, target)
    ric = rank_ic_series(p, target, panel_ranks=sign * rank_rows(raw), target_ranks=target_ranks)
    lab = np.isfinite(target)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return {
            "sign": float(sign),
            "ic": nanmean_quiet(ic), "icir": _ir(ic), "ic_t": _tstat(ic),
            "rank_ic": nanmean_quiet(ric), "rank_icir": _ir(ric), "rank_ic_t": _tstat(ric),
            "ic_pos": float((ic[np.isfinite(ic)] > 0).mean()) if np.isfinite(ic).any() else float("nan"),
            "coverage": float(np.isfinite(raw).mean()),
            # the gate the user's single-factor ranking applies: of the cells that HAVE a label
            "coverage_labelled": float((np.isfinite(raw) & lab).sum() / max(int(lab.sum()), 1)),
            "n_days": int(np.isfinite(ic).sum()),
        }


def distinct_fraction(panel: np.ndarray, step: int = 5, min_names: int = 30) -> float:
    """Median over sampled days of (distinct values / names with a value).  A
    factor with a handful of levels makes a decile book whose membership is
    decided by tie-breaking, i.e. by symbol order."""
    out = []
    for t in range(0, panel.shape[0], step):
        row = panel[t]
        row = row[np.isfinite(row)]
        if row.size >= min_names:
            out.append(np.unique(row).size / row.size)
    return float(np.median(out)) if out else 0.0


def metric_row(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
               cost: float = COST_PER_SIDE, cap: Optional[float] = TURNOVER_CAP,
               top_frac: float = TOP_FRAC, periods: int = 252,
               target_ranks: Optional[np.ndarray] = None) -> Dict[str, float]:
    """One uniform row of prediction + portfolio metrics, after cost."""
    p = sign * np.asarray(panel, dtype=np.float64)
    ic = ic_series(p, target)
    ric = rank_ic_series(p, target, panel_ranks=sign * rank_rows(np.asarray(panel, dtype=np.float64)),
                         target_ranks=target_ranks)
    w = long_short_weights(p, top_frac)
    net, gross, turn = portfolio_returns(w, target, cost)
    c_net, _, c_turn = portfolio_returns(apply_turnover_cap(w, cap), target, cost) if cap else (net, gross, turn)

    def curve(v: np.ndarray) -> Tuple[float, float]:
        f = v[np.isfinite(v)]
        if f.size < 2 or f.std() == 0:
            return float("nan"), float("nan")
        cum = np.cumprod(1.0 + f)
        dd = cum / np.maximum.accumulate(cum) - 1.0
        return float(f.mean() / f.std() * np.sqrt(periods)), float(dd.min())

    sh_g, _ = curve(gross)
    sh_n, dd_n = curve(net)
    sh_c, _ = curve(c_net)
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", RuntimeWarning)
        return {
            "sign": float(sign),
            "ic": nanmean_quiet(ic), "icir": _ir(ic), "ic_t": _tstat(ic),
            "rank_ic": nanmean_quiet(ric), "rank_icir": _ir(ric), "rank_ic_t": _tstat(ric),
            "ic_pos": float((ic[np.isfinite(ic)] > 0).mean()) if np.isfinite(ic).any() else float("nan"),
            "coverage": float(np.isfinite(panel).mean()),
            "n_days": int(np.isfinite(ic).sum()),
            "turnover": float(np.nanmean(turn)),
            "sharpe": sh_g, "sharpe_net": sh_n, "sharpe_capped": sh_c, "maxdd_net": dd_n,
            "ann_ret_net": float((1.0 + np.nanmean(net)) ** periods - 1.0),
            "fitness": abs(nanmean_quiet(ric)) - 0.14 * float(np.nanmean(turn)),   # AlphaCube's GP fitness
        }


# ---------------------------------------------------------------- neutralisation
def _zrank(x: np.ndarray) -> np.ndarray:
    r = rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(r).sum(axis=1, keepdims=True).astype(np.float64)
    u = (r - 1.0) / np.maximum(n - 1.0, 1.0) - 0.5        # uniform [-0.5, 0.5], NaN preserved
    return u


def neutralise(panel: np.ndarray, controls: Dict[str, np.ndarray], space: str = "rank",
               *, panel_ready: bool = False, controls_ready: bool = False
               ) -> Tuple[np.ndarray, Dict[str, float]]:
    """Daily cross-sectional OLS residual of the factor on the controls.

    ``panel_ready`` / ``controls_ready`` say the inputs are already in the
    regression space, so a caller that reuses the same controls across many
    factors pays for ranking them once instead of once per call (ranking a
    1000 x 5000 panel is the expensive part).

    ``space="rank"`` regresses the factor's within-day ranks on the controls'
    within-day ranks -- the right space when the headline metric is rank IC and
    the controls are heavy-tailed (Amt, price).  Returns the residual panel and
    the mean daily R^2 of the regression (how much of the factor the controls
    span).
    """
    y_raw = np.asarray(panel, dtype=np.float64)
    y = y_raw if panel_ready else (_zrank(y_raw) if space == "rank" else y_raw)
    xs = [(np.asarray(c, dtype=np.float64) if controls_ready
           else (_zrank(c) if space == "rank" else np.asarray(c, dtype=np.float64)))
          for c in controls.values()]
    out = np.full_like(y, np.nan)
    r2 = np.full(y.shape[0], np.nan)
    for t in range(y.shape[0]):
        m = np.isfinite(y[t])
        for x in xs:
            m &= np.isfinite(x[t])
        n = int(m.sum())
        if n < 50:
            continue
        X = np.column_stack([np.ones(n)] + [x[t][m] for x in xs])
        yv = y[t][m]
        beta, *_ = np.linalg.lstsq(X, yv, rcond=None)
        resid = yv - X @ beta
        ss = float(((yv - yv.mean()) ** 2).sum())
        rss = float((resid ** 2).sum())
        r2[t] = 1.0 - rss / ss if ss > 0 else np.nan
        if ss > 0 and rss / ss < 1e-10:
            # The controls span the factor exactly; what is left is float noise,
            # and ranking float noise invents a factor that is not there. Say
            # "nothing left" instead of handing back the rounding error.
            continue
        out[t, m] = resid
    return out, {"mean_r2": nanmean_quiet(r2), "days": int(np.isfinite(r2).sum())}


# ---------------------------------------------------------------- interaction
def conditional_ic(panel: np.ndarray, target: np.ndarray, gate: np.ndarray, buckets: int = 5,
                   ) -> List[Dict[str, float]]:
    """Rank IC of ``panel`` inside each within-day quantile bucket of ``gate``.

    A regime gate shows a monotone (or U-shaped) profile of |IC| across buckets;
    an additive second signal shows a flat one.
    """
    p = np.asarray(panel, dtype=np.float64)
    g = np.asarray(gate, dtype=np.float64)
    t = np.asarray(target, dtype=np.float64)
    rg = rank_rows(g)
    n = np.isfinite(rg).sum(axis=1, keepdims=True)
    with np.errstate(invalid="ignore"):
        b = np.floor((rg - 1.0) / np.maximum(n, 1) * buckets)
    rows = []
    for k in range(buckets):
        sel = (b == k)
        pk = np.where(sel, p, np.nan)
        ric = rank_ic_series(pk, np.where(sel, t, np.nan))
        icc = cs_pearson(np.where(sel, p, np.nan), np.where(sel, t, np.nan))
        rows.append({"bucket": k, "rank_ic": nanmean_quiet(ric), "rank_icir": _ir(ric),
                     "ic": nanmean_quiet(icc), "n_days": int(np.isfinite(ric).sum()),
                     "mean_names": float(np.nanmean(sel.sum(axis=1)))})
    return rows


# ---------------------------------------------------------------- time
def decay(panel: np.ndarray, targets: Dict[int, np.ndarray], sign: float = 1.0) -> List[Dict[str, float]]:
    p = sign * np.asarray(panel, dtype=np.float64)
    out = []
    for h in sorted(targets):
        out.append({"horizon": h, "ic": nanmean_quiet(ic_series(p, targets[h])),
                    "rank_ic": nanmean_quiet(rank_ic_series(p, targets[h]))})
    return out


def by_year(panel: np.ndarray, target: np.ndarray, years: np.ndarray, *, sign: float = 1.0,
            cost: float = COST_PER_SIDE, top_frac: float = TOP_FRAC,
            target_ranks: Optional[np.ndarray] = None) -> List[Dict[str, float]]:
    p = sign * np.asarray(panel, dtype=np.float64)
    w = long_short_weights(p, top_frac)
    net, gross, turn = portfolio_returns(w, target, cost)
    ric = rank_ic_series(p, target, target_ranks=target_ranks)
    rows = []
    for y in sorted(set(years.tolist())):
        m = years == y
        f = net[m][np.isfinite(net[m])]
        rows.append({"year": y, "days": int(m.sum()),
                     "rank_ic": nanmean_quiet(ric[m]),
                     "gross_pnl": float(np.nansum(gross[m])), "net_pnl": float(np.nansum(net[m])),
                     "sharpe_net": float(f.mean() / f.std() * np.sqrt(252)) if f.size > 1 and f.std() > 0 else float("nan"),
                     "turnover": float(np.nanmean(turn[m]))})
    return rows


def extreme_day_dependence(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
                           cost: float = COST_PER_SIDE, top_frac: float = TOP_FRAC,
                           fracs: Sequence[float] = (0.01, 0.05, 0.10)) -> List[Dict[str, float]]:
    """Net Sharpe after deleting the days with the largest |P&L| -- broad edge
    or a handful of events?"""
    p = sign * np.asarray(panel, dtype=np.float64)
    w = long_short_weights(p, top_frac)
    net, _, _ = portfolio_returns(w, target, cost)
    f = net[np.isfinite(net)]
    rows = []
    for fr in (0.0,) + tuple(fracs):
        k = int(np.floor(f.size * fr))
        keep = f if k == 0 else f[np.argsort(-np.abs(f))][k:]
        rows.append({"dropped_frac": fr, "dropped_days": k,
                     "sharpe_net": float(keep.mean() / keep.std() * np.sqrt(252)) if keep.size > 1 and keep.std() > 0 else float("nan"),
                     "net_pnl": float(keep.sum())})
    return rows


def smoothing_sweep(panel: np.ndarray, target: np.ndarray, *, sign: float = 1.0,
                    halflives: Sequence[float] = (1, 2, 3, 5, 10, 20),
                    cost: float = COST_PER_SIDE, cap: Optional[float] = TURNOVER_CAP,
                    top_frac: float = TOP_FRAC, target_ranks: Optional[np.ndarray] = None
                    ) -> List[Dict[str, float]]:
    """Trade a per-stock EMA of the factor instead of the factor itself.

    This is AlphaCube's own turnover remedy (``--smooth-halflives``, applied
    after combination); here it is applied to a single factor, because the
    question "is this thing tradable" is mostly a question about turnover.  The
    half-life must be chosen on train and then held fixed, so the sweep is
    reported in full rather than as its best row.
    """
    rows = [{"halflife": 0.0, **metric_row(panel, target, sign=sign, cost=cost, cap=cap,
                                           top_frac=top_frac, target_ranks=target_ranks)}]
    for h in halflives:
        sm = ema_rows(np.asarray(panel, dtype=np.float64), float(h))
        rows.append({"halflife": float(h), **metric_row(sm, target, sign=sign, cost=cost, cap=cap,
                                                        top_frac=top_frac, target_ranks=target_ranks)})
    return rows


# ---------------------------------------------------------------- similarity
def pair_rank_corr(a: np.ndarray, b: np.ndarray) -> float:
    """Mean daily Spearman correlation -- AlphaCube's own family-identity metric."""
    return nanmean_quiet(cs_pearson(rank_rows(np.asarray(a, dtype=np.float64)),
                                    rank_rows(np.asarray(b, dtype=np.float64))))


def rank_corr_matrix(panels: Dict[str, np.ndarray]) -> Dict[str, Dict[str, float]]:
    names = list(panels)
    ranks = {n: rank_rows(np.asarray(panels[n], dtype=np.float64)) for n in names}
    out: Dict[str, Dict[str, float]] = {}
    # `out[a] = {}` used to reset a row that earlier pairs had already written
    # into, so the lower triangle came back empty (and half the report's table
    # read NaN). Build every row first, then fill both triangles.
    out = {n: {} for n in names}
    for i, a in enumerate(names):
        for b in names[i:]:
            v = nanmean_quiet(cs_pearson(ranks[a], ranks[b]))
            out[a][b] = v
            out[b][a] = v
    return out


__all__ = ["COST_PER_SIDE", "TURNOVER_CAP", "TOP_FRAC", "ic_series", "rank_ic_series", "sign_from",
           "rank_rows", "ic_row", "distinct_fraction", "nanmean_quiet",
           "metric_row", "neutralise", "conditional_ic", "decay", "by_year", "smoothing_sweep",
           "extreme_day_dependence", "pair_rank_corr", "rank_corr_matrix"]
