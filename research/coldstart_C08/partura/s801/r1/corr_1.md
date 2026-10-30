# 相关度表:种子 801,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 0 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.00 | `—` | 0.00 | 0.68 | 0.21 | 0.22 | 0.66 | 0.26 | `day_durbin_watson(Volume)` |
| slot a seed 1 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.14 | 0.32 | 0.09 | 0.05 | `cross_zscore(day_durbin_watson(Volume), 60)` |
| slot a seed 2 | 过 | 0.00 | `—` | 0.00 | 0.01 | 0.13 | 0.32 | 0.04 | 0.03 | `cross_madz(day_durbin_watson(Volume), 60)` |
| slot a seed 3 | 废品 | 0.00 | `—` | 0.00 | 0.11 | 0.20 | 0.32 | 0.14 | 0.07 | `ts_rank(day_durbin_watson(Volume), 120)` |
| slot a seed 4 | 过 | 0.00 | `—` | 0.00 | 0.23 | 0.36 | 0.36 | 0.26 | 0.08 | `cross_zscore(cross_ema(day_durbin_watson(Volume), 5), 120)` |
| slot a seed 5 | 过 | 0.00 | `—` | 0.00 | 0.88 | 0.22 | 0.03 | 0.84 | 0.32 | `ts_med(day_durbin_watson(Volume), 30)` |
| slot a seed 6 | 过 | 0.00 | `—` | 0.00 | 0.24 | 0.24 | 0.21 | 0.27 | 0.04 | `cs_bucket_rank(day_durbin_watson(Volume), day_gini(Volume))` |
| slot a seed 7 | 过 | 0.00 | `—` | 0.00 | 0.29 | 0.47 | 0.18 | 0.35 | 0.22 | `cs_bucket_rank(cross_mean(day_durbin_watson(Volume), 20), cross_mean(day_gini(Volume), 20))` |
| slot a seed 8 | 过 | 0.00 | `—` | 0.00 | 0.66 | 0.19 | 0.22 | 0.64 | 0.30 | `cs_bucket_rank(day_durbin_watson(Volume), ListAge)` |
| slot a seed 9 | 过 | 0.00 | `—` | 0.00 | 0.07 | 0.14 | 0.30 | 0.09 | 0.04 | `cs_bucket_rank(cross_zscore(day_durbin_watson(Volume), 60), ListAge)` |
| slot a seed 10 | 过 | 0.00 | `—` | 0.00 | 0.04 | 0.01 | 0.05 | 0.01 | 0.36 | `cs_bucket_rank(cross_mean(day_durbin_watson(Volume), 20), cross_mean(day_sum(Amt), 20))` |
| slot a seed 11 | 过 | 0.00 | `—` | 0.00 | 0.31 | 0.27 | 0.50 | 0.33 | 0.26 | `cross_mean(mul(day_durbin_watson(Volume), day_signed_ratio(Ret, Amt)), 20)` |
| slot a seed 12 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.12 | 0.06 | 0.19 | 0.04 | `cross_corr(day_durbin_watson(Volume), day_mean(Ret), 20)` |
| slot a seed 13 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.10 | 0.06 | 0.23 | 0.18 | `cross_corr(day_durbin_watson(Volume), day_sum(Volume), 20)` |
| slot a seed 14 | 过 | 0.00 | `—` | 0.00 | 0.85 | 0.18 | 0.05 | 0.80 | 0.32 | `cross_tail_mean_q75(day_durbin_watson(Volume), 20)` |
| slot a seed 15 | 过 | 0.00 | `—` | 0.00 | 0.55 | 0.03 | 0.09 | 0.47 | 0.25 | `cross_stddev(day_durbin_watson(Volume), 20)` |
| slot b seed 1 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.29 | 0.51 | 0.27 | 0.11 | `cross_mean(day_topw_mean(Ret, in_madz(Volume, 30)), 20)` |
| slot b seed 2 | 过 | 0.00 | `—` | 0.00 | 0.25 | 0.27 | 0.46 | 0.26 | 0.12 | `cross_mean(sub(day_topw_mean(Ret, in_madz(Volume, 30)), day_mean(Ret)), 20)` |
| slot b seed 3 | 过 | 0.00 | `—` | 0.00 | 0.19 | 0.10 | 0.06 | 0.19 | 0.12 | `cs_bucket_rank(cross_mean(day_topw_mean(Ret, in_madz(Volume, 30)), 20), cross_mean(day_mean(Ret), 20))` |
| slot b seed 4 | 过 | 0.00 | `—` | 0.00 | 0.15 | 0.38 | 0.49 | 0.20 | 0.02 | `cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)` |
| slot b seed 5 | 过 | 0.00 | `—` | 0.00 | 0.23 | 0.44 | 0.18 | 0.29 | 0.08 | `cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 60)` |
| slot b seed 6 | 过 | 0.00 | `—` | 0.00 | 0.17 | 0.28 | 0.53 | 0.20 | 0.09 | `cross_mean(day_corr(Ret, Volume), 20)` |
| slot b seed 7 | 过 | 0.00 | `—` | 0.00 | 0.21 | 0.24 | 0.45 | 0.23 | 0.11 | `cross_mean(day_corr(Ret, in_madz(Volume, 30)), 20)` |
| slot b seed 8 | 过 | 0.00 | `—` | 0.00 | 0.22 | 0.32 | 0.58 | 0.25 | 0.02 | `cross_mean(day_corr(in_delay(Ret, 1), Volume), 20)` |
| slot b seed 9 | 过 | 0.00 | `—` | 0.00 | 0.09 | 0.01 | 0.02 | 0.09 | 0.06 | `cross_mean(day_corr(Ret, in_delay(Volume, 1)), 20)` |
| slot b seed 10 | 过 | 0.00 | `—` | 0.00 | 0.05 | 0.15 | 0.18 | 0.08 | 0.06 | `cross_mean(div(day_wmean(Close, Volume), day_mean(Close)), 20)` |
| slot b seed 11 | 过 | 0.00 | `—` | 0.00 | 0.18 | 0.09 | 0.19 | 0.19 | 0.07 | `cross_mean(day_corr(Close, Volume), 20)` |
| slot b seed 12 | 过 | 0.00 | `—` | 0.00 | 0.08 | 0.18 | 0.56 | 0.10 | 0.22 | `cross_mean(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 13 | 过 | 0.00 | `—` | 0.00 | 0.02 | 0.02 | 0.14 | 0.03 | 0.25 | `cs_bucket_rank(cross_mean(day_signed_ratio(Ret, Amt), 20), cross_mean(day_mean(Ret), 20))` |
| slot b seed 14 | 过 | 0.00 | `—` | 0.00 | 0.06 | 0.04 | 0.22 | 0.06 | 0.00 | `cross_zscore(cross_mean(day_corr(Ret, Volume), 5), 60)` |
| slot b seed 15 | 过 | 0.00 | `—` | 0.00 | 0.26 | 0.32 | 0.57 | 0.27 | 0.13 | `sub(cross_mean(day_topw_mean(Ret, Volume), 20), cross_mean(day_mean(Ret), 20))` |
