"""Assemble the research report from run artefacts.

Two kinds of section.  **Generated** sections (operator dossiers,
decomposition, every metric table, the split ledger, provenance) are built
from the JSON a run wrote, so no number in the report is typed by hand.
**Written** sections (hypotheses, interpretation, diagnosis, risks, next
experiments) come from markdown fragments under ``notes/<factor_id>/``.

Money is shown in the user's convention (``partura.books``): decile long/short
Sharpe after 15 bp, and the long leg as a pure long book against the
equal-weight universe -- gross (what the user's table calls 多头腿年化超额), net,
and as a share of the spread.  In A-shares only the long leg is holdable, so
every table carries it next to the Sharpe.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Optional, Sequence

from .bridge import PARTURA_ROOT
from .decompose import decompose
from .semantics import render_markdown as render_dossiers
from .splits import SPLITS, Ledger

SECTIONS = ["1. 原始表达式", "2. 算子的真实语义", "3. 数学分解", "4. 结构语法", "5. 竞争性假设",
            "6. 基线指标", "7. 消融实验", "8. 语义变体", "9. 机制诊断", "10. 蒸馏 / 升华后的候选",
            "11. 失效模式与风险", "12. 下一步实验"]


def _f(v, nd: int = 2, pct: bool = False, plus: bool = True) -> str:
    if v is None:
        return "—"
    try:
        x = float(v)
    except (TypeError, ValueError):
        return str(v)
    if x != x:
        return "NaN"
    if pct:
        return f"{x:+.1%}" if plus else f"{x:.1%}"
    return f"{x:+.{nd}f}" if plus else f"{x:.{nd}f}"


def _pair(a, b, **kw) -> str:
    return f"{_f(a, **kw)} / {_f(b, **kw)}"


def _load_runs(out_dir: Path) -> Dict[str, dict]:
    runs = {}
    for p in sorted(out_dir.glob("*.json")):
        try:
            data = json.loads(p.read_text(encoding="utf-8"))
        except json.JSONDecodeError:
            continue
        if isinstance(data, dict) and "results" in data and "view" in data:
            runs[p.stem] = data
    return runs


def _merged(runs: Dict[str, dict]) -> Dict[str, dict]:
    """Later files win, except that a row which read the holdout is never
    replaced by one that did not."""
    out: Dict[str, dict] = {}
    for r in runs.values():
        for vid, row in r.get("results", {}).items():
            old = out.get(vid)
            if old and "holdout" in (old.get("books_user") or {}).get("splits", {}) and \
                    "holdout" not in (row.get("books_user") or {}).get("splits", {}):
                keep = dict(row)
                for k in ("books_user", "sign_user", "ic_user", "ic_holdout"):
                    if k in old:
                        keep[k] = old[k]
                out[vid] = keep
            else:
                out[vid] = row
    return out


def _short(expr: str, n: int = 70) -> str:
    return expr if len(expr) <= n else expr[:n - 3] + "..."


def _views(b: dict) -> dict:
    from .books import views_of
    return views_of(b)


def stage_table(results: Dict[str, dict], ids: Sequence[str], a: str = "train", b: str = "valid") -> str:
    """Decision table, long leg first: half-life fitted for the pure long book, net long-leg
    excess and pure-long Sharpe; then the long/short view for comparison."""
    head = (f"| 变体 | 表达式 | 方向 | 半衰期(多头) | **多头腿净超额** {a}/{b} | 纯多头夏普 {a}/{b} | 多头腿毛超额 {a}/{b} "
            f"| 多头日换手 | 半衰期(多空) | 扣费多空夏普 {a}/{b} | 空头腿毛超额 {a} | rank IC {a}/{b} | cov / dist |")
    lines = [head, "|---" * 13 + "|"]
    for vid in ids:
        r = results.get(vid)
        if not r:
            continue
        if "error" in r:
            lines.append(f"| `{vid}` | `{_short(r.get('expr', ''), 50)}` | — | 求值失败 |" + " |" * 9)
            continue
        v = _views(r["books"])
        lo, ls = v["long"], v["ls"]
        x, y = lo["splits"].get(a, {}), lo["splits"].get(b, {})
        pa, pb = ls["splits"].get(a, {}), ls["splits"].get(b, {})
        sa, sb = r["splits"].get(a, {}), r["splits"].get(b, {})
        lines.append(
            f"| `{vid}` | `{_short(r['expr'])}` | {'+' if r['sign'] > 0 else '−'} | {lo['hl']:g} "
            f"| **{_pair(x.get('long_ann'), y.get('long_ann'), pct=True)}** "
            f"| {_pair(x.get('long_sharpe'), y.get('long_sharpe'))} "
            f"| {_pair(x.get('long_gross_ann'), y.get('long_gross_ann'), pct=True)} "
            f"| {_f(x.get('long_turnover'), pct=True, plus=False)} | {ls['hl']:g} "
            f"| {_pair(pa.get('ls_sharpe'), pb.get('ls_sharpe'))} | {_f(pa.get('short_gross_ann'), pct=True)} "
            f"| {_pair(sa.get('rank_ic'), sb.get('rank_ic'), nd=4)} "
            f"| {_f(sa.get('coverage_labelled'), 2, plus=False)} / {_f(r.get('distinct'), 2, plus=False)} |")
    return "\n".join(lines)


def user_table(results: Dict[str, dict], ids: Sequence[str], user: str, published: Optional[dict] = None,
               base_id: Optional[str] = None) -> str:
    """Comparable with the user's own tables: sign and half-life from THEIR training period,
    their test period only if this study read it.  Long leg first."""
    head = ("| 结构 | 方向 | 半衰期(多头) | **多头腿净超额** 训练/测试 | 纯多头夏普 训练/测试 | 多头腿毛超额 训练/测试 | 多头日换手 "
            "| 半衰期(多空) | 扣费多空夏普 训练/测试 | 多头腿毛超额@多空半衰期 训练/测试 | 空头腿毛超额 训练/测试 |")
    lines = [head, "|---" * 11 + "|"]
    if published and base_id:
        lines.append(f"| _用户表里公布的原式(多空口径)_ | {'+' if published.get('sign', 0) > 0 else '−'} | — | — | — | — | — "
                     f"| {published.get('hl')} | {_pair(*published['ls'])} | {_pair(*published['long'], pct=True)} | — |")
    for vid in ids:
        r = results.get(vid)
        if not r or "books_user" not in r:
            continue
        v = _views(r["books_user"])
        lo, ls = v["long"], v["ls"]
        x, y = lo["splits"].get(user, {}), lo["splits"].get("holdout", {})
        pa, pb = ls["splits"].get(user, {}), ls["splits"].get("holdout", {})
        lines.append(
            f"| `{vid}` `{_short(r['expr'], 60)}` | {'+' if r.get('sign_user', r['sign']) > 0 else '−'} | {lo['hl']:g} "
            f"| **{_pair(x.get('long_ann'), y.get('long_ann'), pct=True)}** "
            f"| {_pair(x.get('long_sharpe'), y.get('long_sharpe'))} "
            f"| {_pair(x.get('long_gross_ann'), y.get('long_gross_ann'), pct=True)} "
            f"| {_f(x.get('long_turnover'), pct=True, plus=False)} | {ls['hl']:g} "
            f"| {_pair(pa.get('ls_sharpe'), pb.get('ls_sharpe'))} "
            f"| {_pair(pa.get('long_gross_ann'), pb.get('long_gross_ann'), pct=True)} "
            f"| {_pair(pa.get('short_gross_ann'), pb.get('short_gross_ann'), pct=True)} |")
    return "\n".join(lines)


def fixed_hl_table(results: Dict[str, dict], ids: Sequence[str]) -> str:
    """Net long-leg excess / pure-long Sharpe at the SAME half-life for every variant (fit split),
    so that a difference in smoothing is not read as a difference in structure."""
    hs = (0.0, 2.0, 5.0, 10.0, 20.0)
    lines = ["| 变体 | " + " | ".join(f"hl {h:g}: 多头净超额 / 纯多头夏普 / 换手" for h in hs) + " |",
             "|---" * (len(hs) + 1) + "|"]
    n = 0
    for vid in ids:
        r = results.get(vid)
        if not r or "error" in r or not r["books"].get("sweep"):
            continue
        sw = {x["halflife"]: x for x in r["books"]["sweep"]}
        lines.append(f"| `{vid}` | " + " | ".join(
            f"{_f(sw[h]['long_ann'], pct=True)} / {_f(sw[h]['long_sharpe'])} / {_f(sw[h]['long_turnover'], pct=True, plus=False)}"
            if h in sw else "—" for h in hs) + " |")
        n += 1
    return "\n".join(lines) if n else ""


def by_year_table(by_year: Dict[str, list], ids: Sequence[str]) -> str:
    ids = [i for i in ids if i in by_year and by_year[i]]
    if not ids:
        return ""
    years = [r["year"] for r in by_year[ids[0]]]
    lines = ["| 变体 | 指标 | " + " | ".join(str(y) for y in years) + " |", "|---" * (len(years) + 2) + "|"]
    for vid in ids:
        rows = {r["year"]: r for r in by_year[vid]}
        lines.append(f"| `{vid}` | 多头腿净超额 | " + " | ".join(_f(rows.get(y, {}).get("long_ann"), pct=True) for y in years) + " |")
        lines.append(f"| | 扣费多空夏普 | " + " | ".join(_f(rows.get(y, {}).get("ls_sharpe")) for y in years) + " |")
    return "\n".join(lines)


def sweep_table(r: dict) -> str:
    b = r["books"]
    lines = ["| 半衰期 | 纯多头夏普 | 多头腿净超额 | 多头日换手 | 扣费多空夏普 | 多空日换手 |", "|---|---|---|---|---|---|"]
    for s in b["sweep"]:
        mark = (" ◀多头" if s["halflife"] == b["hl_long"] else "") + (" ◁多空" if s["halflife"] == b["hl_ls"] else "")
        lines.append(f"| {s['halflife']:g}{mark} | {_f(s['long_sharpe'])} | {_f(s['long_ann'], pct=True)} "
                     f"| {_f(s['long_turnover'], pct=True, plus=False)} | {_f(s['ls_sharpe'])} "
                     f"| {_f(s['ls_turnover'], pct=True, plus=False)} |")
    return "\n".join(lines)


def profile_table(r: dict) -> str:
    prof = r.get("profile") or {}
    if not prof:
        return ""
    names = list(prof)
    n = len(next(iter(prof.values())))
    lines = ["| 信号分位(1=最低) | " + " | ".join(f"年化超额 {s}" for s in names) + " |",
             "|---" * (len(names) + 1) + "|"]
    for k in range(n):
        lines.append(f"| Q{k + 1} | " + " | ".join(_f(prof[s][k]["excess_ann"], pct=True) for s in names) + " |")
    return "\n".join(lines)


def _diag(runs: Dict[str, dict]) -> Dict[str, object]:
    d: Dict[str, object] = {}
    for r in runs.values():
        for k, v in (r.get("diagnostics") or {}).items():
            if isinstance(v, dict):
                d.setdefault(k, {}).update(v)
            else:
                d[k] = v
    return d


def rank_corr_table(matrix: Dict[str, Dict[str, float]], ids: Sequence[str]) -> str:
    def cell(a, b):
        v = matrix.get(a, {}).get(b)
        if v is None or (isinstance(v, float) and v != v):
            v = matrix.get(b, {}).get(a)
        return v
    ids = [i for i in ids if i in matrix]
    lines = ["| | " + " | ".join(f"`{i}`" for i in ids) + " |", "|---" * (len(ids) + 1) + "|"]
    for a in ids:
        lines.append(f"| `{a}` | " + " | ".join(_f(cell(a, b), 2) for b in ids) + " |")
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
    if runs and not any("fit_split" in r for r in runs.values()):       # a study from before the book convention
        from .report_legacy import build as legacy_build
        return legacy_build(config_path, out_root=out_root, notes_dir=notes_dir, research_dir=research_dir)
    from .probes import load_study_probes
    for pf in (cfg.get("probes") or []):
        load_study_probes(pf if Path(pf).is_absolute() else PARTURA_ROOT / pf)

    results = _merged(runs)
    any_run = max(runs.values(), key=lambda r: len(r.get("splits_used", [])), default={})
    user = any_run.get("user_split") or cfg.get("user_split", "utrain")
    notes = Path(notes_dir or (PARTURA_ROOT / "notes")) / fid
    dec = decompose(cfg["expression"])
    diag = _diag(runs)
    ledger = Ledger(out_dir / "ledger.json")
    base_id = cfg.get("baseline_id", "v_base")
    pub = cfg.get("published")

    def note(name: str) -> str:
        p = notes / f"{name}.md"
        return p.read_text(encoding="utf-8").strip() if p.is_file() else ""

    questions = {s["id"]: s.get("question", "") for s in cfg["stages"]}
    by_stage: Dict[str, List[str]] = {s["id"]: [] for s in cfg["stages"]}
    for vid, r in results.items():
        by_stage.setdefault(r.get("stage", "?"), []).append(vid)
    by_stage = {k: v for k, v in by_stage.items() if v}

    L: List[str] = [f"# Alpha 研究报告 — {fid}", "", f"> {cfg.get('title', '')}", ""]
    if any_run:
        v, pv, sd = any_run["view"], any_run["provenance"], any_run.get("split_dates", {})
        lab = any_run["label"]
        L += [f"**数据**: {v['days']} 个交易日 × {v['symbols']} 只股票 ({v['first']}–{v['last']}) · "
              f"标签 `{lab['kind']}` h={lab['horizon']}{'(可买入:剔除次日开盘封涨停)' if lab.get('buyable') else ''} · "
              f"成本 {any_run['cost_per_side'] * 1e4:.0f} bp/单位换手 · 前/后 10% · "
              f"AlphaCube `{pv.get('alphacube_commit')}` · Partura `{pv.get('partura_code_sha')}`", "",
              "**数据段**: " + " · ".join(f"{k} {a}–{b}" for k, (a, b) in sd.items()), "",
              f"> 决策用的数字:方向与 EMA 半衰期在 **{any_run.get('fit_split')}** 上定,在 valid 上确认。"
              f"与用户表可比的数字:方向与半衰期在 **{user}**(用户的训练段)上定;holdout = 用户的测试段,只在最后读。", ""]

    L += [f"## {SECTIONS[0]}", "", "```", cfg["expression"], "```", "", note("01_expression"), ""]
    L += [f"## {SECTIONS[1]}", "",
          "> 每一条都来自注册表与内核源码,加上在张量上实跑的探针;没有一条是从算子名字推断的。"
          "探针集合按**这棵树**挑:不适用的写明,本研究新增的单独标出。", "",
          render_dossiers(dec.dossiers, show_questions=True), ""]
    try:
        from .lab import Lab
        from .panels import parse_research
        lab_ = Lab()
        L += ["### 既往研究留下的先验", "",
              lab_.render_markdown(lab_.recall(parse_research(cfg["expression"]), exclude_study=fid)), ""]
    except Exception as exc:
        L += [f"_(实验室笔记本未能加载:{exc})_", ""]
    L += [note("02_operators"), ""]
    L += [f"## {SECTIONS[2]}", "", dec.render_markdown(), "", note("03_decomposition"), ""]
    L += [f"## {SECTIONS[3]}", "", note("04_grammar"), ""]
    L += [f"## {SECTIONS[4]}", "", note("05_hypotheses"), ""]

    # ---- 6 baseline
    L += [f"## {SECTIONS[5]}", ""]
    base = results.get(base_id)
    if base and "books" in base:
        # The final stage needs unique ids, so the original expression is read on the holdout under
        # another id (f_orig).  Show THAT row here if it exists: it is the same tree.
        twin = next((vid for vid, r in results.items() if r.get("expr") == base.get("expr")
                     and "holdout" in (r.get("books_user") or {}).get("splits", {})), None)
        show = twin or (base_id if "books_user" in base else None)
        if show:
            L += ["**与用户表同口径**(方向、半衰期在用户训练段上定;多头口径在前,多空口径 = 用户最早那张表的口径)", "",
                  user_table(results, [show], user, pub, base_id), ""]
        L += ["**决策口径**(方向、半衰期在 train 上定;valid 是它没见过的)", "", stage_table(results, [base_id]), "",
              "**半衰期扫描(fit 段)** — ◀多头 = 按纯多头夏普选中的,◁多空 = 按多空夏普选中的", "", sweep_table(base), ""]
        pt = profile_table(base)
        if pt:
            L += ["**信号分位的次日超额**(相对当天有信号有标签的票的等权;十分位书默认「越强越好」,这张表检验它)",
                  "", pt, ""]
    by_year = diag.get("by_year") if isinstance(diag.get("by_year"), dict) else {}
    if base_id in by_year:
        L += ["**逐年**(实际交易的信号)", "", by_year_table(by_year, [base_id]), ""]
    if isinstance(diag.get("decay"), dict) and diag["decay"]:
        first = next(iter(diag["decay"].values()))
        L += ["**不同预测期的 rank IC(fit 段)**", "", "| 变体 | " + " | ".join(f"h={r['horizon']}" for r in first) + " |",
              "|---" * (len(first) + 1) + "|"]
        for vid, rows in diag["decay"].items():
            L.append(f"| `{vid}` | " + " | ".join(_f(r["rank_ic"], 4) for r in rows) + " |")
        L.append("")
    L += [note("06_baseline"), ""]

    # ---- 7 ablations
    L += [f"## {SECTIONS[6]}", ""]
    for sid, ids in by_stage.items():
        L += [f"### {sid}", "", f"**问题**: {questions.get(sid, '')}", "", stage_table(results, ids), ""]
        fx = fixed_hl_table(results, ids)
        if fx and len(ids) > 1:
            L += ["<details><summary>同一半衰期下的多头腿(fit 段)—— 比结构之前先看这张</summary>", "", fx, "",
                  "</details>", ""]
        whys = [f"- `{i}` — {results[i].get('why', '')}" for i in ids if results[i].get("why")]
        if whys:
            L += ["<details><summary>每个变体为什么存在</summary>", "", *whys, "", "</details>", ""]
        L += [note(f"07_{sid}"), ""]
    if isinstance(diag.get("neutralise"), dict) and diag["neutralise"]:
        L += ["### 中性化(fit 段)", "",
              "> 被中性化的是**实际交易的信号**(方向 × 面板、按选定的半衰期平滑),对控制变量做秩空间逐日截面回归;"
              "残差不再平滑,直接建书 —— 所以残差的换手更高,**扣费夏普塌掉可能只是成本**;alpha 还在不在看 rank IC 与无成本夏普。"
              "R² 是控制变量张成的部分。", "",
              "| 变体 | 对谁中性化 | 截面 R² | rank IC | 多头腿毛超额 | 多头腿净超额 | 空头腿毛超额 | 无成本多空夏普 | 扣费多空夏普 | 多空日换手 |",
              "|---|---|---|---|---|---|---|---|---|---|"]
        for vid, entry in diag["neutralise"].items():
            for ctl, rec in entry.items():
                name = "_(未中性化的交易信号)_" if ctl == "_traded_signal" else ctl
                r2 = "—" if ctl == "_traded_signal" else _f(rec["r2"], 3, plus=False)
                if "r2_raw_panel" in rec:
                    r2 += f"(原始日频面板上 {_f(rec['r2_raw_panel'], 3, plus=False)})"
                L.append(f"| `{vid}` | {name} | {r2} | {_f(rec['rank_ic'], 4)} "
                         f"| {_f(rec['long_gross_ann'], pct=True)} | {_f(rec.get('long_ann'), pct=True)} "
                         f"| {_f(rec.get('short_gross_ann'), pct=True)} | {_f(rec.get('ls_gross_sharpe'))} "
                         f"| {_f(rec['ls_sharpe'])} | {_f(rec['ls_turnover'], pct=True, plus=False)} |")
        L += ["", note("07_neutralise"), ""]
    if isinstance(diag.get("conditional"), dict) and diag["conditional"]:
        L += ["### 条件 IC(fit 段)", "", "| 因子 \\| 分桶变量 | " + " | ".join(f"Q{i}" for i in range(1, 6)) + " |",
              "|---|---|---|---|---|---|"]
        for key, rows in diag["conditional"].items():
            L.append(f"| {key} | " + " | ".join(_f(r["rank_ic"], 4) for r in rows) + " |")
        L += ["", note("07_conditional"), ""]
    if isinstance(diag.get("controls"), dict) and diag["controls"]:
        L += ["### 控制变量 / 已知家族自己当因子(同口径)", "",
              "| 控制变量 | 方向 | rank IC(fit) | 半衰期 | 多头腿净超额 train/valid | 纯多头夏普 train/valid | 扣费多空夏普 train/valid | 多头日换手 |",
              "|---|---|---|---|---|---|---|---|"]
        for k, m in diag["controls"].items():
            L.append(f"| `{k}` | {'+' if m['sign'] > 0 else '−'} | {_f(m['rank_ic'], 4)} | {m['hl']:g} "
                     f"| {_pair(m.get('train_long_ann'), m.get('valid_long_ann'), pct=True)} "
                     f"| {_pair(m.get('train_long_sharpe'), m.get('valid_long_sharpe'))} "
                     f"| {_pair(m.get('train_ls_sharpe'), m.get('valid_ls_sharpe'))} "
                     f"| {_f(m.get('train_long_turnover', m.get('train_ls_turnover')), pct=True, plus=False)} |")
        L += ["", note("07_controls"), ""]
    for extra in sorted(notes.glob("07x_*.md")) if notes.is_dir() else []:     # bespoke analyses of this study
        L += [extra.read_text(encoding="utf-8").strip(), ""]

    # ---- 8 variants
    L += [f"## {SECTIONS[7]}", "", stage_table(results, list(results)), ""]
    all_corr = out_dir / "rank_corr_all.json"
    rc = json.loads(all_corr.read_text(encoding="utf-8")) if all_corr.is_file() else diag.get("rank_corr_train")
    if isinstance(rc, dict) and rc:
        ids = [i for i in (cfg.get("corr_ids") or []) + (cfg.get("corr_with") or []) if i in rc] or list(rc)[:16]
        L += ["**变体之间(以及与控制变量)的日截面 rank 相关(fit 段;变体用的是实际交易的信号,控制变量是原始面板)** — "
              "≥0.95 在 AlphaCube 里算同一因子族", "",
              rank_corr_table(rc, ids), ""]
    L += [note("08_variants"), ""]

    L += [f"## {SECTIONS[8]}", "", note("09_diagnosis"), ""]
    L += [f"## {SECTIONS[9]}", ""]
    finals = [vid for vid, r in results.items() if "holdout" in (r.get("books_user") or {}).get("splits", {})]
    if finals:
        L += ["**最终对比,与用户表同口径**(留出段 = 用户的测试段;多头口径 = 半衰期按纯多头书在用户训练段上选)", "",
              user_table(results, finals, user, pub, base_id), ""]
        yt = by_year_table(by_year, finals)
        if yt:
            L += ["**最终候选逐年**(含留出段年份;方向与半衰期是用户训练段上定的)", "", yt, ""]
    L += [note("10_distilled"), ""]
    L += [f"## {SECTIONS[10]}", "", note("11_risks"), ""]
    L += [f"## {SECTIONS[11]}", "", note("12_next"), ""]

    L += ["## 附录 A — 数据段使用台账", "", ledger.render_markdown(), ""]
    L += ["## 附录 B — 复现", "", "```bash"]
    for name, r in runs.items():
        L.append(f"# {name}: {r.get('seconds')}s, 峰值 anon {r.get('peak_anon_gb')} GiB, stages {r['stages']}")
    L += [f"scripts/run_server.sh {config_path} <stage...>          # EXTRA=--holdout 才读留出段",
          f"python -m partura.cli report {config_path}", "```", ""]
    if any_run:
        L += ["```json", json.dumps(any_run["provenance"], ensure_ascii=False, indent=1), "```", ""]

    dest = Path(research_dir or (PARTURA_ROOT / "research" / "alpha_distillation")) / f"{fid}.md"
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text("\n".join(L), encoding="utf-8")
    return dest


__all__ = ["build", "SECTIONS", "stage_table", "user_table", "fixed_hl_table", "by_year_table"]
