"""PROD W02L (research/prod_W02L/PLAN.md): the in-sample backtest of a few expressions under four rulers side by side --
raw (the factor itself, pure long top decile, 15 bp, minus the universe equal weight), A (residual on the five controls),
B (A plus the two champions) and D (B plus decile dummies of size, liquidity and price: a step tilt in one of them, which the
polynomial ruler cannot remove, is removed too) -- each with its own direction and half-life chosen on train.  View 2018-01-02 ~ 2025-12-31
(train to 2023-08-07, valid after): nothing of 2026 is computed.  CPU; the panels come from the shared cache when a round
has computed them already.

    source tmp/w02l_env.sh; python scripts/w02l_backtest.py <file with one expression per line> > out.md
"""
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
os.environ.pop("PARTURA_RANK_DEVICE", None)
os.environ.pop("PARTURA_REWARD_DEVICE", None)
from partura.guard import limit_threads  # noqa: E402

limit_threads(int(os.environ.get("PARTURA_THREADS", 16)))
import json  # noqa: E402

import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import Guidance, RewardContext, neutral_basis  # noqa: E402
from partura.steer import reward as steer_reward  # noqa: E402

START, END, SPLIT = "20180102", "20251231", "20230808"
CHAMPS = {"H": "runs/prod_W01/two_level/champions/signal_手写库冠军_20260916.npy",
          "X": "runs/prod_W01/two_level/champions/signal_挖掘冠军_20260916.npy"}
CHAMP_DATES = "runs/prod_W01/two_level/champions/two_level_forward_20260916.json"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
exprs = [x.strip() for x in open(sys.argv[1], encoding="utf-8") if x.strip()]

from alphacube.plugins import load_plugins  # noqa: E402

load_plugins(["partura.ac_plugin"])
G = Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")
ps = PanelSet(STORE, START, END, warmup=60, device="cpu", cache_dir=str(SHARED_CACHE), mirror_root=MIRROR, workdir=str(PARTURA_ROOT / "tmp"),
              label_kind="open_vwap15", label_buyable=True, batch=8, daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
dates = np.asarray([str(d) for d in ps.dates])
cut = int(np.searchsorted(dates, SPLIT))
tgt = np.array(ps.target(1), np.float64)
tr, va = slice(0, cut), slice(cut, len(dates))
pool_spec, known_spec = G.spec["pool"][-1], G.spec["pool"][0]
aux = ps.compute({"frozen": "cross_max(day_zero_ratio(Ret), 15)", "age": "cross_valid_count(day_last(Close), 241)",
                  "liq": "cross_mean(day_sum(Amt), 30)", "pool": pool_spec["expr"], "known": known_spec["expr"],
                  "n_vol": "cross_mean(day_std(Ret), 20)", "n_rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "n_size": "LogFloatCap",
                  "price": "day_last(Close)"})
cd = [str(d) for d in json.loads((PARTURA_ROOT / CHAMP_DATES).read_text(encoding="utf-8"))["dates"]]
pos = {d: j for j, d in enumerate(cd)}
take = np.array([pos[d] for d in dates])
champ = {k: np.asarray(np.load(PARTURA_ROOT / f, mmap_mode="r"), np.float64)[take] for k, f in CHAMPS.items()}
frozen = np.asarray(aux["frozen"], np.float64)
possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
untradable = ((dg._zrank(frozen) + 0.5) > 0.8) | (np.asarray(aux["age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
pool_sig = dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(aux["pool"], np.float64), float(pool_spec["hl"])))
ctl5 = [aux["liq"], aux["n_vol"], aux["n_rev"], aux["known"], aux["n_size"]]


def band_basis(ctls, bands):
    """ruler B's basis (powers $PARTURA_NEUTRAL_POWERS) plus, per day, dummies of the deciles of each of ``bands``"""
    powers = [int(x) for x in os.environ.get("PARTURA_NEUTRAL_POWERS", "1").split(",")]
    zs = [dg._zrank(np.asarray(c, np.float64)) ** k for c in ctls for k in powers]
    bz = [dg._zrank(np.asarray(b, np.float64)) for b in bands]
    D, S = zs[0].shape
    Q = np.zeros((D, S, 1 + len(zs) + 9 * len(bz)), np.float32)
    for t in range(D):
        ok = np.ones(S, bool)
        for z in zs + bz:
            ok &= np.isfinite(z[t])
        if ok.sum() < 50:
            continue
        cols = [np.ones(int(ok.sum()))] + [z[t][ok] for z in zs]
        for b in bz:
            v = b[t][ok]
            d = np.searchsorted(np.quantile(v, np.linspace(0.1, 0.9, 9)), v, side="right")
            cols += [(d == j).astype(np.float64) for j in range(1, 10)]
        Q[t, ok] = np.linalg.qr(np.column_stack(cols))[0]
    return Q


ctx = {}
for name, ctls in (("raw", None), ("A", ctl5), ("B", ctl5 + [champ["H"], champ["X"]]), ("D", None)):
    c = RewardContext(tgt, tr, va, untradable=untradable, liq=np.asarray(aux["liq"], np.float64), pool=pool_sig, base=pool_sig,
                      halflives=(0.0, 5.0, 20.0))
    if ctls is not None:
        c.neutral_Q = neutral_basis(ctls)
    if name == "D":
        c.neutral_Q = band_basis(ctl5 + [champ["H"], champ["X"]], [aux["n_size"], aux["liq"], aux["price"]])
    ctx[name] = c

print(f"# 样本内回测(train {dates[0]} ~ {dates[cut - 1]},valid {dates[cut]} ~ {dates[-1]};纯多头头部十分位等权、扣 15 bp、减全市场等权)\n")
print("| # | 口径 | 方向 | 半衰期 | train 夏普 | train 年化超额 | valid 夏普 | valid 年化超额 | 日换手 | score |\n|---|---|---|---|---|---|---|---|---|---|")
P = ps.compute({f"e{i}": e for i, e in enumerate(exprs)})
for i, e in enumerate(exprs):
    if f"e{i}" not in P:
        print(f"| {i + 1} | 算不出:{ps.errors.get(f'e{i}', '?')[:80]} |||||||||")
        continue
    for name, c in ctx.items():
        r = steer_reward(np.asarray(P[f"e{i}"], np.float64), c, "long" if name == "raw" else "long_neutral")
        t, v = r["train"], r["valid"]
        print(f"| {i + 1} | {name} | {r['sign']:+.0f} | {r['hl']:.0f} | {t['long_sharpe']:+.2f} | {t['long_ann']:+.1%} | {v['long_sharpe']:+.2f} | "
              f"{v['long_ann']:+.1%} | {t['long_turnover']:.2f} | {r['score']:+.2f} |")
print("\n" + "\n".join(f"{i + 1}. `{e}`" for i, e in enumerate(exprs)))
