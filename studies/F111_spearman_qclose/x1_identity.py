"""R1 exec script -- the identity + conditioning + known-family + tie analysis.

See notes/F111_spearman_qclose/orders/R1.md for the full spec (blocks a/b/c/d + (c4))
and notes/F111_spearman_qclose/04_grammar.md for the identity being tested: on a window
with no missing data, the cross-sectional ORDER of ts_spearman(day_quantile(Close), 10)
equals the order of

    proj[t, i] = sum_k rc_i[t, k] * M[t, k]

where rc_i is stock i's own window-centred rank path (ranks[t,:,i] - mean_k ranks[t,:,i],
via the SAME double stable-argsort the ts_spearman kernel uses) and M[t, .] is the
cross-sectional mean of that path on day t.

Holdout discipline: every custom computation below is restricted to the `utrain` date
range (train+valid) BEFORE it is used -- this script never computes, prints, or hands to
st.books/st.ic anything derived from a holdout-dated row.  Quantities that must go
through st.books/st.ic (which index a FULL-length array by named split) are embedded back
into a full-length, NaN-outside-utrain array (`_pad`) right before that call; the NaN
region is never populated from real data, so nothing holdout-derived ever reaches those
rows even transiently.  bk.smoothed() in block (c4) runs causally over the full timeline
(the same pattern Study.signal() itself uses) but is only ever READ back through
st.rank_corr(..., "train"), so no holdout value is read either.

`--mock` runs the whole script against a tiny synthetic FakeStudy (random panels, no
server/data needed) to catch shape/key bugs before spending a real server run; this is
IN ADDITION to the self_check() the order requires, which always runs first (against
random arrays) regardless of --mock.

Run via: ./scripts/study.sh exec F111_spearman_qclose x1_identity x1_identity.py
"""
from __future__ import annotations

import sys
import traceback

MOCK = "--mock" in sys.argv[1:]

from partura.study_tools import Study, bk, dg  # noqa: E402  (caps BLAS threads before numpy loads)

import numpy as np  # noqa: E402

D = 10                      # window length, fixed by the expression
CHUNK = 200                  # time-chunk size for the windowed-rank pass (memory)
HL_LIST = list(bk.HALFLIVES)  # (0.0, 1, 2, 3, 5, 10, 20)
SIGN = 1.0                   # S0's fitted sign (published sign=+1); per R1 order, not re-fit here
KNOWN_NAMES = ["known_stdamt_mean30", "known_stdamt_max9", "known_amt_max9"]
FID = "F111_spearman_qclose"


def _p(*a):
    print(*a, flush=True)


def _stats_line(name, arr):
    f = np.asarray(arr, dtype=np.float64).ravel()
    f = f[np.isfinite(f)]
    if f.size == 0:
        _p(f"  {name}: no finite values")
        return
    _p(f"  {name}: n={f.size} mean={f.mean():+.4f} median={np.median(f):+.4f} "
       f"p05={np.percentile(f, 5):+.4f} p95={np.percentile(f, 95):+.4f}")


# --------------------------------------------------------------------- core rank-path machinery
def _rc_from_windows(windows: np.ndarray):
    """windows: (nt, d, N). Replays the ts_spearman kernel's own steps exactly:
    NaN -> +inf, stable argsort twice (ranks 0..d-1), NaN restored, then centred on the
    window's own mean rank. Returns (rc, mask, order1); order1 is reused for tie detection."""
    mask = np.isfinite(windows)
    x_filled = np.where(mask, windows, np.inf)
    order1 = np.argsort(x_filled, axis=1, kind="stable")
    ranks = np.argsort(order1, axis=1, kind="stable").astype(np.float64)
    ranks = np.where(mask, ranks, np.nan)
    with np.errstate(invalid="ignore"):
        rc = ranks - np.nanmean(ranks, axis=1, keepdims=True)
    return rc, mask, order1


