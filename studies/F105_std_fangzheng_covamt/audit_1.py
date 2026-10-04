"""F105 audit (reviewer, mechanism / overfitting lens).  train / valid only -- never the holdout.

The study recommends cross_max(day_std(Amt), 30) over the original because its long leg nets more.
Four explanations the study did not exclude, each with a number that can kill it:

  0  semantics      server source of the NaN-aware reducers; is D finite (0) where the stock has no data?
  1  half-life      is the long-leg advantage structure, or only the half-life the L/S rule happened to pick?
                    (every variant at hl 0 / 3 / 5 / 10, on train AND valid; known9@hl5 vs max30@hl0)
  2  listing age    does the advantage survive dropping names with < 247 observations from the universe?
                    what do the young names inside max30's long decile earn?  which boards are in the long decile?
  3  direction      "the direction of the event carries no information": scale-free relative change D/C,
                    split by the sign of the 5-day change of C, inside the same |D/C| bucket (mature names only)
  4  subsumption    the study's "original is contained in the known family" regressions, repeated on VALID
"""
import inspect
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F105_std_fangzheng_covamt"
A = "day_cov(Amt, Amt)"
C = f"cross_fangzheng(cross_max({A}, 3), 241)"
EXPR = {
    "orig":   f"ts_stddev({C}, 5)",
    "C":      C,
    "A":      A,
    "min3":   "cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)",
    "max15":  "cross_max(day_std(Amt), 15)",
    "max30":  "cross_max(day_std(Amt), 30)",
    "max60":  "cross_max(day_std(Amt), 60)",
    "known9": "cross_max(day_std(Amt), 9)",
}
FACTORS = ("orig", "min3", "known9", "max15", "max30", "max60")
HL_FIT = {"orig": 3.0, "min3": 3.0, "known9": 0.0, "max15": 0.0, "max30": 0.0, "max60": 0.0}
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def pct(x):
    return dg._zrank(np.asarray(x, dtype=np.float64)) + 0.5


def fmt(b):
    return (f"LS {b['ls_sharpe']:+.2f}  Lgross {b['long_gross_ann']:+.1%}  Lnet {b['long_ann']:+.1%}  Lshp {b['long_sharpe']:+.2f}"
            f"  short {b['short_gross_ann']:+.1%}  TO {b['ls_turnover']:.1%}")


def board(sym):
    d = "".join(ch for ch in str(sym) if ch.isdigit())[:6]
    if d[:3] in ("688", "689"):
        return "STAR"
    if d[:1] == "3":
        return "ChiNext"
    if d[:1] in ("4", "8") or d[:2] == "92":
        return "BSE"
    if d[:1] == "6":
        return "SH"
    if d[:1] == "0":
        return "SZ"
    return "other"


