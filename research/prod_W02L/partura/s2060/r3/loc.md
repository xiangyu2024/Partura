# 定位:种子 2060,P 组,第 3 轮(只含 train / valid)

快照:prods2060M1_I0_open_search, prods2060M2_I0_open_search, prods2060M3_I0_open_search, prods2060Pr1a_Ea, prods2060Pr1b_Nb, prods2060Pr2a_Ea, prods2060Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.90 | -1.53 | -1.90 | +1 | 5 | prods2060M3_I0_open_search | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), ts_stddev(day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15))` |
| -2.00 | -1.84 | -2.00 | -1 | 20 | prods2060M2_I0_open_search | `pow_2(pow_05(day_max(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(cross_corr(nt_ts_skew(Ret, 3), nt_ts_med(Volume, 3), 10), 3), 5))))` |
| -2.02 | -1.40 | -2.02 | -1 | 20 | prods2060M2_I0_open_search | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(nt_ts_skew(Ret, 3)))), 5)))` |
| -2.02 | -2.02 | -1.77 | +1 | 20 | prods2060M3_I0_open_search | `ts_stddev(day_durbin_watson(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15)` |
| -2.04 | -2.04 | -1.79 | +1 | 20 | prods2060M3_I0_open_search | `ts_stddev(day_ar1_coefficient(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15)` |
| -2.21 | -2.21 | -1.49 | +1 | 20 | prods2060M2_I0_open_search | `day_argmax(cross_max(nt_ts_skew(Vwap, 15), 241))` |
| -3.05 | -3.05 | -2.35 | +1 | 5 | prods2060M1_I0_open_search | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5))), 5)` |
| -3.11 | -2.86 | -3.11 | +1 | 20 | prods2060M1_I0_open_search | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)))), 5)` |
| -3.17 | -2.89 | -3.17 | +1 | 20 | prods2060M1_I0_open_search | `ts_decay_linear(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)), 5)` |

## 共性:258 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.96 | 0.001 | 7 | -0.58 / -2.54 | `sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Amt)))` |
| +1.94 | 0.000 | 10 | -0.62 / -2.56 | `day_mean(Amt)` |
| +1.87 | 0.000 | 19 | -0.75 / -2.62 | `ts_quantile_q75(day_skew(Volume), 1)` |
| +1.85 | 0.000 | 9 | -0.70 / -2.55 | `pow_2(day_mean(Amt))` |
| +1.73 | 0.000 | 22 | -0.90 / -2.63 | `day_skew(Volume)` |
| +1.46 | 0.000 | 20 | -1.14 / -2.60 | `signedpower(day_cov(Vwap, Volume))` |
| +1.30 | 0.000 | 26 | -1.31 / -2.61 | `day_cov(Vwap, Volume)` |
| +1.14 | 0.005 | 8 | -1.38 / -2.52 | `log(day_autocorr_n1(Amt))` |
| +1.12 | 0.009 | 7 | -1.40 / -2.51 | `cross_delay(log(day_autocorr_n1(Amt)), 10)` |
| +1.11 | 0.004 | 9 | -1.41 / -2.52 | `day_autocorr_n1(Amt)` |
| +1.10 | 0.000 | 20 | -1.47 / -2.57 | `pow_2(day_mean(Close))` |
| +1.10 | 0.000 | 21 | -1.48 / -2.57 | `day_mean(Close)` |
| +1.09 | 0.021 | 7 | -1.43 / -2.51 | `sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Close)))` |
| +1.06 | 0.027 | 5 | -1.44 / -2.50 | `day_cov(Amt, Ret)` |
| +1.06 | 0.027 | 5 | -1.44 / -2.50 | `cross_quantile_q75(day_cov(Amt, Ret), 60)` |
| +1.02 | 0.016 | 6 | -1.49 / -2.51 | `cross_argmax(cross_regres(day_kurt(Volume), day_autocorr_n1(High), 60), 241)` |
| +0.97 | 0.054 | 4 | -1.52 / -2.50 | `pow_3(cross_quantile_q75(day_cov(Amt, Ret), 60))` |
| +0.95 | 0.017 | 7 | -1.56 / -2.51 | `cross_rank(pow_2(day_mean(Close)), 60)` |
| +0.89 | 0.052 | 5 | -1.61 / -2.50 | `cross_zscore(day_at_max_ratio(Open), 60)` |
| +0.84 | 0.096 | 4 | -1.66 / -2.50 | `sub(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), day_std(Ret), 60))` |

## 拆解(17 次评估)

