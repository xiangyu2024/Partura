"""The two-level method on other pools: stage 1 (test period) and stage 2 (carried to the forward segment), read by
the rules written beforehand in research/two_level/PLAN.md.

Local.  Reads runs/_batch_B01/two_level_stage1.json, runs/_forward/two_level_{check,forward,hl_diag}_<end>.json and
runs/_forward/members_<end>.json; writes research/two_level/RESULT.md and, for the charts,
runs/_batch_B01/two_level_series_<end>.json (the layout scripts/best_books_chart.py reads).

    python scripts/two_level_report.py [--end 20260916]
"""
import json
import math
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]
END = argv[argv.index("--end") + 1] if "--end" in argv else "20260916"
S1 = json.loads((root / "runs" / "_batch_B01" / "two_level_stage1.json").read_text(encoding="utf-8"))
F = json.loads((root / "runs" / "_forward" / f"two_level_forward_{END}.json").read_text(encoding="utf-8"))
CHK = F["check"]
DIAG = json.loads((root / "runs" / "_forward" / f"two_level_hl_diag_{END}.json").read_text(encoding="utf-8"))
M = json.loads((root / "runs" / "_forward" / f"members_{END}.json").read_text(encoding="utf-8"))
O1, dates1 = S1["objects"], S1["dates"]
dates = F["dates"]
ix = lambda d: next(i for i, x in enumerate(dates) if x >= d)      # noqa: E731
i_te, i_fw, n = ix("20230808"), ix("20260101"), len(dates)
SEG = {"insample": (0, i_te), "test": (i_te, i_fw), "forward": (i_fw, n), "oos": (i_te, n), "all": (0, n)}
ORDER = ["手写库冠军", "挖掘冠军", "C_Q", "C_LQ", "C_MQ", "C_LM", "C_LMQ"]
WHAT = {"手写库冠军": "AlphaCube 手写库冠军(现成)", "挖掘冠军": "AlphaCube 挖掘冠军(现成)", "C_Q": "只用 Partura 的产出", "C_LQ": "手写库 ∪ Partura",
        "C_MQ": "挖掘库 ∪ Partura", "C_LM": "手写库 ∪ 挖掘库(对照,不含 Partura)", "C_LMQ": "手写库 ∪ 挖掘库 ∪ Partura"}
POOLS = {"C_Q": ("Q", 2730, 2729, 723, 214), "C_LQ": ("LQ", 4097, 4012, 1158, 319), "C_MQ": ("MQ", 6914, 6900, 2263, 432), "C_LM": ("LM", 5593, 5496, 2038, 335),
         "C_LMQ": ("LMQ", 8276, 8178, 2675, 520)}                     # pool, factors, healthy, clusters, clusters past the quality gate (logs/server/_pool_*.log)
BLOCKS = {"C_LQ": [("手写库", 0, 1392), ("Partura", 1392, 4097)], "C_MQ": [("挖掘库", 0, 4206), ("Partura", 4206, 6914)],
          "C_LM": [("手写库", 0, 1392), ("挖掘库", 1392, 5593)], "C_LMQ": [("手写库", 0, 1392), ("挖掘库", 1392, 5593), ("Partura", 5593, 8276)]}   # manifest blocks of the merged pools
MAIN = [("C_LQ", "手写库冠军"), ("C_MQ", "挖掘冠军"), ("C_LMQ", "C_LM")]
p1 = lambda x: f"{100 * x:+.1f}%"      # noqa: E731


def pstat(a, b, key, lo, hi, src):
    d = [x - y for x, y in zip(src[a][key][lo:hi], src[b][key][lo:hi]) if x is not None and y is not None and x == x and y == y]
    m = sum(d) / len(d)
    sd = (sum((x - m) ** 2 for x in d) / len(d)) ** 0.5
    return {"ann": m * 252, "ir": m / sd * math.sqrt(252), "t": m / sd * math.sqrt(len(d)), "n": len(d)}


def total(r):
    f = [x for x in r if x is not None and x == x]
    m = sum(f) / len(f)
    sd = (sum((x - m) ** 2 for x in f) / len(f)) ** 0.5
    nav, peak, mdd = 1.0, 1.0, 0.0
    for x in f:
        nav *= 1 + x
        peak = max(peak, nav)
        mdd = min(mdd, nav / peak - 1)
    return {"cagr": nav ** (252 / len(f)) - 1, "vol": sd * math.sqrt(252), "sharpe": m / sd * math.sqrt(252), "mdd": mdd, "nav": nav, "days": len(f)}


