r"""Does a fresh idea-search run reproduce a stored one?  Compares two ``evidence.json`` files arm by arm.

WHY.  ``scripts/idea_search.py`` reaches AlphaCube through the plugin route (``partura/ac_plugin.py``:
``load_plugins`` + ``SearchHooks`` + a registered scorer); the stored episodes were produced by the monkeypatching
version that ``main`` had before.  The two are meant to propose, accept and score the same candidates in the same
order from the same seed -- the search is deterministic (episode e5's re-runs agreed to the last bit), so a fresh run
under a new tag either reproduces the stored one exactly or it does not.  This script says which, and where it first
does not.  It needs no GPU and no store: it only reads the two JSON files.

HOW TO PRODUCE THE FRESH RUNS  (server; ``./scripts/study.sh code`` first).  The two stored runs are
episodes/e7c1_I5_within_bucket_anything (the control arm) and episodes/e7b1_I5_within_bucket_anything (the steer arm with
only the guidance's priors); both seed 1, budget 192, population 48 (episodes/e7_PLAN.md).  The control arm has a second
stored copy, episodes/acc7c1_I5_within_bucket_anything: the same run replayed with the OLD (monkeypatching) script on the
new engine, candidate-for-candidate equal to e7c1 (handoff/ac_accept/ACCEPTANCE.md) -- so a difference against e7c1 that is
absent against acc7c1 is not the engine's.

The merged script imports ``alphacube.plugins``, so it needs the steering AlphaCube.  It is deployed beside the old one,
at /root/autodl-tmp/Partura/vendor/AlphaCube-steering (``python -c "import alphacube.plugins"`` with that PYTHONPATH must
work).  ``scripts/server/run_idea_seeds.sh`` exports ``ALPHACUBE_ROOT=/root/autodl-tmp/AlphaCube`` unconditionally, i.e. the
OLD engine, so until that directory is replaced use the launcher's own environment with the vendored root.  Under new tags
``e7cx1`` / ``e7bx1`` (the tag of the launcher is <prefix><seed>):

    cd /root/autodl-tmp/Partura
    export ALPHACUBE_ROOT=/root/autodl-tmp/Partura/vendor/AlphaCube-steering
    export PYTHONPATH=$ALPHACUBE_ROOT/src:/root/autodl-tmp/Partura OMP_NUM_THREADS=8 MKL_NUM_THREADS=8 PARTURA_RANK_DEVICE=cuda \
           PARTURA_REWARD_DEVICE=cuda PYTORCH_CUDA_ALLOC_CONF=expandable_segments:True PARTURA_SLOTS=4 PARTURA_GPU_WAYS=2 PARTURA_MEM_WAIT_S=10800
    PY=/root/miniconda3/envs/quant/bin/python
    $PY -u scripts/idea_search.py I5_within_bucket_anything --tag e7cx1 --seed 1 --reward long --arms control --budget 192 --population 48
    $PY -u scripts/idea_search.py I5_within_bucket_anything --tag e7bx1 --seed 1 --reward long --parts priors --arms steer --budget 192 --population 48

(``PARTURA_REWARD_DEVICE=cuda`` is what the stored evidence recorded.)  Once /root/autodl-tmp/AlphaCube is the steering
engine, the launcher form does the same thing:

    screen -dmS accc scripts/server/run_idea_seeds.sh I5_within_bucket_anything e7cx "1" --reward long --arms control --budget 192 --population 48
    screen -dmS accb scripts/server/run_idea_seeds.sh I5_within_bucket_anything e7bx "1" --reward long --parts priors --arms steer --budget 192 --population 48

Then, locally after ``./scripts/study.sh idea-pull`` (or on the server):

    python scripts/plugin_acceptance.py episodes/e7cx1_I5_within_bucket_anything episodes/e7c1_I5_within_bucket_anything
    python scripts/plugin_acceptance.py episodes/e7cx1_I5_within_bucket_anything episodes/acc7c1_I5_within_bucket_anything
    python scripts/plugin_acceptance.py episodes/e7bx1_I5_within_bucket_anything episodes/e7b1_I5_within_bucket_anything

Each prints ``identical`` or the first difference per arm, and exits 0 / 1.  Leave ``PARTURA_AC_FIXES`` unset for
these runs: the two opt-in plugin changes (``in_sustain``, ``nt_twins``) move the draws on purpose.  (If the steered
comparison differs and the control one does not, replay e7b1 with the OLD script on the same vendored engine -- main's
``scripts/idea_search.py`` at commit 31765f1 -- to see whether it is the route or the engine.)

THINGS THAT WILL LOOK LIKE A DIFFERENCE AND ARE NOT THE PLUGIN'S
  * the ``code`` fingerprints of ``scripts/idea_search.py`` / ``partura/ops_ext.py`` differ by construction (and the
    fresh one lists ``partura/ac_plugin.py``); ``steer.py``, ``steer_fast.py``, ``books.py`` must agree -- they are
    printed, and a mismatch there means the reward differs from the stored run's, not the route.
  * ``guidance/B01.yaml`` has been edited since the e7 runs (stored fingerprint 6665faac5bcd = the file at commit
    4109d49; later commits added ``evaluation`` entries E11-E13 and ``why`` notes on D7 / D12).  The rules, pool and ideas
    are identical (``Guidance`` rules, ``operator_weights()`` and ``family_weight`` compared), so the same sampling is
    expected; for a fingerprint-exact run: ``git show 4109d49:guidance/B01.yaml > guidance/B01_e7.yaml`` and add
    ``--guidance guidance/B01_e7.yaml`` to both commands (the guidance fingerprint is compared, not its file name).
  * timings (``seconds``, ``scoring_seconds``) are never compared.
  * on another GPU or driver the float sums inside a Sharpe may differ in the last digit: ``--rtol 1e-9`` reports such a
    pair as "identical within rtol" instead of as a difference; the default is exact.
"""
import argparse
import json
import math
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# what defines the run (a difference here means the two runs are not the same experiment)
HEADER_KEYS = ("reward", "threshold", "screen_base", "score_scale", "budget", "population", "seed", "boost", "period",
               "parts", "halflives")
