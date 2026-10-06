"""The test-period read of one study as a Markdown table, with the paired comparisons against the benchmarks.

Local.  Reads runs/<fid>/sweepfinal_<tag>.json (scripts/sweep_final.py; the candidates were picked by a rule on
train / valid before the test period was opened) and prints one row per candidate: the pure long book in and out of
sample, and the paired daily difference against the known family and against the generic screen.

    python scripts/paired_table.py <factor_id> [--sweep s1]
"""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
argv = sys.argv[1:]
fid = argv[0]
SW = argv[argv.index("--sweep") + 1] if "--sweep" in argv else "s1"
F = json.loads((root / "runs" / fid / f"sweepfinal_{SW}.json").read_text(encoding="utf-8"))
R = F["results"]


def pair(r, ref):
    p = (r.get("paired") or {}).get(ref)
    if not p or p["utrain"]["ann"] != p["utrain"]["ann"]:
        return "—", "—"
    i, o = p["utrain"], p["holdout"]
    return f"{i['ann']:+.1%}(IR {i['ir']:+.2f})", f"{o['ann']:+.1%}(t {o['t']:+.1f})"


print("| 候选 | 样本内:净超额 / 夏普 | 样本外:净超额 / 夏普 | 减已知族:样本内 | 减已知族:样本外 | 减通用筛子:样本内 | 减通用筛子:样本外 |")
print("|---|---|---|---|---|---|---|")
for k, r in R.items():
    v = r["books_user"]["by_rank"]["long"]
    a, h = v["splits"]["utrain"], v["splits"]["holdout"]
    tag = "**规则挑出**" if k in F.get("overlay", []) or k in F.get("picks", []) else ("基准" if r["kind"] in ("base", "bench") else "原样检验")
    print(f"| `{k}`({tag},半衰期 {v['hl']:g}) | {a['long_ann']:+.1%} / {a['long_sharpe']:.2f} | {h['long_ann']:+.1%} / {h['long_sharpe']:.2f} | "
          + " | ".join(pair(r, "k_known") + pair(r, "k_known_xfrozen")) + " |")
