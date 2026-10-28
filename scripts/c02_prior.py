"""C02: what Partura may know from C01 before writing hypotheses -- IN-SAMPLE only (research/coldstart_C02/PLAN.md §2.5).

Local.  From episodes/c01*/evidence.json (both arms): every run's own heads (train / valid numbers only), the share of
passers in the known family, and the pointers to C01's beliefs and cards.  Nothing from the test period is read.

    python scripts/c02_prior.py      -> research/coldstart_C02/prior_c01.md
"""
import glob
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
rows, runs = [], []
for p in sorted(glob.glob(str(ROOT / "episodes" / "c01r*_*" / "evidence.json"))):
    E = json.loads(Path(p).read_text(encoding="utf-8"))
    tag = Path(p).parent.name
    for arm, A in E["arms"].items():
        cands = [c for c in A["candidates"] if isinstance(c.get("score"), (int, float)) and math.isfinite(c["score"])]
        passers = [c for c in cands if c["score"] >= 1.0]
        known = [c for c in passers if max([abs(c[k]) for k in ("rho_pool", "rho_known_traded") if isinstance(c.get(k), (int, float)) and c[k] == c[k]] or [0]) >= 0.5]
        runs.append((tag, arm, A["scored"], len(passers), len(known), len(A.get("heads") or [])))
        for h in A.get("heads") or []:
            rows.append((tag, arm, h))
rows.sort(key=lambda x: -x[2]["score"])
L = ["# C02 的先验知识:C01 的样本内结果(只含 train / valid;没有任何测试段数字)", "",
     "C01:A 组 = AlphaCube GP 盲搜;B 组 = AlphaCube + Partura v1(通过先验与邻域引导 GP)。R1 两组共用。score = 纯多头十分位书扣 15bp 的 train 与 valid 夏普中较差的。",
     "更多:C01 的 PLAN.md、beliefs_r2.md / beliefs_r3.md(Partura v1 自己的信念与诊断)、cards_r2.md / cards_r3.md、digest_r3.md、round3_workflow.json。", "",
     "## 每次运行", "", "| 运行 | 组 | 付费评估 | 通过(score ≥ 1) | 其中已知族(\\|ρ\\| ≥ 0.5) | 自己的 heads |", "|---|---|---|---|---|---|"]
for r in runs:
    L.append("| " + " | ".join(map(str, r)) + " |")
L += ["", f"## C01 的全部 heads(各运行内去重;{len(rows)} 个,按分数排序;C02 的新 head 必须与它们都 \\|ρ\\| < 0.7)", "",
      "| 运行 | 组 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |", "|---|---|---|---|---|---|---|---|---|---|"]
for tag, arm, h in rows:
    L.append(f"| {tag} | {arm} | {h['score']:+.2f} | {h['train']:+.2f} | {h['valid']:+.2f} | {h['hl']:g} | {h['sign']:+g} | {h['turnover']:.3f} | {h.get('rho_known', float('nan')):+.2f} | `{h['expr']}` |")
(ROOT / "research" / "coldstart_C02" / "prior_c01.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote prior_c01.md: {len(runs)} runs, {len(rows)} heads")
