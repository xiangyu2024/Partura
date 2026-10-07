"""The forward-segment read, for a person -- with the judgments of research/forward_2026/PLAN.md applied mechanically.

Local.  Reads runs/_forward/forward_read_<end>.json (scripts/forward_read.py) and writes
research/forward_2026/RESULT.md.  Nothing here decides anything after the fact: every verdict is the rule that
was written down before the read.

    python scripts/forward_report.py [--end 20260916]
"""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]
files = sorted((root / "runs" / "_forward").glob("forward_read_*.json"))
if "--end" in argv:
    files = [root / "runs" / "_forward" / f"forward_read_{argv[argv.index('--end') + 1]}.json"]
R = json.loads(files[-1].read_text(encoding="utf-8"))
end = R["end"]
SEGS = ("insample", "test", "forward", "oos")
pc = lambda x: "—" if x is None or x != x else f"{x:+.1%}"      # noqa: E731
sh = lambda x: "—" if x is None or x != x else f"{x:.2f}"        # noqa: E731
tt = lambda x: "—" if x is None or x != x else f"{x:+.1f}"       # noqa: E731


def d8(x):
    return f"{x[:4]}-{x[4:6]}-{x[6:]}"


def lv(o, seg):
    r = o["level"][seg]
    return f"{pc(r['long_ann'])} / {sh(r['long_sharpe'])}"


def verdict(p):
    """PLAN §1-2: the paired difference on the combined out-of-sample period decides; the forward segment gives the direction."""
    fw, oos = p["forward"]["ann"], p["oos"]["t"]
    if oos >= 2:
        return "**成立**(合并段 t ≥ 2)"
    if fw > 0 and oos >= 1:
        return "方向一致、仍不够(前推段为正,合并段 t 在 1 ~ 2)"
    if fw < 0:
        return "**没有延续**(前推段的差为负)"
    return "前推段为正,但合并段 t < 1:证据仍弱"


F, B, P = R["fusions"], R["benchmarks"], R["paired"]
NAME = {"known": "已知成交额族(基准)", "known_xfrozen": "已知族 + 冻结筛子", "O": "15 条原式等权", "U": "15 条升级版等权", "A": "独立的升级版等权",
        "B": "已知族里最好的升级版(单独)", "C": "独立的升级版 + 已知族最好的一个", "D": "一半已知族最好的一个 + 一半独立的均值"}
PAIR = {"A-known": "独立成员的融合 − 已知族", "C-known": "(独立成员 + 已知族头名)− 已知族", "B-known": "已知族头名 − 已知族", "O-known": "原式的融合 − 已知族",
        "A-O": "独立成员的融合 − 原式的融合", "U-O": "升级版的融合 − 原式的融合", "known_xfrozen-known": "冻结筛子 − 已知族", "A-known_xfrozen": "独立成员的融合 −(已知族 + 冻结筛子)"}
ny = R["forward"][2] / 252.0
L = [f"# 2026 年前推段的读数(截止 {d8(end)})", "",
     f"规则写在读之前:`research/forward_2026/PLAN.md`。前推段 = {d8(R['forward'][0])} ~ {d8(R['forward'][1])},{R['forward'][2]} 个有标签的交易日(约 {ny:.2f} 年);"
     f"样本外合并段 = 2023-08-08 ~ {d8(end)},约 {R['years_oos']:.2f} 年。口径:纯多头十分位、扣 15 bp、相对全市场等权;所有对象的方向、半衰期、成员都是读之前定好的。", "",
     f"**复现检查通过**:{R['check']['objects']} 个对象在延长后的视窗上重算,样本内的年化净超额最大偏差 {R['check']['worst']['train_ann'] * 100:.3f} 个点、夏普 {R['check']['worst']['train_sharpe']:.3f};"
     f"原测试段 {R['check']['worst']['test_ann'] * 100:.3f} 个点、{R['check']['worst']['test_sharpe']:.3f}。", "",
     f"前推段只有 {ny:.2f} 年:一本书自己的夏普,标准误约 ±{(1 / ny) ** 0.5:.1f};所以下面的判读都落在样本外合并段的**成对差**上。", "",
     "## 判读(按事先写下的规则)", "", "__VERDICTS__", "",
     "## 表 1:基准与融合(净超额 / 夏普)", "",
     "| | 样本内 | 原测试段 | **前推段** | 样本外合并段 | 前推段最大回撤 |", "|---|---|---|---|---|---|"]