def verdict2(p):
    fw, oos = p["forward"], p["oos"]
    if oos["t"] >= 2:
        return "成立"
    if fw["ann"] > 0 and oos["t"] >= 1:
        return "方向一致、仍不够"
    if fw["ann"] < 0:
        return "没有延续"
    return "证据弱"


def verdict1(t):
    return "变好了" if t >= 2 else ("方向对、证据不够" if t >= 1 else ("没有" if t >= 0 else "变差"))


L = []
A = L.append
A(f"# 两层合成用到别的因子池:结果(读到 {END[:4]}-{END[4:6]}-{END[6:]})")
A("")
A("规则见 `PLAN.md`(两个阶段的判读都写在出数之前)。本文件由 `scripts/two_level_report.py` 生成,数字全部来自")
A(f"`runs/_batch_B01/two_level_stage1.json`、`runs/_forward/two_level_forward_{END}.json`、`two_level_check_{END}.json`、`two_level_hl_diag_{END}.json`。")
A("")
A("尺子:全市场十分位书、扣单边 15bp;方向与半衰期只用样本内(到 2023-08-07)定;纯多头 = 每天等权买排名最好的 10%,净超额 = 减去当天有信号有标签的股票的等权收益。")
A("样本内 = 2018-01 ~ 2023-08-07(权重在这段拟合,是拟合值);测试段 = 2023-08-08 ~ 2025-12-31;前推段 = 2026-01-05 ~ " + f"{END[:4]}-{END[4:6]}-{END[6:]}" + f"({SEG['forward'][1] - SEG['forward'][0]} 天);合并段 = 测试段 + 前推段。")
A("")

# ---------------------------------------------------------------- pools and membership
A("## 池子与入选")
A("")
A("| 信号 | 池子 | 因子数 | 健康 | 聚成的族 | 过门槛的族 | 入选 100 族的成员数 | 成员来源 |")
A("|---|---|---|---|---|---|---|---|")
src_note = {}
for nm in ORDER[2:]:
    pool, nf, nh, nc, ng = POOLS[nm]
    fams = M["champions"][nm]["families"]
    if nm in BLOCKS:
        cnt = {b[0]: 0 for b in BLOCKS[nm]}
        famhas = {b[0]: 0 for b in BLOCKS[nm]}
        pure = {b[0]: 0 for b in BLOCKS[nm]}
        for f in fams:
            who = [next(b[0] for b in BLOCKS[nm] if b[1] <= m["i"] < b[2]) for m in f]
            for w in who:
                cnt[w] += 1
            for w in set(who):
                famhas[w] += 1
            if len(set(who)) == 1:
                pure[who[0]] += 1
        tot = sum(cnt.values())
        src = ";".join(f"{k} {v} 个({100 * v / tot:.0f}%)、出现在 {famhas[k]} 族、独占 {pure[k]} 族" for k, v in cnt.items())
        src_note[nm] = (cnt, famhas, pure, tot)
    else:
        src = "全部来自 Partura"
    A(f"| {nm} | {WHAT[nm]} | {nf} | {nh} | {nc} | {ng} | {sum(len(f) for f in fams)} | {src} |")
A("")
A("两个现成冠军:手写库冠军 1392 个因子 → 100 族 744 个成员;挖掘冠军 4206 个因子 → 100 族 886 个成员。")
A("")

# ---------------------------------------------------------------- stage 1
A("## 第一阶段:测试段(存档的信号,原视窗)")
A("")
A("| 信号 | 多空 hl | 多空 夏普(年化):样本内 → **测试** | 纯多头 hl | 纯多头 净超额 / 超额夏普:样本内 → **测试** | 测试段超额回撤 | 测试段纯多头换手 |")
A("|---|---|---|---|---|---|---|")
for nm in ORDER:
    o = O1[nm]
    ls, lo = o["rows_ls"], o["rows_long"]
    A(f"| {nm} | {o['hl_ls']:g} | {ls['utrain']['ls_sharpe']:.2f}({p1(ls['utrain']['ls_ann'])})→ **{ls['holdout']['ls_sharpe']:.2f}({p1(ls['holdout']['ls_ann'])})** | {o['hl']:g} | "
      f"{p1(lo['utrain']['long_ann'])} / {lo['utrain']['long_sharpe']:.2f} → **{p1(lo['holdout']['long_ann'])} / {lo['holdout']['long_sharpe']:.2f}** | {p1(lo['holdout']['long_mdd'])} | {100 * lo['holdout']['long_turnover']:.1f}% |")
