"""C01: finish the bookkeeping of a run whose SEARCH completed but whose head count did not (PLAN §6, revision 3).

Server.  scripts/idea_search.py writes evidence.json as soon as an arm's search ends, then rebuilds every passer on the
search view to count the run's distinct heads.  When only that last step fails (a full disk, the job time limit), a
rerun would repeat the same search draw for draw (the search is deterministic) and fail or pass at the same step.  This
script does that last step on the saved evidence with the same code: same view, same reference signals, same rho, same
thresholds (|rho| < 0.5 against the pool and the known family, < 0.7 between heads).

    python scripts/c01_heads_fill.py <episode>  (e.g. c01r3s302A_I0_open_search)   -> fills arms.<arm>.heads in its evidence.json
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
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import Guidance, is_discovery  # noqa: E402

EP = PARTURA_ROOT / "episodes" / sys.argv[1]
E = json.loads((EP / "evidence.json").read_text(encoding="utf-8"))
START, END, SPLIT = E["period"]
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None      # a host without the D-major mirror reads the store itself
G = Guidance.load(PARTURA_ROOT / E["guidance"])
KIND, THR = E["reward"], float(E.get("threshold", 1.0))


def found(c):
    return is_discovery(KIND, c["score"], c.get("s_train"), c.get("s_valid"), THR)


with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    ps = PanelSet(STORE, START, END, warmup=60, device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8)
    pool_spec = G.spec["pool"][-1]
    aux = ps.compute({"pool": pool_spec["expr"], "known": G.spec["pool"][0]["expr"]})
    dates = np.asarray(ps.dates)
    cut = int(np.searchsorted(dates, SPLIT))
    pool_sig = dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(aux["pool"], np.float64), float(pool_spec["hl"])))
    known_z = dg._zrank(float(G.spec["pool"][0]["sign"]) * np.asarray(aux["known"], np.float64))
    allp = {}
    for arm in E["arms"]:
        for c in E["arms"][arm]["candidates"]:
            if found(c):
                allp.setdefault(c["expr"], c)
    Z = {}
    if allp:
        P = ps.compute({f"c{i}": e for i, e in enumerate(allp)})
        for i, (e, c) in enumerate(allp.items()):
            if f"c{i}" in P:
                Z[e] = dg._zrank(bk.smoothed(c["sign"] * np.asarray(P[f"c{i}"], np.float64), c["hl"]))[:cut:5]

    def rho(a, b):
        ok = np.isfinite(a) & np.isfinite(b)
        x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
        n = np.maximum(ok.sum(1), 1)
        with np.errstate(invalid="ignore", divide="ignore"):
            c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
        return float(np.nanmean(c))

    pz, kz = pool_sig[:cut:5], known_z[:cut:5]
    for arm, A in E["arms"].items():
        heads = []
        for c in A["candidates"]:
            if c["expr"] not in Z or not found(c):
                continue
            c["rho_pool"], c["rho_known_traded"] = rho(Z[c["expr"]], pz), rho(Z[c["expr"]], kz)
            if KIND != "long_screen" and not (abs(c["rho_pool"]) < 0.5 and abs(c["rho_known_traded"]) < 0.5):
                continue
            if all(abs(rho(Z[c["expr"]], Z[h["expr"]])) < 0.7 for h in heads):
                heads.append(c)
        A["independent_distinct"] = len(heads)
        A["heads"] = heads
        A["efficiency_per_100"] = 100.0 * len(heads) / max(A["scored"], 1)
        A["heads_filled_by"] = "scripts/c01_heads_fill.py (PLAN §6 revision 3)"
        print(f"[fill] {arm}: {len(heads)} distinct passers outside the known pool = {A['efficiency_per_100']:.1f} per 100 scored", flush=True)
    mem.stop()
(EP / "evidence.json").write_text(json.dumps(E, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print(f"wrote {EP / 'evidence.json'} ({time.time() - t0:.0f}s)")
