"""Emergency state.md: assemble a study's current state from what is on disk, with no model.

Used when a researcher is cut off before writing notes/<fid>/state.md itself.  It cannot know
what the researcher was thinking -- it collects what the researcher wrote and did: the
hypothesis file, the notes, the planned stages, the runs, the scripts, and the timeline of its
actions (each command's own one-line description).  The next researcher rewrites this page.

    python scripts/autostate.py <fid> [...]        # only writes where state.md is missing
    python scripts/autostate.py --force <fid>
"""
import glob
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
WF_GLOB = str(Path.home() / ".claude/projects/*/*/subagents/workflows/wf_*")


def local(ts):
    try:
        return datetime.fromisoformat(ts.replace("Z", "+00:00")).astimezone().strftime("%m-%d %H:%M")
    except Exception:
        return "?"


def timeline(fid):
    """(label, [(time, kind, text)]) of the agent that last worked on this study."""
    best = None
    for d in glob.glob(WF_GLOB):
        for meta in glob.glob(os.path.join(d, "agent-*.meta.json")):
            try:
                desc = json.load(open(meta, encoding="utf-8")).get("description", "")
            except Exception:
                continue
            if fid not in desc:
                continue
            t = meta.replace(".meta.json", ".jsonl")
            if os.path.isfile(t) and os.path.getsize(t) > 400_000 and (best is None or os.path.getmtime(t) > os.path.getmtime(best[1])):
                best = (desc, t)
    if not best:
        return None, []
    ev = []
    for line in open(best[1], encoding="utf-8"):
        try:
            r = json.loads(line)
        except Exception:
            continue
        m = r.get("message") if isinstance(r.get("message"), dict) else {}
        c = m.get("content")
        if r.get("type") == "assistant" and isinstance(c, list):
            for b in c:
                if b.get("type") != "tool_use":
                    continue
                i = b.get("input") or {}
                if b["name"] == "Bash":
                    cmd = i.get("command", "")
                    k = re.search(r"study\.sh\s+(run|final|exec|wait|check|decompose|propose|src|digest|list|report|note)\s+([^|;&>\n]*)", cmd)
                    ev.append((r.get("timestamp"), "跑" if k else "看", (i.get("description") or "")[:110] + (f"  〔study.sh {k.group(1)} {k.group(2).strip()[:70]}〕" if k else "")))
                elif b["name"] in ("Write", "Edit"):
                    ev.append((r.get("timestamp"), "写", str(i.get("file_path", "")).replace(str(ROOT) + "/", "")))
    return best[0], ev


