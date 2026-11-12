import yaml
ONE="create_like(in_slice(Close, 1, 1), 1)"; ZERO="create_like(in_slice(Close, 1, 1), 0)"
def occ(k,lab="in_roll_labels(Close, 241)"): return f"day_mean(select_where(eq({lab}, {k}), {ONE}, {ZERO}))"
A=occ(4); A0=occ(0); A2=occ(2)
Aw=f"day_wmean(select_where(eq(in_roll_labels(Close, 241), 4), {ONE}, {ZERO}), Volume)"
RET="ts_delta(log(day_last(Close)), 1)"
E=[
 f"cross_autocorr_s1({A}, 241)",
 f"cross_mean(cs_bucket_demean({A}, day_std(Ret)), 60)",
 f"cross_mean(cs_bucket_zscore({A}, LogFloatCap), 120)",
 f"cross_mean(sub({A}, {A0}), 60)",
 f"cross_regbeta({RET}, cross_delay({A}, 1), 120)",
 f"cross_corr(cross_delay({A}, 1), {RET}, 120)",
 f"cross_hurst({A}, 241)",
 f"cross_stddev({A}, 60)",
 f"cross_tail_mean_q75({A}, 120)",
 f"cross_mean(cross_zscore({A}, 241), 20)",
 f"sub(cross_mean({A}, 20), cross_mean({A}, 241))",
 f"cross_ema({A}, 60)",
 f"cross_mean(sub({Aw}, {A}), 60)",
 f"cross_mean(div({A}, add({A2}, 0.01)), 60)",
 f"mul(cs_demean(cs_rank(cross_mean({A}, 60))), cs_demean(cs_rank(cross_stddev({A}, 60))))",
 f"cross_mean(mul({A}, is_gt(day_std(Ret), cross_mean(day_std(Ret), 20))), 60)",
]
Z="div(sub(day_wmean(Close, Volume), day_mean(Close)), add(day_std(Close), 0.001))"
CL="div(sub(day_last(Close), day_wmean(Close, Volume)), add(day_std(Close), 0.001))"
N=[
 Z,
 f"cross_mean({Z}, 60)",
 f"cross_mean({Z}, 120)",
 f"cross_ema({Z}, 60)",
 f"cross_autocorr_s1({Z}, 241)",
 f"cross_mean(cs_bucket_demean({Z}, day_std(Ret)), 60)",
 f"cross_mean(cs_bucket_zscore({Z}, LogFloatCap), 120)",
 f"cross_mean(div(sub(day_wmean(Close, Amt), day_mean(Close)), add(day_std(Close), 0.001)), 60)",
 f"cross_stddev({Z}, 60)",
 f"cross_regbeta({RET}, cross_delay({Z}, 1), 120)",
 f"cross_mean(mul({Z}, is_gt(day_sum(Volume), cross_mean(day_sum(Volume), 20))), 60)",
 f"cross_mean({CL}, 60)",
 f"cross_mean(cross_rank({Z}, 241), 20)",
 f"sub(cross_mean({Z}, 20), cross_mean({Z}, 241))",
 f"cross_mean(sub(cs_rank({Z}), cs_rank({CL})), 60)",
 f"cross_mean(cs_bucket_demean({CL}, day_std(Ret)), 120)",
]
open("e.txt","w").write("\n".join(E)); open("n.txt","w").write("\n".join(N))
