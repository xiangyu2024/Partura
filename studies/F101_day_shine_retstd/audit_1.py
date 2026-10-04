"""F101 audit (reviewer: mechanism & over-fitting).  Train / valid only -- the holdout is never touched.

Four claims of the study, each paired with the alternative it did not rule out:

  A  "the Volume-surge mask's unique content is the burst ratio (a short-leg signal)".
     Alternative: ANY statistic that up-weights the high-activity minutes does the same; Volume is not
     needed.  Test: the same trigger machinery with a volume-free mask (|Ret| > day mean + 1 sd of |Ret|)
     and a mask-free tail statistic (Q90 of the rolling 5-minute std).  If their folds reproduce the
     original's short leg / LS and their "burst ratios" absorb J/roll5, the content is not the Volume mask.
  B  "EMA|K| = |EMA K| + instability, each term monotone, consistent in both periods" -- measured on roll5
     only (look3 H).  Test: the same double sort on J itself at the traded half-life (10), and what the
     long decile earns relative to the plateau it is drawn from.
  C  "H5 dead: the short leg is not untradeable names (label-NaN share 3.0%, J==0 share 2.2%)" -- judged by
     head-count, not by return.  Test: return contribution of low-side / J==0 / label-NaN names to the short
     leg, for the original and for the ivol / roll5 folds (is the original's extra short leg on the high side?).
  D  "unrelated to F001's families (rank corr within +-0.05)".  A V fold is rank-uncorrelated with any
     monotone variable by construction (the study's own argument about R2 0.154).  Test: R2 on the folded
     known_ivol_max9, and overlap of the short decile with the monotone known_ivol_max9 book.
"""
import time
import warnings

import numpy as np

from partura.study_tools import Study, bk, dg

from alphacube.metrics import long_short_weights  # noqa: E402  (on path after partura import)

warnings.simplefilter("ignore", RuntimeWarning)
FID = "F101_day_shine_retstd"
V = "in_slice(Volume, 2, 237)"
DV = f"sub({V}, in_delay({V}, 1))"
MASK = f"is_gt({DV}, add(in_mean_full({DV}), in_stddev_full({DV})))"
R = "in_slice(Ret, 2, 237)"
AR = f"abs_({R})"
MASK_RET = f"is_gt({AR}, add(in_mean_full({AR}), in_stddev_full({AR})))"
J_EXPR = f"day_mean(in_sustain_stddev({MASK}, {R}, 5))"
JRET_EXPR = f"day_mean(in_sustain_stddev({MASK_RET}, {R}, 5))"
ROLL5_EXPR = f"day_mean(in_stddev_rolling({R}, 5))"
Q90_EXPR = f"day_quantile(in_stddev_rolling({R}, 5), 0.9)"
NTRIG_RET_EXPR = f"day_mean({MASK_RET})"
T0 = time.time()


def say(msg):
    print(f"[{time.time() - T0:5.0f}s] {msg}", flush=True)


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


def fmt(b):
    return (f"LS {b['ls_sharpe']:+.2f} Lg {b['long_gross_ann']*100:+5.1f}% Ln {b['long_ann']*100:+5.1f}% "
            f"Lshp {b['long_sharpe']:+.2f} short {b['short_gross_ann']*100:+5.1f}% TO {b['ls_turnover']*100:4.1f}%")


def row(name, sm, tgt, SP):
    """sm: sign-aligned, already smoothed."""
    out = [f"  {name:<38}"]
    for k, s in SP.items():
        b = bk.book_row(sm, tgt, s)
        out.append(f"{k}: rIC {np.nanmean(dg.rank_ic_series(sm[s], tgt[s])):+.4f} {fmt(b)}")
    print(" | ".join(out), flush=True)


