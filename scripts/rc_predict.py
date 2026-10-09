"""Risk control R002 (research/risk_control/PLAN_R002.md): PREDICT the market's extreme falls, and gate bad stocks.

Server, CPU.  Inputs from scripts/rc_prepare.py (runs/_risk/, incl. px_open).  Everything is walk-forward: a model at
day t is fitted only on rows whose labels were realised by t, refitted on a schedule; predictions start at day 500.

    rc_predict.py [--only 手写库冠军] [--tag p1] [--skip M|S]

  M  market crash probability (2 targets x {logit, gbm, unfitted composite}) -> exposure (own-history quantile x level)
  S  a LightGBM "bad stock" model on each champion's candidates (2 horizons) -> hard gate (q) / soft penalty (lambda)
  X  the in-sample picks stacked, and the conditional gate (gate only on days M flags)
Writes runs/_risk/risk_control_<tag>.json in the format of scripts/risk_control.py (scripts/rc_table.py reads it), plus
"diagnostics": the predictors' own quality (AUC, what happened after a flag), kept apart from the trading result.
"""
import json
import sys
import time
import warnings
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(16)
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.splits import Ledger  # noqa: E402

warnings.filterwarnings("ignore")
argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


R = Path(opt("--dir")) if opt("--dir") else PARTURA_ROOT / "runs" / "_risk"
if not R.is_absolute():
    R = PARTURA_ROOT / R
TAG = opt("--tag", "p1")
SKIP = set((opt("--skip") or "").split(",")) - {""}
CHAMPS = {"手写库冠军": 20.0, "挖掘冠军": 10.0}
names = [n for n in (opt("--only") or ",".join(CHAMPS)).split(",") if n]
COST, TOP, T0 = 0.0015, 0.10, 500

# ------------------------------------------------------------------ grids (fixed before any result)
M_TARGETS = {"f5": ("fwd5 < -5%", 5), "m10": ("10-day trough < -8%", 10)}
M_MODELS = ("logit", "gbm", "composite")
M_USE = [(q, lvl) for q in (0.8, 0.9) for lvl in (0.5, 0.0)]
M_REFIT, M_HOLD = 20, 3
S_H = (1, 5)
S_USE = [("hard", q) for q in (0.1, 0.2, 0.3)] + [("soft", lam) for lam in (0.1, 0.3)]
S_REFIT, S_CAND, S_BAD, S_SMOOTH = 250, 0.70, 0.10, 3.0


# ------------------------------------------------------------------ tools (as in scripts/risk_control.py)
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
    out[k:] = x[:-k]
    return out


def pct_rows(x):
    return pd.DataFrame(x).rank(axis=1, pct=True).to_numpy()


def ema_rows(x, hl):
    from alphacube.metrics import ema_rows as f
    return f(x, hl) if hl else np.asarray(x, dtype=np.float64)


def top_book(score, k, weight=None):
    D_, S_ = score.shape
    fin = np.isfinite(score)
    n = fin.sum(1)
    order = np.argsort(np.where(fin, score, np.inf), axis=1, kind="stable")
    pos = np.arange(S_)[None, :]
    kk = np.minimum(k, n)
    sel_sorted = (pos >= (n - kk)[:, None]) & (pos < n[:, None]) & (n >= 2)[:, None]
    sel = np.zeros((D_, S_), dtype=bool)
    np.put_along_axis(sel, order, sel_sorted, axis=1)
    w = sel.astype(np.float64)
    return np.where(w.sum(1, keepdims=True) > 0, w / np.maximum(w.sum(1, keepdims=True), 1e-300), 0.0)


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
    exn = np.cumprod(1 + ex)
    return {"ann": ann, "vol": vol, "sharpe": ann / vol if vol > 0 else float("nan"), "mdd": mdd, "calmar": ann / abs(mdd) if mdd < 0 else float("nan"),
            "total": float(nav[-1] - 1), "ex_ann": float(ex.mean() * 252), "ex_sharpe": float(ex.mean() / ex.std() * np.sqrt(252)) if ex.std() > 0 else float("nan"),
            "ex_total": float(ex.sum()), "ex_mdd": float((exn / np.maximum.accumulate(exn) - 1).min()), "expo": float(expo[sl][m].mean()), "turn": float(turn[sl][m].mean()),
            "names": float(nn[sl][m].mean()), "worst20": float((c[20:] - c[:-20]).min()) if x.size > 20 else float("nan"), "n": int(x.size)}


def paired(a, b, sl):
    d = (a - b)[sl]
    d = d[np.isfinite(d)]
    if d.size < 20 or not d.std() > 0:
        return {"ann": float("nan"), "t": float("nan")}
    return {"ann": float(d.mean() * 252), "t": float(d.mean() / d.std() * np.sqrt(d.size))}


def auc(y, p):
    from sklearn.metrics import roc_auc_score
    m = np.isfinite(y) & np.isfinite(p)
    if m.sum() < 50 or y[m].min() == y[m].max():
        return float("nan")
    return float(roc_auc_score(y[m], p[m]))


