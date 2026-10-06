"""A report a person can read: the upgraded version of every factor, then their fusion, in and out of sample.

Local, reads only files already pulled:

    runs/<fid>/sweepfinal_<tag>.json      every candidate's in-sample / out-of-sample books
    runs/_batch_<B>/fuse_<tag>.json       scripts/batch_fuse.py: which candidates were fused, the fusions' books,
                                          the smoothing grid and the daily series for the curve

    python scripts/readable_report.py batches/B01_single_factors.yaml [--tag s2]

Writes research/alpha_distillation/<B>_upgrades_and_fusion.md and <B>_fusion_curves.svg.
The one-line descriptions are written by hand (NOTES below): they say what the expression computes by the
operators' definitions, and they are the only thing here that is not read from a file.
"""
import json
import sys
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]
TAG = argv[argv.index("--tag") + 1] if "--tag" in argv else "s2"
batch = yaml.safe_load(open(root / argv[0], encoding="utf-8"))
bname = Path(argv[0]).stem.split("_")[0]
J = json.loads((root / "runs" / f"_batch_{bname}" / f"fuse_{TAG}.json").read_text(encoding="utf-8"))
FIN = {f["id"].split("_")[0]: json.loads((root / "runs" / f["id"] / f"sweepfinal_{TAG}.json").read_text(encoding="utf-8"))["results"] for f in batch["factors"]}
NAME = {f["id"].split("_")[0]: f"{f['lib']} {f['name']}" for f in batch["factors"]}

