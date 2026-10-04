"""rev2 -- what rev1 could not finish, and the one new question rev1 raised.  train / valid rows only.

rev1 was stopped by the memory guard (the neighbours filled the container to 34.9 GiB) after its sections A, B, D and
most of C.  Two things are still open:

  F. THE EXACT SPLIT OF THE ORIGINAL (rev1's C2, never reached).  rev1 section C found that the original keeps
     61% / 84% of its rank IC after {f_kurt30, a saturated amt30 x kshare30 grid of 30-day liquidity dummies}: the
     "non-linear illiquidity" reading does not span it.  A 30-day grid cannot see a DAILY non-linearity, though.  So:
     each day, put every stock in a cell = (that day's turnover bucket) x (bucket, inside it, of the share of minutes
     the mask overwrote that day) [x (bucket of the average amount the mask injected per overwritten minute)].
     original(day) = cell mean  ("what the mask reads from WHERE the stock sits in liquidity / k that day")
                   + deviation  ("the shape of the stock's own turnover, given its cell").
     The EMA is linear, so the traded original is exactly the sum of the two smoothed parts.  Which part carries the
     rank IC / the long leg / the short leg, which part f_kurt30 spans, and does adding the cell part to
     {f_kurt30, liquidity} finally kill the residual IC?
  E. WHERE THE LABEL CONVENTION BITES.  rev1 section A/D: ranked inside amt30 ventiles, the concentration reading's
     short decile holds 1.09% names locked at limit-up at the next open (f_kurt30: 0.49%), and its L/S falls from
     3.13 / 0.59 to 1.16 / -0.08 when the short leg is charged the raw label.  Redo x2's liquidity x concentration
     double sort under both labels, and split each short leg by amt30 quintile.
  G. the reverse spanning rows rev1 did not reach (does a conditioned concentration reading carry anything the
     original + liquidity does not?).
"""
import os
import sys
import traceback
import warnings

import numpy as np

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from rev1_review import (COST, EX as EX1, FID, TOP, ann, bucket, cell_split, cells, hdr, hybrid, leg_decomp,  # noqa: E402
                         pct_rank, resid, row_corr, wb_rank, where_legs)
from partura.study_tools import Study, bk, dg  # noqa: E402
from partura.books import long_short_weights  # noqa: E402

MASK = "nt_cs_mask_top_replace_mean_neg(Amt)"
FIT = {"base": (-1.0, 20), "bk": (-1.0, 1), "bc": (-1.0, 0)}
FITN = {"wk20": ("k30", -1.0, 1), "wc20": ("c30", -1.0, 1)}          # as fitted on train in rev1 section A


def cell_ann(ex, sel):
    sel = sel & np.isfinite(ex)
    m = sel.sum(1)
    daily = np.where(m > 0, np.where(sel, ex, 0.0).sum(1) / np.maximum(m, 1), np.nan)
    return float(np.nanmean(daily) * 252 * 100)


