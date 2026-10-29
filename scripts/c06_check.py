"""C06: Partura plan checks and the auditor's verdicts (research/coldstart_C06/PLAN.md §2.4-2.5).  Local.

    python scripts/c06_check.py <seed> <round>               the PI's draft partura/s<seed>/r<round>/missions.yaml: admissible?
    python scripts/c06_check.py <seed> <round> --finalize    apply the last audit (audit_<n>.yaml, corr_<n>.json) to the draft
                                                             -> missions_final.yaml (what the server runs) and audit_record.json
Exit 0 = admissible / finalized, 1 = not (the issues are printed).

Draft rules (as C05's c05_check.py): two GP slots, each E or N.  E: a core that parses, is a daily-valued tree reading a field, is a
subtree of a snapshot head (the whole head included) or one of the locate output's subtrees, and has had < 2 E slots before (slots
the audit turned into plain GP do not count); <= 16 seeds, each carrying the core verbatim.  N: a hypothesis and 1-16 seeds.
R: <= 16 variants in all, of heads in the snapshot.  Round 3: at least one N slot over rounds 1-3 (N slots that passed the audit).
No seed uses an operator the environment bans (ts_spearman, nt_*).  Every literature source has a year, before 2023-08-08.

Finalize (§2.5): a seed is struck when the auditor strikes it, or when the correlation table puts it at |rho| >= 0.7 with a head or
>= 0.5 with a control.  A slot passes when novelty >= 3, soundness >= 3, at least 4 seeds remain and (E) its core is not a control
in disguise (|rho| >= 0.5 with one); a slot that does not pass becomes a plain GP.  An R group passes when soundness >= 3.
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
from partura.steer import Guidance  # noqa: E402
from alphacube.expression import is_valid_root  # noqa: E402
from alphacube.parser import parse  # noqa: E402
from alphacube.plugins import load_plugins  # noqa: E402

load_plugins(["partura.ac_plugin"])
S, K = int(sys.argv[1]), int(sys.argv[2])
FINAL = "--finalize" in sys.argv
P = ROOT / "research" / "coldstart_C06" / "partura" / f"s{S}"
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


def prev_final(k):
    f = P / f"r{k}" / "missions_final.yaml"
    if not f.is_file():
        return {}
    return yaml.safe_load(f.read_text(encoding="utf-8")) or {}


try:
    spec = yaml.safe_load((P / f"r{K}" / "missions.yaml").read_text(encoding="utf-8")) or {}
    loc = json.loads((P / f"r{K}" / "loc.json").read_text(encoding="utf-8"))
except Exception as exc:                                       # noqa: BLE001
    print(f"NOT ADMISSIBLE\n- does not load: {exc}")
    sys.exit(1)

# ------------------------------------------------------------------ the draft (the same rules as C05)
if spec.get("seed") != S or spec.get("round") != K:
    issues.append(f"seed / round must be {S} / {K}")
slots = spec.get("slots") or []
if len(slots) != 2:
    issues.append(f"exactly 2 GP slots; got {len(slots)}")
known = set()                                                  # every subtree key the snapshot offers as a core
for h in loc["heads"]:
    t, _ = tree(h["expr"])
    if t is not None:
        known |= {n.key() for n in t.nodes()}
for e in [x["subtree"] for x in loc["enrichment"]] + [c["core"] for c in loc["core_cards"]]:
    t, _ = tree(e)
    if t is not None:
        known.add(t.key())
used, n_before = {}, 0
for k in range(1, K):
    for s in prev_final(k).get("slots", []):
        n_before += s.get("type") == "N" and bool(s.get("seeds"))
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
    issues.append("round 3: at least one N slot over rounds 1-3 (PLAN §2.5; slots the audit turned into plain GP do not count)")
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

if not FINAL:
    print("ADMISSIBLE" if not issues else "NOT ADMISSIBLE\n" + "\n".join(f"- {x}" for x in issues))
    sys.exit(1 if issues else 0)
if issues:
    print("CANNOT FINALIZE: the draft is not admissible\n" + "\n".join(f"- {x}" for x in issues))
    sys.exit(1)

# ------------------------------------------------------------------ finalize: the last audit decides (§2.5)
audits = sorted(P.glob(f"r{K}/audit_*.yaml"), key=lambda f: int(f.stem.split("_")[1]))
if not audits:
    print("CANNOT FINALIZE: no audit_<n>.yaml")
    sys.exit(1)
n = int(audits[-1].stem.split("_")[1])
A = yaml.safe_load(audits[-1].read_text(encoding="utf-8")) or {}
cf = P / f"r{K}" / f"corr_{n}.json"
if not cf.is_file():
    print(f"CANNOT FINALIZE: no corr_{n}.json for audit_{n}.yaml")
    sys.exit(1)
corr = {r["expr"]: r for r in json.loads(cf.read_text(encoding="utf-8"))["rows"]}


def disguised(e):
    """|rho| >= 0.7 with a head (the GP's library ban would refuse it anyway) or >= 0.5 with a control."""
    r = corr.get(e) or {}
    return "error" not in r and bool(r) and (r.get("max_head", 0) >= 0.7 or max(r.get("controls", {}).values() or [0]) >= 0.5)


by_slot = {str(a.get("slot")).lower(): a for a in A.get("slots") or []}
final_slots, record = [], {"seed": S, "round": K, "attempts": n, "slots": [], "R": []}
for s, j in zip(slots, "ab"):
    a = by_slot.get(j) or by_slot.get(str("ab".index(j) + 1)) or {}
    nov, snd = int(a.get("novelty") or 0), int(a.get("soundness") or 0)
    struck_by_auditor = {int(x) for x in a.get("struck_seeds") or []}
    seeds = s.get("seeds") or []
    kept = [e for i, e in enumerate(seeds) if i + 1 not in struck_by_auditor and not disguised(e)]
    core_bad = s["type"] == "E" and max(((corr.get(s["core"]) or {}).get("controls") or {}).values() or [0]) >= 0.5
    ok = nov >= 3 and snd >= 3 and len(kept) >= 4 and not core_bad
    rec = {"slot": j, "type": s["type"], "core": s.get("core"), "novelty": nov, "soundness": snd, "seeds": len(seeds),
           "struck_by_auditor": len(struck_by_auditor), "struck_by_table": sum(disguised(e) for e in seeds), "kept": len(kept),
           "core_is_a_control": core_bad, "pass": ok, "seeds_all": seeds, "seeds_kept": kept}
    record["slots"].append(rec)
    if ok:
        final_slots.append({**{k: v for k, v in s.items() if k != "seeds"}, "seeds": kept})
    else:
        final_slots.append({"type": "N", "note": f"audit did not pass after {n} attempt(s): plain GP (PLAN §2.5)", "audit_failed": True,
                            "proposed_type": s["type"]})
r_audit = {str(x.get("head")): x for x in A.get("R") or []}
final_R = []
for r in spec.get("R") or []:
    a = r_audit.get(str(r.get("head"))) or {}
    ok = int(a.get("soundness") or 0) >= 3
    record["R"].append({"head": r["head"], "soundness": int(a.get("soundness") or 0), "pass": ok, "variants": len(r.get("variants") or [])})
    if ok:
        final_R.append(r)
final = {"seed": S, "round": K, "slots": final_slots, "R": final_R, "audit": {"attempts": n, "file": audits[-1].name}}
(P / f"r{K}" / "missions_final.yaml").write_text(yaml.safe_dump(final, allow_unicode=True, sort_keys=False), encoding="utf-8")
(P / f"r{K}" / "audit_record.json").write_text(json.dumps(record, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"FINALIZED after {n} audit(s): " + "; ".join(f"slot {r['slot']} {r['type']} novelty {r['novelty']} soundness {r['soundness']} "
                                                     f"seeds {r['kept']}/{r['seeds']} -> {'pass' if r['pass'] else 'PLAIN GP'}" for r in record["slots"])
      + f"; R {sum(r['pass'] for r in record['R'])}/{len(record['R'])} groups")