A("")
A("成对差(同一天相减,测试段;纯多头看逐日净超额,多空看逐日净收益):")
A("")
A("| 比较 | 纯多头 成对差(年化) | t | 多空 成对差 | t | 按规则 |")
A("|---|---|---|---|---|---|")
t1 = (1359, len(dates1))
P1 = {}
for a, b in MAIN + [("C_Q", "手写库冠军"), ("C_Q", "挖掘冠军"), ("C_LM", "手写库冠军"), ("C_LM", "挖掘冠军"), ("挖掘冠军", "手写库冠军")]:
    lo, ls = pstat(a, b, "excess", *t1, O1), pstat(a, b, "ls", *t1, O1)
    P1[(a, b)] = lo
    main = (a, b) in MAIN
    A(f"| {'**' if main else ''}{a} − {b}{'**' if main else ''} | {100 * lo['ann']:+.1f} 点 | {lo['t']:+.2f} | {100 * ls['ann']:+.1f} 点 | {ls['t']:+.2f} | {verdict1(lo['t']) if main else '(描述)'} |")
A("")
A("第一阶段的读法:测试段对 Partura 的产出不干净(后几轮的假设是看过前几轮测试段读数之后写的),所以这一段只当筛选。")
A("")

# ---------------------------------------------------------------- stage 2: check
A("## 第二阶段:延到前推段")
A("")
A("### 先核对(只用到 2025-12-31 的数据)")
A("")
A("| 信号 | 族 / 成员(缺) | 重建对存档 逐日秩相关 均值(最小) | 测试段纯多头净超额 重建 / 存档 | 多空夏普 重建 / 存档 | 样本内选出的半衰期 存档 → 重建 | 结果 |")
A("|---|---|---|---|---|---|---|")
for nm in ORDER:
    c = CHK[nm]
    hl = f"{DIAG[nm]['stored']['hl_long']:g} → {DIAG[nm]['rebuilt']['hl_long']:g}" if nm in DIAG else "20 → 20" if nm == "手写库冠军" else "10 → 10"
    A(f"| {nm} | {c['families']} / {c['members']}({c['members_missing']}) | {c['rank_corr_mean']:.4f}({c['rank_corr_min']:.4f}) | {p1(c['test_long_ann'][0])} / {p1(c['test_long_ann'][1])} | "
      f"{c['test_ls_sharpe'][0]:.2f} / {c['test_ls_sharpe'][1]:.2f} | {hl} | {'过' if c['pass'] else '**不过**'} |")
