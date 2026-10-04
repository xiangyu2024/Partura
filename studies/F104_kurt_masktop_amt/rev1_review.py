"""rev1 -- the experiments the two reviews asked for.  train / valid rows only; the holdout is never sliced.

The reviews (and the reviewer's own audit_span.py, logs/..._audit1.log) left four measurable questions:

  A. BUCKET-NEUTRAL CONDITIONING (review: "orthogonal to liquidity" holds only for the linear rank fit).
     cs_regres(rank, rank) leaves a residual whose support depends on liquidity (ranks are bounded), so the
     short decile of f_kurt30 sits at amt30 rank 0.67.  Replace it by the rank of the reading INSIDE its
     amt30 N-tile (N = 10 / 20 / 50) -- every liquidity bucket then gives the same share to every decile --
     and re-read both books.  Also the "residual on bucket dummies" version, the CV reader, and the original's
     30-day twin put through the same conditioning.
  B. LEG ANATOMY: how much of each leg's excess would a RANDOM basket with the same amt30-ventile distribution
     have earned ("liquidity location"), and how much is selection inside the ventile?  Exact version of the
     reviewer's rough 5-point / 10-point estimate; also says what f_exclcv's and the original's long legs are.
  C. SPANNING WITH NON-LINEAR ILLIQUIDITY (review: the original keeps 54% / 59% of its rank IC after
     {f_kurt30, amt30}; is the rest a non-linear illiquidity reading made by the mask?).  Same daily rank-space
     regression, adding amt30 ventile dummies, kshare30 ventile dummies, and a saturated 20 x 5 grid
     (amt30 ventile x kshare30 quintile inside it).  If the residual IC dies the story closes
     (original = concentration on the short side + non-linear illiquidity on the long side); if not, the mask
     carries something this study has not read.  Also: the same grid added to the 14 linear controls
     (is the "known exposure R2 0.175" only a linear lower bound?), and where the unexplained part lives.
  C2. AN EXACT SPLIT OF THE ORIGINAL.  Each day, put every stock in a cell = (that day's turnover ventile) x
     (quintile, inside the ventile, of the share of minutes the mask overwrote that day).  The original's daily
     value = its cell mean ("what the mask reads from WHERE the stock sits in liquidity / k") + the deviation
     from it ("the shape of the stock's own turnover, given its cell").  The EMA is linear, so the traded
     original is exactly the sum of the two smoothed parts.  Which part carries the rank IC, which the long leg,
     which the short leg; and is the deviation part spanned by f_kurt30?
  D. RAW-LABEL SHORT LEG (review: a name locked at limit-up at the t+1 open earns 0 in the short book).
     Reproduce the audit, add the user-fit (utrain) rows and the by-year rows, and do it for the new signals.

Every section starts from a self-check against a number that is already in a stage table or in the audit log.
"""
import traceback
import warnings

import numpy as np

warnings.filterwarnings("ignore")

from partura.study_tools import Study, bk, dg  # noqa: E402
from partura.books import long_short_weights  # noqa: E402

FID = "F104_kurt_masktop_amt"
A30 = "cross_mean(day_sum(Amt), 30)"
K30 = "cross_mean(day_kurt(Amt), 30)"
C30 = "cross_mean(div(day_std(Amt), day_mean(Amt)), 30)"
BK = f"cs_regres(cs_rank({K30}), cs_rank({A30}))"
BC = f"cs_regres(cs_rank({C30}), cs_rank({A30}))"
EX = {
    "base":   "day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))",
    "base30": "cross_mean(day_kurt(nt_cs_mask_top_replace_mean_neg(Amt)), 30)",
    "amt30":  A30,
    "std30":  "cross_mean(day_std(Amt), 30)",
    "k30":    K30,
    "c30":    C30,
    "bk":     BK,
    "bc":     BC,
    "exclcv": f"add(cs_rank({A30}), pow_3(cs_rank({BC})))",
}
# sign and half-life as fitted on TRAIN in the stage tables (decision convention)
FIT = {"base": (-1.0, 20), "base30": (-1.0, 1), "bk": (-1.0, 1), "bc": (-1.0, 0), "exclcv": (-1.0, 0),
       "std30": (-1.0, 0), "amt30": (-1.0, 1)}
# sign and half-life as fitted on UTRAIN in the final table (the user's convention)
FIT_USER = {"base": (-1.0, 20), "bk": (-1.0, 0), "bc": (-1.0, 0), "exclcv": (-1.0, 0), "std30": (-1.0, 0)}
CTL14 = ["ctl_amt", "ctl_price", "ctl_ivol", "ctl_range", "ctl_rev1", "ctl_mom20", "ctl_dvol20", "ctl_amt30",
         "ctl_kshare30", "ctl_max30", "ctl_pvcorr30", "ctl_retkurt30", "ctl_cap", "ctl_turnrate"]
COST = 0.0015
TOP = 0.10


def hdr(s):
    print("\n" + "=" * 8 + " " + s + " " + "=" * 8, flush=True)


def ann(x):
    return float(np.nanmean(x) * 252 * 100) if np.isfinite(x).any() else float("nan")


def pct_rank(a):
    """within-day rank in (0, 1) of the finite cells; NaN elsewhere."""
    r = dg.rank_rows(np.asarray(a, dtype=np.float64))
    n = np.isfinite(r).sum(1, keepdims=True)
    return (r - 0.5) / np.maximum(n, 1)


def bucket(x, mask, n):
    """within-day quantile bucket 0..n-1 of x over the cells in mask (0 = lowest); NaN elsewhere."""
    pr = pct_rank(np.where(mask, x, np.nan))
    return np.where(np.isfinite(pr), np.minimum(np.floor(pr * n), n - 1), np.nan)


