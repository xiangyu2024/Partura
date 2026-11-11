# 相关度表:种子 2056,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `day_max(cross_corr(Amt, Ret, 60))` | 1.00 | 0.09 | 0.03 | 0.06 | 0.05 | 0.35 | `day_max(cross_corr(Amt, Ret, 60))` |
| slot a seed 1 | 过 | 0.97 | `day_max(cross_corr(Amt, Ret, 60))` | 0.96 | 0.16 | 0.05 | 0.00 | 0.12 | 0.39 | `sub(day_max(cross_corr(Amt, Ret, 60)), day_mean(cross_corr(Amt, Ret, 60)))` |
| slot a seed 2 | 过 | 0.26 | `day_max(cross_corr(Amt, Ret, 60))` | 0.40 | 0.14 | 0.08 | 0.02 | 0.15 | 0.07 | `div(day_max(cross_corr(Amt, Ret, 60)), day_std(cross_corr(Amt, Ret, 60)))` |
| slot a seed 3 | 过 | 0.96 | `day_max(cross_corr(Amt, Ret, 60))` | 0.96 | 0.16 | 0.06 | 0.00 | 0.12 | 0.39 | `sub(day_max(cross_corr(Amt, Ret, 60)), day_median(cross_corr(Amt, Ret, 60)))` |
| slot a seed 4 | 过 | 0.33 | `day_max(cross_corr(Amt, Ret, 60))` | 0.29 | 0.01 | 0.01 | 0.09 | 0.02 | 0.02 | `cross_delta(day_max(cross_corr(Amt, Ret, 60)), 20)` |
| slot a seed 5 | 过 | 0.52 | `day_max(cross_corr(Amt, Ret, 60))` | 0.50 | 0.06 | 0.05 | 0.08 | 0.07 | 0.01 | `sub(day_max(cross_corr(Amt, Ret, 60)), cross_mean(day_max(cross_corr(Amt, Ret, 60)), 60))` |
| slot a seed 6 | 过 | 0.59 | `day_max(cross_corr(Amt, Ret, 60))` | 0.60 | 0.08 | 0.05 | 0.07 | 0.10 | 0.02 | `cross_zscore(day_max(cross_corr(Amt, Ret, 60)), 120)` |
| slot a seed 7 | 过 | 0.99 | `day_max(cross_corr(Amt, Ret, 60))` | 1.00 | 0.04 | 0.04 | 0.07 | 0.00 | 0.32 | `cs_regres(day_max(cross_corr(Amt, Ret, 60)), day_sum(Amt))` |
| slot a seed 8 | 过 | 1.00 | `day_max(cross_corr(Amt, Ret, 60))` | 1.00 | 0.09 | 0.02 | 0.05 | 0.05 | 0.35 | `cs_regres(day_max(cross_corr(Amt, Ret, 60)), day_std(Ret))` |
| slot a seed 9 | 过 | 0.17 | `day_max(cross_corr(Amt, Ret, 60))` | 0.15 | 0.10 | 0.09 | 0.01 | 0.09 | 0.04 | `sub(day_max(cross_corr(Amt, Ret, 60)), day_max(in_slice(cross_corr(Amt, Ret, 60), 181, 240)))` |
| slot a seed 10 | 过 | 0.27 | `day_max(cross_corr(Amt, Ret, 60))` | 0.30 | 0.05 | 0.03 | 0.04 | 0.04 | 0.01 | `sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60)))` |
| slot a seed 11 | 过 | 0.19 | `day_max(cross_corr(Ret, Ret, 15))` | 0.08 | 0.03 | 0.17 | 0.64 | 0.04 | 0.03 | `mul(day_max(cross_corr(Amt, Ret, 60)), sign(cross_delta(day_sum(Close), 20)))` |
| slot a seed 12 | 过 | 0.87 | `day_max(cross_corr(Amt, Ret, 60))` | 0.82 | 0.10 | 0.03 | 0.03 | 0.06 | 0.40 | `sub(day_max(cross_corr(Amt, Ret, 60)), day_min(cross_corr(Amt, Ret, 60)))` |
| slot a seed 13 | 过 | 0.08 | `day_max(cross_corr(Amt, Ret, 60))` | 0.05 | 0.01 | 0.06 | 0.04 | 0.02 | 0.02 | `cross_corr(day_max(cross_corr(Amt, Ret, 60)), day_sum(Amt), 60)` |
| slot a seed 14 | 过 | 0.33 | `day_max(cross_corr(Amt, Ret, 60))` | 0.29 | 0.01 | 0.01 | 0.09 | 0.02 | 0.02 | `sub(day_max(cross_corr(Amt, Ret, 60)), cross_delay(day_max(cross_corr(Amt, Ret, 60)), 20))` |
| slot b seed 1 | 过 | 0.14 | `day_max(cross_corr(Amt, Ret, 60))` | 0.19 | 0.10 | 0.13 | 0.15 | 0.10 | 0.03 | `cross_corr(day_sum(Amt), div(day_last(Close), day_first(Open)), 60)` |
| slot b seed 2 | 过 | 0.09 | `day_max(cross_corr(Ret, Ret, 15))` | 0.11 | 0.08 | 0.10 | 0.09 | 0.07 | 0.02 | `cross_corr(day_sum(Amt), div(day_last(Close), day_first(Open)), 120)` |
| slot b seed 3 | 过 | 0.42 | `day_max(cross_corr(Amt, Ret, 60))` | 0.34 | 0.24 | 0.22 | 0.06 | 0.28 | 0.09 | `cross_corr(day_sum(Amt), day_min(Ret), 60)` |
| slot b seed 4 | 过 | 0.37 | `day_max(cross_corr(Amt, Ret, 60))` | 0.26 | 0.18 | 0.15 | 0.02 | 0.21 | 0.14 | `cross_corr(day_sum(Amt), day_min(Ret), 120)` |
| slot b seed 5 | 过 | 0.35 | `day_max(cross_corr(Amt, Ret, 60))` | 0.28 | 0.15 | 0.12 | 0.06 | 0.17 | 0.08 | `cross_corr(day_sum(Amt), day_max(Ret), 90)` |
| slot b seed 6 | 过 | 0.38 | `day_max(cross_corr(Amt, Ret, 60))` | 0.31 | 0.27 | 0.18 | 0.05 | 0.28 | 0.09 | `cross_corr(day_sum(Amt), day_std(Ret), 90)` |
| slot b seed 7 | 过 | 0.25 | `day_max(cross_corr(Amt, Ret, 60))` | 0.22 | 0.21 | 0.20 | 0.07 | 0.23 | 0.01 | `cross_corr(day_sum(Amt), sub(day_max(High), day_min(Low)), 60)` |
| slot b seed 8 | 过 | 0.42 | `day_max(cross_corr(Amt, Ret, 60))` | 0.34 | 0.22 | 0.16 | 0.05 | 0.24 | 0.10 | `cross_corr(day_std(Amt), day_min(Ret), 60)` |
| slot b seed 9 | 过 | 0.41 | `day_max(cross_corr(Amt, Ret, 60))` | 0.32 | 0.20 | 0.17 | 0.05 | 0.23 | 0.11 | `sub(cross_corr(day_sum(Amt), day_max(Ret), 90), cross_corr(day_sum(Amt), day_min(Ret), 90))` |
| slot b seed 10 | 过 | 0.14 | `day_max(cross_corr(Amt, Ret, 60))` | 0.16 | 0.15 | 0.02 | 0.08 | 0.13 | 0.02 | `cross_corr(day_sum(Amt), day_skew(Ret), 90)` |
| slot b seed 11 | 过 | 0.29 | `cross_min(day_max(cross_corr(Amt, Ret, 60)), 15)` | 0.26 | 0.13 | 0.22 | 0.11 | 0.14 | 0.09 | `cross_corr(day_sum(Amt), cross_delay(div(day_last(Close), day_first(Open)), 1), 60)` |
| slot b seed 12 | 过 | 0.39 | `day_max(cross_corr(Amt, Ret, 60))` | 0.27 | 0.18 | 0.15 | 0.02 | 0.21 | 0.15 | `cross_corr(day_sum(Volume), day_min(Ret), 120)` |
| R 1 variant 1 | 过 | 0.72 | `day_max(cross_corr(Amt, Ret, 60))` | 0.65 | 0.15 | 0.03 | 0.04 | 0.12 | 0.40 | `day_max(cross_corr(Amt, Ret, 120))` |
| R 1 variant 2 | 过 | 0.62 | `day_max(cross_corr(Amt, Ret, 60))` | 0.50 | 0.20 | 0.04 | 0.03 | 0.16 | 0.42 | `day_max(cross_corr(Amt, Ret, 180))` |
| R 1 variant 3 | 过 | 0.56 | `day_max(cross_corr(Amt, Ret, 60))` | 0.41 | 0.22 | 0.04 | 0.03 | 0.19 | 0.45 | `day_max(cross_corr(Amt, Ret, 240))` |
| R 1 variant 4 | 过 | 0.42 | `cross_min(day_max(cross_corr(Amt, Ret, 60)), 15)` | 0.37 | 0.22 | 0.18 | 0.08 | 0.23 | 0.17 | `day_quantile_q75(cross_corr(Amt, Ret, 120))` |
| R 1 variant 5 | 过 | 0.25 | `day_max(cross_corr(Ret, Ret, 15))` | 0.22 | 0.29 | 0.20 | 0.12 | 0.28 | 0.14 | `day_mean(cross_corr(Amt, Ret, 120))` |
| R 1 variant 6 | 过 | 0.68 | `day_max(cross_corr(Amt, Ret, 60))` | 0.58 | 0.09 | 0.00 | 0.02 | 0.06 | 0.46 | `day_std(cross_corr(Amt, Ret, 120))` |
| R 1 variant 7 | 过 | 0.72 | `day_max(cross_corr(Amt, Ret, 60))` | 0.65 | 0.15 | 0.02 | 0.04 | 0.12 | 0.39 | `day_max(cross_corr(Volume, Ret, 120))` |
| R 1 variant 8 | 过 | 0.82 | `day_max(cross_corr(Amt, Ret, 60))` | 0.80 | 0.12 | 0.01 | 0.04 | 0.09 | 0.38 | `day_max(cross_corr(Amt, Ret, 90))` |
