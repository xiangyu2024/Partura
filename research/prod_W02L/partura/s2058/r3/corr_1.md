# 相关度表:种子 2058,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.42 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(` | 0.59 | 0.23 | 0.00 | 0.01 | 0.24 | 0.06 | `cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap)` |
| slot a seed 1 | 过 | 0.43 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(` | 0.58 | 0.21 | 0.02 | 0.01 | 0.22 | 0.05 | `cross_ema(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), 20)` |
| slot a seed 2 | 过 | 0.33 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(` | 0.31 | 0.16 | 0.04 | 0.02 | 0.14 | 0.00 | `sub(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), cs_bucket_zscore(day_quantile(cross_corr(Open, Amt, 241)), LogFloatCap))` |
| slot a seed 3 | 过 | 0.17 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.10 | 0.16 | 0.09 | 0.01 | 0.17 | 0.09 | `sub(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), cross_ema(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), 120))` |
| slot a seed 4 | 过 | 0.22 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.23 | 0.16 | 0.14 | 0.05 | 0.17 | 0.00 | `sub(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 60)), LogFloatCap))` |
| slot a seed 5 | 过 | 0.47 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(` | 0.59 | 0.10 | 0.04 | 0.01 | 0.11 | 0.08 | `cs_regres(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), day_quantile(cross_reg_tvalue(Open, Amt, 241)))` |
| slot a seed 6 | 过 | 0.41 | `day_std(pow_2(Volume))` | 0.58 | 0.25 | 0.10 | 0.06 | 0.27 | 0.04 | `cs_regres(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), cs_rank(day_std(pow_2(Ret))))` |
| slot a seed 7 | 过 | 0.44 | `day_std(pow_2(Volume))` | 0.57 | 0.20 | 0.01 | 0.02 | 0.23 | 0.09 | `add(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), cs_bucket_zscore(day_quantile(cross_regbeta(Open, Volume, 241)), LogFloatCap))` |
| slot a seed 8 | 过 | 0.10 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.07 | 0.08 | 0.07 | 0.05 | 0.09 | 0.03 | `cross_zscore(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), 60)` |
| slot a seed 9 | 过 | 0.48 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(` | 0.58 | 0.11 | 0.01 | 0.01 | 0.12 | 0.00 | `mul(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), cs_rank(day_quantile(cross_corr(Open, Amt, 241))))` |
| slot a seed 10 | 过 | 0.46 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(` | 0.57 | 0.06 | 0.04 | 0.01 | 0.07 | 0.10 | `cs_regres(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), day_quantile(cross_corr(Open, Amt, 241)))` |
| slot a seed 11 | 过 | 0.42 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(` | 0.58 | 0.23 | 0.00 | 0.01 | 0.24 | 0.06 | `cross_mean(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), 10)` |
| slot a seed 12 | 过 | 0.17 | `day_std(pow_2(Volume))` | 0.22 | 0.13 | 0.05 | 0.00 | 0.14 | 0.09 | `sub(cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), cs_bucket_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), LogTotalCap))` |
| slot b seed 1 | 废品 | 0.12 | `day_sum(sigmoid(Vwap))` | 0.22 | 0.04 | 0.04 | 0.02 | 0.03 | 0.00 | `sub(LogFloatShares, ts_delay(LogFloatShares, 60))` |
| slot b seed 2 | 废品 | 0.20 | `day_sum(sigmoid(Vwap))` | 0.28 | 0.02 | 0.05 | 0.03 | 0.00 | 0.05 | `sub(LogFloatShares, ts_delay(LogFloatShares, 120))` |
| slot b seed 3 | 废品 | 0.06 | `day_sum(sigmoid(Vwap))` | 0.18 | 0.04 | 0.03 | 0.02 | 0.04 | 0.03 | `sub(LogFloatShares, ts_delay(LogFloatShares, 20))` |
| slot b seed 4 | 过 | 0.17 | `mul(ts_max(cs_stddev_full(day_product(cross_product(sigmoid(` | 0.22 | 0.23 | 0.01 | 0.00 | 0.21 | 0.29 | `cs_regres(sub(LogFloatShares, ts_delay(LogFloatShares, 60)), LogFloatCap)` |
| slot b seed 5 | 过 | 0.23 | `day_std(pow_2(Volume))` | 0.27 | 0.00 | 0.05 | 0.03 | 0.02 | 0.04 | `cross_ema(sub(LogFloatShares, ts_delay(LogFloatShares, 20)), 40)` |
| slot b seed 6 | 废品 | 0.08 | `day_std(pow_2(Volume))` | 0.13 | 0.02 | 0.01 | 0.00 | 0.01 | 0.00 | `cross_zscore(sub(LogFloatShares, ts_delay(LogFloatShares, 20)), 120)` |
| slot b seed 7 | 过 | 0.34 | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_co` | 0.36 | 0.01 | 0.04 | 0.02 | 0.03 | 0.00 | `cs_bucket_rank(sub(LogFloatShares, ts_delay(LogFloatShares, 60)), LogFloatCap)` |
| slot b seed 8 | 废品 | 0.16 | `day_std(pow_2(Volume))` | 0.22 | 0.03 | 0.04 | 0.03 | 0.01 | 0.01 | `cross_max(sub(LogFloatShares, ts_delay(LogFloatShares, 1)), 120)` |
| slot b seed 9 | 废品 | 0.20 | `day_sum(sigmoid(Vwap))` | 0.28 | 0.00 | 0.07 | 0.02 | 0.01 | 0.08 | `cross_mean(is_gt(sub(LogFloatShares, ts_delay(LogFloatShares, 1)), 0.01), 120)` |
| slot b seed 10 | 过 | 0.32 | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(` | 0.28 | 0.03 | 0.01 | 0.02 | 0.03 | 0.23 | `cs_regres(sub(LogTotalCap, LogFloatCap), ListAge)` |
| slot b seed 11 | 过 | 0.33 | `cross_mean(day_std(pow_2(Ret)), 20)` | 0.17 | 0.21 | 0.36 | 0.42 | 0.24 | 0.07 | `sub(sub(LogFloatShares, ts_delay(LogFloatShares, 60)), sub(LogTotalCap, ts_delay(LogTotalCap, 60)))` |
| R 1 variant 1 | 过 | 0.85 | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(` | 0.79 | 0.61 | 0.07 | 0.06 | 0.59 | 0.31 | `ts_std(day_product(pow_2(cross_product(sigmoid(Amt), 10))), 150)` |
| R 1 variant 2 | 过 | 0.93 | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(` | 0.90 | 0.56 | 0.06 | 0.06 | 0.54 | 0.25 | `ts_std(day_product(pow_2(cross_product(sigmoid(Amt), 10))), 200)` |
| R 1 variant 3 | 过 | 0.97 | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(` | 0.97 | 0.52 | 0.05 | 0.07 | 0.49 | 0.20 | `ts_std(day_product(pow_2(cross_product(sigmoid(Amt), 10))), 250)` |
| R 1 variant 4 | 过 | 0.85 | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(` | 0.79 | 0.61 | 0.07 | 0.06 | 0.59 | 0.31 | `ts_std(day_product(pow_2(cross_product(sigmoid(Volume), 10))), 150)` |
| R 1 variant 5 | 过 | 0.75 | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(` | 0.65 | 0.43 | 0.04 | 0.07 | 0.40 | 0.16 | `cross_ema(ts_std(day_product(pow_2(cross_product(sigmoid(Amt), 10))), 100), 20)` |
| R 1 variant 6 | 过 | 0.84 | `cross_fangzheng(cross_max(day_product(cross_product(sigmoid(` | 0.77 | 0.61 | 0.07 | 0.06 | 0.58 | 0.30 | `ts_std(day_product(cross_product(sigmoid(Amt), 10)), 150)` |