def wb_rank(y, q, n):
    """rank in (0, 1) of y among the names that share its bucket q (0..n-1) that day; also the universe-wide rank."""
    ok = np.isfinite(y) & np.isfinite(q)
    u = pct_rank(np.where(ok, y, np.nan))
    r = dg.rank_rows(np.where(ok, q + u, np.nan))          # sorted by bucket, then by y inside the bucket
    out = np.full(y.shape, np.nan)
    below = np.zeros((y.shape[0], 1))
    for i in range(n):
        m = ok & (q == i)
        c = m.sum(1, keepdims=True).astype(np.float64)
        out = np.where(m, (r - below - 0.5) / np.maximum(c, 1.0), out)
        below = below + c
    return out, u


def wb_demean(y, q, n):
    """universe-wide rank of y minus its mean inside the bucket (= the OLS residual on the bucket dummies)."""
    ok = np.isfinite(y) & np.isfinite(q)
    u = pct_rank(np.where(ok, y, np.nan))
    out = np.full(y.shape, np.nan)
    for i in range(n):
        m = ok & (q == i)
        c = m.sum(1, keepdims=True).astype(np.float64)
        mu = np.where(m, u, 0.0).sum(1, keepdims=True) / np.maximum(c, 1.0)
        out = np.where(m, u - mu, out)
    return out


def cells(q):
    return np.where(np.isfinite(q), q, -1).astype(np.int16)


def row_corr(a, b):
    """mean daily Spearman of two panels."""
    ok = np.isfinite(a) & np.isfinite(b)
    ra = dg.rank_rows(np.where(ok, a, np.nan))
    rb = dg.rank_rows(np.where(ok, b, np.nan))
    ra = ra - np.nanmean(ra, axis=1, keepdims=True)
    rb = rb - np.nanmean(rb, axis=1, keepdims=True)
    num = np.nansum(ra * rb, axis=1)
    den = np.sqrt(np.nansum(ra * ra, axis=1) * np.nansum(rb * rb, axis=1))
    return float(np.nanmean(np.where(den > 0, num / np.where(den > 0, den, 1), np.nan)))


def where_legs(s, g):
    """for the decile legs of s: mean within-day rank of g, share in g's bottom / top quintile."""
    w = long_short_weights(s, TOP)
    rg = pct_rank(np.where(np.isfinite(s), g, np.nan))
    out = {}
    for leg, m in (("short", w < 0), ("long", w > 0)):
        x = rg[m]
        x = x[np.isfinite(x)]
        out[leg] = (float(x.mean()), float(np.mean(x < 0.2)), float(np.mean(x > 0.8))) if x.size else (np.nan,) * 3
    return out


def leg_decomp(s, tb, g, nb=20):
    """Decile legs of s, in the book convention (a held name without a label earns 0; benchmark = equal-weight
    label of the names with signal and label).  For each leg, daily series of: total excess, the excess of a basket
    that holds, for every name of the leg, the equal-weight return of that name's within-day g-bucket ('location'),
    and the difference ('selection').  Short-leg numbers are signed as money earned by being short."""
    w = long_short_weights(s, TOP)
    fin = np.isfinite(s)
    ok = fin & np.isfinite(tb)
    r = np.where(ok, tb, 0.0)
    n = ok.sum(1)
    ew = np.where(n > 0, r.sum(1) / np.maximum(n, 1), np.nan)
    q = bucket(g, fin & np.isfinite(g), nb)
    matched = np.where(fin, ew[:, None], 0.0)              # names with a signal but no g: the universe mean
    for i in range(nb):
        m = (q == i)
        c = m.sum(1, keepdims=True)
        mu = np.where(m, r, 0.0).sum(1, keepdims=True) / np.maximum(c, 1)
        matched = np.where(m, mu, matched)
    out = {}
    for leg, wl, sgn in (("long", np.clip(w, 0.0, None) * 2.0, 1.0), ("short", np.clip(-w, 0.0, None) * 2.0, -1.0)):
        have = wl.sum(1) > 0
        tot = np.where(have, sgn * ((wl * r).sum(1) - ew), np.nan)
        loc = np.where(have, sgn * ((wl * matched).sum(1) - ew), np.nan)
        out[leg] = (tot, loc, tot - loc)
    return out


def resid(y, cont=(), groups=(), min_n=50):
    """Daily cross-sectional OLS residual of y (already in the regression space) on an intercept, the continuous
    regressors in `cont` (ready panels) and one full set of dummies per integer panel in `groups` (cell id >= 0,
    -1 = missing).  One group set is absorbed by within-cell demeaning (Frisch-Waugh, exact); several are built
    explicitly.  Returns (residual panel, daily R2)."""
    D = y.shape[0]
    out = np.full(y.shape, np.nan)
    r2 = np.full(D, np.nan)
    for t in range(D):
        yt = y[t]
        m = np.isfinite(yt)
        for x in cont:
            m &= np.isfinite(x[t])
        for g in groups:
            m &= g[t] >= 0
        n = int(m.sum())
        if n < min_n:
            continue
        yv = yt[m].astype(np.float64)
        xs = [x[t][m].astype(np.float64) for x in cont]
        if len(groups) == 1:
            gi = groups[0][t][m].astype(np.int64)
            cnt = np.maximum(np.bincount(gi), 1)

            def dm(v, gi=gi, cnt=cnt):
                return v - (np.bincount(gi, weights=v) / cnt)[gi]

            res = dm(yv)
            if xs:
                X = np.column_stack([dm(v) for v in xs])
                beta = np.linalg.lstsq(X, res, rcond=None)[0]
                res = res - X @ beta
        else:
            cols = [np.ones(n)] + xs
            for g in groups:
                gi = g[t][m].astype(np.int64)
                ids = np.unique(gi)[1:]                     # drop one level
                if ids.size:
                    cols.append((gi[:, None] == ids[None, :]).astype(np.float64))
            X = np.column_stack(cols)
            beta = np.linalg.lstsq(X, yv, rcond=None)[0]
            res = yv - X @ beta
        ss = float(((yv - yv.mean()) ** 2).sum())
        rss = float((res ** 2).sum())
        r2[t] = 1.0 - rss / ss if ss > 0 else np.nan
        if ss > 0 and rss / ss < 1e-10:
            continue
        out[t, m] = res
    return out, r2


