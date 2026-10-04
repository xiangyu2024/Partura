"""F101: direct measurements on the pre-fold quantity J and on the fold itself.

The tree is  J = day_mean(std of Ret over [j, j+4] at volume-surge minutes j)  ->  |J - cs_mean(J)|
and the book then EMA-smooths the FOLDED quantity.  Stock diagnostics cannot answer:

  A  does |J - nanmean_cs(J)| reproduce the panel (i.e. did I read the tree right)?
  B  what does J's cross-section look like: where does the cs mean sit, how many triggers a day?
  C  is J anything other than plain intraday volatility?  (rank corr with day_std(Ret), rolling-5 std)
  D  the top decile of the fold: high-J names or low-J names?
  E  next-day excess by 20 quantiles of J itself: monotone, or a hump (the fold's premise)?
  F  fold-then-smooth (what is traded) vs smooth-then-fold vs no fold vs rank fold vs "instability only"
  G  who is in the short / long decile (label NaN share, J==0 share, size / turnover / vol ranks)
  H  where is the best fold centre (quantile q of J)?
  I  does the number of triggers matter?

Only train / valid are read.
"""
import warnings

import numpy as np

from partura.study_tools import Study, bk, dg

warnings.simplefilter("ignore", RuntimeWarning)
FID = "F101_day_shine_retstd"

V = "in_slice(Volume, 2, 237)"
DV = f"sub({V}, in_delay({V}, 1))"
MASK = f"is_gt({DV}, add(in_mean_full({DV}), in_stddev_full({DV})))"
R = "in_slice(Ret, 2, 237)"
J_EXPR = f"day_mean(in_sustain_stddev({MASK}, {R}, 5))"
HL = 10


def fold(x):
    return np.abs(x - np.nanmean(x, axis=1, keepdims=True))


def pct(x):
    r = dg.rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def ema(x, hl=HL):
    return bk.smoothed(np.asarray(x, dtype=np.float64), hl)


def row(name, sm, tgt, splits):
    """sm is sign-aligned and already smoothed; both books on each split."""
    out = [f"{name:<22}"]
    for k, s in splits.items():
        b = bk.book_row(sm, tgt, s)
        ric = np.nanmean(dg.rank_ic_series(sm[s], tgt[s]))
        out.append(f"{k}: rIC {ric:+.4f} LS {b['ls_sharpe']:+.2f} Lg {b['long_gross_ann']*100:+5.1f}% "
                   f"Ln {b['long_ann']*100:+5.1f}% Lshp {b['long_sharpe']:+.2f} short {b['short_gross_ann']*100:+5.1f}% "
                   f"TO {b['ls_turnover']*100:4.1f}%")
    print(" | ".join(out), flush=True)


def prof(name, sm, tgt, s, n=20):
    q = bk.quantile_profile(sm, tgt, s, n=n)
    print(f"{name}: " + " ".join(f"{r['excess_ann']*100:+.0f}" for r in q), flush=True)


