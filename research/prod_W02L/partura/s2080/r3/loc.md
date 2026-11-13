# 定位:种子 2080,P 组,第 3 轮(只含 train / valid)

快照:prods2080M1_I0_open_search, prods2080M2_I0_open_search, prods2080M3_I0_open_search, prods2080Pr1a_Ea, prods2080Pr1b_Nb, prods2080Pr2a_Ea, prods2080Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.37 | -0.37 | +0.56 | +1 | 0 | prods2080M2_I0_open_search | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 25)` |
| -0.57 | -0.28 | -0.57 | +1 | 0 | prods2080M3_I0_open_search | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30)` |
| -0.70 | -0.56 | -0.70 | +1 | 5 | prods2080M3_I0_open_search | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 10), 20)` |
| -0.79 | -0.79 | -0.55 | +1 | 5 | prods2080M3_I0_open_search | `ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5)` |
| -0.82 | -0.63 | -0.82 | +1 | 5 | prods2080M2_I0_open_search | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30), 60), 10)` |
| -0.90 | -0.68 | -0.90 | +1 | 0 | prods2080M2_I0_open_search | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50), 40)` |
| -1.11 | -0.74 | -1.11 | +1 | 20 | prods2080M1_I0_open_search | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15), 5)` |
| -1.13 | -0.78 | -1.13 | -1 | 5 | prods2080M1_I0_open_search | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` |
| -1.26 | -0.82 | -1.26 | -1 | 20 | prods2080M1_I0_open_search | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Vwap), 3)), 20)` |

## 共性:320 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.25 | 0.001 | 5 | -1.10 / -2.35 | `ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50)` |
| +1.25 | 0.001 | 5 | -1.10 / -2.35 | `day_mean(Volume)` |
| +1.25 | 0.001 | 5 | -1.10 / -2.35 | `cs_normalize(day_mean(Volume))` |
| +1.09 | 0.002 | 8 | -1.26 / -2.36 | `cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40)` |
| +0.96 | 0.009 | 5 | -1.39 / -2.35 | `sqrt(day_sum(Ret))` |
| +0.89 | 0.000 | 20 | -1.49 / -2.39 | `cs_robust_z(LogFloatShares)` |
| +0.79 | 0.066 | 4 | -1.55 / -2.34 | `day_hurst(Open)` |
| +0.74 | 0.138 | 4 | -1.60 / -2.34 | `cross_delay(cs_winsor(day_autocorr_n1(Amt)), 60)` |
| +0.71 | 0.026 | 6 | -1.63 / -2.34 | `day_cov(Close, Ret)` |
| +0.69 | 0.001 | 19 | -1.68 / -2.37 | `day_close(High)` |
| +0.68 | 0.048 | 5 | -1.66 / -2.34 | `sqrt(cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60))` |
| +0.68 | 0.048 | 5 | -1.66 / -2.34 | `cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60)` |
| +0.67 | 0.086 | 4 | -1.67 / -2.34 | `day_sum(Volume)` |
| +0.64 | 0.108 | 8 | -1.71 / -2.35 | `cs_winsor(day_autocorr_n1(Amt))` |
| +0.60 | 0.123 | 4 | -1.74 / -2.34 | `day_last(Amt)` |
| +0.57 | 0.037 | 9 | -1.78 / -2.35 | `abs_(day_sum(Amt))` |
| +0.55 | 0.112 | 4 | -1.79 / -2.34 | `day_gini(Low)` |
| +0.50 | 0.000 | 103 | -1.99 / -2.49 | `day_q_stat_std(Volume)` |
| +0.50 | 0.059 | 31 | -1.88 / -2.38 | `day_ar1_coefficient(Ret)` |
| +0.48 | 0.224 | 9 | -1.87 / -2.34 | `day_autocorr_n1(Amt)` |

## 拆解(32 次评估)

### head score -0.37:`ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 25)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)))` | -0.25 | -0.25 | +0.03 | — | (子树本身) |
| sufficiency | `neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))` | -0.25 | -0.25 | +0.03 | — | (子树本身) |
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | -0.25 | -0.25 | +0.03 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10)` | -2.26 | -2.21 | -2.26 | — | (子树本身) |
| knockout | `neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)))` | -0.37 | -0.37 | +0.56 | -0.00 | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)), 25)` |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | — | — | — | — | `ts_std(neg(neg(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10))), 25)` |
| knockout | `ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10)` | — | — | — | — | `ts_std(neg(neg(cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 241))), 25)` |
| window | `ts_std@25->12` | — | — | — | — | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 12)` |
| window | `ts_std@25->50` | -0.56 | -0.56 | -0.06 | — | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 50)` |