for k in ("known", "known_xfrozen"):
    L.append(f"| {NAME[k]} | {lv(B[k], 'insample')} | {lv(B[k], 'test')} | **{lv(B[k], 'forward')}** | {lv(B[k], 'oos')} | {pc(B[k]['level']['forward']['long_mdd'])} |")
for k in ("O", "U", "A", "B", "C", "D"):
    nm = NAME[k] + (f"({F[k]['n_members']} 个)" if k in ("A", "C", "D") else "")
    L.append(f"| {nm} | {lv(F[k], 'insample')} | {lv(F[k], 'test')} | **{lv(F[k], 'forward')}** | {lv(F[k], 'oos')} | {pc(F[k]['level']['forward']['long_mdd'])} |")
L += ["", "## 表 2:同一天相减的成对差(每年多赚 / t)", "",
      "| 谁 减 谁 | 样本内 | 原测试段 | **前推段** | **样本外合并段** | 合并段信息比 | 判读 |", "|---|---|---|---|---|---|---|"]
for k in ("A-O", "U-O", "A-known", "C-known", "B-known", "O-known", "known_xfrozen-known", "A-known_xfrozen"):
    if k not in P:
        continue
    p = P[k]
    v = verdict(p) if k in ("A-known", "A-O") else ""
    L.append(f"| {PAIR[k]} | {pc(p['insample']['ann'])} / {tt(p['insample']['t'])} | {pc(p['test']['ann'])} / {tt(p['test']['t'])} | **{pc(p['forward']['ann'])} / {tt(p['forward']['t'])}** | "
             f"**{pc(p['oos']['ann'])} / {tt(p['oos']['t'])}** | {sh(p['oos']['ir'])} | {v} |")
# ---- conventions
C = R["conventions"]
CN = {"user": "原口径", "tradable": "可交易池(基准里去掉垃圾票)", "bucket": "桶内(再按成交额分十档)"}
L += ["", "## 表 3:赚的是哪一种钱(纯多头夏普;对象的方向与半衰期固定)", "",
      "| 对象 | 口径 | 2018–2021 | 2022-01 ~ 2023-08 | 原测试段 | **前推段** | 前推段净超额 |", "|---|---|---|---|---|---|---|"]
for k, nm in (("known", "已知族"), ("O", "原式的融合"), ("A", "独立成员的融合")):
    for c in ("user", "tradable", "bucket"):
        x = C[k][c]
        L.append(f"| {nm} | {CN[c]} | {sh(x['train']['long_sharpe'])} | {sh(x['valid']['long_sharpe'])} | {sh(x['test']['long_sharpe'])} | **{sh(x['forward']['long_sharpe'])}** | {pc(x['forward']['long_ann'])} |")
# ---- members
M = R["members"]
L += ["", "## 表 4:成员各自的表现(描述;不据此增减成员)", "",
      "| 成员 | 组 | 样本内 | 原测试段 | **前推段** |", "|---|---|---|---|---|"]
for grp, gn in (("indep", "独立升级版"), ("orig", "原式"), ("known_head", "已知族头名")):
    for k, v in M.items():
        if grp in v["group"] and not (grp == "orig" and "indep" in v["group"]):
            L.append(f"| `{k}` | {gn} | {lv(v, 'insample')} | {lv(v, 'test')} | **{lv(v, 'forward')}** |")
ind = [v for v in M.values() if "indep" in v["group"]]
org = [v for v in M.values() if "orig" in v["group"]]
pos = lambda vs: sum(v["level"]["forward"]["long_ann"] > 0 for v in vs)     # noqa: E731
# ---- screens
K, E4 = R["k001"], R["e4"]
L += ["", "## 表 5:筛子对已知族的成对差(每年多赚 / t)", "",
      "| 筛子 | 样本内 | 原测试段 | **前推段** | 样本外合并段 |", "|---|---|---|---|---|"]
