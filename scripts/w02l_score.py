"""W02L: score library expressions with the production ruler, in sample only.  Server (new host).

    source tmp/prod_env.sh
    python scripts/w02l_score.py <in.csv> <out.jsonl> [--shard i/n] [--view w02|w01]

in.csv: columns lib, i, expression (research/prod_W02L/struct/*.csv).  Each expression gets exactly the reward the PROD GP and
the locate tool give a candidate (scripts/c05_locate.py `evaluate`), on one of two views (--view, below; nothing after the
view's end is loaded): rank first, EMA at half-life 0 / 5 / 20, residual on the five controls with
squares and cubes, decile pure-long book net of 15 bp; score = the worse of train and valid net Sharpe; a discovery is score >= 0.5
with |rho| to the known family < 0.5.  One JSON line per expression, appended as it goes: a rerun skips what is already there.
"""
import json
import os
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(int(os.environ.get("PARTURA_THREADS", 8)))
import numpy as np  # noqa: E402
import pandas as pd  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import study  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import Guidance, RewardContext, neutral_basis  # noqa: E402
from partura.steer import reward as steer_reward  # noqa: E402

assert os.environ.get("PARTURA_RANK_FIRST") == "1" and os.environ.get("PARTURA_NEUTRAL_POWERS") == "1,2,3", "source tmp/prod_env.sh first"
IN, OUTF = Path(sys.argv[1]), Path(sys.argv[2])
SH, NSH = (map(int, sys.argv[sys.argv.index("--shard") + 1].split("/")) if "--shard" in sys.argv else (0, 1))
_caps = study.host_caps()
os.environ.update(PARTURA_SLOTS=_caps["PARTURA_SLOTS"], PARTURA_GPU_WAYS=_caps["PARTURA_GPU_WAYS"], PARTURA_REPROMOTE="1")
# --view w01: the W01 / GP view (train 2018 ~ 2021, valid 2022-01 ~ 2023-08-07; reproduces W01's recorded scores).
# --view w02 (default; the user's split of 2026-11-08): train 2018-01-02 ~ 2023-08-07, valid 2023-08-08 ~ 2025-12-31; 2026 is the
# test and is never loaded here.
VIEW = sys.argv[sys.argv.index("--view") + 1] if "--view" in sys.argv else "w02"
START, END, SPLIT = {"w01": ("20180102", "20230807", "20220101"), "w02": ("20180102", "20251231", "20230808")}[VIEW]
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
RHO, THR = 0.5, 0.5
G = Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")

todo = pd.read_csv(IN)
todo = todo.iloc[SH::NSH]
done = set()
if OUTF.is_file():
    done = {json.loads(x)["expression"] for x in OUTF.read_text(encoding="utf-8").splitlines() if x.strip()}
todo = todo[~todo.expression.isin(done)]
print(f"[w02l] {len(todo)} to score (shard {SH}/{NSH}; {len(done)} already in {OUTF.name})", flush=True)
if not len(todo):
    sys.exit(0)

with slot():
    mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 34)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 70))).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    ps = PanelSet(STORE, START, END, warmup=60, device="cuda", gpu_fraction=0.3, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    pool_spec, known_spec = G.spec["pool"][-1], G.spec["pool"][0]
    aux = ps.compute({"frozen": "cross_max(day_zero_ratio(Ret), 15)", "age": "cross_valid_count(day_last(Close), 241)",
                      "liq": "cross_mean(day_sum(Amt), 30)", "pool": pool_spec["expr"], "known": known_spec["expr"],
                      "n_vol": "cross_mean(day_std(Ret), 20)", "n_rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "n_size": "LogFloatCap"})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates)
    assert str(dates[-1]) <= END <= "20251231"
    cut = int(np.searchsorted(dates, SPLIT))
    tr, va = slice(0, cut), slice(cut, len(dates))
    frozen = np.asarray(aux["frozen"], np.float64)
    possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
    untradable = ((dg._zrank(frozen) + 0.5) > 0.8) | (np.asarray(aux["age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
    pool_sig = dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(aux["pool"], np.float64), float(pool_spec["hl"])))
    known_z = dg._zrank(float(known_spec["sign"]) * np.asarray(aux["known"], np.float64))
    ctx = RewardContext(tgt, tr, va, untradable=untradable, liq=np.asarray(aux["liq"], np.float64), pool=pool_sig, base=pool_sig, halflives=(0.0, 5.0, 20.0))
    ctx.neutral_Q = neutral_basis([aux["liq"], aux["n_vol"], aux["n_rev"], aux["known"], aux["n_size"]])
    labelled = np.isfinite(tgt)
    kz = known_z[:cut:5]
    print(f"[w02l] view {VIEW} ({START} ~ {END}, valid from {SPLIT}); context ready in {time.time() - t0:.0f}s: {len(dates)} days x {tgt.shape[1]} names (last {dates[-1]})", flush=True)

    def corr(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    rows = list(todo.itertuples(index=False))
    with OUTF.open("a", encoding="utf-8") as fh:
        for k in range(0, len(rows), 8):
            chunk = rows[k:k + 8]
            P, err = {}, {}
            try:
                P = ps.compute({f"v{j}": r.expression for j, r in enumerate(chunk)})
            except Exception:                                 # noqa: BLE001
                for j, r in enumerate(chunk):
                    try:
                        P[f"v{j}"] = ps.compute({"x": r.expression})["x"]
                    except Exception as exc:                  # noqa: BLE001
                        err[j] = f"{type(exc).__name__}: {str(exc)[:120]}"
            for j, r in enumerate(chunk):
                out = {"lib": r.lib, "i": int(r.i), "expression": r.expression}
                if f"v{j}" not in P:
                    out["error"] = err.get(j, "did not compute")
                else:
                    panel = np.asarray(P[f"v{j}"], np.float64)
                    out.update(coverage=float(np.isfinite(panel[labelled]).mean()), distinct=float(dg.distinct_fraction(panel)))
                    out["gate"] = bool(out["coverage"] >= 0.9 and out["distinct"] >= 0.5)
                    if out["gate"]:
                        rw = steer_reward(panel, ctx, "long_neutral")
                        z = dg._zrank(rw["sign"] * panel[:cut:5])
                        out.update(score=float(rw["score"]), sign=float(rw["sign"]), hl=float(rw["hl"]), train=float(rw["train"]["long_sharpe"]),
                                   valid=float(rw["valid"]["long_sharpe"]), rho_known=corr(z, kz))
                        out["discovery"] = bool(out["score"] >= THR and abs(out["rho_known"]) < RHO)
                fh.write(json.dumps(out, ensure_ascii=False) + "\n")
            fh.flush()
            print(f"[w02l] {min(k + 8, len(rows))}/{len(rows)} ({time.time() - t0:.0f}s)", flush=True)
print("[w02l] done", flush=True)
