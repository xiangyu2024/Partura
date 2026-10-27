"""C01: the evidence Partura gets before writing the guidance of round k -- its OWN arm only (research/coldstart_C01/PLAN.md §2.6).

Local.  Reads episodes/c01r<j>s<seed>*/evidence.json for every round j < k (pull them first: ./scripts/study.sh idea-pull):
round 1 is the shared blind search (arm "control", the same draws the B arm would have made); later rounds are the B arm
(tag suffix "B", arm "steer").  The A arm of rounds >= 2 is never read here -- a deployed Partura has no control.

    python scripts/c01_digest.py <k>      -> research/coldstart_C01/digest_r<k>.md and .json
"""
import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
D = ROOT / "research" / "coldstart_C01"
K = int(sys.argv[1])
LINE = 1.0
OPS = re.compile(r"[A-Za-z_][A-Za-z_0-9]*(?=\()")
LEAVES = ("Open", "High", "Low", "Close", "Vwap", "Volume", "Amt", "Ret")


def b_arm_runs(j):
    """(path, arm) of the B arm's runs in round j."""
    if j == 1:
        return [(p, "control") for p in sorted((ROOT / "episodes").glob("c01r1s*_*/evidence.json"))]
    return [(p, "steer") for p in sorted((ROOT / "episodes").glob(f"c01r{j}s*B_*/evidence.json"))]


def fin(x):
    return isinstance(x, (int, float)) and math.isfinite(x)


def ops_of(e):
    return OPS.findall(e)


def leaves_of(e):
    return [t for t in re.findall(r"[A-Za-z_]+", e) if t in LEAVES]


runs, cands = [], []
for j in range(1, K):
    for p, arm in b_arm_runs(j):
        E = json.loads(p.read_text(encoding="utf-8"))
        A = E["arms"].get(arm)
        if A is None:
            continue
        heads = {h["expr"] for h in A.get("heads", [])}
        runs.append({"round": j, "episode": p.parent.name, "seed": E["seed"], "idea": E["idea"]["id"], "guidance": E["guidance"],
                     "scored": A["scored"], "gate_fail_share": A["gate_fail"] / max(A["scored"], 1), "live": A["live"],
                     "passers": A["passers"], "heads": len(heads), "heads_per_100": 100.0 * len(heads) / max(A["scored"], 1),
                     "seconds": round(A["seconds"]), "sampling": A.get("sampling", {}), "error": A.get("error")})
        for c in A["candidates"]:
            if not fin(c.get("score")):
                continue
            cands.append({"round": j, "seed": E["seed"], "idea": E["idea"]["id"], "expr": c["expr"], "score": c["score"],
                          "train": c.get("train"), "valid": c.get("valid"), "hl": c.get("hl"), "sign": c.get("sign"),
                          "turnover": c.get("turnover"), "rho_known": c.get("rho_known"), "rho_pool": c.get("rho_pool"),
                          "head": c["expr"] in heads, "pass": c["score"] >= LINE})
# failed B-arm runs of earlier rounds (exit codes from the server's rN.exit / rNrerun.exit, pulled into this folder;
# a rerun's code overrides the first attempt's) -- PLAN §6 revision 2: a B run that still fails counts as 0 discoveries
failed = []
for j in range(1, K):
    status = {}
    for f in (D / f"r{j}.exit", D / f"r{j}rerun.exit"):
        if f.is_file():
            for line in f.read_text().split("\n"):
                if line.strip():
                    tag, code = line.split()[:2]
                    if j == 1 or tag.endswith("B"):
                        status[tag] = int(code)
    for tag, code in sorted(status.items()):
        if code != 0:
            logs = sorted((D / "failures").glob(f"{tag}.fail*.log"))
            why = ""
            for lg in logs:
                txt = lg.read_text(errors="replace")
                hit = [x for x in txt.split("\n") if ("Error" in x or "exit" in x or "No space" in x or "Not enough free space" in x)]
                why += (hit[-1] if hit else "") + " "
            failed.append({"round": j, "tag": tag, "exit": code, "why": why.strip()[:300]})
if not runs:
    raise SystemExit(f"no B-arm evidence for rounds < {K}: pull it first (./scripts/study.sh idea-pull)")

cands.sort(key=lambda c: -c["score"])
passers = [c for c in cands if c["pass"]]
heads = [c for c in cands if c["head"]]


def lift(key):
    """How much more often an operator / leaf appears among passers than among all saved candidates."""
    allc, pas = Counter(), Counter()
    for c in cands:
        for x in set(key(c["expr"])):
            allc[x] += 1
            if c["pass"]:
                pas[x] += 1
    n, m = len(cands), max(len(passers), 1)
    rows = [(x, allc[x], pas[x], (pas[x] / m) / (allc[x] / n)) for x in allc if allc[x] >= 3]
    return sorted(rows, key=lambda r: -r[3])


