"""The batch answer, from the batch method: every factor's sweep, anatomy, synthesis and test-period read.

Reads only local files (pull them first: ``./scripts/study.sh table <fid> s2`` pulls the JSONs):

    runs/<fid>/sweepfinal_<tag>.json     the rule-based test-period read
    runs/<fid>/sweep_<tag>.json          the sweep (train / valid)
    handoff/<fid>/results/synthesis.json the lead's one-pass synthesis (what it is, where / when / why)

    python scripts/batch2_summary.py batches/B01_single_factors.yaml [--tag s2] [--out research/alpha_distillation/B01_batch_summary.md]
"""
import json
import sys
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]


def opt(name, default=None):
    return argv[argv.index(name) + 1] if name in argv else default


TAG = opt("--tag", "s2")
batch = yaml.safe_load(open(root / argv[0], encoding="utf-8"))
out = root / opt("--out", "research/alpha_distillation/B01_batch_summary.md")


def pc(x):
    return "—" if x is None or x != x else f"{x:+.1%}"


def sh(x):
    return "—" if x is None or x != x else f"{x:+.2f}"


def row(r):
    v = r["books_user"]["by_rank"]["long"]
    a, h = v["splits"]["utrain"], v["splits"]["holdout"]
    return v["hl"], a, h


def short(e, n=96):
    return e if len(e) <= n else e[: n - 1] + "…"


L = [f"# {batch.get('name', 'B01')} 批量研究总表(批量扫描 → 市场解剖 → 综合 → 第二批假设 → 按写死规则读测试段)", "",
     "口径同用户的表:训练 20180102–20230807,测试 20230808–20251231;前 10% 纯多头书减有信号有标签股票的等权,扣 15bp;",
     "方向与半衰期在用户训练段上定(半衰期按纯多头书选)。候选**只用 train / valid 按写死的规则选出**,再读测试段:",
     "本因子自己的候选 = 各类变体里用户训练段纯多头夏普最高、过门槛(cov ≥ 0.95、dist ≥ 0.5)、train 与 valid 多头腿都为正的,取最好的 3 类各 1 个;",
     "建在已知族上的候选(叠加 / 筛子)单列。测试段的噪声约为净超额 ±3 个点、夏普 ±0.3。", "",
     "## 1. 一张表(多头腿净超额 训练 / 测试;括号里是纯多头夏普)", "",
     "| # | 因子 | 原式 | 本因子最好的版本 | 它的数字 | ρ原式 / ρ已知族 | 建在已知族上的最好版本 | 它的数字 |",
     "|---|---|---|---|---|---|---|---|"]
detail, missing = [], []
known_row = frozen_row = None
pool = []            # every candidate read on the test period: (factor, id, record, own?)
for i, f in enumerate(batch["factors"], 1):
    fid = f["id"]
    fp = root / "runs" / fid / f"sweepfinal_{TAG}.json"
    if not fp.is_file():
        missing.append(fid)
        continue
    F = json.loads(fp.read_text(encoding="utf-8"))
    R = F["results"]
    ho, ao, to = row(R["v_base"])
    known_row = known_row or (R.get("k_known") and row(R["k_known"]))
    frozen_row = frozen_row or (R.get("k_known_xfrozen") and row(R["k_known_xfrozen"]))
    own = [k for k in F["picks"] if k in R]
    onk = [k for k in R if k not in ("v_base", "k_known", "k_known_xfrozen") and k not in own]
    pool += [(f, k, R[k], k in own) for k in own + onk]
    best = max(own, key=lambda k: row(R[k])[1]["long_sharpe"]) if own else None
    bk = max(onk, key=lambda k: row(R[k])[1]["long_sharpe"]) if onk else None
    cells = [str(i), f"{f['lib']} {f['name']}", f"{pc(ao['long_ann'])} / {pc(to['long_ann'])}({sh(ao['long_sharpe'])} / {sh(to['long_sharpe'])})"]
    for k in (best, bk):
        if k:
            h, a, t = row(R[k])
            cells += [f"`{short(R[k]['expr'], 80)}` hl {h:g}", f"**{pc(a['long_ann'])} / {pc(t['long_ann'])}**({sh(a['long_sharpe'])} / {sh(t['long_sharpe'])})"]
            if k == best:
                cells.append(f"{(R[k].get('corr_orig') or 0):+.2f} / {(R[k].get('corr_known') or 0):+.2f}")
        else:
            cells += ["(没有过规则的)", "—"] + (["—"] if k is best else [])
    L.append("| " + " | ".join(cells) + " |")
    # per-factor detail
    D = [f"### {i}. {f['lib']} {f['name']}({fid.split('_')[0]})", "", f"`{f['expr'][:300]}{'…' if len(f['expr']) > 300 else ''}`", ""]
    sp = root / "handoff" / fid / "results" / "synthesis.json"
    if sp.is_file():
        S = json.loads(sp.read_text(encoding="utf-8"))
        D += [f"**它是什么(按算子定义)**:{S.get('what_it_is', '').strip()}", ""]
        for title, key in (("承重的子结构", "load_bearing"), ("多余的节点", "redundant"), ("可互换的叶子", "swappable_leaves"),
                           ("在哪类股票里有效", "where_it_works"), ("什么时候有效", "when_it_works")):
            if S.get(key):
                D += [f"**{title}**", ""] + [f"- {x}" for x in S[key]] + [""]
        D += [f"**原因推断**:{S.get('why', '').strip()}", "", f"**相对已知成交额族**:{S.get('adds_over_known_family', '').strip()}", ""]
    D += ["**测试段读数(候选按规则选出)**", "",
          "| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |", "|---|---|---|---|---|---|---|---|"]
    for k, r in R.items():
        h, a, t = row(r)
        ls = r["books_user"]["by_rank"]["ls"]["splits"]
        D.append(f"| `{k}` `{short(r['expr'], 90)}` | {r['kind']} | {h:g} | {pc(a['long_ann'])} / {pc(t['long_ann'])} | {sh(a['long_sharpe'])} / {sh(t['long_sharpe'])} "
                 f"| {a['long_turnover']:.1%} | {sh(ls['utrain']['ls_sharpe'])} / {sh(ls['holdout']['ls_sharpe'])} | "
                 + " ".join(f"{x:+.0%}" for x in r["by_year_long_net"].values()) + " |")
    D += ["", f"综合全文:`notes/{fid}/synthesis.md`;回测表与解剖:`./scripts/study.sh table {fid} {TAG}`。", ""]
    detail += D
