"""x2 -- can the long leg of  abs_(cs_demean(day_skew(Low)))  be made better by STRUCTURE (not only by smoothing)?

x1 left four leads that only make sense for this tree, plus one engine discrepancy to chase:

  a. forensics: the engine's cross_mean(base, N) is not the rolling nanmean of the cached base panel
     (x1 0b: Spearman 0.9989, max abs diff 12.6).  Where, and why?
  b. the fold centre: at the event level the best next-day bucket is B in (-0.5, -0.25], not B = 0, and the
     positive side is a slope while the negative side is a cliff.  Shifted folds |B - c| and tilted folds |B| + lam*B.
  c. why cs_demean matters for the LONG leg (x1 4: long gross 9.4% -> 3.4% without it): a stock whose daily level-skew
     moves WITH the market's mean skew.  Measure that directly: rolling corr / beta of A_i,t on mu_t.
     And: who is rotated into the long decile by cs_demean?
  d. the part of |B| not shared with the kurtosis of the same path (x1 7: residual long gross 13.2%).
  e. for every lead that survives a-d: what does a LONG-ONLY user get on top of the known Amt-level family?
  f. by calendar year (utrain only): long-leg net of the slow versions, of the known family, and of their sum.

Only utrain rows are sliced.  `x2_elevate.py --mock` runs on random arrays.
"""
import inspect
import sys
import time
import warnings

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402

import numpy as np  # noqa: E402

from x1_anatomy import (FID, BASE, HEAD, FakeStudy, ann, cs_dm, excess, f64, line, line_fixed,  # noqa: E402
                        pct_rank, roll_mean, row_at, section, spearman_days)

MOCK = "--mock" in sys.argv[1:]
T0 = time.time()
EX = {
    "A":     "day_skew(Low)",
    "base":  BASE,
    "kurtL": "day_kurt(Low)",
    "m20":   f"cross_mean({BASE}, 20)",
    "m60":   f"cross_mean({BASE}, 60)",
    "m120":  f"cross_mean({BASE}, 120)",
}


def hdr(s):
    print(f"\n======== {s} ========  [{time.time() - T0:.0f}s]", flush=True)


def roll_sum(x, n):
    """Causal rolling sum of the finite cells (NaN counted as 0) and the count of finite cells."""
    x = f64(x)
    fin = np.isfinite(x)
    c = np.cumsum(np.where(fin, x, 0.0), axis=0)
    k = np.cumsum(fin, axis=0).astype(np.float64)
    c2, k2 = c.copy(), k.copy()
    c2[n:] = c[n:] - c[:-n]
    k2[n:] = k[n:] - k[:-n]
    return c2, k2


def roll_mean_compact(x, n):
    """Mean of the last n FINITE observations of each stock (the day axis with its gaps removed); NaN on gap days."""
    x = f64(x)
    out = np.full(x.shape, np.nan)
    for j in range(x.shape[1]):
        col = x[:, j]
        idx = np.nonzero(np.isfinite(col))[0]
        if idx.size == 0:
            continue
        c = np.cumsum(col[idx])
        c2 = c.copy()
        c2[n:] = c[n:] - c[:-n]
        out[idx, j] = c2 / np.minimum(np.arange(1, idx.size + 1), n)
    return out


def roll_corr_beta(a, mu, n, min_obs=10):
    """Rolling (over the last n days) correlation and OLS beta of a stock's series a[:, i] on the common series mu[:]."""
    a = f64(a)
    fin = np.isfinite(a) & np.isfinite(mu)[:, None]
    x = np.where(fin, a, np.nan)
    y = np.where(fin, mu[:, None], np.nan)
    sx, k = roll_sum(x, n)
    sy, _ = roll_sum(y, n)
    sxx, _ = roll_sum(x * x, n)
    syy, _ = roll_sum(y * y, n)
    sxy, _ = roll_sum(x * y, n)
    kk = np.maximum(k, 1.0)
    cov = sxy / kk - sx / kk * sy / kk
    vx = sxx / kk - (sx / kk) ** 2
    vy = syy / kk - (sy / kk) ** 2
    ok = (k >= min_obs) & (vx > 1e-12) & (vy > 1e-12)
    corr = np.where(ok, cov / np.sqrt(np.where(ok, vx * vy, 1.0)), np.nan)
    beta = np.where(ok, cov / np.where(ok, vy, 1.0), np.nan)
    return corr, beta


