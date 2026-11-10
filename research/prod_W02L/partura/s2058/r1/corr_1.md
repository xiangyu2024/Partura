# 相关度表:种子 2058,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.84 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.90 | 0.17 | 0.66 | 0.30 | 0.21 | 0.10 | `day_std(pow_2(Ret))` |
| slot a seed 1 | 过 | 0.39 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.33 | 0.28 | 0.68 | 0.01 | 0.31 | 0.14 | `cross_ema(div(day_std(pow_2(Ret)), pow_2(replace_small_with_nan(day_var(Ret)))), 60)` |
| slot a seed 2 | 过 | 0.34 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.28 | 0.27 | 0.62 | 0.01 | 0.29 | 0.15 | `cross_ema(div(day_std(pow_2(Ret)), pow_2(replace_small_with_nan(day_var(Ret)))), 120)` |
| slot a seed 3 | 过 | 0.36 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.26 | 0.26 | 0.63 | 0.01 | 0.29 | 0.13 | `cross_mean(cs_winsor(div(day_std(pow_2(Ret)), pow_2(replace_small_with_nan(day_var(Ret))))), 241)` |
| slot a seed 4 | 过 | 0.61 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.33 | 0.34 | 0.75 | 0.03 | 0.35 | 0.02 | `cross_ema(cs_bucket_rank(day_std(pow_2(Ret)), LogFloatCap), 60)` |
| slot a seed 5 | 过 | 0.44 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.23 | 0.22 | 0.70 | 0.02 | 0.26 | 0.03 | `cross_ema(cs_bucket_rank(div(day_std(pow_2(Ret)), pow_2(replace_small_with_nan(day_var(Ret)))), LogFloatCap), 120)` |
| slot a seed 6 | 过 | 0.55 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.31 | 0.23 | 0.62 | 0.00 | 0.19 | 0.52 | `cross_ema(cs_bucket_rank(day_std(pow_2(Ret)), day_sum(Amt)), 120)` |
| slot a seed 7 | 过 | 0.37 | `cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 3)` | 0.07 | 0.18 | 0.31 | 0.40 | 0.22 | 0.23 | `sub(cross_ema(day_std(pow_2(Ret)), 5), cross_ema(day_std(pow_2(Ret)), 120))` |
| slot a seed 8 | 过 | 0.58 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.30 | 0.17 | 0.69 | 0.04 | 0.20 | 0.23 | `cross_ema(cs_demean(log(add(day_std(pow_2(Ret)), 0.000000001))), 120)` |
| slot a seed 9 | 过 | 0.23 | `cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 3)` | 0.09 | 0.05 | 0.08 | 0.35 | 0.03 | 0.01 | `cross_zscore(div(day_std(pow_2(Ret)), pow_2(replace_small_with_nan(day_var(Ret)))), 60)` |
| slot a seed 10 | 过 | 0.37 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.49 | 0.27 | 0.71 | 0.11 | 0.30 | 0.14 | `cross_max(div(day_std(pow_2(Ret)), pow_2(replace_small_with_nan(day_var(Ret)))), 20)` |
| slot a seed 11 | 过 | 0.52 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.28 | 0.19 | 0.61 | 0.05 | 0.21 | 0.14 | `cross_ema(cs_bucket_rank(day_std(pow_2(Ret)), LogTotalCap), 241)` |
| slot a seed 12 | 过 | 0.52 | `day_std(pow_2(Volume))` | 0.51 | 0.30 | 0.41 | 0.02 | 0.32 | 0.37 | `cross_ema(sub(cs_rank(day_std(pow_2(Ret))), cs_rank(day_var(Ret))), 60)` |
| slot b seed 1 | 过 | 0.46 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.08 | 0.33 | 0.50 | 0.48 | 0.36 | 0.12 | `cross_ema(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), 60)` |
| slot b seed 2 | 废品 | 0.25 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.08 | 0.33 | 0.31 | 0.03 | 0.35 | 0.06 | `cross_mean(is_gt(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.8), 120)` |
| slot b seed 3 | 废品 | 0.19 | `day_std(pow_2(Volume))` | 0.05 | 0.24 | 0.14 | 0.04 | 0.26 | 0.06 | `cross_mean(is_lt(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), -0.8), 120)` |
| slot b seed 4 | 过 | 0.41 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.11 | 0.40 | 0.47 | 0.33 | 0.42 | 0.20 | `cross_ema(cs_demean(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth)), 120)` |
| slot b seed 5 | 过 | 0.32 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.10 | 0.40 | 0.40 | 0.11 | 0.44 | 0.12 | `cross_max(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), 60)` |
| slot b seed 6 | 过 | 0.33 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.12 | 0.44 | 0.39 | 0.21 | 0.45 | 0.28 | `cross_ema(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), 241)` |
| slot b seed 7 | 废品 | 0.35 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.14 | 0.45 | 0.43 | 0.11 | 0.48 | 0.16 | `cross_mean(is_gt(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.5), 60)` |
| slot b seed 8 | 废品 | 0.25 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.07 | 0.26 | 0.31 | 0.06 | 0.29 | 0.02 | `sub(cross_mean(is_gt(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.8), 120), cross_mean(is_lt(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), -0.8), 120))` |
| slot b seed 9 | 过 | 0.17 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.06 | 0.01 | 0.17 | 0.32 | 0.01 | 0.00 | `cross_ema(cs_bucket_rank(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), LogFloatCap), 120)` |
| slot b seed 10 | 过 | 0.06 | `day_std(pow_2(Volume))` | 0.04 | 0.03 | 0.05 | 0.11 | 0.03 | 0.01 | `cross_zscore(div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth), 60)` |
| R 1 variant 1 | 过 | 0.85 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.76 | 0.22 | 0.83 | 0.31 | 0.28 | 0.17 | `cross_mean(day_std(pow_2(Ret)), 10)` |
| R 1 variant 2 | 过 | 0.77 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.48 | 0.26 | 0.89 | 0.23 | 0.32 | 0.20 | `cross_mean(day_std(pow_2(Ret)), 20)` |
| R 1 variant 3 | 过 | 0.64 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.33 | 0.25 | 0.77 | 0.02 | 0.30 | 0.26 | `cross_mean(day_std(pow_2(Ret)), 60)` |
| R 1 variant 4 | 过 | 0.56 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.27 | 0.17 | 0.65 | 0.03 | 0.20 | 0.32 | `cross_mean(day_std(pow_2(Ret)), 120)` |
| R 1 variant 5 | 过 | 0.71 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.40 | 0.26 | 0.82 | 0.09 | 0.31 | 0.28 | `cross_ema(day_std(pow_2(Ret)), 20)` |
| R 1 variant 6 | 过 | 0.60 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.31 | 0.17 | 0.69 | 0.01 | 0.21 | 0.36 | `cross_ema(day_std(pow_2(Ret)), 60)` |
| R 1 variant 7 | 过 | 0.54 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.27 | 0.10 | 0.60 | 0.03 | 0.14 | 0.40 | `cross_ema(day_std(pow_2(Ret)), 120)` |
| R 1 variant 8 | 过 | 0.39 | `cross_mean(day_std(pow_2(Ret)), 3)` | 0.33 | 0.28 | 0.68 | 0.01 | 0.31 | 0.14 | `cross_ema(div(day_std(pow_2(Ret)), pow_2(replace_small_with_nan(day_var(Ret)))), 60)` |
| R 2 variant 1 | 过 | 0.91 | `day_std(pow_2(Volume))` | 0.93 | 0.57 | 0.29 | 0.16 | 0.63 | 0.46 | `cross_mean(day_std(pow_2(Volume)), 20)` |
| R 2 variant 2 | 过 | 0.85 | `day_std(pow_2(Volume))` | 0.86 | 0.47 | 0.13 | 0.03 | 0.51 | 0.41 | `cross_ema(day_std(pow_2(Volume)), 60)` |
| R 2 variant 3 | 过 | 0.85 | `day_std(pow_2(Volume))` | 0.89 | 0.51 | 0.05 | 0.01 | 0.53 | 0.56 | `cross_ema(div(day_std(pow_2(Volume)), pow_2(replace_small_with_nan(day_var(Volume)))), 60)` |
| R 2 variant 4 | 过 | 0.70 | `day_std(pow_2(Volume))` | 0.87 | 0.26 | 0.22 | 0.03 | 0.31 | 0.01 | `cross_ema(cs_bucket_rank(day_std(pow_2(Volume)), LogFloatCap), 60)` |
