"""The guidance, for a person: research conclusions -> the four kinds of intervention on AlphaCube, with the numbers.

Local.  Reads guidance/<batch>.yaml (the rules), guidance/motif_stats_<tag>.json (the paired statistics the rules
cite), lab/findings.yaml (the conclusions they cite) and episodes/*/evidence.json (the intervention experiments).

    python scripts/guidance_report.py guidance/B01.yaml [--tag s2] [--out research/alpha_distillation/B01_reverse_guidance.md]
"""
import json
import re
import sys
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


TAG = opt("--tag", "s3")
G = yaml.safe_load((root / argv[0]).read_text(encoding="utf-8"))
M = json.loads((root / "guidance" / f"motif_stats_{TAG}.json").read_text(encoding="utf-8"))
_lab = yaml.safe_load((root / "lab" / "findings.yaml").read_text(encoding="utf-8"))
LAB = {x["id"]: x for x in (_lab if isinstance(_lab, list) else _lab.get("findings", []))}
out = root / opt("--out", f"research/alpha_distillation/{G['batch'].split('_')[0]}_reverse_guidance.md")
SECT = ("wrappers", "memory_by_window", "ablate_by_operator", "substitute_pairs", "substitute_incoming", "substitute_outgoing", "leaf_field")


def stat(a):
    if not a:
        return ""
    f = lambda x, p=False: "—" if x is None else (f"{x:.0%}" if p else f"{x:+.2f}")  # noqa: E731
    return (f"{a.get('n_live', a['n'])} 例可用 / 共 {a['n']} 例({a['factors']} 条因子):夏普变化中位 {f(a['d_median'])},明显变好 {f(a['up'], 1)}、明显变差 {f(a['down'], 1)}、"
            f"两段都升 {f(a['both'], 1)}" + (f"、废品率 {a['dead']:.0%}" if a["dead"] >= 0.2 else ""))


def ev(e):
    e = str(e)
    m = re.match(r"^(" + "|".join(SECT) + r")\.\"?(.+?)\"?(?:\s+d .*)?$", e)
    if m and m.group(2) in M.get(m.group(1), {}):
        return f"成对统计「{m.group(2)}」{stat(M[m.group(1)][m.group(2)])}"
    if e in LAB:
        return f"结论 `{e}`:{LAB[e]['claim'][:110]}{'…' if len(LAB[e]['claim']) > 110 else ''}"
    return e


def evs(r, n=3):
    return "<br>".join(ev(e) for e in r.get("evidence", [])[:n])


ST = {"implemented": "已实现", "proposed": "建议"}
L = [f"# 反向指引 AlphaCube:{G['batch'].split('_')[0]} 的研究结论怎样改变搜索", "",
     "Partura 不是 AlphaCube 的下游:研究结论在这里变成对搜索的四类干预 —— 奖励、评估、动作与子结构的先验、交给搜索的想法。"
     f"证据来自 {G['evidence_base']['factors']} 条因子、{M['n_variants']} 个打过分的变体(其中 {M['dead_rate']:.1%} 是废品)和 {len(LAB)} 条实验室结论;"
     "范围是这批种子的邻域,所以权重是先验,靠每一次带对照的干预实验去更新。机器读的版本是 `" + argv[0] + "`,做法见 `docs/reverse_guidance.md`。", "",
     "下面的「夏普变化」都是**成对**的:同一个动作套在每条因子上,变体减它自己的底座,训练段纯多头夏普;超过 ±0.3 才算数。", ""]

