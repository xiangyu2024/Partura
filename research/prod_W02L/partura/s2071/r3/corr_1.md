# 相关度表:种子 2071,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 9 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.21 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.18 | 0.04 | 0.00 | 0.03 | 0.00 | 0.11 | `cross_max(abs_(day_corr(Volume, Ret)), 241)` |
| slot a seed 1 | 过 | 0.21 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.18 | 0.10 | 0.02 | 0.03 | 0.13 | 0.06 | `cs_bucket_demean(cross_max(abs_(day_corr(Volume, Ret)), 241), LogFloatCap)` |
| slot a seed 2 | 过 | 0.15 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.07 | 0.11 | 0.12 | 0.02 | 0.08 | 0.29 | `cs_bucket_demean(cross_max(abs_(day_corr(Volume, Ret)), 241), LimitWidth)` |
| slot a seed 3 | 过 | 0.13 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.08 | 0.09 | 0.09 | 0.02 | 0.06 | 0.26 | `cs_bucket_demean(cross_max(abs_(day_corr(Volume, Ret)), 241), BoardCode)` |
| slot a seed 4 | 过 | 0.09 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.08 | 0.09 | 0.05 | 0.02 | 0.06 | 0.26 | `cs_bucket_demean(cross_max(abs_(day_corr(Volume, Ret)), 241), ListAge)` |
| slot a seed 5 | 过 | 0.20 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.18 | 0.06 | 0.02 | 0.03 | 0.08 | 0.00 | `cs_bucket_rank(cross_max(abs_(day_corr(Volume, Ret)), 241), LogFloatCap)` |
| slot a seed 6 | 过 | 0.08 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.08 | 0.08 | 0.03 | 0.02 | 0.06 | 0.24 | `cs_bucket_rank(cross_max(abs_(day_corr(Volume, Ret)), 241), ListAge)` |
| slot a seed 7 | 过 | 0.22 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.18 | 0.01 | 0.01 | 0.03 | 0.04 | 0.08 | `cs_regres(cross_max(abs_(day_corr(Volume, Ret)), 241), cross_mean(day_sum(Amt), 60))` |
| slot a seed 8 | 过 | 0.21 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.18 | 0.03 | 0.00 | 0.03 | 0.00 | 0.11 | `cs_regres(cross_max(abs_(day_corr(Volume, Ret)), 241), cross_mean(day_std(Ret), 60))` |
| slot a seed 9 | 过 | 0.61 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.19 | 0.28 | 0.68 | 0.01 | 0.29 | 0.02 | `div(cross_max(abs_(day_corr(Volume, Ret)), 241), cross_mean(day_std(Ret), 60))` |
| slot a seed 10 | 过 | 0.21 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.18 | 0.04 | 0.00 | 0.03 | 0.00 | 0.11 | `cs_winsor(cross_max(abs_(day_corr(Volume, Ret)), 241))` |
| slot a seed 11 | 过 | 0.21 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.18 | 0.04 | 0.00 | 0.03 | 0.00 | 0.11 | `cs_robust_z(cross_max(abs_(day_corr(Volume, Ret)), 241))` |
| slot a seed 12 | 过 | 0.21 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.19 | 0.06 | 0.02 | 0.02 | 0.02 | 0.10 | `cross_ema(cross_max(abs_(day_corr(Volume, Ret)), 241), 20)` |
| slot b seed 1 | 过 | 0.13 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.15 | 0.06 | 0.06 | 0.01 | 0.04 | 0.20 | `cross_max(abs_(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239))), 241)` |
| slot b seed 2 | 过 | 0.16 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.15 | 0.08 | 0.06 | 0.01 | 0.05 | 0.28 | `cross_max(abs_(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 2, 240))), 241)` |
| slot b seed 3 | 过 | 0.13 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.19 | 0.04 | 0.03 | 0.00 | 0.05 | 0.09 | `cross_max(abs_(day_corr(in_slice(Ret, 6, 240), in_slice(Volume, 1, 235))), 241)` |
| slot b seed 4 | 过 | 0.41 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.15 | 0.37 | 0.34 | 0.19 | 0.38 | 0.10 | `ts_mean(sub(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 2, 240))), 60)` |
| slot b seed 5 | 过 | 0.36 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.16 | 0.37 | 0.28 | 0.10 | 0.38 | 0.12 | `cross_mean(sub(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 2, 240))), 120)` |
| slot b seed 6 | 过 | 0.11 | `day_max(signedpower(cross_argmax(Vwap, 15)))` | 0.10 | 0.09 | 0.06 | 0.02 | 0.08 | 0.17 | `ts_mean(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), 120)` |
| slot b seed 7 | 过 | 0.06 | `pow_2(pow_2(day_q_stat_std(nt_cs_rank(High))))` | 0.17 | 0.15 | 0.01 | 0.01 | 0.14 | 0.21 | `cross_max(sub(abs_(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239))), abs_(day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 2, 240)))), 241)` |
| slot b seed 8 | 过 | 0.17 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.20 | 0.03 | 0.07 | 0.01 | 0.01 | 0.21 | `cross_max(abs_(day_corr(in_slice(Ret, 2, 240), in_slice(Amt, 1, 239))), 120)` |
| slot b seed 9 | 过 | 0.23 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.34 | 0.07 | 0.08 | 0.00 | 0.06 | 0.36 | `cross_tail_mean_q75(abs_(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239))), 120)` |
| slot b seed 10 | 过 | 0.36 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.31 | 0.31 | 0.16 | 0.03 | 0.31 | 0.19 | `ts_std(sub(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239)), day_corr(in_slice(Ret, 1, 239), in_slice(Volume, 2, 240))), 60)` |
| slot b seed 11 | 过 | 0.10 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.08 | 0.01 | 0.07 | 0.02 | 0.00 | 0.03 | `sub(cross_max(abs_(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239))), 241), cross_max(abs_(day_corr(Volume, Ret)), 241))` |
| slot b seed 12 | 废品 | 0.07 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.07 | 0.04 | 0.05 | 0.04 | 0.06 | 0.02 | `cross_argmax(abs_(day_corr(in_slice(Ret, 2, 240), in_slice(Volume, 1, 239))), 120)` |
| R 1 variant 1 | 过 | 0.41 | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Vo` | 0.74 | 0.02 | 0.05 | 0.00 | 0.03 | 0.04 | `ts_regbeta(cs_regres(day_close(Volume), day_kurt(Volume)), day_close(cross_argmax(Vwap, 60)), 20)` |
| R 1 variant 2 | 过 | 0.19 | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Vo` | 0.47 | 0.00 | 0.05 | 0.03 | 0.01 | 0.07 | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume)), day_close(cross_argmax(Vwap, 60)), 40)` |
| R 1 variant 3 | 过 | 0.26 | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Vo` | 0.57 | 0.01 | 0.05 | 0.01 | 0.02 | 0.06 | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume)), day_close(cross_argmax(Vwap, 60)), 30)` |
| R 1 variant 4 | 过 | 0.34 | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Vo` | 0.62 | 0.02 | 0.05 | 0.01 | 0.02 | 0.05 | `ts_regbeta(cs_regres(mul(-5, day_close(Volume)), day_kurt(Volume)), day_close(cross_argmax(Close, 60)), 20)` |
| R 2 variant 1 | 过 | 0.44 | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), d` | 0.70 | 0.30 | 0.16 | 0.04 | 0.29 | 0.17 | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), day_quantile_q25(cross_argmax(Close, 30))), 40)` |
| R 2 variant 2 | 过 | 0.74 | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 5), d` | 0.71 | 0.00 | 0.03 | 0.16 | 0.00 | 0.00 | `ts_autocorr_s1(add(ts_std(signedpower(day_var(Close)), 10), day_quantile_q25(cross_argmax(Close, 30))), 20)` |
| R 2 variant 3 | 过 | 0.15 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.17 | 0.10 | 0.09 | 0.01 | 0.10 | 0.01 | `ts_autocorr_s1(ts_std(signedpower(day_var(Close)), 5), 40)` |