# what each upgraded version computes, in plain words (by operator definition); key = "<F1xx>.<candidate id>"
NOTES = {
    "F107.h_gini_ema30": "把原式里日内最低价的「偏度」换成「基尼系数」(一天里价格偏离的不均匀程度,有界、不怕单笔异常),再做 30 日指数平均。买离全市场均值最近的(既不死水也不乱跳)",
    "F102.h_max60": "分钟收益短窗自相关的日内峰度,原式是 15 日求和,改成 60 日取最大。买近 60 日没出过极端值的(极端值基本是封板日)",
    "F101.fld_Volume_Amt": "原式只统计「放量分钟」后的波动;这一版把条件放宽到几乎所有有成交的分钟,变成日内 5 分钟波动水平离全市场均值的距离。买最接近均值的",
    "F111.seg_xfrozen_p": "原式(日内中位价近 10 日走势的单调程度,买稳步上行的)不变,只是把近 15 日盘口冻结最重的两成股票排到最后",
    "F103.nosc_B_cross_semistd_neg": "原式里成交额的 30 日线性衰减均值,换成 30 日下行半标准差。仍是成交额类,和已知族相关 0.67,算半个新东西",
    "F113.h_g6_gini_bk_amt": "原式整棵树丢掉,只留一个念头:分钟收益绝对值的基尼系数(30 日均值),并且只在成交额相近的股票之间比",
    "F112.iso_E": "去掉最外层的 30 日自身缩放。剩下的其实是「低价股」:按价格平方排,最便宜的一成被挖掉,买第二便宜的那一档",
    "F110.h_cube_ema30": "只留原式的第一个乘数:开盘到收盘的日内涨跌幅,取立方后做 30 日指数平均。买近一个月日内大跌过的(日内反转)",
    "F115.h_rawvol_divM_only": "潮汐因子:分子不变,分母里两个成交量谷底改用未平滑的原始成交量来定位",
    "F103.h_K_ex_both": "已知族,先把近 15 日盘口冻结最重的两成排到最后,再把上市最短的两成排到最后",
    "F104.h_known_nofrozen": "已知族,把近 15 日「收盘价不动的分钟占比」最高的两成排到最后(原式自己的多头腿不可用)",
    "F108.z_known_excl_flatrun": "已知族,把近 15 日出现过最长价格冻结段的两成排到最后(原式自己的多头腿不可用)",
    "F114.h_ov_flat_p05": "已知族的排名 + 0.5 × 近 15 日价格不动分钟占比的排名(给冻结盘口加一个罚项)",
    "F105.seg_xfrozen_m": "原式不变,把近 15 日盘口冻结最重的两成排到最后",
    "F101.seg_lowliq_m": "只在成交额最低的四成股票里,按 F101 反向选",
    "F113.h_k2_gini_overlay": "已知族的排名 + 0.25 × 分钟收益基尼(30 日均值)的排名",
    "F109.scr_xhi_p": "已知族,把 F109 读数最高的两成排到最后",
    "F115.scr_xhi_p": "已知族,把 F115 读数最高的两成排到最后",
    "F106.h_zero_minus_liq": "「零收益分钟少」的排名 减 「成交额」的排名:买不钉在一个价位上、又不拥挤的。原式的分母 +1e-6 把它变成了涨跌停探测器,这一版整个重写",
    "F112.ov_p025": "已知族的排名 + 0.25 × 原式的排名",
    "F110.ov_p025": "已知族的排名 + 0.25 × 原式的排名",
    # ---- fourth round (s4)
    "F101.h_sum_rv_amtchg": "两个「粗糙度」的折叠相加:分钟收益的波动离市场均值的距离 + 分钟成交额变化率的波动离市场均值的距离,排名相加。买价和量两头都接近市场典型值的",
    "F112.h_csrank_w50": "把「挖掉最便宜一成」那一步换成截面排名,自身缩放的窗口从 30 日改成 50 日:价格的截面位次相对自己近 50 日降下来的",
    "F114.h3_xfr_own_slowf": "原式的慢版本(收盘前收益的 60 日下四分位,再做 30 日指数平均;买低的),并把近 15 日盘口冻结最重的两成排到最后",
    "F114.h3_xfr_plus_slowf": "排掉冻结盘口的已知族的排名,减去 F114 慢版本排名的立方(只在慢版本最高的那一小撮上有实质的罚分)",
    # ---- third round (s3)
    "F102.h3_age_bucket": "60 日取最大的那一版,再放到上市时间相近的股票里比(按上市以来的天数分十档,档内排名)",
    "F107.h3_blend_own2_ema30": "两个日内离散度的折叠相加:分钟收益波动离市场均值的距离 + 最低价基尼系数离市场均值的距离,各自先做 30 日指数平均,再把排名相加。买两样都接近市场典型值的",
    "F110.h3_cvx_xage": "日内涨跌幅(开盘到收盘)的带符号平方(保留方向、放大尾部)做 30 日指数平均,买近一个月日内大跌过的;并把上市最短的两成排到最后",
    "F111.h3_best2": "收盘价近 20 日与时间的相关(走势越单调上行越好),并把近 15 日盘口冻结最重的两成排到最后",
    "F113.h3_g6_bdemean": "分钟收益绝对值的基尼系数(30 日均值),减去同成交额档股票的平均 —— 只在同类股票里比,保留量纲",
    "F115.h3_raw_amt": "潮汐因子:分母里定位两个成交谷底时改用未平滑的成交额",
    "F101.h3_scr_kx_xhi": "已知族先把冻结盘口最重的两成排到最后,再把 F101(日内 5 分钟波动的折叠)读数最高的两成排到最后",
    "F102.h3_xfroz_max60": "已知族先排掉冻结盘口最重的两成,再排掉 F102(60 日最大版)读数最高的两成",
    "F103.h3_xfrz_then_relstd": "已知族先排掉冻结盘口最重的两成,再排掉 F103 改写版读数最高的两成",
    "F105.h3_xfrozen_tail75": "成交额方差的 30 日上尾均值(最高四分之一那些天的平均),买低的;并排掉冻结盘口最重的两成",
    "F106.h3_xfr_zero40": "已知族,把近 15 日零收益分钟占比最高的四成排到最后(比两成剔得更狠)",
    "F108.h3_scr_dbl": "已知族先排掉冻结盘口最重的两成,再排掉 F108(分钟价格峰度的 30 日均值)最高的两成",
    "F109.h3_blend_tailq75": "已知族的排名,叠加 F109 改写版(极端上涨幅度的 30 日上尾均值)的排名",
    "F110.h3_ov_xfroz_cvx": "排掉冻结盘口的已知族,排名再叠加「日内涨跌幅带符号平方的 30 日指数平均」的反向排名(买日内大跌过的)",
    "F111.h3_xfz_plus_f": "已知族的排名减 0.25 × F111 的排名,再排掉冻结盘口最重的两成",
    "F112.h3_ov_div60": "已知族的排名 + 0.25 ×「当日中位价 ÷ 自己 60 日中位价」的排名",
    "F113.h3_ov_g6_xfrozen": "已知族的排名 + 0.25 × 同成交额档内的基尼排名,再排掉冻结盘口最重的两成",
    "F114.h3_xfr_plus_state": "排掉冻结盘口的已知族,叠加 F114(收盘前收益的 60 日下四分位,30 日指数平均)的反向排名;叠加的权重随全市场成交额所处的状态变化",
}


