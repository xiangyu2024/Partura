"""Assemble the research report from run artefacts.

The report has two kinds of section.  **Generated** sections (operator
dossiers, decomposition, every metric table, the split ledger, provenance)
are built from the JSON a run wrote, so no number in the report is typed by
hand.  **Written** sections (hypotheses, interpretation, diagnosis, risks,
next experiments) come from markdown fragments under ``notes/<factor_id>/``.

Keeping the two apart is the point: if a claim is in a written section, a
reader can check it against the generated table right above it.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from .bridge import PARTURA_ROOT
from .decompose import decompose
from .semantics import render_markdown as render_dossiers
from .splits import SPLITS, Ledger

SECTIONS = [
    ("01_expression", "1. 原始表达式"),
    ("02_operators", "2. 算子的真实语义"),
    ("03_decomposition", "3. 数学分解"),
    ("04_grammar", "4. 结构语法"),
    ("05_hypotheses", "5. 竞争性假设"),
    ("06_baseline", "6. 基线指标"),
    ("07_ablations", "7. 消融实验"),
    ("08_variants", "8. 语义变体"),
    ("09_diagnosis", "9. 机制诊断"),
    ("10_distilled", "10. 蒸馏后的候选"),
    ("11_risks", "11. 失效模式与风险"),
    ("12_next", "12. 下一步实验"),
]

_COLS = [("rank_ic", "rank IC"), ("rank_icir", "rank ICIR"), ("ic", "IC"), ("icir", "ICIR"),
         ("turnover", "日换手"), ("sharpe", "夏普(无成本)"), ("sharpe_net", "夏普(扣15bp)"),
         ("fitness", "GP 适应度"), ("coverage", "覆盖率")]


def _fmt(v, nd: int = 4) -> str:
    if v is None:
        return "—"
    try:
        f = float(v)
    except (TypeError, ValueError):
        return str(v)
    if f != f:
        return "NaN"
    return f"{f:+.{nd}f}" if abs(f) < 1000 else f"{f:+.1f}"


def _load_runs(out_dir: Path) -> Dict[str, dict]:
    runs = {}
    for p in sorted(out_dir.glob("*.json")):
        if p.name == "ledger.json":
            continue
        runs[p.stem] = json.loads(p.read_text(encoding="utf-8"))
    return runs


def _merged_results(runs: Dict[str, dict]) -> Dict[str, dict]:
    out: Dict[str, dict] = {}
    for r in runs.values():
        out.update(r.get("results", {}))
    return out


def _metric_table(results: Dict[str, dict], ids: Sequence[str], split: str = "train",
                  cols: Sequence = _COLS) -> str:
    head = "| 变体 | 表达式 | 方向 | " + " | ".join(c[1] for c in cols) + " |"
    sep = "|---" * (len(cols) + 3) + "|"
    lines = [head, sep]
    for vid in ids:
        r = results.get(vid)
        if not r:
            continue
        if "error" in r:
            lines.append(f"| `{vid}` | — | — |" + " — |" * len(cols) + f"  <!-- {r['error']} -->")
            continue
        m = r["splits"].get(split, {})
        expr = r["expr"]
        expr = expr if len(expr) <= 74 else expr[:71] + "..."
        lines.append(f"| `{vid}` | `{expr}` | {'+' if r['sign'] > 0 else '−'} | "
                     + " | ".join(_fmt(m.get(c[0])) for c in cols) + " |")
    return "\n".join(lines)


def _split_table(results: Dict[str, dict], vid: str, splits: Sequence[str]) -> str:
    r = results.get(vid)
    if not r or "error" in r:
        return "_(无数据)_"
    lines = ["| 数据段 | 区间 | 天数 | " + " | ".join(c[1] for c in _COLS) + " |",
             "|---" * (len(_COLS) + 3) + "|"]
    for s in splits:
        m = r["splits"].get(s)
        if not m:
            continue
        a, b = SPLITS.get(s, ("", ""))
        lines.append(f"| {s} | {a}–{b} | {m.get('n_days')} | "
                     + " | ".join(_fmt(m.get(c[0])) for c in _COLS) + " |")
    return "\n".join(lines)


def _diag_tables(runs: Dict[str, dict]) -> Dict[str, str]:
    out: Dict[str, str] = {}
    diags = [r.get("diagnostics", {}) for r in runs.values() if r.get("diagnostics")]
    if not diags:
        return out
    d = {}
    for x in diags:
        for k, v in x.items():
            if isinstance(v, dict):
                d.setdefault(k, {}).update(v)
            else:
                d[k] = v

    if d.get("decay"):
        lines = ["| 变体 | " + " | ".join(f"h={r['horizon']}" for r in next(iter(d["decay"].values()))) + " |"]
        lines.append("|---" * (len(next(iter(d["decay"].values()))) + 1) + "|")
        for vid, rows in d["decay"].items():
            lines.append(f"| `{vid}` rank IC | " + " | ".join(_fmt(r["rank_ic"]) for r in rows) + " |")
        out["decay"] = "\n".join(lines)

    if d.get("by_year"):
        for vid, rows in d["by_year"].items():
            lines = ["| 年份 | 天数 | rank IC | 无成本盈亏 | 扣费盈亏 | 扣费夏普 | 日换手 |",
                     "|---|---|---|---|---|---|---|"]
            for r in rows:
                lines.append(f"| {r['year']} | {r['days']} | {_fmt(r['rank_ic'])} | {_fmt(r['gross_pnl'],3)} "
                             f"| {_fmt(r['net_pnl'],3)} | {_fmt(r['sharpe_net'],2)} | {_fmt(r['turnover'],3)} |")
            out[f"by_year::{vid}"] = "\n".join(lines)

    if d.get("extreme_days"):
        lines = ["| 变体 | 剔除比例 | 剔除天数 | 扣费夏普 | 扣费累计盈亏 |", "|---|---|---|---|---|"]
        for vid, rows in d["extreme_days"].items():
            for r in rows:
                lines.append(f"| `{vid}` | {r['dropped_frac']:.0%} | {r['dropped_days']} | "
                             f"{_fmt(r['sharpe_net'],2)} | {_fmt(r['net_pnl'],3)} |")
        out["extreme_days"] = "\n".join(lines)

    if d.get("neutralise"):
        lines = ["| 变体 | 中性化对象 | 截面 R² | 残差 rank IC | 残差扣费夏普 | 残差日换手 |",
                 "|---|---|---|---|---|---|"]
        for vid, entry in d["neutralise"].items():
            for ctl, rec in entry.items():
                m = rec["metrics"]
                lines.append(f"| `{vid}` | {ctl} | {_fmt(rec['r2'],3)} | {_fmt(m['rank_ic'])} | "
                             f"{_fmt(m['sharpe_net'],2)} | {_fmt(m['turnover'],3)} |")
        out["neutralise"] = "\n".join(lines)

    if d.get("conditional"):
        lines = ["| 因子 \\| 门控 | 桶 | 桶内 rank IC | 桶内 rank ICIR | 桶内平均股票数 |",
                 "|---|---|---|---|---|"]
        for key, rows in d["conditional"].items():
            for r in rows:
                lines.append(f"| {key} | Q{r['bucket']+1} | {_fmt(r['rank_ic'])} | {_fmt(r['rank_icir'],2)} "
                             f"| {r['mean_names']:.0f} |")
        out["conditional"] = "\n".join(lines)

    if d.get("controls"):
        lines = ["| 控制变量 | 方向 | rank IC | 扣费夏普 | 日换手 |", "|---|---|---|---|---|"]
        for k, m in d["controls"].items():
            lines.append(f"| `{k}` | {'+' if m['sign'] > 0 else '−'} | {_fmt(m['rank_ic'])} | "
                         f"{_fmt(m['sharpe_net'],2)} | {_fmt(m['turnover'],3)} |")
        out["controls"] = "\n".join(lines)

    if d.get("rank_corr_train"):
        out["rank_corr"] = d["rank_corr_train"]
    return out


def rank_corr_table(matrix: Dict[str, Dict[str, float]], ids: Sequence[str]) -> str:
    ids = [i for i in ids if i in matrix]
    lines = ["| | " + " | ".join(f"`{i}`" for i in ids) + " |", "|---" * (len(ids) + 1) + "|"]
    for a in ids:
        lines.append(f"| `{a}` | " + " | ".join(_fmt(matrix[a].get(b), 2) for b in ids) + " |")
    return "\n".join(lines)


def build(config_path: str, out_root: Optional[str] = None, notes_dir: Optional[str] = None,
          research_dir: Optional[str] = None) -> Path:
    from .runner import load_config
    cfg = load_config(config_path)
    for k, v in (cfg.get("splits") or {}).items():
        SPLITS[k] = (str(v[0]), str(v[1]))
    fid = cfg["factor_id"]
    out_dir = Path(out_root or (PARTURA_ROOT / "runs")) / fid
    runs = _load_runs(out_dir)
    results = _merged_results(runs)
    any_run = next(iter(runs.values()), {})
    notes = Path(notes_dir or (PARTURA_ROOT / "notes")) / fid
    dec = decompose(cfg["expression"])
    diag = _diag_tables(runs)
    ledger = Ledger(out_dir / "ledger.json")

    def note(name: str, fallback: str = "") -> str:
        p = notes / f"{name}.md"
        return p.read_text(encoding="utf-8").strip() if p.is_file() else fallback

    by_stage: Dict[str, List[str]] = {}
    for vid, r in results.items():
        by_stage.setdefault(r.get("stage", "?"), []).append(vid)
    questions = {s["id"]: s.get("question", "") for s in cfg["stages"]}

    L: List[str] = [f"# Alpha 研究报告 — {fid}", "", f"> {cfg.get('title','')}", ""]
    if any_run:
        v = any_run["view"]
        pv = any_run["provenance"]
        L += [f"**数据**: {v['days']} 个交易日 × {v['symbols']} 只股票 "
              f"({v['first']}–{v['last']},另加 {v['warmup_rows']} 行预热) · "
              f"标签 `{any_run['label']['kind']}` h={any_run['label']['horizon']} · "
              f"成本 {any_run['cost_per_side']*1e4:.0f} bp/边 · 十分位多空 · "
              f"AlphaCube `{pv.get('alphacube_commit')}`", ""]

    L += [f"## {SECTIONS[0][1]}", "", "```", cfg["expression"], "```", "", note("01_expression"), ""]
    L += [f"## {SECTIONS[1][1]}", "",
          "> 以下每一条都来自注册表与内核源码,加上在张量上实跑的探针;没有一条是从算子名字推断的。", "",
          render_dossiers(dec.dossiers), ""]
    L += [f"## {SECTIONS[2][1]}", "", dec.render_markdown(), "", note("03_decomposition"), ""]
    L += [f"## {SECTIONS[3][1]}", "", note("04_grammar"), ""]
    L += [f"## {SECTIONS[4][1]}", "", note("05_hypotheses"), ""]

    L += [f"## {SECTIONS[5][1]}", ""]
    base_id = cfg.get("baseline_id", "v_base")
    L += [_split_table(results, base_id, any_run.get("splits_used", ["train", "valid", "full"])), ""]
    if "by_year::" + base_id in diag:
        L += ["**逐年(全样本,方向按训练段固定)**", "", diag["by_year::" + base_id], ""]
    if "decay" in diag:
        L += ["**不同预测期(训练段)**", "", diag["decay"], ""]
    if "extreme_days" in diag:
        L += ["**极端日依赖(训练段)**", "", diag["extreme_days"], ""]
    L += [note("06_baseline"), ""]

    L += [f"## {SECTIONS[6][1]}", ""]
    for stage_id, ids in by_stage.items():
        L += [f"### {stage_id}", "", f"**问题**: {questions.get(stage_id,'')}", "",
              _metric_table(results, sorted(ids), "train"), ""]
        whys = [f"- `{i}` — {results[i].get('why','')}" for i in sorted(ids) if results[i].get("why")]
        L += ["<details><summary>每个变体为什么存在</summary>", "", *whys, "", "</details>", ""]
        L += [note(f"07_{stage_id}"), ""]
    if "neutralise" in diag:
        L += ["### 中性化(训练段)", "",
              "> 对控制变量做逐日截面回归后的残差;R² 是控制变量能张成的部分。", "",
              diag["neutralise"], "", note("07_neutralise"), ""]
    if "conditional" in diag:
        L += ["### 条件 IC(训练段)", "", diag["conditional"], "", note("07_conditional"), ""]
    if "controls" in diag:
        L += ["### 控制变量自身的表现(训练段)", "", diag["controls"], ""]

    L += [f"## {SECTIONS[7][1]}", "", _metric_table(results, sorted(results), "train"), ""]
    if "rank_corr" in diag:
        ids = cfg.get("corr_ids") or sorted(results)[:14]
        L += ["**变体之间的日截面 rank 相关(训练段)** — ≥0.95 在 AlphaCube 里算同一因子族", "",
              rank_corr_table(diag["rank_corr"], ids), ""]
    L += [note("08_variants"), ""]

    L += [f"## {SECTIONS[8][1]}", "", note("09_diagnosis"), ""]
    L += [f"## {SECTIONS[9][1]}", "", note("10_distilled"), ""]
    L += [f"## {SECTIONS[10][1]}", "", note("11_risks"), ""]
    L += [f"## {SECTIONS[11][1]}", "", note("12_next"), ""]

    L += ["## 附录 A — 数据段使用台账", "", ledger.render_markdown(), ""]
    L += ["## 附录 B — 复现", "", "```bash"]
    for name, r in runs.items():
        L.append(f"# {name}: {r['seconds']}s, stages {r['stages']}")
    L += [f"python -m partura.cli run {config_path} --store <cube> --stages <stage> --device cuda",
          f"python -m partura.cli report {config_path}", "```", ""]
    if any_run:
        L += ["```json", json.dumps(any_run["provenance"], ensure_ascii=False, indent=1), "```", ""]

    dest = Path(research_dir or (PARTURA_ROOT / "research" / "alpha_distillation")) / f"{fid}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(L), encoding="utf-8")
    return dest


__all__ = ["build", "SECTIONS"]
