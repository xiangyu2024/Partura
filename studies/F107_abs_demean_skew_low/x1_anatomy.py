"""x1 -- what  abs_(cs_demean(day_skew(Low)))  reads on REAL data, and where its long leg comes from.

No stock diagnostic answers these, and the stage plan depends on the answers:

  0. helper sources the `src` tool cannot show (common._skew), and two self-checks of this script
     (numpy |A - rowmean(A)| == the engine's panel;  numpy rolling nanmean == the engine's cross_mean)
  1. day_skew(Low) on real data: heavy tails, constant paths (+-1 / NaN garbage), tick-grid levels,
     pinned paths; how big the cross-sectional mean is next to the cross-sectional sd (does cs_demean matter?)
  2. event level (no smoothing): next-day excess by SIGNED demeaned-skew bucket -- is the fold symmetric,
     and how much sits in the tails?
  3. persistent level: decile profile of EMA-20 of the SIGNED demeaned skew, and of the traded signal
  4. fold / tail / statistic variants as books (all built in numpy from the same daily panels)
  5. time scale: rolling means of 10..241 days and EMA half-lives beyond the grid
  6. who sits in each decile of the traded signal
  7. known exposure, with fold-matched and tree-specific controls (rank-space R^2, residual IC / long gross)
  8. what a LONG-ONLY user gets on top of the known Amt-level family: residual, sum, double sort, exclusion
  9. the short leg with and without the "could not be bought" filter

Only utrain (= train + valid) rows are ever sliced; the holdout is never touched.
`x1_anatomy.py --mock` runs the whole script on random arrays (shape / NaN handling), no server needed.
"""
import inspect
import sys
import time
import traceback
import warnings

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402  (first: it caps the BLAS threads before numpy loads)

import numpy as np  # noqa: E402

MOCK = "--mock" in sys.argv[1:]

FID = "F107_abs_demean_skew_low"
BASE = "abs_(cs_demean(day_skew(Low)))"
EX = {
    "A":       "day_skew(Low)",
    "base":    BASE,
    "m30":     f"cross_mean({BASE}, 30)",
    "skC":     "day_skew(Close)",
    "skH":     "day_skew(High)",
    "skR":     "day_skew(Ret)",
    "kurtR":   "day_kurt(Ret)",
    "kurtL":   "day_kurt(Low)",
    "mxL":     "day_max(Low)",
    "mnL":     "day_min(Low)",
    "mdL":     "day_median(Low)",
    "meL":     "day_mean(Low)",
    "px":      "day_last(Close)",
    "pos":     "day_mean(is_gt0(Amt))",
    "mktcorr": "day_corr(Ret, nt_cs_mean(Ret))",
}
CTL = ("ctl_amt", "ctl_price", "ctl_ivol", "ctl_range", "ctl_rev1", "ctl_mom20", "ctl_dvol20", "ctl_cap", "ctl_turnrate")
KNOWN = ("known_stdamt_mean30", "known_stdamt_max9", "known_amt_max9", "known_ivol_max9")
T0 = time.time()


def hdr(s):
    print(f"\n======== {s} ========  [{time.time() - T0:.0f}s]", flush=True)


def f64(x):
    return np.asarray(x, dtype=np.float64)


def pct_rank(a):
    r = dg.rank_rows(f64(a))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def cs_dm(a):
    a = f64(a)
    return a - np.nanmean(a, axis=1, keepdims=True)


def spearman_days(a, b, mask=None, min_n=30):
    """Mean daily Spearman over the cells finite in both (and in `mask`)."""
    a = np.array(a, dtype=np.float64)
    b = np.array(b, dtype=np.float64)
    ok = np.isfinite(a) & np.isfinite(b)
    if mask is not None:
        ok &= mask
    a[~ok] = np.nan
    b[~ok] = np.nan
    ra, rb = dg.rank_rows(a), dg.rank_rows(b)
    n = ok.sum(1)
    ra = ra - np.nanmean(ra, axis=1, keepdims=True)
    rb = rb - np.nanmean(rb, axis=1, keepdims=True)
    num = np.nansum(ra * rb, axis=1)
    den = np.sqrt(np.nansum(ra * ra, axis=1) * np.nansum(rb * rb, axis=1))
    c = np.where((n >= min_n) & (den > 0), num / np.where(den > 0, den, 1), np.nan)
    return float(np.nanmean(c)) if np.isfinite(c).any() else float("nan")


def excess(tgt, universe):
    """label minus the equal-weight mean of the universe cells, per day."""
    t = np.where(universe & np.isfinite(tgt), tgt, np.nan)
    return t - np.nanmean(t, axis=1, keepdims=True)


def roll_mean(x, n):
    """Causal rolling nanmean with partial windows -- what cross_mean(x, n) does (NaN-padded window, nanmean)."""
    x = f64(x)
    fin = np.isfinite(x)
    c = np.cumsum(np.where(fin, x, 0.0), axis=0)
    k = np.cumsum(fin, axis=0).astype(np.float64)
    c2, k2 = c.copy(), k.copy()
    c2[n:] = c[n:] - c[:-n]
    k2[n:] = k[n:] - k[:-n]
    return np.where(k2 > 0.5, c2 / np.maximum(k2, 1.0), np.nan)


def ann(x):
    return float(np.nanmean(x) * 252 * 100)


