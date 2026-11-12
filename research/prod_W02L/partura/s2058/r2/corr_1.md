# 相关度表:种子 2058,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.43 | `day_std(pow_2(Volume))` | 0.45 | 0.20 | 0.00 | 0.02 | 0.22 | 0.03 | `day_quantile(cross_regbeta(Open, Amt, 241))` |
| slot a seed 1 | 过 | 0.32 | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_co` | 0.43 | 0.10 | 0.02 | 0.02 | 0.07 | 0.20 | `cross_ema(div(day_quantile(cross_regbeta(Open, Amt, 241)), day_last(Open)), 20)` |
| slot a seed 2 | 过 | 0.47 | `day_std(pow_2(Volume))` | 0.43 | 0.33 | 0.00 | 0.02 | 0.34 | 0.16 | `cs_regres(day_quantile(cross_regbeta(Open, Amt, 241)), day_last(Open))` |
| slot a seed 3 | 过 | 0.29 | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_co` | 0.38 | 0.26 | 0.05 | 0.01 | 0.22 | 0.57 | `cs_regres(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap)` |
| slot a seed 4 | 过 | 0.07 | `cross_mean(day_std(pow_2(Ret)), 20)` | 0.02 | 0.04 | 0.06 | 0.10 | 0.05 | 0.01 | `sub(day_quantile(cross_regbeta(Open, Amt, 241)), ts_delay(day_quantile(cross_regbeta(Open, Amt, 241)), 20))` |
| slot a seed 5 | 过 | 0.13 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.05 | 0.10 | 0.10 | 0.05 | 0.11 | 0.03 | `sub(day_quantile(cross_regbeta(Open, Amt, 241)), ts_delay(day_quantile(cross_regbeta(Open, Amt, 241)), 60))` |
| slot a seed 6 | 过 | 0.14 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.04 | 0.11 | 0.10 | 0.07 | 0.12 | 0.03 | `cross_zscore(day_quantile(cross_regbeta(Open, Amt, 241)), 120)` |
| slot a seed 7 | 过 | 0.39 | `day_std(pow_2(Volume))` | 0.44 | 0.16 | 0.02 | 0.00 | 0.18 | 0.01 | `cross_ema(cs_bucket_rank(day_quantile(cross_regbeta(Open, Amt, 241)), LogFloatCap), 20)` |
| slot a seed 8 | 过 | 0.51 | `day_std(pow_2(Volume))` | 0.40 | 0.50 | 0.03 | 0.04 | 0.51 | 0.29 | `cs_bucket_rank(day_quantile(cross_regbeta(Open, Amt, 241)), day_last(Open))` |
| slot a seed 9 | 过 | 0.22 | `day_std(pow_2(Volume))` | 0.45 | 0.14 | 0.04 | 0.00 | 0.10 | 0.34 | `cs_bucket_demean(day_quantile(cross_regbeta(Open, Amt, 241)), LogTotalCap)` |
| slot a seed 10 | 过 | 0.14 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.11 | 0.13 | 0.08 | 0.00 | 0.12 | 0.09 | `cross_ema(sub(cs_rank(day_quantile(cross_regbeta(Open, Amt, 241))), cs_rank(day_quantile(cross_regbeta(Open, Amt, 60)))), 20)` |
| slot a seed 11 | 过 | 0.32 | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_co` | 0.38 | 0.41 | 0.15 | 0.06 | 0.39 | 0.36 | `div(day_quantile(cross_regbeta(Open, Amt, 241)), cross_mean(day_std(Amt), 120))` |
| slot a seed 12 | 过 | 0.43 | `day_std(pow_2(Volume))` | 0.45 | 0.20 | 0.00 | 0.02 | 0.22 | 0.03 | `cs_robust_z(day_quantile(cross_regbeta(Open, Amt, 241)))` |
| slot b seed 1 | 过 | 0.21 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.11 | 0.25 | 0.07 | 0.13 | 0.24 | 0.03 | `cross_mean(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 2 | 过 | 0.16 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.14 | 0.16 | 0.05 | 0.09 | 0.16 | 0.07 | `cross_ema(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), 120)` |
| slot b seed 3 | 过 | 0.36 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.12 | 0.38 | 0.36 | 0.21 | 0.39 | 0.07 | `sub(cross_mean(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_open(Open)), 1), 60))` |
| slot b seed 4 | 过 | 0.12 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.10 | 0.16 | 0.03 | 0.23 | 0.15 | 0.00 | `cs_regres(cross_mean(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), 60), cross_mean(sub(div(day_last(Close), day_open(Open)), 1), 60))` |
| slot b seed 5 | 过 | 0.05 | `cross_mean(sqrt(neg(neg(sigmoid(day_std(pow_2(Ret)))))), 3)` | 0.03 | 0.02 | 0.04 | 0.04 | 0.03 | 0.02 | `cross_zscore(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 6 | 过 | 0.35 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.19 | 0.31 | 0.15 | 0.07 | 0.32 | 0.05 | `cross_ema(cs_bucket_rank(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), LogFloatCap), 60)` |
| slot b seed 7 | 过 | 0.43 | `cross_mean(day_std(pow_2(Ret)), 20)` | 0.14 | 0.37 | 0.45 | 0.35 | 0.39 | 0.07 | `cross_mean(sub(div(day_last(Close), day_open(Open)), 1), 60)` |
| slot b seed 8 | 过 | 0.60 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.47 | 0.42 | 0.52 | 0.02 | 0.45 | 0.07 | `cross_stddev(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), 60)` |
| slot b seed 9 | 过 | 0.17 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.15 | 0.16 | 0.04 | 0.09 | 0.16 | 0.04 | `cross_ema(div(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), LimitWidth), 120)` |
| slot b seed 10 | 过 | 0.24 | `ts_max(ts_max(log(cross_regbeta(day_corr(nt_ts_quantile_q25(` | 0.13 | 0.29 | 0.06 | 0.11 | 0.28 | 0.07 | `cs_regres(cross_ema(sub(div(day_open(Open), ts_delay(day_last(Close), 1)), 1), 60), LogFloatCap)` |
| R 1 variant 1 | 过 | 0.99 | `day_sum(sigmoid(Vwap))` | 0.99 | 0.53 | 0.11 | 0.13 | 0.53 | 0.44 | `day_sum(sigmoid(div(Vwap, day_last(Close))))` |
| R 1 variant 2 | 过 | 0.93 | `day_sum(sigmoid(Vwap))` | 0.95 | 0.47 | 0.09 | 0.14 | 0.47 | 0.39 | `day_sum(sigmoid(sub(Vwap, day_mean(Vwap))))` |
| R 1 variant 3 | 过 | 0.82 | `day_sum(sigmoid(Vwap))` | 0.92 | 0.62 | 0.05 | 0.01 | 0.60 | 0.54 | `cross_ema(day_sum(sigmoid(Vwap)), 20)` |
| R 1 variant 4 | 废品 | 0.65 | `pow_2(cs_rank(ts_decay_linear(pow_2(day_autocorr_n1(nt_ts_co` | 0.52 | 0.20 | 0.05 | 0.02 | 0.17 | 0.09 | `day_sum(sigmoid(Open))` |
| R 1 variant 5 | 过 | 0.49 | `day_sum(sigmoid(Vwap))` | 0.36 | 0.29 | 0.26 | 0.48 | 0.31 | 0.21 | `cross_ema(day_sum(sigmoid(sub(Vwap, cross_mean(Vwap, 20)))), 20)` |
| R 1 variant 6 | 过 | 0.91 | `day_sum(sigmoid(Vwap))` | 0.82 | 0.49 | 0.20 | 0.37 | 0.50 | 0.40 | `day_sum(sigmoid(div(Vwap, cross_mean(Vwap, 60))))` |