# ------------------------------------------------------------------ data
t00 = time.time()
base = json.loads((R / "base.json").read_text(encoding="utf-8"))
dates = np.asarray(base["dates"])
D, S = len(dates), len(base["symbols"])
ix = lambda d: int(np.searchsorted(dates, d))                   # noqa: E731
TR = base["train_stop"]
SEG = {"insample": slice(T0, TR), "test": slice(TR, ix("20260101")), "forward": slice(ix("20260101"), ix("20260917")), "oos": slice(TR, ix("20260917")), "stampede": slice(ix("20240116"), ix("20240207"))}
tgt = np.load(R / "target.npy")
r = np.nan_to_num(tgt, nan=0.0)
ld = lambda k: np.load(R / f"px_{k}.npy").astype(np.float64)    # noqa: E731
close, opn, high, low, amt, ltc, lfc, lim, rawpx = ld("close"), ld("open"), ld("high"), ld("low"), ld("amt"), ld("ltc"), ld("lfc"), ld("limit"), ld("rawprice")
ret = close / lag(close, 1) - 1.0
ret = np.where(np.abs(ret) < 0.45, ret, np.nan)
fr = np.isfinite(ret)
nfr = np.maximum(fr.sum(1), 1)
frac = lambda c: (c & fr).sum(1) / nfr                          # noqa: E731
vol20 = roll_std(ret, 20, 10)
upl, dnl = ret >= 0.95 * lim, ret <= -0.95 * lim
overnight, intraday = opn / lag(close, 1) - 1.0, close / opn - 1.0
mkt = np.nan_to_num(np.nanmean(ret, axis=1), nan=0.0)
ewt = np.nanmean(tgt, axis=1)                                    # the tradable equal-weight market, row t = t+1 open -> t+2 open
ewt0 = np.nan_to_num(ewt, nan=0.0)
r1 = lambda x, w: roll_sum(x[:, None], w)[0][:, 0]               # noqa: E731
m1 = lambda x, w: roll_mean(x[:, None], w, w)[:, 0]              # noqa: E731
print(f"[rp] data {D} x {S} ({time.time() - t00:.0f}s)", flush=True)


# ------------------------------------------------------------------ M: market features, targets, walk-forward models
def market_features():
    f = {}
    idx = np.cumprod(1 + mkt)
    for w in (1, 5, 20, 60):
        f[f"r{w}"] = r1(mkt, w)
    for w in (5, 20, 60):
        f[f"vol{w}"] = roll_std(mkt[:, None], w, w)[:, 0]
    f["vol5_60"] = f["vol5"] / f["vol60"]
    f["semi20"] = np.sqrt(m1(np.minimum(mkt, 0) ** 2, 20))
    s_idx = pd.Series(idx)
    f["dd60"] = idx / s_idx.rolling(60, min_periods=20).max().to_numpy() - 1
    f["ma20"], f["ma60"] = idx / m1(idx, 20) - 1, idx / m1(idx, 60) - 1
    cdf = pd.DataFrame(close)
    fc = np.isfinite(close)
    fcn = np.maximum(fc.sum(1), 1)
    f["above20"] = ((close > roll_mean(close, 20, 10)) & fc).sum(1) / fcn
    f["above60"] = ((close > roll_mean(close, 60, 30)) & fc).sum(1) / fcn
    f["newlow20"] = ((close <= cdf.rolling(20, min_periods=10).min().to_numpy()) & fc).sum(1) / fcn
    f["adv"] = frac(ret > 0)
    f["adv5"] = m1(f["adv"], 5)
    f["ldb"], f["lub"] = frac(dnl), frac(upl)
    f["ldb5"], f["lub5"] = m1(f["ldb"], 5), m1(f["lub"], 5)
    f["bigdn"], f["bigup"] = frac(ret < -0.05), frac(ret > 0.05)
    f["bigdn5"] = m1(f["bigdn"], 5)
    csd = np.nanstd(ret, axis=1)
    f["csd"], f["csd20"] = csd, m1(csd, 20)
    f["csd_pct"] = pd.Series(f["csd20"]).rolling(250, min_periods=120).apply(lambda v: (v[-1] >= v).mean(), raw=True).to_numpy()
    z = (ret - np.nanmean(ret, 1, keepdims=True)) / np.where(csd > 0, csd, np.nan)[:, None]
    f["skew5"] = m1(np.nan_to_num(np.nanmean(z ** 3, axis=1), nan=0.0), 5)
    q5 = pct_rows(lag(ltc, 1))
    small, big = q5 <= 0.2, q5 > 0.8
    sb = np.nan_to_num(np.nanmean(np.where(small, ret, np.nan), 1) - np.nanmean(np.where(big, ret, np.nan), 1), nan=0.0)
    f["sb1"], f["sb5"], f["sb20"] = sb, r1(sb, 5), r1(sb, 20)
    a0 = np.nan_to_num(amt, nan=0.0)
    tot = a0.sum(1)
    share = (a0 * (q5 <= 0.5)).sum(1) / np.maximum(tot, 1)
    f["small_amt_share"] = share
    f["small_amt_share_d20"] = share - lag(m1(share, 20)[:, None], 1)[:, 0]
    lt = np.log(np.maximum(tot, 1))
    f["amt_vs60"], f["amt5_20"] = lt - np.log(np.maximum(m1(tot, 60), 1)), np.log(np.maximum(m1(tot, 5), 1)) - np.log(np.maximum(m1(tot, 20), 1))
    f["comove"] = f["vol20"] ** 2 / np.maximum(np.nanmean(vol20 ** 2, axis=1), 1e-12)
    f["overnight5"] = r1(np.nan_to_num(np.nanmean(overnight, 1), nan=0.0), 5)
    f["intraday5"] = r1(np.nan_to_num(np.nanmean(intraday, 1), nan=0.0), 5)
    to = amt / np.exp(lfc)
    st = np.nanmedian(np.where(small, to, np.nan), axis=1)
    f["small_turn_heat"] = st / m1(np.nan_to_num(st, nan=np.nanmedian(st)), 250)
    return pd.DataFrame(f)


