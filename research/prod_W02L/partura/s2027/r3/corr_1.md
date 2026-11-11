# 相关度表:种子 2027,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.03 | `day_mean(Volume)` | 0.05 | 0.01 | 0.00 | 0.00 | 0.01 | 0.03 | `ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30)` |
| slot a seed 1 | 过 | 0.12 | `day_mean(Volume)` | 0.09 | 0.08 | 0.00 | 0.01 | 0.08 | 0.13 | `cross_ema(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 20)` |
| slot a seed 2 | 过 | 0.06 | `day_mean(Volume)` | 0.03 | 0.05 | 0.02 | 0.01 | 0.05 | 0.06 | `cross_ema(cross_zscore(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 60), 20)` |
| slot a seed 3 | 过 | 0.10 | `day_mean(Volume)` | 0.07 | 0.06 | 0.01 | 0.00 | 0.06 | 0.11 | `ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 80)` |
| slot a seed 4 | 过 | 0.06 | `day_mean(Volume)` | 0.05 | 0.03 | 0.01 | 0.01 | 0.03 | 0.07 | `ts_decay_linear(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 40)` |
| slot a seed 5 | 废品 | 0.02 | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240)` | 0.02 | 0.01 | 0.02 | 0.01 | 0.01 | 0.00 | `sub(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 60))` |
| slot a seed 6 | 废品 | 0.03 | `ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(Hi` | 0.05 | 0.00 | 0.00 | 0.01 | 0.00 | 0.02 | `div(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), add(ts_stddev(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 60), 0.000001))` |
| slot a seed 7 | 过 | 0.49 | `day_mean(Volume)` | 0.58 | 0.03 | 0.15 | 0.06 | 0.06 | 0.53 | `cs_bucket_rank(LogFloatShares, ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 20))` |
| slot a seed 8 | 过 | 0.22 | `day_mean(Volume)` | 0.16 | 0.06 | 0.09 | 0.04 | 0.02 | 0.16 | `cs_bucket_rank(BoardCode, ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 40))` |
| slot a seed 9 | 过 | 0.05 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` | 0.04 | 0.00 | 0.12 | 0.05 | 0.01 | 0.07 | `cs_regres(ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 40), day_std(in_slice(Ret, 11, 230)))` |
| slot a seed 10 | 过 | 0.02 | `day_mean(Volume)` | 0.02 | 0.01 | 0.01 | 0.00 | 0.01 | 0.01 | `cross_regbeta(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), day_mean(in_slice(Ret, 11, 230)), 120)` |
| slot a seed 11 | 过 | 0.02 | `day_mean(Volume)` | 0.02 | 0.02 | 0.01 | 0.00 | 0.02 | 0.03 | `cross_corr(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), day_std(in_slice(Ret, 11, 230)), 120)` |
| slot a seed 12 | 过 | 0.02 | `ts_sum(cross_cov(ts_sum(cross_cov(day_mean(Vwap), day_max(Hi` | 0.02 | 0.00 | 0.02 | 0.00 | 0.00 | 0.01 | `sub(ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 20), ts_mean(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 120))` |
| slot a seed 13 | 过 | 0.06 | `day_mean(Volume)` | 0.06 | 0.03 | 0.01 | 0.01 | 0.03 | 0.06 | `ts_mean(signedpower(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 0.5), 40)` |
| slot a seed 14 | 过 | 0.17 | `day_mean(Volume)` | 0.06 | 0.17 | 0.03 | 0.00 | 0.17 | 0.30 | `cross_ema(cs_regres(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), LogFloatCap), 20)` |
| slot a seed 15 | 过 | 0.06 | `day_mean(Volume)` | 0.05 | 0.04 | 0.01 | 0.01 | 0.04 | 0.07 | `ts_mean(mul(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), day_flat_ratio(Open)), 40)` |
| slot a seed 16 | 过 | 0.48 | `day_mean(Volume)` | 0.34 | 0.44 | 0.02 | 0.03 | 0.44 | 0.52 | `cross_ema(ts_stddev(ts_cov(inv(day_quantile_q25(Volume)), cross_reg_fvalue(ListAge, day_flat_run_max(Open), 60), 30), 30), 20)` |
| slot b seed 1 | 过 | 0.10 | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240)` | 0.07 | 0.10 | 0.17 | 0.06 | 0.09 | 0.02 | `cross_reg_tvalue(ListAge, day_flat_run_max(Close), 60)` |
| slot b seed 2 | 废品 | 0.21 | `day_mean(Volume)` | 0.04 | 0.24 | 0.34 | 0.24 | 0.26 | 0.08 | `cross_reg_tvalue(ListAge, inv(day_quantile_q25(Volume)), 60)` |
| slot b seed 3 | 过 | 0.09 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` | 0.07 | 0.01 | 0.01 | 0.07 | 0.02 | 0.02 | `cross_regbeta(ListAge, day_flat_run_max(Open), 120)` |
| slot b seed 4 | 过 | 0.10 | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240)` | 0.07 | 0.14 | 0.01 | 0.02 | 0.12 | 0.06 | `cross_reg_fvalue(ListAge, day_std(in_slice(Ret, 11, 230)), 60)` |
| slot b seed 5 | 过 | 0.13 | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240)` | 0.09 | 0.19 | 0.02 | 0.01 | 0.18 | 0.19 | `cross_reg_fvalue(ListAge, day_gini(in_slice(Volume, 11, 230)), 60)` |
| slot b seed 6 | 过 | 0.16 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` | 0.07 | 0.20 | 0.34 | 0.07 | 0.22 | 0.04 | `ts_mean(cross_reg_tvalue(ListAge, day_flat_ratio(Open), 60), 20)` |
| slot b seed 7 | 过 | 0.10 | `ts_mean(div(day_std(in_topk_masked(in_slice(Volume, 11, 240)` | 0.07 | 0.10 | 0.17 | 0.06 | 0.09 | 0.03 | `cross_corr(ListAge, day_flat_run_max(Open), 60)` |
| slot b seed 8 | 过 | 0.04 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` | 0.08 | 0.01 | 0.02 | 0.06 | 0.01 | 0.02 | `sub(cross_reg_tvalue(ListAge, day_flat_run_max(Open), 60), cross_reg_tvalue(ListAge, day_flat_run_max(Open), 250))` |
| slot b seed 9 | 废品 | 0.13 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` | 0.14 | 0.02 | 0.09 | 0.01 | 0.01 | 0.18 | `cross_reg_tvalue(day_flat_run_max(Open), inv(day_quantile_q25(Volume)), 60)` |
| slot b seed 10 | 过 | 0.11 | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 45)` | 0.14 | 0.20 | 0.16 | 0.01 | 0.20 | 0.12 | `cross_reg_fvalue(day_flat_run_max(Open), day_std(in_slice(Ret, 11, 230)), 60)` |
| slot b seed 11 | 废品 | 0.28 | `day_mean(Volume)` | 0.21 | 0.33 | 0.26 | 0.05 | 0.33 | 0.17 | `cross_regbeta(ListAge, inv(day_quantile_q25(Volume)), 120)` |
| slot b seed 12 | 过 | 0.19 | `day_mean(Volume)` | 0.11 | 0.29 | 0.29 | 0.01 | 0.30 | 0.09 | `cross_ema(cross_reg_tvalue(ListAge, day_flat_run_max(Amt), 60), 20)` |
