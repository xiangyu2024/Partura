"""F110 X1: anatomy of  T = D * |M - Q|  and of the signal that is actually traded, -EMA20(T).

The tree has no day-axis operator: everything that makes it tradable is the EMA of the convention.  So the
structural questions can be asked in numpy on four base panels (D, M, Q, sigma = day_std(Ret)), at ONE fixed
half-life, which is the only clean way to separate "structure" from "smoothing":

  0  self-checks     T == D*|M-Q| ?  does the helper reproduce the S0 table row?
  B  what is S       sign of M-Q (is abs_ a no-op?), trigger counts, surge->drop adjacency, the closing-auction
                     bar, rank corr of S with plain intraday vol; does cutting the last bars change S?      (H1 H3 H13)
  C  what is T       swap each part for its naive equivalent, everything at half-life 20, sign fitted on train:
                     D alone / D*sigma / D*M / D*Q / D*(M-Q) / D*|D| / sign(D)*S / close-to-close*S / overnight*S /
                     positive part / negative part / magnitude only / scale-free versions                 (H1 H2 H3 H4 H5 H6 H10)
  D  half-life       the long book at half-lives 10..120, and cross_mean(T, d) followed by the EMA           (H9)
  E  profile         20-quantile excess of the traded signal and of its parts                                (H6 H10)
  F  legs            who is in each decile; how much of the short leg is names that could not be bought      (H6 H7)
  G  matched neutralisation  the traded signal against controls smoothed the same way                        (H8)
  H  known family    residual against / sum with cross_mean(day_std(Amt), 30); conditional sort inside it    (H11)
  I  by year

Only train / valid are read.
"""
import gc
import sys
import time
import warnings

import numpy as np

from partura.study_tools import Study, bk, dg

warnings.simplefilter("ignore", RuntimeWarning)
FID = "F110_ret_fair_log"
T0 = time.time()

LV = "log(Volume)"
G = f"sub({LV}, in_forward_valid_part({LV}))"
UP = f"is_gt({G}, add(in_mean_full({G}), in_stddev_full({G})))"
DN = f"is_lt({G}, sub(in_mean_full({G}), in_stddev_full({G})))"
UP_PREV = f"is_gt(in_delay({G}, 1), add(in_mean_full({G}), in_stddev_full({G})))"
EXPR = {
    "D": "div(sub(day_last(Close), day_first(Open)), day_first(Open))",
    "M": f"day_mean(in_sustain_stddev({UP}, Ret, 5))",
    "Q": f"day_mean(in_sustain_stddev({DN}, Ret, 5))",
    "fU": f"day_mean({UP})",                                   # share of the 241 minutes that fire SURGE
    "fL": f"day_mean({DN})",
    "fAdj": f"day_mean(mul({DN}, {UP_PREV}))",                  # share of minutes that are a DROP right after a SURGE
    "uLast": f"day_mean(in_slice({UP}, 240, 240))",            # does the closing-auction bar fire SURGE?
    "Mc": f"day_mean(in_sustain_stddev(in_slice({UP}, 0, 236), in_slice(Ret, 0, 236), 5))",   # last 4 bars cut off
    "Qc": f"day_mean(in_sustain_stddev(in_slice({DN}, 0, 236), in_slice(Ret, 0, 236), 5))",
}
HL = 20.0
# sections to run (default: all). A run that the memory guard aborts can be resumed with the remaining letters:
#   study.sh exec F110_ret_fair_log x1b x1_anatomy.py C D E      (section C is always computed: later ones need its signals)
SECTIONS = set(a.upper() for a in sys.argv[1:] if a.upper() in set("0BCDEFGHI")) or set("0BCDEFGHI")


def say(*a):
    print(*a, flush=True)


def f64(x):
    return np.asarray(x, dtype=np.float64)


def ema(x, hl=HL):
    return bk.smoothed(f64(x), hl)


def zr(x):
    return dg._zrank(f64(x))                       # uniform [-0.5, 0.5] within the day, NaN kept


def pct(x):
    return zr(x) + 0.5


