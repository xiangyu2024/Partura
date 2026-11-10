# 相关度表:种子 2007,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.19 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.09 | 0.23 | 0.02 | 0.03 | 0.20 | 0.12 | `day_close(in_kurt_full(Amt))` |
| slot a seed 1 | 过 | 0.32 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.14 | 0.46 | 0.11 | 0.07 | 0.38 | 0.34 | `cross_mean(day_close(in_kurt_full(Amt)), 241)` |
| slot a seed 2 | 过 | 0.19 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.14 | 0.32 | 0.04 | 0.06 | 0.26 | 0.20 | `cross_stddev(day_close(in_kurt_full(Amt)), 120)` |
| slot a seed 3 | 过 | 0.36 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.14 | 0.49 | 0.12 | 0.07 | 0.41 | 0.34 | `cross_med(day_close(in_kurt_full(Amt)), 241)` |
| slot a seed 4 | 过 | 0.16 | `cross_sum(day_durbin_watson(Close), 60)` | 0.12 | 0.13 | 0.08 | 0.09 | 0.10 | 0.01 | `sub(cross_mean(day_close(in_kurt_full(Amt)), 20), cross_mean(day_close(in_kurt_full(Amt)), 241))` |
| slot a seed 5 | 过 | 0.16 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.14 | 0.25 | 0.08 | 0.08 | 0.17 | 0.02 | `cs_bucket_zscore(cross_mean(day_close(in_kurt_full(Amt)), 241), LogFloatCap)` |
| slot a seed 6 | 过 | 0.29 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.17 | 0.40 | 0.12 | 0.09 | 0.33 | 0.36 | `cs_bucket_zscore(cross_mean(day_close(in_kurt_full(Amt)), 120), sub(LogFloatCap, LogFloatShares))` |
| slot a seed 7 | 过 | 0.27 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cro` | 0.20 | 0.13 | 0.06 | 0.00 | 0.16 | 0.16 | `cross_corr(day_close(in_kurt_full(Amt)), ts_scale(day_sum(Amt), 30), 241)` |
| slot a seed 8 | 过 | 0.16 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cro` | 0.12 | 0.07 | 0.06 | 0.00 | 0.10 | 0.05 | `cross_corr(day_close(in_kurt_full(Amt)), day_sum(Ret), 241)` |
| slot a seed 9 | 过 | 0.35 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cro` | 0.14 | 0.30 | 0.08 | 0.01 | 0.31 | 0.02 | `cross_corr(day_close(in_kurt_full(Amt)), abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 241)` |
| slot a seed 10 | 过 | 0.06 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.02 | 0.05 | 0.00 | 0.00 | 0.05 | 0.02 | `cross_regbeta(ts_delay(day_close(in_kurt_full(Amt)), 1), day_sum(Ret), 241)` |
| slot a seed 11 | 过 | 0.28 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.14 | 0.42 | 0.09 | 0.07 | 0.35 | 0.31 | `cross_tail_mean_q75(day_close(in_kurt_full(Amt)), 241)` |
| slot a seed 12 | 过 | 0.24 | `cross_sum(day_durbin_watson(Close), 60)` | 0.14 | 0.07 | 0.18 | 0.00 | 0.10 | 0.13 | `cross_corr(day_close(in_kurt_full(Amt)), ts_delay(day_close(in_kurt_full(Amt)), 1), 120)` |
| slot a seed 13 | 过 | 0.25 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.13 | 0.32 | 0.07 | 0.08 | 0.25 | 0.03 | `cross_mean(sub(day_close(in_kurt_full(Amt)), day_close(in_kurt_full(Ret))), 241)` |
| slot a seed 14 | 过 | 0.19 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cro` | 0.16 | 0.06 | 0.06 | 0.00 | 0.09 | 0.18 | `cross_corr(day_close(in_kurt_full(Amt)), day_close(in_kurt_full(Ret)), 241)` |
| slot a seed 15 | 过 | 0.16 | `cross_sum(day_durbin_watson(Close), 60)` | 0.16 | 0.00 | 0.14 | 0.07 | 0.05 | 0.09 | `cross_mean(mul(day_close(in_kurt_full(Amt)), sign(day_sum(Ret))), 241)` |
| slot b seed 1 | 过 | 0.47 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.43 | 0.01 | 0.31 | 0.09 | 0.04 | 0.37 | `cross_stddev(ts_scale(day_sum(Amt), 30), 120)` |
| slot b seed 2 | 过 | 0.43 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.39 | 0.09 | 0.23 | 0.06 | 0.04 | 0.40 | `cross_stddev(cross_stddev(ts_scale(day_sum(Amt), 30), 10), 120)` |
| slot b seed 3 | 过 | 0.12 | `abs_(ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 1` | 0.38 | 0.20 | 0.13 | 0.23 | 0.24 | 0.27 | `sub(cross_stddev(ts_scale(day_sum(Amt), 30), 30), cross_stddev(ts_scale(day_sum(Amt), 30), 241))` |
| slot b seed 4 | 过 | 0.37 | `cross_sum(day_durbin_watson(Close), 60)` | 0.25 | 0.22 | 0.29 | 0.04 | 0.15 | 0.41 | `cross_stddev(day_centroid(Amt), 120)` |
| slot b seed 5 | 过 | 0.47 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.35 | 0.25 | 0.12 | 0.01 | 0.22 | 0.49 | `cross_stddev(day_centroid(pow_2(in_slice(Ret, 1, 240))), 120)` |
| slot b seed 6 | 过 | 0.42 | `cross_sum(day_durbin_watson(Close), 60)` | 0.24 | 0.10 | 0.33 | 0.01 | 0.12 | 0.09 | `cross_stddev(day_gini(Amt), 120)` |
| slot b seed 7 | 过 | 0.23 | `cross_sum(day_durbin_watson(Close), 60)` | 0.20 | 0.29 | 0.18 | 0.05 | 0.21 | 0.34 | `cross_stddev(day_es_ratio_hi(Amt), 120)` |
| slot b seed 8 | 过 | 0.19 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cro` | 0.14 | 0.10 | 0.04 | 0.01 | 0.14 | 0.01 | `div(cross_stddev(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 120), add(cross_stddev(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 120), cross_stddev(day_sum(Ret), 120)))` |
| slot b seed 9 | 过 | 0.10 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.10 | 0.06 | 0.04 | 0.00 | 0.06 | 0.06 | `cross_stddev(cross_corr(ts_scale(day_sum(Amt), 30), day_sum(Ret), 60), 120)` |
| slot b seed 10 | 过 | 0.13 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.11 | 0.04 | 0.06 | 0.00 | 0.05 | 0.10 | `cross_stddev(cross_corr(day_sum(Ret), cs_mean(day_sum(Ret)), 60), 120)` |
| slot b seed 11 | 过 | 0.34 | `cross_sum(day_durbin_watson(Close), 60)` | 0.25 | 0.06 | 0.28 | 0.06 | 0.11 | 0.01 | `cs_bucket_zscore(cross_stddev(day_centroid(Amt), 120), LogFloatCap)` |
| slot b seed 12 | 过 | 0.46 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.41 | 0.04 | 0.31 | 0.08 | 0.08 | 0.32 | `cs_bucket_zscore(cross_stddev(ts_scale(day_sum(Amt), 30), 120), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 13 | 过 | 0.36 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.24 | 0.12 | 0.20 | 0.03 | 0.07 | 0.36 | `cross_stddev(day_zero_ratio(Ret), 120)` |
| slot b seed 14 | 过 | 0.32 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.23 | 0.36 | 0.01 | 0.01 | 0.34 | 0.47 | `cross_stddev(day_signed_ratio(Ret, Amt), 120)` |
| slot b seed 15 | 过 | 0.37 | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` | 0.25 | 0.03 | 0.09 | 0.01 | 0.04 | 0.21 | `cross_stddev(day_durbin_watson(Ret), 120)` |
| slot b seed 16 | 过 | 0.67 | `cross_sum(day_durbin_watson(Close), 60)` | 0.42 | 0.39 | 0.53 | 0.04 | 0.39 | 0.14 | `cross_stddev(div(day_close(Close), day_wmean(Close, Amt)), 120)` |
| R 1 variant 1 | 过 | 0.17 | `cross_sum(day_durbin_watson(Close), 60)` | 0.20 | 0.34 | 0.17 | 0.01 | 0.32 | 0.26 | `div(ts_std(day_close(cross_decay_linear(Amt, 30)), 120), ts_std(day_sum(cross_decay_linear(Amt, 30)), 120))` |
| R 1 variant 2 | 过 | 0.17 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` | 0.15 | 0.33 | 0.15 | 0.03 | 0.31 | 0.26 | `div(ts_std(day_close(cross_decay_linear(Amt, 30)), 241), ts_std(day_sum(cross_decay_linear(Amt, 30)), 241))` |
| R 1 variant 3 | 过 | 0.26 | `cross_sum(day_durbin_watson(Close), 60)` | 0.39 | 0.07 | 0.16 | 0.01 | 0.04 | 0.30 | `ts_std(log(add(day_close(cross_decay_linear(Amt, 30)), 1)), 120)` |
| R 1 variant 4 | 过 | 0.57 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cro` | 0.40 | 0.46 | 0.10 | 0.00 | 0.48 | 0.35 | `ts_std(day_close(cross_decay_linear(Volume, 30)), 120)` |
| R 1 variant 5 | 过 | 0.47 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cro` | 0.27 | 0.41 | 0.06 | 0.01 | 0.44 | 0.34 | `ts_std(day_close(cross_decay_linear(Volume, 30)), 241)` |
| R 2 variant 1 | 过 | 0.15 | `cross_sum(day_durbin_watson(Close), 60)` | 0.20 | 0.20 | 0.14 | 0.01 | 0.20 | 0.10 | `div(ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 10), 120), ts_std(ts_std(day_sum(cross_decay_linear(Amt, 30)), 10), 120))` |
| R 2 variant 2 | 过 | 0.57 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cro` | 0.42 | 0.46 | 0.11 | 0.01 | 0.49 | 0.34 | `abs_(ts_std(ts_std(day_close(cross_decay_linear(Volume, 30)), 10), 120))` |
