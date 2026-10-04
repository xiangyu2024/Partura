"""r1 -- revision after the two reviews (train / valid only, never the holdout; no candidate is changed).

Three review points, three things to measure:

  A  (review 3) "the recommended cross_max(K^2,60) is not a known exposure, its long leg in particular" rested on nine
     controls that all live at a 1-day / 20-day horizon, on train only.  The reviewer's audit_1 added eight naive
     60-day quantities: R^2 0.186 -> 0.454, residual long-leg gross +11.1% -> +4.3% (train), +7.2% -> +3.9% (valid).
     What audit_1 did not separate: seven of those eight are textbook style exposures (vol, MAX, range, intraday vol,
     turnover, amount); the eighth, athi60, is the naive proxy of the factor's OWN event (the limit-up lock that makes
     K >> 0).  Section 1 runs the ladder  base9 -> +style7 -> +athi60 -> +all eight  on train AND valid, for the
     recommended, the 30-day version, the original, and the original at the long-only half-life.
     Self-check: the 'base9' and 'base9 + eight' rows must reproduce audit_1's numbers.

  B  (review 3) "about 45% of the long-leg excess is avoiding names that locked in the last 60 days" was read off a
     double sort (the factor's long decile formed inside each athi60 quintile).  Section 2 measures it on the long
     decile the book actually holds: every held name's excess over the universe is split, exactly, into
         allocation = (equal weight of the name's bucket) - (equal weight of the universe)     "which bucket it sits in"
         selection  = (the name's return) - (equal weight of its bucket)                       "which name inside it"
     for buckets of athi60, of the strict lock flag of x3, of the clean universe of x3, and of the style quantities.
     Self-check: allocation + selection == total, and the pooled total reproduces audit_1's +14.5 / +13.5.

     Two further cuts of the same question: the rankings INSIDE x3's clean universe (benchmark = the clean universe's own
     equal weight), and the 60-day extreme recomputed with the lock days removed from K (a ranking blind to the event).

  C  (reviews 1, 2) the headline compared f_max60 with the original at hl=1 -- a half-life chosen for the SHORT leg.
     The holdout numbers at the long-only half-life are already in final.json (no new read).  What final.json cannot
     give is the standard error of "60-day extreme minus original at hl=5": that needs the two daily long-book series.
     Section 3 prints every candidate at every fixed half-life on train / valid, and for the pairs that matter the
     paired difference of the daily net long-book excess: mean, t, and the correlation of the two series (the reviewer
     assumed 0.6; this measures it, on train / valid).  Section 4 engine-expressed 60-day controls (the ones SR_horizon
     put in the config) on valid, so the report's train table has its valid counterpart.
"""
import time
import traceback

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F102_kurt_autocorr"
T0 = time.time()
ANN = 252.0


def say(*a):
    print(*a, flush=True)


def roll(x, d, how):
    """Trailing d-row statistic that skips missing days (same code as audit_1 / x3)."""
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
    if how == "mean":
        return np.where(cnt > 0, acc / np.maximum(cnt, 1), np.nan)
    if how == "std":
        m = acc / np.maximum(cnt, 1)
        v = sq / np.maximum(cnt, 1) - m * m
        return np.where(cnt > 1, np.sqrt(np.maximum(v, 0.0)), np.nan)
    return acc


def decile_of(panel, ok, n=10):
    """Within-day quantile bucket (0 = lowest) of `panel` among the cells where `ok`; NaN elsewhere."""
    p = np.where(ok, panel, np.nan).astype(np.float64)
    r = dg.rank_rows(p)
    cnt = np.isfinite(r).sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        return np.floor((r - 1.0) / np.maximum(cnt, 1) * n)


