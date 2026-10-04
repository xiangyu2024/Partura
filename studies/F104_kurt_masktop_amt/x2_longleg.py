"""x2 -- what S3/S4 left open, and no stage table answers.  Only train / valid rows are touched.

  1. neighbourhood of the "exclusion" composite l_excl (exponent 2 / 3 / 6, CV reader, std30 as the level,
     60-day window) -- same books as the stage tables; self-checked on two panels whose numbers are known
  2. rank correlation of the TRADED signals (sign x panel, smoothed at the fitted half-life) between the
     original and each candidate -- the stage matrices compare raw panels, and the original is a noisy daily one
  3. liquidity x concentration double sort: inside a low-liquidity book, does "not concentrated" add,
     and is it an exclusion (only the most concentrated bucket is bad) or a ranking?
  4. the two conditional-IC tables disagree (by kshare30 the signal is stronger in illiquid names, by amt30
     in active names).  Is the kshare30 reading confounded by liquidity varying INSIDE a kshare bucket?
  5. who is in the long decile of each candidate: liquidity rank, size rank, traded value, overlap with the
     plain low-liquidity book (capacity, and "is this just the F001 long book")
"""
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402

FID = "F104_kurt_masktop_amt"
A30 = "cross_mean(day_sum(Amt), 30)"
A60 = "cross_mean(day_sum(Amt), 60)"
S30 = "cross_mean(day_std(Amt), 30)"
BK = f"cs_regres(cs_rank(cross_mean(day_kurt(Amt), 30)), cs_rank({A30}))"
BC = f"cs_regres(cs_rank(cross_mean(div(day_std(Amt), day_mean(Amt)), 30)), cs_rank({A30}))"
BK60 = f"cs_regres(cs_rank(cross_mean(day_kurt(Amt), 60)), cs_rank({A60}))"
EX = {
    "base":     "day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))",
    "amt30":    A30,
    "std30":    S30,
    "f001":     "cross_max(day_std(Amt), 9)",
    "bk":       BK,
    "bc":       BC,
    "addcv":    f"add(cs_rank({BC}), cs_rank({A30}))",
    "excl":     f"add(cs_rank({A30}), pow_3(cs_rank({BK})))",
    # neighbours of l_excl -- new panels
    "excl_p2":  f"add(cs_rank({A30}), pow_2(cs_rank({BK})))",
    "excl_p6":  f"add(cs_rank({A30}), pow_3(pow_2(cs_rank({BK}))))",
    "excl_cv":  f"add(cs_rank({A30}), pow_3(cs_rank({BC})))",
    "excl_std": f"add(cs_rank({S30}), pow_3(cs_rank({BK})))",
    "excl_60":  f"add(cs_rank({A60}), pow_3(cs_rank({BK60})))",
}
# sign and half-life as fitted on train in the stage tables (S0 / S3 / S4)
FIT = {"base": (-1.0, 20), "bk": (-1.0, 1), "bc": (-1.0, 0), "excl": (-1.0, 0), "addcv": (-1.0, 0),
       "std30": (-1.0, 0), "f001": (-1.0, 0), "amt30": (-1.0, 1)}


def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