def rep(name, y, cs, tgt, SP):
    """R2 of y (traded signal) on controls in rank space, per split; residual rank IC / gross LS / legs."""
    out = [f"  {name:<52}"]
    for k, s in SP.items():
        yz = dg._zrank(y[s])
        cz = {c: dg._zrank(v[s]) for c, v in cs.items()}
        resid, info = dg.neutralise(yz, cz, panel_ready=True, controls_ready=True)
        b = bk.book_row(resid, tgt[s], slice(0, resid.shape[0]))
        out.append(f"{k}: R2 {info['mean_r2']:.3f} resid rIC {np.nanmean(dg.rank_ic_series(resid, tgt[s])):+.4f} "
                   f"LSgross {b['ls_gross_sharpe']:+.2f} Lg {b['long_gross_ann']*100:+5.1f}% short {b['short_gross_ann']*100:+5.1f}%")
    print(" | ".join(out), flush=True)


def double_sort(name, x, hl, tgt, SP, tr):
    K = x - np.nanmean(x, axis=1, keepdims=True)
    eK = ema(K, hl)
    aeK = np.abs(eK)
    inst = ema(np.abs(K), hl) - aeK
    pa, pi = pct(aeK), pct(inst)
    print(f"  {name}: rank corr(|EMA K|, instability) train {dg.pair_rank_corr(aeK[tr], inst[tr]):+.3f}", flush=True)
    for sn, s in SP.items():
        ex = excess(tgt[s], aeK[s])
        print(f"   {sn}: annualised excess % (cell share %)   rows near->far, cols stable->unstable")
        for i in range(3):
            cells = []
            for j in range(3):
                m = (pa[s] >= i / 3) & (pa[s] < (i + 1) / 3 + 1e-9) & (pi[s] >= j / 3) & (pi[s] < (j + 1) / 3 + 1e-9)
                cells.append(f"{np.nanmean(np.where(m, ex, np.nan))*25200:+6.1f} ({m.sum() / np.isfinite(ex).sum() * 100:4.1f})")
            print("      " + "   ".join(cells), flush=True)
        # inside the near tercile and inside the middle tercile: instability quintiles (conditional sort)
        for lab, sel in (("near tercile", pa[s] < 1 / 3), ("mid tercile ", (pa[s] >= 1 / 3) & (pa[s] < 2 / 3))):
            pin = pct(np.where(sel, inst[s], np.nan))
            q5 = [np.nanmean(np.where(sel & (pin >= a / 5) & (pin < (a + 1) / 5 + 1e-9), ex, np.nan)) * 25200 for a in range(5)]
            print(f"      {lab}: instability quintiles (stable->unstable) " + " ".join(f"{v:+5.1f}" for v in q5), flush=True)


def long_vs_plateau(name, x, hl, tgt, SP):
    sig = -ema(fold(x), hl)
    pl = pct(ema(x, hl))
    out = [f"  {name:<22}"]
    for sn, s in SP.items():
        ex = excess(tgt[s], sig[s])
        top = decile(sig[s], True)
        plat = (pl[s] >= 0.10) & (pl[s] < 0.80) & np.isfinite(sig[s])
        f = lambda m: np.nanmean(np.where(m, ex, np.nan)) * 25200
        out.append(f"{sn}: long decile {f(top):+5.1f}  plateau(level pct .10-.80) {f(plat):+5.1f}  plateau ex-long {f(plat & ~top):+5.1f}  "
                   f"long-decile level pct mean {np.nanmean(pl[s][top]):.2f}")
    print(" | ".join(out), flush=True)


