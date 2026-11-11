import sys
sys.path.insert(0, "/Users/wxy/Desktop/AlphaCube-steering/src")
import torch
from alphacube.operators.dt_in import in_regres, in_mean_full, in_stddev_full
from alphacube.operators.dt_day import day_kurt
from alphacube.operators.common import create_like, add, div
torch.manual_seed(0)
# synthetic minute returns: 300 days x 241 minutes, scale ~1e-3 (NOT market data)
ret = torch.randn(300, 241, dtype=torch.float32) * 1e-3
r = in_regres(ret, in_mean_full(ret), 20)
print("resid abs max", float(r[20:].abs().max()), "resid std", float(r[20:].std()))
print("ret std", float(ret.std()))
z = div(r, torch.add(in_stddev_full(r), 1e-6))
print("Z abs max", float(torch.nan_to_num(z).abs().max()), "Z std", float(torch.nan_to_num(z).std()))
k = day_kurt(z)
print("day_kurt first 5", k[:5].flatten().tolist())
print("day_kurt nan frac", float(torch.isnan(k).float().mean()))
