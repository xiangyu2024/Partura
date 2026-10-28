"""C04 diagnostic (server, in-sample only): why can a seed's fused book be far below each of its heads?

The view ends 20230807 (train + valid), so the test period is never loaded.  For the given (arm, seed) pairs, the heads
that research/coldstart_C04/final_fix.json attributes to that seed are rebuilt exactly as c04_final.py does (sign x EMA at
the chosen half-life, residual on the five controls); printed: each head's sign, the pairwise daily rank correlation on
train (every 5th day, as c04_final's rho), and the train / valid long-book Sharpe of each head and of their equal-weight
z-rank fusion (the per-seed primary's construction).

    source tmp/c04_env.sh; $PY scripts/server/c04_fusion_diag.py B:701 A:708 ...
"""
import json
import os
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2]))
import numpy as np  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
X = json.loads((PARTURA_ROOT / "research" / "coldstart_C04" / "final_fix.json").read_text(encoding="utf-8"))
want = [(a.split(":")[0], int(a.split(":")[1])) for a in sys.argv[1:]]

from alphacube.plugins import load_plugins  # noqa: E402
load_plugins(["partura.ac_plugin"])
ps = PanelSet(STORE, "20180102", "20230807", warmup=60, device="cuda", gpu_fraction=0.5, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
              workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
              daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "C00_base.yaml")
aux = ps.compute({"known": G.spec["pool"][0]["expr"], "liq": "cross_mean(day_sum(Amt), 30)", "vol": "cross_mean(day_std(Ret), 20)",
                  "rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "size": "LogFloatCap"})
QF = steer.neutral_basis([aux["liq"], aux["vol"], aux["rev"], aux["known"], aux["size"]])
tgt = ps.target(1)
dates = np.asarray(ps.dates).astype(str)
tr, va = slice(0, int(np.searchsorted(dates, "20220101"))), slice(int(np.searchsorted(dates, "20220101")), len(dates))


def rho(a, b):
    ok = np.isfinite(a) & np.isfinite(b)
    x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
    n = np.maximum(ok.sum(1), 1)
    with np.errstate(invalid="ignore", divide="ignore"):
        c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
    return float(np.nanmean(c))


for arm, seed in want:
    H = [h for h in X["arms"][arm]["heads"] if h["seed"] == seed]
    P = ps.compute({f"h{i}": h["expr"] for i, h in enumerate(H)})
    SM = [steer.neutral_residual(float(h["sign"]) * bk.smoothed(np.asarray(P[f"h{i}"], np.float64), float(h["hl"])), QF) for i, h in enumerate(H)]
    Z = [dg._zrank(s) for s in SM]
    print(f"== arm {arm} seed {seed}: {len(H)} heads")
    for i, (h, s) in enumerate(zip(H, SM)):
        print(f"  h{i} sign {h['sign']:+.0f} hl {h['hl']:g}  train {bk.book_row(s, tgt, tr)['long_sharpe']:+.2f} valid {bk.book_row(s, tgt, va)['long_sharpe']:+.2f} | {h['expr'][:110]}")
    for i in range(len(H)):
        print("  rho(train) " + " ".join(f"{rho(Z[i][:tr.stop:5], Z[j][:tr.stop:5]):+.2f}" for j in range(len(H))))
    ok = np.sum([np.isfinite(z) for z in Z], 0)
    fz = np.where(ok > 0, np.nansum(Z, 0) / np.maximum(ok, 1), np.nan)
    print(f"  fused: train {bk.book_row(fz, tgt, tr)['long_sharpe']:+.2f} valid {bk.book_row(fz, tgt, va)['long_sharpe']:+.2f}")
