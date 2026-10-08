"""bit-identical-defaults: is the steering branch, given no new argument, the
baseline byte for byte?

Runs every task twice -- once with the baseline tree's src on PYTHONPATH, once with
the steering worktree's -- in separate subprocesses, over ONE on-disk synthetic
cube, and compares the two output trees file by file.

A baseline-vs-baseline pass runs first (`--self-check`) as the control: without it a
difference cannot be told apart from ambient nondeterminism (thread counts, dict
order, a timestamp leaking into a file).

    verify.py build                 # write the shared cube
    verify.py self                  # control: baseline vs baseline
    verify.py cross                 # the claim: baseline vs steering
"""
from __future__ import annotations

import hashlib
import json
import os
import subprocess
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
# Server copy (scripts/server/ac_accept): the two trees, the interpreter, the device and the output root come from the
# environment, so the same comparison runs next to the production store on a GPU (see run.sh).
PY = Path(os.environ.get("VERIFY_PY", str(Path.home() / ".venvs" / "alphacube" / "bin" / "python")))
BASE = Path(os.environ.get("VERIFY_BASE", "/Users/wxy/Desktop/AlphaCube"))
NEW = Path(os.environ.get("VERIFY_NEW", "/Users/wxy/Desktop/AlphaCube-steering"))
ROOT = Path(os.environ.get("VERIFY_ROOT", str(HERE)))
CUBE = ROOT / "cube"
OUT = ROOT / "out"

# Files whose content is wall-clock by construction. They are not dropped: they are
# compared with those two keys stripped, and the stripping is reported.
TIMING_KEYS = ("seconds", "engine_seconds")

TASKS = (
    # (label, task, extra argv)
    *[(f"gp_{k}_seed{s}", "gp", [f"kind={k}", f"seed={s}",
                                 f"penalty={'0.14' if k == 'rank_ic' else '0.0'}"])
      for k in ("ic", "rank_ic", "long", "long_hit") for s in (0, 1)],
    ("rl_alphagen_seed0", "rl", ["miner=alphagen", "seed=0", "budget=64",
                                 'rl_params={"episodes_per_update": 8}']),
    ("rl_alphagen_seed1", "rl", ["miner=alphagen", "seed=1", "budget=64",
                                 'rl_params={"episodes_per_update": 8}']),
    ("rl_alphasage_seed0", "rl", ["miner=alphasage", "seed=0", "budget=32",
                                  'rl_params={"trajectories_per_update": 8}']),
    ("evalexpr", "evalexpr", []),
    ("generator", "generator", ["n_trees=400"]),
    ("registry", "registry", []),
)

# Paths that pass NO new parameter but do reach changed code through OLD parameters.
# These are where the design's "three deliberate behaviour changes" live, so this
# phase measures the scope of the admitted non-identity rather than asserting it away.
EXTRA_TASKS = (
    ("gp_rollingblock_seed0", "gp", ["kind=rank_ic", "seed=0", "penalty=0.14",
                                     "rolling_block=2", "ban_top_n=2"]),
    ("gp_rollingblock_seed7", "gp", ["kind=rank_ic", "seed=7", "penalty=0.14",
                                     "rolling_block=2", "ban_top_n=2"]),
    ("gp_banned_seed0", "gp", ["kind=ic", "seed=0",
                               'gp_extra={"banned_substructures": ["O:log(F:Amt)"]}']),
    ("rl_banned_seed0", "rl", ["miner=alphagen", "seed=0", "budget=64",
                               'rl_params={"episodes_per_update": 8}',
                               'gp_extra={"banned_substructures": ["O:log(F:Amt)"]}']),
    ("rl_banned_typo_seed0", "rl", ["miner=alphagen", "seed=0", "budget=64",
                                    'rl_params={"episodes_per_update": 8}',
                                    'gp_extra={"banned_substructures": ["O:log(F:NoSuchField)"]}']),
)


