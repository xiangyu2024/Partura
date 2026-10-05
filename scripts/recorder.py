"""The recorder: keep every study resumable by someone else -- including another model.

An agent doing a study can be cut off at any moment (usage limit, network, the Mac going
to sleep), and whoever continues may be a different model with no memory of the first.
What an agent THOUGHT is not recoverable from its transcript (reasoning is not stored in
readable form) -- only what it wrote down survives.  So the record has two halves:

* the agent keeps a research journal, ``notes/<fid>/journal.md`` (study_playbook.md §7;
  ``study.sh note``), and writes its notes stage by stage instead of at the end;
* this script, which needs no model and no quota, snapshots everything else:

  handoff/<fid>/results/<phase>.json   every structured result an agent returned to a workflow
  handoff/<fid>/agents/<phase>_<id>.md what each agent did: commands, outputs, files written, in order
  handoff/<fid>/STATE.md               the briefing for whoever takes over (also: study.sh brief <fid>)
  handoff/STATUS.md                    the batch board + how to restart

    python scripts/recorder.py                  # one snapshot of everything
    python scripts/recorder.py --loop 180       # keep snapshotting every 180 s (run it detached)
    python scripts/recorder.py --brief <fid>    # refresh one study's briefing and print it
    python scripts/recorder.py --state [batch]  # machine-readable state of each factor (JSON, for restarts)

It only reads the agents' transcripts and the project's own files, and only writes under
handoff/.  Nothing here touches the server.
"""
from __future__ import annotations

import glob
import json
import os
import re
import sys
import time
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
HAND = ROOT / "handoff"
WF_GLOB = os.environ.get("PARTURA_WF_GLOB", str(Path.home() / ".claude/projects/*/*/subagents/workflows/wf_*"))
# study / audit* / revise return the structured results; lead / work are the rounds of the tiered workflow
LABEL = re.compile(r"^(study|audit|audit-numbers|audit-mechanism|revise|lead|work|revise-lead|revise-work|synth)[:：]\s*(F\d+\w*)(?:#(\d+))?")
RESULT_FILE = {"study": "study.json", "audit": "audit.json", "audit-numbers": "audit-numbers.json",
               "audit-mechanism": "audit-mechanism.json", "revise": "revised.json",
               "synth": "synthesis.json"}        # the one-pass synthesis of a batch sweep (workflows/partura_batch_synthesis.js)
STALE_S = 20 * 60          # an agent with no result and no activity for this long is presumed cut off
FULL_OUTPUT = re.compile(r"study\.sh\s+(wait|digest|final|run|exec|list|brief|note|check)\b")


def local(ts: str | float | None) -> str:
    if ts is None:
        return "?"
    if isinstance(ts, (int, float)):
        return datetime.fromtimestamp(ts).strftime("%m-%d %H:%M")
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().strftime("%m-%d %H:%M")
    except Exception:
        return str(ts)[:16]


STAMP = re.compile(r"_自动生成于 [0-9: -]+")