### head score -1.90:`add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), ts_stddev(day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15)` | -2.60 | -1.80 | -2.60 | — | (子树本身) |
| sufficiency | `day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230))))` | -4.79 | -3.69 | -4.79 | — | (子树本身) |
| sufficiency | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | -1.34 | -1.34 | -0.79 | — | (子树本身) |
| sufficiency | `day_q_stat_std(in_slice(Ret, 11, 230))` | -4.56 | -4.56 | -4.32 | — | (子树本身) |
| knockout | `ts_stddev(day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15)` | -2.42 | -2.17 | -2.42 | +0.52 | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))))` |
| knockout | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | -2.64 | -2.64 | -2.47 | +0.74 | `add(day_q_stat_std(in_slice(Ret, 11, 230)), ts_stddev(day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15))` |
| swap | `Amt->Volume` | -1.85 | -1.52 | -1.85 | — | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), ts_stddev(day_q_stat_std(div(in_slice(in_zscore_rolling(Volume, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Volume, 21), 11, 230)))), 15))` |
| window | `ts_stddev@15->7` | -2.11 | -1.83 | -2.11 | — | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 7), ts_stddev(day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15))` |
| window | `ts_stddev@15->30` | -1.45 | -1.15 | -1.45 | — | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 30), ts_stddev(day_q_stat_std(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15))` |

### head score -2.02:`ts_stddev(day_durbin_watson(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230))))` | -3.99 | -3.99 | -3.22 | — | (子树本身) |
| swap | `Amt->Volume` | -2.07 | -2.07 | -1.66 | — | `ts_stddev(day_durbin_watson(div(in_slice(in_zscore_rolling(Volume, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Volume, 21), 11, 230)))), 15)` |
| window | `ts_stddev@15->7` | -2.06 | -2.03 | -2.06 | — | `ts_stddev(day_durbin_watson(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 7)` |
| window | `ts_stddev@15->30` | -1.67 | -1.65 | -1.67 | — | `ts_stddev(day_durbin_watson(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 30)` |

### head score -2.04:`ts_stddev(day_ar1_coefficient(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230))))` | -3.98 | -3.98 | -3.27 | — | (子树本身) |
| swap | `Amt->Volume` | -2.03 | -2.03 | -1.76 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(in_zscore_rolling(Volume, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Volume, 21), 11, 230)))), 15)` |
| window | `ts_stddev@15->7` | -2.07 | -1.99 | -2.07 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 7)` |
| window | `ts_stddev@15->30` | -1.60 | -1.60 | -1.55 | — | `ts_stddev(day_ar1_coefficient(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Amt)))` — enrichment,均值差 +1.96,p 0.001
2. `day_mean(Amt)` — enrichment,均值差 +1.94,p 0.000
3. `ts_quantile_q75(day_skew(Volume), 1)` — enrichment,均值差 +1.87,p 0.000
4. `pow_2(day_mean(Amt))` — enrichment,均值差 +1.85,p 0.000
5. `day_skew(Volume)` — enrichment,均值差 +1.73,p 0.000
6. `signedpower(day_cov(Vwap, Volume))` — enrichment,均值差 +1.46,p 0.000
7. `day_cov(Vwap, Volume)` — enrichment,均值差 +1.30,p 0.000
8. `log(day_autocorr_n1(Amt))` — enrichment,均值差 +1.14,p 0.005
9. `cross_delay(log(day_autocorr_n1(Amt)), 10)` — enrichment,均值差 +1.12,p 0.009
10. `day_autocorr_n1(Amt)` — enrichment,均值差 +1.11,p 0.004
11. `pow_2(day_mean(Close))` — enrichment,均值差 +1.10,p 0.000
12. `day_mean(Close)` — enrichment,均值差 +1.10,p 0.000
13. `sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Close)))` — enrichment,均值差 +1.09,p 0.021
14. `day_cov(Amt, Ret)` — enrichment,均值差 +1.06,p 0.027
15. `cross_quantile_q75(day_cov(Amt, Ret), 60)` — enrichment,均值差 +1.06,p 0.027
16. `cross_argmax(cross_regres(day_kurt(Volume), day_autocorr_n1(High), 60), 241)` — enrichment,均值差 +1.02,p 0.016
17. `pow_3(cross_quantile_q75(day_cov(Amt, Ret), 60))` — enrichment,均值差 +0.97,p 0.054
18. `cross_rank(pow_2(day_mean(Close)), 60)` — enrichment,均值差 +0.95,p 0.017
19. `cross_zscore(day_at_max_ratio(Open), 60)` — enrichment,均值差 +0.89,p 0.052
20. `sub(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), day_std(Ret), 60))` — enrichment,均值差 +0.84,p 0.096
21. `cross_corr(day_ar1_coefficient(Volume), day_std(Ret), 60)` — enrichment,均值差 +0.81,p 0.073
22. `day_autocorr_n1(High)` — enrichment,均值差 +0.77,p 0.014
23. `day_std(Ret)` — enrichment,均值差 +0.73,p 0.031
24. `sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap))` — enrichment,均值差 +0.65,p 0.004
25. `day_kurt(Volume)` — enrichment,均值差 +0.63,p 0.026
26. `day_at_max_ratio(Open)` — enrichment,均值差 +0.49,p 0.010
27. `cross_regres(day_kurt(Volume), day_autocorr_n1(High), 60)` — enrichment,均值差 +0.49,p 0.095
28. `day_ar1_coefficient(Volume)` — enrichment,均值差 +0.45,p 0.003

