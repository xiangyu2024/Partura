# 相关度表:种子 2063,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.21 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.12 | 0.14 | 0.17 | 0.11 | 0.15 | 0.06 | `cross_corr(day_var(Ret), day_sum(Ret), 60)` |
| slot a seed 1 | 过 | 0.23 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.14 | 0.15 | 0.16 | 0.01 | 0.15 | 0.08 | `cross_ema(cross_corr(day_var(Ret), day_sum(Ret), 60), 20)` |
| slot a seed 2 | 过 | 0.23 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.14 | 0.15 | 0.17 | 0.05 | 0.15 | 0.06 | `cross_mean(cross_corr(day_var(Ret), day_sum(Ret), 60), 20)` |
| slot a seed 3 | 过 | 0.08 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.05 | 0.06 | 0.09 | 0.13 | 0.07 | 0.02 | `cross_zscore(cross_corr(day_var(Ret), day_sum(Ret), 60), 120)` |
| slot a seed 4 | 过 | 0.13 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.08 | 0.10 | 0.11 | 0.10 | 0.11 | 0.04 | `sub(cross_corr(day_var(Ret), day_sum(Ret), 60), cross_corr(day_var(Ret), day_sum(Ret), 250))` |
| slot a seed 5 | 过 | 0.20 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.10 | 0.15 | 0.16 | 0.11 | 0.15 | 0.01 | `cs_bucket_demean(cross_corr(day_var(Ret), day_sum(Ret), 60), ListAge)` |
| slot a seed 6 | 过 | 0.22 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.12 | 0.16 | 0.14 | 0.02 | 0.16 | 0.03 | `cs_bucket_demean(cross_ema(cross_corr(day_var(Ret), day_sum(Ret), 60), 20), BoardCode)` |
| slot a seed 7 | 过 | 0.06 | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60` | 0.08 | 0.04 | 0.43 | 0.01 | 0.06 | 0.01 | `cs_first_low20(cross_corr(day_var(Ret), day_sum(Ret), 60), cross_mean(day_std(Ret), 20))` |
| slot a seed 8 | 过 | 0.07 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.03 | 0.06 | 0.07 | 0.01 | 0.06 | 0.01 | `cs_flip_by_state(cross_corr(day_var(Ret), day_sum(Ret), 60), day_sum(Ret))` |
| slot a seed 9 | 过 | 0.21 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.12 | 0.13 | 0.17 | 0.09 | 0.14 | 0.08 | `add(cross_corr(day_var(Ret), day_sum(Ret), 60), cross_corr(day_var(Ret), day_sum(Ret), 120))` |
| slot a seed 10 | 过 | 0.09 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.07 | 0.09 | 0.03 | 0.03 | 0.09 | 0.03 | `sub(cross_corr(day_var(Ret), day_sum(Ret), 60), cross_corr(day_var(Ret), day_sum(Volume), 60))` |
| slot a seed 11 | 废品 | 0.07 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.06 | 0.06 | 0.09 | 0.12 | 0.06 | 0.02 | `ts_rank(cross_corr(day_var(Ret), day_sum(Ret), 60), 120)` |
| slot a seed 12 | 过 | 0.15 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.10 | 0.10 | 0.13 | 0.06 | 0.11 | 0.03 | `cross_mean(sub(cross_corr(day_var(Ret), day_sum(Ret), 60), cross_mean(cross_corr(day_var(Ret), day_sum(Ret), 60), 250)), 20)` |
| slot b seed 1 | 过 | 0.31 | `day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(High), ` | 0.22 | 0.16 | 0.11 | 0.07 | 0.12 | 0.31 | `cross_mean(day_es_ratio_hi(Ret), 20)` |
| slot b seed 2 | 过 | 0.29 | `day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(High), ` | 0.20 | 0.18 | 0.12 | 0.02 | 0.16 | 0.28 | `cross_mean(day_es_ratio_lo(Ret), 20)` |
| slot b seed 3 | 过 | 0.14 | `day_sum(pow_05(in_rank(pow_2_5(inv(Ret)))))` | 0.19 | 0.02 | 0.02 | 0.06 | 0.00 | 0.11 | `cross_mean(sub(day_es_ratio_hi(Ret), day_es_ratio_lo(Ret)), 20)` |
| slot b seed 4 | 过 | 0.44 | `day_sum(pow_05(in_rank(pow_2_5(inv(Ret)))))` | 0.11 | 0.54 | 0.06 | 0.13 | 0.45 | 0.39 | `cross_mean(day_es_ratio_hi(Volume), 20)` |
| slot b seed 5 | 过 | 0.47 | `day_sum(pow_05(in_rank(pow_2_5(inv(Ret)))))` | 0.16 | 0.52 | 0.13 | 0.09 | 0.42 | 0.43 | `cross_mean(day_es_ratio_hi(Amt), 60)` |
| slot b seed 6 | 过 | 0.06 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.03 | 0.01 | 0.00 | 0.01 | 0.01 | 0.01 | `cross_zscore(day_es_ratio_hi(abs_(Ret)), 120)` |
| slot b seed 7 | 过 | 0.05 | `pow_05(day_var(nt_ts_min(Volume, 30)))` | 0.09 | 0.05 | 0.01 | 0.07 | 0.06 | 0.02 | `sub(cross_mean(day_es_ratio_hi(Ret), 20), cross_mean(day_es_ratio_hi(Ret), 120))` |
| slot b seed 8 | 过 | 0.34 | `day_sum(pow_05(in_rank(pow_2_5(inv(Ret)))))` | 0.10 | 0.25 | 0.02 | 0.15 | 0.17 | 0.06 | `cs_bucket_demean(cross_mean(day_es_ratio_hi(Volume), 20), LogFloatCap)` |
| slot b seed 9 | 过 | 0.14 | `day_sum(pow_05(in_rank(pow_2_5(inv(Ret)))))` | 0.13 | 0.09 | 0.04 | 0.03 | 0.06 | 0.15 | `cross_corr(day_es_ratio_hi(Ret), day_sum(Ret), 60)` |
| slot b seed 10 | 过 | 0.38 | `day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(High), ` | 0.26 | 0.20 | 0.12 | 0.04 | 0.16 | 0.37 | `cross_ema(day_es_ratio_hi(Ret), 20)` |
| slot b seed 11 | 过 | 0.27 | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov` | 0.11 | 0.34 | 0.09 | 0.08 | 0.28 | 0.14 | `cross_mean(sub(day_es_ratio_hi(Volume), day_es_ratio_lo(Ret)), 20)` |
| slot b seed 12 | 过 | 0.21 | `day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(High), ` | 0.16 | 0.17 | 0.04 | 0.03 | 0.13 | 0.39 | `cs_bucket_zscore(cross_mean(day_es_ratio_hi(Ret), 60), sub(LogFloatCap, LogFloatShares))` |
