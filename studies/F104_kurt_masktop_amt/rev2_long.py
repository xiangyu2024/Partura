"""rev2 -- what the LONG-ONLY selection criterion asks of this study.  train / valid rows only; the holdout is never sliced.

The user holds a pure long book (A-shares): candidates are ranked by the NET long-leg excess and the pure-long
Sharpe, at the half-life fitted for the long book; a longer half-life is a legitimate, tradable lever.  The study
was written long/short-first, so five things were never asked directly:

  H. IS THE ORIGINAL'S LONG LEG JUST UNDER-SMOOTHED?  Its long-book half-life is 20 = the upper edge of the grid
     {0,1,2,3,5,10,20}, and the train sweep is still rising there.  Sweep every finalist (plus the original's
     30-day twin and F001's own member) over {0..20, 30, 40, 60, 90, 120} and read the long book on train AND
     valid.  It is also the fixed-half-life table ON VALID (the stage tables print it for train only), i.e. the
     way to tell structure from smoothing.
  P. PAIRED DIFFERENCES of the daily net long-book excess (candidate minus known family): is the composite's
     train advantage / valid shortfall more than noise?
  X. EXCLUSION OVERLAY -- the only way a long-only holder can use a "who NOT to buy" signal: take the known
     family's long decile, drop (or replace) the names this factor flags as worst, charge the extra turnover.
  A. ADDITIVE: rank(known family) + lambda * rank(factor) -- does the long leg beat the known family alone?
  R. RESIDUAL: the factor ranked INSIDE the known family's ventiles -- is there a long leg left once the
     liquidity position is taken out?
  L. where the long legs sit: liquidity location + selection inside the amt30 ventile, at the long-book half-lives.

Every section starts from a self-check against a number already in a stage table or in the rev1 log.
"""
import os
import sys
import traceback
import warnings

import numpy as np

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rev1_review import COST, EX as EX1, FID, TOP, ann, bucket, hdr, leg_decomp, pct_rank, row_corr, wb_rank  # noqa: E402
from partura.study_tools import Study, bk, dg  # noqa: E402
from partura.books import long_short_weights  # noqa: E402

EX = {k: EX1[k] for k in ("base", "base30", "amt30", "std30", "k30", "c30", "bk", "bc", "exclcv")}
EX["f001"] = "cross_max(day_std(Amt), 9)"
# sign and LONG-book half-life as fitted on TRAIN (the stage tables' 多头口径 columns)
FITL = {"base": (-1.0, 20), "base30": (-1.0, 20), "bk": (-1.0, 2), "bc": (-1.0, 1), "exclcv": (-1.0, 0),
        "std30": (-1.0, 0), "f001": (-1.0, 5), "amt30": (-1.0, 1)}
EXPECT = {"base": "hl 20  +4.8%/-5.8%  +1.00/-1.24", "base30": "hl 20  +5.7%/-1.9%  +1.18/-0.40",
          "bk": "hl 2  +6.0%/+0.1%  +1.20/+0.03", "bc": "hl 1  +5.2%/-0.0%  +1.12/-0.01",
          "exclcv": "hl 0  +15.0%/+19.1%  +2.50/+3.55", "std30": "hl 0  +12.6%/+22.3%  +1.78/+3.46",
          "f001": "hl 5  +13.7%/+22.2%  +1.99/+3.59", "amt30": "hl 1  +8.5%/+21.4%  +1.15/+3.24"}
HLS = (0, 1, 2, 3, 5, 10, 20, 30, 40, 60, 90, 120)
GRID = (0, 1, 2, 3, 5, 10, 20)


def p1(x):
    return f"{x * 100:+.1f}%"


def top_k(sig, k):
    """per-row: the k[t] names with the HIGHEST finite sig (ties by symbol order)."""
    fin = np.isfinite(sig)
    order = np.argsort(np.where(fin, -sig, np.inf), axis=1, kind="stable")
    pos = np.empty_like(order)
    np.put_along_axis(pos, order, np.arange(sig.shape[1])[None, :].repeat(sig.shape[0], 0), axis=1)
    return fin & (pos < np.asarray(k)[:, None])