def windowed_rank_quantities(a: np.ndarray, d: int = D, chunk: int = CHUNK) -> dict:
    """Aligned to row t+d-1 (first d-1 rows NaN/False). a: (T, N).  Returns:
      proj            -- sum_k rc_i[k]*M[k], NaN-robust (a missing day contributes 0 to the
                          sum); defined whenever the window has >=1 valid day for stock i
      proj_complete   -- same, but NaN wherever the window is NOT fully populated for i
      complete        -- bool, window fully populated (all d days present) for stock i
      rho_time        -- own rank-vs-time correlation (pure 10-day rank momentum)
      tie             -- bool, the window's FINITE values contain an exact duplicate pair
      c               -- (T,) market path's trend-direction scalar, one per day
    """
    T, N = a.shape
    proj = np.full((T, N), np.nan)
    proj_complete = np.full((T, N), np.nan)
    complete = np.zeros((T, N), dtype=bool)
    rho_time = np.full((T, N), np.nan)
    tie = np.zeros((T, N), dtype=bool)
    c = np.full(T, np.nan)
    ramp = np.arange(d, dtype=np.float64) - (d - 1) / 2.0
    ramp_ss = float(np.sum(ramp ** 2))

    n_starts = T - d + 1
    for start in range(0, max(n_starts, 0), chunk):
        end = min(start + chunk, n_starts)
        windows = np.stack([a[start + k:end + k] for k in range(d)], axis=1)   # (nt, d, N)
        rc, mask, order1 = _rc_from_windows(windows)
        rc0 = np.nan_to_num(rc, nan=0.0)
        with np.errstate(invalid="ignore"):
            M = np.nanmean(rc, axis=2)                     # (nt, d): cross-sectional mean path
        M0 = np.nan_to_num(M, nan=0.0)

        any_valid = mask.any(axis=1)                        # (nt, N)
        win_complete = mask.all(axis=1)                      # (nt, N)

        proj_chunk = np.einsum("jkn,jk->jn", rc0, M0)
        proj_chunk = np.where(any_valid, proj_chunk, np.nan)

        num = np.einsum("jkn,k->jn", rc0, ramp)
        den = np.sqrt(np.einsum("jkn,jkn->jn", rc0, rc0) * ramp_ss) + 1e-8
        rho_chunk = np.where(any_valid, num / den, np.nan)

        cnum = np.einsum("jk,k->j", M0, ramp)
        cden = np.sqrt(np.einsum("jk,jk->j", M0, M0) * ramp_ss) + 1e-8
        c_chunk = cnum / cden

        # ties: sort the ORIGINAL values (order1 pushes NaN, filled to +inf for sorting, to the
        # end) and flag any exact-equal ADJACENT pair among entries finite on both sides -- equal
        # values necessarily land adjacent to each other after a sort, so this is exhaustive.
        sorted_vals = np.take_along_axis(windows, order1, axis=1)
        sorted_mask = np.take_along_axis(mask, order1, axis=1)
        diffs = sorted_vals[:, 1:, :] - sorted_vals[:, :-1, :]
        valid_pair = sorted_mask[:, 1:, :] & sorted_mask[:, :-1, :]
        tie_chunk = np.any((diffs == 0) & valid_pair, axis=1)

        rows = slice(start + d - 1, end + d - 1)
        proj[rows] = proj_chunk
        proj_complete[rows] = np.where(win_complete, proj_chunk, np.nan)
        complete[rows] = win_complete
        rho_time[rows] = rho_chunk
        tie[rows] = tie_chunk
        c[rows] = c_chunk

    return {"proj": proj, "proj_complete": proj_complete, "complete": complete,
            "rho_time": rho_time, "tie": tie, "c": c}


def _ordinal_rank(v: np.ndarray) -> np.ndarray:
    order = np.argsort(v, kind="stable")
    return np.argsort(order, kind="stable").astype(np.float64)


