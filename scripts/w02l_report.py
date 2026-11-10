"""PROD W02L (research/prod_W02L/PLAN.md): in-sample read-out of the rounds that have ended -- per stream and round, the best GP
candidate of each slot and the best R variant, all under ruler B (the missions run with the two champions as extra controls),
with the batch's own best member for comparison; then every new head (score >= 0.5, |rho| to the known family < 0.5).
Server; train 2018-01-02 ~ 2023-08-07 and valid 2023-08-08 ~ 2025-12-31 only -- nothing of 2026 is read.

    python scripts/w02l_report.py > research/prod_W02L/report.md
"""
import glob
import sys
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


# User decision 2026-11-10: a head is judged under ruler D (B plus per-day decile dummies of size, liquidity and price).  The
# missions' candidates carry B only; D comes from research/prod_W02L/d_scores.jsonl (scripts/w02l_backtest.py --d-jsonl), filled for
# every candidate with B >= 0.3 and |rho_known| < 0.5 (--collect-d <file> lists the ones still missing).
DS = {}
if (D / "d_scores.jsonl").is_file():
    for ln in open(D / "d_scores.jsonl", encoding="utf-8"):
        if ln.strip():
            x = json.loads(ln)
            DS[x["expr"]] = x.get("D")


def near(x):
    return isinstance(x.get("score"), (int, float)) and x["score"] >= 0.3 and abs(x.get("rho_known") or 0) < 0.5


def fmt(x):
    if not x:
        return "—"
    rk = x.get("rho_known")
    return (f"{x['score']:+.2f} (tr {x.get('train', float('nan')):+.2f} / va {x.get('valid', float('nan')):+.2f}"
            f"{'' if rk is None else f', ρK {rk:+.2f}'}) `{x.get('expr', '')[:80]}`")


rows, heads, repl, pool = [], [], [], []
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
        pool += [{**c, "seed": S, "round": K, "slot": tag} for c in A.get("candidates", []) + A.get("heads", []) if near(c)]
        for h in A.get("heads", []):
            heads.append({**h, "seed": S, "round": K, "slot": tag})
        heads += [{**c, "seed": S, "round": K, "slot": tag} for c in A.get("candidates", []) if is_head(c) and c not in A.get("heads", [])]
    rf = D / "arms" / f"s{S}_P_r{K}_R.json"
    R = json.loads(rf.read_text(encoding="utf-8")) if rf.is_file() else {}
    rbest = best(R.get("rows", []))
    for r in R.get("replacements", []) + R.get("additions", []):
        (heads if is_head(r) else repl).append({**r, "seed": S, "round": K, "slot": "R"})
        if near(r):
            pool.append({**r, "seed": S, "round": K, "slot": "R"})
    rows.append((S, K, batch, base, slots, rbest))

if "--collect-d" in sys.argv:                                 # the candidates whose D is still missing, one per line
    want = list(dict.fromkeys(x["expr"] for x in pool if x.get("expr") and x["expr"] not in DS))
    Path(sys.argv[sys.argv.index("--collect-d") + 1]).write_text("".join(e + "\n" for e in want), encoding="utf-8")
    print(f"{len(want)} candidates need D ({len(DS)} done)")
    sys.exit(0)


def d_of(x):
    return DS.get(x.get("expr")) if x.get("expr") in DS else None


seen, dheads = set(), []
for x in sorted(pool, key=lambda x: -(d_of(x) or {}).get("score", -9)):
    d = d_of(x)
    if d and d["score"] >= 0.5 and abs(x.get("rho_known") or 0) < 0.5 and x["expr"] not in seen:
        seen.add(x["expr"])
        dheads.append({**x, "D": d})
b_failed = [h for h in heads if d_of(h) and d_of(h)["score"] < 0.5]
b_pending = [h for h in heads if h.get("expr") not in DS]


def fmt_d(x):
    d = x["D"] if "D" in x else d_of(x)
    return f"D {d['score']:+.2f} (tr {d['train']:+.2f} / va {d['valid']:+.2f})" if d else "D 待算"


print(f"# W02L 样本内读数(只有 train / valid,2026 未读)\n\n已结束的轮次 {len(rows)} 个。"
      f"**新 head(尺子 D ≥ 0.5、|ρK| < 0.5;用户 2026-11-10 定)**:{len(dheads)} 个(不重复的表达式)。"
      f"尺子 B 过线的 {len(heads)} 个里，D 没过 {len(b_failed)} 个、D 待算 {len(b_pending)} 个;"
      f"R 的改进(比原素材高 0.1 以上,但不到 head){len(repl)} 个。下表是尺子 B(搜索用的奖励)。\n")
print("| 流 | 轮 | 批 | 批内原最好 | 任务位 a 最好 | 任务位 b 最好 | R 最好 |\n|---|---|---|---|---|---|---|")
for S, K, b, base, slots, rb in rows:
    print(f"| {S} | {K} | {b} | {fmt(base)} | {fmt(slots.get('a'))} | {fmt(slots.get('b'))} | {fmt(rb)} |")
print("\n## 新 head(尺子 D)\n")
for h in dheads:
    print(f"- s{h['seed']} r{h['round']} {h['slot']}: {fmt_d(h)};B {fmt(h)}")
if not dheads:
    print("(还没有)")
print("\n## 尺子 B 过线、D 没过\n")
for h in sorted(b_failed, key=lambda h: -h.get("score", 0)):
    print(f"- s{h['seed']} r{h['round']} {h['slot']}: {fmt_d(h)};B {fmt(h)}")
if b_pending:
    print("\n## 尺子 B 过线、D 待算\n")
    for h in sorted(b_pending, key=lambda h: -h.get("score", 0)):
        print(f"- s{h['seed']} r{h['round']} {h['slot']}: B {fmt(h)}")
print("\n## R 的改进(替换素材,不算 head)\n")
for h in sorted(repl, key=lambda h: -h.get("score", 0)):
    print(f"- s{h['seed']} r{h['round']}: {fmt(h)}")
