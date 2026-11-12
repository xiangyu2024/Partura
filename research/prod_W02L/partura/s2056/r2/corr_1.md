# 相关度表:种子 2056,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 7 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.17 | `day_max(cross_corr(Amt, Ret, 180))` | 0.16 | 0.59 | 0.01 | 0.01 | 0.53 | 0.42 | `div(day_std(Amt), day_sum(Amt))` |
| slot a seed 1 | 过 | 0.68 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.64 | 0.21 | 0.13 | 0.01 | 0.24 | 0.04 | `cross_corr(day_std(Ret), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 90)` |
| slot a seed 2 | 过 | 0.71 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.67 | 0.26 | 0.11 | 0.02 | 0.29 | 0.02 | `cross_corr(day_sum(Volume), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 120)` |
| slot a seed 3 | 过 | 0.06 | `cross_max(day_skew(cross_corr(Vwap, Amt, 30)), 5)` | 0.09 | 0.02 | 0.01 | 0.00 | 0.01 | 0.01 | `cross_corr(cross_delay(div(day_std(Amt), day_sum(Amt)), 1), div(day_last(Close), day_first(Open)), 90)` |
| slot a seed 4 | 过 | 0.15 | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30` | 0.07 | 0.02 | 0.18 | 0.03 | 0.01 | 0.14 | `cross_corr(div(day_std(Amt), day_sum(Amt)), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 60)` |
| slot a seed 5 | 过 | 0.14 | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30` | 0.12 | 0.11 | 0.15 | 0.10 | 0.11 | 0.01 | `cross_zscore(div(day_std(Amt), day_sum(Amt)), 120)` |
| slot a seed 6 | 过 | 0.14 | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30` | 0.16 | 0.06 | 0.16 | 0.10 | 0.08 | 0.03 | `sub(div(day_std(Amt), day_sum(Amt)), cross_mean(div(day_std(Amt), day_sum(Amt)), 60))` |
| slot a seed 7 | 过 | 0.49 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.46 | 0.07 | 0.01 | 0.06 | 0.11 | 0.03 | `cross_corr(cross_delta(day_sum(Amt), 1), div(day_std(Amt), day_sum(Amt)), 60)` |
| slot a seed 8 | 过 | 0.48 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.43 | 0.23 | 0.11 | 0.00 | 0.25 | 0.04 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 5), 90)` |
| slot a seed 9 | 过 | 0.39 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.32 | 0.18 | 0.06 | 0.02 | 0.18 | 0.02 | `cross_corr(div(day_std(Amt), day_sum(Amt)), day_min(Ret), 60)` |
| slot a seed 10 | 过 | 0.65 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.59 | 0.28 | 0.09 | 0.01 | 0.31 | 0.03 | `cross_corr(day_sum(Amt), cross_mean(div(day_std(Amt), day_sum(Amt)), 5), 120)` |
| slot a seed 11 | 过 | 0.05 | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30` | 0.05 | 0.03 | 0.07 | 0.07 | 0.04 | 0.01 | `cross_delta(div(day_std(Amt), day_sum(Amt)), 20)` |
| slot a seed 12 | 过 | 0.55 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.47 | 0.21 | 0.05 | 0.02 | 0.24 | 0.01 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 240)` |
| slot b seed 1 | 过 | 0.38 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.22 | 0.70 | 0.28 | 0.07 | 0.69 | 0.24 | `cross_mean(day_corr(Amt, cross_delay(cross_mean(Amt, 20), 1)), 20)` |
| slot b seed 2 | 过 | 0.38 | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30` | 0.23 | 0.70 | 0.29 | 0.09 | 0.69 | 0.25 | `cross_mean(day_corr(Amt, cross_delay(cross_mean(Amt, 60), 1)), 20)` |
| slot b seed 3 | 过 | 0.42 | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30` | 0.24 | 0.66 | 0.31 | 0.09 | 0.67 | 0.20 | `cross_mean(day_corr(Amt, cross_delay(Amt, 1)), 20)` |
| slot b seed 4 | 过 | 0.43 | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30` | 0.25 | 0.54 | 0.34 | 0.04 | 0.56 | 0.11 | `cross_stddev(day_corr(Amt, cross_delay(cross_mean(Amt, 20), 1)), 60)` |
| slot b seed 5 | 过 | 0.26 | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30` | 0.14 | 0.04 | 0.23 | 0.07 | 0.00 | 0.22 | `cross_corr(day_sum(Amt), day_corr(Amt, cross_delay(cross_mean(Amt, 20), 1)), 60)` |
| slot b seed 6 | 过 | 0.38 | `day_max(cross_corr(Ret, Ret, 15))` | 0.23 | 0.65 | 0.29 | 0.16 | 0.65 | 0.23 | `cross_mean(day_corr(Volume, cross_delay(cross_mean(Volume, 20), 1)), 10)` |
| slot b seed 7 | 过 | 0.16 | `day_max(cross_corr(Ret, Ret, 15))` | 0.12 | 0.05 | 0.11 | 0.20 | 0.07 | 0.03 | `sub(day_corr(Amt, cross_delay(cross_mean(Amt, 20), 1)), cross_mean(day_corr(Amt, cross_delay(cross_mean(Amt, 20), 1)), 60))` |
| slot b seed 8 | 过 | 0.24 | `day_max(cross_corr(Ret, Ret, 15))` | 0.17 | 0.12 | 0.22 | 0.56 | 0.13 | 0.03 | `cross_mean(day_corr(Amt, Ret), 20)` |
| slot b seed 9 | 过 | 0.32 | `cross_min(day_max(cross_corr(Amt, Ret, 60)), 15)` | 0.31 | 0.30 | 0.18 | 0.07 | 0.32 | 0.05 | `cross_corr(day_corr(Amt, cross_delay(cross_mean(Amt, 20), 1)), div(day_last(Close), day_first(Open)), 60)` |
| slot b seed 10 | 过 | 0.29 | `day_max(cross_corr(Ret, Ret, 15))` | 0.18 | 0.14 | 0.24 | 0.53 | 0.15 | 0.02 | `cross_mean(day_corr(cross_delta(Amt, 1), Ret), 20)` |
| slot b seed 11 | 过 | 0.42 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.30 | 0.70 | 0.22 | 0.02 | 0.68 | 0.23 | `cross_mean(day_corr(Amt, cross_delay(cross_mean(Amt, 5), 1)), 40)` |
| slot b seed 12 | 过 | 0.15 | `day_max(cross_corr(Ret, Ret, 15))` | 0.12 | 0.04 | 0.10 | 0.20 | 0.06 | 0.02 | `cross_zscore(day_corr(Amt, cross_delay(cross_mean(Amt, 20), 1)), 60)` |
| R 1 variant 1 | 过 | 0.81 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.80 | 0.28 | 0.13 | 0.02 | 0.31 | 0.02 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 90)` |
| R 1 variant 2 | 过 | 0.64 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.58 | 0.24 | 0.08 | 0.02 | 0.27 | 0.01 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 150)` |
| R 1 variant 3 | 过 | 0.60 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.53 | 0.23 | 0.07 | 0.02 | 0.26 | 0.01 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 180)` |
| R 1 variant 4 | 过 | 0.55 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.47 | 0.21 | 0.05 | 0.02 | 0.24 | 0.01 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 240)` |
| R 1 variant 5 | 过 | 0.71 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.66 | 0.27 | 0.11 | 0.02 | 0.30 | 0.02 | `cross_corr(day_sum(Volume), cross_delay(div(day_std(Volume), day_sum(Volume)), 1), 120)` |
| R 1 variant 6 | 过 | 0.59 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.53 | 0.30 | 0.04 | 0.01 | 0.31 | 0.08 | `cross_corr(day_sum(Amt), div(day_std(Amt), day_sum(Amt)), 120)` |
| R 1 variant 7 | 过 | 0.67 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.62 | 0.28 | 0.07 | 0.01 | 0.31 | 0.04 | `cross_corr(day_sum(Amt), cross_mean(div(day_std(Amt), day_sum(Amt)), 3), 120)` |
| R 1 variant 8 | 过 | 0.71 | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_s` | 0.67 | 0.26 | 0.11 | 0.02 | 0.29 | 0.02 | `cross_corr(day_sum(Volume), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 120)` |
