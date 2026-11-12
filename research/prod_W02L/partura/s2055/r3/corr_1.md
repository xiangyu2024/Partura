# 相关度表:种子 2055,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.02 | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)` | 0.06 | 0.05 | 0.01 | 0.14 | 0.05 | 0.06 | `day_wmean(Ret, in_pct(Amt, 1))` |
| slot a seed 1 | 过 | 0.16 | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` | 0.11 | 0.35 | 0.20 | 0.08 | 0.35 | 0.19 | `ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 120)` |
| slot a seed 2 | 过 | 0.16 | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` | 0.10 | 0.36 | 0.25 | 0.19 | 0.37 | 0.19 | `cross_ema(day_wmean(Ret, in_pct(Amt, 1)), 40)` |
| slot a seed 3 | 过 | 0.03 | `ts_std(ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10` | 0.03 | 0.02 | 0.03 | 0.32 | 0.01 | 0.00 | `sub(ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 10), ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 120))` |
| slot a seed 4 | 过 | 0.15 | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` | 0.10 | 0.34 | 0.25 | 0.17 | 0.35 | 0.18 | `div(ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 60), ts_std(day_wmean(Ret, in_pct(Amt, 1)), 60))` |
| slot a seed 5 | 过 | 0.04 | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` | 0.11 | 0.21 | 0.05 | 0.22 | 0.21 | 0.15 | `cs_bucket_rank(ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 40), ts_mean(day_std(Ret), 40))` |
| slot a seed 6 | 过 | 0.13 | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))),` | 0.10 | 0.20 | 0.26 | 0.23 | 0.22 | 0.00 | `cs_bucket_rank(ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 40), LogFloatCap)` |
| slot a seed 7 | 过 | 0.02 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.03 | 0.01 | 0.01 | 0.04 | 0.00 | 0.00 | `cs_flip_by_state(ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 20), day_sum(Amt))` |
| slot a seed 8 | 过 | 0.13 | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` | 0.10 | 0.30 | 0.21 | 0.13 | 0.30 | 0.15 | `ts_mean(sub(day_wmean(Ret, in_pct(Amt, 1)), day_mean(Ret)), 60)` |
| slot a seed 9 | 过 | 0.31 | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))),` | 0.10 | 0.08 | 0.31 | 0.08 | 0.03 | 0.29 | `ts_mean(sub(day_wmean(Ret, in_pct(Amt, 1)), day_wmean(Ret, Amt)), 60)` |
| slot a seed 10 | 过 | 0.33 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.12 | 0.53 | 0.03 | 0.03 | 0.49 | 0.31 | `ts_corr(day_wmean(Ret, in_pct(Amt, 1)), day_sum(Ret), 60)` |
| slot a seed 11 | 过 | 0.28 | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))), 10` | 0.15 | 0.32 | 0.44 | 0.04 | 0.27 | 0.33 | `cross_tail_mean_q25(day_wmean(Ret, in_pct(Amt, 1)), 60)` |
| slot a seed 12 | 过 | 0.20 | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(Ret, 3))),` | 0.13 | 0.22 | 0.45 | 0.08 | 0.24 | 0.05 | `ts_quantile_q75(ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 5), 100)` |
| slot b seed 1 | 过 | 0.12 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` | 0.11 | 0.01 | 0.17 | 0.27 | 0.02 | 0.03 | `ts_mean(day_corr(in_index(Close), Close), 60)` |
| slot b seed 2 | 过 | 0.44 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.09 | 0.72 | 0.28 | 0.03 | 0.70 | 0.29 | `ts_mean(day_corr(in_index(Amt), Amt), 60)` |
| slot b seed 3 | 过 | 0.12 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` | 0.10 | 0.08 | 0.25 | 0.30 | 0.10 | 0.00 | `ts_mean(day_wmean(Ret, in_index(Ret)), 40)` |
| slot b seed 4 | 过 | 0.22 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.09 | 0.39 | 0.34 | 0.23 | 0.40 | 0.08 | `cross_ema(sub(day_wmean(Ret, in_index(Ret)), day_mean(Ret)), 40)` |
| slot b seed 5 | 过 | 0.12 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` | 0.10 | 0.01 | 0.18 | 0.27 | 0.03 | 0.03 | `ts_mean(day_corr(in_index(Vwap), Vwap), 60)` |
| slot b seed 6 | 过 | 0.26 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.34 | 0.09 | 0.04 | 0.03 | 0.11 | 0.12 | `ts_mean(day_wmean(in_index(Amt), in_pct(Amt, 1)), 60)` |
| slot b seed 7 | 过 | 0.12 | `ts_std(ts_std(ts_sum(day_var(pow_2_5(nt_ts_var(Low, 3))), 10` | 0.07 | 0.22 | 0.01 | 0.11 | 0.21 | 0.02 | `ts_mean(mul(day_corr(in_index(Close), Close), day_corr(in_index(Amt), Amt)), 60)` |
| slot b seed 8 | 过 | 0.12 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` | 0.10 | 0.02 | 0.15 | 0.42 | 0.01 | 0.03 | `cross_ema(day_corr(in_index(Close), Close), 20)` |
| slot b seed 9 | 过 | 0.11 | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` | 0.11 | 0.30 | 0.22 | 0.18 | 0.30 | 0.22 | `ts_mean(day_corr(Ret, in_pct(Amt, 1)), 60)` |
| slot b seed 10 | 过 | 0.34 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.07 | 0.62 | 0.27 | 0.03 | 0.61 | 0.23 | `ts_quantile_q75(day_corr(in_index(Volume), Volume), 60)` |
| slot b seed 11 | 过 | 0.44 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.09 | 0.72 | 0.28 | 0.03 | 0.70 | 0.29 | `ts_mean(day_corr(in_index(Close), Amt), 60)` |