def roll_mean(x, d):
    """cross_mean(x, d): causal nanmean over the last d days (NaN only if the whole window is NaN)."""
    fin = np.isfinite(x)
    cs = np.cumsum(np.where(fin, x, 0.0), axis=0)
    cn = np.cumsum(fin, axis=0).astype(np.float64)
    z = np.zeros((d, x.shape[1]))
    s = cs - np.vstack([z, cs[:-d]])
    n = cn - np.vstack([z, cn[:-d]])
    return np.where(n > 0, s / np.maximum(n, 1), np.nan)


def roll_max(x, d):
    out = np.full_like(x, -np.inf)
    for k in range(d):
        sh = x if k == 0 else np.vstack([np.full((k, x.shape[1]), np.nan), x[:-k]])
        out = np.fmax(out, np.where(np.isfinite(sh), sh, -np.inf))
    return np.where(np.isfinite(out), out, np.nan)


def ric(sm, tgt, s):
    return float(np.nanmean(dg.rank_ic_series(sm[s], tgt[s])))


def fmt(b):
    return (f"LS {b['ls_sharpe']:+5.2f} Lg {b['long_gross_ann']*100:+5.1f}% Ln {b['long_ann']*100:+5.1f}% "
            f"Lshp {b['long_sharpe']:+5.2f} sh {b['short_gross_ann']*100:+5.1f}% LTO {b['long_turnover']*100:4.1f}%")


# ---- tiny self-test of the numpy helpers on a known answer (runs everywhere, before any data is touched)
_x = np.array([[1.0], [np.nan], [3.0], [5.0], [np.nan], [np.nan], [np.nan]])
assert np.allclose(roll_mean(_x, 2)[[0, 1, 2, 3, 4]].ravel(), [1.0, 1.0, 3.0, 4.0, 5.0]) and np.isnan(roll_mean(_x, 2)[6, 0])
assert np.allclose(roll_max(_x, 3)[[0, 1, 2, 3, 4, 5]].ravel(), [1.0, 1.0, 3.0, 5.0, 5.0, 5.0]) and np.isnan(roll_max(_x, 2)[6, 0])
_e = bk.smoothed(np.array([[1.0], [0.0], [0.0]]), 1.0)          # half-life 1 -> weight 0.5 per day
assert np.allclose(_e.ravel(), [1.0, 0.5, 0.25])