def write_if_changed(path: Path, text: str) -> bool:
    """Atomic write; a file that differs only in its 'generated at' stamp is left alone."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.is_file() and STAMP.sub("", path.read_text(encoding="utf-8")) == STAMP.sub("", text):
        return False
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(text, encoding="utf-8")
    tmp.replace(path)
    return True


def batches() -> dict:
    """fid -> {expr, lib, name, batch} for every factor of every batch file."""
    import yaml
    out = {}
    for p in sorted((ROOT / "batches").glob("*.yaml")):
        try:
            d = yaml.safe_load(p.read_text(encoding="utf-8"))
        except Exception:
            continue
        for f in (d or {}).get("factors", []) or []:
            if isinstance(f, dict) and "id" in f and "expr" in f:
                out[f["id"]] = {**f, "batch": p.stem}
    return out


# --------------------------------------------------------------------------- workflow runs

def scan_runs() -> list:
    """Every workflow run dir -> its agents: [{run, agent, label, phase, fid, status, result, transcript}]."""
    agents = []
    for d in sorted(glob.glob(WF_GLOB), key=os.path.getmtime):
        run = os.path.basename(d)
        started, results, failed = {}, {}, set()
        j = os.path.join(d, "journal.jsonl")
        if os.path.isfile(j):
            for line in open(j, encoding="utf-8"):
                try:
                    r = json.loads(line)
                except Exception:
                    continue
                a = r.get("agentId")
                if r.get("type") == "started":
                    started[a] = r
                elif r.get("type") == "result":
                    results[a] = r.get("result")
                elif r.get("type") == "failed":
                    failed.add(a)
        for t in sorted(glob.glob(os.path.join(d, "agent-*.jsonl"))):
            aid = os.path.basename(t)[len("agent-"):-len(".jsonl")]
            label = (started.get(aid) or {}).get("label")
            if not label:
                try:
                    label = json.load(open(t.replace(".jsonl", ".meta.json"), encoding="utf-8")).get("description", "")
                except Exception:
                    label = ""
            m = LABEL.match(label or "")
            if not m:
                continue
            st = os.stat(t)
            if aid in results and results[aid] is not None:
                status = "returned"
            elif aid in failed:
                status = "failed"
            elif time.time() - st.st_mtime > STALE_S:
                status = "cut-off"
            else:
                status = "running"
            agents.append({"run": run, "agent": aid, "label": label, "phase": m.group(1), "fid": m.group(2),
                           "round": m.group(3),
                           "status": status, "result": results.get(aid), "transcript": t,
                           "mtime": st.st_mtime, "size": st.st_size})
    agents.sort(key=lambda a: a["mtime"])      # oldest first: the last one is whoever touched the study most recently
    return agents


# --------------------------------------------------------------------------- one agent's transcript

def _text_of(content) -> str:
    if isinstance(content, str):
        return content
    if isinstance(content, list):
        return "\n".join(b.get("text", "") if isinstance(b, dict) else str(b) for b in content)
    return "" if content is None else str(content)


def _clip(text: str, head: int, tail: int, max_chars: int) -> str:
    lines = text.splitlines()
    if len(lines) > head + tail + 5:
        lines = lines[:head] + [f"… ({len(lines) - head - tail} 行略) …"] + lines[-tail:]
    out = "\n".join(lines)
    if len(out) > max_chars:
        out = out[:max_chars * 2 // 3] + f"\n… ({len(out) - max_chars} 字符略) …\n" + out[-max_chars // 3:]
    return out


def agent_log(a: dict) -> str:
    rows = []
    for line in open(a["transcript"], encoding="utf-8"):
        try:
            rows.append(json.loads(line))
        except Exception:
            continue
    results, prompt, events = {}, [], []
    for r in rows:
        msg = r.get("message") if isinstance(r.get("message"), dict) else None
        if not msg:
            continue
        c = msg.get("content")
        if r.get("type") == "user":
            if isinstance(c, str):
                prompt.append(c)
            elif isinstance(c, list):
                for b in c:
                    if isinstance(b, dict) and b.get("type") == "tool_result":
                        results[b.get("tool_use_id")] = _text_of(b.get("content"))
        elif r.get("type") == "assistant" and isinstance(c, list):
            for b in c:
                if not isinstance(b, dict):
                    continue
                if b.get("type") == "text" and (b.get("text") or "").strip():
                    events.append((r.get("timestamp"), "text", b["text"].strip()))
                elif b.get("type") == "tool_use":
                    events.append((r.get("timestamp"), "tool", b))
    first = rows[0].get("timestamp") if rows else None
    last = next((r.get("timestamp") for r in reversed(rows) if r.get("timestamp")), None)
    n_tools = sum(1 for e in events if e[1] == "tool")
    zh = {"returned": "已返回结果", "failed": "失败(没有返回结果)", "running": "还在跑",
          "cut-off": "中断了(没有返回结果,也已经很久没有动静)"}[a["status"]]
    L = [f"# {a['label']} — agent {a['agent']}(工作流 {a['run']})", "",
         f"- 状态:**{zh}**;开始 {local(first)},最后一次动作 {local(last)};工具调用 {n_tools} 次",
         "- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——",
         f"  它的判断要看 `notes/{a['fid']}/journal.md` 和各 notes 文件。输出过长的地方截了中间。", ""]
    files = []
    L.append("## 动作流水")
    L.append("")
    for ts, kind, b in events:
        if kind == "text":
            L += [f"**{local(ts)} · agent 的话**", "", b, ""]
            continue
        name, inp = b.get("name"), b.get("input") or {}
        res = results.get(b.get("id"))
        if name == "Bash":
            cmd = (inp.get("command") or "").strip()
            L += [f"**{local(ts)} · Bash** — {inp.get('description', '')}", "", "```bash", _clip(cmd, 40, 10, 3000), "```"]
            if res is not None:
                full = bool(FULL_OUTPUT.search(cmd))
                L += ["", "```", _clip(res, 260 if full else 30, 60 if full else 20, 40000 if full else 5000), "```"]
            L.append("")
        elif name in ("Write", "Edit", "NotebookEdit"):
            p = inp.get("file_path", "?")
            files.append(p)
            if name == "Write":
                L += [f"**{local(ts)} · 写文件** `{p}`({len(inp.get('content') or '')} 字符)", ""]
            else:
                L += [f"**{local(ts)} · 改文件** `{p}`", "", "```",
                      "- " + _clip(inp.get("old_string") or "", 6, 2, 500),
                      "+ " + _clip(inp.get("new_string") or "", 14, 4, 1500), "```", ""]
        elif name == "Read":
            L.append(f"{local(ts)} · 读 `{inp.get('file_path', '?')}`")
            L.append("")
        else:
            body = json.dumps(inp, ensure_ascii=False, indent=1)
            L += [f"**{local(ts)} · {name}**", "", "```json", _clip(body, 400, 50, 60000), "```", ""]
            if res:
                L += ["```", _clip(res, 20, 10, 2500), "```", ""]
    if files:
        seen = []
        for p in files:
            if p not in seen:
                seen.append(p)
        L += ["## 它写过 / 改过的文件", ""] + [f"- `{p}`" for p in seen] + [""]
    if a.get("result") is not None:
        if a["phase"] in RESULT_FILE:
            L += ["## 它返回给工作流的结构化结果", "", f"见 `handoff/{a['fid']}/results/{RESULT_FILE[a['phase']]}`。", ""]
        else:
            L += ["## 它返回给工作流的结果", "", "```json", json.dumps(a["result"], ensure_ascii=False, indent=1), "```", ""]
    if prompt:
        L += ["## 它拿到的任务书", "", "```", _clip("\n\n".join(prompt), 400, 40, 60000), "```", ""]
    return "\n".join(L)


# --------------------------------------------------------------------------- one factor's state

def serious(result) -> list:
    return [x for x in ((result or {}).get("issues") or []) if x.get("severity") != "minor"]


def factor_state(fid: str, agents: list) -> dict:
    """What exists for this study and which phase comes next (disk is the only source of truth)."""
    rdir = HAND / fid / "results"
    res = {p.stem: json.loads(p.read_text(encoding="utf-8")) for p in sorted(rdir.glob("*.json"))} if rdir.is_dir() else {}
    mine = [a for a in agents if a["fid"] == fid]
    ledger = ROOT / "runs" / fid / "ledger.json"
    holdout = []
    if ledger.is_file():
        try:
            holdout = [e for e in json.loads(ledger.read_text(encoding="utf-8")).get("entries", [])
                       if e.get("split") == "holdout"]
        except Exception:
            pass
    reads = sorted({e.get("when") for e in holdout})
    audits = {k: v for k, v in res.items() if k.startswith("audit")}
    issues = [dict(x, lens=v.get("lens", k)) for k, v in audits.items() for x in serious(v)]
    kind = (res.get("study") or {}).get("recommended_kind") or ""
    negative = kind in ("none_robust", "known_family", "original_kept")
    audited = "audit" in res or ("audit-numbers" in res and ("audit-mechanism" in res or negative))
    n_crit = sum(1 for x in issues if x.get("severity") == "critical")
    if "revised" in res:
        phase = "done"
    elif audited:
        phase = "revise" if (n_crit or len(issues) >= 2) else "done"
    elif "study" in res:
        phase = "audit"
    else:
        phase = "study"
    live = [a for a in mine if a["status"] == "running"]
    nd = ROOT / "notes" / fid
    orders = sorted(p.stem for p in (nd / "orders").glob("R*.md")) if (nd / "orders").is_dir() else []
    cards = sorted(p.stem for p in (nd / "results").glob("R*.md")) if (nd / "results").is_dir() else []
    return {"fid": fid, "phase": phase, "results": sorted(res), "n_serious": len(issues), "n_critical": n_crit,
            "study_kind": kind,
            "have_audits": sorted(audits), "orders": orders, "cards": cards,
            "pending_orders": [o for o in orders if o not in cards],
            "dossier": (nd / "02_operators.md").is_file() and (nd / "06_baseline.md").is_file(),
            "state_md": (nd / "state.md").stat().st_mtime if (nd / "state.md").is_file() else None,
            "holdout_reads": len(reads), "holdout_when": reads, "agents": mine, "live": live,
            "final_json": (ROOT / "runs" / fid / "final.json").is_file()}


def journal_entries(fid: str) -> list:
    p = ROOT / "notes" / fid / "journal.md"
    if not p.is_file():
        return []
    parts = re.split(r"(?m)^### ", p.read_text(encoding="utf-8"))
    return ["### " + x.rstrip() for x in parts[1:]]


NEXT = {
    "study": "研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑"
             "(`./scripts/study.sh list {fid}` 看服务器上的 tag,`./scripts/study.sh digest {fid} <tag>` 重看结果)。",
    "audit": "研究已完成,结构化结论在 `handoff/{fid}/results/study.json`。下一步是独立审查(审查员不要用研究员的口吻替它说话)。",
    "revise": "研究和审查都完成了,审查提出了 {n} 条 critical/major(`handoff/{fid}/results/audit*.json`)。下一步是修订:"
              "逐条处理,只用 train/valid 补实验,**不许再读留出段**。",
    "done": "这条因子做完了。最终结论在 `handoff/{fid}/results/` 里最新的那个(revised.json 优先,否则 study.json)。",
}


def state_md(fid: str, st: dict, info: dict) -> str:
    import yaml
    L = [f"# {fid} — 交接状态", "",
         f"_自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}(`python scripts/recorder.py --brief {fid}` 刷新)。"
         "这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_", ""]
    if info:
        L += [f"- 来源:{info.get('lib', '')} {info.get('name', '')}(批次 {info.get('batch', '')})",
              f"- 表达式:`{info['expr']}`", ""]
    zh = {"study": "研究进行中(还没有结构化结论)", "audit": "研究完成,待审查", "revise": "审查完成,待修订", "done": "全部完成"}
    L += ["## 现在到哪一步", "", f"- **阶段:{zh[st['phase']]}**"]
    if st["holdout_reads"]:
        L.append(f"- **留出段已经读过 {st['holdout_reads']} 次**({', '.join(local(w) for w in st['holdout_when'])})—— "
                 f"**不许再读**。候选在留出段上的数全在 `runs/{fid}/final.json`(`./scripts/study.sh digest {fid} final`)。")
    else:
        L.append("- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。")
    if st["agents"]:
        L.append("- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):")
    for a in st["agents"][-3:]:
        zs = {"returned": "已返回结果", "failed": "失败", "running": "还在跑", "cut-off": "中断"}[a["status"]]
        if a["status"] == "running":      # very likely the reader itself: no pointer, or it reads its own log
            L.append(f"  - `{a['label']}`:还在跑(多半就是你自己)")
            continue
        if a["size"] < 400_000 and a["status"] != "returned":     # died before doing anything worth reading
            L.append(f"  - `{a['label']}`:{zs},几乎没做事")
            continue
        L.append(f"  - `{a['label']}`:{zs},最后动作 {local(a['mtime'])} → "
                 f"`handoff/{fid}/agents/{a['phase']}_{('R' + a['round'] + '_') if a.get('round') else ''}{a['agent']}.md`")
    L += ["", "**接手的人该做什么:** " + NEXT[st["phase"]].format(fid=fid, n=st["n_serious"]), ""]

    sp = ROOT / "notes" / fid / "state.md"
    if sp.is_file():
        txt = sp.read_text(encoding="utf-8").strip()
        if len(txt) > 6000:            # long: quote the opening only, the reader opens the file itself (once)
            cut = re.search(r"(?m)^## 2", txt)
            txt = txt[:cut.start() if cut else 3000].strip() + f"\n\n(…全文 {len(txt)} 字符,读 `notes/{fid}/state.md`)"
        L += [f"## 研究现状(`notes/{fid}/state.md`,{local(sp.stat().st_mtime)} 更新)—— **先读这个文件**", "", txt, ""]
    else:
        L += [f"## 研究员自己写的现状(`notes/{fid}/state.md`)", "",
              "(**没有**。上一个研究员没有留下现状说明 —— 假设、逻辑和后面的思路只能从 notes、研究日志和动作流水里重建。)", ""]
    ents = journal_entries(fid)
    own = [e for e in ents if "[auto]" not in e.splitlines()[0]]
    L += [f"## 研究日志(`notes/{fid}/journal.md`:{len(ents)} 条,其中研究员自己写的 {len(own)} 条)", ""]
    if ents:
        def short(e):
            return e if len(e) <= 1100 else e[:1100].rstrip() + "\n…(这条日志还有后文,读 journal.md)"
        L += ["最近的 5 条(更早的和全文看文件):", ""] + [short(e) + "\n" for e in ents[-5:]]
    else:
        L += ["(还没有。之前的研究员没有记日志 —— 它的想法只能从 notes 和动作流水里推。)", ""]

    if st["orders"] or st["cards"]:
        L += [f"## 工单与结果卡(`notes/{fid}/orders/`、`notes/{fid}/results/`)", ""]
        for o in sorted(set(st["orders"]) | set(st["cards"]), key=lambda x: int(re.sub(r"\D", "", x) or 0)):
            L.append(f"- {o}:工单 {'有' if o in st['orders'] else '—'},结果卡 {'有' if o in st['cards'] else '**还没有(待执行)**'}")
        L.append("")
    cfg = ROOT / "configs" / f"{fid}.yaml"
    if cfg.is_file():
        try:
            c = yaml.safe_load(cfg.read_text(encoding="utf-8"))
            L += ["## 配置里的实验计划(`configs/" + fid + ".yaml`)", ""]
            if c.get("title"):
                L += [f"- 标题:{c['title']}"]
            for s in c.get("stages", []) or []:
                vs = s.get("variants", []) or []
                L.append(f"- **{s.get('id')}**({len(vs)} 个变体){'【读留出段】' if s.get('final') else ''}:{s.get('question', '')}")
                L.append("  " + "、".join(str(v.get("id")) for v in vs[:14]) + (" …" if len(vs) > 14 else ""))
            L.append("")
        except Exception as e:
            L += [f"(配置解析失败:{e})", ""]

    runs = sorted((p for p in (ROOT / "runs" / fid).glob("*.json") if not p.name.startswith("_") and p.name != "ledger.json"),
                  key=lambda p: p.stat().st_mtime) if (ROOT / "runs" / fid).is_dir() else []
    logs = sorted((ROOT / "logs").glob(f"{fid}_*.log"), key=lambda p: p.stat().st_mtime) if (ROOT / "logs").is_dir() else []
    L += ["## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list " + fid + "`)", ""]
    have = {p.stem for p in runs}
    for p in runs:
        try:
            n = len(json.loads(p.read_text(encoding="utf-8")).get("results", {}))
        except Exception:
            n = "?"
        L.append(f"- `{p.stem}`  {local(p.stat().st_mtime)}  {n} 个变体  → `./scripts/study.sh digest {fid} {p.stem}`")
    for p in logs:
        tag = p.stem[len(fid) + 1:]
        if tag in have:
            continue
        ex = ""
        try:
            m = re.findall(r"\[partura exit (\d+)", p.read_text(encoding="utf-8", errors="replace"))
            ex = f"exit {m[-1]}" if m else "没有退出行"
        except Exception:
            pass
        L.append(f"- `{tag}`(自写脚本的输出)  {local(p.stat().st_mtime)}  {ex}  → `logs/{p.name}`")
    if not runs and not logs:
        L.append("(无)")
    L.append("")

    nd = ROOT / "notes" / fid
    L += [f"## 已写的 notes(`notes/{fid}/`)", ""]
    if nd.is_dir():
        L.append("、".join(f"`{p.name}`({p.stat().st_size // 1024 or 1}K)" for p in sorted(nd.glob("*.md"))))
    else:
        L.append("(无)")
    sd = ROOT / "studies" / fid
    L += ["", f"## 自写的探针与分析脚本(`studies/{fid}/`)", ""]
    if sd.is_dir():
        for p in sorted(sd.glob("*.py")):
            head = ""
            try:
                txt = p.read_text(encoding="utf-8")
                m = re.match(r'\s*(?:"""|\'\'\')(.*?)(?:"""|\'\'\')', txt, re.S)
                head = (m.group(1).strip().splitlines()[0] if m else "")[:110]
            except Exception:
                pass
            L.append(f"- `{p.name}`  {local(p.stat().st_mtime)}  {head}")
    else:
        L.append("(无)")
    L += ["", f"## 结构化结果(`handoff/{fid}/results/`)", ""]
    L += [f"- `{k}.json`" for k in st["results"]] or ["(还没有)"]
    rp = ROOT / "research" / "alpha_distillation" / f"{fid}.md"
    if rp.is_file():
        L += ["", f"报告:`research/alpha_distillation/{fid}.md`({local(rp.stat().st_mtime)} 生成)"]
    return "\n".join(L) + "\n"


