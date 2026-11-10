# 相关度表:种子 2032,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.90 | `cross_sum(day_first(Volume), 3)` | 0.98 | 0.56 | 0.25 | 0.21 | 0.60 | 0.41 | `day_first(Volume)` |
| slot a seed 1 | 过 | 0.35 | `cross_sum(day_first(Volume), 5)` | 0.19 | 0.09 | 0.25 | 0.34 | 0.13 | 0.05 | `cross_ema(cross_zscore(day_first(Volume), 60), 10)` |
| slot a seed 2 | 过 | 0.33 | `cross_sum(day_first(Volume), 5)` | 0.10 | 0.24 | 0.35 | 0.20 | 0.28 | 0.10 | `cross_ema(cross_zscore(log(add(day_first(Volume), 1)), 120), 20)` |
| slot a seed 3 | 过 | 0.27 | `cross_sum(day_first(Volume), 5)` | 0.05 | 0.20 | 0.23 | 0.16 | 0.23 | 0.10 | `cross_tail_mean_q75(cross_zscore(day_first(Volume), 60), 60)` |
| slot a seed 4 | 过 | 0.62 | `cross_sum(day_first(Volume), 60)` | 0.57 | 0.26 | 0.34 | 0.05 | 0.33 | 0.11 | `cross_ema(div(day_first(Volume), day_sum(Volume)), 30)` |
| slot a seed 5 | 过 | 0.33 | `cross_sum(day_first(Volume), 5)` | 0.16 | 0.02 | 0.13 | 0.24 | 0.06 | 0.07 | `cross_ema(cross_zscore(div(day_first(Volume), day_sum(Volume)), 60), 10)` |
| slot a seed 6 | 过 | 0.56 | `cross_sum(day_first(Volume), 60)` | 0.49 | 0.19 | 0.26 | 0.06 | 0.26 | 0.04 | `cross_ema(div(day_first(Volume), day_sum(in_slice(Volume, 1, 30))), 20)` |
| slot a seed 7 | 过 | 0.33 | `cross_sum(day_first(Volume), 60)` | 0.42 | 0.06 | 0.19 | 0.03 | 0.01 | 0.31 | `cs_bucket_zscore(cross_ema(day_first(Volume), 20), cross_mean(day_sum(Volume), 30))` |
| slot a seed 8 | 过 | 0.09 | `cross_sum(day_first(Volume), 5)` | 0.06 | 0.10 | 0.06 | 0.14 | 0.11 | 0.15 | `cross_corr(log(add(day_first(Volume), 1)), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 9 | 过 | 0.22 | `cross_sum(day_first(Volume), 60)` | 0.09 | 0.19 | 0.19 | 0.14 | 0.21 | 0.02 | `cross_ema(mul(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), cross_zscore(day_first(Volume), 60)), 20)` |
| slot a seed 10 | 过 | 0.10 | `cross_sum(day_first(Volume), 3)` | 0.09 | 0.04 | 0.07 | 0.01 | 0.04 | 0.07 | `cross_reg_tvalue(day_first(Volume), abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 60)` |
| slot a seed 11 | 过 | 0.09 | `cross_sum(day_first(Volume), 3)` | 0.03 | 0.16 | 0.04 | 0.06 | 0.16 | 0.14 | `cross_ema(mul(sign(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), cross_zscore(log(add(day_first(Volume), 1)), 60)), 30)` |
| slot a seed 12 | 过 | 0.03 | `cross_sum(day_first(Volume), 3)` | 0.03 | 0.08 | 0.09 | 0.02 | 0.07 | 0.04 | `cross_reg_tvalue(log(add(day_first(Volume), 1)), sub(div(day_last(Close), day_first(Open)), 1), 90)` |
| slot a seed 13 | 过 | 0.14 | `cross_sum(day_first(Volume), 3)` | 0.17 | 0.32 | 0.10 | 0.05 | 0.26 | 0.36 | `div(cross_stddev(day_first(Volume), 60), cross_mean(day_first(Volume), 60))` |
| slot a seed 14 | 过 | 0.18 | `cross_sum(day_first(Volume), 60)` | 0.06 | 0.16 | 0.14 | 0.12 | 0.18 | 0.06 | `cross_ema(select_where(is_gt(cross_zscore(day_first(Volume), 60), 1.5), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 0), 30)` |
| slot a seed 15 | 过 | 0.18 | `cross_sum(day_first(Volume), 5)` | 0.13 | 0.00 | 0.04 | 0.09 | 0.02 | 0.05 | `cross_ema(cross_regres(log(add(day_sum(Volume), 1)), log(add(day_first(Volume), 1)), 60), 15)` |
| slot a seed 16 | 过 | 0.72 | `cross_sum(day_first(Volume), 60)` | 0.45 | 0.71 | 0.24 | 0.04 | 0.72 | 0.46 | `cross_ema(sub(log(add(day_first(Volume), 1)), log(add(day_last(Volume), 1))), 30)` |
| slot b seed 1 | 过 | 0.23 | `cross_sum(day_first(Volume), 5)` | 0.09 | 0.27 | 0.36 | 0.29 | 0.29 | 0.02 | `cross_ema(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 30)` |
| slot b seed 2 | 过 | 0.13 | `cross_sum(day_first(Volume), 60)` | 0.12 | 0.09 | 0.12 | 0.14 | 0.10 | 0.14 | `cross_ema(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40)` |
| slot b seed 3 | 过 | 0.28 | `cross_sum(day_first(Volume), 5)` | 0.06 | 0.34 | 0.45 | 0.44 | 0.37 | 0.03 | `cross_ema(sub(div(day_last(Close), day_first(Open)), 1), 40)` |
| slot b seed 4 | 过 | 0.13 | `cross_sum(day_first(Volume), 5)` | 0.08 | 0.19 | 0.06 | 0.01 | 0.17 | 0.14 | `cross_reg_tvalue(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1), 60)` |
| slot b seed 5 | 过 | 0.18 | `cross_sum(day_first(Volume), 60)` | 0.11 | 0.21 | 0.07 | 0.02 | 0.19 | 0.15 | `cross_regbeta(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1), 120)` |
| slot b seed 6 | 过 | 0.13 | `cross_sum(day_first(Volume), 3)` | 0.09 | 0.19 | 0.06 | 0.01 | 0.17 | 0.14 | `cross_corr(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1), 60)` |
| slot b seed 7 | 过 | 0.07 | `cross_sum(day_first(Volume), 60)` | 0.24 | 0.24 | 0.03 | 0.02 | 0.21 | 0.04 | `cross_ema(is_lt(mul(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 0), 30)` |
| slot b seed 8 | 过 | 0.05 | `cross_sum(day_first(Volume), 3)` | 0.11 | 0.04 | 0.24 | 0.03 | 0.02 | 0.19 | `cross_ema(neg(mul(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1))), 30)` |
| slot b seed 9 | 过 | 0.34 | `cross_sum(day_first(Volume), 60)` | 0.20 | 0.16 | 0.10 | 0.01 | 0.21 | 0.03 | `div(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), add(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 40), cross_mean(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 40)))` |
| slot b seed 10 | 过 | 0.05 | `cross_sum(day_first(Volume), 60)` | 0.08 | 0.03 | 0.06 | 0.14 | 0.03 | 0.11 | `add(cross_tail_mean_q75(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60), cross_tail_mean_q25(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60))` |
| slot b seed 11 | 过 | 0.24 | `cross_sum(day_first(Volume), 5)` | 0.06 | 0.29 | 0.24 | 0.27 | 0.29 | 0.05 | `cross_ema(sub(div(day_first(Open), day_mean(in_slice(Close, 1, 30))), 1), 30)` |
| slot b seed 12 | 过 | 0.20 | `cross_sum(day_first(Volume), 5)` | 0.04 | 0.23 | 0.18 | 0.27 | 0.24 | 0.06 | `cross_ema(sub(div(day_first(Open), day_mean(in_slice(Close, 1, 15))), 1), 20)` |
| slot b seed 13 | 过 | 0.09 | `cross_sum(day_first(Volume), 60)` | 0.02 | 0.13 | 0.05 | 0.03 | 0.12 | 0.01 | `cross_ema(sub(sub(div(day_last(in_slice(Close, 1, 30)), day_first(Open)), 1), sub(div(day_last(Close), day_last(in_slice(Close, 1, 30))), 1)), 30)` |
| slot b seed 14 | 过 | 0.19 | `cross_sum(day_first(Volume), 60)` | 0.08 | 0.11 | 0.15 | 0.01 | 0.13 | 0.02 | `cross_corr(ts_delay(sub(div(day_last(Close), day_first(Open)), 1), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 90)` |
| slot b seed 15 | 过 | 0.19 | `cross_sum(day_first(Volume), 60)` | 0.08 | 0.09 | 0.13 | 0.00 | 0.13 | 0.02 | `cross_ema(mul(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), ts_delay(sub(div(day_last(Close), day_first(Open)), 1), 1)), 30)` |
| R 1 variant 1 | 过 | 0.62 | `cross_sum(day_first(Volume), 60)` | 0.61 | 0.21 | 0.33 | 0.05 | 0.28 | 0.15 | `div(cross_sum(day_first(Volume), 60), cross_sum(day_sum(Volume), 60))` |
| R 1 variant 2 | 过 | 0.35 | `cross_sum(day_first(Volume), 5)` | 0.10 | 0.19 | 0.35 | 0.27 | 0.24 | 0.05 | `cross_zscore(cross_mean(day_first(Volume), 20), 240)` |
| R 1 variant 3 | 过 | 0.36 | `cross_sum(day_first(Volume), 5)` | 0.18 | 0.23 | 0.31 | 0.30 | 0.28 | 0.15 | `sub(log(add(cross_mean(day_first(Volume), 20), 1)), log(add(cross_mean(day_first(Volume), 120), 1)))` |
| R 1 variant 4 | 过 | 0.33 | `cross_sum(day_first(Volume), 60)` | 0.34 | 0.01 | 0.27 | 0.05 | 0.08 | 0.31 | `cs_bucket_zscore(cross_mean(day_first(Volume), 60), cross_mean(day_sum(Volume), 60))` |
| R 1 variant 5 | 过 | 0.71 | `cross_sum(day_first(Volume), 60)` | 0.66 | 0.49 | 0.40 | 0.02 | 0.54 | 0.07 | `cs_bucket_zscore(cross_mean(day_first(Volume), 60), LogFloatShares)` |
| R 2 variant 1 | 过 | 0.45 | `cross_sum(day_first(Volume), 5)` | 0.19 | 0.20 | 0.36 | 0.34 | 0.25 | 0.07 | `sub(cross_ema(log(add(day_first(Volume), 1)), 5), cross_ema(log(add(day_first(Volume), 1)), 60))` |
| R 2 variant 2 | 过 | 0.40 | `cross_sum(day_first(Volume), 5)` | 0.28 | 0.01 | 0.15 | 0.14 | 0.03 | 0.16 | `cs_bucket_rank(cross_sum(day_first(Volume), 5), cross_sum(day_sum(Volume), 5))` |
| R 2 variant 3 | 过 | 0.70 | `cross_sum(day_first(Volume), 5)` | 0.62 | 0.22 | 0.23 | 0.20 | 0.27 | 0.04 | `div(cross_sum(day_first(Volume), 5), cross_sum(day_sum(Volume), 5))` |
| R 2 variant 4 | 过 | 0.46 | `cross_sum(day_first(Volume), 5)` | 0.24 | 0.08 | 0.25 | 0.33 | 0.12 | 0.04 | `cross_zscore(cross_sum(day_first(Volume), 5), 250)` |
| R 3 variant 1 | 过 | 0.63 | `cross_sum(day_first(Volume), 3)` | 0.88 | 0.08 | 0.15 | 0.21 | 0.02 | 0.04 | `cs_bucket_zscore(cross_sum(day_first(Volume), 3), cross_mean(day_sum(Amt), 30))` |
| R 3 variant 2 | 过 | 0.28 | `cross_sum(day_first(Volume), 3)` | 0.25 | 0.02 | 0.12 | 0.14 | 0.05 | 0.17 | `sub(div(cross_sum(day_first(Volume), 3), cross_sum(day_sum(Volume), 3)), div(cross_sum(day_first(Volume), 60), cross_sum(day_sum(Volume), 60)))` |
| R 3 variant 3 | 过 | 0.53 | `cross_sum(day_first(Volume), 3)` | 0.27 | 0.11 | 0.08 | 0.33 | 0.12 | 0.16 | `div(cross_sum(day_first(Volume), 3), cross_sum(day_first(Volume), 60))` |