def attribution(sig, bid, nb, tgt, lab, warm, sl):
    """Allocation / selection split of the long decile of `sig` (higher = long) against buckets `bid` (0..nb-1, NaN =
    not bucketed).  Returns annualised % (day-averaged): total, allocation, selection, the pooled total, the share of
    the long decile in each bucket, each bucket's share of the universe and each bucket's equal weight minus the
    universe's."""
    s, t, b = sig[sl], tgt[sl], bid[sl]
    ok = lab[sl] & np.isfinite(s) & np.isfinite(b) & warm[sl]
    long_ = decile_of(-s, ok) == 0
    tz = np.where(ok, t, 0.0)
    n_all = ok.sum(1)
    ew_all = np.where(n_all > 0, tz.sum(1) / np.maximum(n_all, 1), np.nan)
    ew_cell = np.full(s.shape, np.nan)
    share_long, share_univ, bucket_ex = [], [], []
    for k in range(nb):
        m = ok & (b == k)
        nk = m.sum(1)
        ewk = np.where(nk > 0, (tz * m).sum(1) / np.maximum(nk, 1), np.nan)
        ew_cell = np.where(m, ewk[:, None], ew_cell)
        share_long.append(float((long_ & m).sum() / max(int(long_.sum()), 1)))
        share_univ.append(float(m.sum() / max(int(ok.sum()), 1)))
        bucket_ex.append(float(np.nanmean(ewk - ew_all) * ANN * 100))
    nl = long_.sum(1)
    day = nl > 0
    tot = np.where(long_, t - ew_all[:, None], 0.0).sum(1) / np.maximum(nl, 1)
    alc = np.where(long_, ew_cell - ew_all[:, None], 0.0).sum(1) / np.maximum(nl, 1)
    sel = np.where(long_, t - ew_cell, 0.0).sum(1) / np.maximum(nl, 1)
    f = lambda v: float(np.nanmean(v[day]) * ANN * 100)                      # noqa: E731
    pooled = float(np.nanmean((t - ew_all[:, None])[long_]) * ANN * 100)
    return {"total": f(tot), "alloc": f(alc), "select": f(sel), "pooled": pooled,
            "share_long": share_long, "share_univ": share_univ, "bucket_ex": bucket_ex}


def long_series(sm, tgt, sl, cost=bk.COST, top=bk.TOP_FRAC):
    """Daily net / gross excess of the long leg as a pure long book on `sl` (book started empty), as in partura.books."""
    s, t = sm[sl], tgt[sl]
    w = bk.long_short_weights(s, top)
    net, gross, turn = bk.long_book(w, s, t, cost)
    return net, gross, turn


def paired(a, b):
    """a - b of two daily series: annualised mean diff (%), t, correlation, each one's annualised vol (%), n."""
    m = np.isfinite(a) & np.isfinite(b)
    x, y = a[m], b[m]
    d = x - y
    n = d.size
    if n < 30 or d.std() == 0:
        return None
    return {"diff": float(d.mean() * ANN * 100), "t": float(d.mean() / d.std(ddof=1) * np.sqrt(n)),
            "rho": float(np.corrcoef(x, y)[0, 1]), "vol_a": float(x.std(ddof=1) * np.sqrt(ANN) * 100),
            "vol_b": float(y.std(ddof=1) * np.sqrt(ANN) * 100), "ann_a": float(x.mean() * ANN * 100),
            "ann_b": float(y.mean() * ANN * 100), "n": int(n)}


A = "nt_ts_autocorr_s1(Ret, 3)"
EXPR = {
    "F": f"cross_sum(pow_2(day_kurt({A})), 15)",
    "MA15": f"cross_mean(abs_(day_kurt({A})), 15)",
    "M15": f"cross_max(pow_2(day_kurt({A})), 15)",
    "M30": f"cross_max(pow_2(day_kurt({A})), 30)",
    "M60": f"cross_max(pow_2(day_kurt({A})), 60)",
    "K": f"day_kurt({A})",
    "Z": f"day_mean(abs_(sign({A})))",
    "athi": "day_mean(eq(Close, in_max(High)))",
    "atlo": "day_mean(eq(Close, in_min(Low)))",
}
BASE9 = ("ctl_amt", "ctl_price", "ctl_ivol", "ctl_range", "ctl_rev1", "ctl_mom20", "ctl_dvol20", "ctl_cap", "ctl_turnrate")
ENG60 = ("ctl_athi60", "ctl_ivol60", "ctl_amt60", "ctl_maxrange60", "ctl_dvol60", "ctl_maxret60", "ctl_maxabsret60")


