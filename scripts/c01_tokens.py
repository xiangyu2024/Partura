"""C01: the token ledger of a Partura round, and the audit of its cold-start barrier (research/coldstart_C01/PLAN.md §2.6, §3.4).

Local.  Reads the transcripts the Workflow tool leaves for each agent of a run (<workflow dir>/agent-*.jsonl + .meta.json):
every assistant message's usage (de-duplicated by message id -- one message is logged once per content block), its
model, its timestamps; and every tool call's input, matched against the paths a cold-start agent may not read.

    python scripts/c01_tokens.py <workflow_dir> --round <k> [--out research/coldstart_C01/tokens_r<k>.json]
"""
import json
import re
import sys
from collections import defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WF = Path(sys.argv[1])
argv = sys.argv[2:]
K = int(argv[argv.index("--round") + 1])
OUT = Path(argv[argv.index("--out") + 1]) if "--out" in argv else ROOT / "research" / "coldstart_C01" / f"tokens_r{K}.json"
FORBIDDEN = re.compile(r"(Partura/lab/|findings\.yaml|guidance/(?!C00_base|C01_)[A-Za-z]|Partura/episodes/(?!c01)[a-z]|research/(?!coldstart_C01)[a-z_]+/|"
                       r"Partura/notes/|Partura/studies/|Partura/handoff/|Partura/runs/|Partura/batches/|AlphaCube/docs/|AlphaCube/mining_runs/)")
ROLE = {"coord": "总领", "lead": "主研", "exec": "执行", "check": "检查"}
FIELDS = ("input_tokens", "cache_creation_input_tokens", "cache_read_input_tokens", "output_tokens")


def ts(s):
    return datetime.fromisoformat(s.replace("Z", "+00:00")) if s else None


agents = []
for f in sorted(WF.glob("agent-*.jsonl")):
    meta_p = f.parent / (f.name[:-len(".jsonl")] + ".meta.json")
    meta = json.loads(meta_p.read_text()) if meta_p.is_file() else {}
    label = meta.get("description", f.stem)
    seen, models, times, hits = set(), defaultdict(int), [], []
    per_msg = defaultdict(lambda: defaultdict(int))
    for line in f.open(encoding="utf-8"):
        try:
            m = json.loads(line)
        except json.JSONDecodeError:
            continue
        if m.get("timestamp"):
            times.append(ts(m["timestamp"]))
        msg = m.get("message") or {}
        if m.get("type") == "assistant":
            for blk in msg.get("content") or []:
                if isinstance(blk, dict) and blk.get("type") == "tool_use":
                    s = json.dumps(blk.get("input"), ensure_ascii=False)
                    for x in FORBIDDEN.findall(s):
                        hits.append({"tool": blk.get("name"), "match": x, "input": s[:240]})
            mid = msg.get("id")
            if msg.get("usage"):                      # a message is logged once per content block; its usage grows to the final count
                if mid not in seen:
                    seen.add(mid)
                    models[msg.get("model")] += 1
                for k in FIELDS:
                    per_msg[mid][k] = max(per_msg[mid][k], msg["usage"].get(k, 0) or 0)
    use = {k: sum(v[k] for v in per_msg.values()) for k in FIELDS}
    key = label.split(":")[1] if ":" in label else label
    role = next((v for k, v in ROLE.items() if key.startswith(k)), "?")
    times = [t for t in times if t]
    agents.append({"label": label, "role": role, "models": dict(models), "messages": len(seen), **use,
                   "seconds": (max(times) - min(times)).total_seconds() if len(times) > 1 else 0.0,
                   "start": min(times).isoformat() if times else None, "end": max(times).isoformat() if times else None,
                   "forbidden_reads": hits})

if not agents:
    raise SystemExit(f"no agent transcripts in {WF}")
tot = {k: sum(a[k] for a in agents) for k in FIELDS}
by_role = defaultdict(lambda: defaultdict(float))
by_model = defaultdict(lambda: defaultdict(float))
for a in agents:
    for k in FIELDS:
        by_role[a["role"]][k] += a[k]
        for mdl, n in a["models"].items():
            by_model[mdl][k] += a[k] * n / max(a["messages"], 1)
starts = [a["start"] for a in agents if a["start"]]
ends = [a["end"] for a in agents if a["end"]]
wall = (ts(max(ends)) - ts(min(starts))).total_seconds() if starts and ends else 0.0
out = {"round": K, "workflow_dir": str(WF), "agents": agents, "total": tot, "by_role": {k: dict(v) for k, v in by_role.items()},
       "by_model": {k: dict(v) for k, v in by_model.items()}, "wall_seconds": wall,
       "forbidden_reads": sum(len(a["forbidden_reads"]) for a in agents)}
OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

print(f"round {K}: {len(agents)} agents, wall {wall / 60:.1f} min; forbidden reads {out['forbidden_reads']}")
print(f"{'agent':34s} {'role':4s} {'model':18s} {'msgs':>5s} {'input':>8s} {'cache_w':>9s} {'cache_r':>11s} {'output':>8s} {'min':>5s}")
for a in agents:
    print(f"{a['label'][:34]:34s} {a['role']:4s} {','.join(a['models'])[:18]:18s} {a['messages']:5d} {a['input_tokens']:8d} "
          f"{a['cache_creation_input_tokens']:9d} {a['cache_read_input_tokens']:11d} {a['output_tokens']:8d} {a['seconds'] / 60:5.1f}")
print(f"{'TOTAL':34s} {'':4s} {'':18s} {'':5s} {tot['input_tokens']:8d} {tot['cache_creation_input_tokens']:9d} {tot['cache_read_input_tokens']:11d} {tot['output_tokens']:8d}")
for a in agents:
    for h in a["forbidden_reads"][:5]:
        print(f"  FORBIDDEN  {a['label']}: {h['tool']} {h['match']} :: {h['input'][:160]}")
print(f"wrote {OUT}")
