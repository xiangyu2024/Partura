# 定位:种子 2080,P 组,第 2 轮(只含 train / valid)

快照:prods2080M1_I0_open_search, prods2080M2_I0_open_search, prods2080Pr1a_Ea, prods2080Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.62 | -0.62 | +0.02 | +1 | 0 | prods2080M2_I0_open_search | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 50)` |
| -0.82 | -0.63 | -0.82 | +1 | 5 | prods2080M2_I0_open_search | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30), 60), 10)` |
| -0.90 | -0.68 | -0.90 | +1 | 0 | prods2080M2_I0_open_search | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50), 40)` |
| -1.11 | -0.74 | -1.11 | +1 | 20 | prods2080M1_I0_open_search | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15), 5)` |
| -1.13 | -0.78 | -1.13 | -1 | 5 | prods2080M1_I0_open_search | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` |
| -1.26 | -0.82 | -1.26 | -1 | 20 | prods2080M1_I0_open_search | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Vwap), 3)), 20)` |

## 共性:222 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.18 | 0.002 | 5 | -1.10 / -2.29 | `day_mean(Volume)` |
| +1.18 | 0.002 | 5 | -1.10 / -2.29 | `ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50)` |
| +1.18 | 0.002 | 5 | -1.10 / -2.29 | `cs_normalize(day_mean(Volume))` |
| +1.03 | 0.003 | 8 | -1.26 / -2.30 | `cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40)` |
| +0.90 | 0.014 | 5 | -1.39 / -2.28 | `sqrt(day_sum(Ret))` |
| +0.84 | 0.000 | 20 | -1.49 / -2.34 | `cs_robust_z(LogFloatShares)` |
| +0.67 | 0.160 | 4 | -1.60 / -2.27 | `cross_delay(cs_winsor(day_autocorr_n1(Amt)), 60)` |
| +0.65 | 0.040 | 6 | -1.63 / -2.28 | `day_cov(Close, Ret)` |
| +0.63 | 0.002 | 19 | -1.68 / -2.32 | `day_close(High)` |
| +0.62 | 0.061 | 5 | -1.66 / -2.28 | `sqrt(cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60))` |
| +0.62 | 0.061 | 5 | -1.66 / -2.28 | `cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60)` |
| +0.57 | 0.139 | 8 | -1.71 / -2.28 | `cs_winsor(day_autocorr_n1(Amt))` |
| +0.53 | 0.138 | 4 | -1.74 / -2.27 | `day_last(Amt)` |
| +0.51 | 0.060 | 9 | -1.78 / -2.28 | `abs_(day_sum(Amt))` |
| +0.50 | 0.000 | 101 | -1.99 / -2.49 | `day_q_stat_std(Volume)` |
| +0.44 | 0.095 | 31 | -1.88 / -2.32 | `day_ar1_coefficient(Ret)` |
| +0.41 | 0.277 | 9 | -1.87 / -2.28 | `day_autocorr_n1(Amt)` |
| +0.30 | 0.290 | 4 | -1.97 / -2.27 | `day_q_stat_std(Ret)` |
| +0.29 | 0.070 | 18 | -1.99 / -2.29 | `day_sum(Ret)` |
| +0.28 | 0.206 | 11 | -1.99 / -2.28 | `day_sum(Amt)` |

## 拆解(30 次评估)

### head score -0.62:`ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)))` | -0.25 | -0.25 | +0.03 | — | (子树本身) |
| sufficiency | `neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))` | -0.25 | -0.25 | +0.03 | — | (子树本身) |
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | -0.25 | -0.25 | +0.03 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10)` | -2.26 | -2.21 | -2.26 | — | (子树本身) |
| knockout | `neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)))` | -0.56 | -0.56 | -0.06 | -0.06 | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)), 50)` |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` | — | — | — | — | `ts_std(neg(neg(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10))), 50)` |
| knockout | `ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10)` | -0.39 | -0.39 | -0.11 | -0.23 | `ts_std(neg(neg(cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 241))), 50)` |
| window | `ts_std@50->25` | -0.37 | -0.37 | +0.56 | — | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 25)` |
| window | `ts_std@50->100` | -1.30 | -1.30 | +0.01 | — | `ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 100)` |

