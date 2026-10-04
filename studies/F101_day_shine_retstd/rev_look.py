"""F101 revision (tag rev2): bespoke numbers the review asked for.  Train / valid only -- the holdout is never touched.

  A  (review 1 / 6)  Mean fold vs rank fold.  The study wrote "the rank fold shorts the lowest-vol end, which rallied in
     2024" without ever splitting a rank-fold short leg by side.  2024 is holdout and cannot be re-read; what CAN be
     measured is whether the low-side half of a rank-fold short leg is a sign-changing liability across 2018..2023.
     Per year: short-leg total, low-side head-count share, contribution of each side, each side's own excess.
  B  (review 4)  H5 by RETURN, not head-count.  The raw-J 20-quantile profile with the J == 0 cells removed (is the
     low-side cliff only limit-locked days?), who the J == 0 names are (limit-up / limit-down day, recently listed),
     and what the short decile earns from each kind.
  C  (review 3)  The original's long decile against the plateau it is drawn from, per year, and whether the traded
     signal ranks names INSIDE the plateau (quintiles).  Repeated for ivol and roll5 folds.
  D  (review 5)  F001's three families: rank corr / R2 of the traded signal on each, monotone and folded-and-smoothed.
  E  (review 2)  Tail-weighted vs plain statistics on COMMON cells (zero-return days removed from every statistic).

Self-checks: A must reproduce the table's short leg (+53.7% train for the original) and the audit's 5.6% low-side
share; C on train / valid must reproduce audit_1.py B (long decile +16.7 / +5.7 vs plateau +7.0 / +6.6).
"""
import time
import warnings

import numpy as np

from partura.study_tools import Study, bk, dg

from alphacube.metrics import long_short_weights  # noqa: E402  (on path after the partura import)

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
    out = [f"  {name:<40}"]
    for k, s in SP.items():
        b = bk.book_row(sm, tgt, s)
        out.append(f"{k}: rIC {np.nanmean(dg.rank_ic_series(sm[s], tgt[s])):+.4f} {fmt(b)}")
    print(" | ".join(out), flush=True)


def rep(name, y, cs, tgt, SP):
    """R2 of y (a traded signal) on controls in rank space, per split; residual rank IC / gross LS / legs."""
    out = [f"  {name:<46}"]
    for k, s in SP.items():
        yz = dg._zrank(y[s])
        cz = {c: dg._zrank(v[s]) for c, v in cs.items()}
        resid, info = dg.neutralise(yz, cz, panel_ready=True, controls_ready=True)
        b = bk.book_row(resid, tgt[s], slice(0, resid.shape[0]))
        out.append(f"{k}: R2 {info['mean_r2']:.3f} resid rIC {np.nanmean(dg.rank_ic_series(resid, tgt[s])):+.4f} "
                   f"LSgross {b['ls_gross_sharpe']:+.2f} Lg {b['long_gross_ann']*100:+5.1f}% short {b['short_gross_ann']*100:+5.1f}%")
    print(" | ".join(out), flush=True)


def prof(name, sm, tgt, s, n=20):
    q = bk.quantile_profile(sm, tgt, s, n=n)
    print(f"  {name}: " + " ".join(f"{r_['excess_ann']*100:+.0f}" for r_ in q), flush=True)


def short_parts(sig, tgt, s):
    """Daily contribution of every short name to the short leg (EW universe minus the name, / #shorts)."""
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

    def part(m):
        m = m & shorts
        c = np.where(m, contrib, 0.0).sum(1)[days].mean() * 252
        own = np.nanmean(np.where(m & np.isfinite(t), t - ew[:, None], np.nan)) * 252
        return m.sum() / max(shorts.sum(), 1), c, own

    return shorts, total, part


