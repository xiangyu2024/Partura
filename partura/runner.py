"""Run one experiment stage: expressions -> panels -> metrics -> diagnostics -> JSON.

A stage is a group of expressions that answer ONE question (see the config's
``question`` field).  All expressions of every requested stage -- plus the
controls and gate panels -- go into a single engine call, because the variants
share most of their subtrees and the engine eliminates common subexpressions
inside a call.

Direction handling: the tradable sign is fitted ONCE on the training split
(sign of mean daily rank IC) and then applied unchanged to every other split.
Refitting the sign per split is the most common way an out-of-sample number
becomes meaningless, and it is not done here.
"""

from __future__ import annotations

import json
import time
from dataclasses import asdict
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import numpy as np
import yaml

from . import diagnose as dg
from .bridge import PARTURA_ROOT, provenance
from .panels import PanelSet
from .splits import SPLITS, Ledger


def load_config(path: str) -> dict:
    return yaml.safe_load(Path(path).read_text(encoding="utf-8"))


def _variants_of(cfg: dict, stages: Sequence[str]) -> Dict[str, dict]:
    out: Dict[str, dict] = {}
    for st in cfg["stages"]:
        if stages and st["id"] not in stages:
            continue
        for v in st["variants"]:
            out[v["id"]] = {**v, "stage": st["id"], "question": st.get("question", "")}
    return out


