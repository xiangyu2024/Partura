"""PROD W02L (research/prod_W02L/PLAN.md): in-sample read-out of the rounds that have ended -- per stream and round, the best GP
candidate of each slot and the best R variant, all under ruler B (the missions run with the two champions as extra controls),
with the batch's own best member for comparison; then every new head (score >= 0.5, |rho| to the known family < 0.5).
Server; train 2018-01-02 ~ 2023-08-07 and valid 2023-08-08 ~ 2025-12-31 only -- nothing of 2026 is read.

    python scripts/w02l_report.py > research/prod_W02L/report.md
"""
import glob
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "research" / "prod_W02L"
streams = {x["seed"]: x for x in json.loads((D / "streams.json").read_text(encoding="utf-8"))["streams"]}


def best(cands):
    c = [x for x in cands if isinstance(x.get("score"), (int, float))]
    return max(c, key=lambda x: x["score"]) if c else None


def is_head(x):                                               # PLAN section 7: score >= 0.5 under B and |rho| to the known family < 0.5
    return isinstance(x.get("score"), (int, float)) and x["score"] >= 0.5 and abs(x.get("rho_known") or 0) < 0.5


def fmt(x):
    if not x:
        return "—"
    rk = x.get("rho_known")
    return (f"{x['score']:+.2f} (tr {x.get('train', float('nan')):+.2f} / va {x.get('valid', float('nan')):+.2f}"
            f"{'' if rk is None else f', ρK {rk:+.2f}'}) `{x.get('expr', '')[:80]}`")


rows, heads, repl = [], [], []
for done in sorted(glob.glob(str(D / "arms" / "s*_P_r*.DONE"))):
    m = re.search(r"s(\d+)_P_r(\d)\.DONE", done)
    S, K = int(m.group(1)), int(m.group(2))
    batch = streams.get(S, {}).get("batches", [None] * 3)[K - 1]
    mev = ROOT / "episodes" / f"prods{S}M{K}_I0_open_search" / "evidence.json"
    base = best(json.loads(mev.read_text(encoding="utf-8"))["arms"]["control"]["candidates"]) if mev.is_file() else None
    slots = {}
    for ev in sorted(glob.glob(str(ROOT / "episodes" / f"prods{S}Pr{K}?_*" / "evidence.json"))):
        tag = Path(ev).parent.name.split("_")[0][-1]
        A = list(json.loads(Path(ev).read_text(encoding="utf-8"))["arms"].values())[0]
        slots[tag] = best(A.get("candidates", []))
        for h in A.get("heads", []):
            heads.append({**h, "seed": S, "round": K, "slot": tag})
        heads += [{**c, "seed": S, "round": K, "slot": tag} for c in A.get("candidates", []) if is_head(c) and c not in A.get("heads", [])]
    rf = D / "arms" / f"s{S}_P_r{K}_R.json"
    R = json.loads(rf.read_text(encoding="utf-8")) if rf.is_file() else {}
    rbest = best(R.get("rows", []))
    for r in R.get("replacements", []) + R.get("additions", []):
        (heads if is_head(r) else repl).append({**r, "seed": S, "round": K, "slot": "R"})
    rows.append((S, K, batch, base, slots, rbest))

print(f"# W02L 样本内读数(尺子 B;只有 train / valid,2026 未读)\n\n已结束的轮次 {len(rows)} 个;新 head(score ≥ 0.5、|ρK| < 0.5){len(heads)} 个;"
      f"R 的改进(比原素材高 0.1 以上,但不到 head){len(repl)} 个。\n")
print("| 流 | 轮 | 批 | 批内原最好 | 任务位 a 最好 | 任务位 b 最好 | R 最好 |\n|---|---|---|---|---|---|---|")
for S, K, b, base, slots, rb in rows:
    print(f"| {S} | {K} | {b} | {fmt(base)} | {fmt(slots.get('a'))} | {fmt(slots.get('b'))} | {fmt(rb)} |")
print("\n## 新 head\n")
for h in sorted(heads, key=lambda h: -h.get("score", 0)):
    print(f"- s{h['seed']} r{h['round']} {h['slot']}: {fmt(h)}")
if not heads:
    print("(还没有)")
print("\n## R 的改进(替换素材,不算 head)\n")
for h in sorted(repl, key=lambda h: -h.get("score", 0)):
    print(f"- s{h['seed']} r{h['round']}: {fmt(h)}")
