"""C05 (research/coldstart_C05/PLAN.md): what the runs of one seed have produced so far, as the JSON files the next run reads.

    python scripts/c05_lib.py heads   <out.json> <episode dir> ...   -> [{"expr", "sign", "hl", "score", "train", "valid", "src"}]
    python scripts/c05_lib.py archive <out.json> <episode dir> ...   -> [{"expr", "score", "src"}]  (every scored candidate in the
                                                                        last archive checkpoint of every arm)
A missing or unfinished episode is an error: a run must never start on a library it did not mean to have.
"""
import csv
import json
import math
import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def finished(ep):
    """C05 PLAN revision 7: the evidence is written once after the search and again after the heads; only the last write is
    final.  Final = it says so ("complete", from revision 7 on), or the run's log shows the final write / its exit line, code 0."""
    f = Path(ep) / "evidence.json"
    if not f.is_file():
        return False
    if json.loads(f.read_text(encoding="utf-8")).get("complete"):
        return True
    log = ROOT / "logs" / f"_idea_{Path(ep).name.split('_')[0]}.log"
    tail = log.read_text(encoding="utf-8", errors="replace")[-4000:] if log.is_file() else ""
    # the last thing idea_search prints is "wrote <episode>/evidence.json (<seconds>s)": the final write happened
    return "[partura exit 0" in tail or re.search(r"wrote \S*/evidence\.json \(\d+s\)", tail) is not None


def evidence(ep):
    f = Path(ep) / "evidence.json"
    if not f.is_file():
        raise SystemExit(f"no evidence in {ep}")
    if not finished(ep):
        raise SystemExit(f"{ep}: the run has not finished (no final evidence write, no exit-0 line in its log)")
    E = json.loads(f.read_text(encoding="utf-8"))
    for arm, A in E["arms"].items():
        if "heads" not in A and A.get("passers", 0):
            raise SystemExit(f"{ep} ({arm}) has passers but no heads: unfinished")
    return E


def heads(eps):
    out = []
    for ep in eps:
        for arm, A in evidence(ep)["arms"].items():
            for h in A.get("heads", []):
                out.append({"expr": h["expr"], "sign": h["sign"], "hl": h["hl"], "score": h["score"], "train": h["train"],
                            "valid": h["valid"], "src": Path(ep).name})
    return out


def archive(eps):
    out = []
    for ep in eps:
        for arm in evidence(ep)["arms"]:
            files = sorted((Path(ep) / arm / "checkpoints").glob("archive_gen*.csv"))
            for r in (csv.DictReader(files[-1].open(encoding="utf-8")) if files else []):
                try:
                    s = float(r.get("score_p_score", "nan"))
                except ValueError:
                    s = float("nan")
                out.append({"expr": r["expression"], "score": s if math.isfinite(s) else None, "src": Path(ep).name})
    return out


if __name__ == "__main__":
    kind, dest, eps = sys.argv[1], Path(sys.argv[2]), sys.argv[3:]
    rows = {"heads": heads, "archive": archive}[kind](eps)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(json.dumps(rows, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{dest}: {len(rows)} {kind} from {len(eps)} episode(s)")
