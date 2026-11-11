# 相关度表:种子 2070,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `day_quantile_q75(mul(High, Ret))` | 1.00 | 0.55 | 0.16 | 0.15 | 0.51 | 0.39 | `day_quantile_q75(mul(High, Ret))` |
| slot a seed 1 | 过 | 0.81 | `day_quantile_q75(mul(High, Ret))` | 0.92 | 0.67 | 0.21 | 0.06 | 0.62 | 0.46 | `ts_mean(day_quantile_q75(mul(High, Ret)), 20)` |
| slot a seed 2 | 过 | 0.86 | `day_quantile_q75(mul(High, Ret))` | 0.94 | 0.64 | 0.20 | 0.14 | 0.60 | 0.46 | `ts_decay_linear(day_quantile_q75(mul(High, Ret)), 10)` |
| slot a seed 3 | 过 | 0.54 | `day_quantile_q75(mul(High, Ret))` | 0.47 | 0.36 | 0.07 | 0.04 | 0.30 | 0.21 | `div(ts_mean(day_quantile_q75(mul(High, Ret)), 10), ts_std(day_quantile_q75(mul(High, Ret)), 20))` |
| slot a seed 4 | 过 | 0.39 | `day_quantile_q75(mul(High, Ret))` | 0.06 | 0.06 | 0.00 | 0.37 | 0.05 | 0.02 | `sub(day_quantile_q75(mul(High, Ret)), ts_mean(day_quantile_q75(mul(High, Ret)), 40))` |
| slot a seed 5 | 废品 | 0.15 | `ts_mean(day_q_stat_std(mul(Close, Close)), 40)` | 0.30 | 0.16 | 0.07 | 0.06 | 0.14 | 0.01 | `ts_rank(day_quantile_q75(mul(High, Ret)), 20)` |
| slot a seed 6 | 过 | 0.15 | `ts_mean(day_q_stat_std(mul(Close, Close)), 40)` | 0.23 | 0.05 | 0.15 | 0.01 | 0.04 | 0.05 | `ts_skew(day_quantile_q75(mul(High, Ret)), 20)` |
| slot a seed 7 | 过 | 0.73 | `day_quantile_q75(mul(High, Ret))` | 0.77 | 0.59 | 0.26 | 0.14 | 0.56 | 0.45 | `ts_max(day_quantile_q75(mul(High, Ret)), 10)` |
| slot a seed 8 | 过 | 0.14 | `day_quantile_q75(mul(High, Ret))` | 0.09 | 0.10 | 0.26 | 0.15 | 0.10 | 0.12 | `ts_corr(day_quantile_q75(mul(High, Ret)), day_sum(Amt), 20)` |
| slot a seed 9 | 过 | 0.97 | `day_quantile_q75(mul(High, Ret))` | 0.98 | 0.52 | 0.02 | 0.07 | 0.47 | 0.41 | `div(day_quantile_q75(mul(High, Ret)), day_std(Ret))` |
| slot a seed 10 | 过 | 0.80 | `day_quantile_q75(mul(High, Ret))` | 0.90 | 0.66 | 0.21 | 0.04 | 0.62 | 0.46 | `ts_mean(sub(day_quantile_q75(mul(High, Ret)), day_quantile_q25(mul(High, Ret))), 20)` |
| slot a seed 11 | 过 | 0.24 | `day_quantile_q75(mul(High, Ret))` | 0.03 | 0.09 | 0.04 | 0.38 | 0.08 | 0.01 | `ts_decay_linear(sub(day_quantile_q75(mul(High, Ret)), ts_mean(day_quantile_q75(mul(High, Ret)), 20)), 5)` |
| slot a seed 12 | 过 | 0.07 | `day_quantile_q75(mul(High, Ret))` | 0.09 | 0.09 | 0.16 | 0.06 | 0.10 | 0.04 | `ts_regres(day_quantile_q75(mul(High, Ret)), day_std(Ret), 20)` |
| slot b seed 1 | 过 | 0.07 | `ts_mean(day_q_stat_std(mul(Close, Close)), 40)` | 0.05 | 0.02 | 0.08 | 0.32 | 0.01 | 0.08 | `ts_mean(day_skew(mul(Ret, Volume)), 20)` |
| slot b seed 2 | 过 | 0.04 | `ts_mean(day_q_stat_std(mul(Close, Close)), 40)` | 0.04 | 0.03 | 0.02 | 0.21 | 0.01 | 0.05 | `ts_decay_linear(day_skew(mul(Ret, Amt)), 10)` |
| slot b seed 3 | 过 | 0.02 | `day_quantile_q75(mul(High, Ret))` | 0.03 | 0.05 | 0.05 | 0.18 | 0.05 | 0.00 | `sub(ts_mean(day_skew(mul(Ret, Volume)), 10), ts_mean(day_skew(mul(Ret, Volume)), 60))` |
| slot b seed 4 | 过 | 0.18 | `day_quantile_q75(mul(High, Ret))` | 0.08 | 0.12 | 0.22 | 0.56 | 0.13 | 0.03 | `ts_mean(day_corr(Ret, Volume), 20)` |
| slot b seed 5 | 过 | 0.20 | `day_quantile_q75(mul(High, Ret))` | 0.07 | 0.21 | 0.31 | 0.34 | 0.24 | 0.04 | `ts_mean(day_corr(Ret, Amt), 40)` |
| slot b seed 6 | 过 | 0.32 | `day_quantile_q75(mul(High, Ret))` | 0.04 | 0.48 | 0.43 | 0.52 | 0.51 | 0.21 | `ts_mean(sub(day_mean(mul(Ret, Amt)), day_mean(Ret)), 20)` |
| slot b seed 7 | 过 | 0.04 | `day_quantile_q75(mul(High, Ret))` | 0.04 | 0.03 | 0.09 | 0.32 | 0.04 | 0.03 | `div(ts_mean(day_skew(mul(Ret, Volume)), 20), ts_std(day_skew(mul(Ret, Volume)), 20))` |
| slot b seed 8 | 过 | 0.29 | `day_quantile_q75(mul(High, Ret))` | 0.05 | 0.37 | 0.02 | 0.12 | 0.30 | 0.36 | `ts_mean(day_kurt(mul(Ret, Volume)), 20)` |
| slot b seed 9 | 废品 | 0.03 | `day_quantile_q75(mul(High, Ret))` | 0.02 | 0.00 | 0.02 | 0.00 | 0.00 | 0.01 | `ts_rank(day_skew(mul(Ret, Amt)), 20)` |
| slot b seed 10 | 过 | 0.15 | `day_quantile_q75(mul(High, Ret))` | 0.09 | 0.05 | 0.08 | 0.39 | 0.06 | 0.03 | `ts_decay_linear(day_corr(Ret, Volume), 10)` |
| slot b seed 11 | 过 | 0.48 | `day_quantile_q75(mul(High, Ret))` | 0.09 | 0.85 | 0.32 | 0.12 | 0.84 | 0.48 | `ts_mean(day_quantile_q25(mul(Ret, Volume)), 20)` |
| slot b seed 12 | 过 | 0.52 | `day_quantile_q75(mul(High, Ret))` | 0.09 | 0.85 | 0.33 | 0.17 | 0.84 | 0.50 | `ts_mean(day_quantile_q75(mul(Ret, Volume)), 20)` |