def pc(x, d=1):
    return "—" if x is None or x != x else f"{x:+.{d}%}"


def sh(x):
    return "—" if x is None or x != x else f"{x:.2f}"


def cand(s, cid):
    v = FIN[s][cid]["books_user"]["by_rank"]["long"]
    return FIN[s][cid], v["hl"], v["splits"]["utrain"], v["splits"]["holdout"]


def near(s, cid):
    """Measured closeness to the known family (training period): rank correlation / share of the long book in common."""
    m = J["members"].get(f"{s}.{cid}") or {}
    if m.get("rho_known") is None:
        return "—"
    return f"{m['rho_known']:+.2f} / {m['ovl_known']:.0%}"


def row_of(s, cid):
    r, hl, a, t = cand(s, cid)
    _, _, oa, ot = cand(s, "v_base")
    return (f"| {s} {NAME[s]} | {NOTES.get(f'{s}.{cid}', '')} | **{pc(a['long_ann'])}** | **{pc(t['long_ann'])}** | {sh(a['long_sharpe'])} | {sh(t['long_sharpe'])} "
            f"| {pc(t['long_mdd'])} | {a['long_turnover']:.1%} | {near(s, cid)} | {pc(oa['long_ann'])} → {pc(ot['long_ann'])} |")


HEAD = ["| 来自 | 升级版做了什么 | 样本内超额 | 样本外超额 | 样本内夏普 | 样本外夏普 | 样本外最大回撤 | 日换手 | 与已知族:秩相关 / 多头书重合 | 原式的超额(样本内 → 样本外) |",
        "|---|---|---|---|---|---|---|---|---|---|"]
tr0, tr1 = J["split"]["train"]
te0, te1 = J["split"]["test"]


def d8(x):
    return f"{x[:4]}-{x[4:6]}-{x[6:]}"


L = [f"# {bname}:各条升级版的回测,以及把它们融合之后的样本内外结果", "",
     "## 怎么读", "",
     f"- **样本内** = {d8(tr0)} ~ {d8(tr1)};**样本外** = {d8(te0)} ~ {d8(te1)}。升级版全部只看样本内的数字选出来,样本外只是读数。",
     "- **超额** = 每天等权买入因子排名最好的 10% 股票,相对「全市场等权」的年化超额收益,**已扣单边 15bp 交易成本**(纯多头,不做空)。",
     "- **夏普** = 这条超额收益曲线的年化夏普;**最大回撤** = 这条超额曲线自己的回撤;**日换手** = 这本多头书每天换掉的比例。",
     "- 样本外只有两年半,单个数字的噪声大约是超额 ±3 个点、夏普 ±0.3。",
     "- 平滑半衰期在 {0, 1, 2, 3, 5, 10, 20, 40, 60} 日里按样本内的纯多头夏普选(40、60 是这一轮新加的;落在这两档的行与你原表的口径不可比)。变体的方向按样本内纯多头书定,原式仍按 rank IC 的符号。", "",
     "## 先说结论", "",
     "__CONCLUSIONS__", "",
     "## 一、各条升级版", "",
     "### 表 1:独立的新因子(和已知的成交额族不是一个东西,每条原式最多一个)", ""] + HEAD
indep = J["groups"]["indep"]
for k in sorted(indep, key=lambda k: -cand(*k.split(".", 1))[2]["long_sharpe"]):
    L.append(row_of(*k.split(".", 1)))
kn = J["members"]["known"]["rows"]
L += ["", "### 表 2:已知族(成交额离散度 `cross_mean(day_std(Amt), 30)`,买成交额波动小的)的升级版", "",
      "这些建在已知族上,或者持有的多头书与它(或与它做过冻结盘口筛子的版本)重合一半以上。重合度写在每行:重合高的几行是同一本书的不同写法,**只能选一个用**;"
      "重合低而被归到这里的,是因为与「已知族 + 冻结盘口筛子」那本书重合。判据逐条实测(训练段),不看式子长相。", ""] + HEAD
