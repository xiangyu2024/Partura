"""x3 -- attribution of the S2_overlay long-leg increment (order R2).

R2's single question: is the +2.5pp long-leg increment of the rank-space overlay
g_w25 = cs_rank(K1) + 0.25*cs_rank(D30)  (vs K1 = known_stdamt_mean30 alone) real,
or one of the cheap explanations the engine run (tag S2_overlay) could not settle?
This script does the part that needs custom code -- building the exact two books
by hand so the "can't-buy records 0" bookkeeping effect and the per-name source of
the increment can be inspected (something `digest` cannot show).

Order of sections (most important first; print+flush each; del+gc.collect() between
sections; panels cast to float32; this does NOT run concurrently with S2_overlay):

  SelfCheck.  book1 (K1 alone, top decile, sign -1, hl=0) must match S2_overlay's
              own family-alone reading (+12.6%/+22.3%); book2 (the overlay, same
              construction) must match S2_overlay's g_w25 (+15.1%/+23.7%), each
              within ~0.5pp.  Stop (skip A/B/C/D) if it does not.
  A.  H16 -- how much of the increment is the "can't-buy names score 0" effect.
  B.  where the increment comes from: D30 decile and r=BASE^(1/3) bucket of the
      dropped/added names; how much of the increment a bare "penalise r>=24.9"
      rule alone would capture.
  C.  by calendar year.
  D.  fine weight grid (cheap, last; w=0 reduces to book1, a free cross-check).

Only train / valid are touched -- st.slice("holdout") is never called.
"""
import gc
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402

FID = "F108_max_ntkurt_close"
K_EXPR = "nt_ts_kurt(Close, 30)"
EX = {
    "base": f"day_max(pow_1_5(pow_2({K_EXPR})))",
    "K1": "cross_mean(day_std(Amt), 30)",
    "D30": f"cross_mean(day_max(pow_1_5(pow_2({K_EXPR}))), 30)",
}
COST = 0.0015
TOP_FRAC = 0.10
W_MAIN = 0.25
# expected from the S2_overlay engine run (tag S2_overlay, read via digest), hl0 both books:
EXPECT_B1 = {"train": (12.6, None), "valid": (22.3, None)}     # K1 alone      Lnet%
EXPECT_B2 = {"train": (15.1, 2.31), "valid": (23.7, 3.86)}     # g_w25 overlay Lnet%, Lshp
TOL_PP = 0.5


# ============================================================ copied verbatim from x1_anatomy.py / x2_longonly.py
def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


