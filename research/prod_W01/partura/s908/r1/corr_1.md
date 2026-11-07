# 相关度表:种子 908,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 2 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.16 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.35 | 0.18 | 0.16 | 0.13 | 0.19 | 0.07 | `day_centroid(Amt)` |
| slot a seed 1 | 过 | 0.27 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.37 | 0.48 | 0.42 | 0.19 | 0.51 | 0.13 | `cross_mean(day_centroid(Amt), 20)` |
| slot a seed 2 | 过 | 0.29 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.36 | 0.52 | 0.43 | 0.17 | 0.55 | 0.14 | `cross_ema(day_centroid(Amt), 10)` |
| slot a seed 3 | 过 | 0.23 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.35 | 0.52 | 0.39 | 0.12 | 0.54 | 0.15 | `cross_med(day_centroid(Amt), 30)` |
| slot a seed 4 | 过 | 0.29 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.40 | 0.38 | 0.45 | 0.22 | 0.42 | 0.07 | `cross_quantile_q25(day_centroid(Amt), 20)` |
| slot a seed 5 | 过 | 0.08 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.02 | 0.03 | 0.01 | 0.09 | 0.02 | 0.02 | `cross_zscore(day_centroid(Amt), 40)` |
| slot a seed 6 | 过 | 0.20 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.09 | 0.03 | 0.03 | 0.18 | 0.02 | 0.04 | `sub(cross_mean(day_centroid(Amt), 5), cross_mean(day_centroid(Amt), 60))` |
| slot a seed 7 | 过 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.34 | 0.17 | 0.15 | 0.12 | 0.18 | 0.07 | `cs_bucket_zscore(day_centroid(Amt), ListAge)` |
| slot a seed 8 | 过 | 0.16 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.37 | 0.18 | 0.15 | 0.13 | 0.19 | 0.07 | `cs_regres(day_centroid(Amt), ListAge)` |
| slot a seed 9 | 过 | 0.27 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.35 | 0.46 | 0.40 | 0.19 | 0.49 | 0.14 | `cross_mean(cs_bucket_zscore(day_centroid(Amt), ListAge), 20)` |
| slot a seed 10 | 过 | 0.28 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.38 | 0.45 | 0.41 | 0.19 | 0.48 | 0.10 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)` |
| slot a seed 11 | 过 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.33 | 0.15 | 0.16 | 0.12 | 0.16 | 0.03 | `cs_bucket_zscore(day_centroid(Amt), day_wmean(Open, Amt))` |
| slot a seed 12 | 过 | 0.03 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.08 | 0.02 | 0.01 | 0.03 | 0.02 | 0.00 | `sub(day_centroid(mul(Amt, is_gt0(Ret))), day_centroid(Amt))` |
| slot a seed 13 | 过 | 0.03 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.03 | 0.03 | 0.03 | 0.02 | 0.02 | 0.00 | `sub(day_centroid(Amt), day_centroid(mul(Amt, is_lt0(Ret))))` |
| slot a seed 14 | 过 | 0.04 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.03 | 0.09 | 0.20 | 0.45 | 0.11 | 0.03 | `cross_ema(sub(day_centroid(Amt), day_centroid(Volume)), 20)` |
| slot b seed 1 | 过 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.33 | 0.29 | 0.16 | 0.14 | 0.29 | 0.14 | `day_topw_mean(in_index(Amt), Amt)` |
| slot b seed 2 | 过 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.34 | 0.32 | 0.16 | 0.13 | 0.32 | 0.15 | `day_corr(in_index(Amt), Amt)` |
| slot b seed 3 | 过 | 0.06 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.18 | 0.16 | 0.06 | 0.09 | 0.15 | 0.04 | `day_centroid(Ret)` |
| slot b seed 4 | 过 | 0.13 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.14 | 0.09 | 0.11 | 0.07 | 0.10 | 0.10 | `sub(day_centroid(Ret), day_centroid(Volume))` |
| slot b seed 5 | 过 | 0.06 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.21 | 0.23 | 0.06 | 0.10 | 0.21 | 0.06 | `day_topw_mean(in_index(Amt), Ret)` |
| slot b seed 6 | 过 | 0.14 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.34 | 0.16 | 0.17 | 0.11 | 0.18 | 0.00 | `div(day_sum(in_slice(Amt, 0, 30)), day_sum(Amt))` |
| slot b seed 7 | 过 | 0.11 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.17 | 0.15 | 0.07 | 0.10 | 0.15 | 0.16 | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` |
| slot b seed 8 | 过 | 0.03 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.04 | 0.09 | 0.03 | 0.02 | 0.08 | 0.17 | `day_centroid(in_half(Amt, False))` |
| slot b seed 9 | 过 | 0.01 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt` | 0.04 | 0.00 | 0.01 | 0.01 | 0.00 | 0.00 | `sub(day_centroid(mul(Volume, is_gt0(Ret))), day_centroid(mul(Volume, is_lt0(Ret))))` |
| slot b seed 10 | 过 | 0.23 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.35 | 0.69 | 0.33 | 0.15 | 0.67 | 0.29 | `cross_mean(day_corr(in_index(Amt), Amt), 20)` |
| slot b seed 11 | 过 | 0.21 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.31 | 0.73 | 0.33 | 0.10 | 0.72 | 0.32 | `cross_ema(day_topw_mean(in_index(Amt), Amt), 20)` |
| slot b seed 12 | 过 | 0.23 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.14 | 0.24 | 0.29 | 0.10 | 0.27 | 0.22 | `cross_mean(sub(day_centroid(Ret), day_centroid(Volume)), 20)` |
| slot b seed 13 | 过 | 0.01 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt` | 0.03 | 0.03 | 0.01 | 0.12 | 0.03 | 0.01 | `day_corr(in_index(Close), Close)` |
| slot b seed 14 | 过 | 0.20 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.19 | 0.46 | 0.23 | 0.19 | 0.46 | 0.37 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| R 1 variant 1 | 过 | 0.80 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.95 | 0.15 | 0.17 | 0.12 | 0.17 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt))), 20)` |
| R 1 variant 2 | 过 | 0.80 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.95 | 0.14 | 0.17 | 0.12 | 0.17 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 20)` |
| R 1 variant 3 | 过 | 0.72 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.90 | 0.17 | 0.18 | 0.09 | 0.20 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 30)` |
| R 1 variant 4 | 过 | 0.67 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.87 | 0.19 | 0.18 | 0.07 | 0.21 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 40)` |
| R 1 variant 5 | 过 | 0.78 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.92 | 0.13 | 0.17 | 0.12 | 0.16 | 0.14 | `ts_quantile_q75(cs_regres(ListAge, day_centroid(Volume)), 20)` |
| R 1 variant 6 | 过 | 0.67 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.84 | 0.19 | 0.10 | 0.06 | 0.19 | 0.20 | `ts_quantile_q50(cs_regres(ListAge, pow_3(day_centroid(Volume))), 20)` |
| R 1 variant 7 | 过 | 0.69 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.81 | 0.20 | 0.09 | 0.06 | 0.20 | 0.20 | `ts_mean(cs_regres(ListAge, pow_3(day_centroid(Volume))), 20)` |
| R 1 variant 8 | 过 | 0.64 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt)))` | 0.83 | 0.20 | 0.17 | 0.05 | 0.21 | 0.15 | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 50)` |
| R 2 variant 1 | 过 | 0.97 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt` | 0.96 | 0.04 | 0.03 | 0.00 | 0.04 | 0.03 | `cs_bucket_rank(day_quantile_q25(High), day_wmean(Open, Amt))` |
| R 2 variant 2 | 过 | 0.85 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt` | 0.89 | 0.07 | 0.01 | 0.01 | 0.07 | 0.10 | `cs_bucket_demean(day_quantile_q25(High), day_wmean(Open, Amt))` |
| R 2 variant 3 | 过 | 1.00 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt` | 1.00 | 0.02 | 0.02 | 0.00 | 0.02 | 0.01 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Volume))` |
| R 2 variant 4 | 过 | 0.96 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt` | 0.99 | 0.02 | 0.02 | 0.00 | 0.02 | 0.01 | `cs_bucket_zscore(day_quantile_q25(High), day_mean(Open))` |
| R 2 variant 5 | 过 | 0.99 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt` | 1.00 | 0.04 | 0.00 | 0.01 | 0.03 | 0.00 | `cs_bucket_zscore(day_quantile_q75(High), day_wmean(Open, Amt))` |
| R 2 variant 6 | 过 | 1.00 | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt` | 1.00 | 0.03 | 0.01 | 0.01 | 0.03 | 0.00 | `cs_bucket_zscore(day_median(High), day_wmean(Open, Amt))` |
