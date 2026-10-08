"""K002_daily_fields: the result file and its charts, from the one out-of-sample read (scripts/group_final.py).

Local.  Reads runs/K002_daily_fields/group_final_<tag>.json (the read, with per-day net-excess series), and
runs/_forward/two_level_forward_20260916.json (the two existing champions' series and the equal-weight universe return,
for the comparisons and the total-return view).  Writes studies/K002_daily_fields/RESULT_tables.md (tables only; the
conclusions are written by hand in RESULT.md) and three SVG charts next to it.

Everything marked 事后 is a description computed after the read from series that were already read by rule; it is not
part of the pre-registered verdicts.

    python scripts/k002_report.py [--tag s1]
"""
import json
import math
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]
TAG = argv[argv.index("--tag") + 1] if "--tag" in argv else "s1"
FID = "K002_daily_fields"
G = json.loads((root / "runs" / FID / f"group_final_{TAG}.json").read_text(encoding="utf-8"))
TL = json.loads((root / "runs" / "_forward" / "two_level_forward_20260916.json").read_text(encoding="utf-8"))
out_dir = root / "studies" / FID
R, P, V, S = G["results"], G["paired"], G["verdicts"], G["series"]
dates = G["dates"]["utrain"] + G["dates"]["holdout"] + G["dates"]["forward"]
n_in, n_te, n_fw = len(G["dates"]["utrain"]), len(G["dates"]["holdout"]), len(G["dates"]["forward"])
assert dates == TL["dates"], "the two reads are not on the same days"
SEG = {"utrain": (0, n_in), "holdout": (n_in, n_in + n_te), "forward": (n_in + n_te, len(dates)), "oos": (n_in, len(dates))}
BENCH = TL["series"]["手写库冠军"]["bench"]                       # the equal-weight universe (names with a signal and a label)
pct = lambda x, nd=1: "—" if x is None or x != x else f"{100 * x:+.{nd}f}%"      # noqa: E731


def ser(i, conv="fitted"):
    s = S[i][conv]
    return s["utrain"] + s["holdout"] + s["forward"]


def stat(x):
    f = [v for v in x if v is not None and v == v]
    if len(f) < 20:
        return {"ann": float("nan"), "sharpe": float("nan"), "mdd": float("nan"), "n": len(f)}
    m = sum(f) / len(f)
    sd = (sum((v - m) ** 2 for v in f) / len(f)) ** 0.5
    eq = peak = mdd = 0.0
    for v in f:
        eq += v
        peak = max(peak, eq)
        mdd = min(mdd, eq - peak)
    return {"ann": m * 252, "sharpe": m / sd * math.sqrt(252) if sd > 0 else float("nan"), "mdd": mdd, "n": len(f)}


def pair(a, b):
    d = [x - y for x, y in zip(a, b) if x is not None and y is not None and x == x and y == y]
    m = sum(d) / len(d)
    sd = (sum((v - m) ** 2 for v in d) / len(d)) ** 0.5
    return {"ann": m * 252, "t": m / sd * math.sqrt(len(d)) if sd > 0 else float("nan"), "n": len(d)}


def corr(a, b):
    z = [(x, y) for x, y in zip(a, b) if x is not None and y is not None and x == x and y == y]
    ma, mb = sum(x for x, _ in z) / len(z), sum(y for _, y in z) / len(z)
    va, vb = sum((x - ma) ** 2 for x, _ in z), sum((y - mb) ** 2 for _, y in z)
    return sum((x - ma) * (y - mb) for x, y in z) / math.sqrt(va * vb)


def total(excess, lo, hi):
    nav = peak = 1.0
    mdd, rs = 0.0, []
    for e, b in zip(excess[lo:hi], BENCH[lo:hi]):
        if e is None or b is None or e != e or b != b:
            continue
        r = e + b
        rs.append(r)
        nav *= 1 + r
        peak = max(peak, nav)
        mdd = min(mdd, nav / peak - 1)
    m = sum(rs) / len(rs)
    sd = (sum((v - m) ** 2 for v in rs) / len(rs)) ** 0.5
    return {"cagr": nav ** (252 / len(rs)) - 1, "ret": nav - 1, "sharpe": m / sd * math.sqrt(252), "mdd": mdd, "nav": nav}


def row(i, conv="fitted"):
    b = R[i]["conv"][conv]["books"]
    return " | ".join(f"{pct(b[p]['long_ann'])} / {b[p]['long_sharpe']:+.2f}" for p in ("utrain", "holdout", "forward", "oos"))


def pv(ref, i, conv="fitted"):
    if ref not in P or i not in P[ref]:
        return None
    return P[ref][i][conv]


