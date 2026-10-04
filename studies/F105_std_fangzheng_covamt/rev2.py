"""F105 revision 2 -- is the "entry event" result manufactured by the label's buyable filter?
train / valid only: every panel and both labels are cut at the end of valid before anything is computed.

rev1 replaced "the event half only works in large-amount names" by its opposite: bucketed by a level measured
BEFORE the event, the event's rank IC and the depth of the entry-event names are largest in the SMALLEST names.
Before that goes into the report it has to survive one artefact this study has not checked.  The study's label
drops every name that opens locked at limit-up on the entry day (right for a long-only buyer: it cannot be bought;
in a short basket the name is scored 0).  A volume spike in a small name is exactly where next-day limit-up opens
cluster, so the filter removes the best next-day returns from the entry group and could by itself make that group
look like a deep short.  The same label WITHOUT the filter is available from the label code; this script compares.

  0  the two labels      how many cells the filter drops, and what they earned
  1  event study         entry / exit / quiet names by pre-event level quintile, both labels, share of dropped cells
  2  conditional IC      the event half inside pre-event level quintiles, both labels
  3  direction           entry vs exit in the original's short decile and scale-free, amount-matched, both labels
  4  books               every candidate's short leg and L/S Sharpe under both labels (how much is the filter?)
  5  user convention     known9 / max20 / max30 with sign and half-life fitted on utrain (train + valid): the
                         training-column numbers of "one member + EMA" next to the recommended member
"""
import time

import numpy as np

from partura.study_tools import Study, bk, dg

FID = "F105_std_fangzheng_covamt"
A = "day_cov(Amt, Amt)"
C = f"cross_fangzheng(cross_max({A}, 3), 241)"
EXPR = {
    "orig":   f"ts_stddev({C}, 5)",
    "C":      C,
    "min3":   "cross_stddev(cross_stddev(day_cov(Amt, Amt), 241), 5)",
    "known9": "cross_max(day_std(Amt), 9)",
    "max15":  "cross_max(day_std(Amt), 15)",
    "max20":  "cross_max(day_std(Amt), 20)",
    "max30":  "cross_max(day_std(Amt), 30)",
    "max60":  "cross_max(day_std(Amt), 60)",
    "pos":    "div(cross_max(day_std(Amt), 5), cross_max(day_std(Amt), 241))",
    "med60":  "cross_med(day_sum(Amt), 60)",
}
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def pct(x):
    return dg._zrank(np.asarray(x, dtype=np.float64)) + 0.5


def qbucket(x, ok, n):
    r = dg.rank_rows(np.where(ok, x, np.nan))
    cnt = np.isfinite(r).sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        return np.minimum(np.floor((r - 1.0) / np.maximum(cnt, 1) * n), n - 1)


def matched_excess(t, ok, key, nb=20):
    b = qbucket(key, ok & np.isfinite(key), nb)
    out = np.full_like(t, np.nan)
    for k in range(nb):
        sel = (b == k)
        m = np.where(sel, t, 0.0).sum(1) / np.maximum(sel.sum(1), 1)
        out = np.where(sel, t - m[:, None], out)
    return out


def grp_mean(x, m, min_names=5):
    cnt = m.sum(1)
    days = cnt >= min_names
    if not days.any():
        return float("nan"), 0.0
    v = np.where(m, np.nan_to_num(x), 0.0).sum(1)[days] / cnt[days]
    return float(v.mean() * 252), float(cnt.mean())