# per arm, scalar fields in the order they are compared
ARM_SCALARS = ("error", "checkpoints", "scored", "gate_fail", "archive", "live", "passers")
# per arm, after the candidates
ARM_TAIL = ("independent_distinct", "efficiency_per_100")
NEVER_COMPARED = ("seconds", "scoring_seconds")


def load(arg):
    p = Path(arg)
    if not p.exists() and (ROOT / "episodes" / arg).exists():
        p = ROOT / "episodes" / arg
    if p.is_dir():
        p = p / "evidence.json"
    return p, json.loads(p.read_text(encoding="utf-8"))


def same(a, b, rtol=0.0):
    """(equal, how): exact (NaN equals NaN), or within rtol.  how is "exact" / "rtol"."""
    if isinstance(a, float) and isinstance(b, float):
        if math.isnan(a) and math.isnan(b):
            return True, "exact"
        if a == b:
            return True, "exact"
        if rtol and math.isfinite(a) and math.isfinite(b) and abs(a - b) <= rtol * max(abs(a), abs(b)):
            return True, "rtol"
        return False, ""
    if isinstance(a, (int, float)) and isinstance(b, (int, float)) and not isinstance(a, bool) and not isinstance(b, bool):
        return same(float(a), float(b), rtol)
    if isinstance(a, list) and isinstance(b, list):
        if len(a) != len(b):
            return False, ""
        how = "exact"
        for x, y in zip(a, b):
            ok, h = same(x, y, rtol)
            if not ok:
                return False, ""
            how = "rtol" if h == "rtol" else how
        return True, how
    return (a == b), "exact"


def guidance_fingerprint(code):
    """The fingerprint of whichever ``guidance/...`` file the run used (its file name may differ between runs)."""
    for k, v in (code or {}).items():
        if k.startswith("guidance/"):
            return v
    return None


def compare_header(fresh, stored):
    """[(key, fresh, stored)] of the run-defining keys that differ; keys recorded by only one side are skipped
    (older evidence lacks ``screen_base`` / ``score_scale``)."""
    out = []
    for k in HEADER_KEYS:
        if k in fresh and k in stored and not same(fresh[k], stored[k])[0]:
            out.append((k, fresh[k], stored[k]))
    fi, si = fresh.get("idea", {}).get("id"), stored.get("idea", {}).get("id")
    if fi != si:
        out.append(("idea.id", fi, si))
    return out


