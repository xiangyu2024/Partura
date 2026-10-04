"""F105: what orders the root, and which kind of stock-day earns the money.

The root is  D = ts_stddev(C, 5),  C = cross_fangzheng(B, 241),  B = cross_max(A, 3),  A = day_cov(Amt, Amt).
The probes say D is "how much a one-year level statistic moved in the last 5 days", that it cannot tell a
spike ENTERING the window from the same spike LEAVING it 241 days later, and that an unfilled window
(a stock with < 241 observations) mechanically inflates the move.  No stock diagnostic separates those,
so this script measures them directly on train / valid (never the holdout):

  1  tails        how heavy-tailed is A through time, and how much of C is the std term / the single largest day
  2  ordering     what the cross-sectional order of D follows: level C, relative change D/C, amount, known family
  3  anatomy      the short and the long decile split by event kind: entry / exit(echo) / IPO-young / sample-start
  4  ic by kind   rank IC of -D inside each kind
  5  drop-one     the book at hl=3 with one kind of stock-day removed from the universe
  6  subsumption  the traded signal neutralised on the known family (and the reverse)
  7  long leg     overlap of the long decile with the lowest decile of amount / known family / level C
  8  two-way      conditional IC: relative change inside level buckets, level inside relative-change buckets
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F105_std_fangzheng_covamt"
A = "day_cov(Amt, Amt)"
B = f"cross_max({A}, 3)"
C = f"cross_fangzheng({B}, 241)"
D = f"ts_stddev({C}, 5)"
HL = 3.0
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def q3(x):
    x = x[np.isfinite(x)]
    return "n/a" if x.size == 0 else "p10 %.3g  p25 %.3g  p50 %.3g  p75 %.3g  p90 %.3g" % tuple(np.percentile(x, [10, 25, 50, 75, 90]))


def pct(x):
    return dg._zrank(x) + 0.5          # daily percentile in [0, 1], NaN preserved


def deciles(sig, tgt):
    ok = np.isfinite(sig) & np.isfinite(tgt)
    r = dg.rank_rows(np.where(ok, sig, np.nan))
    n = ok.sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        q = np.minimum(np.floor((r - 1.0) / np.maximum(n, 1) * 10), 9)
    return np.where(ok, q, np.nan), ok


def anatomy(sig, tgt, groups, amt_pct, sl, label):
    s, t = sig[sl], tgt[sl]
    q, ok = deciles(s, t)
    r = np.where(ok, t, 0.0)
    n = ok.sum(1)
    ew = r.sum(1) / np.maximum(n, 1)
    ex = np.where(ok, t - ew[:, None], 0.0)
    for k, name in ((0, "SHORT decile (highest D)"), (9, "LONG decile (lowest D)")):
        dec = (q == k)
        nd = dec.sum(1)
        tot = ((ex * dec).sum(1) / np.maximum(nd, 1)).mean() * 252
        say(f"  [{label}] {name}: decile excess {tot:+.1%}/yr")
        for g, mask in groups.items():
            m = dec & mask[sl]
            share = m.sum() / max(dec.sum(), 1)
            base = (ok & mask[sl]).sum() / max(ok.sum(), 1)
            cnt = m.sum(1)
            contrib = ((ex * m).sum(1) / np.maximum(nd, 1)).mean() * 252
            days = cnt >= 5
            mean_ex = ((ex * m).sum(1)[days] / cnt[days]).mean() * 252 if days.any() else float("nan")
            with np.errstate(invalid="ignore"):
                amt = np.nanmean(np.where(m, amt_pct[sl], np.nan)) if m.any() else float("nan")
            say(f"      {g:<12} share of decile {share:6.1%} (of universe {base:6.1%})   mean excess {mean_ex:+7.1%}/yr"
                f"   contribution {contrib:+6.1%}/yr   mean amt pctile {amt:.2f}")


def book(panel, tgt, sl, hl=HL):
    """Both books at a fixed half-life, sign -1 (fitted on train for the original)."""
    sm = bk.smoothed(-np.asarray(panel, dtype=np.float64), hl)
    return bk.book_row(sm, tgt, sl)


def fmt_book(b):
    return (f"LS {b['ls_sharpe']:+.2f} (gross {b['ls_gross_sharpe']:+.2f})  long gross {b['long_gross_ann']:+.1%} net {b['long_ann']:+.1%}"
            f" sharpe {b['long_sharpe']:+.2f}  short {b['short_gross_ann']:+.1%}  TO {b['ls_turnover']:.1%}")


with Study(FID) as st:
    P = st.panels({"A": A, "B": B, "C": C, "D": D,
                   "Cmean": f"cross_mean({B}, 241)", "Cstd": f"cross_stddev({B}, 241)",
                   "Cmax": f"cross_max({B}, 241)", "Cmed": f"cross_med({B}, 241)"})
    a, c, d = (np.asarray(P[k], dtype=np.float64) for k in ("A", "C", "D"))
    cmean, cstd, cmax, cmed = (np.asarray(P[k], dtype=np.float64) for k in ("Cmean", "Cstd", "Cmax", "Cmed"))
    tgt = st.target()
    tr, va = st.slice("train"), st.slice("valid")
    amt = st.control("ctl_amt")
    cap = st.control("ctl_cap")
    turn = st.control("ctl_turnrate")
    known = np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)
    amt_pct = pct(amt)
    say(f"panels ready {time.time() - T0:.0f}s; days {a.shape[0]}, symbols {a.shape[1]}; train {tr}, valid {va}")

    # ------------------------------------------------------------------ 1 tails
    say("\n== 1 tails (train) ==")
    la = np.log(np.where(a[tr] > 0, a[tr], np.nan))
    nobs = np.isfinite(la).sum(0)
    with np.errstate(invalid="ignore"):
        sig_log = np.where(nobs >= 250, np.nanstd(la, axis=0), np.nan)
    say("  per-stock time-series std of log(day_cov(Amt,Amt)) [stocks with >=250 obs]:", q3(sig_log))
    n_cum = np.cumsum(np.isfinite(a), axis=0)
    mature = n_cum >= 247
    mt = mature[tr]
    with np.errstate(invalid="ignore", divide="ignore"):
        say("  std term share  Cstd / C            [mature stock-days]:", q3((cstd[tr] / c[tr])[mt][::37]))
        say("  largest value / window sum  Cmax/(241*Cmean)         :", q3((cmax[tr] / (241 * cmean[tr]))[mt][::37]))
        say("  yearly max over yearly median  Cmax / Cmed           :", q3((cmax[tr] / cmed[tr])[mt][::37]))
        rel_lvl = {"C/Cmed": c / cmed, "Cmax/Cmed": cmax / cmed, "Cmean/Cmed": cmean / cmed}
    say("  daily Spearman, raw:        C~Cmax %.3f   C~Cmean %.3f   C~Cmed %.3f" % (
        st.rank_corr(c, cmax), st.rank_corr(c, cmean), st.rank_corr(c, cmed)))
    say("  daily Spearman, scale-free: C/Cmed~Cmax/Cmed %.3f   C/Cmed~Cmean/Cmed %.3f" % (
        st.rank_corr(rel_lvl["C/Cmed"], rel_lvl["Cmax/Cmed"]), st.rank_corr(rel_lvl["C/Cmed"], rel_lvl["Cmean/Cmed"])))

    # ------------------------------------------------------------------ 2 ordering
    say("\n== 2 what the cross-sectional order of D follows (daily Spearman, train) ==")
    with np.errstate(invalid="ignore", divide="ignore"):
        rel = np.where(c > 0, d / c, np.nan)
    dc = np.full_like(c, np.nan)
    dc[4:] = c[4:] - c[:-4]
    for name, x in (("level C", c), ("relative change D/C", rel), ("|C_t - C_t-4|", np.abs(dc)), ("ctl_amt", amt),
                    ("ctl_cap", cap), ("ctl_turnrate", turn), ("known_stdamt_max9", known), ("today's A", a)):
        say(f"  D ~ {name:<22} {st.rank_corr(d, x):+.3f}")
    say(f"  relative change ~ level C     {st.rank_corr(rel, c):+.3f}")
    say(f"  relative change ~ ctl_amt     {st.rank_corr(rel, amt):+.3f}")
    say(f"  level C ~ ctl_amt             {st.rank_corr(c, amt):+.3f}")
    say(f"  level C ~ known_stdamt_max9   {st.rank_corr(c, known):+.3f}")

    # ------------------------------------------------------------------ 3 anatomy
    listed0 = np.isfinite(a[:5]).any(0)[None, :]
    fin = np.isfinite(d)
    signed = np.sign(dc) * d
    es = bk.smoothed(signed, HL)
    groups_raw = {"entry(C up)": mature & (dc > 0), "exit(C down)": mature & (dc < 0),
                  "ipo-young": ~mature & ~listed0 & fin, "sample-start": ~mature & listed0 & fin}
    groups_sm = {"entry(C up)": mature & (es > 0), "exit(C down)": mature & (es < 0),
                 "ipo-young": ~mature & ~listed0 & fin, "sample-start": ~mature & listed0 & fin}
    say("\n== 3 anatomy of the two deciles, raw D (hl=0), groups by sign(C_t - C_t-4) ==")
    for name, sl in (("train", tr), ("valid", va)):
        anatomy(-d, tgt, groups_raw, amt_pct, sl, name)
    say("\n== 3b anatomy, traded signal (hl=3), groups by sign of EMA(sign(dC)*D) ==")
    sm = bk.smoothed(-d, HL)
    for name, sl in (("train", tr), ("valid", va)):
        anatomy(sm, tgt, groups_sm, amt_pct, sl, name)

    # ------------------------------------------------------------------ 4 IC by kind
    say("\n== 4 rank IC of -D inside each kind of stock-day (raw panel) ==")
    for name, sl in (("train", tr), ("valid", va)):
        row = []
        for g, mask in {"all": fin, **groups_raw}.items():
            m = mask[sl]
            ric = dg.rank_ic_series(np.where(m, -d[sl], np.nan), np.where(m, tgt[sl], np.nan))
            row.append(f"{g} {np.nanmean(ric):+.4f} (names/day {m.sum(1).mean():.0f})")
        say(f"  [{name}] " + "   ".join(row))

    # ------------------------------------------------------------------ 5 drop-one
    say("\n== 5 the book at hl=3, sign -1, with one kind of stock-day removed from the universe ==")
    say("   (removing names changes the universe day by day, so turnover/net are inflated; read gross + legs)")
    variants = {"all": d,
                "drop exit": np.where(groups_raw["exit(C down)"], np.nan, d),
                "drop entry": np.where(groups_raw["entry(C up)"], np.nan, d),
                "drop ipo-young": np.where(groups_raw["ipo-young"], np.nan, d),
                "mature only": np.where(mature, d, np.nan)}
    for name, sl in (("train", tr), ("valid", va)):
        for k, p in variants.items():
            say(f"  [{name}] {k:<15} {fmt_book(book(p, tgt, sl))}")

    # ------------------------------------------------------------------ 6 subsumption
    say("\n== 6 subsumption (train): traded signal of the original vs the known family ==")
    sig_tr = sm[tr]
    kn_sig = -known[tr]
    n_tr = sig_tr.shape[0]
    ctl_sets = {"known_stdamt_max9": {"k": kn_sig},
                "level C": {"c": -c[tr]},
                "ctl_amt": {"a": -np.asarray(amt[tr], dtype=np.float64)},
                "known + level C": {"k": kn_sig, "c": -c[tr]},
                "known + level C + ctl_amt": {"k": kn_sig, "c": -c[tr], "a": -np.asarray(amt[tr], dtype=np.float64)}}
    base_ic = dg.ic_row(sig_tr, tgt[tr], sign=1.0)["rank_ic"]
    say(f"  original traded signal: rank IC {base_ic:+.4f}   {fmt_book(bk.book_row(sig_tr, tgt[tr], slice(0, n_tr)))}")
    for name, ctl in ctl_sets.items():
        resid, info = dg.neutralise(sig_tr, ctl)
        b = bk.book_row(resid, tgt[tr], slice(0, n_tr))
        say(f"  original | {name:<26} R2 {info['mean_r2']:.3f}  resid rank IC {dg.ic_row(resid, tgt[tr], sign=1.0)['rank_ic']:+.4f}"
            f"  LSgross {b['ls_gross_sharpe']:+.2f}  long gross {b['long_gross_ann']:+.1%}  short {b['short_gross_ann']:+.1%}  TO {b['ls_turnover']:.1%}")
    k_ic = dg.ic_row(kn_sig, tgt[tr], sign=1.0)["rank_ic"]
    say(f"  known_stdamt_max9 itself: rank IC {k_ic:+.4f}   {fmt_book(bk.book_row(kn_sig, tgt[tr], slice(0, n_tr)))}")
    for name, ctl in {"original": {"o": sig_tr}, "level C": {"c": -c[tr]}}.items():
        resid, info = dg.neutralise(kn_sig, ctl)
        b = bk.book_row(resid, tgt[tr], slice(0, n_tr))
        say(f"  known | {name:<29} R2 {info['mean_r2']:.3f}  resid rank IC {dg.ic_row(resid, tgt[tr], sign=1.0)['rank_ic']:+.4f}"
            f"  LSgross {b['ls_gross_sharpe']:+.2f}  long gross {b['long_gross_ann']:+.1%}  short {b['short_gross_ann']:+.1%}  TO {b['ls_turnover']:.1%}")

    # ------------------------------------------------------------------ 7 long leg
    say("\n== 7 the long decile (lowest smoothed D): who is in it ==")
    for name, sl in (("train", tr), ("valid", va)):
        q, ok = deciles(sm[sl], tgt[sl])
        lng = (q == 9)
        row = []
        for k, x in (("ctl_amt", amt), ("known_stdamt_max9", known), ("level C", c), ("ctl_cap", cap)):
            qx, _ = deciles(-np.where(ok, np.asarray(x[sl], dtype=np.float64), np.nan), tgt[sl])
            row.append(f"{k} lowest-decile overlap {(lng & (qx == 9)).sum() / max(lng.sum(), 1):.1%}")
        say(f"  [{name}] " + "   ".join(row))
        with np.errstate(invalid="ignore"):
            say(f"  [{name}] mean percentile inside the long decile: amt {np.nanmean(np.where(lng, amt_pct[sl], np.nan)):.3f}"
                f"  cap {np.nanmean(np.where(lng, pct(cap)[sl], np.nan)):.3f}  turnrate {np.nanmean(np.where(lng, pct(turn)[sl], np.nan)):.3f}"
                f"  level C {np.nanmean(np.where(lng, pct(c)[sl], np.nan)):.3f}  rel change {np.nanmean(np.where(lng, pct(rel)[sl], np.nan)):.3f}"
                f"  ipo-young share {(lng & groups_raw['ipo-young'][sl]).sum() / max(lng.sum(), 1):.1%}")

    # ------------------------------------------------------------------ 8 two-way
    say("\n== 8 conditional rank IC (train, raw panels; sign as measured) ==")
    for name, x, g in (("relative change | level C", rel, c), ("level C | relative change", c, rel),
                       ("D | known_stdamt_max9", d, known), ("known_stdamt_max9 | D", known, d),
                       ("relative change | ctl_amt", rel, amt)):
        rows = dg.conditional_ic(x[tr], tgt[tr], np.asarray(g[tr], dtype=np.float64), buckets=5)
        say(f"  {name:<28} " + "  ".join(f"Q{r['bucket'] + 1} {r['rank_ic']:+.4f}" for r in rows))
    for name, x in (("level C", c), ("relative change D/C", rel), ("D", d), ("known_stdamt_max9", known)):
        say(f"  unconditional {name:<22} train {np.nanmean(dg.rank_ic_series(x[tr], tgt[tr])):+.4f}"
            f"   valid {np.nanmean(dg.rank_ic_series(x[va], tgt[va])):+.4f}")
    say(f"\ndone {time.time() - T0:.0f}s")
