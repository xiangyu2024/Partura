"""PROD W02L, the new synthesis of research/prod_W02L/SYNTH_PLAN.md (written before anything here ran): the W02L heads admitted
by their marginal contribution inside the head pool of C_LX.  Server; `source tmp/w02l_env.sh` first.

    python scripts/w02l_synth.py build [--fit-end 20251231|20230807]
        base B = C_LX (AlphaCube as is, built already); pool P = each day's top 30% by B; candidates = the 79 deduplicated W02L
        heads.  On the fit segment, inside P: greedy admission by the t of the daily cross-sectional coefficient (label demeaned
        in the pool on [B, admitted, candidate]), |t| >= 2, at most 20; then pooled OLS weights; S = z(B) + 1[P] * sum b_h z(h) / b_B.
        -> runs/prod_W02L/two_level/S{,_nested}.npy (full length; the fit never sees a day after --fit-end) and .json
    python scripts/w02l_synth.py describe
        books on the view cut at 2025-12-31 only (nothing of 2026): S and C_LX in sample, S_nested vs C_LX on valid (biased toward
        the heads, description only) -> research/prod_W02L/synth.{json,md}
    python scripts/w02l_synth.py forward
        the plan's test, on days after 2026-09-16 only (refuses while the store has fewer than 60 of them); ledgered "forward".
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(int(os.environ.get("PARTURA_THREADS", 16)))
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.splits import Ledger  # noqa: E402

argv = sys.argv[1:]
MODE = argv[0] if argv else ""
if MODE not in ("build", "describe", "forward"):
    raise SystemExit(__doc__)
assert os.environ.get("PARTURA_RANK_FIRST") == "1" and os.environ.get("PARTURA_STUDY_DIR") == "prod_W02L", "source tmp/w02l_env.sh first"
AC = Path(os.environ.get("ALPHACUBE_ROOT", "/root/autodl-tmp/AlphaCube"))
sys.path.insert(0, str(AC / "scripts"))
D = PARTURA_ROOT / "research" / "prod_W02L"
W = PARTURA_ROOT / "runs" / "prod_W02L" / "two_level"
LEDGER = D / "ledger_prod.json"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
START, END, LAST, VALID, TEST_END = "20180102", "20260916", "20251231", "20230808", "20260916"
POOL_FRAC, T_MIN, K_MAX, FWD_MIN_DAYS = 0.30, 2.0, 20, 60          # SYNTH_PLAN.md, fixed in advance


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


def key(e):
    import hashlib
    return hashlib.sha1(e.encode()).hexdigest()[:20]


def view_dates(end):
    from alphacube.research import warmed_view
    from alphacube.store import open_cube_store
    view, _ = warmed_view(open_cube_store(STORE), START, end, warmup=60)
    return view, np.asarray([str(d) for d in view.dates])


def label(view):
    from alphacube.label import Label, open_vwap15
    return Label("open_vwap15", 1, buyable=True).compute(view, price=open_vwap15(view)).astype(np.float64)


def zrows(x):
    from alphacube.metrics import zscore_rows
    return zscore_rows(np.asarray(x, np.float64))


def pool_mask(zb):
    """each day's top POOL_FRAC of B (among the names B ranks)."""
    r = dg.rank_rows(zb)                                            # ranks 1..n per row (AlphaCube), NaN where B is NaN
    n = np.isfinite(r).sum(axis=1, keepdims=True)
    pct = r / np.maximum(n, 1)
    return np.nan_to_num(pct, nan=-1.0) > 1.0 - POOL_FRAC


