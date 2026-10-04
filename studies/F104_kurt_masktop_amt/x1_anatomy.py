"""x1 -- what  day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))  reads on REAL data.

No stock diagnostic answers these, and the stage plan depends on the answers:

  0. the helper sources the `src` tool cannot show (_kurt, rank, the NT-face adapter)
  1. is abs_ a no-op?  (Amt >= 0)
  2. how many minutes a day does the mask node overwrite per stock (k), and what does the
     tree read as a function of k -- own-turnover kurtosis, or a meter of k?
  3. does the tie-break by column index (stock code) leak into k?
  4. what drives the plain kurtosis of Amt on untouched stocks (auction bars? one burst?)
  5. who sits in the two end deciles of the TRADED signal (EMA-20 of -kurt)
  6. where is the rank IC: inside which regime of k, and how much is between regimes

Only utrain (= train + valid) rows are touched; the holdout is never sliced.
"""
import importlib.util
import inspect
import sys
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402

FID = "F104_kurt_masktop_amt"
M = 241
B = "nt_cs_mask_top_replace_mean_neg(Amt)"
EX = {
    "base":    "day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))",
    "noabs":   f"day_kurt({B})",
    "nat":     "day_kurt(Amt)",
    "kfrac":   f"day_mean(is_gt0(sub({B}, Amt)))",          # share of minutes overwritten (new > old)
    "pos":     "day_mean(is_gt0(Amt))",                      # share of minutes with a trade
    "inj":     f"div(day_sum({B}), day_sum(Amt))",           # (own + injected) / own turnover
    "maxsh":   "div(day_max(Amt), day_sum(Amt))",
    "firstsh": "div(day_first(Amt), day_sum(Amt))",
    "lastsh":  "div(day_last(Amt), day_sum(Amt))",
    "argmax":  "day_argmax(Amt)",
    "cv":      "div(day_std(Amt), day_mean(Amt))",
    "skew":    "day_skew(Amt)",
}


def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


def show_sources():
    hdr("0. helper sources on the SERVER (the `src` tool only shows registered operators)")
    try:
        from alphacube.operators import common as C, nd_cs
        for label, fn in (("common._kurt", getattr(C, "_kurt", None)), ("common.rank", getattr(C, "rank", None)),
                          ("nd_cs._valid", getattr(nd_cs, "_valid", None)), ("nd_cs._mean", getattr(nd_cs, "_mean", None)),
                          ("common._mean", getattr(C, "_mean", None)), ("common.div", getattr(C, "div", None))):
            if fn is None:
                print(f"# {label}: not found")
                continue
            try:
                print(f"# {label}\n{inspect.getsource(inspect.unwrap(fn))}")
            except Exception as exc:
                print(f"# {label}: source unavailable ({exc})")
        from alphacube.engine import kernels
        src = inspect.getsource(kernels.apply_cube).split("\n")
        i = next((j for j, ln in enumerate(src) if 'spec.face == "nt"' in ln), None)
        if i is not None:
            print("# engine.kernels.apply_cube, NT-face branch\n" + "\n".join(src[i:i + 9]))
    except Exception as exc:
        print(f"sources failed: {type(exc).__name__}: {exc}")


