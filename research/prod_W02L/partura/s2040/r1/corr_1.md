# 相关度表:种子 2040,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.10 | `day_mean(log(Volume))` | 0.04 | 0.05 | 0.04 | 0.18 | 0.05 | 0.06 | `day_cov(Ret, log(Amt))` |
| slot a seed 1 | 过 | 0.26 | `day_first(log(Amt))` | 0.10 | 0.36 | 0.49 | 0.12 | 0.38 | 0.06 | `cross_mean(day_cov(Ret, log(Amt)), 120)` |
| slot a seed 2 | 过 | 0.30 | `day_first(log(Amt))` | 0.09 | 0.38 | 0.56 | 0.25 | 0.40 | 0.06 | `cross_decay_linear(day_cov(Ret, log(Amt)), 120)` |
| slot a seed 3 | 过 | 0.31 | `day_first(log(Amt))` | 0.09 | 0.40 | 0.55 | 0.20 | 0.42 | 0.07 | `cross_ema(day_cov(Ret, log(Amt)), 60)` |
| slot a seed 4 | 过 | 0.33 | `day_mean(log(Volume))` | 0.11 | 0.41 | 0.34 | 0.14 | 0.40 | 0.26 | `cross_mean(div(day_cov(Ret, log(Amt)), add(mul(day_std(Ret), day_std(log(Amt))), 0.000001)), 120)` |
| slot a seed 5 | 过 | 0.17 | `day_first(log(Amt))` | 0.14 | 0.02 | 0.22 | 0.64 | 0.05 | 0.01 | `cross_zscore(cross_mean(day_cov(Ret, log(Amt)), 20), 241)` |
| slot a seed 6 | 过 | 0.18 | `day_first(log(Amt))` | 0.14 | 0.03 | 0.22 | 0.65 | 0.06 | 0.00 | `sub(cross_mean(day_cov(Ret, log(Amt)), 20), cross_mean(day_cov(Ret, log(Amt)), 241))` |
| slot a seed 7 | 过 | 0.24 | `day_first(log(Amt))` | 0.06 | 0.30 | 0.53 | 0.23 | 0.33 | 0.04 | `cs_bucket_zscore(cross_mean(day_cov(Ret, log(Amt)), 60), LogFloatCap)` |
| slot a seed 8 | 过 | 0.10 | `day_mean(log(Volume))` | 0.08 | 0.04 | 0.29 | 0.17 | 0.05 | 0.00 | `cs_bucket_zscore(cross_mean(div(day_cov(Ret, log(Amt)), add(mul(day_std(Ret), day_std(log(Amt))), 0.000001)), 120), cross_mean(day_mean(log(Amt)), 60))` |
| slot a seed 9 | 过 | 0.10 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.08 | 0.05 | 0.07 | 0.17 | 0.05 | 0.02 | `mul(cs_demean(cs_rank(cross_mean(day_cov(Ret, log(Amt)), 60))), cs_demean(cs_rank(ts_delta(log(day_last(Close)), 20))))` |
| slot a seed 10 | 过 | 0.08 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.05 | 0.05 | 0.03 | 0.04 | 0.04 | 0.03 | `mul(cs_demean(cs_rank(cross_mean(div(day_cov(Ret, log(Amt)), add(mul(day_std(Ret), day_std(log(Amt))), 0.000001)), 120))), cs_demean(cs_rank(ts_delta(log(day_last(Close)), 60))))` |
| slot a seed 11 | 过 | 0.08 | `day_first(log(Amt))` | 0.09 | 0.02 | 0.03 | 0.07 | 0.03 | 0.01 | `mul(cs_demean(cs_rank(cross_ema(day_cov(Ret, log(Amt)), 20))), cs_demean(cs_rank(ts_delta(log(day_last(Close)), 5))))` |
| slot a seed 12 | 过 | 0.32 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.27 | 0.40 | 0.52 | 0.00 | 0.40 | 0.09 | `cross_mean(mul(cs_demean(cs_rank(day_cov(Ret, log(Amt)))), cs_demean(cs_rank(ts_delta(log(day_last(Close)), 1)))), 60)` |
| slot a seed 13 | 过 | 0.04 | `day_first(log(Amt))` | 0.02 | 0.01 | 0.41 | 0.13 | 0.04 | 0.24 | `cross_mean(mul(day_cov(Ret, log(Amt)), sign(ts_delta(log(day_last(Close)), 5))), 60)` |
| slot a seed 14 | 过 | 0.31 | `day_mean(log(Volume))` | 0.07 | 0.39 | 0.23 | 0.10 | 0.37 | 0.30 | `cross_mean(sub(day_cov(Ret, log(Amt)), day_cov(Ret, in_delay(log(Amt), 1))), 120)` |
| slot a seed 15 | 过 | 0.31 | `day_mean(log(Volume))` | 0.13 | 0.35 | 0.37 | 0.14 | 0.36 | 0.18 | `cross_mean(div(day_cov(Ret, log(Amt)), add(day_std(Ret), 0.000001)), 120)` |
| slot a seed 16 | 过 | 0.25 | `day_first(log(Amt))` | 0.03 | 0.33 | 0.50 | 0.21 | 0.35 | 0.02 | `cross_mean(mul(day_cov(Ret, log(Amt)), is_gt(day_std(Ret), cross_mean(day_std(Ret), 20))), 60)` |
| slot b seed 1 | 过 | 0.25 | `day_mean(log(Volume))` | 0.62 | 0.06 | 0.28 | 0.06 | 0.14 | 0.16 | `cross_mean(sub(day_first(log(Amt)), day_mean(log(Amt))), 60)` |
| slot b seed 2 | 过 | 0.26 | `day_mean(log(Volume))` | 0.58 | 0.04 | 0.24 | 0.04 | 0.11 | 0.18 | `cross_decay_linear(sub(day_first(log(Amt)), day_mean(log(Amt))), 241)` |
| slot b seed 3 | 过 | 0.24 | `day_mean(log(Volume))` | 0.20 | 0.27 | 0.40 | 0.08 | 0.30 | 0.08 | `cross_mean(cross_zscore(day_first(log(Amt)), 241), 60)` |
| slot b seed 4 | 过 | 0.37 | `day_mean(log(Volume))` | 0.59 | 0.18 | 0.21 | 0.04 | 0.24 | 0.03 | `cs_bucket_zscore(cross_mean(sub(day_first(log(Amt)), day_mean(log(Amt))), 120), LogFloatCap)` |
| slot b seed 5 | 过 | 0.14 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.10 | 0.15 | 0.09 | 0.09 | 0.15 | 0.11 | `cross_mean(mul(cross_zscore(day_first(log(Amt)), 120), sub(log(day_first(Open)), ts_delay(log(day_last(Close)), 1))), 60)` |
| slot b seed 6 | 过 | 0.13 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.06 | 0.15 | 0.12 | 0.06 | 0.16 | 0.15 | `cross_mean(mul(cs_demean(sub(day_first(log(Amt)), day_mean(log(Amt)))), sub(log(day_first(Open)), ts_delay(log(day_last(Close)), 1))), 120)` |
| slot b seed 7 | 过 | 0.13 | `day_first(log(Amt))` | 0.04 | 0.15 | 0.11 | 0.07 | 0.16 | 0.16 | `cross_corr(sub(day_first(log(Amt)), day_mean(log(Amt))), sub(log(day_first(Open)), ts_delay(log(day_last(Close)), 1)), 120)` |
| slot b seed 8 | 过 | 0.02 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.03 | 0.02 | 0.06 | 0.09 | 0.01 | 0.04 | `cross_mean(mul(cs_demean(sub(day_first(log(Amt)), day_mean(log(Amt)))), sub(log(day_last(Close)), log(day_first(Open)))), 60)` |
| slot b seed 9 | 过 | 0.47 | `day_mean(log(Volume))` | 0.23 | 0.58 | 0.15 | 0.06 | 0.53 | 0.60 | `cross_stddev(sub(day_first(log(Amt)), day_mean(log(Amt))), 120)` |
| slot b seed 10 | 过 | 0.30 | `day_mean(log(Volume))` | 0.55 | 0.17 | 0.20 | 0.02 | 0.23 | 0.11 | `cross_mean(div(day_first(Amt), add(day_sum(Amt), 1)), 120)` |
| slot b seed 11 | 过 | 0.37 | `day_first(log(Amt))` | 0.53 | 0.39 | 0.30 | 0.01 | 0.42 | 0.19 | `cross_mean(sub(day_first(log(Amt)), day_last(log(Amt))), 120)` |
| slot b seed 12 | 过 | 0.10 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.03 | 0.10 | 0.06 | 0.04 | 0.10 | 0.01 | `mul(cs_demean(cs_rank(cross_mean(sub(day_first(log(Amt)), day_mean(log(Amt))), 60))), cs_demean(cs_rank(ts_delta(log(day_last(Close)), 60))))` |
| slot b seed 13 | 过 | 0.27 | `day_mean(log(Volume))` | 0.60 | 0.05 | 0.26 | 0.05 | 0.13 | 0.17 | `cross_ema(sub(day_first(log(Amt)), day_mean(log(Amt))), 60)` |
| R 1 variant 1 | 过 | 0.68 | `day_mean(log(Volume))` | 0.72 | 0.93 | 0.25 | 0.04 | 0.92 | 0.58 | `cross_mean(day_first(log(Amt)), 60)` |
| R 1 variant 2 | 过 | 0.22 | `day_mean(log(Volume))` | 0.50 | 0.01 | 0.19 | 0.02 | 0.08 | 0.20 | `cross_mean(cs_bucket_zscore(day_first(log(Amt)), day_mean(log(Amt))), 241)` |
| R 1 variant 3 | 过 | 0.25 | `day_mean(log(Volume))` | 0.60 | 0.06 | 0.27 | 0.05 | 0.14 | 0.16 | `cross_mean(cs_bucket_zscore(day_first(log(Amt)), day_mean(log(Amt))), 60)` |
| R 1 variant 4 | 过 | 0.14 | `day_mean(log(Volume))` | 0.23 | 0.02 | 0.17 | 0.03 | 0.04 | 0.04 | `cs_bucket_zscore(cross_mean(day_first(log(Amt)), 241), cross_mean(day_mean(log(Amt)), 60))` |
| R 2 variant 1 | 过 | 0.84 | `day_mean(log(Volume))` | 0.85 | 0.62 | 0.00 | 0.01 | 0.62 | 0.62 | `cross_mean(day_mean(log(Volume)), 241)` |
| R 2 variant 2 | 过 | 0.89 | `day_mean(log(Volume))` | 0.97 | 0.38 | 0.13 | 0.14 | 0.42 | 0.41 | `sub(day_mean(log(Amt)), mul(2, day_mean(log(Volume))))` |
| R 2 variant 3 | 过 | 0.96 | `day_mean(log(Volume))` | 0.99 | 0.52 | 0.16 | 0.16 | 0.56 | 0.50 | `sub(mul(0.5, day_mean(log(Amt))), mul(1.5, day_mean(log(Volume))))` |
| R 2 variant 4 | 过 | 0.76 | `day_mean(log(Volume))` | 0.94 | 0.19 | 0.08 | 0.10 | 0.24 | 0.29 | `sub(mul(2, day_mean(log(Amt))), mul(3, day_mean(log(Volume))))` |
| R 2 variant 5 | 过 | 0.49 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.88 | 0.23 | 0.06 | 0.00 | 0.18 | 0.00 | `sub(day_mean(log(Amt)), day_mean(log(Volume)))` |
| R 2 variant 6 | 过 | 0.79 | `day_mean(log(Volume))` | 0.95 | 0.35 | 0.04 | 0.02 | 0.38 | 0.42 | `cross_mean(sub(day_mean(log(Amt)), mul(2, day_mean(log(Volume)))), 120)` |
| R 3 variant 1 | 过 | 0.72 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.86 | 0.53 | 0.18 | 0.22 | 0.51 | 0.36 | `add(cs_rank(day_min(log(Amt))), cs_rank(day_cov(Ret, log(Amt))))` |
| R 3 variant 2 | 过 | 0.76 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.75 | 0.79 | 0.11 | 0.07 | 0.73 | 0.55 | `cross_mean(add(cs_rank(day_min(log(Amt))), cs_rank(day_cov(Ret, log(Amt)))), 120)` |
| R 3 variant 3 | 过 | 0.72 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.74 | 0.71 | 0.03 | 0.12 | 0.65 | 0.51 | `cross_mean(sub(cs_rank(day_cov(Ret, log(Amt))), cs_rank(day_min(log(Amt)))), 120)` |
| R 3 variant 4 | 过 | 0.72 | `add(day_min(log(Amt)), day_cov(Ret, log(Amt)))` | 0.66 | 0.72 | 0.02 | 0.09 | 0.66 | 0.53 | `cross_mean(day_min(log(Amt)), 241)` |