# ---------------------------------------------------------------------------------------------------------------- build
def build():
    fit_end = opt("--fit-end", LAST)
    name = "S" if fit_end == LAST else "S_nested"
    cut_view, cut_dates = view_dates(LAST)                          # the label from the view cut at 2025-12-31: no 2026 price
    y_cut = label(cut_view)
    n_fit = int(np.searchsorted(cut_dates, fit_end, side="right"))
    assert cut_dates[n_fit - 1] <= fit_end, "calendar"
    B = np.load(W / "C_LX.npy").astype(np.float64)                 # full length (2018-01-02 .. 2026-09-16)
    n_all, S_ = B.shape
    assert y_cut.shape == (len(cut_dates), S_), (y_cut.shape, B.shape)
    zb = zrows(B)
    ic = dg.ic_row(zb[:n_fit], y_cut[:n_fit], target_ranks=dg.rank_rows(y_cut[:n_fit]))
    if np.isfinite(ic["rank_ic"]) and ic["rank_ic"] < 0:
        zb = -zb
    P = pool_mask(zb)
    heads = json.loads((D / "library" / "W_dedup.json").read_text(encoding="utf-8"))["kept"]
    H = np.stack([zrows(np.load(W / "_signals" / f"{key(h['expr'])}.npy")) for h in heads]).astype(np.float32)   # (m, n_all, S)
    m = len(heads)
    print(f"[synth] {name}: fit 20180102..{cut_dates[n_fit - 1]} ({n_fit} days), {m} candidates, pool top {POOL_FRAC:.0%}", flush=True)

    # per fit day: the pool rows with a label, label demeaned in the pool, B and the candidates (NaN -> 0 = the day's mean)
    days = []
    for d in range(n_fit):
        idx = np.flatnonzero(P[d] & np.isfinite(y_cut[d]) & np.isfinite(zb[d]))
        if idx.size < 50:
            continue
        y = y_cut[d, idx] - y_cut[d, idx].mean()
        b = zb[d, idx] - zb[d, idx].mean()
        h = np.nan_to_num(H[:, d, idx].T.astype(np.float64), nan=0.0)
        h -= h.mean(axis=0)
        days.append((y, b, h))
    print(f"[synth] {len(days)} fit days with a pool", flush=True)

    admitted, log = [], []
    for step in range(K_MAX):
        rest = [j for j in range(m) if j not in admitted]
        coefs = np.full((len(days), len(rest)), np.nan)
        for t, (y, b, h) in enumerate(days):
            X = np.column_stack([b] + [h[:, j] for j in admitted])
            Q, _ = np.linalg.qr(X)
            ry = y - Q @ (Q.T @ y)
            Hr = h[:, rest]
            RH = Hr - Q @ (Q.T @ Hr)
            den = (RH * RH).sum(axis=0)
            ok = den > 1e-12
            coefs[t, ok] = (RH[:, ok] * ry[:, None]).sum(axis=0) / den[ok]
        mu, sd, nn = np.nanmean(coefs, 0), np.nanstd(coefs, 0), np.isfinite(coefs).sum(0)
        tstat = np.where(sd > 0, mu / sd * np.sqrt(nn), 0.0)
        k = int(np.nanargmax(np.abs(tstat)))
        best = {"step": step + 1, "head": heads[rest[k]]["expr"], "D": heads[rest[k]]["D"], "t": float(tstat[k]), "coef_mean": float(mu[k])}
        print(f"[synth]   step {step + 1}: best |t| {abs(tstat[k]):.2f} ({heads[rest[k]]['expr'][:90]})", flush=True)
        if abs(tstat[k]) < T_MIN:
            log.append({**best, "admitted": False})
            break
        admitted.append(rest[k])
        log.append({**best, "admitted": True})

    # pooled OLS weights on [B, admitted]
    k1 = 1 + len(admitted)
    XtX, Xty = np.zeros((k1, k1)), np.zeros(k1)
    for y, b, h in days:
        X = np.column_stack([b] + [h[:, j] for j in admitted])
        XtX += X.T @ X
        Xty += X.T @ y
    beta = np.linalg.solve(XtX, Xty)
    if not beta[0] > 0:
        raise SystemExit(f"B's own weight is not positive ({beta[0]}): the plan's S is not defined")
    tilt = np.zeros_like(zb)
    for i, j in enumerate(admitted):
        tilt += beta[1 + i] / beta[0] * np.nan_to_num(H[j].astype(np.float64), nan=0.0)
    S = zb + np.where(P, tilt, 0.0)
    S[~np.isfinite(zb)] = np.nan
    np.save(W / f"{name}.npy", S.astype(np.float32))
    out = {"plan": "research/prod_W02L/SYNTH_PLAN.md", "name": name, "fit": [START, str(cut_dates[n_fit - 1])], "fit_days": len(days),
           "pool_frac": POOL_FRAC, "t_min": T_MIN, "k_max": K_MAX, "candidates": m, "B_orientation_rank_ic": float(ic["rank_ic"]),
           "steps": log, "admitted": [{"expr": heads[j]["expr"], "D": heads[j]["D"], "weight_over_B": float(beta[1 + i] / beta[0])}
                                      for i, j in enumerate(admitted)], "beta_B": float(beta[0])}
    (W / f"{name}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[synth] {name}: {len(admitted)} heads admitted -> {W / (name + '.npy')}", flush=True)