def fp(p, per="oos"):
    if not p:
        return "—"
    if p[per]["ann"] is None or p[per]["t"] is None:
        return "逐日相同"                                          # the two books are the same book on every day of the period
    return f"{100 * p[per]['ann']:+.1f}(t {p[per]['t']:+.1f})"


NAME = {"k_known": "已知族", "k_known_xfrozen": "已知族 + 通用冻结筛子", "a_size": "小流通市值", "a_tsize": "小总市值", "a_turn20": "低换手率(20 日)", "a_amt20": "低成交额(20 日)",
        "a_known_in_size": "已知族,同流通市值档内", "a_size_in_known": "小市值,同已知族档内", "a_known_in_turn": "已知族,同换手率档内", "a_size_plus_known": "小市值 + 已知族(排名相加)",
        "e_main_only": "已知族,只买 10% 涨跌幅的板", "e_wide_only": "已知族,只买 20% 涨跌幅的板", "e_xage1y": "已知族,剔上市不足一年的"}
L = []
A = L.append
A(f"# K002 的读数表(由 `scripts/k002_report.py` 从 `runs/{FID}/group_final_{TAG}.json` 生成;结论在 `RESULT.md`)")
A("")
A("纯多头净超额 / 超额夏普(扣单边 15bp);样本内 2018-01 ~ 2023-08-07,测试段 2023-08-08 ~ 2025-12-31,前推段 2026-01-05 ~ 2026-09-16,合并段 = 后两段。半衰期按规则在样本内选(另一种读法:固定 10)。")
A("")
A("## 尺子")
A("")
A("| 尺子 | 是什么 | 样本内 | 测试段 | 前推段 | **合并段** | 合并段(固定半衰期 10) | 减已知族:合并段 | 减小流通市值:合并段 | 和小流通市值的秩相关 / 多头书重合 |")
A("|---|---|---|---|---|---|---|---|---|---|")
for i in ("k_known", "k_known_xfrozen", "a_tsize", "a_size_plus_known", "a_size", "a_amt20", "a_known_in_turn", "a_known_in_size", "a_size_in_known", "a_turn20", "e_wide_only", "e_main_only", "e_xage1y"):
    b = R[i]["conv"]
    cells = row(i).split(" | ")
    fx = b["fixed"]["books"]["oos"]
    ex = R[i]["exposure"]
    A(f"| `{i}` | {NAME[i]} | {cells[0]} | {cells[1]} | {cells[2]} | **{cells[3]}** | {pct(fx['long_ann'])} / {fx['long_sharpe']:+.2f} | {fp(pv('k_known', i)) if i != 'k_known' else '—'} | "
      f"{fp(pv('a_size', i)) if i != 'a_size' else '—'} | {ex['rank_corr_size']:+.2f} / {ex['book_overlap_size']:.2f} |")
A("")
A("## 按规则挑出来的 16 个假设")
A("")
A("| 组 | id | 类型 | 对谁判 | 样本内 | 测试段 | 前推段 | **合并段** | 成对差:测试 / 前推 / **合并**(点,t) | 固定半衰期下的合并段成对差 | 判读 | 水平判据 |")
A("|---|---|---|---|---|---|---|---|---|---|---|---|")
GT = {"b_": "B 拿掉市值", "c_": "C 换手率写法", "d_": "D 新信息", "e_": "E 筛子"}
picks = [i for i in R if R[i]["role"] in ("standalone", "modification")]
for i in picks:
    v, ref = V[i], V[i]["ref"]
    cells = row(i).split(" | ")
    p, px = pv(ref, i), pv(ref, i, "fixed")
    lv = v["final_level"]
    A(f"| {GT[R[i]['group']]} | `{i}` | {'独立' if R[i]['role'] == 'standalone' else '修改型'} | `{ref}` | {cells[0]} | {cells[1]} | {cells[2]} | **{cells[3]}** | "
      f"{fp(p, 'holdout')} / {fp(p, 'forward')} / **{fp(p)}** | {fp(px)} | **{v['final']}** | {'' if not lv else ('有' if lv['remains'] else '无') + ('(临界)' if lv['edge'] else '')} |")
A("")
A("表达式:")
A("")
for i in picks:
    A(f"- `{i}` = `{R[i]['expr']}`")
A("")
A("## 孪生(父 − 孪生 = 日频字段的边际贡献)与载体")
A("")
A("| 父假设 | 孪生 / 载体 | 它自己的合并段 | 父 − 它:合并段(点,t;拟合 / 固定) |")
A("|---|---|---|---|")
for i in picks:
    for kind, other in (("孪生", R[i].get("twin")), ("载体", R[i].get("base"))):
        if other and other in R and other not in ("k_known",):
            A(f"| `{i}` | {kind} `{other}` | {row(other).split(' | ')[3]} | {fp(pv(other, i))} / {fp(pv(other, i, 'fixed'))} |")