## 本组之前各轮的任务

- `prods2060Pr1a_Ea`:核心 `day_ar1_coefficient(Volume)`;评分 95,过线 0,入 heads 0;采样计数 {'c05_no_core': 2031, 'c05_skeleton': 1041}
  - score -0.36(train +0.15 valid -0.36):`sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap))`
  - score -0.39(train -0.39 valid -0.27):`cross_zscore(sub(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap)), 60)), 241)`
  - score -0.46(train -0.12 valid -0.46):`cross_zscore(sub(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), cross_corr(day_ar1_coefficient(Volume), sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap)), 60), 60)), 241)`
  - score -0.77(train -0.77 valid -0.54):`cross_zscore(sub(sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap)), cs_quantile_q75(LogFloatCap)), 241)`
  - score -0.85(train -0.85 valid -0.48):`cross_zscore(sub(day_ar1_coefficient(Volume), cs_quantile_q75(LogFloatCap)), 241)`
- `prods2060Pr1b_Nb`:核心 `—`;评分 52,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.07(train -0.07 valid +0.17):`neg(cross_autocorr_s1(day_at_max_ratio(Open), 15))`
  - score -0.07(train -0.07 valid +0.17):`neg(neg(cross_autocorr_s1(day_at_max_ratio(Open), 15)))`
  - score -0.07(train -0.07 valid +0.17):`cross_autocorr_s1(day_at_max_ratio(Open), 15)`
  - score -0.33(train -0.11 valid -0.33):`neg(cross_autocorr_s1(day_at_max_ratio(Low), 15))`
  - score -0.33(train -0.11 valid -0.33):`cross_autocorr_s1(day_at_max_ratio(Low), 15)`
- `prods2060Pr2a_Ea`:核心 `day_at_max_ratio(Open)`;评分 93,过线 0,入 heads 0;采样计数 {'c05_no_core': 1423, 'c05_skeleton': 702, 'c05_periphery_seen': 11}
  - score -0.26(train +0.38 valid -0.26):`cross_mean(cross_corr(day_at_max_ratio(Open), day_first(Amt), 60), 30)`
  - score -0.40(train -0.40 valid +0.60):`cross_corr(day_at_max_ratio(Open), cross_zscore(day_at_max_ratio(Open), 60), 60)`
  - score -0.43(train -0.43 valid +0.39):`cross_corr(cross_corr(day_at_max_ratio(Open), cross_corr(day_at_max_ratio(Open), day_first(Amt), 60), 60), cross_corr(day_at_max_ratio(Open), day_first(Amt), 60), 60)`
  - score -0.74(train -0.74 valid -0.26):`cross_mean(cross_mean(sub(day_at_max_ratio(Open), day_at_min_ratio(Open)), 30), 20)`
  - score -0.77(train -0.77 valid -0.37):`cross_mean(sub(day_at_max_ratio(Open), day_at_min_ratio(Open)), 30)`
- `prods2060Pr2b_Nb`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {'c05_skeleton': 12}
  - score +0.33(train +0.69 valid +0.33):`ts_regbeta(sub(signedpower(ts_regbeta(sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Amt))), ts_quantile_q75(day_skew(Volume), 1), 10)), pow_2(day_mean(Amt))), ts_quantile_q75(day_skew(Volume), 1), 10)`
  - score +0.33(train +0.77 valid +0.33):`ts_regbeta(sub(day_skew(Volume), pow_2(day_mean(Amt))), ts_quantile_q75(day_skew(Volume), 1), 10)`
  - score +0.30(train +0.77 valid +0.30):`ts_regbeta(sub(sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Amt))), pow_2(day_mean(Amt))), ts_quantile_q75(day_skew(Volume), 1), 10)`
  - score +0.28(train +0.76 valid +0.28):`ts_regbeta(sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Amt))), ts_quantile_q75(day_skew(Volume), 1), 10)`
  - score +0.17(train +0.17 valid +0.41):`ts_regbeta(sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Close))), ts_regbeta(sub(signedpower(day_cov(Vwap, Volume)), pow_2(day_mean(Amt))), ts_quantile_q75(day_skew(Volume), 1), 10), 10)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.44(window ts_stddev@15->30):`ts_stddev(day_ar1_coefficient(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 30)`
- 增益 +0.36(window ts_stddev@15->30):`ts_stddev(day_durbin_watson(div(in_slice(in_zscore_rolling(Amt, 21), 11, 230), in_sum(in_slice(in_zscore_rolling(Amt, 21), 11, 230)))), 30)`
