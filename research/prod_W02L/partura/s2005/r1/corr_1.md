# 相关度表:种子 2005,P 组,第 1 轮(train 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.57 | `cross_max(day_cov(Ret, Close), 60)` | 0.70 | 0.34 | 0.34 | 0.18 | 0.34 | 0.23 | `day_cov(Ret, Close)` |
| slot a seed 1 | 过 | 0.40 | `cross_max(day_cov(Ret, Close), 60)` | 0.27 | 0.14 | 0.81 | 0.02 | 0.20 | 0.21 | `cross_mean(div(day_cov(Ret, Close), day_mean(Close)), 60)` |
| slot a seed 2 | 过 | 0.44 | `cross_max(day_cov(Ret, Close), 60)` | 0.19 | 0.42 | 0.53 | 0.04 | 0.42 | 0.04 | `cross_mean(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 60)` |
| slot a seed 3 | 过 | 0.52 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.23 | 0.52 | 0.02 | 0.02 | 0.46 | 0.12 | `cross_mean(div(day_cov(Ret, Close), mul(day_std(Ret), day_std(Close))), 60)` |
| slot a seed 4 | 过 | 0.46 | `cross_max(day_cov(Ret, Close), 60)` | 0.33 | 0.19 | 0.39 | 0.00 | 0.21 | 0.19 | `cross_max(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 60)` |
| slot a seed 5 | 过 | 0.44 | `cross_max(day_cov(Ret, Close), 60)` | 0.24 | 0.34 | 0.52 | 0.04 | 0.37 | 0.14 | `cross_min(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 60)` |
| slot a seed 6 | 过 | 0.49 | `cross_max(day_cov(Ret, Close), 60)` | 0.35 | 0.24 | 0.45 | 0.01 | 0.26 | 0.22 | `cross_tail_mean_q75(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 60)` |
| slot a seed 7 | 废品 | 0.05 | `cross_max(day_cov(Ret, Close), 60)` | 0.01 | 0.05 | 0.03 | 0.01 | 0.04 | 0.01 | `cross_semistd_pos(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 60)` |
| slot a seed 8 | 过 | 0.42 | `cross_max(day_cov(Ret, Close), 60)` | 0.18 | 0.38 | 0.50 | 0.04 | 0.38 | 0.06 | `cs_bucket_zscore(cross_mean(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 60), LogFloatCap)` |
| slot a seed 9 | 过 | 0.53 | `cross_max(day_cov(Ret, Close), 60)` | 0.43 | 0.22 | 0.68 | 0.08 | 0.27 | 0.13 | `cs_bucket_zscore(cross_mean(day_cov(Ret, Close), 60), day_last(Close))` |
| slot a seed 10 | 过 | 0.18 | `cross_max(day_cov(Ret, Close), 60)` | 0.19 | 0.08 | 0.16 | 0.06 | 0.00 | 0.15 | `cs_bucket_demean(cross_mean(div(day_cov(Ret, Close), mul(day_std(Ret), day_std(Close))), 60), cross_mean(day_std(Amt), 30))` |
| slot a seed 11 | 过 | 0.07 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.11 | 0.08 | 0.25 | 0.23 | 0.11 | 0.01 | `cross_zscore(cross_mean(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 20), 120)` |
| slot a seed 12 | 过 | 0.07 | `cross_max(day_cov(Ret, Close), 60)` | 0.15 | 0.02 | 0.08 | 0.24 | 0.00 | 0.07 | `sub(cross_mean(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 10), cross_mean(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 120))` |
| slot a seed 13 | 过 | 0.10 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.17 | 0.18 | 0.08 | 0.01 | 0.15 | 0.16 | `div(cross_mean(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 60), cross_stddev(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 60))` |
| slot a seed 14 | 过 | 0.46 | `cross_max(day_cov(Ret, Close), 60)` | 0.20 | 0.43 | 0.54 | 0.04 | 0.43 | 0.07 | `cross_ema(sub(div(day_cov(Ret, Close), day_mean(Close)), mul(0.5, day_var(Ret))), 40)` |
| slot a seed 15 | 过 | 0.03 | `cross_max(day_cov(Ret, Close), 60)` | 0.08 | 0.02 | 0.15 | 0.06 | 0.01 | 0.08 | `cross_mean(mul(sign(day_sum(Ret)), div(day_cov(Ret, Close), day_mean(Close))), 60)` |
| slot a seed 16 | 过 | 0.34 | `cross_max(day_cov(Ret, Close), 60)` | 0.19 | 0.11 | 0.74 | 0.01 | 0.16 | 0.24 | `cross_mean(div(day_cov(Ret, Close), day_mean(Close)), 120)` |
| slot b seed 1 | 算不出:OutOfMemoryError: CUDA out of memory. Tried to allocate 20.0 | | | | | | | | | `cross_mean(div(day_close(Amt), day_sum(Amt)), 40)` |
| slot b seed 2 | 算不出:OutOfMemoryError: CUDA out of memory. Tried to allocate 20.0 | | | | | | | | | `cross_mean(div(day_close(Volume), day_sum(Volume)), 40)` |
| slot b seed 3 | 算不出:OutOfMemoryError: CUDA out of memory. Tried to allocate 20.0 | | | | | | | | | `cs_bucket_zscore(cross_mean(div(day_close(Amt), day_sum(Amt)), 40), LogFloatShares)` |
| slot b seed 4 | 算不出:OutOfMemoryError: CUDA out of memory. Tried to allocate 20.0 | | | | | | | | | `cs_bucket_zscore(cross_mean(div(day_close(Amt), day_sum(Amt)), 40), ListAge)` |
| slot b seed 5 | 算不出:OutOfMemoryError: CUDA out of memory. Tried to allocate 20.0 | | | | | | | | | `cross_stddev(div(day_close(Amt), day_sum(Amt)), 60)` |
| slot b seed 6 | 算不出:OutOfMemoryError: CUDA out of memory. Tried to allocate 20.0 | | | | | | | | | `div(cross_stddev(div(day_close(Amt), day_sum(Amt)), 60), cross_mean(div(day_close(Amt), day_sum(Amt)), 60))` |
| slot b seed 7 | 算不出:OutOfMemoryError: CUDA out of memory. Tried to allocate 20.0 | | | | | | | | | `cross_zscore(cross_mean(div(day_close(Amt), day_sum(Amt)), 10), 120)` |
| slot b seed 8 | 过 | 0.39 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.32 | 0.51 | 0.05 | 0.01 | 0.45 | 0.42 | `cross_tail_mean_q75(div(day_close(Amt), day_sum(Amt)), 60)` |
| slot b seed 9 | 过 | 0.20 | `cross_max(day_cov(Ret, Close), 60)` | 0.06 | 0.22 | 0.28 | 0.07 | 0.25 | 0.07 | `cross_corr(div(day_close(Amt), day_sum(Amt)), day_sum(Ret), 60)` |
| slot b seed 10 | 过 | 0.11 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.07 | 0.08 | 0.12 | 0.07 | 0.10 | 0.00 | `cross_corr(div(day_close(Amt), day_sum(Amt)), div(day_first(Open), ts_delay(day_close(Close), 1)), 60)` |
| slot b seed 11 | 过 | 0.27 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.13 | 0.27 | 0.09 | 0.05 | 0.24 | 0.05 | `cross_mean(mul(div(day_close(Amt), day_sum(Amt)), sign(day_sum(in_slice(Ret, 211, 241)))), 40)` |
| slot b seed 12 | 过 | 0.06 | `cross_max(day_cov(Ret, Close), 60)` | 0.06 | 0.01 | 0.03 | 0.13 | 0.01 | 0.10 | `cross_mean(day_signed_ratio(in_slice(Ret, 211, 241), in_slice(Amt, 211, 241)), 40)` |
| slot b seed 13 | 过 | 0.06 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.09 | 0.03 | 0.06 | 0.07 | 0.03 | 0.02 | `sub(cross_mean(div(day_close(Amt), day_sum(Amt)), 20), cross_mean(div(day_close(Amt), day_sum(Amt)), 120))` |
| slot b seed 14 | 过 | 0.42 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.33 | 0.33 | 0.09 | 0.09 | 0.30 | 0.05 | `cross_mean(div(day_close(Amt), day_max(Amt)), 40)` |
| slot b seed 15 | 过 | 0.28 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.30 | 0.37 | 0.02 | 0.04 | 0.32 | 0.49 | `cross_ema(div(day_close(Amt), day_sum(Amt)), 40)` |
| slot b seed 16 | 过 | 0.35 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.24 | 0.45 | 0.30 | 0.09 | 0.47 | 0.29 | `cross_mean(sub(div(day_close(Amt), day_sum(Amt)), div(day_first(Amt), day_sum(Amt))), 40)` |
| R 1 variant 1 | 过 | 0.30 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.45 | 0.43 | 0.18 | 0.07 | 0.43 | 0.15 | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Volume, Low), 5), 5), 60), cross_mean(day_std(Amt), 30))` |
| R 1 variant 2 | 过 | 0.50 | `cross_max(day_cov(Ret, Close), 60)` | 0.72 | 0.08 | 0.06 | 0.07 | 0.05 | 0.04 | `cs_bucket_zscore(cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 60), cross_mean(day_std(Amt), 30))` |
| R 1 variant 3 | 过 | 0.33 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.44 | 0.07 | 0.34 | 0.03 | 0.11 | 0.24 | `cross_max(cross_max(cross_max(div(day_cov(Volume, Low), mul(day_mean(Volume), day_mean(Low))), 5), 5), 60)` |
| R 1 variant 4 | 过 | 0.50 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.32 | 0.38 | 0.14 | 0.04 | 0.38 | 0.09 | `cross_max(cross_max(cross_max(div(day_cov(Amt, Low), mul(day_std(Amt), day_std(Low))), 5), 5), 30)` |
| R 1 variant 5 | 过 | 0.73 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.57 | 0.59 | 0.28 | 0.01 | 0.61 | 0.22 | `cs_bucket_zscore(cross_max(cross_max(cross_max(day_cov(Volume, Low), 5), 5), 60), LogFloatShares)` |
| R 1 variant 6 | 过 | 0.27 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.75 | 0.43 | 0.17 | 0.05 | 0.45 | 0.23 | `cs_bucket_demean(cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30), cross_mean(day_std(Amt), 30))` |
| R 2 variant 1 | 过 | 0.44 | `cross_max(day_cov(Ret, Close), 60)` | 0.36 | 0.09 | 0.51 | 0.01 | 0.13 | 0.34 | `cross_max(div(day_cov(Ret, Close), day_mean(Close)), 120)` |
| R 2 variant 2 | 过 | 0.36 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.14 | 0.36 | 0.08 | 0.03 | 0.30 | 0.06 | `cross_max(div(day_cov(Ret, Close), mul(day_std(Ret), day_std(Close))), 120)` |
| R 2 variant 3 | 过 | 0.16 | `cross_max(day_cov(Ret, Close), 60)` | 0.10 | 0.00 | 0.34 | 0.09 | 0.04 | 0.33 | `cs_bucket_demean(cross_max(day_cov(Ret, Close), 120), day_last(Close))` |
| R 2 variant 4 | 过 | 0.44 | `cross_max(day_cov(Ret, Close), 60)` | 0.72 | 0.26 | 0.02 | 0.07 | 0.28 | 0.25 | `cs_bucket_demean(cross_max(day_cov(Ret, Close), 120), cross_mean(day_std(Amt), 30))` |
| R 3 variant 1 | 过 | 0.90 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.83 | 0.76 | 0.34 | 0.14 | 0.77 | 0.41 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), div(ts_std(day_close(Amt), 50), ts_mean(day_close(Amt), 50))), 5)` |
| R 3 variant 2 | 过 | 0.20 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.56 | 0.27 | 0.25 | 0.12 | 0.29 | 0.15 | `cs_bucket_demean(ts_std(day_close(Amt), 50), cross_mean(day_std(Amt), 30))` |
| R 3 variant 3 | 过 | 0.37 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 30)` | 0.27 | 0.39 | 0.19 | 0.05 | 0.39 | 0.17 | `div(ts_std(day_close(Amt), 50), ts_std(day_sum(Amt), 50))` |
| R 3 variant 4 | 过 | 0.58 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15)` | 0.49 | 0.77 | 0.30 | 0.07 | 0.79 | 0.44 | `cs_bucket_demean(cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 15), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 5), cross_mean(day_std(Amt), 30))` |
