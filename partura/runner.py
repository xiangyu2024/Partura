"""Run one experiment stage: expressions -> panels -> metrics -> diagnostics -> JSON.

A stage is a group of expressions that answer ONE question (the config's
``question`` field).  The rules the numbers depend on:

* **Direction and half-life are fitted once, on the fit split**, and applied
  unchanged everywhere else.
* **Selection is by the long leg.**  In A-shares only the long book can be held,
  so the half-life is the one that is best for the pure long book
  (``rank_by: long``), and candidates are ranked by net long-leg excess and
  pure-long Sharpe.  The long/short view (half-life fitted by L/S Sharpe) is
  computed for every variant as well, because the user's first table was
  published in it.
* **Decision numbers** fit on ``train`` and are confirmed on ``valid``.  The
  numbers comparable with the user's own tables fit on ``utrain`` (their
  training period) and read ``holdout`` (their test period) only when
  ``--holdout`` is given -- that read is ledgered.
* **Diagnostics look at what is traded**: the sign-aligned panel smoothed at the
  fitted half-life.  For a factor whose memory lives in the EMA, the raw daily
  panel is mostly noise and says little about the book.
"""

from __future__ import annotations

import json
import os
import time
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import numpy as np
import yaml

from . import books as bk
from . import diagnose as dg
from . import guard
from .bridge import PARTURA_ROOT, provenance
from .panels import SHARED_CACHE, PanelSet
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
        use_holdout: bool = False, diagnostics: bool = True, batch: int = 4,
        cpu_fallback: bool = False, cache_dir: Optional[str] = None, tag: Optional[str] = None) -> dict:
    cfg = load_config(config_path)
    from .probes import load_study_probes
    for pf in (cfg.get("probes") or []):
        added = load_study_probes(pf)
        if added:
            print(f"[probes] {pf}: +{', '.join(added)}")
    for k, v in (cfg.get("splits") or {}).items():
        SPLITS[k] = (str(v[0]), str(v[1]))
    fid = cfg["factor_id"]
    out_dir = Path(out_root or (PARTURA_ROOT / "runs")) / fid
    out_dir.mkdir(parents=True, exist_ok=True)
    ledger = Ledger(out_dir / "ledger.json")

    variants = _variants_of(cfg, stages)
    if not variants:
        raise SystemExit(f"no stages matched {list(stages)}")
    every = _variants_of(cfg, ())                       # all stages: ids named by diagnostics may live elsewhere
    controls: Dict[str, str] = cfg.get("controls") or {}
    gates: Dict[str, str] = cfg.get("gates") or {}
    ext_controls: Dict[str, str] = cfg.get("external_controls") or {}
    label = cfg.get("label") or {}
    fit_name = cfg.get("fit_split", "train")
    user_name = cfg.get("user_split", "utrain" if "utrain" in SPLITS else None)
    rank_by = cfg.get("rank_by", "long")
    base_id = cfg.get("baseline_id", "v_base")
    diag_cfg = cfg.get("diagnostics") or {}

    def _say(msg: str) -> None:
        print(f"[runner] {time.strftime('%H:%M:%S')} {msg}", flush=True)

    mem = guard.MemoryGuard(self_limit_gb=float(os.environ.get("PARTURA_SELF_GB", 14)),
                            cgroup_limit_gb=float(os.environ.get("PARTURA_CGROUP_GB", 34))).start()
    t0 = time.perf_counter()
    ps = PanelSet(store, SPLITS["full"][0], SPLITS["full"][1],
                  warmup=int(cfg.get("warmup", 60)), device=device, chunk_symbols=chunk_symbols,
                  chunk_days=chunk_days,
                  cache_dir=str(cache_dir or cfg.get("cache_dir") or
                                (Path(out_root) / "_panels" if out_root else SHARED_CACHE)),
                  mirror_root=mirror_root, max_symbols=max_symbols, gpu_fraction=gpu_fraction,
                  torch_threads=torch_threads, workdir=workdir,
                  label_kind=label.get("kind", "open_vwap15"), label_buyable=bool(label.get("buyable", False)),
                  batch=batch, cpu_fallback=cpu_fallback)

    # Variants of OTHER stages that this run's diagnostics refer to (the baseline, a gate, a row of
    # the correlation matrix).  They were evaluated by the run that owned them, so this is a cache read.
    refs: List[str] = [base_id] + list(cfg.get("corr_ids") or [])
    for pr in diag_cfg.get("conditional") or []:
        refs += [pr.get("factor"), pr.get("gate")]
    refs = [r for r in dict.fromkeys(refs) if r in every and r not in variants]

    todo = {vid: v["expr"] for vid, v in variants.items()}
    todo.update({r: every[r]["expr"] for r in refs})
    todo.update(controls)
    todo.update(gates)
    panels = ps.compute(todo)
    for k, path in ext_controls.items():
        try:
            panels[k] = ps.external(path)
        except Exception as exc:
            ps.errors[k] = f"external: {exc}"
    horizons = [int(h) for h in cfg.get("horizons", [1, 2, 3, 5, 10, 20])]
    h0 = int(label.get("horizon", 1))
    tgt = ps.target(h0)
    if label.get("verify_against") and Path(label["verify_against"]).is_file():
        ref = np.load(label["verify_against"], mmap_mode="r")
        same = ref.shape == tgt.shape and np.array_equal(np.asarray(ref, dtype=np.float64), tgt, equal_nan=True)
        _say(f"label {'==' if same else '!='} {label['verify_against']}")
        if not same:
            raise SystemExit("the label Partura computed is not the label the published table was scored on")

    cost = float(cfg.get("cost_per_side", bk.COST))
    top = float(cfg.get("top_frac", bk.TOP_FRAC))
    dec_splits = [s for s in ("train", "valid") if s in SPLITS]
    splits = list(dec_splits)
    if user_name and user_name in SPLITS and user_name not in splits:
        splits.append(user_name)
    if use_holdout:
        splits += [s for s in ("holdout", "full") if s in SPLITS]
    sl = {s: ps.split_slice(s) for s in splits}
    scope = slice(sl[dec_splits[0]].start, (sl["full"] if use_holdout and "full" in sl
                                            else sl[user_name] if user_name in sl else sl[dec_splits[-1]]).stop)
    tgt_ranks = {s: dg.rank_rows(tgt[sl[s]]) for s in splits if s != "full"}
    fit = sl[fit_name]

    user_ids = set(cfg.get("user_books") or []) | {base_id}
    profile_ids = set(diag_cfg.get("profile") or []) | {base_id}

    _say(f"metrics: {len(variants)} variants; decision splits {dec_splits}, fit on '{fit_name}', "
         f"half-life by the {rank_by} book{'; HOLDOUT WILL BE READ' if use_holdout else ''}")
    results: Dict[str, dict] = {}
    traded: Dict[str, np.ndarray] = {}                  # sign x panel, smoothed at the fitted half-life, fit rows
    traded_full: Dict[str, np.ndarray] = {}

    def _signal(vid: str, p64: np.ndarray, sign: float, hl: float) -> np.ndarray:
        sm = bk.smoothed(sign * p64, hl)
        traded[vid] = sm[fit]
        return sm

    for vid, v in variants.items():
        p = panels.get(vid)
        if p is None:
            results[vid] = {"error": ps.errors.get(vid, "missing panel"), "expr": v["expr"],
                            **{k: v[k] for k in ("stage", "why", "group") if k in v}}
            continue
        p64 = np.asarray(p, dtype=np.float64)
        sign = dg.sign_from(p64[fit], tgt[fit], target_ranks=tgt_ranks[fit_name])
        row = {"expr": v["expr"], "stage": v["stage"], "why": v.get("why", ""), "group": v.get("group", ""),
               "sign": sign, "splits": {}, "distinct": dg.distinct_fraction(p64[fit])}
        for s in dec_splits:
            row["splits"][s] = dg.ic_row(p64[sl[s]], tgt[sl[s]], sign=sign, target_ranks=tgt_ranks[s])
        row["books"] = bk.books(sign * p64, tgt, fit, {s: sl[s] for s in dec_splits},
                                cost=cost, top_frac=top, rank_by=rank_by)
        sm = _signal(vid, p64, sign, row["books"]["hl_used"])
        for s in dec_splits:                                           # the IC of what is actually traded
            row["splits"][s]["rank_ic_traded"] = dg.nanmean_quiet(
                dg.rank_ic_series(sm[sl[s]], tgt[sl[s]], target_ranks=tgt_ranks[s]))
        if use_holdout or vid in profile_ids or vid in (diag_cfg.get("by_year") or []):
            traded_full[vid] = sm
        # the user's convention: sign + half-life from THEIR training period; their test = our holdout
        if user_name in sl and (vid in user_ids or use_holdout or v.get("final")):
            us = sl[user_name]
            sign_u = dg.sign_from(p64[us], tgt[us], target_ranks=tgt_ranks[user_name])
            evals = {user_name: us}
            if use_holdout and "holdout" in sl:
                evals["holdout"] = sl["holdout"]
            row["sign_user"] = sign_u
            row["ic_user"] = dg.ic_row(p64[us], tgt[us], sign=sign_u, target_ranks=tgt_ranks[user_name])
            if use_holdout and "holdout" in sl:
                row["ic_holdout"] = dg.ic_row(p64[sl["holdout"]], tgt[sl["holdout"]], sign=sign_u,
                                              target_ranks=tgt_ranks["holdout"])
            row["books_user"] = bk.books(sign_u * p64, tgt, us, evals, cost=cost, top_frac=top, rank_by=rank_by)
            if use_holdout:
                traded_full[vid] = bk.smoothed(sign_u * p64, row["books_user"]["hl_used"])
        if vid in profile_ids or v.get("profile"):
            row["profile"] = {s: bk.quantile_profile(sm, tgt, sl[s], n=int(diag_cfg.get("profile_n", 10)))
                              for s in dec_splits}
        results[vid] = row

    ok = {vid: panels[vid] for vid in variants if vid in panels}
    report: Dict[str, object] = {
        "factor_id": fid, "config": config_path,
        "stages": list(stages) or [s["id"] for s in cfg["stages"]],
        "provenance": provenance(store),
        "view": {"days": len(ps.dates), "symbols": len(ps.symbols), "first": ps.dates[0], "last": ps.dates[-1],
                 "warmup_rows": ps.trim},
        "label": {"kind": ps.label_kind, "horizon": h0, "buyable": ps.label_buyable},
        "cost_per_side": cost, "top_frac": top, "fit_split": fit_name, "user_split": user_name,
        "rank_by": rank_by, "halflives": list(bk.HALFLIVES), "device": str(ps.device),
        "splits_used": splits, "split_dates": {s: [ps.dates[sl[s].start], ps.dates[sl[s].stop - 1]] for s in splits},
        "results": results, "errors": ps.errors, "engine_timings": ps.timings,
    }

    if diagnostics and ok:
        diag: Dict[str, object] = {}
        tr = fit

        # signals of referenced variants from other stages (sign + half-life fitted here, the same way)
        for r in refs:
            if r in panels and r not in traded:
                p64 = np.asarray(panels[r], dtype=np.float64)
                sg = dg.sign_from(p64[tr], tgt[tr], target_ranks=tgt_ranks[fit_name])
                fh = bk.fit_halflives(sg * p64, tgt, tr, cost, top)
                _signal(r, p64, sg, fh["hl_long" if rank_by == "long" else "hl_ls"])

        want = [v for v in (diag_cfg.get("decay") or []) if v in traded and v in ok]
        if want:
            _say("diagnostics: decay")
            targets = {h: ps.target(h) for h in horizons}
            diag["decay"] = {vid: dg.decay(traded[vid], {h: targets[h][tr] for h in horizons}, sign=1.0)
                             for vid in want}

        want = [v for v in ok if v in traded_full and (use_holdout or v in (diag_cfg.get("by_year") or []))]
        if want:
            _say(f"diagnostics: by_year ({len(want)} variants)")
            rows_y: Dict[str, list] = {}
            for vid in want:
                sm = traded_full[vid]
                out_y = []
                for y in sorted(set(ps.years[scope].tolist())):
                    idx = np.nonzero(ps.years == y)[0]
                    idx = idx[(idx >= scope.start) & (idx < scope.stop)]
                    if idx.size < 20:
                        continue
                    out_y.append({"year": y, "days": int(idx.size),
                                  **bk.book_row(sm, tgt, slice(int(idx[0]), int(idx[-1]) + 1), cost, top)})
                rows_y[vid] = out_y
            diag["by_year"] = rows_y
            diag["by_year_scope"] = [ps.dates[scope.start], ps.dates[scope.stop - 1]]

        ctl_names = [k for k in list(controls) + list(ext_controls) if k in panels]
        want = [v for v in (diag_cfg.get("neutralise") or []) if v in ok and v in traded]
        if want and ctl_names:
            _say(f"diagnostics: neutralise ({len(want)} variants x {len(ctl_names)} controls, on the traded signal)")
            ctl_z = {k: dg._zrank(np.asarray(panels[k][tr], dtype=np.float64)) for k in ctl_names}
            neut: Dict[str, object] = {}
            for vid in want:
                r = results[vid]
                sig = traded[vid]
                y_z = dg._zrank(sig)

                def _resid_row(resid, info):
                    # The residual is not re-smoothed, so it turns over more than the signal it came
                    # from: its AFTER-cost numbers can collapse on cost alone.  The gross figures and
                    # the rank IC say whether the alpha is gone.
                    icr = dg.ic_row(resid, tgt[tr], sign=1.0, target_ranks=tgt_ranks[fit_name])
                    br = bk.book_row(resid, tgt[tr], slice(0, resid.shape[0]), cost, top)
                    return {"r2": info["mean_r2"], "rank_ic": icr["rank_ic"], "rank_icir": icr["rank_icir"],
                            **{k: br[k] for k in ("ls_sharpe", "ls_gross_sharpe", "long_gross_ann",
                                                  "short_gross_ann", "long_ann", "long_sharpe", "ls_turnover",
                                                  "long_turnover")}}

                base_ic = dg.ic_row(sig, tgt[tr], sign=1.0, target_ranks=tgt_ranks[fit_name])
                b0 = r["books"]["splits"][fit_name]
                entry = {"_traded_signal": {"r2": 0.0, "rank_ic": base_ic["rank_ic"],
                                            "rank_icir": base_ic["rank_icir"],
                                            **{k: b0[k] for k in ("ls_sharpe", "ls_gross_sharpe", "long_gross_ann",
                                                                  "short_gross_ann", "long_ann", "long_sharpe",
                                                                  "ls_turnover", "long_turnover")}},
                         "all_controls": _resid_row(*dg.neutralise(y_z, ctl_z, panel_ready=True,
                                                                   controls_ready=True))}
                raw_z = dg._zrank(np.asarray(ok[vid][tr], dtype=np.float64))
                entry["all_controls"]["r2_raw_panel"] = dg.neutralise(
                    raw_z, ctl_z, panel_ready=True, controls_ready=True)[1]["mean_r2"]
                for k in ctl_names:
                    entry[k] = _resid_row(*dg.neutralise(y_z, {k: ctl_z[k]}, panel_ready=True,
                                                         controls_ready=True))
                neut[vid] = entry
            diag["neutralise"] = neut

        pairs = [pr for pr in (diag_cfg.get("conditional") or [])
                 if pr.get("factor") in traded and pr.get("gate") in panels]
        if pairs:
            _say("diagnostics: conditional IC (of the traded signal; positive = works)")
            diag["conditional"] = {f"{pr['factor']}|{pr['gate']}": dg.conditional_ic(
                traded[pr["factor"]], tgt[tr], panels[pr["gate"]][tr], buckets=int(pr.get("buckets", 5)))
                for pr in pairs}

        ctl_all = [k for k in list(controls) + list(ext_controls) + list(gates) if k in panels]
        # The controls' own scores do not depend on the stage, and a dozen of them cost a minute or
        # two: only alongside the baseline, or when a stage asks for them.
        if ctl_all and (base_id in variants or diag_cfg.get("score_controls")):
            _say("diagnostics: the controls as factors")
            crow = {}
            for k in ctl_all:
                pk = np.asarray(panels[k], dtype=np.float64)
                sg = dg.sign_from(pk[tr], tgt[tr], target_ranks=tgt_ranks[fit_name])
                b = bk.books(sg * pk, tgt, tr, {s: sl[s] for s in dec_splits}, cost=cost, top_frac=top,
                             rank_by=rank_by)
                crow[k] = {"sign": sg, "rank_ic": dg.ic_row(pk[tr], tgt[tr], sign=sg,
                                                            target_ranks=tgt_ranks[fit_name])["rank_ic"],
                           "hl": b["hl_used"], "hl_ls": b["hl_ls"], "hl_long": b["hl_long"],
                           **{f"{s}_{m}": b["splits"][s][m] for s in dec_splits
                              for m in ("ls_sharpe", "long_gross_ann", "long_ann", "long_sharpe",
                                        "ls_turnover", "long_turnover")}}
            diag["controls"] = crow

        # Rank correlation of TRADED signals (controls enter raw, unsigned).  The baseline and any id in
        # `corr_ids` are included even when they belong to an earlier stage.
        corr_ids = [v for v in dict.fromkeys([base_id] + list(cfg.get("corr_ids") or []) + list(ok))
                    if v in traded]
        if cfg.get("corr_ids"):
            keep = set(cfg["corr_ids"]) | {base_id} | set(ok)
            corr_ids = [v for v in corr_ids if v in keep]
        extra = [k for k in (cfg.get("corr_with") or []) if k in panels]
        if len(corr_ids) + len(extra) >= 2:
            _say(f"diagnostics: rank correlation of traded signals ({len(corr_ids)} variants + {len(extra)} controls)")
            mats = {k: traded[k] for k in corr_ids}
            mats.update({k: np.asarray(panels[k][tr], dtype=np.float64) for k in extra})
            diag["rank_corr_train"] = dg.rank_corr_matrix(mats)
            diag["rank_corr_on"] = "traded signals (sign x panel, smoothed at the fitted half-life); controls raw"
        report["diagnostics"] = diag

    for s in splits:
        ledger.record(s, len(ok), purpose="stage metrics" + (" + diagnostics" if diagnostics else ""),
                      stage=",".join(report["stages"]))
    mem.stop()
    report["seconds"] = round(time.perf_counter() - t0, 1)
    report["peak_anon_gb"] = round(mem.peak, 2)

    name = tag or ("_".join(report["stages"]) if len(report["stages"]) <= 3 else "batch")
    path = out_dir / f"{name}.json"
    tmp = path.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(report, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
    os.replace(tmp, path)
    print(f"[runner] wrote {path} ({report['seconds']}s, peak anon {report['peak_anon_gb']} GiB)")
    return report


__all__ = ["run", "load_config"]
