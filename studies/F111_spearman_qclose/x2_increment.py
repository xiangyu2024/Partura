"""R2 exec script (修订 R2-a) -- block A/B/C/D/E: does F1/F2 give a long-only user
who already holds a known amt/std-amt family any net increment, and if so, how.

See notes/F111_spearman_qclose/orders/R2.md (section "修订 R2-a") for the full spec.
F1/F2 are fixed by the order:
    F1 = "ts_spearman(day_last(Close), 10)"   (= S1's l_last = S2's a_last_10, rank-corr 1.0000 to both)
    F2 = BESTW, selected by the mechanical rule in 修订 R2-a 改动 2: among
         {w_last_5, w_last_20, w_last_30, w_q_30, p_last_30} the one with the highest
         train Lnet at its own selected hlL (ties -> longer window). From the S2_window
         digest (runs/F111_spearman_qclose/S2_window.json):
             w_last_5   hlL=20 Lnet_tr=+8.1%
             w_last_20  hlL=20 Lnet_tr=+10.9%
             w_last_30  hlL=10 Lnet_tr=+11.1%
             w_q_30     hlL=20 Lnet_tr=+10.4%
             p_last_30  hlL=3  Lnet_tr=+11.6%   <- highest -> BESTW
         so F2 = "ts_pearson(day_last(Close), 30)".

Holdout discipline, copied from studies/F111_spearman_qclose/x1_identity.py: every
custom (non st.books/st.ic/st.sign) computation below -- percentile ranks, the
dual-sort pool mask, the neutralise residual -- is restricted to the `utrain` slice
BEFORE it is computed, then embedded back into a full-length, NaN-outside-utrain
array (`_pad`) right before it is handed to st.sign/st.books/st.ic. Block D's EMA
smoothing is the one exception, by the same precedent x1 uses in its block (c4):
bk.smoothed() runs causally over the FULL timeline (exactly what Study.signal() does
internally) and is only ever read back on the train slice, so no holdout-dated input
is ever read even though later rows of the underlying array exist in memory.

sign_f / sign_k / pct_rank follow x1_identity.py's block (c) (copied, not reinvented),
so this script's w=0 / w=1 edges are directly comparable to results/R1.md 数字 14.

Memory: panels kept resident are cast to float32 and `del`-ed once a block is done
with them (no new expensive kernel evaluation happens here -- F1, F2, the three known
families, v_base and the four controls are all already cached from S0/S1/S2/R1, so
this script should be cheap; w_last_50's exit 97 was a GPU-kernel issue, not a
Python-side residency issue, but the discipline is followed anyway per the order).

Run via: ./scripts/study.sh exec F111_spearman_qclose x2_increment x2_increment.py
Local dry run (no server, no data): python3 studies/F111_spearman_qclose/x2_increment.py --mock
"""
from __future__ import annotations

import sys
import traceback

MOCK = "--mock" in sys.argv[1:]

from partura.study_tools import Study, bk, dg  # noqa: E402  (caps BLAS threads before numpy loads)

import numpy as np  # noqa: E402
from alphacube.metrics import long_short_weights  # noqa: E402

FID = "F111_spearman_qclose"
F1_EXPR = "ts_spearman(day_last(Close), 10)"
F2_EXPR = "ts_pearson(day_last(Close), 30)"      # BESTW, see module docstring
KNOWN_NAMES = ["known_stdamt_mean30", "known_stdamt_max9", "known_amt_max9"]
W_GRID = (0.0, 0.15, 0.25, 0.35, 1.0)

# w=0 reference row per family, copied verbatim from results/R1.md 数字 14 (the combo
# table) -- w=0 drops f entirely, so this row cannot depend on which f R2 uses and
# must reproduce R1's numbers bit-for-bit. Values: (hlL, Lnet_tr, Lnet_va, Lshp_tr,
# Lshp_va, Lgross_tr, Lgross_va, LTO_tr, LTO_va, hlS, LS_tr, LS_va, short_tr, short_va).
R1_W0_REF = {
    "known_stdamt_mean30": (0, 0.1326, 0.2218, 1.86, 3.44, 0.1575, 0.2430, 0.0326, 0.0280, 0, 1.91, 3.62, 0.2133, 0.3277),
    "known_stdamt_max9":   (5, 0.1337, 0.2182, 1.95, 3.51, 0.1687, 0.2487, 0.0458, 0.0403, 0, 2.54, 4.38, 0.3835, 0.4760),
    "known_amt_max9":      (5, 0.1056, 0.2172, 1.45, 3.37, 0.1350, 0.2434, 0.0386, 0.0347, 0, 1.62, 3.69, 0.2449, 0.3834),
}