# Against the PRODUCTION store (read-only), on the device named by $VERIFY_DEVICE: store identity, the batch's fifteen
# expressions plus the known family on a real window, and one GP and one RL run through run_mining.
PROD_TASKS = (
    ("prod_identity", "prod_identity", []),
    ("prod_eval", "prod_eval", ["start=20250102", "end=20250331"]),
    ("prod_gp_rank_ic_seed0", "prod_mine", ["miner=gp", "seed=0", "budget=96", "kind=rank_ic", "penalty=0.14", "start=20240102", "end=20240628"]),
    ("prod_gp_long_seed1", "prod_mine", ["miner=gp", "seed=1", "budget=96", "kind=long", "penalty=0.0", "start=20240102", "end=20240628"]),
    ("prod_rl_alphagen_seed0", "prod_mine", ["miner=alphagen", "seed=0", "budget=64", "start=20240102", "end=20240628",
                                             'rl_params={"episodes_per_update": 8}']),
)


def run(tree: Path, task: str, outdir: Path, extra) -> dict:
    env = dict(os.environ)
    env["PYTHONPATH"] = str(tree / "src")
    env["PYTHONHASHSEED"] = "0"
    for k in ("OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS",
              "OPENBLAS_NUM_THREADS", "NUMEXPR_NUM_THREADS"):
        env[k] = "1"
    env.pop("ALPHACUBE_PLUGINS", None)                # the new branch steers off this
    env.pop("ALPHACUBE_DAILY_FIELDS", None)           # ... and attaches a daily store off this
    env.pop("ALPHACUBE_ROOT", None)
    env["ALPHACUBE_WORKDIR"] = str(ROOT / "work")     # never the engine's default <project>/tmp inside either tree
    (ROOT / "work").mkdir(parents=True, exist_ok=True)
    argv = [str(PY), str(HERE / "worker.py"), task, str(outdir), f"cube={CUBE}", *extra]
    t0 = time.time()
    p = subprocess.run(argv, env=env, cwd=str(HERE), capture_output=True, text=True)
    return {"rc": p.returncode, "secs": round(time.time() - t0, 1),
            "stdout": p.stdout[-4000:], "stderr": p.stderr[-6000:]}


