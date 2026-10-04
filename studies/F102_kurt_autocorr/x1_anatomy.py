"""x1 -- what does  cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)  actually measure?

Questions (each section prints its own answer; train/valid only, never the holdout):
  0  kernel sources the `src` tool cannot reach (`_kurt`, EPS) + probe self-checks
  1  the distribution of K = day_kurt(A): how often negative, how heavy the right tail
  2  is K a sparsity meter?  K against Z = share of minutes with A != 0, W = share with Ret != 0
  3  does the +EPS in the correlation denominator matter at the scale of minute returns?
  4  is the 15-day SUM of K^2 really a 15-day MAX?  which simple quantity ranks stocks the same way?
  5  next-day excess by decile of the SIGNED quantity: is the pow_2 fold a feature or an accident?
  6  who sits in each decile of the factor (lock days, price, activity, missing labels)
  7  the short leg split by "had a limit-lock day in the last 15 days"; books with those names removed
  8  conditional IC of the factor inside activity buckets
"""
import importlib.util
import inspect
import sys
import time
from pathlib import Path

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F102_kurt_autocorr"
HERE = Path(__file__).resolve().parent
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def qt(x, qs=(1, 5, 25, 50, 75, 95, 99)):
    x = np.asarray(x, dtype=np.float64)
    x = x[np.isfinite(x)]
    return "  ".join(f"p{p}={np.percentile(x, p):.4g}" for p in qs) if x.size else "(empty)"


def roll(x, d, how):
    """Causal d-day rolling reduce along axis 0, NaN-skipping (same convention as cross_*)."""
    x = np.asarray(x, dtype=np.float32)
    D = x.shape[0]
    acc = None
    cnt = np.zeros(x.shape, dtype=np.int16)
    for k in range(d):
        sh = np.full_like(x, np.nan)
        sh[k:] = x[:D - k]
        fin = np.isfinite(sh)
        cnt += fin
        if how in ("sum", "mean"):
            z = np.where(fin, sh, 0.0)
            acc = z if acc is None else acc + z
        elif how == "max":
            acc = sh if acc is None else np.fmax(acc, sh)
        elif how == "min":
            acc = sh if acc is None else np.fmin(acc, sh)
    if how == "sum":
        return np.where(cnt > 0, acc, np.nan)
    if how == "mean":
        return np.where(cnt > 0, acc / np.maximum(cnt, 1), np.nan)
    return acc


def prof(name, panel, tgt, sl, n=10):
    rows = bk.quantile_profile(np.asarray(panel, dtype=np.float64), tgt, sl, n=n)
    say(f"  {name:<34}" + " ".join(f"{r['excess_ann'] * 100:+6.1f}" for r in rows))


def decile_of(panel, ok, n=10):
    """Within-day decile index (0 = lowest value) over the cells where ok."""
    p = np.where(ok, panel, np.nan).astype(np.float64)
    r = dg.rank_rows(p)
    cnt = np.isfinite(r).sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        q = np.floor((r - 1.0) / np.maximum(cnt, 1) * n)
    return q


def pct_rank(panel):
    r = dg.rank_rows(np.asarray(panel, dtype=np.float64))
    cnt = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(cnt, 1)


def book_line(name, st, panel, sign=None):
    b = st.books(panel, fit="train", evals=("train", "valid"), sign=sign)
    sg = st.sign(panel, "train") if sign is None else sign
    tr, va = b["splits"]["train"], b["splits"]["valid"]
    say(f"  {name:<30} sgn {sg:+.0f} hl {b['hl_used']:<4g} LS {tr['ls_sharpe']:+.2f}/{va['ls_sharpe']:+.2f}  "
        f"Lgross {tr['long_gross_ann'] * 100:+.1f}%/{va['long_gross_ann'] * 100:+.1f}%  "
        f"Lnet {tr['long_ann'] * 100:+.1f}%/{va['long_ann'] * 100:+.1f}%  "
        f"Lsharpe {tr['long_sharpe']:+.2f}/{va['long_sharpe']:+.2f}  "
        f"short {tr['short_gross_ann'] * 100:+.1f}%/{va['short_gross_ann'] * 100:+.1f}%  TO {tr['ls_turnover'] * 100:.1f}%")


# ------------------------------------------------------------------ 0. sources + self-checks
say("=" * 100 + "\n§0  kernel sources not reachable through `study.sh src`, and probe self-checks")
from alphacube.operators import common as C  # noqa: E402

