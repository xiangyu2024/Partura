"""The one-page answer for a batch: original vs pick, in the selection convention.

Reads only what the studies already produced -- each study's single holdout
read (``runs/<fid>/<run>.json``) and the training-period overview of the picks
(``runs/_batch_<B>/final_overview.json``, from ``scripts/batch_final.py``).
Nothing is evaluated and no split is read again.

    python scripts/batch_summary.py batches/B01_picks.yaml [--out research/alpha_distillation/B01_summary.md]

The numbers of every row are: half-life fitted on the user's training period
(20180102-20230807) by the pure long book's after-cost Sharpe; net long-leg
excess = top-decile pure long book minus the equal-weight universe, after
15 bp per unit turnover; train = that period, test = 20230808-20251231.
"""
import json
import sys
from pathlib import Path

import yaml

root = Path(__file__).resolve().parents[1]
picks = yaml.safe_load(open(sys.argv[1], encoding="utf-8"))
batch = yaml.safe_load(open(root / "batches" / f"{picks['batch']}.yaml", encoding="utf-8"))
out = root / (sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv
              else f"research/alpha_distillation/{picks['batch'].split('_')[0]}_summary.md")
bdir = root / "runs" / f"_batch_{picks['batch'].split('_')[0]}"
ov = json.loads((bdir / "final_overview.json").read_text(encoding="utf-8")) if (bdir / "final_overview.json").is_file() else None
_cache = {}


def run_json(fid, run):
    key = (fid, run)
    if key not in _cache:
        p = root / "runs" / fid / f"{run}.json"
        _cache[key] = json.loads(p.read_text(encoding="utf-8")) if p.is_file() else None
    return _cache[key]


def views(b):
    if "by_rank" in b:
        return b["by_rank"]
    return {"ls": {"hl": b["hl_ls"], "splits": b["splits"]},
            "long": {"hl": b["hl_long"], "splits": b.get("splits_at_hl_long") or b["splits"]}}


def find(fid, run, vid=None, expr=None):
    """The holdout-scored record of one candidate: by id, else by expression, in the named run."""
    d = run_json(fid, run)
    if d is None:
        return None
    us = d.get("user_split", "utrain")
    for k, r in d["results"].items():
        if "books_user" not in r or "holdout" not in r["books_user"]["splits"]:
            continue
        if (vid and k == vid) or (expr and r["expr"].replace(" ", "") == expr.replace(" ", "")):
            return {"id": k, "expr": r["expr"], "sign": r.get("sign_user", r.get("sign")),
                    "views": views(r["books_user"]), "us": us,
                    "distinct": r.get("distinct"), "run": run}
    return None


def pc(x):
    return "—" if x is None or x != x else f"{x:+.1%}"


def sh(x):
    return "—" if x is None or x != x else f"{x:+.2f}"


def pair(v, key, us, f):
    return f"{f(v['splits'][us].get(key))} / {f(v['splits']['holdout'].get(key))}"


def short(expr, n=88):
    return expr if len(expr) <= n else expr[:n - 3] + "..."


KIND = {"original_kept": "保留原式", "distilled": "蒸馏(更简、同样好)", "elevated": "升华(更好)",
        "rejected": "否决(多头腿不可用)", "known_family": "归入已知族", "halflife_only": "只需换半衰期"}

rows, missing = [], []
for i, f in enumerate(batch["factors"], 1):
    fid = f["id"]
    p = picks["picks"].get(fid) or {}
    o = None
    for run in [p.get("orig_run"), p.get("run"), "final"]:
        if run:
            o = find(fid, run, vid=p.get("orig_id"), expr=f["expr"])
            if o:
                break
    if o is None:
        missing.append(fid)
        continue
    k = find(fid, p.get("run", "final"), vid=p.get("id"), expr=p.get("expr")) if (p.get("id") or p.get("expr")) else None
    rows.append({"n": i, "f": f, "p": p, "o": o, "k": k or o, "same": k is None or k["id"] == o["id"]})

