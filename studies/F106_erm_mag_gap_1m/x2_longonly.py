"""x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

x1 said the tree is a memory of locked limit-board days and that no construction of it has a positive
long leg.  The one use left for a long-only book is as an EXCLUSION: do not hold the names this factor
flags.  That is only worth something if the book one would hold anyway (the known family,
cross_mean(day_std(Amt), 30) / cross_max(day_std(Amt), 9)) actually contains such names and loses on them.

  1. the known family's long decile: how many of its names are flagged, and how do the flagged ones do
  2. overlay: the known signal with flagged names pushed to the bottom -- long leg before / after
  3. sum and residual: rank(known) + w * rank(F106 signal); F106 signal neutralised on the known family
  4. what is left of the F106 signal after neutralising on plain "recent limit-up" variables
  5. the same event read with an explicit, shorter memory (the effect lasts ~20 days, EMA-20 keeps it a year)

Only utrain rows are touched.  `python x2_longonly.py selftest` runs the numeric routines on random arrays.
"""
import os
import sys
import warnings

import numpy as np

warnings.filterwarnings("ignore")
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import x1_anatomy as x1  # noqa: E402  (helpers + the expressions, already cached on the server)

FID = x1.FID
hdr = x1.hdr


def push_down(sig, flag):
    """The signal with flagged cells moved below every unflagged cell of that day (they can still be
    shorted, they are still in the benchmark; they just cannot be in the long decile)."""
    s = np.array(sig, dtype=np.float64)
    fin = np.isfinite(s)
    with np.errstate(invalid="ignore"):
        lo = np.nanmin(np.where(fin, s, np.nan), axis=1, keepdims=True)
        hi = np.nanmax(np.where(fin, s, np.nan), axis=1, keepdims=True)
    span = np.where(np.isfinite(hi - lo) & (hi > lo), hi - lo, 1.0)
    out = np.where(fin & flag, s - 2.0 * span, s)
    return out


def top_decile(sig):
    """bool (D,S): the long decile exactly as long_short_weights takes it (ties by symbol order)."""
    from alphacube.metrics import long_short_weights
    return long_short_weights(np.asarray(sig, dtype=np.float64), 0.10) > 0


def row_str(r):
    return (f"Lnet {r['long_ann'] * 100:+6.1f}%  Lshp {r['long_sharpe']:+5.2f}  Lgross {r['long_gross_ann'] * 100:+6.1f}%  "
            f"LTO {r['long_turnover'] * 100:4.1f}%  LS {r['ls_sharpe']:+5.2f}  short {r['short_gross_ann'] * 100:+6.1f}%")


