"""The lab notebook: what carries over between studies.

An expression's experiment plan does not transfer -- the next tree has
different nodes and needs different questions.  What DOES transfer is what
earlier studies established about the operators themselves, and losing that is
how an agent ends up re-deriving "``day_durbin_watson`` on a price level is
realized variance" from scratch every time.

So findings are stored here, keyed by the operator (and optionally the operand
kind or a structural pattern) they are about, each with the evidence that
established it and the study it came from.  When a new expression is parsed,
``recall`` surfaces the ones that touch it.

**A recalled finding is a prior, not a fact.**  It was measured on one store,
one period and one operand.  The report prints it as such, with the
``recheck`` field saying what would make it stop being true, and any finding a
study actually leans on should be re-measured inside that study.
"""

from __future__ import annotations

from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Dict, List, Optional, Sequence

import yaml

from .bridge import PARTURA_ROOT, ensure_alphacube_on_path

DEFAULT_PATH = PARTURA_ROOT / "lab" / "findings.yaml"


@dataclass
class Finding:
    id: str
    claim: str
    evidence: str
    study: str
    date: str = ""
    operators: List[str] = field(default_factory=list)
    operand_kind: Optional[str] = None       # "price" | "flow" | "return" | None
    pattern: Optional[str] = None            # substring of Expression.key(), e.g. "O:cross_max(O:day_cov"
    confidence: str = "medium"               # low | medium | high
    recheck: str = ""

    def to_dict(self) -> dict:
        return {k: v for k, v in asdict(self).items() if v not in (None, "", [])}


class Lab:
    def __init__(self, path: Path = DEFAULT_PATH) -> None:
        self.path = Path(path)
        self.findings: List[Finding] = []
        if self.path.is_file():
            raw = yaml.safe_load(self.path.read_text(encoding="utf-8")) or {}
            self.findings = [Finding(**f) for f in raw.get("findings", [])]

    def save(self) -> None:
        self.path.parent.mkdir(parents=True, exist_ok=True)
        self.path.write_text(
            yaml.safe_dump({"findings": [f.to_dict() for f in self.findings]},
                           allow_unicode=True, sort_keys=False, width=100),
            encoding="utf-8")

    def record(self, f: Finding) -> None:
        f.date = f.date or date.today().isoformat()
        self.findings = [x for x in self.findings if x.id != f.id] + [f]
        self.save()

    def recall(self, expr, exclude_study: Optional[str] = None) -> List[Finding]:
        """Findings that touch this tree: same operator, or a matching pattern.

        ``exclude_study`` drops the ones this very study produced -- a report
        quoting its own conclusions back at itself as "prior evidence" is
        circular, and the first study of a tree should see an empty notebook.
        """
        ops = {n.spec.name for n in expr.nodes() if n.spec is not None}
        key = expr.key()
        hits = []
        for f in self.findings:
            if exclude_study and f.study == exclude_study:
                continue
            if f.pattern and f.pattern in key:
                hits.append(f)
            elif f.operators and ops & set(f.operators):
                hits.append(f)
        return hits

    def render_markdown(self, hits: Sequence[Finding]) -> str:
        if not hits:
            return ("_(实验室里没有与这棵树相关的、来自**其他**研究的既往结论 —— "
                    "本研究自己的结论不算先验。)_")
        lines = ["> **这些是既往研究的先验,不是本研究的结论。** 它们是在别的表达式、别的时间段上测出来的;"
                 "本报告如果依赖其中任何一条,必须在本研究里重新测一次。", "",
                 "| 结论 | 证据 | 出处 | 置信 | 什么情况下会失效 |", "|---|---|---|---|---|"]
        for f in hits:
            lines.append(f"| {f.claim} | {f.evidence} | `{f.study}` ({f.date}) | {f.confidence} | "
                         f"{f.recheck or '—'} |")
        return "\n".join(lines)


def recall_for(src: str, path: Path = DEFAULT_PATH, n_minutes: int = 241,
               exclude_study: Optional[str] = None) -> List[Finding]:
    ensure_alphacube_on_path()
    from alphacube.parser import parse
    e = parse(src, strict=False, coerce_daily=True, n_minutes=n_minutes, allow_general=True)
    return Lab(path).recall(e, exclude_study=exclude_study)


__all__ = ["Finding", "Lab", "recall_for", "DEFAULT_PATH"]