A("")
bad = [nm for nm in ORDER if not CHK[nm]["pass"]]
if bad:
    A(f"**{'、'.join(bad)} 没过核对**,按规则不读前推段,涉及它的成对比较也不出。原因(`scripts/two_level_hl_diag.py`,只用到 2025 年底的数据):")
    A("")
    A("| 信号 | 存档:样本内纯多头夏普(hl 5 / 10 / 20)→ 选中 | 重建:同上 → 选中 | 测试段纯多头净超额(hl 5 / 10 / 20,存档) | 同一个半衰期下 重建 − 存档(点) |")
    A("|---|---|---|---|---|")
    for nm in ORDER[2:]:
        d = DIAG[nm]
        f = lambda v: " / ".join(f"{v['insample_long_sharpe'][k]:.3f}" for k in ("5", "10", "20")) + f" → {v['hl_long']:g}"      # noqa: E731
        A(f"| {nm} | {f(d['stored'])} | {f(d['rebuilt'])} | " + " / ".join(p1(d["stored"]["test"][k]["long_ann"]) for k in ("5", "10", "20")) + " | "
          + " / ".join(f"{d['same_hl_diff_points'][k]:+.2f}" for k in ("5", "10", "20")) + " |")
    A("")
    A("- 重建的信号和存档的信号是同一个东西:半衰期相同时,测试段纯多头净超额只差 0.3 个点以内(C_LMQ 是 0.02 ~ 0.08 个点)。")
    A("- 没过是因为核对时**重新选了半衰期**:样本内两个候选几乎打平(C_LMQ 的 hl 5 和 hl 10 只差 0.004 ~ 0.011 夏普),浮点量级的差别就让选择换了位置;")
    A("  五个新信号里有三个换了(C_Q 10→20、C_MQ 20→10、C_LMQ 10→5),前两个碰巧还在 1 个点的容差里。")
    A("- **这本身是一条要记住的读数**:样本内分不出高下的半衰期,在测试段上能差 1 ~ 3 个点(C_LMQ:hl 5 / 10 / 20 = "
      + " / ".join(p1(DIAG["C_LMQ"]["stored"]["test"][k]["long_ann"]) for k in ("5", "10", "20")) + ")。所以这些合成信号之间 1 ~ 2 个点的纯多头差距,落在「选哪个半衰期」的抖动里。")
    A("- 以后的核对应当固定用存档信号的半衰期(这一条是核对设计的毛病,不是信号的毛病)。本次不事后改规则:C_LMQ 不读。它在测试段上对 C_LM 本来就是 "
      + f"{100 * P1[('C_LMQ', 'C_LM')]['ann']:+.1f} 个点(t {P1[('C_LMQ', 'C_LM')]['t']:+.2f}),合并段 t ≥ 2 在算术上已经够不着,读了也不会改变结论。")
    A("")

# ---------------------------------------------------------------- stage 2: levels
SIG = F["signals"]
READ = [nm for nm in ORDER if nm in SIG]
A("### 各信号的读数")
A("")
A("纯多头(净超额 / 超额夏普):")
A("")
A("| 信号 | hl | 样本内 | 测试段 | **前推段** | **合并段** | 合并段超额回撤 | 换手 |")
A("|---|---|---|---|---|---|---|---|")
for nm in READ:
    s = SIG[nm]["long"]
    A(f"| {nm} | {SIG[nm]['hl_long']:g} | " + " | ".join(("**" if k in ("forward", "oos") else "") + f"{p1(s[k]['long_ann'])} / {s[k]['long_sharpe']:.2f}" + ("**" if k in ("forward", "oos") else "")
                                                       for k in ("insample", "test", "forward", "oos")) + f" | {p1(s['oos']['long_mdd'])} | {100 * s['oos']['long_turnover']:.1f}% |")
A("")
A("多空(夏普(年化)):")
A("")
A("| 信号 | hl | 样本内 | 测试段 | **前推段** | **合并段** | 合并段回撤 |")
A("|---|---|---|---|---|---|---|")
for nm in READ:
    s = SIG[nm]["ls"]
    A(f"| {nm} | {SIG[nm]['hl_ls']:g} | " + " | ".join(("**" if k in ("forward", "oos") else "") + f"{s[k]['ls_sharpe']:.2f}({p1(s[k]['ls_ann'])})" + ("**" if k in ("forward", "oos") else "")
                                                     for k in ("insample", "test", "forward", "oos")) + f" | {p1(s['oos']['ls_mdd'])} |")
A("")
A("纯多头的**全部收益**(净超额 + 全市场等权,复利;不是只看超额):")
A("")
A("| 信号 | 测试段 年化 / 夏普 / 最大回撤 | 前推段(未年化的区间收益)/ 最大回撤 | 合并段 年化 / 夏普 / 最大回撤 | 2018 起净值(含样本内的拟合段) |")
A("|---|---|---|---|---|")
SER = F["series"]
TOT = {}
for nm in READ + ["全市场等权"]:
    key = "total" if nm != "全市场等权" else "bench"
    r = SER[nm if nm != "全市场等权" else READ[0]][key]
    TOT[nm] = {k: total(r[a:b]) for k, (a, b) in SEG.items()}
    t = TOT[nm]
    fwd_ret = t["forward"]["nav"] - 1
    A(f"| {nm} | {p1(t['test']['cagr'])} / {t['test']['sharpe']:.2f} / {p1(t['test']['mdd'])} | {p1(fwd_ret)} / {p1(t['forward']['mdd'])} | "
      f"{p1(t['oos']['cagr'])} / {t['oos']['sharpe']:.2f} / {p1(t['oos']['mdd'])} | {t['all']['nav']:.1f} 倍 |")
