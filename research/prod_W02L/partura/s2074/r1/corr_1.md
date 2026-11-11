# 相关度表:种子 2074,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `pow_2(day_close(neg(Volume)))` | 1.00 | 0.56 | 0.19 | 0.18 | 0.60 | 0.46 | `day_close(neg(Volume))` |
| slot a seed 1 | 过 | 0.47 | `pow_2(day_close(neg(Volume)))` | 0.08 | 0.12 | 0.22 | 0.33 | 0.15 | 0.08 | `cross_zscore(day_close(neg(Volume)), 120)` |
| slot a seed 2 | 过 | 0.29 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.34 | 0.35 | 0.15 | 0.01 | 0.32 | 0.40 | `cross_mean(div(day_close(neg(Volume)), day_sum(Volume)), 60)` |
| slot a seed 3 | 过 | 0.23 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.37 | 0.10 | 0.17 | 0.03 | 0.07 | 0.02 | `cs_bucket_zscore(cross_mean(div(day_close(neg(Volume)), day_sum(Volume)), 20), LogFloatCap)` |
| slot a seed 4 | 过 | 0.31 | `pow_2(day_close(neg(Volume)))` | 0.09 | 0.25 | 0.36 | 0.38 | 0.28 | 0.12 | `div(cross_mean(day_close(neg(Volume)), 10), cross_mean(day_close(neg(Volume)), 120))` |
| slot a seed 5 | 过 | 0.05 | `pow_2(day_close(neg(Volume)))` | 0.08 | 0.12 | 0.14 | 0.06 | 0.14 | 0.09 | `cross_corr(day_close(neg(Volume)), day_sum(Ret), 60)` |
| slot a seed 6 | 过 | 0.04 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.04 | 0.03 | 0.13 | 0.03 | 0.04 | 0.04 | `cross_corr(day_close(neg(Volume)), abs_(day_sum(Ret)), 60)` |
| slot a seed 7 | 过 | 0.17 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.20 | 0.25 | 0.17 | 0.00 | 0.25 | 0.28 | `cross_regbeta(day_sum(Volume), day_close(neg(Volume)), 60)` |
| slot a seed 8 | 过 | 0.12 | `pow_2(day_close(neg(Volume)))` | 0.50 | 0.09 | 0.03 | 0.08 | 0.09 | 0.11 | `cross_regres(day_sum(Volume), day_close(neg(Volume)), 60)` |
| slot a seed 9 | 过 | 0.19 | `pow_2(day_close(neg(Volume)))` | 0.20 | 0.20 | 0.15 | 0.08 | 0.21 | 0.11 | `cross_corr(day_close(neg(Volume)), day_std(Ret), 60)` |
| slot a seed 10 | 过 | 0.08 | `pow_2(day_close(neg(Volume)))` | 0.07 | 0.01 | 0.01 | 0.03 | 0.01 | 0.04 | `mul(cross_zscore(day_close(neg(Volume)), 120), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 11 | 过 | 0.20 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.38 | 0.18 | 0.08 | 0.07 | 0.15 | 0.22 | `cs_regres(cross_mean(day_close(neg(Volume)), 20), cross_mean(neg(day_sum(Volume)), 20))` |
| slot a seed 12 | 过 | 0.28 | `pow_2(day_close(neg(Volume)))` | 0.07 | 0.22 | 0.36 | 0.34 | 0.26 | 0.09 | `cross_ema(div(day_close(neg(Volume)), cross_mean(day_close(neg(Volume)), 60)), 10)` |
| slot a seed 13 | 过 | 0.47 | `pow_2(day_close(neg(Volume)))` | 0.10 | 0.12 | 0.22 | 0.32 | 0.15 | 0.08 | `cs_bucket_zscore(cross_zscore(day_close(neg(Volume)), 120), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 1 | 过 | 0.69 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.62 | 0.50 | 0.14 | 0.04 | 0.45 | 0.14 | `cross_mean(div(day_var(in_logchg(Close, 5)), mul(5, day_var(in_logchg(Close, 1)))), 20)` |
| slot b seed 2 | 过 | 0.69 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.64 | 0.48 | 0.05 | 0.06 | 0.43 | 0.15 | `cross_mean(div(day_var(in_logchg(Close, 5)), mul(5, day_var(in_logchg(Close, 1)))), 60)` |
| slot b seed 3 | 过 | 0.61 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.60 | 0.66 | 0.01 | 0.05 | 0.60 | 0.38 | `cross_mean(div(day_var(in_logchg(Vwap, 5)), mul(5, day_var(in_logchg(Vwap, 1)))), 60)` |
| slot b seed 4 | 过 | 0.70 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.64 | 0.52 | 0.05 | 0.05 | 0.46 | 0.23 | `cross_mean(div(day_var(in_logchg(Close, 15)), mul(15, day_var(in_logchg(Close, 1)))), 60)` |
| slot b seed 5 | 过 | 0.64 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.54 | 0.49 | 0.01 | 0.04 | 0.43 | 0.30 | `cross_mean(div(day_var(in_logchg(Close, 30)), mul(30, day_var(in_logchg(Close, 3)))), 60)` |
| slot b seed 6 | 过 | 0.14 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.10 | 0.09 | 0.11 | 0.18 | 0.10 | 0.01 | `cross_zscore(log(div(day_var(in_logchg(Close, 5)), mul(5, day_var(in_logchg(Close, 1))))), 120)` |
| slot b seed 7 | 过 | 0.64 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.61 | 0.41 | 0.08 | 0.06 | 0.36 | 0.04 | `cs_bucket_zscore(cross_mean(div(day_var(in_logchg(Close, 5)), mul(5, day_var(in_logchg(Close, 1)))), 60), LogFloatCap)` |
| slot b seed 8 | 过 | 0.49 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.44 | 0.62 | 0.07 | 0.06 | 0.59 | 0.46 | `cs_bucket_zscore(cross_mean(div(day_var(in_logchg(Vwap, 15)), mul(15, day_var(in_logchg(Vwap, 1)))), 60), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 9 | 过 | 0.34 | `ts_sum(day_ar1_coefficient(neg(Vwap)), 10)` | 0.20 | 0.54 | 0.11 | 0.01 | 0.51 | 0.51 | `cs_regres(cross_mean(div(day_var(in_logchg(Close, 5)), mul(5, day_var(in_logchg(Close, 1)))), 60), cross_mean(day_ar1_coefficient(Ret), 60))` |
| slot b seed 10 | 过 | 0.53 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.45 | 0.30 | 0.02 | 0.06 | 0.26 | 0.02 | `cross_mean(log(div(mul(day_var(in_logchg(Close, 1)), 240), pow_2(day_sum(in_logchg(Close, 1))))), 60)` |
| slot b seed 11 | 过 | 0.66 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.51 | 0.59 | 0.07 | 0.07 | 0.53 | 0.25 | `cross_mean(div(day_wstd(in_logchg(Close, 5), Volume), mul(2.2, day_wstd(in_logchg(Close, 1), Volume))), 60)` |
| slot b seed 12 | 过 | 0.20 | `day_quantile_q25(in_rank(pow_2_5(neg(Ret))))` | 0.10 | 0.25 | 0.32 | 0.23 | 0.27 | 0.04 | `sub(cross_mean(div(day_var(in_logchg(Close, 5)), mul(5, day_var(in_logchg(Close, 1)))), 20), cross_mean(div(day_var(in_logchg(Close, 5)), mul(5, day_var(in_logchg(Close, 1)))), 120))` |