A("")

# ---------------------------------------------------------------- by year
A("## 逐年(纯多头净超额,年化;拟合半衰期)")
A("")
ys = sorted(R["k_known"]["conv"]["fitted"]["by_year_long_net"])
A("| | " + " | ".join(ys) + " |")
A("|---|" + "---|" * len(ys))
YR = ["k_known", "a_tsize", "a_size", "a_known_in_size", "b_fold_zs_sum_size", "b_fuse5_in_size", "e_xlimup10"]
for i in YR:
    by = R[i]["conv"]["fitted"]["by_year_long_net"]
    A(f"| `{i}` | " + " | ".join(pct(by.get(y), 0) for y in ys) + " |")
A(f"\n(2023 年跨样本内与测试段;{ys[-1]} 年只到 {dates[-1][4:6]}-{dates[-1][6:]}。)")
A("")

# ---------------------------------------------------------------- post-hoc descriptions
E = {i: ser(i) for i in ("k_known", "a_tsize", "a_size", "a_known_in_size", "b_fold_zs_sum_size", "b_fuse5_in_size", "e_xlimup10", "a_size_plus_known")}
CH = {"手写库冠军": TL["series"]["手写库冠军"]["excess"], "挖掘冠军": TL["series"]["挖掘冠军"]["excess"]}
lo, hi = SEG["oos"]
A("## 事后的描述(不在事先的判读里;用的都是已经按规则读过的逐日序列)")
A("")
A("合并段上逐日净超额的相关:")
A("")
names = ["k_known", "a_tsize", "b_fold_zs_sum_size", "手写库冠军", "挖掘冠军"]
allS = {**E, **CH}
A("| | " + " | ".join(f"`{x}`" for x in names) + " |")
A("|---|" + "---|" * len(names))
for a in names:
    A(f"| `{a}` | " + " | ".join("1" if a == b else f"{corr(allS[a][lo:hi], allS[b][lo:hi]):+.2f}" for b in names) + " |")
A("")
A("和两个现成冠军比(合并段;成对差是同一天相减):")
A("")
A("| 对象 | 合并段 净超额 / 夏普 / 超额回撤 | 减手写库冠军(点,t) | 减挖掘冠军(点,t) |")
A("|---|---|---|---|")
for a in ("手写库冠军", "挖掘冠军", "a_tsize", "b_fold_zs_sum_size", "k_known"):
    st = stat(allS[a][lo:hi])
    cmp_ = [("—" if a == c else f"{100 * pair(allS[a][lo:hi], allS[c][lo:hi])['ann']:+.1f}(t {pair(allS[a][lo:hi], allS[c][lo:hi])['t']:+.1f})") for c in ("手写库冠军", "挖掘冠军")]
    A(f"| `{a}` | {pct(st['ann'])} / {st['sharpe']:+.2f} / {pct(st['mdd'])} | {cmp_[0]} | {cmp_[1]} |")
A("")
A("各拿一半资金的组合(逐日净超额取平均;没有事先登记,只当描述):")
A("")
A("| 组合 | 样本内 | 测试段 | 前推段 | 合并段 净超额 / 夏普 / 超额回撤 |")
A("|---|---|---|---|---|")
for a, b in (("b_fold_zs_sum_size", "a_tsize"), ("b_fold_zs_sum_size", "k_known"), ("b_fold_zs_sum_size", "手写库冠军"), ("a_tsize", "手写库冠军")):
    mix = [None if (x is None or y is None or x != x or y != y) else 0.5 * (x + y) for x, y in zip(allS[a], allS[b])]
    cs = [stat(mix[SEG[p][0]:SEG[p][1]]) for p in ("utrain", "holdout", "forward", "oos")]
    A(f"| `{a}` + `{b}` | " + " | ".join(f"{pct(c['ann'])} / {c['sharpe']:+.2f}" for c in cs[:3]) + f" | {pct(cs[3]['ann'])} / {cs[3]['sharpe']:+.2f} / {pct(cs[3]['mdd'])} |")