def short_decomp(name, x, hl, tgt, SP):
    """Who earns the short leg of -EMA_hl(fold(x)): split the short decile's excess by group."""
    K = x - np.nanmean(x, axis=1, keepdims=True)
    eK = ema(K, hl)
    sig = -ema(np.abs(K), hl)
    zero5 = np.zeros_like(x, dtype=bool)                     # x == 0 on any of the last 5 days (incl. today)
    z = (x == 0)
    for k in range(5):
        sh_ = np.zeros_like(z)
        sh_[k:] = z[:z.shape[0] - k] if k else z
        zero5 |= sh_
    for sn, s in SP.items():
        sg, t = sig[s], tgt[s]
        w = long_short_weights(sg, 0.10)
        shorts = w < 0
        kk = shorts.sum(1)
        ok = np.isfinite(sg) & np.isfinite(t)
        r = np.where(ok, t, 0.0)
        n = ok.sum(1)
        ew = np.where(n > 0, r.sum(1) / np.maximum(n, 1), np.nan)
        days = (kk > 0) & np.isfinite(ew)
        contrib = np.where(shorts, ew[:, None] - r, 0.0) / np.maximum(kk, 1)[:, None]
        total = contrib.sum(1)[days].mean() * 252
        print(f"  {name} [{sn}] short leg total {total*100:+5.1f}%  (names/day {kk[days].mean():.0f})")
        groups = {
            "high side (EMA K >= 0)": shorts & (eK[s] >= 0),
            "low side  (EMA K < 0)": shorts & (eK[s] < 0),
            "x == 0 today": shorts & (x[s] == 0),
            "x == 0 within 5d": shorts & zero5[s],
            "label NaN (earns 0)": shorts & ~np.isfinite(t),
        }
        for g, m in groups.items():
            share = m.sum() / max(shorts.sum(), 1)
            c = np.where(m, contrib, 0.0).sum(1)[days].mean() * 252
            exg = np.nanmean(np.where(m & np.isfinite(t), t - ew[:, None], np.nan)) * 252
            print(f"      {g:<24} head-count share {share*100:5.1f}%   contribution {c*100:+5.1f} pts ({c/total*100:4.0f}% of leg)   "
                  f"own annualised excess {exg*100:+7.1f}%", flush=True)


