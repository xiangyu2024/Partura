# 相关度表:种子 2009,P 组,第 3 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.04 | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(R` | 0.06 | 0.02 | 0.03 | 0.15 | 0.02 | 0.01 | `sub(day_wmean(Ret, Amt), day_mean(Ret))` |
| slot a seed 1 | 过 | 0.40 | `ts_max(day_durbin_watson(Close), 80)` | 0.22 | 0.15 | 0.34 | 0.05 | 0.19 | 0.14 | `cross_mean(cs_robust_z(sub(day_wmean(Ret, Amt), day_mean(Ret))), 241)` |
| slot a seed 2 | 过 | 0.44 | `ts_max(day_durbin_watson(Close), 80)` | 0.23 | 0.18 | 0.40 | 0.06 | 0.22 | 0.14 | `cross_mean(cs_winsor(sub(day_wmean(Ret, Amt), day_mean(Ret))), 241)` |
| slot a seed 3 | 过 | 0.33 | `ts_max(day_durbin_watson(Close), 80)` | 0.18 | 0.17 | 0.30 | 0.08 | 0.21 | 0.07 | `cross_mean(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), add(day_std(Ret), 0.00001)), 241)` |
| slot a seed 4 | 过 | 0.27 | `ts_max(day_durbin_watson(Close), 80)` | 0.17 | 0.14 | 0.14 | 0.08 | 0.18 | 0.10 | `cross_mean(cs_bucket_zscore(sub(day_wmean(Ret, Amt), day_mean(Ret)), cross_mean(day_std(Ret), 20)), 241)` |
| slot a seed 5 | 过 | 0.38 | `ts_max(day_durbin_watson(Close), 80)` | 0.24 | 0.28 | 0.34 | 0.05 | 0.31 | 0.01 | `cross_mean(cs_bucket_demean(sub(day_wmean(Ret, Amt), day_mean(Ret)), LogFloatCap), 241)` |
| slot a seed 6 | 过 | 0.25 | `ts_max(day_durbin_watson(Close), 80)` | 0.17 | 0.10 | 0.11 | 0.08 | 0.13 | 0.12 | `cross_mean(cs_bucket_demean(sub(day_wmean(Ret, Amt), day_mean(Ret)), cross_mean(day_std(Ret), 20)), 241)` |
| slot a seed 7 | 过 | 0.45 | `ts_max(day_durbin_watson(Close), 80)` | 0.26 | 0.15 | 0.38 | 0.05 | 0.20 | 0.18 | `cross_mean(cs_bucket_demean(sub(day_wmean(Ret, Amt), day_mean(Ret)), cross_mean(day_sum(Amt), 30)), 241)` |
| slot a seed 8 | 过 | 0.23 | `ts_max(day_durbin_watson(Close), 20)` | 0.12 | 0.19 | 0.27 | 0.10 | 0.21 | 0.03 | `cross_mean(cs_bucket_rank(sub(day_wmean(Ret, Amt), day_mean(Ret)), cross_mean(day_std(Amt), 30)), 241)` |
| slot a seed 9 | 过 | 0.41 | `ts_max(day_durbin_watson(Close), 80)` | 0.25 | 0.09 | 0.35 | 0.07 | 0.13 | 0.16 | `cross_mean(cs_bucket_demean(cs_bucket_demean(sub(day_wmean(Ret, Amt), day_mean(Ret)), LogFloatCap), cross_mean(day_std(Amt), 30)), 241)` |
| slot a seed 10 | 过 | 0.23 | `ts_max(day_durbin_watson(Close), 20)` | 0.13 | 0.03 | 0.20 | 0.52 | 0.06 | 0.02 | `cross_zscore(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 20), 241)` |
| slot a seed 11 | 过 | 0.46 | `ts_max(day_durbin_watson(Close), 80)` | 0.24 | 0.12 | 0.38 | 0.05 | 0.17 | 0.22 | `cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 240)` |
| slot a seed 12 | 过 | 0.50 | `ts_max(day_durbin_watson(Close), 80)` | 0.29 | 0.17 | 0.44 | 0.10 | 0.23 | 0.17 | `cross_decay_linear(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241)` |
| slot a seed 13 | 过 | 0.42 | `ts_max(day_durbin_watson(Close), 80)` | 0.21 | 0.12 | 0.34 | 0.03 | 0.16 | 0.21 | `ts_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 482)` |
| slot a seed 14 | 过 | 0.31 | `ts_quantile_q75(sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day` | 0.14 | 0.36 | 0.20 | 0.06 | 0.36 | 0.19 | `ts_mean(cs_rank(sub(day_wmean(Ret, Amt), day_mean(Ret))), 482)` |
| slot a seed 15 | 过 | 0.23 | `ts_max(day_durbin_watson(Close), 80)` | 0.08 | 0.18 | 0.20 | 0.00 | 0.16 | 0.34 | `cross_cov(sub(day_wmean(Ret, Amt), day_mean(Ret)), cs_mean(day_sum(Ret)), 241)` |
| slot a seed 16 | 过 | 0.22 | `ts_max(day_durbin_watson(Close), 80)` | 0.21 | 0.08 | 0.12 | 0.00 | 0.10 | 0.01 | `cross_corr(sub(day_wmean(Ret, Amt), day_mean(Ret)), cs_mean(day_sum(Ret)), 241)` |
| slot b seed 1 | 过 | 0.18 | `ts_max(day_durbin_watson(Close), 80)` | 0.19 | 0.01 | 0.11 | 0.08 | 0.03 | 0.18 | `cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 241)` |
| slot b seed 2 | 过 | 0.30 | `ts_max(day_durbin_watson(Close), 80)` | 0.25 | 0.22 | 0.29 | 0.07 | 0.24 | 0.07 | `cross_mean(cs_winsor(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1))), 241)` |
| slot b seed 3 | 过 | 0.28 | `ts_max(day_durbin_watson(Close), 80)` | 0.24 | 0.21 | 0.28 | 0.07 | 0.23 | 0.06 | `cross_mean(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 241)` |
| slot b seed 4 | 过 | 0.32 | `ts_max(day_durbin_watson(Close), 80)` | 0.25 | 0.24 | 0.32 | 0.12 | 0.26 | 0.06 | `cross_ema(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 120)` |
| slot b seed 5 | 过 | 0.26 | `ts_max(day_durbin_watson(Close), 80)` | 0.23 | 0.17 | 0.25 | 0.05 | 0.18 | 0.09 | `ts_mean(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 482)` |
| slot b seed 6 | 过 | 0.33 | `ts_max(day_durbin_watson(Close), 80)` | 0.25 | 0.26 | 0.33 | 0.13 | 0.27 | 0.04 | `cross_decay_linear(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 241)` |
| slot b seed 7 | 过 | 0.09 | `ts_max(day_durbin_watson(Close), 80)` | 0.11 | 0.03 | 0.05 | 0.07 | 0.02 | 0.13 | `div(cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 241), add(cross_stddev(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 241), 0.001))` |
| slot b seed 8 | 过 | 0.19 | `ts_quantile_q75(sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day` | 0.12 | 0.21 | 0.11 | 0.01 | 0.19 | 0.19 | `cross_corr(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1), 241)` |
| slot b seed 9 | 过 | 0.21 | `ts_max(day_durbin_watson(Close), 80)` | 0.12 | 0.08 | 0.15 | 0.00 | 0.11 | 0.08 | `cross_corr(ts_delay(sub(div(day_last(Close), day_first(Open)), 1), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 241)` |
| slot b seed 10 | 过 | 0.22 | `ts_max(day_durbin_watson(Close), 80)` | 0.14 | 0.04 | 0.09 | 0.02 | 0.08 | 0.14 | `div(cross_stddev(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 241), add(cross_stddev(sub(div(day_last(Close), day_first(Open)), 1), 241), 0.001))` |
| slot b seed 11 | 过 | 0.17 | `ts_max(day_durbin_watson(Close), 80)` | 0.18 | 0.01 | 0.10 | 0.08 | 0.03 | 0.16 | `cross_mean(div(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), LimitWidth), 241)` |
| slot b seed 12 | 过 | 0.27 | `ts_max(day_durbin_watson(Close), 80)` | 0.23 | 0.21 | 0.27 | 0.07 | 0.23 | 0.04 | `cross_mean(div(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), LimitWidth), 241)` |
| slot b seed 13 | 过 | 0.19 | `ts_max(day_durbin_watson(Close), 20)` | 0.16 | 0.07 | 0.18 | 0.51 | 0.08 | 0.01 | `cross_zscore(cross_mean(sub(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), sub(div(day_last(Close), day_first(Open)), 1)), 20), 241)` |
| slot b seed 14 | 过 | 0.22 | `ts_max(day_durbin_watson(Close), 80)` | 0.12 | 0.11 | 0.18 | 0.01 | 0.09 | 0.19 | `cross_mean(mul(sign(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), sub(div(day_last(Close), day_first(Open)), 1)), 241)` |
| slot b seed 15 | 过 | 0.22 | `ts_max(day_durbin_watson(Close), 80)` | 0.17 | 0.16 | 0.11 | 0.02 | 0.20 | 0.05 | `div(cross_mean(abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 241), add(cross_mean(abs_(sub(div(day_last(Close), day_first(Open)), 1)), 241), 0.0001))` |
| slot b seed 16 | 过 | 0.23 | `ts_max(day_durbin_watson(Close), 80)` | 0.13 | 0.01 | 0.14 | 0.02 | 0.03 | 0.15 | `cross_autocorr(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 241, 1)` |
| R 1 variant 1 | 过 | 0.95 | `ts_max(day_durbin_watson(Close), 80)` | 0.90 | 0.12 | 0.60 | 0.01 | 0.17 | 0.35 | `ts_max(cs_rank(day_durbin_watson(Close)), 80)` |
| R 1 variant 2 | 过 | 0.69 | `ts_max(day_durbin_watson(Close), 80)` | 0.48 | 0.02 | 0.44 | 0.03 | 0.02 | 0.47 | `ts_max(cs_rank(day_durbin_watson(Close)), 241)` |
| R 1 variant 3 | 过 | 0.62 | `ts_max(day_durbin_watson(Close), 20)` | 0.37 | 0.23 | 0.83 | 0.00 | 0.28 | 0.10 | `ts_mean(cs_rank(day_durbin_watson(Close)), 80)` |
| R 1 variant 4 | 过 | 0.53 | `ts_max(day_durbin_watson(Close), 20)` | 0.25 | 0.18 | 0.72 | 0.02 | 0.21 | 0.14 | `ts_mean(cs_rank(day_durbin_watson(Close)), 241)` |
| R 1 variant 5 | 过 | 0.79 | `ts_max(day_durbin_watson(Close), 80)` | 0.63 | 0.24 | 0.83 | 0.01 | 0.30 | 0.20 | `ts_mean(day_durbin_watson(Close), 80)` |
| R 1 variant 6 | 过 | 0.70 | `ts_max(day_durbin_watson(Close), 80)` | 0.47 | 0.27 | 0.82 | 0.00 | 0.31 | 0.17 | `ts_quantile_q75(day_durbin_watson(Close), 80)` |
| R 1 variant 7 | 过 | 0.93 | `ts_max(day_durbin_watson(Close), 80)` | 0.88 | 0.19 | 0.66 | 0.00 | 0.24 | 0.29 | `ts_max(cross_mean(day_durbin_watson(Close), 5), 80)` |
| R 2 variant 1 | 过 | 0.61 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50)` | 0.62 | 0.09 | 0.09 | 0.00 | 0.12 | 0.11 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), day_durbin_watson(Low)), 241)` |
| R 2 variant 2 | 过 | 0.62 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50)` | 0.61 | 0.01 | 0.11 | 0.00 | 0.05 | 0.11 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Volume), 50), day_durbin_watson(Low)), 241)` |
| R 2 variant 3 | 过 | 0.47 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50)` | 0.46 | 0.07 | 0.08 | 0.01 | 0.10 | 0.14 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), day_durbin_watson(Low)), 482)` |
| R 2 variant 4 | 过 | 0.48 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50)` | 0.45 | 0.02 | 0.13 | 0.00 | 0.03 | 0.13 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Volume), 50), day_durbin_watson(Low)), 482)` |
| R 2 variant 5 | 过 | 0.63 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50)` | 0.63 | 0.08 | 0.10 | 0.01 | 0.11 | 0.13 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), day_durbin_watson(Close)), 241)` |
| R 3 variant 1 | 过 | 0.70 | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(R` | 0.86 | 0.31 | 0.03 | 0.04 | 0.27 | 0.12 | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret))))), 120)` |
| R 3 variant 2 | 过 | 0.67 | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(R` | 0.80 | 0.27 | 0.07 | 0.04 | 0.22 | 0.14 | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret))))), 241)` |
| R 3 variant 3 | 过 | 0.64 | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(R` | 0.74 | 0.21 | 0.09 | 0.04 | 0.17 | 0.19 | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret))))), 482)` |