# ---- headline
W = M["wrappers"]
L += ["## 先说结论", "",
      f"1. **现在的奖励在给流动性倾斜付钱。**「只在成交额最低四成里选」这一个动作,不管套在哪条因子上都把纯多头夏普抬高 {W['seg_lowliq_m']['d_median']:+.2f}"
      f"({W['seg_lowliq_m']['up']:.0%} 明显变好、{W['seg_lowliq_m']['both']:.0%} 两段都升);反过来「只在成交额最高四成里选」是 {W['seg_hiliq_p']['d_median']:+.2f} / {W['seg_hiliq_m']['d_median']:+.2f}"
      f"(两个方向都试了,{W['seg_hiliq_p']['down']:.0%} / {W['seg_hiliq_m']['down']:.0%} 明显变差)。所以搜索头部才会全是成交额一族 —— 要改的是奖励(桶内选股、可交易池、对池子的边际贡献),不是再多封几个结构。",
      f"2. **对自身历史做 z 分数必须封禁。** {W['mem_zscore']['n']} 例里 {W['mem_zscore']['down']:.0%} 明显变差、没有一例两段都升,夏普中位 {W['mem_zscore']['d_median']:+.2f}。"
      f"外层的截面折叠({W['fold_mean']['d_median']:+.2f})、滚动标准差({W['mem_stddev']['d_median']:+.2f})、除以自己的历史均值({W['rel60']['d_median']:+.2f})是同一类错误:把持久的截面水平除掉了,而多头腿就在水平里。",
      f"3. **唯一「大多数时候有益、几乎不伤」的外层动作是慢记忆。** 30~60 日的均值 / 指数平均 / 线性衰减:两段都升 {W['mem_mean']['both']:.0%}~{W['mem_ema']['both']:.0%},明显变差只有 {W['mem_mean']['down']:.0%}~{W['mem_ema']['down']:.0%}。它不该靠搜索去重新发现 —— 评估时自动配上。",
      f"4. **把任意因子叠到已知族上没有用。** 三个权重 × 15 条因子,两段都升的是 {W['ov_p025']['both']:.0%} / {W['ov_p05']['both']:.0%} / {W['ov_p10']['both']:.0%}。值钱的是和池子不相关的东西融合之后的增量,所以奖励要直接量「对池子的边际贡献」。",
      f"5. **{M['dead_rate']:.0%} 的评估预算花在废品上**(门槛改算在实际交易的信号上之后;之前算在原面板上时是 10%,一半是误杀),其中有整类可以事先拒绝:截面聚合(cs_mean / cs_sum / cs_median / cs_stddev_full)当因子用 100% 是废品。", "",
      "(更正:上一版这里还写着「分母里的 +1e-6 删掉之后 7 例全部变好」。审查发现那 7 例里真正碰到 1e-6 的只有 4 例、其中 3 例判废,剩下 1 例的消融也不是干净的删除 —— 这句话没有证据,已删;对应的规则由封禁降为降权,理由只剩两条手写因子的机制分析。)", ""]

# ---- 1. reward
L += ["## 一、奖励函数", "", "| | 改什么 | 为什么 | 状态 |", "|---|---|---|---|"]
for r in G["reward"]:
    L.append(f"| {r['id'].split('_')[0]} | {r['change']} | {r['why']} | {ST.get(r['status'], r['status'])} |")
L += ["", "已实现的四种奖励在 `partura/steer.py: reward()`:`long`(原口径)、`long_tradable`(R1)、`long_bucket`(R1 + R2)、`long_marginal`(R1 + R3)、`long_screen`(把候选当筛子用:已知族排掉候选最高两成,减已知族本身);"
      "R4~R6 是它们共有的:两个方向各建一次多头书取好的、半衰期在网格上按纯多头夏普取、分数取 train 与 valid 里较差的那个。", ""]

# ---- 2. evaluation
L += ["## 二、评估方法", "", "| | 改什么 | 为什么 |", "|---|---|---|"]
for r in G["evaluation"]:
    L.append(f"| {r['id'].split('_')[0]} | {r['change']} | {r['why']} |")
L.append("")

# ---- 3. priors
L += ["## 三、动作与子结构的先验(重点)", "",
      "规则对生成器的作用是「接受-拒绝」:每棵候选树以 min(1, 权重 ÷ 最大权重) 的概率放行,封禁的永不放行 —— 生成器原来的提议分布 P 就变成 P × 权重,"
      "不需要生成器自己支持算子概率。改写在打分前做,等价的候选只评一次。", "",
      "### 3.1 证据:同一个外层动作套在 15 条因子上", "",
      "| 外层动作 | 是什么 | 例数 | 夏普变化中位 | 明显变好 | 明显变差 | 两段都升 | 与原式的秩相关 |", "|---|---|---|---|---|---|---|---|"]
NAMES = {"seg_lowliq_m": "只在成交额最低四成里按 −x 选", "seg_lowliq_p": "只在成交额最低四成里按 +x 选", "seg_hiliq_p": "只在成交额最高四成里按 +x 选", "seg_hiliq_m": "只在成交额最高四成里按 −x 选",
         "seg_xfrozen_m": "−x,把冻结盘口最重的两成排到最后", "seg_xfrozen_p": "+x,把冻结盘口最重的两成排到最后",
         "mem_ema": "cross_ema(·, 5~60)", "mem_decay_linear": "cross_decay_linear(·, 5~60)", "mem_mean": "cross_mean(·, 5~60)", "mem_max": "cross_max(·, 5~60)",
         "win": "cs_winsor(·)", "rk": "cs_rank(·)", "ov_p025": "已知族 + 0.25 × 本因子", "ov_p05": "已知族 + 0.5 × 本因子", "ov_p10": "已知族 + 1.0 × 本因子",
         "scr_xhi_p": "已知族,排掉本因子最高两成", "scr_xhi_m": "已知族,排掉本因子最低两成", "mem_min": "cross_min(·, 5~60)", "res_liq": "对成交额取秩残差", "bk_liq": "成交额分桶内排名", "res_known": "对已知族取秩残差",
         "bk_known": "已知族分桶内排名", "mem_stddev": "cross_stddev(·, 5~60)", "fold_sq": "pow_2(cs_demean(·))", "fold_rank": "abs_(cs_demean(cs_rank(·)))",
         "rel60": "除以自己的 60 日均值", "fold_mean": "abs_(cs_demean(·))", "mem_zscore": "cross_zscore(·, 5~60)"}