def main():
    from partura.study_tools import Study, bk, dg
    x1._RANK[0] = dg.rank_rows
    with Study(FID) as st:
        need = {k: x1.EX[k] for k in ("x", "R", "L", "cl", "hi", "lo")}
        P = {k: np.asarray(v, dtype=np.float64) for k, v in st.panels(need).items()}
        ut, tr, va = st.slice("utrain"), st.slice("train"), st.slice("valid")
        n = ut.stop
        tgt_full = st.target()
        rev1 = np.asarray(st.control("ctl_rev1"), dtype=np.float64)
        known = {"known30": np.asarray(st.control("known_stdamt_mean30"), dtype=np.float64),
                 "known9": np.asarray(st.control("known_stdamt_max9"), dtype=np.float64)}
        splits = {"train": tr, "valid": va}

        x = P["x"]
        fin = np.isfinite(x)
        sgn = st.sign(x, "train")
        s106 = bk.smoothed(sgn * x, 20)                              # the traded F106 signal (S0: sign -, hl 20)
        lim = x1.limit_flags(P["cl"], P["hi"], P["lo"], rev1)
        blown = fin & (np.abs(x) >= 5)
        finc = np.isfinite(P["cl"][:n])
        first_day = np.where(finc.any(0), finc.argmax(0), n + 1)
        age = np.arange(x.shape[0])[:, None] - first_day[None, :]
        newl = (first_day[None, :] > 20) & (age < 250) & (age >= 0)
        dec106 = x1.decile_of(s106)
        flags = {
            "blown day within 20d": x1.rolling_any(blown, 20),
            "blown day within 60d": x1.rolling_any(blown, 60),
            "limit-up close within 20d": x1.rolling_any(lim["up"], 20),
            "limit-up close within 60d": x1.rolling_any(lim["up"], 60),
            "limit-up or -down within 20d": x1.rolling_any(lim["up"] | lim["dn"], 20),
            "F106 signal decile 1 (short end)": dec106 == 0,
            "F106 signal decile 1 or 10": (dec106 == 0) | (dec106 == 9),
            "|F106 signal| >= 5": np.isfinite(s106) & (np.abs(s106) >= 5),
            "listed < 250d": newl,
        }

        for kname, kp in known.items():
            hdr(f"known family {kname}: its own books, then the long decile's anatomy and the exclusion overlays")
            b = st.books(kp, fit="train", evals=("train", "valid"))
            ksgn = st.sign(kp, "train")
            hl = b["hl_long"]
            ks = bk.smoothed(ksgn * kp, hl)
            base = {sp: bk.book_row(ks, tgt_full, d) for sp, d in splits.items()}
            print(f"{kname}: sign {ksgn:+.0f}, hl_long {hl:g}")
            for sp in splits:
                print(f"  {sp}: {row_str(base[sp])}")
            print(f"  rank corr with the F106 signal (train): {dg.pair_rank_corr(ks[tr], s106[tr]):+.3f};  "
                  f"with |pct(F106) - 0.5| (fold): {dg.pair_rank_corr(ks[tr], np.abs(x1.pct_rank(s106[:n]) - 0.5)[tr]):+.3f}")
            top = top_decile(ks)
            ex = x1.excess(tgt_full[:n], np.isfinite(ks[:n]))
            print(f"\n  {'flag':<34} {'split':<6} {'share of long decile':>21} {'share of universe':>18} {'flagged ex':>11} {'unflagged ex':>13}")
            for fname, fl in flags.items():
                for sp, d in splits.items():
                    sel_top = np.zeros((n, x.shape[1]), dtype=bool)
                    sel_top[d] = top[d]
                    uni = np.zeros_like(sel_top)
                    uni[d] = np.isfinite(ks[d])
                    f_ = fl[:n]
                    sh = (sel_top & f_).sum() / max(sel_top.sum(), 1)
                    shu = (uni & f_).sum() / max(uni.sum(), 1)
                    e1 = x1.ann(x1.cell_mean_by_day(ex, sel_top & f_))
                    e0 = x1.ann(x1.cell_mean_by_day(ex, sel_top & ~f_))
                    print(f"  {fname:<34} {sp:<6} {sh:21.3f} {shu:18.3f} {e1 * 100:+10.1f}% {e0 * 100:+12.1f}%")
            print(f"\n  overlay: {kname} with flagged names pushed out of the long decile (same sign, same half-life, no refit)")
            print(f"  {'(no exclusion)':<34} train {row_str(base['train'])}")
            print(f"  {'':<34} valid {row_str(base['valid'])}")
            for fname, fl in flags.items():
                so = push_down(ks, fl)
                for sp, d in splits.items():
                    r = bk.book_row(so, tgt_full, d)
                    print(f"  {fname if sp == 'train' else '':<34} {sp:<5} {row_str(r)}  dLnet {100 * (r['long_ann'] - base[sp]['long_ann']):+5.2f}")

            hdr(f"{kname}: sum and residual with the F106 signal")
            zk = x1.pct_rank(ks[:n]) - 0.5
            z6 = x1.pct_rank(s106[:n]) - 0.5
            for w in (0.25, 0.5, 1.0):
                z = zk + w * z6
                print(f"  rank({kname}) + {w:g} x rank(F106): " + "  |  ".join(
                    f"{sp} {row_str(bk.book_row(z, tgt_full[:n], d))}" for sp, d in splits.items()))
            zf = -np.abs(z6)                                          # "not at either end of F106"
            for w in (0.25, 0.5, 1.0):
                z = zk + w * 2.0 * (zf + 0.25)
                print(f"  rank({kname}) + {w:g} x (-fold F106): " + "  |  ".join(
                    f"{sp} {row_str(bk.book_row(z, tgt_full[:n], d))}" for sp, d in splits.items()))
            res, info = dg.neutralise(s106[:n], {kname: ks[:n]})
            print(f"  F106 signal neutralised on {kname}: R2 {info['mean_r2']:.3f}; residual: " + "  |  ".join(
                f"{sp} {row_str(bk.book_row(res, tgt_full[:n], d))}" for sp, d in splits.items()))
            resk, infok = dg.neutralise(ks[:n], {"f106": s106[:n], "fold": np.abs(z6)})
            print(f"  {kname} neutralised on F106 signal and its fold: R2 {infok['mean_r2']:.3f}; residual: " + "  |  ".join(
                f"{sp} {row_str(bk.book_row(resk, tgt_full[:n], d))}" for sp, d in splits.items()))

        hdr("4. what is left of the F106 signal after neutralising on plain recent-limit-up variables (rank space)")
        with np.errstate(invalid="ignore", divide="ignore"):
            max30 = np.asarray(st.control("g_max30"), dtype=np.float64)[:n]
            lu30 = np.asarray(st.control("g_limitup30"), dtype=np.float64)[:n]
        b20 = bk.smoothed(blown.astype(np.float64), 20)[:n]
        b20 = np.where(np.isfinite(s106[:n]), b20, np.nan)
        lu20e = bk.smoothed(np.where(fin, lim["up"].astype(np.float64), np.nan), 20)[:n]
        base6 = {sp: bk.book_row(s106[:n], tgt_full[:n], d) for sp, d in splits.items()}
        print("  F106 signal: " + "  |  ".join(f"{sp} {row_str(base6[sp])} rIC {dg.ic_row(s106[:n][d], tgt_full[:n][d])['rank_ic']:+.4f}" for sp, d in splits.items()))
        sets = {"g_max30": {"max30": max30}, "g_limitup30": {"lu30": lu30}, "EMA20(limit-up close flag)": {"lu20e": lu20e},
                "EMA20(blown flag)": {"b20": b20},
                "all four": {"max30": max30, "lu30": lu30, "lu20e": lu20e, "b20": b20}}
        for name, ctrl in sets.items():
            res, info = dg.neutralise(s106[:n], ctrl)
            print(f"  on {name:<28} R2 {info['mean_r2']:.3f}  residual: " + "  |  ".join(
                f"{sp} {row_str(bk.book_row(res, tgt_full[:n], d))} rIC {dg.ic_row(res[d], tgt_full[:n][d])['rank_ic']:+.4f}" for sp, d in splits.items()))
        fold6 = np.abs(x1.pct_rank(s106[:n]) - 0.5)
        for name, ctrl in sets.items():
            _, info = dg.neutralise(fold6, ctrl)
            print(f"  fold of the F106 signal on {name:<28} R2 {info['mean_r2']:.3f}")

        hdr("5. the same events with an explicit, shorter memory (direction fitted on train; books as in the tables)")
        absx = np.where(fin, np.abs(x), np.nan)
        cons = {}
        for w in (10, 20, 40):
            c = np.cumsum(np.where(blown, 1.0, 0.0), axis=0)
            lag = np.zeros_like(c)
            lag[w:] = c[:-w]
            cons[f"count of blown days, last {w}d"] = np.where(fin, c - lag, np.nan)
            c2 = np.cumsum(np.where(lim["up"], 1.0, 0.0), axis=0)
            lag2 = np.zeros_like(c2)
            lag2[w:] = c2[:-w]
            cons[f"count of limit-up closes, last {w}d"] = np.where(np.isfinite(P["cl"]), c2 - lag2, np.nan)
        cons["log(1+|X|)"] = np.log1p(absx)
        cons["R + L"] = np.where(fin, P["R"] + P["L"], np.nan)
        cons["log(1+R+L)"] = np.log1p(np.where(fin, np.clip(P["R"] + P["L"], 0, None), np.nan))
        for name, pan in cons.items():
            x1.book_line(st, name, pan, s106, tr)
    print("\n[x2 done]")


def selftest():
    rng = np.random.default_rng(1)
    D, S = 60, 50
    s = rng.normal(size=(D, S))
    s[rng.random((D, S)) < 0.1] = np.nan
    fl = rng.random((D, S)) < 0.2
    o = push_down(s, fl)
    assert np.isnan(o[np.isnan(s)]).all()
    for t in range(D):
        f = np.isfinite(s[t])
        if (f & fl[t]).any() and (f & ~fl[t]).any():
            assert o[t][f & fl[t]].max() < o[t][f & ~fl[t]].min()          # every flagged cell below every unflagged one
    assert np.array_equal(o[~fl & np.isfinite(s)], s[~fl & np.isfinite(s)])
    # ordering among the unflagged names is untouched
    t = 5
    f = np.isfinite(s[t]) & ~fl[t]
    assert np.array_equal(np.argsort(o[t][f]), np.argsort(s[t][f]))
    print("x2 selftest OK")


if __name__ == "__main__":
    if "selftest" in sys.argv[1:]:
        selftest()
    else:
        main()
