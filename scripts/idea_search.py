"""Hand an idea to AlphaCube: a short, steered GP search -- and its control.

An idea (``guidance/<batch>.yaml`` -> ``ideas``) is a hypothesis plus the neighbourhood it lives in: seed
expressions, the operators and leaves it is made of, and the reward that would pay for it.  This script turns it
into a search configuration for AlphaCube's own GP and runs it for a small budget, twice:

    steer    seeds in the first population; operators of the idea sampled more often; every proposed tree passed
             through the guidance (bans, down-weights, up-weights -- ``partura.steer.Guidance.accept``) and
             required to stay inside the idea's neighbourhood
    control  the same GP, the same reward, the same budget and random seed, the same operator library --
             no seeds, no guidance, uniform sampling

Both arms are scored by the same Partura reward (``partura.steer.reward``), so the only difference between them
is the intervention.  What is compared is discovery efficiency: of the candidates each arm paid to evaluate, how
many pass the gates with a long leg on both train and valid, and how many of those are distinct and not the
known pool.  Nothing in AlphaCube is edited and nothing in it is monkeypatched: the reward is registered as the
``"partura"`` fitness kind and the sampling hooks are plain ``alphacube.plugins.SearchHooks`` (``op_weight`` /
``accept``), both reached through ``partura.ac_plugin``, AlphaCube's own plugin loader
(``alphacube.plugins.load_plugins``) and ``alphacube.mining.gp.GPMiner(hooks=...)``.

The search sees 20180102..20230807 (train + valid); the test period is not opened.

    python scripts/idea_search.py <idea_id> [--guidance guidance/B01.yaml] [--budget 192] [--population 48]
                                  [--arms steer,control] [--seed 0] [--boost 8] [--tag e1] [--reward KIND]
"""
import csv
import json
import math
import os
import random
import re
import sys
import time
from collections import Counter
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.guard import MemoryGuard, limit_threads, slot  # noqa: E402

limit_threads(8)
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401  (registers the extension operators before the registry is built)
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import Guidance, RewardContext, reward as steer_reward  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


IDEA = argv[0]
GPATH = opt("--guidance", "guidance/B01.yaml")
BUDGET, POP = int(opt("--budget", 192)), int(opt("--population", 48))
ARMS = opt("--arms", "steer,control").split(",")
SEED, BOOST, TAG = int(opt("--seed", 0)), float(opt("--boost", 8)), opt("--tag", "e1")
START, END, SPLIT = "20180102", "20230807", "20220101"
STORE, MIRROR = "/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "/root/autodl-tmp/AlphaCube/mirror"

