"""AlphaCube's two-level champion method (ridge inside a family, least squares across families) on other factor pools.

Server.  AlphaCube's own scripts do the scoring, the family selection and the fitting, UNMODIFIED
(``scripts/score_all_factors.py``, ``scripts/build_champion.py``): this driver only assembles pool directories in the
layout they expect (``manifest.csv``, ``panels/00000.npy`` ..., then ``metrics.csv`` from the scorer) and calls them.
Nothing is written into the AlphaCube tree; pools live in <Partura>/pools/.

    two_level.py export <pool> <candidates.json> [--key all_s4,picked] [--dry]
        a pool of Partura expressions: panels come from Partura's panel cache on the production view
        (2018-01-02 ~ 2025-12-31; computed if missing), hard-linked as panels/<i>.npy
    two_level.py score <pool>
        AlphaCube's scorer with the buyable label (metrics.csv: training-period rank IC, turnover_train, health ...)
    two_level.py merge <pool> <source dir> [<source dir> ...]
        the union of scored pools (AlphaCube's or ours): panels hard-linked under new indices, metrics rows carried
        over, exact duplicate expressions kept once (first source wins)
    two_level.py build <pool> <out name> [--compare name=path ...]
        build_champion.py --buyable on the pool -> pools/signals/<out name>.npy (+ its report in logs/)

Everything that selects or fits reads the training period only (AlphaCube's rule: fitness = |train rank IC| - 0.14 x
train turnover; families by |rank corr| 0.7 on training fingerprints; top 100 families, <= 60 members; weights on
the first 70% of days = to 2023-08-07).
"""
import csv
import json
import os
import subprocess
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.bridge import PARTURA_ROOT  # noqa: E402

AC = Path("/root/autodl-tmp/AlphaCube")
PY = "/root/miniconda3/envs/quant/bin/python"
POOLS = PARTURA_ROOT / "pools"
argv = sys.argv[1:]
cmd = argv[0]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


def ac_run(args, log):
    env = dict(os.environ, PYTHONPATH=str(AC / "src"), OMP_NUM_THREADS="8", MKL_NUM_THREADS="8")
    with open(log, "a", encoding="utf-8") as fh:
        fh.write(f"\n$ {' '.join(map(str, args))}\n")
        fh.flush()
        return subprocess.run([PY, "-u", *map(str, args)], cwd=str(AC), env=env, stdout=fh, stderr=subprocess.STDOUT).returncode


