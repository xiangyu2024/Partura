# 相关度表:种子 2076,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 12 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.05 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.16 | 0.02 | 0.01 | 0.03 | 0.02 | 0.06 | `sqrt(day_skew(in_slice(Open, 0, 60)))` |
| slot a seed 1 | 过 | 0.48 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in` | 0.46 | 0.12 | 0.14 | 0.03 | 0.14 | 0.01 | `cross_mean(ts_cov(day_zero_ratio(Ret), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)` |
| slot a seed 2 | 过 | 0.41 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in` | 0.40 | 0.12 | 0.10 | 0.00 | 0.14 | 0.02 | `cross_mean(ts_corr(day_zero_ratio(Ret), sqrt(day_skew(in_slice(Open, 0, 60))), 20), 30)` |
| slot a seed 3 | 过 | 0.37 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in` | 0.35 | 0.08 | 0.03 | 0.01 | 0.08 | 0.05 | `cross_mean(ts_cov(day_zero_ratio(in_slice(Amt, 0, 60)), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)` |
| slot a seed 4 | 过 | 0.40 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in` | 0.37 | 0.25 | 0.16 | 0.03 | 0.27 | 0.05 | `cross_mean(ts_cov(day_gini(Amt), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)` |
| slot a seed 5 | 过 | 0.13 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.14 | 0.14 | 0.10 | 0.00 | 0.16 | 0.01 | `cross_mean(ts_corr(day_skew(Amt), sqrt(day_skew(in_slice(Open, 0, 60))), 20), 30)` |
| slot a seed 6 | 过 | 0.67 | `day_mean(abs_(cross_regres(Ret, Volume, 20)))` | 0.50 | 0.81 | 0.03 | 0.03 | 0.78 | 0.72 | `cross_ema(mul(day_zero_ratio(Amt), sqrt(day_skew(in_slice(Open, 0, 60)))), 20)` |
| slot a seed 7 | 过 | 0.09 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Ope` | 0.10 | 0.03 | 0.01 | 0.09 | 0.02 | 0.01 | `sub(cross_mean(ts_cov(day_zero_ratio(Ret), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 10), cross_mean(ts_cov(day_zero_ratio(Ret), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 40))` |
| slot a seed 8 | 过 | 0.78 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in` | 0.78 | 0.10 | 0.09 | 0.00 | 0.11 | 0.01 | `cross_mean(ts_corr(day_zero_ratio(Amt), sqrt(day_skew(in_slice(Open, 0, 60))), 20), 30)` |
| slot a seed 9 | 过 | 0.10 | `day_max(cross_corr(Amt, cross_corr(Amt, Ret, 60), 60))` | 0.12 | 0.06 | 0.22 | 0.25 | 0.07 | 0.02 | `cross_zscore(ts_mean(mul(day_zero_ratio(Ret), sqrt(day_skew(in_slice(Open, 0, 60)))), 20), 40)` |
| slot a seed 10 | 过 | 0.39 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in` | 0.36 | 0.11 | 0.15 | 0.03 | 0.14 | 0.00 | `cross_mean(ts_cov(day_pos_ratio(Ret), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)` |
| slot a seed 11 | 过 | 0.65 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(sqrt(day_skew(in` | 0.64 | 0.06 | 0.07 | 0.02 | 0.08 | 0.01 | `cross_mean(ts_cov(day_zero_ratio(in_slice(Amt, 181, 240)), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)` |
| slot a seed 12 | 过 | 0.32 | `day_mean(in_first(Amt))` | 0.19 | 0.40 | 0.18 | 0.02 | 0.43 | 0.22 | `cross_mean(ts_cov(day_std(Amt), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)` |
| slot b seed 1 | 废品 | 0.61 | `day_mean(abs_(cross_regres(Ret, Volume, 20)))` | 0.38 | 0.79 | 0.11 | 0.04 | 0.76 | 0.58 | `cross_mean(sub(day_zero_ratio(in_slice(Amt, 181, 240)), day_zero_ratio(in_slice(Amt, 0, 60))), 30)` |
| slot b seed 2 | 过 | 0.01 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.04 | 0.01 | 0.04 | 0.03 | 0.01 | 0.01 | `cross_mean(ts_cov(sub(day_zero_ratio(in_slice(Amt, 181, 240)), day_zero_ratio(in_slice(Amt, 0, 60))), day_sum(in_slice(Ret, 181, 240)), 10), 30)` |
| slot b seed 3 | 过 | 0.03 | `day_mean(in_first(Amt))` | 0.02 | 0.06 | 0.06 | 0.02 | 0.05 | 0.04 | `cross_mean(ts_corr(day_zero_ratio(in_slice(Amt, 181, 240)), day_sum(in_slice(Ret, 181, 240)), 20), 30)` |
| slot b seed 4 | 过 | 0.62 | `day_mean(abs_(cross_regres(Ret, Volume, 20)))` | 0.46 | 0.77 | 0.04 | 0.05 | 0.73 | 0.65 | `ts_std(sub(day_zero_ratio(in_slice(Amt, 181, 240)), day_zero_ratio(in_slice(Amt, 0, 60))), 30)` |
| slot b seed 5 | 过 | 0.20 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.16 | 0.03 | 0.07 | 0.04 | 0.06 | 0.03 | `cross_mean(ts_cov(day_zero_ratio(in_slice(Amt, 181, 240)), day_sum(in_slice(Ret, 0, 60)), 10), 30)` |
| slot b seed 6 | 过 | 0.50 | `day_mean(abs_(cross_regres(Ret, Volume, 20)))` | 0.24 | 0.57 | 0.04 | 0.01 | 0.54 | 0.60 | `cross_ema(sub(day_zero_ratio(in_slice(Amt, 181, 240)), day_zero_ratio(in_slice(Amt, 61, 180))), 20)` |
| slot b seed 7 | 过 | 0.04 | `day_max(cross_corr(Amt, cross_corr(Amt, Ret, 60), 60))` | 0.09 | 0.04 | 0.10 | 0.09 | 0.04 | 0.02 | `cross_mean(ts_cov(day_zero_ratio(in_slice(Amt, 0, 60)), day_sum(in_slice(Ret, 0, 60)), 10), 30)` |
| slot b seed 8 | 废品 | 0.18 | `day_max(cross_corr(Amt, cross_corr(Amt, Ret, 60), 60))` | 0.14 | 0.09 | 0.24 | 0.25 | 0.11 | 0.00 | `sub(cross_mean(day_zero_ratio(in_slice(Amt, 181, 240)), 10), cross_mean(day_zero_ratio(in_slice(Amt, 181, 240)), 60))` |
| slot b seed 9 | 过 | 0.16 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.13 | 0.03 | 0.08 | 0.04 | 0.05 | 0.02 | `cross_mean(ts_corr(sub(day_zero_ratio(in_slice(Amt, 181, 240)), day_zero_ratio(in_slice(Amt, 0, 60))), day_sum(Ret), 20), 30)` |
| slot b seed 10 | 过 | 0.05 | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(de` | 0.07 | 0.00 | 0.03 | 0.00 | 0.00 | 0.03 | `cross_mean(ts_cov(day_zero_ratio(in_slice(Ret, 181, 240)), day_skew(in_slice(Ret, 181, 240)), 10), 30)` |
