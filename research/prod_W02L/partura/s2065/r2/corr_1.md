# 相关度表:种子 2065,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.83 | `day_var(in_max_rolling(Vwap, 60))` | 0.95 | 0.47 | 0.06 | 0.03 | 0.43 | 0.44 | `day_mean(Close)` |
| slot a seed 1 | 过 | 0.14 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.05 | 0.11 | 0.21 | 0.40 | 0.13 | 0.14 | `div(day_mean(Close), cross_max(day_mean(Close), 250))` |
| slot a seed 2 | 过 | 0.27 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.07 | 0.35 | 0.42 | 0.29 | 0.37 | 0.17 | `div(day_mean(Close), cross_mean(day_mean(Close), 500))` |
| slot a seed 3 | 过 | 0.06 | `day_q_stat_std(in_max_rolling(Volume, 60))` | 0.12 | 0.12 | 0.01 | 0.63 | 0.10 | 0.08 | `div(day_mean(Close), cross_max(day_mean(Close), 60))` |
| slot a seed 4 | 过 | 0.19 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.07 | 0.25 | 0.36 | 0.19 | 0.26 | 0.09 | `cross_delta(day_mean(Close), 250)` |
| slot a seed 5 | 过 | 0.21 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.09 | 0.23 | 0.41 | 0.46 | 0.26 | 0.06 | `div(cross_delta(day_mean(Close), 60), day_mean(Close))` |
| slot a seed 6 | 过 | 0.32 | `day_var(in_max_rolling(Vwap, 60))` | 0.21 | 0.32 | 0.32 | 0.17 | 0.30 | 0.02 | `div(day_mean(Close), cross_stddev(day_mean(Close), 120))` |
| slot a seed 7 | 过 | 0.27 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.07 | 0.37 | 0.41 | 0.12 | 0.38 | 0.17 | `div(cross_mean(day_mean(Close), 20), cross_mean(day_mean(Close), 500))` |
| slot a seed 8 | 过 | 0.19 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.32 | 0.09 | 0.37 | 0.38 | 0.12 | 0.05 | `sub(day_mean(Close), cross_quantile_q75(day_mean(Close), 250))` |
| slot a seed 9 | 过 | 0.25 | `day_var(in_max_rolling(Vwap, 60))` | 0.09 | 0.28 | 0.43 | 0.42 | 0.29 | 0.15 | `div(sub(day_mean(Close), cross_min(day_mean(Close), 250)), sub(cross_max(day_mean(Close), 250), cross_min(day_mean(Close), 250)))` |
| slot a seed 10 | 过 | 0.14 | `day_var(in_max_rolling(Vwap, 60))` | 0.07 | 0.11 | 0.06 | 0.01 | 0.10 | 0.13 | `cross_corr(day_mean(Close), cross_delay(day_mean(Close), 20), 120)` |
| slot b core | 过 | 0.32 | `day_var(in_max_rolling(Vwap, 60))` | 0.22 | 0.08 | 0.04 | 0.04 | 0.06 | 0.02 | `inv(day_q_stat_std(Close))` |
| slot b seed 1 | 过 | 0.28 | `day_var(in_max_rolling(Vwap, 60))` | 0.21 | 0.23 | 0.10 | 0.10 | 0.17 | 0.11 | `cross_mean(inv(day_q_stat_std(Close)), 20)` |
| slot b seed 2 | 过 | 0.30 | `day_var(in_max_rolling(Vwap, 60))` | 0.23 | 0.24 | 0.11 | 0.05 | 0.19 | 0.13 | `cross_med(inv(day_q_stat_std(Close)), 60)` |
| slot b seed 3 | 过 | 0.59 | `day_var(in_max_rolling(Vwap, 60))` | 0.90 | 0.38 | 0.07 | 0.04 | 0.36 | 0.39 | `mul(day_mean(Close), inv(day_q_stat_std(Close)))` |
| slot b seed 4 | 过 | 0.15 | `day_var(in_max_rolling(Vwap, 60))` | 0.02 | 0.01 | 0.00 | 0.02 | 0.01 | 0.00 | `cross_delta(inv(day_q_stat_std(Close)), 20)` |
| slot b seed 5 | 过 | 0.11 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.17 | 0.01 | 0.12 | 0.00 | 0.03 | 0.07 | `div(inv(day_q_stat_std(Close)), cross_mean(inv(day_q_stat_std(Close)), 120))` |
| slot b seed 6 | 过 | 0.56 | `day_q_stat_std(in_max_rolling(Amt, 60))` | 0.66 | 0.46 | 0.23 | 0.21 | 0.47 | 0.18 | `sub(inv(day_q_stat_std(Close)), inv(day_q_stat_std(Amt)))` |
| slot b seed 7 | 废品 | 0.13 | `day_var(in_max_rolling(Vwap, 60))` | 0.17 | 0.08 | 0.08 | nan | 0.04 | 0.04 | `cs_demean(cross_med(inv(day_q_stat_std(Close)), 40))` |
| slot b seed 8 | 过 | 0.03 | `day_var(in_max_rolling(Vwap, 60))` | 0.03 | 0.02 | 0.00 | 0.00 | 0.02 | 0.01 | `cross_corr(inv(day_q_stat_std(Close)), cross_delay(inv(day_q_stat_std(Close)), 10), 60)` |
| slot b seed 9 | 过 | 0.17 | `ts_stddev(abs_(cs_demean(day_sum(sub(in_sorted_cumsum_forwar` | 0.08 | 0.18 | 0.37 | 0.40 | 0.20 | 0.03 | `mul(inv(day_q_stat_std(Close)), cross_delta(day_mean(Close), 60))` |
