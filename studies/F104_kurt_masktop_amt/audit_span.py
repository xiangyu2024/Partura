"""audit_span -- reviewer's refutation attempt (mechanism / overfitting lens).  train / valid rows only.

The study says: "the mask node is an accidental liquidity conditioning; written as an explicit residual
(f_kurt30) it is the same mechanism without the liquidity contamination", and "the money is in the short leg".
Three things that claim rests on were never measured:

  A. SPANNING.  If original = (own concentration | liquidity) + a liquidity tilt, then the original's traded
     signal regressed on {f_kurt30, amt30} (and f_cv30) should leave a residual with ~no rank IC.  If the
     residual keeps a large share of the IC in BOTH train and valid, the mask carries predictive content the
     stated mechanism does not name, and the "purified" form is a different factor rather than a cleaner one.
     Run on the EMA-20 original and on its 30-day-mean twin (same time scale as f_kurt30), both directions.
  B. TAILS.  "orthogonal to liquidity (R2 0.002)" is a statement about the linear rank fit.  The decile book
     lives in the tails: where do f_kurt30's short / long deciles sit in amt30?
  C. LABEL.  A name locked at limit-up at the t+1 open has a NaN label and earns 0 in the SHORT book too.
     The short decile here is "recent big gainers".  How many locked cells sit in each short decile, what did
     they actually return, and what is the L/S Sharpe if the short leg is charged the raw label?
  D. Is f_exclcv's long decile "the illiquid decile minus the most concentrated 10-20%"?
"""
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402
from partura.books import long_short_weights  # noqa: E402

FID = "F104_kurt_masktop_amt"
A30 = "cross_mean(day_sum(Amt), 30)"
BK = f"cs_regres(cs_rank(cross_mean(day_kurt(Amt), 30)), cs_rank({A30}))"
BC = f"cs_regres(cs_rank(cross_mean(div(day_std(Amt), day_mean(Amt)), 30)), cs_rank({A30}))"
EX = {
    "base":   "day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))",
    "base30": "cross_mean(day_kurt(nt_cs_mask_top_replace_mean_neg(Amt)), 30)",
    "amt30":  A30,
    "std30":  "cross_mean(day_std(Amt), 30)",
    "bk":     BK,
    "bc":     BC,
    "exclcv": f"add(cs_rank({A30}), pow_3(cs_rank({BC})))",
}
# sign and half-life as fitted on TRAIN in the stage tables
FIT = {"base": (-1.0, 20), "base30": (-1.0, 1), "bk": (-1.0, 1), "bc": (-1.0, 0), "exclcv": (-1.0, 0),
       "std30": (-1.0, 0), "amt30": (-1.0, 1)}
COST = 0.0015


def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