def expanding_z(x, minp=250):
    s = pd.Series(x)
    return ((s - s.expanding(minp).mean()) / s.expanding(minp).std()).to_numpy()


def market_models(F):
    """{(target, model): p (D,)} -- walk-forward probabilities; and the targets themselves."""
    from sklearn.ensemble import HistGradientBoostingClassifier
    from sklearn.impute import SimpleImputer
    from sklearn.linear_model import LogisticRegression
    from sklearn.pipeline import make_pipeline
    from sklearn.preprocessing import StandardScaler
    c = np.concatenate([[0.0], np.cumsum(ewt0)])
    fwd5 = c[np.minimum(np.arange(D) + 5, D)] - c[:-1]
    cum = np.stack([c[np.minimum(np.arange(D) + k, D)] - c[:-1] for k in range(1, 11)], axis=1)
    Y = {"f5": np.where(np.arange(D) + 5 <= D - 2, (fwd5 < -0.05).astype(float), np.nan),
         "m10": np.where(np.arange(D) + 10 <= D - 2, (cum.min(1) < -0.08).astype(float), np.nan)}
    X = F.replace([np.inf, -np.inf], np.nan).to_numpy()
    comp = np.nanmean(np.stack([expanding_z(F["vol20"]), expanding_z(F["ldb5"]), -expanding_z(F["sb5"]), expanding_z(F["csd_pct"]), -expanding_z(F["above20"]),
                                -expanding_z(F["dd60"]), expanding_z(F["bigdn5"])]), axis=0)
    P = {}
    for tk, (_, h) in M_TARGETS.items():
        y = Y[tk]
        P[(tk, "composite")] = np.where(np.arange(D) >= T0, comp, np.nan)
        for mk in ("logit", "gbm"):
            p = np.full(D, np.nan)
            model = None
            for t in range(T0, D):
                if (t - T0) % M_REFIT == 0:
                    rows = np.arange(60, t - h - 1)                 # label rows of the last training day are realised by t
                    rows = rows[np.isfinite(y[rows])]
                    if y[rows].sum() >= 5:
                        model = (make_pipeline(SimpleImputer(strategy="median"), StandardScaler(), LogisticRegression(C=0.1, class_weight="balanced", max_iter=2000)) if mk == "logit"
                                 else HistGradientBoostingClassifier(max_depth=3, max_iter=100, learning_rate=0.05, l2_regularization=1.0, random_state=0))
                        model.fit(X[rows], y[rows])
                if model is not None:
                    p[t] = model.predict_proba(X[t:t + 1])[0, 1]
            P[(tk, mk)] = p
    return P, Y, fwd5


def flag_of(p, q):
    thr = pd.Series(p[T0:]).expanding(120).quantile(q).shift(1).to_numpy()
    fl = np.zeros(D, dtype=bool)
    fl[T0:] = np.nan_to_num(p[T0:], nan=-np.inf) > np.where(np.isfinite(thr), thr, np.inf)
    out, left = np.zeros(D, dtype=bool), 0
    for t in range(D):
        left = M_HOLD if fl[t] else max(left - 1, 0)
        out[t] = fl[t] or left > 0
    return fl, out


def episodes(y, fwd5, flag_raw, sl):
    """Out-of-sample event episodes (event days at most 5 apart): were they flagged, and how early?"""
    ev = np.flatnonzero(np.nan_to_num(y, nan=0.0)[sl] > 0) + sl.start
    out, cur = [], []
    for t in ev:
        if cur and t - cur[-1] > 5:
            out.append(cur)
            cur = []
        cur.append(t)
    if cur:
        out.append(cur)
    res = []
    for e in out:
        a, b = e[0], e[-1]
        res.append({"start": str(dates[a]), "end": str(dates[b]), "worst_fwd5": float(fwd5[a:b + 1].min()), "flagged_day_before_first": bool(flag_raw[max(a - 1, 0)]),
                    "flagged_on_first": bool(flag_raw[a]), "share_of_episode_flagged": float(flag_raw[a:b + 1].mean()), "flagged_in_prior_5d": bool(flag_raw[max(a - 5, 0):a].any())})
    return res


