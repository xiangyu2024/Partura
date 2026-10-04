"""x2 -- three questions S1/S2 left open (train/valid only, never the holdout):

  1  cross_sum treats a missing day as 0.  x1's numpy cross_MEAN(|K|,15) had a much better long leg than the
     engine's cross_SUM(abs_(K),15) (Lnet +5.4%/+5.5% vs +1.9%/+2.8%).  Is the difference the names with missing
     days (suspended / all-day-locked / newly listed) being pushed into the long leg?
  2  S1 killed "the bulk is the full-day AR(1) coefficient" (rank corr of r_ar1 with the signed 15-day K: 0.00).
     What DOES the 15-day mean of K line up with, away from the lock events?
  3  screen the aggregation layer (sum / mean / max / median, |K| vs K^2, window, built-in smoothing, where the
     fold sits) with the same book functions the tables use -- to choose what goes into the official S3 stage.
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
    for k in range(d):
        sh = np.full_like(x, np.nan)
        sh[k:] = x[:D - k]
        fin = np.isfinite(sh)
        cnt += fin
        if how in ("sum", "mean", "count"):
            z = np.where(fin, sh, 0.0)
            acc = z if acc is None else acc + z
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
    return acc


def roll_med(x, d):
    x = np.asarray(x, dtype=np.float32)
    D, S = x.shape
    out = np.full_like(x, np.nan)
    pad = np.concatenate([np.full((d - 1, S), np.nan, dtype=np.float32), x], axis=0)
    step = 256
    for a in range(0, D, step):
        w = np.lib.stride_tricks.sliding_window_view(pad[a:a + step + d - 1], d, axis=0)   # (rows, S, d)
        with np.errstate(all="ignore"):
            out[a:a + w.shape[0]] = np.nanmedian(w, axis=-1)
    return out


def decile_of(panel, ok, n=10):
    p = np.where(ok, panel, np.nan).astype(np.float64)
    r = dg.rank_rows(p)
    cnt = np.isfinite(r).sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        return np.floor((r - 1.0) / np.maximum(cnt, 1) * n)


A = "nt_ts_autocorr_s1(Ret, 3)"
EXPR = {
    "F": f"cross_sum(pow_2(day_kurt({A})), 15)",
    "K": f"day_kurt({A})",
    "Z": f"day_mean(abs_(sign({A})))",
    "W": "day_mean(abs_(sign(Ret)))",
    "athi": "day_mean(eq(Close, in_max(High)))",
    "atlo": "day_mean(eq(Close, in_min(Low)))",
    "mA": f"day_mean({A})",
    "sA": f"day_skew({A})",
    "sdA": f"day_std({A})",
    "p1": f"day_mean(is_gt0(sub(abs_({A}), 0.99)))",
    "sgac": "day_autocorr_n1(sign(Ret))",
    "ar1": "day_ar1_coefficient(Ret)",
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
    say(f"panels ready at {time.time() - T0:.0f}s")

    def line(name, panel, sign=None, fixed=(5,)):
        p = np.asarray(panel, dtype=np.float64)
        sg = st.sign(p, "train") if sign is None else sign
        b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
        t_, v_ = b["splits"]["train"], b["splits"]["valid"]
        s = (f"  {name:<34} sgn {sg:+.0f} hl {b['hl_used']:<3g} LS {t_['ls_sharpe']:+.2f}/{v_['ls_sharpe']:+.2f} "
             f"Lg {t_['long_gross_ann'] * 100:+5.1f}/{v_['long_gross_ann'] * 100:+5.1f} "
             f"Ln {t_['long_ann'] * 100:+5.1f}/{v_['long_ann'] * 100:+5.1f} "
             f"Lsh {t_['long_sharpe']:+.2f}/{v_['long_sharpe']:+.2f} sh {t_['short_gross_ann'] * 100:+5.1f}/{v_['short_gross_ann'] * 100:+5.1f} "
             f"TO {t_['ls_turnover'] * 100:4.1f}%")
        for hl in fixed:
            sm = bk.smoothed(sg * p, hl)
            a_, c_ = bk.book_row(sm, tgt, tr), bk.book_row(sm, tgt, va)
            s += (f" | hl{hl}: LS {a_['ls_sharpe']:+.2f}/{c_['ls_sharpe']:+.2f} Ln {a_['long_ann'] * 100:+5.1f}/{c_['long_ann'] * 100:+5.1f} "
                  f"Lsh {a_['long_sharpe']:+.2f}/{c_['long_sharpe']:+.2f}")
        say(s)

    absK, K2 = np.abs(K), K ** 2

    # ------------------------------------------------------------------ 1. missing days
    say("\n" + "=" * 110 + "\n§1  missing days inside the 15-day window (cross_sum counts them as 0)")
    nval = roll(K, 15, "count")                                  # finite-K days in the window
    wnan = roll(np.where(np.isfinite(W), np.nan, 1.0), 15, "count")       # days with no Ret at all (suspended / not listed)
    wzero = roll(np.where(W == 0, 1.0, np.nan), 15, "count")              # days traded but the price never moved (all-day lock)
    for nm, sl in (("train", tr), ("valid", va)):
        ok = lab[sl] & np.isfinite(F[sl])
        dec = decile_of(F[sl], ok)
        t_s = tgt[sl]
        ew = np.nansum(np.where(ok, t_s, 0.0), 1) / np.maximum(ok.sum(1), 1)
        ex = t_s - ew[:, None]
        short = nval[sl] < 15
        say(f" [{nm}] share of labelled names with < 15 valid days in the window: {short[ok].mean():.4f}"
            f"   (of them: with a no-data day {(wnan[sl] > 0)[ok & short].mean():.2f}, with a price-never-moved day {(wzero[sl] > 0)[ok & short].mean():.2f})")
        say("   decile:       " + " ".join(f"D{d + 1:<5}" for d in range(10)))
        say("   share <15d:   " + " ".join(f"{short[dec == d].mean():6.3f}" for d in range(10)))
        say("   excess, all:  " + " ".join(f"{np.nanmean(ex[dec == d]) * 25200:+6.1f}" for d in range(10)))
        say("   excess,=15d:  " + " ".join(f"{np.nanmean(ex[(dec == d) & ~short]) * 25200:+6.1f}" for d in range(10)))
        say("   excess,<15d:  " + " ".join(f"{np.nanmean(ex[(dec == d) & short]) * 25200:+6.1f}" if ((dec == d) & short).sum() > 200 else "   n/a" for d in range(10)))
    say(" books (sum = the engine's convention, missing day = 0; mean = missing day skipped):")
    S2, M2 = roll(K2, 15, "sum"), roll(K2, 15, "mean")
    S1, M1 = roll(absK, 15, "sum"), roll(absK, 15, "mean")
    X2 = roll(K2, 15, "max")
    line("cross_sum(K^2,15)  [= original]", S2)
    line("cross_mean(K^2,15)", M2)
    line("cross_sum(|K|,15)", S1)
    line("cross_mean(|K|,15)", M1)
    line("cross_max(K^2,15)", X2)
    line("original, names with <15d removed", np.where(nval < 15, np.nan, S2))
    say(f"  Spearman(sum K^2, mean K^2) = {dg.pair_rank_corr(S2[tr], M2[tr]):+.4f};  (sum |K|, mean |K|) = {dg.pair_rank_corr(S1[tr], M1[tr]):+.4f}")

    # ------------------------------------------------------------------ 2. what is the bulk
    say("\n" + "=" * 110 + "\n§2  what does the 15-day mean of K line up with, away from the lock events?  (train)")
    r1 = ctl["ctl_rev1"].astype(np.float64)
    athi, atlo = np.asarray(P["athi"], dtype=np.float64), np.asarray(P["atlo"], dtype=np.float64)
    lock = ((athi >= 0.3) & (r1 >= 1.045)) | ((atlo >= 0.3) & (r1 <= 0.955))
    lock15 = roll(lock.astype(np.float32), 15, "max") > 0
    Zmin15 = roll(Z, 15, "min")
    calm = (~lock15) & (Zmin15 >= 0.5) & (nval >= 15)             # the "bulk": no event, no stale day, full window
    say(f"  bulk cells (no lock day in 15d, min Z >= 0.5, 15 valid days): {calm[tr][lab[tr]].mean():.3f} of labelled cells")
    Km = roll(K, 15, "mean")
    Kb = np.where(calm, Km, np.nan)
    desc = {}
    for k in ("mA", "sA", "sdA", "p1", "sgac", "ar1"):
        if k in P:
            desc[k] = roll(np.asarray(P[k], dtype=np.float32), 15, "mean")
    desc["Z"], desc["W"] = roll(Z, 15, "mean"), roll(W, 15, "mean")
    say("  single-day Spearman of K (all cells): " + "  ".join(
        f"{k} {dg.pair_rank_corr(K[tr], np.asarray(P[k], dtype=np.float64)[tr]):+.3f}" for k in ("mA", "sA", "sdA", "p1", "sgac", "ar1") if k in P))
    say("  15-day means, bulk cells only -- Spearman with mean K:")
    for k, v in desc.items():
        say(f"     {k:<6} {dg.pair_rank_corr(Kb[tr], np.where(calm, v, np.nan)[tr]):+.3f}")
    for k in ("ctl_ivol", "ctl_dvol20", "ctl_turnrate", "ctl_amt", "ctl_price", "ctl_cap"):
        say(f"     {k:<12} {dg.pair_rank_corr(Kb[tr], np.where(calm, ctl[k], np.nan)[tr]):+.3f}")
    zK = dg._zrank(Kb[tr])
    for label_, names in (("the 3-pair distribution's own moments (mA, sA, sdA, p1, Z)", ["mA", "sA", "sdA", "p1", "Z"]),
                          ("full-day dependence (sgac, ar1)", ["sgac", "ar1"]),
                          ("activity (W, Z)", ["W", "Z"])):
        cz = {k: dg._zrank(np.where(calm, desc[k], np.nan)[tr]) for k in names if k in desc}
        res, info = dg.neutralise(zK, cz, panel_ready=True, controls_ready=True)
        ic = dg.ic_row(res, tgt[tr], sign=1.0)["rank_ic"]
        say(f"  rank-R2 of bulk mean-K on {label_}: {info['mean_r2']:.3f};  rank IC of the residual {ic:+.4f}")
    cz = {k: dg._zrank(np.where(calm, ctl[k], np.nan)[tr]) for k in ("ctl_ivol", "ctl_dvol20", "ctl_turnrate", "ctl_amt", "ctl_price", "ctl_cap")}
    res, info = dg.neutralise(zK, cz, panel_ready=True, controls_ready=True)
    say(f"  rank-R2 of bulk mean-K on six shared controls: {info['mean_r2']:.3f};  rank IC of the residual {dg.ic_row(res, tgt[tr], sign=1.0)['rank_ic']:+.4f}")
    say(f"  rank IC of bulk mean-K itself (raw sign; + = higher K, higher return): train {dg.ic_row(Kb[tr], tgt[tr], sign=1.0)['rank_ic']:+.4f}  valid {dg.ic_row(Kb[va], tgt[va], sign=1.0)['rank_ic']:+.4f}")
    say("  decile profile of mean K inside the bulk (ascending; annualised excess vs the bulk's own equal weight):")
    for nm, sl in (("train", tr), ("valid", va)):
        rows = bk.quantile_profile(Kb, tgt, sl, n=10)
        say(f"    [{nm}] " + " ".join(f"{r['excess_ann'] * 100:+6.1f}" for r in rows))
    say("  the descriptors as factors on the whole universe (15-day mean):")
    for k in ("mA", "sA", "p1", "sgac", "ar1"):
        if k in desc:
            line(f"cross_mean({k},15)", desc[k], fixed=())

    # ------------------------------------------------------------------ 3. the aggregation layer
    say("\n" + "=" * 110 + "\n§3  the aggregation layer, same book functions as the tables (train/valid; half-life fitted on train by L/S Sharpe;")
    say("    after the bar: the same signal at a fixed half-life of 5 days)")
    say(" -- aggregator (window 15)")
    line("cross_sum(K^2,15)  [= original]", S2)
    line("cross_mean(K^2,15)", M2)
    line("cross_mean(|K|,15)", M1)
    line("cross_max(K^2,15)", X2)
    line("cross_med(|K|,15)", roll_med(absK, 15))
    say(" -- window")
    for d in (10, 20, 30, 60):
        line(f"cross_max(K^2,{d})", roll(K2, d, "max"))
    for d in (10, 20, 30, 60):
        line(f"cross_mean(|K|,{d})", roll(absK, d, "mean"))
    for d in (30, 60):
        line(f"cross_mean(K^2,{d})", roll(K2, d, "mean"))
    say(" -- smoothing built into the expression (so the L/S-optimal half-life no longer decides the long leg)")
    for d in (5, 10):
        line(f"cross_mean(cross_max(K^2,15),{d})", roll(X2, d, "mean"))
        line(f"cross_mean(cross_mean(|K|,15),{d})", roll(M1, d, "mean"))
    say(" -- where the fold sits: |K - c| (the original folds at c = 0)")
    for c in (-0.45, -0.30, -0.15, 0.0, 0.15, 0.30):
        line(f"cross_mean(|K - ({c:+.2f})|,15)", roll(np.abs(K - c), 15, "mean"))
    say(" -- capping the event magnitude")
    for cap in (1.0, 3.0):
        line(f"cross_mean(min(|K|,{cap:g}),15)", roll(np.minimum(absK, cap), 15, "mean"))
    say(f"\n  Spearman with the original: mean|K|15 {dg.pair_rank_corr(S2[tr], M1[tr]):+.3f}  max15 {dg.pair_rank_corr(S2[tr], X2[tr]):+.3f}  "
        f"max30 {dg.pair_rank_corr(S2[tr], roll(K2, 30, 'max')[tr]):+.3f}  mean5(max15) {dg.pair_rank_corr(S2[tr], roll(X2, 5, 'mean')[tr]):+.3f}  "
        f"max15~mean|K|15 {dg.pair_rank_corr(X2[tr], M1[tr]):+.3f}")
    say(f"\ndone in {time.time() - T0:.0f}s")
