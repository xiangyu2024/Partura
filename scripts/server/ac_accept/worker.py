"""One task, run inside a subprocess whose PYTHONPATH is ONE tree's src/.

Never imported by the driver: the whole point is that the two trees' ``alphacube``
packages never share an interpreter. Everything this writes is meant to be compared
byte for byte, so every float goes out as its IEEE-754 bits (``struct.pack('>d')``)
and every array as a raw ``.npy``.

    worker.py <task> <outdir> [key=value ...]

tasks: registry | evalexpr | gp | rl
"""
from __future__ import annotations

import hashlib
import json
import os
import struct
import sys
from pathlib import Path

# Determinism controls applied identically on both sides, so a difference cannot be
# BLAS/thread-count noise. Set before torch is imported by anything.
os.environ.setdefault("OMP_NUM_THREADS", "1")
os.environ.setdefault("MKL_NUM_THREADS", "1")
os.environ.setdefault("VECLIB_MAXIMUM_THREADS", "1")


DEVICE = os.environ.get("VERIFY_DEVICE", "cpu")       # server copy: "cuda" there; the local harness was CPU only
STORE = os.environ.get("VERIFY_STORE", "/root/autodl-tmp/qmt_daily_data/fast_factor_compute")
MIRROR = os.environ.get("VERIFY_MIRROR", "/root/autodl-tmp/AlphaCube/mirror")
FACTORS = os.environ.get("VERIFY_FACTORS", "")        # batches/B01_single_factors.yaml


# --------------------------------------------------------------------------- canon

def fbits(x) -> str:
    """A float as its exact 64-bit pattern. ``repr`` would also round-trip, but this
    also separates 0.0 from -0.0 and keeps NaN payloads visible."""
    return struct.pack(">d", float(x)).hex()


def canon(obj):
    """Anything -> JSON-dumpable, with every float replaced by its bit pattern and
    every container's iteration order preserved."""
    import numpy as np

    if obj is None or isinstance(obj, (bool, str)):
        return obj
    if isinstance(obj, (int, np.integer)):
        return ["int", int(obj)]
    if isinstance(obj, (float, np.floating)):
        return ["f64", fbits(obj)]
    if isinstance(obj, (bytes, bytearray)):
        return ["bytes", bytes(obj).hex()]
    if isinstance(obj, np.ndarray):
        return ["ndarray", str(obj.dtype), list(obj.shape),
                hashlib.sha256(np.ascontiguousarray(obj).tobytes()).hexdigest()]
    if isinstance(obj, dict):
        return ["dict", [[canon(k), canon(v)] for k, v in obj.items()]]
    if isinstance(obj, (list, tuple)):
        return [("list" if isinstance(obj, list) else "tuple"), [canon(v) for v in obj]]
    if isinstance(obj, (set, frozenset)):
        return ["set", [canon(v) for v in sorted(obj, key=repr)]]
    if callable(obj):
        return ["callable", getattr(obj, "__module__", "?"), getattr(obj, "__qualname__", repr(obj))]
    if hasattr(obj, "_fields"):                       # namedtuple
        return ["nt", canon(dict(zip(obj._fields, tuple(obj))))]
    if hasattr(obj, "__dataclass_fields__"):
        return ["dc", type(obj).__name__,
                canon({f: getattr(obj, f) for f in obj.__dataclass_fields__})]
    return ["repr", repr(obj)]


def dump(path: Path, obj) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(canon(obj), ensure_ascii=False, indent=1, sort_keys=False),
                    encoding="utf-8")


