"""C05 (observations.md 1): how many heads of each library are a non-linear re-expression of one of the five reward controls.
In sample only (train, every 5th day), defined before the test period is read; descriptive, it changes nothing in the judgement.

For every head kept in research/coldstart_C05/final_dry.json: the traded signal BEFORE the residual step (direction x EMA at its
half-life) against each control, daily rank correlation averaged over train.  A head counts as a re-expression of a control when
|rho| >= 0.5 with it (the threshold the study already uses for "the same thing as the known family").

    python scripts/c05_controls.py      -> research/coldstart_C05/controls.json
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

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

os.environ.setdefault("PARTURA_REPROMOTE", "1")
D = PARTURA_ROOT / "research" / "coldstart_C05"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None
LINE = 0.5

F = json.loads((D / "final_dry.json").read_text(encoding="utf-8"))
heads = {}
for S, libs in F["libraries"].items():
    for X, lst in libs.items():
        for h in lst:
            heads.setdefault(h["expr"], (float(h["sign"]), float(h["hl"])))
uniq = sorted(heads)

with slot():
    mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 60)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 80))).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    ps = PanelSet(STORE, "20180102", "20230807", warmup=60, device="cuda", gpu_fraction=0.4, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")
    CTRL = {"liq": "cross_mean(day_sum(Amt), 30)", "vol": "cross_mean(day_std(Ret), 20)",
            "rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "known": G.spec["pool"][0]["expr"], "size": "LogFloatCap"}
    aux = ps.compute(CTRL)
    dates = np.asarray(ps.dates).astype(str)
    tr = slice(0, int(np.searchsorted(dates, "20220101")))
    CZ = {k: dg._zrank(np.asarray(v, np.float64))[:tr.stop:5] for k, v in aux.items()}

    def rho(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    R = {}
    for i in range(0, len(uniq), 16):
        chunk = uniq[i:i + 16]
        P = ps.compute({f"c{j}": e for j, e in enumerate(chunk)})
        for j, e in enumerate(chunk):
            if f"c{j}" not in P:
                continue
            sg, hl = heads[e]
            z = dg._zrank(sg * bk.smoothed(np.asarray(P[f"c{j}"], np.float64), hl))[:tr.stop:5]
            R[e] = {k: rho(z, cz) for k, cz in CZ.items()}
        print(f"[controls] {min(i + 16, len(uniq))}/{len(uniq)} ({time.time() - t0:.0f}s)", flush=True)
    mem.stop()

out = {"line": LINE, "rho": R, "per_seed": {}, "by_arm": {}}
for S, libs in F["libraries"].items():
    for X, lst in libs.items():
        tags = []
        for h in lst:
            r = R.get(h["expr"], {})
            top = max(r, key=lambda k: abs(r[k])) if r else None
            tags.append({"expr": h["expr"], "role": h["role"], "control": top if top and abs(r[top]) >= LINE else None, "rho": r.get(top) if top else None})
        out["per_seed"].setdefault(S, {})[X] = tags
        a = out["by_arm"].setdefault(X, {"heads": 0, "re_expressions": 0, "by_control": {}})
        a["heads"] += len(tags)
        for t in tags:
            if t["control"]:
                a["re_expressions"] += 1
                a["by_control"][t["control"]] = a["by_control"].get(t["control"], 0) + 1
(D / "controls.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
for X, a in out["by_arm"].items():
    print(f"  {X}: {a['re_expressions']}/{a['heads']} heads re-express a control (|rho| >= {LINE}): {a['by_control']}")
print(f"wrote {D / 'controls.json'} ({time.time() - t0:.0f}s)")
