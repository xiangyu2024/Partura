#!/usr/bin/env python3
"""PROD W02L: one JSON snapshot of the run's progress, for the progress dashboard (artifact "W02L 进度看板").
Read-only: looks at research/prod_W02L (arms / loc / stage0 / report.md / makeup files) and at the process table.
   cd $PARTURA_HOME && python3 scripts/w02l_progress.py > tmp/w02l_progress.json
Tables:  stages  (key, step, done, total, unit, state, note)  -- one row per step of the run
         tail    (stream, r1, r2, r3)                          -- the streams with a round not ended, each round's stage
         history (t, rounds_done)                              -- rounds ended over time (the .DONE files' times, UTC)
         summary (asof, heads, b_pass, d_pending, searching, gp_procs)  -- one row
"""
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
    return "等前一轮"


def state(d, t, running=False):
    return "完成" if t and d >= t else ("进行中" if d > 0 or running else "未开始")


# stage 0 and its ts_spearman makeup
chunks = [os.path.basename(p) for p in glob.glob(f"{D}/stage0/chunks/*.jsonl")]
s0 = sum(1 for c in chunks if not c.startswith("sp"))
sp = sum(1 for c in chunks if c.startswith("sp"))
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
# makeup
started = 0
if os.path.exists(f"{D}/makeup_started.txt"):
    started = sum(1 for l in open(f"{D}/makeup_started.txt") if l.strip())
makeup_running = bool(procs("w02l_makeup.sh"))
result_done = os.path.exists(f"{D}/RESULT.md")
n_rounds = 3 * len(seeds)

stages = [
    {"key": "stage0", "step": "第 0 步:原库重新打分", "done": s0, "total": N_STAGE0_BLOCKS, "unit": "块",
     "note": "两个冠军库 5583 条按结构分成 698 块，逐块用尺子 A / B 打分"},
    {"key": "spearman", "step": "第 0 步补算:ts_spearman", "done": sp, "total": N_SPEARMAN, "unit": "条",
     "note": "CPU 上算，很慢;GPU 空出来后再挪过去"},
    {"key": "streams", "step": "建流", "done": len(seeds), "total": 80, "unit": "条流", "note": "按结构分的 240 批，每条流 3 批"},
    {"key": "plans", "step": "轮次计划(写好、审计、推送)", "done": len(plans), "total": n_rounds, "unit": "轮",
     "note": "每轮：定位 → 写计划 → 相关度表 → 审计 → 推送"},
    {"key": "rounds", "step": "轮次搜索(跑完)", "done": len(done), "total": n_rounds, "unit": "轮",
     "note": f"在搜索的 {len(plans - set(done))} 轮"},
    {"key": "dscore", "step": "尺子 D 打分", "done": (b_pass - d_pending) if b_pass is not None else 0,
     "total": b_pass or 0, "unit": "个候选", "note": "尺子 B 过线的候选，截至上次回测报告"},
    {"key": "makeup", "step": "补跑(坏掉的 GP 任务位)", "done": started, "total": N_MAKEUP_ROUNDS, "unit": "轮",
     "note": f"{N_MAKEUP_SLOTS} 个任务位;全部轮次结束后再跑(用户定)"},
    {"key": "library", "step": "建库(去重、检查、合成)", "done": 0, "total": 1, "unit": "", "note": "补跑之后"},
    {"key": "test", "step": "读一次 2026 测试集", "done": 0, "total": 1, "unit": "", "note": "按事先写好的规则，只读一次"},
    {"key": "result", "step": "写 RESULT.md", "done": int(result_done), "total": 1, "unit": "", "note": "最后一步"},
]
for s in stages:
    s["state"] = state(s["done"], s["total"], running={"spearman": sp_running, "makeup": makeup_running}.get(s["key"], False))

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
