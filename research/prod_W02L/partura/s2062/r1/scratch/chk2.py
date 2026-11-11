import sys
sys.path.insert(0, "/Users/wxy/Desktop/AlphaCube-steering/src")
import torch
from alphacube.operators.dt_in import in_regres, in_mean_full, in_stddev_full
from alphacube.operators.dt_day import day_kurt
torch.manual_seed(0)
ret = torch.randn(300, 241, dtype=torch.float32) * 1e-3
r = in_regres(ret, in_mean_full(ret), 20)
rr = r[:, 19:]  # complete windows, minute axis
print("share exactly zero", float((rr == 0).float().mean()))
print("resid abs max", float(rr.abs().max()), "median abs", float(rr.abs().median()))
print("ret typical", float(ret.abs().median()))
print("share non-nan", float(torch.isfinite(rr).float().mean()))
# double precision comparison
ret64 = ret.double()
r64 = in_regres(ret64, in_mean_full(ret64), 20)[:, 19:]
print("float64 resid abs max", float(r64.abs().max()))