out = {"round_to_write": K, "runs": runs, "failed": failed, "n_candidates": len(cands), "n_passers": len(passers), "n_heads": len(heads),
       "heads": heads, "passers_top": passers[:60], "nonpassers_top": [c for c in cands if not c["pass"]][:30],
       "op_lift": lift(ops_of), "leaf_lift": lift(leaves_of)}
(D / f"digest_r{K}.json").write_text(json.dumps(out, ensure_ascii=False, indent=1, default=float), encoding="utf-8")


def f(x, nd=2):
    return f"{x:+.{nd}f}" if fin(x) else "—"


L = [f"# C01 证据摘要:写第 {K} 轮指引之前(只含 B 臂自己的运行)", "",
     f"运行 {len(runs)} 次;存下的候选 {len(cands)} 个(每次运行最多存 80 个);score ≥ {LINE:g} 的 {len(passers)} 个;"
     f"互不相关且不在已知族里的 heads {len(heads)} 个。score = 纯多头十分位书扣 15bp 后 train 与 valid 夏普中较差的那个。", "",
     "## 每次运行", "", "| 轮 | 种子 | idea | 付费评估 | 门槛废品率 | 通过 | heads | 每百次 heads | 秒 | 采样统计 |", "|---|---|---|---|---|---|---|---|---|---|"]
for r in runs:
    L.append(f"| R{r['round']} | {r['seed']} | {r['idea']} | {r['scored']} | {100 * r['gate_fail_share']:.0f}% | {r['passers']} | {r['heads']} | "
             f"{r['heads_per_100']:.1f} | {r['seconds']} | {json.dumps(r['sampling'], ensure_ascii=False)} |")
if failed:
    L += ["", "## 失败的运行(按 PLAN §6 修订 2:重跑后仍失败的 B 运行,该种子的发现记为 0)", "", "| 轮 | 任务 | 退出码 | 原因(日志摘录) |", "|---|---|---|---|"]
    for x in failed:
        L.append(f"| R{x['round']} | {x['tag']} | {x['exit']} | {x['why']} |")
L += ["", "运行时间:见上表「秒」一列。注意:分钟级跨股票截面算子(nt_cs_* / nt_ts_*)与日内折叠混用的表达式,"
      "引擎要把整块 (股票, 日, 分钟) 中间量落盘,每个节点约 6.8 GB,并且很慢;R2 有一次运行因此写满数据盘。"]
L += ["", "## heads(互不相关、|ρ| 对已知族与 pool 都 < 0.5)", "", "| 轮 | 种子 | score | train | valid | 半衰期 | 方向 | 换手 | ρ已知 | 表达式 |", "|---|---|---|---|---|---|---|---|---|---|"]
for c in heads:
    L.append(f"| R{c['round']} | {c['seed']} | {f(c['score'])} | {f(c['train'])} | {f(c['valid'])} | {c['hl']:g} | {c['sign']:+g} | {c['turnover']:.3f} | {f(c['rho_known'])} | `{c['expr']}` |")
L += ["", "## 通过门槛的前 60 个(含与 heads 相关或与已知族相关的)", "", "| 轮 | 种子 | score | train | valid | 半衰期 | 换手 | ρ已知 | head | 表达式 |", "|---|---|---|---|---|---|---|---|---|---|"]
for c in passers[:60]:
    L.append(f"| R{c['round']} | {c['seed']} | {f(c['score'])} | {f(c['train'])} | {f(c['valid'])} | {c['hl']:g} | {c['turnover']:.3f} | {f(c['rho_known'])} | {'是' if c['head'] else ''} | `{c['expr']}` |")
L += ["", "## 没过线里分数最高的 30 个(对照用)", "", "| 轮 | 种子 | score | train | valid | ρ已知 | 表达式 |", "|---|---|---|---|---|---|---|"]
for c in out["nonpassers_top"]:
    L.append(f"| R{c['round']} | {c['seed']} | {f(c['score'])} | {f(c['train'])} | {f(c['valid'])} | {f(c['rho_known'])} | `{c['expr']}` |")
for name, rows in (("算子", out["op_lift"]), ("叶子字段", out["leaf_lift"])):
    L += ["", f"## {name}在通过者里的富集(出现 ≥ 3 次的;lift = 通过者中占比 ÷ 全部存下的候选中占比)", "", f"| {name} | 全部 | 通过 | lift |", "|---|---|---|---|"]
    for x, a, p, lf in rows[:25] + ([("…", 0, 0, float("nan"))] if len(rows) > 35 else []) + rows[-10:] * (len(rows) > 35):
        L.append(f"| {x} | {a} | {p} | {lf:.2f} |" if x != "…" else "| … | | | |")
L += ["", "注意:存下的候选只是每次运行 archive 里按适应度排前 80 的,不是全部提议;门槛废品不在里面。"]
(D / f"digest_r{K}.md").write_text("\n".join(L) + "\n", encoding="utf-8")
print(f"wrote {D / f'digest_r{K}.md'}: {len(runs)} runs, {len(cands)} candidates, {len(passers)} passers, {len(heads)} heads")
