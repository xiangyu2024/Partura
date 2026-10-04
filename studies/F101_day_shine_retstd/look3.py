"""F101, look3 (after S1 + S2): what is the LONG leg made of, and how should the fold be aggregated in time?

S1/S2 left the long leg explained only by a slogan ("background volatility is more robust than burst
volatility").  The train half-life sweeps already contradict the simple version of it: at hl 20 every
fold (event J, full-day std, roll5 ...) has a train long-leg net excess of +9..+10%.  Three things were
changed at once between the original and the roll5 fold -- the statistic (J -> roll5), where the fold
centre sits (J's cs mean is at its 66th percentile, roll5's at its 59th) and the half-life (10 -> 20).
This script separates them and then asks what the fold-then-smooth construction is actually paying for.

  A  ingredient grid at FIXED half-life: statistic {J, ivol, roll5} x fold {mean-level, rank q=.5} x hl {10, 20}
  B  fold-centre scans on roll5 (rank fold q, level fold c x cs_mean) + 20-quantile profile of EMA20(roll5)
  C  how to aggregate |K| in time (K = roll5 - cs mean): EMA only / mean20 / max20 / Fangzheng mean+std / ...
  D  is "moderate and stable in X" generic?  fold(X) for every control; R2 of the roll5 fold on EMA folded controls
  E  does burst information help the long leg?  hybrid rank sum; split of the long decile by burst ratio / cap / turnover
  F  half-lives beyond the pipeline's grid (40, 60) for the roll5 fold and the original
  H  double sort: |EMA K| (near the centre on average) x instability (EMA|K| - |EMA K|)
  Y  per calendar year for the shortlisted constructions

Only train / valid are read.
"""
import time
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
T0 = time.time()


def say(msg):
    print(f"[{time.time() - T0:5.0f}s] {msg}", flush=True)


def fold(x, c=1.0):
    return np.abs(x - c * np.nanmean(x, axis=1, keepdims=True))


