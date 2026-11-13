import struct, math, random
def f32(v):
    return struct.unpack('f', struct.pack('f', v))[0]
random.seed(0)
for s in [5e-5, 1e-4, 2e-4, 3e-4]:
    ups = [f32(abs(random.gauss(0, s))) for _ in range(241)]
    ups = [u for u in ups if u > 0]  # pow of negatives -> NaN; keep up-minutes
    p2 = [f32(f32(u ** 2.5) ** 2.5) if u > 0 else 0.0 for u in ups]
    m = f32(sum(p2) / len(p2))
    sq = [f32(f32(x - m) ** 2) for x in p2]   # pow(x_demean, 2) in float32
    var = f32(sum(sq) / len(sq))
    sd = f32(math.sqrt(var))
    print(f"sigma={s:g} mean(r^6.25)={m:.3g} var_f32={var:.3g} zero={var == 0.0} sum_sq_zero_frac={sum(1 for x in sq if x==0)/len(sq):.2f}")
