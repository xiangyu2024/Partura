"""Do the hypotheses of a sweep parse?  (server side; see `study.sh hypo`)

    python scripts/check_hypo.py studies/<fid>/hypo.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import yaml  # noqa: E402

from partura.panels import parse_research  # noqa: E402

d = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8")) or {}
bad = 0
for i, v in d.items():
    e = v["expr"] if isinstance(v, dict) else str(v)
    try:
        parse_research(e)
        print(f"OK    {i}")
    except Exception as exc:  # noqa: BLE001
        bad += 1
        print(f"FAIL  {i}: {type(exc).__name__}: {str(exc)[:220]}\n      {e[:200]}")
print(f"{len(d) - bad}/{len(d)} parse")
sys.exit(1 if bad else 0)
