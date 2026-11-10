# 相关度表:种子 2009,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.03 | `ts_max(day_durbin_watson(Close), 20)` | 0.04 | 0.03 | 0.03 | 0.15 | 0.03 | 0.03 | `day_wmean(Ret, div(Amt, cross_mean(Amt, 20)))` |
| slot a seed 1 | 过 | 0.32 | `ts_max(day_durbin_watson(Close), 40)` | 0.12 | 0.32 | 0.32 | 0.05 | 0.34 | 0.03 | `cross_mean(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret)), 241)` |
| slot a seed 2 | 过 | 0.35 | `ts_max(day_durbin_watson(Close), 40)` | 0.14 | 0.34 | 0.36 | 0.08 | 0.37 | 0.02 | `cross_ema(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret)), 120)` |
| slot a seed 3 | 过 | 0.41 | `ts_max(day_durbin_watson(Close), 40)` | 0.15 | 0.05 | 0.35 | 0.04 | 0.01 | 0.34 | `cross_mean(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_wmean(Ret, Amt)), 241)` |
| slot a seed 4 | 过 | 0.38 | `ts_max(day_durbin_watson(Close), 40)` | 0.15 | 0.37 | 0.40 | 0.11 | 0.40 | 0.02 | `cross_ema(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 120)` |
| slot a seed 5 | 过 | 0.26 | `ts_max(day_durbin_watson(Close), 20)` | 0.07 | 0.06 | 0.26 | 0.58 | 0.09 | 0.03 | `sub(cross_mean(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 241), cross_mean(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 21))` |
| slot a seed 6 | 过 | 0.25 | `ts_max(day_durbin_watson(Close), 20)` | 0.06 | 0.07 | 0.25 | 0.54 | 0.10 | 0.04 | `sub(cross_ema(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 10), cross_ema(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 120))` |
| slot a seed 7 | 过 | 0.31 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.10 | 0.42 | 0.29 | 0.09 | 0.43 | 0.17 | `div(cross_mean(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 241), cross_stddev(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 241))` |
| slot a seed 8 | 废品 | 0.22 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.03 | 0.33 | 0.21 | 0.09 | 0.34 | 0.18 | `cross_mean(sign(day_wmean(Ret, div(Amt, cross_mean(Amt, 20)))), 241)` |
| slot a seed 9 | 过 | 0.56 | `ts_max(day_durbin_watson(Close), 40)` | 0.24 | 0.12 | 0.53 | 0.02 | 0.06 | 0.49 | `sub(cross_tail_mean_q75(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 241), cross_tail_mean_q25(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 241))` |
| slot a seed 10 | 过 | 0.42 | `ts_max(day_durbin_watson(Close), 40)` | 0.16 | 0.33 | 0.39 | 0.06 | 0.28 | 0.56 | `cross_tail_mean_q25(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 241)` |
| slot a seed 11 | 过 | 0.27 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.04 | 0.42 | 0.22 | 0.10 | 0.42 | 0.27 | `ts_mean(cs_rank(day_wmean(Ret, div(Amt, cross_mean(Amt, 20)))), 241)` |
| slot a seed 12 | 过 | 0.34 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.11 | 0.45 | 0.12 | 0.01 | 0.40 | 0.21 | `cross_corr(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_sum(Ret), 120)` |
| slot a seed 13 | 过 | 0.27 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.03 | 0.42 | 0.25 | 0.10 | 0.42 | 0.27 | `cross_mean(div(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_wstd(Ret, div(Amt, cross_mean(Amt, 20)))), 241)` |
| slot b seed 1 | 过 | 0.47 | `ts_max(day_durbin_watson(Close), 40)` | 0.19 | 0.17 | 0.44 | 0.10 | 0.22 | 0.19 | `cross_ema(day_wmean(Ret, Amt), 120)` |
| slot b seed 2 | 过 | 0.42 | `ts_max(day_durbin_watson(Close), 40)` | 0.16 | 0.15 | 0.39 | 0.05 | 0.19 | 0.19 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241)` |
| slot b seed 3 | 过 | 0.46 | `ts_max(day_durbin_watson(Close), 40)` | 0.18 | 0.16 | 0.42 | 0.09 | 0.21 | 0.20 | `cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 120)` |
| slot b seed 4 | 过 | 0.24 | `ts_max(day_durbin_watson(Close), 20)` | 0.08 | 0.05 | 0.21 | 0.54 | 0.09 | 0.06 | `sub(cross_mean(day_wmean(Ret, Amt), 241), cross_mean(day_wmean(Ret, Amt), 21))` |
| slot b seed 5 | 过 | 0.26 | `ts_max(day_durbin_watson(Close), 20)` | 0.08 | 0.30 | 0.30 | 0.09 | 0.32 | 0.08 | `div(cross_mean(day_wmean(Ret, Amt), 241), cross_stddev(day_wmean(Ret, Amt), 241))` |
| slot b seed 6 | 废品 | 0.21 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.04 | 0.30 | 0.22 | 0.09 | 0.30 | 0.10 | `cross_mean(sign(day_wmean(Ret, Amt)), 241)` |
| slot b seed 7 | 过 | 0.24 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.05 | 0.35 | 0.27 | 0.10 | 0.36 | 0.14 | `ts_mean(cs_rank(day_wmean(Ret, Amt)), 241)` |
| slot b seed 8 | 过 | 0.05 | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` | 0.15 | 0.23 | 0.20 | 0.13 | 0.25 | 0.39 | `cross_mean(day_signed_ratio(Ret, Amt), 241)` |
| slot b seed 9 | 过 | 0.06 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.17 | 0.24 | 0.21 | 0.17 | 0.26 | 0.41 | `cross_ema(day_signed_ratio(Ret, Volume), 120)` |
| slot b seed 10 | 过 | 0.07 | `ts_max(day_durbin_watson(Close), 20)` | 0.12 | 0.09 | 0.09 | 0.56 | 0.07 | 0.03 | `sub(cross_mean(day_signed_ratio(Ret, Amt), 241), cross_mean(day_signed_ratio(Ret, Amt), 21))` |
| slot b seed 11 | 过 | 0.12 | `ts_max(day_durbin_watson(Close), 20)` | 0.06 | 0.12 | 0.18 | 0.06 | 0.12 | 0.04 | `sub(cross_mean(day_wmean(in_slice(Ret, 121, 240), in_slice(Amt, 121, 240)), 241), cross_mean(day_wmean(in_slice(Ret, 1, 120), in_slice(Amt, 1, 120)), 241))` |
| slot b seed 12 | 过 | 0.10 | `ts_max(day_durbin_watson(Close), 40)` | 0.08 | 0.03 | 0.08 | 0.04 | 0.01 | 0.02 | `cross_mean(day_wmean(in_slice(Ret, 211, 240), in_slice(Amt, 211, 240)), 241)` |
| slot b seed 13 | 过 | 0.19 | `ts_max(day_durbin_watson(Close), 40)` | 0.03 | 0.21 | 0.22 | 0.08 | 0.22 | 0.04 | `cross_mean(day_wmean(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 241)` |
| slot b seed 14 | 过 | 0.03 | `ts_max(day_durbin_watson(Close), 20)` | 0.05 | 0.03 | 0.07 | 0.01 | 0.04 | 0.01 | `cross_mean(day_last(Ret), 241)` |
| slot b seed 15 | 过 | 0.34 | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` | 0.08 | 0.45 | 0.29 | 0.08 | 0.44 | 0.17 | `cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 241)` |
| slot b seed 16 | 过 | 0.31 | `ts_max(day_durbin_watson(Close), 40)` | 0.10 | 0.10 | 0.34 | 0.02 | 0.06 | 0.21 | `cross_mean(day_wmean(Ret, in_delay(Amt, 1)), 241)` |
| R 1 variant 1 | 过 | 0.80 | `ts_max(day_durbin_watson(Close), 40)` | 0.66 | 0.12 | 0.60 | 0.01 | 0.17 | 0.34 | `ts_max(day_durbin_watson(Close), 80)` |
| R 1 variant 2 | 过 | 0.75 | `ts_max(day_durbin_watson(Close), 40)` | 0.56 | 0.10 | 0.56 | 0.01 | 0.14 | 0.36 | `ts_max(day_durbin_watson(Close), 100)` |
| R 1 variant 3 | 过 | 0.71 | `ts_max(day_durbin_watson(Close), 40)` | 0.48 | 0.07 | 0.53 | 0.01 | 0.12 | 0.38 | `ts_max(day_durbin_watson(Close), 120)` |
| R 1 variant 4 | 过 | 0.65 | `ts_max(day_durbin_watson(Close), 40)` | 0.40 | 0.04 | 0.48 | 0.02 | 0.08 | 0.41 | `ts_max(day_durbin_watson(Close), 160)` |
| R 1 variant 5 | 过 | 0.61 | `ts_max(day_durbin_watson(Close), 40)` | 0.35 | 0.01 | 0.45 | 0.03 | 0.05 | 0.43 | `ts_max(day_durbin_watson(Close), 200)` |
| R 1 variant 6 | 过 | 0.58 | `ts_max(day_durbin_watson(Close), 40)` | 0.31 | 0.01 | 0.43 | 0.03 | 0.03 | 0.45 | `ts_max(day_durbin_watson(Close), 241)` |
| R 1 variant 7 | 过 | 0.67 | `ts_max(day_durbin_watson(Close), 40)` | 0.45 | 0.05 | 0.49 | 0.02 | 0.09 | 0.41 | `ts_max(day_durbin_watson(Vwap), 120)` |
| R 1 variant 8 | 过 | 0.56 | `ts_max(day_durbin_watson(Close), 40)` | 0.29 | 0.03 | 0.40 | 0.03 | 0.01 | 0.48 | `ts_max(day_durbin_watson(Vwap), 241)` |
| R 2 variant 1 | 过 | 0.42 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.29 | 0.50 | 0.04 | 0.07 | 0.46 | 0.12 | `cross_stddev(log(cross_mean(log(log(day_durbin_watson(Volume))), 120)), 60)` |
| R 2 variant 2 | 过 | 0.38 | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` | 0.24 | 0.44 | 0.02 | 0.07 | 0.41 | 0.09 | `cross_stddev(cross_stddev(log(cross_mean(log(log(day_durbin_watson(Volume))), 120)), 60), 60)` |
| R 2 variant 3 | 过 | 0.12 | `ts_max(day_durbin_watson(Close), 40)` | 0.09 | 0.01 | 0.05 | 0.03 | 0.01 | 0.17 | `cross_stddev(cross_mean(log(log(day_durbin_watson(Volume))), 120), 60)` |
