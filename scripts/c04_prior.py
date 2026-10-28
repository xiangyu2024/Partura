"""C04: what Partura may know before writing hypotheses -- IN-SAMPLE only, from C01, C02 and C03 (research/coldstart_C04/PLAN.md).

Local.  Every run's own heads (train / valid only) of both arms of C01-C03, the C02 and C03 direct tests, pointers to beliefs.
Nothing from the test period is read (no RESULT.md, final*.json or ledger).  Derived from scripts/c03_prior.py.

    python scripts/c04_prior.py      -> research/coldstart_C04/prior_c04.md
"""
import glob
import json
import math
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
L = ["# C04 的先验知识:C01、C02、C03 的样本内结果(只含 train / valid;没有任何测试段数字)", "",
     "C01:A = GP 盲搜,B = Partura v1(先验 + 邻域);C02:A = GP 盲搜 + 相关度拒绝,B = Partura v2(假设直接测 + 设计初始种群 + GP 精修);"
     "C03:同 C02 的两组,奖励换成 `long_neutral`(对流动性 / 波动 / 20 日反转 / 已知族做截面中性化后的残差书)。",
     "C01、C02 的奖励是 `long`(没有中性化),它们的 head 在 C04 的奖励下分数未知,很多会掉(大多带风格暴露)。"
     "C04 的奖励在 C03 的控制变量上再加市值 `LogFloatCap`:C03 的 head 也可能部分是市值暴露。",
     "更多:C01 的 beliefs_r2/r3.md、cards_r*;C02、C03 的 hypotheses_r1.yaml、direct_r1.md、design_r1.md、beliefs_r1.md。", ""]
for study, pat in (("C01", "c01r*_*"), ("C02", "c02r*_*"), ("C03", "c03r*_*")):
    rows = []
    for p in sorted(glob.glob(str(ROOT / "episodes" / pat / "evidence.json"))):
        E = json.loads(Path(p).read_text(encoding="utf-8"))
        for arm, A in E["arms"].items():
            for h in A.get("heads") or []:
                rows.append((Path(p).parent.name, arm, h))
    rows.sort(key=lambda x: -x[2]["score"])
    L += [f"## {study} 的全部 heads(各运行内去重,{len(rows)} 个;C04 的新 head 必须与它们 \\|ρ\\| < 0.7)", "",
          "| 运行 | 组 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |", "|---|---|---|---|---|---|---|---|---|---|"]
    for tag, arm, h in rows:
        L.append(f"| {tag} | {arm} | {h['score']:+.2f} | {h['train']:+.2f} | {h['valid']:+.2f} | {h['hl']:g} | {h['sign']:+g} | {h['turnover']:.3f} | {h.get('rho_known', float('nan')):+.2f} | `{h['expr']}` |")
    L.append("")
for study in ("C02", "C03"):
    D = json.loads((ROOT / "research" / f"coldstart_{study}" / "direct_r1.json").read_text(encoding="utf-8"))
    rows = sorted(D["rows"], key=lambda r: -(r["score"] if isinstance(r.get("score"), (int, float)) and r["score"] == r["score"] else -9))
    L += [f"## {study} 的直接检验(B 组,{len(rows)} 个变体;只含 train / valid)", "",
          "| 假设 | 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 相关度拒绝 | 表达式 |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    f = lambda x: f"{x:+.2f}" if isinstance(x, (int, float)) and not math.isnan(x) else "—"
    for r in rows:
        L.append(f"| {r.get('hypothesis')} | {r.get('variant', '')} | {r.get('role', '')} | {f(r.get('score'))} | {f(r.get('train'))} | {f(r.get('valid'))} | "
                 f"{f(r.get('sign'))} | {r.get('hl', '—')} | {f(r.get('turnover'))} | {f(r.get('rho_known'))} | {'是' if r.get('rejected') else ''} | `{r.get('expr')}` |")
    L.append("")
(ROOT / "research" / "coldstart_C04").mkdir(exist_ok=True)
(ROOT / "research" / "coldstart_C04" / "prior_c04.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("wrote prior_c04.md")