def sha(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for blk in iter(lambda: fh.read(1 << 20), b""):
            h.update(blk)
    return h.hexdigest()


def listing(root: Path) -> dict:
    return {str(p.relative_to(root)): sha(p)
            for p in sorted(root.rglob("*")) if p.is_file()}


def strip_timing(raw: bytes) -> bytes:
    try:
        d = json.loads(raw.decode("utf-8"))
    except Exception:                                 # noqa: BLE001
        return raw
    if isinstance(d, dict):
        for k in TIMING_KEYS:
            d.pop(k, None)
    return json.dumps(d, sort_keys=True).encode("utf-8")


def compare(a_root: Path, b_root: Path) -> dict:
    la, lb = listing(a_root), listing(b_root)
    la.pop("_tree.txt", None)
    lb.pop("_tree.txt", None)
    only_a = sorted(set(la) - set(lb))
    only_b = sorted(set(lb) - set(la))
    differ, differ_after_timing_strip = [], []
    for rel in sorted(set(la) & set(lb)):
        if la[rel] == lb[rel]:
            continue
        differ.append(rel)
        ra = (a_root / rel).read_bytes()
        rb = (b_root / rel).read_bytes()
        if rel.endswith("meta.json") and strip_timing(ra) == strip_timing(rb):
            continue                                  # wall clock only
        if rel.endswith("log_raw.txt"):
            sa = (a_root / rel.replace("log_raw", "log_scrubbed"))
            sb = (b_root / rel.replace("log_raw", "log_scrubbed"))
            if sa.exists() and sb.exists() and sa.read_bytes() == sb.read_bytes():
                continue                              # wall clock only
        differ_after_timing_strip.append(rel)
    return {"n_files": len(la), "only_a": only_a, "only_b": only_b,
            "differ_raw": differ, "differ": differ_after_timing_strip,
            "identical": not (only_a or only_b or differ_after_timing_strip)}


def first_diff(a: Path, b: Path, rel: str, limit: int = 12) -> list:
    """Smallest reproduction material for one differing file."""
    pa, pb = a / rel, b / rel
    ra, rb = pa.read_bytes(), pb.read_bytes()
    if rel.endswith(".npy"):
        import numpy as np
        xa, xb = np.load(pa), np.load(pb)
        if xa.shape != xb.shape or xa.dtype != xb.dtype:
            return [f"shape/dtype {xa.shape}{xa.dtype} vs {xb.shape}{xb.dtype}"]
        bad = np.argwhere(~((xa == xb) | (np.isnan(xa) & np.isnan(xb))))
        out = [f"{int(bad.shape[0])} of {xa.size} cells differ"]
        for idx in bad[:limit]:
            t = tuple(int(v) for v in idx)
            out.append(f"  {t}: {xa[t]!r} vs {xb[t]!r}")
        return out
    ta = ra.decode("utf-8", "replace").splitlines()
    tb = rb.decode("utf-8", "replace").splitlines()
    out = [f"{len(ta)} vs {len(tb)} lines"]
    n = 0
    for i, (x, y) in enumerate(zip(ta, tb)):
        if x != y:
            out.append(f"  line {i + 1}:")
            out.append(f"    A: {x[:300]}")
            out.append(f"    B: {y[:300]}")
            n += 1
            if n >= limit:
                break
    if len(ta) != len(tb) and n == 0:
        out.append("  (common prefix identical; lengths differ)")
    return out


def phase(name: str, tree_a: Path, tree_b: Path, tasks=TASKS) -> int:
    root = OUT / name
    report = {}
    worst = 0
    for label, task, extra in tasks:
        a = root / "A" / label
        b = root / "B" / label
        ra = run(tree_a, task, a, extra)
        rb = run(tree_b, task, b, extra)
        rec = {"run_a": {k: ra[k] for k in ("rc", "secs")},
               "run_b": {k: rb[k] for k in ("rc", "secs")}}
        if ra["rc"] or rb["rc"]:
            rec["status"] = "ERROR"
            rec["stderr_a"] = ra["stderr"]
            rec["stderr_b"] = rb["stderr"]
            worst = 2
        else:
            cmp = compare(a, b)
            rec["status"] = "IDENTICAL" if cmp["identical"] else "DIFFERS"
            rec.update(cmp)
            if not cmp["identical"]:
                worst = max(worst, 1)
                rec["repro"] = {rel: first_diff(a, b, rel)
                                for rel in (cmp["differ"] or cmp["only_a"] or cmp["only_b"])[:4]
                                if (a / rel).exists() and (b / rel).exists()}
        report[label] = rec
        print(f"[{name}] {label:22s} {rec['status']:10s} "
              f"{rec.get('n_files', '?')} files  A={ra['secs']}s B={rb['secs']}s", flush=True)
        if rec["status"] == "ERROR":
            print(rec["stderr_a"][-2000:] or rec["stderr_b"][-2000:], flush=True)
        elif rec["status"] == "DIFFERS":
            for rel in rec["differ"][:6]:
                print(f"    differs: {rel}", flush=True)
            for rel, lines in (rec.get("repro") or {}).items():
                print(f"    --- {rel}", flush=True)
                for ln in lines[:14]:
                    print(f"      {ln}", flush=True)
    (OUT / f"report_{name}.json").write_text(json.dumps(report, ensure_ascii=False, indent=2),
                                             encoding="utf-8")
    return worst


def main(argv) -> int:
    what = argv[1] if len(argv) > 1 else "cross"
    OUT.mkdir(parents=True, exist_ok=True)
    if what == "build":
        env = dict(os.environ, PYTHONPATH=str(BASE / "src"))
        p = subprocess.run([str(PY), str(HERE / "build_cube.py"), str(CUBE)],
                           env=env, cwd=str(HERE), text=True)
        return p.returncode
    if what == "self":
        return phase("self", BASE, BASE)
    if what == "cross":
        return phase("cross", BASE, NEW)
    if what == "extra_self":
        return phase("extra_self", BASE, BASE, EXTRA_TASKS)
    if what == "extra":
        return phase("extra", BASE, NEW, EXTRA_TASKS)
    if what == "prod_self":
        return phase("prod_self", BASE, BASE, PROD_TASKS)
    if what == "prod":
        return phase("prod", BASE, NEW, PROD_TASKS)
    raise SystemExit(f"unknown phase {what!r}")


if __name__ == "__main__":
    sys.exit(main(sys.argv))
