# 相关度表:种子 2047,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.47 | `sqrt(sigmoid(day_min(Ret)))` | 0.94 | 0.14 | 0.54 | 0.21 | 0.17 | 0.12 | `cross_delay(day_min(Ret), 1)` |
| slot a seed 1 | 过 | 0.20 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.10 | 0.19 | 0.17 | 0.08 | 0.21 | 0.14 | `cross_mean(mul(cross_delay(day_min(Ret), 1), log(div(day_first(Open), cross_delay(day_last(Close), 1)))), 120)` |
| slot a seed 2 | 过 | 0.23 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.12 | 0.04 | 0.18 | 0.02 | 0.07 | 0.26 | `cross_cov(cross_delay(day_min(Ret), 1), log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120)` |
| slot a seed 3 | 过 | 0.20 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.12 | 0.03 | 0.08 | 0.01 | 0.01 | 0.24 | `cross_corr(cross_delay(day_min(Ret), 1), log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120)` |
| slot a seed 4 | 过 | 0.28 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.19 | 0.14 | 0.06 | 0.00 | 0.15 | 0.06 | `cross_corr(cross_delay(day_min(Ret), 1), day_max(Ret), 120)` |
| slot a seed 5 | 过 | 0.32 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.22 | 0.20 | 0.06 | 0.01 | 0.20 | 0.07 | `cross_corr(cross_delay(day_min(Ret), 1), day_std(Ret), 120)` |
| slot a seed 6 | 过 | 0.31 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.24 | 0.11 | 0.08 | 0.03 | 0.13 | 0.05 | `cross_corr(cross_delay(day_min(Ret), 1), cross_zscore(day_sum(Volume), 60), 120)` |
| slot a seed 7 | 过 | 0.31 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.24 | 0.16 | 0.10 | 0.01 | 0.17 | 0.09 | `cross_corr(cross_delay(day_min(Ret), 1), day_min(Ret), 120)` |
| slot a seed 8 | 过 | 0.31 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.24 | 0.16 | 0.10 | 0.01 | 0.17 | 0.07 | `cross_regbeta(cross_delay(day_min(Ret), 1), day_min(Ret), 120)` |
| slot a seed 9 | 过 | 0.03 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.04 | 0.02 | 0.04 | 0.01 | 0.03 | 0.01 | `cross_corr(cross_delay(day_min(Ret), 1), div(day_sum(Ret), cross_mean(day_std(Ret), 20)), 120)` |
| slot a seed 10 | 过 | 0.05 | `add(day_min(Ret), day_var(Open))` | 0.07 | 0.03 | 0.04 | 0.01 | 0.03 | 0.02 | `cross_corr(cross_delay(day_min(Ret), 1), day_argmin(Low), 120)` |
| slot a seed 11 | 过 | 0.26 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.17 | 0.06 | 0.09 | 0.02 | 0.08 | 0.14 | `cross_corr(cross_delay(day_min(Ret), 1), day_centroid(Amt), 120)` |
| slot a seed 12 | 过 | 0.02 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.42 | 0.08 | 0.14 | 0.13 | 0.09 | 0.04 | `sub(cross_delay(day_min(Ret), 1), cross_mean(day_min(Ret), 20))` |
| slot b seed 1 | 过 | 0.11 | `sqrt(sigmoid(day_min(Ret)))` | 0.15 | 0.10 | 0.15 | 0.00 | 0.12 | 0.01 | `cross_corr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), cross_delay(day_sum(Ret), 1), 120)` |
| slot b seed 2 | 过 | 0.11 | `sqrt(sigmoid(day_min(Ret)))` | 0.15 | 0.10 | 0.16 | 0.00 | 0.12 | 0.00 | `cross_regbeta(cross_delay(day_sum(Ret), 1), log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120)` |
| slot b seed 3 | 过 | 0.10 | `sqrt(sigmoid(day_min(Ret)))` | 0.14 | 0.11 | 0.12 | 0.02 | 0.13 | 0.07 | `cross_corr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), cross_delay(log(div(day_last(Close), day_min(Low))), 1), 120)` |
| slot b seed 4 | 过 | 0.13 | `add(day_min(Ret), day_var(Open))` | 0.10 | 0.12 | 0.05 | 0.01 | 0.12 | 0.19 | `cross_corr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), cross_delay(day_max(Ret), 1), 120)` |
| slot b seed 5 | 过 | 0.26 | `sigmoid(pow_2(sigmoid(day_min(Ret))))` | 0.28 | 0.43 | 0.40 | 0.07 | 0.44 | 0.06 | `cross_tail_mean_q25(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120)` |
| slot b seed 6 | 过 | 0.06 | `add(day_min(Ret), day_var(Open))` | 0.07 | 0.18 | 0.03 | 0.09 | 0.16 | 0.09 | `div(cross_tail_mean_q25(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120), cross_stddev(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120))` |
| slot b seed 7 | 过 | 0.09 | `sqrt(sqrt(sigmoid(day_min(Ret))))` | 0.09 | 0.01 | 0.13 | 0.00 | 0.03 | 0.09 | `cross_autocorr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120, 1)` |
| slot b seed 8 | 过 | 0.17 | `add(day_min(Ret), day_var(Open))` | 0.12 | 0.11 | 0.03 | 0.01 | 0.10 | 0.21 | `cross_corr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), cross_delay(cross_zscore(day_sum(Amt), 60), 1), 120)` |
| slot b seed 9 | 过 | 0.07 | `add(day_min(Ret), day_var(Open))` | 0.09 | 0.11 | 0.11 | 0.02 | 0.12 | 0.13 | `cross_corr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), cross_delay(day_centroid(Amt), 1), 120)` |
| slot b seed 10 | 过 | 0.08 | `sqrt(sigmoid(day_min(Ret)))` | 0.09 | 0.06 | 0.12 | 0.01 | 0.08 | 0.02 | `cross_corr(log(div(day_first(Open), cross_delay(day_last(Close), 1))), cross_delay(day_argmin(Low), 1), 120)` |
| slot b seed 11 | 过 | 0.09 | `sqrt(sigmoid(day_min(Ret)))` | 0.13 | 0.13 | 0.14 | 0.00 | 0.16 | 0.05 | `cross_regbeta(cross_delay(sub(day_sum(Ret), cs_mean(day_sum(Ret))), 1), log(div(day_first(Open), cross_delay(day_last(Close), 1))), 120)` |
| slot b seed 12 | 过 | 0.12 | `sqrt(sigmoid(day_min(Ret)))` | 0.17 | 0.12 | 0.16 | 0.02 | 0.14 | 0.03 | `cross_corr(sub(log(div(day_first(Open), cross_delay(day_last(Close), 1))), cs_mean(log(div(day_first(Open), cross_delay(day_last(Close), 1))))), cross_delay(day_sum(Ret), 1), 60)` |
| R 1 variant 1 | 过 | 0.65 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.64 | 0.15 | 0.20 | 0.13 | 0.17 | 0.13 | `cross_corr(day_min(High), day_mean(Amt), 35)` |
| R 1 variant 2 | 过 | 0.73 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.73 | 0.14 | 0.20 | 0.13 | 0.17 | 0.14 | `cross_corr(day_min(High), day_mean(Amt), 40)` |
| R 1 variant 3 | 过 | 0.89 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.91 | 0.13 | 0.19 | 0.12 | 0.16 | 0.14 | `cross_corr(day_min(High), day_mean(Amt), 50)` |
| R 1 variant 4 | 过 | 0.86 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.87 | 0.12 | 0.17 | 0.08 | 0.14 | 0.14 | `cross_corr(day_min(High), day_mean(Amt), 75)` |
| R 1 variant 5 | 过 | 0.81 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.83 | 0.14 | 0.19 | 0.12 | 0.16 | 0.14 | `cross_corr(day_min(Close), day_mean(Amt), 45)` |
| R 1 variant 6 | 过 | 0.68 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.67 | 0.11 | 0.15 | 0.10 | 0.13 | 0.13 | `cross_corr(day_min(High), day_max(Amt), 45)` |
| R 1 variant 7 | 过 | 0.74 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.75 | 0.10 | 0.16 | 0.11 | 0.12 | 0.14 | `cross_corr(day_min(High), day_std(Amt), 45)` |
| R 1 variant 8 | 过 | 0.78 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.80 | 0.08 | 0.14 | 0.13 | 0.11 | 0.17 | `cross_corr(day_min(High), day_mean(Volume), 45)` |
| R 1 variant 9 | 过 | 0.80 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.81 | 0.12 | 0.18 | 0.11 | 0.15 | 0.15 | `cross_corr(day_min(High), log(day_mean(Amt)), 45)` |
| R 1 variant 10 | 过 | 0.80 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.81 | 0.13 | 0.18 | 0.11 | 0.15 | 0.15 | `cross_corr(log(day_min(High)), log(day_mean(Amt)), 45)` |
| R 1 variant 11 | 过 | 0.76 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.76 | 0.12 | 0.18 | 0.13 | 0.15 | 0.18 | `cross_corr(day_max(High), day_mean(Amt), 45)` |
| R 1 variant 12 | 过 | 0.77 | `cross_corr(day_min(High), day_mean(Amt), 60)` | 0.78 | 0.15 | 0.21 | 0.14 | 0.18 | 0.14 | `cross_corr(day_last(Close), day_mean(Amt), 45)` |