with Study(FID) as st:
    P = st.panels({"J": J_EXPR, "trig": f"day_mean({MASK})", "roll5": f"day_mean(in_stddev_rolling({R}, 5))",
                   "base": st.cfg["expression"]})
    J, trig, roll5, base = (np.asarray(P[k], dtype=np.float64) for k in ("J", "trig", "roll5", "base"))
    ivol = np.asarray(st.control("ctl_ivol"), dtype=np.float64)
    dvol = np.asarray(st.control("ctl_dvol20"), dtype=np.float64)
    turn = np.asarray(st.control("ctl_turnrate"), dtype=np.float64)
    cap = np.asarray(st.control("ctl_cap"), dtype=np.float64)
    amt = np.asarray(st.control("ctl_amt"), dtype=np.float64)
    tgt = np.asarray(st.target(), dtype=np.float64)
    tr, va = st.slice("train"), st.slice("valid")
    SP = {"train": tr, "valid": va}
    ntrig = trig * 236.0

    # ---- A: did I read the tree right?
    K = J - np.nanmean(J, axis=1, keepdims=True)
    mine = np.abs(K)
    both = np.isfinite(mine) & np.isfinite(base)
    print("== A  reconstruction |J - nanmean_cs(J)| vs panel")
    print(f"finite cells: mine {np.isfinite(mine).mean():.4f} base {np.isfinite(base).mean():.4f} both {both.mean():.4f}; "
          f"max|diff| {np.nanmax(np.abs(mine - base)[both]):.3e}; median base {np.nanmedian(base[both]):.3e}; "
          f"rank corr {dg.pair_rank_corr(mine[tr], base[tr]):.4f}", flush=True)

    # ---- B: the cross-section of J
    print("== B  cross-section of J (train, per-day stats then averaged)")
    Jt, lab = J[tr], np.isfinite(tgt[tr])
    fin = np.isfinite(Jt)
    m = np.nanmean(Jt, axis=1)
    med = np.nanmedian(Jt, axis=1)
    pm = np.nanmean(np.where(fin, (Jt < m[:, None]), np.nan), axis=1)
    print(f"names/day {fin.sum(1).mean():.0f}; J finite among labelled {(fin & lab).sum() / lab.sum():.4f}; "
          f"share J==0 {np.nanmean(np.where(fin, Jt == 0, np.nan)):.4f}; mean {m.mean():.3e} median {med.mean():.3e} "
          f"mean/median {np.mean(m / med):.3f}; percentile of the cs mean {pm.mean():.3f} (min {pm.min():.3f} max {pm.max():.3f})")
    qs = [1, 5, 10, 25, 50, 75, 90, 95, 99]
    rel = np.nanpercentile(Jt / m[:, None], qs, axis=1).mean(1)
    print("J / cs_mean at pct " + " ".join(f"p{q}={v:.2f}" for q, v in zip(qs, rel)))
    nt = ntrig[tr]
    print("triggers per stock-day: " + " ".join(f"p{q}={np.nanpercentile(nt, q):.0f}" for q in (1, 5, 25, 50, 75, 95, 99))
          + f"; share <=2: {np.nanmean(nt[np.isfinite(nt)] <= 2):.4f}; share ==0: {np.nanmean(nt[np.isfinite(nt)] == 0):.4f}", flush=True)

    # ---- C: is J plain intraday vol?
    print("== C  daily cross-sectional rank corr (train)")
    pairs = {"J~ivol": (J, ivol), "J~roll5": (J, roll5), "J~dvol20": (J, dvol), "J~turnrate": (J, turn), "J~cap": (J, cap),
             "J~amt": (J, amt), "J~ntrig": (J, ntrig), "roll5~ivol": (roll5, ivol),
             "base~fold(ivol)": (base, fold(ivol)), "base~fold(roll5)": (base, fold(roll5)),
             "base~fold(dvol20)": (base, fold(dvol)), "base~ntrig": (base, ntrig), "base~J": (base, J)}
    print("  ".join(f"{k} {dg.pair_rank_corr(a[tr], b[tr]):+.3f}" for k, (a, b) in pairs.items()), flush=True)
    sig = -ema(base)
    pairs2 = {"sig~-ema|fold ivol|": -ema(fold(ivol)), "sig~-ema|fold roll5|": -ema(fold(roll5)), "sig~-ema(J)": -ema(J),
              "sig~-ema(ivol)": -ema(ivol), "sig~-|ema(K)|": -np.abs(ema(K)), "sig~-turnrate": -turn, "sig~cap": cap}
    print("traded signal: " + "  ".join(f"{k} {dg.pair_rank_corr(sig[tr], b[tr]):+.3f}" for k, b in pairs2.items()), flush=True)

    # ---- D: who is in the top decile of the fold?
    print("== D  top decile of the fold: share of names from the LOW side (J < cs mean)")
    for nm, f_, k_ in (("raw daily |K|", mine, K), ("traded EMA10|K|", ema(mine), ema(K))):
        for sn, s in SP.items():
            f, k = f_[s], k_[s]
            thr = np.nanpercentile(f, 90, axis=1, keepdims=True)
            top = f >= thr
            print(f"  {nm:<16} {sn}: low-side share {np.nansum(top & (k < 0)) / np.nansum(top):.3f}", flush=True)

    # ---- E: is next-day excess a hump in J?
    print("== E  annualised excess (%) by 20 quantiles, lowest -> highest")
    for sn, s in SP.items():
        prof(f"J raw           {sn}", J, tgt, s)
        prof(f"EMA10(J)        {sn}", ema(J), tgt, s)
        prof(f"EMA10(|K|)      {sn}", ema(mine), tgt, s)
        prof(f"EMA10(ivol)     {sn}", ema(ivol), tgt, s)

    # ---- F: what does each piece of the construction buy?
    print("== F  books at hl=10, sign fixed (long = low value of the folded/level quantity)")
    eK = ema(K)
    disp = ema(mine) - np.abs(eK)
    cands = {
        "base -EMA|K|": -ema(mine),
        "smooth-then-fold": -np.abs(eK),
        "instability only": -disp,
        "no fold -EMA(J)": -ema(J),
        "rank fold q=.5": -ema(np.abs(pct(J) - 0.5)),
        "hi side only": -ema(np.clip(K, 0, None)),
        "lo side only": -ema(np.clip(-K, 0, None)),
        "fold(ivol)": -ema(fold(ivol)),
        "fold(roll5)": -ema(fold(roll5)),
        "no fold -EMA(ivol)": -ema(ivol),
        "fold(dvol20)": -ema(fold(dvol)),
    }
    for k, v in cands.items():
        row(k, v, tgt, SP)

    # ---- G: who is in each leg of the traded signal?
    print("== G  composition of the legs of the traded signal (train)")
    s = tr
    sg, lab_nan = sig[s], ~np.isfinite(tgt[s])
    lo = sg <= np.nanpercentile(sg, 10, axis=1, keepdims=True)
    hi = sg >= np.nanpercentile(sg, 90, axis=1, keepdims=True)
    allm = np.isfinite(sg)
    feats = {"pct J": pct(J)[s], "pct EMA10 J": pct(ema(J))[s], "pct ivol": pct(ivol)[s], "pct turnrate": pct(turn)[s],
             "pct cap": pct(cap)[s], "pct amt": pct(amt)[s], "pct dvol20": pct(dvol)[s], "ntrig": ntrig[s]}
    for nm, msk in (("short decile", lo), ("long decile", hi), ("all scored", allm)):
        desc = " ".join(f"{k} {np.nanmean(v[msk]):.2f}" for k, v in feats.items())
        print(f"  {nm:<12} label-NaN share {lab_nan[msk].mean():.4f}  J==0 today {np.nanmean(J[s][msk] == 0):.4f}  "
              f"EMA K<0 {np.nanmean(eK[s][msk] < 0):.3f}  {desc}", flush=True)

    # ---- H: where is the best fold centre?
    print("== H  fold centre scan: -EMA10(|pct(J) - q|)")
    pj = pct(J)
    for q in (0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8):
        row(f"q={q:.1f}", -ema(np.abs(pj - q)), tgt, SP)
    print("   smooth first, then rank-fold: -|pct(EMA10 J) - q|")
    pej = pct(ema(J))
    for q in (0.3, 0.5, 0.7):
        row(f"sm-first q={q:.1f}", -np.abs(pej - q), tgt, SP)

    # ---- I: does the number of triggers matter?
    print("== I  rank IC of the traded signal inside terciles of the trigger count (train / valid)")
    pn = pct(ntrig)
    for a, b in ((0, 1 / 3), (1 / 3, 2 / 3), (2 / 3, 1.01)):
        msk = (pn >= a) & (pn < b)
        x = np.where(msk, sig, np.nan)
        print(f"  ntrig pct [{a:.2f},{b:.2f}): train {np.nanmean(dg.rank_ic_series(x[tr], tgt[tr])):+.4f} "
              f"valid {np.nanmean(dg.rank_ic_series(x[va], tgt[va])):+.4f}  mean ntrig {np.nanmean(ntrig[tr][msk[tr]]):.1f}", flush=True)
    row("ntrig itself (+)", ema(ntrig), tgt, SP)
    row("ntrig itself (-)", -ema(ntrig), tgt, SP)
