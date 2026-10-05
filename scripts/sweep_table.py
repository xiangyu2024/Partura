"""Print a batch sweep's backtest table and its market anatomy from the JSONs (local; no server).

    python scripts/sweep_table.py <factor_id> [tag] [--all]     # --all: every variant, not just the top 45
"""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
fid = sys.argv[1]
tag = next((a for a in sys.argv[2:] if not a.startswith("-")), "s1")
ALL = "--all" in sys.argv
sp = root / "runs" / fid / f"sweep_{tag}.json"
if not sp.is_file():
    raise SystemExit(f"还没有 {sp.name}(这条因子的批量扫描 {tag} 没跑完)")
S = json.loads(sp.read_text(encoding="utf-8"))
R = {k: v for k, v in S["results"].items() if not v.get("dead")}


def fmt(x, pct=True):
    return "   —  " if x is None or x != x else (f"{x:+6.1%}" if pct else f"{x:+5.2f}")


def key(k):
    x = R[k]["utrain_long"]["long_sharpe"]
    return -(x if x == x else -9)


def line(k):
    v = R[k]
    a, b, c = v["train_long"], v["valid_long"], v["utrain_long"]
    gate = "  " if (v["cov"] >= 0.95 and v["dist"] >= 0.5) else " ✗"
    return (f"{k[:22]:22s} {v['kind'][:8]:8s} {int(v['sign']):+d} {v['hl_long']:>3g} | {fmt(a['long_ann'])} {fmt(b['long_ann'])} {fmt(c['long_ann'])} "
            f"| {fmt(a['long_sharpe'], 0)} {fmt(b['long_sharpe'], 0)} {fmt(c['long_sharpe'], 0)} | {a['long_turnover']:5.1%} "
            f"| {fmt(v['train_ls']['ls_sharpe'], 0)} {fmt(v['valid_ls']['ls_sharpe'], 0)} | {fmt(a['short_gross_ann'])} {fmt(b['short_gross_ann'])} "
            f"| {v['corr_orig']:+.2f} {v['corr_known']:+.2f} | {v['cov']:.2f} {v['dist']:.2f}{gate} | {v['expr'][:150]}")


order = sorted(R, key=key)
print(f"== {fid}  批量扫描 {tag}:{len(R)} 个变体(只用 train 2018–2021 / valid 2022–202308;方向 sg 与半衰期 hlL 在 train 上定,半衰期按纯多头书选)==")
print("Lnet = 多头腿净超额(扣 15bp,年化),Lshp = 纯多头夏普:train | valid | utrain(用户训练段);LTO = 多头日换手;LS = 多空夏普;")
print("空头腿 = 等权 − 最低十分位(毛,年化):大 = 钱在空头腿(纯多头用不上);为负 = 最低十分位反而跑赢,值得把方向反过来看。")
print("ρo / ρk = 交易信号与原式 / 已知成交额族的 rank 相关;✗ = 没过门槛(cov ≥ 0.95、dist ≥ 0.5),不能当候选。")
print(f"{'id':22s} {'kind':8s} sg hlL | Lnet tr     va     ut   | Lshp tr    va    ut  | LTO   | LS tr   va  | 空头腿 tr   va   |  ρo    ρk  | cov  dist   | expr")
for k in ("v_base", "k_known"):
    if k in R:
        print(line(k))
print("-" * 40 + (" 全部变体,按 utrain 纯多头夏普排序" if ALL else " 按 utrain 纯多头夏普排序的前 45 个(--all 看全部)"))
for k in (order if ALL else order[:45]):
    print(line(k))
if not ALL:
    print("-" * 40 + " 每一类里最好的 3 个")
    for kind in dict.fromkeys(v["kind"] for v in R.values()):
        for k in [x for x in order if R[x]["kind"] == kind][:3]:
            print(line(k))
    print("-" * 40 + " 垫底的 8 个")
    for k in order[-8:]:
        print(line(k))
if S.get("errors"):
    print(f"求值失败 {len(S['errors'])} 个:" + ", ".join(list(S["errors"])[:12]))

ap = root / "runs" / fid / f"anatomy_{tag}.json"
if not ap.is_file():
    raise SystemExit("\n(这条因子的市场解剖还没跑完)")
A = json.loads(ap.read_text(encoding="utf-8"))
cols = A["ids"]


def f1(x):
    return "   — " if x is None or x != x else f"{x:+5.1%}"


print(f"\n== {fid} 市场解剖(用户训练段 {A['split'][0]}–{A['split'][1]};交易信号 = 方向×面板,多头口径半衰期;没有读测试段)==")
for i, k in enumerate(cols):
    s = A["signals"][k]
    print(f"  [{i}] {k:20s} hl {s['hl']:>3g}  全市场多头净超额 {f1(s['all']['long_ann'])} 夏普 {s['all']['long_sharpe']:+.2f} | {s['expr'][:120]}")
print("\n-- 按股票范围:只在这一段里建多头书的净超额(相对这一段的等权);括号 = 全市场多头书在这一段的持仓占比 − 这一段占全市场的比例")
print("   「段等权超额」= 这一段的等权相对全市场等权:段内净超额 + 段等权超额 ≈ 只做这一段时相对全市场的超额")
print(f"{'段':26s} {'占比':>5s} {'段等权超额':>8s} | " + " | ".join(f"[{i}]".center(15) for i in range(len(cols))))
for name, g in A["segments"].items():
    print(f"{name:26s} {g['share']:5.1%} {f1(g['ew_excess']):>8s} | " +
          " | ".join(f"{f1(A['signals'][k]['seg'][name]['in_long_ann'])} ({A['signals'][k]['seg'][name]['tilt']:+5.1%})" for k in cols))
print("\n-- 按时间 / 市场状态(收盘时已知):全市场多头书的净超额(年化)")
t0 = A["signals"][cols[0]]["time"]
print(f"{'时段':26s} {'天数':>5s} | " + " | ".join(f"[{i}]".center(7) for i in range(len(cols))))
for name in t0:
    print(f"{name:26s} {t0[name]['days']:5d} | " + " | ".join(f"{f1(A['signals'][k]['time'][name]['long_ann']):>7s}" for k in cols))