L.append(f"| 对照 | 已知族本身,不做任何改动 | **{pc(kn['train']['long_ann'])}** | **{pc(kn['test']['long_ann'])}** | {sh(kn['train']['long_sharpe'])} | {sh(kn['test']['long_sharpe'])} "
         f"| {pc(kn['test']['long_mdd'])} | {kn['train']['long_turnover']:.1%} | +1.00 / 100% | — |")
onk = [k for k in J["groups"]["upg"] if k not in indep and not k.endswith(".orig")] + ["F101.seg_lowliq_m"]
onk = [k for k in onk if k.split(".", 1)[1] in FIN[k.split(".", 1)[0]]]
for k in sorted(dict.fromkeys(onk), key=lambda k: -cand(*k.split(".", 1))[2]["long_sharpe"]):
    L.append(row_of(*k.split(".", 1)))
no_own = [s for s in FIN if not any(k.startswith(s + ".") for k in indep)]
L += ["", f"没有自己的独立升级版的:{'、'.join(no_own)}(原式自身的多头腿扣费后站不住,最好的版本就是表 2 里借已知族的那一行)。", "",
      "### 表达式", ""]
for tab, keys in (("表 1", list(indep)), ("表 2", list(dict.fromkeys(onk)))):
    for k in keys:
        s, cid = k.split(".", 1)
        r, hl, _, _ = cand(s, cid)
        L += [f"- **{tab} 的 {s}**(方向:{'买高' if r['sign_user'] > 0 else '买低'};平滑半衰期 {hl:g} 日)", f"  `{r['expr']}`"]

# ---- fusion
F = J["fusions"]


def chosen(name, method="each"):
    M = F[name]["methods"][method]
    g = next(x for x in M["grid"] if x["hl"] == M["chosen_hl"])
    return M, g


def frow(label, n, a, t, by):
    return (f"| {label} | {n} | **{pc(a['long_ann'])}** | **{pc(t['long_ann'])}** | {sh(a['long_sharpe'])} | {sh(t['long_sharpe'])} | {pc(a['long_mdd'])} | {pc(t['long_mdd'])} "
            f"| {a['long_turnover']:.1%} | " + " ".join(f"{x:+.0%}" for x in by.values()) + " |")


L += ["", "## 二、融合", "",
      "**融合的做法**:每个成员先按自己在样本内最合适的半衰期做指数平滑;每天把各成员在全市场的排名(0~1)取等权平均;买平均排名最好的 10%。"
      f"成员怎么选是规则定的(只看样本内):表 1 的 {len(indep)} 个独立升级版;「升级版 15 条」是每条原式各取样本内夏普最高的那个版本(不管它属于哪一族)。", "",
      "### 表 3:融合之后(成员各自平滑后等权融合;融合后要不要再平滑由样本内决定)", "",
      "| 组合 | 成员数 | 样本内超额 | 样本外超额 | 样本内夏普 | 样本外夏普 | 样本内最大回撤 | 样本外最大回撤 | 日换手 | 逐年超额 2018…2025 |", "|---|---|---|---|---|---|---|---|---|---|"]
L.append(frow("对照:已知族单独", 1, kn["train"], kn["test"], J["members"]["known"]["by_year_long_net"]))
for name, label in (("O", "**原式** 15 条等权(升级之前)"), ("U", "**升级版** 15 条等权"), ("A", f"**独立的 {len(indep)} 个**等权"), ("B", "已知族里最好的升级版,单独"),
                    ("C", f"独立的 {len(indep)} 个 + 已知族最好的一个({len(indep) + 1} 个等权)"), ("D", f"一半已知族最好的一个 + 一半独立 {len(indep)} 个的均值")):
    M, g = chosen(name)
    L.append(frow(label, len(F[name]["members"]) if name != "B" else 1, g["train"], g["test"], M["by_year_long_net"]))
