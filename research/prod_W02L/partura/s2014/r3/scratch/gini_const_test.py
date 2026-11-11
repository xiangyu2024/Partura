import numpy as np
def gini_formula(v):
    x = np.abs(v.astype(np.float32))
    x = np.sort(x)
    n = np.float32(x.shape[0])
    idx = np.arange(1, x.shape[0]+1, dtype=np.float32)
    tot = x.sum(dtype=np.float32)
    g = (np.float32(2.0) * (x*idx).sum(dtype=np.float32) / (n * tot)) - (n + np.float32(1.0)) / n
    return g
rng = np.random.default_rng(0)
cs = np.round(rng.uniform(3, 150, 20000).astype(np.float32), 2)
gs = np.array([gini_formula(np.full(241, c, dtype=np.float32)) for c in cs])
print("constant-day gini: n", len(gs), "min", gs.min(), "max", gs.max())
print("share exactly 0:", np.mean(gs == 0), " share >0:", np.mean(gs > 0), " share <0:", np.mean(gs < 0))
print("share |g|<1e-5:", np.mean(np.abs(gs) < 1e-5))
print("quantiles of positive gs:", np.quantile(gs[gs>0], [0.5, 0.9, 0.99]) if (gs>0).any() else None)