### head score -0.57:`ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30)` | -3.19 | -3.08 | -3.19 | — | (子树本身) |
| sufficiency | `day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt)))` | — | — | — | — | 门槛废品 |
| swap | `Amt->Volume` | +0.08 | +0.53 | +0.08 | — | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Volume))), 30), 30)` |
| window | `ts_stddev@30->15` | -1.35 | -1.35 | -1.22 | — | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 15)` |
| window | `ts_stddev@30->60` | -0.68 | -0.37 | -0.68 | — | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 60)` |

### head score -0.70:`ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 10), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 10)` | -2.25 | -2.25 | -2.22 | — | (子树本身) |
| sufficiency | `ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30)` | -3.19 | -3.08 | -3.19 | — | (子树本身) |
| sufficiency | `day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt)))` | — | — | — | — | 门槛废品 |
| knockout | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 10)` | -0.82 | -0.82 | -0.59 | +0.11 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 20)` |
| knockout | `ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30)` | -2.92 | -2.92 | -2.36 | +2.22 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 10), 20)` |
| swap | `Amt->Volume` | -0.12 | +0.57 | -0.12 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Volume))), 30), 10), 20)` |
| window | `ts_stddev@20->10` | -0.82 | -0.82 | -0.82 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 10), 10)` |
| window | `ts_stddev@20->40` | -0.92 | -0.60 | -0.92 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 10), 40)` |

### head score -0.79:`ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40)` | -2.25 | -2.25 | -2.08 | — | (子树本身) |
| sufficiency | `cross_cov(day_close(Amt), day_hurst(Open), 30)` | -2.56 | -2.56 | -2.16 | — | (子树本身) |
| sufficiency | `day_close(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| sufficiency | `day_hurst(Open)` | -4.92 | -4.92 | -3.83 | — | (子树本身) |
| knockout | `ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40)` | -1.26 | -1.26 | -0.87 | +0.47 | `ts_var(cross_cov(day_close(Amt), day_hurst(Open), 30), 5)` |
| knockout | `cross_cov(day_close(Amt), day_hurst(Open), 30)` | -0.76 | -0.76 | -0.23 | -0.02 | `ts_var(ts_mean(day_close(Amt), 40), 5)` |
| swap | `Amt->Volume` | -2.54 | -1.40 | -2.54 | — | `ts_var(ts_mean(cross_cov(day_close(Volume), day_hurst(Open), 30), 40), 5)` |
| swap | `Open->Close` | -0.87 | -0.87 | -0.34 | — | `ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Close), 30), 40), 5)` |
| window | `ts_var@5->2` | -0.61 | -0.61 | -0.43 | — | `ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 2)` |
| window | `ts_var@5->10` | -0.80 | -0.65 | -0.80 | — | `ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50)` — enrichment,均值差 +1.25,p 0.001
2. `day_mean(Volume)` — enrichment,均值差 +1.25,p 0.001
3. `cs_normalize(day_mean(Volume))` — enrichment,均值差 +1.25,p 0.001
4. `cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40)` — enrichment,均值差 +1.09,p 0.002
5. `sqrt(day_sum(Ret))` — enrichment,均值差 +0.96,p 0.009
6. `cs_robust_z(LogFloatShares)` — enrichment,均值差 +0.89,p 0.000
7. `day_hurst(Open)` — enrichment,均值差 +0.79,p 0.066
8. `day_cov(Close, Ret)` — enrichment,均值差 +0.71,p 0.026
9. `day_close(High)` — enrichment,均值差 +0.69,p 0.001
10. `sqrt(cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60))` — enrichment,均值差 +0.68,p 0.048
11. `cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60)` — enrichment,均值差 +0.68,p 0.048
12. `day_sum(Volume)` — enrichment,均值差 +0.67,p 0.086
13. `abs_(day_sum(Amt))` — enrichment,均值差 +0.57,p 0.037
14. `day_q_stat_std(Volume)` — enrichment,均值差 +0.50,p 0.000
15. `day_ar1_coefficient(Ret)` — enrichment,均值差 +0.50,p 0.059
16. `day_sum(Ret)` — enrichment,均值差 +0.36,p 0.037
17. `day_mean(Low)` — enrichment,均值差 +0.35,p 0.075
18. `sqrt(day_q_stat_std(Volume))` — enrichment,均值差 +0.29,p 0.091

## 本组之前各轮的任务

- `prods2080Pr1a_Ea`:核心 `day_q_stat_std(Volume)`;评分 100,过线 0,入 heads 0;采样计数 {'c05_no_core': 1125, 'c05_skeleton': 544}
  - score -0.88(train -0.35 valid -0.88):`cross_corr(day_q_stat_std(Volume), sqrt(day_q_stat_std(Volume)), 60)`
  - score -1.05(train -1.05 valid -0.59):`sqrt(cross_corr(day_q_stat_std(Volume), abs_(day_sum(Volume)), 60))`
  - score -1.06(train -0.99 valid -1.06):`cs_last_low20(cs_robust_z(LogFloatShares), sqrt(cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60)))`
  - score -1.14(train -1.14 valid -0.90):`cross_corr(day_q_stat_std(Volume), abs_(day_sum(Ret)), 60)`
  - score -1.14(train -1.14 valid -0.90):`cross_corr(day_q_stat_std(Volume), abs_(abs_(day_sum(Ret))), 60)`
- `prods2080Pr1b_Nb`:核心 `—`;评分 80,过线 0,入 heads 0;采样计数 {'c05_skeleton': 14}
  - score -0.13(train -0.13 valid -0.10):`cross_regbeta(day_q_stat_std(Volume), cross_delay(cs_winsor(day_autocorr_n1(Amt)), 60), 40)`
  - score -0.14(train -0.14 valid -0.13):`cross_regbeta(day_q_stat_std(Volume), cross_delay(cs_winsor(day_autocorr_n1(Volume)), 60), 40)`
  - score -0.17(train +0.04 valid -0.17):`cross_regbeta(day_q_stat_std(Volume), cross_delay(cs_winsor(day_autocorr_n1(Amt)), 10), 40)`
  - score -0.23(train -0.23 valid -0.07):`cross_regbeta(day_q_stat_std(Volume), cross_delay(cs_winsor(day_autocorr_n1(Ret)), 60), 30)`
  - score -0.27(train -0.27 valid -0.08):`cs_winsor(cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40))`
- `prods2080Pr2a_Ea`:核心 `ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50)`;评分 54,过线 0,入 heads 0;采样计数 {'c05_no_core': 5804, 'c05_skeleton': 3269}
  - score -2.68(train -2.42 valid -2.68):`day_es_ratio_hi(Open)`
  - score -2.69(train -2.69 valid -2.58):`day_es_ratio_lo(Open)`
  - score -2.84(train -2.84 valid -2.69):`day_es_ratio_lo(Vwap)`
  - score -3.81(train -2.76 valid -3.81):`day_kurt(Ret)`
  - score -3.99(train -3.63 valid -3.99):`day_kurt(Close)`
- `prods2080Pr2b_Nb`:核心 `—`;评分 94,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.69(train -0.69 valid +0.32):`cross_corr(day_gini(Ret), day_signed_ratio(Ret, Amt), 60)`
  - score -0.80(train -0.80 valid +0.24):`cross_corr(cs_last_high05(day_gini(Ret), day_mean(Low)), day_signed_ratio(Ret, Amt), 60)`
  - score -1.41(train -1.32 valid -1.41):`cross_corr(day_gini(Low), day_signed_ratio(Ret, Amt), 60)`
  - score -1.41(train -1.41 valid -0.72):`ts_max(cs_last_high05(cross_corr(cs_last_high05(LogTotalCap, day_mean(Low)), day_signed_ratio(Ret, Amt), 60), day_mean(Low)), 20)`
  - score -1.44(train -0.80 valid -1.44):`cross_corr(day_gini(Amt), day_signed_ratio(Ret, Amt), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.65(swap Amt->Volume):`ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Volume))), 30), 30)`
- 增益 +0.58(swap Amt->Volume):`ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Volume))), 30), 10), 20)`