if known_row:
    h, a, t = known_row
    L.append(f"| — | _基准:已知成交额族_ `cross_mean(day_std(Amt), 30)` | {pc(a['long_ann'])} / {pc(t['long_ann'])}({sh(a['long_sharpe'])} / {sh(t['long_sharpe'])}) | | | | | |")
if frozen_row:
    h, a, t = frozen_row
    L.append(f"| — | _通用筛子:已知族 + 剔除近 15 日冻结盘口最重的 20%_ | {pc(a['long_ann'])} / {pc(t['long_ann'])}({sh(a['long_sharpe'])} / {sh(t['long_sharpe'])}) | | | | | |")
if missing:
    L += ["", "还没有测试段读数的:" + "、".join(x.split("_")[0] for x in missing)]


def top(rows, title, note):
    out_ = ["", f"### {title}", "", note, "",
            "| 来自 | 表达式 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 训练 / 测试 | 日换手 | 测试段最大回撤 | ρ已知族 | 逐年 2018…2025 |", "|---|---|---|---|---|---|---|---|---|"]
    for f, k, r, _ in rows:
        h, a, t = row(r)
        out_.append(f"| {f['id'].split('_')[0]} {f['name']} | `{short(r['expr'], 110)}` | {h:g} | **{pc(a['long_ann'])} / {pc(t['long_ann'])}** | {sh(a['long_sharpe'])} / {sh(t['long_sharpe'])} "
                    f"| {a['long_turnover']:.1%} | {pc(t['long_mdd'])} | {(r.get('corr_known') or 0):+.2f} | " + " ".join(f"{x:+.0%}" for x in r["by_year_long_net"].values()) + " |")
    return out_


def ush(x):
    return -(row(x[2])[1]["long_sharpe"] or -9)


seen = set()
uniq = [x for x in sorted(pool, key=ush) if not (x[2]["expr"] in seen or seen.add(x[2]["expr"]))]
indep = [x for x in uniq if abs(x[2].get("corr_known") or 0) < 0.5 and "day_std(Amt)" not in x[2]["expr"]][:12]
onkn = [x for x in uniq if x not in indep and (abs(x[2].get("corr_known") or 0) >= 0.5 or "day_std(Amt)" in x[2]["expr"])][:14]
T = ["", "## 0. 最值得看的(两张榜都**按用户训练段的纯多头夏普排序**,没有用测试段挑)", ""]
if known_row:
    h, a, t = known_row
    T.append(f"对照:已知成交额族 `cross_mean(day_std(Amt), 30)` 训练 / 测试 {pc(a['long_ann'])} / {pc(t['long_ann'])},纯多头夏普 {sh(a['long_sharpe'])} / {sh(t['long_sharpe'])},测试段最大回撤 {pc(t['long_mdd'])}。")
T += top(indep, "A. 与已知成交额族相关低于 0.5 的(独立的新东西)",
         "这些可以和已知族并列持有。测试段上单个数字有 ±3 个点 / ±0.3 夏普的噪声,而且一共读了约一百个候选,榜首的数字有向上的选择偏差 —— 看逐年是否稳定比看单个数字可靠。")
T += top(onkn, "B. 建在已知族上的、或实质落在这一族里的(已知族的升级版)",
         "筛子 = 已知族剔掉某类票;分段 = 只在低流动性 40% 里按本因子选;叠加 = 已知族的秩加上本因子的秩。它们和已知族高度相关,是替换而不是并列。")
i0 = L.index("## 1. 一张表(多头腿净超额 训练 / 测试;括号里是纯多头夏普)")
L[i0:i0] = T + [""]
L += ["", "## 2. 逐条", ""] + detail
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(L), encoding="utf-8")
print(f"wrote {out}: {len(batch['factors']) - len(missing)} factors, missing {[x.split('_')[0] for x in missing]}")