with Study(FID) as st:
    tr, va = st.slice("train"), st.slice("valid")
    stop = va.stop
    assert tr.start == 0 and tr.stop == va.start
    P = {k: np.asarray(v[:stop], dtype=np.float64) for k, v in st.panels(EXPR).items()}
    amt = np.asarray(st.control("ctl_amt")[:stop], dtype=np.float64)
    cap = np.asarray(st.control("ctl_cap")[:stop], dtype=np.float64)
    ps = st.ps
    assert ps.label_buyable, "this study's label is the buyable one"
    t_buy = np.asarray(ps.target(1)[:stop], dtype=np.float64)        # the study's label
    SPL = (("train", tr), ("valid", va))
    try:
        ps.label_buyable = False
        ps._targets.pop(1, None)
        t_all = np.asarray(ps.target(1)[:stop], dtype=np.float64)    # same label, limit-up-locked entries kept
        LAB = (("buyable", t_buy), ("unfiltered", t_all))
    except Exception as exc:                                          # noqa: BLE001 -- keep the rest of the run
        say(f"!! could not build the unfiltered label ({type(exc).__name__}: {exc}); sections 0-4 use the study's label only")
        t_all = t_buy.copy()
        LAB = (("buyable", t_buy),)
    finally:
        ps.label_buyable = True
        ps._targets.pop(1, None)
    assert np.array_equal(np.asarray(ps.target(1)[:stop], dtype=np.float64), t_buy, equal_nan=True)
    amt_p = pct(amt)
    say(f"ready {time.time() - T0:.0f}s; rows used {stop}; symbols {t_buy.shape[1]}")

    # ------------------------------------------------------------------ 0 the two labels
    say("\n== 0 the two labels ==")
    locked = np.isfinite(t_all) & ~np.isfinite(t_buy)
    same = np.isfinite(t_all) & np.isfinite(t_buy)
    say(f"  cells where both are finite: {same.sum()}; max |difference| there: {np.nanmax(np.abs(np.where(same, t_all - t_buy, 0.0))):.2e}")
    say(f"  cells finite in buyable but not in unfiltered (should be 0): {(np.isfinite(t_buy) & ~np.isfinite(t_all)).sum()}")
    for name, sl in SPL:
        lk = locked[sl]
        fin = np.isfinite(t_all[sl])
        ew = np.where(fin, t_all[sl], 0.0).sum(1) / np.maximum(fin.sum(1), 1)
        ex = np.where(fin, t_all[sl] - ew[:, None], 0.0)
        say(f"  [{name}] dropped by the buyable filter: {lk.sum() / max(fin.sum(), 1):.2%} of labelled cells ({lk.sum(1).mean():.1f} names/day);"
            f" their mean next-day return {np.nanmean(np.where(lk, t_all[sl], np.nan)):+.2%}, excess over the universe {(ex * lk).sum() / max(lk.sum(), 1):+.2%} per day")

    d, c = P["orig"], P["C"]
    dc = np.full_like(c, np.nan)
    dc[4:] = c[4:] - c[:-4]
    with np.errstate(invalid="ignore", divide="ignore"):
        rel = np.where(c > 0, d / c, np.nan)
    young = np.cumsum(np.isfinite(P["known9"]), axis=0) < 247
    mature = ~young
    pre = np.full_like(P["med60"], np.nan)
    pre[10:] = P["med60"][:-10]

    # ------------------------------------------------------------------ 1 event study, both labels
    say("\n== 1 event study by level quintile (mature names; top decile of |D/C| with one threshold for the whole cross-section) ==")
    say("   excess against the equal-weight mean of the SAME level quintile, annualised; 'locked' = share of the group's labelled cells the buyable filter drops")
    for name, sl in SPL:
        okr = mature[sl] & np.isfinite(rel[sl]) & np.isfinite(t_all[sl])          # one event definition for both labels
        q = qbucket(rel[sl], okr, 10)
        ev = (("entry", okr & (q == 9) & (dc[sl] > 0)), ("exit", okr & (q == 9) & (dc[sl] < 0)), ("quiet", okr & (q <= 4)))
        for gname, g in (("PRE-EVENT 60d median amount, lag 10", pre), ("today's amount (endogenous)", amt), ("float cap", cap)):
            gb = qbucket(g[sl], okr & np.isfinite(g[sl]), 5)
            say(f"  [{name}] by {gname}")
            for b in range(5):
                inb = (gb == b)
                cells = []
                for grp, m0 in ev:
                    m = m0 & inb
                    out = []
                    for lname, t in LAB:
                        tt = t[sl]
                        okt = inb & np.isfinite(tt)
                        mb = np.where(okt, tt, 0.0).sum(1) / np.maximum(okt.sum(1), 1)
                        exb = np.where(okt, tt - mb[:, None], np.nan)
                        v, cnt = grp_mean(exb, m & okt)
                        out.append(f"{lname} {v:+6.1%}")
                    cells.append(f"{grp} n {m.sum(1).mean():5.1f} " + " / ".join(out) + f" locked {(m & locked[sl]).sum() / max(m.sum(), 1):.1%}")
                say(f"      Q{b + 1}  " + "   |   ".join(cells))

    # ------------------------------------------------------------------ 2 conditional IC, both labels
    say("\n== 2 conditional rank IC of the event half inside level quintiles, both labels (negative = same direction as the factor) ==")
    gates = {"PRE-EVENT 60d median amount, lag 10": pre, "today's amount (endogenous)": amt, "float cap": cap,
             "max30 (the family member itself)": P["max30"]}
    facs = {"D/C mature": np.where(mature, rel, np.nan), "D/C mature, C rising only": np.where(mature & (dc > 0), rel, np.nan),
            "pos (recent peak / 1y peak)": P["pos"], "max30": P["max30"], "orig": P["orig"]}
    for name, sl in SPL:
        for fname, f in facs.items():
            for lname, t in LAB:
                say(f"  [{name}] {fname:<28} {lname:<10} unconditional {np.nanmean(dg.rank_ic_series(f[sl], t[sl])):+.4f}   "
                    + "   ".join(f"{gname.split(' ')[0]}: " + " ".join(f"{r['rank_ic']:+.4f}" for r in dg.conditional_ic(f[sl], t[sl], g[sl], buckets=5))
                                 for gname, g in gates.items()))

    # ------------------------------------------------------------------ 3 direction, both labels
    say("\n== 3 entry vs exit, raw and amount-matched excess, both labels ==")
    es = bk.smoothed(np.sign(dc) * d, 3.0)
    sig3 = bk.smoothed(-d, 3.0)
    w3 = bk.long_short_weights(sig3, 0.10)
    for lname, t in LAB:
        okd = np.isfinite(d) & np.isfinite(t)
        ew_all = np.where(okd, t, 0.0).sum(1) / np.maximum(okd.sum(1), 1)
        ex_raw = np.where(okd, t - ew_all[:, None], np.nan)
        ex_amt = matched_excess(t, okd, amt)
        for name, sl in SPL:
            sht = (w3[sl] < 0) & okd[sl]
            row = []
            for g, m in (("entry", sht & mature[sl] & (es[sl] > 0)), ("exit", sht & mature[sl] & (es[sl] < 0)), ("young", sht & young[sl]), ("decile", sht)):
                r0, cnt = grp_mean(ex_raw[sl], m)
                r1, _ = grp_mean(ex_amt[sl], m)
                row.append(f"{g} n {cnt:5.1f} raw {r0:+6.1%} amt-matched {r1:+6.1%}")
            say(f"  [{name}] {lname:<10} original's short decile (hl 3): " + "   |   ".join(row))
            relm = np.where(mature[sl] & okd[sl], rel[sl], np.nan)
            q = qbucket(relm, np.isfinite(relm), 10)
            row = []
            for g, gm in (("C rising", dc[sl] > 0), ("C falling", dc[sl] < 0)):
                m = (q == 9) & gm
                r0, cnt = grp_mean(ex_raw[sl], m)
                r1, _ = grp_mean(ex_amt[sl], m)
                row.append(f"{g} n {cnt:5.1f} raw {r0:+6.1%} amt-matched {r1:+6.1%}")
            say(f"  [{name}] {lname:<10} top decile of scale-free |D/C|:   " + "   |   ".join(row))

    # ------------------------------------------------------------------ 4 books under both labels
    say("\n== 4 the candidates' books under both labels (the long leg under 'unfiltered' holds names that could not be bought: read the short leg and L/S only) ==")
    for k, hl in (("orig", 3.0), ("orig", 10.0), ("min3", 3.0), ("min3", 10.0), ("known9", 0.0), ("known9", 5.0), ("max15", 0.0),
                  ("max30", 0.0), ("max30", 1.0), ("max60", 0.0), ("pos", 1.0)):
        s = bk.smoothed(-P[k], hl)
        for name, sl in SPL:
            w = bk.long_short_weights(s[sl], 0.10)
            lk = locked[sl]
            row = []
            for lname, t in LAB:
                b = bk.book_row(s, t, sl)
                row.append(f"{lname}: LS {b['ls_sharpe']:+.2f} short {b['short_gross_ann']:+.1%} long gross {b['long_gross_ann']:+.1%} net {b['long_ann']:+.1%}")
            say(f"  {k:<6}@{hl:<2.0f} [{name}] " + "   |   ".join(row)
                + f"   locked share: short decile {((w < 0) & lk).sum() / max((w < 0).sum(), 1):.2%}, long decile {((w > 0) & lk).sum() / max((w > 0).sum(), 1):.2%}")

    # ------------------------------------------------------------------ 5 user convention on utrain
    say("\n== 5 sign -1, half-life fitted on utrain (train + valid): the user's training column, no holdout ==")
    full = slice(0, stop)
    for k in ("orig", "min3", "known9", "max15", "max20", "max30", "max60"):
        fitd = bk.fit_halflives(-P[k], t_buy, full)
        say(f"  {k:<6} hl_ls {fitd['hl_ls']:.0f} hl_long {fitd['hl_long']:.0f}   "
            + "  ".join(f"hl{w['halflife']:.0f}: LS {w['ls_sharpe']:.2f} Lshp {w['long_sharpe']:.2f} Ln {w['long_ann']:.1%} TO {w['ls_turnover']:.1%}" for w in fitd["sweep"]))

    # ------------------------------------------------------------------ 6 what the long decile earns beyond its level
    say("\n== 6 the long decile: where it sits by pre-event level, and its excess against pre-event-level-matched peers (study's label) ==")
    okp = np.isfinite(t_buy) & np.isfinite(pre) & np.isfinite(P["max30"])
    ewp = np.where(okp, t_buy, 0.0).sum(1) / np.maximum(okp.sum(1), 1)
    ex_raw = np.where(okp, t_buy - ewp[:, None], np.nan)
    ex_pre = matched_excess(t_buy, okp, pre)
    ex_cap = matched_excess(t_buy, okp & np.isfinite(cap), cap)
    pre_q = qbucket(pre, okp, 5)
    cands = {"orig@10": bk.smoothed(-P["orig"], 10.0), "min3@10": bk.smoothed(-P["min3"], 10.0), "known9@5": bk.smoothed(-P["known9"], 5.0),
             "max30@1": bk.smoothed(-P["max30"], 1.0), "max60@0": -P["max60"], "med60@0 (pure level)": -P["med60"],
             "pre-event level itself": -pre, "pos@10": bk.smoothed(-P["pos"], 10.0)}
    for label, s in cands.items():
        for name, sl in SPL:
            w = bk.long_short_weights(np.where(okp, s, np.nan)[sl], 0.10)
            for leg, m in (("long", w > 0), ("short", w < 0)):
                share = [(m & (pre_q[sl] == b)).sum() / max(m.sum(), 1) for b in range(5)]
                r0, cnt = grp_mean(ex_raw[sl], m)
                r1, _ = grp_mean(ex_pre[sl], m)
                r2, _ = grp_mean(ex_cap[sl], m)
                say(f"  {label:<22} [{name}] {leg:<5} n {cnt:5.1f} raw excess {r0:+6.1%}  pre-level-matched {r1:+6.1%}  cap-matched {r2:+6.1%}"
                    f"  share by pre-event quintile " + " ".join(f"{x:.0%}" for x in share))
    say(f"\ndone {time.time() - T0:.0f}s")
