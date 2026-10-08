"""Two pictures of the best books so far: a long/short one, and a pure long one as TOTAL return (not excess).

Local.  Reads runs/_batch_<B>/book_series_<tag>.json (scripts/book_series.py) and writes two SVG files and a small
JSON of the statistics shown.  No plotting library: plain SVG.

    python scripts/best_books_chart.py [--batch B01] [--tag s4] [--ls F104.sub_A_sqrt@ls,fusion:C] [--long fusion:A]
"""
import json
import math
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


BATCH, TAG = opt("--batch", "B01"), opt("--tag", "s4")
LS = opt("--ls", "F104.sub_A_sqrt@ls,fusion:C").split(",")
LONG = opt("--long", "fusion:A")
S = json.loads((root / "runs" / f"_batch_{BATCH}" / opt("--series", f"book_series_{TAG}.json")).read_text(encoding="utf-8"))
dates, O = S["dates"], S["objects"]
# --forward <forward_read json>: the objects that were on the forward segment's reading list (fusion:X) get their series
# from that read, which runs to the store's last day; anything else keeps its series and simply ends where it ends
if opt("--forward"):
    FR = json.loads((root / opt("--forward")).read_text(encoding="utf-8"))
    pad = len(FR["dates"]) - len(dates)
    assert FR["dates"][:len(dates)] == dates, "the forward read does not start on the same days"
    for o, d in O.items():
        nm = o.split(":")[1] if o.startswith("fusion:") else None
        for k in ("ls", "total", "bench", "excess"):
            d[k] = FR["series"][nm][k] if nm in FR.get("series", {}) else d[k] + [None] * pad
        d["ends"] = len(FR["dates"]) if nm in FR.get("series", {}) else len(dates)
    dates = FR["dates"]
SPLIT = "20230808"
isplit = next(i for i, d in enumerate(dates) if d >= SPLIT)
ifw = next((i for i, d in enumerate(dates) if d >= "20260101"), len(dates))          # the forward segment, when the series has it
NAME = {"trainto/champion_signal_buyable": "AlphaCube 挖掘冠军(4206 个挖掘因子两层合成)", "champion_signal_buyable": "AlphaCube 挖掘冠军(旧选族)",
        "legacy_signal": "AlphaCube 手写库冠军(1392 个手写因子两层合成)", "trainto/legacy_signal": "AlphaCube 手写库冠军",
        "手写库冠军": "AlphaCube 手写库冠军(1392 个手写因子两层合成)", "挖掘冠军": "AlphaCube 挖掘冠军(4206 个挖掘因子两层合成)",
        "C_LQ": "手写库 + Partura 信号的两层合成(C_LQ)", "C_MQ": "挖掘库 + Partura 信号的两层合成(C_MQ)", "C_LM": "手写库 + 挖掘库的两层合成(C_LM)", "C_Q": "只用 Partura 信号的两层合成(C_Q)",
        "fusion:A": "12 个独立升级版的等权融合", "fusion:C": "独立升级版 + 已知族头名的融合", "fusion:D": "一半已知族头名 + 一半独立升级版",
        "F104.sub_A_sqrt@ls": "单因子 F104 升级版(日内成交额峰度)", "F104.sub_A_sqrt@long": "单因子 F104 升级版(日内成交额峰度)"}


def clean(v):
    return [0.0 if x is None else x for x in v]


def stat(r, compound):
    f = [x for x in r if x is not None]
    n = len(f)
    m = sum(f) / n
    sd = (sum((x - m) ** 2 for x in f) / n) ** 0.5
    if compound:
        nav, peak, mdd = 1.0, 1.0, 0.0
        for x in f:
            nav *= 1 + x
            peak = max(peak, nav)
            mdd = min(mdd, nav / peak - 1)
        growth = nav ** (252 / n) - 1
    else:
        eq, peak, mdd = 0.0, 0.0, 0.0
        for x in f:
            eq += x
            peak = max(peak, eq)
            mdd = min(mdd, eq - peak)
        growth = m * 252
    return {"ann": growth, "vol": sd * 252 ** 0.5, "sharpe": m / sd * 252 ** 0.5, "mdd": mdd, "days": n}


