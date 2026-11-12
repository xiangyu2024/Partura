# 定位:种子 2057,P 组,第 3 轮(只含 train / valid)

快照:prods2057M1_I0_open_search, prods2057M2_I0_open_search, prods2057M3_I0_open_search, prods2057Pr1a_Na, prods2057Pr1b_Nb, prods2057Pr2a_Ea, prods2057Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.35 | -1.05 | -1.35 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10), 20)` |
| -1.62 | -1.06 | -1.62 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 50)` |
| -1.62 | -1.07 | -1.62 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20), 20)` |
| -2.06 | -2.06 | -1.51 | +1 | 20 | prods2057M2_I0_open_search | `cross_min(day_corr(pow_2(Close), nt_cs_mask_top_replace_mean_neg(Open)), 5)` |
| -2.21 | -1.98 | -2.21 | +1 | 20 | prods2057M2_I0_open_search | `day_corr(pow_2(Vwap), Close)` |
| -2.39 | -2.27 | -2.39 | -1 | 0 | prods2057M3_I0_open_search | `ts_quantile_q75(cross_mean(day_q_stat_std(pow_2(Ret)), 3), 30)` |
| -2.41 | -2.30 | -2.41 | -1 | 0 | prods2057M3_I0_open_search | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)), 3)), 30)` |
| -2.41 | -2.41 | -1.92 | +1 | 20 | prods2057M2_I0_open_search | `day_autocorr_n1(pow_2(Open))` |
| -2.64 | -2.03 | -2.64 | -1 | 0 | prods2057M3_I0_open_search | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` |

## 共性:193 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.96 | 0.001 | 4 | +0.06 / -1.90 | `ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10)` |
| +1.72 | 0.000 | 7 | -0.21 / -1.92 | `cs_first_low40(LogFloatCap, ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50))` |
| +1.57 | 0.000 | 64 | -0.81 / -2.38 | `ts_stddev(day_zero_ratio(Ret), 10)` |
| +1.54 | 0.000 | 60 | -0.80 / -2.34 | `ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50)` |
| +1.49 | 0.000 | 72 | -0.92 / -2.42 | `day_zero_ratio(Ret)` |
| +1.27 | 0.001 | 13 | -0.67 / -1.94 | `ts_stddev(ts_stddev(day_centroid(Amt), 10), 50)` |
| +1.24 | 0.000 | 20 | -0.75 / -1.99 | `ts_stddev(day_centroid(Amt), 10)` |
| +1.14 | 0.015 | 7 | -0.76 / -1.90 | `ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10)` |
| +0.96 | 0.091 | 4 | -0.92 / -1.88 | `ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10), 50)` |
| +0.95 | 0.002 | 23 | -1.03 / -1.97 | `day_centroid(Amt)` |
| +0.92 | 0.042 | 9 | -0.98 / -1.90 | `day_cov(Ret, Ret)` |
| +0.91 | 0.073 | 6 | -0.97 / -1.89 | `cs_first_high20(day_cov(Ret, Ret), LogFloatShares)` |
| -0.30 | 0.764 | 4 | -2.15 / -1.85 | `day_argmax(Open)` |
| -0.53 | 0.850 | 4 | -2.38 / -1.85 | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10)` |
| -0.79 | 0.947 | 6 | -2.62 / -1.83 | `day_q_stat_std(pow_2(Ret))` |
| -0.88 | 0.997 | 13 | -2.68 / -1.80 | `day_sum(nt_cs_quantile_q25(Amt))` |
| -1.53 | 0.988 | 5 | -3.35 / -1.82 | `day_mean(Ret)` |
| -2.04 | 0.998 | 5 | -3.84 / -1.81 | `day_skew(Amt)` |

## 拆解(17 次评估)

