"""Risk control: the charts and the tables of research/risk_control/RESULT.md.   rc_report.py [tag] [--charts DIR]

Local.  Reads runs/_risk/risk_control_<tag>.json and writes
  research/risk_control/tables_<tag>.md    the per-champion tables (picks + stacks; then every grid cell)
  <DIR>/rc_<tag>_<champion>.png            net value (total return, log scale) and drawdown: baseline vs the picks that matter
"""
import json
import subprocess
import sys
from pathlib import Path

import numpy as np

ROOT = Path(__file__).resolve().parents[1]
args = [a for a in sys.argv[1:] if not a.startswith("--")]
tag = args[0] if args else "r1"
charts = Path(sys.argv[sys.argv.index("--charts") + 1]) if "--charts" in sys.argv else ROOT / "research" / "risk_control"
J = json.loads((ROOT / "runs" / "_risk" / f"risk_control_{tag}.json").read_text(encoding="utf-8"))
dates = np.asarray(J["dates"])

md = [f"# 风险控制 R001:结果表(tag `{tag}`)\n", f"段:{json.dumps(J['segments'], ensure_ascii=False)}\n",
      "列:内 = 样本内,外 = 合并样本外;夏普 / 年化 / 回撤 / Calmar 都是**全部收益**(不满仓时现金记 0);「对基线年化差 / t」是同一天相减;"
      "夏普差区间 = 成对区组自助法 90%;踩踏段 = 2024-01-16 ~ 02-06 的全部收益。`*` = 该方法族样本内选中的格子,`x` = 选中的格子样本内就不如基线。\n"]
for flag, title in (("", "按规则的读数(各方法族样本内选中的格子 + 叠加)"), ("--all", "全部格子(样本外只作敏感性)")):
    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "rc_table.py"), tag, "--md"] + ([flag] if flag else []), capture_output=True, text=True).stdout
    md.append(f"\n# {title}\n" + out)
(ROOT / "research" / "risk_control" / f"tables_{tag}.md").write_text("\n".join(md), encoding="utf-8")

import matplotlib  # noqa: E402

matplotlib.use("Agg")
import matplotlib.dates as mdates  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib import font_manager  # noqa: E402

for f_ in ("PingFang SC", "Heiti SC", "Songti SC", "Arial Unicode MS"):
    if any(f_ in x.name for x in font_manager.fontManager.ttflist):
        plt.rcParams["font.sans-serif"] = [f_]
        break
plt.rcParams["axes.unicode_minus"] = False
x = np.asarray([np.datetime64(f"{d[:4]}-{d[4:6]}-{d[6:]}") for d in dates])
COL = ["#222222", "#d1495b", "#00798c", "#edae49", "#66a182", "#8d5b9a"]
for name, C in J["champions"].items():
    B, S_ = C["books"], C["series"]
    show = ["base"]
    want = [k for k in S_ if k.startswith("C")] + [p["key"] for f, p in C["picks"].items() if f.startswith(("B3", "B2", "A")) and p["passes_insample"]]
    want = sorted(set(want), key=lambda k: -(B[k]["stats"]["oos"].get("calmar") or -9))
    show += [k for k in want if k in S_][:4]
    fig, ax = plt.subplots(2, 1, figsize=(11, 7), sharex=True, gridspec_kw={"height_ratios": [3, 1.3]})
    series = {k: np.nan_to_num(np.asarray([np.nan if v is None else v for v in S_[k]], dtype=float), nan=0.0) for k in show}
    series["全市场等权"] = np.nan_to_num(np.asarray([np.nan if v is None else v for v in C["bench"]], dtype=float), nan=0.0)
    for i, (k, s) in enumerate(series.items()):
        nav = np.cumprod(1 + s)
        st = B[k]["stats"]["oos"] if k in B else None
        lab = (f"{'基线(满仓)' if k == 'base' else k}:样本外 夏普 {st['sharpe']:.2f} / 年化 {st['ann']:+.0%} / 回撤 {st['mdd']:.0%}" if st else k)
        c = "#999999" if k == "全市场等权" else COL[i % len(COL)]
        ax[0].plot(x, nav, color=c, lw=1.6 if k == "base" else 1.1, label=lab, ls="--" if k == "全市场等权" else "-")
        ax[1].plot(x, nav / np.maximum.accumulate(nav) - 1, color=c, lw=0.9, ls="--" if k == "全市场等权" else "-")
    split = x[int(np.searchsorted(dates, J["segments"]["oos"][0]))]
    for a in ax:
        a.axvline(split, color="#888888", lw=0.8, ls=":")
        a.grid(alpha=0.25)
    ax[0].set_yscale("log")
    ax[0].set_title(f"{name}:纯多头全部收益净值(扣 15 bp;虚线右侧 = 样本外,风控参数只在左侧选)", fontsize=11)
    ax[0].legend(fontsize=8, loc="upper left")
    ax[1].set_ylabel("回撤")
    ax[1].xaxis.set_major_locator(mdates.YearLocator())
    fig.tight_layout()
    p = charts / f"rc_{tag}_{name}.png"
    p.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(p, dpi=150)
    plt.close(fig)
    print("wrote", p)
print("wrote", ROOT / "research" / "risk_control" / f"tables_{tag}.md")