stats = {}
for o in set(LS) | {LONG}:
    d = O[o]
    end = d.get("ends", len(dates))
    SEGS = {"in": (0, isplit), "out": (isplit, min(ifw, end)), "all": (0, end)}
    if ifw < end:
        SEGS["fwd"] = (ifw, end)
    stats[o] = {"ls": {s: stat(d["ls"][a:b], False) for s, (a, b) in SEGS.items()}, "total": {s: stat(d["total"][a:b], True) for s, (a, b) in SEGS.items()},
                "bench": {s: stat(d["bench"][a:b], True) for s, (a, b) in SEGS.items()}, "excess": {s: stat(d["excess"][a:b], False) for s, (a, b) in SEGS.items()},
                "long_turnover": d["long_turnover"], "ls_turnover": d["ls_turnover"], "names_held": d["names_held"], "universe": d["universe"]}
    yrs = sorted({x[:4] for x in dates})
    stats[o]["by_year"] = {}
    for y in yrs:
        idx = [i for i, x in enumerate(dates) if x[:4] == y]
        tot, ben, ls = 1.0, 1.0, 0.0
        for i in idx:
            tot *= 1 + (d["total"][i] or 0.0)
            ben *= 1 + (d["bench"][i] or 0.0)
            ls += d["ls"][i] or 0.0
        stats[o]["by_year"][y] = {"total": tot - 1, "bench": ben - 1, "ls": ls}

W, H, ml, mr, mt, mb = 1000, 540, 70, 26, 56, 50
n = len(dates)
X = lambda i: ml + (W - ml - mr) * i / (n - 1)                 # noqa: E731
pct = lambda x: f"{x:+.1%}"                                    # noqa: E731


def frame(title, sub, y_of, ticks, tick_label):
    A = [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" font-family="-apple-system, PingFang SC, Helvetica, Arial, sans-serif" font-size="13">',
         f'<rect width="{W}" height="{H}" fill="#ffffff"/>',
         f'<rect x="{X(isplit):.1f}" y="{mt}" width="{X(min(ifw, n - 1)) - X(isplit):.1f}" height="{H - mt - mb}" fill="#f1f5fb"/>']
    if ifw < n:
        A.append(f'<rect x="{X(ifw):.1f}" y="{mt}" width="{W - mr - X(ifw):.1f}" height="{H - mt - mb}" fill="#fdf3e3"/>')
        A.append(f'<text x="{W - mr - 4}" y="{mt + 16}" text-anchor="end" fill="#9a6a15">前推段(2026)</text>')
    A += [f'<text x="{ml}" y="24" font-size="17" font-weight="600" fill="#111">{title}</text>', f'<text x="{ml}" y="43" fill="#555">{sub}</text>',
          f'<text x="{(X(0) + X(isplit)) / 2:.1f}" y="{mt + 16}" text-anchor="middle" fill="#666">样本内</text>',
          f'<text x="{(X(isplit) + X(min(ifw, n - 1))) / 2:.1f}" y="{mt + 16}" text-anchor="middle" fill="#3b5b8c">样本外</text>']
    for t in ticks:
        y = y_of(t)
        A.append(f'<line x1="{ml}" y1="{y:.1f}" x2="{W - mr}" y2="{y:.1f}" stroke="#e6e6e6"/>')
        A.append(f'<text x="{ml - 8}" y="{y + 4:.1f}" text-anchor="end" fill="#555">{tick_label(t)}</text>')
    for y in sorted({d[:4] for d in dates}):
        i = next(k for k, d in enumerate(dates) if d[:4] == y)
        A.append(f'<line x1="{X(i):.1f}" y1="{H - mb}" x2="{X(i):.1f}" y2="{H - mb + 5}" stroke="#888"/>')
        A.append(f'<text x="{X(i) + 3:.1f}" y="{H - mb + 20}" fill="#555">{y}</text>')
    A.append(f'<line x1="{X(isplit):.1f}" y1="{mt}" x2="{X(isplit):.1f}" y2="{H - mb}" stroke="#444" stroke-dasharray="5 4"/>')
    A.append(f'<rect x="{ml}" y="{mt}" width="{W - ml - mr}" height="{H - mt - mb}" fill="none" stroke="#999"/>')
    return A


