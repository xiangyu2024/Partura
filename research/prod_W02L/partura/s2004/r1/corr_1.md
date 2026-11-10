# 相关度表:种子 2004,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.12 | `day_cov(Volume, Volume)` | 0.06 | 0.03 | 0.03 | 0.14 | 0.03 | 0.02 | `day_cov(Ret, Volume)` |
| slot a seed 1 | 过 | 0.28 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.25 | 0.10 | 0.25 | 0.41 | 0.14 | 0.01 | `cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30)` |
| slot a seed 2 | 过 | 0.40 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.40 | 0.21 | 0.46 | 0.27 | 0.27 | 0.08 | `cross_mean(div(day_cov(Ret, Volume), day_mean(Volume)), 40)` |
| slot a seed 3 | 过 | 0.23 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.26 | 0.16 | 0.13 | 0.02 | 0.17 | 0.06 | `cross_corr(ts_delay(day_cov(Ret, Volume), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 4 | 过 | 0.13 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.16 | 0.12 | 0.08 | 0.00 | 0.11 | 0.10 | `cross_corr(day_cov(Ret, Volume), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 5 | 过 | 0.12 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.13 | 0.07 | 0.01 | 0.03 | 0.06 | 0.01 | `cross_corr(day_cov(Ret, Volume), ts_delay(day_sum(Ret), 1), 60)` |
| slot a seed 6 | 过 | 0.53 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.57 | 0.03 | 0.00 | 0.11 | 0.03 | 0.00 | `cross_corr(day_cov(Ret, Volume), day_sum(Amt), 60)` |
| slot a seed 7 | 过 | 0.60 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.64 | 0.02 | 0.03 | 0.08 | 0.01 | 0.08 | `cross_corr(day_cov(Ret, Volume), day_std(Ret), 60)` |
| slot a seed 8 | 过 | 0.27 | `day_cov(Volume, Volume)` | 0.13 | 0.27 | 0.36 | 0.23 | 0.30 | 0.10 | `cross_mean(cs_bucket_demean(div(day_cov(Ret, Volume), mul(day_std(Ret), day_std(Volume))), sub(LogFloatCap, LogFloatShares)), 60)` |
| slot a seed 9 | 过 | 0.42 | `day_cov(Volume, Volume)` | 0.44 | 0.16 | 0.18 | 0.22 | 0.15 | 0.54 | `cs_first_low40(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 20), LogFloatShares)` |
| slot a seed 10 | 过 | 0.26 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.23 | 0.08 | 0.18 | 0.34 | 0.10 | 0.01 | `cs_mask_top_replace_mean(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30))` |
| slot a seed 11 | 过 | 0.22 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.19 | 0.12 | 0.26 | 0.36 | 0.15 | 0.00 | `cs_mask_top_replace_mean_neg(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30))` |
| slot a seed 12 | 过 | 0.12 | `day_cov(Volume, Volume)` | 0.05 | 0.06 | 0.08 | 0.13 | 0.07 | 0.04 | `mul(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 20), sign(cross_zscore(day_last(Close), 60)))` |
| slot a seed 13 | 过 | 0.26 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.23 | 0.06 | 0.13 | 0.09 | 0.09 | 0.00 | `cs_regres(cs_rank(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 30)), cs_rank(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 14 | 过 | 0.41 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.45 | 0.15 | 0.32 | 0.54 | 0.19 | 0.05 | `div(cross_mean(day_cov(Ret, Volume), 20), cross_mean(abs_(day_cov(Ret, Volume)), 120))` |
| slot a seed 15 | 过 | 0.02 | `day_cov(Volume, Volume)` | 0.02 | 0.02 | 0.00 | 0.01 | 0.02 | 0.03 | `cs_flip_by_state(cross_ema(cross_zscore(day_cov(Ret, Volume), 60), 20), day_sum(Amt))` |
| slot a seed 16 | 过 | 0.38 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.40 | 0.17 | 0.27 | 0.22 | 0.21 | 0.03 | `add(cross_tail_mean_q75(cross_zscore(day_cov(Ret, Volume), 120), 60), cross_tail_mean_q25(cross_zscore(day_cov(Ret, Volume), 120), 60))` |
| slot b seed 1 | 过 | 0.28 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.25 | 0.11 | 0.25 | 0.41 | 0.14 | 0.01 | `cross_ema(cross_zscore(day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60), 30)` |
| slot b seed 2 | 过 | 0.24 | `day_cov(Volume, Volume)` | 0.12 | 0.30 | 0.33 | 0.24 | 0.33 | 0.10 | `cross_mean(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60)` |
| slot b seed 3 | 过 | 0.09 | `day_cov(Volume, Volume)` | 0.05 | 0.09 | 0.06 | 0.48 | 0.07 | 0.01 | `cross_ema(cross_zscore(day_signed_ratio(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60), 30)` |
| slot b seed 4 | 过 | 0.07 | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume,` | 0.03 | 0.11 | 0.02 | 0.03 | 0.10 | 0.00 | `cross_autocorr(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60, 1)` |
| slot b seed 5 | 过 | 0.11 | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume,` | 0.07 | 0.10 | 0.01 | 0.02 | 0.09 | 0.01 | `cross_autocorr(day_signed_ratio(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 120, 1)` |
| slot b seed 6 | 过 | 0.43 | `day_cov(Volume, Volume)` | 0.48 | 0.04 | 0.14 | 0.01 | 0.07 | 0.21 | `cross_mean(day_autocorr(mul(sign(in_slice(Ret, 1, 239)), in_slice(Volume, 1, 239)), 1), 40)` |
| slot b seed 7 | 过 | 0.26 | `day_cov(Volume, Volume)` | 0.13 | 0.28 | 0.35 | 0.22 | 0.31 | 0.11 | `cs_bucket_zscore(cross_mean(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 8 | 过 | 0.14 | `day_cov(Volume, Volume)` | 0.13 | 0.17 | 0.07 | 0.01 | 0.16 | 0.09 | `cross_corr(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 9 | 过 | 0.29 | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume,` | 0.18 | 0.20 | 0.15 | 0.02 | 0.22 | 0.09 | `cross_corr(day_cov(Ret, Volume), day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60)` |
| slot b seed 10 | 过 | 0.07 | `day_cov(Volume, Volume)` | 0.05 | 0.06 | 0.01 | 0.03 | 0.05 | 0.04 | `cross_mean(mul(day_last(Ret), div(day_last(Volume), day_sum(Volume))), 40)` |
| slot b seed 11 | 过 | 0.09 | `cross_quantile_q50(cross_corr(day_sum(High), day_cov(Volume,` | 0.04 | 0.07 | 0.03 | 0.01 | 0.07 | 0.06 | `cross_corr(ts_delay(mul(day_last(Ret), div(day_last(Volume), day_sum(Volume))), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 12 | 过 | 0.06 | `day_cov(Volume, Volume)` | 0.03 | 0.02 | 0.03 | 0.07 | 0.02 | 0.00 | `sub(cross_zscore(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60), cross_zscore(mul(day_last(Ret), div(day_last(Volume), day_sum(Volume))), 60))` |
| slot b seed 13 | 过 | 0.53 | `day_cov(Volume, Volume)` | 0.42 | 0.25 | 0.05 | 0.00 | 0.26 | 0.55 | `cs_first_low40(cross_autocorr(day_signed_ratio(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60, 1), LogFloatShares)` |
| slot b seed 14 | 过 | 0.05 | `day_cov(Volume, Volume)` | 0.02 | 0.08 | 0.06 | 0.02 | 0.08 | 0.03 | `mul(cross_mean(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 40), cross_autocorr(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60, 1))` |
| slot b seed 15 | 过 | 0.20 | `day_cov(Volume, Volume)` | 0.08 | 0.26 | 0.28 | 0.20 | 0.28 | 0.08 | `cs_mask_top_replace_mean_neg(cross_mean(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 60))` |
| R 1 variant 1 | 过 | 0.98 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.98 | 0.03 | 0.06 | 0.09 | 0.01 | 0.08 | `ts_skew(day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 40)` |
| R 1 variant 2 | 过 | 0.60 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.63 | 0.09 | 0.01 | 0.04 | 0.07 | 0.10 | `ts_skew(day_cov(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 80)` |
| R 1 variant 3 | 过 | 0.25 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.26 | 0.14 | 0.04 | 0.04 | 0.11 | 0.09 | `ts_skew(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 1, 239)), 80)` |
| R 1 variant 4 | 过 | 0.44 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.45 | 0.03 | 0.28 | 0.03 | 0.02 | 0.26 | `ts_skew(div(day_cov(Ret, Volume), day_mean(Volume)), 80)` |
| R 1 variant 5 | 过 | 0.06 | `day_cov(Volume, Volume)` | 0.05 | 0.08 | 0.00 | 0.00 | 0.07 | 0.05 | `ts_skew(mul(day_last(Ret), div(day_last(Volume), day_sum(Volume))), 80)` |
| R 1 variant 6 | 过 | 0.48 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.52 | 0.10 | 0.02 | 0.03 | 0.08 | 0.12 | `cross_ema(ts_skew(day_cov(Ret, Volume), 80), 10)` |
| R 1 variant 7 | 过 | 0.56 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.60 | 0.04 | 0.04 | 0.04 | 0.03 | 0.08 | `cs_mask_top_replace_mean(ts_skew(day_cov(Ret, Volume), 80))` |
| R 1 variant 8 | 过 | 0.54 | `ts_skew(day_cov(Ret, Volume), 40)` | 0.58 | 0.12 | 0.00 | 0.04 | 0.09 | 0.14 | `cs_mask_top_replace_mean_neg(ts_skew(day_cov(Ret, Volume), 80))` |
| R 2 variant 1 | 过 | 0.09 | `day_cov(Volume, Volume)` | 0.16 | 0.61 | 0.00 | 0.02 | 0.55 | 0.37 | `div(day_cov(Volume, Volume), pow_2(day_mean(Volume)))` |
| R 2 variant 2 | 过 | 0.14 | `day_cov(Volume, Volume)` | 0.06 | 0.64 | 0.19 | 0.06 | 0.53 | 0.49 | `cross_mean(div(day_cov(Volume, Volume), pow_2(day_mean(Volume))), 40)` |
| R 2 variant 3 | 过 | 0.14 | `day_cov(Volume, Volume)` | 0.07 | 0.64 | 0.20 | 0.06 | 0.53 | 0.49 | `cross_mean(div(day_cov(in_slice(Volume, 1, 239), in_slice(Volume, 1, 239)), pow_2(day_mean(in_slice(Volume, 1, 239)))), 40)` |
| R 2 variant 4 | 过 | 0.24 | `day_cov(Volume, Volume)` | 0.15 | 0.20 | 0.33 | 0.23 | 0.25 | 0.07 | `cross_ema(cross_zscore(day_cov(in_slice(Volume, 1, 239), in_slice(Volume, 1, 239)), 120), 20)` |