def pct_rank(a):
    r = dg.rank_rows(np.asarray(a, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def bucket(pr, n):
    return np.where(np.isfinite(pr), np.minimum(np.floor(pr * n), n - 1), np.nan)


def excess(t, universe):
    """label minus the equal-weight mean of the labelled cells of `universe` (NaN elsewhere)."""
    r = np.where(universe & np.isfinite(t), t, np.nan)
    return r - np.nanmean(r, axis=1, keepdims=True)


def cell_ann(ex, sel):
    """annualised mean (%) of the daily equal-weight excess of the cells in sel; mean names a day."""
    sel = sel & np.isfinite(ex)
    m = sel.sum(1)
    daily = np.where(m > 0, np.where(sel, ex, 0.0).sum(1) / np.maximum(m, 1), np.nan)
    return float(np.nanmean(daily) * 252 * 100), float(m.mean())


def safe(fn, label):
    try:
        fn()
    except Exception as exc:
        import traceback
        print(f"[section {label} FAILED] {type(exc).__name__}: {exc}", flush=True)
        traceback.print_exc()


def mem_mark(label):
    try:
        from partura import guard
        print(f"[mem] {label}: process anon ~ {guard.self_anon_gb():.2f} GiB", flush=True)
    except Exception:
        pass


def screened_book(held, ok, target, cost=COST):
    """copied verbatim from x2_longonly.py.  Pure-long equal-weight book of `held`
    (bool, per day) vs the equal-weight return of every `ok` (available) name that
    day.  A name can be `held` with a NaN `target` (unbuyable) -- it then occupies
    weight but contributes 0 that day, exactly like the engine's own book
    accounting (this is what section A measures)."""
    held = held & ok
    n = held.sum(1).astype(np.float64)
    w_half = np.where(held, 0.5 / np.maximum(n, 1)[:, None], 0.0)
    sig_dummy = np.where(ok, 1.0, np.nan)
    net, gross, turn = bk.long_book(w_half, sig_dummy, target, cost)
    return net, gross, turn, n


def book_stats_row(net, gross, turn, n):
    ln, lg = bk.stats(net), bk.stats(gross)
    return {"Lnet": ln["ann"] * 100, "Lgross": lg["ann"] * 100, "Lshp": ln["sharpe"],
            "LTO": float(np.nanmean(turn)) * 100, "N": float(np.nanmean(n))}


def fmt_row(r):
    return f"Lnet {r['Lnet']:+6.1f}% Lgross {r['Lgross']:+6.1f}% Lshp {r['Lshp']:+5.2f} LTO {r['LTO']:4.1f}% N {r['N']:5.0f}"


# ============================================================ new for x3
def held_top_decile(score_good, ok, frac=TOP_FRAC):
    """score_good already oriented high=good; returns the bool top-`frac` mask."""
    pr = pct_rank(np.where(ok, score_good, np.nan))
    return ok & np.isfinite(pr) & (pr >= 1.0 - frac)


def pct_of(mask_num, mask_den):
    """% of True cells in mask_den that are also True in mask_num (NaN if denom empty)."""
    d = float(mask_den.sum())
    return float(mask_num.sum()) / d * 100.0 if d > 0 else float("nan")


def main(st):
    mem_mark("start")
    P = st.panels(EX)
    missing = [k for k in EX if k not in P]
    if missing:
        print("MISSING panels:", missing, flush=True)
    tr, va = st.slice("train"), st.slice("valid")
    tgt = st.target()                    # buyable-filtered label (NaN where can't buy)
    tgt_raw = st.target(buyable=False)    # real next-day return even where unbuyable
    splits = (("train", tr), ("valid", va))
    mem_mark("after panels+target")

    BASE = np.asarray(P["base"], dtype=np.float32)
    K1 = np.asarray(P["K1"], dtype=np.float32)
    D30 = np.asarray(P["D30"], dtype=np.float32)
    sgn_K1 = st.sign(P["K1"], "train")
    sgn_D30 = st.sign(P["D30"], "train")
    print(f"sign(K1,train)={sgn_K1:+.0f}  sign(D30,train)={sgn_D30:+.0f}  (both expected -1, 'high=bad')", flush=True)

    # Each piece is ranked over ITS OWN natural availability, exactly like the engine's
    # cs_rank(K1) / cs_rank(D30) inside the add() -- NOT pre-intersected.  Only the final
    # held-set (book) is restricted to the universe each book actually needs:
    #   book1 = K1 alone            -> needs only K1            -> ok1
    #   book2 = cs_rank(K1)+w*cs_rank(D30) -> NaN unless BOTH are finite -> ok2 = ok1 & okD
    # (an earlier version of this script intersected ok1&okD even for book1's own ranking,
    # which shrank its universe and mismatched the self-check on train by +1.3pp -- see below).
    # Deliberately NOT requiring isfinite(tgt) anywhere here, so a name can be selected
    # today even if tomorrow turns out unbuyable (exactly how the real book/engine selects;
    # this is what lets section A see the "held but scores 0" mechanism at all).
    ok1 = np.isfinite(K1)
    okD = np.isfinite(D30)
    ok2 = ok1 & okD
    rk = pct_rank(-K1.astype(np.float64))            # high = good (low raw K1); NaN-aware per row
    rD = pct_rank(-D30.astype(np.float64))           # high = good (low raw D30), same "高=坏" convention as the R2 config
    combo = rk + W_MAIN * rD                         # NaN wherever either rk or rD is NaN, i.e. implicitly on ok2
    held1 = held_top_decile(rk, ok1)                 # book1: K1 alone
    held2 = held_top_decile(combo, ok2)              # book2: overlay w=0.25
    r_full = np.cbrt(np.asarray(BASE, dtype=np.float64))
    gc.collect()
    mem_mark("after setup (K1/D30/BASE/ok1/ok2/okD/rk/rD/combo/held1/held2/r_full)")

    STATE = {"ok_pass": True}

    # ------------------------------------------------------------ SelfCheck
    def self_check():
        hdr("SelfCheck -- book1/book2 vs S2_overlay's own engine reading (must match within 0.5pp)")
        for sname, sl in splits:
            b1 = book_stats_row(*screened_book(held1[sl], ok1[sl], tgt[sl]))
            b2 = book_stats_row(*screened_book(held2[sl], ok2[sl], tgt[sl]))
            exp1, _ = EXPECT_B1[sname]
            exp2, exp2shp = EXPECT_B2[sname]
            d1, d2 = b1["Lnet"] - exp1, b2["Lnet"] - exp2
            pass1, pass2 = abs(d1) <= TOL_PP, abs(d2) <= TOL_PP
            print(f"  [{sname}] book1(K1 alone)   {fmt_row(b1)}   vs expect Lnet {exp1:+.1f}%  diff {d1:+.2f}pp  "
                  f"{'OK' if pass1 else 'MISMATCH'}", flush=True)
            print(f"  [{sname}] book2(g_w25 repl) {fmt_row(b2)}   vs expect Lnet {exp2:+.1f}% Lshp {exp2shp:+.2f}  "
                  f"diff {d2:+.2f}pp  {'OK' if pass2 else 'MISMATCH'}", flush=True)
            STATE[f"b1_{sname}"], STATE[f"b2_{sname}"] = b1, b2
            STATE["ok_pass"] = STATE["ok_pass"] and pass1 and pass2
        if not STATE["ok_pass"]:
            print("  >>> SELF-CHECK FAILED (diff > 0.5pp on at least one split/book). Per the order: STOP here, "
                  "sections A/B/C/D below are NOT computed. Report this mismatch as-is.", flush=True)
        else:
            print("  self-check passed on both splits -- proceeding to A/B/C/D.", flush=True)
    safe(self_check, "SelfCheck")
    mem_mark("after SelfCheck")

    if not STATE.get("ok_pass"):
        return

    # ------------------------------------------------------------ A (H16: can't-buy bookkeeping)
    def sA():
        hdr("A. H16 -- how much of the increment is the can't-buy(NaN label) bookkeeping effect")
        unbuy = np.isnan(tgt)                            # unbuyable/no-label next day (cell property, independent of which book)
        held1_clean = held1 & ~unbuy
        held2_clean = held2 & ~unbuy
        dropped = held1 & ~held2                        # held in book1, not in book2
        added = held2 & ~held1                           # held in book2, not in book1
        for sname, sl in splits:
            b1c = book_stats_row(*screened_book(held1_clean[sl], ok1[sl], tgt[sl]))
            b2c = book_stats_row(*screened_book(held2_clean[sl], ok2[sl], tgt[sl]))
            b1, b2 = STATE[f"b1_{sname}"], STATE[f"b2_{sname}"]
            incr_before = b2["Lnet"] - b1["Lnet"]
            incr_after = b2c["Lnet"] - b1c["Lnet"]
            print(f"  [{sname}] NaN-excluded, renormalised: book1' {fmt_row(b1c)}  book2' {fmt_row(b2c)}  "
                  f"increment before {incr_before:+.2f}pp -> after {incr_after:+.2f}pp", flush=True)

            dro, add = dropped[sl], added[sl]
            unb = unbuy[sl]
            frac_dropped_nan = pct_of(dro & unb, dro)
            frac_added_nan = pct_of(add & unb, add)
            # benchmark universe = ok1 (book1's own, the broader of the two) throughout:
            ex_raw = excess(tgt_raw[sl], ok1[sl])        # real (buyable=False) excess, same universe convention as x1/x2
            a_drop_nan, n_drop_nan = cell_ann(ex_raw, dro & unb)
            a_drop_ok, n_drop_ok = cell_ann(ex_raw, dro & ~unb)
            a_add_nan, n_add_nan = cell_ann(ex_raw, add & unb)
            a_add_ok, n_add_ok = cell_ann(ex_raw, add & ~unb)
            print(f"  [{sname}] dropped(book1\\book2): {frac_dropped_nan:5.1f}% 标签NaN(买不进) | 次日真实超额(cell_ann,年化%)"
                  f" NaN组 {a_drop_nan:+6.1f}%(avgN {n_drop_nan:.1f})  非NaN组 {a_drop_ok:+6.1f}%(avgN {n_drop_ok:.1f})", flush=True)
            print(f"  [{sname}] added(book2\\book1):   {frac_added_nan:5.1f}% 标签NaN(买不进) | 次日真实超额(cell_ann,年化%)"
                  f" NaN组 {a_add_nan:+6.1f}%(avgN {n_add_nan:.1f})  非NaN组 {a_add_ok:+6.1f}%(avgN {n_add_ok:.1f})", flush=True)
        del unbuy, held1_clean, held2_clean, dropped, added
        gc.collect()
    safe(sA, "A")
    mem_mark("after A")

    # ------------------------------------------------------------ B (source of the increment)
    def sB():
        hdr("B. where the increment comes from: D30 decile / r=BASE^(1/3) bucket of dropped & added names")
        dropped, added = held1 & ~held2, held2 & ~held1
        bands = [(0.0, 6.0), (6.0, 10.0), (10.0, 15.0), (15.0, 20.0), (20.0, 24.9), (24.9, 26.0)]
        for sname, sl in splits:
            dro, add = dropped[sl], added[sl]
            hdr(f"B.decile(D30) [{sname}]")
            decD = bucket(pct_rank(np.where(okD[sl], D30[sl].astype(np.float64), np.nan)), 10)   # 9 = highest(worst) D30, ranked among D30's own universe
            nd, na = float(dro.sum()), float(add.sum())
            for q in range(10):
                sel = decD == q
                pd_, pa = pct_of(dro & sel, dro) if nd > 0 else float("nan"), pct_of(add & sel, add) if na > 0 else float("nan")
                print(f"    decile {q} (9=worst D30): dropped share {pd_:5.1f}%   added share {pa:5.1f}%", flush=True)
            hdr(f"B.rband(r) [{sname}]")
            rr = r_full[sl]
            for lo, hi in bands:
                sel = (rr >= lo) & (rr < hi)
                pd_, pa = pct_of(dro & sel, dro) if nd > 0 else float("nan"), pct_of(add & sel, add) if na > 0 else float("nan")
                print(f"    r in [{lo:g},{hi:g}): dropped share {pd_:5.1f}%   added share {pa:5.1f}%", flush=True)
            # how much of the total increment a bare "only penalise r>=24.9" rule would capture:
            # book3 = book1 (K1 alone) with EVERY r>=24.9 held name removed, nothing else changed --
            # a minimal standalone exclusion rule, not a config expression (see result card for why
            # this is the executor's own construction of an underspecified request).
            r249 = (rr >= 24.9) & (rr < 26.0)
            held3 = held1[sl] & ~r249
            b1, b2 = STATE[f"b1_{sname}"], STATE[f"b2_{sname}"]
            b3 = book_stats_row(*screened_book(held3, ok1[sl], tgt[sl]))
            incr_full = b2["Lnet"] - b1["Lnet"]
            incr_r249 = b3["Lnet"] - b1["Lnet"]
            pct_capt = incr_r249 / incr_full * 100.0 if abs(incr_full) > 1e-9 else float("nan")
            print(f"    book3 (book1 minus only its r>=24.9 names): {fmt_row(b3)}  "
                  f"incr_full(book2-book1) {incr_full:+.2f}pp   incr_r>=24.9-only {incr_r249:+.2f}pp   "
                  f"capture {pct_capt:+.1f}% of total increment", flush=True)
            del decD, rr, held3, b3
        del dropped, added
        gc.collect()
    safe(sB, "B")
    mem_mark("after B")

    # ------------------------------------------------------------ C (by calendar year)
    def sC():
        hdr("C. by calendar year (utrain = train+valid, 2018..2023) -- book1 vs book2, net excess & pure-long sharpe")
        years_all = np.asarray([d[:4] for d in st.dates])
        u = st.slice("utrain")
        yrs, ok1U, ok2U, h1U, h2U, tgtU = years_all[u], ok1[u], ok2[u], held1[u], held2[u], tgt[u]
        for y in sorted(set(yrs.tolist())):
            m = yrs == y
            b1 = book_stats_row(*screened_book(h1U[m], ok1U[m], tgtU[m]))
            b2 = book_stats_row(*screened_book(h2U[m], ok2U[m], tgtU[m]))
            print(f"  {y}  book1 {fmt_row(b1)}  |  book2 {fmt_row(b2)}  |  incr Lnet {b2['Lnet'] - b1['Lnet']:+5.1f}pp "
                  f"Lshp {b2['Lshp'] - b1['Lshp']:+5.2f}", flush=True)
        del years_all, u, yrs, ok1U, ok2U, h1U, h2U, tgtU
        gc.collect()
    safe(sC, "C")
    mem_mark("after C")

    # ------------------------------------------------------------ D (fine weight grid, cheap, last)
    def sD():
        hdr("D. fine weight grid (hl=0 throughout; universe held fixed at ok2 across all w for a clean sweep -- "
            "NB even w=0 stays on ok2, not ok1, because 0*NaN=NaN propagates through rk+w*rD; see result card)")
        for w in (0.0, 0.1, 0.15, 0.25, 0.4, 0.6, 1.0):
            combo_w = rk + w * rD
            held_w = held_top_decile(combo_w, ok2)
            for sname, sl in splits:
                row = book_stats_row(*screened_book(held_w[sl], ok2[sl], tgt[sl]))
                print(f"  w={w:<4g} [{sname}] {fmt_row(row)}", flush=True)
            del combo_w, held_w
        gc.collect()
    safe(sD, "D")
    mem_mark("end")


if __name__ == "__main__":
    with Study(FID) as st_:
        main(st_)
    print("\n[x3_attrib done]", flush=True)