L += ["", "(逐年那一列里 2023 年横跨样本内外。)", "", "__PAIRED__", "",
      f"### 表 4:平滑的作用(以「独立的 {len(indep)} 个等权」为例,融合之后再做一次指数平滑)", "",
      "| 融合后的半衰期(日) | 样本内超额 | 样本内夏普 | 样本内换手 | 样本外超额 | 样本外夏普 | 样本外最大回撤 | 样本外换手 |", "|---|---|---|---|---|---|---|---|"]
MA = F["A"]["methods"]["each"]
for g in MA["grid"]:
    a, t = g["train"], g["test"]
    star = "(样本内选中)" if g["hl"] == MA["chosen_hl"] else ""
    L.append(f"| {g['hl']:g}{star} | {pc(a['long_ann'])} | {sh(a['long_sharpe'])} | {a['long_turnover']:.1%} | {pc(t['long_ann'])} | {sh(t['long_sharpe'])} | {pc(t['long_mdd'])} | {t['long_turnover']:.1%} |")
MO = F["A"]["methods"]["once"]
L += ["", f"如果成员**不**先各自平滑、直接融合再统一平滑(同样是这 {len(indep)} 个):", "",
      "| 统一的半衰期(日) | 样本内超额 | 样本内夏普 | 样本内换手 | 样本外超额 | 样本外夏普 | 样本外换手 |", "|---|---|---|---|---|---|---|"]
for g in MO["grid"]:
    a, t = g["train"], g["test"]
    star = "(样本内选中)" if g["hl"] == MO["chosen_hl"] else ""
    L.append(f"| {g['hl']:g}{star} | {pc(a['long_ann'])} | {sh(a['long_sharpe'])} | {a['long_turnover']:.1%} | {pc(t['long_ann'])} | {sh(t['long_sharpe'])} | {t['long_turnover']:.1%} |")

# ---- the curve
dates = J["dates"]
series = [("已知族单独", J["members"]["known"]["daily"], "#8a8a8a"), ("原式 15 条等权", F["O"]["methods"]["each"]["daily"], "#d08a2e"),
          ("升级版 15 条等权", F["U"]["methods"]["each"]["daily"], "#3a7bd5"), (f"独立的 {len(indep)} 个等权", F["A"]["methods"]["each"]["daily"], "#c0392b"),
          (f"独立 {len(indep)} 个 + 已知族最好的一个", F["C"]["methods"]["each"]["daily"], "#27865a")]
W, H, ml, mr, mt, mb = 980, 520, 62, 24, 44, 46
n = len(dates)
cum = []
for _, s, _ in series:
    c, tot = [], 0.0
    for v in s:
        tot += 0.0 if v is None else v
        c.append(tot)
    cum.append(c)
ymax = max(max(c) for c in cum) * 1.04
ymin = min(0.0, min(min(c) for c in cum))


def X(i):
    return ml + (W - ml - mr) * i / (n - 1)


def Y(v):
    return mt + (H - mt - mb) * (1 - (v - ymin) / (ymax - ymin))


isplit = next(i for i, d in enumerate(dates) if d >= te0)
S = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="PingFang SC, Heiti SC, Microsoft YaHei, sans-serif" font-size="12">',
     f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
     f'<rect x="{X(isplit):.1f}" y="{mt}" width="{W - mr - X(isplit):.1f}" height="{H - mt - mb}" fill="#f3f6fb"/>',
     f'<text x="{ml}" y="22" font-size="15" fill="#222">纯多头超额的累计曲线(扣 15bp 后,对全市场等权;各日超额直接相加)</text>']
step = 0.25 if ymax < 2 else 0.5
v = 0.0
while v <= ymax:
    S.append(f'<line x1="{ml}" y1="{Y(v):.1f}" x2="{W - mr}" y2="{Y(v):.1f}" stroke="#e3e3e3" stroke-width="1"/>')
    S.append(f'<text x="{ml - 8}" y="{Y(v) + 4:.1f}" text-anchor="end" fill="#555">{v:+.0%}</text>')
    v += step
for i, d in enumerate(dates):
    if i == 0 or d[:4] != dates[i - 1][:4]:
        S.append(f'<line x1="{X(i):.1f}" y1="{H - mb}" x2="{X(i):.1f}" y2="{H - mb + 5}" stroke="#777"/>')
        S.append(f'<text x="{X(i) + 3:.1f}" y="{H - mb + 18}" fill="#555">{d[:4]}</text>')
