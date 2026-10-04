"""x1 -- anatomy of  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))  on real data.
Only train / valid rows are read.

  0. self-checks: the stage-table numbers of the original; is the NT-face window minutes-in-a-day
     (compare with the DT-face twin of the same kernel); is the tree max(Kmax, -Kmin)^3
  1. distribution of r = max|K| over the day: where the fold is active, the EPS mass points,
     next-day excess by band of r
  2. the same by price level (is the tree scale-free on real data?) and by size
  3. who sits in each decile of the TRADED signal (sign x panel, EMA at the long-book half-life)
  4. a finer profile of the traded signal (20 bins)
  5. the short leg and the names that could not have been bought (limit-up at the next open)
  6. books of the pieces and of the naive stand-ins (same convention as the stage tables)
  7. rank correlations of the traded signals
  8. double sorts: inside size buckets; inside the known family's long pool
  9. preview of explicit day-axis memory and of an exclusion overlay on the known family
"""
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402

FID = "F108_max_ntkurt_close"
K = "nt_ts_kurt(Close, 30)"
EX = {
    "base":  f"day_max(pow_1_5(pow_2({K})))",
    "kmax":  f"day_max({K})",
    "kmin":  f"day_min({K})",
    "sd_nt": "day_max(nt_ts_stddev(Close, 30))",
    "sd_in": "day_max(in_stddev_rolling(Close, 30))",
    "zabs":  "day_max(abs_(in_zscore_rolling(Close, 30)))",
    "zup":   "day_max(in_zscore_rolling(Close, 30))",
    "zdn":   "day_min(in_zscore_rolling(Close, 30))",
    "jmax":  "day_max(abs_(Ret))",
    "rkurt": "day_kurt(Ret)",
    "ckurt": "day_kurt(Close)",
}
CTL = ["ctl_cap", "ctl_price", "ctl_amt", "ctl_turnrate", "ctl_ivol", "ctl_dvol20", "ctl_rev1", "ctl_mom20",
       "known_stdamt_mean30", "known_stdamt_max9", "known_ivol_max9"]


def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


