"""C05, before the one out-of-sample read: why some heads of final_dry.json do not reproduce their recorded train Sharpe.
In sample only (both views are cut at 20211231 for the comparison; nothing after 20230807 enters a number printed here).

For every head with reproduces = false: its train Sharpe on
  (m5) the mining view (20180102..20230807, as idea_search builds it) with the five controls  -- the final's rule, mining grid
  (f5) the final view (20180102..the last date) with the five controls                         -- what c05_final.py does
  (mE) the mining view with the five controls plus the E mission's core family (its --neutral-extra file), for E heads
and the largest difference of the raw panel between the two views on train days (look-ahead / view-dependence check).

    python scripts/c05_repro.py      -> research/coldstart_C05/repro.json
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
from partura import ops_ext  # noqa: E402,F401
from partura import steer  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

os.environ.setdefault("PARTURA_REPROMOTE", "1")
D, EP = PARTURA_ROOT / "research" / "coldstart_C05", PARTURA_ROOT / "episodes"
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None

F = json.loads((D / "final_dry.json").read_text(encoding="utf-8"))
todo = {}
for S, libs in F["libraries"].items():
    for X, lst in libs.items():
        for h in lst:
            if not h["reproduces"]:
                todo.setdefault(h["expr"], {"seed": S, "arms": [], "role": h["role"], "mission": h.get("mission"), "sign": h["sign"], "hl": h["hl"],
                                            "train_recorded": h["train"]})["arms"].append(X)
print(f"[repro] {len(todo)} distinct heads", flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=int(os.environ.get("PARTURA_SELF_LIMIT_GB", 60)), cgroup_limit_gb=int(os.environ.get("PARTURA_CGROUP_LIMIT_GB", 80))).start()
    t0 = time.time()
    from alphacube.plugins import load_plugins
    from alphacube.store import open_cube_store
    load_plugins(["partura.ac_plugin"])
    END = str(open_cube_store(STORE, mirror_root=MIRROR).dates[-1])
    G = steer.Guidance.load(PARTURA_ROOT / "guidance" / "C05_base.yaml")
    CTRL = {"liq": "cross_mean(day_sum(Amt), 30)", "vol": "cross_mean(day_std(Ret), 20)",
            "rev": "div(day_last(Close), ts_delay(day_last(Close), 20))", "known": G.spec["pool"][0]["expr"], "size": "LogFloatCap"}
    V = {}
    for name, end in (("m", "20230807"), ("f", END)):
        ps = PanelSet(STORE, "20180102", end, warmup=60, device="cuda", gpu_fraction=float(os.environ.get("C05_GPU_FRACTION", 0.9)),
                      cache_dir=str(SHARED_CACHE), mirror_root=MIRROR, workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15",
                      label_buyable=True, batch=8, daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
        aux = ps.compute(CTRL)
        dates = np.asarray(ps.dates).astype(str)
        V[name] = {"ps": ps, "ctl": [aux[k] for k in ("liq", "vol", "rev", "known", "size")], "tgt": ps.target(1),
                   "tr": slice(0, int(np.searchsorted(dates, "20220101")))}
        V[name]["Q"] = steer.neutral_basis(V[name]["ctl"])

    def train_sharpe(v, raw, sign, hl, Q):
        sm = steer.neutral_residual(sign * bk.smoothed(np.asarray(raw, np.float64), hl), Q)
        return float(np.nan_to_num(bk.book_row(sm, v["tgt"], v["tr"])["long_sharpe"]))

    out = {}
    for e, t in todo.items():
        row = dict(t)
        raw = {}
        for name in ("m", "f"):
            P = V[name]["ps"].compute({"x": e})
            raw[name] = np.asarray(P["x"], np.float64) if "x" in P else None
            row[f"train_{name}5"] = train_sharpe(V[name], raw[name], float(t["sign"]), float(t["hl"]), V[name]["Q"]) if raw[name] is not None else None
        if raw["m"] is not None and raw["f"] is not None:
            n = V["m"]["tr"].stop
            a, b = raw["m"][:n], raw["f"][:n]
            both = np.isfinite(a) & np.isfinite(b)
            row["raw_train_max_absdiff"] = float(np.max(np.abs(a[both] - b[both]))) if both.any() else None
            row["raw_train_scale"] = float(np.nanstd(a))
            row["raw_train_nan_mismatch"] = int((np.isfinite(a) != np.isfinite(b)).sum())
        if t["role"].startswith("E") and t["mission"]:
            fam_f = json.loads((EP / t["mission"] / "evidence.json").read_text(encoding="utf-8"))["c05"]["neutral_extra"]
            fam = json.loads((D / "arms" / Path(fam_f).name).read_text(encoding="utf-8")) if fam_f else []   # recorded with the host's absolute path
            FP = V["m"]["ps"].compute({f"f{i}": f["expr"] for i, f in enumerate(fam)})
            extra = [bk.smoothed(float(f["sign"]) * np.asarray(FP[f"f{i}"], np.float64), float(f["hl"])) for i, f in enumerate(fam) if f"f{i}" in FP]
            row["family"] = len(extra)
            row["train_mE"] = train_sharpe(V["m"], raw["m"], float(t["sign"]), float(t["hl"]), steer.neutral_basis(V["m"]["ctl"] + extra))
        out[e] = row
        print(f"[repro] {t['role']:3s} rec {t['train_recorded']:+.2f} m5 {row['train_m5']:+.2f} f5 {row['train_f5']:+.2f}"
              + (f" mE {row['train_mE']:+.2f}" if "train_mE" in row else "")
              + f" rawdiff {row.get('raw_train_max_absdiff')} (scale {row.get('raw_train_scale', 0):.3g}, nan-mismatch {row.get('raw_train_nan_mismatch')}) | {e[:90]}", flush=True)
    mem.stop()
(D / "repro.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {D / 'repro.json'} ({time.time() - t0:.0f}s)")
