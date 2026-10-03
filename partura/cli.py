"""Partura command line.

    python -m partura.cli decompose "cross_max(day_cov(Amt, Low), 9)"
    python -m partura.cli decompose --config configs/F001.yaml
    python -m partura.cli run configs/F001.yaml --store <cube> --stages S1 S2 --device cuda
    python -m partura.cli report configs/F001.yaml
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .bridge import PARTURA_ROOT


def _study_probes(cfg: dict, config_path=None) -> None:
    """A study may ask questions the built-in probes do not. Load them before
    anything measures an operator."""
    from .probes import load_study_probes
    for p in (cfg.get("probes") or []):
        added = load_study_probes(p)
        if added:
            print(f"[probes] {p}: +{', '.join(added)}")


def _decompose(a) -> int:
    from .decompose import decompose
    from .runner import load_config
    from .semantics import render_markdown
    from .lab import Lab
    from .panels import parse_research
    src = a.expression
    cfg = {}
    if a.config:
        cfg = load_config(a.config)
        src = cfg["expression"]
    if a.probes:
        cfg = {**cfg, "probes": list(cfg.get("probes") or []) + list(a.probes)}
    _study_probes(cfg)
    d = decompose(src)
    print("## 算子的真实语义(注册表 + 探针实测)\n")
    print(render_markdown(d.dossiers, show_questions=True))
    print("## 数学分解\n")
    print(d.render_markdown())
    hits = Lab().recall(parse_research(src), exclude_study=cfg.get("factor_id"))
    print("\n## 实验室里与这棵树相关的既往结论(先验,不是证据)\n")
    print(Lab().render_markdown(hits))
    return 0


def _propose(a) -> int:
    from .propose import propose, to_yaml
    from .lab import Lab
    from .panels import parse_research
    if a.probes:
        _study_probes({"probes": list(a.probes)})
    cands = propose(a.expression, max_substitutes=a.max_substitutes, max_fields=a.max_fields)
    text = to_yaml(a.expression, a.factor_id, cands, title=a.title or "")
    if a.out:
        from pathlib import Path
        Path(a.out).write_text(text, encoding="utf-8")
        print(f"wrote {a.out}: {len(cands)} 条候选 —— 这是**候选**,不是计划,请逐条删改后再跑")
    else:
        print(text)
    hits = Lab().recall(parse_research(a.expression))
    if hits:
        print(f"\n# 实验室里有 {len(hits)} 条与这棵树相关的既往结论,先看一眼再定计划:")
        for f in hits:
            print(f"#   [{f.confidence}] {f.claim}  ({f.study})")
    return 0


def _lab(a) -> int:
    from .lab import Lab, recall_for
    lab = Lab()
    if a.expression:
        hits = recall_for(a.expression)
        print(lab.render_markdown(hits))
    else:
        for f in lab.findings:
            ops = ", ".join(f.operators) or f.pattern or "—"
            print(f"[{f.confidence:<6}] {f.id}\n    算子: {ops}\n    {f.claim}\n    证据: {f.evidence}\n"
                  f"    出处: {f.study} {f.date}\n    失效条件: {f.recheck or '—'}\n")
    return 0


def _run(a) -> int:
    from . import guard
    guard.limit_threads(a.torch_threads or 2)          # before numpy/torch build their pools
    from .runner import run
    with guard.slot():                                 # at most PARTURA_SLOTS studies run at once
        run(a.config, a.stages, store=a.store, device=a.device, chunk_symbols=a.chunk_symbols,
            chunk_days=a.chunk_days, gpu_fraction=a.gpu_fraction, mirror_root=a.mirror_root,
            max_symbols=a.max_symbols, torch_threads=a.torch_threads, workdir=a.workdir,
            out_root=a.out_root, use_holdout=a.holdout, diagnostics=not a.no_diagnostics,
            batch=a.batch, cpu_fallback=a.cpu_fallback, cache_dir=a.cache_dir, tag=a.tag)
    return 0


def _report(a) -> int:
    from .report import build
    out = build(a.config, out_root=a.out_root, notes_dir=a.notes)
    print(f"wrote {out}")
    return 0


def main(argv=None) -> int:
    p = argparse.ArgumentParser(prog="partura")
    sub = p.add_subparsers(dest="cmd", required=True)

    d = sub.add_parser("decompose", help="operator dossiers + SSA decomposition")
    d.add_argument("expression", nargs="?", default=None)
    d.add_argument("--config")
    d.add_argument("--probes", nargs="*", default=[], help="study-specific probe files")
    d.set_defaults(fn=_decompose)

    pr = sub.add_parser("propose", help="derive CANDIDATE experiments from this tree (to be curated)")
    pr.add_argument("expression")
    pr.add_argument("--factor-id", required=True)
    pr.add_argument("--title", default="")
    pr.add_argument("--out", default=None)
    pr.add_argument("--max-substitutes", type=int, default=3)
    pr.add_argument("--max-fields", type=int, default=3)
    pr.add_argument("--probes", nargs="*", default=[])
    pr.set_defaults(fn=_propose)

    lb = sub.add_parser("lab", help="findings that carry over between studies")
    lb.add_argument("expression", nargs="?", default=None, help="recall what touches this tree")
    lb.set_defaults(fn=_lab)

    r = sub.add_parser("run", help="evaluate a stage and write its JSON")
    r.add_argument("config")
    r.add_argument("--store", required=True)
    r.add_argument("--stages", nargs="*", default=[])
    r.add_argument("--device", default="cpu")
    r.add_argument("--gpu-fraction", type=float, default=None)
    r.add_argument("--chunk-symbols", type=int, default=None)
    r.add_argument("--chunk-days", type=int, default=None)
    r.add_argument("--mirror-root", default=None)
    r.add_argument("--max-symbols", type=int, default=None)
    r.add_argument("--torch-threads", type=int, default=None)
    r.add_argument("--workdir", default=None)
    r.add_argument("--out-root", default=None)
    r.add_argument("--holdout", action="store_true", help="also score the final holdout split (ledgered)")
    r.add_argument("--no-diagnostics", action="store_true")
    r.add_argument("--batch", type=int, default=4, help="expressions per engine call")
    r.add_argument("--cpu-fallback", action="store_true",
                   help="retry GPU failures on the CPU engine (a hand-written factor can take ~40 GB there)")
    r.add_argument("--cache-dir", default=None)
    r.add_argument("--tag", default=None, help="output file stem (default: the stage ids)")
    r.add_argument("--probes", nargs="*", default=[])
    r.set_defaults(fn=_run)

    rep = sub.add_parser("report", help="assemble the markdown research report")
    rep.add_argument("config")
    rep.add_argument("--out-root", default=None)
    rep.add_argument("--notes", default=str(PARTURA_ROOT / "notes"))
    rep.set_defaults(fn=_report)

    a = p.parse_args(argv)
    if a.cmd == "decompose" and not a.expression and not a.config:
        p.error("decompose needs an expression or --config")
    return a.fn(a)


if __name__ == "__main__":
    sys.exit(main())
