# 相关度表:种子 2019,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 12 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.29 | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_qu` | 0.24 | 0.56 | 0.19 | 0.18 | 0.60 | 0.46 | `day_last(Volume)` |
| slot a seed 1 | 过 | 0.06 | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q` | 0.05 | 0.06 | 0.00 | 0.01 | 0.07 | 0.06 | `cross_regbeta(cross_delay(mul(day_last(Volume), day_last(Ret)), 1), day_sum(Ret), 241)` |
| slot a seed 2 | 过 | 0.29 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.34 | 0.11 | 0.04 | 0.00 | 0.10 | 0.06 | `cross_regbeta(cross_delay(div(day_last(Volume), day_sum(Volume)), 1), day_sum(Ret), 241)` |
| slot a seed 3 | 过 | 0.87 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.88 | 0.14 | 0.12 | 0.01 | 0.14 | 0.07 | `cross_regbeta(cross_delay(day_last(Volume), 1), day_sum(Ret), 241)` |
| slot a seed 4 | 过 | 0.11 | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(cross` | 0.12 | 0.28 | 0.05 | 0.01 | 0.28 | 0.51 | `cross_regbeta(cross_delay(day_last(Volume), 1), sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 241)` |
| slot a seed 5 | 过 | 0.87 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.88 | 0.14 | 0.12 | 0.01 | 0.15 | 0.09 | `cross_regbeta(cross_delay(day_last(Volume), 1), sub(div(day_close(Close), day_open(Open)), 1), 241)` |
| slot a seed 6 | 过 | 0.65 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.70 | 0.16 | 0.09 | 0.01 | 0.17 | 0.14 | `cross_ema(cross_regbeta(cross_delay(day_last(Volume), 1), day_sum(Ret), 120), 60)` |
| slot a seed 7 | 过 | 0.93 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.93 | 0.20 | 0.09 | 0.01 | 0.20 | 0.14 | `cross_regbeta(cross_delay(mul(day_last(Volume), day_mean(High)), 1), day_sum(Ret), 241)` |
| slot a seed 8 | 过 | 0.81 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.82 | 0.12 | 0.11 | 0.00 | 0.12 | 0.04 | `cross_regbeta(cross_delay(mul(day_last(Volume), day_skew(Volume)), 1), day_sum(Ret), 241)` |
| slot a seed 9 | 过 | 0.81 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.81 | 0.11 | 0.14 | 0.01 | 0.11 | 0.03 | `cross_regbeta(cross_delay(sqrt(day_last(Volume)), 1), day_sum(Ret), 241)` |
| slot a seed 10 | 过 | 0.38 | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cr` | 0.36 | 0.23 | 0.10 | 0.01 | 0.23 | 0.21 | `cross_regbeta(cross_delay(cross_mean(day_last(Volume), 20), 1), day_sum(Ret), 241)` |
| slot a seed 11 | 过 | 0.68 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.72 | 0.08 | 0.13 | 0.01 | 0.08 | 0.02 | `cross_regbeta(cross_delay(div(day_last(Volume), cross_mean(day_last(Volume), 60)), 1), day_sum(Ret), 241)` |
| slot a seed 12 | 过 | 0.62 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.70 | 0.03 | 0.13 | 0.00 | 0.03 | 0.08 | `cross_regbeta(day_sum(Ret), cross_delay(day_last(Volume), 1), 241)` |
| slot a seed 13 | 过 | 0.63 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.70 | 0.01 | 0.11 | 0.00 | 0.01 | 0.07 | `cross_cov(cross_delay(day_last(Volume), 1), day_sum(Ret), 241)` |
| slot a seed 14 | 过 | 0.69 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.72 | 0.04 | 0.08 | 0.02 | 0.05 | 0.03 | `cross_regbeta(cross_delay(sub(day_last(Volume), cross_mean(day_last(Volume), 20)), 1), day_sum(Ret), 241)` |
| slot b seed 1 | 过 | 0.08 | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_qu` | 0.08 | 0.03 | 0.01 | 0.01 | 0.01 | 0.04 | `cross_regbeta(cross_delay(day_signed_ratio(Ret, Amt), 1), day_sum(Ret), 241)` |
| slot b seed 2 | 过 | 0.07 | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cr` | 0.07 | 0.08 | 0.03 | 0.00 | 0.07 | 0.02 | `cross_regbeta(cross_delay(day_centroid(Volume), 1), day_sum(Ret), 241)` |
| slot b seed 3 | 过 | 0.05 | `signedpower(cross_quantile_q75(cross_corr(day_mean(High), mu` | 0.04 | 0.03 | 0.04 | 0.01 | 0.02 | 0.01 | `cross_regbeta(cross_delay(mul(day_centroid(Volume), day_signed_ratio(Ret, Amt)), 1), day_sum(Ret), 241)` |
| slot b seed 4 | 过 | 0.05 | `signedpower(cross_quantile_q75(cross_corr(day_mean(High), mu` | 0.07 | 0.13 | 0.01 | 0.01 | 0.11 | 0.11 | `cross_regbeta(cross_delay(mul(day_signed_ratio(Ret, Amt), day_sum(Amt)), 1), day_sum(Ret), 241)` |
| slot b seed 5 | 过 | 0.05 | `signedpower(cross_quantile_q75(cross_corr(day_mean(High), mu` | 0.06 | 0.04 | 0.04 | 0.00 | 0.03 | 0.01 | `cross_regbeta(cross_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1), day_sum(Ret), 241)` |
| slot b seed 6 | 过 | 0.05 | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_s` | 0.05 | 0.01 | 0.01 | 0.01 | 0.01 | 0.01 | `cross_corr(cross_delay(day_signed_ratio(Ret, Amt), 1), day_sum(Ret), 120)` |
| slot b seed 7 | 过 | 0.07 | `signedpower(cross_quantile_q75(cross_corr(day_mean(High), mu` | 0.06 | 0.00 | 0.02 | 0.01 | 0.01 | 0.03 | `cross_ema(cross_regbeta(cross_delay(day_signed_ratio(Ret, Amt), 1), day_sum(Ret), 60), 60)` |
| slot b seed 8 | 过 | 0.59 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.58 | 0.25 | 0.15 | 0.00 | 0.25 | 0.15 | `cross_regbeta(cross_delay(mul(day_centroid(Amt), day_sum(Amt)), 1), day_sum(Ret), 241)` |
| slot b seed 9 | 过 | 0.09 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.07 | 0.16 | 0.04 | 0.01 | 0.14 | 0.09 | `cross_regbeta(cross_delay(cross_mean(mul(day_signed_ratio(Ret, Amt), day_sum(Amt)), 5), 1), day_sum(Ret), 241)` |
| slot b seed 10 | 过 | 0.13 | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cr` | 0.13 | 0.02 | 0.01 | 0.01 | 0.01 | 0.01 | `cross_regbeta(cross_delay(day_gini(Volume), 1), day_sum(Ret), 241)` |
| slot b seed 11 | 过 | 0.53 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.51 | 0.24 | 0.14 | 0.00 | 0.23 | 0.13 | `cross_regbeta(cross_delay(mul(day_gini(Volume), day_sum(Amt)), 1), day_sum(Ret), 241)` |
| slot b seed 12 | 过 | 0.07 | `signedpower(cross_quantile_q75(cross_corr(day_mean(High), mu` | 0.04 | 0.08 | 0.04 | 0.00 | 0.06 | 0.04 | `cross_regbeta(cross_delay(day_topw_mean(Ret, Volume), 1), day_sum(Ret), 241)` |
| slot b seed 13 | 过 | 0.10 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High),` | 0.08 | 0.17 | 0.05 | 0.01 | 0.16 | 0.10 | `cross_regbeta(cross_delay(mul(day_topw_mean(Ret, Volume), day_sum(Amt)), 1), day_sum(Ret), 241)` |
