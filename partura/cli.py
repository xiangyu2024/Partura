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


def _decompose(a) -> int:
    from .decompose import decompose
    from .runner import load_config
    from .semantics import render_markdown
    src = a.expression
    if a.config:
        src = load_config(a.config)["expression"]
    d = decompose(src)
    print("## 算子的真实语义(注册表 + 探针实测)\n")
    print(render_markdown(d.dossiers))
    print("## 数学分解\n")
    print(d.render_markdown())
    return 0


def _run(a) -> int:
    from .runner import run
    run(a.config, a.stages, store=a.store, device=a.device, chunk_symbols=a.chunk_symbols,
        chunk_days=a.chunk_days, gpu_fraction=a.gpu_fraction, mirror_root=a.mirror_root,
        max_symbols=a.max_symbols, torch_threads=a.torch_threads, workdir=a.workdir,
        out_root=a.out_root, use_holdout=a.holdout, diagnostics=not a.no_diagnostics)
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
    d.set_defaults(fn=_decompose)

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