A("")
A("全部收益(净超额 + 全市场等权,复利;全市场等权取自冠军那次读数的同一口径,各信号的可买范围略有出入):")
A("")
A("| 对象 | 测试段 年化 / 夏普 / 最大回撤 | 2026 年至今 / 最大回撤 | 合并段 年化 / 夏普 / 最大回撤 |")
A("|---|---|---|---|")
for a in ("a_tsize", "b_fold_zs_sum_size", "k_known", "手写库冠军"):
    t = {p: total(allS[a], *SEG[p]) for p in ("holdout", "forward", "oos")}
    A(f"| `{a}` | {pct(t['holdout']['cagr'])} / {t['holdout']['sharpe']:.2f} / {pct(t['holdout']['mdd'])} | {pct(t['forward']['ret'])} / {pct(t['forward']['mdd'])} | "
      f"{pct(t['oos']['cagr'])} / {t['oos']['sharpe']:.2f} / {pct(t['oos']['mdd'])} |")
bt = {p: total([0.0] * len(dates), *SEG[p]) for p in ("holdout", "forward", "oos")}
A(f"| 全市场等权 | {pct(bt['holdout']['cagr'])} / {bt['holdout']['sharpe']:.2f} / {pct(bt['holdout']['mdd'])} | {pct(bt['forward']['ret'])} / {pct(bt['forward']['mdd'])} | "
  f"{pct(bt['oos']['cagr'])} / {bt['oos']['sharpe']:.2f} / {pct(bt['oos']['mdd'])} |")
A("")
(out_dir / "RESULT_tables.md").write_text("\n".join(L) + "\n", encoding="utf-8")