def _brute_mean_pairwise_spearman(window_t: np.ndarray) -> np.ndarray:
    """window_t: (d, N), one day's window for all stocks. Returns (N,) mean_{j!=i} pairwise
    ordinal Spearman correlation (pairwise-complete on the overlap) by nested loop -- the
    obviously-correct reference, only ever called on tiny synthetic self-check data."""
    d, N = window_t.shape
    corr = np.full((N, N), np.nan)
    for i in range(N):
        xi = window_t[:, i]
        for j in range(N):
            if j == i:
                continue
            xj = window_t[:, j]
            m = np.isfinite(xi) & np.isfinite(xj)
            if m.sum() < 2:
                continue
            xr, yr = _ordinal_rank(xi[m]), _ordinal_rank(xj[m])
            if xr.std() == 0 or yr.std() == 0:
                continue
            corr[i, j] = np.corrcoef(xr, yr)[0, 1]
    with np.errstate(invalid="ignore"):
        return np.nanmean(corr, axis=1)


def _daily_spearman(x: np.ndarray, y: np.ndarray):
    """Per-row cross-sectional Spearman between two (T,N) panels -> (T,) array (or a scalar
    for two 1-D vectors)."""
    x = np.asarray(x, dtype=np.float64)
    y = np.asarray(y, dtype=np.float64)
    if x.ndim == 1:
        m = np.isfinite(x) & np.isfinite(y)
        if m.sum() < 2 or x[m].std() == 0 or y[m].std() == 0:
            return float("nan")
        return float(np.corrcoef(_ordinal_rank(x[m]), _ordinal_rank(y[m]))[0, 1])
    return dg.cs_pearson(dg.rank_rows(x), dg.rank_rows(y))


