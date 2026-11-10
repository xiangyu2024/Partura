# 相关度表:种子 2014,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.13 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.07 | 0.01 | 0.16 | 0.03 | 0.01 | 0.14 | `cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241)` |
| slot a seed 1 | 过 | 0.03 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.01 | 0.03 | 0.02 | 0.03 | 0.03 | 0.05 | `cs_flip_by_state(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), day_sum(Amt))` |
| slot a seed 2 | 过 | 0.03 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.02 | 0.01 | 0.01 | 0.00 | 0.01 | 0.03 | `cs_flip_by_state(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), day_std(Ret))` |
| slot a seed 3 | 过 | 0.03 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.03 | 0.01 | 0.04 | 0.01 | 0.01 | 0.03 | `cross_zscore(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), 120)` |
| slot a seed 4 | 过 | 0.07 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.04 | 0.02 | 0.06 | 0.01 | 0.02 | 0.07 | `sub(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), cross_ema(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), 120))` |
| slot a seed 5 | 过 | 0.08 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.06 | 0.07 | 0.06 | 0.00 | 0.07 | 0.17 | `cs_regres(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), ListAge)` |
| slot a seed 6 | 过 | 0.06 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.07 | 0.09 | 0.08 | 0.01 | 0.09 | 0.14 | `cs_bucket_zscore(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), ListAge)` |
| slot a seed 7 | 过 | 0.04 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.05 | 0.03 | 0.09 | 0.01 | 0.03 | 0.08 | `cs_regres(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), sub(LogTotalCap, LogFloatCap))` |
| slot a seed 8 | 过 | 0.06 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.08 | 0.09 | 0.07 | 0.01 | 0.09 | 0.14 | `cross_ema(cs_bucket_zscore(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), ListAge), 20)` |
| slot a seed 9 | 过 | 0.09 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.05 | 0.01 | 0.12 | 0.03 | 0.01 | 0.10 | `add(cs_rank(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241)), cs_rank(cross_zscore(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), 60)))` |
| slot a seed 10 | 过 | 0.01 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.02 | 0.01 | 0.00 | 0.01 | 0.01 | 0.02 | `cs_flip_by_state(cs_bucket_zscore(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), ListAge), day_sum(Amt))` |
| slot a seed 11 | 过 | 0.06 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.03 | 0.00 | 0.05 | 0.01 | 0.00 | 0.06 | `cross_ema(cs_flip_by_state(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), day_std(Ret)), 20)` |
| slot a seed 12 | 过 | 0.11 | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | 0.10 | 0.11 | 0.20 | 0.03 | 0.12 | 0.04 | `sub(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), cross_sum(cross_delta(sub(LogTotalCap, LogFloatCap), 1), 241))` |
| slot a seed 13 | 过 | 0.12 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.09 | 0.10 | 0.09 | 0.03 | 0.12 | 0.09 | `cs_bucket_zscore(cross_ema(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), 20), cross_mean(day_std(Ret), 60))` |
| slot b core | 过 | 0.31 | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | 0.30 | 0.30 | 0.45 | 0.21 | 0.30 | 0.01 | `day_gini(Low)` |
| slot b seed 1 | 过 | 0.10 | `ts_std(day_quantile_q25(Ret), 5)` | 0.18 | 0.01 | 0.07 | 0.26 | 0.00 | 0.01 | `cross_zscore(day_gini(Low), 60)` |
| slot b seed 2 | 过 | 0.47 | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | 0.32 | 0.52 | 0.69 | 0.05 | 0.52 | 0.01 | `cross_ema(day_gini(Low), 20)` |
| slot b seed 3 | 过 | 0.08 | `ts_decay_linear(day_std(sub(nt_ts_stddev(nt_ts_quantile_q50(` | 0.15 | 0.08 | 0.11 | 0.02 | 0.08 | 0.03 | `sub(day_gini(Low), day_gini(High))` |
| slot b seed 4 | 过 | 0.14 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.17 | 0.11 | 0.07 | 0.01 | 0.15 | 0.03 | `cross_semistd_neg(day_gini(Low), 241)` |
| slot b seed 5 | 过 | 0.14 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.07 | 0.08 | 0.06 | 0.05 | 0.06 | 0.06 | `sub(cross_semistd_pos(day_gini(Low), 241), cross_semistd_neg(day_gini(Low), 241))` |
| slot b seed 6 | 过 | 0.31 | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | 0.29 | 0.29 | 0.45 | 0.21 | 0.29 | 0.01 | `cs_bucket_zscore(day_gini(Low), LogFloatCap)` |
| slot b seed 7 | 过 | 0.04 | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(` | 0.07 | 0.03 | 0.02 | 0.02 | 0.02 | 0.02 | `cs_flip_by_state(cross_ema(day_gini(Low), 60), day_std(Ret))` |
| slot b seed 8 | 过 | 0.26 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.09 | 0.26 | 0.32 | 0.18 | 0.27 | 0.07 | `cross_corr(day_gini(Low), day_sum(Ret), 60)` |
| slot b seed 9 | 过 | 0.12 | `ts_std(day_quantile_q25(Ret), 5)` | 0.18 | 0.06 | 0.17 | 0.28 | 0.07 | 0.00 | `cross_madz(day_gini(Low), 120)` |
| slot b seed 10 | 过 | 0.28 | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25` | 0.52 | 0.24 | 0.49 | 0.31 | 0.27 | 0.05 | `sub(cross_ema(day_gini(Low), 10), cross_ema(day_gini(Low), 120))` |
| slot b seed 11 | 过 | 0.53 | `ts_med(ts_cov(day_quantile(pow_3(Open)), day_close(High), 50` | 0.34 | 0.47 | 0.10 | 0.04 | 0.41 | 0.19 | `cs_regres(cross_mean(day_gini(Low), 60), cross_mean(day_std(Ret), 60))` |
| slot b seed 12 | 过 | 0.14 | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), ` | 0.16 | 0.13 | 0.23 | 0.14 | 0.15 | 0.13 | `cross_ema(sub(day_gini(Low), day_gini(Close)), 30)` |
| slot b seed 13 | 过 | 0.26 | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | 0.28 | 0.04 | 0.60 | 0.04 | 0.04 | 0.37 | `cs_bucket_zscore(cross_ema(day_gini(Low), 30), cross_mean(day_sum(Amt), 60))` |
