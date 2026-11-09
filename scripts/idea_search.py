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
(``alphacube.plugins.load_plugins``) and ``alphacube.mining.gp.GPMiner(hooks=...)``.  The route is a re-plumbing,
not a different experiment: with ``$PARTURA_AC_FIXES`` unset it proposes, accepts and scores what the monkeypatching
version of this script did, draw for draw (``scripts/plugin_acceptance.py`` compares two evidence files).

The search sees train + valid of $PARTURA_VIEW (partura/study.py view: w01 = 20180102..20230807, w02 = 20180102..20251231); the test period is not opened.

    python scripts/idea_search.py <idea_id> [--guidance guidance/B01.yaml] [--budget 192] [--population 48]
                                  [--arms steer,control] [--seed 0] [--boost 8] [--tag e1] [--reward KIND]
                                  [--parts seeds,hood,priors|none]     (what the steer arm is made of: ablations)
                                  [--halflives 0,5,20]                 (the reward's half-life grid)
                                  [--screen-base pool|known] [--threshold 1.0]
    environment: PARTURA_REWARD_DEVICE=cuda|cpu  (the reward's sorts on an accelerator; recorded in the evidence)
                 PARTURA_AC_FIXES=in_sustain,nt_twins  (the plugin's two opt-in changes; see partura/ac_plugin.py)
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

limit_threads(int(os.environ.get("PARTURA_THREADS", 8)))
import numpy as np  # noqa: E402
import yaml  # noqa: E402

from partura import books as bk  # noqa: E402
from partura import diagnose as dg  # noqa: E402
from partura import ops_ext  # noqa: E402,F401  (registers the extension operators before the registry is built)
from partura import study  # noqa: E402
from partura.bridge import PARTURA_ROOT  # noqa: E402
from partura.panels import SHARED_CACHE, PanelSet  # noqa: E402
from partura.steer import DISCOVERY_MIN_PERIOD, PAIRED, REWARDS, Guidance, RewardContext, is_discovery  # noqa: E402
from partura import steer  # noqa: E402

argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


IDEA = argv[0]
if study.scheduling_env():    # coldstart_C05 / C06 / C07 and PROD; scheduling only (C05 PLAN revision 2): ~3 GB of the card per run
    os.environ.update(PARTURA_REPROMOTE="1", **study.host_caps())      # 4 slots, 2 ways, cache <= 24 GB unless the host says more
GPATH = opt("--guidance", "guidance/B01.yaml")
BUDGET, POP = int(opt("--budget", 192)), int(opt("--population", 48))
ARMS = opt("--arms", "steer,control").split(",")
if set(ARMS) - {"steer", "control"}:             # (the monkeypatching version ran any other name as a control)
    raise SystemExit(f"--arms takes steer and control; got {ARMS}")
SEED, BOOST, TAG = int(opt("--seed", 0)), float(opt("--boost", 8)), opt("--tag", "e1")
# the share of the first generation the idea's seeds may take (the rest is the generator's own random trees); 0.25 is
# what every episode before C02 used (POP // 4)
SEED_SHARE = float(opt("--seed-share", 0.25))
# What the steer arm is made of -- for ablations.  seeds: the idea's seeds enter the first generation;  hood: the
# idea's operators are sampled more often and a candidate must carry one of its core operators;  priors: the
# guidance's bans, down-weights, exact-equivalence and family thinning (and its coarse operator weights).
# The default is all three; ``--parts none`` makes the steer arm the control.
PARTS = {x for x in opt("--parts", "seeds,hood,priors").split(",") if x and x != "none"}
# the half-lives the reward tries for every candidate (first maximum on the training period wins).  0, 5, 20 is what
# e1-e5 used; a level-type idea whose seeds want slower smoothing (the batch's best members sit at 40-60) takes 60 as well
HLS = tuple(float(x) for x in opt("--halflives", "0,5,20").split(","))
if PARTS - {"seeds", "hood", "priors"}:
    raise SystemExit(f"--parts takes seeds, hood, priors (or none); got {sorted(PARTS)}")
# C05 (research/coldstart_C05/PLAN.md §2.1-2.5).  --ban-library: a JSON list of {"expr": ...} -- a candidate whose daily
# ranks correlate with one of them (|rho| >= --ban-rank-corr; AlphaCube's own RankSimilarityBan) or that has the same
# operator skeleton (fields, constants and windows abstracted) is refused.  --must-contain: an E mission's core -- every
# candidate must carry it verbatim, and its periphery (the operators outside the core) must not be one already seen around
# it (--periphery-seen, a JSON list of expressions).  --neutral-extra: a JSON list of {"expr", "sign", "hl"} -- the core's
# family, added to the long_neutral controls.  --graft-fill N: the seeds are topped up to N with random trees carrying
# the core (a daily-shaped non-root subtree of a generated tree replaced by it).
BAN_LIB, BAN_RHO = opt("--ban-library"), float(opt("--ban-rank-corr", 0.7))
CORE, PERI_SEEN, NEUTRAL_EXTRA = opt("--must-contain"), opt("--periphery-seen"), opt("--neutral-extra")
GRAFT_FILL = int(opt("--graft-fill", 0))
START, END, SPLIT = study.view()                             # $PARTURA_VIEW: w01 (default) or w02 (PROD W02L)
STORE = os.environ.get("PARTURA_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("PARTURA_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
MIRROR = MIRROR if MIRROR and os.path.isdir(MIRROR) else None      # a host without the D-major mirror reads the store itself

G = Guidance.load(PARTURA_ROOT / GPATH)
idea = next(i for i in G.spec["ideas"] if i["id"] == IDEA)
KIND = opt("--reward", idea.get("reward", "long_tradable"))
# a "discovery": the reward's own score (the worse of train and valid) clears this.  Level rewards are pure-long
# Sharpes; the marginal and screen rewards are differences against the pool / the base.
# (level rewards: a pure-long Sharpe; paired rewards: the information ratio of the paired daily difference --
# 1.0 over the 5.4 years of train + valid is a t-statistic of about 2.3)
THR = float(opt("--threshold", 1.0))


def found(c):
    """A find, by the one definition in partura.steer (paired rewards: both periods have to carry it)."""
    return is_discovery(KIND, c["score"], c.get("s_train"), c.get("s_valid"), THR)
if KIND not in REWARDS:
    raise SystemExit(f"unknown reward {KIND!r}; choose from {REWARDS}")
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
# which code produced this evidence: episode e3_I1 ran an older copy of this script on the server (a file missed in a
# sync) and nothing in its evidence said so -- the reference of the screen was not the one the card described
import hashlib  # noqa: E402

CODE = {f: hashlib.sha1((PARTURA_ROOT / f).read_bytes()).hexdigest()[:12] for f in
        ("scripts/idea_search.py", "partura/steer.py", "partura/steer_fast.py", "partura/ops_ext.py", "partura/books.py", "partura/ac_plugin.py", GPATH) if (PARTURA_ROOT / f).is_file()}
print(f"[idea] steer arm = {sorted(PARTS) or 'nothing (= the control)'}", flush=True)
print(f"[idea] code {CODE}; screen base {opt('--screen-base', 'pool')}; reward device {os.environ.get('PARTURA_REWARD_DEVICE', '') or 'numpy (reference)'}", flush=True)
print(f"[idea] {IDEA}: reward {KIND}; budget {BUDGET} (population {POP}); arms {ARMS}; idea operators {sorted(IDEA_OPS)}; must-contain {sorted(MUST)}", flush=True)

with slot():
    mem = MemoryGuard(self_limit_gb=float(os.environ.get("PARTURA_SELF_LIMIT_GB", 34)), cgroup_limit_gb=70).start()   # C05 PLAN revision 11: the host may allow more
    t0 = time.time()
    import torch
    # Load before anything touches default_registry() (ps.compute() below parses expressions, which does): installs
    # ops_ext's legacy-table entries and registers the "partura" fitness kind (see partura/ac_plugin.py; the one
    # thing it does NOT do by default is declare AlphaCube's in_sustain_* kernels real-valued -- that would enlarge
    # the search vocabulary, which the monkeypatching version never did).  Idempotent, so running this script twice
    # in one process (e.g. two arms of one pytest session) is safe.
    from alphacube.plugins import load_plugins

    from partura import ac_plugin
    FIXES = sorted(ac_plugin.fixes())
    print(f"[idea] plugins loaded: {', '.join(load_plugins(['partura.ac_plugin']))}; opt-in plugin fixes: {FIXES or 'none'}", flush=True)
    # PROD W02L ($PARTURA_GP_CPU_FALLBACK=1): when every GPU way is taken at the start, the whole search runs on the CPU
    # (the 1 TB / 96-core host) instead of queueing for the card -- same reward, same budget, numpy reward.  Unset = as before.
    from partura import guard as _guard
    GP_DEV = "cuda"
    _fb = os.environ.get("PARTURA_GP_CPU_FALLBACK", "")
    # W02L 2026-11-09: a CPU search took hours where the card takes 40 min, and with 12 run slots on 4 ways nearly every search
    # found the ways busy at its start -- tmp/gp_no_cpu_fallback (a runtime switch: running conductors keep their env) turns
    # "1" off, so a search waits for the card batch by batch like any other; "force" still forces the CPU.
    if _fb == "1" and (PARTURA_ROOT / "tmp" / "gp_no_cpu_fallback").exists():
        _fb = ""
    if _fb == "force" or (_fb == "1" and not _guard.way_free("gpu")):
        GP_DEV = "cpu"
        for _v in ("PARTURA_RANK_DEVICE", "PARTURA_REWARD_DEVICE"):
            os.environ.pop(_v, None)
        torch.set_num_threads(int(os.environ.get("PARTURA_GP_CPU_THREADS", 6)))
    print(f"[idea] search device: {GP_DEV}", flush=True)
    # ---- the reward's context, on the grid the GP will use (same view: start, end, warm-up)
    ps = PanelSet(STORE, START, END, warmup=60, device=GP_DEV, gpu_fraction=0 if GP_DEV == "cuda" else None, cache_dir=str(SHARED_CACHE), mirror_root=MIRROR,
                  workdir=str(PARTURA_ROOT / "tmp"), label_kind="open_vwap15", label_buyable=True, batch=8,
                  daily_root=os.environ.get("PARTURA_DAILY_ROOT") or None)
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
    # what a SCREEN idea is measured against: by default the pool's strongest member (the known family that already
    # has the generic frozen-quote screen) -- against the unscreened family one candidate in four "works" (e2_I1),
    # because its long book has a junk tail that almost any marker of odd names removes.  --screen-base known for the old reference.
    SCREEN_BASE = opt("--screen-base", "pool")
    ctx = RewardContext(tgt, tr, va, untradable=untradable, liq=np.asarray(aux["liq"], np.float64), pool=pool_sig,
                        base=pool_sig if SCREEN_BASE == "pool" else known_z, halflives=HLS)
    if KIND == "long_neutral":                     # C03: liquidity, volatility, 20-day reversal and the known family regressed out
        from partura.steer import neutral_basis, neutral_residual
        nq = ps.compute({"n_vol": "cross_mean(day_std(Ret), 20)", "n_rev": "div(day_last(Close), ts_delay(day_last(Close), 20))"})
        ctls = [aux["liq"], nq["n_vol"], nq["n_rev"], aux["known"]]
        if os.environ.get("PARTURA_NEUTRAL_SIZE"):   # C04: size (log float cap) regressed out as well
            ctls.append(ps.compute({"n_size": "LogFloatCap"})["n_size"])
        ctls += study.extra_controls(dates, PARTURA_ROOT)   # PROD W02L ruler B: the two champions ($PARTURA_EXTRA_CONTROLS; unset = none)
        if NEUTRAL_EXTRA:                            # C05 E missions: the core's family, as traded (sign x smoothed)
            fam = json.loads(Path(NEUTRAL_EXTRA).read_text(encoding="utf-8"))
            FP = ps.compute({f"f{i}": f["expr"] for i, f in enumerate(fam)})
            ctls += [bk.smoothed(float(f["sign"]) * np.asarray(FP[f"f{i}"], np.float64), float(f["hl"])) for i, f in enumerate(fam) if f"f{i}" in FP]
            print(f"[idea] neutral basis: {sum(f'f{i}' in FP for i in range(len(fam)))} of {len(fam)} family members added", flush=True)
        ctx.neutral_Q = neutral_basis(ctls)
        print(f"[idea] neutral basis ready: {ctx.neutral_Q.shape}", flush=True)
    print(f"[idea] context ready in {time.time() - t0:.0f}s: {len(dates)} days x {tgt.shape[1]} names; train {cut} days, valid {len(dates) - cut}; "
          f"untradable {untradable[np.isfinite(tgt)].mean():.1%} of the labelled cells", flush=True)

    from alphacube.catalog import default_registry
    from alphacube.parser import parse
    from alphacube.pipeline import run_mining

    EXT = ac_plugin.partura_operator_names()
    reg = default_registry()
    risky = {s.name for s in reg.list_all() if getattr(s, "resource_risk", False)}
    searchable = {s.name for s in reg.searchable(include_boolean=False, include_resource_risk=True)}
    print(f"[idea] registry: {len(searchable)} searchable operators ({len(EXT & searchable)} of Partura's); "
          f"idea operators missing from the search vocabulary: {sorted(n for n in IDEA_OPS if n not in searchable and n in {s.name for s in reg.list_all()})}", flush=True)

    # ---- the reward, as an AlphaCube scorer.  ParturaScorer lives in partura/ac_plugin.py (registered under the
    # fitness kind "partura" by load_plugins, above); this just tells it what to score with -- the ctx / KIND the
    # inline class used to capture, and the z-rank of the known family that p_rho_known is measured against (which
    # is NOT always ctx.base: with --screen-base pool the base is the pool's strongest member).
    ac_plugin.set_scorer_state(ctx, KIND, SPLIT, known=known_z)

    # ---- sampling hooks.  Both arms: the same operator library (Partura's operators in, AlphaCube's own
    # per-element-loop operators out).  The steer arm adds the guidance and the idea.  Built as plain SearchHooks
    # (alphacube.plugins) instead of rebinding the generator's methods: its own op_weight / accept hooks reach every
    # acceptance point (generate, the mutators -- the window and constant ones included --, crossover, the seeds).
    # Both arms' weights come from ONE formula, ac_plugin.arm_hooks (which also decides which arm the boost and the
    # guidance belong to, and is tested on that directly) -- not from a local copy that could drift from it.
    OPW = G.operator_weights()
    stats = Counter()
    seeds_repr = set()
    first_form = {}                                         # canonical key -> the first spelling the search proposed
    family_first = {}                                       # family key -> the first canonical member proposed
    # The guidance's own stream, reseeded per arm below: the thinning and sibling draws never come from the miner's
    # tree-building stream (reading them there made an arm's trajectory depend on how many candidates were thinned,
    # not just on the seed).  AlphaCube's generator keeps a stream of that kind itself, but accept(tree) is not
    # handed it and run_mining builds the generator out of the caller's reach, so the script keeps its own.
    hook_rng = random.Random((SEED * 2654435761) & 0xFFFFFFFF)

    def refused():
        """A tree turned down.  When it is the child of a window or constant mutation -- the two mutations AlphaCube
        used not to ask `acceptable` about at all -- it is also counted as a refused mutation."""
        if ac_plugin.asked_from("mutate_window", "mutate_constant"):
            stats["mutation_refused"] += 1
        return False

    def guidance_accept(tree):
        """``SearchHooks.accept``: AlphaCube asks it from the generator's own ``acceptable()``, AFTER the legal-root and
        the ban-set checks, for every tree it builds, mutates or crosses -- and for the seeds."""
        e = repr(tree)
        if e in seeds_repr and "seeds" in PARTS:
            return True
        stats["proposed"] += 1
        priors = "priors" in PARTS
        try:
            # a different spelling of something already proposed (abs_ of a non-negative, a window-1 identity,
            # a price leaf swapped ...) is not a new candidate: episode e1's first run spent most of the steer
            # arm on re-wrappings of one seed, all with the same score
            key = G.dedup_key(e)
            if priors and first_form.setdefault(key, e) != e:
                stats["equivalent"] += 1
                return refused()
            if priors and G.banned(e):
                stats["banned"] += 1
                return refused()
            if "hood" in PARTS and MUST and not (MUST & set(re.findall(r"[A-Za-z_][A-Za-z_0-9]*", e))):
                stats["outside"] += 1
                return refused()
            if priors and not G.accept(e, u=hook_rng.random()):
                stats["thinned"] += 1
                return refused()
            # a sibling by renaming of price fields of something already proposed: usually close, sometimes
            # not -- sampled less often, never refused for good
            fam = G.family_key(e)
            if priors and family_first.setdefault(fam, key) != key and hook_rng.random() >= G.family_weight:
                stats["sibling"] += 1
                return refused()
        except ValueError:
            stats["unread"] += 1                         # a tree the string matcher cannot read is not judged
        stats["accepted"] += 1
        return True

    seeds = []
    for s in idea.get("seeds", []):
        try:
            e = parse(G.canonical(s), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
            seeds.append(e)
            seeds_repr.add(repr(e))
        except Exception as exc:                             # noqa: BLE001
            print(f"[idea] seed dropped ({type(exc).__name__}: {str(exc)[:80]}): {s}", flush=True)
    print(f"[idea] {len(seeds)} of {len(idea.get('seeds', []))} seeds parse in the search grammar", flush=True)

    # ---- C05: the library bans, the pinned core and its periphery, the grafted seeds
    from collections import Counter as _Counter
    from dataclasses import replace as _dc_replace

    from alphacube.expression import ShapeError, is_valid_root
    from alphacube.expression import replace as _ex_replace
    from alphacube.mining.clustering import skeleton_key

    def _p(s):
        return parse(s, strict=True, coerce_daily=True, n_minutes=241, allow_general=True)

    def skel(t):
        return re.sub(r"@\d+", "", skeleton_key(t))

    def _ops(t):
        return _Counter(n.name for n in t.nodes() if n.operands)

    LIB = []
    if BAN_LIB:
        for x in json.loads(Path(BAN_LIB).read_text(encoding="utf-8")):
            try:
                LIB.append(_p(x["expr"] if isinstance(x, dict) else x))
            except Exception as exc:                         # noqa: BLE001
                print(f"[idea] library member dropped ({type(exc).__name__}): {str(x)[:80]}", flush=True)
    SKEL_BAN = {skel(t) for t in LIB}
    if os.environ.get("PARTURA_SKELETON_BAN_FILE"):          # PROD W02L: the skeletons of a whole library, refused without being
        n0 = len(SKEL_BAN)                                   # rank-ban exemplars (a JSON list of expressions); unset = as before
        for x in json.loads(Path(os.environ["PARTURA_SKELETON_BAN_FILE"]).read_text(encoding="utf-8")):
            try:
                SKEL_BAN.add(skel(_p(x["expr"] if isinstance(x, dict) else x)))
            except Exception:                                # noqa: BLE001
                pass
        print(f"[idea] skeleton ban file: +{len(SKEL_BAN) - n0} skeletons", flush=True)
    core_t = _p(CORE) if CORE else None
    core_key = core_t.key() if core_t is not None else None
    core_ops = _ops(core_t) if core_t is not None else _Counter()

    def has_core(t):
        return any(n.key() == core_key for n in t.nodes())

    def periphery(t):
        c = _ops(t)
        c.subtract(core_ops)
        return frozenset(k for k, v in c.items() if v > 0)

    SEEN = {frozenset()}                                      # the core alone is not a new periphery
    if core_t is not None and PERI_SEEN:
        for s in json.loads(Path(PERI_SEEN).read_text(encoding="utf-8")):
            try:
                t = _p(s["expr"] if isinstance(s, dict) else s)
            except Exception:                                # noqa: BLE001
                continue
            if has_core(t):
                SEEN.add(periphery(t))

    def c05_ok(t, count=True):
        why = ("c05_skeleton" if SKEL_BAN and skel(t) in SKEL_BAN else
               "c05_no_core" if core_t is not None and not has_core(t) else
               "c05_periphery_seen" if core_t is not None and periphery(t) in SEEN else None)
        if why and count:
            stats[why] += 1
        return why is None

    C05 = bool(SKEL_BAN or core_t is not None)
    print(f"[idea] C05: library {len(LIB)} (rank ban {BAN_RHO if LIB else 'off'}, {len(SKEL_BAN)} skeletons); core {CORE or 'none'}; "
          f"{len(SEEN) - 1} peripheries seen around it", flush=True)
    if core_t is not None and GRAFT_FILL > len(seeds):
        from alphacube.mining.generator import TypedTreeGenerator
        bh = ac_plugin.arm_hooks("control", risky=risky, ext=EXT)
        gseed = (SEED * 7919 + 17) & 0xFFFFFFFF
        gen = TypedTreeGenerator(reg, seed=gseed, allow_resource_risk=True, op_weight=bh.op_weight,
                                 daily_fields=bh.daily_fields, daily_leaf_prob=bh.daily_leaf_prob)
        grng = random.Random(gseed)
        have = {skel(e) for e in seeds}
        n0, tries = len(seeds), 0
        while len(seeds) < GRAFT_FILL and tries < 20000:
            tries += 1
            try:
                t = gen.generate()
            except Exception:                                # noqa: BLE001
                continue
            slots = [n for n in t.nodes()[1:] if n.shape.collapsed and n.shape.degenerate]
            if not slots:
                continue
            try:
                g = _ex_replace(t, grng.choice(slots), core_t)
            except ShapeError:
                continue
            if not is_valid_root(g) or not c05_ok(g, count=False) or skel(g) in have:
                continue
            have.add(skel(g))
            seeds.append(g)
            seeds_repr.add(repr(g))
        print(f"[idea] C05: {len(seeds) - n0} grafted seeds carry the core ({tries} trees drawn)", flush=True)

    from partura.guard import exclusive
    import contextlib as _ctx
    gpu_lock = exclusive("gpu") if GP_DEV == "cuda" else _ctx.nullcontext()   # one of the GPU ways for the whole search (a CPU search takes none)
    gpu_lock.__enter__()
    if GP_DEV == "cuda" and torch.cuda.is_available():
        # $PARTURA_GP_GPU_FRACTION: a search holds its way and this share of the card for the whole search, so ways x fraction
        # must stay under 1 (W02L, 2026-11-09: 4 ways x 0.40 left the card short and whole searches came back with 0 valid)
        torch.cuda.set_per_process_memory_fraction(float(os.environ.get("PARTURA_GP_GPU_FRACTION", 0.40)))
    evidence = {"idea": idea, "reward": KIND, "threshold": THR, "screen_base": SCREEN_BASE, "score_scale": "paired_ir_sized" if KIND in PAIRED else "long_sharpe", "code": CODE, "reward_device": os.environ.get("PARTURA_REWARD_DEVICE", ""), "search_device": GP_DEV, "budget": BUDGET, "population": POP, "seed": SEED, "boost": BOOST, "period": [START, END, SPLIT],
                "guidance": GPATH, "parts": sorted(PARTS), "halflives": list(HLS), "plugin_fixes": FIXES, "seed_share": SEED_SHARE,
                "env_opw": os.environ.get("PARTURA_ENV_OPW", ""), "rho_reject": os.environ.get("PARTURA_RHO_REJECT", ""),
                "daily_fields": os.environ.get("PARTURA_DAILY_FIELDS", ""), "neutral_size": bool(os.environ.get("PARTURA_NEUTRAL_SIZE")),
                "c05": {"ban_library": BAN_LIB, "library": len(LIB), "ban_rank_corr": BAN_RHO if LIB else None, "skeletons": len(SKEL_BAN),
                        "core": CORE, "peripheries_seen": len(SEEN) - 1, "neutral_extra": NEUTRAL_EXTRA, "graft_fill": GRAFT_FILL,
                        "seeds": [repr(e) for e in seeds]} if C05 or NEUTRAL_EXTRA else None, "arms": {}}
    for arm in ARMS:
        ta = time.time()
        stats.clear()
        first_form.clear()
        family_first.clear()
        hook_rng.seed((SEED * 2654435761) & 0xFFFFFFFF)
        n0 = len(ac_plugin.SCORERS)
        # THIS arm's hooks, built from the arm's own name -- arm_hooks is what decides that the boost (the idea's
        # operators) and the guidance's weights belong to "steer" and that "control" gets the base library filter
        # alone; the keywords below are the same for both arms.  What the steer arm is made of (--parts) is passed on
        # as well: no priors = no guidance weights, no hood = no boost, neither = no accept hook at all, which makes
        # that arm the control to the last draw.  Set as the plugin's module state as well as passed, so anything
        # else in the process that asks the plugin for its hooks mid-run (alphacube.plugins.search_hooks_from) sees
        # the arm actually running.
        hooks = ac_plugin.arm_hooks(arm, parts=PARTS, risky=risky, ext=EXT, opw=OPW, idea_ops=IDEA_OPS, boost=BOOST,
                                    accept=guidance_accept, nt_twins="nt_twins" in FIXES)
        if C05:                                              # the library's skeletons and the core, in front of whatever else judges
            inner = hooks.accept

            def c05_accept(t, inner=inner):
                if not c05_ok(t):
                    return refused()
                return True if inner is None else inner(t)
            hooks = _dc_replace(hooks, accept=c05_accept)
        ac_plugin.set_search_hooks(hooks)
        # the in-memory panel cache only saves recomputation (results do not depend on it); a host with more memory
        # (the second server: 1 TB) raises it with $PARTURA_PANEL_CACHE_GB / $PARTURA_PANEL_CACHE_ITEMS
        gp = dict(population_size=POP, min_depth=2, max_depth=4, fitness_kind="partura",
                  panel_cache_items=int(os.environ.get("PARTURA_PANEL_CACHE_ITEMS", 256)),
                  panel_cache_bytes=int(float(os.environ.get("PARTURA_PANEL_CACHE_GB", 6)) * 1024 ** 3), hooks=ac_plugin.search_hooks())
        if arm == "steer" and seeds and "seeds" in PARTS:
            gp.update(initial_population=list(seeds), seed_keep=min(len(seeds), max(1, int(POP * SEED_SHARE))), seed_max_depth=9)
        if LIB:
            gp.update(ban_rank_corr=BAN_RHO, ban_exemplars=list(LIB))
            if os.environ.get("PARTURA_EXEMPLAR_CACHE"):   # PROD W02L: an exemplar's rank fingerprint is computed once and kept
                gp.update(exemplar_cache=os.environ["PARTURA_EXEMPLAR_CACHE"],   # on disk (AlphaCube's ExemplarCache, keyed by
                          exemplar_cache_gb=float(os.environ.get("PARTURA_EXEMPLAR_CACHE_GB", 40)))   # the view); unset = as before
        import shutil
        shutil.rmtree(ep_dir / arm, ignore_errors=True)       # a shorter rerun must not read the longer run's last checkpoint
        err = None
        try:
            run_mining(STORE, mirror_root=MIRROR, start=START, end=END, warmup=60, label="open_vwap15_buyable", horizon=1, miner="gp",
                       budget=BUDGET, seed=SEED, device=GP_DEV, pool="mse", pool_capacity=10, dedup=0.95, min_coverage=0.9,
                       min_scored_days=0.5, cost_per_side=0.0015, checkpoint_every=1, rolling_block=0, block_combine=False,
                       combine_methods=(), smooth_halflives=(), allow_resource_risk=True, workdir=str(PARTURA_ROOT / "tmp"),
                       out_root=str(ep_dir), run_id=arm, save_values=False, gp_params=gp,
                       **({"daily_root": os.environ["PARTURA_DAILY_ROOT"]} if os.environ.get("PARTURA_DAILY_ROOT") else {}))
        except Exception as exc:                             # noqa: BLE001  (the archive checkpoints are what we read)
            err = f"{type(exc).__name__}: {str(exc)[:300]}"
            print(f"[idea] {arm}: run_mining ended with {err}", flush=True)
        ac_plugin.set_search_hooks(None)                     # nothing of this arm's opinion outlives it
        files = sorted((ep_dir / arm / "checkpoints").glob("archive_gen*.csv"))
        rows = list(csv.DictReader(files[-1].open(encoding="utf-8"))) if files else []

        def num(r, k):
            try:
                return float(r.get(k, "nan"))
            except ValueError:
                return float("nan")

        cand = [{"expr": r["expression"], "fit": num(r, "fitness"), "score": num(r, "score_p_score"), "s_train": num(r, "score_p_s_train"),
                 "s_valid": num(r, "score_p_s_valid"), "share": num(r, "score_p_share"), "train": num(r, "score_p_train_sharpe"), "valid": num(r, "score_p_valid_sharpe"),
                 "train_ann": num(r, "score_p_train_ann"), "valid_ann": num(r, "score_p_valid_ann"), "hl": num(r, "score_p_hl"), "sign": num(r, "score_p_sign"),
                 "turnover": num(r, "score_p_turnover"), "rho_known": num(r, "score_p_rho_known"),
                 **{k: num(r, f"score_p_{k}") for k in ("ir_train", "ir_valid", "dann_train", "dann_valid")}} for r in rows]
        live = [c for c in cand if math.isfinite(c["fit"])]
        passers = [c for c in live if found(c)]
        scored = sum(s.n for s in ac_plugin.SCORERS[n0:])
        best5 = sorted(live, key=lambda c: -c["fit"])[:5]
        for c in best5:
            print(f"        best: score {c['score']:+.2f} (train {c['train']:+.2f} valid {c['valid']:+.2f}) hl {c['hl']:g} rho_known {c['rho_known']:+.2f} | {c['expr'][:140]}", flush=True)
        evidence["arms"][arm] = {"error": err, "checkpoints": len(files), "seconds": time.time() - ta, "scored": scored, "gate_fail": sum(s.gate for s in ac_plugin.SCORERS[n0:]),
                                 "rho_rejected": sum(getattr(s, "rho_rejected", 0) for s in ac_plugin.SCORERS[n0:]),
                                 "scoring_seconds": sum(s.seconds for s in ac_plugin.SCORERS[n0:]), "archive": len(cand), "live": len(live),
                                 "passers": len(passers), "sampling": dict(stats), "candidates": sorted(live, key=lambda c: -c["fit"])[:80],
                                 "heads": [], "independent_distinct": 0}   # (no passers at all: stays 0 -- C05 PLAN revision 2)
        print(f"[idea] {arm}: {scored} scored, {len(live)} live in the archive, {len(passers)} pass (score >= {THR:g}{', each period >= ' + format(DISCOVERY_MIN_PERIOD, 'g') if KIND in PAIRED else ''}) "
              f"in {time.time() - ta:.0f}s; sampling {dict(stats)}", flush=True)
        (ep_dir / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=1, default=float), encoding="utf-8")

    gpu_lock.__exit__(None, None, None)
    # ---- are the passers distinct, and are they the known pool?  (training period, every 5th day)
    allp = {}
    for arm in evidence["arms"]:
        for c in evidence["arms"][arm]["candidates"]:
            if found(c):
                allp.setdefault(c["expr"], c)
    if allp:
        P = ps.compute({f"c{i}": e for i, e in enumerate(allp)})
        Z = {}
        for i, (e, c) in enumerate(allp.items()):
            if f"c{i}" in P:
                sm_ = bk.smoothed(c["sign"] * steer.signal_input(P[f"c{i}"]), c["hl"])     # C07: ranked first if asked
                if KIND == "long_neutral":                   # what the reward traded: the residual on the style controls
                    sm_ = neutral_residual(sm_, ctx.neutral_Q)
                Z[e] = dg._zrank(sm_)[:cut:5]

        def rho(a, b):
            ok = np.isfinite(a) & np.isfinite(b)
            x, y = np.where(ok, a, 0.0), np.where(ok, b, 0.0)
            n = np.maximum(ok.sum(1), 1)
            with np.errstate(invalid="ignore", divide="ignore"):
                c = ((x * y).sum(1) - x.sum(1) * y.sum(1) / n) / np.sqrt(((x ** 2).sum(1) - x.sum(1) ** 2 / n) * ((y ** 2).sum(1) - y.sum(1) ** 2 / n))
            return float(np.nanmean(c))

        pz, kz = pool_sig[:cut:5], known_z[:cut:5]
        for arm in evidence["arms"]:
            A = evidence["arms"][arm]
            heads = []
            for c in A["candidates"]:
                if c["expr"] not in Z or not found(c):
                    continue
                # both correlations on the signal that would be TRADED (smoothed at the chosen half-life), the same
                # measurement for the pool and for the known family; one that cannot be measured does not pass
                c["rho_pool"], c["rho_known_traded"] = rho(Z[c["expr"]], pz), rho(Z[c["expr"]], kz)
                if KIND != "long_screen" and not (abs(c["rho_pool"]) < 0.5 and abs(c["rho_known_traded"]) < 0.5):
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

evidence["complete"] = True                                  # C05 PLAN revision 7: only the last write says so
(ep_dir / "evidence.json").write_text(json.dumps(evidence, ensure_ascii=False, indent=1, default=float), encoding="utf-8")
print(f"\nwrote {ep_dir / 'evidence.json'} ({time.time() - t0:.0f}s)")