if cmd == "export":
    from partura.guard import MemoryGuard, limit_threads, slot
    limit_threads(8)
    import numpy as np
    from partura import ops_ext  # noqa: F401
    from partura.panels import SHARED_CACHE, PanelSet, parse_research

    pool, src = POOLS / argv[1], PARTURA_ROOT / argv[2]
    keys = (opt("--key") or "all_s4,picked").split(",")
    J = json.loads(src.read_text(encoding="utf-8"))
    items, seen = [], set()
    for k in keys:
        for fid, cid, kind, expr in J[k]:
            e = expr.replace(" ", "")
            if e not in seen:
                seen.add(e)
                items.append((fid, cid, kind, expr))
    (pool / "panels").mkdir(parents=True, exist_ok=True)
    with slot():
        mem = MemoryGuard(self_limit_gb=30, cgroup_limit_gb=70).start()
        ps = PanelSet("/root/autodl-tmp/qmt_daily_data/fast_factor_compute", "20180102", "20251231", warmup=60, device="cuda", gpu_fraction=0,
                      cache_dir=str(SHARED_CACHE), mirror_root="/root/autodl-tmp/AlphaCube/mirror", workdir=str(PARTURA_ROOT / "tmp"),
                      label_kind="open_vwap15", label_buyable=True, batch=32)
        have, miss, bad = [], [], []
        for n, (fid, cid, kind, expr) in enumerate(items):
            try:
                key = parse_research(expr, n_minutes=ps.store.n_minutes).key()
            except Exception as exc:                          # noqa: BLE001
                bad.append((fid, cid, f"{type(exc).__name__}: {str(exc)[:80]}"))
                continue
            p = ps._cache_path(key)
            (have if p is not None and p.is_file() else miss).append((fid, cid, kind, expr, p))
        print(f"[export] {len(items)} expressions: {len(have)} cached, {len(miss)} to compute, {len(bad)} do not parse", flush=True)
        if "--dry" in argv:
            mem.stop()
            raise SystemExit(0)
        for a in range(0, len(miss), 64):                     # compute the missing ones (the panel store caches them)
            chunk = miss[a:a + 64]
            ps.compute({f"x{a + j}": m[3] for j, m in enumerate(chunk)})
            ps._mem.clear()
            print(f"[export] computed {min(a + 64, len(miss))}/{len(miss)}", flush=True)
        rows = []
        for fid, cid, kind, expr, p in have + miss:
            if p is None or not p.is_file():
                bad.append((fid, cid, "no panel"))
                continue
            i = len(rows)
            dst = pool / "panels" / f"{i:05d}.npy"
            if dst.exists():
                dst.unlink()
            os.link(p, dst)
            rows.append({"i": i, "run": f"partura:{fid}", "expression": expr, "name": f"{fid}.{cid}", "kind": kind})
        with open(pool / "manifest.csv", "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=["i", "run", "expression", "name", "kind"])
            w.writeheader()
            w.writerows(rows)
        (pool / "export.json").write_text(json.dumps({"n": len(rows), "failed": bad, "source": str(src), "keys": keys}, ensure_ascii=False, indent=1), encoding="utf-8")
        print(f"[export] {pool}: {len(rows)} panels linked; {len(bad)} failed", flush=True)
        mem.stop()

elif cmd == "score":
    pool = POOLS / argv[1]
    rc = ac_run(["scripts/score_all_factors.py", pool, "--buyable", "--workers", "8"], PARTURA_ROOT / "logs" / f"_pool_{argv[1]}.log")
    print(f"[score] {pool}: exit {rc}")
    raise SystemExit(rc)

elif cmd == "merge":
    pool = POOLS / argv[1]
    sources = [Path(a) if a.startswith("/") else POOLS / a for a in argv[2:] if not a.startswith("-")]
    (pool / "panels").mkdir(parents=True, exist_ok=True)
    rows, seen, fields = [], set(), []
    stat = {}
    for s in sources:
        R = list(csv.DictReader(open(s / "metrics.csv", encoding="utf-8")))
        kept = 0
        for r in R:
            e = (r.get("expression") or "").replace(" ", "")
            src_panel = s / "panels" / f"{int(r['i']):05d}.npy"
            if not e or e in seen or not src_panel.exists():
                continue
            seen.add(e)
            i = len(rows)
            dst = pool / "panels" / f"{i:05d}.npy"
            if dst.exists() or dst.is_symlink():
                dst.unlink()
            try:
                os.link(os.path.realpath(src_panel), dst)
            except OSError:
                os.symlink(os.path.realpath(src_panel), dst)
            r = dict(r, i=i, source=s.name, source_i=r["i"])
            rows.append(r)
            kept += 1
            for k in r:
                if k not in fields:
                    fields.append(k)
        stat[s.name] = {"rows": len(R), "kept": kept}
    for nm in ("_target.npy", "_target_ranks.npy", "dates.npy"):
        if (sources[0] / nm).exists() and not (pool / nm).exists():
            os.link(os.path.realpath(sources[0] / nm), pool / nm)
    for name, flds in (("metrics.csv", fields), ("manifest.csv", ["i", "run", "expression", "source", "source_i"])):
        with open(pool / name, "w", newline="", encoding="utf-8") as fh:
            w = csv.DictWriter(fh, fieldnames=flds, extrasaction="ignore")
            w.writeheader()
            w.writerows(rows)
    (pool / "merge.json").write_text(json.dumps({"sources": [str(s) for s in sources], "stat": stat, "n": len(rows)}, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"[merge] {pool}: {len(rows)} factors from {stat}")

elif cmd == "build":
    pool, name = POOLS / argv[1], argv[2]
    (POOLS / "signals").mkdir(parents=True, exist_ok=True)
    out = POOLS / "signals" / f"{name}.npy"
    comp = []
    for i, a in enumerate(argv):
        if a == "--compare":
            comp += ["--compare", argv[i + 1]]
    t0 = time.time()
    rc = ac_run(["scripts/build_champion.py", "--dir", pool, "--buyable", "--out", out, *comp], PARTURA_ROOT / "logs" / f"_pool_{argv[1]}.log")
    print(f"[build] {out}: exit {rc} ({time.time() - t0:.0f}s)")
    raise SystemExit(rc)
else:
    raise SystemExit(__doc__)