A("")
yrs = sorted({d[:4] for d in dates})
A("逐年全部收益(" + "、".join(READ[:2] + ["C_LQ"]) + " 与全市场等权):")
A("")
A("| | " + " | ".join(yrs) + " |")
A("|---|" + "---|" * len(yrs))
for nm in READ[:2] + (["C_LQ"] if "C_LQ" in READ else []) + ["全市场等权"]:
    key = "total" if nm != "全市场等权" else "bench"
    r = SER[nm if nm != "全市场等权" else READ[0]][key]
    cells = []
    for y in yrs:
        nav = 1.0
        for i, d in enumerate(dates):
            if d[:4] == y and r[i] is not None:
                nav *= 1 + r[i]
        cells.append(f"{100 * (nav - 1):+.0f}%")
    A(f"| {nm} | " + " | ".join(cells) + " |")
A(f"\n({yrs[-1]} 年只到 {dates[-1][4:6]}-{dates[-1][6:]}。)")
A("")

# ---------------------------------------------------------------- stage 2: paired
A("### 成对差与判读")
A("")
A("纯多头逐日净超额,同一天相减(年化的点数;括号里是 t):")
A("")
A("| 比较 | 测试段 | 前推段 | 合并段 | 多空的合并段成对差 | 按规则 |")
A("|---|---|---|---|---|---|")
PR = F["paired"]
for a, b in MAIN + [("C_Q", "手写库冠军"), ("C_Q", "挖掘冠军"), ("C_LM", "手写库冠军"), ("C_LM", "挖掘冠军"), ("挖掘冠军", "手写库冠军")]:
    k = f"{a}-{b}"
    main = (a, b) in MAIN
    if k not in PR:
        A(f"| {'**' if main else ''}{a} − {b}{'**' if main else ''} | (测试段,存档信号){100 * P1[(a, b)]['ann']:+.1f}(t {P1[(a, b)]['t']:+.1f}) | 不读 | 不读 | 不读 | {a if not CHK[a]['pass'] else b} 没过核对,不出 |")
        continue
    e, s = PR[k]["excess"], PR[k]["ls"]
    A(f"| {'**' if main else ''}{a} − {b}{'**' if main else ''} | " + " | ".join(f"{100 * e[x]['ann']:+.1f}(t {e[x]['t']:+.1f})" for x in ("test", "forward", "oos"))
      + f" | {100 * s['oos']['ann']:+.1f}(t {s['oos']['t']:+.1f}) | {'**' + verdict2(e) + '**' if main else '(描述)'} |")
A("")

# ---------------------------------------------------------------- best
best_ls = max(READ, key=lambda nm: SIG[nm]["ls"]["oos"]["ls_sharpe"])
best_lo = max(READ, key=lambda nm: SIG[nm]["long"]["oos"]["long_ann"])
best_sh = max(READ, key=lambda nm: SIG[nm]["long"]["oos"]["long_sharpe"])
fw_lo = max(READ, key=lambda nm: SIG[nm]["long"]["forward"]["long_ann"])
fw_ls = max(READ, key=lambda nm: SIG[nm]["ls"]["forward"]["ls_sharpe"])
A("### 「最好的」(按事先的规则:从读到的信号里按合并段各报一个,并写明是挑出来的)")
A("")
A(f"- 合并段多空夏普最高:**{best_ls}**({SIG[best_ls]['ls']['oos']['ls_sharpe']:.2f},年化 {p1(SIG[best_ls]['ls']['oos']['ls_ann'])})。")
A(f"- 合并段纯多头净超额最高:**{best_lo}**({p1(SIG[best_lo]['long']['oos']['long_ann'])},超额夏普 {SIG[best_lo]['long']['oos']['long_sharpe']:.2f});"
  f"合并段纯多头超额夏普最高:**{best_sh}**({SIG[best_sh]['long']['oos']['long_sharpe']:.2f},净超额 {p1(SIG[best_sh]['long']['oos']['long_ann'])})。")