def main(study_cls=Study):
    with study_cls(FID) as st:
        EX = {k: EX1[k] for k in ("base", "amt30", "k30", "c30", "bk", "bc")}
        EX["kfrac"] = f"day_mean(is_gt0(sub({MASK}, Amt)))"
        P = st.panels(EX)
        miss = [k for k in EX if k not in P]
        if miss:
            print("MISSING panels:", miss, flush=True)
        ut, tr_, va_ = st.slice("utrain"), st.slice("train"), st.slice("valid")
        off = ut.start
        tr = slice(tr_.start - off, tr_.stop - off)
        va = slice(va_.start - off, va_.stop - off)
        splits = (("train", tr), ("valid", va))
        tgt = np.asarray(st.target()[ut], dtype=np.float64)
        ps = st.ps
        keep = (ps.label_buyable, ps._targets)
        ps.label_buyable, ps._targets = False, {}
        try:
            traw = np.asarray(ps.target(1)[ut], dtype=np.float64)
        finally:
            ps.label_buyable, ps._targets = keep
        locked = np.isfinite(traw) & ~np.isfinite(tgt)

        def smooth(panel, sign, hl):
            return np.asarray(bk.smoothed(sign * np.asarray(panel[:ut.stop], dtype=np.float64), hl)[ut], dtype=np.float64)

        SM = {n: smooth(P[n], *FIT[n]) for n in FIT}
        RAW = {n: P[n][ut] for n in P}
        a30 = np.asarray(RAW["amt30"], dtype=np.float64)
        for name, (src, sg, hl) in FITN.items():
            y = np.asarray(RAW[src], dtype=np.float64)
            w, u = wb_rank(y, bucket(a30, np.isfinite(y) & np.isfinite(a30), 20), 20)
            SM[name] = np.asarray(bk.smoothed(sg * (w + 1e-6 * u), hl), dtype=np.float64)
            del w, u, y

        # the ORIGINAL's traded signal (EMA-20) itself, ranked inside amt30 ventiles: what is the original worth once its
        # liquidity position is neutralised the same way?  (rev1 only did this for its 30-day-mean twin, wb20: 2.61 / 1.09)
        w, u = wb_rank(SM["base"], bucket(a30, np.isfinite(SM["base"]) & np.isfinite(a30), 20), 20)
        SM["wbE20"] = w + 1e-6 * u
        del w, u

        hdr("0. self-check (LS net train/valid: base 3.91/1.47, bk 3.75/1.91, bc 3.77/2.37; rev1: wk20 3.13/0.59 -> raw-short "
            "1.16/-0.08, wc20 3.21/1.11 -> 1.10/0.40); wbE20 = the original's EMA-20 signal ranked inside amt30 ventiles (new)")
        for n in SM:
            r = [bk.book_row(SM[n], tgt, sl, COST) for _, sl in splits]
            h = [hybrid(SM[n][sl], tgt[sl], traw[sl]) for _, sl in splits]
            print(f"{n:>6}  LS {r[0]['ls_sharpe']:+.2f}/{r[1]['ls_sharpe']:+.2f}  raw-short {h[0][0]['sharpe']:+.2f}/"
                  f"{h[1][0]['sharpe']:+.2f}", flush=True)

        def run(fn, *a, **k):
            try:
                fn(*a, **k)
            except Exception:
                print(f"\n!!! {getattr(fn, '__name__', fn)} failed:\n{traceback.format_exc()}", flush=True)

        def z32(x):
            return dg._zrank(np.asarray(x, dtype=np.float64)).astype(np.float32)

        Z = {"bk": z32(SM["bk"]), "bc": z32(SM["bc"]), "a": z32(a30), "base": z32(SM["base"])}
        ks = np.asarray(st.control("ctl_kshare30")[ut], dtype=np.float64)
        fa, fk = np.isfinite(a30), np.isfinite(ks)
        qa20 = bucket(a30, fa, 20)
        Ga = cells(qa20)
        wks, _ = wb_rank(np.where(fa & fk, ks, np.nan), qa20, 20)
        Gak = cells(qa20 * 5 + np.minimum(np.floor(wks * 5), 4))           # the 30-day grid of rev1 section C
        del wks, qa20

        def ncell(G):
            return np.mean([np.unique(G[t][G[t] >= 0]).size for t in range(0, G.shape[0], 50)])

        def fixed(name, sm):
            r = [bk.book_row(sm, tgt, sl, COST) for _, sl in splits]
            ic = [dg.ic_row(sm[sl], tgt[sl], sign=1.0) for _, sl in splits]
            wl = [where_legs(sm[sl], a30[sl]) for _, sl in splits]
            d = [leg_decomp(sm[sl], tgt[sl], a30[sl]) for _, sl in splits]
            h = [hybrid(sm[sl], tgt[sl], traw[sl]) for _, sl in splits]
            print(f"{name:<34} LS {r[0]['ls_sharpe']:+.2f}/{r[1]['ls_sharpe']:+.2f} (gross {r[0]['ls_gross_sharpe']:+.2f}/"
                  f"{r[1]['ls_gross_sharpe']:+.2f}; raw-short {h[0][0]['sharpe']:+.2f}/{h[1][0]['sharpe']:+.2f}) | rIC "
                  f"{ic[0]['rank_ic']:+.4f}/{ic[1]['rank_ic']:+.4f} (t {ic[0]['rank_ic_t']:+.1f}/{ic[1]['rank_ic_t']:+.1f}) | "
                  f"Lgross {r[0]['long_gross_ann'] * 100:+.1f}%/{r[1]['long_gross_ann'] * 100:+.1f}% Lnet "
                  f"{r[0]['long_ann'] * 100:+.1f}%/{r[1]['long_ann'] * 100:+.1f}% | short {r[0]['short_gross_ann'] * 100:+.1f}%/"
                  f"{r[1]['short_gross_ann'] * 100:+.1f}% | TO {r[0]['ls_turnover'] * 100:.1f}%\n"
                  f"{'':<6}long dec amt30 rank {wl[0]['long'][0]:.2f}/{wl[1]['long'][0]:.2f} (least-active quintile "
                  f"{wl[0]['long'][1]:.0%}/{wl[1]['long'][1]:.0%}), short dec {wl[0]['short'][0]:.2f}/{wl[1]['short'][0]:.2f} "
                  f"(most-active quintile {wl[0]['short'][2]:.0%}/{wl[1]['short'][2]:.0%}); long = location + selection "
                  + " / ".join(f"{ann(d[i]['long'][0]):+.1f} = {ann(d[i]['long'][1]):+.1f} + {ann(d[i]['long'][2]):+.1f}"
                               for i in range(2))
                  + "; short "
                  + " / ".join(f"{ann(d[i]['short'][0]):+.1f} = {ann(d[i]['short'][1]):+.1f} + {ann(d[i]['short'][2]):+.1f}"
                               for i in range(2)), flush=True)
            return [ic[0]["rank_ic"], ic[1]["rank_ic"]]

        def line(name, y, cont=(), groups=(), ref=None, extra=False):
            if cont or groups:
                res, r2 = resid(dg._zrank(np.asarray(y, dtype=np.float64)), cont, groups)
            else:
                res, r2 = np.asarray(y, dtype=np.float64), np.full(y.shape[0], np.nan)
            ic = [dg.ic_row(res[sl], tgt[sl], sign=1.0) for _, sl in splits]
            b = [bk.book_row(res, tgt, sl, COST) for _, sl in splits]
            kp = ["%.0f%%" % (100 * ic[i]["rank_ic"] / ref[i]) if ref else "--" for i in range(2)]
            print(f"{name:<40} R2 {np.nanmean(r2[tr]):5.3f}/{np.nanmean(r2[va]):5.3f} | rIC {ic[0]['rank_ic']:+.4f}/"
                  f"{ic[1]['rank_ic']:+.4f} (t {ic[0]['rank_ic_t']:+5.1f}/{ic[1]['rank_ic_t']:+5.1f}) | kept {kp[0]}/{kp[1]} | "
                  f"LSgross {b[0]['ls_gross_sharpe']:+.2f}/{b[1]['ls_gross_sharpe']:+.2f} | L {b[0]['long_gross_ann'] * 100:+5.1f}% "
                  f"S {b[0]['short_gross_ann'] * 100:+5.1f}% , L {b[1]['long_gross_ann'] * 100:+5.1f}% S "
                  f"{b[1]['short_gross_ann'] * 100:+5.1f}%", flush=True)
            if extra:
                wl = [where_legs(res[sl], a30[sl]) for _, sl in splits]
                ci = [dg.conditional_ic(res[sl], tgt[sl], a30[sl], buckets=5) for _, sl in splits]
                d = [leg_decomp(res[sl], tgt[sl], a30[sl]) for _, sl in splits]
                print(f"{'':<6}residual's long decile amt30 rank {wl[0]['long'][0]:.2f}/{wl[1]['long'][0]:.2f}, short decile "
                      f"{wl[0]['short'][0]:.2f}/{wl[1]['short'][0]:.2f}; rank IC by amt30 quintile (Q1 least active): train "
                      + " ".join(f"{r['rank_ic']:+.4f}" for r in ci[0]) + "  valid "
                      + " ".join(f"{r['rank_ic']:+.4f}" for r in ci[1]) + "\n"
                      f"{'':<6}long leg = location + selection: "
                      + " / ".join(f"{ann(d[i]['long'][0]):+.1f} = {ann(d[i]['long'][1]):+.1f} + {ann(d[i]['long'][2]):+.1f}"
                                   for i in range(2))
                      + "; short leg: "
                      + " / ".join(f"{ann(d[i]['short'][0]):+.1f} = {ann(d[i]['short'][1]):+.1f} + {ann(d[i]['short'][2]):+.1f}"
                                   for i in range(2)), flush=True)
            return [ic[0]["rank_ic"], ic[1]["rank_ic"]]

        # daily descriptors of where the stock sits, for the cells of section F
        kf = np.asarray(RAW["kfrac"], dtype=np.float64)
        amd = np.asarray(st.control("ctl_amt")[ut], dtype=np.float64)       # log(1 + that day's turnover)
        base_d = np.asarray(RAW["base"], dtype=np.float64)
        okd = np.isfinite(amd) & np.isfinite(kf)

        def split_cells(n_amt, n_k, mu=None, n_mu=4):
            qd = bucket(amd, okd, n_amt)
            wk_, _ = wb_rank(np.where(okd, kf, np.nan), qd, n_amt)
            c = qd * n_k + np.minimum(np.floor(wk_ * n_k), n_k - 1)
            if mu is None:
                return cells(c)
            # third key: 0 for names with no overwritten minute, else 1 + bucket of mu inside the (amt, k) cell
            has = okd & np.isfinite(mu) & (kf > 0)
            wm, _ = wb_rank(np.where(has, mu, np.nan), np.where(has, c, np.nan), n_amt * n_k)
            third = np.where(has, 1 + np.minimum(np.floor(wm * n_mu), n_mu - 1), 0.0)
            return cells(np.where(okd, c * (n_mu + 1) + third, np.nan))

        def section_f(label, xd, cell, full=True):
            fit, dev = cell_split(xd, cell)
            v_all = np.nanvar(np.where(np.isfinite(fit), xd, np.nan), axis=1)
            v_fit = np.nanvar(fit, axis=1)
            tot = np.asarray(bk.smoothed(-np.where(np.isfinite(fit), xd, np.nan), 20), dtype=np.float64)
            s_fit = np.asarray(bk.smoothed(-fit, 20), dtype=np.float64)
            s_dev = np.asarray(bk.smoothed(-dev, 20), dtype=np.float64)
            del fit, dev
            print(f"\n[{label}] cells per day {ncell(cell):.0f}; daily cross-sectional variance of the original explained by "
                  f"the cell mean {np.nanmean(v_fit / np.where(v_all > 0, v_all, np.nan)):.3f}\n"
                  f"   rank corr of the traded parts (train/valid): total~original {row_corr(tot[tr], SM['base'][tr]):+.2f}/"
                  f"{row_corr(tot[va], SM['base'][va]):+.2f}, cell~total {row_corr(s_fit[tr], tot[tr]):+.2f}/"
                  f"{row_corr(s_fit[va], tot[va]):+.2f}, deviation~total {row_corr(s_dev[tr], tot[tr]):+.2f}/"
                  f"{row_corr(s_dev[va], tot[va]):+.2f}, cell~deviation {row_corr(s_fit[tr], s_dev[tr]):+.2f}/"
                  f"{row_corr(s_fit[va], s_dev[va]):+.2f}, cell~amt30 {row_corr(s_fit[tr], a30[tr]):+.2f}/"
                  f"{row_corr(s_fit[va], a30[va]):+.2f}, deviation~amt30 {row_corr(s_dev[tr], a30[tr]):+.2f}/"
                  f"{row_corr(s_dev[va], a30[va]):+.2f}, deviation~bk {row_corr(s_dev[tr], SM['bk'][tr]):+.2f}/"
                  f"{row_corr(s_dev[va], SM['bk'][va]):+.2f}, cell~bk {row_corr(s_fit[tr], SM['bk'][tr]):+.2f}/"
                  f"{row_corr(s_fit[va], SM['bk'][va]):+.2f}", flush=True)
            ref = fixed("total (cell + deviation), EMA-20", tot)
            fixed("cell-mean part, EMA-20", s_fit)
            fixed("deviation part, EMA-20", s_dev)
            zc, zd = z32(s_fit), z32(s_dev)
            line("total | bk, amt30 (linear)", tot, [Z["bk"], Z["a"]], [], ref)
            line("total | bk, amt30, cell part", tot, [Z["bk"], Z["a"], zc], [], ref)
            line("total | bk, grid(30d), cell part", tot, [Z["bk"], zc], [Gak], ref, extra=True)
            line("total | cell part", tot, [zc], [], ref)
            rd = line("deviation part", s_dev)
            line("deviation part | bk", s_dev, [Z["bk"]], [], rd)
            line("deviation part | bk, bc, grid(30d)", s_dev, [Z["bk"], Z["bc"]], [Gak], rd, extra=True)
            if full:
                rf = line("cell part", s_fit)
                line("cell part | amt30 (linear)", s_fit, [Z["a"]], [], rf)
                line("cell part | grid(30d)", s_fit, [], [Gak], rf, extra=True)
                rb_ = line("bk", SM["bk"])
                line("bk | deviation part", SM["bk"], [zd], [], rb_)
                line("bk | deviation part, cell part", SM["bk"], [zd, zc], [], rb_)
                line("bk | total, grid(30d)", SM["bk"], [z32(tot)], [Gak], rb_)

        def section_e():
            hdr("E. where the label convention bites")
            for sname, sl in splits:
                lk = locked[sl]
                print(f"[{sname}] locked cells {lk.mean() * 100:.3f}% of all; mean raw label on them "
                      f"{np.nanmean(traw[sl][lk]) * 1e4:+.0f} bp", flush=True)
            bkr = np.asarray(RAW["bk"], dtype=np.float64)
            print("\ndouble sort: rows = amt30 quintile (L1 least active), columns = concentration (bk) quintile inside the row "
                  "(B5 most concentrated); next-day excess, annualised %.\n(a) buyable label, locked names left out (x2 section 3; "
                  "self-check train L1 21.0 17.0 12.9 9.0 -6.8, L5 2.5 -1.4 -5.1 -13.7 -44.7)\n(b) raw label, locked names in with "
                  "what they actually returned\n(c) share of the cell's names that are locked, %")
            for sname, sl in splits:
                a, b, tb, trw, lk = a30[sl], bkr[sl], tgt[sl], traw[sl], locked[sl]
                for lab, t_use in (("a buyable", tb), ("b raw", trw)):
                    ok = np.isfinite(a) & np.isfinite(b) & np.isfinite(t_use)
                    ex = np.where(ok, t_use, np.nan)
                    ex = ex - np.nanmean(ex, axis=1, keepdims=True)
                    qa = bucket(a, ok, 5)
                    print(f"[{sname}] ({lab})" + ("  | (c) locked %" if lab == "b raw" else ""))
                    for i in range(5):
                        row = ok & (qa == i)
                        qb = bucket(b, row, 5)
                        cs = [cell_ann(ex, row & (qb == j)) for j in range(5)]
                        txt = f"   L{i + 1} " + " ".join(f"{c:7.1f}" for c in cs) + f"   B1-B5 {cs[0] - cs[4]:6.1f}"
                        if lab == "b raw":
                            txt += "  | " + " ".join(f"{lk[row & (qb == j)].mean() * 100:5.2f}" for j in range(5))
                        print(txt, flush=True)
            print("\neach short decile split by amt30 quintile (Q1 least active): share of the decile | locked % | contribution to "
                  "the short-leg excess under the buyable label (locked = 0) -> under the raw label (annualised %, sums to the leg)")
            for n in ("base", "bk", "bc", "wk20", "wc20"):
                for sname, sl in splits:
                    s, tb, trw, lk, a = SM[n][sl], tgt[sl], traw[sl], locked[sl], a30[sl]
                    w = long_short_weights(s, TOP)
                    sh = w < 0
                    k = sh.sum(1)
                    fin = np.isfinite(s)
                    okb = fin & np.isfinite(tb)
                    rb = np.where(okb, tb, 0.0)
                    ew = np.where(okb.sum(1) > 0, rb.sum(1) / np.maximum(okb.sum(1), 1), np.nan)
                    rr = np.where(np.isfinite(trw), trw, 0.0)
                    qa = bucket(a, fin & np.isfinite(a), 5)
                    out, tb_, tr2_ = [], 0.0, 0.0
                    for i in range(5):
                        m = sh & (qa == i)
                        cb = ann(np.where(k > 0, ((ew[:, None] - rb) * m).sum(1) / np.maximum(k, 1), np.nan))
                        cr = ann(np.where(k > 0, ((ew[:, None] - rr) * m).sum(1) / np.maximum(k, 1), np.nan))
                        tb_, tr2_ = tb_ + cb, tr2_ + cr
                        out.append(f"Q{i + 1} {m.sum() / max(sh.sum(), 1):.0%} lk {lk[m].mean() * 100 if m.any() else 0:.2f}% "
                                   f"{cb:+.1f}->{cr:+.1f}")
                    print(f"{n:>6} [{sname}] " + " | ".join(out) + f" | total {tb_:+.1f}->{tr2_:+.1f}", flush=True)
            # how old are the locked names in the least-active part of the bucket-neutral short decile?
            first = np.argmax(np.isfinite(base_d), axis=0)                 # first row with a daily value = listing proxy
            age = np.arange(base_d.shape[0])[:, None] - first[None, :]
            for n in ("wk20", "bk"):
                w = long_short_weights(SM[n], TOP)
                fin = np.isfinite(SM[n])
                qa = bucket(a30, fin & np.isfinite(a30), 5)
                late = (np.arange(base_d.shape[0]) >= 250)[:, None]
                m = (w < 0) & locked & late
                m1 = m & (qa == 0)
                if m.any():
                    print(f"{n:>6}: locked names in the short decile (rows >= 250): {int(m.sum())} cells, of which in the least-"
                          f"active quintile {m1.sum() / m.sum():.0%}; share first seen < 120 rows earlier {np.mean(age[m] < 120):.0%} "
                          f"(least-active quintile only: {np.mean(age[m1] < 120) if m1.any() else float('nan'):.0%}); mean raw "
                          f"label {np.nanmean(traw[m]) * 1e4:+.0f} bp", flush=True)

        def section_g():
            hdr("G. reverse spanning (rev1 stopped here): does a conditioned concentration reading carry anything the original + "
                "liquidity does not?   rev1 already has: bk | base, amt30 -> +0.0096/+0.0005; bk | base, grid -> -0.0015/-0.0090; "
                "bk | grid -> +0.0121/-0.0013")
            for dep in ("bk", "bc", "wk20", "wc20"):
                ref = line(dep, SM[dep])
                line(f"{dep} | grid(30d)", SM[dep], [], [Gak], ref)
                line(f"{dep} | base, amt30 (linear)", SM[dep], [Z["base"], Z["a"]], [], ref)
                line(f"{dep} | base, grid(30d)", SM[dep], [Z["base"]], [Gak], ref)
                print()
            ref = line("base", SM["base"])
            line("base | grid(30d)", SM["base"], [], [Gak], ref)
            for dep in ("wk20", "wc20"):
                line(f"base | {dep}, grid(30d)", SM["base"], [z32(SM[dep])], [Gak], ref)

        print("\nbucket-neutral original vs bucket-neutral own kurtosis (both books, legs, raw-label short):", flush=True)
        run(fixed, "original EMA-20, in-ventile rank", SM["wbE20"])
        run(fixed, "kurt30, in-ventile rank (wk20)", SM["wk20"])

        hdr("F. exact split of the ORIGINAL's daily panel into a cell mean and a deviation; both smoothed with the original's "
            "EMA-20.  self-check: 'total | bk, amt30 (linear)' must reproduce rev1's base | bk, amt30 -> rIC +0.0147/+0.0078")
        print(f"share of stock-days with no minute overwritten {np.nanmean(np.where(okd, kf == 0, np.nan)):.1%}; daily "
              f"Spearman(kfrac, turnover) {row_corr(kf[tr], amd[tr]):+.2f}" + (f"; note: utrain starts at row {off}" if off else ""),
              flush=True)
        cA = split_cells(20, 10)
        run(section_f, "raw values; cell = turnover ventile x k decile", base_d, cA, True)
        run(section_e)
        try:
            inj = np.asarray(st.panels({"inj": f"div(day_sum({MASK}), day_sum(Amt))"})["inj"][ut], dtype=np.float64)
            mu = (inj - 1.0) * np.expm1(amd) / np.where(kf > 0, kf * 241.0, np.nan)   # amount injected per overwritten minute
            del inj
            cB = split_cells(10, 5, mu, 4)
            run(section_f, "raw values; cell = turnover decile x k quintile x injected-per-minute quartile", base_d, cB, False)
            del cB, mu
        except Exception:
            print(f"\n!!! three-key split failed:\n{traceback.format_exc()}", flush=True)
        run(section_f, "within-day ranks; cell = turnover ventile x k decile", pct_rank(base_d), cA, False)
        del cA
        run(section_g)
        try:
            from partura import guard
            print(f"\nanon of this process at the end: {guard.self_anon_gb():.2f} GiB", flush=True)
        except Exception:
            pass
    print("\n[rev2 done]")


if __name__ == "__main__":
    main()