# ------------------------------------------------------------------ S: stock features and the bad-stock model
def stock_features(sigpct):
    cdf, rdf = pd.DataFrame(close), pd.DataFrame(ret)
    mk = mkt[:, None]
    er, em = roll_mean(ret, 60, 30), roll_mean(mk, 60, 60)
    beta = (roll_mean(ret * mk, 60, 30) - er * em) / np.maximum(roll_std(mk, 60, 60) ** 2, 1e-12)
    v60 = roll_std(ret, 60, 30)
    mu, sd = roll_mean(ret, 20, 10), vol20
    to20 = roll_mean(amt, 20, 5) / np.exp(lfc)
    f = {"vol5": roll_std(ret, 5, 4), "vol20": vol20, "semi20": np.sqrt(roll_mean(np.minimum(ret, 0) ** 2, 20, 10)),
         "mom5": close / lag(close, 5) - 1, "mom20": close / lag(close, 20) - 1, "mom60": close / lag(close, 60) - 1,
         "dd60": close / cdf.rolling(60, min_periods=20).max().to_numpy() - 1, "maxret20": rdf.rolling(20, min_periods=10).max().to_numpy(), "minret20": rdf.rolling(20, min_periods=10).min().to_numpy(),
         "to20": to20, "to5_20": roll_mean(amt, 5, 3) / np.exp(lfc) / np.where(to20 > 0, to20, np.nan), "lfc": lfc, "ltc": ltc, "price": rawpx,
         "amihud": roll_mean(np.abs(ret) / np.where(amt > 0, amt, np.nan), 20, 10),
         "skew20": (roll_mean(ret ** 3, 20, 10) - 3 * mu * roll_mean(ret ** 2, 20, 10) + 2 * mu ** 3) / np.where(sd > 0, sd, np.nan) ** 3,
         "beta60": beta, "ivol60": np.sqrt(np.clip(v60 ** 2 - beta ** 2 * roll_std(mk, 60, 60) ** 2, 0, None)),
         "nup20": roll_sum(upl.astype(float), 20)[0], "ndn20": roll_sum(dnl.astype(float), 20)[0], "zero20": roll_sum(np.where(fr, (ret == 0).astype(float), np.nan), 20)[0],
         "gap20": roll_mean(overnight, 20, 10), "intra5": roll_sum(intraday, 5)[0], "age": np.minimum(np.cumsum(np.isfinite(close), axis=0), 500).astype(float),
         "range20": roll_mean(high / low - 1, 20, 10), "sig": sigpct, "dsig5": sigpct - lag(sigpct, 5)}
    names_ = list(f)
    X = np.stack([pct_rows(np.where(np.isfinite(close), f[k], np.nan)).astype(np.float32) for k in names_], axis=-1)      # (D, S, K) cross-sectional percentiles
    return names_, X


def bad_model(name, sm, ew, X, fnames, h):
    """Walk-forward P(next-h-day excess in the universe's worst 10 %) for the champion's candidates: (D, S), NaN elsewhere."""
    import lightgbm as lgb
    sigpct = pct_rows(sm)
    cand = np.nan_to_num(sigpct, nan=0.0) > S_CAND
    ex = tgt - ew[:, None]
    ex0 = np.nan_to_num(ex, nan=0.0)
    c = np.concatenate([np.zeros((1, S)), np.cumsum(ex0, 0)])
    fx = np.where(np.isfinite(tgt), c[np.minimum(np.arange(D) + h, D)] - c[:-1], np.nan)
    fx[max(D - h - 1, 0):] = np.nan
    y = (pct_rows(fx) <= S_BAD).astype(np.float32)
    y[~np.isfinite(fx)] = np.nan
    y_top = (pct_rows(fx) > 1 - S_BAD).astype(np.float32)          # post hoc (S2): the mirror target, to take the volatility out of "bad"
    pb = np.full((D, S), np.nan, dtype=np.float32)
    pt = np.full((D, S), np.nan, dtype=np.float32)
    imp = None
    for t in range(T0, D, S_REFIT):
        tr = np.zeros((D, S), dtype=bool)
        tr[60:t - h - 1] = cand[60:t - h - 1] & np.isfinite(y[60:t - h - 1])
        model = lgb.LGBMClassifier(n_estimators=200, max_depth=4, num_leaves=15, learning_rate=0.05, subsample=0.8, subsample_freq=1, colsample_bytree=0.8,
                                   min_child_samples=200, n_jobs=16, verbose=-1, random_state=0)
        model.fit(X[tr], y[tr])
        hi = min(t + S_REFIT, D)
        te = np.zeros((D, S), dtype=bool)
        te[t:hi] = cand[t:hi]
        pb[te] = model.predict_proba(X[te])[:, 1]
        m2 = lgb.LGBMClassifier(n_estimators=200, max_depth=4, num_leaves=15, learning_rate=0.05, subsample=0.8, subsample_freq=1, colsample_bytree=0.8,
                                min_child_samples=200, n_jobs=16, verbose=-1, random_state=0)
        m2.fit(X[tr], y_top[tr])
        pt[te] = m2.predict_proba(X[te])[:, 1]
        imp = model.feature_importances_
        print(f"[rp] {name}: bad-stock model h={h}, fit at {dates[t]} on {int(tr.sum()):,} rows (base rate {float(y[tr].mean()):.3f})", flush=True)
    top = sorted(zip(fnames, (imp / max(imp.sum(), 1)).tolist()), key=lambda kv: -kv[1])[:8]
    return pb, y, cand, top, pb - pt


