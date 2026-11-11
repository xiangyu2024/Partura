# 相关度表:种子 2054,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.19 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.10 | 0.11 | 0.41 | 0.55 | 0.16 | 0.08 | `cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)` |
| slot a seed 2 | 过 | 0.18 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.09 | 0.20 | 0.50 | 0.20 | 0.25 | 0.15 | `cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 60)` |
| slot a seed 3 | 过 | 0.19 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.09 | 0.22 | 0.30 | 0.41 | 0.24 | 0.04 | `cross_ema(day_corr(Ret, Volume), 20)` |
| slot a seed 4 | 过 | 0.17 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.08 | 0.25 | 0.32 | 0.24 | 0.27 | 0.04 | `cross_mean(day_corr(Ret, Amt), 60)` |
| slot a seed 5 | 过 | 0.28 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.18 | 0.67 | 0.29 | 0.17 | 0.71 | 0.51 | `cross_mean(sub(day_mean(in_topk_masked(Ret, Volume, 20)), day_mean(Ret)), 20)` |
| slot a seed 6 | 过 | 0.09 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.04 | 0.06 | 0.02 | 0.50 | 0.05 | 0.05 | `cross_mean(div(sub(day_wmean(Vwap, Volume), day_last(Close)), day_last(Close)), 20)` |
| slot a seed 7 | 过 | 0.21 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.10 | 0.24 | 0.46 | 0.39 | 0.29 | 0.02 | `cs_bucket_zscore(cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 30), LogFloatCap)` |
| slot a seed 8 | 过 | 0.18 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.10 | 0.23 | 0.32 | 0.33 | 0.24 | 0.01 | `cs_bucket_zscore(cross_ema(day_corr(Ret, Volume), 30), LogFloatCap)` |
| slot a seed 9 | 过 | 0.07 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.09 | 0.16 | 0.12 | 0.10 | 0.18 | 0.25 | `cross_regbeta(day_sum(Volume), day_sum(Ret), 60)` |
| slot a seed 10 | 过 | 0.03 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.03 | 0.22 | 0.03 | 0.01 | 0.20 | 0.07 | `cross_corr(day_wmean(Ret, Volume), day_mean(Ret), 60)` |
| slot a seed 11 | 过 | 0.08 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.03 | 0.06 | 0.04 | 0.27 | 0.06 | 0.01 | `cross_zscore(cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 5), 60)` |
| slot a seed 12 | 过 | 0.15 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.10 | 0.14 | 0.35 | 0.36 | 0.18 | 0.07 | `cross_mean(div(day_wmean(Ret, Amt), day_std(Ret)), 40)` |
| slot b seed 1 | 过 | 0.07 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.02 | 0.07 | 0.05 | 0.00 | 0.07 | 0.08 | `cross_corr(day_sum(in_slice(Ret, 11, 60)), day_sum(in_slice(Ret, 181, 230)), 60)` |
| slot b seed 2 | 过 | 0.07 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.02 | 0.08 | 0.04 | 0.01 | 0.07 | 0.09 | `cross_corr(day_sum(in_slice(Ret, 11, 60)), day_sum(in_slice(Ret, 181, 230)), 120)` |
| slot b seed 3 | 过 | 0.07 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.02 | 0.09 | 0.06 | 0.00 | 0.08 | 0.08 | `cross_regbeta(day_sum(in_slice(Ret, 11, 60)), day_sum(in_slice(Ret, 181, 230)), 60)` |
| slot b seed 4 | 过 | 0.02 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.01 | 0.00 | 0.04 | 0.02 | 0.01 | 0.07 | `cross_mean(mul(day_sum(in_slice(Ret, 11, 60)), day_sum(in_slice(Ret, 181, 230))), 30)` |
| slot b seed 5 | 过 | 0.03 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.01 | 0.02 | 0.01 | 0.01 | 0.01 | 0.07 | `cross_mean(mul(sign(day_sum(in_slice(Ret, 11, 60))), day_sum(in_slice(Ret, 181, 230))), 30)` |
| slot b seed 6 | 过 | 0.05 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.03 | 0.02 | 0.04 | 0.01 | 0.02 | 0.05 | `cross_corr(day_sum(in_slice(Ret, 11, 120)), day_sum(in_slice(Ret, 121, 230)), 60)` |
| slot b seed 7 | 过 | 0.05 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.03 | 0.02 | 0.04 | 0.00 | 0.02 | 0.04 | `cross_regbeta(day_sum(in_slice(Ret, 11, 120)), day_sum(in_slice(Ret, 121, 230)), 90)` |
| slot b seed 8 | 过 | 0.03 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.02 | 0.03 | 0.05 | 0.01 | 0.02 | 0.01 | `cross_corr(day_sum(in_slice(Ret, 11, 30)), day_sum(in_slice(Ret, 31, 211)), 60)` |
| slot b seed 9 | 过 | 0.01 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.01 | 0.03 | 0.02 | 0.01 | 0.03 | 0.01 | `cross_mean(mul(sign(day_sum(in_slice(Ret, 11, 30))), day_sum(in_slice(Ret, 31, 211))), 40)` |
| slot b seed 10 | 过 | 0.01 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.02 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | `cross_corr(day_sum(in_slice(Ret, 11, 60)), cross_delay(day_sum(in_slice(Ret, 181, 230)), 1), 60)` |
| slot b seed 11 | 过 | 0.02 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.02 | 0.02 | 0.03 | 0.00 | 0.02 | 0.01 | `cross_regres(day_sum(in_slice(Ret, 11, 60)), day_sum(in_slice(Ret, 181, 230)), 60)` |
| slot b seed 12 | 过 | 0.05 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.02 | 0.02 | 0.05 | 0.00 | 0.02 | 0.00 | `cs_bucket_zscore(cross_corr(day_sum(in_slice(Ret, 11, 60)), day_sum(in_slice(Ret, 181, 230)), 60), LogFloatCap)` |