# ----------------------------------------------------------------- the expressions
# Harvested from /Users/wxy/Desktop/AlphaCube/tests/*.py (every one of these string
# literals appears there), filtered to roots the engine will actually evaluate.
EXPRS = [
    "day_std(Ret)",
    "day_mean(Close)",
    "day_max(log(Amt))",
    "day_max(High)",
    "day_min(Low)",
    "day_mean(Ret)",
    "day_last(Close)",
    "day_sum(is_gt0(Ret))",
    "ts_mean(day_mean(Close), 5)",
    "day_std(in_mean_rolling(Close, 5))",
    "day_mean(nt_cs_rank(Close))",
    "mul(day_mean(Close), 2)",
    "add(day_mean(Close), 3)",
    "sub(0.5, day_max(Amt))",
    "cs_rank(day_mean(Close))",
    "cs_rank(Close)",
    "cross_mean(day_max(High), 3)",
    "ts_mean(day_std(Ret), 21)",
    "ts_corr(day_first(Open), day_sum(Volume), 10)",
    "nt_cs_rank(day_mean(Close))",
    "day_last(in_rank(Volume))",
    "sub(day_mean(Close), day_mean(Open))",
    "div(day_max(Close), close_1d)",
    "ts_mean(day_last(Close), 5)",
    "pow(day_mean(Close), 2)",
    "cs_scale(day_first(Vwap))",
    "ts_delta(day_mean(Close), 5)",
    "day_mean(in_zscore_rolling(Amt, 21))",
    "day_std(in_stddev_rolling(Ret, 5))",
    "is_gt0(day_mean(Ret))",
]


# -------------------------------------------------------------------------- tasks

def task_registry(out: Path, _args) -> None:
    """Operator name set, every OpSpec field (and every derived property), and
    searchable()'s ORDER under all four flag combinations."""
    import dataclasses

    from alphacube import catalog as cat

    reg = cat.default_registry()
    ops = reg._ops                                    # insertion-ordered dict

    spec_fields = [f.name for f in dataclasses.fields(type(next(iter(ops.values()))))]
    props = [n for n, v in vars(type(next(iter(ops.values())))).items()
             if isinstance(v, property)]

    rows = []
    for name, s in ops.items():                       # registration order, not sorted
        row = {"__key__": name}
        for f in spec_fields:
            row[f] = getattr(s, f)
        for p in sorted(props):
            try:
                row["@" + p] = getattr(s, p)
            except Exception as exc:                  # noqa: BLE001
                row["@" + p] = f"<raised {type(exc).__name__}: {exc}>"
        rows.append(row)

    dump(out / "ops_in_registration_order.json", rows)
    dump(out / "op_names_sorted.json", sorted(ops))
    dump(out / "op_names_registration_order.json", list(ops))

    searchable = {}
    for b in (True, False):
        for r in (True, False):
            key = f"boolean={b},resource_risk={r}"
            searchable[key] = [s.name for s in reg.searchable(include_boolean=b,
                                                              include_resource_risk=r)]
    dump(out / "searchable_order.json", searchable)
    dump(out / "list_all_order.json", [s.name for s in reg.list_all()])

    dump(out / "registry_scalars.json", {
        "fields": reg.fields, "constants": reg.constants, "len": len(reg),
        "n_skipped": len(reg.skipped),
        "skipped": [canon(dataclasses.asdict(r)) if dataclasses.is_dataclass(r) else repr(r)
                    for r in reg.skipped],
        "CUBE_FIELDS": cat.CUBE_FIELDS, "WINDOWS": cat.WINDOWS, "CONSTANTS": cat.CONSTANTS,
        "LOOKAHEAD_KERNELS": sorted(cat.LOOKAHEAD_KERNELS),
        "EXCLUDED_KERNELS": sorted(cat.EXCLUDED_KERNELS),
    })
    # Recorded separately: an attribute the new branch ADDS. Compared as an
    # additive-surface report, never folded into the bit-identity verdict.
    dump(out / "additive_surface.json", {
        "registry_daily_fields": getattr(reg, "daily_fields", "<absent>"),
        "catalog_DAILY_FIELDS": getattr(cat, "DAILY_FIELDS", "<absent>"),
        "catalog_REAL_VALUED_OVERRIDES": sorted(getattr(cat, "REAL_VALUED_OVERRIDES", ())),
        "collision_daily_vs_ops": sorted(set(getattr(reg, "daily_fields", ())) & set(reg._ops)),
        "collision_daily_vs_fields": sorted(set(getattr(reg, "daily_fields", ())) & set(reg.fields)),
    })


