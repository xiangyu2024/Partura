"""F105 revision 1 -- the researcher's follow-up to the two reviews.  train / valid only: every panel is cut at
the end of valid before anything is computed, so no holdout row is touched.

  1  half-life grid   the family (d = 9, 15, 20, 30, 60), the original and the 3-operator distillate at every
                      half-life of the rule's grid.  Is "the long leg is a plateau at d = 15..60" a property of
                      the window, or only of the turnover the L/S rule happened to pick?
  1b equivalence      known9 @ hl 5 against max30 @ hl 0/1: rank correlation, long-decile overlap, two-way residuals
  1c by year          the long book at the half-life the LONG rule picks, 2018..2023
  2  long side        the review: the residual of the original on the family has long-side information.
                      (a) smooth that residual and charge costs   (b) rank-average the original / the distillate
                      with a family member, against the control of averaging two members of the same family
                      (c) the same as an expression: raw panels, rule-picked half-life   (d) who is in the long deciles
  3  direction        entry vs exit names: raw excess and excess against a benchmark matched on amount / on the
                      family value.  Is "exit names still underperform" the level, or the event?
  4  pre-event level  conditional IC and an event study by buckets of a level measured BEFORE the event
                      (60-day median daily amount lagged 10 days; float cap) against the endogenous buckets
  5  event half       the clean event factor (recent peak / one-year peak) with young names removed
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
HLS = (0.0, 1.0, 2.0, 3.0, 5.0, 10.0, 20.0)
FAM = ("orig", "min3", "known9", "max15", "max20", "max30", "max60")
T0 = time.time()


def say(*a):
    print(*a, flush=True)


def pct(x):
    return dg._zrank(np.asarray(x, dtype=np.float64)) + 0.5


def fmt(b):
    return (f"LS {b['ls_sharpe']:+.2f} Lg {b['long_gross_ann']:+.1%} Ln {b['long_ann']:+.1%} Lshp {b['long_sharpe']:+.2f}"
            f" short {b['short_gross_ann']:+.1%} TO {b['ls_turnover']:.1%}")


def qbucket(x, ok, n):
    """Within-day quantile bucket 0..n-1 of x among the cells where ok; NaN elsewhere."""
    r = dg.rank_rows(np.where(ok, x, np.nan))
    cnt = np.isfinite(r).sum(1, keepdims=True)
    with np.errstate(invalid="ignore"):
        q = np.minimum(np.floor((r - 1.0) / np.maximum(cnt, 1) * n), n - 1)
    return q


def matched_excess(t, ok, key, nb=20):
    """t minus the same-day equal-weight mean of the names in the same quantile bin of `key` (among ok)."""
    b = qbucket(key, ok & np.isfinite(key), nb)
    out = np.full_like(t, np.nan)
    for k in range(nb):
        sel = (b == k)
        m = np.where(sel, t, 0.0).sum(1) / np.maximum(sel.sum(1), 1)
        out = np.where(sel, t - m[:, None], out)
    return out


def grp_mean(x, m, min_names=5):
    """Mean over days (with >= min_names members) of the within-day mean of x over mask m, annualised."""
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
    tgt = np.asarray(st.target()[:stop], dtype=np.float64)
    amt = np.asarray(st.control("ctl_amt")[:stop], dtype=np.float64)
    cap = np.asarray(st.control("ctl_cap")[:stop], dtype=np.float64)
    SPL = (("train", tr), ("valid", va))
    amt_p, cap_p = pct(amt), pct(cap)
    years = np.array([int(str(d)[:4]) for d in st.dates[:stop]])
    say(f"panels ready {time.time() - T0:.0f}s; rows used {stop} (train {tr}, valid {va}); symbols {P['orig'].shape[1]}")
    _sig = {}

    def sig(k, hl):
        if (k, hl) not in _sig:
            _sig[(k, hl)] = bk.smoothed(-P[k], hl)
        return _sig[(k, hl)]

    for name, sl in SPL:      # stage tables: orig@3 LS +2.54 / +4.62, Ln +8.2% / +20.7%;  max30@0 +2.37 / +4.12, +13.6% / +22.2%
        say(f"  selfcheck [{name}] orig@3  {fmt(bk.book_row(sig('orig', 3.0), tgt, sl))}")
        say(f"  selfcheck [{name}] max30@0 {fmt(bk.book_row(sig('max30', 0.0), tgt, sl))}")

    # ------------------------------------------------------------------ 1 half-life grid
    say("\n== 1 every factor at every half-life of the rule's grid (sign -1); *LS / *LONG = what each rule picks on train ==")
    grid, HL_LS, HL_LONG = {}, {}, {}
    for k in FAM:
        for hl in HLS:
            s = bk.smoothed(-P[k], hl)
            grid[(k, hl)] = {name: bk.book_row(s, tgt, sl) for name, sl in SPL}
        HL_LS[k] = max(HLS, key=lambda h: grid[(k, h)]["train"]["ls_sharpe"])
        HL_LONG[k] = max(HLS, key=lambda h: grid[(k, h)]["train"]["long_sharpe"])
        for hl in HLS:
            mark = ("*LS " if hl == HL_LS[k] else "") + ("*LONG" if hl == HL_LONG[k] else "")
            say(f"  {k:<6} hl {hl:>2.0f} {mark:<9} " + "   ".join(f"[{name}] {fmt(grid[(k, hl)][name])}" for name, _ in SPL))
    say("  -- summary at the LONG-rule half-life")
    for k in FAM:
        say(f"  {k:<6} hl_long {HL_LONG[k]:>2.0f}  " + "   ".join(f"[{name}] {fmt(grid[(k, HL_LONG[k])][name])}" for name, _ in SPL))

    say("  -- the same, universe restricted to names with >= 247 observations (drops IPO-young names and all of 2018)")
    young0 = np.cumsum(np.isfinite(P["known9"]), axis=0) < 247
    for k in FAM:
        s = np.where(young0, np.nan, sig(k, HL_LONG[k]))
        say(f"  mature {k:<6} hl_long {HL_LONG[k]:>2.0f}  " + "   ".join(f"[{name}] {fmt(bk.book_row(s, tgt, sl))}" for name, sl in SPL))

    # ------------------------------------------------------------------ 1b equivalence
    say("\n== 1b is one member + EMA the same thing as a slower member?  (traded signals) ==")

    def overlap(sa, sb, sl):
        wa = bk.long_short_weights(sa[sl], 0.10)
        wb = bk.long_short_weights(sb[sl], 0.10)
        return ((wa > 0) & (wb > 0)).sum() / max((wa > 0).sum(), 1), ((wa < 0) & (wb < 0)).sum() / max((wa < 0).sum(), 1)

    def resid_line(y, x, sl):
        resid, info = dg.neutralise(sig(*y)[sl], {"x": sig(*x)[sl]})
        n = sl.stop - sl.start
        b = bk.book_row(resid, tgt[sl], slice(0, n))
        ic = dg.ic_row(resid, tgt[sl], sign=1.0)
        return (f"R2 {info['mean_r2']:.3f} resid rIC {ic['rank_ic']:+.4f} (t {ic['rank_ic_t']:+.1f}) LSgross {b['ls_gross_sharpe']:+.2f}"
                f" Lg {b['long_gross_ann']:+.1%} short {b['short_gross_ann']:+.1%} TO {b['ls_turnover']:.1%}")

    for a, b in ((("known9", 5.0), ("max30", 0.0)), (("known9", 5.0), ("max30", 1.0)), (("known9", 0.0), ("max30", 0.0)),
                 (("max15", 3.0), ("max30", 1.0)), (("max60", 0.0), ("max30", 1.0)),
                 (("min3", 10.0), ("max30", 1.0)), (("orig", 10.0), ("max30", 1.0)), (("min3", 10.0), ("known9", 5.0))):
        la, lb = f"{a[0]}@{a[1]:.0f}", f"{b[0]}@{b[1]:.0f}"
        for name, sl in SPL:
            ol, os_ = overlap(sig(*a), sig(*b), sl)
            say(f"  [{name}] {la:<10} ~ {lb:<9} rank corr {dg.pair_rank_corr(sig(*a)[sl], sig(*b)[sl]):.3f}  long-decile overlap {ol:.1%}  short-decile overlap {os_:.1%}")
            say(f"      {la} | {lb}: {resid_line(a, b, sl)}")
            say(f"      {lb} | {la}: {resid_line(b, a, sl)}")

    # ------------------------------------------------------------------ 1c by year at the long-rule half-life
    say("\n== 1c by year, each factor at its LONG-rule half-life (each year starts from an empty book): Ln / Lshp / LS ==")
    for y in sorted(set(years.tolist())):
        idx = np.nonzero(years == y)[0]
        if idx.size < 20:
            continue
        sl = slice(int(idx[0]), int(idx[-1]) + 1)
        row = []
        for k in FAM:
            b = bk.book_row(sig(k, HL_LONG[k]), tgt, sl)
            row.append(f"{k}@{HL_LONG[k]:.0f} {b['long_ann']:+.1%}/{b['long_sharpe']:+.2f}/{b['ls_sharpe']:+.2f}")
        say(f"  {y} ({idx.size}d)  " + "  |  ".join(row))

    # ------------------------------------------------------------------ 2a the residual, smoothed and charged
    say("\n== 2a the residual of one traded signal on another, then EMA-smoothed and charged 15 bp ==")
    full = slice(0, stop)
    for y, x in ((("orig", 3.0), ("max30", 0.0)), (("min3", 3.0), ("max30", 0.0)), (("orig", 3.0), ("known9", 0.0)),
                 (("min3", 10.0), ("max30", 1.0)), (("orig", 10.0), ("max30", 1.0)),
                 (("known9", 0.0), ("max30", 0.0)), (("max30", 0.0), ("orig", 3.0)), (("max30", 1.0), ("min3", 10.0))):
        resid, info = dg.neutralise(sig(*y), {"x": sig(*x)})
        icr = {name: dg.ic_row(resid[sl], tgt[sl], sign=1.0) for name, sl in SPL}
        ics = "  ".join(f"[{name}] rIC {icr[name]['rank_ic']:+.4f} (t {icr[name]['rank_ic_t']:+.1f})" for name, _ in SPL)
        say(f"  {y[0]}@{y[1]:.0f} | {x[0]}@{x[1]:.0f}   R2 {info['mean_r2']:.3f}   {ics}")
        for hl in (0.0, 3.0, 5.0, 10.0, 20.0):
            sm = bk.smoothed(resid, hl)
            say(f"      resid hl {hl:>2.0f}  " + "   ".join(f"[{name}] {fmt(bk.book_row(sm, tgt, sl))}" for name, sl in SPL))

    # ------------------------------------------------------------------ 2b rank-average of two traded signals
    say("\n== 2b rank-average of two traded signals (equal weights), no further smoothing ==")
    Z = {}

    def z(k, hl):
        if (k, hl) not in Z:
            Z[(k, hl)] = dg._zrank(sig(k, hl))
        return Z[(k, hl)]

    combos = (("orig@3 + max30@0", ("orig", 3.0), ("max30", 0.0)),
              ("min3@3 + max30@0", ("min3", 3.0), ("max30", 0.0)),
              ("orig@10 + max30@1", ("orig", 10.0), ("max30", 1.0)),
              ("min3@10 + max30@1", ("min3", 10.0), ("max30", 1.0)),
              ("min3@10 + max60@0", ("min3", 10.0), ("max60", 0.0)),
              ("min3@10 + known9@5", ("min3", 10.0), ("known9", 5.0)),
              ("pos@10 + max30@1", ("pos", 10.0), ("max30", 1.0)),
              ("CONTROL known9@5 + max30@1", ("known9", 5.0), ("max30", 1.0)),
              ("CONTROL max15@3 + max60@0", ("max15", 3.0), ("max60", 0.0)),
              ("CONTROL known9@5 + max60@0", ("known9", 5.0), ("max60", 0.0)),
              ("CONTROL orig@10 + min3@10", ("orig", 10.0), ("min3", 10.0)))
    for label, a, b in combos:
        s = z(*a) + z(*b)
        say(f"  {label:<28} " + "   ".join(f"[{name}] {fmt(bk.book_row(s, tgt, sl))}" for name, sl in SPL))
        for part in (a, b):
            say(f"      alone {part[0]}@{part[1]:.0f}".ljust(31) + "   ".join(f"[{name}] {fmt(bk.book_row(sig(*part), tgt, sl))}" for name, sl in SPL))
    say("  -- by year for the long-rule pair min3@10 + max30@1 against max30@1 alone and min3@10 alone: Ln / Lshp")
    s_combo = z("min3", 10.0) + z("max30", 1.0)
    for y in sorted(set(years.tolist())):
        idx = np.nonzero(years == y)[0]
        if idx.size < 20:
            continue
        sl = slice(int(idx[0]), int(idx[-1]) + 1)
        row = []
        for lbl, s in (("combo", s_combo), ("max30@1", sig("max30", 1.0)), ("min3@10", sig("min3", 10.0))):
            b = bk.book_row(s, tgt, sl)
            row.append(f"{lbl} {b['long_ann']:+.1%}/{b['long_sharpe']:+.2f}")
        say(f"  {y} ({idx.size}d)  " + "  |  ".join(row))

    # ------------------------------------------------------------------ 2c the same thing as an expression
    say("\n== 2c as an expression: add(cs_rank(-a), cs_rank(-b)) on RAW panels, half-life picked by the rule ==")
    for label, a, b in (("orig + max30", "orig", "max30"), ("min3 + max30", "min3", "max30"), ("min3 + max60", "min3", "max60"),
                        ("min3 + known9", "min3", "known9"), ("CONTROL known9 + max60", "known9", "max60"),
                        ("CONTROL max15 + max60", "max15", "max60")):
        raw = dg._zrank(-P[a]) + dg._zrank(-P[b])
        for fitname, fit, evals in (("train", tr, {"train": tr, "valid": va}), ("utrain", full, {"utrain": full})):
            bb = bk.books(raw, tgt, fit, evals)
            say(f"  {label:<24} fit {fitname:<6} hl_ls {bb['hl_ls']:.0f} hl_long {bb['hl_long']:.0f}")
            say("      @hl_ls   " + "   ".join(f"[{n}] {fmt(v)}" for n, v in bb["splits"].items()))
            if "splits_at_hl_long" in bb:
                say("      @hl_long " + "   ".join(f"[{n}] {fmt(v)}" for n, v in bb["splits_at_hl_long"].items()))

    # ------------------------------------------------------------------ 2d who is in the long deciles
    say("\n== 2d two long deciles at matched turnover: what do the names only one of them holds earn? ==")
    n_cum = np.cumsum(np.isfinite(P["known9"]), axis=0)
    young = n_cum < 247
    mature = ~young
    for la, a, lb, b in (("min3@10", ("min3", 10.0), "max30@1", ("max30", 1.0)), ("orig@10", ("orig", 10.0), "max30@1", ("max30", 1.0))):
        for name, sl in SPL:
            t = tgt[sl]
            sa, sb = sig(*a)[sl], sig(*b)[sl]
            ok = np.isfinite(sa) & np.isfinite(sb) & np.isfinite(t)
            ew = np.where(ok, t, 0.0).sum(1) / np.maximum(ok.sum(1), 1)
            ex = np.where(ok, t - ew[:, None], 0.0)
            wa = bk.long_short_weights(sa, 0.10) > 0
            wb = bk.long_short_weights(sb, 0.10) > 0
            for g, m in (("both", wa & wb & ok), (f"only {la}", wa & ~wb & ok), (f"only {lb}", wb & ~wa & ok)):
                mx, cnt = grp_mean(ex, m)
                with np.errstate(invalid="ignore"):
                    say(f"  [{name}] {g:<14} names/day {cnt:6.1f}  mean excess {mx:+6.1%}/yr  amt pctile {np.nanmean(np.where(m, amt_p[sl], np.nan)):.2f}"
                        f"  cap pctile {np.nanmean(np.where(m, cap_p[sl], np.nan)):.2f}  young share {(m & young[sl]).sum() / max(m.sum(), 1):.1%}")

    # ------------------------------------------------------------------ 3 direction, level-matched
    say("\n== 3 entry vs exit: raw excess, and excess against a benchmark matched on today's amount / on max30 (20 bins) ==")
    d, c = P["orig"], P["C"]
    dc = np.full_like(c, np.nan)
    dc[4:] = c[4:] - c[:-4]
    with np.errstate(invalid="ignore", divide="ignore"):
        rel = np.where(c > 0, d / c, np.nan)
    okd = np.isfinite(d) & np.isfinite(tgt)
    ew_all = np.where(okd, tgt, 0.0).sum(1) / np.maximum(okd.sum(1), 1)
    ex_raw = np.where(okd, tgt - ew_all[:, None], np.nan)
    ex_amt = matched_excess(tgt, okd, amt)
    ex_fam = matched_excess(tgt, okd, P["max30"])
    es = bk.smoothed(np.sign(dc) * d, 3.0)
    w3 = bk.long_short_weights(sig("orig", 3.0), 0.10)
    for name, sl in SPL:
        sht = (w3[sl] < 0) & okd[sl]
        say(f"  [{name}] the original's short decile (traded signal, hl 3), groups as in events.py 3b:")
        for g, m in (("entry (C rising)", sht & mature[sl] & (es[sl] > 0)), ("exit (C falling)", sht & mature[sl] & (es[sl] < 0)),
                     ("young", sht & young[sl]), ("whole decile", sht)):
            r0, cnt = grp_mean(ex_raw[sl], m)
            r1, _ = grp_mean(ex_amt[sl], m)
            r2, _ = grp_mean(ex_fam[sl], m)
            with np.errstate(invalid="ignore"):
                say(f"      {g:<18} names/day {cnt:6.1f}  raw excess {r0:+6.1%}  amount-matched {r1:+6.1%}  max30-matched {r2:+6.1%}"
                    f"  amt pctile {np.nanmean(np.where(m, amt_p[sl], np.nan)):.2f}")
        relm = np.where(mature[sl] & okd[sl], rel[sl], np.nan)
        q = qbucket(relm, np.isfinite(relm), 10)
        say(f"  [{name}] scale-free |D/C| (mature names), by the sign of the 5-day change of C:")
        for lo, hi, lbl in ((9, 9, "top decile"), (8, 8, "9th decile"), (5, 7, "deciles 6-8"), (0, 4, "bottom half")):
            cells = []
            for g, gm in (("C rising", dc[sl] > 0), ("C falling", dc[sl] < 0)):
                m = (q >= lo) & (q <= hi) & gm
                r0, cnt = grp_mean(ex_raw[sl], m)
                r1, _ = grp_mean(ex_amt[sl], m)
                r2, _ = grp_mean(ex_fam[sl], m)
                with np.errstate(invalid="ignore"):
                    cells.append(f"{g}: n {cnt:6.1f} raw {r0:+6.1%} amt-matched {r1:+6.1%} max30-matched {r2:+6.1%} amt pct {np.nanmean(np.where(m, amt_p[sl], np.nan)):.2f}")
            say(f"      {lbl:<12} " + "   |   ".join(cells))

    # ------------------------------------------------------------------ 4 pre-event level
    say("\n== 4 conditional rank IC of the event half inside quintiles of a level (negative = same direction as the factor) ==")
    pre = np.full_like(P["med60"], np.nan)
    pre[10:] = P["med60"][:-10]
    amt_lag = np.full_like(amt, np.nan)
    amt_lag[10:] = amt[:-10]
    gates = {"today's amount (endogenous)": amt, "known9 (endogenous)": P["known9"], "one-year level C": c,
             "PRE-EVENT 60d median amount, lag 10": pre, "PRE-EVENT one-day amount, lag 10": amt_lag, "float cap": cap}
    facs = {"D/C all names": rel, "D/C mature": np.where(mature, rel, np.nan),
            "D/C mature, C rising only": np.where(mature & (dc > 0), rel, np.nan),
            "D/C mature, C falling only": np.where(mature & (dc < 0), rel, np.nan),
            "pos (recent peak / 1y peak)": P["pos"]}
    for name, sl in SPL:
        for fname, f in facs.items():
            for gname, g in gates.items():
                rows = dg.conditional_ic(f[sl], tgt[sl], g[sl], buckets=5)
                say(f"  [{name}] {fname:<28} | {gname:<36} " + "  ".join(f"{r['rank_ic']:+.4f}" for r in rows)
                    + "   names " + "/".join(f"{r['mean_names']:.0f}" for r in rows))
    say("  -- how endogenous is the bucket?  rank corr of the gates (train), and where the entry events sit")
    say(f"     today's amount ~ pre-event median: {dg.pair_rank_corr(amt[tr], pre[tr]):.3f};  known9 ~ pre-event median: {dg.pair_rank_corr(P['known9'][tr], pre[tr]):.3f}")
    say("\n== 4b event study by level quintile: mature names in the top decile of |D/C| (one threshold for the whole cross-section) ==")
    say("   excess is against the equal-weight mean of the SAME level quintile, annualised; quiet = bottom half of |D/C|")
    for name, sl in SPL:
        t = tgt[sl]
        okm = mature[sl] & np.isfinite(rel[sl]) & np.isfinite(t)
        q = qbucket(rel[sl], okm, 10)
        groups = (("entry", okm & (q == 9) & (dc[sl] > 0)), ("exit", okm & (q == 9) & (dc[sl] < 0)), ("quiet", okm & (q <= 4)))
        for gname, g in (("today's amount (endogenous)", amt), ("PRE-EVENT 60d median amount, lag 10", pre), ("float cap", cap)):
            gb = qbucket(g[sl], okm & np.isfinite(g[sl]), 5)
            share = [((groups[0][1]) & (gb == b)).sum() / max(groups[0][1].sum(), 1) for b in range(5)]
            say(f"  [{name}] by {gname}: share of entry events per quintile " + " ".join(f"{s:.0%}" for s in share))
            for b in range(5):
                inb = (gb == b)
                mb = np.where(inb, t, 0.0).sum(1) / np.maximum(inb.sum(1), 1)
                exb = np.where(inb, t - mb[:, None], np.nan)
                cells = []
                for grp, m in groups:
                    v, cnt = grp_mean(exb, m & inb)
                    cells.append(f"{grp} n {cnt:5.1f} {v:+6.1%}")
                say(f"      Q{b + 1}  " + "   ".join(cells))

    # ------------------------------------------------------------------ 5 the clean event factor without young names
    say("\n== 5 the event half as a factor of its own: all names vs mature names only (sign -1) ==")
    for label, p in (("pos all names", P["pos"]), ("pos mature only", np.where(mature, P["pos"], np.nan)),
                     ("D/C all names", rel), ("D/C mature only", np.where(mature, rel, np.nan)),
                     ("orig mature only", np.where(mature, P["orig"], np.nan)), ("max30 mature only", np.where(mature, P["max30"], np.nan))):
        for hl in (1.0, 5.0, 10.0):
            s = bk.smoothed(-p, hl)
            say(f"  {label:<18} hl {hl:>2.0f}  " + "   ".join(f"[{name}] {fmt(bk.book_row(s, tgt, sl))}" for name, sl in SPL))
        s = bk.smoothed(-p, 5.0)
        for name, sl in SPL:
            say(f"      profile hl 5 [{name}] " + " ".join(f"{x['excess_ann']:+.1%}" for x in bk.quantile_profile(s, tgt, sl)))
    say(f"\ndone {time.time() - T0:.0f}s")
