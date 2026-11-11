# 相关度表:种子 2053,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.12 | `day_sum(cross_sum(Volume, 3))` | 0.19 | 0.03 | 0.32 | 0.18 | 0.06 | 0.00 | `day_topw_mean(Ret, Close)` |
| slot a seed 1 | 过 | 0.21 | `day_sum(cross_sum(Volume, 3))` | 0.17 | 0.12 | 0.77 | 0.31 | 0.18 | 0.06 | `cross_mean(day_topw_mean(Ret, Close), 20)` |
| slot a seed 2 | 过 | 0.22 | `day_sum(cross_sum(Volume, 3))` | 0.18 | 0.13 | 0.79 | 0.26 | 0.19 | 0.07 | `cross_ema(day_topw_mean(Ret, Close), 10)` |
| slot a seed 3 | 过 | 0.22 | `day_sum(cross_sum(Volume, 3))` | 0.18 | 0.09 | 0.72 | 0.35 | 0.15 | 0.05 | `cross_decay_linear(day_topw_mean(Ret, Close), 20)` |
| slot a seed 4 | 过 | 0.03 | `day_sum(cross_sum(Volume, 3))` | 0.07 | 0.02 | 0.00 | 0.15 | 0.02 | 0.03 | `cross_zscore(day_topw_mean(Ret, Close), 60)` |
| slot a seed 5 | 过 | 0.11 | `day_sum(cross_sum(Volume, 3))` | 0.19 | 0.02 | 0.31 | 0.14 | 0.05 | 0.01 | `sub(day_topw_mean(Ret, Close), day_mean(Ret))` |
| slot a seed 6 | 过 | 0.19 | `day_sum(cross_sum(Volume, 3))` | 0.15 | 0.11 | 0.76 | 0.23 | 0.17 | 0.07 | `cross_mean(sub(day_topw_mean(Ret, Close), day_mean(Ret)), 20)` |
| slot a seed 7 | 过 | 0.10 | `day_first(cross_sum(Amt, 241))` | 0.12 | 0.14 | 0.14 | 0.43 | 0.12 | 0.10 | `cross_mean(sub(day_topw_mean(Ret, Close), day_topw_mean(Ret, Volume)), 20)` |
| slot a seed 8 | 过 | 0.20 | `day_first(cross_sum(Amt, 30))` | 0.12 | 0.26 | 0.17 | 0.24 | 0.23 | 0.19 | `cross_ema(sub(day_topw_mean(Ret, Close), day_topw_mean(Ret, Amt)), 30)` |
| slot a seed 9 | 过 | 0.16 | `day_first(cross_sum(Amt, 30))` | 0.11 | 0.10 | 0.24 | 0.13 | 0.14 | 0.12 | `cross_corr(day_topw_mean(Ret, Close), day_mean(Ret), 60)` |
| slot a seed 10 | 过 | 0.07 | `day_sum(cross_sum(Volume, 3))` | 0.09 | 0.07 | 0.01 | 0.27 | 0.06 | 0.03 | `sub(cross_mean(day_topw_mean(Ret, Close), 5), cross_mean(day_topw_mean(Ret, Close), 40))` |
| slot a seed 11 | 过 | 0.15 | `day_first(cross_sum(Amt, 30))` | 0.27 | 0.19 | 0.13 | 0.21 | 0.17 | 0.06 | `cross_min(day_topw_mean(Ret, Close), 20)` |
| slot a seed 12 | 过 | 0.20 | `day_first(cross_sum(Amt, 30))` | 0.19 | 0.14 | 0.79 | 0.11 | 0.20 | 0.11 | `cross_ema(day_topw_mean(Ret, Close), 30)` |
| slot b seed 1 | 过 | 0.26 | `day_first(cross_sum(Amt, 30))` | 0.12 | 0.24 | 0.36 | 0.31 | 0.26 | 0.00 | `cross_mean(day_topw_mean(Ret, in_demean(Close)), 20)` |
| slot b seed 2 | 过 | 0.29 | `day_first(cross_sum(Amt, 30))` | 0.14 | 0.28 | 0.38 | 0.26 | 0.30 | 0.00 | `cross_ema(day_topw_mean(Ret, in_demean(Close)), 10)` |
| slot b seed 3 | 过 | 0.20 | `day_first(cross_sum(Amt, 30))` | 0.12 | 0.18 | 0.31 | 0.46 | 0.20 | 0.02 | `cross_mean(day_topw_mean(Ret, in_delta(Close, 30)), 20)` |
| slot b seed 4 | 过 | 0.02 | `day_sum(cross_sum(Volume, 3))` | 0.03 | 0.01 | 0.00 | 0.10 | 0.01 | 0.01 | `cross_zscore(day_topw_mean(Ret, in_delta(Close, 30)), 60)` |
| slot b seed 5 | 过 | 0.34 | `day_first(cross_sum(Amt, 30))` | 0.22 | 0.33 | 0.46 | 0.32 | 0.34 | 0.03 | `cross_mean(day_topw_mean(Ret, abs_(in_delta(Close, 15))), 30)` |
| slot b seed 6 | 过 | 0.25 | `day_first(cross_sum(Amt, 30))` | 0.09 | 0.24 | 0.41 | 0.64 | 0.26 | 0.05 | `cross_mean(day_topw_mean(Ret, in_rank(Volume)), 20)` |
| slot b seed 7 | 过 | 0.20 | `day_sum(cross_sum(Volume, 3))` | 0.06 | 0.12 | 0.25 | 0.54 | 0.13 | 0.06 | `cross_mean(sub(day_topw_mean(Ret, in_demean(Close)), day_topw_mean(Ret, Volume)), 20)` |
| slot b seed 8 | 过 | 0.38 | `day_first(cross_sum(Amt, 30))` | 0.32 | 0.44 | 0.34 | 0.23 | 0.44 | 0.20 | `cross_ema(day_topw_mean(in_delta(Close, 5), in_demean(Close)), 10)` |
| slot b seed 9 | 过 | 0.95 | `day_sum(cross_sum(Volume, 3))` | 0.94 | 0.69 | 0.28 | 0.13 | 0.73 | 0.53 | `cross_mean(day_topw_mean(Volume, in_demean(Close)), 20)` |
| slot b seed 10 | 过 | 0.16 | `day_first(cross_sum(Amt, 30))` | 0.11 | 0.15 | 0.25 | 0.42 | 0.16 | 0.02 | `cross_decay_linear(day_topw_mean(Ret, in_delta(Close, 30)), 20)` |