def pct_rank(a):
    r = dg.rank_rows(np.asarray(a, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def bucket(x, mask, n):
    """within-day quantile bucket 0..n-1 of x over the cells in mask (0 = lowest); NaN elsewhere."""
    pr = pct_rank(np.where(mask, x, np.nan))
    return np.where(np.isfinite(pr), np.minimum(np.floor(pr * n), n - 1), np.nan)


def cell_ann(ex, sel):
    """annualised mean (in %) of the daily equal-weight excess of the cells in sel."""
    m = sel.sum(1)
    daily = np.where(m > 0, np.where(sel, ex, 0.0).sum(1) / np.maximum(m, 1), np.nan)
    return float(np.nanmean(daily) * 252 * 100)


def sp_series(a, b, mask, min_n=30):
    """daily Spearman of a and b over the cells of mask finite in both."""
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    ok = mask & np.isfinite(a) & np.isfinite(b)
    a[~ok] = np.nan
    b[~ok] = np.nan
    ra, rb = dg.rank_rows(a), dg.rank_rows(b)
    n = ok.sum(1)
    ra = ra - np.nanmean(ra, axis=1, keepdims=True)
    rb = rb - np.nanmean(rb, axis=1, keepdims=True)
    num = np.nansum(ra * rb, axis=1)
    den = np.sqrt(np.nansum(ra * ra, axis=1) * np.nansum(rb * rb, axis=1))
    return np.where((n >= min_n) & (den > 0), num / np.where(den > 0, den, 1), np.nan)


def row_corr(ra, rb):
    ok = np.isfinite(ra) & np.isfinite(rb)
    a = np.where(ok, ra, np.nan)
    b = np.where(ok, rb, np.nan)
    a = a - np.nanmean(a, axis=1, keepdims=True)
    b = b - np.nanmean(b, axis=1, keepdims=True)
    num = np.nansum(a * b, axis=1)
    den = np.sqrt(np.nansum(a * a, axis=1) * np.nansum(b * b, axis=1))
    return float(np.nanmean(np.where(den > 0, num / np.where(den > 0, den, 1), np.nan)))


def show_book(st, name, panel):
    b = st.books(panel, fit="train", evals=("train", "valid"))
    tr, va = b["splits"]["train"], b["splits"]["valid"]
    sg = st.sign(panel, "train")
    dist = dg.distinct_fraction(np.asarray(panel[st.slice("train")], dtype=np.float64))
    print(f"{name:<10} sgn {sg:+.0f} hl {b['hl_used']:>3g}  LS {tr['ls_sharpe']:+.2f}/{va['ls_sharpe']:+.2f}  "
          f"Lgross {tr['long_gross_ann'] * 100:+.1f}%/{va['long_gross_ann'] * 100:+.1f}%  "
          f"Lnet {tr['long_ann'] * 100:+.1f}%/{va['long_ann'] * 100:+.1f}%  "
          f"Lsharpe {tr['long_sharpe']:+.2f}/{va['long_sharpe']:+.2f}  short {tr['short_gross_ann'] * 100:+.1f}%/"
          f"{va['short_gross_ann'] * 100:+.1f}%  TO {tr['ls_turnover'] * 100:.1f}%  dist {dist:.2f}", flush=True)


def main():
    with Study(FID) as st:
        P = st.panels(EX)
        missing = [k for k in EX if k not in P]
        if missing:
            print("MISSING panels:", missing)
        tr, va = st.slice("train"), st.slice("valid")
        tgt = st.target()
        splits = (("train", tr), ("valid", va))

        # ------------------------------------------------------------ 1
        hdr("1. neighbourhood of l_excl (train/valid; sign and half-life fitted on train)")
        print("self-check -- the stage tables say: bk (= r_ref30) hl 1 LS +3.75/+1.91 Lnet +5.4%/+0.3%;  "
              "excl (= l_excl) hl 0 LS +3.52/+3.96 Lnet +13.1%/+16.7%")
        for name in ("bk", "excl", "excl_p2", "excl_p6", "excl_cv", "excl_std", "excl_60"):
            if name in P:
                try:
                    show_book(st, name, P[name])
                except Exception as exc:
                    print(f"{name}: books failed: {type(exc).__name__}: {exc}", flush=True)

        # ------------------------------------------------------------ 2
        hdr("2. rank correlation of the TRADED signals (sign x panel, EMA at the fitted half-life)")
        names = [n for n in FIT if n in P]
        SM = {n: bk.smoothed(FIT[n][0] * P[n].astype(np.float64), FIT[n][1]) for n in names}
        for sname, sl in splits:
            R = {n: dg.rank_rows(SM[n][sl]) for n in names}
            print(f"[{sname}]  " + " ".join(f"{n:>7}" for n in names))
            for a in names:
                print(f"{a:>8}  " + " ".join(f"{row_corr(R[a], R[b]):7.2f}" for b in names), flush=True)
            del R

        # ------------------------------------------------------------ 3
        hdr("3. liquidity x concentration double sort (next-day excess vs the equal-weight universe, annualised %)")
        a30 = P["amt30"].astype(np.float64)
        s30 = P["std30"].astype(np.float64)
        for rname in ("bk", "bc"):
            bur = P[rname].astype(np.float64)
            for sname, sl in splits:
                a, s, b, t = a30[sl], s30[sl], bur[sl], tgt[sl]
                ok = np.isfinite(a) & np.isfinite(b) & np.isfinite(t) & np.isfinite(s)
                ex = np.where(ok, t, np.nan)
                ex = ex - np.nanmean(ex, axis=1, keepdims=True)
                qa = bucket(a, ok, 5)
                qb_all = bucket(b, ok, 5)                      # universe-wide concentration quintile
                print(f"\n[{sname}] reader = {rname}; rows = amt30 quintile (L1 = least active); "
                      f"columns = concentration quintile WITHIN the row (B1 = least concentrated)")
                print(f"{'':>10} " + " ".join(f"{'B' + str(j + 1):>8}" for j in range(5)) + f" {'row':>8} {'B1-B5':>8}")
                for i in range(5):
                    row = ok & (qa == i)
                    qb = bucket(b, row, 5)
                    cells = [cell_ann(ex, row & (qb == j)) for j in range(5)]
                    print(f"{'L' + str(i + 1):>10} " + " ".join(f"{c:8.1f}" for c in cells)
                          + f" {cell_ann(ex, row):8.1f} {cells[0] - cells[4]:8.1f}", flush=True)
                for lab, x in (("amt30", a), ("std30", s)):
                    dec = ok & (bucket(x, ok, 10) == 0)        # the least-liquid decile = the long book's home
                    cells = [cell_ann(ex, dec & (qb_all == j)) for j in range(5)]
                    share = [float((dec & (qb_all == j)).sum() / max(dec.sum(), 1)) for j in range(5)]
                    keep = dec & (qb_all < 4)
                    print(f"  bottom decile by {lab}: all {cell_ann(ex, dec):+.1f}%; by UNIVERSE-wide concentration quintile "
                          + " ".join(f"B{j + 1} {cells[j]:+.1f}% ({share[j]:.0%})" for j in range(5))
                          + f"; dropping B5 -> {cell_ann(ex, keep):+.1f}%", flush=True)

        # by year (utrain): the least-liquid decile with and without its most concentrated names
        ut = st.slice("utrain")
        yrs = np.array([int(str(d)[:4]) for d in np.asarray(st.dates)[ut]])
        a, b, t = a30[ut], P["bk"].astype(np.float64)[ut], tgt[ut]
        ok = np.isfinite(a) & np.isfinite(b) & np.isfinite(t)
        ex = np.where(ok, t, np.nan)
        ex = ex - np.nanmean(ex, axis=1, keepdims=True)
        dec = ok & (bucket(a, ok, 10) == 0)
        qb_all = bucket(b, ok, 5)
        print("\nby year -- bottom decile by amt30 (reader bk, UNIVERSE-wide concentration quintile):")
        for y in sorted(set(yrs.tolist())):
            r = yrs == y
            print(f"   {y}: all {cell_ann(ex[r], dec[r]):+6.1f}%   B1-B4 {cell_ann(ex[r], (dec & (qb_all < 4))[r]):+6.1f}%   "
                  f"B5 only {cell_ann(ex[r], (dec & (qb_all == 4))[r]):+6.1f}%   B1 only "
                  f"{cell_ann(ex[r], (dec & (qb_all == 0))[r]):+6.1f}%   share of B5 "
                  f"{(dec & (qb_all == 4))[r].sum() / max(dec[r].sum(), 1):.0%}", flush=True)

        # ------------------------------------------------------------ 4
        hdr("4. conditional rank IC of the concentration residual (bk): by amt30 vs by kshare30")
        ks = st.control("ctl_kshare30").astype(np.float64)
        bur = P["bk"].astype(np.float64)
        for sname, sl in splits:
            a, k, b, t = a30[sl], ks[sl], bur[sl], tgt[sl]
            ok = np.isfinite(a) & np.isfinite(b) & np.isfinite(t) & np.isfinite(k)
            for glab, g in (("amt30", a), ("kshare30", k)):
                qg = bucket(g, ok, 5)
                print(f"[{sname}] gate = {glab} (Q1 = lowest value of the gate)")
                for i in range(5):
                    m = ok & (qg == i)
                    r_bt = sp_series(b, t, m)
                    r_ba = sp_series(b, a, m)
                    r_at = sp_series(a, t, m)
                    part = (r_bt - r_ba * r_at) / np.sqrt(np.clip((1 - r_ba ** 2) * (1 - r_at ** 2), 1e-12, None))
                    print(f"   Q{i + 1}: IC(bk) {np.nanmean(r_bt):+.4f}   Spearman(bk, amt30) {np.nanmean(r_ba):+.3f}   "
                          f"IC(amt30) {np.nanmean(r_at):+.4f}   IC(bk | amt30) {np.nanmean(part):+.4f}", flush=True)

        # ------------------------------------------------------------ 5
        hdr("5. who is in the long decile (traded signal; decile book membership as in partura.books)")
        amt_day = np.expm1(st.control("ctl_amt").astype(np.float64))
        cap = st.control("ctl_cap").astype(np.float64)
        for sname, sl in splits:
            t = tgt[sl]
            L = {n: bk.long_short_weights(SM[n][sl], 0.10) > 0 for n in names}
            uni_med = float(np.nanmedian(amt_day[sl][np.isfinite(SM["amt30"][sl])]))
            print(f"[{sname}] universe median daily Amt = {uni_med:.4g} (raw units)")
            print(f"{'':>8} {'rk amt30':>9} {'rk cap':>7} {'med Amt / universe med':>23} {'in amt30 long':>14} "
                  f"{'in f001 long':>13} {'in std30 long':>14} {'gross excess':>13}")
            for n in names:
                okc = np.isfinite(SM[n][sl])
                ra = pct_rank(np.where(okc, a30[sl], np.nan))
                rc = pct_rank(np.where(okc, cap[sl], np.nan))
                ln = L[n]
                tt = np.where(okc & np.isfinite(t), t, np.nan)
                ex = tt - np.nanmean(tt, axis=1, keepdims=True)
                print(f"{n:>8} {np.nanmean(ra[ln]):9.2f} {np.nanmean(rc[ln]):7.2f} "
                      f"{np.nanmedian(amt_day[sl][ln]) / uni_med:23.3f} "
                      f"{(ln & L['amt30']).sum() / max(ln.sum(), 1):14.2f} {(ln & L['f001']).sum() / max(ln.sum(), 1):13.2f} "
                      f"{(ln & L['std30']).sum() / max(ln.sum(), 1):14.2f} {cell_ann(ex, ln & np.isfinite(ex)):12.1f}%",
                      flush=True)
    print("\n[x2 done]")


if __name__ == "__main__":
    main()
