"""PROD W02L (research/prod_W02L/PLAN.md): turn the structural batches of the two champion libraries into the "main AlphaCube
batches" the production round machinery reads, so that scripts/server/prod_conductor.sh, c05_locate.py and c05_round.py run
unchanged.  Server; reads only stage 0's in-sample results (train 2018-01-02 ~ 2023-08-07, valid 2023-08-08 ~ 2025-12-31).

    python scripts/w02l_lib.py build --ruler A|B [--max-heads 8] [--min-heads 1] [--first-seed 2001] [--per-stream 3]

  - a batch's "heads" = its members that are discoveries under the ruler (gate passed, score >= 0.5, |rho| to the known family
    < 0.5), best score first, at most --max-heads; members using ts_spearman never are (C01 revision 4)
  - a batch with fewer than --min-heads heads gets no round
  - streams: the eligible batches, theme by theme (themes with most heads first; inside a theme, most heads first), cut into
    runs of --per-stream; stream j is seed first_seed + j, its round k reads batches 1..k (W01: M batches 1..k)
  - per stream and k: episodes/prods<seed>M<k>_I0_open_search/evidence.json (arms.control.heads / candidates, complete) and
    control/checkpoints/archive_gen001.csv (every member with its score: the locate tool's enrichment table), and
    research/prod_W02L/m/s<seed>.DONE (there is no M chain to start)
  - research/prod_W02L/streams.json, research/prod_W02L/library_all.json (every library expression: the skeleton ban)
Refuses to overwrite an existing episode unless --force.
"""
import csv
import glob
import json
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "research" / "prod_W02L"
EP = ROOT / "episodes"


def opt(name, default):
    return type(default)(sys.argv[sys.argv.index(name) + 1]) if name in sys.argv else default


assert sys.argv[1] == "build"
RULER = opt("--ruler", "B")
MAXH, MINH, FIRST, PER = opt("--max-heads", 8), opt("--min-heads", 1), opt("--first-seed", 2001), opt("--per-stream", 3)
FORCE = "--force" in sys.argv

rows = [json.loads(x) for f in sorted(glob.glob(str(D / "stage0" / "chunks" / "*.jsonl"))) for x in open(f, encoding="utf-8") if x.strip()]
batches = {b["batch"]: b for b in json.loads((D / "struct" / "batches.json").read_text(encoding="utf-8"))["batches"]}
members = list(csv.DictReader(open(D / "struct" / "members.csv", encoding="utf-8")))
scored = {(r["lib"], int(r["i"])): r for r in rows}
missing = [m for m in members if (m["lib"], int(m["i"])) not in scored]
if missing:
    raise SystemExit(f"stage 0 not finished: {len(missing)} of {len(members)} expressions have no result")

by_batch = defaultdict(list)
for r in rows:
    by_batch[r["batch"]].append(r)


def head(r):
    s = r[RULER]
    return {"expr": r["expression"], "sign": s["sign"], "hl": s["hl"], "score": s["score"], "train": s["train"], "valid": s["valid"],
            "rho_known": r["rho"]["known"], "rho_H": r["rho"]["H"], "rho_X": r["rho"]["X"], "lib": r["lib"], "i": r["i"]}


heads = {}
for b, rs in by_batch.items():
    hs = [r for r in rs if r.get(f"discovery_{RULER}") and "ts_spearman" not in r["expression"]]
    hs.sort(key=lambda r: -r[RULER]["score"])
    heads[b] = [head(r) for r in hs[:MAXH]]
eligible = [b for b in heads if len(heads[b]) >= MINH]
MATERIAL = []
if len(eligible) < 24:                                        # PLAN section 4: too few batches with heads for the pilot -> the batches
    for b, rs in by_batch.items():                            # without one get their 3 best gated members with score > 0 as "material"
        if heads[b]:                                          # (a starting point for the PI and the locate tool; never counted as a
            continue                                          # W02L head)
        ms = sorted([r for r in rs if r.get("gate") and r[RULER]["score"] > 0 and "ts_spearman" not in r["expression"]],
                    key=lambda r: -r[RULER]["score"])[:3]
        if ms:
            heads[b] = [{**head(r), "material": True} for r in ms]
            MATERIAL.append(b)
    eligible = [b for b in heads if len(heads[b]) >= MINH]
theme_heads = defaultdict(int)
for b in eligible:
    theme_heads[batches[b]["theme"]] += len(heads[b])
order = sorted(eligible, key=lambda b: (-theme_heads[batches[b]["theme"]], batches[b]["theme"], -len(heads[b]), b))
streams = [order[j:j + PER] for j in range(0, len(order), PER)]

out = []
for j, bs in enumerate(streams):
    seed = FIRST + j
    for k, b in enumerate(bs, 1):
        ep = EP / f"prods{seed}M{k}_I0_open_search"
        if (ep / "evidence.json").is_file() and not FORCE:
            raise SystemExit(f"{ep} exists (use --force)")
        (ep / "control" / "checkpoints").mkdir(parents=True, exist_ok=True)
        cands = []
        for r in sorted(by_batch[b], key=lambda r: -r[RULER]["score"] if r.get("gate") else 9e9):   # best first, ungated last
            c = {"expr": r["expression"], "lib": r["lib"], "i": r["i"], "gate": bool(r.get("gate"))}
            if r.get("gate"):
                c.update({k2: r[RULER][k2] for k2 in ("score", "train", "valid", "sign", "hl", "turnover")}, rho_known=r["rho"]["known"])
            cands.append(c)
        ev = {"idea": "W02L library batch", "reward": "long_neutral", "threshold": 0.5, "complete": True,
              "period": ["20180102", "20251231", "20230808"],
              "w02l": {"batch": b, "theme": batches[b]["theme"], "kind": batches[b]["kind"], "ruler": RULER, "n_members": len(by_batch[b]),
                       "core": batches[b].get("core", [])[:3], "source": "stage 0 (research/prod_W02L/stage0)"},
              "arms": {"control": {"error": None, "scored": sum(c["gate"] for c in cands), "passers": len(heads[b]), "archive": len(cands),
                                   "heads": heads[b], "candidates": cands}}}
        (ep / "evidence.json").write_text(json.dumps(ev, ensure_ascii=False, indent=1), encoding="utf-8")
        with open(ep / "control" / "checkpoints" / "archive_gen001.csv", "w", encoding="utf-8", newline="") as fh:
            w = csv.writer(fh)
            w.writerow(["expression", "score_p_score"])
            for c in cands:
                w.writerow([c["expr"], c.get("score", "")])
    (D / "m").mkdir(parents=True, exist_ok=True)
    (D / "m" / f"s{seed}.DONE").touch()
    out.append({"seed": seed, "batches": bs, "themes": [batches[b]["theme"] for b in bs], "heads": [len(heads[b]) for b in bs]})

(D / "streams.json").write_text(json.dumps({"ruler": RULER, "max_heads": MAXH, "min_heads": MINH, "per_stream": PER, "material_batches": MATERIAL,
                                            "eligible_batches": len(eligible), "streams": out}, ensure_ascii=False, indent=1), encoding="utf-8")
(D / "library_all.json").write_text(json.dumps([{"expr": m["expression"]} for m in members], ensure_ascii=False), encoding="utf-8")
print(f"ruler {RULER}: {sum(len(h) for h in heads.values())} heads ({len(MATERIAL)} batches on material) in {sum(1 for h in heads.values() if h)} batches; "
      f"{len(eligible)} eligible (>= {MINH}); {len(streams)} streams of <= {PER} (seeds {FIRST}..{FIRST + len(streams) - 1})")
