"""Re-read a finished study's holdout numbers under the selection convention (the long leg).

The first studies of batch B01 were written while tables were long/short-first:
half-life fitted by L/S Sharpe, the long leg quoted at that half-life.  The user
then fixed the selection criterion -- net long-leg excess, half-life fitted for
the pure long book -- and every candidate's numbers under THAT convention were
already stored by the one holdout read (``books_user``).  This prints them and
appends a clearly marked addendum to ``notes/<fid>/10_distilled.md``.  It reads
no data: nothing here touches the holdout again.

    python scripts/long_reread.py <factor_id> [--write]
"""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
fid = sys.argv[1]
write = "--write" in sys.argv
MARK = "### 附:按选拔口径(多头腿)重读"


def views(b):
    if "by_rank" in b:
        return b["by_rank"]
    return {"ls": {"hl": b["hl_ls"], "splits": b["splits"]},
            "long": {"hl": b["hl_long"], "splits": b.get("splits_at_hl_long") or b["splits"]}}


d = json.loads((root / "runs" / fid / "final.json").read_text(encoding="utf-8"))
us = d.get("user_split", "utrain")
rows = []
for vid, r in d["results"].items():
    if "books_user" not in r or "holdout" not in r["books_user"]["splits"]:
        continue
    v = views(r["books_user"])
    rows.append((vid, r["expr"], v))
orig = next((x for x in rows if x[0] in ("f_orig", "f_base", "v_base")), None) or \
    min(rows, key=lambda x: 0 if "orig" in x[0] else 1)
rows.sort(key=lambda x: -(x[2]["long"]["splits"][us].get("long_sharpe") or -9))


def pc(x):
    return "—" if x is None or x != x else f"{x:+.1%}"


def sh(x):
    return "—" if x is None or x != x else f"{x:+.2f}"


L = [MARK, "",
     "> **2026-10-04 口径更新。** 用户明确:做的是 A 股纯多头,**选拔看多头腿净超额与纯多头夏普;延长半衰期带来的多头腿"
     "净超额是有效的、可交易的改进**。下表是读留出段那一次(`final.json`)里**已经存下**的数,按「半衰期由纯多头书在用户"
     "训练段上选」重读 —— 没有再读留出段。排序按用户训练段的纯多头夏普,是按新口径的机械排序,**不是**研究事前登记的推荐"
     "(那个见上文)。", "",
     "| 候选 | 半衰期(多头) | **多头腿净超额** 训练/测试 | 纯多头夏普 训练/测试 | 多头腿毛超额 训练/测试 | 多头日换手 | 扣费多空夏普@多空半衰期 训练/测试 |",
     "|---|---|---|---|---|---|---|"]
ov = orig[2]
a, h = ov["ls"]["splits"][us], ov["ls"]["splits"]["holdout"]
L.append(f"| _原式,多空口径的半衰期 {ov['ls']['hl']:g}(用户最早那张表的口径)_ | {ov['ls']['hl']:g} "
         f"| {pc(a['long_ann'])} / {pc(h['long_ann'])} | {sh(a['long_sharpe'])} / {sh(h['long_sharpe'])} "
         f"| {pc(a['long_gross_ann'])} / {pc(h['long_gross_ann'])} | {a['long_turnover']:.1%} "
         f"| {sh(a['ls_sharpe'])} / {sh(h['ls_sharpe'])} |")
for vid, expr, v in rows:
    x, y = v["long"]["splits"][us], v["long"]["splits"]["holdout"]
    p, q = v["ls"]["splits"][us], v["ls"]["splits"]["holdout"]
    name = "**原式**" if vid == orig[0] else f"`{vid}`"
    e = expr if len(expr) <= 66 else expr[:63] + "..."
    L.append(f"| {name} `{e}` | {v['long']['hl']:g} | **{pc(x['long_ann'])} / {pc(y['long_ann'])}** "
             f"| {sh(x['long_sharpe'])} / {sh(y['long_sharpe'])} | {pc(x['long_gross_ann'])} / {pc(y['long_gross_ann'])} "
             f"| {x['long_turnover']:.1%} | {sh(p['ls_sharpe'])} / {sh(q['ls_sharpe'])} |")
ol = ov["long"]
top = rows[0]
L += ["",
      f"- **只换半衰期**:原式把半衰期从 {ov['ls']['hl']:g}(为多空选的)换成 {ol['hl']:g}(为多头选的),多头腿净超额 "
      f"训练 {pc(a['long_ann'])} → {pc(ol['splits'][us]['long_ann'])}、测试 {pc(h['long_ann'])} → {pc(ol['splits']['holdout']['long_ann'])}。"
      + ("(两种规则选到同一个半衰期,没有可挪的空间。)" if ov['ls']['hl'] == ol['hl'] else ""),
      f"- **用户训练段上纯多头夏普最高的候选**是 {'原式' if top[0] == orig[0] else '`' + top[0] + '`'}"
      f"(半衰期 {top[2]['long']['hl']:g}):测试段多头腿净超额 {pc(top[2]['long']['splits']['holdout']['long_ann'])}、"
      f"纯多头夏普 {sh(top[2]['long']['splits']['holdout']['long_sharpe'])};"
      f"原式(多头口径)是 {pc(ol['splits']['holdout']['long_ann'])}、{sh(ol['splits']['holdout']['long_sharpe'])}。"
      f"测试段上的噪声大约是净超额 ±3 个点、夏普 ±0.3。", ""]
text = "\n".join(L)
print(text)
if write:
    p = root / "notes" / fid / "10_distilled.md"
    old = p.read_text(encoding="utf-8") if p.is_file() else ""
    if MARK in old:
        old = old[:old.index(MARK)].rstrip() + "\n"
    p.write_text(old.rstrip() + "\n\n" + text, encoding="utf-8")
    print(f"\n[appended to {p}]")