with Study(FID) as st:
    P = {k: np.asarray(v, dtype=np.float64) for k, v in st.panels(EXPR).items()}
    tgt = st.target()
    tr, va = st.slice("train"), st.slice("valid")
    SPL = (("train", tr), ("valid", va))
    amt = np.asarray(st.control("ctl_amt"), dtype=np.float64)
    cap = np.asarray(st.control("ctl_cap"), dtype=np.float64)
    amt_p, cap_p = pct(amt), pct(cap)
    say(f"panels ready {time.time() - T0:.0f}s; train {tr}, valid {va}; symbols {len(st.symbols)}")
    sm_cache = {}

    def sig(k, hl):
        if (k, hl) not in sm_cache:
            sm_cache[(k, hl)] = bk.smoothed(-P[k], hl)
        return sm_cache[(k, hl)]

    for name, sl in SPL:
        say(f"  selfcheck [{name}] orig@3  {fmt(bk.book_row(sig('orig', 3.0), tgt, sl))}")
        say(f"  selfcheck [{name}] max30@0 {fmt(bk.book_row(sig('max30', 0.0), tgt, sl))}")

    # ------------------------------------------------------------------ 0 semantics
    say("\n== 0 semantics ==")
    try:
        from alphacube.operators import common as _c
        for fn in ("nanstd_last", "nanmax_last", "nanmean_last", "rolling_windows", "_stddev"):
            say(f"--- server source: {fn}\n{inspect.getsource(getattr(_c, fn))}")
    except Exception as exc:                                             # noqa: BLE001
        say(f"  (could not print reducer source: {exc})")
    a, d, c = P["A"], P["orig"], P["C"]
    ever = np.cumsum(np.isfinite(a), axis=0) > 0
    n_cum = np.cumsum(np.isfinite(P["known9"]), axis=0)
    young = n_cum < 247
    lab = np.isfinite(tgt)
    stop = va.stop
    say(f"  cells (train+valid): total {d[:stop].size}; D finite {np.isfinite(d[:stop]).sum()}; "
        f"D finite where the stock has never had a finite day_cov {(np.isfinite(d[:stop]) & ~ever[:stop]).sum()}; "
        f"D == 0 exactly {(d[:stop] == 0).sum()} (of which labelled {((d[:stop] == 0) & lab[:stop]).sum()}); "
        f"D finite & day_cov NaN today {(np.isfinite(d[:stop]) & ~np.isfinite(a[:stop])).sum()}")
    m30 = P["max30"]
    say(f"  max30 finite {np.isfinite(m30[:stop]).sum()}; max30 finite & day_cov NaN today {(np.isfinite(m30[:stop]) & ~np.isfinite(a[:stop])).sum()}; "
        f"max30 == 0 exactly {(m30[:stop] == 0).sum()}")
    for name, sl in SPL:
        for k in ("orig", "max30"):
            s = sig(k, HL_FIT[k])[sl]
            w = bk.long_short_weights(s, 0.10)
            lng, sht = w > 0, w < 0
            say(f"  [{name}] {k:<6} long decile: names/day {lng.sum(1).mean():.0f}; share with NO label {(lng & ~lab[sl]).sum() / max(lng.sum(), 1):.2%}"
                f"; share with day_cov NaN today {(lng & ~np.isfinite(a[sl])).sum() / max(lng.sum(), 1):.2%}"
                f"; young share {(lng & young[sl]).sum() / max(lng.sum(), 1):.2%}"
                f" | short decile: no label {(sht & ~lab[sl]).sum() / max(sht.sum(), 1):.2%}, young {(sht & young[sl]).sum() / max(sht.sum(), 1):.2%}")

    # ------------------------------------------------------------------ 1 half-life
    say("\n== 1 every factor at a FIXED half-life (sign -1), train and valid ==")
    for k in FACTORS:
        for hl in (0.0, 3.0, 5.0, 10.0):
            row = "   ".join(f"[{name}] {fmt(bk.book_row(sig(k, hl), tgt, sl))}" for name, sl in SPL)
            mark = " *fit" if hl == HL_FIT[k] else ""
            say(f"  {k:<6} hl {hl:>4.0f}{mark:<5} {row}")

    # ------------------------------------------------------------------ 2 listing age / boards
    say("\n== 2 drop names with < 247 observations from the universe, then rebuild the books ==")
    for k, hl in (("orig", 3.0), ("orig", 10.0), ("min3", 3.0), ("known9", 0.0), ("known9", 5.0), ("max15", 0.0),
                  ("max30", 0.0), ("max60", 0.0)):
        s = np.where(young, np.nan, sig(k, hl))
        row = "   ".join(f"[{name}] {fmt(bk.book_row(s, tgt, sl))}" for name, sl in SPL)
        say(f"  mature only  {k:<6} hl {hl:>4.0f}  {row}")
    say("  -- what the young names inside each long decile earn (excess vs equal-weight of scored+labelled names)")
    for name, sl in SPL:
        t = tgt[sl]
        for k in ("orig", "max30", "max60"):
            s = sig(k, HL_FIT[k])[sl]
            ok = np.isfinite(s) & np.isfinite(t)
            w = bk.long_short_weights(s, 0.10)
            lng = (w > 0)
            r = np.where(ok, t, 0.0)
            ew = r.sum(1) / np.maximum(ok.sum(1), 1)
            ex = np.where(ok, t - ew[:, None], 0.0)
            out = []
            for g, m in (("young", lng & young[sl]), ("mature", lng & ~young[sl])):
                cnt = m.sum(1)
                days = cnt >= 3
                mean_ex = ((ex * m).sum(1)[days] / cnt[days]).mean() * 252 if days.any() else float("nan")
                contrib = ((ex * m).sum(1) / np.maximum(lng.sum(1), 1)).mean() * 252
                with np.errstate(invalid="ignore"):
                    out.append(f"{g}: share {m.sum() / max(lng.sum(), 1):.1%}, names/day {cnt.mean():.1f}, mean excess {mean_ex:+.1%}/yr, "
                               f"contribution to the long leg {contrib:+.2%}/yr, amt pctile {np.nanmean(np.where(m, amt_p[sl], np.nan)):.2f}, "
                               f"cap pctile {np.nanmean(np.where(m, cap_p[sl], np.nan)):.2f}")
            say(f"  [{name}] {k:<6} " + " | ".join(out))
    try:
        boards = np.array([board(s) for s in st.symbols])
        say(f"  symbols sample: {list(map(str, st.symbols[:3]))} ... {list(map(str, st.symbols[-3:]))}")
        for name, sl in SPL:
            okc = np.isfinite(tgt[sl])
            base = {b: (okc & (boards == b)[None, :]).sum() / max(okc.sum(), 1) for b in sorted(set(boards.tolist()))}
            say(f"  [{name}] labelled universe by board: " + "  ".join(f"{b} {v:.1%}" for b, v in base.items()))
            for k in ("orig", "max30", "max60"):
                w = bk.long_short_weights(sig(k, HL_FIT[k])[sl], 0.10)
                lng = w > 0
                say(f"  [{name}] {k:<6} long decile by board: " + "  ".join(
                    f"{b} {(lng & (boards == b)[None, :]).sum() / max(lng.sum(), 1):.1%}" for b in base))
    except Exception as exc:                                             # noqa: BLE001
        say(f"  (board split failed: {exc})")
    say("  -- the two halves of the cap distribution (universe restricted; compare within a block)")
    for mname, m in (("cap pctile < 0.5", cap_p < 0.5), ("cap pctile >= 0.5", cap_p >= 0.5)):
        for k, hl in (("orig", 3.0), ("orig", 10.0), ("max30", 0.0), ("max60", 0.0)):
            s = np.where(m, sig(k, hl), np.nan)
            row = "   ".join(f"[{name}] {fmt(bk.book_row(s, tgt, sl))}" for name, sl in SPL)
            say(f"  [{mname:<17}] {k:<6} hl {hl:>4.0f}  {row}")

    # ------------------------------------------------------------------ 3 direction
    say("\n== 3 does the DIRECTION of the event carry information?  scale-free relative change, mature names only ==")
    with np.errstate(invalid="ignore", divide="ignore"):
        rel = np.where(c > 0, d / c, np.nan)
    dc = np.full_like(c, np.nan)
    dc[4:] = c[4:] - c[:-4]
    mature = ~young
    relm = np.where(mature, rel, np.nan)
    srel = np.sign(dc) * relm
    for name, sl in SPL:
        t = tgt[sl]
        ic_u = np.nanmean(dg.rank_ic_series(relm[sl], t))
        ic_s = np.nanmean(dg.rank_ic_series(srel[sl], t))
        up = np.where(dc[sl] > 0, relm[sl], np.nan)
        dn = np.where(dc[sl] < 0, relm[sl], np.nan)
        ic_up = np.nanmean(dg.rank_ic_series(up, np.where(np.isfinite(up), t, np.nan)))
        ic_dn = np.nanmean(dg.rank_ic_series(dn, np.where(np.isfinite(dn), t, np.nan)))
        say(f"  [{name}] rank IC: unsigned D/C {ic_u:+.4f}   signed sign(dC)*D/C {ic_s:+.4f}   "
            f"D/C inside C-rising names {ic_up:+.4f}   D/C inside C-falling names {ic_dn:+.4f}")
        ok = np.isfinite(relm[sl]) & np.isfinite(t)
        r = np.where(np.isfinite(t), t, 0.0)
        okall = np.isfinite(d[sl]) & np.isfinite(t)
        ew = np.where(okall, t, 0.0).sum(1) / np.maximum(okall.sum(1), 1)
        ex = np.where(np.isfinite(t), t - ew[:, None], 0.0)
        rk = dg.rank_rows(np.where(ok, relm[sl], np.nan))
        n = ok.sum(1, keepdims=True)
        with np.errstate(invalid="ignore"):
            q = np.minimum(np.floor((rk - 1.0) / np.maximum(n, 1) * 10), 9)
        for lo, hi, lbl in ((9, 9, "top decile of |D/C|"), (8, 8, "9th decile"), (5, 7, "deciles 6-8"), (0, 4, "bottom half")):
            cell = []
            for g, gm in (("C rising", dc[sl] > 0), ("C falling", dc[sl] < 0)):
                m = ok & (q >= lo) & (q <= hi) & gm
                cnt = m.sum(1)
                days = cnt >= 5
                mean_ex = ((ex * m).sum(1)[days] / cnt[days]).mean() * 252 if days.any() else float("nan")
                with np.errstate(invalid="ignore"):
                    cell.append(f"{g}: names/day {cnt.mean():6.1f}  excess {mean_ex:+6.1%}/yr  amt pctile {np.nanmean(np.where(m, amt_p[sl], np.nan)):.2f}")
            say(f"      [{name}] {lbl:<20} " + "   |   ".join(cell))
    say("  -- quantile profile of the signed relative change (sign -1: Q1 = C rose most, Q10 = C fell most), hl 0 and hl 5")
    for hl in (0.0, 5.0):
        s = bk.smoothed(-srel, hl)
        for name, sl in SPL:
            prof = bk.quantile_profile(s, tgt, sl)
            say(f"  hl {hl:.0f} [{name}] " + " ".join(f"{x['excess_ann']:+.1%}" for x in prof) + f"   | book: {fmt(bk.book_row(s, tgt, sl))}")
    s = bk.smoothed(-relm, 5.0)
    for name, sl in SPL:
        prof = bk.quantile_profile(s, tgt, sl)
        say(f"  unsigned D/C, mature only, hl 5 [{name}] " + " ".join(f"{x['excess_ann']:+.1%}" for x in prof) + f"   | book: {fmt(bk.book_row(s, tgt, sl))}")

    # ------------------------------------------------------------------ 4 subsumption on valid
    say("\n== 4 subsumption regressions (rank space, traded signals) on TRAIN and on VALID ==")
    for name, sl in SPL:
        n = sl.stop - sl.start
        tt = tgt[sl]
        for y, x in (("orig", "known9"), ("orig", "max30"), ("min3", "max30"), ("known9", "orig"), ("max30", "orig"), ("max30", "known9")):
            ys, xs = sig(y, HL_FIT[y])[sl], sig(x, HL_FIT[x])[sl]
            resid, info = dg.neutralise(ys, {x: xs})
            b = bk.book_row(resid, tt, slice(0, n))
            icr = dg.ic_row(resid, tt, sign=1.0)
            say(f"  [{name}] {y:<6} | {x:<6} R2 {info['mean_r2']:.3f}  resid rank IC {icr['rank_ic']:+.4f} (t {icr['rank_ic_t']:+.1f})"
                f"  LSgross {b['ls_gross_sharpe']:+.2f}  long gross {b['long_gross_ann']:+.1%}  short {b['short_gross_ann']:+.1%}  TO {b['ls_turnover']:.1%}")
    say(f"\ndone {time.time() - T0:.0f}s")