def task_evalexpr(out: Path, args) -> None:
    """Parse each expression, dump its tree identity, then evaluate the whole batch
    on the shared cube and dump each panel as a raw .npy."""
    import numpy as np

    from alphacube.catalog import default_registry
    from alphacube.engine.engine import CubeEngine
    from alphacube.expression import contains_lookahead, is_valid_root, max_window
    from alphacube.parser import parse
    from alphacube.store import open_cube_store

    reg = default_registry()
    store = open_cube_store(args["cube"])
    view = store.view()

    parsed, meta = [], []
    for src in EXPRS:
        rec = {"src": src}
        try:
            e = parse(src, reg, n_minutes=view.n_minutes)
        except Exception as exc:                      # noqa: BLE001
            rec["error"] = f"{type(exc).__name__}: {exc}"
            meta.append(rec)
            continue
        rec.update(repr=repr(e), key=e.key(), shape=repr(e.shape),
                   degenerate=bool(e.shape.degenerate),
                   max_window_D=max_window(e, "D"), max_window_M=max_window(e, "M"),
                   is_valid_root=is_valid_root(e), lookahead=contains_lookahead(e))
        parsed.append((src, e))
        meta.append(rec)
    dump(out / "parse.json", meta)

    eng = CubeEngine(view, device=DEVICE)
    res = eng.evaluate([e for _, e in parsed], tolerant=True)
    pans = out / "panels"
    pans.mkdir(parents=True, exist_ok=True)
    summary = []
    for i, ((src, _e), p) in enumerate(zip(parsed, res.panels)):
        rec = {"i": i, "src": src}
        if p is None:
            rec["panel"] = None
        else:
            a = np.ascontiguousarray(p)
            np.save(pans / f"{i:03d}.npy", a)
            rec.update(dtype=str(a.dtype), shape=list(a.shape),
                       sha256=hashlib.sha256(a.tobytes()).hexdigest(),
                       n_nan=int(np.isnan(a).sum()))
        summary.append(rec)
    dump(out / "eval.json", {"panels": summary, "errors": res.errors,
                             "n_rounds": len(getattr(res.plan, "rounds", []) or []),
                             "plan": repr(res.plan)})
    # chunked evaluation too: a different traversal of the same engine code
    eng2 = CubeEngine(view, device=DEVICE, chunk_symbols=3, chunk_days=7)
    res2 = eng2.evaluate([e for _, e in parsed], tolerant=True)
    pans2 = out / "panels_chunked"
    pans2.mkdir(parents=True, exist_ok=True)
    for i, p in enumerate(res2.panels):
        if p is not None:
            np.save(pans2 / f"{i:03d}.npy", np.ascontiguousarray(p))
    dump(out / "eval_chunked.json", {"errors": res2.errors})


def _scrub(line: str, out: Path) -> str:
    """Remove the two things that cannot match across two runs of the SAME code:
    wall-clock numbers, and this invocation's own output directory (which the run
    prints as it writes). Everything numeric that is a RESULT is compared
    unscrubbed, in result.json / members.csv / the archive CSVs / the .npy panels.
    The baseline-vs-baseline control is what proves this scrubber removes only
    noise: with it, every file in every task matches."""
    import re
    s = line.replace(str(out.resolve()), "<OUT>").replace(str(out), "<OUT>")
    s = re.sub(r"\d+(?:\.\d+)?s\b", "<T>s", s)
    s = re.sub(r"eta [^\s,)]+", "eta <T>", s)
    # server copy: the progress line also prints the process's and the container's memory, which another tenant's job
    # moves between two runs of the same code (seen: "cg 37/90G" against "cg 38/90G", every result file identical)
    s = re.sub(r"mem rss \S+ cache \S+ exem \S+ fam \S+ cg \S+", "mem <M>", s)
    return s


def _write_logs(out: Path, logs) -> None:
    (out / "log_raw.txt").write_text("\n".join(logs), encoding="utf-8")
    (out / "log_scrubbed.txt").write_text("\n".join(_scrub(s, out) for s in logs),
                                          encoding="utf-8")