say(inspect.getsource(C._kurt))
say("EPS =", C.EPS)
from partura.remote_tools import _catalogs  # noqa: E402

reg, _cat = _catalogs()
spec = importlib.util.spec_from_file_location("f102_probes", HERE / "probes.py")
mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
mod.selfcheck(reg)
from partura.probes import run_probes, values  # noqa: E402

for w in (3, 15, 60):
    say(f"[probe] nt_ts_autocorr_s1 w={w}:",
        values(run_probes(reg._ops["nt_ts_autocorr_s1"], window=w,
                          only=["eps_shrink_at_scale", "iid_null_location", "impulse_in_zeros", "constant_input_value"])))

# ------------------------------------------------------------------ panels
A = "nt_ts_autocorr_s1(Ret, 3)"
EXPR = {
    "F": f"cross_sum(pow_2(day_kurt({A})), 15)",
    "K": f"day_kurt({A})",
    "K1k": "day_kurt(nt_ts_autocorr_s1(mul(Ret, 1000), 3))",
    "Z": f"day_mean(abs_(sign({A})))",
    "W": "day_mean(abs_(sign(Ret)))",
    "athi": "day_mean(eq(Close, in_max(High)))",
    "atlo": "day_mean(eq(Close, in_min(Low)))",
    "first": "day_first(Ret)",
}

