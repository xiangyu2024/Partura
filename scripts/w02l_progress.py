#!/usr/bin/env python3
"""PROD W02L: one JSON snapshot of the run's progress, for the progress dashboard (artifact "W02L 进度看板").
Read-only: looks at research/prod_W02L (arms / loc / stage0 / report.md / makeup files) and at the process table.
   cd $PARTURA_HOME && python3 scripts/w02l_progress.py > tmp/w02l_progress.json
Tables:  stages  (key, step, done, total, unit, state, note)  -- one row per step of the run
         tail    (stream, r1, r2, r3)                          -- the streams with a round not ended, each round's stage
         history (t, rounds_done)                              -- rounds ended over time (the .DONE files' times, UTC)
         summary (asof, heads, b_pass, d_pending, searching, gp_procs)  -- one row
"""
import csv
import datetime as dt
import glob
import json
import os
import re
import subprocess

D = "research/prod_W02L"
N_STAGE0_BLOCKS, N_SPEARMAN, N_MAKEUP_ROUNDS, N_MAKEUP_SLOTS = 698, 22, 33, 37


def utc(ts):
    return dt.datetime.fromtimestamp(ts, dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def procs(pattern):
    out = subprocess.run(["pgrep", "-fa", pattern], capture_output=True, text=True).stdout
    return [l for l in out.splitlines() if "pgrep" not in l and "w02l_progress" not in l]


def pairs(pattern, lines):
    got = set()
    for l in lines:
        m = re.search(pattern, l)
        if m:
            got.add((int(m.group(1)), int(m.group(2))))
    return got


seeds = [int(s["seed"]) for s in json.load(open(f"{D}/streams.json"))["streams"]]
missions = pairs(r"c05_round\.py mission (\d+) P (\d)", procs("c05_round.py mission"))
locating = pairs(r"c05_locate\.py locate (\d+) P (\d)", procs("c05_locate.py locate"))
done, plans, ready = {}, set(), set()
for S in seeds:
    for k in (1, 2, 3):
        f = f"{D}/arms/s{S}_P_r{k}.DONE"
        if os.path.exists(f):
            done[(S, k)] = os.path.getmtime(f)
        if os.path.exists(f"{D}/arms/s{S}_P_r{k}.yaml"):
            plans.add((S, k))
        if os.path.exists(f"{D}/loc/s{S}_P_r{k}.READY"):
            ready.add((S, k))


def stage(S, k):
    if (S, k) in done:
        return "完成"
    if (S, k) in plans:
        return "搜索中"
    if (S, k) in ready:
        return "写计划和审计"
    if (S, k) in locating:
        return "定位中"
    if k == 1 or (S, k - 1) in done:                 # its previous round has ended: the locate is queued (e.g. waiting for the card)
        return "等定位"
    return "等前一轮"


def state(d, t, running=False):
    return "完成" if t and d >= t else ("进行中" if d > 0 or running else "未开始")


# stage 0 and its ts_spearman makeup
chunks = [os.path.basename(p) for p in glob.glob(f"{D}/stage0/chunks/*.jsonl")]
s0 = sum(1 for c in chunks if not c.startswith("sp"))
# ts_spearman members done, by content (the members, not the chunk files: 11-12 the files were named by position and collided)
sp_members = set()
for r in csv.DictReader(open(f"{D}/struct/members.csv", encoding="utf-8")):
    if "ts_spearman" in r["expression"]:
        sp_members.add((r["lib"], int(r["i"])))
have = set()
for f in glob.glob(f"{D}/stage0/chunks/*.jsonl"):
    for ln in open(f, encoding="utf-8"):
        if ln.strip():
            x = json.loads(ln)
            have.add((x.get("lib"), int(x.get("i", -1))))
N_SPEARMAN = len(sp_members)
sp = len(sp_members & have)
sp_running = bool(procs("w02l_stage0.py"))
# ruler D, from the last report (regenerated after each D batch)
heads = b_pass = d_pending = None
try:
    head = open(f"{D}/report.md", encoding="utf-8").read(4000)
    m = re.search(r"新 head[^:]*\*\*:(\d+) 个", head)
    heads = int(m.group(1)) if m else None
    m = re.search(r"尺子 B 过线的 (\d+) 个里，D 没过 (\d+) 个、D 待算 (\d+) 个", head)
    if m:
        b_pass, d_pending = int(m.group(1)), int(m.group(3))
except OSError:
    pass
# ruler D, live: d_scores.jsonl against the pending lists of the makeup passes (tmp/w2tl/d_makeup*.txt)
d_have = set()
if os.path.exists(f"{D}/d_scores.jsonl"):
    for ln in open(f"{D}/d_scores.jsonl", encoding="utf-8"):
        if ln.strip():
            d_have.add(json.loads(ln).get("expr"))
d_want = set()
for f in sorted(os.listdir("tmp/w2tl")) if os.path.isdir("tmp/w2tl") else []:
    if f.startswith("d_makeup") and f.endswith(".txt"):
        d_want |= {x.strip() for x in open(f"tmp/w2tl/{f}", encoding="utf-8") if x.strip()}
d_live_pending = len(d_want - d_have)
d_running = bool(procs("scripts/w02l_backtest.py"))
# the two R groups of MAKEUP.md (finalize dropped them by mistake): 2075 r3 gets its first R file, 2067 r3's is rewritten
A_ = f"{D}/arms"
r_done = int(os.path.exists(f"{A_}/s2075_P_r3_R.json"))
r_done += int(os.path.exists(f"{A_}/s2067_P_r3_R.json.pre_makeup")
              and os.path.getmtime(f"{A_}/s2067_P_r3_R.json") > os.path.getmtime(f"{A_}/s2067_P_r3_R.json.pre_makeup"))
r_running = bool(procs("c05_locate.py direct"))
# makeup
started, mk_done, mk_ok = 0, 0, 0
if os.path.exists(f"{D}/makeup_started.txt"):
    for l in open(f"{D}/makeup_started.txt"):
        m = re.match(r"s(\d+) r(\d) started (\S+)", l.strip())
        if not m:
            continue
        started += 1
        t0 = dt.datetime.strptime(m.group(3), "%Y-%m-%d_%H:%M:%S").timestamp()
        f = f"{D}/arms/s{m.group(1)}_P_r{m.group(2)}.DONE"
        if os.path.exists(f) and os.path.getmtime(f) > t0:        # the round's mission ran again and wrote its DONE
            mk_done += 1
            mk_ok += " 98" not in open(f).read()
makeup_running = bool(procs("w02l_makeup.sh"))
result_done = os.path.exists(f"{D}/RESULT.md")
# the library (scripts/w02l_two_level.py): signals made, then scored, then built
TL = "runs/prod_W02L/two_level"
n_lx = sum(1 for _ in open(f"{D}/struct/members.csv")) - 1
n_w = len(json.load(open(f"{D}/library/heads_D.json"))) if os.path.exists(f"{D}/library/heads_D.json") else 0
lib_total = n_lx + n_w
lib_done = len(os.listdir(f"{TL}/_signals")) if os.path.isdir(f"{TL}/_signals") else 0
lib_note, lib_unit = "信号生成中(原库从缓存读)", "条信号"
if os.path.exists(f"{TL}/score_LX/metrics.csv"):
    SYN = ["C_LX", "C_LX_ng", "C_LXW", "C_LXW_ng", "C_W", "C_W_ng"]          # the six two-level signals of LIBRARY_PLAN section 4
    HJ = f"{D}/library/heads_D.json"                                       # C_W / C_LXW count only once built on the final W02L list

    def after(n):
        t = os.path.getmtime(f"{TL}/score_LX/metrics.csv")
        if "W" in n.split("_")[1]:                                         # the final list: heads_D.json rewritten after the last D
            if not os.path.exists(HJ) or os.path.getmtime(HJ) < os.path.getmtime(f"{D}/d_scores.jsonl") or d_live_pending:
                return False
            t = max(t, os.path.getmtime(HJ))
        return os.path.exists(f"{TL}/{n}.npy") and os.path.getmtime(f"{TL}/{n}.npy") > t
    built = [n for n in SYN if after(n)]
    lib_done, lib_total, lib_unit = len(built), len(SYN), "个合成"
    lib_note = (f"原库已打分;已建 {', '.join(built) if built else '无'}"
                + ("" if len(built) == len(SYN) else "(C_LXW、C_W 等补跑的尺子 D 算完、W02L 名单定下后再建)"))
n_rounds = 3 * len(seeds)

stages = [
    {"key": "stage0", "step": "第 0 步:原库重新打分", "done": s0, "total": N_STAGE0_BLOCKS, "unit": "块",
     "note": "两个冠军库 5583 条按结构分成 698 块，逐块用尺子 A / B 打分"},
    {"key": "spearman", "step": "第 0 步补算:ts_spearman", "done": sp, "total": N_SPEARMAN, "unit": "条",
     "note": "GPU 上补算(空卡、上限 0.9),按成员计数"},
    {"key": "streams", "step": "建流", "done": len(seeds), "total": 80, "unit": "条流", "note": "按结构分的 240 批，每条流 3 批"},
    {"key": "plans", "step": "轮次计划(写好、审计、推送)", "done": len(plans), "total": n_rounds, "unit": "轮",
     "note": "每轮：定位 → 写计划 → 相关度表 → 审计 → 推送"},
    {"key": "rounds", "step": "轮次搜索(跑完)", "done": len(done), "total": n_rounds, "unit": "轮",
     "note": f"在搜索的 {len(plans - set(done))} 轮"},
    {"key": "dscore", "step": "尺子 D 打分", "done": len(d_have), "total": len(d_have) + d_live_pending, "unit": "个候选",
     "note": f"B ≥ 0.3 且 |ρK| < 0.5 的候选;已算 {len(d_have)} 个，补跑产出待算 {d_live_pending} 个"},
    {"key": "makeup", "step": "补跑(坏掉的 GP 任务位)", "done": mk_done, "total": N_MAKEUP_ROUNDS, "unit": "轮",
     "note": f"{N_MAKEUP_SLOTS} 个任务位;已开跑 {started} 轮，跑完 {mk_done} 轮(其中成功 {mk_ok} 轮)"},
    {"key": "rmakeup", "step": "补评 R 组(定稿误删的 2 组)", "done": r_done, "total": 2, "unit": "组",
     "note": "2075 r3 偏度/峰度组 4 个变体;2067 r3 Volume 组 4 个(与已评的 Amt 组 6 个合并重评)"},
    {"key": "library", "step": "建库：信号 → 打分 → 两层合成", "done": lib_done, "total": lib_total, "unit": lib_unit, "note": lib_note},
    {"key": "test", "step": "读一次 2026 测试集", "done": 0, "total": 1, "unit": "", "note": "按事先写好的规则，只读一次"},
    {"key": "result", "step": "写 RESULT.md", "done": int(result_done), "total": 1, "unit": "", "note": "最后一步"},
]
for s in stages:
    s["state"] = state(s["done"], s["total"], running={"spearman": sp_running, "makeup": makeup_running, "dscore": d_running, "rmakeup": r_running}.get(s["key"], False))

tail = []
for S in seeds:
    st = [stage(S, k) for k in (1, 2, 3)]
    if any(x != "完成" for x in st):
        tail.append({"stream": str(S), "r1": st[0], "r2": st[1], "r3": st[2]})

ts = sorted(done.values())
history = [{"t": utc(t), "rounds_done": i + 1} for i, t in enumerate(ts)]
gp_procs = len([l for l in procs("scripts/idea_search.py") if l.split()[1].endswith("python")])
summary = [{"asof": utc(dt.datetime.now().timestamp()), "heads": heads, "b_pass": b_pass, "d_pending": d_pending,
            "searching": len(plans - set(done)), "gp_procs": gp_procs, "rounds_total": n_rounds}]
print(json.dumps({"stages": stages, "tail": tail, "history": history, "summary": summary}, ensure_ascii=False))