def compare_arm(fresh, stored, rtol=0.0):
    """None if the two arms are identical, else a one-line description of the FIRST difference.  Second value:
    "exact" or "rtol" (how the identical arms matched)."""
    how = "exact"

    def note(h):
        nonlocal how
        if h == "rtol":
            how = "rtol"

    for k in ARM_SCALARS:
        if k in fresh and k in stored:
            ok, h = same(fresh[k], stored[k], rtol)
            if not ok:
                return f"{k}: fresh {fresh[k]!r} vs stored {stored[k]!r}", how
            note(h)
    fs, ss = fresh.get("sampling", {}), stored.get("sampling", {})
    for k in sorted(set(fs) | set(ss)):
        if fs.get(k, 0) != ss.get(k, 0):
            return f"sampling[{k!r}]: fresh {fs.get(k, 0)} vs stored {ss.get(k, 0)}  (fresh {fs}; stored {ss})", how
    fc, sc = fresh.get("candidates", []), stored.get("candidates", [])
    if len(fc) != len(sc):
        return f"candidates: fresh lists {len(fc)}, stored {len(sc)}", how
    for i, (a, b) in enumerate(zip(fc, sc)):
        if a.get("expr") != b.get("expr"):
            n_same = sum(1 for x, y in zip(fc, sc) if x.get("expr") == y.get("expr"))
            return (f"candidate #{i}: expression fresh {a.get('expr')!r} vs stored {b.get('expr')!r} "
                    f"({n_same} of {len(fc)} ranks hold the same expression)"), how
        for key in sorted(set(a) | set(b)):
            if key == "expr":
                continue
            ok, h = same(a.get(key), b.get(key), rtol)
            if not ok:
                return f"candidate #{i} ({a.get('expr')[:70]}): {key} fresh {a.get(key)!r} vs stored {b.get(key)!r}", how
            note(h)
    for k in ARM_TAIL:
        if k in fresh and k in stored:
            ok, h = same(fresh[k], stored[k], rtol)
            if not ok:
                return f"{k}: fresh {fresh[k]!r} vs stored {stored[k]!r}", how
            note(h)
    fh, sh = fresh.get("heads", []), stored.get("heads", [])
    if len(fh) != len(sh):
        return f"heads: fresh lists {len(fh)}, stored {len(sh)}", how
    for i, (a, b) in enumerate(zip(fh, sh)):
        if a.get("expr") != b.get("expr"):
            return f"head #{i}: expression fresh {a.get('expr')!r} vs stored {b.get('expr')!r}", how
        for key in sorted(set(a) | set(b)):
            ok, h = same(a.get(key), b.get(key), rtol)
            if not ok:
                return f"head #{i}: {key} fresh {a.get(key)!r} vs stored {b.get(key)!r}", how
            note(h)
    return None, how


def compare(fresh, stored, rtol=0.0):
    """-> (report lines, ok).  ok means: same experiment, at least one arm in common, every common arm identical."""
    lines, ok = [], True
    diffs = compare_header(fresh, stored)
    for k, a, b in diffs:
        lines.append(f"NOT THE SAME EXPERIMENT -- {k}: fresh {a!r} vs stored {b!r}")
        ok = False
    fg, sg = guidance_fingerprint(fresh.get("code")), guidance_fingerprint(stored.get("code"))
    if fg and sg and fg != sg:
        lines.append(f"note: guidance fingerprint fresh {fg} vs stored {sg} (see the header of this script)")
    fixes = fresh.get("plugin_fixes") or []
    if fixes:
        lines.append(f"NOT THE SAME EXPERIMENT -- the fresh run had opt-in plugin fixes on: {fixes}")
        ok = False
    for f in ("partura/steer.py", "partura/steer_fast.py", "partura/books.py"):
        a, b = (fresh.get("code") or {}).get(f), (stored.get("code") or {}).get(f)
        if a and b and a != b:
            lines.append(f"note: {f} differs (fresh {a}, stored {b}) -- the reward code is not the stored run's")
    common = [a for a in fresh.get("arms", {}) if a in stored.get("arms", {})]
    for a in fresh.get("arms", {}):
        if a not in stored.get("arms", {}):
            lines.append(f"arm {a}: only in the fresh evidence (not compared)")
    for a in stored.get("arms", {}):
        if a not in fresh.get("arms", {}):
            lines.append(f"arm {a}: only in the stored evidence (not compared)")
    if not common:
        lines.append("no arm in common: nothing to compare")
        return lines, False
    for a in common:
        diff, how = compare_arm(fresh["arms"][a], stored["arms"][a], rtol)
        A = fresh["arms"][a]
        if diff is None:
            tail = "" if how == "exact" else f" (within rtol {rtol:g})"
            lines.append(f"arm {a}: identical{tail} -- {len(A.get('candidates', []))} candidates, scored {A.get('scored')}, "
                         f"gate_fail {A.get('gate_fail')}, sampling {A.get('sampling')}")
        else:
            ok = False
            lines.append(f"arm {a}: DIFFERENT -- first difference: {diff}")
    return lines, ok


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("fresh", help="the fresh run: an evidence.json, or an episode directory (or its name under episodes/)")
    ap.add_argument("stored", help="the stored run, same forms")
    ap.add_argument("--rtol", type=float, default=0.0, help="relative tolerance for floats (default 0: exact)")
    a = ap.parse_args(argv)
    (pf, fresh), (ps, stored) = load(a.fresh), load(a.stored)
    print(f"fresh : {pf}\nstored: {ps}")
    fc, sc = fresh.get("code") or {}, stored.get("code") or {}
    for f in sorted(set(fc) | set(sc)):
        if f.startswith("guidance/"):
            continue
        print(f"  code {f:28s} fresh {fc.get(f, '-'):13s} stored {sc.get(f, '-'):13s}{'' if fc.get(f) == sc.get(f) else '  (differs)'}")
    print(f"  plugin fixes in the fresh run: {fresh.get('plugin_fixes') or 'none'};  reward device fresh {fresh.get('reward_device')!r} vs stored {stored.get('reward_device')!r}")
    lines, ok = compare(fresh, stored, a.rtol)
    print("\n".join(lines))
    print("identical" if ok else "NOT identical")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
