"""x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.

No stock diagnostic answers these, and the stage plan depends on the answers:

  0. helper sources / probe self-checks with the SERVER kernels
  A. what is `Ret`?  valid minutes per day; does the first minute carry the overnight gap;
     does day_sum(Ret) add up to close/prev-close or to close/open
  B. the three regimes (regular / edge / blown-up) of each side on real stock-days: how often, how big,
     and what kind of day it is (limit board, one-word board, low price, thin trading)
  C. the TRADED signal (EMA-20 of -X): how much of the cross-section is ruled by blown-up days,
     and who sits in each decile (limit history, listing age, price/cap/amt/turnover/vol, unbuyable share)
  D. event time: what happens to a stock in the days AFTER each kind of blown-up day
  E. quick book rows (same convention as the tables) for the constructions the stage plan is choosing between
  F. the short leg with and without the "could not be bought" filter
  G. is the FOLDED signal (distance from the cross-sectional middle) a known exposure?

Only utrain (= train + valid) rows are touched; the holdout is never sliced.
`python x1_anatomy.py selftest` runs every numeric routine on random arrays (no data, no server).
"""
import sys
import warnings

import numpy as np

warnings.filterwarnings("ignore")

FID = "F106_erm_mag_gap_1m"
M = 241

Q95, Q05 = "day_quantile(Ret, 0.95)", "day_quantile(Ret, 0.05)"
E95, E05 = f"create_like({Q95}, 1e-06)", f"create_like({Q05}, 1e-06)"
ES_UP = f"div(day_sum(select_where(is_gt(Ret, {Q95}), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, {Q95})), {E95}))"
ES_DN = f"div(day_sum(select_where(is_lt(Ret, {Q05}), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, {Q05})), {E05}))"
R_SIDE = f"div({ES_UP}, add({Q95}, {E95}))"
L_SIDE = f"div({ES_DN}, add(abs_({Q05}), {E05}))"
BASE = f"sub({R_SIDE}, {L_SIDE})"


def tree_on(ret: str) -> str:
    """The whole tree with `Ret` replaced by another minute series."""
    return BASE.replace("Ret", ret)


EX = {
    "x": BASE, "R": R_SIDE, "L": L_SIDE, "q95": Q95, "q05": Q05, "es_up": ES_UP, "es_dn": ES_DN,
    "nup": "day_sum(is_gt0(Ret))", "ndn": "day_sum(is_lt0(Ret))",
    "nval": "day_sum(is_gt0(add(abs_(Ret), 1)))",
    "first": "day_first(Ret)", "sumret": "day_sum(Ret)", "maxret": "day_max(Ret)", "minret": "day_min(Ret)",
    "op": "day_first(Open)", "cl": "day_last(Close)", "hi": "day_max(High)", "lo": "day_min(Low)",
    "x_nofirst": tree_on("in_slice(Ret, 1, 240)"),
}


def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


# ------------------------------------------------------------------ numeric helpers (numpy only)
def rank_rows_np(a):
    """Average ranks per row, NaN preserved (numpy fallback for the selftest)."""
    import pandas as pd
    return pd.DataFrame(np.asarray(a, dtype=np.float64)).rank(axis=1).to_numpy()


_RANK = [rank_rows_np]