with Study(FID) as st:
    P = st.panels({"T": st.cfg["expression"], **EXPR})
    missing = [k for k in ["T", *EXPR] if k not in P]
    say(f"panels ready {time.time() - T0:.0f}s; missing: {missing}")
    T = f64(P["T"]); D = f64(P["D"]); M = f64(P["M"]); Q = f64(P["Q"])
    sigma = f64(st.control("ctl_ivol"))
    rev1 = f64(st.control("ctl_rev1"))
    ctl = {k: f64(st.control(k)) for k in ("ctl_amt", "ctl_price", "ctl_ivol", "ctl_range", "ctl_rev1", "ctl_mom20",
                                           "ctl_dvol20", "ctl_cap", "ctl_turnrate")}
    known = {k: f64(st.control(k)) for k in ("known_stdamt_mean30", "known_stdamt_max9", "known_amt_max9", "known_ivol_max9")}
    tgt = f64(st.target())
    raw = f64(st.target(buyable=False))
    tr, va = st.slice("train"), st.slice("valid")
    SP = {"train": tr, "valid": va}
    years = np.array([int(str(d)[:4]) for d in st.dates])
    say(f"train {tr} valid {va}; days {T.shape[0]} names {T.shape[1]}; label NaN share buyable {np.isnan(tgt[tr]).mean():.4f} raw {np.isnan(raw[tr]).mean():.4f}")

    R = M - Q
    S = np.abs(R)
    sig = -ema(T)                                    # the traded signal (sign -1, half-life 20: fitted on train in S0)

    # ================================================================== 0 self-checks
    if "0" in SECTIONS:
        say("\n== 0 self-checks")
        T2 = D * S
        both = np.isfinite(T2) & np.isfinite(T)
        say(f"T vs D*|M-Q|: finite T {np.isfinite(T).mean():.4f} mine {np.isfinite(T2).mean():.4f} both {both.mean():.4f}; "
            f"max|diff| {np.nanmax(np.abs(T2 - T)[both]):.3e} (median |T| {np.nanmedian(np.abs(T[both])):.3e}); "
            f"rank corr {dg.pair_rank_corr(T2[tr], T[tr]):.5f}")
        for k, s in SP.items():
            say(f"  base hl20 [{k}] rIC {ric(sig, tgt, s):+.4f} {fmt(bk.book_row(sig, tgt, s))}   (S0 table: train LS +2.77 Lg +8.0% Ln -0.0%; valid LS +2.74 Lg +7.4% Ln -0.6%)")

    # ================================================================== B what is S
    if "B" in SECTIONS:
        say("\n== B anatomy of S = |M - Q| (train unless said)")
        fin = np.isfinite(R[tr])
        lab = np.isfinite(tgt[tr])
        say(f"S finite among labelled {(np.isfinite(S[tr]) & lab).sum() / lab.sum():.4f}; share S==0 {np.mean(S[tr][fin] == 0):.4f}; "
            f"share M<Q {np.mean(R[tr][fin] < 0):.4f} (valid {np.mean(R[va][np.isfinite(R[va])] < 0):.4f}); "
            f"share D>0 {np.mean(D[tr][np.isfinite(D[tr])] > 0):.4f} D==0 {np.mean(D[tr][np.isfinite(D[tr])] == 0):.4f}")
        rel = (R / (0.5 * (M + Q)))[tr]
        rel = rel[np.isfinite(rel)]
        say("(M-Q)/mean(M,Q) percentiles: " + " ".join(f"p{q}={np.percentile(rel, q):+.3f}" for q in (1, 5, 25, 50, 75, 95, 99)))
        if all(k in P for k in ("fU", "fL", "fAdj", "uLast")):
            nU, nL, nAdj, uLast = (f64(P[k]) * (241.0 if k != "uLast" else 1.0) for k in ("fU", "fL", "fAdj", "uLast"))
            a, b, c = nU[tr][fin], nL[tr][fin], nAdj[tr][fin]
            say("surge triggers / day: " + " ".join(f"p{q}={np.percentile(a, q):.0f}" for q in (1, 5, 25, 50, 75, 95, 99))
                + "   drop triggers / day: " + " ".join(f"p{q}={np.percentile(b, q):.0f}" for q in (1, 5, 25, 50, 75, 95, 99)))
            say(f"share of DROP triggers that come right after a SURGE trigger: {c.sum() / b.sum():.3f}; "
                f"share of stock-days whose closing-auction bar fires SURGE: {np.nanmean(uLast[tr][fin]):.3f} "
                f"(2018H1 {np.nanmean(uLast[tr][:120]):.3f}, 2021 {np.nanmean(uLast[tr][-240:]):.3f}; valid {np.nanmean(uLast[va]):.3f})")
        pairs = {"M~Q": (M, Q), "S~sigma": (S, sigma), "M~sigma": (M, sigma), "Q~sigma": (Q, sigma), "S~M": (S, M),
                 "R~sigma": (R, sigma), "S~|D|": (S, np.abs(D)), "sigma~|D|": (sigma, np.abs(D)), "S/sigma~sigma": (S / np.where(sigma > 0, sigma, np.nan), sigma),
                 "D~rev1": (D, rev1), "T~D": (T, D), "T~D*sigma": (T, D * sigma), "T~D*|D|": (T, D * np.abs(D))}
        say("daily cross-sectional rank corr: " + "  ".join(f"{k} {dg.pair_rank_corr(a[tr], b[tr]):+.3f}" for k, (a, b) in pairs.items()))
        if "Mc" in P and "Qc" in P:
            Rc = f64(P["Mc"]) - f64(P["Qc"])
            okc = np.isfinite(Rc[tr]) & fin
            say(f"last 4 bars cut off: share M<Q {np.mean(Rc[tr][okc] < 0):.4f} (uncut {np.mean(R[tr][okc] < 0):.4f}); "
                f"rank corr |Rc|~S {dg.pair_rank_corr(np.abs(Rc)[tr], S[tr]):+.3f}; Mc/M median {np.nanmedian((f64(P['Mc']) / M)[tr]):.3f}; "
                f"rank corr Mc~M {dg.pair_rank_corr(f64(P['Mc'])[tr], M[tr]):+.3f}")
    del P   # R1 fix C2: nothing after section B reads P (T/D/M/Q are already independent f64 copies); ~400MB back

    # ================================================================== C what is T: one half-life, swap the parts
    say(f"\n== C structure at ONE half-life ({HL:.0f}); sign fitted on train by the rank IC of the smoothed signal; corr = rank corr with the base traded signal (train)")
    Dcc = np.clip(rev1 - 1.0, -0.21, 0.21)                                  # close-to-close (unadjusted; ex-right days clipped)
    Don = np.clip(rev1 / (1.0 + D) - 1.0, -0.21, 0.21)                      # overnight: open / previous close - 1
    sg_ok = np.where(sigma > 0, sigma, np.nan)
    Srel = np.where(np.isfinite(S) & (sigma > 0), S / sg_ok, np.where(np.isfinite(S), 0.0, np.nan))
    Tp = np.where(np.isfinite(T), np.clip(T, 0, None), np.nan)
    Tn = np.where(np.isfinite(T), np.clip(T, None, 0), np.nan)
    cands = {
        "c0  D*S (base)": lambda: T,
        "c1  D": lambda: D,
        "c2  D*sigma": lambda: D * sigma,
        "c3  D*M": lambda: D * M,
        "c4  D*Q": lambda: D * Q,
        "c5  D*(M-Q) no abs": lambda: D * R,
        "c6  D*|D|": lambda: D * np.abs(D),
        "c7  sign(D)*S": lambda: np.sign(D) * S,
        "c8  D*(S/sigma)": lambda: D * Srel,
        "c9  zr(D)*pct(S)": lambda: zr(D) * pct(S),
        "c10 Dcc*S": lambda: Dcc * S,
        "c11 Don*S": lambda: Don * S,
        "c12 Dcc": lambda: Dcc,
        "c13 Don": lambda: Don,
        "c14 T+ (pos part)": lambda: Tp,
        "c15 T- (neg part)": lambda: Tn,
        "c16 |D|*S": lambda: np.abs(D) * S,
        "c17 S": lambda: S,
        "c18 sigma": lambda: sigma,
        "c19 D*sigma^2": lambda: D * sigma * sigma,
        "c20 D/sigma": lambda: np.where(sigma > 0, D / sg_ok, np.where(np.isfinite(D), 0.0, np.nan)),
    }
    KEEP = {"c1", "c2", "c6", "c8", "c14", "c15"}            # the signals later sections need
    NEED_SIG = bool(SECTIONS & set("EGHI"))                  # R1 fix C1: only these sections read SIG
    SIG = {}
    for name, mk in cands.items():
        key = name.split()[0]
        if "C" not in SECTIONS and (not NEED_SIG or key not in KEEP):
            continue
        e = ema(mk())
        sgn = -1.0 if np.nanmean(dg.rank_ic_series(e[tr], tgt[tr])) < 0 else 1.0
        sm = sgn * e
        del e
        if key in KEEP:
            SIG[key] = sm.astype(np.float32)
        if "C" in SECTIONS:
            say(f"  {name:<20} sgn {sgn:+.0f} corr {dg.pair_rank_corr(sm[tr], sig[tr]):+.3f} | "
                + " | ".join(f"{k[:2]}: rIC {ric(sm, tgt, s):+.4f} {fmt(bk.book_row(sm, tgt, s))}" for k, s in SP.items()))
        del sm
        gc.collect()

    # the identity EMA(D*S) = EMA(D)*EMA(S) + Cov_EMA(D, S): which piece carries it?
    if "C" in SECTIONS:
        eD0, eS0, eT0 = ema(D), ema(S), ema(T)
        for name, x in (("p1  EMA(D)*EMA(S)", eD0 * eS0), ("p2  EMA(DS)-EMA(D)EMA(S)", eT0 - eD0 * eS0)):
            sgn = -1.0 if np.nanmean(dg.rank_ic_series(x[tr], tgt[tr])) < 0 else 1.0
            sm = sgn * x
            say(f"  {name:<24} sgn {sgn:+.0f} corr {dg.pair_rank_corr(sm[tr], sig[tr]):+.3f} | "
                + " | ".join(f"{k[:2]}: rIC {ric(sm, tgt, s):+.4f} {fmt(bk.book_row(sm, tgt, s))}" for k, s in SP.items()))
        del eD0, eS0, eT0

        say("\n== C2 lag profile of the RAW daily panels (no smoothing): -x[t-k] against the label; rIC, long-decile gross, short-decile gross (train | valid)")
        def lagged(x, k):
            return x if k == 0 else np.vstack([np.full((k, x.shape[1]), np.nan), x[:-k]])
        for nm, x in (("T", T), ("D", D), ("T-", Tn), ("T+", Tp)):
            for k_ in (0, 1, 2, 3, 5, 10, 20, 30, 40, 60, 90):
                sm = -lagged(x, k_)
                out = []
                for k, s in SP.items():
                    b = bk.book_row(sm, tgt, s)
                    out.append(f"{k[:2]}: rIC {ric(sm, tgt, s):+.4f} Lg {b['long_gross_ann']*100:+5.1f}% sh {b['short_gross_ann']*100:+5.1f}%")
                say(f"  -{nm:<3} lag {k_:>2} | " + " | ".join(out))

    # ================================================================== D half-life
    if "D" in SECTIONS:
        say("\n== D half-life extension (sign fixed from C); each row: half-life -> train | valid")
        for key in ("c0", "c1", "c2"):
            x = {"c0": T, "c1": D, "c2": D * sigma}[key]
            for hl in (5, 10, 20, 30, 40, 60, 90, 120):
                sm = -ema(x, hl)
                say(f"  {key} hl {hl:>3} | " + " | ".join(f"{k[:2]}: rIC {ric(sm, tgt, s):+.4f} {fmt(bk.book_row(sm, tgt, s))}" for k, s in SP.items()))
        say("   cross_mean(T, d) then EMA (what an in-expression smoother would give; half-life from the grid):")
        for d in (10, 20, 30, 60):
            rm = roll_mean(T, d)
            for hl in (0, 5, 10, 20):
                sm = -ema(rm, hl) if hl else -rm
                say(f"  cross_mean(T,{d:>2}) hl {hl:>2} corr {dg.pair_rank_corr(sm[tr], sig[tr]):+.3f} | "
                    + " | ".join(f"{k[:2]}: rIC {ric(sm, tgt, s):+.4f} {fmt(bk.book_row(sm, tgt, s))}" for k, s in SP.items()))
        for d in (20, 60):
            rm = roll_mean(D, d)
            for hl in (0, 10, 20):
                sm = -ema(rm, hl) if hl else -rm
                say(f"  cross_mean(D,{d:>2}) hl {hl:>2} corr {dg.pair_rank_corr(sm[tr], sig[tr]):+.3f} | "
                    + " | ".join(f"{k[:2]}: rIC {ric(sm, tgt, s):+.4f} {fmt(bk.book_row(sm, tgt, s))}" for k, s in SP.items()))
        say("   20-day rolling max / min of T and of D (the MAX-effect reading), at half-life 0 and 5:")
        for nm, x in (("-max20(T)", -roll_max(T, 20)), ("-max20(D)", -roll_max(D, 20)), ("+max20(-T)", roll_max(-T, 20)), ("+max20(-D)", roll_max(-D, 20))):
            for hl in (0, 5):
                sm = ema(x, hl) if hl else x
                say(f"  {nm:<11} hl {hl} corr {dg.pair_rank_corr(sm[tr], sig[tr]):+.3f} | "
                    + " | ".join(f"{k[:2]}: rIC {ric(sm, tgt, s):+.4f} {fmt(bk.book_row(sm, tgt, s))}" for k, s in SP.items()))

    # ================================================================== E profiles
    if "E" in SECTIONS:
        say("\n== E annualised excess (%) by 20 quantiles of the traded signal, short end -> long end")
        for nm, sm in (("base -EMA20(T)", sig), ("c1 -EMA20(D)", SIG["c1"]), ("c14 T+ only", SIG["c14"]), ("c15 T- only", SIG["c15"]),
                       ("c2 -EMA20(D*sigma)", SIG["c2"]), ("c8 D*(S/sigma)", SIG["c8"]), ("base hl60", -ema(T, 60)), ("c1 D hl60", -ema(D, 60))):
            for k, s in SP.items():
                q = bk.quantile_profile(sm, tgt, s, n=20)
                say(f"  {nm:<20} {k[:2]}: " + " ".join(f"{r['excess_ann']*100:+.0f}" for r in q))

    # ================================================================== F legs
    if "F" in SECTIONS:
        say("\n== F who is in the deciles of the base traded signal")
        eD, eS, eT = ema(D), ema(S), ema(T)
        feats = {"cap": pct(ctl["ctl_cap"]), "amt": pct(ctl["ctl_amt"]), "turn": pct(ctl["ctl_turnrate"]), "dvol20": pct(ctl["ctl_dvol20"]),
                 "ivol": pct(ctl["ctl_ivol"]), "mom20": pct(ctl["ctl_mom20"]), "price": pct(ctl["ctl_price"]),
                 "stdamt30": pct(known["known_stdamt_mean30"]), "EMA_D": pct(eD), "EMA_S": pct(eS)}
        for k, s in SP.items():
            sg = sig[s]
            r = dg.rank_rows(np.where(np.isfinite(sg) , sg, np.nan))
            n = np.isfinite(r).sum(1, keepdims=True)
            dec = np.minimum(np.floor((r - 1.0) / np.maximum(n, 1) * 10), 9)
            for dname, dsel in (("short Q1", dec == 0), ("Q2", dec == 1), ("Q5-6", (dec == 4) | (dec == 5)), ("Q9", dec == 8), ("long Q10", dec == 9)):
                desc = " ".join(f"{fk} {np.nanmean(fv[s][dsel]):.2f}" for fk, fv in feats.items())
                say(f"  [{k[:2]}] {dname:<9} labelNaN {np.mean(~np.isfinite(tgt[s][dsel])):.4f} EMA(T)<0 {np.mean(eT[s][dsel] < 0):.3f} "
                    f"EMA(D) bp/day {np.nanmean(eD[s][dsel])*1e4:+.1f} | mean pctile: {desc}")
            b0, b1 = bk.book_row(sig, tgt, s), bk.book_row(sig, raw, s)
            say(f"  [{k[:2]}] label WITH the cannot-buy filter: {fmt(b0)}")
            say(f"  [{k[:2]}] label WITHOUT it (raw)        : {fmt(b1)}")
            short = dec == 0
            nb = short & ~np.isfinite(tgt[s]) & np.isfinite(raw[s])
            say(f"  [{k[:2]}] short decile: {nb.sum() / max(short.sum(), 1):.4f} of name-days are unbuyable-next-open; their mean raw label {np.nanmean(raw[s][nb])*1e4:+.1f} bp "
                f"vs the buyable shorts {np.nanmean(tgt[s][short & np.isfinite(tgt[s])])*1e4:+.1f} bp vs universe {np.nanmean(tgt[s])*1e4:+.1f} bp")

    # R2: the long-only candidates from R1's D section (roll_mean is the numpy twin of cross_mean)
    CM20 = -ema(roll_mean(D, 20), 20)
    CMT20 = -ema(roll_mean(T, 20), 20)
    CM20L = -ema(roll_mean(np.vstack([np.full((10, D.shape[1]), np.nan), D[:-10]]), 20), 20)
    SIG["cm20"] = CM20.astype(np.float32)

    # ================================================================== G matched neutralisation
    if "G" in SECTIONS:
        say("\n== G rank-space neutralisation of the base traded signal (daily cross-sectional OLS; residual is not re-smoothed)")
        matched = {"mEMA_D": -ema(D), "mEMA_Dsig": -ema(D * sigma), "mEMA_sigma": -ema(sigma), "mEMA_absT": -ema(np.abs(T)),
                   "mEMA_Dcc": -ema(Dcc), "mEMA_Don": -ema(Don)}
        sets = {
            "9 controls (S0: R2 0.349)": dict(ctl),
            "EMA20(D)": {"a": matched["mEMA_D"]},
            "EMA20(Dcc)": {"a": matched["mEMA_Dcc"]},
            "EMA20(D), EMA20(sigma), EMA20(|T|)": {"a": matched["mEMA_D"], "b": matched["mEMA_sigma"], "c": matched["mEMA_absT"]},
            "9 controls + EMA20(D) + EMA20(sigma) + EMA20(|T|)": {**ctl, "a": matched["mEMA_D"], "b": matched["mEMA_sigma"], "c": matched["mEMA_absT"]},
            "known_stdamt_mean30": {"a": known["known_stdamt_mean30"]},
            "EMA20(cross_mean(D,20))": {"a": CM20},
            "ctl_mom20 alone": {"a": ctl["ctl_mom20"]},
        }
        for k, s in SP.items():
            n = s.stop - s.start
            b = bk.book_row(sig[s], tgt[s], slice(0, n))
            say(f"  [{k[:2]}] (un-neutralised)  rIC {ric(sig, tgt, s):+.4f} Lg {b['long_gross_ann']*100:+5.1f}% short {b['short_gross_ann']*100:+5.1f}% LSgross {b['ls_gross_sharpe']:+.2f}")
            for nm, cs in sets.items():
                resid, info = dg.neutralise(sig[s], {a: c[s] for a, c in cs.items()})
                b = bk.book_row(resid, tgt[s], slice(0, n))
                say(f"  [{k[:2]}] {nm:<52} R2 {info['mean_r2']:.3f} resid rIC {np.nanmean(dg.rank_ic_series(resid, tgt[s])):+.4f} "
                    f"Lg {b['long_gross_ann']*100:+5.1f}% short {b['short_gross_ann']*100:+5.1f}% LSgross {b['ls_gross_sharpe']:+.2f} LTO {b['long_turnover']*100:4.1f}%")
        # who subsumes whom between the base and the two simplest rewrites
        for nm, key in (("c1 -EMA20(D)", "c1"), ("c2 -EMA20(D*sigma)", "c2"), ("c6 -EMA20(D*|D|)", "c6"), ("cm20 cross_mean(D,20)+EMA20", "cm20")):
            for k, s in SP.items():
                n = s.stop - s.start
                r1, i1 = dg.neutralise(sig[s], {"a": SIG[key][s]})
                r2, i2 = dg.neutralise(SIG[key][s], {"a": sig[s]})
                b1, b2 = bk.book_row(r1, tgt[s], slice(0, n)), bk.book_row(r2, tgt[s], slice(0, n))
                say(f"  [{k[:2]}] base | {nm:<20} R2 {i1['mean_r2']:.3f} resid rIC {np.nanmean(dg.rank_ic_series(r1, tgt[s])):+.4f} Lg {b1['long_gross_ann']*100:+5.1f}% short {b1['short_gross_ann']*100:+5.1f}%"
                    f"   ||   {nm} | base: resid rIC {np.nanmean(dg.rank_ic_series(r2, tgt[s])):+.4f} Lg {b2['long_gross_ann']*100:+5.1f}% short {b2['short_gross_ann']*100:+5.1f}%")

    # ================================================================== H known family, for a long-only user
    kn = -known["known_stdamt_mean30"]                       # S0: sign -, long half-life 0
    kn9 = -ema(known["known_stdamt_max9"], 5)                # S0: sign -, long half-life 5
    zk = zr(kn)
    if "H" in SECTIONS:
        say("\n== H increment over the known Amt-level family (long-only view)")
        for k, s in SP.items():
            say(f"  [{k[:2]}] known mean30 alone: rIC {ric(kn, tgt, s):+.4f} {fmt(bk.book_row(kn, tgt, s))}   (S0: Ln +12.6% / +22.3%, Lshp +1.78 / +3.46)")
            say(f"  [{k[:2]}] known max9  alone: rIC {ric(kn9, tgt, s):+.4f} {fmt(bk.book_row(kn9, tgt, s))}")
        partners = {"base hl20": sig, "base hl60": -ema(T, 60), "c1 D hl20": SIG["c1"], "c1 D hl60": -ema(D, 60),
                    "c2 D*sigma hl20": SIG["c2"], "c14 T+ hl20": SIG["c14"], "c15 T- hl20": SIG["c15"],
                    "cm20 cmD20+EMA20": CM20, "cmT20 cmT20+EMA20": CMT20, "cm20lag10 cmD20lag10+EMA20": CM20L}
        for nm, p in partners.items():
            zp = zr(p)
            say(f"  -- partner {nm}: rank corr with known mean30 {dg.pair_rank_corr(p[tr], kn[tr]):+.3f}")
            for w in (0.25, 0.5, 1.0):
                combo = zk + w * zp
                say(f"     known + {w:.2f} x partner | " + " | ".join(f"{k[:2]}: rIC {ric(combo, tgt, s):+.4f} {fmt(bk.book_row(combo, tgt, s))}" for k, s in SP.items()))
            for k, s in SP.items():
                n = s.stop - s.start
                r1, i1 = dg.neutralise(p[s], {"a": kn[s]})
                b1 = bk.book_row(r1, tgt[s], slice(0, n))
                say(f"     [{k[:2]}] partner | known: R2 {i1['mean_r2']:.3f} resid rIC {np.nanmean(dg.rank_ic_series(r1, tgt[s])):+.4f} Lg {b1['long_gross_ann']*100:+5.1f}% short {b1['short_gross_ann']*100:+5.1f}% LTO {b1['long_turnover']*100:4.1f}%")
        for k, s in SP.items():
            top_b, top_k = pct(sig)[s] >= 0.9, pct(kn)[s] >= 0.9
            say(f"  [{k[:2]}] overlap of the long deciles: {(top_b & top_k).sum() / max(top_b.sum(), 1):.3f} of base's long decile is in known mean30's long decile (random 0.10); "
                f"{(top_b & (pct(kn)[s] >= 0.7)).sum() / max(top_b.sum(), 1):.3f} is in its top 30%; "
                f"short deciles: {((pct(sig)[s] < 0.1) & (pct(kn)[s] < 0.1)).sum() / max((pct(sig)[s] < 0.1).sum(), 1):.3f}")
        say("  conditional sort: inside the known family's top 30% (its long pool), terciles of the base signal (low -> high), mean excess vs the universe, %/yr")
        for k, s in SP.items():
            pk, ps = pct(kn)[s], sig[s]
            pool = pk >= 0.7
            ok = np.isfinite(tgt[s]) & np.isfinite(ps)
            ew = np.nansum(np.where(ok, tgt[s], 0.0), 1) / np.maximum(ok.sum(1), 1)
            ex = tgt[s] - ew[:, None]
            pin = dg._zrank(np.where(pool & ok, ps, np.nan)) + 0.5
            row = []
            for a, b in ((0, 1 / 3), (1 / 3, 2 / 3), (2 / 3, 1.01)):
                m = (pin >= a) & (pin < b)
                row.append(f"{np.nanmean(np.nansum(np.where(m, ex, 0.0), 1) / np.maximum(m.sum(1), 1)) * 252 * 100:+.1f}")
            m = pool & ok
            say(f"  [{k[:2]}] pool {np.nanmean(np.nansum(np.where(m, ex, 0.0), 1) / np.maximum(m.sum(1), 1)) * 252 * 100:+.1f} | terciles of base signal inside the pool: " + " / ".join(row))

    # ================================================================== I by year
    if "I" in SECTIONS:
        say("\n== I by year (each year starts from an empty book; signs / half-lives as above)")
        stop = va.stop
        rows = {"base hl20": sig, "base hl60": -ema(T, 60), "c1 D hl20": SIG["c1"], "c2 D*sig hl20": SIG["c2"], "known mean30": kn,
                "known+0.5base": zk + 0.5 * zr(sig), "cm20 cmD20+EMA20": CM20, "known+0.5cm20": zk + 0.5 * zr(CM20)}
        for y in sorted(set(years[:stop].tolist())):
            idx = np.nonzero(years[:stop] == y)[0]
            if idx.size < 20:
                continue
            sl = slice(int(idx[0]), int(idx[-1]) + 1)
            out = []
            for nm, p in rows.items():
                b = bk.book_row(p, tgt, sl)
                out.append(f"{nm}: LS {b['ls_sharpe']:+.2f} Ln {b['long_ann']*100:+.1f}% Lshp {b['long_sharpe']:+.2f}")
            say(f"  {y} ({idx.size}d) " + " | ".join(out))
    say(f"\ndone {time.time() - T0:.0f}s")
