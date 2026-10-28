"""C03 (derived from c02_check.py; reward long_neutral, base C03_base): deterministic admissibility checks for what Partura writes (research/coldstart_C03/PLAN.md §2.4).  Local.

    python scripts/c02_check.py hypotheses research/coldstart_C02/hypotheses_r<k>.yaml
    python scripts/c02_check.py guidance guidance/C02_r<k>.yaml
    exit 0 = admissible, 1 = not (the issues are printed)

hypotheses: <= 8 hypotheses, <= 64 variants in all; every hypothesis has a thesis (mechanism / counterparty / prediction /
fails_if) and at least one ``control`` variant; every variant parses in the search grammar and uses no operator the
environment bans (ts_spearman, nt_*); variant ids unique.
guidance:  loads; pool = C02_base; reward / evaluation empty; 1-2 ideas, reward long; seeds parse, use no banned operator,
<= 24 per idea, each with a role in ``seed_roles`` (new | improve), improve <= 1/3; priors well formed.
Both: nothing cites a file the plan forbids (RESULT.md, final*.json, ledger, runs/, lab/, C02 arm A).
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
import yaml  # noqa: E402

from partura import ops_ext  # noqa: E402,F401
from partura.steer import Guidance, Pattern  # noqa: E402
from alphacube.parser import parse  # noqa: E402
from alphacube.plugins import load_plugins  # noqa: E402

load_plugins(["partura.ac_plugin"])
MODE, PATH = sys.argv[1], Path(sys.argv[2])
BANNED = re.compile(r"\b(ts_spearman|nt_[A-Za-z0-9_]+)\s*\(")
FORBIDDEN = re.compile(r"(RESULT\.md|final(_dry)?\.json|ledger|runs/|lab/|c03r\d+s\d+A|findings\.yaml)")
THESIS = ("mechanism", "counterparty", "prediction", "fails_if")
issues = []
G0 = Guidance.load(ROOT / "guidance" / "C03_base.yaml")


def parses(expr: str) -> str:
    try:
        parse(G0.canonical(expr), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)
        return ""
    except Exception as exc:                                   # noqa: BLE001
        return f"{type(exc).__name__}: {str(exc)[:90]}"


try:
    spec = yaml.safe_load(PATH.read_text(encoding="utf-8"))
except Exception as exc:                                       # noqa: BLE001
    print(f"NOT ADMISSIBLE\n- does not load: {exc}")
    sys.exit(1)
if FORBIDDEN.search(PATH.read_text(encoding="utf-8")):
    issues.append("cites a file the plan forbids (RESULT.md / final*.json / ledger / runs/ / lab/ / C02 arm A)")

if MODE == "hypotheses":
    hs = spec.get("hypotheses") or []
    nv = sum(len(h.get("variants") or []) for h in hs)
    if not 1 <= len(hs) <= 8:
        issues.append(f"{len(hs)} hypotheses (1-8)")
    if nv > 64:
        issues.append(f"{nv} variants in all (<= 64)")
    seen = set()
    for h in hs:
        hid = h.get("id", "?")
        miss = [k for k in THESIS if not str((h.get("thesis") or {}).get(k, "")).strip()]
        if miss:
            issues.append(f"{hid}: thesis lacks {miss}")
        vs = h.get("variants") or []
        if not any(v.get("role") == "control" for v in vs):
            issues.append(f"{hid}: no control variant")
        for v in vs:
            vid = f"{hid}/{v.get('id', '?')}"
            if vid in seen:
                issues.append(f"{vid}: duplicate id")
            seen.add(vid)
            if v.get("role") not in ("core", "ablation", "control"):
                issues.append(f"{vid}: role must be core / ablation / control")
            e = str(v.get("expr", ""))
            if BANNED.search(e):
                issues.append(f"{vid}: uses an operator the environment bans (ts_spearman / nt_*): {e}")
            err = parses(e)
            if err:
                issues.append(f"{vid}: does not parse: {e} ({err})")
    head = f"{len(hs)} hypotheses, {nv} variants"
else:
    try:
        G = Guidance(spec)
    except Exception as exc:                                   # noqa: BLE001
        print(f"NOT ADMISSIBLE\n- guidance does not load: {exc}")
        sys.exit(1)
    if spec.get("pool") != G0.spec["pool"]:
        issues.append("pool differs from guidance/C03_base.yaml")
    for k in ("reward", "evaluation"):
        if spec.get(k):
            issues.append(f"'{k}' must be empty")
    ideas = spec.get("ideas") or []
    if not 1 <= len(ideas) <= 2:
        issues.append(f"{len(ideas)} ideas (1-2)")
    for i in ideas:
        iid = i.get("id", "?")
        if i.get("reward") != "long_neutral":
            issues.append(f"{iid}: reward must be long_neutral")
        seeds, roles = i.get("seeds") or [], i.get("seed_roles") or []
        if iid != "I0_open_search":
            if not 1 <= len(seeds) <= 24:
                issues.append(f"{iid}: {len(seeds)} seeds (1-24)")
            if len(roles) != len(seeds) or set(roles) - {"new", "improve"}:
                issues.append(f"{iid}: seed_roles must give new / improve for every seed")
            elif sum(r == "improve" for r in roles) * 3 > len(roles):
                issues.append(f"{iid}: improve seeds {sum(r == 'improve' for r in roles)} > 1/3 of {len(roles)}")
            miss = [k for k in THESIS if not str((i.get("thesis") or {}).get(k, "")).strip()]
            if miss:
                issues.append(f"{iid}: thesis lacks {miss}")
        for s in seeds:
            if BANNED.search(s):
                issues.append(f"{iid}: seed uses a banned operator: {s}")
            err = parses(s)
            if err:
                issues.append(f"{iid}: seed does not parse: {s} ({err})")
    for r in spec.get("priors") or []:
        rid = r.get("id", "?")
        if r.get("action") not in ("ban", "weight", "rewrite", "family"):
            issues.append(f"{rid}: action {r.get('action')!r}")
        try:
            Pattern.compile(str(r.get("pattern", "")))
        except Exception as exc:                               # noqa: BLE001
            issues.append(f"{rid}: pattern does not compile ({exc})")
        if r.get("action") == "weight" and not (isinstance(r.get("w"), (int, float)) and r["w"] > 0):
            issues.append(f"{rid}: weight needs w > 0")
        if not str(r.get("why", "")).strip() or not r.get("evidence"):
            issues.append(f"{rid}: needs why and evidence")
    head = f"{len(ideas)} ideas, {len(spec.get('priors') or [])} priors, {sum(len(i.get('seeds') or []) for i in ideas)} seeds"

print(("ADMISSIBLE" if not issues else "NOT ADMISSIBLE") + f" -- {PATH}: {head}")
for x in issues:
    print("- " + x)
sys.exit(1 if issues else 0)
