# 相关度表:种子 2076,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 7 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 1.00 | 0.24 | 0.16 | 0.02 | 0.26 | 0.10 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30)` |
| slot a seed 1 | 过 | 0.56 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.56 | 0.06 | 0.08 | 0.06 | 0.07 | 0.01 | `cross_zscore(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 60)` |
| slot a seed 2 | 过 | 0.07 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.08 | 0.00 | 0.01 | 0.09 | 0.00 | 0.02 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 10), cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30))` |
| slot a seed 3 | 过 | 0.59 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.56 | 0.23 | 0.14 | 0.02 | 0.24 | 0.09 | `cross_ema(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 20)` |
| slot a seed 4 | 过 | 0.73 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.72 | 0.03 | 0.14 | 0.01 | 0.06 | 0.09 | `cross_tail_mean_q75(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 20)` |
| slot a seed 5 | 过 | 0.85 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.84 | 0.24 | 0.15 | 0.00 | 0.26 | 0.10 | `ts_decay_linear(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 20)` |
| slot a seed 6 | 过 | 0.99 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.99 | 0.24 | 0.16 | 0.02 | 0.26 | 0.10 | `cs_winsor(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30))` |
| slot a seed 7 | 过 | 0.90 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.91 | 0.10 | 0.18 | 0.04 | 0.13 | 0.04 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), cross_mean(ts_cov(day_zero_ratio(Amt), day_pos_ratio(Ret), 10), 30))` |
| slot a seed 8 | 过 | 0.98 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.98 | 0.23 | 0.15 | 0.02 | 0.25 | 0.10 | `mul(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), cross_mean(day_zero_ratio(Amt), 30))` |
| slot a seed 9 | 过 | 0.89 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.90 | 0.18 | 0.17 | 0.02 | 0.21 | 0.04 | `div(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), cross_stddev(day_zero_ratio(Amt), 30))` |
| slot a seed 10 | 过 | 0.60 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.59 | 0.11 | 0.09 | 0.05 | 0.12 | 0.06 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), ts_mean(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 120))` |
| slot a seed 11 | 废品 | 0.53 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.53 | 0.09 | 0.09 | 0.06 | 0.11 | 0.04 | `ts_rank(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 60)` |
| slot a seed 12 | 过 | 0.17 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.17 | 0.03 | 0.00 | 0.11 | 0.01 | 0.02 | `sub(cross_zscore(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), 20), cross_zscore(cross_mean(ts_cov(day_zero_ratio(Amt), day_pos_ratio(Ret), 10), 30), 20))` |
| slot b core | 废品 | 0.67 | `day_first(in_first(Amt))` | 0.46 | 0.73 | 0.18 | 0.15 | 0.72 | 0.55 | `day_zero_ratio(Amt)` |
| slot b seed 1 | 过 | 0.19 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.15 | 0.11 | 0.11 | 0.03 | 0.12 | 0.01 | `cross_mean(ts_corr(day_zero_ratio(Amt), day_skew(Ret), 20), 30)` |
| slot b seed 2 | 过 | 0.37 | `day_first(in_first(Amt))` | 0.23 | 0.47 | 0.12 | 0.07 | 0.44 | 0.59 | `cross_mean(ts_corr(day_zero_ratio(Amt), day_pos_ratio(Ret), 20), 30)` |
| slot b seed 3 | 过 | 0.39 | `day_first(in_first(Amt))` | 0.37 | 0.49 | 0.01 | 0.03 | 0.48 | 0.44 | `cross_mean(ts_cov(day_zero_ratio(Amt), day_std(Low), 10), 30)` |
| slot b seed 4 | 过 | 0.48 | `day_first(in_first(Amt))` | 0.34 | 0.66 | 0.08 | 0.06 | 0.62 | 0.63 | `cross_mean(ts_cov(day_zero_ratio(Amt), day_gini(Amt), 10), 30)` |
| slot b seed 5 | 过 | 0.38 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.34 | 0.15 | 0.13 | 0.00 | 0.16 | 0.05 | `cross_mean(ts_cov(day_zero_ratio(Amt), day_centroid(Amt), 10), 30)` |
| slot b seed 6 | 过 | 0.78 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.78 | 0.21 | 0.16 | 0.00 | 0.22 | 0.06 | `cross_mean(ts_corr(day_zero_ratio(Amt), sqrt(day_skew(Close)), 20), 30)` |
| slot b seed 7 | 过 | 0.20 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.16 | 0.11 | 0.11 | 0.02 | 0.13 | 0.00 | `cross_mean(ts_cov(day_zero_ratio(Amt), day_skew(Ret), 10), 30)` |
| slot b seed 8 | 过 | 0.12 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.09 | 0.11 | 0.04 | 0.02 | 0.10 | 0.12 | `sub(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(Open)), 10), 30), cross_mean(ts_cov(day_zero_ratio(in_slice(Amt, 210, 240)), sqrt(day_skew(Open)), 10), 30))` |
| slot b seed 9 | 过 | 0.28 | `sigmoid(cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew` | 0.24 | 0.11 | 0.09 | 0.02 | 0.12 | 0.04 | `cross_mean(ts_cov(day_zero_ratio(Amt), sqrt(day_skew(in_slice(Open, 0, 60))), 10), 30)` |
| slot b seed 10 | 废品 | 0.62 | `day_first(in_first(Amt))` | 0.44 | 0.85 | 0.11 | 0.03 | 0.82 | 0.67 | `cross_mean(sub(day_zero_ratio(Amt), day_zero_ratio(in_slice(Amt, 0, 30))), 30)` |
| slot b seed 11 | 过 | 0.03 | `day_first(in_first(Amt))` | 0.04 | 0.02 | 0.04 | 0.01 | 0.03 | 0.01 | `cross_zscore(ts_corr(day_zero_ratio(Amt), day_skew(Ret), 20), 40)` |
| slot b seed 12 | 过 | 0.34 | `day_first(in_first(Amt))` | 0.25 | 0.46 | 0.01 | 0.01 | 0.43 | 0.46 | `cross_mean(ts_cov(day_zero_ratio(Amt), day_es_ratio_hi(Close), 10), 30)` |
