"""C05: deterministic admissibility checks for a Partura plan (research/coldstart_C05/PLAN.md §2.5-2.6).  Local.

    python scripts/c05_check.py <seed> <round>
        reads research/coldstart_C05/partura/s<seed>/r<round>/missions.yaml (and loc.json, the locate output it was written from)
        exit 0 = admissible, 1 = not (the issues are printed)

Two GP slots, each E or N.  E: a core that parses, is a daily-valued tree reading a field, is a subtree of a snapshot head (the whole head
included) or one of the locate output's subtrees, and has had < 2 E slots before; <= 16 seeds, each carrying the core verbatim.  N: a hypothesis and
1-16 seeds.  R: <= 16 variants in all, of heads in the snapshot.  Round 3: at least one N slot over rounds 1-3.  No seed uses an
operator the environment bans (ts_spearman, nt_*).  Every literature source has a year, before 2023-08-08.
"""
import os
import re
import sys
import warnings
from pathlib import Path

warnings.filterwarnings("ignore")
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT))
os.environ.setdefault("ALPHACUBE_ROOT", str(Path.home() / "Desktop" / "AlphaCube-steering"))
sys.path.insert(0, str(Path(os.environ["ALPHACUBE_ROOT"]) / "src"))
import json  # noqa: E402

import yaml  # noqa: E402

from partura import ops_ext  # noqa: E402,F401
from partura.steer import Guidance  # noqa: E402
from alphacube.expression import is_valid_root  # noqa: E402
from alphacube.parser import parse  # noqa: E402
from alphacube.plugins import load_plugins  # noqa: E402

load_plugins(["partura.ac_plugin"])
S, K = int(sys.argv[1]), int(sys.argv[2])
P = ROOT / "research" / "coldstart_C05" / "partura" / f"s{S}"
BANNED = re.compile(r"\b(ts_spearman|nt_[A-Za-z0-9_]+)\s*\(")
G0 = Guidance.load(ROOT / "guidance" / "C05_base.yaml")
issues = []


def tree(expr):
    try:
        return parse(G0.canonical(expr), strict=True, coerce_daily=True, n_minutes=241, allow_general=True), ""
    except Exception as exc:                                   # noqa: BLE001
        return None, f"{type(exc).__name__}: {str(exc)[:90]}"


def expr_ok(e, where):
    t, err = tree(e)
    if t is None:
        issues.append(f"{where}: does not parse ({err}): {e[:100]}")
    elif not is_valid_root(t):
        issues.append(f"{where}: not a daily-valued tree reading a field: {e[:100]}")
    elif BANNED.search(e):
        issues.append(f"{where}: uses an operator the environment bans (ts_spearman / nt_*): {e[:100]}")
    return t


f = P / f"r{K}" / "missions.yaml"
try:
    spec = yaml.safe_load(f.read_text(encoding="utf-8")) or {}
    loc = json.loads((P / f"r{K}" / "loc.json").read_text(encoding="utf-8"))
except Exception as exc:                                       # noqa: BLE001
    print(f"NOT ADMISSIBLE\n- does not load: {exc}")
    sys.exit(1)
if spec.get("seed") != S or spec.get("round") != K:
    issues.append(f"seed / round must be {S} / {K}")
slots = spec.get("slots") or []
if len(slots) != 2:
    issues.append(f"exactly 2 GP slots; got {len(slots)}")
known = set()                                                  # every subtree key the snapshot offers as a core
for h in loc["heads"]:
    t, _ = tree(h["expr"])
    if t is not None:
        known |= {n.key() for n in t.nodes()}                 # a whole head counts too (PLAN revision 3)
for e in [x["subtree"] for x in loc["enrichment"]] + [c["core"] for c in loc["core_cards"]]:
    t, _ = tree(e)
    if t is not None:
        known.add(t.key())
used = {}
n_before = 0
for k in range(1, K):
    prev = yaml.safe_load((P / f"r{k}" / "missions.yaml").read_text(encoding="utf-8")) or {}
    for s in prev.get("slots", []):
        n_before += s.get("type") == "N"
        if s.get("type") == "E":
            used[s["core"]] = used.get(s["core"], 0) + 1
for i, s in enumerate(slots):
    w = f"slot {i + 1}"
    if s.get("type") not in ("E", "N"):
        issues.append(f"{w}: type must be E or N")
        continue
    if not str(s.get("hypothesis", "")).strip():
        issues.append(f"{w}: no hypothesis")
    seeds = s.get("seeds") or []
    if len(seeds) > 16:
        issues.append(f"{w}: {len(seeds)} seeds (at most 16)")
    if s["type"] == "E":
        ct = expr_ok(str(s.get("core", "")), f"{w} core")
        if ct is not None:
            if ct.key() not in known:
                issues.append(f"{w}: the core is not a subtree of a snapshot head nor a locate subtree")
            if used.get(s["core"], 0) >= 2:
                issues.append(f"{w}: this core already had 2 E slots")
            used[s["core"]] = used.get(s["core"], 0) + 1
            for j, e in enumerate(seeds):
                t = expr_ok(e, f"{w} seed {j + 1}")
                if t is not None and not any(n.key() == ct.key() for n in t.nodes()):
                    issues.append(f"{w} seed {j + 1}: does not carry the core verbatim: {e[:100]}")
    else:
        if not seeds:
            issues.append(f"{w}: an N slot needs seeds")
        for j, e in enumerate(seeds):
            expr_ok(e, f"{w} seed {j + 1}")
    for j, src in enumerate(s.get("literature") or []):
        y = str(src.get("year", ""))
        if not re.fullmatch(r"\d{4}(-\d{2})?", y):
            issues.append(f"{w} literature {j + 1}: no year (YYYY or YYYY-MM)")
        elif y[:4] > "2023" or (y[:4] == "2023" and (len(y) == 4 or y[5:7] > "07")):
            issues.append(f"{w} literature {j + 1}: {y} is not before 2023-08-08")
if K == 3 and n_before + sum(s.get("type") == "N" for s in slots) == 0:
    issues.append("round 3: at least one N slot over rounds 1-3 (PLAN §2.5)")
heads = {h["expr"] for h in loc["heads"]}
nv = 0
for i, r in enumerate(spec.get("R") or []):
    if r.get("head") not in heads:
        issues.append(f"R {i + 1}: the head is not in the snapshot")
    for j, e in enumerate(r.get("variants") or []):
        nv += 1
        expr_ok(e, f"R {i + 1} variant {j + 1}")
if nv > 16:
    issues.append(f"R: {nv} variants (at most 16)")
print("ADMISSIBLE" if not issues else "NOT ADMISSIBLE\n" + "\n".join(f"- {x}" for x in issues))
sys.exit(1 if issues else 0)
