"""x3 -- what S3 left open about the long-memory candidates (train/valid only, never the holdout).

S3: cross_max(K^2, 60) doubles the long leg's net excess (train/valid +11.3%/+10.1% vs +4.9%/+4.5%) and its long leg
survives the nine controls (residual gross +11.1%), while its short leg does not (+2.3%).  Before it can be a
candidate, five things have to be looked at directly:

  1  H18: cross_max skips missing days.  A name with only a few valid days in the 60-day window (new listing,
     resumption after a suspension) has a small max by construction.  Are such names in the long leg, and is the
     long leg's excess theirs?
  2  who sits in each decile of the 60-day max (lock events in 60d, activity, K level / dispersion), next to the original
  3  is the long leg anything beyond "no lock day in 60 days and a full history"?  -> the factor INSIDE the event-free,
     full-history universe
  4  S3 showed level-only (a_level15) holds in train and collapses in valid, dispersion-only (a_disp15) the other way
     round.  Year by year: which of the two carries the rank IC, and what does the per-day fold do?
  5  long-only practicalities: breadth (top 5% / 10% / 20%), the long book's own turnover, where the long leg sits in
     turnover-rate / size quintiles (double sort), and whether "fast event + slow state" as a rank sum beats either.
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F102_kurt_autocorr"
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def roll(x, d, how):
    x = np.asarray(x, dtype=np.float32)
    D = x.shape[0]
    acc = None
    cnt = np.zeros(x.shape, dtype=np.int16)
    sq = None
    for k in range(d):
        sh = np.full_like(x, np.nan)
        sh[k:] = x[:D - k]
        fin = np.isfinite(sh)
        cnt += fin
        if how in ("sum", "mean", "count", "std"):
            z = np.where(fin, sh, 0.0)
            acc = z if acc is None else acc + z
            if how == "std":
                sq = z * z if sq is None else sq + z * z
        elif how == "max":
            acc = sh if acc is None else np.fmax(acc, sh)
        elif how == "min":
            acc = sh if acc is None else np.fmin(acc, sh)
    if how == "count":
        return cnt.astype(np.float32)
    if how == "sum":
        return np.where(cnt > 0, acc, np.nan)
    if how == "mean":
        return np.where(cnt > 0, acc / np.maximum(cnt, 1), np.nan)
    if how == "std":
        m = acc / np.maximum(cnt, 1)
        v = sq / np.maximum(cnt, 1) - m * m
        return np.where(cnt > 1, np.sqrt(np.maximum(v, 0.0)), np.nan)
    return acc


def decile_of(panel, ok, n=10):
    p = np.where(ok, panel, np.nan).astype(np.float64)
    r = dg.rank_rows(p)
    cnt = np.isfinite(r).sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        return np.floor((r - 1.0) / np.maximum(cnt, 1) * n)


def pct_rank(x):
    r = dg.rank_rows(np.asarray(x, dtype=np.float64))
    cnt = np.isfinite(r).sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        return (r - 0.5) / np.maximum(cnt, 1)


A = "nt_ts_autocorr_s1(Ret, 3)"
EXPR = {
    "F": f"cross_sum(pow_2(day_kurt({A})), 15)",
    "K": f"day_kurt({A})",
    "Z": f"day_mean(abs_(sign({A})))",
    "W": "day_mean(abs_(sign(Ret)))",
    "athi": "day_mean(eq(Close, in_max(High)))",
    "atlo": "day_mean(eq(Close, in_min(Low)))",
    "M60e": f"cross_max(pow_2(day_kurt({A})), 60)",
}

with Study(FID) as st:
    P = st.panels(EXPR)
    say("missing panels:", [k for k in EXPR if k not in P])
    F = np.asarray(P["F"], dtype=np.float32)
    K = np.asarray(P["K"], dtype=np.float64)
    Z, W = np.asarray(P["Z"], dtype=np.float32), np.asarray(P["W"], dtype=np.float32)
    ctl = {n: np.asarray(st.control(n), dtype=np.float32)
           for n in ("ctl_rev1", "ctl_amt", "ctl_price", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_dvol20")}
    tgt = st.target()
    tr, va = st.slice("train"), st.slice("valid")
    lab = np.isfinite(tgt)
    years = np.array([int(str(d)[:4]) for d in st.dates])
    say(f"panels ready at {time.time() - T0:.0f}s; rows train {tr}, valid {va}")

    def line(name, panel, sign=None, fixed=(), top=None):
        p = np.asarray(panel, dtype=np.float64)
        sg = st.sign(p, "train") if sign is None else sign
        b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
        t_, v_ = b["splits"]["train"], b["splits"]["valid"]
        s = (f"  {name:<40} sgn {sg:+.0f} hl {b['hl_used']:<3g} LS {t_['ls_sharpe']:+.2f}/{v_['ls_sharpe']:+.2f} "
             f"Lg {t_['long_gross_ann'] * 100:+5.1f}/{v_['long_gross_ann'] * 100:+5.1f} "
             f"Ln {t_['long_ann'] * 100:+5.1f}/{v_['long_ann'] * 100:+5.1f} "
             f"Lsh {t_['long_sharpe']:+.2f}/{v_['long_sharpe']:+.2f} sh {t_['short_gross_ann'] * 100:+5.1f}/{v_['short_gross_ann'] * 100:+5.1f} "
             f"TO {t_['ls_turnover'] * 100:4.1f}% LTO {t_['long_turnover'] * 100:4.1f}%")
        for hl in fixed:
            sm = bk.smoothed(sg * p, hl)
            a_, c_ = bk.book_row(sm, tgt, tr), bk.book_row(sm, tgt, va)
            s += (f" | hl{hl}: LS {a_['ls_sharpe']:+.2f}/{c_['ls_sharpe']:+.2f} Ln {a_['long_ann'] * 100:+5.1f}/{c_['long_ann'] * 100:+5.1f} "
                  f"Lsh {a_['long_sharpe']:+.2f}/{c_['long_sharpe']:+.2f}")
        say(s)
        return b

    absK, K2 = np.abs(K), K ** 2
    M60, M30, M15 = roll(K2, 60, "max"), roll(K2, 30, "max"), roll(K2, 15, "max")
    MA15 = roll(absK, 15, "mean")
    say(f"  numpy rebuild of cross_max(K^2,60) vs the engine's: Spearman {dg.pair_rank_corr(M60[tr], np.asarray(P['M60e'], dtype=np.float32)[tr]):+.5f}")
    n60 = roll(K, 60, "count")
    r1 = ctl["ctl_rev1"].astype(np.float64)
    athi, atlo = np.asarray(P["athi"], dtype=np.float64), np.asarray(P["atlo"], dtype=np.float64)
    uplock = (athi >= 0.3) & (r1 >= 1.045)
    dnlock = (atlo >= 0.3) & (r1 <= 0.955)
    lock60 = roll((uplock | dnlock).astype(np.float32), 60, "max") > 0
    up60 = roll(uplock.astype(np.float32), 60, "max") > 0
    lock15 = roll((uplock | dnlock).astype(np.float32), 15, "max") > 0
    Zmin60 = roll(Z, 60, "min")
    Km60, Ks60 = roll(K, 60, "mean"), roll(K, 60, "std")
    Km15, Ks15 = roll(K, 15, "mean"), roll(K, 15, "std")
    rowid = np.arange(K.shape[0])[:, None] + np.zeros((1, K.shape[1]), dtype=np.int64)
    warm = rowid >= 60                                           # the first 60 rows have short windows for everybody

    # ------------------------------------------------------------------ 1. short history
    say("\n" + "=" * 110 + "\n§1  H18: names with fewer than 60 valid days inside the 60-day window (rows >= 60 only)")
    for nm, sl in (("train", tr), ("valid", va)):
        ok = lab[sl] & np.isfinite(M60[sl]) & warm[sl]
        dec = decile_of(M60[sl], ok)
        t_s = tgt[sl]
        ew = np.nansum(np.where(ok, t_s, 0.0), 1) / np.maximum(ok.sum(1), 1)
        ex = t_s - ew[:, None]
        for lim in (60, 40):
            short = n60[sl] < lim
            say(f" [{nm}] share of labelled names with < {lim} valid days: {short[ok].mean():.4f}")
            say("   decile (D1 = smallest max = long leg): " + " ".join(f"D{d + 1:<5}" for d in range(10)))
            say(f"   share <{lim}d:   " + " ".join(f"{short[dec == d].mean():6.3f}" for d in range(10)))
            say("   excess, all:  " + " ".join(f"{np.nanmean(ex[dec == d]) * 25200:+6.1f}" for d in range(10)))
            say(f"   excess,>={lim}d: " + " ".join(f"{np.nanmean(ex[(dec == d) & ~short]) * 25200:+6.1f}" for d in range(10)))
            say(f"   excess,<{lim}d:  " + " ".join(f"{np.nanmean(ex[(dec == d) & short]) * 25200:+6.1f}" if ((dec == d) & short).sum() > 200 else "   n/a" for d in range(10)))
    say(" books:")
    line("cross_max(K^2,60)", M60, fixed=(5,))
    line("  .. names with <60 valid days removed", np.where(n60 < 60, np.nan, M60))
    line("  .. names with <40 valid days removed", np.where(n60 < 40, np.nan, M60))
    line("  .. short-history names sent to the short end", np.where((n60 < 60) & warm, np.nanmax(M60), M60))
    line("cross_max(K^2,30)", M30, fixed=(5,))
    line("cross_sum(K^2,15)  [= original]", F, fixed=(5, 10, 20))

    # ------------------------------------------------------------------ 2. who is where
    say("\n" + "=" * 110 + "\n§2  who sits in each decile (train, rows >= 60; D1 = long leg).  pct = median cross-sectional percentile")
    pr = {k: pct_rank(ctl[k]) for k in ("ctl_price", "ctl_amt", "ctl_turnrate", "ctl_cap", "ctl_ivol")}
    for label_, panel in (("cross_max(K^2,60)", M60), ("original cross_sum(K^2,15)", F)):
        say(f"  -- {label_}")
        say("  dec | lock60  up60  <60d | price% amt% turn% cap% ivol% | med Kmean60  med Kstd60  med sqrt(max60) med Zmin60 | excess ann")
        sl = tr
        ok = lab[sl] & np.isfinite(panel[sl]) & warm[sl]
        dec = decile_of(panel[sl], ok)
        t_s = tgt[sl]
        ew = np.nansum(np.where(ok, t_s, 0.0), 1) / np.maximum(ok.sum(1), 1)
        ex = t_s - ew[:, None]
        for d in range(10):
            m = dec == d
            say(f"  D{d + 1:<2} | {lock60[sl][m].mean() * 100:5.1f}% {up60[sl][m].mean() * 100:5.1f}% {(n60[sl][m] < 60).mean() * 100:4.1f}% | "
                + " ".join(f"{np.nanmedian(pr[k][sl][m]):.2f}" for k in pr)
                + f" | {np.nanmedian(Km60[sl][m]):+.3f}  {np.nanmedian(Ks60[sl][m]):.3f}  {np.nanmedian(np.sqrt(M60[sl][m])):.3f}  {np.nanmedian(Zmin60[sl][m]):.3f}"
                + f" | {np.nanmean(ex[m]) * 25200:+6.1f}%")

    # ------------------------------------------------------------------ 3. inside the clean universe
    say("\n" + "=" * 110 + "\n§3  is the long leg more than 'no lock day in 60d + full history'?")
    clean = (~lock60) & (n60 >= 60) & (Zmin60 >= 0.5)
    for nm, sl in (("train", tr), ("valid", va)):
        ok = lab[sl] & np.isfinite(M60[sl]) & warm[sl]
        t_s = tgt[sl]
        ew = np.nansum(np.where(ok, t_s, 0.0), 1) / np.maximum(ok.sum(1), 1)
        c = ok & clean[sl]
        ewc = np.nansum(np.where(c, t_s, 0.0), 1) / np.maximum(c.sum(1), 1)
        d_ = (ewc - ew)
        say(f" [{nm}] clean universe = {c.sum() / ok.sum():.3f} of labelled cells; its equal weight beats the full equal weight by {np.nanmean(d_[warm[sl][:, 0]]) * 25200:+.1f}%/yr")
    Mc = np.where(clean, M60, np.nan)
    say(" decile profile of cross_max(K^2,60) INSIDE the clean universe (ascending in signal = descending in the max; vs the clean universe's own equal weight):")
    for nm, sl in (("train", tr), ("valid", va)):
        rows = bk.quantile_profile(-Mc, tgt, sl, n=10)
        say(f"    [{nm}] " + " ".join(f"{r['excess_ann'] * 100:+6.1f}" for r in rows))
    line("cross_max(K^2,60) inside clean universe", Mc)
    line("original inside clean universe", np.where(clean, F, np.nan))
    line("60d mean of K, signed, clean universe", np.where(clean, Km60, np.nan))
    line("60d std of K, clean universe", np.where(clean, Ks60, np.nan))
    line("|60d mean of K|, clean universe", np.where(clean, np.abs(Km60), np.nan))

    # ------------------------------------------------------------------ 4. level vs dispersion by year
    say("\n" + "=" * 110 + "\n§4  rank IC by year (raw panels, sign fixed at 'higher = worse' i.e. IC of -panel; train+valid years)")
    cand = {
        "original sum K^2 15": F,
        "max K^2 60": M60,
        "level |mean K 15|": np.abs(Km15),
        "disp  std K 15": Ks15,
        "signed mean K 15 (+)": -Km15,          # so that the printed number is IC of +Km15
        "signed mean K 60 (+)": -Km60,
        "level |mean K 60|": np.abs(Km60),
        "disp  std K 60": Ks60,
        "signed mean K 15, no lock15 (+)": -np.where(lock15, np.nan, Km15),
    }
    ys = sorted(set(years[tr.start:va.stop].tolist()))
    say("  " + " " * 34 + " ".join(f"{y:>8}" for y in ys))
    for nm, p in cand.items():
        out = []
        for y in ys:
            idx = np.nonzero(years == y)[0]
            idx = idx[(idx >= tr.start) & (idx < va.stop)]
            sl_ = slice(int(idx[0]), int(idx[-1]) + 1)
            out.append(dg.ic_row(np.asarray(-p[sl_], dtype=np.float64), tgt[sl_], sign=1.0)["rank_ic"])
        say(f"  {nm:<34} " + " ".join(f"{v:+8.4f}" for v in out))
    say("  x2's oddity (rank IC of the bulk 15-day mean K on valid printed +0.0000): recomputed here --")
    calm15 = (~lock15) & (roll(Z, 15, "min") >= 0.5) & (roll(K, 15, "count") >= 15)
    Kb = np.where(calm15, Km15, np.nan)
    for nm, sl in (("train", tr), ("valid", va)):
        r = dg.ic_row(np.asarray(Kb[sl], dtype=np.float64), tgt[sl], sign=1.0)
        say(f"    [{nm}] rank IC {r['rank_ic']:+.5f}  (ICIR {r.get('rank_icir', float('nan')):+.3f})")

    # ------------------------------------------------------------------ 5. long-only practicalities
    say("\n" + "=" * 110 + "\n§5  long-only practicalities")
    say(" -- breadth: the long book at top 5% / 10% / 20% (sign -1; half-life as fitted on train at 10%)")
    for label_, panel in (("cross_max(K^2,60)", M60), ("cross_max(K^2,30)", M30), ("cross_mean(|K|,15)", MA15), ("original", F)):
        p = np.asarray(panel, dtype=np.float64)
        b = st.books(p, fit="train", evals=("train",), sign=-1.0)
        sm = bk.smoothed(-p, b["hl_used"])
        s = f"  {label_:<22} hl {b['hl_used']:<3g}"
        for tf in (0.05, 0.10, 0.20):
            a_, c_ = bk.book_row(sm, tgt, tr, top_frac=tf), bk.book_row(sm, tgt, va, top_frac=tf)
            s += (f" | top {tf:.0%}: Lg {a_['long_gross_ann'] * 100:+5.1f}/{c_['long_gross_ann'] * 100:+5.1f} Ln {a_['long_ann'] * 100:+5.1f}/{c_['long_ann'] * 100:+5.1f} "
                  f"Lsh {a_['long_sharpe']:+.2f}/{c_['long_sharpe']:+.2f} LTO {a_['long_turnover'] * 100:4.1f}%")
        say(s)
    say(" -- double sort (train / valid): excess of the factor's long decile formed INSIDE each quintile of the gate, vs that quintile's equal weight")
    for gname in ("ctl_turnrate", "ctl_cap", "ctl_amt"):
        for label_, panel in (("cross_max(K^2,60)", M60), ("original", F)):
            outs = []
            for nm, sl in (("train", tr), ("valid", va)):
                ok = lab[sl] & np.isfinite(panel[sl]) & np.isfinite(ctl[gname][sl]) & warm[sl]
                gq = decile_of(ctl[gname][sl], ok, n=5)
                t_s = tgt[sl]
                res = []
                for q in range(5):
                    inq = ok & (gq == q)
                    dq = decile_of(panel[sl], inq)
                    ewq = np.nansum(np.where(inq, t_s, 0.0), 1) / np.maximum(inq.sum(1), 1)
                    exq = t_s - ewq[:, None]
                    res.append(np.nanmean(exq[dq == 0]) * 25200)
                outs.append(" ".join(f"{v:+6.1f}" for v in res))
            say(f"  gate {gname:<13} {label_:<20} train Q1..Q5: {outs[0]}   valid: {outs[1]}")
    say(" -- 'fast event + slow state' as a rank sum, against its parts")
    rk60, rk15 = pct_rank(M60), pct_rank(MA15)
    line("rank(max60) + rank(mean|K|15)", rk60 + rk15, fixed=(5,))
    line("rank(max60) + 0.5 rank(mean|K|15)", rk60 + 0.5 * rk15)
    line("cross_max(K^2,60)", M60)
    line("cross_mean(|K|,15)", MA15, fixed=(5,))
    line("cross_max(K^2,30)", M30)
    say(f"  Spearman: max60~max30 {dg.pair_rank_corr(M60[tr], M30[tr]):+.3f}  max60~mean|K|15 {dg.pair_rank_corr(M60[tr], MA15[tr]):+.3f}  "
        f"max60~original {dg.pair_rank_corr(M60[tr], F[tr]):+.3f}  max30~original {dg.pair_rank_corr(M30[tr], F[tr]):+.3f}")
    say(f"\ndone in {time.time() - T0:.0f}s")