def _pct_rank(panel: np.ndarray) -> np.ndarray:
    """Within-day percentile rank in (0,1), NaN preserved -- same convention as the project's
    other studies (e.g. studies/F107_abs_demean_skew_low/x1_anatomy.py:pct_rank)."""
    r = dg.rank_rows(np.asarray(panel, dtype=np.float64))
    n = np.isfinite(r).sum(axis=1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def _print_book(label, b, extra=""):
    L, S = b["by_rank"]["long"], b["by_rank"]["ls"]
    t, v = L["splits"]["train"], L["splits"]["valid"]
    st_, sv_ = S["splits"]["train"], S["splits"]["valid"]
    _p(f"  [{label}] hlL={L['hl']:g} Lnet {t['long_ann']*100:+.2f}%/{v['long_ann']*100:+.2f}%  "
       f"Lshp {t['long_sharpe']:+.2f}/{v['long_sharpe']:+.2f}  "
       f"Lgross {t['long_gross_ann']*100:+.2f}%/{v['long_gross_ann']*100:+.2f}%  "
       f"LTO {t['long_turnover']*100:.2f}%/{v['long_turnover']*100:.2f}%  |  "
       f"hlS={S['hl']:g} LS {st_['ls_sharpe']:+.2f}/{sv_['ls_sharpe']:+.2f}  "
       f"short {st_['short_gross_ann']*100:+.2f}%/{sv_['short_gross_ann']*100:+.2f}%" + extra)


# --------------------------------------------------------------------------------- self-check
def self_check():
    """Required by the order, before touching real data: (i) the complete-window rank
    variance is exactly (d^2-1)/12; (ii) a brute double loop over stock pairs agrees with
    `proj` (this is what directly checks the identity derivation); then the same check with
    10% of cells set to NaN (expected to degrade -- that is H1's boundary)."""
    _p("=" * 78); _p("SELF-CHECK (synthetic random data; no real panel touched)"); _p("=" * 78)
    try:
        rng = np.random.default_rng(0)
        Tn, Nn, d = 30, 20, D
        a = rng.uniform(1.0, 100.0, size=(Tn, Nn))

        windows = np.stack([a[k:Tn - d + 1 + k] for k in range(d)], axis=1)
        rc, mask, _ = _rc_from_windows(windows)
        rc_var = np.nanmean(rc ** 2, axis=1)
        expect = (d ** 2 - 1) / 12.0
        ok_i = bool(np.all(mask) and abs(rc_var.min() - expect) < 1e-5 and abs(rc_var.max() - expect) < 1e-5)
        _p(f"(i) expect rank_var == {expect} exactly (complete window); got min={rc_var.min():.8f} "
           f"max={rc_var.max():.8f}  -> {'PASS' if ok_i else 'FAIL'}")

        res = windowed_rank_quantities(a, d=d, chunk=200)
        proj = res["proj"]
        day_corrs = []
        for t in range(d - 1, Tn):
            Bt = _brute_mean_pairwise_spearman(windows[t - d + 1])
            pt = proj[t]
            m = np.isfinite(Bt) & np.isfinite(pt)
            if m.sum() >= 2 and Bt[m].std() > 0 and pt[m].std() > 0:
                day_corrs.append(np.corrcoef(_ordinal_rank(Bt[m]), _ordinal_rank(pt[m]))[0, 1])
        day_corrs = np.array(day_corrs)
        mean_dc = float(np.nanmean(day_corrs)) if day_corrs.size else float("nan")
        ok_ii = mean_dc > 1 - 1e-3
        _p(f"(ii) no-NaN: brute-force-mean-pairwise-spearman vs proj, daily rank-corr "
           f"mean={mean_dc:.6f} min={np.nanmin(day_corrs):.6f} over {day_corrs.size} days "
           f"(tol 1e-3 around 1.0) -> {'PASS' if ok_ii else 'FAIL -- recheck the derivation'}")
        if not ok_ii:
            _p(f"    RAW brute B[last day]: {Bt}")
            _p(f"    RAW proj [last day]: {pt}")

        a2 = a.copy()
        rng2 = np.random.default_rng(1)
        a2[rng2.random(a2.shape) < 0.10] = np.nan
        windows2 = np.stack([a2[k:Tn - d + 1 + k] for k in range(d)], axis=1)
        res2 = windowed_rank_quantities(a2, d=d, chunk=200)
        proj2 = res2["proj"]
        day_corrs2 = []
        for t in range(d - 1, Tn):
            Bt2 = _brute_mean_pairwise_spearman(windows2[t - d + 1])
            pt2 = proj2[t]
            m = np.isfinite(Bt2) & np.isfinite(pt2)
            if m.sum() >= 2 and Bt2[m].std() > 0 and pt2[m].std() > 0:
                day_corrs2.append(np.corrcoef(_ordinal_rank(Bt2[m]), _ordinal_rank(pt2[m]))[0, 1])
        day_corrs2 = np.array(day_corrs2)
        mean_dc2 = float(np.nanmean(day_corrs2)) if day_corrs2.size else float("nan")
        _p(f"(ii, 10% NaN) same comparison with 10% of cells knocked out: mean={mean_dc2:.6f} "
           f"min={np.nanmin(day_corrs2):.6f} over {day_corrs2.size} days "
           f"(expected to drop vs the no-NaN case -- this is H1's boundary, not a pass/fail)")
    except Exception:
        _p("!! self-check raised -- printing a warning and continuing to the real analysis:")
        traceback.print_exc()
    _p("")


# --------------------------------------------------------------------------------- mock harness
class FakeStudy:
    """--mock only: random panels through the REAL bk/dg code (pure numpy/pandas, no server),
    so this script's control flow, dict keys and shapes are exercised before a real run."""

    def __init__(self):
        self.cfg = {"cost_per_side": bk.COST, "top_frac": bk.TOP_FRAC}
        self.rng = np.random.default_rng(0)
        self.Tn, self.Nn = 260, 120
        self._sl = {"train": slice(0, 150), "valid": slice(150, 220), "utrain": slice(0, 220)}
        base = 10 + np.cumsum(self.rng.normal(0, 0.1, (self.Tn, self.Nn)), axis=0)
        base = np.round(base, 2)
        base[self.rng.random(base.shape) < 0.02] = np.nan
        self._a = base
        amt = np.abs(self.rng.normal(0, 1, (self.Tn, self.Nn)))
        self._cache = {"a": self._a}
        self._known = {k: amt * (1 + 0.1 * i) + self.rng.normal(0, 0.3, (self.Tn, self.Nn))
                        for i, k in enumerate(KNOWN_NAMES)}
        t = self.rng.normal(0, 0.02, (self.Tn, self.Nn))
        t[self.rng.random(t.shape) < 0.03] = np.nan
        self._t = t

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return None

    def panels(self, exprs):
        out = {}
        for k, e in exprs.items():
            if "day_quantile(Close)" in e and "ts_spearman" not in e and "ts_pearson" not in e and "ts_rank" not in e:
                out[k] = self._a
            elif e.strip() == "ts_spearman(day_quantile(Close), 10)":
                # crude mock of the real kernel, just enough shape/NaN behaviour to exercise block (c)/(d)
                out[k] = np.tanh(windowed_rank_quantities(self._a)["proj"] / 50.0)
            else:
                g = np.random.default_rng(abs(hash(e)) % (2 ** 32))
                out[k] = g.normal(0, 1, (self.Tn, self.Nn))
        return out

    def control(self, name):
        return self._known.get(name, self.rng.normal(0, 1, (self.Tn, self.Nn)))

    def target(self, horizon=1, buyable=None):
        return self._t

    def slice(self, split):
        if split in ("holdout", "full"):
            raise PermissionError("mock: holdout/full not available")
        return self._sl[split]

    def sign(self, panel, split="train"):
        s = self._sl[split]
        return dg.sign_from(np.asarray(panel, dtype=np.float64)[s], self.target()[s])

    def ic(self, panel, split="train", sign=None):
        s = self._sl[split]
        sg = self.sign(panel) if sign is None else sign
        return dg.ic_row(np.asarray(panel, dtype=np.float64)[s], self.target()[s], sign=sg)

    def signal(self, panel, fit="train", sign=None, halflife=None):
        p = np.asarray(panel, dtype=np.float64)
        sg = self.sign(p, fit) if sign is None else sign
        if halflife is None:
            halflife = bk.fit_halflives(sg * p, self.target(), self.slice(fit))["hl_long"]
        return bk.smoothed(sg * p, halflife)

    def books(self, panel, fit="train", evals=("train", "valid"), sign=None):
        sg = self.sign(panel, fit) if sign is None else sign
        return bk.books(sg * np.asarray(panel, dtype=np.float64), self.target(), self.slice(fit),
                        {e: self.slice(e) for e in evals}, cost=self.cfg["cost_per_side"],
                        top_frac=self.cfg["top_frac"], rank_by="long")

    def rank_corr(self, a, b, split="train"):
        s = self.slice(split)
        return dg.pair_rank_corr(np.asarray(a)[s], np.asarray(b)[s])


# --------------------------------------------------------------------------------- main
def main():
    self_check()

    _p("=" * 78); _p(f"LOADING PANELS ({'MOCK' if MOCK else 'real server data'})"); _p("=" * 78)
    ctx = FakeStudy() if MOCK else Study(FID)
    with ctx as st:
        a = st.panels({"a": "day_quantile(Close)"})["a"]
        f = st.panels({"f": "ts_spearman(day_quantile(Close), 10)"})["f"]
        target = st.target()
        sig = st.signal(f)
        _p(f"a.shape={a.shape} f.shape={f.shape} target.shape={target.shape}")

        tr_sl, va_sl, ut_sl = st.slice("train"), st.slice("valid"), st.slice("utrain")
        _p(f"train={tr_sl} valid={va_sl} utrain={ut_sl}")

        lookback = D - 1
        a_ext = a[max(ut_sl.start - lookback, 0):ut_sl.stop]
        res = windowed_rank_quantities(a_ext, d=D, chunk=CHUNK)
        used_lookback = ut_sl.start - max(ut_sl.start - lookback, 0)
        proj_u = res["proj"][used_lookback:]
        proj_complete_u = res["proj_complete"][used_lookback:]
        complete_u = res["complete"][used_lookback:]
        rho_time_u = res["rho_time"][used_lookback:]
        tie_u = res["tie"][used_lookback:]
        c_u = res["c"][used_lookback:]
        _p(f"windowed pass: {a_ext.shape[0]} rows in ({used_lookback} lookback + "
           f"{ut_sl.stop - ut_sl.start} utrain), chunk={CHUNK} -> utrain-aligned outputs "
           f"shape {proj_u.shape}")

        f_u = f[ut_sl]
        target_u = target[ut_sl]
        n_u = ut_sl.stop - ut_sl.start
        local_train = slice(tr_sl.start - ut_sl.start, tr_sl.stop - ut_sl.start)
        local_valid = slice(va_sl.start - ut_sl.start, va_sl.stop - ut_sl.start)
        _p(f"local_train={local_train} local_valid={local_valid} of n_u={n_u} "
           f"(sanity: should tile start=0 with no gap/overlap)")

        def _pad(local_arr):
            out = np.full_like(np.asarray(f, dtype=np.float64), np.nan)
            out[ut_sl] = local_arr
            return out

        # ============================================================== block (a) -- H1
        _p(""); _p("=" * 78); _p("BLOCK (a) -- H1: does the identity hold on real data"); _p("=" * 78)
        try:
            lab_u = np.isfinite(target_u)
            frac_complete = float(complete_u[lab_u].mean()) if lab_u.any() else float("nan")
            frac_complete_tr = float(complete_u[local_train][lab_u[local_train]].mean())
            frac_complete_va = float(complete_u[local_valid][lab_u[local_valid]].mean())
            _p(f"window-complete fraction of labelled cells: utrain={frac_complete:.4f} "
               f"train={frac_complete_tr:.4f} valid={frac_complete_va:.4f}")

            d_all = _daily_spearman(proj_u, f_u)
            _stats_line("proj vs f, ALL cells (daily spearman, utrain)", d_all)
            d_complete = _daily_spearman(proj_complete_u, f_u)
            _stats_line("proj vs f, WINDOW-COMPLETE cells only (daily spearman, utrain)", d_complete)

            proj_full = _pad(proj_u)
            rc_sig = st.rank_corr(sig, st.signal(proj_full), "train")
            _p(f"st.rank_corr(sig, st.signal(proj)), train = {rc_sig:+.4f}")

            sg_p = st.sign(proj_full, "train")
            b_p = st.books(proj_full, fit="train", evals=("train", "valid"), sign=sg_p)
            _p(f"sign(proj, train)={sg_p:+.0f}")
            _print_book("proj", b_p)
        except Exception:
            traceback.print_exc()

        # ============================================================== block (b) -- H2 vs H11
        _p(""); _p("=" * 78); _p("BLOCK (b) -- H2 vs H11: market-direction conditioning"); _p("=" * 78)
        try:
            c_fin = c_u[np.isfinite(c_u)]
            _p(f"c(t) distribution (utrain): mean={c_fin.mean():+.4f} "
               f"frac_c_gt0={(c_fin > 0).mean():.4f} median|c|={np.median(np.abs(c_fin)):.4f} n={c_fin.size}")

            daily_f_rho = _daily_spearman(f_u, rho_time_u)
            pos, neg = (c_u > 0), (c_u < 0)
            _stats_line("f vs rho_time, ALL days", daily_f_rho)
            _p(f"  f vs rho_time, c>0 days: mean={np.nanmean(daily_f_rho[pos]):+.4f} (n_days={int(pos.sum())})")
            _p(f"  f vs rho_time, c<0 days: mean={np.nanmean(daily_f_rho[neg]):+.4f} (n_days={int(neg.sum())})")

            c_rho_u = c_u[:, None] * rho_time_u
            daily_f_crho = _daily_spearman(f_u, c_rho_u)
            _stats_line("f vs c*rho_time, ALL days", daily_f_crho)

            rho_full, crho_full = _pad(rho_time_u), _pad(c_rho_u)
            sg_r = st.sign(rho_full, "train")
            b_r = st.books(rho_full, fit="train", evals=("train", "valid"), sign=sg_r)
            _p(f"sign(rho_time, train)={sg_r:+.0f}")
            _print_book("rho_time", b_r)

            sg_cr = st.sign(crho_full, "train")
            b_cr = st.books(crho_full, fit="train", evals=("train", "valid"), sign=sg_cr)
            _p(f"sign(c*rho_time, train)={sg_cr:+.0f}")
            _print_book("c*rho_time", b_cr)
        except Exception:
            traceback.print_exc()

        # ============================================================== block (c) -- H4
        _p(""); _p("=" * 78); _p("BLOCK (c) -- H4: increment over known families (most important)"); _p("=" * 78)
        for name in KNOWN_NAMES:
            _p(""); _p(f"--- known family: {name} ---")
            try:
                known = st.control(name)
                known_u = known[ut_sl]

                # 1. residual, MAIN/tradable convention: raw f vs raw known, rank-space daily OLS,
                #    residual handed to the full st.books pipeline (own sign + half-life fit).
                resid1_u, info1 = dg.neutralise(f_u, {"known": known_u}, space="rank")
                resid1_full = _pad(resid1_u)
                sg1 = st.sign(resid1_full, "train")
                b1 = st.books(resid1_full, fit="train", evals=("train", "valid"), sign=sg1)
                ic1_tr = st.ic(resid1_full, "train")
                ic1_va = st.ic(resid1_full, "valid")
                _p(f"  [1 tradable residual] rank-space R2(mean daily, utrain)={info1['mean_r2']:.4f} "
                   f"days={info1['days']} sign={sg1:+.0f}")
                _print_book("resid#1 tradable", b1)
                _p(f"    rank_ic: train={ic1_tr['rank_ic']:+.4f} valid={ic1_va['rank_ic']:+.4f}")

                # 2. residual, S0-SS7-COMPARABLE convention: on the already-smoothed traded `sig`,
                #    residual NOT re-smoothed, applied independently to the train slice and the
                #    valid slice (matches partura/runner.py's own neutralise diagnostic exactly).
                for split_name, loc in (("train", local_train), ("valid", local_valid)):
                    sig_seg = sig[ut_sl][loc]
                    known_seg = known_u[loc]
                    y_z = dg._zrank(sig_seg)
                    k_z = dg._zrank(known_seg)
                    resid2, info2 = dg.neutralise(y_z, {"known": k_z}, panel_ready=True, controls_ready=True)
                    tgt_seg = target_u[loc]
                    icr2 = dg.ic_row(resid2, tgt_seg, sign=1.0)
                    br2 = bk.book_row(resid2, tgt_seg, slice(0, resid2.shape[0]),
                                       cost=float(st.cfg.get("cost_per_side", bk.COST)),
                                       top_frac=float(st.cfg.get("top_frac", bk.TOP_FRAC)))
                    _p(f"  [2 S0-Sec7-comparable residual, {split_name}] R2={info2['mean_r2']:.4f} "
                       f"rank_ic={icr2['rank_ic']:+.4f} Lnet={br2['long_ann']*100:+.2f}% "
                       f"Lgross={br2['long_gross_ann']*100:+.2f}% Lshp={br2['long_sharpe']:+.2f} "
                       f"LTO={br2['long_turnover']*100:.2f}% LS={br2['ls_sharpe']:+.2f} "
                       f"short={br2['short_gross_ann']*100:+.2f}%")

                # 3. combination: each side oriented by its OWN train rank-IC sign, converted to
                #    its own within-day percentile rank, then w*f + (1-w)*known.
                sign_f = st.sign(f, "train")
                sign_k = st.sign(known, "train")
                pr_f = _pct_rank(sign_f * f_u)
                pr_k = _pct_rank(sign_k * known_u)
                for w in (0.0, 0.25, 0.5, 0.75, 1.0):
                    combo_u = w * pr_f + (1.0 - w) * pr_k
                    combo_full = _pad(combo_u)
                    sg3 = st.sign(combo_full, "train")
                    b3 = st.books(combo_full, fit="train", evals=("train", "valid"), sign=sg3)
                    _print_book(f"combo w={w:g}", b3, extra=f"  sign={sg3:+.0f}")
            except Exception:
                traceback.print_exc()

        # ============================================================== block (c4) -- H11
        _p(""); _p("=" * 78); _p("BLOCK (c4) -- H11: |rank_corr(f, known)| vs half-life (train)"); _p("=" * 78)
        try:
            known_panels = {name: st.control(name) for name in KNOWN_NAMES}
            header = f"{'hl':<6}" + "".join(f"{n:>24}" for n in KNOWN_NAMES)
            _p(header)
            for hl in HL_LIST:
                f_sm_full = bk.smoothed(SIGN * f, hl)
                row = f"{hl!s:<6}"
                for name in KNOWN_NAMES:
                    k_sm_full = bk.smoothed(known_panels[name], hl)
                    rc_ = st.rank_corr(f_sm_full, k_sm_full, "train")
                    row += f"{rc_:>+24.4f}"
                _p(row)
            _p("(H11 predicts |value| rising monotonically down this table; sign of each cell is incidental)")
        except Exception:
            traceback.print_exc()

        # ============================================================== block (d) -- H3
        _p(""); _p("=" * 78); _p("BLOCK (d) -- H3: tied values"); _p("=" * 78)
        try:
            lab_u = np.isfinite(target_u)
            tie_all = float(tie_u[lab_u].mean()) if lab_u.any() else float("nan")
            tie_tr = float(tie_u[local_train][lab_u[local_train]].mean())
            tie_va = float(tie_u[local_valid][lab_u[local_valid]].mean())
            _p(f"tie fraction of labelled cells: utrain={tie_all:.4f} train={tie_tr:.4f} valid={tie_va:.4f}")

            pct_f = _pct_rank(SIGN * f_u)          # (0,1); near 1 = long end (Q10)
            decile = np.clip(np.floor(pct_f * 10), 0, 9)
            rates = []
            for k in range(10):
                sel = (decile == k) & lab_u
                rates.append(float(tie_u[sel].mean()) if sel.any() else float("nan"))
            _p("tie rate by f-decile (Q1=short end .. Q10=long end):")
            _p("  " + "  ".join(f"Q{k+1}={rates[k]:.4f}" for k in range(10)))

            pct_tie = pct_f[tie_u & lab_u]
            pct_notie = pct_f[(~tie_u) & lab_u]
            _p(f"mean f-percentile: tie=True {np.nanmean(pct_tie):.4f} (n={pct_tie.size})   "
               f"tie=False {np.nanmean(pct_notie):.4f} (n={pct_notie.size})")

            f_detied_u = np.where(tie_u, np.nan, f_u)
            f_detied_full = _pad(f_detied_u)
            sg_d = st.sign(f_detied_full, "train")
            b_d = st.books(f_detied_full, fit="train", evals=("train", "valid"), sign=sg_d)
            cov_tr = st.ic(f_detied_full, "train")["coverage_labelled"]
            cov_va = st.ic(f_detied_full, "valid")["coverage_labelled"]
            _p(f"sign(de-tied f, train)={sg_d:+.0f}  coverage_labelled: train={cov_tr:.4f} valid={cov_va:.4f}")
            _print_book("de-tied f", b_d)
        except Exception:
            traceback.print_exc()

    _p(""); _p("DONE.")


if __name__ == "__main__":
    main()
