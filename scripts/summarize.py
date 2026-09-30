"""Console digest of a Partura run: the few numbers a decision actually turns on.

    python scripts/summarize.py runs/<factor_id>/batch.json [baseline_id]
"""
import json
import sys
from pathlib import Path

path = Path(sys.argv[1])
base = sys.argv[2] if len(sys.argv) > 2 else "v_base"
d = json.loads(path.read_text(encoding="utf-8"))
res, diag = d["results"], d.get("diagnostics", {})

v = d["view"]
print(f"{d['factor_id']}  {v['days']}d x {v['symbols']}s  {v['first']}..{v['last']}  "
      f"cost {d['cost_per_side']*1e4:.0f}bp  splits {d['splits_used']}")
if d.get("errors"):
    print("errors:", d["errors"])

hdr = f"{'variant':<18}{'stage':<16}{'sgn':>4}{'rIC(tr)':>9}{'rICIR':>7}{'IC(tr)':>9}{'TO':>7}{'shN(tr)':>9}{'rIC(va)':>9}{'shN(va)':>9}"
print("\n" + hdr)
print("-" * len(hdr))
rows = [(k, r) for k, r in res.items() if "error" not in r]
rows.sort(key=lambda kr: -(kr[1]["splits"]["train"]["rank_ic"] or 0))
for k, r in rows:
    t, va = r["splits"]["train"], r["splits"].get("valid", {})
    print(f"{k:<18}{r['stage'][:15]:<16}{'+' if r['sign']>0 else '-':>4}"
          f"{t['rank_ic']:>9.4f}{t['rank_icir']:>7.3f}{t['ic']:>9.4f}{t['turnover']:>7.3f}"
          f"{t['sharpe_net']:>9.2f}{va.get('rank_ic', float('nan')):>9.4f}{va.get('sharpe_net', float('nan')):>9.2f}")

if diag.get("rank_corr_train"):
    m = diag["rank_corr_train"]
    if base in m:
        print(f"\n与 {base} 的日截面 rank 相关(训练段,|.|>=0.95 = 同一因子族):")
        for k, val in sorted(m[base].items(), key=lambda kv: -abs(kv[1]))[:16]:
            if k != base:
                print(f"  {k:<20}{val:+.3f}")

for vid, entry in (diag.get("neutralise") or {}).items():
    print(f"\n中性化 {vid}(训练段):")
    b = res[vid]["splits"]["train"]
    print(f"  {'(未中性化)':<16}{'R2 —':>10}  rIC {b['rank_ic']:+.4f}  shN {b['sharpe_net']:+.2f}  TO {b['turnover']:.3f}")
    for ctl, rec in entry.items():
        m2 = rec["metrics"]
        print(f"  {ctl:<16}R2 {rec['r2']:>7.3f}  rIC {m2['rank_ic']:+.4f}  shN {m2['sharpe_net']:+.2f}  TO {m2['turnover']:.3f}")

for key, rowsc in (diag.get("conditional") or {}).items():
    print(f"\n条件 IC  {key}:  " + "  ".join(f"Q{r['bucket']+1} {r['rank_ic']:+.4f}" for r in rowsc))

if diag.get("controls"):
    print("\n控制变量自身(训练段):")
    for k, m2 in diag["controls"].items():
        print(f"  {k:<14}{'+' if m2['sign']>0 else '-'}  rIC {m2['rank_ic']:+.4f}  shN {m2['sharpe_net']:+.2f}  TO {m2['turnover']:.3f}")

for vid, rowsy in (diag.get("by_year") or {}).items():
    sc = diag.get("by_year_scope")
    print(f"\n逐年 {vid} ({sc[0] if sc else ''}..{sc[1] if sc else ''}):")
    for r in rowsy:
        print(f"  {r['year']}  rIC {r['rank_ic']:+.4f}  net {r['net_pnl']:+.3f}  shN {r['sharpe_net']:+.2f}  TO {r['turnover']:.3f}")

for vid, rowsd in (diag.get("decay") or {}).items():
    print(f"\n衰减 {vid}: " + "  ".join(f"h{r['horizon']} {r['rank_ic']:+.4f}" for r in rowsd))

for vid, rowse in (diag.get("extreme_days") or {}).items():
    print(f"\n极端日 {vid}: " + "  ".join(f"drop{r['dropped_frac']:.0%} shN {r['sharpe_net']:+.2f}" for r in rowse))
