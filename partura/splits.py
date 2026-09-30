"""Date splits and the holdout ledger.

AlphaCube's GP selects on the whole 2018-2025 panel, so *everything* an
archive reports is in-sample.  Partura's job is model selection on top of an
already-selected expression, which is exactly the situation where a test set
quietly turns into a validation set.  So:

* ``train``   -- every hypothesis, every ablation, every mutation is judged here.
* ``valid``   -- used to confirm the few candidates that survived train.
* ``holdout`` -- read as few times as possible, ideally once, at the very end.

The ledger is a JSON file next to the run: each time metrics are computed on
a split it records the split, how many expressions were scored and why.  A
report that quotes the holdout must also quote the ledger, so the reader can
see how used-up that period is.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, List, Optional, Tuple

# The production view of the AlphaCube store: 20180102..20251231, 1942 trading days.
SPLITS: Dict[str, Tuple[str, str]] = {
    "train":   ("20180102", "20211231"),
    "valid":   ("20220101", "20231231"),
    "holdout": ("20240101", "20251231"),
    "full":    ("20180102", "20251231"),
}

DECISION_SPLITS = ("train", "valid")


@dataclass
class LedgerEntry:
    when: str
    split: str
    n_expressions: int
    purpose: str
    stage: str


class Ledger:
    """Append-only record of which split was looked at, how often, for what."""

    def __init__(self, path: Path) -> None:
        self.path = Path(path)
        self.entries: List[LedgerEntry] = []
        if self.path.is_file():
            raw = json.loads(self.path.read_text(encoding="utf-8"))
            self.entries = [LedgerEntry(**e) for e in raw.get("entries", [])]

    def record(self, split: str, n_expressions: int, purpose: str, stage: str = "") -> None:
        self.entries.append(LedgerEntry(
            when=datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
            split=split, n_expressions=int(n_expressions), purpose=purpose, stage=stage))
        self.flush()

    def flush(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(json.dumps(
            {"entries": [e.__dict__ for e in self.entries], "summary": self.summary()},
            ensure_ascii=False, indent=2), encoding="utf-8")

    def summary(self) -> Dict[str, Dict[str, int]]:
        out: Dict[str, Dict[str, int]] = {}
        for e in self.entries:
            s = out.setdefault(e.split, {"reads": 0, "expressions": 0})
            s["reads"] += 1
            s["expressions"] += e.n_expressions
        return out

    def warning(self) -> Optional[str]:
        s = self.summary().get("holdout")
        if not s:
            return None
        if s["reads"] > 1:
            return (f"留出段已被读取 {s['reads']} 次、累计打分 {s['expressions']} 条表达式 —— "
                    f"它已经不是干净的测试集,后续数字应按验证段口径解读。")
        return f"留出段被读取 1 次({s['expressions']} 条表达式)。"

    def render_markdown(self) -> str:
        lines = ["| 数据段 | 区间 | 读取次数 | 累计打分表达式 |", "|---|---|---|---|"]
        summ = self.summary()
        for name, (a, b) in SPLITS.items():
            s = summ.get(name, {"reads": 0, "expressions": 0})
            lines.append(f"| {name} | {a}–{b} | {s['reads']} | {s['expressions']} |")
        w = self.warning()
        if w:
            lines += ["", f"> {w}"]
        return "\n".join(lines)


__all__ = ["SPLITS", "DECISION_SPLITS", "Ledger", "LedgerEntry"]