def line(vals, y_of, color, width=2.0, dash="", end=None):
    pts = " ".join(f"{X(i):.1f},{y_of(v):.1f}" for i, v in enumerate(vals[:end]))
    return f'<polyline points="{pts}" fill="none" stroke="{color}" stroke-width="{width}"{" stroke-dasharray=" + chr(34) + dash + chr(34) if dash else ""} stroke-linejoin="round"/>'


# ---- 1. long / short: cumulative net return (sum of daily returns: the book is rebalanced to gross 1 every day)
cum = {}
for o in LS:
    c, s = [], 0.0
    for x in clean(O[o]["ls"]):
        s += x
        c.append(s)
    cum[o] = c
top = max(max(c[:O[o].get("ends")]) for o, c in cum.items())
step = 0.5 if top > 2 else 0.25
ticks = [k * step for k in range(int(top / step) + 2)]
if ifw < len(dates):                                              # the two-line legend needs head-room above the curves
    while ticks[-1] < top * 1.45:
        ticks.append(ticks[-1] + step)
y1 = lambda v: H - mb - (H - mt - mb) * v / ticks[-1]          # noqa: E731
A = frame("多空:做多排名最好的 10%、做空最差的 10%(总敞口 1,扣 15bp 成本)", "纵轴 = 累计净收益(每日收益相加);虚线右侧是样本外" + (",橙色底是 2026 年的前推段" if ifw < len(dates) else ""),
          y1, ticks, lambda t: f"{t:.0%}")
COL = ["#1f5fbf", "#c0392b", "#27865a"]
for j, o in enumerate(LS):
    A.append(line(cum[o], y1, COL[j], end=O[o].get("ends")))
    if O[o].get("ends", len(dates)) < len(dates):
        e = O[o]["ends"] - 1
        A.append(f'<text x="{X(e) - 6:.1f}" y="{y1(cum[o][e]) + 20:.1f}" text-anchor="end" fill="{COL[j]}" font-size="12">止于 {dates[e][:4]}-{dates[e][4:6]}(不在前推段的读数清单里)</text>')
two = any("fwd" in stats[o]["ls"] for o in LS)                    # with a forward segment the legend takes two lines per series
for j, o in enumerate(LS):
    s = stats[o]["ls"]
    y = mt + 40 + (38 if two else 22) * j
    A.append(f'<line x1="{ml + 14}" y1="{y - 4}" x2="{ml + 42}" y2="{y - 4}" stroke="{COL[j]}" stroke-width="3"/>')
    body = (f'样本内 年化 {pct(s["in"]["ann"])}、夏普 {s["in"]["sharpe"]:.2f}、回撤 {pct(s["in"]["mdd"])};'
            f'样本外 {pct(s["out"]["ann"])}、夏普 {s["out"]["sharpe"]:.2f}、回撤 {pct(s["out"]["mdd"])}')
    if two:
        A.append(f'<text x="{ml + 48}" y="{y}" fill="#222" font-weight="600">{NAME.get(o, o)}</text>')
        tail = f';前推段 {pct(s["fwd"]["ann"])}、夏普 {s["fwd"]["sharpe"]:.2f}、回撤 {pct(s["fwd"]["mdd"])}' if "fwd" in s else ""
        A.append(f'<text x="{ml + 48}" y="{y + 17}" fill="#333" font-size="12">{body}{tail}</text>')
    else:
        A.append(f'<text x="{ml + 48}" y="{y}" fill="#222">{NAME.get(o, o)}:{body}</text>')
