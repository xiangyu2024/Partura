C='in_topk_masked(Ret, Volume, 20)'
D='in_topk_masked(Ret, Volume, 20, False)'
U=f'day_sum({C})'; L=f'day_sum({D})'
E_SEEDS=[
 f'div(sub({U}, {L}), cross_mean(day_sum(Volume), 60))',
 f'cross_mean(div(sub({U}, {L}), cross_mean(day_sum(Volume), 60)), 20)',
 f'sub(log({U}), log({L}))',
 f'cross_mean(sub(log({U}), log({L})), 30)',
 f'div({U}, cross_mean(day_sum(Volume), 60))',
 f'cross_zscore(log({U}), 60)',
 f'cs_regres(cross_mean({U}, 20), cross_mean(day_sum(Volume), 60))',
 f'cs_bucket_zscore(cross_mean(div({U}, cross_mean(day_sum(Volume), 60)), 10), cross_mean(day_sum(Amt), 30))',
 f'cross_corr(div({U}, cross_mean(day_sum(Volume), 60)), day_sum(Ret), 60)',
 f'cross_regbeta(day_sum(Ret), cross_zscore(log({U}), 60), 60)',
 f'cross_ema(sub(cross_zscore(log({U}), 60), cross_zscore(log({L}), 60)), 10)',
 f'cs_bucket_demean(cross_mean(div(sub({U}, {L}), day_sum(Volume)), 30), LogFloatCap)',
 f'cross_mean(mul(div({U}, cross_mean(day_sum(Volume), 60)), sign(day_sum(Ret))), 20)',
 f'ts_decay_linear(div(sub({U}, {L}), cross_mean(day_sum(Volume), 120)), 20)',
 f'cross_regres(cross_zscore(log(day_sum(Volume)), 60), cross_zscore(log({U}), 60), 60)',
 f'cross_tail_mean_q75(div({U}, cross_mean(day_sum(Volume), 60)), 30)',
]
HV='in_topk_masked(Volume, Ret, 5)'
LV='in_topk_masked(Volume, Ret, 5, False)'
H=f'day_sum({HV})'; Lw=f'day_sum({LV})'
N_SEEDS=[
 f'cross_mean({H}, 20)',
 f'cross_mean(sub({H}, {Lw}), 20)',
 f'cross_mean(div(sub({H}, {Lw}), day_std(Ret)), 20)',
 f'cross_mean(div({H}, day_std(Ret)), 20)',
 f'cross_zscore(sub({H}, {Lw}), 60)',
 f'cs_bucket_zscore(cross_mean(sub({H}, {Lw}), 20), LogFloatCap)',
 f'cross_corr({H}, {Lw}, 60)',
 f'cross_regres(day_sum(Ret), {H}, 60)',
 f'cross_mean(div({H}, cross_mean(abs_(day_sum(Ret)), 60)), 20)',
 f'cross_mean(sub(day_sum(in_topk_masked(Volume, Ret, 2)), {H}), 40)',
 f'cross_ema(sign(sub({H}, {Lw})), 20)',
 f'cross_regbeta({Lw}, {H}, 60)',
 f'cs_regres(cross_mean({H}, 30), cross_mean(day_std(Ret), 30))',
 f'cross_stddev(sub({H}, {Lw}), 40)',
 f'cross_mean(sub(day_sum(in_topk_masked(Volume, Ret, 10)), day_sum(in_topk_masked(Volume, Ret, 10, False))), 30)',
 f'sub(cross_mean({H}, 20), cross_mean({Lw}, 60))',
]