with Study(FID) as st:
    P = st.panels(EXPR)
    missing = [k for k in EXPR if k not in P]
    if missing:
        say("MISSING PANELS:", missing)
    F, K, Z, W = (np.asarray(P[k], dtype=np.float32) for k in ("F", "K", "Z", "W"))
    ctl = {n: np.asarray(st.control(n), dtype=np.float32)
           for n in ("ctl_rev1", "ctl_amt", "ctl_price", "ctl_cap", "ctl_turnrate", "ctl_ivol")}
    tgt = st.target()
    tr, va = st.slice("train"), st.slice("valid")
    ut = slice(tr.start, va.stop)                       # train + valid; nothing after it is ever touched
    lab = np.isfinite(tgt)
    say(f"\npanels ready at {time.time() - T0:.0f}s; shape {F.shape}; train rows {tr}, valid rows {va}")

    # ------------------------------------------------------------------ 1. K
    say("\n" + "=" * 100 + "\n§1  K = day_kurt(A), train, labelled cells")
    k_tr, ok_tr = K[tr], lab[tr]
    kk = k_tr[ok_tr]
    say("  quantiles:", qt(kk))
    fin = np.isfinite(kk)
    say(f"  NaN share {1 - fin.mean():.4f};  K<0 share {(kk[fin] < 0).mean():.3f};  |K|<0.5 share {(np.abs(kk[fin]) < 0.5).mean():.3f};"
        f"  K>10 share {(kk[fin] > 10).mean():.4f};  K>50 share {(kk[fin] > 50).mean():.4f}")
    k2 = kk[fin].astype(np.float64) ** 2
    srt = np.sort(k2)[::-1]
    say(f"  K^2: mean {k2.mean():.2f} median {np.median(k2):.3f};  top 1% of stock-days carry {srt[:max(1, srt.size // 100)].sum() / srt.sum():.1%} of the total")
    if "first" in P:
        fr = np.asarray(P["first"], dtype=np.float64)[tr][ok_tr]
        say("  day_first(Ret) quantiles (is the first bar an overnight return?):", qt(fr))

    # ------------------------------------------------------------------ 2. sparsity meter
    say("\n" + "=" * 100 + "\n§2  is K a sparsity meter?  (mean daily Spearman, train)")
    say(f"  K ~ Z (share of minutes with A != 0): {dg.pair_rank_corr(K[tr], Z[tr]):+.3f}")
    say(f"  K ~ W (share of minutes with Ret != 0): {dg.pair_rank_corr(K[tr], W[tr]):+.3f}")
    say(f"  Z ~ W: {dg.pair_rank_corr(Z[tr], W[tr]):+.3f}")
    z_tr, w_tr = Z[tr][ok_tr], W[tr][ok_tr]
    say("  Z quantiles:", qt(z_tr))
    say("  W quantiles:", qt(w_tr))
    say("  by Z bucket:   share of cells | median K | K p25..p75 | median (K+3)*Z  [constant if K = c/Z - 3]")
    edges = [0, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0001]
    m_all = np.isfinite(z_tr) & np.isfinite(kk)
    for lo, hi in zip(edges[:-1], edges[1:]):
        m = m_all & (z_tr >= lo) & (z_tr < hi)
        if m.sum() < 50:
            say(f"    Z in [{lo:.2f},{hi:.2f})  n={int(m.sum())}")
            continue
        kb = kk[m].astype(np.float64)
        say(f"    Z in [{lo:.2f},{hi:.2f})  {m.sum() / m_all.sum():6.1%} | {np.median(kb):+8.2f} | {np.percentile(kb, 25):+8.2f} .. {np.percentile(kb, 75):+8.2f} | "
            f"{np.median((kb + 3) * z_tr[m]):.3f}")

    # ------------------------------------------------------------------ 3. EPS
    say("\n" + "=" * 100 + "\n§3  does the +EPS matter at the scale of minute returns?  K from Ret vs K from 1000*Ret (train)")
    if "K1k" in P:
        K1 = np.asarray(P["K1k"], dtype=np.float32)
        say(f"  mean daily Spearman(K, K_1000x): {dg.pair_rank_corr(K[tr], K1[tr]):+.4f}")
        d = (K1[tr][ok_tr] - kk).astype(np.float64)
        say("  K_1000x - K quantiles:", qt(d))
        say(f"  sign flips: {(np.sign(K1[tr][ok_tr]) != np.sign(kk))[np.isfinite(d)].mean():.4f}")
        pr = pct_rank(ctl["ctl_price"][tr])[ok_tr]
        for lo, hi in ((0, .2), (.2, .4), (.4, .6), (.6, .8), (.8, 1.01)):
            m = np.isfinite(d) & (pr >= lo) & (pr < hi)
            say(f"    price pct [{lo:.1f},{hi:.1f}): median K {np.median(kk[m]):+.3f}  median K_1000x {np.median(K1[tr][ok_tr][m]):+.3f}  median |diff| {np.median(np.abs(d[m])):.4f}")
        F1 = roll(K1.astype(np.float64) ** 2, 15, "sum")
        say(f"  15-day factor rebuilt from K_1000x vs the original: Spearman {dg.pair_rank_corr(F[tr], F1[tr]):+.4f}")
        book_line("F (orig)", st, F)
        book_line("F from 1000*Ret", st, F1)

    # ------------------------------------------------------------------ 4. sum or max
    say("\n" + "=" * 100 + "\n§4  the 15-day sum of K^2: is it a max in disguise?  what ranks stocks the same way?  (train)")
    K64 = K.astype(np.float64)
    K2 = K64 ** 2
    S15 = roll(K2, 15, "sum")
    both = np.isfinite(S15[ut]) & np.isfinite(F[ut])
    rel = np.abs(S15[ut][both] - F[ut][both]) / np.maximum(np.abs(F[ut][both]), 1e-6)
    say(f"  my numpy rebuild of the factor vs the engine's: Spearman {dg.pair_rank_corr(F[tr], S15[tr]):+.5f}; "
        f"median rel diff {np.median(rel):.2e}, p99 {np.percentile(rel, 99):.2e};  NaN mismatch {(np.isfinite(S15[ut]) != np.isfinite(F[ut])).mean():.5f}")
    M15 = roll(K2, 15, "max")
    sh = (M15[tr] / S15[tr])[ok_tr]
    say("  share of the 15-day sum carried by its largest day:", qt(sh))
    Ks15 = roll(K64, 15, "mean")
    Ka15 = roll(np.abs(K64), 15, "mean")
    Kp15 = roll((K64 + 3.0) ** 2, 15, "sum")
    Kmax15 = roll(K64, 15, "max")
    Zmin15, Zmean15 = roll(Z, 15, "min"), roll(Z, 15, "mean")
    Wmin15, Wmean15 = roll(W, 15, "min"), roll(W, 15, "mean")
    cands = {"cross_max(K^2,15)": M15, "cross_max(K,15)  [no fold]": Kmax15, "cross_mean(K,15)  [no fold, linear]": Ks15,
             "cross_mean(|K|,15) [fold, linear]": Ka15, "cross_sum((K+3)^2,15) [no fold, convex]": Kp15,
             "-cross_min(Z,15)": -Zmin15, "-cross_mean(Z,15)": -Zmean15, "-cross_min(W,15)": -Wmin15, "-cross_mean(W,15)": -Wmean15,
             "K^2 today": K2, "K today": K64}
    for n, p in cands.items():
        say(f"  Spearman(F, {n:<40}) = {dg.pair_rank_corr(F[tr], p[tr]):+.3f}")

    # ------------------------------------------------------------------ 5. signed profiles
    say("\n" + "=" * 100 + "\n§5  next-day excess (annualised %, vs equal-weight universe) by decile, ASCENDING in the quantity; no smoothing")
    for nm, sl in (("train", tr), ("valid", va)):
        say(f" [{nm}]                              D1 (lowest) ... D10 (highest)")
        prof("F (the factor)", F, tgt, sl)
        prof("cross_mean(K,15)  signed", Ks15, tgt, sl)
        prof("cross_max(K,15)   signed", Kmax15, tgt, sl)
        prof("cross_mean(Z,15)  activity", Zmean15, tgt, sl)
        prof("cross_min(Z,15)   stalest day", Zmin15, tgt, sl)
        prof("cross_mean(W,15)", Wmean15, tgt, sl)
        prof("K today  signed", K64, tgt, sl)
        prof("Z today", Z, tgt, sl)
    say(" [train] 20 buckets of cross_mean(K,15), to see where the hump (if any) is:")
    rows = bk.quantile_profile(Ks15, tgt, tr, n=20)
    say("   " + " ".join(f"{r['excess_ann'] * 100:+6.1f}" for r in rows))
    q20 = decile_of(Ks15[tr], ok_tr & np.isfinite(Ks15[tr]), n=20)
    say("   median cross_mean(K,15) per bucket: " + " ".join(f"{np.nanmedian(np.where(q20 == b, Ks15[tr], np.nan)):+.2f}" for b in range(20)))
    say("   median F per bucket:               " + " ".join(f"{np.nanmedian(np.where(q20 == b, F[tr], np.nan)):.3g}" for b in range(20)))

    # ------------------------------------------------------------------ 6. who is in each decile
    say("\n" + "=" * 100 + "\n§6  who sits in each decile of F (train; D1 = lowest F = the LONG leg, D10 = highest F = the SHORT leg)")
    r1 = ctl["ctl_rev1"].astype(np.float64)
    athi, atlo = np.asarray(P["athi"], dtype=np.float64), np.asarray(P["atlo"], dtype=np.float64)
    lock_up = (athi >= 0.3) & (r1 >= 1.045)                 # >= 30% of the minutes closed at the day's high, on a day up >= 4.5%
    lock_dn = (atlo >= 0.3) & (r1 <= 0.955)
    say(f"  lock-day proxy: up-lock {np.nanmean(lock_up[tr][ok_tr]):.4f} of stock-days, down-lock {np.nanmean(lock_dn[tr][ok_tr]):.4f}")
    for nm, lk in (("up-lock", lock_up), ("down-lock", lock_dn)):
        kl = K64[tr][lk[tr] & ok_tr]
        say(f"  K on {nm} days: NaN share {1 - np.isfinite(kl).mean():.3f};", qt(kl, (5, 25, 50, 75, 95)))
        zl = Z[tr][lk[tr] & ok_tr]
        say(f"  Z on {nm} days:", qt(zl, (5, 25, 50, 75, 95)))
    up15 = roll(lock_up.astype(np.float32), 15, "max") > 0
    dn15 = roll(lock_dn.astype(np.float32), 15, "max") > 0
    okF = ok_tr & np.isfinite(F[tr])
    dec = decile_of(F[tr], okF)
    t_tr = tgt[tr]
    ew = np.nansum(np.where(okF, t_tr, 0.0), 1) / np.maximum(okF.sum(1), 1)
    ex = t_tr - ew[:, None]
    prk = {n: pct_rank(ctl[n][tr]) for n in ("ctl_price", "ctl_amt", "ctl_turnrate", "ctl_cap", "ctl_ivol")}
    say("  dec | up-lock15 dn-lock15 | price% amt% turn% cap% ivol% (median pct-rank) | med Zmean15 med Zmin15 med Kmean15 | share K<0 today | excess ann")
    for d in range(10):
        m = dec == d
        say(f"  D{d + 1:<2} |   {up15[tr][m].mean():6.1%}   {dn15[tr][m].mean():6.1%} |  "
            + " ".join(f"{np.nanmedian(prk[n][m]):.2f}" for n in prk)
            + f" |   {np.nanmedian(Zmean15[tr][m]):.3f}   {np.nanmedian(Zmin15[tr][m]):.3f}   {np.nanmedian(Ks15[tr][m]):+.2f} |"
              f"   {np.nanmean((K64[tr][m] < 0)):.2f} | {np.nanmean(ex[m]) * 252 * 100:+.1f}%")
    # H10: missing labels in the short basket (signal present, label missing -> counted as 0 in the books)
    sigF = np.isfinite(F[tr])
    decS = decile_of(F[tr], sigF)
    for d in (0, 4, 9):
        m = decS == d
        say(f"  signal-decile D{d + 1}: share of names whose label is NaN (cannot be bought at t+1 open) = {(~lab[tr])[m].mean():.4f}")
    say(f"  whole universe with a signal: {(~lab[tr])[sigF].mean():.4f}")

    # ------------------------------------------------------------------ 7. the short leg, split
    say("\n" + "=" * 100 + "\n§7  the two extreme deciles split by 'had a lock day in the last 15 days'")
    for nm, sl in (("train", tr), ("valid", va)):
        okS = lab[sl] & np.isfinite(F[sl])
        dc = decile_of(F[sl], okS)
        t_s = tgt[sl]
        ew_s = np.nansum(np.where(okS, t_s, 0.0), 1) / np.maximum(okS.sum(1), 1)
        ex_s = t_s - ew_s[:, None]
        for d, legname in ((9, "D10 short leg"), (0, "D1 long leg")):
            m = dc == d
            tot = m.sum()
            say(f"  [{nm}] {legname}: mean excess {np.nanmean(ex_s[m]) * 252 * 100:+.1f}%/yr over {tot} name-days")
            g_up = m & up15[sl]
            g_dn = m & dn15[sl] & ~up15[sl]
            g_no = m & ~up15[sl] & ~dn15[sl]
            for gname, g in (("up-lock in 15d", g_up), ("down-lock only", g_dn), ("no lock", g_no)):
                if g.sum() == 0:
                    continue
                say(f"       {gname:<16} share {g.sum() / tot:6.1%}  excess {np.nanmean(ex_s[g]) * 252 * 100:+7.1f}%/yr  -> contributes {np.nansum(ex_s[g]) / tot * 252 * 100:+6.1f} pts")
            # inside "no lock": stale (Zmin15 small) vs hyper-active (K mean negative)
            zmin_s, ks_s = Zmin15[sl], Ks15[sl]
            for gname, g in (("no lock & Kmean15>0 (stale side)", g_no & (ks_s > 0)), ("no lock & Kmean15<=0 (active side)", g_no & (ks_s <= 0))):
                if g.sum() == 0:
                    continue
                say(f"       {gname:<34} share {g.sum() / tot:6.1%}  excess {np.nanmean(ex_s[g]) * 252 * 100:+7.1f}%/yr")
    say("  books (same convention as the tables; sign and half-life fitted on train):")
    anylock = up15 | dn15
    book_line("F", st, F)
    book_line("F, lock names removed", st, np.where(anylock, np.nan, F))
    book_line("F, only lock names", st, np.where(anylock, F, np.nan))
    lockfrac = roll(np.fmax(np.where(lock_up, athi, 0.0), np.where(lock_dn, atlo, 0.0)).astype(np.float32), 15, "sum")
    book_line("lock time in 15d (naive)", st, lockfrac.astype(np.float64))
    book_line("-cross_mean(Z,15)", st, -Zmean15.astype(np.float64))
    book_line("-cross_min(Z,15)", st, -Zmin15.astype(np.float64))
    book_line("cross_mean(K,15) signed", st, Ks15)
    book_line("cross_max(K,15) signed", st, Kmax15)
    book_line("cross_max(K^2,15)", st, M15)
    book_line("cross_sum((K+3)^2,15)", st, Kp15)
    book_line("cross_mean(|K|,15)", st, Ka15)

    # ------------------------------------------------------------------ 8. conditional IC
    say("\n" + "=" * 100 + "\n§8  rank IC of F (raw sign) inside quintiles of activity and of price (train)")
    for gname, g in (("cross_mean(Z,15)", Zmean15), ("ctl_price", ctl["ctl_price"]), ("ctl_turnrate", ctl["ctl_turnrate"])):
        rows = dg.conditional_ic(F[tr], tgt[tr], g[tr], 5)
        say(f"  gate {gname:<18} " + "  ".join(f"Q{r['bucket'] + 1} {r['rank_ic']:+.4f}" for r in rows))
    rows = dg.conditional_ic(Ks15[tr], tgt[tr], Zmean15[tr], 5)
    say(f"  signed cross_mean(K,15) | gate Zmean15  " + "  ".join(f"Q{r['bucket'] + 1} {r['rank_ic']:+.4f}" for r in rows))
    say(f"\ndone in {time.time() - T0:.0f}s")
