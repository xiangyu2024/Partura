# 相关度表:种子 2047,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.21 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.24 | 0.16 | 0.10 | 0.01 | 0.17 | 0.09 | `cross_autocorr(day_min(Ret), 120, 1)` |
| slot a seed 2 | 过 | 0.10 | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` | 0.17 | 0.01 | 0.02 | 0.00 | 0.01 | 0.05 | `sub(cross_autocorr(day_min(Ret), 120, 1), cross_autocorr(day_max(Ret), 120, 1))` |
| slot a seed 3 | 过 | 0.21 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.18 | 0.14 | 0.07 | 0.04 | 0.17 | 0.14 | `cross_mean(div(add(day_max(Ret), day_min(Ret)), sub(day_max(Ret), day_min(Ret))), 120)` |
| slot a seed 4 | 过 | 0.23 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.18 | 0.13 | 0.26 | 0.04 | 0.16 | 0.25 | `cross_mean(add(day_max(Ret), day_min(Ret)), 120)` |
| slot a seed 5 | 过 | 0.14 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.14 | 0.01 | 0.05 | 0.01 | 0.01 | 0.31 | `div(cross_tail_mean_q25(day_min(Ret), 120), cross_mean(day_min(Ret), 120))` |
| slot a seed 6 | 过 | 0.14 | `add(day_min(Ret), day_var(Open))` | 0.12 | 0.04 | 0.05 | 0.01 | 0.01 | 0.30 | `div(cross_stddev(day_min(Ret), 120), neg(cross_mean(day_min(Ret), 120)))` |
| slot a seed 7 | 过 | 0.13 | `add(day_min(Ret), day_var(Open))` | 0.29 | 0.19 | 0.05 | 0.04 | 0.21 | 0.34 | `cross_mean(div(day_min(Ret), day_std(Ret)), 120)` |
| slot a seed 8 | 过 | 0.03 | `add(day_min(Ret), day_var(Open))` | 0.04 | 0.04 | 0.06 | 0.01 | 0.05 | 0.01 | `cross_regbeta(cross_delay(day_min(Ret), 1), day_sum(Ret), 120)` |
| slot a seed 9 | 过 | 0.03 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.04 | 0.04 | 0.07 | 0.01 | 0.05 | 0.01 | `cross_corr(cross_delay(day_min(Ret), 1), day_sum(Ret), 120)` |
| slot a seed 10 | 过 | 0.05 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.04 | 0.07 | 0.10 | 0.02 | 0.08 | 0.00 | `cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_sum(Ret))), 120)` |
| slot a seed 11 | 过 | 0.09 | `add(day_min(Ret), day_var(Open))` | 0.08 | 0.02 | 0.01 | 0.02 | 0.01 | 0.12 | `cross_regbeta(cross_delay(day_min(Ret), 1), sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1), 120)` |
| slot a seed 12 | 过 | 0.22 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.12 | 0.18 | 0.34 | 0.12 | 0.21 | 0.07 | `cross_mean(cross_regres(cs_mean(day_min(Ret)), day_min(Ret), 120), 60)` |
| slot a seed 13 | 过 | 0.01 | `add(day_min(Ret), day_var(Open))` | 0.05 | 0.06 | 0.02 | 0.04 | 0.07 | 0.14 | `cross_regbeta(cs_mean(day_min(Ret)), day_min(Ret), 120)` |
| slot a seed 14 | 过 | 0.13 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.15 | 0.01 | 0.11 | 0.02 | 0.02 | 0.25 | `cross_corr(day_min(Ret), day_max(Ret), 120)` |
| slot a seed 15 | 过 | 0.17 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.18 | 0.11 | 0.09 | 0.02 | 0.14 | 0.08 | `cross_corr(day_min(Ret), cross_zscore(day_sum(Volume), 60), 120)` |
| slot a seed 16 | 过 | 0.23 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.17 | 0.17 | 0.22 | 0.04 | 0.18 | 0.09 | `cross_corr(day_min(Ret), cross_delay(day_sum(Ret), 1), 120)` |
| slot b seed 1 | 过 | 0.08 | `add(day_min(Ret), day_var(Open))` | 0.11 | 0.07 | 0.06 | 0.25 | 0.05 | 0.02 | `cross_mean(div(sub(day_last(Close), day_min(Low)), sub(day_max(High), day_min(Low))), 60)` |
| slot b seed 2 | 过 | 0.08 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.06 | 0.04 | 0.15 | 0.28 | 0.04 | 0.04 | `div(cross_sum(mul(sub(mul(2, div(sub(day_last(Close), day_min(Low)), sub(day_max(High), day_min(Low)))), 1), day_sum(Volume)), 60), cross_sum(day_sum(Volume), 60))` |
| slot b seed 3 | 过 | 0.03 | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` | 0.05 | 0.06 | 0.01 | 0.51 | 0.06 | 0.03 | `cross_zscore(cross_mean(div(sub(day_last(Close), day_min(Low)), sub(day_max(High), day_min(Low))), 20), 120)` |
| slot b seed 4 | 过 | 0.32 | `add(day_min(Ret), day_var(Open))` | 0.25 | 0.26 | 0.16 | 0.17 | 0.20 | 0.10 | `cross_mean(div(log(div(cross_delay(day_last(Close), 1), day_min(Low))), cross_mean(day_std(Ret), 20)), 60)` |
| slot b seed 5 | 过 | 0.31 | `add(day_min(Ret), day_var(Open))` | 0.27 | 0.15 | 0.18 | 0.11 | 0.10 | 0.07 | `cross_mean(div(log(div(day_first(Open), day_min(Low))), cross_mean(day_std(Ret), 20)), 60)` |
| slot b seed 6 | 过 | 0.43 | `add(day_min(Ret), day_var(Open))` | 0.20 | 0.44 | 0.21 | 0.21 | 0.41 | 0.14 | `cross_mean(div(log(div(day_last(Close), day_min(Low))), cross_mean(day_std(Ret), 20)), 60)` |
| slot b seed 7 | 过 | 0.40 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.22 | 0.41 | 0.41 | 0.28 | 0.43 | 0.07 | `cross_mean(sub(div(log(div(day_max(High), day_first(Open))), cross_mean(day_std(Ret), 20)), div(log(div(day_first(Open), day_min(Low))), cross_mean(day_std(Ret), 20))), 60)` |
| slot b seed 8 | 过 | 0.40 | `add(day_min(Ret), day_var(Open))` | 0.24 | 0.37 | 0.11 | 0.04 | 0.29 | 0.28 | `cross_mean(div(day_locate(Volume, day_argmin(Low)), day_mean(Volume)), 60)` |
| slot b seed 9 | 过 | 0.08 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.06 | 0.06 | 0.21 | 0.00 | 0.09 | 0.06 | `cross_regbeta(cross_delay(div(log(div(cross_delay(day_last(Close), 1), day_min(Low))), cross_mean(day_std(Ret), 20)), 1), sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1), 120)` |
| slot b seed 10 | 过 | 0.02 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.03 | 0.05 | 0.05 | 0.01 | 0.06 | 0.03 | `cross_regbeta(cross_delay(div(sub(day_last(Close), day_min(Low)), sub(day_max(High), day_min(Low))), 1), day_sum(Ret), 120)` |
| slot b seed 11 | 过 | 0.04 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.02 | 0.10 | 0.02 | 0.02 | 0.10 | 0.07 | `cross_autocorr(div(sub(day_last(Close), day_min(Low)), sub(day_max(High), day_min(Low))), 120, 1)` |
| slot b seed 12 | 过 | 0.45 | `add(day_min(Ret), day_var(Open))` | 0.22 | 0.46 | 0.18 | 0.16 | 0.43 | 0.14 | `cross_mean(div(log(div(day_wmean(Close, Amt), day_min(Low))), cross_mean(day_std(Ret), 20)), 60)` |
| slot b seed 13 | 过 | 0.06 | `add(day_min(Ret), day_var(Open))` | 0.13 | 0.04 | 0.26 | 0.20 | 0.08 | 0.01 | `cross_mean(div(day_argmin(Low), 240), 60)` |
| slot b seed 14 | 过 | 0.03 | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` | 0.06 | 0.06 | 0.01 | 0.52 | 0.06 | 0.03 | `sub(cross_mean(div(sub(day_last(Close), day_min(Low)), sub(day_max(High), day_min(Low))), 20), cross_mean(div(sub(day_last(Close), day_min(Low)), sub(day_max(High), day_min(Low))), 120))` |
| slot b seed 15 | 过 | 0.22 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.12 | 0.21 | 0.24 | 0.32 | 0.23 | 0.03 | `cross_mean(div(sub(day_last(Close), day_first(Open)), sub(day_max(High), day_min(Low))), 60)` |
| slot b seed 16 | 过 | 0.20 | `add(day_min(Ret), day_var(Open))` | 0.11 | 0.20 | 0.15 | 0.06 | 0.18 | 0.06 | `cross_regbeta(div(log(div(cross_delay(day_last(Close), 1), day_min(Low))), cross_mean(day_std(Ret), 20)), div(log(div(day_last(Close), day_min(Low))), cross_mean(day_std(Ret), 20)), 120)` |
| R 1 variant 1 | 过 | 0.41 | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` | 0.62 | 0.15 | 0.16 | 0.07 | 0.18 | 0.04 | `cross_autocorr(day_min(Ret), 30, 1)` |
| R 1 variant 2 | 过 | 0.26 | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` | 0.42 | 0.18 | 0.15 | 0.04 | 0.20 | 0.06 | `cross_autocorr(day_min(Ret), 60, 1)` |
| R 1 variant 3 | 过 | 0.29 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.37 | 0.23 | 0.18 | 0.04 | 0.25 | 0.06 | `cross_autocorr(cs_rank(day_min(Ret)), 60, 1)` |
| R 1 variant 4 | 过 | 0.26 | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` | 0.42 | 0.18 | 0.15 | 0.05 | 0.20 | 0.06 | `cross_regbeta(cross_delay(day_min(Ret), 1), day_min(Ret), 60)` |
| R 1 variant 5 | 过 | 0.26 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.38 | 0.18 | 0.17 | 0.05 | 0.20 | 0.08 | `cross_autocorr(cs_demean(day_min(Ret)), 60, 1)` |
| R 1 variant 6 | 过 | 0.16 | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` | 0.27 | 0.02 | 0.05 | 0.00 | 0.01 | 0.03 | `cross_autocorr(div(day_min(Ret), day_std(Ret)), 60, 1)` |
| R 2 variant 1 | 过 | 0.41 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.49 | 0.13 | 0.18 | 0.11 | 0.15 | 0.14 | `cross_corr(day_min(High), day_mean(Amt), 60)` |
| R 2 variant 2 | 过 | 0.37 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.47 | 0.06 | 0.12 | 0.12 | 0.09 | 0.18 | `cross_corr(day_min(High), day_mean(Volume), 60)` |
| R 2 variant 3 | 过 | 0.60 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.66 | 0.47 | 0.23 | 0.08 | 0.49 | 0.21 | `cross_cov(day_min(High), day_mean(Volume), 60)` |
| R 2 variant 4 | 过 | 0.59 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.66 | 0.46 | 0.23 | 0.08 | 0.48 | 0.21 | `cross_cov(day_min(Low), day_mean(Volume), 60)` |
| R 2 variant 5 | 过 | 0.23 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.29 | 0.02 | 0.07 | 0.06 | 0.04 | 0.20 | `cross_corr(day_min(High), day_mean(Volume), 120)` |
| R 2 variant 6 | 过 | 0.33 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.33 | 0.12 | 0.21 | 0.16 | 0.15 | 0.16 | `cross_corr(cross_delta(log(day_min(High)), 1), cross_delta(log(day_mean(Volume)), 1), 60)` |
| R 2 variant 7 | 过 | 0.22 | `cross_cov(day_min(High), day_mean(Amt), 30)` | 0.26 | 0.03 | 0.12 | 0.10 | 0.05 | 0.21 | `cross_regbeta(cross_delta(log(day_mean(Volume)), 1), cross_delta(log(day_min(High)), 1), 120)` |
