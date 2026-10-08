"""What does each reward say about a handful of known expressions?  (calibration before an idea search)

Server.  Builds the search's reward context exactly as scripts/idea_search.py does (view 2018-01 ~ 2023-08-07,
valid from 2022-01) and scores every expression of a YAML file ({name: expr}) under every reward: the level
rewards (pure-long Sharpe, the worse of train and valid) and the paired ones (sized information ratio against the
pool / as a screen on the base).  Reads train / valid only.  Use it to see whether an idea's seeds clear the line
under the reward you are about to hand to the search, and what half-life grid they need.

    python scripts/reward_probe.py studies/<x>/probe.yaml [--halflives 0,5,20,60] [--tag name] [--rewards long,long_bucket]
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


EX = yaml.safe_load((PARTURA_ROOT / argv[0]).read_text(encoding="utf-8"))
EX = {str(k): (v["expr"] if isinstance(v, dict) else str(v)) for k, v in EX.items()}
HL = tuple(float(x) for x in opt("--halflives", "0,5,20").split(","))
KINDS = [k for k in opt("--rewards", ",".join(steer.REWARDS)).split(",") if k in steer.REWARDS]
TAG = opt("--tag", Path(argv[0]).stem)
START, END, SPLIT = "20180102", "20230807", "20220101"

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "B01.yaml")
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", START, END, warmup=60, device="cuda", gpu_fraction=0,
                  cache_dir=str(SHARED_CACHE), mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=8)
    pool_spec, known_spec = G.spec["pool"][-1], G.spec["pool"][0]
    aux = ps.compute({"frozen": "cross_max(day_zero_ratio(Ret), 15)", "age": "cross_valid_count(day_last(Close), 241)",
                      "liq": "cross_mean(day_sum(Amt), 30)", "pool": pool_spec["expr"], "known": known_spec["expr"]})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates)
    cut = int(np.searchsorted(dates, SPLIT))
    frozen = np.asarray(aux["frozen"], np.float64)
    possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
    untradable = ((dg._zrank(frozen) + 0.5) > 0.8) | (np.asarray(aux["age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
    pool_sig = dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(aux["pool"], np.float64), float(pool_spec["hl"])))
    known_z = dg._zrank(float(known_spec["sign"]) * np.asarray(aux["known"], np.float64))
    ctx = steer.RewardContext(tgt, slice(0, cut), slice(cut, len(dates)), untradable=untradable, liq=np.asarray(aux["liq"], np.float64),
                              pool=pool_sig, base=pool_sig, halflives=HL)
    P = ps.compute(EX)
    print(f"[probe] {len(P)}/{len(EX)} panels on {len(dates)} days x {tgt.shape[1]} names; half-lives {HL}; rewards {KINDS}; errors {dict(ps.errors) if ps.errors else 'none'}", flush=True)

    def rho(a, b):                                           # mean daily rank correlation of two z-rank panels (every 5th day)
        a, b = a[::5], b[::5]
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    out = {}
    for name, p in P.items():
        row = {"expr": EX[name], "dist": float(dg.distinct_fraction(p)), "cov": float(np.isfinite(np.asarray(p))[np.isfinite(tgt)].mean())}
        for kind in KINDS:
            r = steer.reward(p, ctx, kind)
            row[kind] = {k: r.get(k) for k in ("score", "sign", "hl", "score_train", "score_valid", "ir_train", "ir_valid", "dann_train", "dann_valid", "screened_share")
                         if r.get(k) is not None} | {"train_sharpe": r["train"]["long_sharpe"], "valid_sharpe": r["valid"]["long_sharpe"],
                                                     "train_ann": r["train"]["long_ann"], "valid_ann": r["valid"]["long_ann"], "turnover": r["train"]["long_turnover"]}
        k0 = KINDS[0]
        z = dg._zrank(bk.smoothed(row[k0]["sign"] * np.asarray(p, np.float64), row[k0]["hl"]))
        row["rho_known"], row["rho_pool"] = rho(z, known_z), rho(z, pool_sig)
        out[name] = row
    mem.stop()

d = PARTURA_ROOT / "runs" / "_ideas"
d.mkdir(parents=True, exist_ok=True)
(d / f"probe_{TAG}.json").write_text(json.dumps({"halflives": HL, "period": [START, END, SPLIT], "results": out}, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print(f"\n{'name':28s} cov  dist | " + " | ".join(f"{k:^30s}" for k in KINDS) + " | ρ已知  ρ池")
print(f"{'':28s}           | " + " | ".join(f"{'score  sg  hl  train / valid':^30s}" for _ in KINDS))
for name, r in out.items():
    cells = []
    for k in KINDS:
        x = r[k]
        cells.append(f"{x['score']:+6.2f} {int(x['sign']):+d} {x['hl']:>3g}  {x['train_sharpe']:+5.2f} / {x['valid_sharpe']:+5.2f}".ljust(30))
    print(f"{name[:28]:28s} {r['cov']:.2f} {r['dist']:.2f} | " + " | ".join(cells) + f" | {r['rho_known']:+.2f} {r['rho_pool']:+.2f}")
print(f"\nwrote runs/_ideas/probe_{TAG}.json ({time.time() - t0:.0f}s)")
