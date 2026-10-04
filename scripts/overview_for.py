"""What the batch overview says about one factor: its nearest neighbours among
the batch, among the controls and among the known families, and how much of it
the controls span.  (Signals are sign x panel, EMA-smoothed at the published
half-life, on the fit split -- i.e. the thing that would actually be traded.)

    python scripts/overview_for.py <factor_id> [batch_dir]
"""
import json
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
fid = sys.argv[1]
d = json.loads((root / "runs" / (sys.argv[2] if len(sys.argv) > 2 else "_batch_B01") / "overview.json")
               .read_text(encoding="utf-8"))
if fid not in d["corr"]:
    raise SystemExit(f"{fid} is not in the overview (its base panel failed?)")
row = d["corr"][fid]
info = d["info"]
print(f"== {fid}  ({info[fid]['lib']} {info[fid]['name']}; 方向 {info[fid]['sign']:+d}, 半衰期 {info[fid]['hl']}) ==")
print("可交易信号(方向 x 面板,按公布的半衰期平滑)在 train 上的日截面 rank 相关:")
batch = sorted(((k, v) for k, v in row.items() if k in info and k != fid), key=lambda kv: -abs(kv[1]))
print("  本批其他因子: " + "  ".join(f"{k.split('_')[0]}({info[k]['name']}) {v:+.2f}" for k, v in batch[:6]))
print("  控制变量:     " + "  ".join(f"{k} {row[k]:+.2f}" for k in sorted(d["controls"], key=lambda k: -abs(row.get(k, 0)))
                                   if k in row))
print("  已知家族:     " + "  ".join(f"{k} {row[k]:+.2f}" for k in d["known"] if k in row))
sp = d["span"].get(fid, {})
print(f"控制变量能张成它多少(秩空间逐日回归的 R²): 全部 {sp.get('r2_all_controls', float('nan')):.3f};单个: " +
      "  ".join(f"{k} {sp[k]:.3f}" for k in sorted(d["controls"], key=lambda k: -sp.get(k, 0)) if k in sp))
print("(注意:控制变量的符号没有对齐方向;相关的正负要结合因子方向读。|相关| ≥ 0.95 在 AlphaCube 里算同一因子族。)")