### head score -0.82:`ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30), 60), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30), 60)` | -1.05 | -1.05 | -1.05 | — | (子树本身) |
| sufficiency | `ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30)` | -1.47 | -1.43 | -1.47 | — | (子树本身) |
| sufficiency | `day_cov(cross_quantile_q75(Low, 241), Amt)` | -1.53 | -1.53 | -1.04 | — | (子树本身) |
| knockout | `cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30), 60)` | -2.16 | -1.67 | -2.16 | +1.34 | `ts_std(ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30), 10)` |
| knockout | `ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30)` | -1.27 | -1.27 | -0.58 | +0.45 | `ts_std(cross_stddev(day_cov(cross_quantile_q75(Low, 241), Amt), 60), 10)` |
| swap | `Low->High` | -0.69 | -0.69 | -0.35 | — | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(High, 241), Amt), 30), 60), 10)` |
| swap | `Amt->Volume` | -1.08 | -0.29 | -1.08 | — | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 241), Volume), 30), 60), 10)` |
| window | `ts_std@10->5` | -0.98 | -0.75 | -0.98 | — | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30), 60), 5)` |
| window | `ts_std@10->20` | -0.75 | -0.66 | -0.75 | — | `ts_std(cross_stddev(ts_std(day_cov(cross_quantile_q75(Low, 241), Amt), 30), 60), 20)` |

### head score -0.90:`ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50)` | -1.34 | -1.34 | -1.12 | — | (子树本身) |
| sufficiency | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40)` | -0.86 | -0.78 | -0.86 | — | (子树本身) |
| sufficiency | `ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50)` | -1.43 | -0.95 | -1.43 | — | (子树本身) |
| sufficiency | `ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40)` | -1.14 | -0.55 | -1.14 | — | (子树本身) |
| knockout | `ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50)` | -0.90 | -0.26 | -0.90 | -0.00 | `ts_std(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 40)` |
| knockout | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40)` | -0.96 | -0.59 | -0.96 | +0.06 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 50), 40)` |
| knockout | `ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50)` | -1.00 | -0.59 | -1.00 | +0.10 | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 40), 50), 40)` |
| knockout | `ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40)` | -0.91 | -0.71 | -0.91 | +0.01 | `ts_std(ts_cov(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50), 40)` |
| swap | `Volume->Amt` | -1.05 | -0.96 | -1.05 | — | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Amt)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Amt)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Amt)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Amt)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Amt)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50), 40)` |
| swap | `High->Low` | -0.89 | -0.69 | -0.89 | — | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(Low), 50), 40), day_close(Low), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(Low), 50), 40), day_close(Low), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(Low), 50), 40), day_close(Low), 50), 40), 50), 40), 50), 40)` |
| window | `ts_std@40->20` | -1.00 | -0.71 | -1.00 | — | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50), 20)` |
| window | `ts_std@40->80` | -0.93 | -0.82 | -0.93 | — | `ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), ts_std(ts_cov(ts_std(ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50), 40), day_close(High), 50), 40), 50), 40), 50), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_mean(Volume)` — enrichment,均值差 +1.18,p 0.002
2. `ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50)` — enrichment,均值差 +1.18,p 0.002
3. `cs_normalize(day_mean(Volume))` — enrichment,均值差 +1.18,p 0.002
4. `cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40)` — enrichment,均值差 +1.03,p 0.003
5. `sqrt(day_sum(Ret))` — enrichment,均值差 +0.90,p 0.014
6. `cs_robust_z(LogFloatShares)` — enrichment,均值差 +0.84,p 0.000
7. `day_cov(Close, Ret)` — enrichment,均值差 +0.65,p 0.040
8. `day_close(High)` — enrichment,均值差 +0.63,p 0.002
9. `sqrt(cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60))` — enrichment,均值差 +0.62,p 0.061
10. `cross_corr(day_q_stat_std(Volume), abs_(day_sum(Amt)), 60)` — enrichment,均值差 +0.62,p 0.061
11. `abs_(day_sum(Amt))` — enrichment,均值差 +0.51,p 0.060
12. `day_q_stat_std(Volume)` — enrichment,均值差 +0.50,p 0.000
13. `day_ar1_coefficient(Ret)` — enrichment,均值差 +0.44,p 0.095
14. `day_sum(Ret)` — enrichment,均值差 +0.29,p 0.070

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.25(window ts_std@50->25):`ts_std(neg(neg(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241))), 25)`
- 增益 +0.23(knockout ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10)):`ts_std(neg(neg(cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 241))), 50)`
