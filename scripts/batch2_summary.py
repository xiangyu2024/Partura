"""The batch answer, from the batch method: every factor's sweep, anatomy, synthesis and test-period read.

Reads only local files (pull them first: ``./scripts/study.sh table <fid> s2`` pulls the JSONs):

    runs/<fid>/sweepfinal_<tag>.json     the rule-based test-period read
    runs/<fid>/sweep_<tag>.json          the sweep (train / valid)
    handoff/<fid>/results/synthesis.json the lead's one-pass synthesis (what it is, where / when / why)
    handoff/<fid>/results/verdict.json   the lead's reconciliation of the second batch (confirmed / refuted), when there is one
    runs/_batch_<B>/cluster_<tag>.json   scripts/batch_cluster.py: clusters of the picks and the combination books, when there is one

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
_cp = root / "runs" / f"_batch_{Path(argv[0]).stem.split('_')[0]}" / f"cluster_{TAG}.json"
_kl = {v["expr"].replace(" ", ""): v.get("known_like") for v in json.loads(_cp.read_text(encoding="utf-8"))["info"].values()} if _cp.is_file() else {}


def _known_like(x):
    """The measured verdict of batch_cluster (rank correlation / long-book overlap with the known family and with
    its screened version), so that this table and the readable report cannot disagree; the old rule when absent."""
    v = _kl.get(x[2]["expr"].replace(" ", ""))
    return v if v is not None else (abs(x[2].get("corr_known") or 0) >= 0.5 or "day_std(Amt)" in x[2]["expr"])


indep = [x for x in uniq if not _known_like(x)][:12]
onkn = [x for x in uniq if _known_like(x)][:14]
T = ["", "## 0. 最值得看的(两张榜都**按用户训练段的纯多头夏普排序**,没有用测试段挑)", ""]
if known_row:
    h, a, t = known_row
    T.append(f"对照:已知成交额族 `cross_mean(day_std(Amt), 30)` 训练 / 测试 {pc(a['long_ann'])} / {pc(t['long_ann'])},纯多头夏普 {sh(a['long_sharpe'])} / {sh(t['long_sharpe'])},测试段最大回撤 {pc(t['long_mdd'])}。")
T += top(indep, "A. 与已知成交额族相关低于 0.5 的(独立的新东西)",
         "这些可以和已知族并列持有。测试段上单个数字有 ±3 个点 / ±0.3 夏普的噪声,而且一共读了约一百个候选,榜首的数字有向上的选择偏差 —— 看逐年是否稳定比看单个数字可靠。")
T += top(onkn, "B. 建在已知族上的、或实质落在这一族里的(已知族的升级版)",
         "筛子 = 已知族剔掉某类票;分段 = 只在低流动性 40% 里按本因子选;叠加 = 已知族的秩加上本因子的秩。它们和已知族高度相关,是替换而不是并列。")


def cluster_section():
    cp = root / "runs" / f"_batch_{Path(argv[0]).stem.split('_')[0]}" / f"cluster_{TAG}.json"
    if not cp.is_file():
        return []
    K = json.loads(cp.read_text(encoding="utf-8"))
    I, C, O = K["info"], K["corr"], K["overlap"]
    th = K["thresholds"]

    def src(k):
        fid = I[k].get("fid") or ""
        also = I[k].get("also") or []
        return (fid.split("_")[0] if fid else "基准") + (f"(另 {len(also)} 条因子也选到)" if also else "")

    def b(k, sp, m):
        return I[k]["books"][sp][m]

    S = ["", "## 0.5 跨因子:这些候选是几个东西(只用用户训练段)", "",
         f"把 15 条因子按规则选出的 {sum(1 for v in I.values() if v['role'] != 'orig')} 个候选放在一起。**同簇** = 逐日截面秩相关 ≥ {th['rho']:g} 或多头书(前 10%)重合 ≥ {th['overlap']:.0%};"
         "簇按训练段纯多头夏普排,簇首是簇里夏普最高的。筛子把两成股票压到最底,秩相关会掉很多而持有的书几乎不变,所以要同时看重合度。", "",
         "| 簇 | 类 | 簇首来自 | 簇首表达式 | 半衰期 | 多头净超额 训练 / 验证 | 纯多头夏普(训练段) | ρ已知族 / 多头书重合 | 成员 |", "|---|---|---|---|---|---|---|---|---|"]
    for i, c in enumerate(K["clusters"], 1):
        h = c["head"]
        mem = sorted({(I[k].get("fid") or "基准").split("_")[0] for k in c["members"]})
        kc = f"{C[h]['known']:+.2f} / {O[h]['known']:.0%}" if "known" in C[h] else "—"
        S.append(f"| {i} | {'已知族' if c['known_family'] else '**独立**'} | {src(h)} | `{short(I[h]['expr'], 100)}` | {I[h]['hl']:g} | {pc(b(h, 'train', 'long_ann'))} / {pc(b(h, 'valid', 'long_ann'))} "
                 f"| {sh(b(h, 'utrain', 'long_sharpe'))} | {kc} | {len(c['members'])} 个:{' '.join(mem)} |")
    orig = [k for k in K["names"] if I[k]["role"] == "orig"]
    if orig:
        S += ["", "原式各自落在哪:" + ";".join(
            f"{k.split('.')[0]} → " + (f"簇首 `{I[k]['in_cluster']}`" if I[k].get("in_cluster") else f"不属于任何簇(最近 `{I[k]['nearest_head']}` ρ {C[k][I[k]['nearest_head']]:+.2f})")
            for k in orig) + "。"]
    if K["combos"]:
        ho = K.get("holdout_read")
        S += ["", "### 组合书(规则在看结果前写死:成员 z-rank 的等权均值;半衰期在用户训练段上再定)", "",
              "`known_head` = 已知族里最好的簇首单独持有;`indep_eq` = 所有训练段夏普 ≥ " + f"{th['min_sharpe']:g}" + " 的独立簇首等权;`indep_top3` = 其中最好的三个;"
              "`all_eq` = 独立簇首 + 已知族簇首等权;`half_half` = 一半已知族簇首、一半独立簇首的均值。"
              + ("测试段**只读了这一次**(记账在 `runs/_batch_B01/ledger.json`)。" if ho else "**测试段还没读**(等第三轮的候选定下来后只读一次)。"), "",
              "| 组合 | 成员 | 半衰期 | 多头净超额 训练" + (" / 测试" if ho else "") + " | 纯多头夏普 训练" + (" / 测试" if ho else "") + " | 日换手 | 最大回撤 训练" + (" / 测试" if ho else "") + " | 逐年 |", "|---|---|---|---|---|---|---|---|"]
        for name, c in K["combos"].items():
            a, t = c["splits"]["utrain"], c["splits"].get("holdout")
            S.append(f"| `{name}` | {len(c['members'])} 个:{' '.join('`' + m + '`' for m in c['members'])} | {c['hl']:g} | **{pc(a['long_ann'])}" + (f" / {pc(t['long_ann'])}" if t else "") + "** "
                     f"| {sh(a['long_sharpe'])}" + (f" / {sh(t['long_sharpe'])}" if t else "") + f" | {a['long_turnover']:.1%} | {pc(a['long_mdd'])}" + (f" / {pc(t['long_mdd'])}" if t else "")
                     + " | " + " ".join(f"{x:+.0%}" for x in c["by_year_long_net"].values()) + " |")
    if K.get("leave_one_out"):
        S += ["", "`indep_eq` 里每个独立簇首带了多少(训练段;去掉它之后组合掉多少):", "",
              "| 去掉的簇首 | 表达式 | 去掉后 净超额 / 夏普 | 它的贡献 净超额 / 夏普 | 与已知族簇首五五混合(训练段)净超额 / 夏普 |", "|---|---|---|---|---|"]
        for h, r in K["leave_one_out"].items():
            pr = K.get("pair_with_known_head", {}).get(h)
            S.append(f"| `{h}` | `{short(I[h]['expr'], 90)}` | {pc(r['without_long_ann'])} / {sh(r['without_long_sharpe'])} | {r['d_long_ann']:+.1%} / {r['d_long_sharpe']:+.2f} | "
                     + (f"{pc(pr['long_ann'])} / {sh(pr['long_sharpe'])}" if pr else "—") + " |")
    return S


i0 = L.index("## 1. 一张表(多头腿净超额 训练 / 测试;括号里是纯多头夏普)")
L[i0:i0] = T + cluster_section() + [""]
L += ["", "## 2. 逐条", ""] + detail
out.parent.mkdir(parents=True, exist_ok=True)
out.write_text("\n".join(L), encoding="utf-8")
print(f"wrote {out}: {len(batch['factors']) - len(missing)} factors, missing {[x.split('_')[0] for x in missing]}")
