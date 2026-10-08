"""e7 read by the rule written in episodes/e7_PLAN.md: do priors learned from GP's own archives help a new search?

Local.  Three cells (e7c control, e7l learned priors, e7b the B01 priors), seeds 1..3, reward ``long``.

    main      quality yield = saved candidates with score >= 1.0 per 100 paid evaluations
    side      gate-failure share; best score; mean of the top ten; independent_distinct
    verdict   useful   = above the same-seed control in >= 2 of 3 seeds AND pooled >= 1.3 x the control
              useless  = pooled within +-15% of the control
              unclear  = anything else

    python scripts/e7_summary.py            -> prints the table, writes episodes/e7_summary.json
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from partura.steer import Guidance  # noqa: E402

root = Path(__file__).resolve().parents[1]
CELLS = {"e7c": ("对照(什么都不开)", "control"), "e7l": ("学到的先验(GP 存档,8 条)", "steer"), "e7b": ("B01 的先验(原样)", "steer")}
LINE = 1.0


def read(tag):
    hit = sorted((root / "episodes").glob(f"{tag}_I*/evidence.json"))
    if not hit:
        return None
    E = json.loads(hit[0].read_text(encoding="utf-8"))
    arm = CELLS[tag[:3]][1]
    A = E["arms"][arm]
    G = Guidance.load(root / E.get("guidance", "guidance/B01.yaml"))
    cs = [c for c in A["candidates"] if c.get("score") == c.get("score") and abs(c["score"]) != float("inf")]
    cs.sort(key=lambda c: -c["score"])
    good = [c for c in cs if c["score"] >= LINE]
    seen = set()
    for c in good:
        try:
            seen.add(G.dedup_key(c["expr"]))
        except ValueError:
            seen.add(c["expr"])
    fams = {}
    for c in good:                                             # families among the good ones: the main metric counts spellings, this counts things
        try:
            f = G.family_key(c["expr"])
        except ValueError:
            f = c["expr"]
        fams[f] = fams.get(f, 0) + 1
    samp = A.get("sampling") or {}
    top = [c["score"] for c in cs[:10]]
    return {"tag": tag, "seed": E["seed"], "arm": arm, "guidance": E.get("guidance"), "parts": E.get("parts"), "code": E.get("code"),
            "scored": A["scored"], "gate_fail": A["gate_fail"], "saved": len(cs), "good": len(good), "good_dedup": len(seen),
            "yield": 100.0 * len(good) / max(A["scored"], 1), "gate_share": A["gate_fail"] / max(A["scored"], 1),
            "best": cs[0]["score"] if cs else None, "top10": sum(top) / len(top) if top else None,
            "independent_distinct": A.get("independent_distinct"), "seconds": A["seconds"],
            "good_families": len(fams), "largest_family": max(fams.values(), default=0), "known_like": sum(1 for c in good if abs(c.get("rho_known") or 0.0) >= 0.7),
            "proposed": samp.get("proposed"), "thinned": samp.get("thinned"),
            "head": [[round(c["score"], 3), c["sign"], c["hl"], c.get("rho_known"), c["expr"]] for c in cs[:3]]}


rows = {cell: [r for r in (read(f"{cell}{s}") for s in (1, 2, 3)) if r] for cell in CELLS}
print(f"{'cell':5s} {'seed':>4s} {'scored':>6s} {'gate':>5s} {'gate%':>6s} {'saved':>5s} {'>=1.0':>5s} {'(dedup)':>7s} {'yield/100':>9s} {'best':>6s} {'top10':>6s} {'indep':>5s} {'sec':>5s}"
      f" {'fams':>5s} {'largest':>7s} {'known':>5s} {'thinned/proposed':>17s}")
for cell, rs in rows.items():
    for r in rs:
        th = f"{r['thinned']}/{r['proposed']}" if r["proposed"] else "-"
        print(f"{cell:5s} {r['seed']:4d} {r['scored']:6d} {r['gate_fail']:5d} {100 * r['gate_share']:5.0f}% {r['saved']:5d} {r['good']:5d} {r['good_dedup']:7d} "
              f"{r['yield']:9.1f} {r['best']:6.2f} {r['top10']:6.2f} {str(r['independent_distinct']):>5s} {r['seconds']:5.0f} {r['good_families']:5d} {r['largest_family']:7d} {r['known_like']:5d} {th:>17s}")

pooled = {}
for cell, rs in rows.items():
    sc, gd, gf = sum(r["scored"] for r in rs), sum(r["good"] for r in rs), sum(r["gate_fail"] for r in rs)
    pooled[cell] = {"runs": len(rs), "scored": sc, "good": gd, "good_dedup": sum(r["good_dedup"] for r in rs), "yield": 100.0 * gd / max(sc, 1),
                    "gate_share": gf / max(sc, 1), "best": max((r["best"] for r in rs), default=None),
                    "top10": sum(r["top10"] for r in rs) / max(len(rs), 1), "independent_distinct": sum(r["independent_distinct"] or 0 for r in rs),
                    "good_families": sum(r["good_families"] for r in rs), "families_per_100": 100.0 * sum(r["good_families"] for r in rs) / max(sc, 1),
                    "independent_per_100": 100.0 * sum(r["independent_distinct"] or 0 for r in rs) / max(sc, 1),
                    "thinned": sum(r["thinned"] or 0 for r in rs), "proposed": sum(r["proposed"] or 0 for r in rs)}
base = pooled["e7c"]
by_seed = {r["seed"]: r for r in rows["e7c"]}
verdict = {}
print()
for cell, P in pooled.items():
    line = f"{cell} {CELLS[cell][0]}: 三个种子合计 质量产出 {P['yield']:.1f} / 百次(≥1.0 的 {P['good']} 个、去重 {P['good_dedup']} 个,付费 {P['scored']} 次),没过门槛 {100 * P['gate_share']:.0f}%,最好 {P['best']:.2f},前十均分 {P['top10']:.2f},互不相关且不在已知池里 {P['independent_distinct']}"
    if cell != "e7c":
        wins = sum(1 for r in rows[cell] if r["seed"] in by_seed and r["yield"] > by_seed[r["seed"]]["yield"])
        ratio = P["yield"] / base["yield"] if base["yield"] else float("nan")
        v = "有用" if wins >= 2 and ratio >= 1.3 else ("没用" if abs(ratio - 1) <= 0.15 else "不确定")
        verdict[cell] = {"wins": wins, "ratio": ratio, "verdict": v}
        line += f" → 同种子胜 {wins}/3,合计是对照的 {ratio:.2f} 倍:**{v}**"
    line += f"\n      按族数:好候选的族 {P['good_families']} 个({P['families_per_100']:.1f} / 百次);实测互不相关 {P['independent_per_100']:.1f} / 百次" + (f";先验抽掉的提议 {P['thinned']}/{P['proposed']}" if P["proposed"] else "")
    print(line)
(root / "episodes" / "e7_summary.json").write_text(json.dumps({"line": LINE, "rows": rows, "pooled": pooled, "verdict": verdict}, ensure_ascii=False, indent=1), encoding="utf-8")
print("\nwrote episodes/e7_summary.json")