def short_sides(name, K, x, hl, tgt, YS):
    """K: signed distance from the fold centre (level fold: x - cs mean; rank fold: pct(x) - 0.5)."""
    eK = ema(K, hl)
    sig = -ema(np.abs(K), hl)
    lvl = pct(ema(x, hl))
    print(f"  {name}", flush=True)
    for lab, s in YS.items():
        shorts, total, part = short_parts(sig, tgt, s)
        b = bk.book_row(sig, tgt, s)
        lo, hi = part(eK[s] < 0), part(eK[s] >= 0)
        lo_lvl = np.nanmean(np.where(shorts & (eK[s] < 0), lvl[s], np.nan))
        print(f"    {lab:<6} LS {b['ls_sharpe']:+5.2f} Ln {b['long_ann']*100:+5.1f}%  short leg {total*100:+6.1f}% (book {b['short_gross_ann']*100:+6.1f}%)  "
              f"low-side head share {lo[0]*100:5.1f}% (level pct {lo_lvl:.2f})  contribution low {lo[1]*100:+6.1f} / high {hi[1]*100:+6.1f} pts  "
              f"own excess low {lo[2]*100:+7.1f}% / high {hi[2]*100:+7.1f}%", flush=True)


def long_plateau(name, x, hl, tgt, YS):
    sig = -ema(fold(x), hl)
    pl = pct(ema(x, hl))
    print(f"  {name}: gross annualised excess %, pooled over cells", flush=True)
    for lab, s in YS.items():
        ex = excess(tgt[s], sig[s])
        top = decile(sig[s], True)
        fin = np.isfinite(sig[s])
        plat = (pl[s] >= 0.10) & (pl[s] < 0.80) & fin
        nothi = (pl[s] < 0.80) & fin
        f = lambda m: np.nanmean(np.where(m, ex, np.nan)) * 25200          # noqa: E731
        pin = pct(np.where(plat, sig[s], np.nan))
        q5 = [f(plat & (pin >= a / 5) & (pin < (a + 1) / 5 + 1e-9)) for a in range(5)]
        print(f"    {lab:<6} long decile {f(top):+5.1f}  plateau(.10-.80) {f(plat):+5.1f}  below-.80 {f(nothi):+5.1f}  "
              f"decile minus plateau {f(top) - f(plat):+5.1f}  share of decile inside plateau {(top & plat).sum() / max(top.sum(), 1):.2f}  "
              f"| inside the plateau, quintiles of the traded signal (worst->best): " + " ".join(f"{v:+5.1f}" for v in q5), flush=True)