def run(config_path: str, stages: Sequence[str] = (), *, store: str, device: str = "cpu",
        chunk_symbols: Optional[int] = None, chunk_days: Optional[int] = None,
        gpu_fraction: Optional[float] = None, mirror_root: Optional[str] = None,
        max_symbols: Optional[int] = None, torch_threads: Optional[int] = None,
        workdir: Optional[str] = None, out_root: Optional[str] = None,
        use_holdout: bool = False, diagnostics: bool = True) -> dict:
    cfg = load_config(config_path)
    for k, v in (cfg.get("splits") or {}).items():      # smoke runs use a shorter calendar
        SPLITS[k] = (str(v[0]), str(v[1]))
    fid = cfg["factor_id"]
    out_dir = Path(out_root or (PARTURA_ROOT / "runs")) / fid
    out_dir.mkdir(parents=True, exist_ok=True)
    ledger = Ledger(out_dir / "ledger.json")

    variants = _variants_of(cfg, stages)
    if not variants:
        raise SystemExit(f"no stages matched {list(stages)}")
    controls: Dict[str, str] = cfg.get("controls", {})
    gates: Dict[str, str] = cfg.get("gates", {})

    ps = PanelSet(store, SPLITS["full"][0], SPLITS["full"][1],
                  warmup=int(cfg.get("warmup", 60)), device=device, chunk_symbols=chunk_symbols,
                  chunk_days=chunk_days, cache_dir=str(out_dir / "panels"), mirror_root=mirror_root,
                  max_symbols=max_symbols, gpu_fraction=gpu_fraction, torch_threads=torch_threads,
                  workdir=workdir, label_kind=cfg.get("label", {}).get("kind", "open_vwap15"))

    todo = {vid: v["expr"] for vid, v in variants.items()}
    todo.update(controls)
    todo.update(gates)
    t0 = time.perf_counter()
    panels = ps.compute(todo)
    horizons = [int(h) for h in cfg.get("horizons", [1, 2, 3, 5, 10, 20])]
    targets = {h: ps.target(h) for h in horizons}
    tgt = targets[int(cfg.get("label", {}).get("horizon", 1))]

    cost = float(cfg.get("cost_per_side", dg.COST_PER_SIDE))
    cap = cfg.get("turnover_cap", dg.TURNOVER_CAP)
    cap = None if cap in (None, 0) else float(cap)
    top = float(cfg.get("top_frac", dg.TOP_FRAC))

    splits = ["train", "valid"] + (["holdout"] if use_holdout else []) + ["full"]
    sl = {s: ps.split_slice(s) for s in splits}

    results: Dict[str, dict] = {}
    for vid, v in variants.items():
        p = panels.get(vid)
        if p is None:
            results[vid] = {"error": ps.errors.get(vid, "missing panel"), **{k: v[k] for k in ("stage", "why") if k in v}}
            continue
        tr = sl["train"]
        sign = dg.sign_from(p[tr], tgt[tr])
        row = {"expr": v["expr"], "stage": v["stage"], "why": v.get("why", ""),
               "group": v.get("group", ""), "sign": sign, "splits": {}}
        for s in splits:
            row["splits"][s] = dg.metric_row(p[sl[s]], tgt[sl[s]], sign=sign, cost=cost, cap=cap, top_frac=top)
        results[vid] = row

    ok = {vid: panels[vid] for vid in variants if vid in panels}
    report: Dict[str, object] = {
        "factor_id": fid,
        "config": config_path,
        "stages": list(stages) or [s["id"] for s in cfg["stages"]],
        "provenance": provenance(store),
        "view": {"days": len(ps.dates), "symbols": len(ps.symbols),
                 "first": ps.dates[0], "last": ps.dates[-1], "warmup_rows": ps.trim},
        "label": cfg.get("label", {"kind": "open_vwap15", "horizon": 1}),
        "cost_per_side": cost, "turnover_cap": cap, "top_frac": top,
        "splits_used": splits,
        "results": results,
        "errors": ps.errors,
        "seconds": round(time.perf_counter() - t0, 1),
    }

    if diagnostics and ok:
        diag_cfg = cfg.get("diagnostics", {})
        diag: Dict[str, object] = {}
        tr = sl["train"]

        want_decay = diag_cfg.get("decay", list(ok)[:1])
        diag["decay"] = {vid: dg.decay(ok[vid][tr], {h: targets[h][tr] for h in horizons},
                                       sign=results[vid]["sign"]) for vid in want_decay if vid in ok}

        want_year = diag_cfg.get("by_year", list(ok)[:1])
        diag["by_year"] = {vid: dg.by_year(ok[vid], tgt, ps.years, sign=results[vid]["sign"],
                                           cost=cost, top_frac=top) for vid in want_year if vid in ok}

        want_ext = diag_cfg.get("extreme_days", list(ok)[:1])
        diag["extreme_days"] = {vid: dg.extreme_day_dependence(ok[vid][tr], tgt[tr], sign=results[vid]["sign"],
                                                               cost=cost, top_frac=top)
                                for vid in want_ext if vid in ok}

        ctl_panels = {k: panels[k] for k in controls if k in panels}
        neut: Dict[str, object] = {}
        for vid in diag_cfg.get("neutralise", []):
            if vid not in ok or not ctl_panels:
                continue
            entry: Dict[str, object] = {}
            resid, info = dg.neutralise(ok[vid][tr], {k: c[tr] for k, c in ctl_panels.items()})
            entry["all_controls"] = {"r2": info["mean_r2"],
                                     "metrics": dg.metric_row(resid, tgt[tr], sign=results[vid]["sign"],
                                                              cost=cost, cap=cap, top_frac=top)}
            for k, c in ctl_panels.items():          # leave-one-in: which control does the damage
                r1, i1 = dg.neutralise(ok[vid][tr], {k: c[tr]})
                entry[k] = {"r2": i1["mean_r2"],
                            "metrics": dg.metric_row(r1, tgt[tr], sign=results[vid]["sign"],
                                                     cost=cost, cap=cap, top_frac=top)}
            neut[vid] = entry
        diag["neutralise"] = neut

        cond: Dict[str, object] = {}
        for pair in diag_cfg.get("conditional", []):
            a, g = pair["factor"], pair["gate"]
            if a in ok and g in panels:
                cond[f"{a}|{g}"] = dg.conditional_ic(ok[a][tr], tgt[tr], panels[g][tr],
                                                     buckets=int(pair.get("buckets", 5)))
        diag["conditional"] = cond

        diag["controls"] = {k: dg.metric_row(panels[k][tr], tgt[tr],
                                             sign=dg.sign_from(panels[k][tr], tgt[tr]),
                                             cost=cost, cap=cap, top_frac=top)
                            for k in list(controls) + list(gates) if k in panels}

        diag["rank_corr_train"] = dg.rank_corr_matrix({vid: ok[vid][tr] for vid in ok})
        report["diagnostics"] = diag

    for s in splits:
        ledger.record(s, len(ok), purpose="stage metrics" + (" + diagnostics" if diagnostics else ""),
                      stage=",".join(report["stages"]))

    name = "_".join(report["stages"]) if len(report["stages"]) <= 3 else "batch"
    path = out_dir / f"{name}.json"
    path.write_text(json.dumps(report, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    print(f"[runner] wrote {path} ({report['seconds']}s)")
    return report


__all__ = ["run", "load_config"]
