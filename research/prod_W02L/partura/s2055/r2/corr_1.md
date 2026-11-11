# 相关度表:种子 2055,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 废品 | 0.10 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.04 | 0.17 | 0.13 | 0.12 | 0.18 | 0.05 | `day_argmax(Amt)` |
| slot a seed 1 | 过 | 0.05 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` | 0.10 | 0.07 | 0.22 | 0.30 | 0.10 | 0.06 | `ts_mean(day_locate(Ret, day_argmax(Amt)), 20)` |
| slot a seed 2 | 过 | 0.19 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.11 | 0.25 | 0.28 | 0.08 | 0.26 | 0.06 | `ts_mean(div(day_locate(Vwap, day_argmax(Amt)), day_last(Close)), 20)` |
| slot a seed 3 | 废品 | 0.34 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.09 | 0.48 | 0.31 | 0.29 | 0.48 | 0.14 | `ts_mean(sub(day_argmax(Amt), day_argmax(High)), 20)` |
| slot a seed 4 | 过 | 0.39 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.10 | 0.52 | 0.31 | 0.19 | 0.51 | 0.12 | `cross_mean(sub(day_argmax(Amt), day_argmax(Low)), 30)` |
| slot a seed 5 | 过 | 0.16 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.04 | 0.27 | 0.22 | 0.06 | 0.27 | 0.13 | `ts_std(day_argmax(Amt), 20)` |
| slot a seed 6 | 过 | 0.04 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.04 | 0.05 | 0.03 | 0.05 | 0.05 | 0.01 | `cross_zscore(day_argmax(Amt), 20)` |
| slot a seed 7 | 过 | 0.38 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.41 | 0.06 | 0.13 | 0.13 | 0.11 | 0.07 | `ts_mean(div(sub(day_locate(High, day_argmax(Amt)), day_locate(Low, day_argmax(Amt))), sub(day_max(High), day_min(Low))), 20)` |
| slot a seed 8 | 过 | 0.10 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` | 0.09 | 0.14 | 0.14 | 0.18 | 0.15 | 0.02 | `ts_corr(day_argmax(Amt), day_argmax(High), 20)` |
| slot a seed 9 | 过 | 0.10 | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)` | 0.14 | 0.12 | 0.22 | 0.50 | 0.14 | 0.10 | `ts_mean(mul(day_argmax(Amt), day_signed_ratio(Ret, Amt)), 20)` |
| slot a seed 10 | 过 | 0.37 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.09 | 0.51 | 0.29 | 0.25 | 0.50 | 0.14 | `cross_ema(sub(day_argmax(Amt), day_argmax(Close)), 10)` |
| slot b seed 1 | 过 | 0.14 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` | 0.16 | 0.11 | 0.41 | 0.55 | 0.16 | 0.09 | `ts_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 20)` |
| slot b seed 2 | 过 | 0.16 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.20 | 0.00 | 0.17 | 0.61 | 0.02 | 0.14 | `ts_mean(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 3 | 过 | 0.18 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.18 | 0.24 | 0.41 | 0.64 | 0.26 | 0.05 | `ts_mean(day_topw_mean(Ret, Amt), 20)` |
| slot b seed 4 | 过 | 0.45 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.57 | 0.07 | 0.27 | 0.12 | 0.12 | 0.07 | `ts_mean(sub(day_centroid(Amt), day_centroid(Ret)), 20)` |
| slot b seed 5 | 过 | 0.25 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.20 | 0.33 | 0.48 | 0.45 | 0.35 | 0.05 | `cross_mean(day_topw_mean(Ret, Volume), 30)` |
| slot b seed 6 | 过 | 0.07 | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` | 0.09 | 0.19 | 0.20 | 0.41 | 0.20 | 0.10 | `ts_mean(day_wmean(Ret, in_pct(Amt, 1)), 20)` |
| slot b seed 7 | 过 | 0.09 | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` | 0.15 | 0.14 | 0.08 | 0.51 | 0.13 | 0.03 | `ts_quantile_q75(day_signed_ratio(Ret, Amt), 20)` |
| slot b seed 8 | 过 | 0.28 | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))),` | 0.13 | 0.23 | 0.12 | 0.29 | 0.19 | 0.18 | `ts_mean(sub(day_topw_mean(Ret, Amt), day_wmean(Ret, Amt)), 20)` |
| slot b seed 9 | 过 | 0.20 | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)` | 0.11 | 0.14 | 0.36 | 0.54 | 0.16 | 0.14 | `cross_ema(day_signed_ratio(in_pct(Vwap, 1), Volume), 10)` |
| slot b seed 10 | 过 | 0.14 | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)` | 0.19 | 0.11 | 0.10 | 0.28 | 0.11 | 0.24 | `ts_mean(day_signed_ratio(Ret, in_pct(Amt, 1)), 30)` |
