# 相关度表:种子 2079,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.03 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.04 | 0.03 | 0.04 | 0.16 | 0.04 | 0.03 | `day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239))` |
| slot a seed 1 | 过 | 0.52 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.23 | 0.45 | 0.28 | 0.10 | 0.47 | 0.04 | `ts_stddev(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 20)` |
| slot a seed 2 | 过 | 0.63 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.47 | 0.46 | 0.17 | 0.04 | 0.45 | 0.07 | `ts_stddev(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 60)` |
| slot a seed 3 | 过 | 0.03 | `ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open` | 0.06 | 0.03 | 0.04 | 0.11 | 0.03 | 0.02 | `sub(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), cross_mean(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 40))` |
| slot a seed 4 | 过 | 0.17 | `ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open` | 0.04 | 0.18 | 0.20 | 0.45 | 0.19 | 0.03 | `mul(cross_mean(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 20), sign(cross_mean(day_sum(Ret), 20)))` |
| slot a seed 5 | 过 | 0.41 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.26 | 0.39 | 0.09 | 0.03 | 0.37 | 0.08 | `cross_corr(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), day_sum(Ret), 60)` |
| slot a seed 6 | 过 | 0.68 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.41 | 0.37 | 0.64 | 0.02 | 0.37 | 0.01 | `cross_regbeta(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), day_sum(Ret), 60)` |
| slot a seed 7 | 过 | 0.28 | `ts_max(ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10` | 0.06 | 0.35 | 0.10 | 0.01 | 0.32 | 0.19 | `ts_skew(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 60)` |
| slot a seed 8 | 过 | 0.40 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.21 | 0.20 | 0.18 | 0.09 | 0.23 | 0.17 | `ts_max(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 40)` |
| slot a seed 9 | 过 | 0.38 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.25 | 0.28 | 0.03 | 0.10 | 0.28 | 0.06 | `ts_min(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 40)` |
| slot a seed 10 | 过 | 0.32 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.09 | 0.30 | 0.41 | 0.41 | 0.33 | 0.01 | `cs_bucket_demean(cross_mean(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 30), LogFloatCap)` |
| slot a seed 11 | 过 | 0.48 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.19 | 0.49 | 0.25 | 0.09 | 0.48 | 0.06 | `sub(ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 20), ts_mean(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 20))` |
| slot a seed 12 | 过 | 0.09 | `ts_max(log(cross_regbeta(log(ts_max(log(cross_regbeta(log(da` | 0.27 | 0.05 | 0.01 | 0.18 | 0.04 | 0.03 | `cross_regres(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), day_corr(in_slice(Volume, 2, 240), in_slice(Ret, 1, 239)), 40)` |
| slot b seed 1 | 过 | 0.13 | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 24` | 0.19 | 0.00 | 0.17 | 0.61 | 0.02 | 0.14 | `cross_mean(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 2 | 过 | 0.02 | `ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open` | 0.12 | 0.03 | 0.04 | 0.10 | 0.03 | 0.01 | `cross_zscore(day_signed_ratio(Ret, Amt), 40)` |
| slot b seed 3 | 过 | 0.08 | `ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open` | 0.09 | 0.09 | 0.10 | 0.24 | 0.09 | 0.00 | `sub(cross_mean(day_signed_ratio(Ret, Amt), 5), cross_mean(day_signed_ratio(Ret, Amt), 60))` |
| slot b seed 4 | 过 | 0.26 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.06 | 0.11 | 0.41 | 0.55 | 0.16 | 0.09 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 20)` |
| slot b seed 5 | 过 | 0.02 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.06 | 0.02 | 0.04 | 0.10 | 0.02 | 0.02 | `cross_zscore(sub(day_wmean(Ret, Amt), day_mean(Ret)), 40)` |
| slot b seed 6 | 过 | 0.49 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.25 | 0.17 | 0.51 | 0.27 | 0.22 | 0.18 | `cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 30)` |
| slot b seed 7 | 过 | 0.29 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.11 | 0.24 | 0.41 | 0.64 | 0.26 | 0.05 | `cross_mean(day_topw_mean(Ret, Amt), 20)` |
| slot b seed 8 | 过 | 0.03 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.05 | 0.02 | 0.03 | 0.14 | 0.02 | 0.02 | `cross_zscore(day_topw_mean(Ret, Amt), 60)` |
| slot b seed 9 | 过 | 0.10 | `ts_max(log(cross_regbeta(log(ts_max(log(cross_regbeta(log(da` | 0.07 | 0.09 | 0.06 | 0.38 | 0.08 | 0.01 | `sub(cross_mean(day_topw_mean(Ret, Amt), 10), cross_mean(day_topw_mean(Ret, Amt), 40))` |
| slot b seed 10 | 过 | 0.22 | `ts_max(ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10` | 0.06 | 0.29 | 0.15 | 0.03 | 0.25 | 0.22 | `cross_corr(day_signed_ratio(Ret, Amt), day_sum(Ret), 40)` |
| slot b seed 11 | 过 | 0.14 | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 24` | 0.19 | 0.09 | 0.17 | 0.60 | 0.07 | 0.00 | `cs_bucket_demean(cross_mean(day_signed_ratio(Ret, Amt), 20), LogFloatCap)` |
| slot b seed 12 | 过 | 0.15 | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1` | 0.10 | 0.06 | 0.17 | 0.01 | 0.05 | 0.14 | `cross_mean(sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Volume)), 30)` |