def build(fid):
    import yaml
    nd, sd, rd = ROOT / "notes" / fid, ROOT / "studies" / fid, ROOT / "runs" / fid
    cfg = yaml.safe_load((ROOT / "configs" / f"{fid}.yaml").read_text(encoding="utf-8"))
    label, ev = timeline(fid)
    runs = sorted((p for p in rd.glob("*.json") if not p.name.startswith("_") and p.name != "ledger.json"), key=lambda p: p.stat().st_mtime) if rd.is_dir() else []
    logs = sorted((ROOT / "logs").glob(f"{fid}_*.log"), key=lambda p: p.stat().st_mtime)
    done_tags = {p.stem for p in runs}
    started, finished = [], set()
    for ts, kind, text in ev:
        m = re.search(r"study\.sh (run|exec|final) (\S+) (\S+)", text)
        if m:
            started.append((ts, m.group(1), m.group(3), text))
    jr = (nd / "journal.md").read_text(encoding="utf-8") if (nd / "journal.md").is_file() else ""
    for m in re.finditer(r"\[auto\] (\S+) 跑完", jr):
        finished.add(m.group(1))
    for p in logs:
        if "partura exit" in p.read_text(encoding="utf-8", errors="replace"):
            finished.add(p.stem[len(fid) + 1:])
    pending = [(ts, k, tag) for ts, k, tag, _ in started if tag not in finished and tag not in done_tags]
    holdout = False
    if (rd / "ledger.json").is_file():
        holdout = any(e.get("split") == "holdout" for e in json.loads((rd / "ledger.json").read_text(encoding="utf-8")).get("entries", []))
    L = [f"# {fid} — 研究现状(**自动汇编**,{datetime.now().strftime('%Y-%m-%d %H:%M')})", "",
         "> 这一页不是研究员写的。上一位研究员(Opus 5.5,工作流 agent `" + str(label) + "`)在写下现状之前就被换下了;",
         "> 协调者用脚本(`scripts/autostate.py`,不经过任何模型)把磁盘上**它写过的和做过的**汇编成这一页。",
         "> 它当时怎么想的没有留下 —— 假设的最新状态、对结果的解读,需要接手的主研读下面列出的材料后**重写这一页**。", "",
         "## 1. 一句话现状", "",
         f"- 配置里的一句话(研究员读完这棵树之后写的):{cfg.get('title', '(没写)')}",
         f"- 已写 notes:{'、'.join(p.name for p in sorted(nd.glob('*.md')) if p.name not in ('state.md', 'journal.md')) or '无'}",
         f"- 已拉回本地的运行:{'、'.join(p.stem for p in runs) or '无'};已启动但**结果还没人读**的:{'、'.join(t for _, _, t in pending) or '无'}",
         f"- 留出段:{'**已读过,不许再读**' if holdout else '未读'}", ""]
    L += ["## 2. 中间结果(事实在这些文件里,还没有汇总)", ""]
    for p in runs:
        L.append(f"- 运行 `{p.stem}`({datetime.fromtimestamp(p.stat().st_mtime).strftime('%m-%d %H:%M')}):`./scripts/study.sh digest {fid} {p.stem}`")
    for p in logs:
        tag = p.stem[len(fid) + 1:]
        if tag not in done_tags:
            L.append(f"- 自写分析 `{tag}` 的输出:`logs/{p.name}`")
    for name in ("06_baseline.md",):
        if (nd / name).is_file():
            L += ["", f"### 基线读数(原文照录 `notes/{fid}/{name}`)", "", (nd / name).read_text(encoding="utf-8").strip(), ""]
    for p in sorted(nd.glob("07*.md")):
        L += ["", f"### 已写的阶段结论(原文照录 `notes/{fid}/{p.name}`)", "", p.read_text(encoding="utf-8").strip(), ""]
    L += ["", "## 3. 研究过程与逻辑(从对话记录里抽的动作时间线;每条是研究员给自己那条命令写的说明)", ""]
    last = None
    for ts, kind, text in ev:
        line = f"- {local(ts)} [{kind}] {text}"
        if line != last:
            L.append(line)
        last = line
    for name in ("02_operators.md", "03_decomposition.md", "04_grammar.md"):
        if (nd / name).is_file():
            L += ["", f"### 研究员对这棵树的理解(原文照录 `notes/{fid}/{name}`)", "", (nd / name).read_text(encoding="utf-8").strip(), ""]
    L += ["", "## 4. 假设表", ""]
    if (nd / "05_hypotheses.md").is_file():
        L += [f"下面是研究员在跑实验**之前**写的假设表(原文照录 `notes/{fid}/05_hypotheses.md`)。**其后的实验结果没有回填**:",
              "每条假设现在是「未验证 / 被支持 / 被否定」,要对照第 2 节列出的运行结果重新判定。", "",
              (nd / "05_hypotheses.md").read_text(encoding="utf-8").strip(), ""]
    else:
        L += ["(研究员还没有写假设表。)", ""]
    L += ["## 5. 当前的候选(提纯 / 升华)", "", "(没有留下。研究还没进行到选候选的阶段,或者候选只在研究员脑子里。)", "",
          "## 6. 后面的研究思路(研究员已经写进配置和脚本、但还没做完的)", ""]
    for s in cfg.get("stages", []) or []:
        tagged = "已有结果" if any(s.get("id") in json.loads(p.read_text(encoding="utf-8")).get("stages", []) for p in runs) else "**还没有结果**"
        L.append(f"- 阶段 **{s.get('id')}**({tagged}):{s.get('question', '')}")
        for v in (s.get("variants") or [])[:14]:
            L.append(f"    - `{v.get('id')}` = `{str(v.get('expr'))[:150]}` —— {str(v.get('why', ''))[:200]}")
    if sd.is_dir():
        for p in sorted(sd.glob("*.py")):
            txt = p.read_text(encoding="utf-8")
            m = re.match(r'\s*(?:"""|\'\'\')(.*?)(?:"""|\'\'\')', txt, re.S)
            L.append(f"- 脚本 `studies/{fid}/{p.name}`:{(m.group(1).strip() if m else '')[:600]}")
    L += ["", "## 7. 留出段", "", "**已读过一次,绝不再读**(数字在 `runs/" + fid + "/final.json`)。" if holdout else "未读。读之前要先在 `10_distilled.md` 里写下候选排序和判据。", "",
          "## 8. 给接手者的提醒", ""]
    for ts, k, tag in pending:
        L.append(f"- `{tag}`({local(ts)} 用 {k} 启动)在服务器上跑着或已跑完,**结果没人读过**:`./scripts/study.sh wait {fid} {tag}` 拉回来看。")
    L += ["- 上一位研究员的完整动作流水(含每条命令的输出):`handoff/" + fid + "/agents/`。",
          "- 这一页是自动汇编的;你读完材料、形成判断之后,**按 playbook §7 的 8 节把它整个重写**。", ""]
    return "\n".join(L)


force = "--force" in sys.argv
for fid in [a for a in sys.argv[1:] if not a.startswith("-")]:
    p = ROOT / "notes" / fid / "state.md"
    if p.is_file() and not force:
        print(f"{fid}: state.md 已存在,不覆盖")
        continue
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(build(fid), encoding="utf-8")
    print(f"{fid}: 写了 {p}({p.stat().st_size} 字节)")
