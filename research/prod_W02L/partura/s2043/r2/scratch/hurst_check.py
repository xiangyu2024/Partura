import numpy as np
rng = np.random.default_rng(0)
def rs_hurst(x):
    # same algebra as dt_day._hurst_rows
    T = len(x)
    xd = x - x.mean()
    cs = np.cumsum(xd)
    R = cs.max() - cs.min()
    S = np.sqrt(np.mean(xd**2))
    return np.log(R/S)/np.log(T)
def sim(n=2000, T=240):
    lv, inc = [], []
    for _ in range(n):
        r = rng.normal(0, 1e-3, T)           # iid minute returns: true persistence H = 0.5 on increments
        p = 10*np.exp(np.cumsum(r))          # price level path
        lv.append(rs_hurst(p)); inc.append(rs_hurst(r))
    lv, inc = np.array(lv), np.array(inc)
    return lv, inc
lv, inc = sim()
print('iid returns, T=240: hurst on price LEVELS mean %.3f sd %.3f | hurst on RETURNS mean %.3f sd %.3f' % (lv.mean(), lv.std(), inc.mean(), inc.std()))