HEAD = (f"{'variant':<34} sgn | {'hlL':>3} {'Lnet tr':>8} {'Lnet va':>8} {'Lshp tr':>7} {'Lshp va':>7} {'Lgro tr':>8} "
        f"{'Lgro va':>8} {'LTO':>6} | {'hlS':>3} {'LS tr':>6} {'LS va':>6} {'short tr':>8} | {'rho(base)':>9}")


def line(name, sg, b, rho=float("nan")):
    L, S = b["by_rank"]["long"], b["by_rank"]["ls"]
    lt, lv = L["splits"]["train"], L["splits"]["valid"]
    s_t, s_v = S["splits"]["train"], S["splits"]["valid"]
    print(f"{name:<34}  {'+' if sg > 0 else '-'}  | {L['hl']:>3g} {lt['long_ann'] * 100:+7.1f}% {lv['long_ann'] * 100:+7.1f}% "
          f"{lt['long_sharpe']:+7.2f} {lv['long_sharpe']:+7.2f} {lt['long_gross_ann'] * 100:+7.1f}% "
          f"{lv['long_gross_ann'] * 100:+7.1f}% {lt['long_turnover'] * 100:5.1f}% | {S['hl']:>3g} {s_t['ls_sharpe']:+6.2f} "
          f"{s_v['ls_sharpe']:+6.2f} {s_t['short_gross_ann'] * 100:+7.1f}% | {rho:+9.2f}", flush=True)


def row_at(sm, tgt, sl):
    return {k: bk.book_row(sm, tgt, sl[k]) for k in ("train", "valid")}


def line_fixed(name, r, rho=float("nan"), extra=""):
    t, v = r["train"], r["valid"]
    print(f"{name:<34} Lnet {t['long_ann'] * 100:+6.1f}% / {v['long_ann'] * 100:+6.1f}%   Lshp {t['long_sharpe']:+5.2f} / "
          f"{v['long_sharpe']:+5.2f}   Lgross {t['long_gross_ann'] * 100:+6.1f}% / {v['long_gross_ann'] * 100:+6.1f}%   "
          f"LTO {t['long_turnover'] * 100:4.1f}%   LS {t['ls_sharpe']:+5.2f} / {v['ls_sharpe']:+5.2f}   "
          f"short {t['short_gross_ann'] * 100:+6.1f}% / {v['short_gross_ann'] * 100:+6.1f}%"
          + (f"   rho(base) {rho:+.2f}" if np.isfinite(rho) else "") + extra, flush=True)


def section(fn):
    try:
        fn()
    except Exception:
        print("!! section failed:\n" + traceback.format_exc(), flush=True)


# ------------------------------------------------------------------------------------------------ mock
class FakeStudy:
    """Random panels with the real bk / dg code paths: exercises shapes and NaN handling only."""

    def __init__(self):
        self.rng = np.random.default_rng(0)
        self.D, self.S = 320, 300
        self._sl = {"train": slice(0, 180), "valid": slice(180, 260), "utrain": slice(0, 260)}
        self.dates = [f"{2018 + i // 110}{1 + (i % 110) // 30:02d}{1 + i % 28:02d}" for i in range(self.D)]
        self.symbols = [f"{i:06d}" for i in range(self.S)]
        t = self.rng.normal(0, 0.02, (self.D, self.S))
        t[self.rng.random((self.D, self.S)) < 0.03] = np.nan
        self._t = t
        self._tb = np.where(self.rng.random((self.D, self.S)) < 0.02, np.nan, t)
        self._cache = {}

    def __enter__(self):
        return self

    def __exit__(self, *a):
        return None

    def _rand(self, name):
        if name not in self._cache:
            g = np.random.default_rng(abs(hash(name)) % (2 ** 32))
            x = g.normal(0, 1, (self.D, self.S)).astype(np.float32)
            if name in ("mxL", "mnL", "mdL", "meL", "px"):
                base = 10 + np.cumsum(g.normal(0, .1, (self.D, self.S)), 0)
                off = {"mxL": .2, "mnL": -.2, "mdL": 0.0, "meL": .01, "px": .05}[name]
                x = (np.round((base + off) * 100) / 100).astype(np.float32)
            if name == "pos":
                x = np.clip(0.9 + 0.1 * x, 0, 1).astype(np.float32)
            if name == "ctl_rev1":
                x = (1 + 0.02 * x).astype(np.float32)
            x[g.random((self.D, self.S)) < 0.03] = np.nan
            self._cache[name] = x
        return self._cache[name]

    def panels(self, ex):
        out = {k: self._rand(k) for k in ex}
        if "A" in out and "base" in ex:
            a = out["A"].astype(np.float64)
            out["base"] = np.abs(a - np.nanmean(a, 1, keepdims=True)).astype(np.float32)
            self._cache["base"] = out["base"]
        if "m30" in ex:
            out["m30"] = roll_mean(out["base"], 30).astype(np.float32)
        return out

    def control(self, name):
        return self._rand(name)

    def target(self, horizon=1, buyable=None):
        return self._t if buyable is False else self._tb

    def slice(self, s):
        return self._sl[s]

    def sign(self, p, split="train"):
        s = self._sl[split]
        return dg.sign_from(f64(p)[s], self.target()[s])

    def books(self, p, fit="train", evals=("train", "valid"), sign=None):
        sg = self.sign(p, fit) if sign is None else sign
        return bk.books(sg * f64(p), self.target(), self._sl[fit], {e: self._sl[e] for e in evals}, rank_by="long")


