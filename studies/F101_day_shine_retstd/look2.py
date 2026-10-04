"""F101, after S1: the surge mask changes the SHORT leg, not the long leg.

S1 said: the same 5-minute std taken at ALL minutes (roll5) or at NON-surge minutes, folded the same
way, loses half of the short leg and keeps (train) or greatly improves (valid) the long leg.  Questions
the stage tables cannot answer:

  A  How much of the original is "a fold of a volatility level"?  Linear controls cannot span a V, so
     the batch R^2 (0.154) is an underestimate: regress the traded signal on FOLDED controls.
  B  Which names does the original short / hold that the roll5 fold does not, and how do those names do?
     (set overlap of the deciles and next-day excess of the three regions)
  C  What is the burst ratio J / roll5 related to?  What is roll5 related to (price = tick size)?
  D  Who is in the long decile of the roll5 fold (price, size, turnover ...) vs the original's?
  E  Year by year: long-leg gross / net excess and long-only Sharpe of the candidates.
  F  Is "fold-then-smooth beats smooth-then-fold" also true on roll5?  Where does its cs mean sit?

Only train / valid are read.
"""
import warnings

import numpy as np

from partura.study_tools import Study, bk, dg

warnings.simplefilter("ignore", RuntimeWarning)
FID = "F101_day_shine_retstd"
V = "in_slice(Volume, 2, 237)"
DV = f"sub({V}, in_delay({V}, 1))"
MASK = f"is_gt({DV}, add(in_mean_full({DV}), in_stddev_full({DV})))"
R = "in_slice(Ret, 2, 237)"
J_EXPR = f"day_mean(in_sustain_stddev({MASK}, {R}, 5))"


def fold(x):
    return np.abs(x - np.nanmean(x, axis=1, keepdims=True))


def pct(x):
    r = dg.rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def ema(x, hl):
    return bk.smoothed(np.asarray(x, dtype=np.float64), hl)


def excess(tgt, sig):
    ok = np.isfinite(sig) & np.isfinite(tgt)
    r = np.where(ok, tgt, 0.0)
    ew = r.sum(1) / np.maximum(ok.sum(1), 1)
    return np.where(ok, tgt - ew[:, None], np.nan)


def decile(sig, top=True):
    q = np.nanpercentile(sig, 90 if top else 10, axis=1, keepdims=True)
    return (sig >= q) if top else (sig <= q)