### head score -2.39:`ts_quantile_q75(cross_mean(day_q_stat_std(pow_2(Ret)), 3), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_q_stat_std(pow_2(Ret)), 3)` | -2.81 | -2.09 | -2.81 | — | (子树本身) |
| sufficiency | `day_q_stat_std(pow_2(Ret))` | -2.90 | -2.57 | -2.90 | — | (子树本身) |
| knockout | `cross_mean(day_q_stat_std(pow_2(Ret)), 3)` | -2.63 | -2.01 | -2.63 | +0.24 | `ts_quantile_q75(day_q_stat_std(pow_2(Ret)), 30)` |
| window | `ts_quantile_q75@30->15` | -2.33 | -1.94 | -2.33 | — | `ts_quantile_q75(cross_mean(day_q_stat_std(pow_2(Ret)), 3), 15)` |
| window | `ts_quantile_q75@30->60` | -3.18 | -2.53 | -3.18 | — | `ts_quantile_q75(cross_mean(day_q_stat_std(pow_2(Ret)), 3), 60)` |

### head score -2.41:`ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)), 3)), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(cross_mean(day_q_stat_std(pow_2(Ret)), 3))` | -2.81 | -2.09 | -2.81 | — | (子树本身) |
| sufficiency | `cross_mean(day_q_stat_std(pow_2(Ret)), 3)` | -2.81 | -2.09 | -2.81 | — | (子树本身) |
| sufficiency | `day_q_stat_std(pow_2(Ret))` | -2.90 | -2.57 | -2.90 | — | (子树本身) |
| knockout | `pow_2(cross_mean(day_q_stat_std(pow_2(Ret)), 3))` | -2.35 | -2.27 | -2.35 | -0.06 | `ts_quantile_q75(cross_mean(day_q_stat_std(pow_2(Ret)), 3), 30)` |
| knockout | `cross_mean(day_q_stat_std(pow_2(Ret)), 3)` | -2.59 | -2.03 | -2.59 | +0.18 | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)` |
| window | `ts_quantile_q75@30->15` | -2.34 | -1.96 | -2.34 | — | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)), 3)), 15)` |
| window | `ts_quantile_q75@30->60` | -3.19 | -2.56 | -3.19 | — | `ts_quantile_q75(pow_2(cross_mean(day_q_stat_std(pow_2(Ret)), 3)), 60)` |

### head score -2.64:`ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_q_stat_std(pow_2(Ret)))` | -2.90 | -2.57 | -2.90 | — | (子树本身) |
| sufficiency | `day_q_stat_std(pow_2(Ret))` | -2.90 | -2.57 | -2.90 | — | (子树本身) |
| knockout | `pow_2(day_q_stat_std(pow_2(Ret)))` | -2.63 | -2.01 | -2.63 | -0.01 | `ts_quantile_q75(day_q_stat_std(pow_2(Ret)), 30)` |
| window | `ts_quantile_q75@30->15` | -2.24 | -1.40 | -2.24 | — | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 15)` |
| window | `ts_quantile_q75@30->60` | -3.18 | -2.60 | -3.18 | — | `ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10)` — enrichment,均值差 +1.96,p 0.001
2. `cs_first_low40(LogFloatCap, ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50))` — enrichment,均值差 +1.72,p 0.000
3. `ts_stddev(day_zero_ratio(Ret), 10)` — enrichment,均值差 +1.57,p 0.000
4. `ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50)` — enrichment,均值差 +1.54,p 0.000
5. `day_zero_ratio(Ret)` — enrichment,均值差 +1.49,p 0.000
6. `ts_stddev(ts_stddev(day_centroid(Amt), 10), 50)` — enrichment,均值差 +1.27,p 0.001
7. `ts_stddev(day_centroid(Amt), 10)` — enrichment,均值差 +1.24,p 0.000
8. `ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10)` — enrichment,均值差 +1.14,p 0.015
9. `ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10), 50)` — enrichment,均值差 +0.96,p 0.091
10. `day_centroid(Amt)` — enrichment,均值差 +0.95,p 0.002
11. `day_cov(Ret, Ret)` — enrichment,均值差 +0.92,p 0.042
12. `cs_first_high20(day_cov(Ret, Ret), LogFloatShares)` — enrichment,均值差 +0.91,p 0.073

## 本组之前各轮的任务

- `prods2057Pr1a_Na`:核心 `—`;评分 57,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score +0.13(train +0.15 valid +0.13):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10), 50)`
  - score -0.02(train +0.11 valid -0.02):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 10), 5), 10), 50)`
  - score -0.10(train +0.19 valid -0.10):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Ret), 10), 50), 10), 50), 10), 50)`
  - score -0.15(train -0.15 valid -0.06):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 20), 50)`
  - score -0.27(train -0.05 valid -0.27):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_centroid(Amt), 10), 50), 10), 10), 50)`