def pct(x):
    r = dg.rank_rows(np.asarray(x, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def ema(x, hl):
    return bk.smoothed(np.asarray(x, dtype=np.float64), hl)


def roll_mean(x, d, minp=1):
    fin = np.isfinite(x)
    c = np.cumsum(np.where(fin, x, 0.0), axis=0)
    n = np.cumsum(fin, axis=0).astype(np.float64)
    c2, n2 = c.copy(), n.copy()
    c2[d:] -= c[:-d]
    n2[d:] -= n[:-d]
    return np.where(n2 >= minp, c2 / np.maximum(n2, 1), np.nan)


def roll_std(x, d, minp=5):
    m = roll_mean(x, d, minp)
    m2 = roll_mean(x * x, d, minp)
    return np.sqrt(np.clip(m2 - m * m, 0.0, None))


def roll_max(x, d):
    out = x.copy()
    for k in range(1, d):
        sh = np.full_like(x, np.nan)
        sh[k:] = x[:-k]
        out = np.fmax(out, sh)
    return out


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


with Study(FID) as st:
    P = st.panels({"J": J_EXPR, "roll5": f"day_mean(in_stddev_rolling({R}, 5))"})
    J, roll5 = np.asarray(P["J"], dtype=np.float64), np.asarray(P["roll5"], dtype=np.float64)
    ctl = {k: np.asarray(st.control(k), dtype=np.float64) for k in
           ("ctl_ivol", "ctl_dvol20", "ctl_turnrate", "ctl_cap", "ctl_amt", "ctl_price", "ctl_range", "ctl_rev1", "ctl_mom20")}
    ivol = ctl["ctl_ivol"]
    tgt = np.asarray(st.target(), dtype=np.float64)
    tr, va = st.slice("train"), st.slice("valid")
    SP = {"train": tr, "valid": va}
    years = np.array([int(str(d)[:4]) for d in st.dates])
    say("panels ready")

    def row(name, sm):
        """sm: sign-aligned, already smoothed."""
        out = [f"  {name:<34}"]
        for k, s in SP.items():
            b = bk.book_row(sm, tgt, s)
            out.append(f"{k}: rIC {np.nanmean(dg.rank_ic_series(sm[s], tgt[s])):+.4f} {fmt(b)}")
        print(" | ".join(out), flush=True)

    def fitrow(name, panel, sign=None):
        """The table's convention: sign by train rank IC (unless given), half-life by train L/S Sharpe."""
        p = np.asarray(panel, dtype=np.float64)
        sg = dg.sign_from(p[tr], tgt[tr]) if sign is None else sign
        b = bk.books(sg * p, tgt, tr, SP)
        print(f"  {name:<34} sgn {'+' if sg > 0 else '-'} hl {b['hl_used']:>2g} (long-best hl {b['hl_long']:g}) | "
              + " | ".join(f"{k}: {fmt(v)}" for k, v in b["splits"].items()), flush=True)
        return sg, b["hl_used"]

    def per_year(name, sm):
        out = []
        end = va.stop
        for y in sorted(set(years[:end].tolist())):
            idx = np.where(years[:end] == y)[0]
            b = bk.book_row(sm, tgt, slice(idx[0], idx[-1] + 1))
            out.append(f"{y}: {b['ls_sharpe']:+.2f}|{b['long_ann']*100:+5.1f}|{b['long_sharpe']:+.2f}")
        print(f"  {name:<28} " + "  ".join(out), flush=True)

    # ---------------------------------------------------------------- A
    print("== A  ingredient grid at fixed half-life (sign fixed: long = small folded value)")
    stats_ = {"J(burst)": J, "ivol(full-day std)": ivol, "roll5(background)": roll5}
    for sn, x in stats_.items():
        for fn, f in (("mean-fold", fold(x)), ("rank-fold q=.5", np.abs(pct(x) - 0.5))):
            for hl in (10, 20):
                row(f"{sn} {fn} hl{hl}", -ema(f, hl))
    say("A done")

    # ---------------------------------------------------------------- B
    print("== B  fold-centre scans on roll5, hl 20")
    pr = pct(roll5)
    for q in (0.3, 0.4, 0.5, 0.6, 0.7):
        row(f"rank fold q={q:.1f}", -ema(np.abs(pr - q), 20))
    for c in (0.7, 0.85, 1.0, 1.15, 1.3):
        m = np.nanmean(roll5[tr], axis=1, keepdims=True)
        where = np.nanmean(np.where(np.isfinite(roll5[tr]), roll5[tr] < c * m, np.nan))
        row(f"level fold c={c:.2f} (pct {where:.2f})", -ema(fold(roll5, c), 20))
    row("median-centre level fold", -ema(np.abs(roll5 - np.nanmedian(roll5, axis=1, keepdims=True)), 20))
    row("log-level fold (geo mean)", -ema(np.abs(np.where(roll5 > 0, np.log(roll5), np.nan)
                                                 - np.nanmean(np.where(roll5 > 0, np.log(roll5), np.nan), axis=1, keepdims=True)), 20))
    print("   annualised excess (%) by 20 quantiles of EMA20(roll5), lowest -> highest")
    for sn, s in SP.items():
        q = bk.quantile_profile(ema(roll5, 20), tgt, s, n=20)
        print(f"   {sn}: " + " ".join(f"{r_['excess_ann']*100:+.0f}" for r_ in q), flush=True)
    say("B done")

    # ---------------------------------------------------------------- C
    print("== C  time aggregation of |K| (table convention: half-life fitted on train by L/S Sharpe)")
    for sn, x in (("roll5", roll5), ("J", J)):
        K = x - np.nanmean(x, axis=1, keepdims=True)
        aK = np.abs(K)
        m20, s20 = roll_mean(aK, 20), roll_std(aK, 20)
        cands = {
            f"{sn}: |K| (EMA only)": aK,
            f"{sn}: mean20(|K|)": m20,
            f"{sn}: mean40(|K|)": roll_mean(aK, 40),
            f"{sn}: max10(|K|)": roll_max(aK, 10),
            f"{sn}: max20(|K|)": roll_max(aK, 20),
            f"{sn}: mean20+std20 (cross_fangzheng)": m20 + s20,
            f"{sn}: std20(|K|) alone": s20,
            f"{sn}: std20(K) alone": roll_std(K, 20),
            f"{sn}: rms20(K)": np.sqrt(roll_mean(K * K, 20)),
            f"{sn}: rank(mean20)+rank(std20)": pct(m20) + pct(s20),
        }
        for k, v in cands.items():
            fitrow(k, v)
        if sn == "roll5":
            keep = {"mean20": m20, "max20": cands["roll5: max20(|K|)"], "fz20": m20 + s20}
        del cands
    say("C done")

    # ---------------------------------------------------------------- D
    print("== D  is 'moderate and stable in X' generic?  mean-fold of each control (table convention)")
    for k, v in ctl.items():
        fitrow(f"fold({k[4:]})", fold(v))
    print("   R2 of the roll5-fold traded signal (hl 20) on controls, rank space, train; residual (not re-smoothed)")
    sig_r = -ema(fold(roll5), 20)
    yz = dg._zrank(sig_r[tr])

    def rep(name, cs):
        cz = {k: dg._zrank(v[tr]) for k, v in cs.items()}
        resid, info = dg.neutralise(yz, cz, panel_ready=True, controls_ready=True)
        b = bk.book_row(resid, tgt[tr], slice(0, resid.shape[0]))
        print(f"   {name:<44} R2 {info['mean_r2']:.3f}  resid rIC {np.nanmean(dg.rank_ic_series(resid, tgt[tr])):+.4f}  "
              f"LSgross {b['ls_gross_sharpe']:+.2f}  Lgross {b['long_gross_ann']*100:+5.1f}%  short {b['short_gross_ann']*100:+5.1f}%", flush=True)

    rep("9 linear controls", ctl)
    rep("EMA20 fold(turnrate)", {"a": ema(fold(ctl["ctl_turnrate"]), 20)})
    rep("EMA20 fold(dvol20)", {"a": ema(fold(ctl["ctl_dvol20"]), 20)})
    rep("EMA20 fold(ivol)", {"a": ema(fold(ivol), 20)})
    rep("EMA20 folds of turnrate/dvol20/amt/cap/range", {k: ema(fold(ctl[k]), 20) for k in
                                                        ("ctl_turnrate", "ctl_dvol20", "ctl_amt", "ctl_cap", "ctl_range")})
    rep("9 linear + those 5 EMA20 folds", {**ctl, **{k + "_f": ema(fold(ctl[k]), 20) for k in
                                                     ("ctl_turnrate", "ctl_dvol20", "ctl_amt", "ctl_cap", "ctl_range")}})
    say("D done")

    # ---------------------------------------------------------------- E
    print("== E  does burst information help the long leg?")
    sig_o10, sig_o20 = -ema(fold(J), 10), -ema(fold(J), 20)
    fitrow("rank(fold J)+rank(fold roll5)", pct(fold(J)) + pct(fold(roll5)))
    fitrow("max(rank fold J, rank fold roll5)", np.maximum(pct(fold(J)), pct(fold(roll5))))
    B = J / np.where(roll5 > 0, roll5, np.nan)
    eB = ema(B, 20)
    print("   long decile of the roll5 fold (hl 20), split in halves inside the decile-day; annualised excess % (low half / high half)")
    feats = {"EMA20 burst ratio": eB, "cap": ctl["ctl_cap"], "turnrate": ctl["ctl_turnrate"], "EMA20 roll5 level": ema(roll5, 20),
             "price": ctl["ctl_price"], "mom20": ctl["ctl_mom20"]}
    for sn, s in SP.items():
        ex = excess(tgt[s], sig_r[s])
        top = decile(sig_r[s], True)
        out = []
        for fn, f in feats.items():
            fv = np.where(top, f[s], np.nan)
            med = np.nanmedian(fv, axis=1, keepdims=True)
            lo_, hi_ = top & (fv <= med), top & (fv > med)
            out.append(f"{fn} {np.nanmean(np.where(lo_, ex, np.nan))*25200:+5.1f}/{np.nanmean(np.where(hi_, ex, np.nan))*25200:+5.1f}")
        print(f"   {sn}: " + "  ".join(out), flush=True)
    say("E done")

    # ---------------------------------------------------------------- F
    print("== F  half-lives beyond the pipeline grid (fixed)")
    for hl in (10, 20, 40, 60):
        row(f"roll5 mean-fold hl{hl}", -ema(fold(roll5), hl))
    for hl in (10, 20, 40):
        row(f"original (J mean-fold) hl{hl}", -ema(fold(J), hl))
    say("F done")

    # ---------------------------------------------------------------- H
    print("== H  double sort on roll5: |EMA20 K| tercile (rows: near -> far from centre) x instability tercile (cols: stable -> unstable)")
    K = roll5 - np.nanmean(roll5, axis=1, keepdims=True)
    eK = ema(K, 20)
    aeK = np.abs(eK)
    inst = ema(np.abs(K), 20) - aeK
    pa, pi = pct(aeK), pct(inst)
    print(f"   rank corr(|EMA K|, instability) train {dg.pair_rank_corr(aeK[tr], inst[tr]):+.3f}")
    for sn, s in SP.items():
        ex = excess(tgt[s], aeK[s])
        print(f"   {sn}: annualised excess % (cell share %)")
        for i in range(3):
            cells = []
            for j in range(3):
                m = (pa[s] >= i / 3) & (pa[s] < (i + 1) / 3 + 1e-9) & (pi[s] >= j / 3) & (pi[s] < (j + 1) / 3 + 1e-9)
                cells.append(f"{np.nanmean(np.where(m, ex, np.nan))*25200:+6.1f} ({m.sum() / np.isfinite(ex).sum() * 100:4.1f})")
            print("      " + "   ".join(cells), flush=True)
        # the same, splitting the near-centre tercile by which SIDE of the centre the name sits on average
        near = pa[s] < 1 / 3
        lo_side, hi_side = near & (eK[s] < 0), near & (eK[s] >= 0)
        print(f"      near-centre tercile: below-centre side {np.nanmean(np.where(lo_side, ex, np.nan))*25200:+.1f}  "
              f"above-centre side {np.nanmean(np.where(hi_side, ex, np.nan))*25200:+.1f}", flush=True)
    say("H done")

    # ---------------------------------------------------------------- Y
    print("== Y  per calendar year: LS net Sharpe | long net % | long-only Sharpe")
    per_year("original hl10", sig_o10)
    per_year("original hl20", sig_o20)
    per_year("roll5 mean-fold hl20", sig_r)
    per_year("roll5 rank-fold hl20", -ema(np.abs(pr - 0.5), 20))
    for nm, p in keep.items():
        sg, hl = -1.0, None
        b = bk.books(-p, tgt, tr, SP)
        per_year(f"roll5 {nm} hl{b['hl_used']:g}", -ema(p, b["hl_used"]))
    per_year("fold(ivol) hl20", -ema(fold(ivol), 20))
    hyb = pct(fold(J)) + pct(fold(roll5))
    b = bk.books(-hyb, tgt, tr, SP)
    per_year(f"hybrid rank sum hl{b['hl_used']:g}", -ema(hyb, b["hl_used"]))
    say("all done")