L = [f"# {picks['batch'].split('_')[0]} 批次总表:原式 vs 提纯 / 升华后的入选式", "",
     picks.get("preamble", "").strip(), "",
     "## 1. 一张表", "",
     "口径:半衰期在用户训练段(20180102–20230807)上由**纯多头书**的扣费夏普选;多头腿净超额 = 前 10% 纯多头书 − 有信号有标签"
     "股票的等权,扣 15bp/单位换手,年化;训练 = 上述区间,测试 = 20230808–20251231(每个因子的研究只读了这一次)。"
     "测试段的噪声大约是净超额 ±3 个点、夏普 ±0.3。", "",
     "| # | 因子 | 原式·你的表的口径(多空半衰期)多头净 训练/测试 | 原式·多头半衰期 | 原式 多头净 训练/测试 | 原式 纯多头夏普 | **入选式** | 半衰期 | **入选 多头净 训练/测试** | **入选 纯多头夏普** | 日换手 | 结论 |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for r in rows:
    f, p, o, k = r["f"], r["p"], r["o"], r["k"]
    us = o["us"]
    vl, vo, vk = o["views"]["ls"], o["views"]["long"], k["views"]["long"]
    name = f"{f['lib']} {f['name']}"
    pick_txt = "(原式)" if r["same"] else f"`{short(k['expr'], 70)}`"
    L.append(f"| {r['n']} | {name} | {pair(vl, 'long_ann', us, pc)}(hl {vl['hl']:g}) | {vo['hl']:g} "
             f"| {pair(vo, 'long_ann', us, pc)} | {pair(vo, 'long_sharpe', us, sh)} | {pick_txt} | {vk['hl']:g} "
             f"| **{pair(vk, 'long_ann', us, pc)}** | **{pair(vk, 'long_sharpe', us, sh)}** "
             f"| {vk['splits'][us]['long_turnover']:.1%} | {KIND.get(p.get('kind'), p.get('kind', ''))} |")
for b in picks.get("benchmark_rows", []):
    k = find(b["fid"], b.get("run", "final"), vid=b.get("id"), expr=b.get("expr"))
    if k:
        vk = k["views"]["long"]
        L.append(f"| — | _基准:{b['label']}_ | | | | | `{short(k['expr'], 70)}` | {vk['hl']:g} "
                 f"| {pair(vk, 'long_ann', k['us'], pc)} | {pair(vk, 'long_sharpe', k['us'], sh)} "
                 f"| {vk['splits'][k['us']]['long_turnover']:.1%} | 已知族(读数来自 {b['fid'].split('_')[0]} 的那次留出段) |")
if missing:
    L += ["", "没有留出段读数的因子(研究未完成): " + ", ".join(missing)]

L += ["", "## 2. 每个因子一句话", ""]
for r in rows:
    f, p = r["f"], r["p"]
    L.append(f"**{r['n']}. {f['lib']} {f['name']}**({f['id'].split('_')[0]})— {p.get('one_line', '').strip()}")
    if p.get("family"):
        L.append(f"  - 家族:{p['family'].strip()}")
    if p.get("caveat"):
        L.append(f"  - 注意:{p['caveat'].strip()}")
    L.append(f"  - 报告:[{f['id']}.md]({f['id']}.md)")
    L.append("")

if ov:
    info, corr, marg = ov["info"], ov["corr"], ov.get("marginal", {})
    keys = [k for k in info if k.endswith(".pick") or (k.endswith(".orig") and k.replace(".orig", ".pick") not in info)]
    bench = [k for k in info if not (k.endswith(".pick") or k.endswith(".orig"))]
    cols = keys + bench
    L += ["## 3. 分辨:入选式之间是几个因子", "",
          f"可交易信号(方向 × 面板,按多头口径的半衰期平滑)在用户训练段({ov['split'][0]}–{ov['split'][1]})上的日截面 rank 相关。"
          "只用训练段,没有读留出段。|相关| ≥ 0.8 基本是同一个因子。", "",
          "| | " + " | ".join(c.replace(".pick", "′").replace(".orig", "") for c in cols) + " |",
          "|---|" + "---|" * len(cols)]
    for a in cols:
        cells = []
        for b in cols:
            c = corr[a].get(b)
            if a == b:
                cells.append("·")
            elif c is None:
                cells.append("")
            else:
                cells.append(f"**{c:+.2f}**" if abs(c) >= 0.8 else (f"{c:+.2f}" if abs(c) >= 0.3 else f"<sub>{c:+.2f}</sub>"))
        L.append(f"| {a.replace('.pick', '′').replace('.orig', '')} | " + " | ".join(cells) + " |")
    L += ["", "(带 ′ 的是入选式;不带的是原式被保留的因子;最后几列是已知族基准。)", ""]

    # clusters by single linkage at |corr| >= 0.8
    parent = {k: k for k in cols}

    def root_of(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for i, a in enumerate(cols):
        for b in cols[i + 1:]:
            c = corr[a].get(b)
            if c is not None and abs(c) >= 0.8:
                parent[root_of(a)] = root_of(b)
    groups = {}
    for k in cols:
        groups.setdefault(root_of(k), []).append(k)
    L += ["按 |相关| ≥ 0.8 单链接聚类:", ""]
    for g in sorted(groups.values(), key=lambda g: -len(g)):
        L.append("- " + "、".join(x.replace(".pick", "′").replace(".orig", "") for x in g)
                 + ("(单独一类)" if len(g) == 1 else f"({len(g)} 个,同一个因子)"))
    L.append("")

    if marg:
        kn = ov["known"]
        any_ = next(iter(marg.values()))
        L += [f"## 4. 分辨:对已知的成交额水平族(`{info[kn]['expr']}`)还有没有增量", "",
              f"全部在用户训练段上量(没有读留出段)。已知族自己的纯多头书:净超额 {pc(any_['known_long_ann'])}、夏普 {sh(any_['known_long_sharpe'])}。"
              "「残差」= 把信号在秩空间对已知族逐日回归后剩下的部分单独做多头书;「五五混合」= 两个信号的秩各取一半。", "",
              "| 信号 | 半衰期 | 自己的多头净超额(夏普) | 被已知族解释的 R² | 残差的多头净超额(夏普) | 与已知族五五混合(夏普) | 混合 − 已知族 |",
              "|---|---|---|---|---|---|---|"]
        for k in cols:
            if k not in marg:
                continue
            m, inf = marg[k], info[k]
            L.append(f"| {k.replace('.pick', '′').replace('.orig', '')} | {inf['hl_long']:g} "
                     f"| {pc(inf['utrain_long_ann'])}({sh(inf['utrain_long_sharpe'])}) | {m['r2_by_known']:.2f} "
                     f"| {pc(m['resid_long_ann'])}({sh(m['resid_long_sharpe'])}) "
                     f"| {pc(m['blend_long_ann'])}({sh(m['blend_long_sharpe'])}) "
                     f"| {pc(m['blend_long_ann'] - m['known_long_ann'])} / {m['blend_long_sharpe'] - m['known_long_sharpe']:+.2f} |")
        L.append("")
if picks.get("closing"):
    L += [picks["closing"].strip(), ""]
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(L), encoding="utf-8")
print(f"wrote {out} ({len(L)} lines; {len(rows)} factors, {len(missing)} missing)")
