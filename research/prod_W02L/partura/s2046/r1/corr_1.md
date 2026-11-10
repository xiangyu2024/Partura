# 相关度表:种子 2046,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.58 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.55 | 0.52 | 0.26 | 0.13 | 0.49 | 0.36 | `day_var(Low)` |
| slot a seed 1 | 过 | 0.11 | `ts_sum(day_var(Amt), 50)` | 0.05 | 0.10 | 0.11 | 0.02 | 0.10 | 0.00 | `cross_regbeta(cross_delay(cross_zscore(log(day_var(Low)), 60), 1), day_sum(Ret), 120)` |
| slot a seed 2 | 过 | 0.10 | `ts_sum(day_var(Amt), 50)` | 0.04 | 0.09 | 0.11 | 0.03 | 0.09 | 0.00 | `cross_corr(cross_delay(cross_zscore(log(day_var(Low)), 60), 1), day_sum(Ret), 120)` |
| slot a seed 3 | 过 | 0.13 | `ts_sum(day_var(Amt), 50)` | 0.05 | 0.12 | 0.14 | 0.04 | 0.12 | 0.00 | `cross_reg_tvalue(cross_delay(cross_zscore(log(day_var(Low)), 60), 1), cs_demean(day_sum(Ret)), 120)` |
| slot a seed 4 | 过 | 0.05 | `ts_sum(day_var(Amt), 50)` | 0.02 | 0.07 | 0.02 | 0.00 | 0.06 | 0.05 | `cross_regbeta(cross_delay(mul(sign(day_sum(Ret)), cross_zscore(log(day_var(Low)), 60)), 1), day_sum(Ret), 120)` |
| slot a seed 5 | 过 | 0.09 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.05 | 0.10 | 0.05 | 0.01 | 0.10 | 0.05 | `cross_corr(cross_delay(mul(sign(day_sum(Ret)), cross_zscore(log(day_var(Low)), 60)), 1), day_sum(Ret), 241)` |
| slot a seed 6 | 过 | 0.11 | `ts_sum(day_var(Amt), 50)` | 0.14 | 0.06 | 0.14 | 0.04 | 0.08 | 0.06 | `cross_autocorr(cross_zscore(log(day_var(Low)), 60), 120, 1)` |
| slot a seed 7 | 过 | 0.26 | `ts_sum(day_var(Amt), 50)` | 0.20 | 0.22 | 0.21 | 0.01 | 0.23 | 0.06 | `cross_corr(log(day_var(Low)), log(day_var(Amt)), 120)` |
| slot a seed 8 | 过 | 0.29 | `ts_sum(day_var(Amt), 50)` | 0.25 | 0.23 | 0.26 | 0.01 | 0.24 | 0.12 | `cross_corr(cross_delay(log(day_var(Low)), 1), log(day_var(Amt)), 120)` |
| slot a seed 9 | 过 | 0.25 | `ts_sum(day_var(Amt), 50)` | 0.21 | 0.18 | 0.03 | 0.00 | 0.19 | 0.14 | `cross_corr(log(day_var(Low)), log(day_var(Ret)), 120)` |
| slot a seed 10 | 过 | 0.14 | `ts_sum(day_var(Amt), 50)` | 0.06 | 0.14 | 0.03 | 0.04 | 0.15 | 0.31 | `cross_regbeta(log(day_var(Ret)), log(day_var(Low)), 241)` |
| slot a seed 11 | 过 | 0.46 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.48 | 0.04 | 0.10 | 0.01 | 0.04 | 0.09 | `cross_corr(ts_max(day_last(Amt), 20), day_var(Low), 241)` |
| slot a seed 12 | 过 | 0.73 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.64 | 0.40 | 0.07 | 0.03 | 0.40 | 0.21 | `div(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 241), cross_stddev(day_var(Low), 241))` |
| slot a seed 13 | 过 | 0.32 | `ts_sum(day_var(Amt), 50)` | 0.28 | 0.34 | 0.57 | 0.28 | 0.36 | 0.08 | `sub(cross_mean(log(day_var(Low)), 20), cross_mean(log(day_var(Low)), 241))` |
| slot a seed 14 | 过 | 0.02 | `ts_sum(day_var(Amt), 50)` | 0.03 | 0.03 | 0.07 | 0.00 | 0.03 | 0.11 | `cs_last_high05(cross_corr(cross_delay(cross_zscore(log(day_var(Low)), 60), 1), day_sum(Ret), 120), day_var(Low))` |
| slot a seed 15 | 过 | 0.14 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.13 | 0.11 | 0.05 | 0.01 | 0.10 | 0.07 | `cross_regbeta(cross_delay(day_var(Low), 1), day_sum(Ret), 120)` |
| slot b seed 1 | 过 | 0.03 | `ts_sum(day_var(Amt), 50)` | 0.01 | 0.04 | 0.01 | 0.00 | 0.03 | 0.01 | `cross_regbeta(cross_delay(cross_zscore(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 60), 1), day_sum(Ret), 120)` |
| slot b seed 2 | 过 | 0.04 | `ts_sum(day_var(Amt), 50)` | 0.01 | 0.04 | 0.02 | 0.00 | 0.04 | 0.01 | `cross_corr(cross_delay(cross_zscore(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 60), 1), day_sum(Ret), 120)` |
| slot b seed 3 | 过 | 0.04 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.02 | 0.04 | 0.01 | 0.01 | 0.03 | 0.02 | `cross_reg_tvalue(cross_delay(cross_zscore(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 60), 1), cs_demean(day_sum(Ret)), 120)` |
| slot b seed 4 | 过 | 0.04 | `ts_sum(day_var(Amt), 50)` | 0.01 | 0.05 | 0.01 | 0.01 | 0.05 | 0.02 | `cross_corr(cross_delay(cross_zscore(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 60), 1), day_sum(Ret), 241)` |
| slot b seed 5 | 过 | 0.15 | `ts_sum(day_var(Amt), 50)` | 0.06 | 0.14 | 0.15 | 0.02 | 0.14 | 0.04 | `cross_regbeta(cross_delay(cross_zscore(log(day_var(Amt)), 60), 1), day_sum(Ret), 120)` |
| slot b seed 6 | 过 | 0.00 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.02 | 0.01 | 0.00 | 0.00 | 0.00 | 0.02 | `cross_regbeta(cross_delay(mul(cross_zscore(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 60), sign(day_sum(Ret))), 1), day_sum(Ret), 120)` |
| slot b seed 7 | 过 | 0.13 | `ts_sum(day_var(Amt), 50)` | 0.05 | 0.12 | 0.16 | 0.02 | 0.12 | 0.02 | `cross_regbeta(cross_delay(cross_zscore(log(day_var(Ret)), 60), 1), day_sum(Ret), 120)` |
| slot b seed 8 | 过 | 0.15 | `ts_sum(day_var(Amt), 50)` | 0.05 | 0.14 | 0.17 | 0.04 | 0.14 | 0.02 | `cross_corr(cross_delay(cross_zscore(log(day_var(Ret)), 60), 1), cs_demean(day_sum(Ret)), 120)` |
| slot b seed 9 | 过 | 0.17 | `ts_sum(day_var(Amt), 50)` | 0.21 | 0.09 | 0.02 | 0.00 | 0.11 | 0.20 | `cross_corr(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), log(day_var(Ret)), 120)` |
| slot b seed 10 | 过 | 0.14 | `ts_sum(day_var(Amt), 50)` | 0.18 | 0.06 | 0.00 | 0.01 | 0.09 | 0.18 | `cross_regbeta(log(day_var(Ret)), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 241)` |
| slot b seed 11 | 过 | 0.18 | `ts_sum(day_var(Amt), 50)` | 0.18 | 0.11 | 0.06 | 0.01 | 0.13 | 0.16 | `cross_corr(cross_delay(log(day_var(Ret)), 1), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 120)` |
| slot b seed 12 | 过 | 0.23 | `ts_sum(day_var(Amt), 50)` | 0.28 | 0.13 | 0.14 | 0.01 | 0.16 | 0.15 | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), log(day_var(Ret)), 120)` |
| slot b seed 13 | 过 | 0.14 | `ts_sum(day_var(Amt), 50)` | 0.19 | 0.06 | 0.16 | 0.02 | 0.09 | 0.05 | `cross_autocorr(cross_zscore(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 60), 120, 1)` |
| slot b seed 14 | 过 | 0.24 | `ts_sum(day_var(Amt), 50)` | 0.20 | 0.27 | 0.18 | 0.07 | 0.23 | 0.06 | `sub(cross_mean(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 20), cross_mean(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 241))` |
| slot b seed 15 | 过 | 0.53 | `ts_sum(day_var(Amt), 50)` | 0.23 | 0.65 | 0.20 | 0.07 | 0.56 | 0.58 | `cross_mean(log(div(day_var(Amt), pow_2(day_mean(Amt)))), 241)` |
| slot b seed 16 | 过 | 0.26 | `ts_sum(day_var(Amt), 50)` | 0.11 | 0.25 | 0.11 | 0.01 | 0.25 | 0.14 | `cross_regbeta(cross_delay(day_var(Amt), 1), day_sum(Ret), 120)` |
| R 1 variant 1 | 过 | 0.42 | `ts_sum(day_var(Amt), 50)` | 0.20 | 0.56 | 0.17 | 0.08 | 0.46 | 0.45 | `ts_sum(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))), 100)` |
| R 1 variant 2 | 过 | 0.36 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.19 | 0.48 | 0.17 | 0.07 | 0.40 | 0.34 | `ts_sum(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))), 241)` |
| R 1 variant 3 | 过 | 0.36 | `ts_sum(day_var(Amt), 50)` | 0.39 | 0.41 | 0.53 | 0.33 | 0.45 | 0.16 | `div(ts_sum(day_var(Amt), 241), ts_sum(day_var(Amt), 20))` |
| R 1 variant 4 | 过 | 0.26 | `ts_sum(day_var(Amt), 50)` | 0.49 | 0.08 | 0.32 | 0.06 | 0.16 | 0.22 | `cs_regres(log(ts_sum(day_var(Amt), 100)), log(ts_sum(day_mean(Amt), 100)))` |
| R 1 variant 5 | 过 | 0.80 | `ts_sum(day_var(Amt), 50)` | 0.39 | 0.79 | 0.10 | 0.05 | 0.79 | 0.58 | `ts_sum(day_var(Amt), 241)` |
| R 1 variant 6 | 过 | 0.30 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.37 | 0.36 | 0.22 | 0.08 | 0.28 | 0.54 | `div(ts_sum(day_var(Amt), 100), pow_2(ts_sum(day_mean(Amt), 100)))` |
| R 2 variant 1 | 过 | 0.47 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.47 | 0.06 | 0.14 | 0.02 | 0.07 | 0.09 | `ts_max(cross_corr(ts_max(day_last(Amt), 20), day_var(Low), 241), 20)` |
| R 2 variant 2 | 过 | 0.28 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.24 | 0.08 | 0.17 | 0.06 | 0.09 | 0.08 | `ts_max(cross_corr(ts_max(day_last(Amt), 20), day_var(Low), 120), 20)` |
| R 2 variant 3 | 过 | 0.13 | `ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(L` | 0.19 | 0.13 | 0.02 | 0.05 | 0.10 | 0.14 | `ts_max(cross_regbeta(day_var(Low), ts_max(day_last(Amt), 20), 241), 20)` |
| R 2 variant 4 | 过 | 0.47 | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 24` | 0.48 | 0.06 | 0.14 | 0.01 | 0.07 | 0.14 | `ts_max(cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241), 20)` |
| R 3 variant 1 | 过 | 0.64 | `ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(L` | 0.70 | 0.04 | 0.11 | 0.18 | 0.06 | 0.02 | `ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 2)` |
| R 3 variant 2 | 过 | 0.19 | `ts_sum(day_var(Amt), 50)` | 0.22 | 0.15 | 0.22 | 0.11 | 0.17 | 0.00 | `ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 60), 5)` |
| R 3 variant 3 | 过 | 0.54 | `ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(L` | 0.47 | 0.05 | 0.12 | 0.15 | 0.06 | 0.01 | `ts_min(ts_reg_tvalue(day_std(High), ts_std(pow_2_5(day_var(Low)), 20), 20), 5)` |
| R 3 variant 4 | 过 | 0.43 | `ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(L` | 0.55 | 0.10 | 0.25 | 0.23 | 0.13 | 0.05 | `ts_mean(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 20)` |
