"""C01: is a guidance file Partura wrote admissible under research/coldstart_C01/PLAN.md §2.5 / §2.6?  Deterministic.

Local.  Checks: it loads; pool is C00's, unchanged; reward / evaluation lists are empty; at most two ideas, each with
reward long, a thesis (mechanism / counterparty / prediction / fails_if), seeds that parse in the search grammar and
grammar operators that exist in the search vocabulary; every prior has a known action, a pattern that compiles, a
weight, a why and evidence; no evidence cites a file the cold start forbids.  Also prints what the priors would have
done to the candidates already seen (the B arm's digest) -- a diagnostic, not a gate.

    python scripts/c01_check_guidance.py guidance/C01_r<k>.yaml [--digest research/coldstart_C01/digest_r<k>.json]
    exit 0 = admissible, 1 = not (the issues are printed)
"""
import json
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
import yaml  # noqa: E402

from partura import ops_ext  # noqa: E402,F401
from partura.steer import Guidance, Pattern  # noqa: E402

path = Path(sys.argv[1])
dig = sys.argv[sys.argv.index("--digest") + 1] if "--digest" in sys.argv else None
issues, notes = [], []
FORBIDDEN = re.compile(r"(lab/|findings\.yaml|guidance/(?!C00_base|C01_)|episodes/(?!c01)|research/(?!coldstart_C01)|notes/|studies/|handoff/|runs/|batches/|\bB01\b|GP01|\be[1-7][a-z]*\d*_I\d)")
THESIS = ("mechanism", "counterparty", "prediction", "fails_if")

try:
    spec = yaml.safe_load(path.read_text(encoding="utf-8"))
    G = Guidance(spec)
except Exception as exc:                                     # noqa: BLE001
    print(f"NOT ADMISSIBLE\n- does not load: {type(exc).__name__}: {exc}")
    sys.exit(1)
base = yaml.safe_load((ROOT / "guidance" / "C00_base.yaml").read_text(encoding="utf-8"))
if spec.get("pool") != base["pool"]:
    issues.append("pool differs from guidance/C00_base.yaml (it is an environment constant)")
for k in ("reward", "evaluation"):
    if spec.get(k):
        issues.append(f"'{k}' must be empty in C01 (only priors and ideas may change)")

from alphacube.catalog import default_registry  # noqa: E402
from alphacube.parser import parse  # noqa: E402
from alphacube.plugins import load_plugins  # noqa: E402

load_plugins(["partura.ac_plugin"])
reg = default_registry()
searchable = {s.name for s in reg.searchable(include_boolean=False, include_resource_risk=True)}

ideas = spec.get("ideas") or []
if not 1 <= len(ideas) <= 2:
    issues.append(f"{len(ideas)} ideas: C01 takes one or two (use I0_open_search for 'priors only')")
ids = [i.get("id") for i in ideas]
if len(set(ids)) != len(ids):
    issues.append("idea ids are not unique")
for i in ideas:
    tag = i.get("id", "?")
    if i.get("reward") != "long":
        issues.append(f"{tag}: reward must be long (got {i.get('reward')!r})")
    if tag != "I0_open_search":
        th = i.get("thesis") or {}
        miss = [k for k in THESIS if not str(th.get(k, "")).strip()]
        if miss:
            issues.append(f"{tag}: thesis lacks {miss}")
        if not str(i.get("hypothesis", "")).strip():
            issues.append(f"{tag}: no hypothesis")
    for s in i.get("seeds") or []:
        try:
            parse(G.canonical(s), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
        except Exception as exc:                             # noqa: BLE001
            issues.append(f"{tag}: seed does not parse in the search grammar: {s} ({type(exc).__name__}: {str(exc)[:80]})")
    gram = i.get("grammar") or {}
    bad_keys = set(gram) - {"day_ops", "memory_ops", "leaves", "windows", "convex", "fold", "inner", "ops"}
    if bad_keys:
        issues.append(f"{tag}: unknown grammar keys {sorted(bad_keys)}")
    for key in ("day_ops", "memory_ops", "convex", "fold", "inner", "ops"):
        for x in gram.get(key, []) or []:
            for nm in re.findall(r"[A-Za-z_][A-Za-z_0-9]*(?=\()", x) or [x]:
                if nm not in searchable:
                    issues.append(f"{tag}: grammar.{key} names {nm}, not in the search vocabulary")
    for x in gram.get("leaves", []) or []:
        if x not in ("Open", "High", "Low", "Close", "Vwap", "Volume", "Amt", "Ret"):
            issues.append(f"{tag}: unknown leaf {x}")
    if FORBIDDEN.search(json.dumps(i, ensure_ascii=False)):
        issues.append(f"{tag}: cites a file the cold start forbids")

for r in spec.get("priors") or []:
    rid = r.get("id", "?")
    if r.get("action") not in ("ban", "weight", "rewrite", "family"):
        issues.append(f"{rid}: action {r.get('action')!r}")
    try:
        Pattern.compile(str(r.get("pattern", "")))
    except Exception as exc:                                 # noqa: BLE001
        issues.append(f"{rid}: pattern does not compile ({exc})")
    if r.get("action") == "weight" and not (isinstance(r.get("w"), (int, float)) and r["w"] > 0):
        issues.append(f"{rid}: a weight rule needs w > 0 (a ban is action: ban)")
    if not str(r.get("why", "")).strip():
        issues.append(f"{rid}: no why")
    if not r.get("evidence"):
        issues.append(f"{rid}: no evidence")
    if FORBIDDEN.search(json.dumps(r, ensure_ascii=False)):
        issues.append(f"{rid}: cites a file the cold start forbids")

if dig and Path(dig).is_file():
    D = json.loads(Path(dig).read_text(encoding="utf-8"))
    seen = D["passers_top"] + D["nonpassers_top"]
    for grp, cs in (("passers", [c for c in seen if c["pass"]]), ("non-passers", [c for c in seen if not c["pass"]])):
        if not cs:
            continue
        ws = []
        for c in cs:
            try:
                ws.append(G.weight(c["expr"]))
            except ValueError:
                ws.append(1.0)
        notes.append(f"priors on the {len(cs)} {grp} already seen: banned {sum(w <= 0 for w in ws)}, down-weighted {sum(0 < w < 1 for w in ws)}, "
                     f"up-weighted {sum(w > 1 for w in ws)}")

print(("ADMISSIBLE" if not issues else "NOT ADMISSIBLE") + f" -- {path}: {len(ideas)} ideas, {len(spec.get('priors') or [])} priors")
for x in issues:
    print("- " + x)
for x in notes:
    print("  (diagnostic) " + x)
sys.exit(1 if issues else 0)