A(f"- 这是从 {len(READ)} 个里挑的。只看前推段({SEG['forward'][1] - SEG['forward'][0]} 天,不作结论):纯多头净超额最高的是 {fw_lo}({p1(SIG[fw_lo]['long']['forward']['long_ann'])}),多空夏普最高的是 {fw_ls}({SIG[fw_ls]['ls']['forward']['ls_sharpe']:.2f})。")
for b in ("手写库冠军", "挖掘冠军"):
    k = f"{best_lo}-{b}"
    if k in PR:
        e, s = PR[k]["excess"]["oos"], PR[k]["ls"]["oos"]
        A(f"- {best_lo} 对 {b} 的合并段成对差:纯多头 {100 * e['ann']:+.1f} 个点(t {e['t']:+.1f}),多空 {100 * s['ann']:+.1f} 个点(t {s['t']:+.1f})—— 分不出高下。")
A("")

# ---------------------------------------------------------------- conclusions (every number is read from the data above)
def pr(a, b):
    e = PR[f"{a}-{b}"]["excess"]
    return f"测试段 {100 * e['test']['ann']:+.1f} 个点(t {e['test']['t']:+.1f})、前推段 {100 * e['forward']['ann']:+.1f}(t {e['forward']['t']:+.1f})、合并段 {100 * e['oos']['ann']:+.1f}(t {e['oos']['t']:+.1f})"


def lv(nm, seg):
    s = SIG[nm]["long"][seg]
    return f"{p1(s['long_ann'])} / {s['long_sharpe']:.2f}"


C = ["## 结论", ""]
C.append("1. **把 Partura 的信号加进池子,没有让两层合成变好。** 主判据的三对(纯多头逐日净超额,同一天相减):")
for a, b in MAIN:
    k = f"{a}-{b}"
    if k in PR:
        C.append(f"   - {a} − {b}:{pr(a, b)} → **{verdict2(PR[k]['excess'])}**。")
    else:
        C.append(f"   - {a} − {b}:测试段就是 {100 * P1[(a, b)]['ann']:+.1f} 个点(t {P1[(a, b)]['t']:+.1f});{a} 没过核对,按规则不读前推段(原因见下,是核对设计的毛病)。")
C.append(f"2. **不含 Partura 的对照是同一个样子。** 把手写库和挖掘库并起来(C_LM):对手写库冠军 {pr('C_LM', '手写库冠军')};对挖掘冠军 {pr('C_LM', '挖掘冠军')}。")
C.append("   「池子并大一点,测试段好看两个点、前推段还回去」不是 Partura 特有的,所以测试段上那两个点不能当成增益。")
c, fh, pu, tot = src_note["C_LQ"]
c2, fh2, pu2, tot2 = src_note["C_LM"]
C.append(f"3. **按训练段适应度选族,会偏向搜出来的池子。** C_LQ 的 100 族里有 {pu['Partura']} 族全是 Partura 的成员(手写库只占成员的 {100 * c['手写库'] / tot:.0f}%);"
         f"C_LM 里有 {pu2['挖掘库']} 族全是挖掘库的。")
C.append(f"   这些池子本身就是在同一段时间(到 2023-08-07)上按表现筛出来的,训练段适应度天然偏高:样本内的拟合值跟着涨(手写库冠军 {lv('手写库冠军', 'insample')} → C_LQ {lv('C_LQ', 'insample')}),"
         f"前推段反而低(手写库冠军 {lv('手写库冠军', 'forward')} → C_LQ {lv('C_LQ', 'forward')})。这是解释,不是已经证明的因果。")
C.append(f"4. **两个现成冠军在 2026 年站住了**(对它们来说前推段是干净的:选族和权重都只用到 2023-08-07):纯多头净超额 / 超额夏普,手写库冠军 测试段 {lv('手写库冠军', 'test')} → 前推段 **{lv('手写库冠军', 'forward')}**;"
         f"挖掘冠军 {lv('挖掘冠军', 'test')} → **{lv('挖掘冠军', 'forward')}**。")
C.append(f"   多空夏普降了:手写库冠军 {SIG['手写库冠军']['ls']['test']['ls_sharpe']:.2f} → {SIG['手写库冠军']['ls']['forward']['ls_sharpe']:.2f},挖掘冠军 {SIG['挖掘冠军']['ls']['test']['ls_sharpe']:.2f} → {SIG['挖掘冠军']['ls']['forward']['ls_sharpe']:.2f}。"
         f"2026 年(到 {dates[-1][4:6]}-{dates[-1][6:]})全部收益:手写库冠军 {p1(TOT['手写库冠军']['forward']['nav'] - 1)}、挖掘冠军 {p1(TOT['挖掘冠军']['forward']['nav'] - 1)},全市场等权 {p1(TOT['全市场等权']['forward']['nav'] - 1)}。")
