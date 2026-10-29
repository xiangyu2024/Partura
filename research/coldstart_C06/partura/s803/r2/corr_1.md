# 相关度表:种子 803,C 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.88 | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` | 0.89 | 0.18 | 0.16 | 0.13 | 0.19 | 0.07 | `day_centroid(Amt)` |
| slot a seed 1 | 过 | 0.76 | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` | 0.14 | 0.03 | 0.03 | 0.04 | 0.03 | 0.02 | `cross_zscore(day_centroid(Amt), 20)` |
| slot a seed 2 | 过 | 0.80 | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` | 0.23 | 0.01 | 0.04 | 0.11 | 0.01 | 0.01 | `cross_madz(day_centroid(Amt), 60)` |
| slot a seed 3 | 过 | 0.35 | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` | 0.22 | 0.03 | 0.04 | 0.18 | 0.01 | 0.03 | `cross_mean(cross_zscore(day_centroid(Amt), 60), 5)` |
| slot a seed 4 | 过 | 0.16 | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` | 0.27 | 0.02 | 0.01 | 0.03 | 0.02 | 0.00 | `sub(day_centroid(mul(Amt, is_gt0(Ret))), day_centroid(Amt))` |
| slot a seed 5 | 过 | 0.09 | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` | 0.27 | 0.05 | 0.02 | 0.03 | 0.05 | 0.01 | `cross_mean(sub(day_centroid(mul(Amt, is_gt0(Ret))), day_centroid(Amt)), 10)` |
| slot a seed 6 | 过 | 0.04 | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` | 0.11 | 0.08 | 0.07 | 0.04 | 0.06 | 0.00 | `cross_mean(sub(day_centroid(mul(Amt, is_lt0(Ret))), day_centroid(Amt)), 10)` |
| slot a seed 7 | 过 | 0.10 | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` | 0.26 | 0.00 | 0.01 | 0.02 | 0.01 | 0.03 | `cs_bucket_rank(cross_mean(sub(day_centroid(mul(Amt, is_gt0(Ret))), day_centroid(Amt)), 10), cross_mean(day_sum(Amt), 20))` |
| slot a seed 8 | 过 | 0.40 | `day_kurt(Ret)` | 0.72 | 0.04 | 0.04 | 0.01 | 0.03 | 0.09 | `cs_regres(day_centroid(Ret), day_centroid(Amt))` |
| slot a seed 9 | 过 | 0.54 | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(R` | 0.72 | 0.08 | 0.01 | 0.05 | 0.07 | 0.16 | `ts_mean(cs_regres(day_centroid(Ret), day_centroid(Amt)), 10)` |
| slot a seed 10 | 过 | 0.47 | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(R` | 0.62 | 0.24 | 0.28 | 0.09 | 0.27 | 0.22 | `cross_mean(sub(day_centroid(Ret), day_centroid(Amt)), 20)` |
| slot a seed 11 | 过 | 0.44 | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(R` | 0.60 | 0.01 | 0.23 | 0.07 | 0.03 | 0.08 | `cs_bucket_rank(cross_mean(sub(day_centroid(Ret), day_centroid(Amt)), 20), cross_mean(day_sum(Amt), 20))` |
| slot a seed 12 | 过 | 0.35 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.33 | 0.05 | 0.30 | 0.21 | 0.04 | 0.16 | `cs_bucket_rank(cross_stddev(day_centroid(Amt), 20), cross_mean(day_sum(Amt), 20))` |
| slot b seed 1 | 过 | 0.22 | `day_kurt(Ret)` | 0.40 | 0.04 | 0.04 | 0.14 | 0.04 | 0.04 | `div(day_sum(mul(Ret, abs_(Ret))), day_sum(mul(Ret, Ret)))` |
| slot b seed 2 | 过 | 0.23 | `day_kurt(Ret)` | 0.39 | 0.10 | 0.11 | 0.31 | 0.11 | 0.07 | `cross_mean(div(day_sum(mul(Ret, abs_(Ret))), day_sum(mul(Ret, Ret))), 5)` |
| slot b seed 3 | 过 | 0.22 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.36 | 0.08 | 0.10 | 0.29 | 0.10 | 0.07 | `div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 5), cross_sum(day_sum(mul(Ret, Ret)), 5))` |
| slot b seed 4 | 过 | 0.35 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.34 | 0.14 | 0.23 | 0.43 | 0.17 | 0.13 | `div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 20), cross_sum(day_sum(mul(Ret, Ret)), 20))` |
| slot b seed 5 | 过 | 0.34 | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(R` | 0.31 | 0.10 | 0.13 | 0.01 | 0.12 | 0.18 | `cs_bucket_rank(div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 20), cross_sum(day_sum(mul(Ret, Ret)), 20)), div(day_last(Close), cross_delay(day_last(Close), 20)))` |
| slot b seed 6 | 过 | 0.25 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.36 | 0.10 | 0.10 | 0.06 | 0.11 | 0.13 | `cs_bucket_rank(cross_mean(div(day_sum(mul(Ret, abs_(Ret))), day_sum(mul(Ret, Ret))), 5), div(day_last(Close), cross_delay(day_last(Close), 5)))` |
| slot b seed 7 | 过 | 0.19 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.24 | 0.01 | 0.09 | 0.27 | 0.03 | 0.08 | `cs_bucket_rank(div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 5), cross_sum(day_sum(mul(Ret, Ret)), 5)), cross_mean(day_zero_ratio(Ret), 20))` |
| slot b seed 8 | 过 | 0.38 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.34 | 0.03 | 0.18 | 0.41 | 0.00 | 0.23 | `cs_bucket_rank(div(cross_sum(day_sum(mul(Ret, abs_(Ret))), 20), cross_sum(day_sum(mul(Ret, Ret)), 20)), cross_mean(day_sum(Amt), 20))` |
| slot b seed 9 | 过 | 0.14 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.18 | 0.02 | 0.06 | 0.23 | 0.04 | 0.03 | `div(cross_sum(day_sum(mul(mul(Ret, abs_(Ret)), Amt)), 5), cross_sum(day_sum(mul(mul(Ret, Ret), Amt)), 5))` |
| slot b seed 10 | 过 | 0.25 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.38 | 0.10 | 0.09 | 0.18 | 0.10 | 0.09 | `cross_mean(mul(day_skew(Ret), sqrt(sub(1, day_zero_ratio(Ret)))), 5)` |
| R 1 variant 1 | 过 | 0.35 | `ts_skew(day_durbin_watson(Open), 50)` | 0.43 | 0.14 | 0.07 | 0.01 | 0.12 | 0.09 | `ts_skew(log(day_durbin_watson(Open)), 50)` |
| R 1 variant 2 | 过 | 0.54 | `ts_skew(day_durbin_watson(Open), 50)` | 0.64 | 0.13 | 0.02 | 0.01 | 0.10 | 0.18 | `ts_skew(div(day_durbin_watson(Open), cross_mean(day_durbin_watson(Open), 50)), 50)` |
| R 2 variant 1 | 过 | 0.97 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.96 | 0.15 | 0.12 | 0.09 | 0.12 | 0.40 | `cross_mean(day_kurt(Ret), 15)` |
| R 2 variant 2 | 过 | 0.99 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.97 | 0.14 | 0.14 | 0.09 | 0.10 | 0.36 | `cross_tail_mean_q75(day_kurt(Ret), 15)` |
| R 2 variant 3 | 过 | 0.80 | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3))` | 0.90 | 0.14 | 0.08 | 0.07 | 0.12 | 0.39 | `cross_quantile_q75(day_kurt(Ret), 15)` |
| R 2 variant 4 | 过 | 0.73 | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(R` | 0.84 | 0.14 | 0.04 | 0.06 | 0.13 | 0.39 | `cross_med(day_kurt(Ret), 15)` |
| R 3 variant 1 | 过 | 0.44 | `day_kurt(Ret)` | 0.56 | 0.18 | 0.01 | 0.00 | 0.17 | 0.18 | `sub(day_kurt(Ret), day_kurt(in_logchg(Vwap, 1)))` |
| R 3 variant 2 | 过 | 0.76 | `day_kurt(Ret)` | 0.66 | 0.19 | 0.01 | 0.02 | 0.18 | 0.25 | `cs_regres(cs_rank(day_kurt(Ret)), cs_rank(day_kurt(in_logchg(Vwap, 1))))` |
