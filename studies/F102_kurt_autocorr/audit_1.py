"""audit_1 -- reviewer's refutation attempt (train / valid only, never the holdout).

The claim under attack: the recommended cross_max(pow_2(K), 60) "is not a known exposure, and its LONG leg in
particular is not" -- evidence: nine controls span R^2 0.186 of it and the residual keeps a long-leg gross excess of
+11.1% (train).  But every one of those nine controls lives at a 1-day or 20-day horizon (today's intraday vol /
range / return / amount / turnover, 20-day momentum, 20-day daily vol), while the factor is a 60-day extreme.  The
competing reading that was never tested: the factor is a 60-day "quiet stock / no lottery day" exposure
(MAX effect, 60-day realised vol, 60-day max range, 60-day limit-up proxy, 60-day turnover) -- a textbook family --
and the 1d/20d controls simply cannot span it because of the horizon mismatch.

It predicts: (a) adding naive 60-day controls lifts R^2 well above 0.19; (b) the residual's long-leg gross excess and
rank IC collapse on BOTH train and valid; (c) a naive 60-day control traded on its own has a comparable long leg;
(d) inside quintiles of the naive control the factor's long decile earns little.
If instead the residual long leg stays near +10% and the naive factors have no long leg, the claim survives.

The same test is run on the original (15-day sum) with 15-day naive controls.
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
        if how in ("sum", "mean", "std"):
            z = np.where(fin, sh, 0.0)
            acc = z if acc is None else acc + z
            if how == "std":
                sq = z * z if sq is None else sq + z * z
        elif how == "max":
            acc = sh if acc is None else np.fmax(acc, sh)
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


A = "nt_ts_autocorr_s1(Ret, 3)"
EXPR = {
    "F": f"cross_sum(pow_2(day_kurt({A})), 15)",
    "M60": f"cross_max(pow_2(day_kurt({A})), 60)",
    "athi": "day_mean(eq(Close, in_max(High)))",
}
BASE9 = ("ctl_amt", "ctl_price", "ctl_ivol", "ctl_range", "ctl_rev1", "ctl_mom20", "ctl_dvol20", "ctl_cap", "ctl_turnrate")

with Study(FID) as st:
    P = st.panels(EXPR)
    say("missing panels:", [k for k in EXPR if k not in P])
    F = np.asarray(P["F"], dtype=np.float64)
    M60 = np.asarray(P["M60"], dtype=np.float64)
    athi = np.asarray(P["athi"], dtype=np.float32)
    ctl = {n: np.asarray(st.control(n), dtype=np.float32) for n in BASE9}
    tgt = st.target()
    tr, va = st.slice("train"), st.slice("valid")
    lab = np.isfinite(tgt)
    say(f"panels ready at {time.time() - T0:.0f}s; rows train {tr}, valid {va}")
    assert tr.start == 0 and va.start == tr.stop
    ALL = slice(tr.start, va.stop)
    SPL = (("train", slice(0, tr.stop - tr.start)), ("valid", slice(va.start - tr.start, va.stop - tr.start)))

    with np.errstate(invalid="ignore", divide="ignore"):
        lr = np.log(ctl["ctl_rev1"].astype(np.float64)).astype(np.float32)
    lr[~np.isfinite(lr)] = np.nan

    def naive(d):
        return {
            f"maxret{d}": roll(lr, d, "max"),                      # MAX effect: best single day
            f"maxabsret{d}": roll(np.abs(lr), d, "max"),           # most extreme single day
            f"vol{d}": roll(lr, d, "std"),                         # realised daily vol
            f"maxrange{d}": roll(ctl["ctl_range"], d, "max"),      # widest intraday range
            f"ivol{d}": roll(ctl["ctl_ivol"], d, "mean"),          # mean intraday vol
            f"turn{d}": roll(ctl["ctl_turnrate"], d, "mean"),      # mean log turnover rate
            f"amt{d}": roll(ctl["ctl_amt"], d, "mean"),            # mean log amount
            f"athi{d}": roll(athi, d, "max"),                      # limit-up-lock proxy (share of minutes at the day high)
        }

    H60, H15 = naive(60), naive(15)
    say(f"naive controls built at {time.time() - T0:.0f}s")

    tgt_a = tgt[ALL]
    zc = {k: dg._zrank(np.asarray(v[ALL], dtype=np.float64)) for k, v in {**ctl, **H60, **H15}.items()}
    say(f"control ranks ready at {time.time() - T0:.0f}s")

    def resid_rows(tag, sig, sets):
        """sig = traded signal (sign x panel, smoothed), full rows.  Prints, per split, what each control set leaves."""
        y_all = dg._zrank(np.asarray(sig[ALL], dtype=np.float64))
        say(f"\n  -- {tag}")
        say(f"  {'control set':<34} | " + " | ".join(f"{nm}: R2    rIC   LSgross  Lgross   short " for nm, _ in SPL))
        row = f"  {'(not neutralised)':<34} | "
        for nm, sl in SPL:
            s_ = np.asarray(sig[ALL], dtype=np.float64)[sl]
            ic = dg.ic_row(s_, tgt_a[sl], sign=1.0)["rank_ic"]
            b = bk.book_row(s_, tgt_a[sl], slice(0, s_.shape[0]))
            row += f"{nm}:  —   {ic:+.4f}  {b['ls_gross_sharpe']:+5.2f}  {b['long_gross_ann'] * 100:+6.1f}%  {b['short_gross_ann'] * 100:+6.1f}% | "
        say(row)
        for sname, keys in sets.items():
            row = f"  {sname:<34} | "
            for nm, sl in SPL:
                res, info = dg.neutralise(y_all[sl], {k: zc[k][sl] for k in keys}, panel_ready=True, controls_ready=True)
                ic = dg.ic_row(res, tgt_a[sl], sign=1.0)["rank_ic"]
                b = bk.book_row(res, tgt_a[sl], slice(0, res.shape[0]))
                row += (f"{nm}: {info['mean_r2']:.3f} {ic:+.4f}  {b['ls_gross_sharpe']:+5.2f}  {b['long_gross_ann'] * 100:+6.1f}%  "
                        f"{b['short_gross_ann'] * 100:+6.1f}% | ")
            say(row)

    def line(name, panel, sign=None):
        p = np.asarray(panel, dtype=np.float64)
        sg = st.sign(p, "train") if sign is None else sign
        b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
        t_, v_ = b["splits"]["train"], b["splits"]["valid"]
        say(f"  {name:<28} sgn {sg:+.0f} hl {b['hl_used']:<3g} LS {t_['ls_sharpe']:+.2f}/{v_['ls_sharpe']:+.2f} "
            f"Lg {t_['long_gross_ann'] * 100:+5.1f}/{v_['long_gross_ann'] * 100:+5.1f} "
            f"Ln {t_['long_ann'] * 100:+5.1f}/{v_['long_ann'] * 100:+5.1f} "
            f"Lsh {t_['long_sharpe']:+.2f}/{v_['long_sharpe']:+.2f} sh {t_['short_gross_ann'] * 100:+5.1f}/{v_['short_gross_ann'] * 100:+5.1f} "
            f"TO {t_['ls_turnover'] * 100:4.1f}%")
        return sg

    # ------------------------------------------------------------------ 1. spanning
    say("\n" + "=" * 118 + "\n§1  what is left of the TRADED signal after controls (rank space, daily regression; residual not re-smoothed)")
    say("    self-check: the 'base9' train row of cross_max(K^2,60) must reproduce the s3 table: R2 0.186, rIC +0.0115, LSgross +2.76, Lgross +11.1%, short +2.3%")
    k60, k15 = tuple(H60), tuple(H15)
    resid_rows("cross_max(K^2,60), sign -1, hl 0", -M60, {
        "base9": BASE9,
        "base9 + eight 60d naive": BASE9 + k60,
        "eight 60d naive only": k60,
        "base9 + vol60 + maxabsret60": BASE9 + ("vol60", "maxabsret60"),
        **{f"{k} alone": (k,) for k in k60},
    })
    resid_rows("original cross_sum(K^2,15), sign -1, hl 1", bk.smoothed(-F, 1), {
        "base9": BASE9,
        "base9 + eight 15d naive": BASE9 + k15,
        "base9 + eight 60d naive": BASE9 + k60,
        **{f"{k} alone": (k,) for k in k15},
    })

    # ------------------------------------------------------------------ 2. the naive things as factors
    say("\n" + "=" * 118 + "\n§2  the naive 60-day quantities traded on their own (same books; sign and half-life fitted on train)")
    line("cross_max(K^2,60)", M60)
    signs = {}
    for k, v in H60.items():
        signs[k] = line(k, v)
    comp = sum(dg._zrank(np.asarray(H60[k], dtype=np.float64)) for k in ("maxabsret60", "vol60", "maxrange60", "ivol60", "turn60"))
    signs["quiet60"] = line("quiet60 = rank-sum of 5", comp)
    say("  Spearman with cross_max(K^2,60) (train): " + "  ".join(
        f"{k} {dg.pair_rank_corr(M60[tr], np.asarray(v[tr], dtype=np.float64)):+.2f}" for k, v in {**H60, 'quiet60': comp}.items()))
    say("  share of the factor's LONG decile (lowest max K^2) that is also in the naive quantity's lowest decile (train / valid; 0.10 = chance):")
    for k, v in {**H60, "quiet60": comp}.items():
        out = []
        for sl in (tr, va):
            ok = lab[sl] & np.isfinite(M60[sl]) & np.isfinite(v[sl])
            dm, dh = decile_of(M60[sl], ok), decile_of(v[sl], ok)
            out.append(float((dh[dm == 0] == 0).mean()))
        say(f"    {k:<14} {out[0]:.3f} / {out[1]:.3f}")

    # ------------------------------------------------------------------ 3. double sort on the naive quantities
    say("\n" + "=" * 118 + "\n§3  the factor's long decile formed INSIDE each quintile of a naive 60-day quantity, vs that quintile's equal weight (annualised %, gross)")
    rowid = np.arange(M60.shape[0])[:, None] + np.zeros((1, M60.shape[1]), dtype=np.int64)
    warm = rowid >= 60
    for gname in ("vol60", "maxabsret60", "maxrange60", "athi60", "quiet60"):
        g = comp if gname == "quiet60" else np.asarray(H60[gname], dtype=np.float64)
        for label_, panel in (("cross_max(K^2,60)", M60), ("original", F)):
            outs = []
            for sl in (tr, va):
                ok = lab[sl] & np.isfinite(panel[sl]) & np.isfinite(g[sl]) & warm[sl]
                gq = decile_of(g[sl], ok, n=5)
                t_s = tgt[sl]
                res = []
                for q in range(5):
                    inq = ok & (gq == q)
                    dq = decile_of(panel[sl], inq)
                    ewq = np.nansum(np.where(inq, t_s, 0.0), 1) / np.maximum(inq.sum(1), 1)
                    exq = t_s - ewq[:, None]
                    res.append(np.nanmean(exq[dq == 0]) * 25200)
                outs.append(" ".join(f"{x:+6.1f}" for x in res))
            say(f"  gate {gname:<12} {label_:<18} train Q1..Q5: {outs[0]}   valid: {outs[1]}")
    say("  (reference, no gate) the factor's long decile vs the full equal weight, same rows:")
    for label_, panel in (("cross_max(K^2,60)", M60), ("original", F)):
        outs = []
        for sl in (tr, va):
            ok = lab[sl] & np.isfinite(panel[sl]) & warm[sl]
            d_ = decile_of(panel[sl], ok)
            t_s = tgt[sl]
            ew = np.nansum(np.where(ok, t_s, 0.0), 1) / np.maximum(ok.sum(1), 1)
            outs.append(f"{np.nanmean((t_s - ew[:, None])[d_ == 0]) * 25200:+6.1f}")
        say(f"    {label_:<18} train {outs[0]}   valid {outs[1]}")
    say(f"\ndone in {time.time() - T0:.0f}s")
