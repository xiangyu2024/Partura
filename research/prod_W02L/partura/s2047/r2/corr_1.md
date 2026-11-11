# 相关度表:种子 2047,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.11 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.23 | 0.00 | 0.01 | 0.18 | 0.00 | 0.04 | `day_sum(Ret)` |
| slot a seed 1 | 过 | 0.21 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.11 | 0.36 | 0.35 | 0.10 | 0.38 | 0.05 | `sub(cross_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120), cross_mean(day_sum(Ret), 120))` |
| slot a seed 2 | 过 | 0.26 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.13 | 0.37 | 0.46 | 0.19 | 0.40 | 0.06 | `cross_mean(day_sum(Ret), 120)` |
| slot a seed 3 | 过 | 0.20 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.11 | 0.03 | 0.21 | 0.02 | 0.02 | 0.28 | `cross_regbeta(cs_mean(day_sum(Ret)), day_sum(Ret), 120)` |
| slot a seed 4 | 过 | 0.22 | `add(day_min(Ret), day_var(Open))` | 0.29 | 0.35 | 0.25 | 0.02 | 0.36 | 0.22 | `cross_corr(day_sum(Ret), cs_mean(day_sum(Ret)), 120)` |
| slot a seed 5 | 过 | 0.07 | `add(day_min(Ret), day_var(Open))` | 0.05 | 0.03 | 0.01 | 0.01 | 0.01 | 0.03 | `cross_autocorr(day_sum(Ret), 120, 1)` |
| slot a seed 6 | 过 | 0.09 | `add(day_min(Ret), day_var(Open))` | 0.09 | 0.21 | 0.05 | 0.01 | 0.20 | 0.15 | `cross_corr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), day_sum(Ret), 120)` |
| slot a seed 7 | 过 | 0.07 | `add(day_min(Ret), day_var(Open))` | 0.10 | 0.23 | 0.04 | 0.01 | 0.22 | 0.14 | `cross_regbeta(log(div(day_first(Open), cross_delay(day_last(Close), 1))), day_sum(Ret), 120)` |
| slot a seed 8 | 过 | 0.35 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.49 | 0.30 | 0.43 | 0.12 | 0.29 | 0.16 | `cross_tail_mean_q25(day_sum(Ret), 120)` |
| slot a seed 9 | 过 | 0.24 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.14 | 0.36 | 0.43 | 0.22 | 0.38 | 0.09 | `div(cross_mean(day_sum(Ret), 120), cross_stddev(day_sum(Ret), 120))` |
| slot a seed 10 | 过 | 0.04 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.04 | 0.01 | 0.03 | 0.00 | 0.01 | 0.03 | `sub(cross_semistd_neg(day_sum(Ret), 120), cross_semistd_pos(day_sum(Ret), 120))` |
| slot a seed 11 | 过 | 0.21 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.16 | 0.12 | 0.17 | 0.12 | 0.12 | 0.04 | `cross_corr(day_sum(Ret), cross_zscore(day_sum(Volume), 60), 120)` |
| slot a seed 12 | 过 | 0.21 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.09 | 0.37 | 0.39 | 0.21 | 0.39 | 0.06 | `sub(cross_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 60), cross_mean(day_sum(Ret), 60))` |
| slot b seed 1 | 过 | 0.43 | `add(day_min(Ret), day_var(Open))` | 0.46 | 0.32 | 0.04 | 0.07 | 0.27 | 0.01 | `cross_mean(day_ar1_coefficient(Ret), 120)` |
| slot b seed 2 | 过 | 0.09 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.12 | 0.03 | 0.24 | 0.13 | 0.07 | 0.02 | `cross_mean(day_argmin(Low), 120)` |
| slot b seed 3 | 过 | 0.08 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.06 | 0.07 | 0.15 | 0.16 | 0.09 | 0.04 | `sub(cross_mean(day_argmin(Low), 120), cross_mean(day_argmax(High), 120))` |
| slot b seed 4 | 过 | 0.27 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.13 | 0.46 | 0.36 | 0.02 | 0.48 | 0.04 | `cross_mean(day_centroid(Amt), 120)` |
| slot b seed 5 | 过 | 0.11 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.11 | 0.13 | 0.18 | 0.01 | 0.14 | 0.10 | `cross_corr(day_centroid(Amt), day_sum(Ret), 120)` |
| slot b seed 6 | 废品 | 0.44 | `add(day_min(Ret), day_var(Open))` | 0.41 | 0.19 | 0.00 | 0.04 | 0.12 | 0.02 | `cross_mean(day_at_min_ratio(Low), 120)` |
| slot b seed 7 | 过 | 0.50 | `add(day_min(Ret), day_var(Open))` | 0.36 | 0.42 | 0.10 | 0.07 | 0.35 | 0.23 | `cross_mean(day_ar1_coefficient(Close), 120)` |
| slot b seed 8 | 过 | 0.10 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.05 | 0.16 | 0.17 | 0.07 | 0.17 | 0.27 | `cross_stddev(day_argmin(Low), 120)` |
| slot b seed 9 | 过 | 0.47 | `add(day_min(Ret), day_var(Open))` | 0.13 | 0.74 | 0.15 | 0.07 | 0.66 | 0.63 | `cross_mean(day_gini(Amt), 120)` |
| slot b seed 10 | 过 | 0.20 | `sqrt(sigmoid(day_min(Ret)))` | 0.03 | 0.04 | 0.15 | 0.26 | 0.06 | 0.02 | `cross_zscore(cross_mean(day_centroid(Amt), 5), 120)` |
| slot b seed 11 | 过 | 0.11 | `add(day_min(Ret), day_var(Open))` | 0.14 | 0.10 | 0.08 | 0.01 | 0.09 | 0.01 | `cross_corr(day_argmin(Low), day_min(Ret), 120)` |
| slot b seed 12 | 过 | 0.21 | `sqrt(sigmoid(day_min(Ret)))` | 0.14 | 0.15 | 0.20 | 0.25 | 0.16 | 0.04 | `cross_zscore(cross_mean(day_ar1_coefficient(Ret), 5), 120)` |
| R 1 variant 1 | 过 | 0.81 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.83 | 0.14 | 0.19 | 0.12 | 0.16 | 0.14 | `cross_corr(day_min(High), day_mean(Amt), 45)` |
| R 1 variant 2 | 过 | 0.73 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.72 | 0.12 | 0.16 | 0.06 | 0.14 | 0.15 | `cross_corr(day_min(High), day_mean(Amt), 90)` |
| R 1 variant 3 | 过 | 0.75 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.74 | 0.01 | 0.05 | 0.11 | 0.02 | 0.13 | `cross_corr(day_min(High), cross_zscore(day_mean(Amt), 60), 60)` |
| R 1 variant 4 | 过 | 0.95 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.95 | 0.15 | 0.18 | 0.12 | 0.16 | 0.10 | `cross_corr(day_min(High), cross_delay(day_mean(Amt), 1), 60)` |
| R 1 variant 5 | 过 | 0.40 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.30 | 0.12 | 0.10 | 0.01 | 0.14 | 0.11 | `cross_corr(day_min(High), day_mean(Amt), 241)` |
| R 1 variant 6 | 过 | 0.95 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.95 | 0.12 | 0.17 | 0.11 | 0.15 | 0.17 | `cross_corr(day_max(Low), day_mean(Amt), 60)` |
| R 1 variant 7 | 过 | 0.91 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.89 | 0.15 | 0.17 | 0.09 | 0.18 | 0.11 | `cross_corr(day_min(High), cs_rank(day_mean(Amt)), 60)` |
