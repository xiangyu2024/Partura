"""Copy what every workflow agent of this session has returned so far into the repository (no model quota).

Workflow agents' reasoning is not kept; their RETURN VALUES are, in each run's journal.jsonl under
~/.claude/projects/<project>/<session>/subagents/workflows/wf_*/ -- outside the repository.  This copies every
run's journal and writes one readable JSON per completed agent to handoff/workflows/<run_id>/, so that whoever
takes over (another model, another session) has the results even if the run never finishes.

    python scripts/wf_dump.py [--loop 120] [--hours 24]
"""
import json
import re
import shutil
import sys
import time
from pathlib import Path

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]
loop = int(argv[argv.index("--loop") + 1]) if "--loop" in argv else 0
hours = float(argv[argv.index("--hours") + 1]) if "--hours" in argv else 36.0
base = Path.home() / ".claude" / "projects"


def once():
    n = 0
    for wf in base.glob("*/*/subagents/workflows/wf_*"):
        j = wf / "journal.jsonl"
        if not j.is_file() or time.time() - j.stat().st_mtime > hours * 3600:
            continue
        out = root / "handoff" / "workflows" / wf.name
        out.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(j, out / "journal.jsonl")
        index = []
        for i, line in enumerate(j.read_text(encoding="utf-8", errors="replace").splitlines()):
            try:
                rec = json.loads(line)
            except Exception:
                continue
            label = str(rec.get("label") or rec.get("opts", {}).get("label") or rec.get("key") or f"agent{i}") if isinstance(rec, dict) else f"agent{i}"
            name = re.sub(r"[^A-Za-z0-9_.:-]+", "_", label)[:80]
            (out / f"{i:03d}_{name}.json").write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
            index.append({"i": i, "label": label, "type": rec.get("type") if isinstance(rec, dict) else None,
                          "has_result": bool(isinstance(rec, dict) and rec.get("result") is not None)})
            n += 1
        (out / "INDEX.json").write_text(json.dumps({"run": wf.name, "source": str(j), "dumped_at": time.strftime("%F %T"), "agents": index},
                                                   ensure_ascii=False, indent=1), encoding="utf-8")
    return n


while True:
    k = once()
    print(f"[wf_dump] {time.strftime('%T')} {k} journal records copied", flush=True)
    if not loop:
        break
    time.sleep(loop)