C.append(f"5. **只用 Partura 的产出(C_Q)**:测试段和两个冠军差不多({lv('C_Q', 'test')},多空 {SIG['C_Q']['ls']['test']['ls_sharpe']:.2f}),前推段明显弱({lv('C_Q', 'forward')},多空 {SIG['C_Q']['ls']['forward']['ls_sharpe']:.2f})。事先的预期是「单独不如两个冠军」,前推段上是这样。")
e, s_ = PR[f"{best_lo}-手写库冠军"]["excess"]["oos"], PR[f"{best_lo}-手写库冠军"]["ls"]["oos"]
C.append(f"6. **「最好的」没有实质换人。** 合并段上名义最高的是 {best_lo}(多空夏普 {SIG[best_ls]['ls']['oos']['ls_sharpe']:.2f},纯多头净超额 {p1(SIG[best_lo]['long']['oos']['long_ann'])});"
         f"它对手写库冠军的成对差只有 {100 * e['ann']:+.1f} 个点(t {e['t']:+.1f}),分不出高下,而且是从 {len(READ)} 个里挑的。")
C.append(f"   纯多头超额夏普最高的仍是{best_sh}({SIG[best_sh]['long']['oos']['long_sharpe']:.2f});只看 2026 年,{fw_lo}在纯多头和多空上都是最高的。稳妥的说法:**手写库冠军和挖掘冠军并列,加料的版本没有超过它们。**")
C += ["", "### 对「反向指引」意味着什么", "",
      "- 不要指望「把搜出来的变体并进池子」带来增益;池子并大带来的测试段改善到前推段就没了(读到前推段的三个并集 C_LQ、C_MQ、C_LM 都是)。",
      "- 值得单独检验的一条评估规则(还只是假设,要先写规则再跑):选族的适应度不要用整段训练期,而是留出其中靠后的一段(例如 2022-01 ~ 2023-08)只用来给族排序,",
      "  这样在前段上被筛选过的池子就占不到便宜。检验方式:同样五个池子重建一遍,只看前推段的成对差。",
      "- 比较合成信号时要固定半衰期(或在打平的几个里取平均):样本内分不出高下的半衰期在样本外能差 1 ~ 3 个点,比我们想分辨的差距还大。", ""]
i0 = L.index("## 池子与入选")
L[i0:i0] = C
(root / "research" / "two_level" / "RESULT.md").write_text("\n".join(L) + "\n", encoding="utf-8")

# ---------------------------------------------------------------- series for the charts
objs = {}
for nm in READ:
    o1 = O1[nm]
    objs[nm] = {**{k: SER[nm][k] for k in ("ls", "total", "bench", "excess")}, "long_turnover": SIG[nm]["long"]["oos"]["long_turnover"], "ls_turnover": o1["ls_turnover"],
                "names_held": o1["names_held"], "universe": o1["universe"]}
(root / "runs" / "_batch_B01" / f"two_level_series_{END}.json").write_text(json.dumps({"dates": dates, "objects": objs}, ensure_ascii=False), encoding="utf-8")
(root / "runs" / "_forward" / f"two_level_summary_{END}.json").write_text(json.dumps({
    "end": END, "read": READ, "not_read": bad, "best": {"ls_oos": best_ls, "long_ann_oos": best_lo, "long_sharpe_oos": best_sh, "long_ann_forward": fw_lo, "ls_forward": fw_ls},
    "main": {f"{a}-{b}": (verdict2(PR[f"{a}-{b}"]["excess"]) if f"{a}-{b}" in PR else "not read") for a, b in MAIN},
    "stage1_main": {f"{a}-{b}": {"ann": P1[(a, b)]["ann"], "t": P1[(a, b)]["t"], "verdict": verdict1(P1[(a, b)]["t"])} for a, b in MAIN},
    "total": TOT, "sources": {k: {"members": v[0], "families_with": v[1], "families_only": v[2]} for k, v in src_note.items()}}, ensure_ascii=False, indent=1), encoding="utf-8")
print("\n".join(L))
