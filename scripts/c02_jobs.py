"""C02: the GP jobs of round k from the coordinator's seed assignment (research/coldstart_C02/PLAN.md §2.3-2.4).

Local.  Each seed gets two adjacent jobs, A then B (a batch cut short leaves whole pairs), with the same seed:
    c02r<k>s<seed>A  I0_open_search  guidance/C02_base.yaml  control  <seed>  --parts priors --budget 192 --population 48 --threshold 0.7
    c02r<k>s<seed>B  <idea>          <guidance>             steer    <seed>  --budget <192 - ceil(n_direct/8)> --population 48 --threshold 0.7 --seed-share 0.5
--split h: seeds are cut into h consecutive groups, one jobs file per host (a seed's A and B always on the same host).

    python scripts/c02_jobs.py <k> <guidance> <n_direct> '<json [{"idea": ..., "seeds": [...]}]>' [--split 2]
        -> research/coldstart_C02/jobs_r<k>.tsv  (or jobs_r<k>_h1.tsv, jobs_r<k>_h2.tsv ...)
"""
import json
import math
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
K, GPATH, NDIRECT, ASSIGN = int(sys.argv[1]), sys.argv[2], int(sys.argv[3]), json.loads(sys.argv[4])
SPLIT = int(sys.argv[sys.argv.index("--split") + 1]) if "--split" in sys.argv else 1
SEEDS = [400 + 100 * (K - 1) + 1 + i for i in range(8)]
GPB = 192 - math.ceil(NDIRECT / 8)
ideas = {i["id"] for i in yaml.safe_load((ROOT / GPATH).read_text(encoding="utf-8"))["ideas"]}
by_seed = {}
for a in ASSIGN:
    if a["idea"] not in ideas:
        raise SystemExit(f"{a['idea']} is not an idea of {GPATH}")
    for s in a["seeds"]:
        by_seed[int(s)] = a["idea"]
if sorted(by_seed) != SEEDS:
    raise SystemExit(f"the assignment must cover exactly {SEEDS}; got {sorted(by_seed)}")
common = "--population\t48\t--threshold\t0.7"
lines = {}
for n, s in enumerate(SEEDS):
    h = n * SPLIT // len(SEEDS) + 1
    idea = by_seed[s]
    extra = "\t--parts\tpriors" if idea == "I0_open_search" else ""
    lines.setdefault(h, []).append(f"c02r{K}s{s}A\tI0_open_search\tguidance/C02_base.yaml\tcontrol\t{s}\t--parts\tpriors\t--budget\t192\t{common}")
    lines.setdefault(h, []).append(f"c02r{K}s{s}B\t{idea}\t{GPATH}\tsteer\t{s}\t--budget\t{GPB}\t{common}\t--seed-share\t0.5{extra}")
for h, ls in lines.items():
    out = ROOT / "research" / "coldstart_C02" / (f"jobs_r{K}.tsv" if SPLIT == 1 else f"jobs_r{K}_h{h}.tsv")
    out.write_text("\n".join(ls) + "\n", encoding="utf-8")
    print(f"wrote {out.name}: {len(ls)} jobs (B budget {GPB} = 192 - ceil({NDIRECT}/8))")
