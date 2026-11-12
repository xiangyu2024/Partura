# 相关度表:种子 2053,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.25 | `day_sum(cross_sum(Volume, 3))` | 0.08 | 0.18 | 0.35 | 0.75 | 0.20 | 0.05 | `cross_sum(cross_sum(day_mean(Ret), 10), 15)` |
| slot a seed 1 | 过 | 0.25 | `day_sum(cross_sum(Volume, 3))` | 0.08 | 0.17 | 0.34 | 0.73 | 0.19 | 0.05 | `div(cross_sum(cross_sum(day_mean(Ret), 10), 15), cross_stddev(day_mean(Ret), 60))` |
| slot a seed 2 | 过 | 0.25 | `day_sum(cross_sum(Volume, 3))` | 0.08 | 0.17 | 0.34 | 0.74 | 0.20 | 0.05 | `div(cross_sum(cross_sum(day_mean(Ret), 10), 15), cross_mean(day_std(Ret), 60))` |
| slot a seed 3 | 过 | 0.24 | `day_sum(cross_sum(Volume, 3))` | 0.08 | 0.18 | 0.35 | 0.73 | 0.20 | 0.05 | `sub(cross_sum(cross_sum(day_mean(Ret), 10), 15), cross_sum(day_mean(Ret), 5))` |
| slot a seed 4 | 过 | 0.14 | `day_sum(cross_sum(Volume, 3))` | 0.26 | 0.02 | 0.18 | 0.71 | 0.04 | 0.01 | `cross_zscore(cross_sum(cross_sum(day_mean(Ret), 10), 15), 120)` |
| slot a seed 5 | 废品 | 0.12 | `day_sum(cross_sum(Volume, 3))` | 0.16 | 0.02 | 0.10 | 0.66 | 0.00 | 0.00 | `cross_rank(cross_sum(cross_sum(day_mean(Ret), 10), 15), 60)` |
| slot a seed 6 | 过 | 0.62 | `day_sum(cross_sum(Volume, 3))` | 0.62 | 0.30 | 0.06 | 0.04 | 0.33 | 0.25 | `cross_regbeta(cross_sum(cross_sum(day_mean(Ret), 10), 15), day_sum(Volume), 120)` |
| slot a seed 7 | 过 | 0.33 | `ts_std(ts_cov(day_quantile_q25(Ret), day_close(cross_delta(n` | 0.27 | 0.23 | 0.14 | 0.01 | 0.23 | 0.03 | `cross_regbeta(cross_sum(cross_sum(day_mean(Ret), 10), 15), day_std(Ret), 120)` |
| slot a seed 8 | 过 | 0.08 | `day_sum(cross_sum(Volume, 3))` | 0.12 | 0.05 | 0.07 | 0.60 | 0.04 | 0.01 | `sub(cross_sum(cross_sum(day_mean(Ret), 10), 15), cross_delay(cross_sum(cross_sum(day_mean(Ret), 10), 15), 20))` |
| slot a seed 9 | 过 | 0.39 | `day_first(cross_sum(Amt, 30))` | 0.13 | 0.32 | 0.48 | 0.39 | 0.35 | 0.07 | `cross_ema(div(cross_sum(cross_sum(day_mean(Ret), 10), 15), cross_stddev(day_mean(Ret), 120)), 10)` |
| slot a seed 10 | 过 | 0.22 | `day_sum(cross_sum(Volume, 3))` | 0.15 | 0.14 | 0.22 | 0.37 | 0.17 | 0.07 | `cross_min(cross_sum(cross_sum(day_mean(Ret), 10), 15), 20)` |
| slot a seed 11 | 过 | 0.24 | `day_sum(cross_sum(Volume, 3))` | 0.08 | 0.17 | 0.34 | 0.71 | 0.20 | 0.05 | `sub(div(cross_sum(cross_sum(day_mean(Ret), 10), 15), cross_stddev(day_mean(Ret), 120)), div(cross_sum(day_mean(Ret), 10), cross_stddev(day_mean(Ret), 20)))` |
| slot a seed 12 | 过 | 0.15 | `ts_std(ts_cov(day_quantile_q25(Ret), day_close(cross_delta(n` | 0.13 | 0.02 | 0.05 | 0.04 | 0.03 | 0.07 | `cross_corr(cross_sum(cross_sum(day_mean(Ret), 10), 15), day_sum(Volume), 60)` |
| slot b seed 1 | 过 | 0.40 | `day_first(cross_sum(Amt, 30))` | 0.14 | 0.38 | 0.36 | 0.21 | 0.39 | 0.07 | `cross_mean(sub(div(day_first(Close), cross_delay(day_close(Close), 1)), div(day_close(Close), day_first(Close))), 60)` |
| slot b seed 2 | 过 | 0.41 | `day_first(cross_sum(Amt, 30))` | 0.12 | 0.39 | 0.38 | 0.31 | 0.40 | 0.08 | `cross_ema(sub(div(day_first(Close), cross_delay(day_close(Close), 1)), div(day_close(Close), day_first(Close))), 30)` |
| slot b seed 3 | 过 | 0.28 | `day_first(cross_sum(Amt, 241))` | 0.21 | 0.21 | 0.04 | 0.10 | 0.21 | 0.01 | `cross_mean(div(day_first(Close), cross_delay(day_close(Close), 1)), 120)` |
| slot b seed 4 | 过 | 0.40 | `day_first(cross_sum(Amt, 30))` | 0.28 | 0.39 | 0.42 | 0.20 | 0.40 | 0.07 | `cross_mean(div(day_close(Close), day_first(Close)), 120)` |
| slot b seed 5 | 过 | 0.02 | `day_sum(cross_sum(Volume, 3))` | 0.04 | 0.01 | 0.01 | 0.12 | 0.01 | 0.01 | `cross_zscore(sub(div(day_first(Close), cross_delay(day_close(Close), 1)), div(day_close(Close), day_first(Close))), 60)` |
| slot b seed 6 | 过 | 0.12 | `day_first(cross_sum(Amt, 30))` | 0.06 | 0.10 | 0.04 | 0.00 | 0.10 | 0.04 | `cross_regbeta(cross_mean(div(day_first(Close), cross_delay(day_close(Close), 1)), 20), cross_mean(div(day_close(Close), day_first(Close)), 20), 120)` |
| slot b seed 7 | 过 | 0.18 | `day_first(cross_sum(Amt, 30))` | 0.06 | 0.20 | 0.02 | 0.00 | 0.19 | 0.13 | `cross_corr(div(day_first(Close), cross_delay(day_close(Close), 1)), div(day_close(Close), day_first(Close)), 60)` |
| slot b seed 8 | 过 | 0.10 | `day_first(cross_sum(Amt, 30))` | 0.09 | 0.11 | 0.10 | 0.14 | 0.11 | 0.06 | `sub(cross_mean(div(day_first(Close), cross_delay(day_close(Close), 1)), 20), cross_mean(div(day_first(Close), cross_delay(day_close(Close), 1)), 120))` |
| slot b seed 9 | 过 | 0.45 | `day_first(cross_sum(Amt, 30))` | 0.31 | 0.43 | 0.64 | 0.02 | 0.45 | 0.10 | `cross_stddev(sub(div(day_first(Close), cross_delay(day_close(Close), 1)), div(day_close(Close), day_first(Close))), 60)` |
