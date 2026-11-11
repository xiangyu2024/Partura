# 相关度表:种子 2050,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.18 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.05 | 0.47 | 0.06 | 0.03 | 0.43 | 0.44 | `day_sum(Open)` |
| slot a seed 1 | 过 | 0.36 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.19 | 0.24 | 0.44 | 0.56 | 0.27 | 0.08 | `div(day_sum(Open), cross_mean(day_sum(Open), 120))` |
| slot a seed 2 | 过 | 0.10 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.08 | 0.11 | 0.21 | 0.40 | 0.13 | 0.14 | `div(day_sum(Open), cross_max(day_sum(Open), 250))` |
| slot a seed 3 | 过 | 0.16 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.04 | 0.30 | 0.31 | 0.07 | 0.30 | 0.13 | `div(cross_delay(day_sum(Open), 20), cross_delay(day_sum(Open), 240))` |
| slot a seed 4 | 过 | 0.31 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.17 | 0.23 | 0.44 | 0.23 | 0.25 | 0.03 | `sub(cross_mean(day_sum(Open), 20), cross_mean(day_sum(Open), 120))` |
| slot a seed 5 | 过 | 0.39 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.20 | 0.24 | 0.44 | 0.61 | 0.27 | 0.07 | `cross_zscore(day_sum(Open), 120)` |
| slot a seed 6 | 过 | 0.19 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.02 | 0.02 | 0.12 | 0.00 | 0.03 | 0.27 | `cs_bucket_demean(day_sum(Open), LogFloatCap)` |
| slot a seed 7 | 过 | 0.38 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.14 | 0.20 | 0.45 | 0.39 | 0.23 | 0.07 | `cs_bucket_demean(div(day_sum(Open), cross_mean(day_sum(Open), 240)), LogFloatCap)` |
| slot a seed 8 | 过 | 0.33 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.26 | 0.14 | 0.18 | 0.12 | 0.16 | 0.15 | `cross_corr(day_sum(Open), day_sum(Amt), 60)` |
| slot a seed 9 | 过 | 0.35 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.18 | 0.23 | 0.41 | 0.46 | 0.26 | 0.06 | `div(cross_delta(day_sum(Open), 60), cross_mean(day_sum(Open), 60))` |
| slot a seed 10 | 过 | 0.22 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.15 | 0.03 | 0.31 | 0.28 | 0.01 | 0.13 | `cs_bucket_zscore(div(day_sum(Open), cross_delay(day_sum(Open), 120)), cross_mean(day_sum(Amt), 20))` |
| slot a seed 11 | 过 | 0.21 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.06 | 0.36 | 0.36 | 0.06 | 0.37 | 0.17 | `div(cross_ema(day_sum(Open), 20), cross_ema(day_sum(Open), 250))` |
| slot a seed 12 | 过 | 0.61 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.29 | 0.50 | 0.63 | 0.02 | 0.52 | 0.04 | `cross_stddev(div(day_sum(Open), cross_delay(day_sum(Open), 1)), 60)` |
| slot b seed 1 | 过 | 0.23 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.27 | 0.25 | 0.07 | 0.13 | 0.24 | 0.03 | `cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 60)` |
| slot b seed 2 | 过 | 0.40 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.39 | 0.37 | 0.45 | 0.35 | 0.39 | 0.07 | `cross_mean(div(day_last(Close), day_first(Open)), 60)` |
| slot b seed 3 | 过 | 0.34 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.39 | 0.38 | 0.36 | 0.21 | 0.39 | 0.07 | `sub(cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 60), cross_mean(div(day_last(Close), day_first(Open)), 60))` |
| slot b seed 4 | 过 | 0.04 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.12 | 0.02 | 0.04 | 0.04 | 0.03 | 0.02 | `cross_zscore(div(day_first(Open), cross_delay(day_last(Close), 1)), 60)` |
| slot b seed 5 | 过 | 0.06 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.07 | 0.20 | 0.02 | 0.00 | 0.19 | 0.13 | `cross_corr(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open)), 60)` |
| slot b seed 6 | 过 | 0.08 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.07 | 0.18 | 0.03 | 0.01 | 0.16 | 0.12 | `cross_regbeta(div(day_last(Close), day_first(Open)), div(day_first(Open), cross_delay(day_last(Close), 1)), 60)` |
| slot b seed 7 | 过 | 0.54 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.25 | 0.42 | 0.52 | 0.02 | 0.45 | 0.07 | `cross_stddev(div(day_first(Open), cross_delay(day_last(Close), 1)), 60)` |
| slot b seed 8 | 过 | 0.18 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.25 | 0.26 | 0.10 | 0.14 | 0.25 | 0.05 | `cs_bucket_demean(cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 40), LogFloatCap)` |
| slot b seed 9 | 过 | 0.09 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.06 | 0.10 | 0.11 | 0.03 | 0.10 | 0.06 | `sub(cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 10), cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 120))` |
| slot b seed 10 | 过 | 0.35 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.28 | 0.23 | 0.29 | 0.59 | 0.24 | 0.06 | `cross_mean(sub(div(day_first(Open), cross_delay(day_last(Close), 1)), div(day_last(Close), day_first(Open))), 20)` |
| slot b seed 11 | 过 | 0.23 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.26 | 0.21 | 0.04 | 0.10 | 0.21 | 0.01 | `cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 120)` |
| slot b seed 12 | 过 | 0.28 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.27 | 0.00 | 0.00 | 0.15 | 0.00 | 0.14 | `cs_bucket_zscore(cross_mean(div(day_first(Open), cross_delay(day_last(Close), 1)), 60), cross_mean(day_sum(Amt), 20))` |
| R 1 variant 1 | 过 | 0.90 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.87 | 0.25 | 0.15 | 0.04 | 0.21 | 0.60 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 160)` |
| R 1 variant 2 | 过 | 0.84 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.77 | 0.29 | 0.14 | 0.03 | 0.25 | 0.64 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 240)` |
| R 1 variant 3 | 过 | 0.94 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(R` | 0.94 | 0.21 | 0.16 | 0.05 | 0.17 | 0.57 | `cross_mean(div(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), day_std(Ret)), 120)` |
| R 1 variant 4 | 过 | 0.40 | `cross_stddev(day_std(select_where(is_gt(Ret, create_like(Ret` | 0.15 | 0.22 | 0.73 | 0.03 | 0.25 | 0.17 | `cross_mean(day_std(select_where(is_gt(Ret, create_like(Ret, 0), False), Ret, create_like(Ret, 0))), 160)` |