with Study(FID) as st:
    P = st.panels({"J": J_EXPR, "roll5": f"day_mean(in_stddev_rolling({R}, 5))"})
    J, roll5 = np.asarray(P["J"], dtype=np.float64), np.asarray(P["roll5"], dtype=np.float64)
    ctl = {k: np.asarray(st.control(k), dtype=np.float64) for k in
           ("ctl_ivol", "ctl_dvol20", "ctl_turnrate", "ctl_cap", "ctl_amt", "ctl_price", "ctl_range", "ctl_rev1", "ctl_mom20")}
    tgt = np.asarray(st.target(), dtype=np.float64)
    tr, va = st.slice("train"), st.slice("valid")
    SP = {"train": tr, "valid": va}
    sig_o = -ema(fold(J), 10)            # the original, as traded
    sig_r = -ema(fold(roll5), 20)        # the roll5 fold, as traded (hl fitted on train in S1 = 20)
    sig_k = -ema(np.abs(pct(J) - 0.5), 20)   # rank fold of J (S1: hl 20)

    # ---- A: folded controls
    print("== A  R2 of the ORIGINAL traded signal on controls (rank space, train); residual rank IC / gross LS Sharpe / long gross")
    yz = dg._zrank(sig_o[tr])

    def rep(name, cs):
        cz = {k: dg._zrank(v[tr]) for k, v in cs.items()}
        resid, info = dg.neutralise(yz, cz, panel_ready=True, controls_ready=True)
        ic = np.nanmean(dg.rank_ic_series(resid, tgt[tr]))
        b = bk.book_row(resid, tgt[tr], slice(0, resid.shape[0]))
        print(f"  {name:<46} R2 {info['mean_r2']:.3f}  resid rIC {ic:+.4f}  LSgross {b['ls_gross_sharpe']:+.2f}  "
              f"Lgross {b['long_gross_ann']*100:+5.1f}%  short {b['short_gross_ann']*100:+5.1f}%", flush=True)

    b0 = bk.book_row(sig_o, tgt, tr)
    print(f"  {'(unneutralised)':<46} R2   —    rIC {np.nanmean(dg.rank_ic_series(sig_o[tr], tgt[tr])):+.4f}  "
          f"LSgross {b0['ls_gross_sharpe']:+.2f}  Lgross {b0['long_gross_ann']*100:+5.1f}%  short {b0['short_gross_ann']*100:+5.1f}%")
    rep("9 linear controls (the batch set)", ctl)
    rep("fold(ivol) daily", {"a": fold(ctl["ctl_ivol"])})
    rep("EMA10 fold(ivol)", {"a": ema(fold(ctl["ctl_ivol"]), 10)})
    rep("EMA10 fold(roll5)", {"a": ema(fold(roll5), 10)})
    rep("EMA10 of fold(ivol), fold(roll5), fold(dvol20)", {"a": ema(fold(ctl["ctl_ivol"]), 10), "b": ema(fold(roll5), 10),
                                                         "c": ema(fold(ctl["ctl_dvol20"]), 10)})
    rep("EMA10 ivol, roll5, J levels (no fold)", {"a": ema(ctl["ctl_ivol"], 10), "b": ema(roll5, 10), "c": ema(J, 10)})
    rep("9 linear + 3 EMA10 folds", {**ctl, "a": ema(fold(ctl["ctl_ivol"]), 10), "b": ema(fold(roll5), 10),
                                    "c": ema(fold(ctl["ctl_dvol20"]), 10)})

    # ---- B: overlap of the deciles
    print("== B  decile overlap original vs roll5 fold; mean next-day excess (annualised %) of each region")
    for sn, s in SP.items():
        ex = excess(tgt[s], sig_o[s])
        for leg, top in (("long", True), ("short", False)):
            a, b = decile(sig_o[s], top), decile(sig_r[s], top)
            both, only_o, only_r = a & b, a & ~b, b & ~a
            f = lambda m: np.nanmean(np.where(m, ex, np.nan)) * 252 * 100
            print(f"  {sn} {leg:<5}: overlap {both.sum() / a.sum():.2f}  both {f(both):+6.1f}  only-original {f(only_o):+6.1f}  "
                  f"only-roll5 {f(only_r):+6.1f}", flush=True)

    # ---- C: what are the burst ratio and roll5 related to?
    print("== C  daily rank corr (train)")
    B = J / roll5
    others = {**ctl, "J": J, "roll5": roll5}
    print("  burst ratio J/roll5 ~ " + "  ".join(f"{k[4:] if k.startswith('ctl_') else k} {dg.pair_rank_corr(B[tr], v[tr]):+.2f}" for k, v in others.items()))
    print("  roll5 ~ " + "  ".join(f"{k[4:] if k.startswith('ctl_') else k} {dg.pair_rank_corr(roll5[tr], v[tr]):+.2f}" for k, v in others.items() if k != "roll5"))
    print("  J ~ " + "  ".join(f"{k[4:] if k.startswith('ctl_') else k} {dg.pair_rank_corr(J[tr], v[tr]):+.2f}" for k, v in others.items() if k != "J"))
    print(f"  traded signals: orig~roll5fold {dg.pair_rank_corr(sig_o[tr], sig_r[tr]):+.3f}  orig~rankfold {dg.pair_rank_corr(sig_o[tr], sig_k[tr]):+.3f}  "
          f"roll5fold~rankfold {dg.pair_rank_corr(sig_r[tr], sig_k[tr]):+.3f}", flush=True)
    m = np.nanmean(roll5[tr], axis=1, keepdims=True)
    print(f"  percentile of the cs mean inside roll5: {np.nanmean(np.where(np.isfinite(roll5[tr]), roll5[tr] < m, np.nan)):.3f};  "
          f"J/roll5 median {np.nanmedian(B[tr]):.2f} p10 {np.nanpercentile(B[tr], 10):.2f} p90 {np.nanpercentile(B[tr], 90):.2f}")

    # ---- D: who is in the legs
    print("== D  mean within-day percentile of each characteristic inside the legs (train)")
    feats = {"J": pct(J)[tr], "roll5": pct(roll5)[tr], "burst": pct(B)[tr], **{k[4:]: pct(v)[tr] for k, v in ctl.items()}}
    for nm, sg in (("original", sig_o), ("roll5 fold", sig_r), ("rank fold J", sig_k)):
        for leg, top in (("long", True), ("short", False)):
            msk = decile(sg[tr], top)
            print(f"  {nm:<12} {leg:<5} " + " ".join(f"{k} {np.nanmean(v[msk]):.2f}" for k, v in feats.items()), flush=True)

    # ---- E: year by year
    print("== E  per calendar year: LS net Sharpe | long gross % | long net % | long-only Sharpe")
    years = np.array([int(str(d)[:4]) for d in st.dates])
    end = va.stop
    for nm, sg in (("original hl10", sig_o), ("roll5 fold hl20", sig_r), ("rank fold J hl20", sig_k),
                   ("fold(ivol) hl10", -ema(fold(ctl["ctl_ivol"]), 10))):
        out = []
        for y in sorted(set(years[:end].tolist())):
            idx = np.where(years[:end] == y)[0]
            b = bk.book_row(sg, tgt, slice(idx[0], idx[-1] + 1))
            out.append(f"{y}: {b['ls_sharpe']:+.2f}|{b['long_gross_ann']*100:+5.1f}|{b['long_ann']*100:+5.1f}|{b['long_sharpe']:+.2f}")
        print(f"  {nm:<17} " + "  ".join(out), flush=True)

    # ---- F: fold-then-smooth vs smooth-then-fold on roll5
    print("== F  roll5: fold-then-smooth vs smooth-then-fold vs instability (hl 20)")
    K = roll5 - np.nanmean(roll5, axis=1, keepdims=True)
    eK = ema(K, 20)
    for nm, sg in (("fold-then-smooth", sig_r), ("smooth-then-fold", -np.abs(eK)), ("instability only", -(ema(np.abs(K), 20) - np.abs(eK))),
                   ("no fold", -ema(roll5, 20))):
        out = [f"  {nm:<18}"]
        for sn, s in SP.items():
            b = bk.book_row(sg, tgt, s)
            out.append(f"{sn}: rIC {np.nanmean(dg.rank_ic_series(sg[s], tgt[s])):+.4f} LS {b['ls_sharpe']:+.2f} Lg {b['long_gross_ann']*100:+5.1f}% "
                       f"Ln {b['long_ann']*100:+5.1f}% Lshp {b['long_sharpe']:+.2f} short {b['short_gross_ann']*100:+5.1f}% TO {b['ls_turnover']*100:4.1f}%")
        print(" | ".join(out), flush=True)