def pct_rank(a):
    r = dg.rank_rows(np.asarray(a, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def bucket(pr, n):
    return np.where(np.isfinite(pr), np.minimum(np.floor(pr * n), n - 1), np.nan)


def excess(t, universe):
    """label minus the equal-weight mean of the labelled cells of `universe` (NaN elsewhere)."""
    r = np.where(universe & np.isfinite(t), t, np.nan)
    return r - np.nanmean(r, axis=1, keepdims=True)


def cell_ann(ex, sel):
    """annualised mean (%) of the daily equal-weight excess of the cells in sel; mean names a day."""
    sel = sel & np.isfinite(ex)
    m = sel.sum(1)
    daily = np.where(m > 0, np.where(sel, ex, 0.0).sum(1) / np.maximum(m, 1), np.nan)
    return float(np.nanmean(daily) * 252 * 100), float(m.mean())


def row_corr(ra, rb):
    ok = np.isfinite(ra) & np.isfinite(rb)
    a = np.where(ok, ra, np.nan)
    b = np.where(ok, rb, np.nan)
    a = a - np.nanmean(a, axis=1, keepdims=True)
    b = b - np.nanmean(b, axis=1, keepdims=True)
    num = np.nansum(a * b, axis=1)
    den = np.sqrt(np.nansum(a * a, axis=1) * np.nansum(b * b, axis=1))
    return float(np.nanmean(np.where(den > 0, num / np.where(den > 0, den, 1), np.nan)))


def roll_mean(x, d):
    x = np.asarray(x, dtype=np.float64)
    fin = np.isfinite(x)
    cs = np.cumsum(np.where(fin, x, 0.0), axis=0)
    cn = np.cumsum(fin, axis=0).astype(np.float64)
    s, n = cs.copy(), cn.copy()
    s[d:] -= cs[:-d]
    n[d:] -= cn[:-d]
    return np.where(n > 0, s / np.maximum(n, 1), np.nan)


def roll_max(x, d):
    x = np.asarray(x, dtype=np.float64)
    out = np.where(np.isfinite(x), x, -np.inf)
    acc = out.copy()
    for k in range(1, d):
        acc[k:] = np.maximum(acc[k:], out[:-k])
    return np.where(np.isfinite(acc), acc, np.nan)


def book_line(st, name, panel, sign=None):
    b = st.books(panel, fit="train", evals=("train", "valid"), sign=sign)
    lo, ls = b["by_rank"]["long"], b["by_rank"]["ls"]
    tr, va = lo["splits"]["train"], lo["splits"]["valid"]
    str_, sva = ls["splits"]["train"], ls["splits"]["valid"]
    sg = st.sign(panel, "train") if sign is None else sign
    print(f"{name:<14} sgn {sg:+.0f} | hlL {lo['hl']:>3g}  Lnet {tr['long_ann'] * 100:+6.1f}%/{va['long_ann'] * 100:+6.1f}%  "
          f"Lshp {tr['long_sharpe']:+5.2f}/{va['long_sharpe']:+5.2f}  Lgross {tr['long_gross_ann'] * 100:+6.1f}%/"
          f"{va['long_gross_ann'] * 100:+6.1f}%  LTO {tr['long_turnover'] * 100:4.1f}% | hlS {ls['hl']:>3g}  "
          f"LS {str_['ls_sharpe']:+5.2f}/{sva['ls_sharpe']:+5.2f}  short {str_['short_gross_ann'] * 100:+6.1f}%/"
          f"{sva['short_gross_ann'] * 100:+6.1f}%", flush=True)
    return b


def fixed_line(st, name, panel, tgt, tr, va, sign, hls=(0, 5, 20)):
    p = sign * np.asarray(panel, dtype=np.float64)
    bits = []
    for hl in hls:
        sm = bk.smoothed(p, hl)
        a, b = bk.book_row(sm, tgt, tr), bk.book_row(sm, tgt, va)
        bits.append(f"hl{hl:<2} Lnet {a['long_ann'] * 100:+6.1f}%/{b['long_ann'] * 100:+6.1f}% Lgross "
                    f"{a['long_gross_ann'] * 100:+5.1f}%/{b['long_gross_ann'] * 100:+5.1f}% LTO {a['long_turnover'] * 100:4.1f}%")
    print(f"{name:<14} " + "  |  ".join(bits), flush=True)


def safe(fn, label):
    try:
        fn()
    except Exception as exc:                                    # one broken section must not waste the run
        import traceback
        print(f"[section {label} FAILED] {type(exc).__name__}: {exc}", flush=True)
        traceback.print_exc()


def main(st):
    P = st.panels(EX)
    missing = [k for k in EX if k not in P]
    if missing:
        print("MISSING panels:", missing, flush=True)
    C = {}
    for k in CTL:
        try:
            C[k] = st.control(k)
        except Exception as exc:
            print(f"control {k} unavailable: {exc}", flush=True)
    tr, va = st.slice("train"), st.slice("valid")
    tgt = st.target()
    splits = (("train", tr), ("valid", va))
    base64 = np.asarray(P["base"], dtype=np.float64)
    r_full = np.cbrt(base64)                                   # max|K| over the day

    # ------------------------------------------------------------ 0
    def s0():
        hdr("0. self-checks")
        print("stage table S0 says: v_base sgn - | hlL 20 Lnet +0.3%/+2.5% Lshp +0.05/+0.46 Lgross +3.9%/+6.2% "
              "LTO 4.7% | hlS 5 LS +2.83/+2.53 short +48.3%")
        book_line(st, "base", P["base"])
        if "sd_nt" in P and "sd_in" in P:
            a, b = np.asarray(P["sd_nt"][tr], dtype=np.float64), np.asarray(P["sd_in"][tr], dtype=np.float64)
            ok = np.isfinite(a) & np.isfinite(b)
            rel = np.abs(a - b)[ok] / np.maximum(np.abs(b[ok]), 1e-12)
            print(f"window axis: day_max(nt_ts_stddev(Close,30)) vs day_max(in_stddev_rolling(Close,30)) [train]: "
                  f"rank corr {dg.pair_rank_corr(a, b):.5f}, median rel diff {np.median(rel):.2e}, "
                  f"p99 rel diff {np.quantile(rel, 0.99):.2e}, both finite {ok.mean():.4f} "
                  f"(nt finite {np.isfinite(a).mean():.4f}, in finite {np.isfinite(b).mean():.4f})")
        if "kmax" in P and "kmin" in P:
            kx, kn = np.asarray(P["kmax"][tr], dtype=np.float64), np.asarray(P["kmin"][tr], dtype=np.float64)
            b_ = base64[tr]
            rec = np.maximum(kx, -kn) ** 3
            ok = np.isfinite(b_) & np.isfinite(rec)
            rel = np.abs(b_ - rec)[ok] / np.maximum(b_[ok], 1e-12)
            print(f"fold identity: base vs max(Kmax, -Kmin)^3 [train]: median rel diff {np.median(rel):.2e}, "
                  f"p99 {np.quantile(rel, 0.99):.2e}, p99.9 {np.quantile(rel, 0.999):.2e}, max {rel.max():.2e}; "
                  f"rank corr {dg.pair_rank_corr(b_, rec):.5f}; finite base {np.isfinite(b_).mean():.4f} "
                  f"recon {np.isfinite(rec).mean():.4f}")
            print(f"Kmin range [{np.nanmin(kn):.4f}, {np.nanmax(kn):.4f}]  Kmax range [{np.nanmin(kx):.4f}, "
                  f"{np.nanmax(kx):.4f}]  (EPS-damped kernel: Kmin > -3; one outlier in 30: Kmax <= 25.0345)")
    safe(s0, "0")

    # ------------------------------------------------------------ 1
    def s1():
        hdr("1. distribution of r = max|K| over the day [train rows]")
        r = r_full[tr]
        fin = np.isfinite(r)
        lab = np.isfinite(tgt[tr])
        print(f"cells with a label: {lab.mean():.4f}; of those, base finite: {(fin & lab).sum() / lab.sum():.4f}")
        qs = [0.01, 0.05, 0.10, 0.25, 0.50, 0.75, 0.90, 0.95, 0.99]
        print("quantiles of r: " + "  ".join(f"q{int(q * 100):02d} {v:.3f}" for q, v in zip(qs, np.nanquantile(r, qs))))
        if "kmax" in P and "kmin" in P:
            kx, kn = np.asarray(P["kmax"][tr], dtype=np.float64), np.asarray(P["kmin"][tr], dtype=np.float64)
            okk = np.isfinite(kx) & np.isfinite(kn)
            n = okk.sum()
            print(f"fold active (-Kmin > Kmax): {((-kn > kx) & okk).sum() / n:.4f};  Kmax > 3: {((kx > 3) & okk).sum() / n:.4f};  "
                  f"Kmin <= -1.99: {((kn <= -1.99) & okk).sum() / n:.4f};  Kmin < -2.05: {((kn < -2.05) & okk).sum() / n:.4f};  "
                  f"Kmin < -2.5: {((kn < -2.5) & okk).sum() / n:.4f}")
            print("quantiles of Kmin: " + "  ".join(f"q{int(q * 100):02d} {v:.3f}" for q, v in zip(qs, np.nanquantile(kn, qs))))
            print("quantiles of Kmax: " + "  ".join(f"q{int(q * 100):02d} {v:.3f}" for q, v in zip(qs, np.nanquantile(kx, qs))))
        nf = fin.sum()
        for lo, hi, what in ((2.7109, 2.7129, "one-tick blip in a flat window (-2.7119)"),
                             (2.6144, 2.6164, "two closes one tick apart, 50/50 (-2.6154)"),
                             (1.995, 2.005, "2-point opening window, undamped (-2.00)"),
                             (25.02, 25.05, "one outlier in a flat 30-minute window (25.03)")):
            print(f"mass at r in [{lo}, {hi}] ({what}): {((r >= lo) & (r <= hi)).sum() / nf:.4f}")
        bands = [(0, 1.995), (1.995, 2.005), (2.005, 2.3), (2.3, 2.6), (2.6, 2.75), (2.75, 3.0), (3.0, 4.0), (4.0, 6.0),
                 (6.0, 10.0), (10.0, 15.0), (15.0, 20.0), (20.0, 24.9), (24.9, 26.0)]
        print("next-day excess by band of TODAY's r (annualised %, equal-weight vs all scored names; train | valid):")
        for sname, sl in splits:
            rr = r_full[sl]
            ex = excess(tgt[sl], np.isfinite(rr))
            line = []
            for lo, hi in bands:
                sel = (rr >= lo) & (rr < hi)
                a, m = cell_ann(ex, sel)
                line.append(f"[{lo:g},{hi:g}) {sel.sum() / np.isfinite(rr).sum() * 100:4.1f}% {a:+6.1f}")
            print(f"  [{sname}] " + " | ".join(line))
    safe(s1, "1")

    # ------------------------------------------------------------ 2
    def s2():
        hdr("2. by price level and by size [train rows]")
        r = r_full[tr]
        for cname in ("ctl_price", "ctl_cap"):
            if cname not in C:
                continue
            c = np.asarray(C[cname][tr], dtype=np.float64)
            if cname == "ctl_price":
                px = np.exp(c)
                qs = [0.01, 0.10, 0.25, 0.50, 0.75, 0.90, 0.99]
                print("day_last(Close) quantiles (yuan): " + "  ".join(
                    f"q{int(q * 100):02d} {v:.2f}" for q, v in zip(qs, np.nanquantile(px, qs))))
            bq = bucket(pct_rank(np.where(np.isfinite(r), c, np.nan)), 5)
            print(f"by quintile of {cname} (low -> high): median r | share fold active | share Kmin<-2.5 | share Kmax>3 | "
                  f"share r>=10 | share r in [1.995,2.3)")
            for q in range(5):
                sel = bq == q
                bits = [f"Q{q + 1}", f"med r {np.nanmedian(r[sel]):.3f}"]
                if "kmax" in P and "kmin" in P:
                    kx, kn = np.asarray(P["kmax"][tr], dtype=np.float64), np.asarray(P["kmin"][tr], dtype=np.float64)
                    bits += [f"fold {(-kn > kx)[sel].mean():.3f}", f"Kmin<-2.5 {(kn < -2.5)[sel].mean():.3f}",
                             f"Kmax>3 {(kx > 3)[sel].mean():.3f}"]
                bits += [f"r>=10 {(r >= 10)[sel].mean():.3f}", f"r in [1.995,2.3) {((r >= 1.995) & (r < 2.3))[sel].mean():.3f}"]
                print("  " + "  ".join(bits))
    safe(s2, "2")

    # ------------------------------------------------------------ 3 + 4
    sig = st.signal(P["base"])                                  # sign x panel, EMA at the long-book half-life (train fit)
    sig0 = -base64                                              # the raw daily panel, sign-aligned

    def s3():
        hdr("3. who is in each decile of the traded signal (D1 = short end ... D10 = long end)")
        names = [c for c in ("ctl_cap", "ctl_price", "ctl_amt", "ctl_turnrate", "ctl_ivol", "ctl_dvol20",
                             "known_stdamt_mean30") if c in C]
        for label, s_ in (("traded (EMA hl fitted on train)", sig), ("raw daily panel (hl 0)", sig0)):
            for sname, sl in splits:
                pr = pct_rank(s_[sl])
                dec = bucket(pr, 10)
                ex = excess(tgt[sl], np.isfinite(s_[sl]))
                ranks = {c: pct_rank(np.where(np.isfinite(s_[sl]), C[c][sl], np.nan)) for c in names}
                print(f"-- {label} [{sname}]")
                print("   dec  excess%   " + "  ".join(f"{c.replace('ctl_', '').replace('known_', 'k_'):>12}" for c in names)
                      + "   med r today   fold today")
                for d in range(10):
                    sel = dec == d
                    a, _ = cell_ann(ex, sel)
                    line = f"   D{d + 1:<3} {a:+7.1f}   " + "  ".join(f"{np.nanmean(ranks[c][sel]):12.3f}" for c in names)
                    line += f"   {np.nanmedian(r_full[sl][sel]):10.3f}"
                    if "kmax" in P and "kmin" in P:
                        kx, kn = np.asarray(P["kmax"][sl], dtype=np.float64), np.asarray(P["kmin"][sl], dtype=np.float64)
                        line += f"   {np.nanmean((-kn > kx)[sel]):9.3f}"
                    print(line)
    safe(s3, "3")

    def s4():
        hdr("4. finer profile of the traded signal: 20 bins (B1 = short end ... B20 = long end), annualised excess %")
        for sname, sl in splits:
            b20 = bucket(pct_rank(sig[sl]), 20)
            ex = excess(tgt[sl], np.isfinite(sig[sl]))
            print(f"  [{sname}] " + " ".join(f"{cell_ann(ex, b20 == k)[0]:+6.1f}" for k in range(20)))
    safe(s4, "4")

    # ------------------------------------------------------------ 5
    def s5():
        hdr("5. the short leg and the names that could not be bought at the next open")
        raw = st.target(buyable=False)
        b = st.books(P["base"], fit="train", evals=("train",))
        for view, hl in (("L/S view", b["hl_ls"]), ("long view", b["hl_long"])):
            sm = bk.smoothed(sig0, hl)
            for sname, sl in splits:
                s_, tb, trw = sm[sl], tgt[sl], raw[sl]
                w = bk.long_short_weights(s_, 0.10)
                held_s, held_l = w < 0, w > 0
                unb = ~np.isfinite(tb) & np.isfinite(trw)
                sh_s = (held_s & unb).sum() / max(held_s.sum(), 1)
                sh_l = (held_l & unb).sum() / max(held_l.sum(), 1)
                sh_u = (unb & np.isfinite(s_)).sum() / max((np.isfinite(s_) & np.isfinite(trw)).sum(), 1)
                mean_unb = float(np.nanmean(trw[held_s & unb])) * 1e4 if (held_s & unb).any() else float("nan")
                se_b = bk.stats(bk.short_leg_excess(w, s_, tb))["ann"] * 100
                se_r = bk.stats(bk.short_leg_excess(w, s_, trw))["ann"] * 100
                lg_b = bk.stats(bk.long_book(w, s_, tb)[1])["ann"] * 100
                lg_r = bk.stats(bk.long_book(w, s_, trw)[1])["ann"] * 100
                ls_b = bk.stats(bk.portfolio_returns(w, tb, 0.0015)[0])["sharpe"]
                ls_r = bk.stats(bk.portfolio_returns(w, trw, 0.0015)[0])["sharpe"]
                print(f"  {view} hl {hl:g} [{sname}]: unbuyable share -- universe {sh_u * 100:.2f}%, short book {sh_s * 100:.2f}%, "
                      f"long book {sh_l * 100:.2f}%; mean next-day return of the unbuyable shorts {mean_unb:+.0f} bp; "
                      f"short-leg gross excess {se_b:+.1f}% (buyable label) vs {se_r:+.1f}% (label without the filter); "
                      f"long-leg gross {lg_b:+.1f}% vs {lg_r:+.1f}%; L/S net Sharpe {ls_b:+.2f} vs {ls_r:+.2f}")
    safe(s5, "5")

    # ------------------------------------------------------------ 6
    PIECES = {}

    def s6():
        hdr("6. books of the pieces and of naive stand-ins (sign and half-life fitted on train, like the tables)")
        PIECES["base"] = base64
        PIECES["r=max|K|"] = r_full
        if "kmax" in P:
            kx = np.asarray(P["kmax"], dtype=np.float64)
            PIECES["Kmax"] = kx
            PIECES["Kmax^3 signed"] = np.sign(kx) * np.abs(kx) ** 3
        if "kmin" in P:
            PIECES["Kmin"] = np.asarray(P["kmin"], dtype=np.float64)
        for k in ("zabs", "zup", "zdn", "jmax", "rkurt", "ckurt"):
            if k in P:
                PIECES[k] = np.asarray(P[k], dtype=np.float64)
        for name, p in PIECES.items():
            safe(lambda: book_line(st, name, p), f"6/{name}")
        print("fixed half-life, sign from train (Lnet train/valid):")
        for name in ("base", "r=max|K|", "Kmax", "Kmax^3 signed", "zabs"):
            if name in PIECES:
                safe(lambda: fixed_line(st, name, PIECES[name], tgt, tr, va, st.sign(PIECES[name], "train")), f"6f/{name}")
    safe(s6, "6")

    # ------------------------------------------------------------ 7
    def s7():
        hdr("7. rank correlation of TRADED signals with the original's traded signal, and with controls [train]")
        Rb = dg.rank_rows(sig[tr])
        Rb0 = dg.rank_rows(sig0[tr])
        RC = {c: dg.rank_rows(np.asarray(C[c][tr], dtype=np.float64)) for c in C}
        print(f"{'':<14} {'vs base(traded)':>15} {'raw vs raw':>10}  " + " ".join(
            f"{c.replace('ctl_', '').replace('known_', 'k_'):>13}" for c in C))
        for name, p in PIECES.items():
            s_ = st.signal(p)
            R = dg.rank_rows(s_[tr])
            sg = st.sign(p, "train")
            R0 = dg.rank_rows((sg * p)[tr])
            print(f"{name:<14} {row_corr(R, Rb):15.3f} {row_corr(R0, Rb0):10.3f}  " + " ".join(
                f"{row_corr(R, RC[c]):13.3f}" for c in C), flush=True)
    safe(s7, "7")

    # ------------------------------------------------------------ 8
    def s8():
        hdr("8a. inside size quintiles: top decile of the traded signal WITHIN the bucket (annualised excess %)")
        if "ctl_cap" in C:
            for sname, sl in splits:
                s_ = sig[sl]
                ok = np.isfinite(s_) & np.isfinite(C["ctl_cap"][sl])
                cq = bucket(pct_rank(np.where(ok, C["ctl_cap"][sl], np.nan)), 5)
                ex_u = excess(tgt[sl], ok)
                out = []
                for q in range(5):
                    inb = cq == q
                    pr = pct_rank(np.where(inb, s_, np.nan))
                    top, bot = inb & (pr >= 0.9), inb & (pr < 0.1)
                    a_top, _ = cell_ann(ex_u, top)
                    a_bot, _ = cell_ann(ex_u, bot)
                    a_all, _ = cell_ann(ex_u, inb)
                    out.append(f"capQ{q + 1}: bucket {a_all:+5.1f} | low-D decile {a_top:+5.1f} ({a_top - a_all:+5.1f} vs bucket) | "
                               f"high-D decile {a_bot:+6.1f}")
                print(f"  [{sname}] " + "\n           ".join(out))
        hdr("8b. inside the known family's long pool (lowest cross_mean(day_std(Amt),30)): split by the F108 traded signal")
        if "known_stdamt_mean30" in C:
            kf = -np.asarray(C["known_stdamt_mean30"], dtype=np.float64)
            for sname, sl in splits:
                s_ = sig[sl]
                ok = np.isfinite(s_) & np.isfinite(kf[sl])
                prk = pct_rank(np.where(ok, kf[sl], np.nan))
                prs = pct_rank(np.where(ok, s_, np.nan))
                ex_u = excess(tgt[sl], ok)
                for frac, nm in ((0.9, "decile"), (0.8, "quintile")):
                    pool = ok & (prk >= frac)
                    pin = pct_rank(np.where(pool, s_, np.nan))
                    a_pool, m_pool = cell_ann(ex_u, pool)
                    parts = [f"pool {a_pool:+5.1f} ({m_pool:.0f} names)"]
                    for lo, hi, nm2 in ((0.0, 1 / 3, "high-D third"), (1 / 3, 2 / 3, "mid"), (2 / 3, 1.01, "low-D third")):
                        a, _ = cell_ann(ex_u, pool & (pin >= lo) & (pin < hi))
                        parts.append(f"{nm2} {a:+5.1f}")
                    a_w, m_w = cell_ann(ex_u, pool & (prs < 0.1))
                    a_b, m_b = cell_ann(ex_u, pool & (prs >= 0.1))
                    parts.append(f"in F108 short decile {a_w:+6.1f} ({m_w:.0f} names) vs rest {a_b:+5.1f}")
                    a_w2, m_w2 = cell_ann(ex_u, pool & (prs < 0.2))
                    parts.append(f"in F108 bottom quintile {a_w2:+6.1f} ({m_w2:.0f} names)")
                    print(f"  [{sname}] known-family long {nm}: " + " | ".join(parts))
                # where does F108's own long / short decile sit in the known family?
                kq = bucket(prk, 5)
                for nm, selx in (("F108 long decile", prs >= 0.9), ("F108 short decile", prs < 0.1)):
                    sh = [float(((kq == q) & selx).sum() / max(selx.sum(), 1)) for q in range(5)]
                    print(f"  [{sname}] {nm}: share in known-family quintiles (short end -> long end) "
                          + " ".join(f"{x:.2f}" for x in sh))
    safe(s8, "8")

    # ------------------------------------------------------------ 9
    def s9():
        hdr("9a. explicit day-axis memory instead of the EMA (books; numpy stand-ins for cross_mean / cross_max)")
        mem = {
            "mean30(base)": roll_mean(base64, 30), "mean60(base)": roll_mean(base64, 60),
            "mean30(r)": roll_mean(r_full, 30), "mean60(r)": roll_mean(r_full, 60),
            "max30(r)": roll_max(r_full, 30), "max10(r)": roll_max(r_full, 10),
            "freq30(r>=10)": roll_mean(np.where(np.isfinite(r_full), (r_full >= 10).astype(np.float64), np.nan), 30),
            "freq60(r>=5)": roll_mean(np.where(np.isfinite(r_full), (r_full >= 5).astype(np.float64), np.nan), 60),
            "freq60(r<3)": roll_mean(np.where(np.isfinite(r_full), (r_full < 3).astype(np.float64), np.nan), 60),
        }
        for name, p in mem.items():
            safe(lambda: book_line(st, name, p), f"9a/{name}")
        hdr("9b. overlay on the known family (pct ranks within day; books fitted like the tables)")
        if "known_stdamt_mean30" in C:
            kf = np.asarray(C["known_stdamt_mean30"], dtype=np.float64)
            book_line(st, "known alone", kf)
            rk = pct_rank(-kf)                                   # high = long in the known family
            m30 = roll_mean(base64, 30)
            rD_ema = 1.0 - pct_rank(sig)                         # high = jumpy (EMA hl 20 of base)
            rD_m30 = pct_rank(m30)
            rD_m60 = pct_rank(roll_mean(base64, 60))
            ov = {
                "add ema20": rk - rD_ema,
                "excl^3 ema20": rk - rD_ema ** 3,
                "add m30": rk - rD_m30,
                "excl^3 m30": rk - rD_m30 ** 3,
                "excl^6 m30": rk - rD_m30 ** 6,
                "excl^3 m60": rk - rD_m60 ** 3,
                "0.5 add m30": rk - 0.5 * rD_m30,
            }
            for name, p in ov.items():
                safe(lambda: book_line(st, name, p, sign=1.0), f"9b/{name}")
            print("fixed half-life (Lnet train/valid), sign +1:")
            fixed_line(st, "known alone", -kf, tgt, tr, va, 1.0)
            for name in ("add m30", "excl^3 m30", "excl^3 ema20"):
                fixed_line(st, name, ov[name], tgt, tr, va, 1.0)
            # residual of the F108 traded signal on the known family (rank space), as a long book
            res, info = dg.neutralise(sig[tr], {"kf": kf[tr]})
            br = bk.book_row(res, tgt[tr], slice(0, res.shape[0]))
            ic = dg.ic_row(res, tgt[tr], sign=1.0)
            print(f"F108 traded signal neutralised on the known family [train]: R2 {info['mean_r2']:.3f}  residual rIC "
                  f"{ic['rank_ic']:+.4f}  Lgross {br['long_gross_ann'] * 100:+.1f}%  Lnet {br['long_ann'] * 100:+.1f}%  "
                  f"short {br['short_gross_ann'] * 100:+.1f}%  LTO {br['long_turnover'] * 100:.1f}%")
            res, info = dg.neutralise(sig[va], {"kf": kf[va]})
            br = bk.book_row(res, tgt[va], slice(0, res.shape[0]))
            ic = dg.ic_row(res, tgt[va], sign=1.0)
            print(f"F108 traded signal neutralised on the known family [valid]: R2 {info['mean_r2']:.3f}  residual rIC "
                  f"{ic['rank_ic']:+.4f}  Lgross {br['long_gross_ann'] * 100:+.1f}%  Lnet {br['long_ann'] * 100:+.1f}%  "
                  f"short {br['short_gross_ann'] * 100:+.1f}%  LTO {br['long_turnover'] * 100:.1f}%")
    safe(s9, "9")


if __name__ == "__main__":
    with Study(FID) as st_:
        main(st_)
    print("\n[x1 done]", flush=True)