def task_gp(out: Path, args) -> None:
    import alphacube.pipeline as P
    from alphacube.store import open_cube_store

    kind, seed = args["kind"], int(args["seed"])
    penalty = float(args.get("penalty", 0.0))
    store = open_cube_store(args["cube"])

    gp_params = dict(population_size=int(args.get("population", 16)), max_depth=3,
                     fitness_kind=kind, turnover_penalty=penalty)
    gp_params.update(json.loads(args.get("gp_extra", "{}")))

    logs = []
    runs = out / "runs"
    r = P.run_mining(
        store, start=store.dates[5], label="close", miner="gp",
        budget=int(args.get("budget", 64)), seed=seed,
        pool_capacity=4, dedup=0.99, warmup=int(args.get("warmup", 40)),
        gp_params=gp_params,
        rolling_block=int(args.get("rolling_block", 0)),
        ban_top_n=int(args.get("ban_top_n", 0)),
        block_combine=False,
        combine_methods=(), cost_per_side=0.0015,
        checkpoint_every=1, out_root=runs, run_id="r", save_values=True,
        log=logs.append, device=DEVICE,
    )
    _write_logs(out, logs)
    dump(out / "result.json", {
        "pool_size": r.pool_size, "added": r.added, "pool_metrics": r.pool_metrics,
        "members": r.members, "rejected": r.rejected, "summary": r.summary,
        "combination_is_none": r.combination is None,
        "run_dir_tail": None if r.run_dir is None else Path(r.run_dir).name,
    })


def task_rl(out: Path, args) -> None:
    """An RL miner through the same entry. The reward sequence is captured by
    subclassing BatchRewarder and teeing its return value -- no extra RNG use, no
    change to what the miner sees."""
    import alphacube.mining as M
    import alphacube.pipeline as P
    from alphacube.store import open_cube_store

    seq = []
    Base = M.BatchRewarder

    class Recording(Base):                            # noqa: D401
        def rewards(self, exprs):
            res = super().rewards(exprs)
            seq.append([{"expr": (None if e is None else repr(e)),
                         "reward": r.reward, "ic": r.ic, "added": bool(r.added),
                         "novelty": r.novelty, "reason": r.reason}
                        for e, r in zip(exprs, res)])
            return res

    store = open_cube_store(args["cube"])
    logs = []
    M.BatchRewarder = Recording                       # pipeline does `from .mining import ...`
    try:
        r = P.run_mining(
            store, start=store.dates[5], label="close", miner=args.get("miner", "alphagen"),
            budget=int(args.get("budget", 24)), seed=int(args["seed"]),
            pool_capacity=3, warmup=int(args.get("warmup", 40)),
            max_expr_len=12, rl_params=json.loads(args.get("rl_params", "{}")),
            gp_params=json.loads(args.get("gp_extra", "null")),
            combine_methods=(), out_root=out / "runs", run_id="r", save_values=True,
            log=logs.append, device=DEVICE,
        )
    except Exception as exc:                          # noqa: BLE001
        # A raise is itself a comparable outcome: one side crashing where the other
        # returned is exactly the kind of default-path break this task hunts for.
        _write_logs(out, logs)
        dump(out / "raised.json", {"type": type(exc).__name__, "msg": str(exc)})
        return
    finally:
        M.BatchRewarder = Base
    _write_logs(out, logs)
    dump(out / "reward_sequence.json", seq)
    dump(out / "result.json", {
        "pool_size": r.pool_size, "added": r.added, "pool_metrics": r.pool_metrics,
        "members": r.members, "rejected": r.rejected, "summary": r.summary,
    })


