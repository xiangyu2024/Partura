# 相关度表:种子 2005,P 组,第 2 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.05 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.32 | 0.02 | 0.01 | 0.03 | 0.02 | 0.02 | `day_cov(Amt, Low)` |
| slot a seed 1 | 过 | 0.42 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.07 | 0.44 | 0.03 | 0.01 | 0.42 | 0.23 | `cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241)` |
| slot a seed 2 | 过 | 0.14 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.09 | 0.13 | 0.18 | 0.01 | 0.11 | 0.12 | `cross_mean(div(day_cov(Amt, Low), mul(day_mean(Amt), day_mean(Low))), 241)` |
| slot a seed 3 | 过 | 0.41 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.08 | 0.42 | 0.08 | 0.01 | 0.39 | 0.25 | `cross_mean(div(day_cov(Amt, Low), mul(day_mean(Amt), day_std(Low))), 120)` |
| slot a seed 4 | 过 | 0.47 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.10 | 0.47 | 0.02 | 0.01 | 0.45 | 0.22 | `cross_ema(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 60)` |
| slot a seed 5 | 过 | 0.18 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.09 | 0.14 | 0.15 | 0.11 | 0.14 | 0.01 | `cross_zscore(cross_ema(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 20), 241)` |
| slot a seed 6 | 过 | 0.15 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.07 | 0.11 | 0.14 | 0.14 | 0.11 | 0.02 | `sub(cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 20), cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241))` |
| slot a seed 7 | 过 | 0.57 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.14 | 0.57 | 0.01 | 0.04 | 0.53 | 0.18 | `cross_tail_mean_q75(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241)` |
| slot a seed 8 | 过 | 0.33 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.12 | 0.33 | 0.09 | 0.05 | 0.31 | 0.01 | `cross_tail_mean_q25(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241)` |
| slot a seed 9 | 过 | 0.47 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.08 | 0.49 | 0.02 | 0.01 | 0.46 | 0.23 | `div(cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241), cross_stddev(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241))` |
| slot a seed 10 | 过 | 0.61 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.22 | 0.60 | 0.14 | 0.04 | 0.57 | 0.14 | `cross_stddev(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 120)` |
| slot a seed 11 | 过 | 0.29 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.07 | 0.29 | 0.01 | 0.03 | 0.27 | 0.00 | `cs_bucket_zscore(cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241), LogFloatCap)` |
| slot a seed 12 | 过 | 0.36 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.06 | 0.39 | 0.05 | 0.01 | 0.37 | 0.37 | `cs_last_low10(cross_mean(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 241), ListAge)` |
| slot a seed 13 | 过 | 0.32 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.11 | 0.38 | 0.20 | 0.02 | 0.38 | 0.18 | `cross_mean(mul(sign(day_sum(Ret)), div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low)))), 120)` |
| slot a seed 14 | 过 | 0.36 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.11 | 0.41 | 0.24 | 0.01 | 0.42 | 0.13 | `cross_corr(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), day_sum(Ret), 120)` |
| slot a seed 15 | 过 | 0.17 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.10 | 0.14 | 0.18 | 0.01 | 0.12 | 0.12 | `cross_ema(div(day_cov(Amt, Low), mul(day_mean(Amt), day_mean(Low))), 120)` |
| slot a seed 16 | 过 | 0.14 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.10 | 0.12 | 0.08 | 0.03 | 0.11 | 0.02 | `cross_zscore(cross_mean(div(day_cov(Amt, Low), mul(day_mean(Amt), day_std(Low))), 60), 241)` |
| slot b seed 1 | 过 | 0.40 | `cross_max(day_cov(Ret, Close), 60)` | 0.32 | 0.28 | 0.04 | 0.06 | 0.23 | 0.02 | `sub(LogFloatCap, LogFloatShares)` |
| slot b seed 2 | 过 | 0.80 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.90 | 0.46 | 0.01 | 0.07 | 0.42 | 0.42 | `log(day_last(Close))` |
| slot b seed 3 | 过 | 0.44 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.58 | 0.17 | 0.03 | 0.02 | 0.18 | 0.45 | `sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 4 | 过 | 0.09 | `cross_max(day_cov(Ret, Close), 60)` | 0.06 | 0.01 | 0.08 | 0.03 | 0.01 | 0.42 | `sub(LogTotalCap, LogFloatCap)` |
| slot b seed 5 | 过 | 0.40 | `cross_max(day_cov(Ret, Close), 60)` | 0.32 | 0.24 | 0.01 | 0.06 | 0.19 | 0.02 | `cs_bucket_demean(sub(LogFloatCap, LogFloatShares), LogFloatCap)` |
| slot b seed 6 | 过 | 0.38 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.57 | 0.05 | 0.02 | 0.02 | 0.03 | 0.02 | `cs_bucket_zscore(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), LogFloatCap)` |
| slot b seed 7 | 过 | 0.29 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.07 | 0.32 | 0.04 | 0.01 | 0.29 | 0.07 | `cs_bucket_demean(sub(LogTotalCap, LogFloatCap), LogFloatCap)` |
| slot b seed 8 | 过 | 0.31 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.23 | 0.20 | 0.16 | 0.04 | 0.18 | 0.00 | `cs_last_low05(neg(sub(LogFloatCap, LogFloatShares)), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 9 | 过 | 0.56 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.64 | 0.40 | 0.02 | 0.05 | 0.38 | 0.46 | `cs_last_low05(neg(log(day_last(Close))), log(day_last(Close)))` |
| slot b seed 10 | 过 | 0.46 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.22 | 0.48 | 0.11 | 0.06 | 0.43 | 0.38 | `cs_last_high20(neg(sub(LogFloatCap, LogFloatShares)), LogFloatCap)` |
| slot b seed 11 | 过 | 0.37 | `cross_max(day_cov(Ret, Close), 60)` | 0.28 | 0.27 | 0.04 | 0.04 | 0.21 | 0.08 | `cs_last_low10(neg(sub(LogFloatCap, LogFloatShares)), ListAge)` |
| slot b seed 12 | 过 | 0.12 | `cross_mean(day_cov(Close, Ret), 3)` | 0.26 | 0.04 | 0.00 | 0.03 | 0.01 | 0.27 | `sub(sub(LogFloatCap, LogFloatShares), sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)))` |
| slot b seed 13 | 过 | 0.40 | `cross_max(day_cov(Ret, Close), 60)` | 0.32 | 0.28 | 0.04 | 0.06 | 0.23 | 0.02 | `log(div(day_sum(Amt), day_sum(Volume)))` |
| slot b seed 14 | 过 | 0.43 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.57 | 0.17 | 0.03 | 0.02 | 0.18 | 0.45 | `cross_mean(sub(log(day_last(Close)), log(div(day_sum(Amt), day_sum(Volume)))), 60)` |
| slot b seed 15 | 过 | 0.68 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.79 | 0.33 | 0.01 | 0.05 | 0.32 | 0.47 | `cs_bucket_zscore(cross_mean(sub(log(day_last(Close)), log(div(day_sum(Amt), day_sum(Volume)))), 60), sub(LogFloatCap, LogFloatShares))` |
| slot b seed 16 | 过 | 0.57 | `cross_max(day_cov(Ret, Close), 60)` | 0.55 | 0.40 | 0.05 | 0.08 | 0.34 | 0.23 | `cs_bucket_demean(sub(LogFloatCap, LogFloatShares), sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)))` |
| R 1 variant 1 | 过 | 0.92 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.91 | 0.48 | 0.33 | 0.02 | 0.47 | 0.26 | `cross_mean(day_cov(Close, Ret), 120)` |
| R 1 variant 2 | 过 | 0.88 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.89 | 0.45 | 0.26 | 0.03 | 0.43 | 0.24 | `cross_mean(day_cov(Close, Ret), 241)` |
| R 1 variant 3 | 过 | 0.34 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.17 | 0.38 | 0.00 | 0.01 | 0.33 | 0.13 | `cross_mean(div(day_cov(Close, Ret), mul(day_mean(Close), day_var(Ret))), 241)` |
| R 1 variant 4 | 过 | 0.55 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.57 | 0.31 | 0.10 | 0.04 | 0.31 | 0.26 | `cs_bucket_demean(cross_mean(day_cov(Close, Ret), 120), sub(LogFloatCap, LogFloatShares))` |
| R 1 variant 5 | 过 | 0.47 | `cross_max(day_cov(Ret, Close), 60)` | 0.34 | 0.33 | 0.23 | 0.00 | 0.31 | 0.08 | `cs_bucket_demean(cross_mean(day_cov(Close, Ret), 120), sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)))` |
| R 2 variant 1 | 过 | 0.79 | `cross_max(day_cov(Ret, Close), 60)` | 0.72 | 0.40 | 0.23 | 0.03 | 0.38 | 0.09 | `cross_max(day_cov(Ret, Close), 241)` |
| R 2 variant 2 | 过 | 0.84 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.84 | 0.48 | 0.25 | 0.03 | 0.46 | 0.19 | `cross_tail_mean_q75(day_cov(Ret, Close), 241)` |
| R 2 variant 3 | 过 | 0.37 | `cross_max(day_cov(Ret, Close), 60)` | 0.21 | 0.13 | 0.62 | 0.04 | 0.17 | 0.34 | `cross_tail_mean_q75(div(day_cov(Ret, Close), day_mean(Close)), 241)` |
| R 3 variant 1 | 过 | 0.49 | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cr` | 0.49 | 0.07 | 0.00 | 0.01 | 0.07 | 0.05 | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 60), 241)` |
| R 3 variant 2 | 过 | 0.26 | `cross_sum(cross_sum(neg(cross_cov(cross_min(neg(cross_min(cr` | 0.26 | 0.00 | 0.03 | 0.01 | 0.00 | 0.02 | `cross_sum(cross_sum(neg(cross_corr(cross_min(neg(cross_min(cross_mean(day_cov(Low, Ret), 60), 15)), 15), mul(day_autocorr_n1(High), day_std(Low)), 60)), 60), 120)` |
| R 4 variant 1 | 过 | 0.60 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.40 | 0.53 | 0.21 | 0.02 | 0.54 | 0.18 | `cs_bucket_zscore(cross_max(cross_max(cross_max(day_cov(Volume, Low), 5), 5), 120), LogFloatShares)` |
| R 4 variant 2 | 过 | 0.53 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.43 | 0.43 | 0.27 | 0.02 | 0.45 | 0.05 | `cs_bucket_zscore(cross_max(cross_max(cross_max(day_cov(Volume, Low), 5), 5), 60), LogFloatCap)` |
| R 4 variant 3 | 过 | 0.12 | `cross_sum(cross_sum(neg(cross_mean(day_cov(Close, Ret), 10))` | 0.10 | 0.03 | 0.23 | 0.01 | 0.01 | 0.03 | `cs_bucket_zscore(cross_mean(div(day_cov(Volume, Low), mul(day_mean(Volume), day_mean(Low))), 241), LogFloatShares)` |
| R 5 variant 1 | 过 | 0.21 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.20 | 0.34 | 0.14 | 0.02 | 0.33 | 0.16 | `div(ts_std(day_close(Amt), 120), ts_std(day_sum(Amt), 120))` |
| R 5 variant 2 | 过 | 0.17 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.17 | 0.28 | 0.10 | 0.00 | 0.27 | 0.15 | `div(ts_std(day_close(Amt), 241), ts_std(day_sum(Amt), 241))` |