def board(states: dict, info: dict) -> str:
    zh = {"study": "研究中", "audit": "待审查", "revise": "待修订", "done": "**完成**"}
    L = ["# 批次状态板", "",
         f"_自动生成于 {datetime.now().strftime('%Y-%m-%d %H:%M')}(后台记录器 `scripts/recorder.py`,不依赖任何模型)。_", "",
         "| 因子 | 来源 | 阶段 | 留出段 | 已有结果 | 运行数 | 现状说明 state.md | 日志条数(研究员写的) | 当前 agent | 最后动静 |",
         "|---|---|---|---|---|---|---|---|---|---|"]
    for fid in sorted(states):
        st, f = states[fid], info.get(fid, {})
        ents = journal_entries(fid)
        own = sum(1 for e in ents if "[auto]" not in e.splitlines()[0])
        nrun = len([p for p in (ROOT / "runs" / fid).glob("*.json")
                    if not p.name.startswith("_") and p.name != "ledger.json"]) if (ROOT / "runs" / fid).is_dir() else 0
        live = "、".join(f"{a['phase']}(在跑)" for a in st["live"]) or \
            ("—" if not st["agents"] else f"{st['agents'][-1]['phase']}({ {'returned': '已返回', 'failed': '失败', 'cut-off': '中断', 'running': '在跑'}[st['agents'][-1]['status']] })")
        times = [a["mtime"] for a in st["agents"]]
        nd = ROOT / "notes" / fid
        if nd.is_dir():
            times += [p.stat().st_mtime for p in nd.glob("*.md")]
        L.append(f"| [{fid}]({fid}/STATE.md) | {f.get('lib', '')} {f.get('name', '')} | {zh[st['phase']]} "
                 f"| {'已读' if st['holdout_reads'] else '未读'} | {'、'.join(st['results']) or '—'} | {nrun} "
                 f"| {local((nd / 'state.md').stat().st_mtime) if (nd / 'state.md').is_file() else '**无**'} "
                 f"| {len(ents)}({own}) | {live} | {local(max(times)) if times else '—'} |")
    todo = {p: [f for f in sorted(states) if states[f]["phase"] == p] for p in ("study", "audit", "revise")}
    L += ["", "## 还剩什么", ""]
    for p, name in (("study", "研究没做完"), ("audit", "待审查"), ("revise", "待修订")):
        L.append(f"- {name}({len(todo[p])}):{'、'.join(x.split('_')[0] for x in todo[p]) or '无'}")
    L += ["", "怎样接着跑(换了模型、换了会话都一样):看 `handoff/README.md`。", ""]
    return "\n".join(L)


