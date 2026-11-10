# 相关度表:种子 2051,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.16 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))` | 0.21 | 0.23 | 0.02 | 0.02 | 0.20 | 0.12 | `day_kurt(Volume)` |
| slot a seed 1 | 过 | 0.16 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` | 0.21 | 0.49 | 0.05 | 0.09 | 0.40 | 0.32 | `cross_mean(day_kurt(Volume), 60)` |
| slot a seed 2 | 过 | 0.17 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` | 0.21 | 0.51 | 0.07 | 0.09 | 0.42 | 0.34 | `cross_ema(day_kurt(Volume), 40)` |
| slot a seed 3 | 过 | 0.17 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` | 0.20 | 0.48 | 0.08 | 0.08 | 0.40 | 0.34 | `cross_mean(day_kurt(Volume), 120)` |
| slot a seed 4 | 过 | 0.12 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))` | 0.05 | 0.04 | 0.06 | 0.01 | 0.04 | 0.01 | `cross_zscore(day_kurt(Volume), 60)` |
| slot a seed 5 | 过 | 0.06 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))` | 0.05 | 0.14 | 0.10 | 0.05 | 0.10 | 0.01 | `cross_ema(cross_zscore(day_kurt(Volume), 60), 20)` |
| slot a seed 6 | 过 | 0.10 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.13 | 0.08 | 0.09 | 0.01 | 0.10 | 0.03 | `cross_corr(day_kurt(Volume), day_sum(Ret), 60)` |
| slot a seed 7 | 过 | 0.15 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.15 | 0.07 | 0.06 | 0.00 | 0.10 | 0.05 | `cross_corr(day_kurt(Volume), day_sum(Ret), 241)` |
| slot a seed 8 | 过 | 0.10 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.15 | 0.01 | 0.03 | 0.00 | 0.02 | 0.04 | `cross_regbeta(day_sum(Ret), day_kurt(Volume), 60)` |
| slot a seed 9 | 过 | 0.14 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` | 0.21 | 0.27 | 0.02 | 0.10 | 0.19 | 0.01 | `cs_bucket_demean(cross_mean(day_kurt(Volume), 60), LogFloatCap)` |
| slot a seed 10 | 过 | 0.06 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))` | 0.04 | 0.15 | 0.10 | 0.05 | 0.12 | 0.02 | `cs_bucket_demean(cross_ema(cross_zscore(day_kurt(Volume), 60), 20), LogFloatCap)` |
| slot a seed 11 | 过 | 0.11 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` | 0.18 | 0.31 | 0.01 | 0.06 | 0.25 | 0.19 | `cross_stddev(day_kurt(Volume), 60)` |
| slot a seed 12 | 过 | 0.14 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` | 0.20 | 0.42 | 0.04 | 0.08 | 0.34 | 0.27 | `cross_tail_mean_q75(day_kurt(Volume), 60)` |
| slot a seed 13 | 过 | 0.04 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))` | 0.06 | 0.11 | 0.07 | 0.07 | 0.08 | 0.00 | `sub(cross_mean(day_kurt(Volume), 20), cross_mean(day_kurt(Volume), 120))` |
| slot a seed 14 | 过 | 0.13 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.12 | 0.14 | 0.08 | 0.01 | 0.16 | 0.10 | `cross_corr(day_kurt(Volume), day_kurt(in_delta(Vwap, 1)), 120)` |
| slot b seed 1 | 废品 | 0.04 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.04 | 0.02 | 0.11 | 0.41 | 0.01 | 0.05 | `cross_argmax(day_sum(Amt), 30)` |
| slot b seed 2 | 废品 | 0.03 | `day_skew(nt_ts_kurt(Low, 10))` | 0.04 | 0.10 | 0.18 | 0.25 | 0.13 | 0.06 | `cross_argmax(day_sum(Volume), 60)` |
| slot b seed 3 | 废品 | 0.04 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.02 | 0.05 | 0.03 | 0.33 | 0.05 | 0.02 | `cross_argmax(day_sum(Ret), 30)` |
| slot b seed 4 | 过 | 0.10 | `day_skew(nt_ts_kurt(Low, 10))` | 0.08 | 0.31 | 0.46 | 0.20 | 0.32 | 0.05 | `cross_mean(mul(day_sum(Ret), cross_zscore(day_sum(Amt), 20)), 60)` |
| slot b seed 5 | 过 | 0.09 | `day_skew(nt_ts_kurt(Low, 10))` | 0.07 | 0.25 | 0.38 | 0.11 | 0.26 | 0.10 | `cross_mean(mul(day_sum(Ret), cross_zscore(day_sum(Volume), 20)), 120)` |
| slot b seed 6 | 过 | 0.04 | `day_skew(nt_ts_kurt(Low, 10))` | 0.03 | 0.11 | 0.14 | 0.15 | 0.10 | 0.02 | `cross_corr(day_sum(Ret), day_sum(Amt), 60)` |
| slot b seed 7 | 过 | 0.04 | `day_skew(nt_ts_kurt(Low, 10))` | 0.02 | 0.11 | 0.14 | 0.10 | 0.10 | 0.01 | `cross_corr(day_sum(Ret), day_sum(Volume), 120)` |
| slot b seed 8 | 过 | 0.02 | `day_max(nt_ts_kurt(Vwap, 10))` | 0.05 | 0.01 | 0.01 | 0.22 | 0.01 | 0.03 | `cross_regbeta(day_sum(Ret), cross_zscore(day_sum(Amt), 20), 60)` |
| slot b seed 9 | 过 | 0.05 | `day_skew(nt_ts_kurt(Low, 10))` | 0.03 | 0.19 | 0.24 | 0.20 | 0.19 | 0.05 | `cross_corr(day_sum(Ret), sub(log(day_sum(Volume)), LogFloatShares), 60)` |
| slot b seed 10 | 过 | 0.10 | `day_max(nt_ts_kurt(Vwap, 30))` | 0.04 | 0.04 | 0.17 | 0.45 | 0.07 | 0.04 | `cross_zscore(sub(log(day_sum(Volume)), LogFloatShares), 60)` |
| slot b seed 11 | 过 | 0.10 | `day_skew(nt_ts_kurt(Low, 10))` | 0.08 | 0.37 | 0.44 | 0.20 | 0.37 | 0.02 | `cs_bucket_demean(cross_mean(mul(day_sum(Ret), cross_zscore(day_sum(Amt), 20)), 60), LogFloatCap)` |
| slot b seed 12 | 过 | 0.09 | `day_skew(nt_ts_kurt(Low, 10))` | 0.07 | 0.22 | 0.29 | 0.23 | 0.22 | 0.04 | `cross_ema(mul(sign(day_sum(Ret)), cross_zscore(day_sum(Amt), 30)), 40)` |
| slot b seed 13 | 废品 | 0.02 | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` | 0.02 | 0.05 | 0.11 | 0.11 | 0.06 | 0.02 | `sub(cross_argmax(day_sum(Amt), 30), cross_argmax(day_sum(Ret), 30))` |
| slot b seed 14 | 过 | 0.05 | `day_skew(nt_ts_kurt(Low, 10))` | 0.04 | 0.15 | 0.20 | 0.08 | 0.15 | 0.06 | `cross_corr(cross_zscore(day_sum(Amt), 20), day_sum(Ret), 241)` |