- `prods2057Pr1b_Nb`:核心 `—`;评分 72,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score +0.32(train +0.32 valid +0.80):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), 50)`
  - score +0.26(train +0.26 valid +0.70):`ts_stddev(ts_stddev(ts_delta(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), 10), 50)`
  - score +0.16(train +0.16 valid +0.67):`ts_kurt(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 50), 10), 50)`
  - score +0.08(train +0.08 valid +0.18):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50), 10), 10), 50), 10), 50)`
  - score +0.02(train +0.02 valid +0.64):`ts_stddev(ts_stddev(ts_stddev(ts_stddev(day_zero_ratio(Ret), 20), 50), 10), 50)`
- `prods2057Pr2a_Ea`:核心 `ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50)`;评分 63,过线 0,入 heads 0;采样计数 {'c05_no_core': 571, 'c05_skeleton': 222, 'mutation_refused': 11, 'c05_periphery_seen': 7}
  - score +0.20(train +0.20 valid +0.69):`cs_first_low40(LogFloatCap, cs_first_low40(LogFloatCap, cs_first_low40(LogFloatCap, ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50))))`
  - score +0.15(train +0.15 valid +0.80):`cs_first_low40(LogFloatCap, cs_first_low40(LogFloatCap, ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50)))`
  - score +0.15(train +0.15 valid +0.80):`cs_first_low40(LogFloatCap, cs_first_low40(LogFloatCap, cs_first_low40(LogFloatCap, cs_first_low40(LogFloatCap, ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50)))))`
  - score +0.02(train +0.02 valid +0.96):`cs_first_low20(LogFloatCap, ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50))`
  - score -0.02(train -0.02 valid +0.83):`cs_first_low40(LogFloatCap, cs_first_low40(LogFloatCap, ts_stddev(cs_first_low40(LogFloatCap, cs_first_low40(LogFloatCap, ts_stddev(ts_stddev(day_zero_ratio(Ret), 10), 50))), 50)))`
- `prods2057Pr2b_Nb`:核心 `—`;评分 70,过线 0,入 heads 0;采样计数 {'c05_skeleton': 10}
  - score -0.97(train -0.67 valid -0.97):`cs_first_high20(day_cov(Ret, Ret), LogFloatShares)`
  - score -0.97(train -0.67 valid -0.97):`cs_first_high20(cs_first_high20(day_cov(Ret, Ret), LogFloatShares), LogFloatShares)`
  - score -0.97(train -0.67 valid -0.97):`cs_first_high20(cs_first_high20(cs_first_high20(day_cov(Ret, Ret), LogFloatShares), LogFloatShares), LogFloatShares)`
  - score -0.97(train -0.67 valid -0.97):`cs_first_high20(cs_first_high20(cs_first_high20(cs_first_high20(day_cov(Ret, Ret), LogFloatShares), LogFloatShares), LogFloatShares), LogFloatShares)`
  - score -0.97(train -0.67 valid -0.97):`cs_first_high20(day_cov(Ret, Ret), cs_first_high20(day_cov(Ret, Ret), LogFloatShares))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.40(window ts_quantile_q75@30->15):`ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), 15)`
