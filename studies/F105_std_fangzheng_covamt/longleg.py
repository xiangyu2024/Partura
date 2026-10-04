"""F105: why the slow members of the known family have a better long leg than the original,
and whether that survives the checks a long-only user cares about.

S3/S4 found that cross_max(day_std(Amt), d) for d = 15..60 has a long-leg net excess of 12-14% (train)
against the original's 8%, and that valid is a tie.  Before the holdout is read, four questions that no
stage table answers (train / valid only, never the holdout):

  1  subsumption   does the original add anything to cross_max(day_std(Amt), 30), or the reverse?
  2  long decile   how much do the two long deciles overlap, and what do the names only one of them holds earn?
  3  by year       is the long-leg advantage there year by year (2018..2023), or is it one year?
  4  capacity      does the advantage survive dropping the smallest 20% by float cap / by amount from the universe?
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F105_std_fangzheng_covamt"
EXPR = {
    "orig":   "ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)",
    "min3":   "cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)",
    "max15":  "cross_max(day_std(Amt), 15)",
    "max30":  "cross_max(day_std(Amt), 30)",
    "max60":  "cross_max(day_std(Amt), 60)",
    "known9": "cross_max(day_std(Amt), 9)",
}
HL = {"orig": 3.0, "min3": 3.0, "max15": 0.0, "max30": 0.0, "max60": 0.0, "known9": 0.0}   # fitted on train (stage tables)
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def pct(x):
    return dg._zrank(np.asarray(x, dtype=np.float64)) + 0.5


def deciles(sig, tgt):
    ok = np.isfinite(sig) & np.isfinite(tgt)
    r = dg.rank_rows(np.where(ok, sig, np.nan))
    n = ok.sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        q = np.minimum(np.floor((r - 1.0) / np.maximum(n, 1) * 10), 9)
    return np.where(ok, q, np.nan), ok


def fmt(b):
    return (f"LS {b['ls_sharpe']:+.2f}  long gross {b['long_gross_ann']:+.1%} net {b['long_ann']:+.1%} sharpe {b['long_sharpe']:+.2f}"
            f"  short {b['short_gross_ann']:+.1%}  TO {b['ls_turnover']:.1%}")


with Study(FID) as st:
    P = {k: np.asarray(v, dtype=np.float64) for k, v in st.panels(EXPR).items()}
    tgt = st.target()
    tr, va = st.slice("train"), st.slice("valid")
    amt = np.asarray(st.control("ctl_amt"), dtype=np.float64)
    cap = np.asarray(st.control("ctl_cap"), dtype=np.float64)
    turn = np.asarray(st.control("ctl_turnrate"), dtype=np.float64)
    sig = {k: bk.smoothed(-P[k], HL[k]) for k in P}            # the traded signals (sign -1 for all, fitted on train)
    say(f"panels ready {time.time() - T0:.0f}s; train {tr}, valid {va}")

    # self-check: the helper reproduces the stage-table rows (orig: LS +2.54 / +4.62, long net +8.2% / +20.7%)
    for name, sl in (("train", tr), ("valid", va)):
        say(f"  selfcheck [{name}] orig   {fmt(bk.book_row(sig['orig'], tgt, sl))}")
        say(f"  selfcheck [{name}] max30  {fmt(bk.book_row(sig['max30'], tgt, sl))}")

    # ------------------------------------------------------------------ 1 subsumption
    say("\n== 1 subsumption (train; rank-space daily regression of one traded signal on another) ==")
    n_tr = tr.stop - tr.start

    def resid_row(y, ctl, label):
        resid, info = dg.neutralise(sig[y][tr], {k: sig[k][tr] if k in sig else -np.asarray(v[tr], dtype=np.float64)
                                                 for k, v in ctl.items()})
        b = bk.book_row(resid, tgt[tr], slice(0, n_tr))
        say(f"  {label:<28} R2 {info['mean_r2']:.3f}  resid rank IC {dg.ic_row(resid, tgt[tr], sign=1.0)['rank_ic']:+.4f}"
            f"  LSgross {b['ls_gross_sharpe']:+.2f}  long gross {b['long_gross_ann']:+.1%}  short {b['short_gross_ann']:+.1%}  TO {b['ls_turnover']:.1%}")

    for k in ("orig", "min3", "max15", "max30", "max60", "known9"):
        b = bk.book_row(sig[k], tgt[tr], slice(0, n_tr))
        say(f"  {k:<28} (itself)   rank IC {dg.ic_row(sig[k][tr], tgt[tr], sign=1.0)['rank_ic']:+.4f}  LSgross {b['ls_gross_sharpe']:+.2f}"
            f"  long gross {b['long_gross_ann']:+.1%}  short {b['short_gross_ann']:+.1%}  TO {b['ls_turnover']:.1%}")
    resid_row("orig", {"max30": None}, "orig | max30")
    resid_row("orig", {"max15": None}, "orig | max15")
    resid_row("orig", {"max60": None}, "orig | max60")
    resid_row("min3", {"max30": None}, "min3 | max30")
    resid_row("max30", {"orig": None}, "max30 | orig")
    resid_row("max30", {"known9": None}, "max30 | known9")
    resid_row("known9", {"max30": None}, "known9 | max30")
    resid_row("max30", {"amt": amt}, "max30 | ctl_amt")
    resid_row("max30", {"max60": None}, "max30 | max60")
    resid_row("max60", {"max30": None}, "max60 | max30")

    # ------------------------------------------------------------------ 2 long decile overlap
    say("\n== 2 the two long deciles: orig (hl 3) vs max30 (hl 0) ==")
    amt_p, cap_p, turn_p = pct(amt), pct(cap), pct(turn)
    m30_p, orig_p = pct(P['max30']), pct(P['orig'])
    n_cum = np.cumsum(np.isfinite(P["known9"]), axis=0)
    young = n_cum < 247
    for name, sl in (("train", tr), ("valid", va)):
        t = tgt[sl]
        qo, oko = deciles(sig["orig"][sl], t)
        qm, okm = deciles(sig["max30"][sl], t)
        ok = oko & okm
        r = np.where(ok, t, 0.0)
        ew = r.sum(1) / np.maximum(ok.sum(1), 1)
        ex = np.where(ok, t - ew[:, None], 0.0)
        lo, lm = (qo == 9) & ok, (qm == 9) & ok
        groups = {"both": lo & lm, "orig only": lo & ~lm, "max30 only": lm & ~lo,
                  "orig long (all)": lo, "max30 long (all)": lm}
        say(f"  [{name}] overlap: {(lo & lm).sum() / max(lo.sum(), 1):.1%} of orig's long decile is in max30's long decile;"
            f" {(lo & (qm >= 7)).sum() / max(lo.sum(), 1):.1%} is in max30's top 3 deciles;"
            f" {(lm & (qo >= 7)).sum() / max(lm.sum(), 1):.1%} of max30's long decile is in orig's top 3 deciles")
        for g, m in groups.items():
            cnt = m.sum(1)
            days = cnt >= 5
            mean_ex = ((ex * m).sum(1)[days] / cnt[days]).mean() * 252
            with np.errstate(invalid="ignore"):
                say(f"      {g:<17} names/day {cnt.mean():6.1f}   mean excess {mean_ex:+6.1%}/yr   amt pctile {np.nanmean(np.where(m, amt_p[sl], np.nan)):.2f}"
                    f"  cap pctile {np.nanmean(np.where(m, cap_p[sl], np.nan)):.2f}  turnrate pctile {np.nanmean(np.where(m, turn_p[sl], np.nan)):.2f}"
                    f"  max30 pctile {np.nanmean(np.where(m, m30_p[sl], np.nan)):.2f}  orig pctile {np.nanmean(np.where(m, orig_p[sl], np.nan)):.2f}"
                    f"  young share {(m & young[sl]).sum() / max(m.sum(), 1):.1%}")
        # day-to-day persistence of membership in the long decile (what turnover is made of)
        for g, m in (("orig", lo), ("max30", lm)):
            stay = (m[1:] & m[:-1]).sum() / max(m[1:].sum(), 1)
            say(f"      {g:<17} share of today's long decile that was in it yesterday: {stay:.1%}")

    # ------------------------------------------------------------------ 3 by year
    say("\n== 3 by year (each year starts from an empty book; sign / half-life fixed from train) ==")
    years = np.array([int(str(d)[:4]) for d in st.dates])
    stop = va.stop
    for y in sorted(set(years[:stop].tolist())):
        idx = np.nonzero(years[:stop] == y)[0]
        if idx.size < 20:
            continue
        sl = slice(int(idx[0]), int(idx[-1]) + 1)
        row = []
        for k in ("orig", "min3", "max15", "max30", "max60"):
            b = bk.book_row(sig[k], tgt, sl)
            row.append(f"{k} LS {b['ls_sharpe']:+.2f} Lnet {b['long_ann']:+.1%} Lshp {b['long_sharpe']:+.2f}")
        say(f"  {y} ({idx.size}d)  " + "  |  ".join(row))

    # ------------------------------------------------------------------ 4 capacity
    say("\n== 4 capacity: drop the smallest names from the universe, then rebuild both books ==")
    say("   (the universe changes day by day, so turnover and net are inflated the same way for every factor; compare within a row block)")
    masks = {"all names": np.ones_like(cap_p, dtype=bool),
             "cap pctile >= 0.2": cap_p >= 0.2,
             "cap pctile >= 0.5": cap_p >= 0.5,
             "amt pctile >= 0.2": amt_p >= 0.2}
    for mname, m in masks.items():
        for name, sl in (("train", tr), ("valid", va)):
            for k in ("orig", "max15", "max30", "max60"):
                b = bk.book_row(np.where(m, sig[k], np.nan), tgt, sl)
                say(f"  [{mname:<18}] [{name}] {k:<6} {fmt(b)}")
    say(f"\ndone {time.time() - T0:.0f}s")
