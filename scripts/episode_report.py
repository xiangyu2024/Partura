"""A research episode, written down: hypothesis / intervention / control / evidence / belief update.

Local.  Reads episodes/<tag>_<idea>/evidence.json (scripts/idea_search.py) and, if present, belief.md in the same
directory (written by the researcher: what this episode changes in the guidance, and why).  Writes episode.md.

The evidence is read on more than one yardstick, because a pass / fail line set before the run can be the wrong
line (the first episodes showed it):

* scored / gate failures / live          what the arm paid for and what survived the gates;
* distinct                                candidates that are not a re-spelling of one another (canonical form of
                                          the guidance): a search that scores five spellings of one tree found one thing;
* how many clear each of several score levels, and the best and the mean of the five best distinct candidates;
* when the run measured it: distinct passers that are not the known pool.

    python scripts/episode_report.py [<episode dir name> ...]      (default: every episode with evidence)
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.steer import Guidance  # noqa: E402

root = Path(__file__).resolve().parents[1]
names = [a for a in sys.argv[1:] if not a.startswith("-")] or sorted(p.parent.name for p in (root / "episodes").glob("*/evidence.json"))
LEVELS = {"long_marginal": (0.0, 0.1, 0.2, 0.3), "long_screen": (0.0, 0.1, 0.2, 0.3)}
ARM = {"steer": "带指引", "control": "对照"}


def fin(x):
    return x is not None and x == x and abs(x) != float("inf")


for name in names:
    d = root / "episodes" / name
    E = json.loads((d / "evidence.json").read_text(encoding="utf-8"))
    G = Guidance.load(root / E.get("guidance", "guidance/B01.yaml"))
    idea, kind = E["idea"], E["reward"]
    levels = LEVELS.get(kind, (0.0, 0.3, 0.5, 1.0))
    rows, found = [], {}
    for arm, A in E["arms"].items():
        cs = [c for c in A["candidates"] if fin(c.get("score"))]
        seen, distinct = set(), []
        for c in sorted(cs, key=lambda c: -c["score"]):
            try:
                k = G.dedup_key(c["expr"])
            except ValueError:
                k = c["expr"]
            if k not in seen:
                seen.add(k)
                distinct.append(c)
        top5 = distinct[:5]
        rows.append({"arm": arm, "scored": A["scored"], "gate": A["gate_fail"], "live": A["live"], "saved": len(cs), "distinct": len(distinct),
                     "levels": [sum(c["score"] >= lv for c in distinct) for lv in levels], "best": distinct[0]["score"] if distinct else float("nan"),
                     "top5": sum(c["score"] for c in top5) / len(top5) if top5 else float("nan"), "heads": A.get("independent_distinct"),
                     "minutes": A["seconds"] / 60, "sampling": A.get("sampling") or {}})
        found[arm] = distinct[:6]
    L = [f"# 研究实验 `{name}`", "",
         f"想法 `{idea['id']}`;奖励 `{kind}`;每臂预算 {E['budget']} 个候选(种群 {E['population']},随机种子 {E['seed']});搜索只看 {E['period'][0]}–{E['period'][1]}(其中 {E['period'][2]} 起算 valid),测试段没有打开。", "",
         "## 假设", "", idea.get("hypothesis", ""), "",
         "## 干预(带指引的一臂)", "",
         f"- 种子进首代:{'、'.join('`' + s + '`' for s in idea.get('seeds', [])) or '(无)'}",
         f"- 想法里的算子采样概率 × {E.get('boost')};候选必须含这些算子之一:{'、'.join((idea.get('grammar') or {}).get('day_ops', [])) or '(不限)'}",
         f"- 每棵候选树过指引 `{E.get('guidance')}`:封禁的不放行,降权 / 升权按概率放行,等价写法只放行第一个",
         "", "## 对照", "", "同一个 GP、同一个奖励、同样的预算与随机种子、同一个算子库;不带种子、不过指引、均匀采样。", "",
         "## 证据", "",
         "| 臂 | 付费评估 | 没过门槛 | 活着的 | 互不等价的(存下来的前 80 里) | " + " | ".join(f"分数 ≥ {lv:g}" for lv in levels) + " | 最好 | 前五(互不等价)均值 | 过线且不在已知池里、互不重复 | 用时 |",
         "|---|---|---|---|---|" + "---|" * len(levels) + "---|---|---|---|"]
    for r in rows:
        L.append(f"| {ARM.get(r['arm'], r['arm'])} | {r['scored']} | {r['gate']} | {r['live']} | {r['distinct']} / {r['saved']} | " + " | ".join(str(x) for x in r["levels"])
                 + f" | {r['best']:+.2f} | {r['top5']:+.2f} | {'—' if r['heads'] is None else r['heads']} | {r['minutes']:.0f} 分 |")
    L += ["", f"分数的含义:" + {"long_marginal": "候选与已知池五五混合后的纯多头夏普减池子自己的,train 与 valid 取较差的", "long_screen": "已知族把候选最高的两成排到最后之后的纯多头夏普减已知族自己的,train 与 valid 取较差的",
                           "long_bucket": "可交易池里、成交额十档内排名之后的纯多头夏普,train 与 valid 取较差的", "long_tradable": "可交易池里的纯多头夏普,train 与 valid 取较差的",
                           "long": "纯多头夏普,train 与 valid 取较差的"}.get(kind, kind) + "。「分数 ≥」各列数的是互不等价的候选。", ""]
    for r in rows:
        if r["sampling"]:
            s = r["sampling"]
            L.append(f"带指引的一臂提出了 {s.get('proposed', 0)} 棵树:封禁 {s.get('banned', 0)}、不在想法邻域 {s.get('outside', 0)}、按权重抽掉 {s.get('thinned', 0)}、"
                     f"与已提过的等价 {s.get('equivalent', 0)}、放行 {s.get('accepted', 0)}。")
    L += ["", "## 各臂找到的(互不等价的前几个;纯多头夏普 train / valid 是奖励口径下的)", ""]
    for arm, cs in found.items():
        L += [f"**{ARM.get(arm, arm)}**", ""] + [f"- {c['score']:+.2f}(train {c['train']:+.2f} / valid {c['valid']:+.2f},半衰期 {c['hl']:g},与已知族相关 {c['rho_known']:+.2f}):`{c['expr']}`" for c in cs] + [""]
    b = d / "belief.md"
    L += ["## 信念更新", "", b.read_text(encoding="utf-8").strip() if b.is_file() else "(待写:这次实验让哪条规则的权重 / 状态变了,为什么。)", ""]
    (d / "episode.md").write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"wrote {d / 'episode.md'}")
    for r in rows:
        print(f"   {r['arm']:8s} scored {r['scored']:4d} live {r['live']:4d} distinct {r['distinct']:3d}/{r['saved']:<3d} levels {dict(zip(levels, r['levels']))} best {r['best']:+.2f} top5 {r['top5']:+.2f}")