def run_selfchecks():
    hdr("0b. probe self-checks with the SERVER kernels")
    try:
        from alphacube.catalog import default_registry
        from partura.bridge import PARTURA_ROOT
        p = PARTURA_ROOT / "studies" / FID / "probes.py"
        spec = importlib.util.spec_from_file_location("f104_probes", p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.selfcheck_report(default_registry())
    except Exception as exc:
        print(f"selfcheck failed: {type(exc).__name__}: {exc}")


def spearman_days(a, b, mask=None, min_n=30):
    """Mean daily Spearman over the cells finite in both (and in `mask`)."""
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    ok = np.isfinite(a) & np.isfinite(b)
    if mask is not None:
        ok &= mask
    a[~ok] = np.nan
    b[~ok] = np.nan
    ra, rb = dg.rank_rows(a), dg.rank_rows(b)
    n = ok.sum(1)
    ra = ra - np.nanmean(ra, axis=1, keepdims=True)
    rb = rb - np.nanmean(rb, axis=1, keepdims=True)
    num = np.nansum(ra * rb, axis=1)
    den = np.sqrt(np.nansum(ra * ra, axis=1) * np.nansum(rb * rb, axis=1))
    c = np.where((n >= min_n) & (den > 0), num / np.where(den > 0, den, 1), np.nan)
    return float(np.nanmean(c)), int(np.isfinite(c).sum())


def pct_rank(a):
    r = dg.rank_rows(np.asarray(a, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def excess(tgt, universe):
    """next-day return minus the equal-weight mean of the universe cells, per day."""
    t = np.where(universe & np.isfinite(tgt), tgt, np.nan)
    return t - np.nanmean(t, axis=1, keepdims=True)


def main():
    if "data" not in sys.argv[1:]:        # `x1_anatomy.py data` = skip the source/self-check part (already printed once)
        show_sources()
        run_selfchecks()
    with Study(FID) as st:
        P = st.panels(EX)
        missing = [k for k in EX if k not in P]
        if missing:
            print("MISSING panels:", missing)
        ut, tr, va = st.slice("utrain"), st.slice("train"), st.slice("valid")
        tgt_full = st.target()
        ctl = {n: st.control(n) for n in ("ctl_amt", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_mom20")}
        dates = np.asarray(st.dates)
        syms = np.asarray(st.symbols)
        ncol = len(syms)

        base, nat = P["base"], P["nat"]
        k_full = np.rint(P["kfrac"].astype(np.float64) * M)
        fin = np.isfinite(base)

        # ---------------------------------------------------------------- 1
        hdr("1. is abs_ a no-op?")
        if "noabs" in P:
            a, b = base[ut], P["noabs"][ut]
            both = np.isfinite(a) & np.isfinite(b)
            print(f"finite pattern equal: {bool((np.isfinite(a) == np.isfinite(b)).all())};  "
                  f"max |base - noabs| = {float(np.abs(a[both] - b[both]).max()):.3g};  "
                  f"cells exactly equal = {float((a[both] == b[both]).mean()):.6f}")

        # ---------------------------------------------------------------- 2
        hdr("2. the tree as a function of k = minutes overwritten by the mask node (utrain)")
        print(f"symbols[0:3]={list(syms[:3])}  symbols[-3:]={list(syms[-3:])}  n={ncol}")
        b_, n_, k_ = base[ut].astype(np.float64), nat[ut].astype(np.float64), k_full[ut]
        f_ = np.isfinite(b_) & np.isfinite(k_)
        ex = excess(tgt_full[ut], f_)
        ra = pct_rank(np.where(f_, ctl["ctl_amt"][ut], np.nan))
        rb = pct_rank(np.where(f_, b_, np.nan))
        edges = [(0, 0), (1, 1), (2, 2), (3, 5), (6, 12), (13, 30), (31, 60), (61, 120), (121, 180), (181, 241)]
        print(f"{'k':>9} {'share':>7} {'base med':>9} {'base p10':>9} {'base p90':>9} {'nat med':>8} "
              f"{'2pt 1/(w(1-w))-6':>17} {'rank(base)':>10} {'rank(Amt)':>9} {'next-day excess ann':>20}")
        for lo, hi in edges:
            m = f_ & (k_ >= lo) & (k_ <= hi)
            if m.sum() == 0:
                continue
            w = np.clip(k_[m] / M, 1e-9, 1 - 1e-9)
            tp = np.median(1 / (w * (1 - w)) - 6) if lo > 0 else float("nan")
            e = ex[m]
            print(f"{(str(lo) if lo == hi else f'{lo}-{hi}'):>9} {m.sum() / f_.sum():7.3f} {np.median(b_[m]):9.2f} "
                  f"{np.quantile(b_[m], .1):9.2f} {np.quantile(b_[m], .9):9.2f} {np.nanmedian(n_[m]):8.2f} "
                  f"{tp:17.2f} {np.nanmean(rb[m]):10.3f} {np.nanmean(ra[m]):9.3f} {np.nanmean(e) * 252 * 100:19.1f}%")
        m0 = f_ & (k_ == 0) & np.isfinite(n_)
        d0 = np.abs(b_[m0] - n_[m0]) / np.maximum(np.abs(n_[m0]), 1.0)
        print(f"k=0 cells: base vs plain kurt  max rel diff {float(d0.max()):.3g}, share within 1e-3: {float((d0 < 1e-3).mean()):.4f}")
        w_all = np.clip(k_ / M, 1e-9, 1 - 1e-9)
        two_pt = np.where(k_ > 0, 1 / (w_all * (1 - w_all)) - 6, np.nan)
        print("daily Spearman:  (base, plain kurt) all cells            %.3f  [%d days]" % spearman_days(b_, n_, f_))
        print("                 (base, plain kurt) cells with k>0       %.3f" % spearman_days(b_, n_, f_ & (k_ > 0))[0])
        print("                 (base, 2-point formula of k) k>0        %.3f" % spearman_days(b_, two_pt, f_ & (k_ > 0))[0])
        print("                 (base, k) cells with k>=12              %.3f" % spearman_days(b_, k_, f_ & (k_ >= 12))[0])
        print("                 (base, log Amt) all                     %.3f" % spearman_days(b_, ctl["ctl_amt"][ut], f_)[0])
        print("                 (plain kurt, log Amt) all               %.3f" % spearman_days(n_, ctl["ctl_amt"][ut], f_)[0])
        if "inj" in P:
            inj = P["inj"][ut].astype(np.float64)
            for lo, hi in ((1, 1), (2, 5), (6, 30), (31, 241)):
                m = f_ & (k_ >= lo) & (k_ <= hi) & np.isfinite(inj)
                print(f"   k in [{lo},{hi}]: median (own+injected)/own daily turnover = {np.median(inj[m]):.2f}")
        yrs = np.array([int(str(d)[:4]) for d in dates[ut]])
        print("by year: share of stock-days with k>0 / k>=12 / k>=60, and share of zero-trade minutes:")
        for y in sorted(set(yrs)):
            r = yrs == y
            ff = f_[r]
            print(f"   {y}: k>0 {((k_[r] > 0) & ff).sum() / ff.sum():.3f}  k>=12 {((k_[r] >= 12) & ff).sum() / ff.sum():.3f}  "
                  f"k>=60 {((k_[r] >= 60) & ff).sum() / ff.sum():.3f}  zero-minute share {1 - np.nanmean(P['pos'][ut][r][ff]):.4f}")

        # ---------------------------------------------------------------- 3
        hdr("3. tie-break by column index: does stock order leak into k?")
        nz = np.rint((1.0 - P["pos"][ut].astype(np.float64)) * M)
        nz_x = nz - np.nanmin(np.where(f_, nz, np.nan), axis=1, keepdims=True)     # beyond the bars every stock has at 0
        col = np.broadcast_to(np.arange(ncol)[None, :], k_.shape)
        terc = np.minimum((col * 3) // ncol, 2)
        print("universal zero bars per day (min over stocks), median:", float(np.nanmedian(np.nanmin(np.where(f_, nz, np.nan), axis=1))))
        print(f"{'own zero minutes':>18} {'cells':>9} {'k | low-index third':>20} {'mid':>8} {'high-index third':>17}")
        for lo, hi in ((0, 0), (1, 4), (5, 19), (20, 59), (60, 149), (150, 241)):
            m = f_ & (nz_x >= lo) & (nz_x <= hi)
            if m.sum() < 100:
                continue
            ks = [float(np.mean(k_[m & (terc == t)])) if (m & (terc == t)).sum() else float("nan") for t in range(3)]
            print(f"{f'{lo}-{hi}':>18} {int(m.sum()):9d} {ks[0]:20.1f} {ks[1]:8.1f} {ks[2]:17.1f}")
        print("daily Spearman (k, column index) over cells with >=20 own zero minutes: %.3f [%d days]"
              % spearman_days(k_, col.astype(np.float64), f_ & (nz_x >= 20), min_n=20))
        print("daily Spearman (base, column index) all cells: %.3f" % spearman_days(b_, col.astype(np.float64), f_)[0])
        for t, nm in enumerate(("low-index third", "mid third", "high-index third")):
            print(f"   {nm}: first={syms[t * ncol // 3]} last={syms[min((t + 1) * ncol // 3, ncol) - 1]}  "
                  f"mean k {np.mean(k_[f_ & (terc == t)]):.2f}  mean own zero minutes {np.mean(nz_x[f_ & (terc == t)]):.2f}")

        # ---------------------------------------------------------------- 4
        hdr("4. what drives the plain kurtosis of Amt (cells with k=0, utrain)")
        for nm in ("maxsh", "firstsh", "lastsh", "cv", "skew"):
            if nm in P:
                print(f"   daily Spearman (plain kurt, {nm:<7}) = %.3f" % spearman_days(n_, P[nm][ut], m0)[0])
        if "argmax" in P:
            am = P["argmax"][ut].astype(np.float64)[m0]
            print(f"   argmax(Amt) range [{np.nanmin(am):.3g}, {np.nanmax(am):.3g}]")
            top = np.nanmax(am)
            for lab, sel in (("first bar", am == np.nanmin(am)), ("bars 2-6", (am > np.nanmin(am)) & (am <= np.nanmin(am) + 5 * (top - np.nanmin(am)) / 240)),
                             ("last bar", am == top)):
                print(f"   biggest minute is the {lab}: {float(np.mean(sel)):.3f} of stock-days")
            for nm in ("maxsh", "firstsh", "lastsh"):
                print(f"   median {nm} = {float(np.nanmedian(P[nm][ut][m0])):.4f}  (1/241 = {1 / 241:.4f})")
            print(f"   median plain kurt = {float(np.nanmedian(n_[m0])):.2f}, p90 = {float(np.nanquantile(n_[m0], .9)):.2f}, "
                  f"p99 = {float(np.nanquantile(n_[m0], .99)):.2f}")

        # ---------------------------------------------------------------- 5 / 6
        sg = st.sign(base, "train")
        sm_full = bk.smoothed(sg * base.astype(np.float64), 20)
        smn_full = bk.smoothed(sg * nat.astype(np.float64), 20)
        ek_full = bk.smoothed(np.where(fin, k_full, np.nan), 20)
        print(f"\nsign fitted on train: {sg:+.0f}")
        for name, sl in (("train", tr), ("valid", va)):
            hdr(f"5. deciles of the TRADED signal (EMA-20 of sign x base) -- {name}; D1 = short end, D10 = long end")
            sm, smn, ek = sm_full[sl], smn_full[sl], ek_full[sl]
            tg = tgt_full[sl]
            okc = np.isfinite(sm)
            pr = pct_rank(np.where(okc, sm, np.nan))
            dec = np.where(okc, np.minimum(np.floor(pr * 10), 9), np.nan)
            ex = excess(tg, okc)
            R = {n: pct_rank(np.where(okc, c[sl], np.nan)) for n, c in ctl.items()}
            rnat = pct_rank(np.where(okc, -smn, np.nan))        # rank of EMA-20 plain kurt (high = high kurt)
            print(f"{'D':>3} {'excess ann':>11} {'EMA k':>7} {'k<0.5':>6} {'k>=20':>6} {'rk Amt':>7} {'rk cap':>7} {'rk turn':>8} "
                  f"{'rk ivol':>8} {'rk mom20':>9} {'rk EMA plain kurt':>18}")
            for d in range(10):
                m = dec == d
                print(f"{d + 1:>3} {np.nanmean(ex[m]) * 252 * 100:10.1f}% {np.nanmean(ek[m]):7.1f} {np.mean(ek[m] < 0.5):6.2f} "
                      f"{np.mean(ek[m] >= 20):6.2f} {np.nanmean(R['ctl_amt'][m]):7.2f} {np.nanmean(R['ctl_cap'][m]):7.2f} "
                      f"{np.nanmean(R['ctl_turnrate'][m]):8.2f} {np.nanmean(R['ctl_ivol'][m]):8.2f} {np.nanmean(R['ctl_mom20'][m]):9.2f} "
                      f"{np.nanmean(rnat[m]):18.2f}")
            hdr(f"6. where the rank IC lives -- {name}; regimes by EMA-20 of k")
            regs = (("U0 never masked (EMA k<0.5)", ek < 0.5), ("U1 borderline (0.5<=EMA k<20)", (ek >= 0.5) & (ek < 20)),
                    ("U2 deep illiquid (EMA k>=20)", ek >= 20))
            print(f"{'regime':<32} {'share':>6} {'excess ann':>11} {'IC traded':>10} {'IC EMA plain kurt':>18} {'long-decile share':>18} "
                  f"{'short-decile share':>19} {'excess | long dec':>18} {'excess | short dec':>19}")
            for lab, rm in regs:
                rm = rm & okc
                ic1 = spearman_days(sm, tg, rm)[0]
                ic2 = spearman_days(smn, tg, rm)[0]
                lm, shm = rm & (dec == 9), rm & (dec == 0)
                print(f"{lab:<32} {rm.sum() / okc.sum():6.3f} {np.nanmean(ex[rm]) * 252 * 100:10.1f}% {ic1:10.4f} {ic2:18.4f} "
                      f"{lm.sum() / (dec == 9).sum():18.3f} {shm.sum() / (dec == 0).sum():19.3f} "
                      f"{np.nanmean(ex[lm]) * 252 * 100:17.1f}% {np.nanmean(ex[shm]) * 252 * 100:18.1f}%")
            print("whole universe: IC traded %.4f   IC EMA-20 plain kurt %.4f   Spearman(traded, EMA plain kurt) %.3f"
                  % (spearman_days(sm, tg, okc)[0], spearman_days(smn, tg, okc)[0], spearman_days(sm, smn, okc)[0]))
    print("\n[x1 done]")


if __name__ == "__main__":
    main()
