"""PROD W02L (research/prod_W02L/PLAN.md): turn the structural batches of the two champion libraries into the "main AlphaCube
batches" the production round machinery reads, so that scripts/server/prod_conductor.sh, c05_locate.py and c05_round.py run
unchanged.  Server; reads only stage 0's in-sample results (train 2018-01-02 ~ 2023-08-07, valid 2023-08-08 ~ 2025-12-31).

    python scripts/w02l_lib.py build --ruler B [--max-heads 8] [--first-seed 2001] [--per-stream 3]      (re-run as stage 0 goes on)

  - a batch's "heads" = its members that are discoveries under the ruler (gate passed, score >= 0.5, |rho| to the known family
    < 0.5), best score first, at most --max-heads; a batch with none gets its 3 best gated members by score as "material"
    (PLAN revision 1); members using ts_spearman never are (C01 revision 4)
  - streams: consecutive batch numbers (B001-B003 -> seed 2001, ...); a stream is built as soon as stage 0 has scored every
    member of its three batches; its round k reads batches 1..k (W01: M batches 1..k); streams built earlier are left alone
  - per stream and k: episodes/prods<seed>M<k>_I0_open_search/evidence.json (arms.control.heads / candidates, complete) and
    control/checkpoints/archive_gen001.csv (every member with its score: the locate tool's enrichment table), and
    research/prod_W02L/m/s<seed>.DONE (there is no M chain to start)
  - research/prod_W02L/streams.json, research/prod_W02L/library_all.json (every library expression: the skeleton ban)
Refuses to overwrite an existing episode unless --force.

User decision 2026-11-10: --head-ruler (default D) judges the heads: discovery under ruler D (stage 0's discovery_D, B plus
per-day decile dummies of size, liquidity and price), best D score first; --ruler still gives the scores the episodes carry
and the order of the material.  Stage 0's rows are read from stage0/chunks and then stage0/rescore (a rescore row wins), and a
batch counts as complete only when each of its rows is up to date for the head ruler (scored under it if gated, re-gated
under diagnose.levels_ok if the old gate rejected it).
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
HEADR = opt("--head-ruler", "D")
MAXH, FIRST, PER = opt("--max-heads", 8), opt("--first-seed", 2001), opt("--per-stream", 3)
FORCE = "--force" in sys.argv

rows = [json.loads(x) for sub_ in ("chunks", "rescore") for f in sorted(glob.glob(str(D / "stage0" / sub_ / "*.jsonl")))
        for x in open(f, encoding="utf-8") if x.strip()]                  # a rescore row comes later and wins
batches = {b["batch"]: b for b in json.loads((D / "struct" / "batches.json").read_text(encoding="utf-8"))["batches"]}
members = list(csv.DictReader(open(D / "struct" / "members.csv", encoding="utf-8")))
scored = {(r["lib"], int(r["i"])): r for r in rows}                # one row per member (a re-scored one counts once)
rows = list(scored.values())
missing = [m for m in members if (m["lib"], int(m["i"])) not in scored]
print(f"stage 0: {len(members) - len(missing)} of {len(members)} expressions scored", flush=True)

by_batch = defaultdict(list)
for r in rows:
    by_batch[r["batch"]].append(r)


def head(r):
    s = r[RULER]
    h = {"expr": r["expression"], "sign": s["sign"], "hl": s["hl"], "score": s["score"], "train": s["train"], "valid": s["valid"],
         "rho_known": r["rho"]["known"], "rho_H": r["rho"]["H"], "rho_X": r["rho"]["X"], "lib": r["lib"], "i": r["i"]}
    if HEADR != RULER and HEADR in r:
        h.update({f"score_{HEADR}": r[HEADR]["score"], f"train_{HEADR}": r[HEADR]["train"], f"valid_{HEADR}": r[HEADR]["valid"]})
    return h


heads, MATERIAL = {}, []
for b, rs in by_batch.items():                                # PLAN revision 1: discoveries if any, else the 3 best by score (material)
    ok = [r for r in rs if r.get("gate") and "ts_spearman" not in r["expression"]]
    hs = sorted([r for r in ok if r.get(f"discovery_{HEADR}")], key=lambda r: -r[HEADR]["score"])[:MAXH]
    if hs:
        heads[b] = [head(r) for r in hs]
    else:
        heads[b] = [{**head(r), "material": True} for r in sorted(ok, key=lambda r: -r[RULER]["score"])[:3]]
        MATERIAL.append(b)
# PLAN revision 1: streams = consecutive batch numbers (B001-B003 -> first seed, ...); a stream is built once all three of its
# batches are fully scored by stage 0 -- streams already built are left alone
allb = sorted(batches)
streams = [allb[j:j + PER] for j in range(0, len(allb), PER)]
# a batch is complete when every member that can matter is scored: ts_spearman members are deferred to the end of stage 0
# (scripts/w02l_stage0.py --defer-spearman) and can never be a head or material (above), so a batch does not wait for them
need = defaultdict(set)
for m in members:
    if "ts_spearman" not in m["expression"]:
        need[m["batch"]].add((m["lib"], int(m["i"])))
def current(r):
    """Is stage 0's row up to date for the head ruler and the levels gate (user decision 2026-11-10)?"""
    if "error" in r or "ts_spearman" in r["expression"]:
        return True
    if r.get("gate"):
        return HEADR in r
    return "levels" in r or r.get("coverage", 0.0) < 0.9


complete = {b for b in allb if need[b] <= {(r["lib"], int(r["i"])) for r in by_batch.get(b, [])}
            and all(current(r) for r in by_batch.get(b, []))}
prev = json.loads((D / "streams.json").read_text(encoding="utf-8")) if (D / "streams.json").is_file() else {"streams": []}
out = list(prev["streams"])
built_now = []
for j, bs in enumerate(streams):
    seed = FIRST + j
    if any(x["seed"] == seed for x in out) and not FORCE:
        continue                                              # built earlier
    if not all(b in complete for b in bs):
        continue                                              # stage 0 has not finished one of its batches yet
    built_now.append(seed)
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
    out = [x for x in out if x["seed"] != seed] + [{"seed": seed, "batches": bs, "themes": [batches[b]["theme"] for b in bs],
                                                    "heads": [len(heads[b]) for b in bs], "material": [b in MATERIAL for b in bs]}]

out.sort(key=lambda x: x["seed"])
(D / "streams.json").write_text(json.dumps({"ruler": RULER, "max_heads": MAXH, "per_stream": PER, "rule": "PLAN revision 1",
                                            "streams": out}, ensure_ascii=False, indent=1), encoding="utf-8")
(D / "library_all.json").write_text(json.dumps([{"expr": m["expression"]} for m in members], ensure_ascii=False), encoding="utf-8")
print(f"ruler {RULER}: built now {built_now or 'nothing'}; streams built {len(out)} of {len(streams)}; "
      f"next waiting for stage 0: {[FIRST + j for j, bs in enumerate(streams) if not all(b in complete for b in bs)][:3]}")