scr = []
for k, v in K.items():
    if k in ("k_known",):
        continue
    p = v["paired_vs_known"]
    scr.append(p)
    L.append(f"| K001 `{k}` | {pc(p['insample']['ann'])} / {tt(p['insample']['t'])} | {pc(p['test']['ann'])} / {tt(p['test']['t'])} | **{pc(p['forward']['ann'])} / {tt(p['forward']['t'])}** | {pc(p['oos']['ann'])} / {tt(p['oos']['t'])} |")
for r in E4:
    p = r["paired_vs_known"]
    scr.append(p)
    L.append(f"| e4 {r['episode'].split('_')[0]} / {'带指引' if r['arm'] == 'steer' else '对照'} `{r['expr'][:60]}` | {pc(p['insample']['ann'])} / {tt(p['insample']['t'])} | {pc(p['test']['ann'])} / {tt(p['test']['t'])} | "
             f"**{pc(p['forward']['ann'])} / {tt(p['forward']['t'])}** | {pc(p['oos']['ann'])} / {tt(p['oos']['t'])} |")
# ---- the verdicts, in the order of the plan
ak, ao = P["A-known"], P["A-O"]
kn_f = B["known"]["level"]["forward"]
ab = C["A"]["bucket"]["forward"]["long_sharpe"]
n_scr_ok = sum(p["oos"]["t"] >= 2 for p in scr if p["oos"]["t"] == p["oos"]["t"])
n_scr_in = sum(abs(p["forward"]["ann"]) <= 0.015 for p in scr if p["forward"]["ann"] == p["forward"]["ann"])
V = [f"1. **独立成员的融合比已知族好不好**:原测试段每年 {pc(ak['test']['ann'])}(t {tt(ak['test']['t'])});前推段 {pc(ak['forward']['ann'])}(t {tt(ak['forward']['t'])});"
     f"合并段 {pc(ak['oos']['ann'])}、t = {tt(ak['oos']['t'])}。→ {verdict(ak)}",
     f"2. **升级有没有用(独立成员的融合 − 原式的融合)**:原测试段 {pc(ao['test']['ann'])}(t {tt(ao['test']['t'])});前推段 {pc(ao['forward']['ann'])}(t {tt(ao['forward']['t'])});"
     f"合并段 {pc(ao['oos']['ann'])}、t = {tt(ao['oos']['t'])}。→ {verdict(ao)}",
     f"3. **已知族本身**:前推段净超额 {pc(kn_f['long_ann'])}、夏普 {sh(kn_f['long_sharpe'])}、最大回撤 {pc(kn_f['long_mdd'])}。"
     + ("**前推段净超额不为正 —— 整条流动性倾斜在这一段失效,要单独看。**" if not kn_f["long_ann"] > 0 else "流动性倾斜在前推段仍在赚钱。")
     + f" 原式的融合:{lv(F['O'], 'forward')}。",
     f"4. **筛子**:{len(scr)} 个里,前推段的成对差在 ±1.5 个点以内的有 {n_scr_in} 个;合并段 t ≥ 2 的有 {n_scr_ok} 个。"
     + ("和事先的预期一致,这条线维持「已停」。" if n_scr_ok == 0 else "有合并段 t ≥ 2 的,按约定只记下、不改结论,下次增量再看。"),
     f"5. **哪一种钱**:独立成员的融合在桶内口径下,前推段夏普 {sh(ab)}。→ "
     + ("在 ±1 以内:没有可辨认的流动性之外的内容(和事先的预期一致)。" if abs(ab) <= 1 else "≥ 1.5:记为「值得跟」的线索,不作结论。" if ab >= 1.5 else "介于两者之间,不作结论。" if ab > 1 else "明显为负:在同流动性档内它在前推段是亏的。"),
     f"6. **成员**(描述):12 个独立升级版里前推段净超额为正的 {pos(ind)} 个;15 条原式里 {pos(org)} 个。"]
L[L.index("__VERDICTS__")] = "\n".join(V)
L += ["", "## 提醒", "",
      f"- 这是前推段的第一次读数,已记账(`runs/_forward/ledger.json`)。{ny:.2f} 年的样本对任何单个数字都很吵,能用的是方向和合并段的成对差。",
      "- 以后每次按规则的读数都会另起一列报前推段;它仍然只读不选。新的增量日进来会延长它。", ""]
out = root / "research" / "forward_2026" / "RESULT.md"
out.write_text("\n".join(L), encoding="utf-8")
print("\n".join(V))
print(f"\nwrote {out}")