def pct_rank(a):
    r = dg.rank_rows(np.asarray(a, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def main():
    with Study(FID) as st:
        P = st.panels(EX)
        miss = [k for k in EX if k not in P]
        if miss:
            print("MISSING panels:", miss)
        ut, tr_, va_ = st.slice("utrain"), st.slice("train"), st.slice("valid")
        off = ut.start
        tr = slice(tr_.start - off, tr_.stop - off)
        va = slice(va_.start - off, va_.stop - off)
        splits = (("train", tr), ("valid", va))
        tgt = np.asarray(st.target()[ut], dtype=np.float64)                     # buyable label, utrain rows only
        SM = {n: np.asarray(bk.smoothed(FIT[n][0] * P[n].astype(np.float64), FIT[n][1])[ut], dtype=np.float64)
              for n in FIT if n in P}
        RAW = {n: np.asarray(P[n][ut], dtype=np.float64) for n in P}

        # ------------------------------------------------------------ 0
        hdr("0. self-check against the stage tables (LS net train/valid: base 3.91/1.47, bk 3.75/1.91, "
            "bc 3.77/2.37, exclcv 3.94/4.44, std30 1.87/3.70, base30 3.25/1.38)")
        for n in SM:
            r = [bk.book_row(SM[n], tgt, sl, COST) for _, sl in splits]
            ic = [dg.ic_row(SM[n][sl], tgt[sl], sign=1.0) for _, sl in splits]
            print(f"{n:>7} hl {FIT[n][1]:>2}  LS {r[0]['ls_sharpe']:+.2f}/{r[1]['ls_sharpe']:+.2f}  "
                  f"traded rIC {ic[0]['rank_ic']:+.4f}/{ic[1]['rank_ic']:+.4f} (t {ic[0]['rank_ic_t']:+.1f}/"
                  f"{ic[1]['rank_ic_t']:+.1f})  Lnet {r[0]['long_ann'] * 100:+.1f}%/{r[1]['long_ann'] * 100:+.1f}%",
                  flush=True)

        # ------------------------------------------------------------ A
        hdr("A. spanning: rank-space daily OLS residual of a TRADED signal on other traded signals (dg.neutralise)")
        print("columns: R2 | residual rank IC train/valid (t) | gross LS Sharpe train/valid | "
              "long gross / short gross excess train, valid | share of rank IC kept train/valid")

        def line(name, y, ctl, ref_ic):
            if ctl:
                res, info = dg.neutralise(y, ctl)
                r2 = info["mean_r2"]
            else:
                res, r2 = y, float("nan")
            ic = [dg.ic_row(res[sl], tgt[sl], sign=1.0) for _, sl in splits]
            b = [bk.book_row(res, tgt, sl, COST) for _, sl in splits]
            keep = ["%.0f%%" % (100 * ic[i]["rank_ic"] / ref_ic[i]) if ref_ic else "--" for i in range(2)]
            print(f"{name:<26} R2 {r2:5.3f} | rIC {ic[0]['rank_ic']:+.4f}/{ic[1]['rank_ic']:+.4f} "
                  f"(t {ic[0]['rank_ic_t']:+5.1f}/{ic[1]['rank_ic_t']:+5.1f}) | LSgross {b[0]['ls_gross_sharpe']:+.2f}/"
                  f"{b[1]['ls_gross_sharpe']:+.2f} | L {b[0]['long_gross_ann'] * 100:+5.1f}% S "
                  f"{b[0]['short_gross_ann'] * 100:+5.1f}% , L {b[1]['long_gross_ann'] * 100:+5.1f}% S "
                  f"{b[1]['short_gross_ann'] * 100:+5.1f}% | kept {keep[0]}/{keep[1]}", flush=True)
            return [ic[0]["rank_ic"], ic[1]["rank_ic"]]

        A = RAW["amt30"]
        for dep in ("base", "base30"):
            ref = line(f"{dep}", SM[dep], None, None)
            line(f"{dep} | amt30", SM[dep], {"a": A}, ref)
            line(f"{dep} | bk", SM[dep], {"k": SM["bk"]}, ref)
            line(f"{dep} | bk, amt30", SM[dep], {"k": SM["bk"], "a": A}, ref)
            line(f"{dep} | bk, bc, amt30", SM[dep], {"k": SM["bk"], "c": SM["bc"], "a": A}, ref)
            print()
        for dep in ("bk", "bc"):
            ref = line(f"{dep}", SM[dep], None, None)
            line(f"{dep} | base30", SM[dep], {"o": SM["base30"]}, ref)
            line(f"{dep} | base30, amt30", SM[dep], {"o": SM["base30"], "a": A}, ref)
            line(f"{dep} | base(EMA20), amt30", SM[dep], {"o": SM["base"], "a": A}, ref)
            print()

        # ------------------------------------------------------------ B
        hdr("B. where the decile books of the 'liquidity-orthogonal' residual sit in amt30 (traded signal)")
        cap = np.asarray(st.control("ctl_cap")[ut], dtype=np.float64)
        for n in ("bk", "bc", "base"):
            for sname, sl in splits:
                s = SM[n][sl]
                okc = np.isfinite(s)
                w = long_short_weights(s, 0.10)
                ra = pct_rank(np.where(okc, A[sl], np.nan))
                rc = pct_rank(np.where(okc, cap[sl], np.nan))
                for leg, m in (("short", w < 0), ("long", w > 0)):
                    x = ra[m]
                    x = x[np.isfinite(x)]
                    print(f"{n:>5} [{sname}] {leg:>5} decile: mean amt30 rank {x.mean():.2f}  "
                          f"share in least-active quintile {np.mean(x < 0.2):.0%}  in most-active quintile "
                          f"{np.mean(x > 0.8):.0%}  mean cap rank {np.nanmean(rc[m]):.2f}", flush=True)

        # ------------------------------------------------------------ C
        hdr("C. locked-at-limit-up cells (label NaN -> earns 0 in the short book): how much of the short leg is that?")
        ps = st.ps
        keep = (ps.label_buyable, ps._targets)
        ps.label_buyable, ps._targets = False, {}
        try:
            traw_full = np.asarray(ps.target(1), dtype=np.float64)
        finally:
            ps.label_buyable, ps._targets = keep
        traw = traw_full[ut]
        del traw_full
        both = np.isfinite(tgt) & np.isfinite(traw)
        print(f"label check: buyable-finite cells {int(np.isfinite(tgt).sum())}, raw-finite {int(np.isfinite(traw).sum())}, "
              f"buyable finite but raw NaN {int((np.isfinite(tgt) & ~np.isfinite(traw)).sum())}, "
              f"max |diff| where both finite {float(np.nanmax(np.abs(tgt[both] - traw[both]))):.2e}")
        locked = np.isfinite(traw) & ~np.isfinite(tgt)
        for sname, sl in splits:
            lk = locked[sl]
            print(f"[{sname}] locked cells: {lk.mean() * 100:.3f}% of all cells; mean raw label on them "
                  f"{np.nanmean(traw[sl][lk]) * 1e4:+.0f} bp; per day {lk.sum(1).mean():.1f} names", flush=True)

        def hybrid(s, tb, tr_raw):
            """L/S daily gross with the long leg on the buyable label and the short leg on the raw label."""
            w = long_short_weights(s, 0.10)
            rb = np.where(np.isfinite(tb), tb, 0.0)
            rr = np.where(np.isfinite(tr_raw), tr_raw, 0.0)
            gross = (np.clip(w, 0.0, None) * rb).sum(1) + (np.clip(w, None, 0.0) * rr).sum(1)
            turn = 0.5 * np.abs(np.diff(w, axis=0, prepend=np.zeros((1, w.shape[1])))).sum(1)
            net = gross - turn * 2.0 * COST
            ws = np.clip(-w, 0.0, None) * 2.0
            ok = np.isfinite(s) & np.isfinite(tb)
            n = ok.sum(1)
            ew = np.where(n > 0, np.where(ok, tb, 0.0).sum(1) / np.maximum(n, 1), np.nan)
            short_ex = np.where(ws.sum(1) > 0, ew - (ws * rr).sum(1), np.nan)
            return bk.stats(net), bk.stats(gross), bk.stats(short_ex)

        print("columns: locked share in universe / short decile / long decile | mean raw label of locked cells in the "
              "short decile | LS net Sharpe buyable -> short leg on raw label | short-leg gross excess buyable -> raw")
        for n in ("base", "bk", "bc", "exclcv", "std30", "amt30"):
            for sname, sl in splits:
                s, tb, trw, lk = SM[n][sl], tgt[sl], traw[sl], locked[sl]
                okc = np.isfinite(s)
                w = long_short_weights(s, 0.10)
                sh, lg = w < 0, w > 0
                ref = bk.book_row(SM[n], tgt, sl, COST)
                chk_net, _, chk_short = hybrid(s, tb, tb)            # self-check: must equal book_row
                hyb_net, _, hyb_short = hybrid(s, tb, trw)
                print(f"{n:>7} [{sname}] locked {lk[okc].mean() * 100:.2f}% / {lk[sh].mean() * 100:.2f}% / "
                      f"{lk[lg].mean() * 100:.2f}% | {np.nanmean(trw[sh & lk]) * 1e4:+.0f} bp | LS {ref['ls_sharpe']:+.2f} "
                      f"(chk {chk_net['sharpe']:+.2f}) -> {hyb_net['sharpe']:+.2f} | short {ref['short_gross_ann'] * 100:+.1f}% "
                      f"(chk {chk_short['ann'] * 100:+.1f}%) -> {hyb_short['ann'] * 100:+.1f}%", flush=True)

        # ------------------------------------------------------------ D
        hdr("D. f_exclcv's long decile: is it 'the least-active decile minus the most concentrated 10-20%'?")
        for sname, sl in splits:
            s = SM["exclcv"][sl]
            okc = np.isfinite(s)
            lg = long_short_weights(s, 0.10) > 0
            rc = pct_rank(np.where(okc, RAW["bc"][sl], np.nan))       # 1 = most concentrated given liquidity
            ra = pct_rank(np.where(okc, A[sl], np.nan))
            l_amt = long_short_weights(SM["amt30"][sl], 0.10) > 0
            l_std = long_short_weights(SM["std30"][sl], 0.10) > 0
            x, y = rc[lg], ra[lg]
            print(f"[{sname}] long decile of f_exclcv: concentration rank mean {np.nanmean(x):.2f}, max {np.nanmax(x):.2f}, "
                  f"share >0.6 {np.nanmean(x > 0.6):.1%}, share >0.4 {np.nanmean(x > 0.4):.1%}; amt30 rank mean "
                  f"{np.nanmean(y):.2f}, p90 {np.nanpercentile(y, 90):.2f}; overlap with amt30 long {np.mean(l_amt[lg]):.0%}, "
                  f"with std30 long {np.mean(l_std[lg]):.0%}", flush=True)
            x2 = rc[l_std]
            print(f"[{sname}] long decile of f_std30: concentration rank mean {np.nanmean(x2):.2f}, share >0.8 "
                  f"{np.nanmean(x2 > 0.8):.1%}, share >0.6 {np.nanmean(x2 > 0.6):.1%}", flush=True)
    print("\n[audit_span done]")


if __name__ == "__main__":
    main()
