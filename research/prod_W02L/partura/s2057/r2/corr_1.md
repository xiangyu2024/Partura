# 相关度表:种子 2057,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.36 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.37 | 0.04 | 0.32 | 0.09 | 0.10 | 0.21 | `ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50)` |
| slot a seed 1 | 废品 | 0.21 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.17 | 0.10 | 0.16 | 0.12 | 0.13 | 0.00 | `ts_rank(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 60)` |
| slot a seed 2 | 过 | 0.20 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.14 | 0.09 | 0.17 | 0.14 | 0.12 | 0.00 | `ts_delta(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 20)` |
| slot a seed 3 | 过 | 0.48 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.32 | 0.41 | 0.42 | 0.03 | 0.43 | 0.02 | `div(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), cross_mean(day_zero_ratio(Ret), 50))` |
| slot a seed 4 | 过 | 0.26 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.21 | 0.14 | 0.21 | 0.11 | 0.17 | 0.00 | `sub(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), ts_mean(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 60))` |
| slot a seed 5 | 过 | 0.04 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.02 | 0.01 | 0.04 | 0.07 | 0.02 | 0.01 | `ts_corr(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), day_sum(Amt), 30)` |
| slot a seed 6 | 过 | 0.17 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.07 | 0.13 | 0.25 | 0.57 | 0.15 | 0.03 | `mul(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), sign(ts_mean(day_sum(Ret), 20)))` |
| slot a seed 7 | 过 | 0.36 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.37 | 0.04 | 0.32 | 0.09 | 0.10 | 0.21 | `sub(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), ts_stddev(ts_stddev(day_std(Ret), 10), 50))` |
| slot a seed 8 | 过 | 0.34 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.36 | 0.04 | 0.30 | 0.03 | 0.09 | 0.21 | `ts_decay_linear(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 30)` |
| slot a seed 9 | 过 | 0.33 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.29 | 0.10 | 0.27 | 0.07 | 0.14 | 0.11 | `div(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), ts_stddev(ts_stddev(day_centroid(Amt), 10), 50))` |
| slot a seed 10 | 过 | 0.37 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.38 | 0.05 | 0.34 | 0.08 | 0.11 | 0.23 | `add(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), ts_stddev(ts_stddev(day_centroid(Amt), 10), 50))` |
| slot a seed 11 | 过 | 0.34 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.33 | 0.07 | 0.30 | 0.04 | 0.11 | 0.20 | `ts_max(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 30)` |
| slot a seed 12 | 过 | 0.08 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.15 | 0.03 | 0.01 | 0.11 | 0.01 | 0.03 | `ts_skew(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 40)` |
| slot b seed 1 | 过 | 0.53 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.58 | 0.33 | 0.24 | 0.01 | 0.28 | 0.02 | `ts_mean(sub(day_zero_ratio(Ret), day_zero_ratio(Amt)), 20)` |
| slot b seed 2 | 过 | 0.22 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.28 | 0.01 | 0.10 | 0.19 | 0.04 | 0.05 | `ts_stddev(sub(day_zero_ratio(Ret), day_zero_ratio(Amt)), 20)` |
| slot b seed 3 | 废品 | 0.15 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.13 | 0.03 | 0.07 | 0.08 | 0.04 | 0.10 | `ts_mean(sub(day_zero_ratio(in_slice(Ret, 121, 240)), day_zero_ratio(in_slice(Ret, 1, 120))), 20)` |
| slot b seed 4 | 过 | 0.26 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.24 | 0.29 | 0.11 | 0.13 | 0.22 | 0.21 | `ts_stddev(sub(day_zero_ratio(in_slice(Ret, 121, 240)), day_zero_ratio(in_slice(Ret, 1, 120))), 30)` |
| slot b seed 5 | 废品 | 0.54 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.58 | 0.40 | 0.21 | 0.02 | 0.35 | 0.09 | `ts_mean(day_zero_ratio(in_slice(Ret, 211, 240)), 20)` |
| slot b seed 6 | 废品 | 0.45 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.53 | 0.40 | 0.10 | 0.10 | 0.33 | 0.19 | `ts_stddev(day_zero_ratio(in_slice(Ret, 1, 30)), 20)` |
| slot b seed 7 | 过 | 0.53 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.58 | 0.33 | 0.24 | 0.01 | 0.28 | 0.02 | `ts_decay_linear(sub(day_zero_ratio(Ret), day_zero_ratio(Amt)), 30)` |
| slot b seed 8 | 废品 | 0.54 | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean` | 0.58 | 0.37 | 0.26 | 0.01 | 0.32 | 0.05 | `ts_mean(sub(day_zero_ratio(in_slice(Ret, 1, 120)), day_zero_ratio(in_slice(Amt, 1, 120))), 20)` |
| slot b seed 9 | 过 | 0.10 | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt` | 0.18 | 0.19 | 0.28 | 0.08 | 0.16 | 0.35 | `ts_corr(day_zero_ratio(Ret), day_gini(Amt), 40)` |
| slot b seed 10 | 过 | 0.47 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 5` | 0.40 | 0.19 | 0.04 | 0.03 | 0.21 | 0.01 | `ts_stddev(ts_mean(sub(day_zero_ratio(Ret), day_zero_ratio(Amt)), 10), 50)` |
