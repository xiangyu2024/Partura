"""C03: what Partura may know before writing hypotheses -- IN-SAMPLE only, from C01 and C02 (research/coldstart_C03/PLAN.md).

Local.  Every run's own heads (train / valid only) of both arms of C01 and C02, the C02 direct tests, pointers to beliefs.
Nothing from the test period is read (no RESULT.md, final*.json or ledger).

    python scripts/c03_prior.py      -> research/coldstart_C03/prior_c03.md
"""
import glob
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L = ["# C03 的先验知识:C01 与 C02 的样本内结果(只含 train / valid;没有任何测试段数字)", "",
     "C01:A = GP 盲搜,B = Partura v1(先验 + 邻域);C02:A = GP 盲搜 + 相关度拒绝,B = Partura v2(假设直接测 + 设计初始种群 + GP 精修)。",
     "两个实验的奖励都是 `long`(没有中性化)。C03 换成 `long_neutral`:这些 head 在新奖励下的分数未知,很多会掉(它们大多带风格暴露)。",
     "更多:C01 的 beliefs_r2/r3.md、cards_r*;C02 的 hypotheses_r1.yaml、direct_r1.md、design_r1.md、beliefs_r1.md。", ""]
for study, pat, line in (("C01", "c01r*_*", 1.0), ("C02", "c02r*_*", 0.7)):
    rows = []
    for p in sorted(glob.glob(str(ROOT / "episodes" / pat / "evidence.json"))):
        E = json.loads(Path(p).read_text(encoding="utf-8"))
        for arm, A in E["arms"].items():
            for h in A.get("heads") or []:
                rows.append((Path(p).parent.name, arm, h))
    rows.sort(key=lambda x: -x[2]["score"])
    L += [f"## {study} 的全部 heads(各运行内去重,{len(rows)} 个;C03 的新 head 必须与它们 \\|ρ\\| < 0.7)", "",
          "| 运行 | 组 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for tag, arm, h in rows:
        L.append(f"| {tag} | {arm} | {h['score']:+.2f} | {h['train']:+.2f} | {h['valid']:+.2f} | {h['hl']:g} | {h['sign']:+g} | {h['turnover']:.3f} | {h.get('rho_known', float('nan')):+.2f} | `{h['expr']}` |")
    L.append("")
(ROOT / "research" / "coldstart_C03" / "prior_c03.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote prior_c03.md")
