"""Do the hypotheses of a sweep parse?  (server side; see `study.sh hypo`)

An entry is `id: {expr: "...", why: "..."}` (or just `id: "expr"`); `lock: true` pins its direction to the way the
expression is written (partura/hypo.py) -- the value must be a real boolean.  `base: <id>` marks a modification of another
object; the id must be an entry of this file or one of v_base / k_known / k_known_xfrozen.  `twin: <id>` names the comparison object of a
hypothesis (same rule for the id); `kind: carrier` marks an object that exists to be someone's base.

    python scripts/check_hypo.py studies/<fid>/hypo.yaml
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import yaml  # noqa: E402

from partura.hypo import BENCHMARK_IDS, base_of, kind_of, lock_of, twin_key_of  # noqa: E402
from partura.panels import parse_research  # noqa: E402

try:
    d = yaml.safe_load(Path(sys.argv[1]).read_text(encoding="utf-8")) or {}
except yaml.YAMLError as exc:
    mark = getattr(exc, "problem_mark", None)
    where = f"第 {mark.line + 1} 行第 {mark.column + 1} 列附近" if mark else ""
    print(f"YAML 写法有误 {where}:{getattr(exc, 'problem', exc)}\n"
          "常见原因:键后面的冒号要跟一个空格(`h_x: {expr: \"…\", why: \"…\"}`);表达式里的引号要成对;why 里有冒号时整句加引号。")
    sys.exit(2)
bad = 0
for i, v in d.items():
    e = v["expr"] if isinstance(v, dict) else str(v)
    try:
        lock = lock_of(str(i), v)
        base, twin, kind = base_of(str(i), v), twin_key_of(str(i), v), kind_of(str(i), v)
        for what, ref in (("base", base), ("twin", twin)):
            if ref is not None and ref not in d and ref not in BENCHMARK_IDS:
                raise ValueError(f"hypothesis {i}: {what} {ref!r} is neither an entry of this file nor one of {', '.join(BENCHMARK_IDS)}")
        parse_research(e)
        print(f"OK    {i}" + ("  [lock: direction as written]" if lock else "") + (f"  [base: {base}]" if base else "")
              + (f"  [twin: {twin}]" if twin else "") + (f"  [kind: {kind}]" if kind else ""))
    except Exception as exc:  # noqa: BLE001
        bad += 1
        print(f"FAIL  {i}: {type(exc).__name__}: {str(exc)[:220]}\n      {e[:200]}")
print(f"{len(d) - bad}/{len(d)} parse")
sys.exit(1 if bad else 0)