# ---------------------------------------------------------------------------------------------------------------- books
def paired_books(sigs, tgt, fit, SEG):
    from alphacube.metrics import long_short_weights, portfolio_returns

    def stats(x):
        f = x[np.isfinite(x)]
        if f.size < 20 or not f.std() > 0:
            return {"ann": float("nan"), "t": float("nan"), "n": int(f.size)}
        return {"ann": float(f.mean() * 252), "t": float(f.mean() / f.std() * np.sqrt(f.size)), "n": int(f.size)}

    res, daily = {}, {}
    for name, sig in sigs.items():
        ic = dg.ic_row(sig[fit], tgt[fit], target_ranks=dg.rank_rows(tgt[fit]))
        sig = (-1.0 if np.isfinite(ic["rank_ic"]) and ic["rank_ic"] < 0 else 1.0) * sig
        b = bk.books(sig, tgt, fit, SEG)
        L, S_ = b["by_rank"]["long"], b["by_rank"]["ls"]
        res[name] = {"hl_long": L["hl"], "hl_ls": S_["hl"],
                     "long": {k: {m_: float(v[m_]) for m_ in ("long_ann", "long_sharpe", "long_mdd", "long_turnover")} for k, v in L["splits"].items()},
                     "ls": {k: {m_: float(v[m_]) for m_ in ("ls_ann", "ls_sharpe")} for k, v in S_["splits"].items()}}
        sm_lo, sm_ls = bk.smoothed(sig, L["hl"]), bk.smoothed(sig, S_["hl"])
        daily[name] = {"excess": bk.long_book(long_short_weights(sm_lo, bk.TOP_FRAC), sm_lo, tgt)[0],
                       "ls": portfolio_returns(long_short_weights(sm_ls, bk.TOP_FRAC), tgt, bk.COST)[0]}
    return res, daily, stats


