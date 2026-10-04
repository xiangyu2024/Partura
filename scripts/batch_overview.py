"""分辨: how the factors of a batch relate to each other and to what is already known.

For every factor of the batch it takes the signal that would actually be
traded -- sign x panel, EMA-smoothed at the half-life fitted on the user's
training period -- and reports, on the Partura fit split:

* its daily cross-sectional rank correlation with every other factor of the batch,
* with the shared controls (amount, float cap, turnover rate, intraday vol, ...),
* and with the "known family" panels earlier studies established,
* plus how much of it those controls span (rank-space R^2) and what is left.

All panels come from the shared content-addressed cache that the S0 runs
filled, so this evaluates nothing.

    python scripts/batch_overview.py batches/B01_single_factors.yaml
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(2)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.splits import SPLITS  # noqa: E402

batch = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
first = yaml.safe_load(open(PARTURA_ROOT / "configs" / f"{batch['factors'][0]['id']}.yaml", encoding="utf-8"))
for k, v in first["splits"].items():
    SPLITS[k] = (str(v[0]), str(v[1]))

with slot():
    mem = MemoryGuard().start()
    ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", SPLITS["full"][0], SPLITS["full"][1],
                  warmup=60, device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE),
                  mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                  label_kind="open_vwap15", label_buyable=True, batch=2)
    exprs = {f["id"]: f["expr"] for f in batch["factors"]}
    extra = {**first["controls"], **first["gates"]}
    panels = ps.compute({**exprs, **extra})
    for k, path in first["external_controls"].items():
        panels[k] = ps.external(path)
    tgt = ps.target(1)
    tr, us = ps.split_slice("train"), ps.split_slice("utrain")
    t0 = time.time()

    signal, info = {}, {}
    for f in batch["factors"]:
        p = panels.get(f["id"])
        if p is None:
            print(f"{f['id']}: no panel ({ps.errors.get(f['id'])})", flush=True)
            continue
        sm = bk.smoothed(float(f["sign"]) * np.asarray(p, dtype=np.float64), float(f["hl"]))
        signal[f["id"]] = sm[tr]
        info[f["id"]] = {"name": f["name"], "lib": f["lib"], "sign": f["sign"], "hl": f["hl"]}
    others = {k: np.asarray(panels[k][tr], dtype=np.float64)
              for k in list(extra) + list(first["external_controls"]) if k in panels}

    ranks = {k: dg.rank_rows(v) for k, v in {**signal, **others}.items()}
    from alphacube.metrics import cs_pearson, nanmean_quiet
    names = list(ranks)
    corr = {a: {} for a in names}
    for i, a in enumerate(names):
        for b in names[i:]:
            if a in others and b in others:
                continue
            c = nanmean_quiet(cs_pearson(ranks[a], ranks[b]))
            corr[a][b] = c
            corr[b][a] = c
    print(f"rank correlations in {time.time() - t0:.0f}s", flush=True)

    ctl_keys = [k for k in others if k.startswith("ctl_")]
    ctl_z = {k: dg._zrank(others[k]) for k in ctl_keys}
    span = {}
    for fid, sig in signal.items():
        y = dg._zrank(sig)
        _, i_all = dg.neutralise(y, ctl_z, panel_ready=True, controls_ready=True)
        span[fid] = {"r2_all_controls": i_all["mean_r2"]}
        for k in ctl_keys:
            _, i1 = dg.neutralise(y, {k: ctl_z[k]}, panel_ready=True, controls_ready=True)
            span[fid][k] = i1["mean_r2"]
        print(f"{fid}: R2 by all controls {i_all['mean_r2']:.3f}", flush=True)
    mem.stop()

out_dir = PARTURA_ROOT / "runs" / "_batch_B01"
out_dir.mkdir(parents=True, exist_ok=True)
(out_dir / "overview.json").write_text(json.dumps(
    {"info": info, "corr": corr, "span": span, "controls": ctl_keys,
     "known": [k for k in others if k.startswith("known_")], "split": list(SPLITS["train"]),
     "note": "signals are sign x panel, EMA-smoothed at the published half-life; fit split only"},
    ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print("wrote", out_dir / "overview.json", flush=True)