def task_generator(out: Path, args) -> None:
    """The random stream itself, with no engine in the way.

    This is backward-compat items 11-14 head-on: ``_pick``'s two ``choice`` calls
    (not ``choices``), ``hook_rng``'s construction not consuming a draw, and no new
    draw site inside ``generate`` / the five mutations / ``crossover``. Every draw
    the generator makes is observable here as the exact sequence of trees it builds
    and the RNG's internal state afterwards, so a single extra or reordered draw
    anywhere shows up as a diverging tree and a diverging state."""
    import random

    from alphacube.catalog import default_registry
    from alphacube.mining.generator import TypedTreeGenerator, one_layer_keys

    reg = default_registry()
    n_trees = int(args.get("n_trees", 400))
    mutations = ("mutate_subtree", "mutate_operator", "mutate_hoist",
                 "mutate_window", "mutate_constant")

    report, added = {}, {}
    for seed in (0, 1, 7, 12345):
        g = TypedTreeGenerator(reg, n_minutes=24, max_depth=4, min_depth=2,
                              rng=random.Random(seed))
        trees = [g.generate() for _ in range(n_trees)]
        rec = {
            "reprs": [repr(t) for t in trees],
            "keys": [t.key() for t in trees],
            "one_layer_keys": [sorted(one_layer_keys(t)) for t in trees],
            "rng_state_after_generate": repr(g._rng.getstate()),
            "first_random_after": g._rng.random(),
        }
        # mutations and crossover, driven off a fresh generator so the stream
        # position is reproducible and the mutation draws are the only ones left
        g2 = TypedTreeGenerator(reg, n_minutes=24, max_depth=4, min_depth=2,
                                rng=random.Random(seed))
        base = [g2.generate() for _ in range(60)]
        mut = {}
        for name in mutations:
            fn = getattr(g2, name)
            mut[name] = [(None if (r := fn(t)) is None else repr(r)) for t in base]
        mut["crossover"] = [(None if (r := g2.crossover(a, b)) is None else repr(r))
                            for a, b in zip(base, base[1:] + base[:1])]
        mut["rng_state_after_mutations"] = repr(g2._rng.getstate())
        rec["mutations"] = mut
        # population builder: its own retry loop on top of generate()
        g3 = TypedTreeGenerator(reg, n_minutes=24, max_depth=4, min_depth=2,
                                rng=random.Random(seed))
        rec["population"] = [repr(t) for t in g3.generate_population(48)]
        rec["rng_state_after_population"] = repr(g3._rng.getstate())
        report[f"seed{seed}"] = rec
        # Attributes the new branch ADDS. Kept out of generator.json so the identity
        # verdict is about the stream, and reported separately.
        added[f"seed{seed}"] = {
            "unaccepted_fallbacks": getattr(g3, "unaccepted_fallbacks", "<absent>"),
            "has_hook_rng": hasattr(g3, "hook_rng"),
            "accept_hook": getattr(g3, "accept_hook", "<absent>"),
            "op_weight": getattr(g3, "op_weight", "<absent>"),
            "daily_fields": getattr(g3, "daily_fields", "<absent>"),
            "daily_leaf_prob": getattr(g3, "daily_leaf_prob", "<absent>"),
            "leaf_slots": getattr(g3, "leaf_slots", "<absent>"),
            "mutation_checks_bans": getattr(g3, "mutation_checks_bans", "<absent>"),
        }

    dump(out / "generator.json", report)
    dump(out / "additive_surface.json", added)
    # The vocabulary the generator draws from, and in what order.
    g = TypedTreeGenerator(reg, n_minutes=24)
    dump(out / "vocabulary.json", {
        "fields": g.fields, "constants": g.constants,
        "specs": [s.name for s in g.specs],
        "producers": {k: [s.name for s in v] for k, v in g._producers.items()},
        "root_ops": [s.name for s in g._root_ops],
    })


# ------------------------------------------------------------------ production store

KNOWN = ["cross_mean(day_std(Amt), 30)", "cross_mean(day_sum(Amt), 30)", "ts_pearson(day_last(Close), 20)", "cross_mean(day_gini(Ret), 30)",
         "cs_rank(day_mean(Vwap))", "ts_decay_linear(day_close(Amt), 10)", "day_wmean(Amt, Volume)", "cross_ema(day_kurt(Amt), 20)"]


def _prod_store():
    from alphacube.store import open_cube_store
    return open_cube_store(STORE, mirror_root=MIRROR)


def task_prod_identity(out: Path, _args) -> None:
    """What a run keys its caches and its provenance on, for the real (segmented) store with no daily source."""
    st = _prod_store()
    dump(out / "identity.json", {"type": type(st).__name__, "contract_hash": st.contract_hash, "n_days": len(st.dates), "first": st.dates[0], "last": st.dates[-1],
                                 "n_symbols": len(st.symbols), "symbols_head": list(st.symbols[:5]), "fields": list(st.fields), "n_minutes": st.n_minutes})
    dump(out / "additive_surface.json", {"daily": repr(getattr(st, "daily", "<absent>"))})