def cell_split(x, cell, min_n=50):
    """x = (its mean over the names sharing its cell that day) + (deviation).  cell: int ids, -1 = missing."""
    fit = np.full(x.shape, np.nan)
    for t in range(x.shape[0]):
        m = np.isfinite(x[t]) & (cell[t] >= 0)
        if int(m.sum()) < min_n:
            continue
        gi = cell[t][m].astype(np.int64)
        cnt = np.maximum(np.bincount(gi), 1)
        fit[t, m] = (np.bincount(gi, weights=x[t][m].astype(np.float64)) / cnt)[gi]
    return fit, x - fit


def hybrid(s, tb, tr_raw):
    """L/S with the long leg on the buyable label and the short leg charged the raw label (audit_span section C)."""
    w = long_short_weights(s, TOP)
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


def main(study_cls=Study):
    with study_cls(FID) as st:
        P = st.panels(EX)
        miss = [k for k in EX if k not in P]
        if miss:
            print("MISSING panels:", miss, flush=True)
        ut, tr_, va_ = st.slice("utrain"), st.slice("train"), st.slice("valid")
        off = ut.start
        tr = slice(tr_.start - off, tr_.stop - off)
        va = slice(va_.start - off, va_.stop - off)
        splits = (("train", tr), ("valid", va))
        tgt = np.asarray(st.target()[ut], dtype=np.float64)             # buyable label, utrain rows only
        yrs = np.array([int(str(d)[:4]) for d in np.asarray(st.dates)[ut]])
        years = [y for y in sorted(set(yrs.tolist())) if int((yrs == y).sum()) >= 20]

        def ysl(y):
            idx = np.nonzero(yrs == y)[0]
            return slice(int(idx[0]), int(idx[-1]) + 1)

        def smooth(panel, sign, hl):
            return np.asarray(bk.smoothed(sign * np.asarray(panel[:ut.stop], dtype=np.float64), hl)[ut], dtype=np.float64)

        SM = {n: smooth(P[n], *FIT[n]) for n in FIT if n in P}
        RAW = {n: P[n][ut] for n in P}                                   # float32 views, utrain rows
        a30 = np.asarray(RAW["amt30"], dtype=np.float64)
        SMN, FITN = {}, {}
        allsig = dict(SM)

        # ------------------------------------------------------------ 0
        hdr("0. self-check against the stage tables (LS net train/valid: base 3.91/1.47, base30 3.25/1.38, bk 3.75/1.91, "
            "bc 3.77/2.37, exclcv 3.94/4.44, std30 1.87/3.70, amt30 1.20/3.19)")
        for n in SM:
            r = [bk.book_row(SM[n], tgt, sl, COST) for _, sl in splits]
            ic = [dg.ic_row(SM[n][sl], tgt[sl], sign=1.0) for _, sl in splits]
            print(f"{n:>7} hl {FIT[n][1]:>2}  LS {r[0]['ls_sharpe']:+.2f}/{r[1]['ls_sharpe']:+.2f}  traded rIC "
                  f"{ic[0]['rank_ic']:+.4f}/{ic[1]['rank_ic']:+.4f}  Lnet {r[0]['long_ann'] * 100:+.1f}%/"
                  f"{r[1]['long_ann'] * 100:+.1f}%  Lsharpe {r[0]['long_sharpe']:+.2f}/{r[1]['long_sharpe']:+.2f}",
                  flush=True)

        # raw (not-buyable) label, as in audit_span section C
        ps = st.ps
        keep = (ps.label_buyable, ps._targets)
        ps.label_buyable, ps._targets = False, {}
        try:
            traw = np.asarray(ps.target(1)[ut], dtype=np.float64)
        finally:
            ps.label_buyable, ps._targets = keep
        both = np.isfinite(tgt) & np.isfinite(traw)
        print(f"label check: buyable finite but raw NaN {int((np.isfinite(tgt) & ~np.isfinite(traw)).sum())}, "
              f"max |diff| where both finite {float(np.nanmax(np.abs(tgt[both] - traw[both]))):.2e}", flush=True)
        locked = np.isfinite(traw) & ~np.isfinite(tgt)

        desc = {"wk10": "kurt30 ranked inside amt30 decile", "wk20": "kurt30 ranked inside amt30 ventile",
                "wk50": "kurt30 ranked inside amt30 50-tile", "dk20": "rank(kurt30) minus its amt30-ventile mean",
                "wc20": "cv30 ranked inside amt30 ventile", "wb20": "ORIGINAL's 30d mean ranked inside amt30 ventile",
                "bk": "f_kurt30 (linear rank residual)", "bc": "f_cv30 (linear rank residual)",
                "base": "original (raw daily panel; EMA fitted)", "base30": "original, 30d mean"}

        def show(name, x):
            """fit sign + half-life on train (as a stage would) and print both books, the raw-label short leg and
            where the two deciles sit in amt30."""
            x = np.asarray(x, dtype=np.float64)
            sg = dg.sign_from(x[tr], tgt[tr])
            b = bk.books(sg * x, tgt, tr, {"train": tr, "valid": va}, cost=COST, top_frac=TOP, rank_by="ls")
            hl = b["hl_used"]
            sm = np.asarray(bk.smoothed(sg * x, hl), dtype=np.float64)
            t_, v_ = b["splits"]["train"], b["splits"]["valid"]
            ic = [dg.ic_row(sm[sl], tgt[sl], sign=1.0) for _, sl in splits]
            hy = [hybrid(sm[sl], tgt[sl], traw[sl]) for _, sl in splits]
            wl = [where_legs(sm[sl], a30[sl]) for _, sl in splits]
            dist = dg.distinct_fraction(x[tr])
            print(f"{name:>6} [{desc.get(name, '')}]\n"
                  f"        sgn {sg:+.0f} hl {hl:g} | LS {t_['ls_sharpe']:+.2f}/{v_['ls_sharpe']:+.2f} | rIC "
                  f"{ic[0]['rank_ic']:+.4f}/{ic[1]['rank_ic']:+.4f} (t {ic[0]['rank_ic_t']:+.1f}/{ic[1]['rank_ic_t']:+.1f}) | "
                  f"Lgross {t_['long_gross_ann'] * 100:+.1f}%/{v_['long_gross_ann'] * 100:+.1f}% | Lnet "
                  f"{t_['long_ann'] * 100:+.1f}%/{v_['long_ann'] * 100:+.1f}% | Lsharpe {t_['long_sharpe']:+.2f}/"
                  f"{v_['long_sharpe']:+.2f} | short {t_['short_gross_ann'] * 100:+.1f}%/{v_['short_gross_ann'] * 100:+.1f}% | "
                  f"TO {t_['ls_turnover'] * 100:.1f}% | dist {dist:.2f}\n"
                  f"        || LS raw-short {hy[0][0]['sharpe']:+.2f}/{hy[1][0]['sharpe']:+.2f} | short raw "
                  f"{hy[0][2]['ann'] * 100:+.1f}%/{hy[1][2]['ann'] * 100:+.1f}% || short dec amt30 rank "
                  f"{wl[0]['short'][0]:.2f}/{wl[1]['short'][0]:.2f} least {wl[0]['short'][1]:.0%}/{wl[1]['short'][1]:.0%} "
                  f"most {wl[0]['short'][2]:.0%}/{wl[1]['short'][2]:.0%} | long dec amt30 rank {wl[0]['long'][0]:.2f}/"
                  f"{wl[1]['long'][0]:.2f} least {wl[0]['long'][1]:.0%}/{wl[1]['long'][1]:.0%} most "
                  f"{wl[0]['long'][2]:.0%}/{wl[1]['long'][2]:.0%}", flush=True)
            if "splits_at_hl_long" in b:
                tl, vl = b["splits_at_hl_long"]["train"], b["splits_at_hl_long"]["valid"]
                print(f"        (half-life chosen by the long book instead: hl {b['hl_long']:g}  Lnet "
                      f"{tl['long_ann'] * 100:+.1f}%/{vl['long_ann'] * 100:+.1f}%  Lsharpe {tl['long_sharpe']:+.2f}/"
                      f"{vl['long_sharpe']:+.2f}  LS {tl['ls_sharpe']:+.2f}/{vl['ls_sharpe']:+.2f})", flush=True)
            return sg, hl, sm

        def fixed(name, sm, note=""):
            """books of an already-smoothed, already-signed signal (no fitting)."""
            r = [bk.book_row(sm, tgt, sl, COST) for _, sl in splits]
            ic = [dg.ic_row(sm[sl], tgt[sl], sign=1.0) for _, sl in splits]
            wl = [where_legs(sm[sl], a30[sl]) for _, sl in splits]
            d = [leg_decomp(sm[sl], tgt[sl], a30[sl]) for _, sl in splits]
            print(f"{name:<30} LS {r[0]['ls_sharpe']:+.2f}/{r[1]['ls_sharpe']:+.2f} (gross {r[0]['ls_gross_sharpe']:+.2f}/"
                  f"{r[1]['ls_gross_sharpe']:+.2f}) | rIC {ic[0]['rank_ic']:+.4f}/{ic[1]['rank_ic']:+.4f} (t "
                  f"{ic[0]['rank_ic_t']:+.1f}/{ic[1]['rank_ic_t']:+.1f}) | Lgross {r[0]['long_gross_ann'] * 100:+.1f}%/"
                  f"{r[1]['long_gross_ann'] * 100:+.1f}% Lnet {r[0]['long_ann'] * 100:+.1f}%/{r[1]['long_ann'] * 100:+.1f}% | "
                  f"short {r[0]['short_gross_ann'] * 100:+.1f}%/{r[1]['short_gross_ann'] * 100:+.1f}% | TO "
                  f"{r[0]['ls_turnover'] * 100:.1f}% {note}\n"
                  f"{'':<6}long dec amt30 rank {wl[0]['long'][0]:.2f}/{wl[1]['long'][0]:.2f} (least-active quintile "
                  f"{wl[0]['long'][1]:.0%}/{wl[1]['long'][1]:.0%}), short dec {wl[0]['short'][0]:.2f}/{wl[1]['short'][0]:.2f} "
                  f"(most-active quintile {wl[0]['short'][2]:.0%}/{wl[1]['short'][2]:.0%}); long = location + selection "
                  + " / ".join(f"{ann(d[i]['long'][0]):+.1f} = {ann(d[i]['long'][1]):+.1f} + {ann(d[i]['long'][2]):+.1f}"
                               for i in range(2))
                  + "; short "
                  + " / ".join(f"{ann(d[i]['short'][0]):+.1f} = {ann(d[i]['short'][1]):+.1f} + {ann(d[i]['short'][2]):+.1f}"
                               for i in range(2)), flush=True)
            return [ic[0]["rank_ic"], ic[1]["rank_ic"]]

        # ------------------------------------------------------------ A
        def section_a():
            hdr("A. bucket-neutral conditioning: rank of the reading INSIDE its amt30 N-tile (train/valid; sign and "
                "half-life fitted on train, as in the stage tables)")

            def cond(y, n, kind="rank"):
                y = np.asarray(y, dtype=np.float64)
                q = bucket(a30, np.isfinite(y) & np.isfinite(a30), n)
                if kind == "demean":
                    return wb_demean(y, q, n)
                w, u = wb_rank(y, q, n)
                return w + 1e-6 * u                                       # the 1e-6 only breaks exact cross-bucket ties

            print("columns: sign hl | LS net | traded rank IC | long gross | long net | long-only Sharpe | short gross | "
                  "L/S turnover | distinct || LS net with the short leg on the RAW label | short gross on the raw label "
                  "|| short decile: mean amt30 rank, share in least / most active quintile | long decile: same")
            for name in ("base", "base30", "bk", "bc"):
                try:
                    show(name, RAW[name])
                except Exception as exc:
                    print(f"{name}: failed: {type(exc).__name__}: {exc}", flush=True)
            plan = (("wk10", "k30", 10, "rank"), ("wk20", "k30", 20, "rank"), ("wk50", "k30", 50, "rank"),
                    ("dk20", "k30", 20, "demean"), ("wc20", "c30", 20, "rank"), ("wb20", "base30", 20, "rank"))
            for name, src, n, kind in plan:
                try:
                    sg, hl, sm = show(name, cond(RAW[src], n, kind))
                    SMN[name], FITN[name] = sm, (sg, hl)
                    allsig[name] = sm
                except Exception as exc:
                    print(f"{name}: failed: {type(exc).__name__}: {exc}", flush=True)

            print("\nsignal-decile excess, Q1 (shorted) .. Q10 (held), annualised %:")
            for n in ("bk", "wk20", "wc20", "wb20"):
                if n not in allsig:
                    continue
                for sname, sl in splits:
                    prof = bk.quantile_profile(allsig[n], tgt, sl, n=10)
                    print(f"   {n:>6} [{sname}] " + " ".join(f"{r['excess_ann'] * 100:+6.1f}" for r in prof), flush=True)

            print("\ntraded-signal rank correlations (train / valid):")
            pairs = [("wk20", "bk"), ("wk20", "base"), ("wk20", "amt30"), ("wk20", "wk10"), ("wk20", "wk50"),
                     ("wk20", "dk20"), ("wc20", "bc"), ("wc20", "wk20"), ("wb20", "base30"), ("wb20", "wk20"),
                     ("wb20", "base"), ("bk", "amt30"), ("bk", "base")]
            for a, b in pairs:
                if a in allsig and b in allsig:
                    print(f"   {a:>6} ~ {b:<6}  {row_corr(allsig[a][tr], allsig[b][tr]):+.2f} / "
                          f"{row_corr(allsig[a][va], allsig[b][va]):+.2f}", flush=True)

            print("\nby year: LS net (buyable label) -> with the short leg on the raw label; long gross excess:")
            for n in ("bk", "wk20", "wc20", "base"):
                if n not in allsig:
                    continue
                out = []
                for y in years:
                    sl = ysl(y)
                    r = bk.book_row(allsig[n], tgt, sl, COST)
                    h = hybrid(allsig[n][sl], tgt[sl], traw[sl])
                    out.append(f"{y} {r['ls_sharpe']:+.2f}->{h[0]['sharpe']:+.2f} Lg {r['long_gross_ann'] * 100:+.1f}%")
                print(f"   {n:>6}: " + "  ".join(out), flush=True)

        # ------------------------------------------------------------ B
        def section_b():
            hdr("B. leg anatomy: total excess = 'location' (a random basket with the same amt30-ventile distribution) "
                "+ 'selection' (inside the ventile).  annualised %, gross, train / valid")
            print("columns: SHORT leg total = location + selection | LONG leg total = location + selection")
            for n in ("base", "base30", "bk", "bc", "wk20", "wc20", "wb20", "exclcv", "std30", "amt30"):
                if n not in allsig:
                    continue
                d = [leg_decomp(allsig[n][sl], tgt[sl], a30[sl]) for _, sl in splits]
                sh = [tuple(ann(x) for x in d[i]["short"]) for i in range(2)]
                lg = [tuple(ann(x) for x in d[i]["long"]) for i in range(2)]
                print(f"{n:>7}  short {sh[0][0]:+5.1f} = {sh[0][1]:+5.1f} + {sh[0][2]:+5.1f} / {sh[1][0]:+5.1f} = "
                      f"{sh[1][1]:+5.1f} + {sh[1][2]:+5.1f}   |   long {lg[0][0]:+5.1f} = {lg[0][1]:+5.1f} + {lg[0][2]:+5.1f} / "
                      f"{lg[1][0]:+5.1f} = {lg[1][1]:+5.1f} + {lg[1][2]:+5.1f}", flush=True)
            print("\nby year (utrain): long leg total = location + selection, then short leg total = location + selection")
            for n in ("base", "bk", "exclcv", "std30"):
                if n not in allsig:
                    continue
                d = leg_decomp(allsig[n], tgt, a30)
                out = []
                for y in years:
                    m = yrs == y
                    lo = [ann(x[m]) for x in d["long"]]
                    so = [ann(x[m]) for x in d["short"]]
                    out.append(f"{y}: L {lo[0]:+.1f}={lo[1]:+.1f}{lo[2]:+.1f} S {so[0]:+.1f}={so[1]:+.1f}{so[2]:+.1f}")
                print(f"{n:>7}  " + "   ".join(out), flush=True)

        # ------------------------------------------------------------ C
        def section_c():
            hdr("C. spanning: daily rank-space OLS residual of a TRADED signal; continuous regressors as uniform ranks, "
                "non-linear liquidity as bucket dummies")
            ks = np.asarray(st.control("ctl_kshare30")[ut], dtype=np.float64)
            fa, fk = np.isfinite(a30), np.isfinite(ks)
            qa20 = bucket(a30, fa, 20)
            Ga = cells(qa20)                                               # amt30 ventile
            Gk = cells(bucket(ks, fk, 20))                                 # kshare30 ventile
            wks, _ = wb_rank(np.where(fa & fk, ks, np.nan), qa20, 20)
            Gak = cells(qa20 * 5 + np.minimum(np.floor(wks * 5), 4))       # amt30 ventile x kshare30 quintile inside it
            del wks

            def ncell(G):
                return np.mean([np.unique(G[t][G[t] >= 0]).size for t in range(0, G.shape[0], 50)])

            print(f"cells per day: Ga {ncell(Ga):.0f}, Gk {ncell(Gk):.0f}, Gak {ncell(Gak):.0f}; daily Spearman(kshare30, "
                  f"amt30) {row_corr(ks[tr], a30[tr]):+.2f}", flush=True)

            def z32(x):
                return dg._zrank(np.asarray(x, dtype=np.float64)).astype(np.float32)

            Z = {"bk": z32(SM["bk"]), "bc": z32(SM["bc"]), "a": z32(a30), "ks": z32(ks), "base": z32(SM["base"])}
            if "wk20" in SMN:
                Z["wk"] = z32(SMN["wk20"])
            if "wc20" in SMN:
                Z["wc"] = z32(SMN["wc20"])
            C14 = []
            for k in CTL14:
                try:
                    C14.append(z32(st.control(k)[ut]))
                except Exception as exc:
                    print(f"control {k} unavailable: {type(exc).__name__}: {exc}", flush=True)
            print(f"{len(C14)} of {len(CTL14)} linear controls loaded", flush=True)
            print("columns: R2 train/valid | residual rank IC train/valid (t) | share of the rank IC kept | gross LS Sharpe | "
                  "long gross, short gross excess (train) , (valid)")

            def line(name, y, cont=(), groups=(), ref=None, extra=False):
                if cont or groups:
                    res, r2 = resid(dg._zrank(np.asarray(y, dtype=np.float64)), cont, groups)
                else:
                    res, r2 = np.asarray(y, dtype=np.float64), np.full(y.shape[0], np.nan)
                ic = [dg.ic_row(res[sl], tgt[sl], sign=1.0) for _, sl in splits]
                b = [bk.book_row(res, tgt, sl, COST) for _, sl in splits]
                kp = ["%.0f%%" % (100 * ic[i]["rank_ic"] / ref[i]) if ref else "--" for i in range(2)]
                print(f"{name:<36} R2 {np.nanmean(r2[tr]):5.3f}/{np.nanmean(r2[va]):5.3f} | rIC {ic[0]['rank_ic']:+.4f}/"
                      f"{ic[1]['rank_ic']:+.4f} (t {ic[0]['rank_ic_t']:+5.1f}/{ic[1]['rank_ic_t']:+5.1f}) | kept {kp[0]}/{kp[1]} | "
                      f"LSgross {b[0]['ls_gross_sharpe']:+.2f}/{b[1]['ls_gross_sharpe']:+.2f} | L "
                      f"{b[0]['long_gross_ann'] * 100:+5.1f}% S {b[0]['short_gross_ann'] * 100:+5.1f}% , L "
                      f"{b[1]['long_gross_ann'] * 100:+5.1f}% S {b[1]['short_gross_ann'] * 100:+5.1f}%", flush=True)
                if extra:
                    wl = [where_legs(res[sl], a30[sl]) for _, sl in splits]
                    wk_ = [where_legs(res[sl], ks[sl]) for _, sl in splits]
                    ci = [dg.conditional_ic(res[sl], tgt[sl], a30[sl], buckets=5) for _, sl in splits]
                    d = [leg_decomp(res[sl], tgt[sl], a30[sl]) for _, sl in splits]
                    print(f"{'':<6}residual's long decile: amt30 rank {wl[0]['long'][0]:.2f}/{wl[1]['long'][0]:.2f}, in "
                          f"least-active quintile {wl[0]['long'][1]:.0%}/{wl[1]['long'][1]:.0%}, kshare30 rank "
                          f"{wk_[0]['long'][0]:.2f}/{wk_[1]['long'][0]:.2f}; short decile: amt30 rank {wl[0]['short'][0]:.2f}/"
                          f"{wl[1]['short'][0]:.2f}\n"
                          f"{'':<6}residual's rank IC by amt30 quintile (Q1 least active): train "
                          + " ".join(f"{r['rank_ic']:+.4f}" for r in ci[0]) + "  valid "
                          + " ".join(f"{r['rank_ic']:+.4f}" for r in ci[1]) + "\n"
                          f"{'':<6}residual's long leg = location + selection: "
                          + " / ".join(f"{ann(d[i]['long'][0]):+.1f} = {ann(d[i]['long'][1]):+.1f} + {ann(d[i]['long'][2]):+.1f}"
                                       for i in range(2))
                          + "; short leg: "
                          + " / ".join(f"{ann(d[i]['short'][0]):+.1f} = {ann(d[i]['short'][1]):+.1f} + "
                                       f"{ann(d[i]['short'][2]):+.1f}" for i in range(2)), flush=True)
                return [ic[0]["rank_ic"], ic[1]["rank_ic"]]

            print("self-check (audit_span A): base | bk, amt30 -> R2 0.338 (utrain mean), rIC +0.0147/+0.0078, LSgross "
                  "+1.65/+1.48; base30 | bk, amt30 -> rIC +0.0072/+0.0025;  bk | base, amt30 -> rIC +0.0096/+0.0005;  "
                  "stage table: base | 14 controls -> train R2 0.175, rIC +0.0137, LSgross +2.56")
            for dep in ("base", "base30"):
                y = SM[dep]
                ref = line(dep, y)
                specs = [
                    ("amt30 (linear)", [Z["a"]], []),
                    ("amt30 ventiles", [], [Ga]),
                    ("amt30 x kshare30 grid", [], [Gak]),
                    ("bk, amt30 (linear)", [Z["bk"], Z["a"]], []),
                    ("bk, amt30, kshare30 (linear)", [Z["bk"], Z["a"], Z["ks"]], []),
                    ("bk, amt30 ventiles", [Z["bk"]], [Ga]),
                    ("bk, amt30 vent., kshare30 vent.", [Z["bk"]], [Ga, Gk]),
                    ("bk, grid", [Z["bk"]], [Gak]),
                    ("bk, bc, grid", [Z["bk"], Z["bc"]], [Gak]),
                ]
                if "wk" in Z:
                    specs.append(("wk20, grid", [Z["wk"]], [Gak]))
                if "wk" in Z and "wc" in Z:
                    specs.append(("wk20, wc20, grid", [Z["wk"], Z["wc"]], [Gak]))
                if C14:
                    specs += [("14 controls (linear)", C14, []),
                              ("14 controls, grid", C14, [Gak]),
                              ("bk, 14 controls, grid", [Z["bk"]] + C14, [Gak]),
                              ("bk, bc, 14 controls, grid", [Z["bk"], Z["bc"]] + C14, [Gak])]
                for nm, cont, grp in specs:
                    try:
                        line(f"{dep} | {nm}", y, cont, grp, ref,
                             extra=nm in ("bk, amt30 (linear)", "bk, grid", "bk, bc, 14 controls, grid"))
                    except Exception as exc:
                        print(f"{dep} | {nm}: failed: {type(exc).__name__}: {exc}", flush=True)
                print()
            deps = [("bk", SM["bk"]), ("bc", SM["bc"])]
            if "wk20" in SMN:
                deps.append(("wk20", SMN["wk20"]))
            if "wc20" in SMN:
                deps.append(("wc20", SMN["wc20"]))
            for dep, y in deps:
                ref = line(dep, y)
                specs = [("base, amt30 (linear)", [Z["base"], Z["a"]], []),
                         ("base, grid", [Z["base"]], [Gak]),
                         ("grid", [], [Gak])]
                if C14:
                    specs += [("14 controls (linear)", C14, []), ("14 controls, grid", C14, [Gak]),
                              ("base, 14 controls, grid", [Z["base"]] + C14, [Gak])]
                for nm, cont, grp in specs:
                    try:
                        line(f"{dep} | {nm}", y, cont, grp, ref)
                    except Exception as exc:
                        print(f"{dep} | {nm}: failed: {type(exc).__name__}: {exc}", flush=True)
                print()
            del C14

            # -------------------------------------------------------- C2
            hdr("C2. exact split of the ORIGINAL's daily panel: cell mean (cell = that day's turnover ventile x quintile of "
                "the share of minutes overwritten, inside the ventile) + deviation; both smoothed with the original's EMA-20")
            if off != 0:
                print(f"note: utrain starts at row {off}; the EMA of the two parts is started there", flush=True)
            kf = np.asarray(st.panels({"kfrac": "day_mean(is_gt0(sub(nt_cs_mask_top_replace_mean_neg(Amt), Amt)))"})
                            ["kfrac"][ut], dtype=np.float64)
            amd = np.asarray(st.control("ctl_amt")[ut], dtype=np.float64)
            base_d = np.asarray(RAW["base"], dtype=np.float64)
            okd = np.isfinite(amd) & np.isfinite(kf)
            qd = bucket(amd, okd, 20)
            wkd, _ = wb_rank(np.where(okd, kf, np.nan), qd, 20)
            cell_d = cells(qd * 5 + np.minimum(np.floor(wkd * 5), 4))
            del wkd
            print(f"daily cells per day {ncell(cell_d):.0f}; share of stock-days with no minute overwritten "
                  f"{np.nanmean(np.where(okd, kf == 0, np.nan)):.1%}; daily Spearman(kfrac, turnover) "
                  f"{row_corr(kf[tr], amd[tr]):+.2f}", flush=True)
            for label, xd in (("raw values", base_d), ("within-day ranks", pct_rank(base_d))):
                fit, dev = cell_split(xd, cell_d)
                v_all = np.nanvar(xd, axis=1)
                v_fit = np.nanvar(np.where(np.isfinite(fit), fit, np.nan), axis=1)
                tot = np.asarray(bk.smoothed(-np.where(np.isfinite(fit), xd, np.nan), 20), dtype=np.float64)
                s_fit = np.asarray(bk.smoothed(-fit, 20), dtype=np.float64)
                s_dev = np.asarray(bk.smoothed(-dev, 20), dtype=np.float64)
                print(f"\n[{label}] daily cross-sectional variance explained by the cell mean: "
                      f"{np.nanmean(v_fit / np.where(v_all > 0, v_all, np.nan)):.3f};  rank corr of the traded parts "
                      f"(train/valid): total~original {row_corr(tot[tr], SM['base'][tr]):+.2f}/"
                      f"{row_corr(tot[va], SM['base'][va]):+.2f}, cell part~total {row_corr(s_fit[tr], tot[tr]):+.2f}/"
                      f"{row_corr(s_fit[va], tot[va]):+.2f}, deviation part~total {row_corr(s_dev[tr], tot[tr]):+.2f}/"
                      f"{row_corr(s_dev[va], tot[va]):+.2f}, cell~deviation {row_corr(s_fit[tr], s_dev[tr]):+.2f}/"
                      f"{row_corr(s_fit[va], s_dev[va]):+.2f}, cell part~amt30 {row_corr(s_fit[tr], a30[tr]):+.2f}, "
                      f"deviation part~bk {row_corr(s_dev[tr], SM['bk'][tr]):+.2f}/{row_corr(s_dev[va], SM['bk'][va]):+.2f}",
                      flush=True)
                ref = fixed("total (cell + deviation), EMA-20", tot)
                fixed("cell-mean part, EMA-20", s_fit)
                fixed("deviation part, EMA-20", s_dev)
                zc, zd = z32(s_fit), z32(s_dev)
                line("total | cell part", tot, [zc], [], ref)
                line("total | deviation part", tot, [zd], [], ref)
                line("total | bk, amt30, cell part", tot, [Z["bk"], Z["a"], zc], [], ref)
                line("total | bk, grid(30d), cell part", tot, [Z["bk"], zc], [Gak], ref)
                rf = line("cell part", s_fit)
                line("cell part | amt30 (linear)", s_fit, [Z["a"]], [], rf)
                line("cell part | amt30 ventiles", s_fit, [], [Ga], rf)
                line("cell part | grid(30d)", s_fit, [], [Gak], rf)
                rd = line("deviation part", s_dev)
                line("deviation part | bk", s_dev, [Z["bk"]], [], rd)
                line("deviation part | bk, amt30", s_dev, [Z["bk"], Z["a"]], [], rd)
                line("deviation part | bk, bc, grid(30d)", s_dev, [Z["bk"], Z["bc"]], [Gak], rd, extra=True)
                rb_ = line("bk", SM["bk"])
                line("bk | deviation part", SM["bk"], [zd], [], rb_)
                line("bk | deviation part, cell part", SM["bk"], [zd, zc], [], rb_)
                del fit, dev, tot, s_fit, s_dev, zc, zd

        # ------------------------------------------------------------ D
        def section_d():
            hdr("D. the short leg charged the RAW label (a name locked at limit-up at the t+1 open is no longer worth 0)")
            for sname, sl in splits:
                lk = locked[sl]
                print(f"[{sname}] locked cells: {lk.mean() * 100:.3f}% of all cells; mean raw label on them "
                      f"{np.nanmean(traw[sl][lk]) * 1e4:+.0f} bp; per day {lk.sum(1).mean():.1f} names", flush=True)
            print("decision convention (sign / half-life fitted on train).  columns: locked share in the short decile | LS "
                  "net buyable -> raw-short | short gross buyable -> raw-short | long net, long-only Sharpe (label-independent)")
            print("self-check (audit_span C): base 3.91->3.22 / 1.47->0.85, bk 3.75->3.13 / 1.91->1.44, bc 3.77->3.16 / "
                  "2.37->1.87, exclcv 3.94->3.59 / 4.44->4.05, std30 1.87->1.79 / 3.70->3.62")
            for n in ("base", "bk", "bc", "exclcv", "std30", "amt30", "wk20", "wc20", "wb20"):
                if n not in allsig:
                    continue
                for sname, sl in splits:
                    s = allsig[n][sl]
                    sh = long_short_weights(s, TOP) < 0
                    ref = bk.book_row(allsig[n], tgt, sl, COST)
                    hyb = hybrid(s, tgt[sl], traw[sl])
                    print(f"{n:>7} [{sname}] locked in short decile {locked[sl][sh].mean() * 100:.2f}% | LS "
                          f"{ref['ls_sharpe']:+.2f} -> {hyb[0]['sharpe']:+.2f} | short {ref['short_gross_ann'] * 100:+.1f}% -> "
                          f"{hyb[2]['ann'] * 100:+.1f}% | Lnet {ref['long_ann'] * 100:+.1f}% Lsharpe {ref['long_sharpe']:+.2f}",
                          flush=True)
            print("\nuser convention (sign / half-life fitted on utrain), utrain as one book.  self-check (final table, 训练 "
                  "column): LS base 3.20, bk 3.20, bc 3.36, exclcv 4.06, std30 2.33; short gross 31.2 / 33.8 / 37.5 / 38.5 / 24.7")
            whole = slice(0, tgt.shape[0])
            SU = {}
            for n, (sg, hl) in FIT_USER.items():
                if n not in P:
                    continue
                SU[n] = smooth(P[n], sg, hl)
                ref = bk.book_row(SU[n], tgt, whole, COST)
                hyb = hybrid(SU[n], tgt, traw)
                print(f"{n:>7} hl {hl:>2} | LS {ref['ls_sharpe']:+.2f} -> {hyb[0]['sharpe']:+.2f} | short "
                      f"{ref['short_gross_ann'] * 100:+.1f}% -> {hyb[2]['ann'] * 100:+.1f}% | Lnet {ref['long_ann'] * 100:+.1f}% "
                      f"Lsharpe {ref['long_sharpe']:+.2f}", flush=True)
            print("\nuser convention, by year (utrain years only): LS net buyable -> raw-short")
            for n in SU:
                out = []
                for y in years:
                    sl = ysl(y)
                    r = bk.book_row(SU[n], tgt, sl, COST)
                    h = hybrid(SU[n][sl], tgt[sl], traw[sl])
                    out.append(f"{y} {r['ls_sharpe']:+.2f}->{h[0]['sharpe']:+.2f}")
                print(f"{n:>7}  " + "  ".join(out), flush=True)

        for sec in (section_a, section_b, section_d, section_c):
            try:
                sec()
            except Exception:
                print(f"\n!!! {sec.__name__} failed:\n{traceback.format_exc()}", flush=True)
        try:
            from partura import guard
            print(f"\nanon of this process at the end: {guard.self_anon_gb():.2f} GiB", flush=True)
        except Exception:
            pass
    print("\n[rev1 done]")


if __name__ == "__main__":
    main()