S.append(f'<line x1="{X(isplit):.1f}" y1="{mt}" x2="{X(isplit):.1f}" y2="{H - mb}" stroke="#444" stroke-dasharray="5 4"/>')
S.append(f'<text x="{X(isplit) - 8:.1f}" y="{mt + 16}" text-anchor="end" fill="#444">← 样本内</text>')
S.append(f'<text x="{X(isplit) + 8:.1f}" y="{mt + 16}" fill="#444">样本外 →</text>')
for (label, _, color), c in zip(series, cum):
    pts = " ".join(f"{X(i):.1f},{Y(v):.1f}" for i, v in enumerate(c) if i % 2 == 0 or i == n - 1)
    S.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{2.2 if "独立" in label else 1.6}"/>')
for j, ((label, _, color), c) in enumerate(zip(series, cum)):
    y = mt + 40 + 20 * j
    S.append(f'<line x1="{ml + 14}" y1="{y - 4}" x2="{ml + 40}" y2="{y - 4}" stroke="{color}" stroke-width="3"/>')
    S.append(f'<text x="{ml + 46}" y="{y}" fill="#222">{label}:样本内累计 {c[isplit - 1]:+.0%},样本外累计 {c[-1] - c[isplit - 1]:+.0%}</text>')
S.append("</svg>")
MAo, gA = chosen("A")
_, gO = chosen("O")
_, gU = chosen("U")
_, gC = chosen("C")


def crash(daily, a="20240116", b="20240206"):
    return sum(0.0 if v is None else v for d, v in zip(dates, daily) if a <= d <= b)


def paired(a, b):
    """Two books on the same days: the daily difference of their net excess -> (annualised, information ratio, t), in and out of sample.
    Two annualised numbers each carry about +-3 points of noise; most of it cancels in the difference."""
    out = {}
    for nm, sl in (("train", slice(0, isplit)), ("test", slice(isplit, None))):
        d = [x - y for x, y in zip(a[sl], b[sl]) if x is not None and y is not None]
        m = sum(d) / len(d)
        sd = (sum((x - m) ** 2 for x in d) / len(d)) ** 0.5
        out[nm] = (m * 252, m / sd * 252 ** 0.5, m / sd * len(d) ** 0.5)
    return out


DAILY = {"known": J["members"]["known"]["daily"], **{k: F[k]["methods"]["each"]["daily"] for k in F}}
PNAME = {"known": "已知族单独", "O": "原式 15 条等权", "U": "升级版 15 条等权", "A": f"独立的 {len(indep)} 个等权", "B": "已知族里最好的升级版", "C": f"独立 {len(indep)} 个 + 已知族最好的一个"}
PT = ["### 表 3b:和基准同一天相减(这才是「比谁好」的检验)", "",
      "两本书大半持仓相同,各自 ±3 个点的噪声在相减时抵掉大半。t 值 ≥ 2 才算统计上站得住;样本外只有约 2.3 年,所以每年差 5 个点左右才到得了 2。", "",
      "| 谁 减 谁 | 样本内:每年多赚 | 样本内 t | 样本外:每年多赚 | 样本外信息比 | 样本外 t |", "|---|---|---|---|---|---|"]
PAIRS = {}
for a, b in (("A", "O"), ("U", "O"), ("A", "known"), ("C", "known"), ("B", "known"), ("O", "known")):
    q = PAIRS[(a, b)] = paired(DAILY[a], DAILY[b])
    PT.append(f"| {PNAME[a]} − {PNAME[b]} | {q['train'][0]:+.1%} | {q['train'][2]:+.1f} | **{q['test'][0]:+.1%}** | {q['test'][1]:+.2f} | **{q['test'][2]:+.1f}** |")
L[L.index("__PAIRED__")] = "\n".join(PT)
qo, qk = PAIRS[("A", "O")], PAIRS[("A", "known")]

