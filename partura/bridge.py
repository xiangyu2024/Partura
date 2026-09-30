"""Locate and import AlphaCube, and record exactly which version was used.

Partura never reimplements AlphaCube's store, parser, engine, label or
backtest primitives -- it imports them.  The only thing this module adds is
provenance: every Partura artefact carries the AlphaCube commit, the store
path and the library versions it was produced with, so a number in a report
can always be traced back to the code that made it.
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path
from typing import Dict, Optional

PARTURA_ROOT = Path(__file__).resolve().parents[1]


def alphacube_root() -> Path:
    """`$ALPHACUBE_ROOT`, else the sibling directory of the Partura checkout."""
    env = os.environ.get("ALPHACUBE_ROOT")
    cands = [Path(env)] if env else []
    cands += [PARTURA_ROOT.parent / "AlphaCube", Path.home() / "Desktop" / "AlphaCube",
              Path("/root/autodl-tmp/AlphaCube")]
    for c in cands:
        if (c / "src" / "alphacube" / "__init__.py").is_file():
            return c.resolve()
    raise RuntimeError(f"AlphaCube not found; set ALPHACUBE_ROOT (tried {[str(c) for c in cands]})")


def ensure_alphacube_on_path() -> Path:
    root = alphacube_root()
    src = str(root / "src")
    if src not in sys.path:
        sys.path.insert(0, src)
    return root


def _git(root: Path, *args: str) -> Optional[str]:
    try:
        out = subprocess.run(["git", "-C", str(root), *args], capture_output=True, text=True, timeout=10)
        return out.stdout.strip() or None if out.returncode == 0 else None
    except Exception:
        return None


def provenance(store_path: Optional[str] = None) -> Dict[str, object]:
    root = ensure_alphacube_on_path()
    import numpy
    import torch
    ac_commit = _git(root, "rev-parse", "--short", "HEAD")
    ac_dirty = bool(_git(root, "status", "--porcelain"))
    return {
        "alphacube_root": str(root),
        "alphacube_commit": ac_commit,
        "alphacube_dirty": ac_dirty,
        "partura_root": str(PARTURA_ROOT),
        "partura_commit": _git(PARTURA_ROOT, "rev-parse", "--short", "HEAD"),
        "store": store_path,
        "python": sys.version.split()[0],
        "torch": torch.__version__,
        "numpy": numpy.__version__,
        "host": os.uname().nodename,
    }


__all__ = ["PARTURA_ROOT", "alphacube_root", "ensure_alphacube_on_path", "provenance"]
