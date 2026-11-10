# 相关度表:种子 2007,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | inf | `log(day_durbin_watson(Vwap))` | 0.36 | 0.05 | 0.10 | 0.07 | 0.06 | 0.06 | `ts_scale(day_durbin_watson(Vwap), 10)` |
| slot a seed 1 | 过 | 0.25 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.49 | 0.05 | 0.18 | 0.03 | 0.09 | 0.34 | `cross_stddev(ts_scale(day_durbin_watson(Vwap), 10), 60)` |
| slot a seed 2 | 过 | 0.19 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.36 | 0.08 | 0.12 | 0.03 | 0.06 | 0.46 | `cross_stddev(ts_scale(day_durbin_watson(Vwap), 10), 241)` |
| slot a seed 3 | 过 | 0.23 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.52 | 0.04 | 0.11 | 0.01 | 0.02 | 0.35 | `cross_semistd_pos(ts_scale(day_durbin_watson(Vwap), 10), 60)` |
| slot a seed 4 | 过 | 0.14 | `log(day_durbin_watson(Vwap))` | 0.04 | 0.07 | 0.00 | 0.04 | 0.07 | 0.03 | `sub(cross_semistd_pos(ts_scale(day_durbin_watson(Vwap), 10), 60), cross_semistd_neg(ts_scale(day_durbin_watson(Vwap), 10), 60))` |
| slot a seed 5 | 过 | 0.32 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.56 | 0.10 | 0.24 | 0.09 | 0.13 | 0.31 | `cross_tail_mean_q75(ts_scale(day_durbin_watson(Vwap), 10), 60)` |
| slot a seed 6 | 过 | 0.03 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.09 | 0.07 | 0.01 | 0.01 | 0.05 | 0.13 | `ts_kurt(ts_scale(day_durbin_watson(Vwap), 10), 50)` |
| slot a seed 7 | 过 | 0.09 | `cross_sum(day_durbin_watson(Close), 60)` | 0.07 | 0.25 | 0.05 | 0.01 | 0.24 | 0.07 | `cross_corr(ts_scale(day_durbin_watson(Vwap), 10), ts_delay(ts_scale(day_durbin_watson(Vwap), 10), 1), 60)` |
| slot a seed 8 | 过 | 0.19 | `cross_sum(day_durbin_watson(Close), 60)` | 0.08 | 0.20 | 0.17 | 0.11 | 0.21 | 0.01 | `cross_corr(ts_scale(day_durbin_watson(Vwap), 10), day_sum(Ret), 60)` |
| slot a seed 9 | 过 | 0.30 | `cross_sum(day_durbin_watson(Close), 60)` | 0.16 | 0.28 | 0.23 | 0.08 | 0.29 | 0.02 | `cross_corr(ts_scale(day_durbin_watson(Vwap), 10), ts_delay(day_sum(Ret), 1), 60)` |
| slot a seed 10 | 过 | 0.16 | `cross_sum(day_durbin_watson(Close), 60)` | 0.08 | 0.10 | 0.13 | 0.09 | 0.12 | 0.01 | `cross_corr(ts_scale(day_durbin_watson(Vwap), 10), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot a seed 11 | 过 | 0.22 | `cross_sum(day_durbin_watson(Close), 60)` | 0.11 | 0.36 | 0.17 | 0.04 | 0.38 | 0.04 | `cross_corr(ts_scale(day_durbin_watson(Vwap), 10), ts_scale(day_sum(Amt), 10), 60)` |
| slot a seed 12 | 过 | 0.12 | `cross_sum(day_durbin_watson(Close), 60)` | 0.10 | 0.12 | 0.11 | 0.01 | 0.13 | 0.04 | `cross_corr(ts_scale(day_durbin_watson(Vwap), 10), ts_scale(day_durbin_watson(Volume), 10), 60)` |
| slot a seed 13 | 过 | 0.24 | `cross_sum(day_durbin_watson(Close), 60)` | 0.35 | 0.12 | 0.22 | 0.01 | 0.10 | 0.16 | `cross_regbeta(abs_(day_sum(Ret)), ts_scale(day_durbin_watson(Vwap), 10), 60)` |
| slot a seed 14 | 过 | 0.18 | `cross_sum(day_durbin_watson(Close), 60)` | 0.07 | 0.30 | 0.15 | 0.07 | 0.30 | 0.08 | `cross_corr(ts_scale(day_durbin_watson(Vwap), 10), day_signed_ratio(Ret, Amt), 60)` |
| slot a seed 15 | 过 | 0.43 | `log(day_durbin_watson(Vwap))` | 0.14 | 0.05 | 0.11 | 0.03 | 0.05 | 0.01 | `cross_madz(ts_scale(day_durbin_watson(Vwap), 10), 60)` |
| slot a seed 16 | 过 | 0.06 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.04 | 0.15 | 0.01 | 0.01 | 0.13 | 0.29 | `cross_corr(ts_scale(day_durbin_watson(Vwap), 10), day_max(Ret), 241)` |
| slot b seed 1 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.33 | 0.37 | 0.21 | 0.03 | 0.36 | 0.08 | `cross_mean(day_centroid(in_slice(Ret, 1, 240)), 40)` |
| slot b seed 2 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.31 | 0.38 | 0.13 | 0.01 | 0.35 | 0.04 | `cross_mean(day_centroid(pow_2(in_slice(Ret, 1, 240))), 40)` |
| slot b seed 3 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.26 | 0.56 | 0.07 | 0.00 | 0.52 | 0.18 | `cross_mean(div(day_sum(in_slice(pow_2(Ret), 211, 240)), day_sum(in_slice(pow_2(Ret), 1, 240))), 40)` |
| slot b seed 4 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.29 | 0.24 | 0.14 | 0.01 | 0.23 | 0.15 | `cross_mean(div(day_sum(in_slice(pow_2(Ret), 1, 30)), day_sum(in_slice(pow_2(Ret), 1, 240))), 40)` |
| slot b seed 5 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.22 | 0.07 | 0.09 | 0.00 | 0.07 | 0.23 | `cross_mean(div(day_sum(in_slice(pow_2(Ret), 121, 150)), day_sum(in_slice(pow_2(Ret), 1, 240))), 40)` |
| slot b seed 6 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.30 | 0.35 | 0.15 | 0.04 | 0.34 | 0.07 | `sub(cross_mean(div(day_sum(in_slice(pow_2(Ret), 211, 240)), day_sum(in_slice(pow_2(Ret), 1, 240))), 30), cross_mean(div(day_sum(in_slice(pow_2(Ret), 1, 30)), day_sum(in_slice(pow_2(Ret), 1, 240))), 30))` |
| slot b seed 7 | 过 | 0.13 | `cross_sum(day_durbin_watson(Close), 60)` | 0.31 | 0.40 | 0.09 | 0.00 | 0.36 | 0.03 | `cross_mean(sub(log(day_durbin_watson(in_slice(Vwap, 1, 120))), log(day_durbin_watson(in_slice(Vwap, 121, 240)))), 40)` |
| slot b seed 8 | 过 | 0.14 | `cross_sum(day_durbin_watson(Close), 60)` | 0.21 | 0.41 | 0.09 | 0.01 | 0.42 | 0.03 | `cross_mean(div(pow_2(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), add(pow_2(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), day_sum(in_slice(pow_2(Ret), 1, 240)))), 40)` |
| slot b seed 9 | 过 | 0.10 | `cross_sum(day_durbin_watson(Close), 60)` | 0.16 | 0.32 | 0.04 | 0.01 | 0.33 | 0.04 | `div(cross_sum(pow_2(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 60), add(cross_sum(pow_2(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 60), cross_sum(day_sum(in_slice(pow_2(Ret), 1, 240)), 60)))` |
| slot b seed 10 | 过 | 0.18 | `log(day_durbin_watson(Vwap))` | 0.18 | 0.01 | 0.04 | 0.10 | 0.02 | 0.01 | `cross_zscore(div(day_sum(in_slice(pow_2(Ret), 211, 240)), day_sum(in_slice(pow_2(Ret), 1, 240))), 60)` |
| slot b seed 11 | 过 | 0.12 | `cross_sum(day_durbin_watson(Close), 60)` | 0.06 | 0.13 | 0.10 | 0.10 | 0.14 | 0.03 | `cross_corr(day_centroid(in_slice(Ret, 1, 240)), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 12 | 过 | 0.29 | `cross_sum(day_durbin_watson(Close), 60)` | 0.13 | 0.30 | 0.29 | 0.17 | 0.30 | 0.01 | `cross_mean(sub(day_sum(in_slice(Ret, 211, 240)), day_sum(in_slice(Ret, 1, 30))), 60)` |
| slot b seed 13 | 过 | 0.29 | `cross_sum(day_durbin_watson(Close), 60)` | 0.18 | 0.25 | 0.22 | 0.03 | 0.28 | 0.08 | `cross_corr(day_centroid(in_slice(Ret, 1, 240)), day_centroid(Amt), 60)` |
| slot b seed 14 | 过 | 0.07 | `cross_sum(day_durbin_watson(Close), 60)` | 0.04 | 0.01 | 0.03 | 0.10 | 0.02 | 0.12 | `cross_mean(day_signed_ratio(in_slice(Ret, 211, 240), in_slice(Amt, 211, 240)), 60)` |
| slot b seed 15 | 过 | 0.38 | `cross_sum(day_durbin_watson(Close), 60)` | 0.18 | 0.26 | 0.36 | 0.20 | 0.28 | 0.01 | `cross_mean(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), day_sum(in_slice(Ret, 1, 240))), 60)` |
| slot b seed 16 | 过 | 0.07 | `cross_sum(day_durbin_watson(Close), 60)` | 0.06 | 0.07 | 0.07 | 0.02 | 0.08 | 0.07 | `cross_regbeta(day_sum(in_slice(Ret, 1, 30)), day_sum(in_slice(Ret, 211, 240)), 60)` |
| R 1 variant 1 | 过 | inf | `log(day_durbin_watson(Vwap))` | 0.83 | 0.01 | 0.20 | 0.34 | 0.04 | 0.17 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 20)` |
| R 1 variant 2 | 过 | inf | `log(day_durbin_watson(Vwap))` | 0.52 | 0.07 | 0.23 | 0.10 | 0.11 | 0.30 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` |
| R 1 variant 3 | 过 | inf | `log(day_durbin_watson(Vwap))` | 0.72 | 0.00 | 0.24 | 0.39 | 0.04 | 0.12 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 20), 20)` |
| R 1 variant 4 | 过 | 0.45 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.75 | 0.04 | 0.20 | 0.20 | 0.08 | 0.23 | `cross_stddev(ts_scale(day_durbin_watson(Vwap), 10), 20)` |
| R 1 variant 5 | 过 | 0.23 | `cross_sum(day_durbin_watson(Close), 60)` | 0.52 | 0.04 | 0.20 | 0.01 | 0.07 | 0.37 | `cross_ema(cross_stddev(ts_scale(day_durbin_watson(Vwap), 10), 20), 20)` |
| R 1 variant 6 | 过 | 0.32 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.62 | 0.00 | 0.13 | 0.07 | 0.02 | 0.27 | `cross_semistd_pos(ts_scale(day_durbin_watson(Vwap), 10), 20)` |
| R 2 variant 1 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.45 | 0.06 | 0.08 | 0.01 | 0.05 | 0.35 | `cross_sum(sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap))), 60)` |
| R 2 variant 2 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.24 | 0.26 | 0.46 | 0.02 | 0.28 | 0.22 | `cross_sum(cs_regres(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap))), 60)` |
| R 2 variant 3 | 过 | inf | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 10)` | 0.68 | 0.22 | 0.65 | 0.03 | 0.17 | 0.43 | `cs_bucket_demean(cross_sum(log(day_durbin_watson(Close)), 60), cross_mean(day_std(Amt), 30))` |
| R 3 variant 1 | 过 | 0.40 | `log(day_durbin_watson(Vwap))` | 0.40 | 0.14 | 0.55 | 0.32 | 0.19 | 0.07 | `sub(cross_mean(log(day_durbin_watson(Vwap)), 20), cross_mean(log(day_durbin_watson(Vwap)), 241))` |
| R 3 variant 2 | 过 | 0.19 | `log(day_durbin_watson(Vwap))` | 0.42 | 0.10 | 0.05 | 0.01 | 0.10 | 0.38 | `cross_ema(sub(log(day_durbin_watson(Vwap)), log(day_durbin_watson(Close))), 60)` |
| R 3 variant 3 | 过 | 0.72 | `log(day_durbin_watson(Vwap))` | 0.14 | 0.03 | 0.28 | 0.36 | 0.06 | 0.05 | `cross_zscore(log(day_durbin_watson(Vwap)), 241)` |
