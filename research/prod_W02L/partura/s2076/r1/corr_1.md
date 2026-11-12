# 相关度表:种子 2076,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.23 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.08 | 0.18 | 0.55 | 0.29 | 0.21 | 0.10 | `day_var(pow_2_5(pow_2_5(Ret)))` |
| slot a seed 1 | 过 | 0.44 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.27 | 0.10 | 0.34 | 0.10 | 0.12 | 0.24 | `sub(cross_mean(day_var(pow_2_5(pow_2_5(Ret))), 5), cross_mean(day_var(pow_2_5(pow_2_5(Ret))), 60))` |
| slot a seed 2 | 过 | 0.73 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.69 | 0.20 | 0.12 | 0.11 | 0.19 | 0.47 | `sub(cross_ema(day_var(pow_2_5(pow_2_5(Ret))), 5), cross_ema(day_var(pow_2_5(pow_2_5(Ret))), 40))` |
| slot a seed 3 | 废品 | 0.40 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.23 | 0.17 | 0.46 | 0.04 | 0.21 | 0.22 | `cross_zscore(day_var(pow_2_5(pow_2_5(Ret))), 40)` |
| slot a seed 4 | 废品 | 0.28 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.25 | 0.15 | 0.45 | 0.17 | 0.20 | 0.15 | `cross_zscore(day_var(pow_2_5(pow_2_5(Ret))), 20)` |
| slot a seed 5 | 废品 | 0.32 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.27 | 0.17 | 0.52 | 0.24 | 0.22 | 0.17 | `cross_stddev(day_var(pow_2_5(pow_2_5(Ret))), 20)` |
| slot a seed 6 | 过 | 0.41 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.34 | 0.19 | 0.67 | 0.25 | 0.24 | 0.23 | `cross_tail_mean_q75(day_var(pow_2_5(pow_2_5(Ret))), 20)` |
| slot a seed 7 | 过 | 0.34 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.31 | 0.17 | 0.61 | 0.30 | 0.21 | 0.19 | `cross_max(day_var(pow_2_5(pow_2_5(Ret))), 10)` |
| slot a seed 8 | 过 | 0.21 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.09 | 0.21 | 0.77 | 0.32 | 0.26 | 0.02 | `sub(day_var(pow_2_5(pow_2_5(Ret))), day_var(Ret))` |
| slot a seed 9 | 过 | 0.28 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.02 | 0.27 | 0.94 | 0.32 | 0.33 | 0.06 | `sub(cross_mean(day_var(pow_2_5(pow_2_5(Ret))), 10), cross_mean(day_var(Ret), 10))` |
| slot a seed 10 | 过 | 0.79 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.67 | 0.01 | 0.45 | 0.05 | 0.06 | 0.43 | `cross_ema(day_var(pow_2_5(pow_2_5(Ret))), 10)` |
| slot a seed 11 | 过 | 0.03 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.02 | 0.09 | 0.08 | 0.22 | 0.09 | 0.01 | `sub(cross_zscore(day_var(pow_2_5(pow_2_5(Ret))), 20), cross_zscore(day_var(Ret), 20))` |
| slot a seed 12 | 过 | 0.41 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.33 | 0.21 | 0.67 | 0.25 | 0.26 | 0.22 | `mul(cross_mean(day_var(pow_2_5(pow_2_5(Ret))), 20), day_pos_ratio(Ret))` |
| slot b seed 1 | 过 | 0.03 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.03 | 0.07 | 0.01 | 0.00 | 0.06 | 0.08 | `cross_mean(day_corr(Ret, in_delay(Amt, 1)), 20)` |
| slot b seed 2 | 过 | 0.06 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.07 | 0.01 | 0.02 | 0.02 | 0.00 | 0.03 | `cross_mean(day_corr(Ret, in_delay(Amt, 3)), 20)` |
| slot b seed 3 | 过 | 0.04 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.04 | 0.07 | 0.01 | 0.02 | 0.07 | 0.09 | `cross_ema(day_corr(Ret, in_delay(Amt, 1)), 10)` |
| slot b seed 4 | 过 | 0.04 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.03 | 0.04 | 0.03 | 0.00 | 0.04 | 0.07 | `cross_mean(day_corr(Ret, in_delay(Volume, 1)), 20)` |
| slot b seed 5 | 过 | 0.09 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.10 | 0.06 | 0.04 | 0.00 | 0.07 | 0.03 | `cross_mean(day_corr(Ret, in_delay(Amt, 5)), 40)` |
| slot b seed 6 | 过 | 0.27 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.20 | 0.24 | 0.35 | 0.59 | 0.26 | 0.04 | `cross_mean(day_corr(in_delay(Ret, 1), Amt), 20)` |
| slot b seed 7 | 过 | 0.03 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.03 | 0.07 | 0.01 | 0.00 | 0.06 | 0.08 | `cross_mean(day_corr(Ret, in_delay(in_demean(Amt), 1)), 20)` |
| slot b seed 8 | 过 | 0.05 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.05 | 0.00 | 0.03 | 0.14 | 0.00 | 0.06 | `cross_mean(day_corr(Ret, in_delay(in_stddev_rolling(Ret, 5), 1)), 20)` |
| slot b seed 9 | 过 | 0.01 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.01 | 0.00 | 0.01 | 0.02 | 0.00 | 0.01 | `sub(cross_mean(day_corr(Ret, in_delay(Amt, 1)), 5), cross_mean(day_corr(Ret, in_delay(Amt, 1)), 40))` |
| slot b seed 10 | 过 | 0.01 | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | 0.01 | 0.00 | 0.01 | 0.01 | 0.00 | 0.01 | `cross_zscore(day_corr(Ret, in_delay(Amt, 1)), 40)` |
| slot b seed 11 | 过 | 0.22 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.19 | 0.01 | 0.10 | 0.08 | 0.01 | 0.20 | `cross_stddev(day_corr(Ret, in_delay(Amt, 1)), 20)` |
| slot b seed 12 | 过 | 0.16 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.10 | 0.12 | 0.19 | 0.49 | 0.14 | 0.06 | `sub(cross_mean(day_corr(Ret, in_delay(Amt, 1)), 20), cross_mean(day_corr(Ret, Amt), 20))` |