# --------------------------------------------------------------------------- snapshot

def snapshot(only: str | None = None, quiet: bool = False) -> dict:
    HAND.mkdir(exist_ok=True)
    cache_p = HAND / ".recorder_cache.json"
    try:
        cache = json.loads(cache_p.read_text(encoding="utf-8"))
    except Exception:
        cache = {}
    agents = scan_runs()
    info = batches()
    changed = 0
    for a in agents:
        if only and a["fid"] != only:
            continue
        if a["result"] is not None and a["phase"] in RESULT_FILE:      # oldest first, so a later result wins
            changed += write_if_changed(HAND / a["fid"] / "results" / RESULT_FILE[a["phase"]],
                                        json.dumps(a["result"], ensure_ascii=False, indent=1) + "\n")
        key = f"{a['run']}/{a['agent']}"
        sig = [a["size"], int(a["mtime"]), a["status"]]
        if cache.get(key) != sig:
            try:
                rnd = f"R{a['round']}_" if a.get("round") else ""
                changed += write_if_changed(HAND / a["fid"] / "agents" / f"{a['phase']}_{rnd}{a['agent']}.md", agent_log(a))
                cache[key] = sig
            except Exception as e:           # a half-written last line, etc.: try again next round
                if not quiet:
                    print(f"[recorder] {key}: {e}", file=sys.stderr)
    fids = sorted(set(info) | {a["fid"] for a in agents})
    states = {}
    for fid in fids:
        st = factor_state(fid, agents)
        states[fid] = st
        if only and fid != only:
            continue
        changed += write_if_changed(HAND / fid / "STATE.md", state_md(fid, st, info.get(fid, {})))
    if not only:
        write_if_changed(HAND / "STATUS.md", board({f: s for f, s in states.items() if f in info or s["agents"]}, info))
    cache_p.write_text(json.dumps(cache), encoding="utf-8")
    if not quiet:
        print(f"[recorder] {datetime.now().strftime('%H:%M:%S')} {len(agents)} agents, {len(states)} factors, "
              f"{changed} files updated", flush=True)
    return states