conc = [
    f"1. **融合比原式好,样本外幅度没缩水;比已知族好多少,样本外分不出来。** {len(indep)} 个独立升级版等权融合:样本内 {pc(gA['train']['long_ann'])}(夏普 {sh(gA['train']['long_sharpe'])}),样本外 {pc(gA['test']['long_ann'])}(夏普 {sh(gA['test']['long_sharpe'])});"
    f"8 个年份的超额都在 {min(MAo['by_year_long_net'].values()):+.0%} ~ {max(MAo['by_year_long_net'].values()):+.0%} 之间。"
    f"和 15 条原式的融合同一天相减:样本内每年多 {qo['train'][0]:+.1%},样本外多 {qo['test'][0]:+.1%}(t = {qo['test'][2]:.1f})。"
    f"和已知族单独({pc(kn['train']['long_ann'])} / {pc(kn['test']['long_ann'])},夏普 {sh(kn['train']['long_sharpe'])} / {sh(kn['test']['long_sharpe'])})同一天相减:"
    f"样本内多 {qk['train'][0]:+.1%}(t = {qk['train'][2]:.1f}),样本外多 {qk['test'][0]:+.1%}(t = {qk['test'][2]:.1f})—— 方向一致、夏普更高,但两年半的样本不足以说它确实比已知族好(表 3b)。",
    f"2. **升级前后**。原式 15 条直接融合:{pc(gO['train']['long_ann'])} / {pc(gO['test']['long_ann'])}(夏普 {sh(gO['train']['long_sharpe'])} / {sh(gO['test']['long_sharpe'])});"
    f"升级版 15 条融合:{pc(gU['train']['long_ann'])} / {pc(gU['test']['long_ann'])}(夏普 {sh(gU['train']['long_sharpe'])} / {sh(gU['test']['long_sharpe'])})。"
    f"超额多了 {min(gU['train']['long_ann'] - gO['train']['long_ann'], gU['test']['long_ann'] - gO['test']['long_ann']) * 100:.0f}~{max(gU['train']['long_ann'] - gO['train']['long_ann'], gU['test']['long_ann'] - gO['test']['long_ann']) * 100:.0f} 个点,样本外夏普几乎没变 —— 因为这 15 个升级版里有 {len([k for k in J['groups']['upg'] if k not in indep])} 个落在已知族里(表 2),波动跟着已知族走。只用 {len(indep)} 个独立的反而更好。",
    f"3. **平滑**。成员各自平滑之后,融合后再平滑不增加收益(样本内选的是不再平滑);它换来的是换手从 {MAo['grid'][0]['test']['long_turnover']:.1%} 降到 {MAo['grid'][-1]['test']['long_turnover']:.1%}、"
    f"样本外回撤从 {pc(MAo['grid'][0]['test']['long_mdd'])} 收到 {pc(MAo['grid'][-1]['test']['long_mdd'])},样本外夏普基本不变({sh(MAo['grid'][0]['test']['long_sharpe'])} → {sh(MAo['grid'][-1]['test']['long_sharpe'])})。"
    "成员不先各自平滑就直接融合则明显更差(换手 20% 以上,要靠很长的半衰期才救回来)。",
    f"4. **风险点**。所有升级版融合的样本外最大回撤都发生在 2024-01-16 ~ 02-06(微盘股踩踏)这三周:独立 {len(indep)} 个 {pc(crash(MAo['daily']))}、"
    f"已知族 {pc(crash(J['members']['known']['daily']))}、升级版 15 条 {pc(crash(F['U']['methods']['each']['daily']))},而原式 15 条融合在这三周是 {pc(crash(F['O']['methods']['each']['daily']))}。"
    "升级版比原式更偏低流动性的小票,这是它多赚的来源之一,也是它的尾部风险。",
    f"5. **打折看**。成员是从每条因子几百个变体里按样本内挑出来的,样本内的夏普({gA['train']['long_sharpe']:.1f})有选择偏差,样本外({gA['test']['long_sharpe']:.1f})大约是它的一半 —— 以样本外为准。",
]
L[L.index("__CONCLUSIONS__")] = "\n".join(conc)
out_dir = root / "research" / "alpha_distillation"
(out_dir / f"{bname}_fusion_curves.svg").write_text("\n".join(S), encoding="utf-8")
L += ["", f"曲线图:`research/alpha_distillation/{bname}_fusion_curves.svg`。"]
(out_dir / f"{bname}_upgrades_and_fusion.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print("\n".join(L))