for k in NAMES:
    a = W.get(k)
    if a:
        p = lambda x: "—" if x is None else f"{x:.0%}"  # noqa: E731
        L.append(f"| `{k}` | {NAMES[k]} | {a['n']} | {a['d_median']:+.2f} | {p(a['up'])} | {p(a['down'])} | {p(a['both'])} | {a['rho_orig_median']:.2f} |")
L += ["", "叠加 / 筛子类(`ov_*`、`scr_*`)是和已知族比,其余是和原式比。分桶 / 残差类(`bk_*`、`res_*`)变差,说明这批因子的多头腿大半就是流动性 —— 这正是结论 1。",
      "筛子 / 分段类(根是 `cs_first_*` / `cs_last_*`)的方向是锁定的,±x 两个方向各算一行;`seg_new_*`(按上市时间分段)这一轮的读数作废 —— 分段键 93% 并列,旧算子在并列块里按股票顺序任意切,已修,等第四轮。", ""]


def rule_table(title, rows, cols):
    if not rows:
        return []
    T = ["### " + title, "", "| | 模式 | " + ("权重 | " if "w" in cols else "") + ("改成 | " if "to" in cols else "") + "为什么 | 证据 |", "|---|---|" + ("---|" if "w" in cols else "") + ("---|" if "to" in cols else "") + "---|---|"]
    for r in rows:
        pat = "`" + r["pattern"].replace("|", "∣") + "`" + (f"<br>(例外:`{r['unless'].replace('|', '∣')}`)" if r.get("unless") else "") + (f"<br>(嵌套 ≥ {r['depth_ge']} 层)" if r.get("depth_ge") else "")
        T.append(f"| {r['id'].split('_')[0]} | {pat} | " + (f"{r['w']:g} | " if "w" in cols else "") + (f"{'去掉这一层' if r.get('to') == 'operand' else r.get('to', '')} | " if "to" in cols else "") + f"{r['why']} | {evs(r)} |")
    return T + [""]


P = G["priors"]
L += rule_table("3.2 拒绝(概率 0)", [r for r in P if r["action"] == "ban"], ())
L += rule_table("3.3 降权", sorted([r for r in P if r["action"] == "weight" and r["w"] < 1], key=lambda r: r["w"]), ("w",))
L += rule_table("3.4 升权", [r for r in P if r["action"] == "weight" and r["w"] > 1], ("w",))
L += rule_table("3.5 打分前改写 / 去重(等价的候选只评一次)", [r for r in P if r["action"] in ("rewrite", "dedup_key")], ("to",))

# selected paired substitution evidence
L += ["### 3.6 换算子 / 删节点 / 换叶子的成对统计(节选)", "", "| 动作 | 例数 | 夏普变化中位 | 明显变好 | 明显变差 | 废品率 | 读法 |", "|---|---|---|---|---|---|---|"]
PICK = [("ablate_by_operator", "div", "「删掉」除法 = 只留被除数(整个分母一起没了):多数变好"),
        ("substitute_pairs", "div → mul", "除法换乘法"), ("substitute_pairs", "add → mul", "加法换乘法"),
        ("substitute_outgoing", "ts_min →", "窗口为 1 的 ts_min 换成任何东西都不变:它是恒等"), ("substitute_outgoing", "day_quantile →", "价格水平取哪个统计量无所谓"),
        ("substitute_outgoing", "pow_1_5 →", "外层幂次是乘客"), ("substitute_outgoing", "cs_demean →", "换成别的截面算子多数是废品"),
        ("substitute_outgoing", "ts_spearman →", "不可替代"), ("substitute_outgoing", "nt_ts_autocorr_s1 →", "不可替代"),
        ("substitute_incoming", "→ cs_mean", "截面聚合当因子:废品"), ("substitute_incoming", "→ ts_product", "滚动连乘:废品"),
        ("leaf_field", "Close → Low", "价格叶子互换不改因子"), ("leaf_field", "Volume → Amt", "量换额:基本不变"),
        ("leaf_field", "Amt → Volume", "额换量:变差(价格混淆)"), ("leaf_field", "Amt → in_pct", "水平换变化率:全部变差"),
        ("leaf_field", "Ret → in_pct", "收益换量的变化率:换了一个因子,少数变好")]