def _p(*a):
    print(*a, flush=True)


def _pct_rank(panel: np.ndarray) -> np.ndarray:
    """Within-day percentile rank in (0,1), NaN preserved -- copied from
    studies/F111_spearman_qclose/x1_identity.py (block (c)'s convention)."""
    r = dg.rank_rows(np.asarray(panel, dtype=np.float64))
    n = np.isfinite(r).sum(axis=1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def _book_line(label, b, extra=""):
    L, S = b["by_rank"]["long"], b["by_rank"]["ls"]
    t, v = L["splits"]["train"], L["splits"]["valid"]
    st_, sv_ = S["splits"]["train"], S["splits"]["valid"]
    _p(f"  [{label}] hlL={L['hl']:g} Lnet {t['long_ann']*100:+.2f}%/{v['long_ann']*100:+.2f}%  "
       f"Lshp {t['long_sharpe']:+.2f}/{v['long_sharpe']:+.2f}  "
       f"Lgross {t['long_gross_ann']*100:+.2f}%/{v['long_gross_ann']*100:+.2f}%  "
       f"LTO {t['long_turnover']*100:.2f}%/{v['long_turnover']*100:.2f}%  |  "
       f"hlS={S['hl']:g} LS {st_['ls_sharpe']:+.2f}/{sv_['ls_sharpe']:+.2f}  "
       f"short {st_['short_gross_ann']*100:+.2f}%/{sv_['short_gross_ann']*100:+.2f}%" + extra)


def _book_vals(b):
    """Flat tuple in the same order/units as R1_W0_REF, for a numeric self-check diff."""
    L, S = b["by_rank"]["long"], b["by_rank"]["ls"]
    t, v = L["splits"]["train"], L["splits"]["valid"]
    st_, sv_ = S["splits"]["train"], S["splits"]["valid"]
    return (L["hl"], t["long_ann"], v["long_ann"], t["long_sharpe"], v["long_sharpe"],
            t["long_gross_ann"], v["long_gross_ann"], t["long_turnover"], v["long_turnover"],
            S["hl"], st_["ls_sharpe"], sv_["ls_sharpe"], st_["short_gross_ann"], sv_["short_gross_ann"])


# --------------------------------------------------------------- synthetic self-check
def self_check():
    """Required by R2's "写脚本的硬要求" #1: on synthetic random panels (no server),
    verify the block-A combo collapses exactly at its two edges: w=0 must equal a
    book built from `known` alone and w=1 must equal a book built from `f` alone.

    Done at hl=0 (bk.book_row, no half-life sweep), which is the provable exact
    invariant: pct_rank is a strictly monotonic per-day transform (ties get the
    same averaged rank dg.rank_rows already uses), so at hl=0 -- no cross-day
    mixing yet -- it cannot change which names a stable argsort puts in the
    top/bottom top_frac, hence cannot change the book. That invariant does NOT
    survive a half-life sweep (st.books): R1 already found pct_rank+smoothing
    shifts the swept numbers by a few pp (results/R1.md "值得注意"#6), so this
    check does not go through st.books/fit_halflives at all.

    This also exercises the one edge-case a naive `w*pr_f + (1-w)*pr_k` has: at
    w=0 or w=1 the zero-weighted side's own NaNs still propagate (0*NaN=NaN in
    IEEE float), silently shrinking coverage by the OTHER panel's missingness.
    Both the check below and the real block-A loop bypass the arithmetic at the
    two edges (assign the surviving side directly) to avoid that."""
    _p("=" * 78); _p("SELF-CHECK (synthetic random data; no real panel touched)"); _p("=" * 78)
    try:
        rng = np.random.default_rng(42)
        T, N = 120, 40
        train = slice(0, 80)
        target_syn = rng.normal(0, 0.02, (T, N))
        target_syn[rng.random((T, N)) < 0.03] = np.nan
        f_syn = rng.normal(0, 1, (T, N))
        k_syn = rng.normal(0, 1, (T, N))
        f_syn[rng.random((T, N)) < 0.08] = np.nan   # deliberately NOT the same mask as k_syn,
        k_syn[rng.random((T, N)) < 0.08] = np.nan   # so a 0*NaN leak would show up as a coverage drop

        sign_f = dg.sign_from(f_syn[train], target_syn[train])
        sign_k = dg.sign_from(k_syn[train], target_syn[train])
        pr_f = _pct_rank(sign_f * f_syn)
        pr_k = _pct_rank(sign_k * k_syn)

        cases = [("w=0 (edge-safe) vs book_row(known), hl=0", pr_k, sign_k * k_syn),
                 ("w=1 (edge-safe) vs book_row(f), hl=0", pr_f, sign_f * f_syn)]
        keys = ["long_ann", "long_sharpe", "ls_sharpe", "long_turnover", "short_gross_ann", "n_days"]
        all_ok = True
        for label, combo, ref in cases:
            b_combo = bk.book_row(combo, target_syn, train, cost=bk.COST, top_frac=bk.TOP_FRAC)
            b_ref = bk.book_row(ref, target_syn, train, cost=bk.COST, top_frac=bk.TOP_FRAC)
            diffs = [abs(b_combo[k] - b_ref[k]) for k in keys]
            ok = max(diffs) < 1e-9
            all_ok &= ok
            _p(f"  {label}: " + "  ".join(f"{k}={b_combo[k]:+.6f}(ref {b_ref[k]:+.6f})" for k in keys)
               + f"  -> {'PASS' if ok else 'FAIL'}")
        _p(f"self-check overall: {'PASS' if all_ok else 'FAIL -- STOP, formula wiring is wrong'}")
    except Exception:
        _p("!! self-check raised -- printing a warning and continuing to the real analysis:")
        traceback.print_exc()
    _p("")


# ---------------------------------------------------------------------------- mock harness
class FakeStudy:
    """--mock only: a local dry run of main()'s control flow (dict keys, shapes, NaN
    handling) against random panels, so the one real `exec` this order is budgeted
    for is not spent finding a KeyError. Values are not meaningful."""

    def __init__(self):
        self.cfg = {"cost_per_side": bk.COST, "top_frac": bk.TOP_FRAC}
        self.rng = np.random.default_rng(0)
        self.Tn, self.Nn = 260, 120
        self._sl = {"train": slice(0, 150), "valid": slice(150, 220), "utrain": slice(0, 220)}
        amt = np.abs(self.rng.normal(0, 1, (self.Tn, self.Nn)))
        self._known = {}
        for i, k in enumerate(KNOWN_NAMES):
            arr = amt * (1 + 0.1 * i) + self.rng.normal(0, 0.3, (self.Tn, self.Nn))
            arr[self.rng.random(arr.shape) < 0.04] = np.nan   # own, non-aligned NaN mask per family,
            self._known[k] = arr                              # to exercise the w=0/1 edge-case check
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
            g = np.random.default_rng(abs(hash(e)) % (2 ** 32))
            arr = g.normal(0, 1, (self.Tn, self.Nn))
            arr[g.random(arr.shape) < 0.04] = np.nan
            out[k] = arr
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
        f_panels = st.panels({"f1": F1_EXPR, "f2": F2_EXPR})
        F = {"F1": f_panels["f1"].astype(np.float32), "F2": f_panels["f2"].astype(np.float32)}
        del f_panels
        known_panels = {name: st.control(name).astype(np.float32) for name in KNOWN_NAMES}
        target = st.target()
        _p(f"F1.shape={F['F1'].shape} F2.shape={F['F2'].shape} target.shape={target.shape}")

        tr_sl, va_sl, ut_sl = st.slice("train"), st.slice("valid"), st.slice("utrain")
        _p(f"train={tr_sl} valid={va_sl} utrain={ut_sl}")

        def _pad(local_arr, template=F["F1"]):
            out = np.full_like(np.asarray(template, dtype=np.float64), np.nan)
            out[ut_sl] = local_arr
            return out

        sign_f = {name: st.sign(F[name], "train") for name in F}
        sign_k = {name: st.sign(known_panels[name], "train") for name in KNOWN_NAMES}
        _p(f"sign(F1,train)={sign_f['F1']:+.0f}  sign(F2,train)={sign_f['F2']:+.0f}  "
           + "  ".join(f"sign({n},train)={sign_k[n]:+.0f}" for n in KNOWN_NAMES))

        # ============================================================== block A -- combo book
        _p(""); _p("=" * 78)
        _p("BLOCK A -- combo book: w*pct_rank(sign_f*f) + (1-w)*pct_rank(sign_k*known)")
        _p("=" * 78)
        w1_rows = {}     # fname -> {known_name: _book_vals}
        w0_rows = {}     # known_name -> _book_vals (should not depend on fname)
        try:
            pr_f_u = {name: _pct_rank(sign_f[name] * F[name][ut_sl]) for name in F}
            pr_k_u = {name: _pct_rank(sign_k[name] * known_panels[name][ut_sl]) for name in KNOWN_NAMES}
            for fname in ("F1", "F2"):
                w1_rows[fname] = {}
                for kname in KNOWN_NAMES:
                    _p(f"--- f={fname} known={kname} ---")
                    for w in W_GRID:
                        # bypass the weighted-sum arithmetic exactly at the two edges: with
                        # it, 0*NaN=NaN would let the ZERO-weighted side's own missingness
                        # leak into the book even at w=0/1 (see self_check()'s docstring).
                        if w == 0.0:
                            combo_u = pr_k_u[kname]
                        elif w == 1.0:
                            combo_u = pr_f_u[fname]
                        else:
                            combo_u = w * pr_f_u[fname] + (1.0 - w) * pr_k_u[kname]
                        combo_full = _pad(combo_u)
                        sg3 = st.sign(combo_full, "train")
                        b3 = st.books(combo_full, fit="train", evals=("train", "valid"), sign=sg3)
                        _book_line(f"w={w:g}", b3, extra=f"  sign={sg3:+.0f}")
                        if w == 1.0:
                            w1_rows[fname][kname] = _book_vals(b3)
                        if w == 0.0:
                            w0_rows[kname] = _book_vals(b3)
                        del combo_u, combo_full
            _p("")
            _p("-- self-check 1: w=1 row identical across the 3 known families, per f --")
            for fname in ("F1", "F2"):
                rows = [w1_rows[fname][k] for k in KNOWN_NAMES]
                ok = all(all(np.isclose(a, b, equal_nan=True, atol=1e-9) for a, b in zip(rows[0], r))
                         for r in rows[1:])
                _p(f"  {fname}: w=1 across {KNOWN_NAMES} identical -> {'PASS' if ok else 'FAIL'}  "
                   f"(Lnet_tr per family: {[f'{r[1]*100:+.2f}%' for r in rows]})")
            _p("-- self-check 2: w=0 row vs results/R1.md 数字 14 (must not depend on f, bit-for-bit) --")
            for kname in KNOWN_NAMES:
                got, ref = w0_rows[kname], R1_W0_REF[kname]
                diffs = [abs(a - b) for a, b in zip(got, ref)]
                ok = max(diffs) < 5e-4
                _p(f"  {kname}: got={tuple(round(x, 4) for x in got)}")
                _p(f"            ref={ref}")
                _p(f"            max abs diff={max(diffs):.6f} -> {'PASS' if ok else 'FAIL/DIFFERS'}")
        except Exception:
            traceback.print_exc()

        # ============================================================== block B -- dual sort
        _p(""); _p("=" * 78)
        _p("BLOCK B -- dual sort: f inside the top-width%% pool of sign_k*known (NaN outside)")
        _p("=" * 78)
        try:
            top_frac_cfg = float(st.cfg.get("top_frac", bk.TOP_FRAC)) if hasattr(st, "cfg") else bk.TOP_FRAC
            combos = [
                ("F1", "known_stdamt_mean30", 0.30),
                ("F1", "known_stdamt_mean30", 0.10),
                ("F1", "known_stdamt_max9", 0.30),
                ("F1", "known_stdamt_max9", 0.10),
                ("F2", "known_stdamt_mean30", 0.30),
            ]
            for fname, kname, width in combos:
                _p(f"--- f={fname} known={kname} width={width:.0%} ---")
                pr_k_pool_u = _pct_rank(sign_k[kname] * known_panels[kname][ut_sl])
                pool_mask_u = pr_k_pool_u >= (1.0 - width)     # NaN compares False -> pool excludes NaN known cells
                f_u = F[fname][ut_sl]
                f_masked_u = np.where(pool_mask_u, f_u, np.nan)
                f_masked_full = _pad(f_masked_u)
                sg = st.sign(f_masked_full, "train")
                b = st.books(f_masked_full, fit="train", evals=("train", "valid"), sign=sg)
                _book_line(f"{fname}|pool({kname},{width:.0%})", b, extra=f"  sign={sg:+.0f}")
                hlL = b["by_rank"]["long"]["hl"]
                cov_tr = st.ic(f_masked_full, "train")["coverage_labelled"]
                cov_va = st.ic(f_masked_full, "valid")["coverage_labelled"]
                sm_full = bk.smoothed(sg * f_masked_full, hlL)
                w_pos = long_short_weights(sm_full, top_frac_cfg) > 0
                n_tr = np.median(w_pos[tr_sl].sum(axis=1))
                n_va = np.median(w_pos[va_sl].sum(axis=1))
                _p(f"    coverage_labelled: train={cov_tr:.4f} valid={cov_va:.4f}  "
                   f"long-leg names/day median: train={n_tr:g} valid={n_va:g}")
                prof_tr = bk.quantile_profile(sm_full, target, tr_sl, n=10)
                prof_va = bk.quantile_profile(sm_full, target, va_sl, n=10)
                _p("    profile train Q1..Q10: " + " ".join(f"{r['excess_ann']*100:+.1f}%" for r in prof_tr))
                _p("    profile valid Q1..Q10: " + " ".join(f"{r['excess_ann']*100:+.1f}%" for r in prof_va))
                del pr_k_pool_u, pool_mask_u, f_masked_u, f_masked_full, sm_full, w_pos
        except Exception:
            traceback.print_exc()

        # ============================================================== block C -- residual
        _p(""); _p("=" * 78)
        _p("BLOCK C -- residual (f - beta*known, R1's 主口径① only): dg.neutralise(space='rank')")
        _p("=" * 78)
        try:
            for fname in ("F1", "F2"):
                f_u = F[fname][ut_sl]
                for kname in KNOWN_NAMES:
                    known_u = known_panels[kname][ut_sl]
                    resid_u, info = dg.neutralise(f_u, {"known": known_u}, space="rank")
                    resid_full = _pad(resid_u)
                    sg = st.sign(resid_full, "train")
                    b = st.books(resid_full, fit="train", evals=("train", "valid"), sign=sg)
                    ic_tr = st.ic(resid_full, "train")["rank_ic"]
                    ic_va = st.ic(resid_full, "valid")["rank_ic"]
                    _p(f"--- f={fname} known={kname} rank-space R2(utrain mean daily)={info['mean_r2']:.4f} "
                       f"days={info['days']} sign={sg:+.0f} ---")
                    _p(f"    rank_ic: train={ic_tr:+.4f} valid={ic_va:+.4f}")
                    _book_line("resid", b)
                    del resid_u, resid_full
        except Exception:
            traceback.print_exc()

        # ============================================================== block D -- what it likes
        _p(""); _p("=" * 78)
        _p("BLOCK D -- what F1's long end is made of (numpy only, no st.books); train only")
        _p("=" * 78)
        try:
            sig0_full = sign_f["F1"] * np.asarray(F["F1"], dtype=np.float64)       # hl=0, raw signed
            sig20_full = bk.smoothed(sign_f["F1"] * np.asarray(F["F1"], dtype=np.float64), 20)  # hl=20

            r = dg.rank_rows(sig20_full)
            n = np.isfinite(r).sum(axis=1, keepdims=True)
            with np.errstate(invalid="ignore"):
                q_full = np.clip(np.floor((r - 1.0) / np.maximum(n, 1) * 10), 0, 9)
            q_tr = q_full[tr_sl]

            _p("(d1) mean within-day percentile of each control, by F1-decile (train; Q1=short..Q10=long):")
            ctl_names = ["ctl_amt", "ctl_cap", "ctl_ivol", "ctl_dvol20", "known_stdamt_mean30"]
            for cname in ctl_names:
                ctl_full = (known_panels[cname] if cname in known_panels else st.control(cname))
                pct_ctl_tr = _pct_rank(np.asarray(ctl_full, dtype=np.float64))[tr_sl]
                row = []
                for k in range(10):
                    sel = (q_tr == k)
                    vals = pct_ctl_tr[sel]
                    vals = vals[np.isfinite(vals)]
                    row.append(float(vals.mean()) if vals.size else float("nan"))
                _p(f"  {cname:<20}" + " ".join(f"{v:.3f}" for v in row))
                if cname not in known_panels:
                    del ctl_full, pct_ctl_tr

            _p("(d2) mean F1 value by its own decile (train): raw (hl=0) vs smoothed (hl=20):")
            sig0_tr, sig20_tr = sig0_full[tr_sl], sig20_full[tr_sl]
            row0, row20 = [], []
            for k in range(10):
                sel = (q_tr == k)
                v0, v20 = sig0_tr[sel], sig20_tr[sel]
                v0, v20 = v0[np.isfinite(v0)], v20[np.isfinite(v20)]
                row0.append(float(v0.mean()) if v0.size else float("nan"))
                row20.append(float(v20.mean()) if v20.size else float("nan"))
            _p("  hl0 : " + " ".join(f"{v:+.4f}" for v in row0))
            _p("  hl20: " + " ".join(f"{v:+.4f}" for v in row20))
            _p("(d3) BESTW(=F2) 的 rank 相关(交易信号口径,train): 直接引用 S2_window 的 rank_corr_train,"
               "没有在本脚本里重算 -- 见结果卡。")
            del sig0_full, sig20_full, r, n, q_full, q_tr, sig0_tr, sig20_tr
        except Exception:
            traceback.print_exc()

        # ============================================================== block E -- two small checks
        _p(""); _p("=" * 78)
        _p("BLOCK E -- (e1) H8 buyable=False re-check; (e2) H9 by-ctl_cap-bucket rank IC, 2 splits")
        _p("=" * 78)
        try:
            cost = float(st.cfg.get("cost_per_side", bk.COST)) if hasattr(st, "cfg") else bk.COST
            top_frac_cfg = float(st.cfg.get("top_frac", bk.TOP_FRAC)) if hasattr(st, "cfg") else bk.TOP_FRAC
            b_normal = st.books(F["F1"], fit="train", evals=("train", "valid"), sign=sign_f["F1"])
            raw_target = st.target(buyable=False)
            b_raw = bk.books(sign_f["F1"] * np.asarray(F["F1"], dtype=np.float64), raw_target, tr_sl,
                              {"train": tr_sl, "valid": va_sl}, cost=cost, top_frac=top_frac_cfg, rank_by="long")
            _p("(e1) F1, normal label vs buyable=False label (same sign, own refit half-life each):")
            _book_line("normal label", b_normal)
            _book_line("buyable=False label", b_raw)
        except Exception:
            traceback.print_exc()
        try:
            ctl_cap = st.control("ctl_cap")
            for split_name, sl in (("train", tr_sl), ("valid", va_sl)):
                rows = dg.conditional_ic(sign_f["F1"] * np.asarray(F["F1"], dtype=np.float64)[sl],
                                         target[sl], np.asarray(ctl_cap, dtype=np.float64)[sl], buckets=5)
                _p(f"(e2) F1 rank_ic by ctl_cap-bucket, {split_name}: " +
                   "  ".join(f"Q{r['bucket']+1}={r['rank_ic']:+.4f}" for r in rows))
            del ctl_cap
        except Exception:
            traceback.print_exc()

    _p(""); _p("DONE.")


if __name__ == "__main__":
    main()