# ------------------------------------------------------------------ 6.1: the frozen market model, forward ledger
def track():
    P, Y, fwd5 = market_models(market_features())
    p = P[("f5", "logit")]
    raw, held = flag_of(p, 0.8)
    out = {"spec": "M_f5_logit_q0.8_l0.5 (research/risk_control/FROZEN_M.json)", "last_day": str(dates[-1]), "rows": []}
    ref = PARTURA_ROOT / "runs" / "_risk" / "risk_control_p2.json"
    if ref.is_file():
        old = json.loads(ref.read_text(encoding="utf-8"))
        op = np.asarray([np.nan if v is None else v for v in old["diagnostics"]["market_prob"]["f5_logit"]], dtype=float)
        n = min(len(op), D)
        same = bool(list(old["dates"][:n]) == [str(d) for d in dates[:n]])
        out["overlap_check"] = {"days": int(n), "same_calendar": same, "max_abs_diff_prob": float(np.nanmax(np.abs(op[:n] - p[:n]))) if same else None}
    f0 = ix("20260917")
    for t in range(f0, D):
        out["rows"].append({"date": str(dates[t]), "prob": None if p[t] != p[t] else float(p[t]), "flag": bool(raw[t]), "half_exposure": bool(held[t]),
                            "market_next": None if ewt[t] != ewt[t] else float(ewt[t]), "fwd5": float(fwd5[t]) if t + 5 <= D - 2 else None})
    x = ewt0[f0:]
    e = np.where(held[f0:], 0.5, 1.0)
    if x.size > 20:
        sh = lambda v: float(v.mean() / v.std() * np.sqrt(252)) if v.std() > 0 else float("nan")     # noqa: E731
        f5 = np.asarray([r_["fwd5"] if r_["fwd5"] is not None else np.nan for r_ in out["rows"]])
        fl = np.asarray([r_["flag"] for r_ in out["rows"]])
        out["summary"] = {"days": int(x.size), "flag_share": float(held[f0:].mean()), "market_sharpe": sh(x), "half_on_flag_sharpe": sh(e * x),
                          "fwd5_after_flag": float(np.nanmean(f5[fl])) if fl.any() else None, "fwd5_otherwise": float(np.nanmean(f5[~fl])) if (~fl).any() else None}
    (R / "track_M.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[rp] track: last day {dates[-1]}, {len(out['rows'])} forward days; overlap {out.get('overlap_check')}; summary {out.get('summary')}", flush=True)