def long_series(sel, uni, tgt):
    """A pure long book that holds `sel` equal-weight (book convention of partura.books.long_book: a held name
    without a label earns 0; benchmark = equal-weight label of the `uni` names that have one).
    Returns (net, gross, one-sided turnover, names held) per day; the book starts empty on the first row."""
    ok = uni & np.isfinite(tgt)
    r = np.where(ok, tgt, 0.0)
    k = sel.sum(1)
    wl = sel / np.maximum(k, 1)[:, None]
    n = ok.sum(1)
    ew = np.where(n > 0, r.sum(1) / np.maximum(n, 1), np.nan)
    gross = np.where(k > 0, (wl * r).sum(1) - ew, np.nan)
    traded = np.abs(np.diff(wl, axis=0, prepend=np.zeros((1, wl.shape[1])))).sum(1)
    return gross - COST * traded, gross, 0.5 * traded, k


def long_stats(sel, uni, tgt, sl):
    net, gross, turn, k = long_series(sel[sl], uni[sl], tgt[sl])
    a, g = bk.stats(net), bk.stats(gross)
    return {"net": a["ann"], "sharpe": a["sharpe"], "gross": g["ann"], "to": float(np.nanmean(turn)),
            "k": float(np.mean(k)), "mdd": a["mdd"], "series": net}


def paired(a, b):
    """annualised mean of (a - b) in points, and its t-statistic."""
    d = a - b
    d = d[np.isfinite(d)]
    if d.size < 3 or d.std() == 0:
        return float("nan"), float("nan")
    return float(d.mean() * 252 * 100), float(d.mean() / d.std(ddof=1) * np.sqrt(d.size))