def pct_rank(a):
    r = _RANK[0](np.asarray(a, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def excess(tgt, universe):
    """label minus the per-day equal-weight mean over the universe cells (NaN where no label)."""
    t = np.where(universe & np.isfinite(tgt), tgt, np.nan)
    with np.errstate(invalid="ignore"):
        return t - np.nanmean(t, axis=1, keepdims=True)


def ann(v):
    v = np.asarray(v, dtype=np.float64)
    v = v[np.isfinite(v)]
    return float(v.mean() * 252) if v.size else float("nan")


def cell_mean_by_day(val, sel):
    """Per-day mean of `val` over the cells in `sel` (NaN-aware), then the list of daily means."""
    v = np.where(sel & np.isfinite(val), val, np.nan)
    with np.errstate(invalid="ignore"):
        return np.nanmean(v, axis=1)


def rolling_any(flag, w):
    """flag (D,S) bool -> True where the flag was set in any of the last w days (inclusive of today)."""
    c = np.cumsum(flag.astype(np.int32), axis=0)
    lag = np.zeros_like(c)
    if w < c.shape[0]:
        lag[w:] = c[:-w]
    return (c - lag) > 0


def days_since(flag):
    """(D,S) int: days since the flag was last set (0 on the day itself; 9999 if never)."""
    out = np.empty(flag.shape, dtype=np.int32)
    since = np.full(flag.shape[1], 9999, dtype=np.int32)
    for t in range(flag.shape[0]):
        since = np.where(flag[t], 0, np.minimum(since + 1, 9999))
        out[t] = since
    return out


def band(x, centres=(0.05, 0.10, 0.20), tol=0.004):
    m = np.zeros(x.shape, dtype=bool)
    with np.errstate(invalid="ignore"):
        for c in centres:
            m |= np.abs(x - c) <= tol
    return m


def limit_flags(cl, hi, lo, rev1):
    """Close-at-limit days from daily bars: return in a 5/10/20% band AND the close is the day's extreme."""
    with np.errstate(invalid="ignore", divide="ignore"):
        up = band(rev1 - 1.0) & (cl >= hi * (1 - 1e-6))
        dn = band(1.0 - rev1) & (cl <= lo * (1 + 1e-6))
        touch_up = band(hi / cl * rev1 - 1.0)
        touch_dn = band(1.0 - lo / cl * rev1)
        flat = np.isfinite(hi) & (hi <= lo * (1 + 1e-9))
    return {"up": up, "dn": dn, "touch_up": touch_up & ~up, "touch_dn": touch_dn & ~dn,
            "oneword_up": up & flat, "oneword_dn": dn & flat, "flat": flat}


def cls3(v):
    """0 regular (<5), 1 edge (5..500), 2 blown-up (>=500); -1 where not finite."""
    out = np.full(v.shape, -1, dtype=np.int8)
    f = np.isfinite(v)
    with np.errstate(invalid="ignore"):
        out[f & (v < 5)] = 0
        out[f & (v >= 5) & (v < 500)] = 1
        out[f & (v >= 500)] = 2
    return out


def decile_of(sig):
    """0..9 by within-day rank of the signal (0 = lowest = short end), -1 where no signal."""
    pr = pct_rank(sig)
    d = np.floor(pr * 10).astype(np.int8)
    d = np.clip(d, 0, 9)
    return np.where(np.isfinite(pr), d, -1).astype(np.int8)


def qtiles(v, qs=(0.001, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 0.999)):
    f = v[np.isfinite(v)]
    return {q: float(np.quantile(f, q)) for q in qs} if f.size else {}


def pooled_corr(a, b):
    m = np.isfinite(a) & np.isfinite(b)
    if m.sum() < 100:
        return float("nan")
    return float(np.corrcoef(a[m], b[m])[0, 1])


# ------------------------------------------------------------------ sections
def section_A(P, rev1, n):
    hdr("A. what is Ret?")
    x, nval = P["x"][:n], P["nval"][:n]
    fin = np.isfinite(x)
    nv = nval[fin]
    print(f"valid minutes per stock-day (cells with a factor value): =241 {np.mean(nv == 241):.4f}  =240 {np.mean(nv == 240):.4f}  "
          f"<240 {np.mean(nv < 240):.4f}  median {np.median(nv):.0f}  p1 {np.quantile(nv, 0.01):.0f}")
    first, sumret, op, cl = P["first"][:n], P["sumret"][:n], P["op"][:n], P["cl"][:n]
    with np.errstate(invalid="ignore", divide="ignore"):
        oc = cl / op - 1.0
        cc = rev1[:n] - 1.0
        gap = rev1[:n] / (cl / op) - 1.0
    sl = slice(0, n, 5)
    print(f"corr(day_first(Ret), overnight gap = open/prev close - 1) = {pooled_corr(first[sl], gap[sl]):+.4f}")
    print(f"corr(day_first(Ret), open-to-close return)              = {pooled_corr(first[sl], oc[sl]):+.4f}")
    print(f"median |day_first(Ret)| = {np.nanmedian(np.abs(first[sl])):.6f}   median |gap| = {np.nanmedian(np.abs(gap[sl])):.6f}   "
          f"median q95 = {np.nanmedian(P['q95'][:n][sl]):.6f}   median |q05| = {np.nanmedian(np.abs(P['q05'][:n][sl])):.6f}")
    print(f"share of stock-days with day_first(Ret) == 0 exactly: {np.nanmean((first[sl] == 0)[np.isfinite(first[sl])]):.4f}")
    with np.errstate(invalid="ignore"):
        print(f"median |day_sum(Ret) - (close/prev close - 1)| = {np.nanmedian(np.abs(sumret[sl] - cc[sl])):.6f}")
        print(f"median |day_sum(Ret) - (close/open - 1)|       = {np.nanmedian(np.abs(sumret[sl] - oc[sl])):.6f}")
        print(f"median |day_sum(Ret) - day_first(Ret) - (close/open - 1)| = {np.nanmedian(np.abs(sumret[sl] - first[sl] - oc[sl])):.6f}")
    print(f"corr(day_sum(Ret), close/prev close - 1) = {pooled_corr(sumret[sl], cc[sl]):+.4f}   corr(day_sum(Ret), close/open - 1) = {pooled_corr(sumret[sl], oc[sl]):+.4f}")
    # is the first minute in the tail set?
    with np.errstate(invalid="ignore"):
        in_up = first > P["q95"][:n]
        in_dn = first < P["q05"][:n]
    f2 = np.isfinite(first) & fin
    print(f"first minute is in the right tail on {np.mean(in_up[f2]):.3f} of stock-days, in the left tail on {np.mean(in_dn[f2]):.3f} "
          f"(a random minute would be ~0.05 each)")
    xn = P.get("x_nofirst")
    if xn is not None:
        xn = xn[:n]
        both = np.isfinite(x) & np.isfinite(xn)
        reg = both & (np.abs(x) < 5) & (np.abs(xn) < 5)
        a, b = np.where(reg, x, np.nan), np.where(reg, xn, np.nan)
        c = np.nanmean([pooled_corr(pct_rank(a[t:t + 1])[0], pct_rank(b[t:t + 1])[0]) for t in range(0, n, 20)])
        print(f"tree without the first minute vs tree: mean daily rank corr on regular days (|.|<5 both) = {c:+.3f}; "
              f"share of days where both are regular = {reg.sum() / max(both.sum(), 1):.3f}")
    return gap


def section_B(P, n, lim, tgt, raw, ctl):
    hdr("B. regimes of each side on real stock-days (utrain)")
    x, R, L = P["x"][:n], P["R"][:n], P["L"][:n]
    fin = np.isfinite(x)
    print("quantiles of X:", {k: round(v, 3) for k, v in qtiles(x).items()})
    print("quantiles of R:", {k: round(v, 3) for k, v in qtiles(R).items()})
    print("quantiles of L:", {k: round(v, 3) for k, v in qtiles(L).items()})
    cr, cL = cls3(R), cls3(L)
    names = {0: "reg", 1: "edge", 2: "blown"}
    ex_b = excess(tgt[:n], fin)
    ex_r = excess(raw[:n], fin)
    nolab = fin & ~np.isfinite(tgt[:n])
    pr_price, pr_amt = pct_rank(ctl["ctl_price"][:n]), pct_rank(ctl["ctl_amt"][:n])
    pr_turn = pct_rank(ctl["ctl_turnrate"][:n])
    tot = fin.sum()
    print(f"\n{'R side':>6} {'L side':>6} {'share':>8} {'med X':>10} {'nup':>5} {'ndn':>5} {'limUp':>6} {'limDn':>6} {'1word':>6} "
          f"{'flat':>6} {'price%':>6} {'amt%':>6} {'turn%':>6} {'close':>6} {'ex_buy':>8} {'ex_raw':>8} {'nolab':>6}")
    for a in (0, 1, 2):
        for b in (0, 1, 2):
            sel = fin & (cr == a) & (cL == b)
            k = sel.sum()
            if k == 0:
                continue
            print(f"{names[a]:>6} {names[b]:>6} {k / tot:8.4f} {np.median(x[sel]):10.2f} {P['nup'][:n][sel].mean():5.1f} "
                  f"{P['ndn'][:n][sel].mean():5.1f} {lim['up'][sel].mean():6.3f} {lim['dn'][sel].mean():6.3f} "
                  f"{(lim['oneword_up'] | lim['oneword_dn'])[sel].mean():6.3f} {lim['flat'][sel].mean():6.3f} "
                  f"{np.nanmean(pr_price[sel]):6.2f} {np.nanmean(pr_amt[sel]):6.2f} {np.nanmean(pr_turn[sel]):6.2f} "
                  f"{np.nanmedian(P['cl'][:n][sel]):6.2f} {ann(cell_mean_by_day(ex_b, sel)) * 100:+7.1f}% "
                  f"{ann(cell_mean_by_day(ex_r, sel)) * 100:+7.1f}% {nolab[sel].mean():6.3f}")
    print("(ex_buy / ex_raw = mean next-day excess of the cells, annualised, with the buyable / unfiltered label; "
          "nolab = share whose label is missing = opened locked at limit-up)")
    blown = fin & ((cr >= 1) | (cL >= 1))
    yrs = np.asarray([int(str(d)[:4]) for d in P["_dates"][:n]])
    print("share of stock-days with a non-regular side, by year: " +
          "  ".join(f"{y} {blown[yrs == y].sum() / max(fin[yrs == y].sum(), 1):.3f}" for y in sorted(set(yrs.tolist()))))
    # what kind of day is a blown-up day?  split the R-blown days and the L-blown days by cause
    for tag, sel in (("R blown (x >= +500)", fin & (x >= 500)), ("L blown (x <= -500)", fin & (x <= -500)),
                     ("edge (5 <= |x| < 500)", fin & (np.abs(x) >= 5) & (np.abs(x) < 500))):
        k = max(sel.sum(), 1)
        cl = P["cl"][:n]
        print(f"  {tag:<22} n={sel.sum():>8} ({sel.sum() / tot:.4f})  limit-up close {lim['up'][sel].mean():.3f}  touched-up {lim['touch_up'][sel].mean():.3f}  "
              f"limit-down close {lim['dn'][sel].mean():.3f}  touched-dn {lim['touch_dn'][sel].mean():.3f}  one-word {((lim['oneword_up'] | lim['oneword_dn'])[sel]).mean():.3f}  "
              f"close<3 {np.nanmean(cl[sel] < 3):.3f}  close<5 {np.nanmean(cl[sel] < 5):.3f}  amt-rank<0.2 {np.nanmean(pr_amt[sel] < 0.2):.3f}  "
              f"median |first| {np.nanmedian(np.abs(P['first'][:n][sel])):.4f}  median max(Ret) {np.nanmedian(P['maxret'][:n][sel]):.4f}  median min(Ret) {np.nanmedian(P['minret'][:n][sel]):.4f}")
    base_rates = {k: float(v[fin].mean()) for k, v in lim.items()}
    print("  base rates over all stock-days:", {k: round(v, 4) for k, v in base_rates.items()})
    return cr, cL


def section_C(P, sig, n, tr, lim, tgt, raw, ctl, first_day):
    hdr("C. the traded signal EMA(-X): who is in each decile (train)")
    x = P["x"][:n]
    s = sig[:n]
    dec = decile_of(s)
    fin = np.isfinite(s)
    T = slice(tr.start, tr.stop)
    big = np.isfinite(x) & (np.abs(x) >= 5)
    since = days_since(big)
    print(f"share of cells with |signal| >= 5 (a blown-up day still rules the EMA): {np.mean(np.abs(s[T][fin[T]]) >= 5):.3f};  "
          f">= 1: {np.mean(np.abs(s[T][fin[T]]) >= 1):.3f};  >= 0.3: {np.mean(np.abs(s[T][fin[T]]) >= 0.3):.3f}")
    print(f"share of cells whose last non-regular day was within 20 / 60 / 250 days: "
          f"{np.mean(since[T][fin[T]] <= 20):.3f} / {np.mean(since[T][fin[T]] <= 60):.3f} / {np.mean(since[T][fin[T]] <= 250):.3f};  never: {np.mean(since[T][fin[T]] >= 9999):.3f}")
    up20, dn20 = rolling_any(lim["up"], 20), rolling_any(lim["dn"], 20)
    up60 = rolling_any(lim["up"], 60)
    ow60 = rolling_any(lim["oneword_up"], 60)
    idx = np.arange(n)[:, None]
    age = idx - first_day[None, :]
    newl = (first_day[None, :] > 20) & (age < 250) & (age >= 0)
    pr = {k: pct_rank(ctl[k][:n]) for k in ("ctl_price", "ctl_cap", "ctl_amt", "ctl_turnrate", "ctl_ivol", "ctl_mom20")}
    ex_b, ex_r = excess(tgt[:n], fin), excess(raw[:n], fin)
    nolab = fin & ~np.isfinite(tgt[:n])
    print(f"\n{'dec':>3} {'med sig':>10} {'|s|>=5':>7} {'since':>6} {'up20':>6} {'up60':>6} {'dn20':>6} {'1w60':>6} {'new':>6} "
          f"{'price':>6} {'cap':>6} {'amt':>6} {'turn':>6} {'ivol':>6} {'mom20':>6} {'ex_buy':>8} {'ex_raw':>8} {'nolab':>6}")
    for d in range(10):
        sel = np.zeros_like(fin)
        sel[T] = (dec[T] == d)
        if sel.sum() == 0:
            continue
        print(f"{d + 1:>3} {np.median(s[sel]):10.2f} {np.mean(np.abs(s[sel]) >= 5):7.3f} {np.median(since[sel]):6.0f} "
              f"{up20[sel].mean():6.3f} {up60[sel].mean():6.3f} {dn20[sel].mean():6.3f} {ow60[sel].mean():6.3f} {newl[sel].mean():6.3f} "
              + " ".join(f"{np.nanmean(pr[k][sel]):6.2f}" for k in pr) +
              f" {ann(cell_mean_by_day(ex_b, sel)) * 100:+7.1f}% {ann(cell_mean_by_day(ex_r, sel)) * 100:+7.1f}% {nolab[sel].mean():6.3f}")
    print("(dec 1 = lowest signal = SHORT end = largest EMA of X; dec 10 = LONG end.  price..mom20 are mean within-day percentile ranks;"
          " up20 = had a limit-up close in the last 20 days; new = listed inside the sample and < 250 days old)")
    allsel = np.zeros_like(fin)
    allsel[T] = fin[T]
    print(f"universe: up20 {up20[allsel].mean():.3f} up60 {up60[allsel].mean():.3f} dn20 {dn20[allsel].mean():.3f} 1w60 {ow60[allsel].mean():.3f} "
          f"new {newl[allsel].mean():.3f} nolab {nolab[allsel].mean():.4f}")
    # finer cut of the short end: where inside decile 1 is the damage
    prs = pct_rank(s)
    print("\nfiner cut of the two ends (train): excess with the buyable label / raw label / share unbuyable")
    for lo_, hi_ in ((0.0, 0.01), (0.01, 0.02), (0.02, 0.05), (0.05, 0.10), (0.10, 0.20), (0.80, 0.90), (0.90, 0.95), (0.95, 0.98), (0.98, 1.0)):
        sel = np.zeros_like(fin)
        with np.errstate(invalid="ignore"):
            sel[T] = (prs[T] >= lo_) & (prs[T] < hi_ + (1e-9 if hi_ == 1.0 else 0))
        print(f"  signal pct [{lo_:.2f},{hi_:.2f})  ex_buy {ann(cell_mean_by_day(ex_b, sel)) * 100:+7.1f}%  ex_raw {ann(cell_mean_by_day(ex_r, sel)) * 100:+7.1f}%  "
              f"nolab {nolab[sel].mean():.3f}  up20 {up20[sel].mean():.3f}  new {newl[sel].mean():.3f}  med sig {np.median(s[sel]):.1f}")
    return dec, since, up20, newl


def section_D(P, n, lim, tgt, newl):
    hdr("D. event time: mean excess of the buyable label k days after each kind of non-regular day (utrain)")
    x = P["x"][:n]
    fin = np.isfinite(x)
    ex = excess(tgt[:n], fin)
    cl = P["cl"][:n]
    kinds = {
        "R blown & limit-up close": fin & (x >= 500) & lim["up"],
        "R blown & one-word up": fin & (x >= 500) & lim["oneword_up"],
        "R blown, no limit, close<3": fin & (x >= 500) & ~lim["up"] & ~lim["touch_up"] & (cl < 3),
        "R blown, no limit, close>=3": fin & (x >= 500) & ~lim["up"] & ~lim["touch_up"] & (cl >= 3),
        "L blown & limit-down close": fin & (x <= -500) & lim["dn"],
        "L blown, no limit, close<3": fin & (x <= -500) & ~lim["dn"] & ~lim["touch_dn"] & (cl < 3),
        "L blown, no limit, close>=3": fin & (x <= -500) & ~lim["dn"] & ~lim["touch_dn"] & (cl >= 3),
        "edge +(5..500)": fin & (x >= 5) & (x < 500),
        "edge -(5..500)": fin & (x <= -5) & (x > -500),
        "limit-up close, X regular": fin & (np.abs(x) < 5) & lim["up"],
        "limit-down close, X regular": fin & (np.abs(x) < 5) & lim["dn"],
        "new listing (<250d), any X": fin & newl,
    }
    lags = (0, 1, 2, 5, 10, 20, 40, 60, 120)
    print(f"{'kind':<30} {'n':>8} " + " ".join(f"{'k=' + str(k):>8}" for k in lags) + "   (bp per day; label of day t+k)")
    for name, sel in kinds.items():
        row = []
        for k in lags:
            if k == 0:
                v = ex[sel]
            else:
                v = ex[k:][sel[:-k]]
            v = v[np.isfinite(v)]
            row.append(v.mean() * 1e4 if v.size > 50 else float("nan"))
        print(f"{name:<30} {int(sel.sum()):>8} " + " ".join(f"{r:+8.1f}" for r in row))


def book_line(st, name, panel, base_sig, tr, sign=None):
    from partura.study_tools import bk, dg
    try:
        b = st.books(panel, fit="train", evals=("train", "valid"), sign=sign)
        sg = st.sign(panel, "train") if sign is None else sign
        vl, vs = b["by_rank"]["long"], b["by_rank"]["ls"]
        ic_tr = st.ic(panel, "train", sign=sg)["rank_ic"]
        ic_va = st.ic(panel, "valid", sign=sg)["rank_ic"]
        sm = bk.smoothed(sg * np.asarray(panel, dtype=np.float64), vl["hl"])
        rc = dg.pair_rank_corr(sm[tr], base_sig[tr]) if base_sig is not None else float("nan")
        cov = float(np.isfinite(panel[tr]).mean())
        print(f"{name:<26} {'+' if sg > 0 else '-'} | hlL {vl['hl']:>4g} Lnet {vl['splits']['train']['long_ann'] * 100:+6.1f}%/{vl['splits']['valid']['long_ann'] * 100:+6.1f}% "
              f"Lshp {vl['splits']['train']['long_sharpe']:+5.2f}/{vl['splits']['valid']['long_sharpe']:+5.2f} LTO {vl['splits']['train']['long_turnover'] * 100:4.1f}% "
              f"| hlS {vs['hl']:>4g} LS {vs['splits']['train']['ls_sharpe']:+5.2f}/{vs['splits']['valid']['ls_sharpe']:+5.2f} short {vs['splits']['train']['short_gross_ann'] * 100:+6.1f}% "
              f"| rIC {ic_tr:+.4f}/{ic_va:+.4f} | corr(base) {rc:+.2f} | fin {cov:.2f}", flush=True)
        return b
    except Exception as exc:                                    # one bad construction must not kill the run
        print(f"{name:<26} FAILED: {type(exc).__name__}: {exc}", flush=True)
        return None


def constructions(P, n_full, lim_full):
    """Day-level panels built from the pieces (full length; every operation is same-day or causal)."""
    x, R, L = P["x"], P["R"], P["L"]
    fin = np.isfinite(x)
    out = {}
    out["R only"] = R
    out["L only"] = L
    reg = fin & (R < 5) & (L < 5)
    out["X regular days only(NaN)"] = np.where(reg, x, np.nan)
    out["X regular, blown->0"] = np.where(fin, np.where(reg, x, 0.0), np.nan)
    out["clip(X,-3,3)"] = np.where(fin, np.clip(x, -3, 3), np.nan)
    out["sign event 1[R>=5]-1[L>=5]"] = np.where(fin, (R >= 5).astype(float) - (L >= 5).astype(float), np.nan)
    out["1[R>=5]"] = np.where(fin, (R >= 5).astype(float), np.nan)
    out["1[L>=5]"] = np.where(fin, (L >= 5).astype(float), np.nan)
    out["1[any side>=5]"] = np.where(fin, ((R >= 5) | (L >= 5)).astype(float), np.nan)
    with np.errstate(invalid="ignore", divide="ignore"):
        out["up-minute share"] = np.where(fin, P["nup"] / P["nval"], np.nan)
        out["down-minute share"] = np.where(fin, P["ndn"] / P["nval"], np.nan)
        out["zero-minute share"] = np.where(fin, 1.0 - (P["nup"] + P["ndn"]) / P["nval"], np.nan)
        out["up share - down share"] = np.where(fin, (P["nup"] - P["ndn"]) / P["nval"], np.nan)
    if P.get("x_nofirst") is not None:
        out["X without first minute"] = P["x_nofirst"]
    out["rank(X) then EMA"] = pct_rank(x)
    out["ES_up - q95 (no ratio)"] = np.where(fin, P["es_up"] - P["q95"], np.nan)
    out["ES_dn - |q05| (no ratio)"] = np.where(fin, P["es_dn"] - np.abs(P["q05"]), np.nan)
    out["(ES_up-q95)-(ES_dn-|q05|)"] = out["ES_up - q95 (no ratio)"] - out["ES_dn - |q05| (no ratio)"]
    with np.errstate(invalid="ignore", divide="ignore"):
        out["log(R/L) regular only"] = np.where(reg & (R > 0) & (L > 0), np.log(R / L), np.nan)
    out["limit-up close flag"] = np.where(fin, lim_full["up"].astype(float), np.nan)
    out["limit-down close flag"] = np.where(fin, lim_full["dn"].astype(float), np.nan)
    out["first minute Ret"] = P["first"]
    return out


def section_E(st, P, sig, tr, lim_full):
    hdr("E. quick book rows, same convention as the tables (fit = train; train/valid)")
    print("(a row is: direction | long-book view | L/S view | rank IC of the raw daily panel | rank corr of its traded signal with the base's | finite share)")
    book_line(st, "X (base)", P["x"], sig, tr)
    cons = constructions(P, P["x"].shape[0], lim_full)
    for name, pan in cons.items():
        book_line(st, name, pan, sig, tr)
    # the folded readings: is "no event" a long leg?   (direction forced, so that the LONG end is the named end)
    hdr("E2. folded readings (direction FORCED so the long end is the named end)")
    from partura.study_tools import bk
    s20 = bk.smoothed(np.asarray(P["x"], dtype=np.float64), 20)
    book_line(st, "long = small |EMA20(X)|", -np.abs(s20), sig, tr, sign=1.0)
    book_line(st, "long = small |X| today", -np.abs(P["x"]), sig, tr, sign=1.0)
    anyb = cons["1[any side>=5]"]
    book_line(st, "long = fewest blown days", -anyb, sig, tr, sign=1.0)
    book_line(st, "long = most zero minutes", cons["zero-minute share"], sig, tr, sign=1.0)
    book_line(st, "long = fewest zero minutes", -cons["zero-minute share"], sig, tr, sign=1.0)
    return cons


def section_F(st, P, sig, raw):
    hdr("F. the short leg with and without the could-not-be-bought filter (base signal, hl 20)")
    from partura.study_tools import bk
    for name in ("train", "valid"):
        d = st.slice(name)
        a = bk.book_row(sig, st.target(), d)
        b = bk.book_row(sig, raw, d)
        print(f"{name}: buyable label  short {a['short_gross_ann'] * 100:+6.1f}%  long gross {a['long_gross_ann'] * 100:+6.1f}%  LS {a['ls_sharpe']:+5.2f} | "
              f"unfiltered label  short {b['short_gross_ann'] * 100:+6.1f}%  long gross {b['long_gross_ann'] * 100:+6.1f}%  LS {b['ls_sharpe']:+5.2f}")


def section_G(P, sig, n, tr, ctl, cons):
    hdr("G. is the FOLDED signal a known exposure?  (train; mean daily rank corr)")
    from partura.study_tools import bk, dg
    T = slice(tr.start, tr.stop)
    s = sig[:n]
    fold = np.abs(pct_rank(s) - 0.5)
    z20 = bk.smoothed(np.asarray(cons["zero-minute share"], dtype=np.float64), 20)[:n]
    b20 = bk.smoothed(np.asarray(cons["1[any side>=5]"], dtype=np.float64), 20)[:n]
    items = {"EMA20(zero-minute share)": z20, "EMA20(1[any side blown])": b20}
    for k in ("ctl_price", "ctl_amt", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_dvol20", "ctl_mom20"):
        items[k] = ctl[k][:n]
    print(f"{'variable':<28} {'corr(signal, v)':>16} {'corr(fold, v)':>14} {'corr(fold, fold v)':>19}")
    for k, v in items.items():
        fv = np.abs(pct_rank(v) - 0.5)
        print(f"{k:<28} {dg.pair_rank_corr(s[T], v[T]):+16.3f} {dg.pair_rank_corr(fold[T], v[T]):+14.3f} {dg.pair_rank_corr(fold[T], fv[T]):+19.3f}")
    # how much of the fold do they span together (rank-space OLS, daily R2)?
    ctrl = {"zero20": z20[T], "blown20": b20[T], "price": ctl["ctl_price"][:n][T], "amt": ctl["ctl_amt"][:n][T],
            "turn": ctl["ctl_turnrate"][:n][T], "ivol": ctl["ctl_ivol"][:n][T], "cap": ctl["ctl_cap"][:n][T]}
    for names in (("blown20",), ("zero20",), ("price", "amt", "turn", "ivol", "cap"), tuple(ctrl)):
        _, info = dg.neutralise(fold[T], {k: ctrl[k] for k in names})
        print(f"  R2 of fold on {names}: {info['mean_r2']:.3f}")
    for names in (("blown20",), tuple(ctrl)):
        _, info = dg.neutralise(s[T], {k: ctrl[k] for k in names})
        print(f"  R2 of the signed signal on {names}: {info['mean_r2']:.3f}")


# ------------------------------------------------------------------ main
def show_sources():
    hdr("0. helper sources on the SERVER and probe self-checks")
    try:
        import inspect
        import torch
        from alphacube.operators import common as C
        print("torch", torch.__version__)
        for label in ("_sum", "_mean"):
            fn = getattr(C, label, None)
            if fn is not None:
                print(f"# common.{label}\n{inspect.getsource(inspect.unwrap(fn))}")
    except Exception as exc:
        print(f"sources failed: {type(exc).__name__}: {exc}")
    try:
        import importlib.util
        from partura.bridge import PARTURA_ROOT
        p = PARTURA_ROOT / "studies" / FID / "probes.py"
        spec = importlib.util.spec_from_file_location("f106_probes", p)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        mod.selfcheck_report()
    except Exception as exc:
        print(f"selfcheck failed: {type(exc).__name__}: {exc}")


def main():
    from partura.study_tools import Study, bk, dg
    _RANK[0] = dg.rank_rows
    show_sources()
    with Study(FID) as st:
        P = st.panels(EX)
        missing = [k for k in EX if k not in P]
        if missing:
            print("MISSING panels:", missing)
        P = {k: np.asarray(v, dtype=np.float64) for k, v in P.items()}
        ut, tr, va = st.slice("utrain"), st.slice("train"), st.slice("valid")
        n = ut.stop                                              # everything below is cut to [0, n): utrain only
        assert ut.start == tr.start and va.stop == ut.stop, (ut, tr, va)
        P["_dates"] = np.asarray(st.dates)
        tgt, raw = st.target(), st.target(buyable=False)
        ctl = {k: np.asarray(st.control(k), dtype=np.float64) for k in
               ("ctl_price", "ctl_amt", "ctl_cap", "ctl_turnrate", "ctl_ivol", "ctl_dvol20", "ctl_mom20", "ctl_rev1")}
        rev1 = ctl["ctl_rev1"]
        print(f"panel {P['x'].shape}, utrain rows [0,{n}), train {tr}, valid {va}; label finite share (utrain) {np.isfinite(tgt[:n]).mean():.3f}; "
              f"raw label finite share {np.isfinite(raw[:n]).mean():.3f}")
        # self-check of the pieces against the tree: R - L must reproduce X
        both = np.isfinite(P["x"][:n]) & np.isfinite(P["R"][:n]) & np.isfinite(P["L"][:n])
        d = np.abs(P["x"][:n][both] - (P["R"][:n][both] - P["L"][:n][both]))
        scale = np.maximum(np.abs(P["x"][:n][both]), 1.0)
        print(f"selfcheck: max relative |X - (R - L)| = {float((d / scale).max()):.2e} over {both.sum()} cells (must be ~1e-3 or less)")
        b0 = st.books(P["x"], fit="train", evals=("train", "valid"))
        sgn = st.sign(P["x"], "train")
        print(f"selfcheck: base sign {sgn:+.0f}, hl_long {b0['hl_long']}, hl_ls {b0['hl_ls']} (S0 table: -, 20, 20); "
              f"Lnet train {b0['by_rank']['long']['splits']['train']['long_ann'] * 100:+.1f}% (S0: -6.9%)")
        sig = bk.smoothed(sgn * P["x"], b0["hl_long"])

        lim_full = limit_flags(P["cl"], P["hi"], P["lo"], rev1)
        lim = {k: v[:n] for k, v in lim_full.items()}
        finc = np.isfinite(P["cl"][:n])
        first_day = np.where(finc.any(0), finc.argmax(0), n + 1)

        section_A(P, rev1, n)
        section_B(P, n, lim, tgt, raw, ctl)
        dec, since, up20, newl = section_C(P, sig, n, tr, lim, tgt, raw, ctl, first_day)
        section_D(P, n, lim, tgt, newl)
        section_F(st, P, sig, raw)
        cons = section_E(st, P, sig, tr, lim_full)
        section_G(P, sig, n, tr, ctl, cons)
    print("\n[x1 done]")


def selftest():
    """Every numeric routine on random arrays: shapes, NaN handling, a few known answers."""
    rng = np.random.default_rng(0)
    D, S = 120, 80
    a = rng.normal(size=(D, S))
    a[rng.random((D, S)) < 0.1] = np.nan
    pr = pct_rank(a)
    assert np.nanmin(pr) > 0 and np.nanmax(pr) < 1 and np.isnan(pr[np.isnan(a)]).all()
    d = decile_of(a)
    assert d.min() == -1 and d.max() == 9 and (d[np.isnan(a)] == -1).all()
    ex = excess(a, np.isfinite(a))
    assert abs(np.nanmean(ex, axis=1)).max() < 1e-12
    fl = rng.random((D, S)) < 0.05
    ra = rolling_any(fl, 5)
    assert ra[10, 3] == fl[6:11, 3].any() and ra[2, 0] == fl[0:3, 0].any()
    ds = days_since(fl)
    t0 = np.where(fl[:, 1])[0]
    if t0.size:
        assert ds[t0[0], 1] == 0 and (t0[0] == 0 or ds[t0[0] - 1, 1] == 9999 or ds[t0[0] - 1, 1] > 0)
    c = cls3(np.array([[0.5, 5.0, 499.0, 500.0, np.nan]]))
    assert c.tolist() == [[0, 1, 1, 2, -1]]
    cl = np.array([[11.0, 10.5, 9.0, 10.0]])
    hi = np.array([[11.0, 11.0, 10.0, 10.0]])
    lo = np.array([[10.0, 10.0, 9.0, 10.0]])
    rev = np.array([[1.10, 1.05, 0.90, 1.10]])
    lf = limit_flags(cl, hi, lo, rev)
    assert lf["up"].tolist() == [[True, False, False, True]] and lf["dn"].tolist() == [[False, False, True, False]]
    assert lf["oneword_up"].tolist() == [[False, False, False, True]]
    assert lf["touch_up"].tolist() == [[False, True, False, False]]            # 11/10.5*1.05 = 1.10: touched, closed below
    assert abs(ann(np.full(10, 0.001)) - 0.252) < 1e-12
    v = cell_mean_by_day(a, np.isfinite(a))
    assert np.allclose(v, np.nanmean(a, axis=1))
    P = {"x": a, "R": np.abs(a) + 1, "L": np.abs(a), "nup": np.full((D, S), 30.0), "ndn": np.full((D, S), 20.0),
         "nval": np.full((D, S), 241.0), "es_up": np.abs(a), "q95": np.abs(a) * 0.5, "es_dn": np.abs(a), "q05": -np.abs(a) * 0.5,
         "first": a * 0.01, "x_nofirst": a}
    cons = constructions(P, D, {"up": fl, "dn": ~fl})
    assert all(v.shape == (D, S) for v in cons.values()), {k: v.shape for k, v in cons.items()}
    assert np.isnan(cons["zero-minute share"][np.isnan(a)]).all()
    assert abs(np.nanmax(cons["zero-minute share"]) - (1 - 50 / 241)) < 1e-12
    print("selftest OK:", len(cons), "constructions;", "tree_on check:", "in_slice(Ret, 1, 240)" in tree_on("in_slice(Ret, 1, 240)"),
          "; no stray Ret:", tree_on("ZZ").count("Ret") == 0)


if __name__ == "__main__":
    if "selftest" in sys.argv[1:]:
        selftest()
    else:
        main()