def main() -> None:
    argv = sys.argv[1:]
    if "--brief" in argv:
        fid = argv[argv.index("--brief") + 1]
        snapshot(only=fid, quiet=True)
        print((HAND / fid / "STATE.md").read_text(encoding="utf-8"))
        return
    if "--state" in argv:
        i = argv.index("--state")
        batch = argv[i + 1] if len(argv) > i + 1 and not argv[i + 1].startswith("-") else None
        states, info = snapshot(quiet=True), batches()
        out = []
        for fid, st in sorted(states.items()):
            f = info.get(fid)
            if not f or (batch and f["batch"] != Path(batch).stem):
                continue
            out.append({"id": fid, "lib": f.get("lib"), "name": f.get("name"), "expr": f["expr"], "phase": st["phase"],
                        **({"note": f["note"]} if f.get("note") else {}),
                        "dossier": st["dossier"], "have_audits": st["have_audits"], "n_serious": st["n_serious"],
                        "n_critical": st["n_critical"], "study_kind": st["study_kind"],
                        "holdout_reads": st["holdout_reads"], "has_state_md": st["state_md"] is not None,
                        "pending_orders": st["pending_orders"], "running": [a["label"] for a in st["live"]]})
        print(json.dumps(out, ensure_ascii=False, indent=1))
        return
    if "--loop" in argv:
        every = float(argv[argv.index("--loop") + 1])
        hours = float(argv[argv.index("--hours") + 1]) if "--hours" in argv else 30.0
        end = time.time() + hours * 3600
        stop = HAND / ".stop_recorder"
        while time.time() < end and not stop.exists():
            try:
                snapshot()
            except Exception as e:
                print(f"[recorder] snapshot failed: {e!r}", file=sys.stderr, flush=True)
            time.sleep(every)
        return
    snapshot()


if __name__ == "__main__":
    main()
