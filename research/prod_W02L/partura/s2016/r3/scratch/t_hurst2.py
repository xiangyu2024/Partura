import math, random
random.seed(1)
d = 120
x = []
p = 10.0
for _ in range(300):
    p += random.gauss(0, 0.2)
    x.append(p)

def rs(w):
    # mirrors dt_cross.cross_hurst: nanmean, demean, cumsum (NaN propagates), valid_cs filter, S over nansum/(d-1)
    vals = [v for v in w if not math.isnan(v)]
    m = sum(vals)/len(vals)
    dem = [v - m if not math.isnan(v) else float('nan') for v in w]
    cs = []
    acc = 0.0
    nan_seen = False
    for v in dem:
        if nan_seen or math.isnan(v):
            nan_seen = True
            cs.append(float('nan'))
        else:
            acc += v
            cs.append(acc)
    vc = [c for c in cs if not math.isnan(c)]
    if not vc: return (float('nan'),)*3
    R = max(vc) - min(vc)
    S = math.sqrt(sum(v*v for v in dem if not math.isnan(v)) / (d-1))
    return R, S, R/S

full = x[200-d+1:201]
print("clean window RS:", rs(full))
for pos in [0, 30, 60, 90, 119]:
    w = list(full); w[pos] = float('nan')
    print("NaN at window pos", pos, "->", rs(w))
