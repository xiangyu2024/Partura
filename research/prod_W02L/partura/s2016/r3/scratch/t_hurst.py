import torch
torch.manual_seed(0)
d = 120
x = torch.cumsum(torch.randn(1, 300) * 0.02, dim=1) + 10.0  # a price-like path, treat as day_last(Close)
def rhurst(x, d):
    w = x.unfold(1, d, 1)  # windows
    mean = w.nanmean(dim=-1, keepdim=True)
    demean = w - mean
    cs = demean.cumsum(dim=-1)
    valid_cs = ~torch.isnan(cs)
    r_max = torch.where(valid_cs, cs, torch.full_like(cs, float("-inf"))).max(dim=-1).values
    r_min = torch.where(valid_cs, cs, torch.full_like(cs, float("inf"))).min(dim=-1).values
    R = r_max - r_min
    S = torch.sqrt(torch.nansum(demean.pow(2), dim=-1) / max(d - 1, 1))
    return R / S, R, S
base, R0, S0 = rhurst(x, d)
# same window, but one day in the middle (index 60 of window) suspended
xm = x.clone(); xm[0, 200 - 60] = float('nan')
print("clean  RS at last window:", base[0, -1].item(), "R", R0[0,-1].item(), "S", S0[0,-1].item())
mid, Rm, Sm = rhurst(xm, d)
print("1 missing at window pos 60 -> RS", mid[0, 200].item() if True else None)
# window ending at idx 200 contains global index 140..200 -> missing at global 140 is position 0 of that window
xs = x.clone(); xs[0, 170] = float('nan')  # window ending at 200 covers 81..200; 170 at pos 89
res, Rs, Ss = rhurst(xs, d)
print("window ending 200 with NaN at pos ~89: RS", res[0,200-d+1+0].item() if False else res[0, 200-d+1-0].item() if False else res[0, 200].item(), "R", Rs[0,200].item(), "S", Ss[0,200].item())