def main():
    if MOCK:
        st_cm = FakeStudy()
    else:
        try:
            from alphacube.operators import common as C
            print("# common._kurt\n" + inspect.getsource(inspect.unwrap(C._kurt)))
        except Exception as exc:
            print(f"_kurt source unavailable: {exc}")
        st_cm = Study(FID)
    with st_cm as st:
        P = st.panels(EX)
        miss = [k for k in EX if k not in P]
        if miss:
            print("MISSING panels:", miss, flush=True)
        ut, tr, va = st.slice("utrain"), st.slice("train"), st.slice("valid")
        sl = {"train": tr, "valid": va}
        tgt = st.target()
        dates = np.asarray(st.dates)
        syms = np.asarray(st.symbols)
        A, base = f64(P["A"]), f64(P["base"])
        Bs = cs_dm(A)
        absB = np.abs(Bs)
        mu = np.nanmean(A, axis=1)
        kurtL = f64(P["kurtL"])
        known = f64(st.control("known_stdamt_mean30"))
        ctl = {n: f64(st.control(n)) for n in ("ctl_cap", "ctl_amt", "ctl_turnrate", "ctl_dvol20", "ctl_price", "ctl_mom20")}

        base_sg = st.sign(base, "train")
        base_b = st.books(base, fit="train", evals=("train", "valid"), sign=base_sg)
        base_sm = bk.smoothed(base_sg * base, base_b["by_rank"]["long"]["hl"])
        SIG = {}

        def book(name, panel, keep=True):
            p = f64(panel)
            sg = st.sign(p, "train")
            b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
            sm = bk.smoothed(sg * p, b["by_rank"]["long"]["hl"])
            line(name, sg, b, spearman_days(sm[tr], base_sm[tr]))
            if keep:
                SIG[name] = (sg, b, sm)
            return sg, b, sm

        # ---------------------------------------------------------------- a
        def sa():
            hdr("a. forensics: engine cross_mean(base, 60) vs numpy rolling nanmean of the cached base panel (utrain rows)")
            e = f64(P["m60"])[ut]
            for nm, m_full in (("rolling nanmean over calendar rows (what the kernel source says)", roll_mean(base, 60)),
                               ("mean of the last 60 FINITE observations (gaps removed)", roll_mean_compact(base, 60))):
                m = m_full[ut]
                both = np.isfinite(e) & np.isfinite(m)
                d = np.abs(e - m)[both]
                print(f"-- {nm}:\n   cells finite in both {both.sum()}; engine-only finite {int((np.isfinite(e) & ~np.isfinite(m)).sum())}; "
                      f"numpy-only finite {int((~np.isfinite(e) & np.isfinite(m)).sum())}")
                print("   |diff| quantiles: " + "  ".join(f"q{q:g}={np.quantile(d, q):.3g}" for q in (0.5, 0.9, 0.99, 0.999, 1.0))
                      + f";  share > 1e-3: {float((d > 1e-3).mean()):.4f};  share > 0.05: {float((d > 0.05).mean()):.4f};  Spearman {spearman_days(e, m):.5f}")
            m = roll_mean(base, 60)[ut]
            both = np.isfinite(e) & np.isfinite(m)
            d = np.where(both, np.abs(e - m), -1.0)
            bu = base[ut]
            nfin = roll_sum(base, 60)[1][ut]
            order = np.argsort(d, axis=None)[::-1][:8]
            print("-- the 8 largest differences (calendar-row version):")
            for flat in order:
                i, j = np.unravel_index(flat, d.shape)
                w = bu[max(0, i - 59):i + 1, j]
                wf = w[np.isfinite(w)]
                print(f"   {dates[ut][i]} {syms[j]}: engine {e[i, j]:.3f}  numpy {m[i, j]:.3f}  finite days in window {int(nfin[i, j])}  "
                      f"base today {bu[i, j]:.3f}  window max {wf.max() if wf.size else float('nan'):.2f}  window mean {wf.mean() if wf.size else float('nan'):.3f}  "
                      f"last 5 finite {np.round(wf[-5:], 2).tolist()}")
            bigm = both & (np.abs(e - m) > 0.05)
            if bigm.sum():
                print(f"   cells with |diff| > 0.05: {int(bigm.sum())}; their mean finite-days-in-window {float(nfin[bigm].mean()):.1f} "
                      f"(all cells: {float(nfin[both].mean()):.1f}); share whose base is NaN today {float(np.isnan(bu[bigm]).mean()):.3f}; "
                      f"engine > numpy in {float((e[bigm] > m[bigm]).mean()):.3f}")
                col = bigm.sum(0)
                print(f"   stocks involved: {int((col > 0).sum())}; the 5 with most such cells: "
                      + ", ".join(f"{syms[j]}({int(col[j])})" for j in np.argsort(col)[::-1][:5]))
        section(sa)

        # ---------------------------------------------------------------- b
        def sb():
            hdr("b. fold centre and tilt (numpy), 20- and 60-day rolling mean, half-life grid on top")
            print(HEAD)
            for n in (20, 60):
                for c in (-0.6, -0.4, -0.2, 0.0, 0.2):
                    book(f"mean{n}(|B - ({c:+.1f})|)", roll_mean(np.abs(Bs - c), n), keep=(c in (-0.4, 0.0)))
                for lam in (-0.3, 0.3, 0.6):
                    book(f"mean{n}(|B| {lam:+.1f}*B)", roll_mean(absB + lam * Bs, n), keep=(lam == 0.3))
            print("-- the same shift on the raw daily panel with the EMA grid (no rolling mean), for the fixed-half-life comparison:")
            for c in (-0.4, -0.2, 0.0):
                book(f"|B - ({c:+.1f})|", np.abs(Bs - c), keep=False)
        section(sb)

        # ---------------------------------------------------------------- c
        def sc():
            hdr("c. co-movement of the daily level-skew with the market's mean skew: rolling corr / beta of A_i on mu")
            print(f"mu_t (cross-sectional mean of A): sd over utrain days {float(np.nanstd(mu[ut])):.3f}; lag-1 autocorr "
                  f"{float(np.corrcoef(mu[ut][1:], mu[ut][:-1])[0, 1]):+.3f}")
            print(HEAD)
            sync = {}
            for n in (30, 60, 120):
                corr, beta = roll_corr_beta(A, mu, n)
                sync[n] = corr
                book(f"corr{n}(A_i, mu)", corr, keep=(n == 60))
                if n == 60:
                    book(f"beta{n}(A_i on mu)", beta, keep=False)
                    book(f"|beta{n} - 1|", np.abs(beta - 1.0), keep=False)
            c60 = sync[60]
            print(f"Spearman(corr60, base traded signal) train: {spearman_days(c60[tr], base_sm[tr]):+.3f};  "
                  f"with -known_stdamt_mean30: {spearman_days(c60[tr], -known[tr]):+.3f};  with log cap: {spearman_days(c60[tr], ctl['ctl_cap'][tr]):+.3f}")
            # who does cs_demean rotate into the long decile?
            smA = bk.smoothed(-np.abs(A), 20)
            R = {n: pct_rank(c) for n, c in ctl.items()}
            R["corr60(A,mu)"] = pct_rank(c60)
            R["known_stdamt"] = pct_rank(known)
            for name, s in sl.items():
                rb, ra = pct_rank(base_sm[s]), pct_rank(smA[s])
                ok = np.isfinite(rb) & np.isfinite(ra)
                ex = excess(tgt[s], ok)
                tb, ta = ok & (rb >= 0.9), ok & (ra >= 0.9)
                print(f"-- {name}: long deciles of EMA20(-|B|) and EMA20(-|A|): overlap {float((tb & ta).sum() / max(tb.sum(), 1)):.3f}")
                print(f"   {'group':<34} {'share':>6} {'excess':>8} " + " ".join(f"{k.replace('ctl_', '')[:12]:>12}" for k in R))
                for gn, m in (("in both", tb & ta), ("only with cs_demean (|B|)", tb & ~ta), ("only without (|A|)", ta & ~tb)):
                    print(f"   {gn:<34} {m.sum() / max(ok.sum(), 1):6.3f} {ann(ex[m]):+7.1f}% "
                          + " ".join(f"{np.nanmean(v[s][m]):12.2f}" for v in R.values()))
        section(sc)

        # ---------------------------------------------------------------- d
        def sd():
            hdr("d. the part of |B| not shared with the kurtosis of the same price-level path")
            print(HEAD)
            for n in (20, 60):
                f, k = roll_mean(base, n), roll_mean(kurtL, n)
                resid, info = dg.neutralise(f, {"k": k})
                print(f"   (mean{n}: rank-space R2 of |B| on kurt(Low) = {info['mean_r2']:.3f})")
                book(f"resid(mean{n}|B| ~ mean{n} kurtLow)", resid, keep=(n == 20))
                book(f"mean{n}(kurt(Low))", k, keep=False)
            ratio = absB / np.sqrt(np.maximum(kurtL + 2.0, 1e-6))        # |skew| / sqrt(kurt - 1): one-sidedness in [0, 1]
            for n in (20, 60):
                book(f"mean{n}(|B| / sqrt(kurtLow + 2))", roll_mean(ratio, n), keep=False)
        section(sd)

        # ---------------------------------------------------------------- e
        def se():
            hdr("e. on top of the known Amt-level family (K = cross_mean(day_std(Amt), 30)), for a long-only book")
            print(HEAD)
            ksg, kb, ksm = book("known_stdamt_mean30", known, keep=False)
            F = {}
            for nm in ("m20", "m60", "m120"):
                if nm in P:
                    F[f"engine {nm}"] = book(f"engine {nm}", P[nm], keep=False)[2]
            for nm in ("mean20(|B - (-0.4)|)", "mean60(|B - (-0.4)|)", "mean20(|B| +0.3*B)", "corr60(A_i, mu)",
                       "resid(mean20|B| ~ mean20 kurtLow)"):
                if nm in SIG:
                    F[nm] = SIG[nm][2]
            for name, s in sl.items():
                zk, rk = dg._zrank(ksm[s]), pct_rank(ksm[s])
                n_ = slice(0, zk.shape[0])
                b0 = bk.book_row(zk, tgt[s], n_)
                print(f"\n-- {name}:  K alone: Lnet {b0['long_ann'] * 100:+6.1f}%  Lshp {b0['long_sharpe']:+5.2f}  Lgross {b0['long_gross_ann'] * 100:+6.1f}%  "
                      f"LTO {b0['long_turnover'] * 100:4.1f}%  Lmdd {b0['long_mdd'] * 100:+6.1f}%")
                for fn, fsm in F.items():
                    zf, rf = dg._zrank(fsm[s]), pct_rank(fsm[s])
                    both = np.isfinite(rk) & np.isfinite(rf)
                    ex = excess(tgt[s], both)
                    resid, info = dg.neutralise(zf, {"k": zk}, panel_ready=True, controls_ready=True)
                    rows = (("F alone", bk.book_row(zf, tgt[s], n_)), ("F resid on K", bk.book_row(resid, tgt[s], n_)),
                            ("rank F + rank K", bk.book_row(zf + zk, tgt[s], n_)), ("0.5 rank F + rank K", bk.book_row(0.5 * zf + zk, tgt[s], n_)))
                    print(f"   F = {fn}: Spearman(F, K) {spearman_days(fsm[s], ksm[s]):+.3f}; R2(F ~ K) {info['mean_r2']:.3f}")
                    for lab_, b_ in rows:
                        print(f"      {lab_:<22} Lnet {b_['long_ann'] * 100:+6.1f}%  Lshp {b_['long_sharpe']:+5.2f}  Lgross {b_['long_gross_ann'] * 100:+6.1f}%  "
                              f"LTO {b_['long_turnover'] * 100:4.1f}%  LS {b_['ls_sharpe']:+5.2f}  Lmdd {b_['long_mdd'] * 100:+6.1f}%")
                    inK = both & (rk >= 0.9) & np.isfinite(ex)
                    rin = pct_rank(np.where(inK, fsm[s], np.nan))
                    t3 = [ann(ex[inK & (rin >= a) & (rin < b)]) for a, b in ((0, 1 / 3), (1 / 3, 2 / 3), (2 / 3, 1.01))]
                    bad = inK & (rf < 0.3)
                    print(f"      inside K top 10%, by F tercile (low -> high): {t3[0]:+6.1f}% {t3[1]:+6.1f}% {t3[2]:+6.1f}%;   "
                          f"K-top names in F's bottom 30%: share {bad.sum() / max(inK.sum(), 1):.3f}, {ann(ex[bad]):+6.1f}% vs rest {ann(ex[inK & ~bad]):+6.1f}%")
        section(se)

        # ---------------------------------------------------------------- f
        def sf():
            hdr("f. by calendar year (utrain only): long-leg NET excess / pure-long Sharpe / long turnover")
            yrs = np.array([int(str(d)[:4]) for d in dates])
            ksg = st.sign(known, "train")
            kb = st.books(known, fit="train", evals=("train", "valid"), sign=ksg)
            ksm = bk.smoothed(ksg * known, kb["by_rank"]["long"]["hl"])
            sigs = {"base EMA20": base_sm, "K (known_stdamt_mean30)": ksm}
            for nm in ("m20", "m60", "m120"):
                if nm in P:
                    p = f64(P[nm])
                    b = st.books(p, fit="train", evals=("train", "valid"), sign=base_sg)
                    sm = bk.smoothed(base_sg * p, b["by_rank"]["long"]["hl"])
                    sigs[f"engine {nm} @hl{b['by_rank']['long']['hl']:g}"] = sm
                    if nm == "m60":
                        sigs["0.5 rank(m60) + rank(K)"] = 0.5 * dg._zrank(sm) + dg._zrank(ksm)
                        sigs["rank(m60) + rank(K)"] = dg._zrank(sm) + dg._zrank(ksm)
            ylist = sorted(set(yrs[ut].tolist()))
            print(f"{'signal':<30} " + " ".join(f"{y:>20}" for y in ylist))
            for nm, sm in sigs.items():
                cells = []
                for y in ylist:
                    idx = np.nonzero(yrs == y)[0]
                    idx = idx[(idx >= ut.start) & (idx < ut.stop)]
                    r = bk.book_row(sm, tgt, slice(int(idx[0]), int(idx[-1]) + 1))
                    cells.append(f"{r['long_ann'] * 100:+6.1f}% {r['long_sharpe']:+5.2f} {r['long_turnover'] * 100:4.1f}%")
                print(f"{nm:<30} " + " ".join(f"{c:>20}" for c in cells))
        section(sf)
    print(f"\n[x2 done in {time.time() - T0:.0f}s]", flush=True)


if __name__ == "__main__":
    main()