# ------------------------------------------------------------------------------------------------ main
def show_sources():
    hdr("0. helper sources on the SERVER (the `src` tool does not unfold C._skew)")
    try:
        from alphacube.operators import common as C
        for label in ("_skew", "_mean", "_stddev", "div"):
            fn = getattr(C, label, None)
            if fn is None:
                print(f"# common.{label}: not found")
                continue
            try:
                print(f"# common.{label}\n{inspect.getsource(inspect.unwrap(fn))}")
            except Exception as exc:
                print(f"# common.{label}: source unavailable ({exc})")
        print(f"# common.EPS = {getattr(C, 'EPS', None)}")
    except Exception as exc:
        print(f"sources failed: {type(exc).__name__}: {exc}")


def main():
    if MOCK:
        st_cm = FakeStudy()
    else:
        show_sources()
        st_cm = Study(FID)
    with st_cm as st:
        P = st.panels(EX)
        miss = [k for k in EX if k not in P]
        if miss:
            print("MISSING panels:", miss, flush=True)
        ut, tr, va = st.slice("utrain"), st.slice("train"), st.slice("valid")
        sl = {"train": tr, "valid": va}
        tgt = st.target()
        ctl = {n: f64(st.control(n)) for n in CTL}
        known = {n: f64(st.control(n)) for n in KNOWN}
        dates = np.asarray(st.dates)
        A = f64(P["A"])
        base = f64(P["base"])
        Bs = cs_dm(A)                       # signed demeaned skew, numpy
        absB = np.abs(Bs)
        finB = np.isfinite(absB)
        mx, mn, md, me = (f64(P[k]) if k in P else None for k in ("mxL", "mnL", "mdL", "meL"))
        px = f64(P["px"]) if "px" in P else None
        have_lv = all(v is not None for v in (mx, mn, md, me, px))
        if have_lv:
            const = np.isfinite(mx) & (mx == mn)
            pin_hi = np.isfinite(mx) & (mx > mn) & (md == mx)          # >= half the minutes AT the day's highest Low
            pin_lo = np.isfinite(mx) & (mx > mn) & (md == mn)
            pinned = const | pin_hi | pin_lo
            ticks = np.rint((mx - mn) / 0.01)                          # tick steps spanned, if prices are raw (checked in 1)
        r1 = ctl["ctl_rev1"] - 1.0                                     # close-to-close return of day t

        SIG = {}                                                       # name -> (sign, books, traded signal)
        base_sg = st.sign(base, "train")
        base_b = st.books(base, fit="train", evals=("train", "valid"), sign=base_sg)
        base_sm = bk.smoothed(base_sg * base, base_b["by_rank"]["long"]["hl"])

        def book(name, panel, show=True, keep=False):
            p = f64(panel)
            sg = st.sign(p, "train")
            b = st.books(p, fit="train", evals=("train", "valid"), sign=sg)
            sm = bk.smoothed(sg * p, b["by_rank"]["long"]["hl"])
            rho = spearman_days(sm[tr], base_sm[tr])
            if show:
                line(name, sg, b, rho)
            if keep:
                SIG[name] = (sg, b, sm)
            return sg, b, sm

        # ---------------------------------------------------------------- 0b
        def s0():
            hdr("0b. self-checks of this script against the engine")
            d = np.abs(absB[ut] - base[ut])
            both = np.isfinite(absB[ut]) & np.isfinite(base[ut])
            print(f"numpy |A - rowmean(A)| vs engine panel: finite pattern equal = "
                  f"{bool((np.isfinite(absB[ut]) == np.isfinite(base[ut])).all())}; max abs diff = {float(np.nanmax(d[both])):.3g}; "
                  f"Spearman = {spearman_days(absB[ut], base[ut]):.5f}")
            if "m30" in P:
                e = f64(P["m30"])[ut]
                m = roll_mean(base, 30)[ut]
                both = np.isfinite(e) & np.isfinite(m)
                late = slice(60, None)
                print(f"numpy roll_mean(base, 30) vs engine cross_mean(base, 30): max abs diff after row 60 = "
                      f"{float(np.nanmax(np.abs(e[late] - m[late])[both[late]])):.3g}; finite-pattern mismatch share = "
                      f"{float((np.isfinite(e) != np.isfinite(m)).mean()):.5f}; Spearman = {spearman_days(e, m):.5f}")
            print(f"sign fitted on train for the base panel: {base_sg:+.0f}; hlL = {base_b['by_rank']['long']['hl']}, "
                  f"hlS = {base_b['by_rank']['ls']['hl']}")
            print(HEAD)
            line("base (st.books; must match S0)", base_sg, base_b, 1.0)
        section(s0)

        # ---------------------------------------------------------------- 1
        def s1():
            hdr("1. day_skew(Low) on real data (utrain rows)")
            a, lab = A[ut], np.isfinite(tgt[ut])
            fin = np.isfinite(a)
            print(f"cells with a label: {int(lab.sum())}; of those, A finite: {float((fin & lab).sum() / lab.sum()):.4f}")
            v = a[fin]
            qs = (0.001, 0.01, 0.05, 0.25, 0.5, 0.75, 0.95, 0.99, 0.999)
            print("quantiles of A (signed skew):   " + "  ".join(f"q{q:g}={np.quantile(v, q):+.2f}" for q in qs))
            vb = absB[ut][finB[ut]]
            print("quantiles of |B| = |A - mean|:  " + "  ".join(f"q{q:g}={np.quantile(vb, q):.2f}" for q in (0.1, 0.25, 0.5, 0.75, 0.9, 0.95, 0.99, 0.999)))
            print("share of finite cells with |B| >= 0.5 / 1 / 1.5 / 2 / 3 / 5:  "
                  + "  ".join(f"{float((vb >= c).mean()):.4f}" for c in (0.5, 1, 1.5, 2, 3, 5)))
            print(f"share of finite cells with |A| within 1e-3 of exactly 1 (constant-path float garbage): "
                  f"{float((np.abs(np.abs(v) - 1.0) < 1e-3).mean()):.5f}")
            tot = float(np.nansum(vb))
            print("share of the cross-sectional SUM of |B| carried by cells with |B| >= 1 / 2 / 3:  "
                  + "  ".join(f"{float(vb[vb >= c].sum() / tot):.3f}" for c in (1, 2, 3)))
            mu = np.nanmean(a, axis=1)
            sd = np.nanstd(a, axis=1)
            ratio = np.abs(mu) / sd
            print("per-day cross-sectional mean of A:  " + "  ".join(f"q{q:g}={np.quantile(mu, q):+.3f}" for q in (0.05, 0.25, 0.5, 0.75, 0.95)))
            print("per-day cross-sectional sd of A:    " + "  ".join(f"q{q:g}={np.quantile(sd, q):.3f}" for q in (0.05, 0.25, 0.5, 0.75, 0.95)))
            print("per-day |mean| / sd:                " + "  ".join(f"q{q:g}={np.quantile(ratio, q):.3f}" for q in (0.25, 0.5, 0.75, 0.9, 0.99))
                  + f"   share of days > 0.25: {float((ratio > 0.25).mean()):.3f}, > 0.5: {float((ratio > 0.5).mean()):.3f}")
            print(f"daily Spearman(|A - mean|, |A|): mean {spearman_days(absB[ut], np.abs(a)):.3f}")
            print(f"daily Spearman(EMA20 |A - mean|, EMA20 |A|) on train: "
                  f"{spearman_days(bk.smoothed(absB, 20)[tr], bk.smoothed(np.abs(A), 20)[tr]):.3f}")
            if not have_lv:
                return
            p = px[ut][np.isfinite(px[ut])]
            print(f"prices raw? share of day_last(Close) within 1e-3 of a 0.01 grid: "
                  f"{float((np.abs(p * 100 - np.rint(p * 100)) < 1e-1).mean()):.4f}  (median price {np.median(p):.2f})")
            tk = ticks[ut]
            print(f"{'tick steps spanned by Low':>26} {'share':>7} {'mean |A|':>9} {'median |A|':>10} {'A NaN share':>11} {'mean |B|':>9}")
            cells = np.isfinite(tk) & lab
            for lo, hi in ((0, 0), (1, 1), (2, 2), (3, 4), (5, 9), (10, 19), (20, 49), (50, 99), (100, 10 ** 9)):
                m = cells & (tk >= lo) & (tk <= hi)
                if m.sum() == 0:
                    continue
                aa = np.abs(a[m])
                print(f"{(str(lo) if lo == hi else f'{lo}-{hi}' if hi < 10 ** 8 else f'>={lo}'):>26} {m.sum() / cells.sum():7.4f} "
                      f"{np.nanmean(aa):9.3f} {np.nanmedian(aa):10.3f} {float(np.isnan(a[m]).mean()):11.3f} {np.nanmean(absB[ut][m]):9.3f}")
            print(f"\n{'path type (utrain, labelled)':<44} {'share':>7} {'mean A':>8} {'mean |B|':>9} {'|B|>=2':>7} {'ret>9%':>7} {'ret<-9%':>8}")
            for nm, m0 in (("constant all day (max == min)", const), ("pinned high (median == max, not const)", pin_hi),
                           ("pinned low (median == min, not const)", pin_lo), ("everything else", ~pinned & np.isfinite(mx))):
                m = m0[ut] & lab
                if m.sum() == 0:
                    continue
                print(f"{nm:<44} {m.sum() / lab.sum():7.4f} {np.nanmean(a[m]):+8.2f} {np.nanmean(absB[ut][m]):9.2f} "
                      f"{float(np.nanmean(absB[ut][m] >= 2)):7.3f} {float(np.nanmean(r1[ut][m] > 0.09)):7.3f} {float(np.nanmean(r1[ut][m] < -0.09)):8.3f}")
            big = (absB[ut] >= 2) & lab
            print(f"of the cells with |B| >= 2 ({big.sum() / lab.sum():.4f} of labelled cells): pinned high {float(pin_hi[ut][big].mean()):.3f}, "
                  f"pinned low {float(pin_lo[ut][big].mean()):.3f}, constant {float(const[ut][big].mean()):.3f}; "
                  f"day return > 9%: {float((r1[ut][big] > 0.09).mean()):.3f}, < -9%: {float((r1[ut][big] < -0.09).mean()):.3f}; "
                  f"mean sign of B: {float(np.sign(Bs[ut][big]).mean()):+.2f}")
            yrs = np.array([int(str(d)[:4]) for d in dates[ut]])
            print("by year: mean |B|, share |B|>=2, share pinned(high/low/const), share <=2 tick steps")
            for y in sorted(set(yrs)):
                r = yrs == y
                m = lab[r]
                print(f"   {y}: mean|B| {np.nanmean(absB[ut][r][m]):.3f}  |B|>=2 {float(np.nanmean(absB[ut][r][m] >= 2)):.4f}  "
                      f"pinned {float(pinned[ut][r][m].mean()):.4f}  ticks<=2 {float((tk[r][m] <= 2).mean()):.4f}")
        section(s1)

        # ---------------------------------------------------------------- 2
        def s2():
            hdr("2. EVENT level (no smoothing): next-day excess by SIGNED B bucket (annualised %, vs equal-weight of scored names)")
            edges = [(-np.inf, -2), (-2, -1), (-1, -.5), (-.5, -.25), (-.25, 0), (0, .25), (.25, .5), (.5, 1), (1, 2), (2, np.inf)]
            rk_v, rk_a = pct_rank(ctl["ctl_dvol20"]), pct_rank(ctl["ctl_amt"])
            for name, s in sl.items():
                b = Bs[s]
                ex = excess(tgt[s], np.isfinite(b))
                ok = np.isfinite(ex)
                print(f"-- {name}:  {'B in':>14} {'share':>7} {'excess':>8} {'rk dvol20':>9} {'rk amt':>7} {'label NaN share':>28}")
                for lo, hi in edges:
                    m = (b > lo) & (b <= hi)
                    mo = m & ok
                    print(f"            {f'({lo:g}, {hi:g}]':>14} {mo.sum() / ok.sum():7.4f} {ann(ex[mo]):+7.1f}% "
                          f"{np.nanmean(rk_v[s][m]):9.2f} {np.nanmean(rk_a[s][m]):7.2f} {float(np.isnan(tgt[s][m]).mean()):28.4f}")
                if have_lv:
                    for nm, m0 in (("constant", const), ("pinned high", pin_hi), ("pinned low", pin_lo),
                                   ("other, |B|>=1", ~pinned & (absB >= 1)), ("other, |B|<1", ~pinned & (absB < 1))):
                        mo = m0[s] & ok
                        print(f"            {nm:>14} {mo.sum() / ok.sum():7.4f} {ann(ex[mo]):+7.1f}%")
        section(s2)

        # ---------------------------------------------------------------- 3
        def s3():
            hdr("3. PERSISTENT level: decile profiles (annualised excess %, D1..D10)")
            sm_signed = bk.smoothed(Bs, 20)
            sm_abs = bk.smoothed(-absB, 20)
            for name, s in sl.items():
                pr = bk.quantile_profile(sm_abs, tgt, s, n=10)
                print(f"-- {name}: traded signal EMA20(-|B|), D1 = short end:  " + " ".join(f"{r['excess_ann'] * 100:+6.1f}" for r in pr))
                pr = bk.quantile_profile(sm_signed, tgt, s, n=10)
                print(f"-- {name}: EMA20 of SIGNED B, D1 = most negative:      " + " ".join(f"{r['excess_ann'] * 100:+6.1f}" for r in pr))
                a_abs = pct_rank(np.where(np.isfinite(sm_abs[s]), -sm_abs[s], np.nan))        # high = large EMA |B|
                ex = excess(tgt[s], np.isfinite(sm_abs[s]))
                print(f"   {name}: cells by EMA20|B| rank x sign of EMA20 signed B:  (share, excess)")
                for lo, hi in ((0.9, 1.01), (0.7, 0.9), (0.3, 0.7), (0.0, 0.3)):
                    out = []
                    for sg_name, sgm in (("signed<0", sm_signed[s] < 0), ("signed>=0", sm_signed[s] >= 0)):
                        m = (a_abs >= lo) & (a_abs < hi) & sgm & np.isfinite(ex)
                        out.append(f"{sg_name}: {m.sum() / np.isfinite(ex).sum():.3f}, {ann(ex[m]):+6.1f}%")
                    print(f"      EMA|B| rank in [{lo:.1f}, {min(hi, 1):.1f}):  " + "   ".join(out))
        section(s3)

        # ---------------------------------------------------------------- 4
        def s4():
            hdr("4. fold / tail / statistic variants as books (sign + half-life fitted on train; rho = rank corr of traded signals with base, train)")
            med = np.nanmedian(absB, axis=1, keepdims=True)
            V = [("base |B| (engine panel)", base),
                 ("|A| (no cs_demean)", np.abs(A)),
                 ("signed B", Bs),
                 ("B+ = max(B, 0)", np.where(finB, np.maximum(Bs, 0), np.nan)),
                 ("B- = max(-B, 0)", np.where(finB, np.maximum(-Bs, 0), np.nan)),
                 ("B^2", Bs ** 2),
                 ("sqrt|B|", np.sqrt(absB)),
                 ("min(|B|, 1.0)", np.minimum(absB, 1.0)),
                 ("min(|B|, 0.6)", np.minimum(absB, 0.6)),
                 ("cs pct-rank of |B|", pct_rank(absB)),
                 ("1{|B| > 1}", np.where(finB, (absB > 1).astype(np.float64), np.nan)),
                 ("1{|B| > 2}", np.where(finB, (absB > 2).astype(np.float64), np.nan))]
            if have_lv:
                rng_ = np.where(mx > mn, mx - mn, np.nan)
                rs = (mx + mn - 2 * md) / rng_                         # range-based asymmetry in [-1, 1]
                mp = (me - mn) / rng_                                  # time-average position in the day's range
                V += [("|B|, pinned/const days -> cs median", np.where(pinned & finB, med, absB)),
                      ("|B| on pinned/const days, else 0", np.where(finB, np.where(pinned, absB, 0.0), np.nan)),
                      ("1{pinned or const}", np.where(np.isfinite(mx), pinned.astype(np.float64), np.nan)),
                      ("|dm (max+min-2med)/(max-min)|", np.abs(cs_dm(rs))),
                      ("|dm (mean-min)/(max-min)|", np.abs(cs_dm(mp)))]
            for k, nm in (("skC", "|dm day_skew(Close)|"), ("skH", "|dm day_skew(High)|"), ("skR", "|dm day_skew(Ret)|"),
                          ("kurtL", "day_kurt(Low)"), ("kurtR", "day_kurt(Ret)"), ("mktcorr", "day_corr(Ret, mkt Ret)")):
                if k in P:
                    V.append((nm, np.abs(cs_dm(P[k])) if k.startswith("sk") else f64(P[k])))
            print(HEAD)
            fixed = []
            for nm, p in V:
                sg, b, sm = book(nm, p, keep=True)
                if b["by_rank"]["long"]["hl"] != 20:
                    fixed.append((nm, sg, p))
            if fixed:
                print("-- the ones that did not choose hl 20, AT hl 20 (same smoothing as base):")
                for nm, sg, p in fixed:
                    sm = bk.smoothed(sg * f64(p), 20)
                    line_fixed(nm, row_at(sm, tgt, sl), spearman_days(sm[tr], base_sm[tr]))
        section(s4)

        # ---------------------------------------------------------------- 5
        def s5():
            hdr("5. time scale: rolling nanmean over N days (= cross_mean(., N)), half-life grid on top; then EMA beyond the grid")
            X = [("|B|", base), ("pct-rank|B|", pct_rank(absB)), ("min(|B|,1)", np.minimum(absB, 1.0))]
            print(HEAD)
            for xn, x in X:
                for n in (10, 20, 30, 60, 120, 241):
                    book(f"mean{n}({xn})", roll_mean(x, n), keep=(n in (60, 120)))
            print("-- EMA with a half-life outside the grid (sign from base; no further smoothing):")
            for xn, x in X[:2]:
                for hl in (20, 40, 60, 120):
                    sm = bk.smoothed(base_sg * f64(x), hl)
                    line_fixed(f"EMA{hl}({xn})", row_at(sm, tgt, sl), spearman_days(sm[tr], base_sm[tr]))
            print("-- rolling means AT fixed half-lives 0 / 20 (structure vs smoothing):")
            for n in (30, 60, 120):
                for hl in (0, 20):
                    sm = bk.smoothed(base_sg * roll_mean(base, n), hl)
                    line_fixed(f"mean{n}(|B|) @hl{hl}", row_at(sm, tgt, sl), spearman_days(sm[tr], base_sm[tr]))
        section(s5)

        # ---------------------------------------------------------------- 6
        def s6():
            hdr("6. who sits in each decile (D1 = short end, D10 = long end); mean within-day pct-rank of each characteristic")
            R = {n: pct_rank(c) for n, c in ctl.items()}
            R["known_stdamt_mean30"] = pct_rank(known["known_stdamt_mean30"])
            extra = {}
            if "kurtR" in P:
                extra["EMA20 kurt(Ret)"] = pct_rank(bk.smoothed(f64(P["kurtR"]), 20))
            if "mktcorr" in P:
                extra["EMA20 mktcorr"] = pct_rank(bk.smoothed(f64(P["mktcorr"]), 20))
            if have_lv:
                extra["EMA20 ticks"] = pct_rank(bk.smoothed(ticks, 20))
            recent_big = roll_mean((absB >= 2).astype(np.float64), 20) > 0          # any |B|>=2 day in the last 20
            recent_pin = (roll_mean(pinned.astype(np.float64), 20) > 0) if have_lv else None
            sigs = [("base, EMA20", base_sm)]
            if "mean60(|B|)" in SIG:
                sigs.append(("mean60(|B|) at its own hl", SIG["mean60(|B|)"][2]))
            for sname, sm_full in sigs:
                for name, s in sl.items():
                    sm = sm_full[s]
                    okc = np.isfinite(sm)
                    pr = pct_rank(np.where(okc, sm, np.nan))
                    dec = np.where(okc, np.minimum(np.floor(pr * 10), 9), np.nan)
                    ex = excess(tgt[s], okc)
                    cols = ["ctl_cap", "ctl_amt", "ctl_turnrate", "ctl_dvol20", "ctl_ivol", "ctl_price", "ctl_mom20", "ctl_rev1",
                            "known_stdamt_mean30"]
                    print(f"-- {sname} / {name}\n{'D':>3} {'excess':>8} " + " ".join(f"{c.replace('ctl_', '').replace('known_', 'k_')[:9]:>9}" for c in cols)
                          + " " + " ".join(f"{k[6:]:>10}" for k in extra) + f" {'|B|>=2 in 20d':>13} {'pinned in 20d':>13}")
                    for d in range(10):
                        m = dec == d
                        print(f"{d + 1:>3} {ann(ex[m]):+7.1f}% " + " ".join(f"{np.nanmean(R[c][s][m]):9.2f}" for c in cols)
                              + " " + " ".join(f"{np.nanmean(v[s][m]):10.2f}" for v in extra.values())
                              + f" {float(recent_big[s][m].mean()):13.3f} "
                              + (f"{float(recent_pin[s][m].mean()):13.3f}" if recent_pin is not None else f"{'-':>13}"))
        section(s6)

        # ---------------------------------------------------------------- 7
        def s7():
            hdr("7. known exposure of the traded signal EMA20(-|B|) on train: fold-matched and tree-specific controls")
            S = base_sm[tr]
            cand = {"EMA20 |dm rev1| (fold-matched)": bk.smoothed(np.abs(cs_dm(ctl["ctl_rev1"])), 20),
                    "EMA20 |dm mom20| (fold-matched)": bk.smoothed(np.abs(cs_dm(ctl["ctl_mom20"])), 20),
                    "EMA20 |dm log amt| (fold-matched)": bk.smoothed(np.abs(cs_dm(ctl["ctl_amt"])), 20),
                    "EMA20 1{|B|>=2}": bk.smoothed((absB >= 2).astype(np.float64), 20)}
            for k, nm in (("kurtR", "EMA20 day_kurt(Ret)"), ("kurtL", "EMA20 day_kurt(Low)"), ("mktcorr", "EMA20 mktcorr"),
                          ("pos", "EMA20 traded-minute share"), ("skR", "EMA20 |dm day_skew(Ret)|")):
                if k in P:
                    cand[nm] = bk.smoothed(np.abs(cs_dm(P[k])) if k == "skR" else f64(P[k]), 20)
            if have_lv:
                cand["EMA20 1{pinned or const}"] = bk.smoothed(np.where(np.isfinite(mx), pinned.astype(np.float64), np.nan), 20)
                cand["EMA20 log(1 + tick steps)"] = bk.smoothed(np.log1p(ticks), 20)
                cand["EMA20 1{|ret| > 9%}"] = bk.smoothed(np.where(np.isfinite(r1), (np.abs(r1) > 0.09).astype(np.float64), np.nan), 20)
            print("daily Spearman of the traded signal (long = small |B|) with:")
            for nm, c in list(cand.items()) + [(n, v) for n, v in ctl.items()] + [(n, v) for n, v in known.items()]:
                print(f"   {nm:<36} {spearman_days(S, c[tr]):+.3f}")
            yz = dg._zrank(S)
            Z = {n: dg._zrank(c[tr]) for n, c in ctl.items()}
            Zc = {n: dg._zrank(c[tr]) for n, c in cand.items()}

            def fit(nm, controls):
                resid, info = dg.neutralise(yz, controls, panel_ready=True, controls_ready=True)
                icr = dg.ic_row(resid, tgt[tr], sign=1.0)
                br = bk.book_row(resid, tgt[tr], slice(0, resid.shape[0]))
                print(f"   {nm:<58} R2 {info['mean_r2']:.3f}   resid rIC {icr['rank_ic']:+.4f}   resid Lgross {br['long_gross_ann'] * 100:+5.1f}%   "
                      f"resid short {br['short_gross_ann'] * 100:+5.1f}%   resid LTO {br['long_turnover'] * 100:4.1f}%")
            print("rank-space daily regressions of the traded signal (train):")
            fit("(a) the 9 shared controls [S0 says R2 0.214]", Z)
            sq = {f"{n}^2": (z ** 2 - np.nanmean(z ** 2, axis=1, keepdims=True)) for n, z in Z.items()}
            fit("(b) (a) + the square of each (non-monotone dependence)", {**Z, **sq})
            fit("(c) (a) + all tree-specific / fold-matched candidates", {**Z, **Zc})
            fit("(d) tree-specific / fold-matched candidates only", Zc)
            for nm in Zc:
                fit(f"    only {nm}", {nm: Zc[nm]})
            fit("(e) known_stdamt_mean30 only", {"k": dg._zrank(known["known_stdamt_mean30"][tr])})
            fit("(f) ctl_dvol20 + known_stdamt_mean30", {"v": Z["ctl_dvol20"], "k": dg._zrank(known["known_stdamt_mean30"][tr])})
        section(s7)

        # ---------------------------------------------------------------- 8
        def s8():
            hdr("8. what a LONG-ONLY user gets on top of the known Amt-level family")
            K = {}
            print(HEAD)
            for kn in ("known_stdamt_mean30", "known_stdamt_max9"):
                K[kn] = book(kn, known[kn])
            F = {"base EMA20": base_sm}
            for nm in ("mean60(|B|)", "mean120(|B|)", "mean60(pct-rank|B|)"):
                if nm in SIG:
                    F[nm] = SIG[nm][2]
            ksm = K["known_stdamt_mean30"][2]
            for name, s in sl.items():
                print(f"\n-- {name}: K = known_stdamt_mean30 traded signal (its own sign / half-life from train)")
                zk = dg._zrank(ksm[s])
                rk = pct_rank(ksm[s])
                n_ = slice(0, zk.shape[0])
                for fn, fsm in F.items():
                    zf = dg._zrank(fsm[s])
                    rf = pct_rank(fsm[s])
                    both = np.isfinite(rk) & np.isfinite(rf)
                    top_k, top_f = both & (rk >= 0.9), both & (rf >= 0.9)
                    ex = excess(tgt[s], both)
                    resid, info = dg.neutralise(zf, {"k": zk}, panel_ready=True, controls_ready=True)
                    br = bk.book_row(resid, tgt[s], n_)
                    bs = bk.book_row(zf + zk, tgt[s], n_)
                    bs2 = bk.book_row(0.5 * zf + zk, tgt[s], n_)
                    bk0 = bk.book_row(np.where(both, zk, np.nan), tgt[s], n_)
                    bf0 = bk.book_row(np.where(both, zf, np.nan), tgt[s], n_)
                    print(f"   F = {fn}: Spearman(F, K) {spearman_days(fsm[s], ksm[s]):+.3f}; top-decile overlap {float((top_k & top_f).sum() / max(top_k.sum(), 1)):.3f}; "
                          f"R2(F ~ K) {info['mean_r2']:.3f}")
                    for lab_, b_ in (("F alone", bf0), ("K alone (same cells)", bk0), ("F resid on K (not re-smoothed)", br),
                                     ("rank F + rank K", bs), ("0.5 rank F + rank K", bs2)):
                        print(f"      {lab_:<32} Lnet {b_['long_ann'] * 100:+6.1f}%  Lshp {b_['long_sharpe']:+5.2f}  Lgross {b_['long_gross_ann'] * 100:+6.1f}%  "
                              f"LTO {b_['long_turnover'] * 100:4.1f}%  LS {b_['ls_sharpe']:+5.2f}  short {b_['short_gross_ann'] * 100:+6.1f}%  Lmdd {b_['long_mdd'] * 100:+6.1f}%")
                    # double sort: inside K's long side, does F still order returns?
                    for lo, tag in ((0.9, "K top 10%"), (0.8, "K top 20%"), (0.7, "K top 30%")):
                        inK = both & (rk >= lo) & np.isfinite(ex)
                        rin = pct_rank(np.where(inK, fsm[s], np.nan))
                        t3 = [ann(ex[inK & (rin >= a) & (rin < b)]) for a, b in ((0, 1 / 3), (1 / 3, 2 / 3), (2 / 3, 1.01))]
                        print(f"      inside {tag}: excess by F tercile (low F -> high F): {t3[0]:+6.1f}% {t3[1]:+6.1f}% {t3[2]:+6.1f}%   (all: {ann(ex[inK]):+6.1f}%)")
                    inK = both & (rk >= 0.9) & np.isfinite(ex)
                    for cut in (0.1, 0.3):
                        bad = inK & (rf < cut)
                        print(f"      exclusion: K-top-decile names that are in F's bottom {int(cut * 100)}%: share {bad.sum() / max(inK.sum(), 1):.3f}, "
                              f"excess {ann(ex[bad]):+6.1f}%  vs the rest {ann(ex[inK & ~bad]):+6.1f}%")
                    inF = both & (rf >= 0.9) & np.isfinite(ex)
                    rin = pct_rank(np.where(inF, ksm[s], np.nan))
                    t3 = [ann(ex[inF & (rin >= a) & (rin < b)]) for a, b in ((0, 1 / 3), (1 / 3, 2 / 3), (2 / 3, 1.01))]
                    print(f"      inside F top 10%: excess by K tercile (low K -> high K): {t3[0]:+6.1f}% {t3[1]:+6.1f}% {t3[2]:+6.1f}%   (all: {ann(ex[inF]):+6.1f}%)")
        section(s8)

        # ---------------------------------------------------------------- 9
        def s9():
            hdr("9. the short leg with and without the 'opened locked at limit-up, could not be bought' filter (base, EMA20)")
            raw = st.target(buyable=False)
            for name, s in sl.items():
                sm = base_sm[s]
                w = bk.long_short_weights(sm, bk.TOP_FRAC)
                shorts = w < 0
                longs = w > 0
                unb = np.isnan(tgt[s]) & np.isfinite(raw[s])
                sb = bk.short_leg_excess(w, sm, tgt[s])
                sr = bk.short_leg_excess(w, sm, raw[s])
                ls_b = bk.stats(bk.portfolio_returns(w, tgt[s], bk.COST)[0])["sharpe"]
                ls_r = bk.stats(bk.portfolio_returns(w, raw[s], bk.COST)[0])["sharpe"]
                lb = bk.long_book(w, sm, tgt[s])[1]
                lr = bk.long_book(w, sm, raw[s])[1]
                print(f"-- {name}: unbuyable share in the short decile {float(unb[shorts].mean()):.4f}, in the long decile {float(unb[longs].mean()):.4f}, "
                      f"universe {float(unb[np.isfinite(sm)].mean()):.4f}")
                print(f"      short-leg gross excess: buyable label {ann(sb):+6.1f}%  raw label {ann(sr):+6.1f}%;   L/S net Sharpe: buyable {ls_b:+.2f}  raw {ls_r:+.2f};   "
                      f"long-leg gross excess: buyable {ann(lb):+6.1f}%  raw {ann(lr):+6.1f}%")
        section(s9)
    print(f"\n[x1 done in {time.time() - T0:.0f}s]", flush=True)


if __name__ == "__main__":
    main()