for sec, key, note in PICK:
    a = M.get(sec, {}).get(key)
    if a:
        p = lambda x, s=False: "—" if x is None else (f"{x:+.2f}" if s else f"{x:.0%}")  # noqa: E731
        L.append(f"| {key} | {a['n']} | {p(a['d_median'], 1)} | {p(a['up'])} | {p(a['down'])} | {a['dead']:.0%} | {note} |")
L.append("")

# ---- 4. ideas and episodes
L += ["## 四、交给 AlphaCube 短搜的想法", "",
      "以前研究一个想法只能自己写几十个表达式。现在一个想法 = 假设 + 种子 + 它所在的邻域(算子、叶子)+ 该为它付钱的奖励,"
      "`./scripts/study.sh idea <id>` 让 AlphaCube 的 GP 在这个邻域里搜一小会儿,并配一个同预算、不带干预的对照。", "",
      "| 想法 | 假设 | 种子 | 奖励 |", "|---|---|---|---|"]
for i in G["ideas"]:
    L.append(f"| `{i['id']}` | {i['hypothesis']} | " + "<br>".join(f"`{s}`" for s in i.get("seeds", [])[:3]) + ("" if i.get("seeds") else "(不限结构)") + f" | `{i['reward']}` |")
eps = sorted((root / "episodes").glob("*/evidence.json")) if (root / "episodes").is_dir() else []
eps = [e for e in eps if not e.parent.name.startswith(("smoke", "e1_"))]          # e1: the reward compared two universes -- void
if eps:
    L += ["", "### 干预实验(同一个想法的两臂只差「有没有指引」;完整的实验卡在 `episodes/<实验>/episode.md`)", "",
          "| 实验 | 奖励 | 带指引:评估 / 过线 / 最好 | 对照:评估 / 过线 / 最好 | 结论 |", "|---|---|---|---|---|"]
    for e in eps:
        E = json.loads(e.read_text(encoding="utf-8"))
        thr = float(E.get("threshold", 1.0))

        def cell(A):
            sc = sorted([c["score"] for c in A["candidates"] if c.get("score") == c.get("score")], reverse=True)
            return f"{A['scored']} / {sum(x >= thr for x in sc)} / {sc[0]:+.2f}" if sc else f"{A['scored']} / 0 / —"

        bf = e.parent / "belief.md"
        head = bf.read_text(encoding="utf-8").strip().split("\n")[0].strip("* ") if bf.is_file() else "(信念更新待写)"
        arms = E["arms"]
        L.append(f"| `{e.parent.name}` | `{E['reward']}`(过线 ≥ {thr:g}) | {cell(arms['steer']) if 'steer' in arms else '—'} | {cell(arms['control']) if 'control' in arms else '—'} | {head} |")
    L += ["", "「过线」数的是存下来的前 80 个候选里分数达到线的个数。首跑(`e1_*`)作废:那时对池子的边际奖励两边不在同一个股票池里。"]
else:
    L += ["", "(干预实验的结果出来后会列在这里。)"]
L.append("")

# ---- 5. what would go into AlphaCube proper
L += ["## 五、值得并进 AlphaCube 本体的改动(等对照实验证实后由你决定)", "",
      "现在这些都是运行时装上去的,AlphaCube 的文件没有动。", "",
      "| 改动 | 位置 | 现状 |", "|---|---|---|",
      "| 算子采样权重 | `mining/generator.py:268` `_pick`(现在是按面均匀) | Partura 运行时替换 |",
      "| 候选必须留在某个邻域 / 过指引 | `mining/generator.py:107` `acceptable` | Partura 运行时包一层 |",
      "| 奖励注册表(现在是四处写死的 if / choices) | `mining/scoring.py:510` `make_scorer`、`mining/gp.py:52`、`cli.py:330` | Partura 运行时包一层 |",
      "| 封禁的漏洞:改窗口 / 改常数的变异不查封禁 | `mining/generator.py:234`、`:246` | 未修(实测 300 次窗口变异里 67 个孩子带着被封的键) |",
      "| 封禁键只能写一层、窗口也算在键里 | `mining/generator.py:51` `one_layer_keys` | Partura 的模式匹配器可以表达多层与通配 |",
      "| 搜索内部没有 train / valid 之分 | `pipeline.py` | Partura 的奖励自己切两段、取差的那段 |",
      "| 按时间的预算、断点续跑 | `mining/gp.py:747` | 没有;短搜索用候选个数控制 |", ""]
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote {out} ({len(L)} lines)")