def main(st):
    P = st.panels(EXPR)
    say("missing panels:", [k for k in EXPR if k not in P])
    F, MA15, M15, M30, M60 = (np.asarray(P[k], dtype=np.float64) for k in ("F", "MA15", "M15", "M30", "M60"))
    K = np.asarray(P["K"], dtype=np.float64)
    Z = np.asarray(P["Z"], dtype=np.float32)
    athi, atlo = np.asarray(P["athi"], dtype=np.float32), np.asarray(P["atlo"], dtype=np.float32)
    ctl = {n: np.asarray(st.control(n), dtype=np.float32) for n in BASE9}
    tgt = st.target()
    tr, va = st.slice("train"), st.slice("valid")
    lab = np.isfinite(tgt)
    years = np.array([int(str(d)[:4]) for d in st.dates])
    say(f"panels ready at {time.time() - T0:.0f}s; rows train {tr}, valid {va}")
    assert tr.start == 0 and va.start == tr.stop
    ALL = slice(tr.start, va.stop)
    SPL = (("train", slice(0, tr.stop - tr.start)), ("valid", slice(va.start - tr.start, va.stop - tr.start)))
    rowid = np.arange(K.shape[0])[:, None] + np.zeros((1, K.shape[1]), dtype=np.int64)
    warm = rowid >= 60

    with np.errstate(invalid="ignore", divide="ignore"):
        lr = np.log(ctl["ctl_rev1"].astype(np.float64)).astype(np.float32)
    lr[~np.isfinite(lr)] = np.nan

    def naive(d):                                                   # the reviewer's eight, same construction
        return {
            f"maxret{d}": roll(lr, d, "max"),
            f"maxabsret{d}": roll(np.abs(lr), d, "max"),
            f"vol{d}": roll(lr, d, "std"),
            f"maxrange{d}": roll(ctl["ctl_range"], d, "max"),
            f"ivol{d}": roll(ctl["ctl_ivol"], d, "mean"),
            f"turn{d}": roll(ctl["ctl_turnrate"], d, "mean"),
            f"amt{d}": roll(ctl["ctl_amt"], d, "mean"),
            f"athi{d}": roll(athi, d, "max"),
        }

    H60, H15 = naive(60), naive(15)
    # x3's definitions: a lock day = >= 30% of the minutes closed at the day's high (low) and the day moved >= 4.5%
    r1 = ctl["ctl_rev1"].astype(np.float64)
    uplock = (athi >= 0.3) & (r1 >= 1.045)
    dnlock = (atlo >= 0.3) & (r1 <= 0.955)
    lockday = uplock | dnlock
    lock60 = roll(lockday.astype(np.float32), 60, "max") > 0
    n60 = roll(K, 60, "count")
    Zmin60 = roll(Z, 60, "min")
    clean = (~lock60) & (n60 >= 60) & (Zmin60 >= 0.5)
    # the 60-day extreme with the lock days themselves taken out of K: a ranking that cannot see the event
    M60x = np.asarray(roll(np.where(lockday, np.nan, K ** 2), 60, "max"), dtype=np.float64)
    say(f"naive controls built at {time.time() - T0:.0f}s; lock days {lockday[lab].mean():.4f} of labelled cells, lock60 {lock60[lab].mean():.3f}, clean {clean[lab].mean():.3f}")
    tgt_a = tgt[ALL]
    zc = {k: dg._zrank(np.asarray(v[ALL], dtype=np.float64)) for k, v in {**ctl, **H60, **H15}.items()}
    say(f"control ranks ready at {time.time() - T0:.0f}s")

    def resid_rows(tag, sig, sets, zctl=None):
        """What each control set leaves of the traded signal `sig` (sign x panel, smoothed), per split."""
        zz = zc if zctl is None else zctl
        s_all = np.asarray(sig[ALL], dtype=np.float64)
        y_all = dg._zrank(s_all)
        say(f"\n  -- {tag}")
        say(f"  {'control set':<34} | " + " | ".join(f"{nm}: R2    rIC   LSgross  Lgross   short " for nm, _ in SPL))
        row = f"  {'(not neutralised)':<34} | "
        for nm, sl in SPL:
            ic = dg.ic_row(s_all[sl], tgt_a[sl], sign=1.0)["rank_ic"]
            b = bk.book_row(s_all[sl], tgt_a[sl], slice(0, s_all[sl].shape[0]))
            row += (f"{nm}:  —   {ic:+.4f}  {b['ls_gross_sharpe']:+5.2f}  {b['long_gross_ann'] * 100:+6.1f}%  "
                    f"{b['short_gross_ann'] * 100:+6.1f}% | ")
        say(row)
        for sname, keys in sets.items():
            row = f"  {sname:<34} | "
            for nm, sl in SPL:
                res, info = dg.neutralise(y_all[sl], {k: zz[k][sl] for k in keys}, panel_ready=True, controls_ready=True)
                ic = dg.ic_row(res, tgt_a[sl], sign=1.0)["rank_ic"]
                b = bk.book_row(res, tgt_a[sl], slice(0, res.shape[0]))
                row += (f"{nm}: {info['mean_r2']:.3f} {ic:+.4f}  {b['ls_gross_sharpe']:+5.2f}  {b['long_gross_ann'] * 100:+6.1f}%  "
                        f"{b['short_gross_ann'] * 100:+6.1f}% | ")
            say(row)

    # ---------------------------------------------------------------------------------------------- 1. the ladder
    say("\n" + "=" * 118 + "\n§1  what each control set leaves of the TRADED signal (rank space, daily regression; residual not re-smoothed)")
    say("    self-check against audit_1 -- cross_max(K^2,60): base9  train 0.186 +0.0115 +2.76 +11.1% +2.3% | valid 0.167 +0.0051 +0.88 +7.2% -2.5%")
    say("                                                  base9 + eight  train 0.454 +0.0063 +1.80 +4.3% +4.5% | valid 0.461 +0.0038 +2.10 +3.9% +4.9%")
    k60, k15 = tuple(H60), tuple(H15)
    st7_60 = tuple(k for k in k60 if not k.startswith("athi"))
    st7_15 = tuple(k for k in k15 if not k.startswith("athi"))

    def ladder(sfx, style, allk):
        return {
            "base9": BASE9,
            f"base9 + style7 {sfx} (no athi)": BASE9 + style,
            f"base9 + athi{sfx[:-1]}": BASE9 + (f"athi{sfx[:-1]}",),
            f"base9 + eight {sfx}": BASE9 + allk,
            f"style7 {sfx} only": style,
            f"athi{sfx[:-1]} alone": (f"athi{sfx[:-1]}",),
        }

    try:
        resid_rows("cross_max(K^2,60), sign -1, hl 0   [recommended]", -M60, ladder("60d", st7_60, k60))
        resid_rows("cross_max(K^2,30), sign -1, hl 0", -M30, ladder("60d", st7_60, k60))
        resid_rows("original cross_sum(K^2,15), sign -1, hl 1", bk.smoothed(-F, 1), {**ladder("15d", st7_15, k15), "base9 + eight 60d": BASE9 + k60})
        resid_rows("original cross_sum(K^2,15), sign -1, hl 5   [the long-only half-life]", bk.smoothed(-F, 5),
                   {**ladder("15d", st7_15, k15), "base9 + eight 60d": BASE9 + k60})
    except Exception:
        say("§1 FAILED:\n" + traceback.format_exc())
    say(f"  [§1 done at {time.time() - T0:.0f}s]")

    # ---------------------------------------------------------------------------------------------- 2. attribution
    say("\n" + "=" * 118 + "\n§2  the long decile the book holds: excess over the universe = allocation (its buckets' equal weight - universe)"
        "\n    + selection (the name - its bucket's equal weight).  Annualised %, gross, day-averaged; rows >= 60; cells with a label.")
    say("    self-check: alloc + select = total; pooled total of cross_max(K^2,60) should be +14.5 / +13.5 (audit_1 §3, no gate)")
    try:
        sigs = {
            "cross_max(K^2,60) hl0": -M60,
            "max(K^2 with lock days removed,60) hl0": -M60x,
            "cross_max(K^2,30) hl0": -M30,
            "original hl1": bk.smoothed(-F, 1),
            "original hl5": bk.smoothed(-F, 5),
        }
        fixed = {                                       # bucket ids that do not depend on the signal
            "lock60 flag (x3: 0 = no lock day in 60d)": (lock60.astype(np.float64), 2),
            "clean universe (x3: 0 = clean)": ((~clean).astype(np.float64), 2),
        }
        quant = {
            "athi60 quintiles": (H60["athi60"], 5), "athi60 deciles": (H60["athi60"], 10),
            "ivol60 quintiles": (H60["ivol60"], 5), "vol60 quintiles": (H60["vol60"], 5),
            "maxabsret60 quintiles": (H60["maxabsret60"], 5), "turn60 quintiles": (H60["turn60"], 5),
            "amt60 quintiles": (H60["amt60"], 5), "cap quintiles": (ctl["ctl_cap"], 5),
        }
        for sname, sig in sigs.items():
            say(f"\n  -- {sname}")
            say(f"  {'buckets':<42} | train: total = alloc + select  (pooled) | valid: total = alloc + select  (pooled)")
            for bname, (g, nb) in {**fixed, **quant}.items():
                row = f"  {bname:<42} | "
                det = []
                for nm, sl in (("train", tr), ("valid", va)):
                    if bname in fixed:
                        bid = np.asarray(g, dtype=np.float64)
                    else:
                        okq = lab & np.isfinite(sig) & np.isfinite(g) & warm
                        bid = np.full(sig.shape, np.nan)
                        bid[sl] = decile_of(np.asarray(g[sl], dtype=np.float64), okq[sl], n=nb)
                    a = attribution(sig, bid, nb, tgt, lab, warm, sl)
                    row += f"{nm}: {a['total']:+6.1f} = {a['alloc']:+6.1f} + {a['select']:+6.1f}  ({a['pooled']:+6.1f}) | "
                    det.append(a)
                say(row)
                if bname.startswith(("athi60 quintiles", "lock60", "clean")):
                    for nm, a in zip(("train", "valid"), det):
                        say(f"      [{nm}] long decile's share per bucket: " + " ".join(f"{v:.3f}" for v in a["share_long"])
                            + "   universe: " + " ".join(f"{v:.3f}" for v in a["share_univ"])
                            + "   bucket EW - universe EW: " + " ".join(f"{v:+.1f}" for v in a["bucket_ex"]))
            # joint buckets: athi60 quintile x a style quintile (25 cells)
            for jn, g2 in (("athi60 x ivol60 (5x5)", H60["ivol60"]), ("athi60 x turn60 (5x5)", H60["turn60"])):
                row = f"  {jn:<42} | "
                for nm, sl in (("train", tr), ("valid", va)):
                    okq = lab & np.isfinite(sig) & np.isfinite(H60["athi60"]) & np.isfinite(g2) & warm
                    q1 = decile_of(np.asarray(H60["athi60"][sl], dtype=np.float64), okq[sl], n=5)
                    q2 = decile_of(np.asarray(g2[sl], dtype=np.float64), okq[sl], n=5)
                    bid = np.full(sig.shape, np.nan)
                    bid[sl] = q1 * 5 + q2
                    a = attribution(sig, bid, 25, tgt, lab, warm, sl)
                    row += f"{nm}: {a['total']:+6.1f} = {a['alloc']:+6.1f} + {a['select']:+6.1f}  ({a['pooled']:+6.1f}) | "
                say(row)
    except Exception:
        say("§2 FAILED:\n" + traceback.format_exc())
    say(f"  [§2 done at {time.time() - T0:.0f}s]")

    # ---------------------------------------------------------------------------------------------- 3. speed vs structure
    say("\n" + "=" * 118 + "\n§3  every candidate at every FIXED half-life (sign -1): after-cost L/S Sharpe, long-leg net excess, long-only Sharpe, long book's one-sided turnover")
    say("    self-check: original hl1 = LS +3.68/+3.88, Lnet +4.9%/+4.5%;  cross_max(K^2,60) hl0 = +3.37/+3.32, +11.3%/+10.1% (s3.json / final.json)")
    cands = {"original sum(K^2,15)": F, "mean(|K|,15)": MA15, "max(K^2,15)": M15, "max(K^2,30)": M30, "max(K^2,60)": M60,
             # the same rankings INSIDE x3's clean universe (no lock day in 60d, full history, no zombie day): the benchmark is
             # then the clean universe's own equal weight, so "avoiding the event names" earns nothing here
             "original | clean universe": np.where(clean, F, np.nan), "max(K^2,30) | clean universe": np.where(clean, M30, np.nan),
             "max(K^2,60) | clean universe": np.where(clean, M60, np.nan),
             # the 60-day extreme that cannot see the lock days (they are removed from K before the max)
             "max(K^2 ex lock days,60)": M60x}
    HL = (0, 1, 2, 3, 5, 10, 20)
    series = {}
    try:
        for cn, p in cands.items():
            say(f"\n  -- {cn}")
            say("   hl | LS tr/va      | Lnet tr/va        | Lgross tr/va      | Lsharpe tr/va | long TO tr")
            for hl in HL:
                sm = bk.smoothed(-p, hl)
                a_, c_ = bk.book_row(sm, tgt, tr), bk.book_row(sm, tgt, va)
                say(f"   {hl:>2} | {a_['ls_sharpe']:+.2f} / {c_['ls_sharpe']:+.2f} | {a_['long_ann'] * 100:+6.2f}% / {c_['long_ann'] * 100:+6.2f}% | "
                    f"{a_['long_gross_ann'] * 100:+6.2f}% / {c_['long_gross_ann'] * 100:+6.2f}% | {a_['long_sharpe']:+.2f} / {c_['long_sharpe']:+.2f} | {a_['long_turnover'] * 100:5.2f}%")
                for nm, sl in (("train", tr), ("valid", va), ("utrain", ALL)):
                    series[(cn, hl, nm)] = long_series(sm, tgt, sl)
    except Exception:
        say("§3 grid FAILED:\n" + traceback.format_exc())

    say("\n  paired differences of the daily long-book NET excess, a - b (annualised %, t = mean/sd*sqrt(n), rho = correlation of the two daily series):")
    O, X15, X30, X60, MA = "original sum(K^2,15)", "max(K^2,15)", "max(K^2,30)", "max(K^2,60)", "mean(|K|,15)"
    pairs = [
        ("headline: max60@hl0 - original@hl1", (X60, 0), (O, 1)),
        ("speed only: original@hl5 - original@hl1", (O, 5), (O, 1)),
        ("structure at the fair baseline: max60@hl0 - original@hl5", (X60, 0), (O, 5)),
        ("structure, both at hl_long (utrain): max60@hl2 - original@hl5", (X60, 2), (O, 5)),
        ("max60@hl0 - original@hl10", (X60, 0), (O, 10)),
        ("max60@hl0 - mean|K|15@hl10", (X60, 0), (MA, 10)),
        ("max60@hl0 - max15@hl5", (X60, 0), (X15, 5)),
        ("30 vs 60 at hl_ls: max60@hl0 - max30@hl0", (X60, 0), (X30, 0)),
        ("30 vs 60 at hl_long: max60@hl2 - max30@hl5", (X60, 2), (X30, 5)),
        ("max30@hl5 - original@hl5", (X30, 5), (O, 5)),
        ("max30@hl0 - original@hl5", (X30, 0), (O, 5)),
        ("INSIDE the clean universe: max60@hl0 - original@hl5", ("max(K^2,60) | clean universe", 0), ("original | clean universe", 5)),
        ("INSIDE the clean universe: max60@hl0 - original@hl1", ("max(K^2,60) | clean universe", 0), ("original | clean universe", 1)),
        ("INSIDE the clean universe: max30@hl0 - original@hl5", ("max(K^2,30) | clean universe", 0), ("original | clean universe", 5)),
        ("INSIDE the clean universe: original@hl5 - original@hl1", ("original | clean universe", 5), ("original | clean universe", 1)),
        ("blind to lock days: max60@hl0 - max(ex lock days)60@hl0", (X60, 0), ("max(K^2 ex lock days,60)", 0)),
        ("blind to lock days vs the fair baseline: max(ex lock days)60@hl0 - original@hl5", ("max(K^2 ex lock days,60)", 0), (O, 5)),
    ]
    try:
        for label_, (ca, ha), (cb, hb) in pairs:
            say(f"  {label_}")
            for nm in ("train", "valid", "utrain"):
                for kind, idx in (("net", 0), ("gross", 1)):
                    r = paired(series[(ca, ha, nm)][idx], series[(cb, hb, nm)][idx])
                    if r is None:
                        continue
                    say(f"      [{nm:<6} {kind:<5}] a {r['ann_a']:+6.2f}%  b {r['ann_b']:+6.2f}%  diff {r['diff']:+6.2f}%  t {r['t']:+5.2f}  rho {r['rho']:+.3f}  "
                        f"vol a/b {r['vol_a']:.2f}% / {r['vol_b']:.2f}%  n {r['n']}")
        say("\n  the structure increment by calendar year (max60@hl0 - original@hl5, daily net long-book excess, utrain book; annualised %):")
        da = series[(X60, 0, "utrain")][0] - series[(O, 5, "utrain")][0]
        dh = series[(X60, 0, "utrain")][0] - series[(O, 1, "utrain")][0]
        ya = years[ALL]
        for y in sorted(set(ya.tolist())):
            m = (ya == y) & np.isfinite(da)
            if m.sum() < 20:
                continue
            say(f"      {y}: vs original@hl5 {da[m].mean() * ANN * 100:+6.2f}% (t {da[m].mean() / da[m].std(ddof=1) * np.sqrt(m.sum()):+.2f})   "
                f"vs original@hl1 {dh[m].mean() * ANN * 100:+6.2f}% (t {dh[m].mean() / dh[m].std(ddof=1) * np.sqrt(m.sum()):+.2f})   days {int(m.sum())}")
    except Exception:
        say("§3 pairs FAILED:\n" + traceback.format_exc())
    say(f"  [§3 done at {time.time() - T0:.0f}s]")

    # ---------------------------------------------------------------------------------------------- 4. engine controls on valid
    say("\n" + "=" * 118 + "\n§4  the engine-expressed 60-day controls SR_horizon put in the config (seven; turn60 cannot be written as an expression),"
        "\n    on train AND valid.  self-check: the train rows must equal the 'all_controls' rows of h_max60 / h_max30 / h_orig in runs/.../rev1.json")
    try:
        eng = {}
        for n in ENG60:
            try:
                eng[n] = np.asarray(st.control(n), dtype=np.float32)
            except Exception as exc:                               # a control the engine could not evaluate
                say(f"   {n}: not available ({type(exc).__name__}: {exc})")
        say("   available engine 60d controls: " + ", ".join(eng))
        ze = {**{k: zc[k] for k in BASE9}, **{k: dg._zrank(np.asarray(v[ALL], dtype=np.float64)) for k, v in eng.items()}}
        ek = tuple(eng)
        sets = {"base9": BASE9, f"base9 + engine {len(ek)}": BASE9 + ek}
        if "ctl_athi60" in eng:
            sets["base9 + engine, no athi60"] = BASE9 + tuple(k for k in ek if k != "ctl_athi60")
            sets["base9 + ctl_athi60"] = BASE9 + ("ctl_athi60",)
        resid_rows("cross_max(K^2,60), sign -1, hl 0", -M60, sets, zctl=ze)
        resid_rows("cross_max(K^2,30), sign -1, hl 0", -M30, sets, zctl=ze)
        resid_rows("original cross_sum(K^2,15), sign -1, hl 1", bk.smoothed(-F, 1), sets, zctl=ze)
        say("\n   Spearman of the engine controls with their numpy twins (train): " + "  ".join(
            f"{a}~{b} {dg.pair_rank_corr(np.asarray(eng[a][tr], dtype=np.float64), np.asarray(H60[b][tr], dtype=np.float64)):+.3f}"
            for a, b in (("ctl_athi60", "athi60"), ("ctl_ivol60", "ivol60"), ("ctl_amt60", "amt60"), ("ctl_maxrange60", "maxrange60"),
                         ("ctl_dvol60", "vol60"), ("ctl_maxret60", "maxret60"), ("ctl_maxabsret60", "maxabsret60")) if a in eng))
        say("   Spearman with cross_max(K^2,60) (train / valid): " + "  ".join(
            f"{k} {dg.pair_rank_corr(M60[tr], np.asarray(v[tr], dtype=np.float64)):+.2f}/{dg.pair_rank_corr(M60[va], np.asarray(v[va], dtype=np.float64)):+.2f}"
            for k, v in {**eng, "turn60(numpy)": H60["turn60"]}.items()))
    except Exception:
        say("§4 FAILED:\n" + traceback.format_exc())
    say(f"\ndone in {time.time() - T0:.0f}s")


if __name__ == "__main__":
    with Study(FID) as st_:
        main(st_)