def main():
    with Study(FID) as st:
        P = st.panels({"J": J_EXPR, "roll5": ROLL5_EXPR, "Jret": JRET_EXPR, "q90": Q90_EXPR, "ivol_s": f"day_std({R})"})
        J, roll5, Jret, q90, ivol_s = (np.asarray(P[k], dtype=np.float64) for k in ("J", "roll5", "Jret", "q90", "ivol_s"))
        C = {k: np.asarray(st.control(k), dtype=np.float64) for k in
             ("ctl_ivol", "ctl_rev1", "ctl_price", "ctl_amt", "known_ivol_max9", "known_stdamt_max9", "known_amt_max9")}
        ivol = C["ctl_ivol"]
        tgt = np.asarray(st.target(), dtype=np.float64)
        tr, va = st.slice("train"), st.slice("valid")
        SP = {"train": tr, "valid": va}
        years = np.array([int(str(d)[:4]) for d in st.dates])
        YS = dict(SP)
        for y in sorted(set(years[tr.start:va.stop].tolist())):
            idx = np.where(years[:va.stop] == y)[0]
            idx = idx[idx >= tr.start]
            YS[str(y)] = slice(int(idx[0]), int(idx[-1]) + 1)
        say(f"panels ready; rows {tgt.shape}; year slices {[(k, v.stop - v.start) for k, v in YS.items()]}")
        sig_o = -ema(fold(J), 10)

        # ------------------------------------------------------------ A
        print("== A  who is in the SHORT decile: low side vs high side of the fold centre, per year (train + valid years only)")
        short_sides("J  mean fold hl10  [= f_orig; check: train short +53.7%, low-side share 5.6%]", J - np.nanmean(J, axis=1, keepdims=True), J, 10, tgt, YS)
        short_sides("J  rank fold hl20  [= f_j_rank; table LS 3.64 / 3.46]", pct(J) - 0.5, J, 20, tgt, YS)
        short_sides("roll5 mean fold hl20  [= f_roll5 at its train half-life; table LS 3.19 / 3.33]", roll5 - np.nanmean(roll5, axis=1, keepdims=True), roll5, 20, tgt, YS)
        short_sides("roll5 rank fold hl20  [= f_roll5_rank; table LS 3.10 / 3.43]", pct(roll5) - 0.5, roll5, 20, tgt, YS)
        print("  -- the two ends on their own, per year: annualised excess % of the lowest / highest 5% of EMA20(level)")
        for nm, x in (("J", J), ("roll5", roll5)):
            lv = pct(ema(x, 20))
            out = []
            for lab, s in YS.items():
                ex = excess(tgt[s], lv[s])
                out.append(f"{lab} {np.nanmean(np.where(lv[s] < 0.05, ex, np.nan))*25200:+6.1f}/{np.nanmean(np.where(lv[s] >= 0.95, ex, np.nan))*25200:+6.1f}")
            print(f"    {nm:<6} lowest 5% / highest 5%:  " + "   ".join(out), flush=True)
        say("A done")

        # ------------------------------------------------------------ B
        print("== B  the J == 0 cells (no price move in any trigger window: limit-locked days) -- by return, not head-count")
        z = (J == 0)
        Jnz = np.where(z, np.nan, J)
        print("  annualised excess (%) by 20 quantiles of the same-day J, lowest -> highest")
        for sn, s in SP.items():
            prof(f"J raw, all cells       {sn}", J, tgt, s)
            prof(f"J raw, J==0 removed    {sn}", Jnz, tgt, s)
        for sn, s in SP.items():
            pj = pct(J)[s]
            ex = excess(tgt[s], J[s])
            b5 = pj < 0.05
            print(f"  {sn}: lowest-5% bucket of raw J: share J==0 {np.nansum(b5 & z[s]) / max(b5.sum(), 1):.3f}; pooled excess: whole bucket "
                  f"{np.nanmean(np.where(b5, ex, np.nan))*25200:+.1f}  its J==0 cells {np.nanmean(np.where(b5 & z[s], ex, np.nan))*25200:+.1f}  "
                  f"its J>0 cells {np.nanmean(np.where(b5 & ~z[s], ex, np.nan))*25200:+.1f}", flush=True)
        rev1, price = C["ctl_rev1"], C["ctl_price"]
        T = J.shape[0]
        finp = np.isfinite(price)
        first = np.where(finp.any(0), finp.argmax(0), 10 ** 9)
        age = np.arange(T)[:, None] - first[None, :]
        young = (first[None, :] > 20) & (age >= 0) & (age < 60)
        up, dn = z & (rev1 > 1.03), z & (rev1 < 0.97)
        other = z & ~up & ~dn
        print("  who are the J == 0 stock-days?  (day return from ctl_rev1; 'young' = first close in the panel < 60 rows ago)")
        for sn, s in SP.items():
            ex = excess(tgt[s], J[s])
            finJ = np.isfinite(J[s])
            for g, m in (("all J==0", z), ("  day return > +3% (locked limit-up)", up), ("  day return < -3% (locked limit-down)", dn),
                         ("  other / no previous close", other), ("  of which listed < 60 rows ago", z & young)):
                mm = m[s]
                print(f"    {sn} {g:<38} share of J-finite cells {mm.sum() / finJ.sum()*100:6.3f}%  label-NaN share {np.mean(~np.isfinite(tgt[s][mm])) if mm.sum() else float('nan'):.3f}  "
                      f"next-day excess (labelled) {np.nanmean(np.where(mm, ex, np.nan))*100:+.2f}%/day = {np.nanmean(np.where(mm, ex, np.nan))*25200:+.0f}%/yr", flush=True)

        def within(m, d=5):
            out = np.zeros_like(m)
            for k in range(d):
                out[k:] |= m[:m.shape[0] - k] if k else m
            return out

        z5, up5, dn5 = within(z), within(up), within(dn)
        print("  the original's short decile (hl 10): contribution by kind of J == 0 history (mutually exclusive, in this priority)")
        for sn, s in SP.items():
            shorts, total, part = short_parts(sig_o, tgt, s)
            groups = [("J==0 within 5d, listed < 60 rows ago", z5[s] & young[s]),
                      ("J==0 within 5d, a locked limit-down day", z5[s] & ~young[s] & dn5[s]),
                      ("J==0 within 5d, a locked limit-up day", z5[s] & ~young[s] & ~dn5[s] & up5[s]),
                      ("J==0 within 5d, other", z5[s] & ~young[s] & ~dn5[s] & ~up5[s]),
                      ("no J==0 within 5d", ~z5[s]),
                      ("(memo) J==0 within 20d", within(z, 20)[s]),
                      ("(memo) listed < 60 rows ago, any J", young[s])]
            print(f"    {sn}: short leg total {total*100:+5.1f}%")
            for g, m in groups:
                sh, c, own = part(m)
                nanlab = np.mean(~np.isfinite(tgt[s][m & shorts])) if (m & shorts).sum() else float("nan")
                print(f"      {g:<42} head share {sh*100:5.1f}%  contribution {c*100:+5.1f} pts ({c/total*100:4.0f}% of leg)  own excess {own*100:+7.1f}%  label-NaN {nanlab:.3f}", flush=True)
        print("  -- the same three folds with every zero-statistic cell removed (fixed hl 10): how much of each book is the locked days")
        for nm, x in (("J", J), ("ivol", ivol), ("roll5", roll5)):
            row(f"fold({nm})", -ema(fold(x), 10), tgt, SP)
            row(f"fold({nm}), {nm}==0 cells removed", -ema(fold(np.where(x == 0, np.nan, x)), 10), tgt, SP)
        say("B done")

        # ------------------------------------------------------------ C
        print("== C  the long decile against the plateau it is drawn from (level pct of EMA(x) in .10-.80), per year")
        long_plateau("J hl10 (original)   [check: train +16.7 vs +7.0, valid +5.7 vs +6.6]", J, 10, tgt, YS)
        long_plateau("J hl20", J, 20, tgt, YS)
        long_plateau("ivol hl10 (= f_ivol)", ivol, 10, tgt, YS)
        long_plateau("roll5 hl20 (= f_roll5 at its train half-life)", roll5, 20, tgt, YS)
        say("C done")

        # ------------------------------------------------------------ D
        print("== D  F001's families against the traded signal (hl 10)")
        for nm in ("known_ivol_max9", "known_stdamt_max9", "known_amt_max9", "ctl_amt"):
            k = C[nm]
            lk = np.where(k > 0, np.log(k), np.nan) if nm != "ctl_amt" else k
            print(f"  {nm}: rank corr (train) traded ~ k {dg.pair_rank_corr(sig_o[tr], k[tr]):+.3f}   raw fold panel ~ k {dg.pair_rank_corr(fold(J)[tr], k[tr]):+.3f}   "
                  f"traded ~ -EMA10 fold(k) {dg.pair_rank_corr(sig_o[tr], -ema(fold(k), 10)[tr]):+.3f}   traded ~ -EMA10 fold(log k) {dg.pair_rank_corr(sig_o[tr], -ema(fold(lk), 10)[tr]):+.3f}", flush=True)
            rep(f"orig | EMA10 fold({nm})", sig_o, {"a": ema(fold(k), 10)}, tgt, SP)
            rep(f"orig | EMA10 fold(log {nm})", sig_o, {"a": ema(fold(lk), 10)}, tgt, SP)
            row(f"fold({nm}) hl10", -ema(fold(k), 10), tgt, SP)
            row(f"fold(log {nm}) hl10", -ema(fold(lk), 10), tgt, SP)
        for sn, s in SP.items():
            a = decile(sig_o[s], False)
            ex = excess(tgt[s], sig_o[s])
            f = lambda mm: np.nanmean(np.where(mm, ex, np.nan)) * 25200      # noqa: E731
            for nm in ("known_ivol_max9", "known_stdamt_max9", "known_amt_max9"):
                b = decile((-ema(C[nm], 10))[s], False)
                print(f"  {sn}: original short decile vs short decile of -EMA10({nm}): overlap {(a & b).sum() / a.sum():.2f}  both {f(a & b):+6.1f}  "
                      f"only-original {f(a & ~b):+6.1f}  only-family {f(b & ~a):+6.1f}", flush=True)
            a = decile(sig_o[s], True)
            for nm in ("known_ivol_max9",):
                b = decile((-ema(fold(C[nm]), 10))[s], True)
                print(f"  {sn}: original LONG decile vs long decile of -EMA10 fold({nm}): overlap {(a & b).sum() / a.sum():.2f}  both {f(a & b):+6.1f}  "
                      f"only-original {f(a & ~b):+6.1f}  only-family {f(b & ~a):+6.1f}", flush=True)
        say("D done")

        # ------------------------------------------------------------ E
        print("== E  tail-weighted vs plain statistics on COMMON cells (finite & > 0 for every statistic), fixed half-life")
        common = np.isfinite(J) & np.isfinite(Jret) & np.isfinite(q90) & np.isfinite(ivol) & np.isfinite(roll5) & (J > 0) & (ivol > 0) & (roll5 > 0)
        allfin = np.isfinite(J)
        print(f"  cells kept: {common[tr].sum() / allfin[tr].sum():.4f} of J-finite (train), {common[va].sum() / allfin[va].sum():.4f} (valid)")
        stats_ = {"J (volume-surge mask)": J, "Jret (|Ret|-surge mask, no Volume)": Jret, "q90 (mask-free tail)": q90, "ivol (full-day std)": ivol,
                  "ivol_s (std of the sliced minutes)": ivol_s, "roll5 (background)": roll5}
        for hl in (10, 20):
            for nm, x in stats_.items():
                row(f"fold({nm}) hl{hl}", -ema(fold(np.where(common, x, np.nan)), hl), tgt, SP)
        print("  -- per year, hl 10, common cells: LS net Sharpe | long net % | short gross %")
        for nm, x in stats_.items():
            sm = -ema(fold(np.where(common, x, np.nan)), 10)
            out = []
            for lab, s in YS.items():
                if lab in SP:
                    continue
                b = bk.book_row(sm, tgt, s)
                out.append(f"{lab}: {b['ls_sharpe']:+.2f}|{b['long_ann']*100:+5.1f}|{b['short_gross_ann']*100:+5.1f}")
            print(f"    {nm:<36} " + "  ".join(out), flush=True)
        say("E done")

        # ------------------------------------------------------------ F
        print("== F  the 'burst ratio' without a mask: J/roll5 vs Jret/roll5 vs ivol_s/roll5 (traded = -EMA_hl(ratio); rank-space residuals)")
        den = np.where(roll5 > 0, roll5, np.nan)
        rt = {"J/roll5": J / den, "Jret/roll5": Jret / den, "ivol_s/roll5": ivol_s / den, "ivol/roll5": ivol / den}
        nm = list(rt)
        print("  ratio rank corr (train): " + "  ".join(f"{a}~{b} {dg.pair_rank_corr(rt[a][tr], rt[b][tr]):+.3f}" for a, b in
              ((nm[0], nm[1]), (nm[0], nm[2]), (nm[1], nm[2]), (nm[2], nm[3]))), flush=True)
        for hl in (5, 10):
            for k, v in rt.items():
                row(f"-EMA{hl}({k})", -ema(v, hl), tgt, SP)
        t = {k: -ema(v, 10) for k, v in rt.items()}
        rep("J/roll5 | ivol_s/roll5", t[nm[0]], {"a": t[nm[2]]}, tgt, SP)
        rep("J/roll5 | Jret/roll5", t[nm[0]], {"a": t[nm[1]]}, tgt, SP)
        rep("J/roll5 | Jret/roll5 + ivol_s/roll5", t[nm[0]], {"a": t[nm[1]], "b": t[nm[2]]}, tgt, SP)
        rep("ivol_s/roll5 | J/roll5   (reverse)", t[nm[2]], {"a": t[nm[0]]}, tgt, SP)
        rep("Jret/roll5 | J/roll5   (reverse)", t[nm[1]], {"a": t[nm[0]]}, tgt, SP)
        print("  -- the original traded signal on mask-free / volume-free folds, both periods")
        rep("orig | EMA10 fold(ivol_s)", sig_o, {"a": ema(fold(ivol_s), 10)}, tgt, SP)
        rep("orig | EMA10 fold(ivol_s) + EMA10(ivol_s/roll5)", sig_o, {"a": ema(fold(ivol_s), 10), "b": ema(rt[nm[2]], 10)}, tgt, SP)
        rep("orig | EMA10 fold(Jret)", sig_o, {"a": ema(fold(Jret), 10)}, tgt, SP)
        say("all done")


if __name__ == "__main__":
    main()
