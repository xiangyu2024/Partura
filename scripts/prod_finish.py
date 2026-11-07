"""PROD W01, laptop side: the last three steps of one seed's round in one command -- finalize, check, push.

    python scripts/prod_finish.py <round> <seed> [--no-push]

1. scripts/c06_check.py <seed> <round> --finalize   (PARTURA_C0X=PROD, PARTURA_STUDY_DIR from research/prod_W01/hosts.json, strike line 0.8):
   applies the audit (audit_1.yaml, corr_1.json) to the PI's draft -> missions_final.yaml, audit_record.json.  It refuses a draft that is
   not admissible (the same rules the PI checked: parse, core inside a snapshot head, <= 16 seeds / R variants, banned operators, round-3 N slot).
2. check_final(): the structure of what is about to run on a server -- two slots, E has a core and 4..16 seeds, an N slot has 4..16 seeds
   or is a plain GP (no seeds), no banned operator anywhere, <= 16 R variants, an audit record for both slots.
3. scripts/prod_sync.sh push <round> <seed>   (atomic, md5-checked; refuses to replace a different plan already on the server).
Exit 0 only if all three succeeded.  Prints the FINALIZED line of step 1 and one final line "PUSHED ..." / "NOT PUSHED ...".
"""
import json
import os
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANNED = re.compile(r"\b(ts_spearman|nt_[A-Za-z0-9_]+)\s*\(")


def check_final(plan, record, seed, rnd):
    """Problems with a finalized plan (empty list = fine).  Pure: takes the loaded missions_final.yaml and audit_record.json."""
    issues = []
    if plan.get("seed") != seed or plan.get("round") != rnd:
        issues.append(f"seed / round are {plan.get('seed')} / {plan.get('round')}, expected {seed} / {rnd}")
    slots = plan.get("slots") or []
    if len(slots) != 2:
        issues.append(f"{len(slots)} slots, expected 2")
    for i, s in enumerate(slots):
        w = f"slot {'ab'[i] if i < 2 else i + 1}"
        seeds = s.get("seeds") or []
        if s.get("type") not in ("E", "N"):
            issues.append(f"{w}: type {s.get('type')!r}")
        elif s.get("audit_failed"):
            if s["type"] != "N" or seeds:
                issues.append(f"{w}: a plain-GP slot must be type N without seeds")
        else:
            if not 4 <= len(seeds) <= 16:
                issues.append(f"{w}: {len(seeds)} seeds, expected 4..16")
            if s["type"] == "E" and not str(s.get("core", "")).strip():
                issues.append(f"{w}: an E slot without a core")
        for e in ([s.get("core")] if s.get("core") else []) + list(seeds):
            if BANNED.search(str(e)):
                issues.append(f"{w}: banned operator in {str(e)[:80]}")
    nv = 0
    for i, r in enumerate(plan.get("R") or []):
        vs = r.get("variants") or []
        nv += len(vs)
        if not str(r.get("head", "")).strip() or not vs:
            issues.append(f"R {i + 1}: no head or no variants")
        for e in vs:
            if BANNED.search(str(e)):
                issues.append(f"R {i + 1}: banned operator in {str(e)[:80]}")
    if nv > 16:
        issues.append(f"R: {nv} variants, at most 16")
    if len(record.get("slots") or []) != 2:
        issues.append("audit_record.json does not describe both slots")
    return issues


def main(argv):
    rnd, seed = int(argv[0]), int(argv[1])
    push = "--no-push" not in argv
    sys.path.insert(0, str(ROOT / "scripts"))
    import prod_hosts
    dirname = prod_hosts.load()["dir"]
    env = {**os.environ, "PARTURA_C0X": "PROD", "PARTURA_STUDY_DIR": dirname}
    env.setdefault("C06_CTRL_STRIKE", "0.8")
    r = subprocess.run([sys.executable, str(ROOT / "scripts" / "c06_check.py"), str(seed), str(rnd), "--finalize"], cwd=ROOT, env=env,
                       capture_output=True, text=True)
    print((r.stdout + r.stderr).strip())
    if r.returncode != 0:
        print(f"NOT PUSHED: finalize failed (exit {r.returncode})")
        return 1
    base = ROOT / "research" / dirname / "partura" / f"s{seed}" / f"r{rnd}"
    import yaml
    plan = yaml.safe_load((base / "missions_final.yaml").read_text(encoding="utf-8")) or {}
    record = json.loads((base / "audit_record.json").read_text(encoding="utf-8"))
    issues = check_final(plan, record, seed, rnd)
    if issues:
        print("NOT PUSHED: the final plan fails its check\n" + "\n".join(f"- {x}" for x in issues))
        return 1
    print(f"CHECK OK: {len(plan['slots'])} slots, R {sum(len(x.get('variants') or []) for x in plan.get('R') or [])} variants")
    if not push:
        print("NOT PUSHED (--no-push)")
        return 0
    p = subprocess.run(["bash", str(ROOT / "scripts" / "prod_sync.sh"), "push", str(rnd), str(seed)], cwd=ROOT, capture_output=True, text=True)
    print((p.stdout + p.stderr).strip())
    if p.returncode != 0 or "pushed" not in p.stdout:
        print("NOT PUSHED: the push failed")
        return 1
    print(f"PUSHED seed {seed} round {rnd}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
