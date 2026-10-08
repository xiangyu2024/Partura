"""Risk control on both sides of the fusion (research/risk_control/PLAN.md), step 2: every method, one table.

Server, CPU (family statistics use the GPU when it is free).  Inputs come from scripts/rc_prepare.py (runs/_risk/).

    risk_control.py [--only 手写库冠军] [--skip A|B2] [--tag r1] [--workers 12]

For each champion: the baseline book (smoothed signal, top 10 %, equal weight, fully invested, 15 bp), then
  A  before the fusion: family gates / stops / vol weights / disagreement penalty / neutralised families (GRID_A),
  B1 stock-level screens and risk weights, B2 a constrained mean-variance book, B3 exposure rules (not fully invested),
  C  the in-sample picks stacked.
Every grid is fixed here; a method family's cell is picked by the in-sample sqrt(Calmar x Sharpe) of the TOTAL return, and
only that cell's out-of-sample reading counts as a reading by the rule.  Writes runs/_risk/risk_control_<tag>.json.
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.splits import Ledger  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


R = PARTURA_ROOT / "runs" / "_risk"
TAG = opt("--tag", "r1")
SKIP = set((opt("--skip") or "").split(",")) - {""}
WORKERS = int(opt("--workers", "12"))
CHAMPS = {"手写库冠军": 20.0, "挖掘冠军": 10.0}                # half-lives of the stored long books (guidance E12: held fixed)
names = [n for n in (opt("--only") or ",".join(CHAMPS)).split(",") if n]
COST, TOP = 0.0015, 0.10

# ------------------------------------------------------------------ the grids (fixed before any result; PLAN section 3)
GRID_A1 = [(w, thr, lvl) for w in (60, 120, 250) for thr in (0.0, -1.0) for lvl in (0.0, 0.5)]
GRID_A2 = [2.0, 3.0]
GRID_A4 = [0.0, 0.25, 0.5, 1.0]                                 # 0 = the ruler (normalised mean, no penalty)
SPEC_A5 = {"ind": [], "ind_size": ["size"], "ind_size_vol_liq": ["size", "vol", "liq"]}
GRID_Q = [0.05, 0.10, 0.20]
GRID_B2 = ([(lam, "full", dl) for lam in (1.0, 5.0, 20.0, 80.0) for dl in (None, 0.05)]
           + [(lam, "free", dl) for lam in (2.0, 5.0, 10.0) for dl in (None, 0.05)])
B2_EVERY, B2_CAND, B2_CAP_MULT, B2_H = 5, 0.20, 5.0, 10.0
GRID_B3 = ([("tv", s, None) for s in (0.15, 0.20, 0.25)] + [("trend", n, lvl) for n in (20, 60, 120) for lvl in (0.5, 0.0)]
           + [("stamp", k, lvl) for k in ("sp3", "sp5", "ld3", "ld5", "any") for lvl in (0.5, 0.0)]
           + [("owndd", d, 0.5) for d in (0.10, 0.15)] + [("disp", 0.9, lvl) for lvl in (0.5, 0.0)])


# ------------------------------------------------------------------ small tools
def roll_sum(x, w):
    fin = np.isfinite(x)
    z = np.zeros((1,) + x.shape[1:])
    c = np.concatenate([z, np.cumsum(np.where(fin, x, 0.0), 0)])
    n = np.concatenate([z, np.cumsum(fin, 0)])
    lo = np.maximum(np.arange(x.shape[0]) + 1 - w, 0)
    return c[1:] - c[lo], n[1:] - n[lo]


def roll_mean(x, w, minp=None):
    s, n = roll_sum(x, w)
    return np.where(n >= (minp or w), s / np.maximum(n, 1), np.nan)


def roll_std(x, w, minp=None):
    s, n = roll_sum(x, w)
    ss, _ = roll_sum(x * x, w)
    var = (ss - s * s / np.maximum(n, 1)) / np.maximum(n - 1, 1)
    return np.where(n >= (minp or w), np.sqrt(np.clip(var, 0, None)), np.nan)


def lag(x, k):
    out = np.full_like(x, np.nan, dtype=np.float64)
    if k < x.shape[0]:
        out[k:] = x[:-k]
    return out


def pct_rows(x):
    return pd.DataFrame(x).rank(axis=1, pct=True).to_numpy()


def ema_rows(x, hl):
    from alphacube.metrics import ema_rows as f
    return f(x, hl) if hl else np.asarray(x, dtype=np.float64)


def top_book(score, k, weight=None):
    """Top-k names by ``score`` (NaN = not eligible), ties by symbol order exactly as alphacube.metrics.long_short_weights."""
    D, S = score.shape
    fin = np.isfinite(score)
    n = fin.sum(1)
    order = np.argsort(np.where(fin, score, np.inf), axis=1, kind="stable")
    pos = np.arange(S)[None, :]
    kk = np.minimum(k, n)
    sel_sorted = (pos >= (n - kk)[:, None]) & (pos < n[:, None]) & (n >= 2)[:, None]
    sel = np.zeros((D, S), dtype=bool)
    np.put_along_axis(sel, order, sel_sorted, axis=1)
    w = sel.astype(np.float64) if weight is None else np.where(sel, np.nan_to_num(weight, nan=0.0), 0.0)
    tot = w.sum(1, keepdims=True)
    return np.where(tot > 0, w / np.maximum(tot, 1e-300), 0.0)


def boot_dsharpe(a, b, n=2000, block=20, seed=7):
    m = np.isfinite(a) & np.isfinite(b)
    a, b = a[m], b[m]
    L = a.size
    if L < 60:
        return [float("nan")] * 3
    rng = np.random.default_rng(seed)
    nb = int(np.ceil(L / block))
    idx = ((rng.integers(0, L, size=(n, nb))[:, :, None] + np.arange(block)[None, None, :]) % L).reshape(n, -1)[:, :L]
    sh = lambda x: x.mean(1) / x.std(1) * np.sqrt(252)          # noqa: E731
    d = sh(a[idx]) - sh(b[idx])
    return [float(np.quantile(d, 0.05)), float(np.median(d)), float(np.quantile(d, 0.95))]


# ------------------------------------------------------------------ data
t00 = time.time()
base = json.loads((R / "base.json").read_text(encoding="utf-8"))
dates = np.asarray(base["dates"])
D, S = len(dates), len(base["symbols"])
ix = lambda d: int(np.searchsorted(dates, d))                   # noqa: E731
TR = base["train_stop"]
SEG = {"insample": slice(0, TR), "test": slice(TR, ix("20260101")), "forward": slice(ix("20260101"), D), "oos": slice(TR, D),
       "stampede": slice(ix("20240116"), ix("20240207"))}
tgt = np.load(R / "target.npy")
r = np.nan_to_num(tgt, nan=0.0)
ld = lambda k: np.load(R / f"px_{k}.npy").astype(np.float64)    # noqa: E731
close, amt, ltc, lfc, lim, rawpx = ld("close"), ld("amt"), ld("ltc"), ld("lfc"), ld("limit"), ld("rawprice")
industry = np.load(R / "px_industry.npy").astype(int)
ret = close / lag(close, 1) - 1.0
ret = np.where(np.abs(ret) < 0.45, ret, np.nan)
vol20 = roll_std(ret, 20, 10)
mom20 = close / lag(close, 20) - 1.0
amt20 = np.log(np.clip(roll_mean(np.where(amt > 0, amt, np.nan), 20, 5), 1.0, None))
upl, dnl = ret >= 0.95 * lim, ret <= -0.95 * lim
xup10 = roll_sum(upl.astype(float), 10)[0] > 0
xdn5 = roll_sum(dnl.astype(float), 5)[0] > 0
mkt = np.nanmean(ret, axis=1)                                    # equal-weight close-to-close market return (known at the close of t)
mkt[~np.isfinite(mkt)] = 0.0
print(f"[rc] data {D} x {S}; train {TR}; ({time.time() - t00:.0f}s)", flush=True)


def seg_stats(net, ew, expo, turn, nn, sl):
    x, b = net[sl], ew[sl]
    m = np.isfinite(x)
    x, b = x[m], b[m]
    if x.size < 5:
        return {}
    nav = np.cumprod(1 + x)
    mdd = float((nav / np.maximum.accumulate(nav) - 1).min())
    ann, vol = float(x.mean() * 252), float(x.std() * np.sqrt(252))
    ex = x - b
    c = np.concatenate([[0.0], np.cumsum(x)])
    w20 = float((c[20:] - c[:-20]).min()) if x.size > 20 else float("nan")
    return {"ann": ann, "vol": vol, "sharpe": ann / vol if vol > 0 else float("nan"), "mdd": mdd, "calmar": ann / abs(mdd) if mdd < 0 else float("nan"),
            "total": float(nav[-1] - 1), "ex_ann": float(ex.mean() * 252), "ex_sharpe": float(ex.mean() / ex.std() * np.sqrt(252)) if ex.std() > 0 else float("nan"),
            "ex_total": float(ex.sum()), "expo": float(expo[sl][m].mean()), "turn": float(turn[sl][m].mean()), "names": float(nn[sl][m].mean()), "worst20": w20, "n": int(x.size)}


def paired(a, b, sl):
    d = (a - b)[sl]
    d = d[np.isfinite(d)]
    if d.size < 20 or not d.std() > 0:
        return {"ann": float("nan"), "t": float("nan")}
    return {"ann": float(d.mean() * 252), "t": float(d.mean() / d.std() * np.sqrt(d.size))}


# ------------------------------------------------------------------ risk exposures, neutralisation bases, risk model
IND = sorted(set(industry.tolist()))
DUM = (industry[:, None] == np.asarray(IND)[None, :]).astype(np.float64)       # (S, I); unmapped names are their own group
STY = {"size": lfc, "vol": vol20, "liq": amt20, "mom": mom20}


def zs_row(x, valid):
    out = np.zeros_like(x)
    v = x[valid]
    if v.size > 10:
        lo, hi = np.quantile(v, [0.01, 0.99])
        v = np.clip(v, lo, hi)
        sd = v.std()
        out[valid] = (v - v.mean()) / sd if sd > 0 else 0.0
    return out


def exposures(t, styles):
    valid = np.ones(S, dtype=bool)
    for s_ in styles:
        valid &= np.isfinite(STY[s_][t])
    cols = [DUM] + [zs_row(STY[s_][t], valid)[:, None] for s_ in styles]
    return valid, np.concatenate(cols, axis=1)


def neutral_basis(styles):
    """Per day an orthonormal basis Q (S, J) of the exposures over the valid names (zero rows elsewhere)."""
    J = DUM.shape[1] + len(styles)
    Q = np.zeros((D, S, J), dtype=np.float32)
    V = np.zeros((D, S), dtype=bool)
    for t in range(D):
        valid, X = exposures(t, styles)
        if valid.sum() < 200:
            continue
        Xv = X[valid]
        Xv = Xv[:, np.abs(Xv).sum(0) > 0]
        q, _ = np.linalg.qr(Xv)
        Q[t][np.ix_(valid, np.arange(q.shape[1]))] = q
        V[t] = valid
    return Q, V


def neutralise(A, Q, V):
    A0 = np.where(V, np.nan_to_num(A, nan=0.0), 0.0).astype(np.float32)
    coef = np.matmul(Q.transpose(0, 2, 1), A0[:, :, None])
    return np.where(V, A0 - np.matmul(Q, coef)[:, :, 0], 0.0)


# ------------------------------------------------------------------ family statistics (rank IC and decile L/S return per day)
def family_stats(F, name):
    p = R / f"famstat_{name}.npz"
    if p.is_file():
        z = np.load(p)
        return z["ic"], z["ls"]
    import torch
    dev = "cuda" if torch.cuda.is_available() else "cpu"
    T = torch.from_numpy(tgt).to(dev)
    ft = torch.isfinite(T)

    def ranks(x, fin):
        o = torch.argsort(torch.where(fin, x, torch.full_like(x, float("inf"))), dim=1, stable=True)
        rk = torch.empty_like(o)
        rk.scatter_(1, o, torch.arange(x.shape[1], device=x.device).expand_as(o))
        return rk.double()

    rt = ranks(T, ft)
    r0 = torch.nan_to_num(T, nan=0.0)
    K = F.shape[0]
    ic, ls = np.full((K, D), np.nan), np.full((K, D), np.nan)
    for k in range(K):
        x = torch.from_numpy(np.asarray(F[k])).to(dev).double()
        fx = torch.isfinite(x)
        rx = ranks(x, fx)
        m = (fx & ft).double()
        n = m.sum(1).clamp(min=1)
        ma, mb = (rx * m).sum(1) / n, (rt * m).sum(1) / n
        da, db = (rx - ma[:, None]) * m, (rt - mb[:, None]) * m
        c = (da * db).sum(1) / torch.sqrt((da * da).sum(1) * (db * db).sum(1)).clamp(min=1e-12)
        ic[k] = torch.where(m.sum(1) > 100, c, torch.full_like(c, float("nan"))).cpu().numpy()
        nx = fx.sum(1)
        kk = torch.floor(nx * 0.1).clamp(min=1)
        lo_, hi_ = (rx < kk[:, None]) & fx, (rx >= (nx - kk)[:, None]) & fx
        v = (r0 * hi_).sum(1) / kk - (r0 * lo_).sum(1) / kk
        ls[k] = torch.where(nx > 100, v, torch.full_like(v, float("nan"))).cpu().numpy()
    np.savez(p, ic=ic, ls=ls)
    return ic, ls


def a_side(name, hl):
    """Every pre-fusion variant's RAW signal: {key: (family, params, signal)}."""
    F = np.load(R / f"fam_{name}.npy", mmap_mode="r")
    w = np.load(R / f"famw_{name}.npy")
    K = F.shape[0]
    t0 = time.time()
    ic, ls = family_stats(F, name)
    sg = np.where(w >= 0, 1.0, -1.0)
    perf_ic = lag((ic * sg[:, None]).T, 2)                       # (D, K): what the family contributed, known at the close of t
    perf_ls = lag((ls * sg[:, None]).T, 2)
    coef = {"base": np.tile(w, (D, 1)), "A0_equal": np.full((D, K), 1.0 / K)}
    meta = {"base": ("base", {}), "A0_equal": ("A0 族等权(尺子)", {})}
    for W_, thr, lvl in GRID_A1:
        m_, s_ = roll_mean(perf_ic, W_, W_ // 2), roll_std(perf_ic, W_, W_ // 2)
        tstat = m_ / np.where(s_ > 0, s_, np.nan) * np.sqrt(W_)
        g = np.where(np.isfinite(tstat) & (tstat < thr), lvl, 1.0)
        key = f"A1_w{W_}_t{thr:g}_l{lvl:g}"
        coef[key], meta[key] = w[None, :] * g, ("A1 族失效门控", {"window": W_, "t_below": thr, "level": lvl, "off_share": float(1 - g[TR:].mean())})
    cum = np.nancumsum(np.nan_to_num(perf_ls, nan=0.0), axis=0)
    sd60 = roll_std(perf_ls, 60, 30) * np.sqrt(60)
    for kst in GRID_A2:
        g = np.ones((D, K))
        peak, on, back = cum[0].copy(), np.ones(K, dtype=bool), np.zeros(K)
        for t in range(D):
            peak = np.where(on, np.maximum(peak, cum[t]), peak)
            dd = peak - cum[t]
            stop = on & np.isfinite(sd60[t]) & (dd > kst * sd60[t])
            back = np.where(stop, cum[t] + 0.5 * dd, back)       # re-enter once half the drawdown is recovered
            on = on & ~stop
            again = ~on & ~stop & (cum[t] >= back)
            peak = np.where(again, cum[t], peak)
            on = on | again
            g[t] = on
        key = f"A2_k{kst:g}"
        coef[key], meta[key] = w[None, :] * g, ("A2 族回撤止损", {"k": kst, "off_share": float(1 - g[TR:].mean())})
    v60 = roll_std(perf_ls, 60, 30)
    ref = np.nanmedian(v60[:TR])
    coef["A3_invvol"] = w[None, :] * np.clip(ref / np.where(v60 > 0, v60, np.nan), 0.5, 2.0)
    coef["A3_invvol"] = np.where(np.isfinite(coef["A3_invvol"]), coef["A3_invvol"], w[None, :])
    meta["A3_invvol"] = ("A3 族波动倒数加权", {})
    keys = list(coef)
    acc = {k: np.zeros((D, S), dtype=np.float32) for k in keys}
    seen = np.zeros((D, S), dtype=bool)
    aw = np.abs(w)
    m1, m2, m0 = np.zeros((D, S)), np.zeros((D, S)), np.zeros((D, S))
    NB = {}
    if "A5" not in SKIP:
        for spec, styles in SPEC_A5.items():
            NB[spec] = neutral_basis(styles)
        print(f"[rc] {name}: neutralisation bases ({time.time() - t0:.0f}s)", flush=True)
    XN = {spec: np.zeros((K, TR * S), dtype=np.float32) for spec in NB}
    for k in range(K):
        x = np.asarray(F[k])
        fin = np.isfinite(x)
        x0 = np.where(fin, x, np.float32(0))
        seen |= fin
        for key in keys:
            acc[key] += coef[key][:, k].astype(np.float32)[:, None] * x0
        sx = sg[k] * x0.astype(np.float64)
        m1 += aw[k] * sx
        m2 += aw[k] * sx * sx
        m0 += aw[k] * fin
        for spec, (Q, V) in NB.items():
            XN[spec][k] = neutralise(x[:TR], Q[:TR], V[:TR]).reshape(-1)
        if (k + 1) % 25 == 0:
            print(f"[rc] {name}: A pass {k + 1}/{K} ({time.time() - t0:.0f}s)", flush=True)
    out = {}
    for key in keys:
        out[key] = (*meta[key], np.where(seen, acc[key].astype(np.float64), np.nan))
    mean = m1 / np.maximum(m0, 1e-12)
    std = np.sqrt(np.clip(m2 / np.maximum(m0, 1e-12) - mean * mean, 0, None))
    for lam in GRID_A4:
        out[f"A4_l{lam:g}"] = ("A4 分歧惩罚", {"lambda": lam}, np.where(seen & (m0 > 0.5 * aw.sum()), mean - lam * std, np.nan))
    raw = out["base"][2]
    y = r[:TR].reshape(-1).astype(np.float32)
    for spec, (Q, V) in NB.items():
        out[f"A5_{spec}_keepw"] = ("A5 族因子中性化", {"spec": spec, "weights": "original"}, np.where(V & seen, neutralise(raw, Q, V), np.nan))
        X = XN[spec]
        G, b = (X @ X.T).astype(np.float64), (X @ y).astype(np.float64)
        try:
            w2 = np.linalg.solve(G, b)
        except np.linalg.LinAlgError:
            w2 = np.linalg.pinv(G, rcond=1e-10) @ b
        blend2 = np.zeros((D, S), dtype=np.float32)
        for k in range(K):
            blend2 += np.float32(w2[k]) * np.nan_to_num(np.asarray(F[k]), nan=0.0)
        out[f"A5_{spec}_refit"] = ("A5 族因子中性化", {"spec": spec, "weights": "refit on neutralised families", "weight_corr_with_original": float(np.corrcoef(w, w2)[0, 1])},
                                   np.where(V & seen, neutralise(blend2.astype(np.float64), Q, V), np.nan))
        del X
    print(f"[rc] {name}: A side {len(out)} signals ({time.time() - t0:.0f}s)", flush=True)
    return out


# ------------------------------------------------------------------ B2: constrained mean-variance
_B2 = {}


def b2_prepare(sm, ew):
    """Factor risk model + alpha, per rebalance day.  Everything a child process needs goes into _B2 (inherited by fork)."""
    styles = ["size", "vol", "liq", "mom"]
    J = DUM.shape[1] + len(styles)
    f = np.full((D, J), np.nan)
    sv = np.full(S, np.nan)
    a_ = 1 - 0.5 ** (1 / 60.0)
    rebal = set(range(120, D, B2_EVERY))
    prevX, prevV = None, None
    z = np.full((D, S), np.nan)
    fin = np.isfinite(sm)
    mu, sd = np.nanmean(sm, 1, keepdims=True), np.nanstd(sm, 1, keepdims=True)
    z = np.clip((sm - mu) / np.where(sd > 0, sd, np.nan), -3, 3)
    pct = pct_rows(sm)
    cand_all = fin & (pct > 1 - B2_CAND)
    # alpha inside the candidate set, from the training period: excess = a + s * z
    m = cand_all[:TR] & np.isfinite(tgt[:TR])
    yy = (tgt[:TR] - ew[:TR, None])[m]
    zz = z[:TR][m]
    s_ = float(np.cov(zz, yy)[0, 1] / zz.var())
    a0 = float(yy.mean() - s_ * zz.mean())
    mu_m = float(np.nanmean(ew[:TR]))
    days = {}
    for t in range(1, D):
        valid, X = exposures(t, styles)
        if prevX is not None:
            m_ = prevV & np.isfinite(ret[t])
            if m_.sum() > 500:
                beta, *_ = np.linalg.lstsq(prevX[m_], ret[t][m_], rcond=None)
                f[t] = beta
                u = np.full(S, np.nan)
                u[m_] = ret[t][m_] - prevX[m_] @ beta
                u2 = u * u
                sv = np.where(np.isfinite(u2), np.where(np.isfinite(sv), a_ * u2 + (1 - a_) * sv, u2), sv)
        prevX, prevV = X, valid
        if t in rebal:
            ff = f[max(0, t - 249):t + 1]
            ff = ff[np.isfinite(ff).all(1)]
            if ff.shape[0] < 60:
                continue
            Fc = np.cov(ff.T) + 1e-8 * np.eye(J)
            c = np.flatnonzero(cand_all[t] & valid)
            if c.size < 50:
                continue
            med, hi = np.nanmedian(sv), np.nanquantile(sv, 0.9)
            d = np.where(np.isfinite(sv[c]), 0.5 * sv[c] + 0.5 * med, hi)
            bench = DUM[fin[t]].mean(0)
            days[t] = {"c": c, "X": X[c], "G": np.linalg.cholesky(Fc).T, "d": d, "alpha": mu_m + a0 + s_ * z[t, c], "ind": DUM[c], "bench": bench,
                       "cap": B2_CAP_MULT / max(1.0, np.floor(fin[t].sum() * TOP))}
    _B2.update(days=days, base=top_book(sm, np.maximum(1, np.floor(fin.sum(1) * TOP).astype(int))), alpha_fit={"slope": s_, "intercept": a0, "market": mu_m})
    return _B2["alpha_fit"]


def b2_cell(cell):
    import cvxpy as cp
    lam, bud, dl = cell
    days = _B2["days"]
    W = _B2["base"].astype(np.float32).copy()
    first = min(days) if days else D
    prev = np.zeros(S)
    cur = None
    fails = 0
    for t in range(first, D):
        if t in days:
            q = days[t]
            n = q["c"].size
            w = cp.Variable(n)
            risk = cp.sum_squares(q["G"] @ (q["X"].T @ w)) + cp.sum_squares(cp.multiply(np.sqrt(q["d"]), w))
            obj = q["alpha"] @ w - 0.5 * lam * risk - (COST / B2_H) * cp.norm1(w - prev[q["c"]])
            cons = [w >= 0, w <= q["cap"], (cp.sum(w) == 1) if bud == "full" else (cp.sum(w) <= 1)]
            if dl is not None:
                cons += [cp.abs(q["ind"].T @ w - q["bench"] * cp.sum(w)) <= dl]
            prob = cp.Problem(cp.Maximize(obj), cons)
            try:
                prob.solve(solver=cp.OSQP, eps_abs=1e-6, eps_rel=1e-6, max_iter=20000, warm_start=True)
                ok = w.value is not None and prob.status in ("optimal", "optimal_inaccurate")
            except Exception:
                ok = False
            if not ok:
                try:
                    prob.solve(solver=cp.CLARABEL)
                    ok = w.value is not None
                except Exception:
                    ok = False
            if ok:
                x = np.clip(np.asarray(w.value).ravel(), 0, None)
                x[x < 1e-5] = 0.0
                if bud == "full" and x.sum() > 0:
                    x = x / x.sum()
                elif x.sum() > 1:
                    x = x / x.sum()
                cur = np.zeros(S)
                cur[q["c"]] = x
                prev = cur
            else:
                fails += 1
        if cur is not None:
            W[t] = cur
    return cell, W, fails


# ------------------------------------------------------------------ the study, per champion
def run(name):
    hl = CHAMPS[name]
    t0 = time.time()
    raw = np.load(PARTURA_ROOT / "runs" / "_forward" / f"signal_{name}_{base['end']}.npy").astype(np.float64)
    sm = ema_rows(raw, hl)
    fin = np.isfinite(sm)
    k10 = np.maximum(1, np.floor(fin.sum(1) * TOP).astype(int))
    ok = fin & np.isfinite(tgt)
    cnt = ok.sum(1)
    ew = np.where(cnt > 0, np.where(ok, tgt, 0.0).sum(1) / np.maximum(cnt, 1), np.nan)
    W0 = top_book(sm, k10)
    live = (W0.sum(1) > 0) & np.isfinite(ew)                    # the two last days have no label yet
    res, series, makers = {}, {}, {}

    def book(W, e=None):
        if e is not None:
            W = W * e[:, None]
        traded = np.abs(np.diff(W, axis=0, prepend=np.zeros((1, S)))).sum(1)
        net = (W * r).sum(1) - COST * traded
        return np.where(live, net, np.nan), W.sum(1), 0.5 * traded, (W > 0).sum(1).astype(float)

    def add(key, family, params, W=None, e=None, maker=None, keep=False):
        if W is None:
            W = maker()
        net, expo, turn, nn = book(W, e)
        res[key] = {"family": family, "params": params, "stats": {s: seg_stats(net, ew, expo, turn, nn, sl) for s, sl in SEG.items()}}
        series[key] = net
        if maker is not None or keep:
            makers[key] = maker if maker is not None else (lambda W=W: W)
        return net

    add("base", "基线(满仓、前 10% 等权)", {"halflife": hl}, W=W0, keep=True)
    b = res["base"]["stats"]
    print(f"[rc] {name}: baseline excess {b['oos']['ex_ann']:+.2%} / {b['oos']['ex_sharpe']:.2f} oos (stored: see two_level_forward); total {b['oos']['ann']:+.1%} / sharpe {b['oos']['sharpe']:.2f} / mdd {b['oos']['mdd']:.1%}", flush=True)

    # ---- A: before the fusion
    if "A" not in SKIP:
        A = a_side(name, hl)
        chk = A.pop("base")[2]
        both = np.isfinite(chk) & np.isfinite(raw)
        res["base"]["params"]["a_side_rebuild_max_rel_err"] = float(np.max(np.abs(chk[both] - raw[both]) / (np.abs(raw[both]) + 1e-6)))
        for key, (family, params, sig) in A.items():
            s2 = ema_rows(sig, hl)
            add(key, family, params, maker=(lambda s2=s2: top_book(s2, k10)))
            makers[key + "#sm"] = s2
        del A
        print(f"[rc] {name}: A books ({time.time() - t0:.0f}s)", flush=True)

    # ---- B1: stock-level screens and risk weights
    pv, pc, pm = pct_rows(np.where(fin, vol20, np.nan)), pct_rows(np.where(fin, ltc, np.nan)), pct_rows(np.where(fin, mom20, np.nan))
    SCR = {"B1_xlimup10": ("B1 剔近 10 日涨停", {}, xup10), "B1_xlimdn5": ("B1 剔近 5 日跌停", {}, xdn5), "B1_lowprice": ("B1 剔低价(<2 元)", {}, rawpx < 2.0)}
    for q in GRID_Q:
        SCR[f"B1_volhi_q{q:g}"] = ("B1 剔高波动", {"q": q}, pv > 1 - q)
        SCR[f"B1_caplo_q{q:g}"] = ("B1 剔最小市值", {"q": q}, pc < q)
        SCR[f"B1_momhi_q{q:g}"] = ("B1 剔近 20 日涨幅最高", {"q": q}, pm > 1 - q)
    for key, (family, params, bad) in SCR.items():
        params = dict(params, removed_share_of_book=float((W0 > 0)[TR:][bad[TR:]].sum() / max((W0 > 0)[TR:].sum(), 1)))
        add(key, family, params, maker=(lambda bad=bad: top_book(np.where(bad, np.nan, sm), k10)))
    vq = np.nanquantile(np.where(fin, vol20, np.nan), [0.1, 0.9], axis=1)
    iv = 1.0 / np.clip(np.where(np.isfinite(vol20), vol20, vq[1][:, None]), vq[0][:, None], vq[1][:, None])
    add("B1w_invvol", "B1w 权重 ∝ 1/波动", {}, maker=lambda: top_book(sm, k10, iv))
    add("B1w_invvar", "B1w 权重 ∝ 1/波动", {"power": 2}, maker=lambda: top_book(sm, k10, iv * iv))
    print(f"[rc] {name}: B1 ({time.time() - t0:.0f}s)", flush=True)

    # ---- B3: exposure rules on the baseline book
    net0 = series["base"]
    idx = np.cumprod(1 + mkt)
    sv_ = lag(roll_std(np.nan_to_num(net0, nan=0.0)[:, None], 20, 20), 2)[:, 0] * np.sqrt(252)
    q5 = pct_rows(lag(ltc, 1))
    spread5 = roll_sum((np.nanmean(np.where(q5 <= 0.2, ret, np.nan), 1) - np.nanmean(np.where(q5 > 0.8, ret, np.nan), 1))[:, None], 5)[0][:, 0]
    ldb = np.nansum(dnl, 1) / np.maximum(np.isfinite(ret).sum(1), 1)
    csd = roll_mean(np.nanstd(ret, axis=1)[:, None], 20, 20)[:, 0]
    csd_pct = pd.Series(csd).rolling(250, min_periods=120).apply(lambda v: (v[-1] >= v).mean(), raw=True).to_numpy()

    def hold(cond, n=5):                                         # stays on until the condition has been off for n days
        out, left = np.zeros(D, dtype=bool), 0
        for t in range(D):
            left = n if cond[t] else max(left - 1, 0)
            out[t] = cond[t] or left > 0
        return out

    def exposure(kind, p, lvl):
        if kind == "tv":
            return np.where(np.isfinite(sv_) & (sv_ > 0), np.round(np.minimum(1.0, p / np.where(sv_ > 0, sv_, 1.0)), 1), 1.0)
        if kind == "trend":
            ma = roll_mean(idx[:, None], p, p)[:, 0]
            return np.where(np.isfinite(ma) & (idx < ma), lvl, 1.0)
        if kind == "stamp":
            c = {"sp3": spread5 < -0.03, "sp5": spread5 < -0.05, "ld3": ldb > 0.03, "ld5": ldb > 0.05, "any": (spread5 < -0.05) | (ldb > 0.05)}[p]
            return np.where(hold(np.nan_to_num(c, nan=0).astype(bool)), lvl, 1.0)
        if kind == "disp":
            return np.where(np.nan_to_num(csd_pct, nan=0.0) >= p, lvl, 1.0)
        if kind == "owndd":
            e, nav, peak, st = np.ones(D), 1.0, 1.0, 1.0
            x = np.nan_to_num(net0, nan=0.0)
            for t in range(D):
                if t >= 2:
                    nav *= 1 + e[t - 2] * x[t - 2]
                peak = max(peak, nav)
                dd = nav / peak - 1
                st = lvl if (st == 1.0 and dd < -p) else (1.0 if (st < 1.0 and dd > -p / 2) else st)
                e[t] = st
            return e
        raise ValueError(kind)

    FAM3 = {"tv": "B3a 目标波动", "trend": "B3b 市场趋势", "stamp": "B3c 踩踏识别", "owndd": "B3d 自身回撤", "disp": "B3e 截面离散度"}
    EXPO = {}
    for kind, p, lvl in GRID_B3:
        key = f"B3_{kind}_{p}" + ("" if lvl is None else f"_l{lvl:g}")
        EXPO[key] = exposure(kind, p, lvl)
        add(key, FAM3[kind], {"param": p, "level": lvl}, W=W0, e=EXPO[key])
    print(f"[rc] {name}: B3 ({time.time() - t0:.0f}s)", flush=True)

    # ---- B2: optimiser
    if "B2" not in SKIP:
        fit = b2_prepare(sm, np.nan_to_num(ew, nan=0.0))
        print(f"[rc] {name}: B2 risk model ready, {len(_B2['days'])} rebalances, alpha fit {fit} ({time.time() - t0:.0f}s)", flush=True)
        import multiprocessing as mp
        with mp.get_context("fork").Pool(min(WORKERS, len(GRID_B2))) as pool:
            for (lam, bud, dl), W, fails in pool.imap_unordered(b2_cell, GRID_B2):
                key = f"B2_lam{lam:g}_{bud}" + ("" if dl is None else f"_ind{dl:g}")
                Wd = W.astype(np.float64)
                add(key, "B2 组合优化", {"lambda": lam, "budget": bud, "industry_dev": dl, "failed_solves": fails, "alpha_fit": fit}, W=Wd, keep=True)
        print(f"[rc] {name}: B2 ({time.time() - t0:.0f}s)", flush=True)

    # ---- selection (in-sample only) and verdicts
    def score(k):
        s_ = res[k]["stats"]["insample"]
        return float(np.sqrt(max(s_.get("calmar", 0) or 0, 0) * max(s_.get("sharpe", 0) or 0, 0)))

    b_in = res["base"]["stats"]["insample"]
    fams = {}
    for k, v in res.items():
        if k != "base" and "尺子" not in v["family"]:
            fams.setdefault(v["family"], []).append(k)
    picks = {}
    for fam, ks in fams.items():
        best = max(ks, key=score)
        s_ = res[best]["stats"]["insample"]
        picks[fam] = {"key": best, "passes_insample": bool(s_["calmar"] > b_in["calmar"] or s_["sharpe"] > b_in["sharpe"]), "score": score(best), "base_score": score("base")}
        res[best]["picked"] = True

    # ---- C: stacks of the in-sample picks
    ok_ = lambda fam: fam in picks and picks[fam]["passes_insample"]            # noqa: E731
    scr = [picks[f]["key"] for f in picks if f.startswith("B1 ") and ok_(f) and score(picks[f]["key"]) > score("base")]
    bad_all = np.zeros((D, S), dtype=bool)
    for k in scr:
        bad_all |= SCR[k][2]
    b3 = [picks[f]["key"] for f in picks if f.startswith("B3") and ok_(f) and score(picks[f]["key"]) > score("base")]
    b3best = max(b3, key=score) if b3 else None
    e_all = np.minimum.reduce([EXPO[k] for k in b3]) if b3 else None
    a_ok = [picks[f]["key"] for f in picks if f.startswith("A") and ok_(f) and score(picks[f]["key"]) > score("base")]
    abest = max(a_ok, key=score) if a_ok else None
    stacks = {}
    if scr:
        Wc = top_book(np.where(bad_all, np.nan, sm), k10)
        add("C1_screens", "C 叠加", {"screens": scr}, W=Wc)
        if b3best:
            add("C2_screens+expo", "C 叠加", {"screens": scr, "exposure": b3best}, W=Wc, e=EXPO[b3best])
            add("C2b_screens+allexpo", "C 叠加", {"screens": scr, "exposure": b3}, W=Wc, e=e_all)
    if abest:
        sA = makers[abest + "#sm"]
        Wa = top_book(np.where(bad_all, np.nan, sA), k10)
        add("C3_A+screens", "C 叠加", {"A": abest, "screens": scr}, W=Wa)
        if b3best:
            add("C4_A+screens+expo", "C 叠加", {"A": abest, "screens": scr, "exposure": b3best}, W=Wa, e=EXPO[b3best])
    if "B2 组合优化" in picks and b3best:
        add("C5_opt+expo", "C 叠加", {"B2": picks["B2 组合优化"]["key"], "exposure": b3best}, W=makers[picks["B2 组合优化"]["key"]](), e=EXPO[b3best])
    stacks = {"screens": scr, "exposure_best": b3best, "exposure_all": b3, "A_best": abest}

    # ---- paired readings against the baseline
    o = SEG["oos"]
    for k, v in res.items():
        if k == "base":
            continue
        v["paired"] = {s: paired(series[k], net0, sl) for s, sl in SEG.items() if s != "stampede"}
        v["dsharpe_oos_ci90"] = boot_dsharpe(series[k][o], net0[o])
        v["dsharpe_insample_ci90"] = boot_dsharpe(series[k][SEG["insample"]], net0[SEG["insample"]])
        so, bo = v["stats"]["oos"], res["base"]["stats"]["oos"]
        v["dmdd_oos"] = so["mdd"] - bo["mdd"]
        useful = (v["dsharpe_oos_ci90"][0] > 0) or (so["mdd"] > bo["mdd"] * 0.75 and so["ann"] >= bo["ann"] - 0.02)
        v["verdict"] = "有用" if useful else ("降风险换收益" if so["mdd"] > bo["mdd"] and so["sharpe"] <= bo["sharpe"] else ("夏普更高、未过判据" if so["sharpe"] > bo["sharpe"] else "没有"))
    keep = {"base"} | {p["key"] for p in picks.values()} | {k for k in res if k.startswith("C")}
    r5 = lambda a: [None if x != x else round(float(x), 7) for x in a]           # noqa: E731
    print(f"[rc] {name}: done, {len(res)} books ({time.time() - t0:.0f}s)", flush=True)
    return {"halflife": hl, "books": res, "picks": picks, "stacks": stacks, "series": {k: r5(series[k]) for k in keep}, "bench": r5(ew), "market_cc": r5(mkt)}


with slot():
    mem = MemoryGuard(self_limit_gb=60, cgroup_limit_gb=80).start()
    out = {"tag": TAG, "dates": [str(d) for d in dates], "segments": {k: [str(dates[v.start]), str(dates[v.stop - 1])] for k, v in SEG.items()},
           "grids": {"A1": GRID_A1, "A2": GRID_A2, "A4": GRID_A4, "A5": SPEC_A5, "q": GRID_Q, "B2": GRID_B2, "B3": GRID_B3,
                     "B2_const": {"every": B2_EVERY, "candidates": B2_CAND, "cap_mult": B2_CAP_MULT, "cost_horizon": B2_H}}, "champions": {}}
    n_books = 0
    for name in names:
        out["champions"][name] = run(name)
        n_books += len(out["champions"][name]["books"])
        (R / f"risk_control_{TAG}.json").write_text(json.dumps(out, ensure_ascii=False, default=float), encoding="utf-8")
    Ledger(PARTURA_ROOT / "runs" / "_forward" / "ledger.json").record(
        "forward", n_books, f"risk control R001 ({TAG}): {n_books} books on {', '.join(names)}; parameters picked in-sample only (research/risk_control/PLAN.md)", f"risk_control_{TAG}")
    mem.stop()
print(f"[rc] wrote {R / f'risk_control_{TAG}.json'} ({time.time() - t00:.0f}s)")