def describe():
    cut_view, cut_dates = view_dates(LAST)
    tgt = label(cut_view)
    n = len(cut_dates)
    ix = lambda d_: int(np.searchsorted(cut_dates, d_))            # noqa: E731
    out = {"plan": "research/prod_W02L/SYNTH_PLAN.md", "note": "description only; nothing of 2026", "runs": {}}
    for nm in ("S", "S_nested"):
        f = W / f"{nm}.json"
        if f.is_file():
            out["runs"][nm] = json.loads(f.read_text(encoding="utf-8"))
    with slot():
        mem = MemoryGuard(self_limit_gb=150, cgroup_limit_gb=850).start()
        # (1) S vs C_LX in sample (both fitted to 2025-12-31): how much the tilt moves the book
        sigs = {nm: np.load(W / f"{nm}.npy")[:n].astype(np.float64) for nm in ("C_LX", "S")}
        us = slice(0, n)
        res1, d1, stats = paired_books(sigs, tgt, us, {"insample": us, "valid": slice(ix(VALID), n)})
        out["insample"] = {"books": res1, "paired": {k: {s: stats((d1["S"][k] - d1["C_LX"][k])[sl]) for s, sl in
                                                          (("insample", us), ("valid", slice(ix(VALID), n)))} for k in ("excess", "ls")}}
        # (2) S_nested vs C_LX on valid (the head layer fitted to 2023-08-07; biased toward the heads)
        if (W / "S_nested.npy").is_file():
            sigs = {nm: np.load(W / f"{nm}.npy")[:n].astype(np.float64) for nm in ("C_LX", "S_nested")}
            tr, va = slice(0, ix(VALID)), slice(ix(VALID), n)
            res2, d2, _ = paired_books(sigs, tgt, tr, {"train": tr, "valid": va})
            out["nested"] = {"books": res2, "paired": {k: {"valid": stats((d2["S_nested"][k] - d2["C_LX"][k])[va])} for k in ("excess", "ls")}}
        mem.stop()
    (D / "synth.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    (D / "synth.md").write_text(report(out), encoding="utf-8")
    print((D / "synth.md").read_text(encoding="utf-8"))


def report(out):
    L = ["# W02L 新合成(头部边际贡献)的样本内描述(2026 未读)\n", "做法见 SYNTH_PLAN.md。下面全是描述，不是检验;检验要等 2026-09-16 以后的新数据。\n"]
    for nm, r in out["runs"].items():
        L.append(f"## {nm}:拟合 {r['fit'][0]} ~ {r['fit'][1]},收了 {len(r['admitted'])} 个 head(候选 {r['candidates']})\n")
        L += ["| 步 | |t| | 收 | head |", "|---|---|---|---|"]
        for s in r["steps"]:
            L.append(f"| {s['step']} | {abs(s['t']):.2f} | {'是' if s['admitted'] else '否'} | `{s['head'][:100]}` |")
        if r["admitted"]:
            L.append("\n权重(相对 B):" + ";".join(f"{a['weight_over_B']:+.3f}" for a in r["admitted"]) + "\n")
    for part, title in (("insample", "S 与 C_LX(都拟合到 2025-12-31)"), ("nested", "S_nested(头部层拟合到 2023-08-07)与 C_LX,valid 段(偏向新 head)")):
        if part not in out:
            continue
        L += [f"\n## {title}\n", "| 信号 | hl | 段 | 纯多头净超额 | 夏普 | 回撤 |", "|---|---|---|---|---|---|"]
        for nm, b in out[part]["books"].items():
            for seg, x in b["long"].items():
                L.append(f"| {nm} | {b['hl_long']:g} | {seg} | {x['long_ann']:+.1%} | {x['long_sharpe']:.2f} | {x['long_mdd']:.1%} |")
        L.append("\n成对差(纯多头逐日净超额):" + ";".join(f"{seg} {v['ann']:+.2%}(t {v['t']:+.2f})" for seg, v in out[part]["paired"]["excess"].items()))
        L.append("多空成对差:" + ";".join(f"{seg} {v['ann']:+.2%}(t {v['t']:+.2f})" for seg, v in out[part]["paired"]["ls"].items()) + "\n")
    return "\n".join(L) + "\n"


# ---------------------------------------------------------------------------------------------------------------- forward
def forward():
    view, dates = view_dates(time.strftime("%Y%m%d"))
    new = np.flatnonzero(dates > TEST_END)
    if new.size < FWD_MIN_DAYS:
        raise SystemExit(f"{new.size} trading days after {TEST_END} in the store; SYNTH_PLAN wants >= {FWD_MIN_DAYS} before the first read")
    raise SystemExit("forward read: the signals must first be extended past 2026-09-16 (w02l_two_level signals on the longer view, "
                     "then C_LX and S rebuilt with the same fits); not written yet -- there is no such data today")


if __name__ == "__main__":
    {"build": build, "describe": describe, "forward": forward}[MODE]()
