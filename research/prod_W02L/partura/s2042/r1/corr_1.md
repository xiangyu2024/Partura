# 相关度表:种子 2042,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.09 | `ts_std(day_kurt(Low), 50)` | 0.17 | 0.00 | 0.06 | 0.03 | 0.01 | 0.04 | `day_kurt(Low)` |
| slot a seed 1 | 过 | 0.34 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.13 | 0.36 | 0.39 | 0.10 | 0.38 | 0.08 | `cross_mean(div(day_sum(Ret), add(day_kurt(Low), 4)), 241)` |
| slot a seed 2 | 过 | 0.05 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.07 | 0.19 | 0.25 | 0.16 | 0.21 | 0.36 | `cross_ema(mul(day_signed_ratio(Ret, Amt), inv(add(day_kurt(Low), 4))), 120)` |
| slot a seed 3 | 过 | 0.09 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.06 | 0.03 | 0.09 | 0.01 | 0.04 | 0.04 | `mul(cross_ema(cross_corr(day_kurt(Low), day_sum(Ret), 60), 60), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot a seed 4 | 过 | 0.15 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.05 | 0.22 | 0.19 | 0.13 | 0.24 | 0.17 | `mul(cross_mean(mul(cs_rank(day_kurt(Low)), sub(cs_rank(day_sum(Ret)), 0.5)), 241), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot a seed 5 | 过 | 0.12 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.07 | 0.04 | 0.12 | 0.11 | 0.07 | 0.06 | `cross_mean(mul(sign(day_sum(Ret)), neg(cs_rank(day_kurt(Low)))), 241)` |
| slot a seed 6 | 过 | 0.17 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.11 | 0.08 | 0.03 | 0.02 | 0.07 | 0.27 | `mul(cross_mean(sub(cs_rank(day_kurt(Low)), cs_rank(day_kurt(High))), 241), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot a seed 7 | 过 | 0.30 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.21 | 0.12 | 0.14 | 0.01 | 0.08 | 0.30 | `cross_ema(cs_winsor(sub(day_kurt(Low), day_kurt(High))), 120)` |
| slot a seed 8 | 过 | 0.21 | `ts_std(day_kurt(Low), 50)` | 0.22 | 0.23 | 0.12 | 0.00 | 0.21 | 0.24 | `cross_ema(cs_robust_z(sub(day_kurt(Low), day_kurt(Vwap))), 90)` |
| slot a seed 9 | 过 | 0.51 | `ts_std(day_kurt(Low), 50)` | 0.50 | 0.09 | 0.15 | 0.08 | 0.11 | 0.04 | `cross_ema(cross_zscore(day_kurt(Low), 120), 40)` |
| slot a seed 10 | 过 | 0.31 | `ts_std(day_kurt(Low), 50)` | 0.28 | 0.07 | 0.15 | 0.05 | 0.09 | 0.03 | `sub(cross_ema(cs_rank(day_kurt(Low)), 30), cross_ema(cs_rank(day_kurt(Low)), 240))` |
| slot a seed 11 | 过 | 0.45 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.41 | 0.14 | 0.14 | 0.01 | 0.11 | 0.33 | `cs_bucket_zscore(cross_mean(cs_rank(day_kurt(Low)), 241), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 12 | 过 | 0.39 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.40 | 0.02 | 0.04 | 0.06 | 0.02 | 0.10 | `cs_bucket_demean(cross_ema(ts_std(cs_rank(day_kurt(Low)), 60), 90), cross_mean(day_std(Amt), 30))` |
| slot a seed 13 | 过 | 0.34 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.15 | 0.34 | 0.35 | 0.09 | 0.35 | 0.06 | `cs_bucket_zscore(cross_mean(div(day_sum(Ret), add(day_kurt(Low), 4)), 241), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 14 | 过 | 0.25 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.18 | 0.13 | 0.40 | 0.06 | 0.16 | 0.19 | `cross_mean(div(day_wmean(Ret, Amt), add(day_kurt(Low), 4)), 241)` |
| slot a seed 15 | 过 | 0.39 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.12 | 0.42 | 0.49 | 0.29 | 0.44 | 0.11 | `mul(cross_ema(div(day_sum(Ret), add(day_kurt(Low), 4)), 60), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 1 | 过 | 0.46 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.41 | 0.03 | 0.12 | 0.01 | 0.05 | 0.15 | `mul(cross_ema(cross_corr(day_kurt(Vwap), day_kurt(Volume), 60), 60), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 2 | 过 | 0.37 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.32 | 0.02 | 0.09 | 0.01 | 0.04 | 0.14 | `mul(cross_mean(cross_corr(day_kurt(High), day_kurt(Amt), 60), 120), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 3 | 过 | 0.34 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.28 | 0.07 | 0.13 | 0.01 | 0.09 | 0.11 | `mul(cross_corr(day_kurt(Close), day_kurt(Volume), 120), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 4 | 过 | 0.43 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.09 | 0.47 | 0.10 | 0.07 | 0.40 | 0.25 | `cross_mean(sub(cs_rank(day_kurt(Vwap)), cs_rank(day_kurt(Volume))), 241)` |
| slot b seed 5 | 过 | 0.44 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.11 | 0.46 | 0.05 | 0.08 | 0.39 | 0.20 | `cross_ema(sub(cs_rank(day_kurt(High)), cs_rank(day_kurt(Amt))), 120)` |
| slot b seed 6 | 过 | 0.35 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.07 | 0.40 | 0.10 | 0.09 | 0.35 | 0.27 | `cs_bucket_zscore(cross_mean(sub(cs_rank(day_kurt(Vwap)), cs_rank(day_kurt(Volume))), 241), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 7 | 过 | 0.50 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.46 | 0.45 | 0.13 | 0.07 | 0.37 | 0.39 | `cross_mean(mul(cs_rank(day_kurt(Vwap)), cs_rank(day_kurt(Volume))), 241)` |
| slot b seed 8 | 过 | 0.25 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.17 | 0.16 | 0.12 | 0.04 | 0.12 | 0.03 | `mul(cross_ema(ts_regres(day_kurt(Vwap), day_kurt(Volume), 60), 60), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 9 | 过 | 0.41 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.39 | 0.03 | 0.04 | 0.02 | 0.04 | 0.17 | `cross_mean(cs_regres(cs_rank(day_kurt(Vwap)), cs_rank(day_kurt(Volume))), 241)` |
| slot b seed 10 | 过 | 0.42 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.09 | 0.50 | 0.10 | 0.08 | 0.42 | 0.29 | `cross_mean(sub(log(add(day_kurt(Vwap), 4)), log(add(day_kurt(Volume), 4))), 241)` |
| slot b seed 11 | 过 | 0.44 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.12 | 0.50 | 0.06 | 0.08 | 0.42 | 0.26 | `cross_ema(sub(log(add(day_kurt(Close), 4)), log(add(day_kurt(Amt), 4))), 120)` |
| slot b seed 12 | 过 | 0.41 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.36 | 0.07 | 0.15 | 0.02 | 0.06 | 0.36 | `mul(cross_ema(cs_regres(cs_rank(day_kurt(High)), cs_rank(day_kurt(Amt))), 120), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 13 | 过 | 0.22 | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Volume), ts_h` | 0.12 | 0.13 | 0.09 | 0.03 | 0.10 | 0.04 | `mul(cross_mean(cross_regres(day_kurt(High), day_kurt(Volume), 120), 60), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 14 | 过 | 0.47 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.41 | 0.05 | 0.10 | 0.01 | 0.02 | 0.20 | `mul(cs_bucket_demean(cross_ema(cross_corr(day_kurt(Vwap), day_kurt(Amt), 60), 60), cross_mean(day_std(Amt), 30)), replace_small_with_nan(is_gt(ListAge, 120)))` |
| slot b seed 15 | 过 | 0.35 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.29 | 0.10 | 0.06 | 0.02 | 0.12 | 0.13 | `mul(cross_ema(cross_corr(day_kurt(Ret), day_kurt(Volume), 60), 60), replace_small_with_nan(is_gt(ListAge, 120)))` |
| R 1 variant 1 | 过 | 0.73 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.70 | 0.06 | 0.15 | 0.02 | 0.02 | 0.21 | `ts_std(day_kurt(Low), 150)` |
| R 1 variant 2 | 过 | 0.90 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.90 | 0.08 | 0.13 | 0.02 | 0.04 | 0.22 | `ts_std(day_kurt(Low), 241)` |
| R 1 variant 3 | 过 | 0.66 | `ts_std(day_kurt(Low), 50)` | 0.63 | 0.05 | 0.15 | 0.02 | 0.01 | 0.21 | `ts_std(day_kurt(Low), 120)` |
| R 1 variant 4 | 过 | 0.37 | `ts_std(day_kurt(Low), 50)` | 0.35 | 0.14 | 0.15 | 0.01 | 0.15 | 0.07 | `ts_std(cs_rank(day_kurt(Low)), 120)` |
| R 1 variant 5 | 过 | 0.66 | `ts_std(day_kurt(Low), 50)` | 0.63 | 0.03 | 0.16 | 0.02 | 0.01 | 0.20 | `ts_std(cs_demean(day_kurt(Low)), 120)` |
| R 1 variant 6 | 过 | 0.38 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.40 | 0.09 | 0.11 | 0.03 | 0.10 | 0.10 | `ts_std(cs_rank(day_kurt(Low)), 241)` |
| R 1 variant 7 | 过 | 0.91 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.91 | 0.11 | 0.11 | 0.00 | 0.07 | 0.23 | `cross_ema(ts_std(day_kurt(Low), 60), 120)` |
| R 1 variant 8 | 过 | 0.61 | `ts_std(day_kurt(Low), 50)` | 0.59 | 0.03 | 0.20 | 0.02 | 0.06 | 0.18 | `cs_bucket_zscore(ts_std(day_kurt(Low), 120), sub(LogFloatCap, LogFloatShares))` |
| R 1 variant 9 | 过 | 0.58 | `ts_std(day_kurt(Low), 50)` | 0.61 | 0.15 | 0.12 | 0.03 | 0.19 | 0.07 | `cs_bucket_zscore(ts_std(day_kurt(Low), 120), LogFloatCap)` |
| R 1 variant 10 | 过 | 0.64 | `ts_std(day_kurt(Low), 50)` | 0.61 | 0.05 | 0.14 | 0.02 | 0.01 | 0.18 | `div(ts_std(day_kurt(Low), 120), add(ts_mean(day_kurt(Low), 120), 4))` |
| R 1 variant 11 | 过 | 0.65 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.62 | 0.05 | 0.18 | 0.02 | 0.01 | 0.23 | `mul(ts_std(day_kurt(Low), 120), replace_small_with_nan(is_gt(ListAge, 120)))` |
| R 2 variant 1 | 过 | 0.45 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.45 | 0.07 | 0.01 | 0.02 | 0.07 | 0.12 | `neg(cross_sum(ts_std(cs_rank(day_kurt(Low)), 50), 241))` |
| R 2 variant 2 | 过 | 0.98 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.97 | 0.10 | 0.07 | 0.01 | 0.07 | 0.14 | `neg(cross_sum(ts_std(day_kurt(Low), 100), 241))` |
| R 2 variant 3 | 过 | 0.91 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.91 | 0.11 | 0.11 | 0.00 | 0.07 | 0.23 | `neg(cross_ema(ts_std(day_kurt(Low), 50), 120))` |
| R 2 variant 4 | 过 | 0.98 | `neg(cross_sum(ts_decay_linear(ts_std(day_kurt(Low), 50), 10)` | 0.97 | 0.09 | 0.08 | 0.01 | 0.06 | 0.13 | `neg(cross_sum(ts_std(cs_demean(day_kurt(Low)), 100), 241))` |