def task_prod_eval(out: Path, args) -> None:
    """The batch's fifteen expressions and the known family on a real window, on $VERIFY_DEVICE; raw panels compared."""
    import numpy as np
    import yaml

    from alphacube.catalog import default_registry
    from alphacube.engine.engine import CubeEngine
    from alphacube.parser import parse
    from alphacube.research import warmed_view

    exprs = [f["expr"] for f in yaml.safe_load(Path(FACTORS).read_text(encoding="utf-8"))["factors"]] + KNOWN
    st = _prod_store()
    view, trim = warmed_view(st, args["start"], args["end"], warmup=60)
    reg = default_registry()
    parsed, meta = [], []
    for src in exprs:
        try:
            e = parse(src, reg, n_minutes=view.n_minutes)
        except Exception as exc:                      # noqa: BLE001
            meta.append({"src": src, "error": f"{type(exc).__name__}: {exc}"})
            continue
        meta.append({"src": src, "key": e.key(), "shape": repr(e.shape)})
        parsed.append(e)
    dump(out / "parse.json", meta)
    res = CubeEngine(view, device=DEVICE, workdir=os.environ["ALPHACUBE_WORKDIR"]).evaluate(parsed, tolerant=True)
    summary = []
    (out / "panels").mkdir(parents=True, exist_ok=True)
    for i, p in enumerate(res.panels):
        if p is None:
            summary.append({"i": i, "panel": None})
            continue
        a = np.ascontiguousarray(p[trim:])
        np.save(out / "panels" / f"{i:03d}.npy", a)
        summary.append({"i": i, "dtype": str(a.dtype), "shape": list(a.shape), "sha256": hashlib.sha256(a.tobytes()).hexdigest(), "n_nan": int(np.isnan(a).sum())})
    dump(out / "eval.json", {"view": [str(view.dates[0]), str(view.dates[-1]), int(view.n_symbols), int(trim)], "panels": summary, "errors": res.errors})


def task_prod_mine(out: Path, args) -> None:
    """One mining run through run_mining on a real half-year window, on $VERIFY_DEVICE."""
    import alphacube.pipeline as P

    st = _prod_store()
    miner = args["miner"]
    kw = dict(start=args["start"], end=args["end"], label="open_vwap15", miner=miner, budget=int(args["budget"]), seed=int(args["seed"]),
              pool_capacity=4, warmup=60, combine_methods=(), out_root=out / "runs", run_id="r", save_values=True, device=DEVICE,
              workdir=os.environ["ALPHACUBE_WORKDIR"])
    if miner == "gp":
        kw.update(dedup=0.99, checkpoint_every=1, cost_per_side=0.0015,
                  gp_params=dict(population_size=24, max_depth=3, fitness_kind=args["kind"], turnover_penalty=float(args.get("penalty", 0.0))))
    else:
        kw.update(max_expr_len=12, rl_params=json.loads(args.get("rl_params", "{}")))
    logs = []
    try:
        r = P.run_mining(st, log=logs.append, **kw)
    except Exception as exc:                          # noqa: BLE001
        _write_logs(out, logs)
        dump(out / "raised.json", {"type": type(exc).__name__, "msg": str(exc)})
        return
    _write_logs(out, logs)
    dump(out / "result.json", {"pool_size": r.pool_size, "added": r.added, "pool_metrics": r.pool_metrics, "members": r.members, "rejected": r.rejected, "summary": r.summary})


TASKS = {"prod_identity": task_prod_identity, "prod_eval": task_prod_eval, "prod_mine": task_prod_mine,
         "registry": task_registry, "evalexpr": task_evalexpr, "gp": task_gp, "rl": task_rl,
         "generator": task_generator}


def main(argv) -> int:
    task, outdir = argv[1], Path(argv[2])
    args = dict(kv.split("=", 1) for kv in argv[3:])
    outdir.mkdir(parents=True, exist_ok=True)
    import alphacube
    (outdir / "_tree.txt").write_text(str(Path(alphacube.__file__).resolve()), encoding="utf-8")
    TASKS[task](outdir, args)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
