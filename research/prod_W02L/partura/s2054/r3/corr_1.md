# 相关度表:种子 2054,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.41 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.82 | 0.19 | 0.08 | 0.03 | 0.16 | 0.00 | `day_at_max_ratio(High)` |
| slot a seed 1 | 废品 | 0.52 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.71 | 0.18 | 0.07 | 0.23 | 0.11 | 0.01 | `cross_mean(day_at_max_ratio(High), 20)` |
| slot a seed 2 | 废品 | 0.27 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.36 | 0.16 | 0.35 | 0.15 | 0.08 | 0.23 | `cs_bucket_zscore(cross_mean(day_at_max_ratio(High), 30), LimitWidth)` |
| slot a seed 3 | 过 | 0.26 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.35 | 0.15 | 0.34 | 0.12 | 0.08 | 0.26 | `cross_mean(cs_bucket_zscore(day_at_max_ratio(High), BoardCode), 40)` |
| slot a seed 4 | 过 | 0.06 | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_` | 0.03 | 0.07 | 0.10 | 0.01 | 0.09 | 0.00 | `cross_corr(day_at_max_ratio(High), cross_delay(day_sum(Ret), 1), 60)` |
| slot a seed 5 | 过 | 0.02 | `sigmoid(day_durbin_watson(nt_ts_autocorr_s1(Ret, 3)))` | 0.01 | 0.02 | 0.06 | 0.01 | 0.04 | 0.05 | `cross_regbeta(day_sum(Ret), cross_delay(day_at_max_ratio(High), 1), 60)` |
| slot a seed 6 | 过 | 0.52 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.65 | 0.12 | 0.15 | 0.12 | 0.04 | 0.02 | `cross_tail_mean_q75(day_at_max_ratio(High), 60)` |
| slot a seed 7 | 废品 | 0.07 | `ts_quantile_q75(day_q_stat_std(nt_ts_autocorr_s1(nt_ts_autoc` | 0.21 | 0.12 | 0.20 | 0.03 | 0.14 | 0.01 | `sub(cross_mean(day_at_max_ratio(High), 5), cross_mean(day_at_max_ratio(High), 60))` |
| slot a seed 8 | 过 | 0.47 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.55 | 0.16 | 0.18 | 0.12 | 0.10 | 0.07 | `cross_mean(cs_regres(day_at_max_ratio(High), day_std(Ret)), 30)` |
| slot a seed 9 | 过 | 0.23 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.18 | 0.26 | 0.22 | 0.07 | 0.27 | 0.07 | `cross_corr(day_at_max_ratio(High), day_sum(Amt), 60)` |
| slot a seed 10 | 废品 | 0.19 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.15 | 0.17 | 0.30 | 0.23 | 0.20 | 0.04 | `sub(cross_mean(day_at_max_ratio(High), 30), cross_mean(day_at_min_ratio(Low), 30))` |
| slot a seed 11 | 过 | 0.32 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.45 | 0.04 | 0.26 | 0.12 | 0.11 | 0.00 | `cross_stddev(day_at_max_ratio(High), 60)` |
| slot a seed 12 | 过 | 0.36 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.52 | 0.00 | 0.23 | 0.11 | 0.08 | 0.05 | `cs_bucket_zscore(cross_ema(day_at_max_ratio(High), 20), LogFloatCap)` |
| slot b core | 过 | 0.10 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.11 | 0.08 | 0.03 | 0.06 | 0.06 | 0.04 | `day_q_stat_std(High)` |
| slot b seed 1 | 过 | 0.25 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.16 | 0.26 | 0.13 | 0.10 | 0.20 | 0.21 | `cross_mean(day_q_stat_std(High), 30)` |
| slot b seed 2 | 过 | 0.29 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.19 | 0.31 | 0.14 | 0.10 | 0.25 | 0.26 | `cross_ema(day_q_stat_std(High), 20)` |
| slot b seed 3 | 过 | 0.24 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.17 | 0.13 | 0.12 | 0.09 | 0.07 | 0.00 | `cs_bucket_zscore(cross_mean(day_q_stat_std(High), 40), LogFloatCap)` |
| slot b seed 4 | 过 | 0.11 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.11 | 0.09 | 0.00 | 0.04 | 0.07 | 0.04 | `cs_regres(day_q_stat_std(High), day_std(Ret))` |
| slot b seed 5 | 过 | 0.08 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.09 | 0.08 | 0.10 | 0.07 | 0.10 | 0.17 | `cross_corr(day_q_stat_std(High), day_sum(Amt), 60)` |
| slot b seed 6 | 过 | 0.05 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.14 | 0.01 | 0.02 | 0.07 | 0.01 | 0.01 | `sub(day_q_stat_std(High), day_q_stat_std(Low))` |
| slot b seed 7 | 过 | 0.48 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.58 | 0.02 | 0.07 | 0.10 | 0.00 | 0.26 | `cross_mean(sub(day_q_stat_std(High), day_q_stat_std(Close)), 30)` |
| slot b seed 8 | 过 | 0.03 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.03 | 0.02 | 0.04 | 0.01 | 0.02 | 0.01 | `cross_regbeta(day_mean(Ret), cross_delay(day_q_stat_std(High), 1), 60)` |
| slot b seed 9 | 过 | 0.14 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.08 | 0.16 | 0.06 | 0.04 | 0.12 | 0.12 | `cross_stddev(day_q_stat_std(High), 40)` |
| slot b seed 10 | 过 | 0.02 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.06 | 0.03 | 0.01 | 0.11 | 0.02 | 0.01 | `sub(cross_mean(day_q_stat_std(High), 10), cross_mean(day_q_stat_std(High), 60))` |
| slot b seed 11 | 过 | 0.20 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.14 | 0.19 | 0.12 | 0.06 | 0.14 | 0.17 | `cross_tail_mean_q75(day_q_stat_std(High), 40)` |
| slot b seed 12 | 过 | 0.28 | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3` | 0.17 | 0.32 | 0.02 | 0.08 | 0.26 | 0.19 | `cs_regres(cross_mean(day_q_stat_std(High), 30), cross_mean(day_std(Ret), 30))` |
