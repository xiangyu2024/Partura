# 相关度表:种子 2018,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 1 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.37 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.38 | 0.18 | 0.25 | 0.30 | 0.20 | 0.06 | `cross_argmax(day_quantile(Open), 60)` |
| slot a seed 1 | 过 | 0.28 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.26 | 0.05 | 0.17 | 0.27 | 0.08 | 0.02 | `cross_zscore(cross_argmax(day_quantile(Open), 60), 120)` |
| slot a seed 2 | 过 | 0.31 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.27 | 0.28 | 0.27 | 0.11 | 0.28 | 0.11 | `cross_ema(cross_argmax(day_quantile(Open), 60), 20)` |
| slot a seed 3 | 过 | 0.36 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.30 | 0.10 | 0.23 | 0.22 | 0.13 | 0.02 | `sub(cross_ema(cross_argmax(day_quantile(Open), 60), 5), cross_ema(cross_argmax(day_quantile(Open), 60), 60))` |
| slot a seed 4 | 过 | 0.26 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.22 | 0.29 | 0.28 | 0.10 | 0.29 | 0.10 | `cross_ema(sub(cross_argmax(day_quantile(Open), 60), cross_argmin(day_quantile(Open), 60)), 20)` |
| slot a seed 5 | 过 | 0.26 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.35 | 0.01 | 0.00 | 0.03 | 0.00 | 0.01 | `ts_std(sub(cross_argmax(day_quantile(Open), 60), cross_argmin(day_quantile(Open), 60)), 25)` |
| slot a seed 6 | 过 | 0.22 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.19 | 0.29 | 0.29 | 0.11 | 0.29 | 0.10 | `sub(log(cross_ema(cross_argmax(day_quantile(Open), 60), 20)), log(cross_ema(cross_argmin(day_quantile(Open), 60), 20)))` |
| slot a seed 7 | 过 | 0.06 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.19 | 0.10 | 0.11 | 0.02 | 0.11 | 0.05 | `cross_corr(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 60)` |
| slot a seed 8 | 过 | 0.08 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.19 | 0.16 | 0.15 | 0.04 | 0.17 | 0.07 | `cross_regbeta(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 120)` |
| slot a seed 9 | 过 | 0.13 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.17 | 0.06 | 0.03 | 0.00 | 0.06 | 0.04 | `cross_corr(cross_argmax(day_quantile(Open), 60), cross_argmax(day_sum(Amt), 60), 120)` |
| slot a seed 10 | 过 | 0.02 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.08 | 0.03 | 0.05 | 0.18 | 0.01 | 0.04 | `ts_std(sub(cross_argmax(day_quantile(Open), 60), cross_argmax(day_sum(Amt), 60)), 25)` |
| slot a seed 11 | 过 | 0.11 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.09 | 0.14 | 0.10 | 0.02 | 0.12 | 0.04 | `cross_ema(sub(cross_argmax(day_sum(Amt), 60), cross_argmax(day_quantile(Open), 60)), 20)` |
| slot a seed 12 | 过 | 0.24 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.46 | 0.39 | 0.08 | 0.01 | 0.37 | 0.72 | `cs_first_low40(ts_std(cross_argmax(day_quantile(Open), 60), 25), LogFloatCap)` |
| slot a seed 13 | 过 | 0.14 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.20 | 0.02 | 0.01 | 0.03 | 0.02 | 0.04 | `cs_flip_by_state(cross_ema(cross_argmax(day_quantile(Open), 60), 20), day_sum(Amt))` |
| slot b seed 1 | 过 | 0.30 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.30 | 0.27 | 0.36 | 0.48 | 0.29 | 0.10 | `div(cross_sum(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 60), cross_sum(abs_(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 60))` |
| slot b seed 2 | 过 | 0.10 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.07 | 0.32 | 0.34 | 0.34 | 0.33 | 0.15 | `div(sub(log(day_close(Close)), cross_delay(log(day_close(Close)), 120)), cross_sum(abs_(cross_delta(log(day_close(Close)), 1)), 120))` |
| slot b seed 3 | 过 | 0.08 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.28 | 0.08 | 0.11 | 0.06 | 0.09 | 0.05 | `div(abs_(cross_sum(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 60)), cross_sum(abs_(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 60))` |
| slot b seed 4 | 过 | 0.20 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.22 | 0.04 | 0.21 | 0.47 | 0.07 | 0.02 | `cross_zscore(div(cross_sum(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 60), cross_sum(abs_(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 60)), 120)` |
| slot b seed 5 | 过 | 0.30 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.32 | 0.26 | 0.35 | 0.36 | 0.28 | 0.09 | `cross_corr(log(day_close(Close)), cross_age(day_close(Close)), 60)` |
| slot b seed 6 | 过 | 0.14 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.12 | 0.32 | 0.32 | 0.15 | 0.32 | 0.12 | `cross_reg_tvalue(cross_age(day_close(Close)), log(day_close(Close)), 120)` |
| slot b seed 7 | 过 | 0.01 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.01 | 0.16 | 0.15 | 0.02 | 0.15 | 0.03 | `div(cross_max(abs_(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 60), cross_sum(abs_(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 60))` |
| slot b seed 8 | 过 | 0.08 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.20 | 0.11 | 0.12 | 0.01 | 0.11 | 0.04 | `mul(cross_sum(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 60), cross_mean(sign(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1)), 60))` |
| slot b seed 9 | 过 | 0.01 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.08 | 0.09 | 0.13 | 0.01 | 0.11 | 0.05 | `div(sub(cross_max(day_max(High), 60), cross_min(day_min(Low), 60)), cross_sum(sub(day_max(High), day_min(Low)), 60))` |
| slot b seed 10 | 过 | 0.26 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.23 | 0.28 | 0.34 | 0.39 | 0.31 | 0.13 | `sub(log(cross_semistd_pos(day_close(Close), 60)), log(cross_semistd_neg(day_close(Close), 60)))` |
| slot b seed 11 | 过 | 0.12 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.07 | 0.33 | 0.33 | 0.27 | 0.34 | 0.16 | `div(cross_semistd_pos(day_close(Close), 120), add(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120)))` |
| R 1 variant 1 | 过 | 0.47 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.56 | 0.00 | 0.03 | 0.12 | 0.01 | 0.01 | `ts_std(cross_argmax(day_quantile(Open), 60), 25)` |
| R 1 variant 2 | 废品 | 0.23 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.29 | 0.01 | 0.01 | 0.06 | 0.01 | 0.00 | `ts_std(cross_argmax(day_quantile(Open), 60), 15)` |
| R 1 variant 3 | 废品 | 0.16 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.22 | 0.01 | 0.03 | 0.03 | 0.02 | 0.01 | `ts_std(cross_argmax(day_quantile(Open), 60), 10)` |
| R 1 variant 4 | 过 | 0.03 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.16 | 0.01 | 0.02 | 0.19 | 0.01 | 0.01 | `ts_std(cross_argmax(day_quantile(Open), 30), 25)` |
| R 1 variant 5 | 废品 | 0.24 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.37 | 0.02 | 0.05 | 0.10 | 0.03 | 0.02 | `ts_std(cross_argmax(day_quantile(Open), 120), 25)` |
| R 1 variant 6 | 过 | 0.47 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.55 | 0.00 | 0.03 | 0.12 | 0.01 | 0.01 | `ts_std(cross_argmax(day_quantile(Close), 60), 25)` |
| R 1 variant 7 | 过 | 0.46 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.55 | 0.00 | 0.03 | 0.11 | 0.01 | 0.01 | `ts_std(cross_argmax(day_quantile(Vwap), 60), 25)` |
| R 1 variant 8 | 过 | 0.41 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.49 | 0.01 | 0.04 | 0.13 | 0.01 | 0.01 | `ts_std(cross_argmax(day_max(High), 60), 25)` |
| R 1 variant 9 | 过 | 0.67 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.79 | 0.02 | 0.03 | 0.08 | 0.03 | 0.01 | `ts_std(cross_ema(cross_argmax(day_quantile(Open), 60), 5), 25)` |
| R 1 variant 10 | 废品 | 0.11 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.19 | 0.06 | 0.08 | 0.10 | 0.06 | 0.02 | `ts_std(cross_argmin(day_quantile(Open), 60), 25)` |
| R 1 variant 11 | 过 | 0.26 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.35 | 0.01 | 0.00 | 0.03 | 0.00 | 0.01 | `ts_std(sub(cross_argmax(day_quantile(Open), 60), cross_argmin(day_quantile(Open), 60)), 25)` |
| R 1 variant 12 | 过 | 0.28 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.35 | 0.06 | 0.11 | 0.20 | 0.07 | 0.01 | `sub(ts_std(cross_argmax(day_quantile(Open), 60), 25), ts_std(cross_argmin(day_quantile(Open), 60), 25))` |
| R 1 variant 13 | 废品 | 0.21 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.12 | 0.02 | 0.10 | 0.23 | 0.04 | 0.01 | `ts_mean(abs_(cross_delta(cross_argmax(day_quantile(Open), 60), 1)), 25)` |
| R 1 variant 14 | 过 | 0.26 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.20 | 0.01 | 0.04 | 0.10 | 0.02 | 0.00 | `cross_zscore(ts_std(cross_argmax(day_quantile(Open), 60), 25), 120)` |
| R 1 variant 15 | 过 | 0.77 | `ts_std(cross_argmax(day_quantile(Open), 60), 50)` | 0.80 | 0.05 | 0.09 | 0.10 | 0.07 | 0.03 | `cross_ema(ts_std(cross_argmax(day_quantile(Open), 60), 25), 20)` |
