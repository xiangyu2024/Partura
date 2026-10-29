# 相关度表:种子 807,C 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 8 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.27 | `cross_mean(cs_winsor(pow_2(day_wmean(Ret, Ret))), 10)` | 0.08 | 0.13 | 0.28 | 0.53 | 0.15 | 0.02 | `sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), cross_mean(log(div(day_last(Close), day_first(Open))), 20))` |
| slot a seed 2 | 过 | 0.32 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.16 | 0.21 | 0.33 | 0.20 | 0.23 | 0.05 | `sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60), cross_mean(log(div(day_last(Close), day_first(Open))), 60))` |
| slot a seed 3 | 过 | 0.31 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.14 | 0.19 | 0.31 | 0.12 | 0.21 | 0.08 | `sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 120), cross_mean(log(div(day_last(Close), day_first(Open))), 120))` |
| slot a seed 4 | 过 | 0.29 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.12 | 0.16 | 0.28 | 0.08 | 0.17 | 0.11 | `sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 241), cross_mean(log(div(day_last(Close), day_first(Open))), 241))` |
| slot a seed 5 | 过 | 0.23 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.13 | 0.04 | 0.13 | 0.14 | 0.05 | 0.17 | `cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60)` |
| slot a seed 6 | 过 | 0.23 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.13 | 0.05 | 0.16 | 0.08 | 0.04 | 0.26 | `cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 241)` |
| slot a seed 7 | 过 | 0.33 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.15 | 0.29 | 0.37 | 0.24 | 0.31 | 0.01 | `cross_mean(log(div(day_last(Close), day_first(Open))), 120)` |
| slot a seed 8 | 过 | 0.26 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.12 | 0.16 | 0.27 | 0.20 | 0.18 | 0.04 | `div(sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60), cross_mean(log(div(day_last(Close), day_first(Open))), 60)), add(cross_mean(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), 60), cross_mean(abs_(log(div(day_last(Close), day_first(Open)))), 60)))` |
| slot a seed 9 | 过 | 0.21 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.07 | 0.10 | 0.23 | 0.09 | 0.12 | 0.07 | `div(sub(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 241), cross_mean(log(div(day_last(Close), day_first(Open))), 241)), add(cross_mean(abs_(log(div(day_first(Open), ts_delay(day_last(Close), 1)))), 241), cross_mean(abs_(log(div(day_last(Close), day_first(Open)))), 241)))` |
| slot a seed 10 | 过 | 0.23 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.13 | 0.05 | 0.14 | 0.12 | 0.05 | 0.17 | `cs_regres(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60), cross_mean(log(div(day_last(Close), day_first(Open))), 60))` |
| slot a seed 11 | 过 | 0.23 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.11 | 0.03 | 0.16 | 0.07 | 0.04 | 0.20 | `cs_regres(cross_mean(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 120), cross_mean(log(div(day_last(Close), day_first(Open))), 120))` |
| slot a seed 12 | 过 | 0.11 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.10 | 0.18 | 0.07 | 0.02 | 0.16 | 0.13 | `cross_corr(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open))), 60)` |
| slot a seed 13 | 过 | 0.15 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.12 | 0.20 | 0.09 | 0.01 | 0.17 | 0.16 | `cross_corr(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open))), 120)` |
| slot a seed 14 | 过 | 0.10 | `ts_sum(LogFloatShares, 30)` | 0.09 | 0.18 | 0.06 | 0.02 | 0.16 | 0.12 | `cross_regbeta(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(day_last(Close), day_first(Open))), 60)` |
| slot b seed 1 | 废品 | 0.15 | `ts_sum(LogFloatShares, 30)` | 0.14 | 0.03 | 0.12 | 0.02 | 0.03 | 0.07 | `ts_delta(sub(LogFloatCap, log(day_last(Close))), 120)` |
| slot b seed 2 | 废品 | 0.25 | `ts_sum(LogFloatShares, 30)` | 0.19 | 0.01 | 0.13 | 0.02 | 0.01 | 0.12 | `ts_delta(sub(LogFloatCap, log(day_last(Close))), 241)` |
| slot b seed 3 | 废品 | 0.14 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.07 | 0.03 | 0.14 | 0.02 | 0.04 | 0.06 | `ts_delta(sub(LogTotalCap, log(day_last(Close))), 120)` |
| slot b seed 4 | 废品 | 0.21 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.08 | 0.05 | 0.21 | 0.02 | 0.06 | 0.11 | `ts_delta(sub(LogTotalCap, log(day_last(Close))), 241)` |
| slot b seed 5 | 废品 | 0.15 | `ts_sum(LogFloatShares, 30)` | 0.14 | 0.03 | 0.11 | 0.02 | 0.03 | 0.07 | `cs_regres(ts_delta(sub(LogFloatCap, log(day_last(Close))), 120), ts_delta(sub(LogTotalCap, log(day_last(Close))), 120))` |
| slot b seed 6 | 废品 | 0.25 | `ts_sum(LogFloatShares, 30)` | 0.19 | 0.01 | 0.12 | 0.02 | 0.01 | 0.12 | `cs_regres(ts_delta(sub(LogFloatCap, log(day_last(Close))), 241), ts_delta(sub(LogTotalCap, log(day_last(Close))), 241))` |
| slot b seed 7 | 废品 | 0.42 | `ts_sum(LogFloatShares, 30)` | 0.18 | 0.02 | 0.06 | 0.01 | 0.01 | 0.31 | `add(sub(LogTotalCap, LogFloatCap), ts_delta(sub(LogTotalCap, log(day_last(Close))), 241))` |
| slot b seed 8 | 废品 | 0.26 | `ts_sum(LogFloatShares, 30)` | 0.20 | 0.01 | 0.12 | 0.02 | 0.01 | 0.13 | `cross_mean(ts_delta(sub(LogFloatCap, log(day_last(Close))), 241), 20)` |
| slot b seed 9 | 废品 | 0.21 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.08 | 0.04 | 0.21 | 0.02 | 0.06 | 0.12 | `cross_mean(ts_delta(sub(LogTotalCap, log(day_last(Close))), 241), 20)` |
| slot b seed 10 | 废品 | 0.08 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.11 | 0.03 | 0.07 | 0.01 | 0.03 | 0.02 | `ts_delta(sub(LogFloatCap, log(day_last(Close))), 60)` |
| R 1 variant 1 | 过 | 1.00 | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1` | 1.00 | 0.09 | 0.68 | 0.29 | 0.13 | 0.17 | `ts_sum(pow_2_5(ts_sum(pow_3(mul(day_durbin_watson(High), 1000.0)), 1)), 1)` |
| R 1 variant 2 | 过 | 0.91 | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1` | 0.78 | 0.16 | 0.72 | 0.29 | 0.21 | 0.06 | `ts_sum(pow_2_5(ts_sum(pow_3(day_std(Ret)), 1)), 1)` |
| R 2 variant 1 | 过 | 0.72 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.83 | 0.01 | 0.09 | 0.00 | 0.04 | 0.28 | `ts_sum(div(cross_stddev(day_durbin_watson(High), 60), cross_mean(day_durbin_watson(High), 60)), 1)` |
| R 2 variant 2 | 过 | 0.74 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.76 | 0.05 | 0.18 | 0.01 | 0.09 | 0.36 | `ts_sum(div(cross_stddev(day_std(Ret), 60), cross_mean(day_std(Ret), 60)), 1)` |
| R 2 variant 3 | 过 | 0.93 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.87 | 0.17 | 0.56 | 0.03 | 0.22 | 0.35 | `ts_sum(cross_stddev(day_std(Ret), 60), 1)` |
| R 3 variant 1 | 过 | 0.52 | `ts_sum(LogFloatShares, 30)` | 0.85 | 0.29 | 0.11 | 0.02 | 0.23 | 0.01 | `ts_sum(sub(LogFloatCap, LogFloatShares), 30)` |
| R 3 variant 2 | 废品 | 0.17 | `ts_sum(LogFloatShares, 30)` | 0.14 | 0.03 | 0.12 | 0.02 | 0.03 | 0.08 | `ts_sum(ts_delta(sub(LogFloatCap, log(day_last(Close))), 120), 30)` |
| R 3 variant 3 | 废品 | 0.15 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` | 0.08 | 0.03 | 0.15 | 0.02 | 0.04 | 0.07 | `ts_sum(ts_delta(sub(LogTotalCap, log(day_last(Close))), 120), 30)` |
| R 4 variant 1 | 过 | 0.79 | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | 0.86 | 0.01 | 0.27 | 0.12 | 0.07 | 0.33 | `ts_mean(pow_2(div(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)` |
