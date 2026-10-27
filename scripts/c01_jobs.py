"""C01: the server jobs of round k >= 2 from the coordinator's seed assignment (research/coldstart_C01/PLAN.md §2.3–2.5).

Local.  Each seed gets two jobs, A then B, so a round cut short leaves whole pairs:
    c01r<k>s<seed>A  I0_open_search  guidance/C00_base.yaml  control  <seed>  --parts priors     (AlphaCube alone)
    c01r<k>s<seed>B  <idea>          <guidance>              steer    <seed>                    (AlphaCube + Partura)
An I0_open_search B job (priors only) also takes --parts priors, as e7 did.

    python scripts/c01_jobs.py <k> <guidance> '<json [{"idea": ..., "seeds": [...]}, ...]>'  -> research/coldstart_C01/jobs_r<k>.tsv
"""
import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
K, GPATH, ASSIGN = int(sys.argv[1]), sys.argv[2], json.loads(sys.argv[3])
SEEDS = [100 * K + 1 + i for i in range(8)]
ideas = {i["id"] for i in yaml.safe_load((ROOT / GPATH).read_text(encoding="utf-8"))["ideas"]}
by_seed = {}
for a in ASSIGN:
    if a["idea"] not in ideas:
        raise SystemExit(f"{a['idea']} is not an idea of {GPATH}")
    for s in a["seeds"]:
        if s in by_seed:
            raise SystemExit(f"seed {s} assigned twice")
        by_seed[int(s)] = a["idea"]
if sorted(by_seed) != SEEDS:
    raise SystemExit(f"the assignment must cover exactly the seeds {SEEDS}; got {sorted(by_seed)}")
lines = []
for s in SEEDS:
    lines.append(f"c01r{K}s{s}A\tI0_open_search\tguidance/C00_base.yaml\tcontrol\t{s}\t--parts\tpriors")
    idea = by_seed[s]
    lines.append(f"c01r{K}s{s}B\t{idea}\t{GPATH}\tsteer\t{s}" + ("\t--parts\tpriors" if idea == "I0_open_search" else ""))
out = ROOT / "research" / "coldstart_C01" / f"jobs_r{K}.tsv"
out.write_text("\n".join(lines) + "\n", encoding="utf-8")
print(f"wrote {out}: {len(lines)} jobs")