def main(study_cls=Study):
    with study_cls(FID) as st:
        P = st.panels(EX)
        miss = [k for k in EX if k not in P]
        if miss:
            print("MISSING panels:", miss, flush=True)
        ut, tr_, va_ = st.slice("utrain"), st.slice("train"), st.slice("valid")
        off = ut.start
        tr = slice(tr_.start - off, tr_.stop - off)
        va = slice(va_.start - off, va_.stop - off)
        splits = (("train", tr), ("valid", va))
        tgt = np.asarray(st.target()[ut], dtype=np.float64)             # buyable label, utrain rows only
        yrs = np.array([int(str(d)[:4]) for d in np.asarray(st.dates)[ut]])
        years = [y for y in sorted(set(yrs.tolist())) if int((yrs == y).sum()) >= 20]
        print(f"rows: utrain {tgt.shape[0]} (starts at view row {off}), train {tr.stop - tr.start}, valid "
              f"{va.stop - va.start}; years {years}", flush=True)

        def ysl(y):
            idx = np.nonzero(yrs == y)[0]
            return slice(int(idx[0]), int(idx[-1]) + 1)

        def smooth(name, hl, sign=-1.0):
            return np.asarray(bk.smoothed(sign * np.asarray(P[name][:ut.stop], dtype=np.float64), hl)[ut],
                              dtype=np.float64)

        def run(fn):
            try:
                fn()
            except Exception:
                print(f"\n!!! {fn.__name__} failed:\n{traceback.format_exc()}", flush=True)

        # ------------------------------------------------------------ 0
        hdr("0. self-check: sign and half-life fitted on TRAIN for the LONG book, long book on train/valid.  "
            "the stage tables (多头口径) say: " + "; ".join(f"{k} {v}" for k, v in EXPECT.items()))
        SM = {}
        for n, (sg0, hl0) in FITL.items():
            if n not in P:
                continue
            x = np.asarray(P[n][ut], dtype=np.float64)
            sg = dg.sign_from(x[tr], tgt[tr])
            b = bk.books(sg * x, tgt, tr, {"train": tr, "valid": va}, cost=COST, top_frac=TOP, rank_by="long")
            lo, ls = b["by_rank"]["long"], b["by_rank"]["ls"]
            t_, v_ = lo["splits"]["train"], lo["splits"]["valid"]
            flag = "" if (sg == sg0 and lo["hl"] == hl0) else "   <-- DIFFERS from the hard-coded fit"
            print(f"{n:>7} sgn {sg:+.0f} hlL {lo['hl']:g} (hlS {ls['hl']:g}) | Lnet {p1(t_['long_ann'])}/{p1(v_['long_ann'])} | "
                  f"Lshp {t_['long_sharpe']:+.2f}/{v_['long_sharpe']:+.2f} | Lgross {p1(t_['long_gross_ann'])}/"
                  f"{p1(v_['long_gross_ann'])} | LTO {t_['long_turnover'] * 100:.1f}%/{v_['long_turnover'] * 100:.1f}% | LS@hlS "
                  f"{ls['splits']['train']['ls_sharpe']:+.2f}/{ls['splits']['valid']['ls_sharpe']:+.2f}{flag}", flush=True)
            SM[n] = smooth(n, hl0, sg0)
        a30 = np.asarray(P["amt30"][ut], dtype=np.float64)

        # ------------------------------------------------------------ H
        def section_h():
            hdr("H. half-life sweep BEYOND the grid, long book (sign fixed at -1; grid = 0..20, the rest is outside the "
                "user's grid and is a diagnosis, not a candidate).  self-check: base hl10 train Lnet +0.3%, hl20 +4.8%; "
                "bk hl2 +6.0%, hl20 +5.8%; std30 hl0 +12.6%, hl20 +8.4%; f001 hl5 +13.7% (stage sweep tables)")
            print("columns: hl | Lnet train/valid | Lshp train/valid | Lgross train/valid | LTO train/valid | LS train/valid")
            keep = {}
            for n in ("base", "base30", "bk", "bc", "exclcv", "std30", "f001"):
                if n not in P:
                    continue
                best = {"train": (-9e9, None), "valid": (-9e9, None)}
                for hl in HLS:
                    sm = smooth(n, hl)
                    r = [bk.book_row(sm, tgt, sl, COST, TOP) for _, sl in splits]
                    for i, s in enumerate(("train", "valid")):
                        if np.isfinite(r[i]["long_sharpe"]) and r[i]["long_sharpe"] > best[s][0]:
                            best[s] = (r[i]["long_sharpe"], hl)
                    mark = "  <- long-fit on the grid" if hl == FITL[n][1] else ("  (outside the grid)" if hl > 20 else "")
                    print(f"{n:>7} hl {hl:>3} | Lnet {p1(r[0]['long_ann']):>7}/{p1(r[1]['long_ann']):>7} | Lshp "
                          f"{r[0]['long_sharpe']:+.2f}/{r[1]['long_sharpe']:+.2f} | Lgross {p1(r[0]['long_gross_ann']):>7}/"
                          f"{p1(r[1]['long_gross_ann']):>7} | LTO {r[0]['long_turnover'] * 100:4.1f}%/"
                          f"{r[1]['long_turnover'] * 100:4.1f}% | LS {r[0]['ls_sharpe']:+.2f}/{r[1]['ls_sharpe']:+.2f}{mark}",
                          flush=True)
                    if n == "base" and hl in (20, 60, 120):
                        keep[hl] = sm
                print(f"{'':>7} best pure-long Sharpe over ALL swept half-lives: train at hl {best['train'][1]} "
                      f"({best['train'][0]:+.2f}); valid (not a fit -- for reading only) at hl {best['valid'][1]} "
                      f"({best['valid'][0]:+.2f})\n", flush=True)
            print("by year, the ORIGINAL's long book (Lnet; Lgross) at hl 20 / 60 / 120:")
            for hl, sm in keep.items():
                out = []
                for y in years:
                    r = bk.book_row(sm, tgt, ysl(y), COST, TOP)
                    out.append(f"{y} {p1(r['long_ann'])} ({p1(r['long_gross_ann'])})")
                print(f"   base hl {hl:>3}: " + "  ".join(out), flush=True)

        # ------------------------------------------------------------ P
        def section_p():
            hdr("P. paired difference of the DAILY net long-book excess (a minus b), annualised points and t; each at its "
                "own long-fit half-life")

            def net_of(n, sl):
                s = SM[n][sl]
                w = long_short_weights(s, TOP)
                return bk.long_book(w, s, tgt[sl], COST)[0]

            pairs = [("exclcv", "std30"), ("exclcv", "f001"), ("f001", "std30"), ("std30", "amt30"), ("bk", "base"),
                     ("bc", "base"), ("base30", "base"), ("bk", "bc")]
            for a, b in pairs:
                if a not in SM or b not in SM:
                    continue
                o = []
                for sname, sl in splits:
                    d, t = paired(net_of(a, sl), net_of(b, sl))
                    o.append(f"{sname} {d:+.1f} pts (t {t:+.1f})")
                yr = []
                for y in years:
                    d, t = paired(net_of(a, ysl(y)), net_of(b, ysl(y)))
                    yr.append(f"{y} {d:+.1f}")
                print(f"   {a:>7} - {b:<6} | " + " | ".join(o) + " | by year: " + "  ".join(yr), flush=True)

        # ------------------------------------------------------------ X
        def section_x():
            hdr("X. exclusion overlay on the KNOWN FAMILY's long decile (pure long book, net of 15 bp per unit traded).  "
                "'drop' = remove the flagged names, hold the rest equal-weight; 'refill' = replace them with the next names "
                "of the known-family ranking (same number of names); 'dsort' = known family's top 20%, keep the better "
                "half by the factor.  flagged = the worst q of the UNIVERSE by the factor's traded signal (base = original "
                "EMA-20; bk / bc = f_kurt30 / f_cv30 at their long-fit half-lives; wk20 = kurt30 ranked inside amt30 ventiles, "
                "hl 2; wbE20 = the original's EMA-20 signal ranked inside amt30 ventiles)")
            PR = {x: pct_rank(SM[x]) for x in ("base", "bk", "bc") if x in SM}
            XS = {x: SM[x] for x in PR}
            # the same-liquidity versions (rank INSIDE the amt30 ventile): "the most concentrated fifth among equally
            # liquid names" is what a long-only holder of an illiquid book would actually screen on
            qa = bucket(a30, np.isfinite(a30), 20)
            for name, y, hl in (("wk20", -np.asarray(P["k30"][ut], dtype=np.float64), 2), ("wbE20", SM["base"], 0)):
                w, u = wb_rank(y, np.where(np.isfinite(y), qa, np.nan), 20)
                XS[name] = np.asarray(bk.smoothed(w + 1e-6 * u, hl), dtype=np.float64)
                PR[name] = pct_rank(XS[name])
            del qa
            for kn in ("std30", "f001"):
                if kn not in SM:
                    continue
                ks = SM[kn]
                uni = np.isfinite(ks)
                sel0 = long_short_weights(ks, TOP) > 0
                k0 = sel0.sum(1)
                ref = [bk.book_row(ks, tgt, sl, COST, TOP) for _, sl in splits]
                b0 = [long_stats(sel0, uni, tgt, sl) for _, sl in splits]
                print(f"\n[{kn} @ hl {FITL[kn][1]}] self-check: book_row Lnet {p1(ref[0]['long_ann'])}/{p1(ref[1]['long_ann'])} "
                      f"Lshp {ref[0]['long_sharpe']:+.2f}/{ref[1]['long_sharpe']:+.2f}  ==  this section's book "
                      f"{p1(b0[0]['net'])}/{p1(b0[1]['net'])} {b0[0]['sharpe']:+.2f}/{b0[1]['sharpe']:+.2f}", flush=True)
                print("columns: Lnet train/valid | Lshp train/valid | Lgross train/valid | LTO train | names held | "
                      "paired net difference vs the known family alone, points (t) train / valid")
                print(f"   {kn + ' alone':<26} | {p1(b0[0]['net']):>7}/{p1(b0[1]['net']):>7} | {b0[0]['sharpe']:+.2f}/"
                      f"{b0[1]['sharpe']:+.2f} | {p1(b0[0]['gross']):>7}/{p1(b0[1]['gross']):>7} | {b0[0]['to'] * 100:4.1f}% | "
                      f"{b0[0]['k']:5.0f} |", flush=True)
                pk = pct_rank(ks)
                yearly = {}
                for x, pr in PR.items():
                    variants = []
                    for q in (0.1, 0.2):
                        bad = pr < q
                        variants.append((f"drop worst {q:.0%} by {x}", sel0 & ~bad))
                        variants.append((f"refill worst {q:.0%} by {x}", top_k(np.where(bad, np.nan, ks), k0)))
                    variants.append((f"drop BEST 20% by {x} (placebo)", sel0 & ~(pr > 0.8)))
                    top20 = pk > 0.8
                    w = pct_rank(np.where(top20, XS[x], np.nan))               # rank of the factor INSIDE the known top 20%
                    variants.append((f"dsort top20% x better half {x}", top20 & (w > 0.5)))
                    for name, sel in variants:
                        s = [long_stats(sel, uni, tgt, sl) for _, sl in splits]
                        d = [paired(s[i]["series"], b0[i]["series"]) for i in range(2)]
                        dropped = 1.0 - (sel & sel0).sum() / max(sel0.sum(), 1)
                        print(f"   {name:<34} | {p1(s[0]['net']):>7}/{p1(s[1]['net']):>7} | {s[0]['sharpe']:+.2f}/"
                              f"{s[1]['sharpe']:+.2f} | {p1(s[0]['gross']):>7}/{p1(s[1]['gross']):>7} | {s[0]['to'] * 100:4.1f}% | "
                              f"{s[0]['k']:5.0f} | {d[0][0]:+.1f} ({d[0][1]:+.1f}) / {d[1][0]:+.1f} ({d[1][1]:+.1f}) | "
                              f"left the known decile: {dropped:.0%}", flush=True)
                        if name.startswith("drop worst 20%"):
                            yearly[x] = sel
                print(f"   by year, net gain of 'drop worst 20%' over {kn} alone (points):")
                for x, sel in yearly.items():
                    out = []
                    for y in years:
                        sl = ysl(y)
                        a = long_stats(sel, uni, tgt, sl)
                        b = long_stats(sel0, uni, tgt, sl)
                        out.append(f"{y} {(a['net'] - b['net']) * 100:+.1f}")
                    print(f"      by {x:>4}: " + "  ".join(out), flush=True)

        # ------------------------------------------------------------ A
        def section_a():
            hdr("A. additive: rank(known family) + lambda * rank(factor), both as traded signals (already smoothed); the sum "
                "is traded as is.  'cub' = rank(known) - (1 - rank(factor))^3, the f_exclcv form in signed ranks")

            def ranks(ks, xs):
                ok = np.isfinite(ks) & np.isfinite(xs)
                return pct_rank(np.where(ok, ks, np.nan)), pct_rank(np.where(ok, xs, np.nan))

            def combo(rk, rx, lam, form):
                return rk + lam * rx if form == "lin" else rk - lam * (1.0 - rx) ** 3

            raw_a = -np.asarray(P["amt30"][ut], dtype=np.float64)
            raw_c = -np.asarray(P["bc"][ut], dtype=np.float64)
            chk = combo(*ranks(raw_a, raw_c), 1.0, "cub")
            r = [bk.book_row(chk, tgt, sl, COST, TOP) for _, sl in splits]
            print(f"self-check: rank(-amt30) - (1 - rank(-f_cv30))^3 on the raw panels, hl 0 -> Lnet {p1(r[0]['long_ann'])}/"
                  f"{p1(r[1]['long_ann'])} Lshp {r[0]['long_sharpe']:+.2f}/{r[1]['long_sharpe']:+.2f} LS {r[0]['ls_sharpe']:+.2f}/"
                  f"{r[1]['ls_sharpe']:+.2f}   (f_exclcv in the stage table: +15.0%/+19.1%, +2.50/+3.55, +3.94/+4.44)",
                  flush=True)
            del raw_a, raw_c, chk
            print("columns: Lnet train/valid | Lshp train/valid | Lgross train/valid | LTO train | LS train/valid | overlap of "
                  "the long decile with the known family's (train/valid) | paired net difference vs the known family alone, "
                  "points (t) train / valid")
            for kn in ("std30", "f001"):
                if kn not in SM:
                    continue
                ks = SM[kn]
                sel0 = long_short_weights(ks, TOP) > 0
                r0 = [bk.book_row(ks, tgt, sl, COST, TOP) for _, sl in splits]
                n0 = [bk.long_book(long_short_weights(ks[sl], TOP), ks[sl], tgt[sl], COST)[0] for _, sl in splits]
                print(f"\n   {kn + ' alone (hl ' + str(FITL[kn][1]) + ')':<30} | {p1(r0[0]['long_ann']):>7}/"
                      f"{p1(r0[1]['long_ann']):>7} | {r0[0]['long_sharpe']:+.2f}/{r0[1]['long_sharpe']:+.2f} | "
                      f"{p1(r0[0]['long_gross_ann']):>7}/{p1(r0[1]['long_gross_ann']):>7} | {r0[0]['long_turnover'] * 100:4.1f}% | "
                      f"{r0[0]['ls_sharpe']:+.2f}/{r0[1]['ls_sharpe']:+.2f} |", flush=True)
                for x in ("base", "base30", "bk", "bc"):
                    if x not in SM:
                        continue
                    rk, rx = ranks(ks, SM[x])
                    for lam, form in ((0.25, "lin"), (0.5, "lin"), (1.0, "lin"), (1.0, "cub")):
                        s = combo(rk, rx, lam, form)
                        r = [bk.book_row(s, tgt, sl, COST, TOP) for _, sl in splits]
                        selc = long_short_weights(s, TOP) > 0
                        ov = [(selc[sl] & sel0[sl]).sum() / max(selc[sl].sum(), 1) for _, sl in splits]
                        d = [paired(bk.long_book(long_short_weights(s[sl], TOP), s[sl], tgt[sl], COST)[0], n0[i])
                             for i, (_, sl) in enumerate(splits)]
                        print(f"   {kn} + {lam:g}*{form}({x})".ljust(33) + f" | {p1(r[0]['long_ann']):>7}/"
                              f"{p1(r[1]['long_ann']):>7} | {r[0]['long_sharpe']:+.2f}/{r[1]['long_sharpe']:+.2f} | "
                              f"{p1(r[0]['long_gross_ann']):>7}/{p1(r[1]['long_gross_ann']):>7} | "
                              f"{r[0]['long_turnover'] * 100:4.1f}% | {r[0]['ls_sharpe']:+.2f}/{r[1]['ls_sharpe']:+.2f} | "
                              f"{ov[0]:.0%}/{ov[1]:.0%} | {d[0][0]:+.1f} ({d[0][1]:+.1f}) / {d[1][0]:+.1f} ({d[1][1]:+.1f})",
                              flush=True)

        # ------------------------------------------------------------ R
        def section_r():
            hdr("R. residual long leg: the factor ranked INSIDE the known family's ventiles (every liquidity bucket gives the "
                "same share to every decile); sign -1; half-life fitted on train for the long book (grid).  self-check (rev1, "
                "inside amt30 ventiles, long-fit): kurt30 hl 2 +5.6%/-2.4% +1.09/-0.47; cv30 hl 2 +5.8%/-1.3% +1.19/-0.27; "
                "original's 30d mean hl 10 +3.8%/-2.0% +0.86/-0.51")
            print("columns: hlL | Lnet train/valid | Lshp train/valid | Lgross train/valid | LTO train | long decile's mean "
                  "amt30 rank train/valid")
            readers = [("kurt30 (30d mean)", -np.asarray(P["k30"][ut], dtype=np.float64)),
                       ("cv30 (30d mean)", -np.asarray(P["c30"][ut], dtype=np.float64)),
                       ("original, 30d mean", -np.asarray(P["base30"][ut], dtype=np.float64)),
                       ("original, EMA-20 signal", SM["base"])]
            for gname in ("amt30", "std30"):
                g = np.asarray(P[gname][ut], dtype=np.float64)
                for rname, y in readers:
                    q = bucket(g, np.isfinite(y) & np.isfinite(g), 20)
                    w, u = wb_rank(y, q, 20)
                    s = w + 1e-6 * u
                    b = bk.books(s, tgt, tr, {"train": tr, "valid": va}, cost=COST, top_frac=TOP, rank_by="long")
                    lo = b["by_rank"]["long"]
                    t_, v_ = lo["splits"]["train"], lo["splits"]["valid"]
                    sm = np.asarray(bk.smoothed(s, lo["hl"]), dtype=np.float64)
                    pa = pct_rank(np.where(np.isfinite(sm), a30, np.nan))
                    sel = long_short_weights(sm, TOP) > 0
                    loc = [float(np.nanmean(pa[sl][sel[sl]])) for _, sl in splits]
                    print(f"   {rname:<24} inside {gname} ventiles | hlL {lo['hl']:>2g} | {p1(t_['long_ann']):>7}/"
                          f"{p1(v_['long_ann']):>7} | {t_['long_sharpe']:+.2f}/{v_['long_sharpe']:+.2f} | "
                          f"{p1(t_['long_gross_ann']):>7}/{p1(v_['long_gross_ann']):>7} | {t_['long_turnover'] * 100:4.1f}% | "
                          f"{loc[0]:.2f}/{loc[1]:.2f}", flush=True)

        # ------------------------------------------------------------ L
        def section_l():
            hdr("L. long leg = 'location' (a basket with the same amt30-ventile distribution) + 'selection' (inside the "
                "ventile); gross, annualised %, train / valid; each signal at its long-fit half-life.  self-check (rev1 B, "
                "same half-life): base +10.1 = +1.0 + +9.1 / +0.4 = -2.4 + +2.8; exclcv +19.1 = +10.1 + +9.0 / +23.0 = "
                "+20.5 + +2.6; std30 +15.2 = +10.2 + +5.0 / +24.4 = +23.4 + +1.0")
            for n in ("base", "base30", "bk", "bc", "exclcv", "std30", "f001", "amt30"):
                if n not in SM:
                    continue
                d = [leg_decomp(SM[n][sl], tgt[sl], a30[sl]) for _, sl in splits]
                lg = [tuple(ann(x) for x in d[i]["long"]) for i in range(2)]
                r = [bk.book_row(SM[n], tgt, sl, COST, TOP) for _, sl in splits]
                cost = [(r[i]["long_gross_ann"] - r[i]["long_ann"]) * 100 for i in range(2)]
                print(f"{n:>7} hl {FITL[n][1]:>2} | long {lg[0][0]:+5.1f} = {lg[0][1]:+5.1f} + {lg[0][2]:+5.1f} / {lg[1][0]:+5.1f} = "
                      f"{lg[1][1]:+5.1f} + {lg[1][2]:+5.1f} | cost of the long book {cost[0]:.1f} / {cost[1]:.1f} pts | "
                      f"selection net of cost {lg[0][2] - cost[0]:+.1f} / {lg[1][2] - cost[1]:+.1f}", flush=True)
            print("\nby year (utrain): long leg total = location + selection (gross)")
            for n in ("base", "bk", "exclcv", "std30", "f001"):
                if n not in SM:
                    continue
                d = leg_decomp(SM[n], tgt, a30)
                out = []
                for y in years:
                    m = yrs == y
                    lo = [ann(x[m]) for x in d["long"]]
                    out.append(f"{y}: {lo[0]:+.1f}={lo[1]:+.1f}{lo[2]:+.1f}")
                print(f"{n:>7}  " + "   ".join(out), flush=True)
            print("\ntraded-signal rank correlations at the long-fit half-lives (train / valid):")
            for a, b in (("exclcv", "std30"), ("exclcv", "f001"), ("exclcv", "base"), ("exclcv", "amt30"), ("f001", "std30"),
                         ("bk", "base"), ("bc", "base"), ("std30", "base"), ("base30", "base")):
                if a in SM and b in SM:
                    print(f"   {a:>7} ~ {b:<6}  {row_corr(SM[a][tr], SM[b][tr]):+.2f} / {row_corr(SM[a][va], SM[b][va]):+.2f}",
                          flush=True)

        for sec in (section_h, section_p, section_x, section_a, section_r, section_l):
            run(sec)
        try:
            from partura import guard
            print(f"\nanon of this process at the end: {guard.self_anon_gb():.2f} GiB", flush=True)
        except Exception:
            pass
    print("\n[rev2 done]")


if __name__ == "__main__":
    main()
