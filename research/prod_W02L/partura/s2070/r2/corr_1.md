# 相关度表:种子 2070,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.07 | `day_quantile_q75(mul(High, Ret))` | 0.05 | 0.02 | 0.02 | 0.04 | 0.01 | 0.01 | `ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20)` |
| slot a seed 1 | 过 | 0.05 | `day_quantile_q75(mul(High, Ret))` | 0.11 | 0.02 | 0.01 | 0.03 | 0.01 | 0.01 | `div(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), ts_std(day_last(Vwap), 20))` |
| slot a seed 2 | 过 | 0.05 | `day_quantile_q75(mul(High, Ret))` | 0.11 | 0.02 | 0.03 | 0.04 | 0.01 | 0.02 | `div(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), day_last(Vwap))` |
| slot a seed 3 | 过 | 0.13 | `day_quantile_q75(mul(High, Ret))` | 0.07 | 0.13 | 0.07 | 0.07 | 0.14 | 0.12 | `ts_decay_linear(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 10)` |
| slot a seed 4 | 废品 | 0.04 | `cross_mean(day_cov(signed_pow(div(in_stddev_rolling_multi([i` | 0.05 | 0.11 | 0.04 | 0.03 | 0.10 | 0.05 | `ts_rank(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 60)` |
| slot a seed 5 | 过 | 0.05 | `day_quantile_q75(mul(High, Ret))` | 0.09 | 0.08 | 0.01 | 0.05 | 0.07 | 0.04 | `sub(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), ts_mean(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 60))` |
| slot a seed 6 | 过 | 0.06 | `day_quantile_q75(mul(High, Ret))` | 0.04 | 0.01 | 0.02 | 0.01 | 0.01 | 0.02 | `sub(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), ts_delay(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 5))` |
| slot a seed 7 | 过 | 0.10 | `day_quantile_q75(mul(High, Ret))` | 0.05 | 0.06 | 0.06 | 0.07 | 0.07 | 0.06 | `div(ts_mean(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 5), ts_std(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 40))` |
| slot a seed 8 | 过 | 0.24 | `day_quantile_q75(mul(High, Ret))` | 0.21 | 0.46 | 0.14 | 0.16 | 0.45 | 0.39 | `ts_corr(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), day_sum(Amt), 20)` |
| slot a seed 9 | 过 | 0.07 | `day_quantile_q75(mul(High, Ret))` | 0.05 | 0.02 | 0.02 | 0.03 | 0.01 | 0.01 | `mul(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), ts_mean(day_zero_ratio(Volume), 20))` |
| slot a seed 10 | 过 | 0.15 | `day_quantile_q75(mul(High, Ret))` | 0.06 | 0.26 | 0.09 | 0.02 | 0.26 | 0.16 | `ts_skew(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 30)` |
| slot a seed 11 | 过 | 0.10 | `day_quantile_q75(mul(High, Ret))` | 0.06 | 0.09 | 0.08 | 0.09 | 0.10 | 0.09 | `cross_mean(div(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), ts_std(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 20)), 10)` |
| slot a seed 12 | 过 | 0.10 | `day_quantile_q75(mul(High, Ret))` | 0.22 | 0.10 | 0.04 | 0.36 | 0.09 | 0.06 | `ts_regres(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), day_std(Ret), 40)` |
| slot a seed 13 | 过 | 0.06 | `day_quantile_q75(mul(High, Ret))` | 0.06 | 0.03 | 0.01 | 0.03 | 0.02 | 0.01 | `div(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), ts_mean(day_sum(Amt), 20))` |
| slot a seed 14 | 过 | 0.39 | `day_quantile_q75(mul(High, Ret))` | 0.41 | 0.80 | 0.05 | 0.04 | 0.76 | 0.67 | `ts_min(ts_regres(day_last(Vwap), day_zero_ratio(Volume), 20), 20)` |
| slot b seed 1 | 过 | 0.03 | `cross_mean(day_cov(signed_pow(div(in_stddev_rolling_multi([i` | 0.14 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | `day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236))` |
| slot b seed 2 | 过 | 0.15 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.18 | 0.05 | 0.03 | 0.01 | 0.04 | 0.08 | `ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236)), 20)` |
| slot b seed 3 | 过 | 0.14 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.17 | 0.09 | 0.02 | 0.00 | 0.08 | 0.11 | `ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Amt, 1, 236)), 40)` |
| slot b seed 4 | 过 | 0.18 | `day_quantile_q75(mul(High, Ret))` | 0.23 | 0.11 | 0.16 | 0.41 | 0.13 | 0.04 | `ts_decay_linear(day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237)), 10)` |
| slot b seed 5 | 过 | 0.20 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.13 | 0.22 | 0.28 | 0.50 | 0.24 | 0.07 | `sub(ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236)), 20), ts_mean(day_corr(in_slice(Ret, 1, 236), in_slice(Volume, 2, 237)), 20))` |
| slot b seed 6 | 过 | 0.59 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.62 | 0.40 | 0.12 | 0.03 | 0.37 | 0.03 | `ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Ret, 1, 236)), 20)` |
| slot b seed 7 | 过 | 0.58 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.61 | 0.39 | 0.09 | 0.02 | 0.35 | 0.03 | `ts_mean(day_autocorr(Ret, 1), 20)` |
| slot b seed 8 | 过 | 0.20 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.17 | 0.19 | 0.17 | 0.09 | 0.20 | 0.09 | `ts_mean(day_cov(in_slice(Ret, 2, 237), in_slice(Amt, 1, 236)), 20)` |
| slot b seed 9 | 过 | 0.12 | `cross_mean(day_cov(signed_pow(div(in_stddev_rolling_multi([i` | 0.14 | 0.05 | 0.02 | 0.01 | 0.04 | 0.06 | `div(ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236)), 20), ts_std(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 1, 236)), 60))` |
| slot b seed 10 | 过 | 0.08 | `cross_mean(day_cov(signed_pow(div(in_stddev_rolling_multi([i` | 0.08 | 0.04 | 0.01 | 0.04 | 0.05 | 0.04 | `ts_mean(day_corr(in_slice(Ret, 2, 237), in_slice(Volume, 0, 235)), 20)` |
| slot b seed 11 | 过 | 0.13 | `cross_mean(day_cov(signed_pow(div(in_stddev_rolling_multi([i` | 0.16 | 0.12 | 0.10 | 0.11 | 0.13 | 0.00 | `ts_decay_linear(day_corr(in_slice(Vwap, 2, 237), in_slice(Volume, 1, 236)), 10)` |
| slot b seed 12 | 过 | 0.05 | `add(cross_mean(day_cov(signed_pow(div(in_stddev_rolling_mult` | 0.02 | 0.05 | 0.05 | 0.01 | 0.05 | 0.02 | `ts_mean(day_corr(in_slice(Ret, 5, 237), in_slice(Amt, 0, 232)), 20)` |