A.append("</svg>")
out_dir = root / "research" / "alpha_distillation"
SUF = opt("--suffix") or ("_to2026" if opt("--forward") else "")
(out_dir / f"{BATCH}_best_longshort{SUF}.svg").write_text("\n".join(A), encoding="utf-8")

# ---- 2. pure long: TOTAL return (compounded), next to the equal-weight universe; log scale
d = O[LONG]
nav, ben, exc = [], [], []
a = b = c = 1.0
for t, e, x in zip(clean(d["total"]), clean(d["bench"]), clean(d["excess"])):
    a *= 1 + t
    b *= 1 + e
    c *= 1 + x
    nav.append(a)
    ben.append(b)
    exc.append(c)
lo, hi = min(min(nav), min(ben)), max(max(nav), max(ben))
ticks = [t for t in (0.25, 0.5, 1, 2, 4, 8, 16, 32, 64) if lo / 1.5 <= t <= hi * 3.2]      # head-room above the curve for the legend
l0, l1 = math.log(ticks[0]), math.log(ticks[-1])
y2 = lambda v: H - mb - (H - mt - mb) * (math.log(v) - l0) / (l1 - l0)      # noqa: E731
s = stats[LONG]
B = frame(f"纯多头的全部收益:{NAME.get(LONG, LONG)}(每天等权买排名最好的 10%,约 {d['names_held']:.0f} 只,扣 15bp)",
          "纵轴 = 净值(起点 1,复利,对数刻度);红线是这本多头书自己的全部收益,灰线是全市场等权", y2, ticks, lambda t: f"{t:g}")
B.append(line(ben, y2, "#8a8a8a", 1.8))
B.append(line(nav, y2, "#c0392b", 2.2))
def leg(tag):
    t, b = s["total"][tag], s["bench"][tag]
    return (f"多头书 年化 {pct(t['ann'])}、波动 {t['vol']:.0%}、夏普 {t['sharpe']:.2f}、最大回撤 {pct(t['mdd'])}"
            f"  |  全市场等权 年化 {pct(b['ann'])}、最大回撤 {pct(b['mdd'])}")


rows = [("#c0392b", "这本多头书的全部收益"), ("#8a8a8a", "全市场等权(它的比较基准)"), (None, "样本内:" + leg("in")), (None, "样本外:" + leg("out"))]
if "fwd" in s["total"]:
    rows.append((None, "前推段(2026):" + leg("fwd")))
    B.append(f'<rect x="{ml + 8}" y="{mt + 22}" width="{728}" height="{20 * len(rows) + 8}" fill="#ffffff" fill-opacity="0.86"/>')
for j, (col, txt) in enumerate(rows):
    y = mt + 40 + 20 * j
    if col:
        B.append(f'<line x1="{ml + 14}" y1="{y - 4}" x2="{ml + 42}" y2="{y - 4}" stroke="{col}" stroke-width="3"/>')
    B.append(f'<text x="{ml + 48 if col else ml + 14}" y="{y}" fill="#222">{txt}</text>')
B.append(f'<text x="{W - mr - 6}" y="{y2(nav[-1]) - 8:.1f}" text-anchor="end" fill="#c0392b" font-weight="600">{nav[-1]:.1f} 倍</text>')
B.append(f'<text x="{W - mr - 6}" y="{y2(ben[-1]) + 16:.1f}" text-anchor="end" fill="#666">{ben[-1]:.1f} 倍</text>')
B.append("</svg>")
(out_dir / f"{BATCH}_best_long_total{SUF}.svg").write_text("\n".join(B), encoding="utf-8")
(out_dir / f"{BATCH}_best_books{SUF}.json").write_text(json.dumps({"end": dates[-1], "ls": LS, "long": LONG, "stats": stats}, ensure_ascii=False, indent=1), encoding="utf-8")
print(f"wrote {BATCH}_best_longshort{SUF}.svg and {BATCH}_best_long_total{SUF}.svg in {out_dir}; data to {dates[-1]}; final NAV {nav[-1]:.2f} vs {ben[-1]:.2f}")
