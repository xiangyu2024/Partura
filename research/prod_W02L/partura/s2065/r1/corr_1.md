# 相关度表:种子 2065,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.43 | `day_var(in_max_rolling(Vwap, 60))` | 0.17 | 0.66 | 0.06 | 0.12 | 0.57 | 0.48 | `cross_mean(div(day_max(Volume), day_sum(Volume)), 20)` |
| slot a seed 2 | 过 | 0.44 | `day_var(in_max_rolling(Vwap, 60))` | 0.19 | 0.64 | 0.11 | 0.10 | 0.54 | 0.51 | `cross_mean(div(day_max(Amt), day_mean(Amt)), 40)` |
| slot a seed 3 | 过 | 0.15 | `day_var(in_max_rolling(Vwap, 60))` | 0.06 | 0.22 | 0.31 | 0.34 | 0.24 | 0.04 | `cross_mean(day_corr(Volume, Ret), 40)` |
| slot a seed 4 | 过 | 0.15 | `day_var(in_max_rolling(Vwap, 60))` | 0.07 | 0.25 | 0.32 | 0.24 | 0.27 | 0.04 | `cross_mean(day_corr(Amt, Ret), 60)` |
| slot a seed 5 | 过 | 0.05 | `day_var(in_max_rolling(Vwap, 60))` | 0.14 | 0.16 | 0.17 | 0.02 | 0.14 | 0.01 | `cross_zscore(cross_mean(div(day_max(Volume), day_sum(Volume)), 10), 120)` |
| slot a seed 6 | 过 | 0.12 | `day_var(in_max_rolling(Vwap, 60))` | 0.12 | 0.32 | 0.41 | 0.21 | 0.35 | 0.05 | `cross_mean(mul(div(day_max(Volume), day_sum(Volume)), sign(cross_mean(day_sum(Ret), 20))), 40)` |
| slot a seed 7 | 过 | 0.44 | `day_var(in_max_rolling(Vwap, 60))` | 0.18 | 0.66 | 0.10 | 0.11 | 0.55 | 0.50 | `cross_mean(sub(div(day_max(Amt), day_mean(Amt)), div(day_median(Amt), day_mean(Amt))), 30)` |
| slot a seed 8 | 过 | 0.13 | `day_var(in_max_rolling(Vwap, 60))` | 0.02 | 0.17 | 0.25 | 0.27 | 0.19 | 0.03 | `cross_mean(day_corr(in_max_rolling(Volume, 5), Ret), 40)` |
| slot a seed 9 | 过 | 0.39 | `day_var(in_max_rolling(Vwap, 60))` | 0.19 | 0.53 | 0.21 | 0.09 | 0.43 | 0.49 | `cross_mean(div(day_max(Volume), day_median(Volume)), 60)` |
| slot a seed 10 | 过 | 0.34 | `day_var(in_max_rolling(Vwap, 60))` | 0.32 | 0.47 | 0.18 | 0.01 | 0.46 | 0.00 | `cross_mean(day_corr(Volume, abs_(Ret)), 40)` |
| slot b seed 1 | 过 | 0.06 | `day_q_stat_std(in_max_rolling(Volume, 60))` | 0.07 | 0.01 | 0.14 | 0.53 | 0.02 | 0.01 | `cross_mean(div(day_last(Close), day_mean(Vwap)), 20)` |
| slot b seed 2 | 过 | 0.06 | `day_var(in_max_rolling(Vwap, 60))` | 0.11 | 0.10 | 0.02 | 0.36 | 0.09 | 0.04 | `cross_mean(div(sub(day_last(Close), day_mean(Vwap)), day_std(Close)), 20)` |
| slot b seed 3 | 过 | 0.05 | `day_var(in_max_rolling(Vwap, 60))` | 0.14 | 0.10 | 0.01 | 0.54 | 0.09 | 0.01 | `cross_mean(div(sub(day_max(High), day_last(Close)), sub(day_max(High), day_min(Low))), 20)` |
| slot b seed 4 | 过 | 0.04 | `day_q_stat_std(in_max_rolling(Volume, 60))` | 0.12 | 0.04 | 0.10 | 0.55 | 0.03 | 0.02 | `cross_mean(day_corr(Close, in_index(Close)), 20)` |
| slot b seed 5 | 过 | 0.04 | `day_q_stat_std(in_max_rolling(Volume, 60))` | 0.11 | 0.01 | 0.17 | 0.36 | 0.02 | 0.03 | `cross_mean(day_corr(Vwap, in_index(Vwap)), 40)` |
| slot b seed 6 | 过 | 0.05 | `day_q_stat_std(in_max_rolling(Volume, 60))` | 0.02 | 0.04 | 0.02 | 0.28 | 0.04 | 0.01 | `cross_zscore(cross_mean(div(day_last(Close), day_mean(Vwap)), 10), 60)` |
| slot b seed 7 | 过 | 0.17 | `day_var(in_max_rolling(Vwap, 60))` | 0.09 | 0.27 | 0.30 | 0.38 | 0.29 | 0.07 | `cross_mean(sub(div(day_last(Close), day_mean(Vwap)), div(day_mean(Vwap), day_first(Open))), 30)` |
| slot b seed 8 | 过 | 0.07 | `day_var(in_max_rolling(Vwap, 60))` | 0.15 | 0.07 | 0.06 | 0.34 | 0.06 | 0.02 | `cross_mean(div(sub(day_last(Close), day_min(Low)), sub(day_max(High), day_min(Low))), 40)` |
| slot b seed 9 | 过 | 0.12 | `day_var(in_max_rolling(Vwap, 60))` | 0.17 | 0.27 | 0.14 | 0.05 | 0.27 | 0.02 | `cross_mean(day_corr(Close, Volume), 40)` |
| slot b seed 10 | 废品 | 0.07 | `day_var(in_max_rolling(Vwap, 60))` | 0.21 | 0.10 | 0.24 | 0.17 | 0.14 | 0.11 | `cross_mean(div(day_mean(Vwap), day_mean(Close)), 40)` |