G = Guidance.load(PARTURA_ROOT / GPATH)
idea = next(i for i in G.spec["ideas"] if i["id"] == IDEA)
KIND = opt("--reward", idea.get("reward", "long_tradable"))
# a "discovery": the reward's own score (the worse of train and valid) clears this.  Level rewards are pure-long
# Sharpes; the marginal and screen rewards are differences against the pool / the base.
THR = float(opt("--threshold", 0.2 if KIND in ("long_marginal", "long_screen") else 1.0))
gram = idea.get("grammar") or {}
IDEA_OPS = set()
for key in ("day_ops", "memory_ops", "convex", "fold", "inner", "ops"):
    for x in gram.get(key, []):
        IDEA_OPS.update(re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", x) or [x])
for s in idea.get("seeds", []):
    IDEA_OPS.update(re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", s))
MUST = set(gram.get("day_ops", []))                       # the neighbourhood: a candidate must carry one of these
ep_dir = PARTURA_ROOT / "episodes" / f"{TAG}_{IDEA}"
ep_dir.mkdir(parents=True, exist_ok=True)
print(f"[idea] {IDEA}: reward {KIND}; budget {BUDGET} (population {POP}); arms {ARMS}; idea operators {sorted(IDEA_OPS)}; must-contain {sorted(MUST)}", flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=34, cgroup_limit_gb=70).start()
    t0 = time.time()
    import torch
    # Load before anything touches default_registry() (ps.compute() below parses
    # expressions, which does): installs ops_ext's legacy-table entries, declares
    # AlphaCube's own in_sustain_* kernels real-valued and registers the "partura"
    # fitness kind -- see partura/ac_plugin.py.  Idempotent, so running this script
    # twice in one process (e.g. two arms of one pytest session) is safe.
    from alphacube.plugins import load_plugins

    from partura import ac_plugin
    print(f"[idea] plugins loaded: {', '.join(load_plugins(['partura.ac_plugin']))}", flush=True)
    # ---- the reward's context, on the grid the GP will use (same view: start, end, warm-up)
    ps = PanelSet(STORE, START, END, warmup=60, device="cuda", gpu_fraction=0, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8)
    pool_spec = G.spec["pool"][-1]
    aux = ps.compute({"frozen": "cross_max(day_zero_ratio(Ret), 15)", "age": "cross_valid_count(day_last(Close), 241)",
                      "liq": "cross_mean(day_sum(Amt), 30)", "pool": pool_spec["expr"], "known": G.spec["pool"][0]["expr"]})
    tgt = ps.target(1)
    dates = np.asarray(ps.dates)
    cut = int(np.searchsorted(dates, SPLIT))
    tr, va = slice(0, cut), slice(cut, len(dates))
    frozen = np.asarray(aux["frozen"], np.float64)
    fr_rank = dg._zrank(frozen) + 0.5                                         # per-day percentile in [0, 1]
    # listed (or trading) for less than nine tenths of the last 241 days -- of the days the view has seen so far,
    # so the first year of the view is not thrown away wholesale
    possible = np.minimum(241, np.arange(1, len(dates) + 1))[:, None]
    untradable = (fr_rank > 0.8) | (np.asarray(aux["age"], np.float64) < 0.9 * possible) | ~np.isfinite(frozen)
    pool_sig = dg._zrank(bk.smoothed(float(pool_spec["sign"]) * np.asarray(aux["pool"], np.float64), float(pool_spec["hl"])))
    known_z = dg._zrank(float(G.spec["pool"][0]["sign"]) * np.asarray(aux["known"], np.float64))
    ctx = RewardContext(tgt, tr, va, untradable=untradable, liq=np.asarray(aux["liq"], np.float64), pool=pool_sig, base=known_z, halflives=(0.0, 5, 20))
    print(f"[idea] context ready in {time.time() - t0:.0f}s: {len(dates)} days x {tgt.shape[1]} names; train {cut} days, valid {len(dates) - cut}; "
          f"untradable {untradable[np.isfinite(tgt)].mean():.1%} of the labelled cells", flush=True)

    from alphacube.catalog import default_registry
    from alphacube.parser import parse
    from alphacube.pipeline import run_mining
    from alphacube.plugins import SearchHooks

    EXT = {getattr(f, "__name__", str(f)) for f in getattr(ops_ext, "NEW_OPERATORS", ())}
    EXT |= {"nt_" + n for n in EXT}
    reg = default_registry()
    risky = {s.name for s in reg.list_all() if getattr(s, "resource_risk", False)}
    searchable = {s.name for s in reg.searchable(include_boolean=False, include_resource_risk=True)}
    print(f"[idea] registry: {len(searchable)} searchable operators ({len(EXT & searchable)} of Partura's); "
          f"idea operators missing from the search vocabulary: {sorted(n for n in IDEA_OPS if n not in searchable and n in {s.name for s in reg.list_all()})}", flush=True)

    # ---- the reward, as an AlphaCube scorer.  ParturaScorer now lives in partura/ac_plugin.py
    # (registered under the fitness kind "partura" by load_plugins, above); this just tells it
    # what to score with -- the ctx/KIND closure the inline class used to capture directly.
    ac_plugin.set_scorer_state(ctx, KIND, SPLIT)

    # ---- sampling hooks.  Both arms: the same operator library (Partura's operators in, AlphaCube's own
    # per-element-loop operators out).  The steer arm adds the guidance and the idea.  Built as plain
    # SearchHooks (alphacube.plugins) instead of rebinding TypedTreeGenerator._pick / .acceptable: the
    # generator's own op_weight / accept hook reach every acceptance point for free (generate, the three
    # mutators, crossover, and generate()'s own fallback -- see docs/alphacube_steering_design.md, "乙
    # Steering hooks" items 1 and "must_fix #1"), which the old rebinding did not cover.
    OPW = G.operator_weights()
    stats = Counter()
    seeds_repr = set()
    first_form = {}                                         # canonical key -> the first spelling the search proposed
    # A dedicated, seed-reproducible stream for the guidance's thinning draw, reseeded per arm (below) --
    # never gen._rng: that is the miner's OWN tree-building stream, and reading u from it made the control
    # arm meaningless (its trajectory depended on how many candidates were thinned, not just on the seed).
    # TypedTreeGenerator exposes exactly this as gen.hook_rng -- but gen is built INSIDE run_mining and
    # never reaches the caller (no parameter, return field or callback carries it; verified: pipeline.py's
    # own `miner_ref` is a local, and RunResult has no such field), so this script cannot draw from the
    # live object itself and instead keeps its own, under the same name.
    hook_rng = random.Random(SEED)

    def base_weight(s):
        return 0.0 if (s.name in risky and s.name not in EXT) else 1.0

    def weighted(s):
        return base_weight(s) * OPW.get(s.name, 1.0) * (BOOST if s.name in IDEA_OPS else 1.0)

    def guidance_accept(tree):
        """``SearchHooks.accept``: called as ``self.accept_hook(tree)`` from the generator's own
        ``acceptable()``, AFTER it has already checked ``is_valid_root`` and the ban set -- so, unlike the
        old rebound ``acceptable(self, tree)``, this does not re-check either itself."""
        e = repr(tree)
        if e in seeds_repr:
            return True
        stats["proposed"] += 1
        try:
            # a different spelling of something already proposed (abs_ of a non-negative, a window-1 identity,
            # a price leaf swapped ...) is not a new candidate: episode e1's first run spent most of the steer
            # arm on re-wrappings of one seed, all with the same score
            key = G.dedup_key(e)
            if first_form.setdefault(key, e) != e:
                stats["equivalent"] += 1
                return False
            if G.banned(e):
                stats["banned"] += 1
                return False
            if MUST and not (MUST & set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", e))):
                stats["outside"] += 1
                return False
            if not G.accept(e, u=hook_rng.random()):
                stats["thinned"] += 1
                return False
        except ValueError:
            stats["unread"] += 1                         # a tree the string matcher cannot read is not judged
        stats["accepted"] += 1
        return True

    HOOKS = {"control": SearchHooks(op_weight=base_weight), "steer": SearchHooks(op_weight=weighted, accept=guidance_accept)}

    seeds = []
    for s in idea.get("seeds", []):
        try:
            e = parse(G.canonical(s), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
            seeds.append(e)
            seeds_repr.add(repr(e))
        except Exception as exc:                             # noqa: BLE001
            print(f"[idea] seed dropped ({type(exc).__name__}: {str(exc)[:80]}): {s}", flush=True)
    print(f"[idea] {len(seeds)} of {len(idea.get('seeds', []))} seeds parse in the search grammar", flush=True)

    from partura.guard import exclusive
    gpu_lock = exclusive("gpu")                               # one of the GPU ways for the whole search: a sweep may share the card, two may not
    gpu_lock.__enter__()
    if torch.cuda.is_available():
        torch.cuda.set_per_process_memory_fraction(0.40)
    evidence = {"idea": idea, "reward": KIND, "threshold": THR, "budget": BUDGET, "population": POP, "seed": SEED, "boost": BOOST, "period": [START, END, SPLIT],
                "guidance": GPATH, "arms": {}}
    for arm in ARMS:
        ta = time.time()
        stats.clear()
        first_form.clear()
        hook_rng = random.Random(SEED)      # fresh per arm; only the steer arm's guidance_accept ever draws from it
        n0 = len(ac_plugin.SCORERS)
        gp = dict(population_size=POP, min_depth=2, max_depth=4, fitness_kind="partura", panel_cache_items=256,
                  panel_cache_bytes=6 * 1024 ** 3, hooks=HOOKS[arm])
        if arm == "steer" and seeds:
            gp.update(initial_population=list(seeds), seed_keep=min(len(seeds), POP // 4), seed_max_depth=9)
        try:
            run_mining(STORE, mirror_root=MIRROR, start=START, end=END, warmup=60, label="open_vwap15_buyable", horizon=1, miner="gp",
                       budget=BUDGET, seed=SEED, device="cuda", pool="mse", pool_capacity=10, dedup=0.95, min_coverage=0.9,
                       min_scored_days=0.5, cost_per_side=0.0015, checkpoint_every=1, rolling_block=0, block_combine=False,
                       combine_methods=(), smooth_halflives=(), allow_resource_risk=True, workdir=str(PARTURA_ROOT / "tmp"),
                       out_root=str(ep_dir), run_id=arm, save_values=False, gp_params=gp)
        except Exception as exc:                             # noqa: BLE001  (the archive checkpoints are what we read)
            print(f"[idea] {arm}: run_mining ended with {type(exc).__name__}: {str(exc)[:300]}", flush=True)
        files = sorted((ep_dir / arm / "checkpoints").glob("archive_gen*.csv"))
        rows = list(csv.DictReader(files[-1].open(encoding="utf-8"))) if files else []

        def num(r, k):
            try:
                return float(r.get(k, "nan"))
            except ValueError:
                return float("nan")

        cand = [{"expr": r["expression"], "fit": num(r, "fitness"), "score": num(r, "score_p_score"), "train": num(r, "score_p_train_sharpe"), "valid": num(r, "score_p_valid_sharpe"),
                 "train_ann": num(r, "score_p_train_ann"), "valid_ann": num(r, "score_p_valid_ann"), "hl": num(r, "score_p_hl"), "sign": num(r, "score_p_sign"),
                 "turnover": num(r, "score_p_turnover"), "rho_known": num(r, "score_p_rho_known")} for r in rows]
        live = [c for c in cand if math.isfinite(c["fit"])]
        passers = [c for c in live if c["score"] >= THR]
        scored = sum(s.n for s in ac_plugin.SCORERS[n0:])
        best5 = sorted(live, key=lambda c: -c["fit"])[:5]
        for c in best5:
            print(f"        best: score {c['score']:+.2f} (train {c['train']:+.2f} valid {c['valid']:+.2f}) hl {c['hl']:g} rho_known {c['rho_known']:+.2f} | {c['expr'][:140]}", flush=True)
        # generator.unaccepted_fallbacks (how much of the steer arm's population the guidance never got
        # to see) is NOT reported here: it lives on the TypedTreeGenerator run_mining constructs internally,
        # and nothing run_mining/GPMiner returns -- not RunResult, not the checkpoint files, not an
        # on_generation callback -- exposes a reference to it or to the generator that built it (verified
        # against alphacube/pipeline.py and mining/gp.py). Surfacing it needs a channel added on the
        # AlphaCube side (outside WP11's file list); flagged here rather than faked.
        evidence["arms"][arm] = {"seconds": time.time() - ta, "scored": scored, "gate_fail": sum(s.gate for s in ac_plugin.SCORERS[n0:]),
                                 "scoring_seconds": sum(s.seconds for s in ac_plugin.SCORERS[n0:]), "archive": len(cand), "live": len(live),
                                 "passers": len(passers), "sampling": dict(stats), "candidates": sorted(live, key=lambda c: -c["fit"])[:80]}
        print(f"[idea] {arm}: {scored} scored, {len(live)} live in the archive, {len(passers)} pass (score >= {THR:g}) "
              f"in {time.time() - ta:.0f}s; sampling {dict(stats)}", flush=True)
        (ep_dir / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=1, default=float), encoding="utf-8")

    gpu_lock.__exit__(None, None, None)
    # ---- are the passers distinct, and are they the known pool?  (training period, every 5th day)
    allp = {}
    for arm in evidence["arms"]:
        for c in evidence["arms"][arm]["candidates"]:
            if c["score"] >= THR:
                allp.setdefault(c["expr"], c)
    if allp:
        P = ps.compute({f"c{i}": e for i, e in enumerate(allp)})
        Z = {}
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

        pz = pool_sig[:cut:5]
        for arm in evidence["arms"]:
            A = evidence["arms"][arm]
            heads = []
            for c in A["candidates"]:
                if c["expr"] not in Z or not c["score"] >= THR:
                    continue
                c["rho_pool"] = rho(Z[c["expr"]], pz)
                if KIND != "long_screen" and (abs(c["rho_pool"]) >= 0.5 or abs(c.get("rho_known") or 0) >= 0.5):
                    continue                                 # a screen is judged by what it does to the base, not by being unlike it
                if all(abs(rho(Z[c["expr"]], Z[h["expr"]])) < 0.7 for h in heads):
                    heads.append(c)
            A["independent_distinct"] = len(heads)
            A["heads"] = heads
            A["efficiency_per_100"] = 100.0 * len(heads) / max(A["scored"], 1)
            print(f"[idea] {arm}: {len(heads)} distinct passers outside the known pool = {A['efficiency_per_100']:.1f} per 100 scored", flush=True)
            for h in heads[:8]:
                print(f"        score {h['score']:+.2f} (train {h['train']:+.2f} valid {h['valid']:+.2f}) hl {h['hl']:g} rho_pool {h['rho_pool']:+.2f} | {h['expr'][:150]}", flush=True)
    mem.stop()

(ep_dir / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print(f"\nwrote {ep_dir / 'evidence.json'} ({time.time() - t0:.0f}s)")