# ---------------------------------------------------------------- charts (plain SVG)
def chart(path, title, sub, lines, yfmt, cumulative=True, legend_w=560):
    W, H, ml, mr, mt, mb = 1000, 540, 70, 26, 56, 50
    n = len(dates)
    X = lambda k: ml + (W - ml - mr) * k / (n - 1)          # noqa: E731
    curves = []
    for name, color, vals, dash in lines:
        c, s = [], 0.0
        for v in vals:
            s += 0.0 if (v is None or v != v) else v
            c.append(s)
        curves.append((name, color, c, dash))
    hi_ = max(max(c) for _, _, c, _ in curves)
    lo_ = min(min(c) for _, _, c, _ in curves)
    span = hi_ - lo_
    step = next(s for s in (0.02, 0.05, 0.1, 0.25, 0.5, 1.0) if span / s <= 9)
    t0 = math.floor(lo_ / step) * step
    ticks = [t0 + k * step for k in range(int((hi_ * 1.38 - t0) / step) + 2)]
    Y = lambda v: H - mb - (H - mt - mb) * (v - ticks[0]) / (ticks[-1] - ticks[0])      # noqa: E731
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="-apple-system, PingFang SC, Helvetica, Arial, sans-serif" font-size="13">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<rect x="{X(n_in):.1f}" y="{mt}" width="{X(n_in + n_te) - X(n_in):.1f}" height="{H - mt - mb}" fill="#f1f5fb"/>',
         f'<rect x="{X(n_in + n_te):.1f}" y="{mt}" width="{W - mr - X(n_in + n_te):.1f}" height="{H - mt - mb}" fill="#fdf3e3"/>',
         f'<text x="{ml}" y="24" font-size="17" font-weight="600" fill="#111">{title}</text>', f'<text x="{ml}" y="43" fill="#555">{sub}</text>',
         f'<text x="{(X(0) + X(n_in)) / 2:.1f}" y="{H - mb - 8}" text-anchor="middle" fill="#666">样本内</text>',
         f'<text x="{(X(n_in) + X(n_in + n_te)) / 2:.1f}" y="{H - mb - 8}" text-anchor="middle" fill="#3b5b8c">测试段</text>',
         f'<text x="{W - mr - 4}" y="{H - mb - 8}" text-anchor="end" fill="#9a6a15">前推段(2026)</text>']
    for t in ticks:
        o.append(f'<line x1="{ml}" y1="{Y(t):.1f}" x2="{W - mr}" y2="{Y(t):.1f}" stroke="{"#bbbbbb" if abs(t) < 1e-9 else "#e6e6e6"}"/>')
        o.append(f'<text x="{ml - 8}" y="{Y(t) + 4:.1f}" text-anchor="end" fill="#555">{yfmt(t)}</text>')
    for y in sorted({d[:4] for d in dates}):
        k = next(j for j, d in enumerate(dates) if d[:4] == y)
        o.append(f'<line x1="{X(k):.1f}" y1="{H - mb}" x2="{X(k):.1f}" y2="{H - mb + 5}" stroke="#888"/>')
        o.append(f'<text x="{X(k) + 3:.1f}" y="{H - mb + 20}" fill="#555">{y}</text>')
    o.append(f'<line x1="{X(n_in):.1f}" y1="{mt}" x2="{X(n_in):.1f}" y2="{H - mb}" stroke="#444" stroke-dasharray="5 4"/>')
    o.append(f'<rect x="{ml}" y="{mt}" width="{W - ml - mr}" height="{H - mt - mb}" fill="none" stroke="#999"/>')
    for name, color, c, dash in curves:
        pts = " ".join(f"{X(k):.1f},{Y(v):.1f}" for k, v in enumerate(c))
        o.append(f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="2"{" stroke-dasharray=" + chr(34) + dash + chr(34) if dash else ""} stroke-linejoin="round"/>')
    for j, (name, color, c, dash) in enumerate(curves):
        y = mt + 22 + 20 * j
        o.append(f'<line x1="{ml + 14}" y1="{y - 4}" x2="{ml + 42}" y2="{y - 4}" stroke="{color}" stroke-width="3"{" stroke-dasharray=" + chr(34) + dash + chr(34) if dash else ""}/>')
        o.append(f'<text x="{ml + 48}" y="{y}" fill="#222">{name}</text>')
    o.append("</svg>")
    path.write_text("\n".join(o), encoding="utf-8")


def lab(i, name):
    b = R[i]["conv"]["fitted"]["books"]
    return f"{name}:样本内 {pct(b['utrain']['long_ann'])} / {b['utrain']['long_sharpe']:.2f};合并段 {pct(b['oos']['long_ann'])} / {b['oos']['long_sharpe']:.2f}"


chart(out_dir / "K002_excess_rulers.svg", "市值之内和市值之外:纯多头的累计净超额(扣 15bp)", "纵轴 = 逐日净超额相加;图例里是 净超额 / 超额夏普。蓝底 = 测试段,橙底 = 2026 年的前推段",
      [(lab("a_tsize", "小总市值"), "#c0392b", E["a_tsize"], ""), (lab("k_known", "已知族"), "#1f5fbf", E["k_known"], ""),
       (lab("b_fold_zs_sum_size", "同市值档内的典型性(市值中性)"), "#27865a", E["b_fold_zs_sum_size"], ""),
       (lab("a_size", "小流通市值"), "#b7791f", E["a_size"], "6 4"), (lab("a_known_in_size", "已知族,同市值档内"), "#7f8c8d", E["a_known_in_size"], "6 4")],
      lambda t: f"{t:.0%}")
d_scr = [None if (x is None or y is None or x != x or y != y) else x - y for x, y in zip(E["e_xlimup10"], E["k_known"])]
p_ = pv("k_known", "e_xlimup10")
chart(out_dir / "K002_limitup_screen.svg", "剔掉近 10 日涨停过的票:这本书减已知族那本书(逐日净超额之差的累计)",
      f"样本内每年 {100 * p_['utrain']['ann']:+.1f} 个点(t {p_['utrain']['t']:+.1f});测试段 {100 * p_['holdout']['ann']:+.1f}(t {p_['holdout']['t']:+.1f});"
      f"前推段 {100 * p_['forward']['ann']:+.1f}(t {p_['forward']['t']:+.1f});合并段 {100 * p_['oos']['ann']:+.1f}(t {p_['oos']['t']:+.1f})",
      [("e_xlimup10 − k_known", "#27865a", d_scr, "")], lambda t: f"{t:+.0%}")
# total return, log scale is not needed for a three-year-plus view of two curves: plot cumulative log NAV
tot = lambda i: [None if (e is None or b is None or e != e or b != b) else math.log1p(e + b) for e, b in zip(allS[i], BENCH)]      # noqa: E731
t_ts, t_fd, t_b = total(allS["a_tsize"], 0, len(dates)), total(allS["b_fold_zs_sum_size"], 0, len(dates)), total([0.0] * len(dates), 0, len(dates))
chart(out_dir / "K002_total_return.svg", "纯多头的全部收益(净超额 + 全市场等权;不是只看超额)", "纵轴 = 净值的自然对数(0 = 起点;0.69 = 翻倍;1.39 = 4 倍;2.08 = 8 倍)",
      [(f"小总市值:2018 年起净值 {t_ts['nav']:.1f} 倍,最大回撤 {pct(t_ts['mdd'])}", "#c0392b", tot("a_tsize"), ""),
       (f"同市值档内的典型性:{t_fd['nav']:.1f} 倍,最大回撤 {pct(t_fd['mdd'])}", "#27865a", tot("b_fold_zs_sum_size"), ""),
       (f"全市场等权:{t_b['nav']:.1f} 倍,最大回撤 {pct(t_b['mdd'])}", "#8a8a8a", [None if b is None else math.log1p(b) for b in BENCH], "")],
      lambda t: f"{t:.1f}")
print("\n".join(L))
