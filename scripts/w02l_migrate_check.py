"""W02L: does a library factor recomputed on the new host from its expression match the panel the old host stored?

The two hosts share no files, so the check moves only a small slice: 16 in-sample dates x every name of each factor.

    old host:  python scripts/w02l_migrate_check.py extract <sample.csv> <out.npz>
               reads AlphaCube's stored panels _bench/trainto/{legacy,allfac_buyable}/panels/<i>.npy (2018-01-02 ~ 2025-12-31)
    new host:  source tmp/prod_env.sh; python scripts/w02l_migrate_check.py compare <in.npz> <out.json> [--every k] [--shard i/n] [--device cpu|cuda]
               recomputes each expression on 20180102 ~ 20251231 (the stored view, and the W02 view stage 0 scores on; a cache
               hit for what it already computed) and compares on the same dates

Only factor values on dates up to 2025-12-31 are compared (no label, no return; 2026, the test, never enters).
Per factor: the mean over the 16 dates of the daily rank correlation (names finite on both hosts), the share of names whose
"has a value" agrees, the largest relative difference; class identical (max rel diff < 1e-4), same (rank rho >= 0.99),
close (0.9 ~ 0.99), different (< 0.9), or failed (did not compute on the new host).
"""
import json
import os
import sys
from pathlib import Path

import numpy as np

MODE = sys.argv[1]
BENCH = Path(os.environ.get("W02L_BENCH", "/root/autodl-tmp/AlphaCube/_bench/trainto"))
SUB = {"L": "legacy", "X": "allfac_buyable"}
N_DATES, FIRST, LAST = 16, 250, 1941            # day indices of the stored view: skip the first year (warm-up), to 2025-12-31

if MODE == "extract":
    import pandas as pd
    smp = pd.read_csv(sys.argv[2])
    dates = np.load(BENCH / "legacy" / "dates.npy")
    assert str(dates[LAST]) <= "20251231", dates[LAST]
    idx = np.unique(np.linspace(FIRST, LAST, N_DATES).astype(int))
    keys, vals = [], []
    for r in smp.itertuples(index=False):
        f = BENCH / SUB[r.lib] / "panels" / f"{int(r.i):05d}.npy"
        if not f.is_file():
            continue
        p = np.load(f, mmap_mode="r")
        keys.append(f"{r.lib}{int(r.i)}")
        vals.append(np.asarray(p[idx], np.float32))
    np.savez_compressed(sys.argv[3], keys=np.array(keys), exprs=np.array([smp.set_index(smp.lib + smp.i.astype(str)).expression[k] for k in keys]),
                        dates=dates[idx], values=np.stack(vals))
    print(f"extracted {len(keys)} factors x {len(idx)} dates ({dates[idx][0]} ~ {dates[idx][-1]})")
    sys.exit(0)

assert MODE == "compare"
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura import ops_ext  # noqa: E402,F401
from partura import study  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.guard import slot  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402

_caps = study.host_caps()
os.environ.update(PARTURA_SLOTS=_caps["PARTURA_SLOTS"], PARTURA_GPU_WAYS=_caps["PARTURA_GPU_WAYS"], PARTURA_REPROMOTE="1")
Z = np.load(sys.argv[2])
keys, exprs, dts, old = list(Z["keys"]), list(Z["exprs"]), [str(d) for d in Z["dates"]], Z["values"]
# --every k: compare every k-th factor of the slice only; --shard i/n: this process takes every n-th of those, from the i-th
EV = int(sys.argv[sys.argv.index("--every") + 1]) if "--every" in sys.argv else 1
SH, NSH = (map(int, sys.argv[sys.argv.index("--shard") + 1].split("/")) if "--shard" in sys.argv else (0, 1))
pick = list(range(0, len(keys), EV))[SH::NSH]
keys, exprs, old = [keys[j] for j in pick], [exprs[j] for j in pick], old[pick]
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None


def rank_rows(a):
    import pandas as pd
    return pd.DataFrame(a).rank(axis=1).to_numpy()


out = []
with slot():
    from alphacube.plugins import load_plugins
    load_plugins(["partura.ac_plugin"])
    DEV = sys.argv[sys.argv.index("--device") + 1] if "--device" in sys.argv else "cpu"     # cpu: no GPU lock, chunked by names
    if not DEV.startswith("cuda"):       # PanelSet takes the "gpu" lock around every batch whatever the device; on the CPU
        os.environ["PARTURA_GPU_WAYS"] = "16"                  # that lock guards nothing here, so give it enough ways never to queue
    ps = PanelSet(STORE, "20180102", "20251231", warmup=60, device=DEV, gpu_fraction=0.3 if DEV.startswith("cuda") else None, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
    pd_ = [str(d) for d in ps.dates]
    di = [pd_.index(d) for d in dts]
    for c0 in range(0, len(keys), 8):                          # eight expressions per engine call, the result file rewritten each time
        ck, ce = keys[c0:c0 + 8], exprs[c0:c0 + 8]
        try:
            P = ps.compute({f"v{j}": e for j, e in enumerate(ce)})
        except Exception:                                     # noqa: BLE001
            P = {}
            for j, e in enumerate(ce):
                try:
                    P[f"v{j}"] = ps.compute({"x": e})["x"]
                except Exception as exc:                      # noqa: BLE001
                    P[f"v{j}"] = exc
        for j, (k, e) in enumerate(zip(ck, ce)):
            o = old[c0 + j]
            rec = {"key": k, "expr": e}
            p = P.get(f"v{j}")
            if p is None or isinstance(p, Exception):
                rec.update(cls="failed", error=f"{type(p).__name__}: {str(p)[:160]}" if p is not None else "did not compute")
                out.append(rec)
                continue
            p = np.asarray(p, np.float64)[di]
            o = o.astype(np.float64)
            fo, fn = np.isfinite(o), np.isfinite(p)
            both = fo & fn
            rho = []
            for t in range(len(di)):
                m = both[t]
                if m.sum() < 50 or np.nanstd(o[t][m]) == 0 or np.nanstd(p[t][m]) == 0:
                    continue
                ro, rn = rank_rows(o[t][m][None])[0], rank_rows(p[t][m][None])[0]
                rho.append(float(np.corrcoef(ro, rn)[0, 1]))
            with np.errstate(invalid="ignore", divide="ignore"):
                rel = np.abs(p - o) / np.maximum(np.abs(o), 1e-12)
            mrel = float(np.nanmax(np.where(both, rel, np.nan))) if both.any() else float("nan")
            r = float(np.mean(rho)) if rho else float("nan")
            rec.update(rank_rho=r, rank_rho_min=float(np.min(rho)) if rho else float("nan"), valid_agree=float((fo == fn).mean()),
                       old_valid=float(fo.mean()), new_valid=float(fn.mean()), max_rel=mrel,
                       cls=("identical" if mrel < 1e-4 and (fo == fn).mean() > 0.999 else "same" if r >= 0.99 else "close" if r >= 0.9
                            else "different" if r == r else "failed"))
            out.append(rec)
        Path(sys.argv[3]).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"[migrate] {len(out)}/{len(keys)}", flush=True)
Path(sys.argv[3]).write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter  # noqa: E402
print("classes:", dict(Counter(r["cls"] for r in out)))
