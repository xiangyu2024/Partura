# 相关度表:种子 2059,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 10 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.38 | `ts_min(cs_rank(ts_decay_linear(pow_2(ts_min(ts_decay_linear(` | 0.20 | 0.24 | 0.41 | 0.32 | 0.26 | 0.02 | `ts_kurt(day_es_ratio_lo(Open), 10)` |
| slot a seed 1 | 过 | 0.48 | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(t` | 0.39 | 0.31 | 0.41 | 0.05 | 0.31 | 0.06 | `cross_quantile_q75(ts_kurt(day_es_ratio_lo(Open), 10), 241)` |
| slot a seed 2 | 过 | 0.52 | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(t` | 0.35 | 0.34 | 0.46 | 0.03 | 0.34 | 0.04 | `cross_quantile_q75(ts_kurt(day_es_ratio_lo(Open), 10), 120)` |
| slot a seed 3 | 过 | 0.82 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.81 | 0.21 | 0.39 | 0.02 | 0.22 | 0.15 | `cross_mean(ts_kurt(day_es_ratio_lo(Open), 10), 241)` |
| slot a seed 4 | 过 | 0.93 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.93 | 0.10 | 0.29 | 0.01 | 0.12 | 0.19 | `cross_stddev(ts_kurt(day_es_ratio_lo(Open), 10), 241)` |
| slot a seed 5 | 过 | 0.59 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.51 | 0.31 | 0.49 | 0.03 | 0.33 | 0.09 | `cross_decay_linear(ts_kurt(day_es_ratio_lo(Open), 10), 120)` |
| slot a seed 6 | 过 | 0.43 | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(t` | 0.27 | 0.28 | 0.32 | 0.06 | 0.26 | 0.07 | `cross_med(ts_kurt(day_es_ratio_lo(Open), 10), 482)` |
| slot a seed 7 | 过 | 0.76 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.72 | 0.00 | 0.19 | 0.01 | 0.02 | 0.20 | `cross_max(ts_kurt(day_es_ratio_lo(Open), 10), 482)` |
| slot a seed 8 | 过 | 0.93 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.96 | 0.20 | 0.24 | 0.01 | 0.21 | 0.01 | `cs_bucket_zscore(cross_max(ts_kurt(day_es_ratio_lo(Open), 10), 241), LogFloatCap)` |
| slot a seed 9 | 过 | 0.61 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.58 | 0.34 | 0.41 | 0.01 | 0.35 | 0.00 | `cs_bucket_zscore(cross_mean(ts_kurt(day_es_ratio_lo(Open), 10), 120), LogFloatCap)` |
| slot a seed 10 | 废品 | 0.17 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.15 | 0.16 | 0.32 | 0.19 | 0.19 | 0.08 | `cross_regres(cross_max(ts_kurt(day_es_ratio_lo(Open), 10), 241), cross_mean(day_std(Ret), 60), 120)` |
| slot a seed 11 | 过 | 0.17 | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(t` | 0.11 | 0.14 | 0.21 | 0.09 | 0.15 | 0.03 | `cross_zscore(cross_max(ts_kurt(day_es_ratio_lo(Open), 10), 120), 60)` |
| slot a seed 12 | 过 | 0.95 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.95 | 0.03 | 0.22 | 0.01 | 0.05 | 0.19 | `sub(cross_max(ts_kurt(day_es_ratio_lo(Open), 10), 241), cross_mean(ts_kurt(day_es_ratio_lo(Open), 10), 241))` |
| slot b seed 1 | 过 | 0.18 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.15 | 0.01 | 0.07 | 0.01 | 0.00 | 0.03 | `cross_max(ts_kurt(day_es_ratio_hi(Ret), 10), 241)` |
| slot b seed 2 | 过 | 0.08 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.06 | 0.01 | 0.06 | 0.00 | 0.02 | 0.04 | `cross_max(ts_kurt(day_es_ratio_lo(Ret), 10), 241)` |
| slot b seed 3 | 过 | 0.44 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.34 | 0.21 | 0.22 | 0.01 | 0.17 | 0.49 | `cross_max(ts_kurt(day_wstd(Ret, Volume), 10), 241)` |
| slot b seed 4 | 过 | 0.35 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.21 | 0.01 | 0.28 | 0.03 | 0.00 | 0.34 | `cross_max(ts_kurt(day_topw_mean(Ret, Volume), 10), 482)` |
| slot b seed 5 | 过 | 0.93 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.92 | 0.05 | 0.25 | 0.01 | 0.08 | 0.20 | `cross_max(ts_kurt(day_es_ratio_lo(Low), 10), 241)` |
| slot b seed 6 | 过 | 0.90 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.88 | 0.09 | 0.25 | 0.01 | 0.11 | 0.15 | `cross_max(ts_kurt(day_es_ratio_lo(Vwap), 10), 241)` |
| slot b seed 7 | 过 | 0.23 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.19 | 0.01 | 0.09 | 0.01 | 0.01 | 0.05 | `cross_max(ts_skew(day_es_ratio_hi(Ret), 20), 241)` |
| slot b seed 8 | 过 | 0.39 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.29 | 0.25 | 0.20 | 0.01 | 0.20 | 0.52 | `cross_max(ts_std(day_wstd(Ret, Volume), 10), 482)` |
| slot b seed 9 | 过 | 0.49 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.40 | 0.14 | 0.30 | 0.02 | 0.09 | 0.53 | `cross_quantile_q75(ts_kurt(day_wstd(Ret, Volume), 20), 241)` |
| slot b seed 10 | 过 | 0.54 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.47 | 0.16 | 0.25 | 0.02 | 0.10 | 0.42 | `cross_max(ts_kurt(day_wmean(Ret, Amt), 10), 241)` |
| slot b seed 11 | 过 | 0.31 | `cross_max(cs_first_high20(ts_kurt(day_es_ratio_lo(Open), 10)` | 0.20 | 0.03 | 0.20 | 0.04 | 0.04 | 0.21 | `cross_max(ts_kurt(day_es_ratio_hi(Close), 10), 241)` |
| slot b seed 12 | 过 | 0.13 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.10 | 0.02 | 0.11 | 0.03 | 0.02 | 0.06 | `cross_mean(ts_kurt(day_es_ratio_lo(Ret), 20), 120)` |