# ------------------------------------------------------------------ 6.2: the asymmetric bad-stock prediction as a pool factor
def asym_factor_study():
    import lightgbm as lgb
    sys.path.insert(0, "/root/autodl-tmp/AlphaCube/scripts")
    from combine_two_level import blend, fit_weights
    from alphacube.metrics import cs_pearson, nanmean_quiet, zscore_rows
    t0 = time.time()
    h, cap = 5, 3_000_000
    fnames, X = stock_features(np.full((D, S), np.nan))
    K = X.shape[-1]
    ex0 = np.nan_to_num(tgt - ewt0[:, None], nan=0.0)
    c = np.concatenate([np.zeros((1, S)), np.cumsum(ex0, 0)])
    fx = np.where(np.isfinite(tgt), c[np.minimum(np.arange(D) + h, D)] - c[:-1], np.nan)
    fx[max(D - h - 1, 0):] = np.nan
    pr = pct_rows(fx)
    yb, yt = (pr <= S_BAD).astype(np.float32).ravel(), (pr > 1 - S_BAD).astype(np.float32).ravel()
    fc = np.isfinite(close)
    valid = np.isfinite(fx) & fc
    fac = np.full((D, S), np.nan)
    rng = np.random.default_rng(0)
    Xf = X.reshape(-1, K)
    kw = dict(n_estimators=200, max_depth=4, num_leaves=15, learning_rate=0.05, subsample=0.8, subsample_freq=1, colsample_bytree=0.8, min_child_samples=500, n_jobs=16, verbose=-1, random_state=0)
    for t in range(T0, D, S_REFIT):
        tr = np.zeros((D, S), dtype=bool)
        tr[60:t - h - 1] = valid[60:t - h - 1]
        idx = np.flatnonzero(tr.ravel())
        if idx.size > cap:
            idx = np.sort(rng.choice(idx, cap, replace=False))
        Xt = Xf[idx]
        mb, mt = lgb.LGBMClassifier(**kw).fit(Xt, yb[idx]), lgb.LGBMClassifier(**kw).fit(Xt, yt[idx])
        hi = min(t + S_REFIT, D)
        te = np.zeros((D, S), dtype=bool)
        te[t:hi] = fc[t:hi]
        fac[te] = -(mb.predict_proba(X[te])[:, 1] - mt.predict_proba(X[te])[:, 1])
        print(f"[rp] asym factor: fit at {dates[t]} on {idx.size:,} rows ({time.time() - t0:.0f}s)", flush=True)
    np.save(R / "asym_factor_h5.npy", fac.astype(np.float32))
    seg = {"train_window": slice(T0, TR), "test": SEG["test"], "forward": SEG["forward"], "oos": SEG["oos"]}
    tw = slice(T0, TR)

    def long_excess(sig, hl):
        sm = ema_rows(sig, hl)
        fin = np.isfinite(sm)
        W = top_book(sm, np.maximum(1, np.floor(fin.sum(1) * TOP).astype(int)))
        ok = fin & np.isfinite(tgt)
        ew = np.where(ok.sum(1) > 0, np.where(ok, tgt, 0.0).sum(1) / np.maximum(ok.sum(1), 1), np.nan)
        net = (W * r).sum(1) - COST * np.abs(np.diff(W, axis=0, prepend=np.zeros((1, S)))).sum(1)
        return np.where((W.sum(1) > 0) & np.isfinite(ew), net - ew, np.nan), np.where((W.sum(1) > 0) & np.isfinite(ew), net, np.nan)

    def st(x, sl):
        f = x[sl][np.isfinite(x[sl])]
        return {"ann": float(f.mean() * 252), "sharpe": float(f.mean() / f.std() * np.sqrt(252)), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)} if f.size > 20 and f.std() > 0 else {}

    z = zscore_rows(fac)
    ric = cs_pearson(pct_rows(fac), pct_rows(tgt))
    res = {"factor": {"rank_ic": {k: float(np.nanmean(ric[sl])) for k, sl in seg.items()}, "long_excess_hl5": {k: st(long_excess(fac, 5.0)[0], sl) for k, sl in seg.items()}}, "champions": {}}
    print(f"[rp] asym factor alone: rank IC {res['factor']['rank_ic']}; long excess {res['factor']['long_excess_hl5']}", flush=True)
    if nanmean_quiet(cs_pearson(z[tw], tgt[tw])) < 0:
        z = -z
    for name in names:
        F = np.load(R / f"fam_{name}.npy", mmap_mode="r")
        comp = [np.asarray(F[k], dtype=np.float64) for k in range(F.shape[0])]
        w_orig = np.load(R / f"famw_{name}.npy")
        w100, w101 = fit_weights(comp, tgt, tw, "lstsq"), fit_weights(comp + [z], tgt, tw, "lstsq")
        hl = CHAMPS[name]
        S_ = {"orig": blend(comp, w_orig), "c100_window": blend(comp, w100), "c101_window": blend(comp + [z], w101)}
        E = {k: long_excess(v, hl) for k, v in S_.items()}
        out = {"halflife": hl, "weight_new": float(w101[-1]), "weight_new_vs_abs_median": float(abs(w101[-1]) / np.median(np.abs(w101[:-1]))), "weight_rank_of_new_by_abs": int((np.abs(w101) > abs(w101[-1])).sum() + 1),
               "books": {k: {s_: st(E[k][0], sl) for s_, sl in seg.items()} for k in E},
               "total_oos": {k: (lambda x: {"sharpe": float(np.nanmean(x) / np.nanstd(x) * np.sqrt(252)), "mdd": float((np.cumprod(1 + np.nan_to_num(x)) / np.maximum.accumulate(np.cumprod(1 + np.nan_to_num(x))) - 1).min())})(E[k][1][SEG["oos"]]) for k in E},
               "paired_c101_minus_c100": {s_: st(E["c101_window"][0] - E["c100_window"][0], sl) for s_, sl in seg.items()},
               "paired_c101_minus_orig": {s_: st(E["c101_window"][0] - E["orig"][0], sl) for s_, sl in seg.items()},
               "paired_c100_minus_orig": {s_: st(E["c100_window"][0] - E["orig"][0], sl) for s_, sl in seg.items()}}
        res["champions"][name] = out
        p_ = out["paired_c101_minus_c100"]
        print(f"[rp] {name}: new family weight rank {out['weight_rank_of_new_by_abs']}/101; 101 − 100 (same window): test {p_['test']['ann']:+.2%} (t {p_['test']['t']:+.1f}), forward {p_['forward']['ann']:+.2%} (t {p_['forward']['t']:+.1f}), "
              f"oos {p_['oos']['ann']:+.2%} (t {p_['oos']['t']:+.1f}); 100-window − orig oos {out['paired_c100_minus_orig']['oos']['ann']:+.2%} ({time.time() - t0:.0f}s)", flush=True)
        del comp
    (R / "asym_factor_study.json").write_text(json.dumps(res, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    Ledger(PARTURA_ROOT / "runs" / "_forward" / "ledger.json").record("forward", 2 * len(names) + 1, "risk control R002 section 6.2: asymmetric bad-stock factor added to the champions' pools", "asym_factor_study")


# ------------------------------------------------------------------ the study
def run(name, MK):
    hl = CHAMPS[name]
    t0 = time.time()
    sm = ema_rows(np.load(PARTURA_ROOT / "runs" / "_forward" / f"signal_{name}_{base['end']}.npy").astype(np.float64), hl)
    fin = np.isfinite(sm)
    k10 = np.maximum(1, np.floor(fin.sum(1) * TOP).astype(int))
    ok = fin & np.isfinite(tgt)
    cnt = ok.sum(1)
    ew = np.where(cnt > 0, np.where(ok, tgt, 0.0).sum(1) / np.maximum(cnt, 1), np.nan)
    W0 = top_book(sm, k10)
    live = (W0.sum(1) > 0) & np.isfinite(ew)
    res, series, diag = {}, {}, {}

    def book(W, e=None):
        if e is not None:
            W = W * e[:, None]
        traded = np.abs(np.diff(W, axis=0, prepend=np.zeros((1, S)))).sum(1)
        net = (W * r).sum(1) - COST * traded
        return np.where(live, net, np.nan), W.sum(1), 0.5 * traded, (W > 0).sum(1).astype(float)

    def add(key, family, params, W, e=None):
        net, expo, turn, nn = book(W, e)
        res[key] = {"family": family, "params": params, "stats": {s: seg_stats(net, ew, expo, turn, nn, sl) for s, sl in SEG.items()}}
        series[key] = net

    add("base", "基线(满仓、前 10% 等权)", {"halflife": hl}, W0)
    net0 = series["base"]

    # ---- M
    FLAG = {}
    if MK is not None:
        P, Y, fwd5 = MK
        for (tk, mk), p in P.items():
            for q, lvl in M_USE:
                raw, held = flag_of(p, q)
                key = f"M_{tk}_{mk}_q{q:g}_l{lvl:g}"
                FLAG[key] = (raw, held)
                add(key, f"M 市场下跌预测·{M_TARGETS[tk][0]}", {"target": tk, "model": mk, "quantile": q, "level": lvl, "flag_share_oos": float(held[SEG["oos"]].mean())}, W0, np.where(held, lvl, 1.0))
        print(f"[rp] {name}: M books ({time.time() - t0:.0f}s)", flush=True)

    # ---- S
    GATE = {}
    if "S" not in SKIP:
        sigpct = pct_rows(sm)
        fnames, X = stock_features(sigpct)
        print(f"[rp] {name}: {len(fnames)} stock features ({time.time() - t0:.0f}s)", flush=True)
        held0 = W0 > 0
        for h in S_H:
            pb, y, cand, top, pasym = bad_model(name, sm, np.nan_to_num(ew, nan=0.0), X, fnames, h)
            for pfx, fam_, pb in (("S", "S 坏股票门控", pb), ("S2", "S2 不对称门控(事后):P(最差一成) − P(最好一成)", pasym)):
                pbs = pct_rows(ema_rows(pct_rows(pb), S_SMOOTH))            # percentile among the candidates, smoothed, re-ranked
                o = SEG["oos"]
                ex1 = tgt - ew[:, None]
                inb = held0[o] & np.isfinite(pbs[o]) & np.isfinite(ex1[o])
                hi_ = inb & (pbs[o] > 0.8)
                diag[f"{pfx}_h{h}"] = {"auc_insample_window": auc(y[SEG["insample"]][cand[SEG["insample"]]], pb[SEG["insample"]][cand[SEG["insample"]]]),
                                   "auc_oos": auc(y[o][cand[o]], pb[o][cand[o]]), "top_features": top,
                                   "oos_next_day_excess_bp_in_book": {"predicted_worst_fifth": float(ex1[o][hi_].mean() * 1e4), "rest": float(ex1[o][inb & ~hi_].mean() * 1e4),
                                                                      "share_of_book": float(hi_.sum() / max(inb.sum(), 1))}}
                for kind, v in S_USE:
                    key = f"{pfx}_h{h}_{kind}{v:g}"
                    if kind == "hard":
                        Wg = top_book(np.where(np.nan_to_num(pbs, nan=0.0) > 1 - v, np.nan, sm), k10)
                    else:
                        Wg = top_book(np.where(fin, sigpct - v * np.nan_to_num(pbs, nan=0.0), np.nan), k10)
                    GATE[key] = Wg
                    add(key, f"{fam_}·未来 {h} 天", {"horizon": h, "use": kind, "value": v}, Wg)
                top20 = np.nan_to_num(sigpct, nan=0.0) > 0.8
                half = pct_rows(np.where(top20, pbs, np.nan))
                for lab, m_ in (("worsthalf", half > 0.5), ("besthalf", half <= 0.5)):
                    w_ = np.where(m_ & (np.arange(D) >= T0)[:, None], 1.0, 0.0)
                    w_ = np.where(w_.sum(1, keepdims=True) > 0, w_ / np.maximum(w_.sum(1, keepdims=True), 1), W0)
                    add(f"{pfx}_h{h}_ruler_{lab}", f"{pfx} 尺子(前 20% 按预测对半分)", {"horizon": h, "half": lab}, w_)
            print(f"[rp] {name}: S h={h} books; AUC oos {diag[f'S_h{h}']['auc_oos']:.3f} ({time.time() - t0:.0f}s)", flush=True)
        del X

    # ---- picks (in-sample window only)
    def score(k):
        s_ = res[k]["stats"]["insample"]
        return float(np.sqrt(max(s_.get("calmar", 0) or 0, 0) * max(s_.get("sharpe", 0) or 0, 0)))

    b_in = res["base"]["stats"]["insample"]
    fams = {}
    for k, v in res.items():
        if k != "base" and "尺子" not in v["family"]:
            fams.setdefault(v["family"].split(" ")[0], []).append(k)             # one pick for M, one for S, one for S2
    picks = {}
    for fam, ks in fams.items():
        best = max(ks, key=score)
        s_ = res[best]["stats"]["insample"]
        picks[{"M": "M 市场下跌预测", "S": "S 坏股票门控", "S2": "S2 不对称门控(事后)"}[fam]] = {"key": best, "passes_insample": bool(s_["calmar"] > b_in["calmar"] or s_["sharpe"] > b_in["sharpe"]), "score": score(best), "base_score": score("base")}
        res[best]["picked"] = True
    mp, sp = picks.get("M 市场下跌预测"), picks.get("S 坏股票门控")
    if mp and sp:
        lvl = res[mp["key"]]["params"]["level"]
        raw, held = FLAG[mp["key"]]
        add("X1_M+S", "X 叠加", {"M": mp["key"], "S": sp["key"]}, GATE[sp["key"]], np.where(held, lvl, 1.0))
        for h in S_H:
            add(f"X2_cond_gate_h{h}", "X 条件门控(只在 M 标记的日子用 S,q = 30%)", {"M": mp["key"], "S": f"S_h{h}_hard0.3"}, np.where(held[:, None], GATE[f"S_h{h}_hard0.3"], W0))
    if mp:
        tk = res[mp["key"]]["params"]["target"]
        diag["M_pick_episodes_oos"] = episodes(MK[1][tk], MK[2], FLAG[mp["key"]][0], SEG["oos"])
        diag["M_pick_flag_days_oos"] = [str(dates[t]) for t in np.flatnonzero(FLAG[mp["key"]][0][SEG["oos"]]) + SEG["oos"].start]

    o = SEG["oos"]
    for k, v in res.items():
        if k == "base":
            continue
        v["paired"] = {s: paired(series[k], net0, sl) for s, sl in SEG.items() if s != "stampede"}
        v["dsharpe_oos_ci90"] = boot_dsharpe(series[k][o], net0[o])
        v["dexsharpe_oos_ci90"] = boot_dsharpe(series[k][o] - ew[o], net0[o] - ew[o])
        so, bo = v["stats"]["oos"], res["base"]["stats"]["oos"]
        useful = (v["dsharpe_oos_ci90"][0] > 0) or (so["mdd"] > bo["mdd"] * 0.75 and so["ann"] >= bo["ann"] - 0.02)
        v["verdict"] = "有用" if useful else ("降风险换收益" if so["mdd"] > bo["mdd"] and so["sharpe"] <= bo["sharpe"] else ("夏普更高、未过判据" if so["sharpe"] > bo["sharpe"] else "没有"))
    keep = {"base"} | {p["key"] for p in picks.values()} | {k for k in res if k.startswith(("X", "M_"))}
    r5 = lambda a: [None if x != x else round(float(x), 7) for x in a]           # noqa: E731
    print(f"[rp] {name}: done, {len(res)} books ({time.time() - t0:.0f}s)", flush=True)
    return {"halflife": hl, "books": res, "picks": picks, "stacks": {k: v["params"] for k, v in res.items() if k.startswith("X")}, "series": {k: r5(series[k]) for k in keep},
            "bench": r5(ew), "diagnostics": diag}


if "--track" in argv or "--asym-factor" in argv:
    with slot():
        mem = MemoryGuard(self_limit_gb=60, cgroup_limit_gb=80).start()
        track() if "--track" in argv else asym_factor_study()
        mem.stop()
    raise SystemExit(0)

with slot():
    mem = MemoryGuard(self_limit_gb=60, cgroup_limit_gb=80).start()
    out = {"tag": TAG, "dates": [str(d) for d in dates], "segments": {k: [str(dates[v.start]), str(dates[v.stop - 1])] for k, v in SEG.items()},
           "grids": {"M_targets": M_TARGETS, "M_models": M_MODELS, "M_use": M_USE, "S_h": S_H, "S_use": S_USE}, "champions": {}, "diagnostics": {}}
    MK = None
    if "M" not in SKIP:
        F = market_features()
        P, Y, fwd5 = market_models(F)
        MK = (P, Y, fwd5)
        o, i_ = SEG["oos"], SEG["insample"]
        md = {}
        for (tk, mk), p in P.items():
            raw = flag_of(p, 0.9)[0]
            md[f"{tk}_{mk}"] = {"auc_insample_window": auc(Y[tk][i_], p[i_]), "auc_oos": auc(Y[tk][o], p[o]), "event_rate_insample": float(np.nanmean(Y[tk][i_])), "event_rate_oos": float(np.nanmean(Y[tk][o])),
                                "oos_fwd5_after_flag_q0.9": float(np.nanmean(fwd5[o][raw[o]])) if raw[o].any() else float("nan"), "oos_fwd5_otherwise": float(np.nanmean(fwd5[o][~raw[o]])),
                                "oos_event_days_flagged_share": float(raw[o][np.nan_to_num(Y[tk][o], nan=0.0) > 0].mean()) if (np.nan_to_num(Y[tk][o], nan=0.0) > 0).any() else float("nan"),
                                "oos_flag_share": float(raw[o].mean())}
            print(f"[rp] M {tk}/{mk}: AUC in-sample window {md[f'{tk}_{mk}']['auc_insample_window']:.3f}, oos {md[f'{tk}_{mk}']['auc_oos']:.3f}; fwd5 after a flag {md[f'{tk}_{mk}']['oos_fwd5_after_flag_q0.9']:+.2%} vs {md[f'{tk}_{mk}']['oos_fwd5_otherwise']:+.2%}", flush=True)
        out["diagnostics"]["market"] = md
        out["diagnostics"]["market_episodes_q0.8"] = {f"{tk}_{mk}": episodes(Y[tk], fwd5, flag_of(p, 0.8)[0], o) for (tk, mk), p in P.items()}
        out["diagnostics"]["market_flags_q0.8"] = {f"{tk}_{mk}": [int(x) for x in flag_of(p, 0.8)[1]] for (tk, mk), p in P.items()}
        out["diagnostics"]["market_prob"] = {f"{tk}_{mk}": [None if x != x else round(float(x), 5) for x in p] for (tk, mk), p in P.items()}
        out["diagnostics"]["fwd5"] = [round(float(x), 6) for x in fwd5]
        out["diagnostics"]["market_features"] = list(F.columns)
        print(f"[rp] market models ({time.time() - t00:.0f}s)", flush=True)
    n_books = 0
    for name in names:
        out["champions"][name] = run(name, MK)
        n_books += len(out["champions"][name]["books"])
        (R / f"risk_control_{TAG}.json").write_text(json.dumps(out, ensure_ascii=False, default=float), encoding="utf-8")
    Ledger(PARTURA_ROOT / "runs" / "_forward" / "ledger.json").record(
        "forward", n_books, f"risk control R002 ({TAG}): predicted market falls + bad-stock gate, {n_books} books on {', '.join(names)} (research/risk_control/PLAN_R002.md)", f"risk_control_{TAG}")
    mem.stop()
print(f"[rp] wrote {R / f'risk_control_{TAG}.json'} ({time.time() - t00:.0f}s)")