def main():
    with Study(FID) as st:
        P = st.panels({"J": J_EXPR, "roll5": ROLL5_EXPR, "Jret": JRET_EXPR, "q90": Q90_EXPR, "ntr": NTRIG_RET_EXPR})
        J, roll5, Jret, q90, ntr = (np.asarray(P[k], dtype=np.float64) for k in ("J", "roll5", "Jret", "q90", "ntr"))
        ivol = np.asarray(st.control("ctl_ivol"), dtype=np.float64)
        kiv = np.asarray(st.control("known_ivol_max9"), dtype=np.float64)
        tgt = np.asarray(st.target(), dtype=np.float64)
        tr, va = st.slice("train"), st.slice("valid")
        SP = {"train": tr, "valid": va}
        say("panels ready")
        sig_o = -ema(fold(J), 10)

        # ------------------------------------------------------------ A
        print("== A  is the VOLUME mask needed?  volume-free mask (|Ret| > mean + 1sd) and mask-free tail statistic (Q90 of roll-5 std)")
        m = np.nanmean(Jret[tr], axis=1, keepdims=True)
        print(f"  Jret: finite among J-finite {np.isfinite(Jret[tr])[np.isfinite(J[tr])].mean():.4f}; triggers/day median "
              f"{np.nanmedian(ntr[tr]) * 236:.0f}; percentile of its cs mean {np.nanmean(np.where(np.isfinite(Jret[tr]), Jret[tr] < m, np.nan)):.3f}")
        m = np.nanmean(q90[tr], axis=1, keepdims=True)
        print(f"  q90 : percentile of its cs mean {np.nanmean(np.where(np.isfinite(q90[tr]), q90[tr] < m, np.nan)):.3f}")
        lv = {"J": J, "Jret": Jret, "q90": q90, "ivol": ivol, "roll5": roll5}
        print("  level rank corr (train): " + "  ".join(f"{a}~{b} {dg.pair_rank_corr(lv[a][tr], lv[b][tr]):+.3f}" for a, b in
              (("J", "Jret"), ("J", "q90"), ("J", "ivol"), ("J", "roll5"), ("Jret", "ivol"), ("Jret", "q90"), ("q90", "roll5"))))
        print("  fold rank corr with the original panel (train): " + "  ".join(
            f"fold({k}) {dg.pair_rank_corr(fold(v)[tr], fold(J)[tr]):+.3f}" for k, v in lv.items() if k != "J"))
        print("  traded-signal (hl 10) rank corr with the original (train): " + "  ".join(
            f"{k} {dg.pair_rank_corr((-ema(fold(v), 10))[tr], sig_o[tr]):+.3f}" for k, v in lv.items() if k != "J"), flush=True)
        print("  -- folds, sign -, hl 10 fixed")
        row("fold(J)  [original]", sig_o, tgt, SP)
        row("fold(J), J==0 cells dropped", -ema(fold(np.where(J == 0, np.nan, J)), 10), tgt, SP)
        row("fold(Jret)  volume-free mask", -ema(fold(Jret), 10), tgt, SP)
        row("fold(q90)   mask-free tail", -ema(fold(q90), 10), tgt, SP)
        row("fold(ivol)", -ema(fold(ivol), 10), tgt, SP)
        row("fold(roll5)", -ema(fold(roll5), 10), tgt, SP)
        print("  -- same, hl 20 fixed")
        for k, v in lv.items():
            row(f"fold({k}) hl20", -ema(fold(v), 20), tgt, SP)
        print("  -- no fold (monotone), sign -, hl 10: is the top decile of the tail-weighted statistic worse?")
        for k, v in lv.items():
            row(f"-EMA10({k})", -ema(v, 10), tgt, SP)
        say("A folds done")
        print("  -- 'burst ratios' as monotone factors, sign -, hl 10 (study: J/roll5 rIC +0.0285/+0.0415)")
        den = np.where(roll5 > 0, roll5, np.nan)
        ratios = {"J/roll5 (study's burst ratio)": J / den, "Jret/roll5 (volume-free)": Jret / den, "q90/roll5 (mask-free)": q90 / den,
                  "ivol/roll5 (mask-free)": ivol / den, "J/Jret (volume vs return mask)": J / np.where(Jret > 0, Jret, np.nan),
                  "J/ivol": J / np.where(ivol > 0, ivol, np.nan)}
        for k, v in ratios.items():
            row(k, -ema(v, 10), tgt, SP)
        names = list(ratios)
        print("  ratio rank corr (train): " + "  ".join(f"[{names[0][:7]}]~[{k[:10]}] {dg.pair_rank_corr(ratios[names[0]][tr], ratios[k][tr]):+.3f}"
                                                         for k in names[1:]))
        print("  -- does the volume burst ratio survive the volume-free ones?  (traded = -EMA10(ratio); rank-space residual)")
        bv = -ema(ratios[names[0]], 10)
        rep("J/roll5 | Jret/roll5", bv, {"a": -ema(ratios[names[1]], 10)}, tgt, SP)
        rep("J/roll5 | q90/roll5", bv, {"a": -ema(ratios[names[2]], 10)}, tgt, SP)
        rep("J/roll5 | ivol/roll5", bv, {"a": -ema(ratios[names[3]], 10)}, tgt, SP)
        rep("J/roll5 | Jret/roll5, q90/roll5, ivol/roll5", bv, {"a": -ema(ratios[names[1]], 10), "b": -ema(ratios[names[2]], 10),
                                                               "c": -ema(ratios[names[3]], 10)}, tgt, SP)
        rep("Jret/roll5 | J/roll5   (reverse)", -ema(ratios[names[1]], 10), {"a": bv}, tgt, SP)
        print("  -- the original traded signal on volume-free folds (study: EMA10 fold(ivol) R2 0.749)")
        rep("orig | EMA10 fold(ivol)", sig_o, {"a": ema(fold(ivol), 10)}, tgt, SP)
        rep("orig | EMA10 fold(Jret)", sig_o, {"a": ema(fold(Jret), 10)}, tgt, SP)
        rep("orig | EMA10 fold(q90)", sig_o, {"a": ema(fold(q90), 10)}, tgt, SP)
        rep("orig | EMA10 folds of ivol, Jret, q90, roll5", sig_o, {"a": ema(fold(ivol), 10), "b": ema(fold(Jret), 10),
                                                                   "c": ema(fold(q90), 10), "d": ema(fold(roll5), 10)}, tgt, SP)
        rep("fold(Jret) traded | EMA10 fold(J)  (reverse)", -ema(fold(Jret), 10), {"a": ema(fold(J), 10)}, tgt, SP)
        say("A done")

        # ------------------------------------------------------------ B
        print("== B  the double sort of look3 H, on J itself (traded hl 10); roll5 hl 20 repeated as a code check")
        double_sort("roll5 hl20 (must match look3 H)", roll5, 20, tgt, SP, tr)
        double_sort("J hl10 (the recommended factor)", J, 10, tgt, SP, tr)
        double_sort("J hl20", J, 20, tgt, SP, tr)
        print("  -- what does the long decile earn over the plateau it is drawn from? (gross annualised excess %)")
        long_vs_plateau("J hl10 (original)", J, 10, tgt, SP)
        long_vs_plateau("J hl20", J, 20, tgt, SP)
        long_vs_plateau("ivol hl10", ivol, 10, tgt, SP)
        long_vs_plateau("roll5 hl20", roll5, 20, tgt, SP)
        say("B done")

        # ------------------------------------------------------------ C
        print("== C  who earns the short leg: return contribution by group (not head-count)")
        short_decomp("fold(J) hl10 [original]", J, 10, tgt, SP)
        short_decomp("fold(ivol) hl10", ivol, 10, tgt, SP)
        short_decomp("fold(roll5) hl10", roll5, 10, tgt, SP)
        say("C done")

        # ------------------------------------------------------------ D
        print("== D  F001's 'intraday vol + extreme memory' family: known_ivol_max9 = cross_max(day_var(Ret), 9)")
        print(f"  rank corr (train): raw fold(J) ~ kiv {dg.pair_rank_corr(fold(J)[tr], kiv[tr]):+.3f}   traded orig ~ -kiv {dg.pair_rank_corr(sig_o[tr], -kiv[tr]):+.3f}   "
              f"traded orig ~ -EMA10(kiv) {dg.pair_rank_corr(sig_o[tr], -ema(kiv, 10)[tr]):+.3f}   "
              f"traded orig ~ -EMA10 fold(kiv) {dg.pair_rank_corr(sig_o[tr], -ema(fold(kiv), 10)[tr]):+.3f}   "
              f"traded orig ~ -fold(kiv) {dg.pair_rank_corr(sig_o[tr], -fold(kiv)[tr]):+.3f}", flush=True)
        rep("orig | -kiv (monotone, as published)", sig_o, {"a": kiv}, tgt, SP)
        rep("orig | EMA10 fold(kiv)", sig_o, {"a": ema(fold(kiv), 10)}, tgt, SP)
        rep("orig | fold(kiv) unsmoothed", sig_o, {"a": fold(kiv)}, tgt, SP)
        row("fold(kiv) hl10", -ema(fold(kiv), 10), tgt, SP)
        row("fold(kiv) hl0", -fold(kiv), tgt, SP)
        row("-EMA10(kiv) monotone", -ema(kiv, 10), tgt, SP)
        for sn, s in SP.items():
            a = decile(sig_o[s], False)
            for nm, other in (("-EMA10(kiv)", -ema(kiv, 10)), ("-EMA10(J)", -ema(J, 10)), ("-EMA10(ivol)", -ema(ivol, 10))):
                b = decile(other[s], False)
                ex = excess(tgt[s], sig_o[s])
                f = lambda mm: np.nanmean(np.where(mm, ex, np.nan)) * 25200
                print(f"  {sn}: original short decile vs short decile of {nm:<13}: overlap {(a & b).sum() / a.sum():.2f}  "
                      f"both {f(a & b):+6.1f}  only-original {f(a & ~b):+6.1f}  only-{nm} {f(b & ~a):+6.1f}", flush=True)
        say("all done")


if __name__ == "__main__":
    main()
