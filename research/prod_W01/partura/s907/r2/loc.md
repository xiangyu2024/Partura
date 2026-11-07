# 定位:种子 907,P 组,第 2 轮(只含 train / valid)

快照:prods907M1_I0_open_search, prods907M2_I0_open_search, prods907Pr1a_Na, prods907Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.57 | +1.71 | +1.57 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mean(day_gini(Volume), 30))` |
| +1.43 | +1.49 | +1.43 | -1 | 20 | prods907M2_I0_open_search | `signedpower(cs_first_low40(abs_(LogFloatShares), day_std(Volume)))` |
| +0.99 | +1.09 | +0.99 | +1 | 5 | prods907M2_I0_open_search | `signedpower(cs_first_low40(LogFloatShares, signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))))` |
| +0.99 | +0.99 | +1.25 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))` |
| +0.92 | +0.92 | +1.26 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 20), 20))))` |
| +0.78 | +1.11 | +0.78 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(ts_hurst(ts_autocorr_s1(cs_rank(cross_mean(day_centroid(Volume), 30)), 20), 20))))` |
| +0.73 | +1.24 | +0.73 | +1 | 5 | prods907M2_I0_open_search | `signedpower(cs_first_low40(cs_bucket_zscore(LogFloatShares, cs_first_low40(LogFloatShares, day_std(Volume))), cs_first_low40(LogFloatShares, day_std(Volume))))` |
| +0.73 | +1.17 | +0.73 | -1 | 5 | prods907Pr1b_Nb | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(cross_mean(sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 20), 30)))), 30))))` |
| +0.72 | +0.72 | +0.86 | -1 | 0 | prods907M2_I0_open_search | `signedpower(cs_first_low40(abs_(LogFloatShares), LogFloatShares))` |
| +0.51 | +0.51 | +1.35 | +1 | 20 | prods907Pr1a_Na | `div(day_last(Close), div(ts_cov(day_durbin_watson(Close), day_distinct_ratio(Close), 50), FloatShares))` |

## 共性:315 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.06 | 0.001 | 4 | +1.12 / -0.95 | `cs_first_low40(abs_(LogFloatShares), day_std(Volume))` |
| +2.03 | 0.000 | 9 | +1.05 / -0.98 | `cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))` |
| +1.98 | 0.001 | 5 | +1.03 / -0.95 | `signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))` |
| +1.95 | 0.000 | 10 | +0.97 / -0.98 | `cs_first_low40(LogFloatShares, day_std(Volume))` |
| +1.94 | 0.001 | 6 | +0.98 / -0.96 | `cs_first_low40(day_std(Volume), day_std(Volume))` |
| +1.59 | 0.005 | 4 | +0.65 / -0.94 | `signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))` |
| +1.59 | 0.000 | 21 | +0.56 / -1.03 | `cs_rank(cross_mean(day_centroid(Volume), 30))` |
| +1.55 | 0.000 | 23 | +0.51 / -1.03 | `cross_mean(day_centroid(Volume), 30)` |
| +1.42 | 0.000 | 28 | +0.38 / -1.05 | `day_centroid(Volume)` |
| +1.26 | 0.000 | 104 | -0.08 / -1.34 | `day_std(Volume)` |
| +1.19 | 0.000 | 20 | +0.20 / -1.00 | `cs_quantile_q25(LogFloatShares)` |
| +1.18 | 0.001 | 13 | +0.21 / -0.97 | `abs_(LogFloatShares)` |
| +1.12 | 0.001 | 14 | +0.15 / -0.97 | `cross_mean(day_gini(Volume), 30)` |
| +0.96 | 0.053 | 5 | +0.03 / -0.94 | `ts_autocorr_s1(day_argmax(Vwap), 20)` |
| +0.90 | 0.007 | 12 | -0.05 / -0.95 | `cs_rank(cross_mean(day_gini(Volume), 30))` |
| +0.86 | 0.094 | 4 | -0.07 / -0.93 | `cs_bucket_zscore(LogFloatShares, day_std(Volume))` |
| +0.83 | 0.003 | 18 | -0.13 / -0.97 | `day_gini(Volume)` |
| +0.79 | 0.122 | 4 | -0.14 / -0.93 | `cs_rank(cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 20), 20)))` |
| +0.79 | 0.122 | 4 | -0.14 / -0.93 | `ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 20), 20)` |
| +0.79 | 0.122 | 4 | -0.14 / -0.93 | `cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 20), 20))` |

## 拆解(37 次评估)

### head score +1.57:`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mean(day_gini(Volume), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(cross_mean(day_centroid(Volume), 30))` | +1.73 | +1.73 | +1.88 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Volume), 30)` | +1.73 | +1.73 | +1.88 | — | (子树本身) |
| sufficiency | `cross_mean(day_gini(Volume), 30)` | -2.02 | -2.02 | -1.96 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `cs_rank(cross_mean(day_centroid(Volume), 30))` | -1.49 | -1.05 | -1.49 | +3.05 | `sub(cross_mean(day_centroid(Volume), 30), cross_mean(day_gini(Volume), 30))` |
| knockout | `cross_mean(day_centroid(Volume), 30)` | -0.22 | +1.26 | -0.22 | +1.79 | `sub(cs_rank(day_centroid(Volume)), cross_mean(day_gini(Volume), 30))` |
| knockout | `cross_mean(day_gini(Volume), 30)` | +1.30 | +1.47 | +1.30 | +0.27 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), day_gini(Volume))` |
| swap | `Volume->Amt` | +1.55 | +1.72 | +1.55 | — | `sub(cs_rank(cross_mean(day_centroid(Amt), 30)), cross_mean(day_gini(Amt), 30))` |
| window | `cross_mean@30->15` | +0.89 | +1.83 | +0.89 | — | `sub(cs_rank(cross_mean(day_centroid(Volume), 15)), cross_mean(day_gini(Volume), 30))` |
| window | `cross_mean@30->60` | +0.70 | +1.51 | +0.70 | — | `sub(cs_rank(cross_mean(day_centroid(Volume), 60)), cross_mean(day_gini(Volume), 30))` |

### head score +1.43:`signedpower(cs_first_low40(abs_(LogFloatShares), day_std(Volume)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low40(abs_(LogFloatShares), day_std(Volume))` | +1.43 | +1.49 | +1.43 | — | (子树本身) |
| sufficiency | `abs_(LogFloatShares)` | -0.54 | -0.54 | -0.41 | — | (子树本身) |
| sufficiency | `day_std(Volume)` | -1.87 | -0.20 | -1.87 | — | (子树本身) |
| knockout | `cs_first_low40(abs_(LogFloatShares), day_std(Volume))` | -0.54 | -0.54 | -0.41 | +1.97 | `signedpower(abs_(LogFloatShares))` |
| knockout | `abs_(LogFloatShares)` | +1.43 | +1.49 | +1.43 | -0.00 | `signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))` |
| swap | `Volume->Amt` | -2.49 | -0.93 | -2.49 | — | `signedpower(cs_first_low40(abs_(LogFloatShares), day_std(Amt)))` |

### head score +0.99:`signedpower(cs_first_low40(LogFloatShares, signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low40(LogFloatShares, signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))))` | +0.99 | +1.09 | +0.99 | — | (子树本身) |
| sufficiency | `signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))` | +1.38 | +1.38 | +2.03 | — | (子树本身) |
| sufficiency | `cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))` | +1.38 | +1.38 | +2.03 | — | (子树本身) |
| sufficiency | `day_std(Volume)` | -1.87 | -0.20 | -1.87 | — | (子树本身) |
| knockout | `cs_first_low40(LogFloatShares, signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))))` | -0.54 | -0.54 | -0.41 | +1.52 | `signedpower(LogFloatShares)` |
| knockout | `signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))` | +0.99 | +1.09 | +0.99 | +0.00 | `signedpower(cs_first_low40(LogFloatShares, cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))))` |
| knockout | `cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))` | -0.54 | -0.54 | -0.41 | +1.52 | `signedpower(cs_first_low40(LogFloatShares, signedpower(cs_quantile_q25(LogFloatShares))))` |
| knockout | `cs_quantile_q25(LogFloatShares)` | +1.32 | +1.38 | +1.32 | -0.34 | `signedpower(cs_first_low40(LogFloatShares, signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))))` |
| swap | `Volume->Amt` | -3.50 | -1.51 | -3.50 | — | `signedpower(cs_first_low40(LogFloatShares, signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Amt)))))` |

### head score +0.99:`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20))` | -3.53 | -2.21 | -3.53 | — | (子树本身) |
| sufficiency | `cs_rank(cross_mean(day_centroid(Volume), 30))` | +1.73 | +1.73 | +1.88 | — | (子树本身) |
| sufficiency | `ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)` | -3.53 | -2.21 | -3.53 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Volume), 30)` | +1.73 | +1.73 | +1.88 | — | (子树本身) |
| knockout | `cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20))` | +1.90 | +1.90 | +2.08 | -0.92 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20))` |
| knockout | `cs_rank(cross_mean(day_centroid(Volume), 30))` | -1.68 | -1.68 | -1.00 | +2.67 | `sub(cross_mean(day_centroid(Volume), 30), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))` |
| knockout | `ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)` | +0.92 | +0.92 | +1.03 | +0.07 | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(ts_autocorr_s1(day_argmax(Vwap), 10)))` |
| knockout | `cross_mean(day_centroid(Volume), 30)` | +0.64 | +0.84 | +0.64 | +0.34 | `sub(cs_rank(day_centroid(Volume)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))` |
| swap | `Volume->Amt` | +1.02 | +1.02 | +1.23 | — | `sub(cs_rank(cross_mean(day_centroid(Amt), 30)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))` |
| swap | `Vwap->Close` | +1.02 | +1.02 | +1.03 | — | `sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Close), 10), 20)))` |
| window | `cross_mean@30->15` | +1.09 | +1.31 | +1.09 | — | `sub(cs_rank(cross_mean(day_centroid(Volume), 15)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))` |
| window | `cross_mean@30->60` | -0.44 | +0.78 | -0.44 | — | `sub(cs_rank(cross_mean(day_centroid(Volume), 60)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_rank(cross_mean(day_centroid(Volume), 30))` — ablation,自身 score +1.73(所在 head +1.57)
2. `cross_mean(day_centroid(Volume), 30)` — ablation,自身 score +1.73(所在 head +1.57)
3. `cs_first_low40(abs_(LogFloatShares), day_std(Volume))` — ablation,自身 score +1.43(所在 head +1.43)
4. `signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume)))` — ablation,自身 score +1.38(所在 head +0.99)
5. `cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))` — ablation,自身 score +1.38(所在 head +0.99)
6. `cs_first_low40(LogFloatShares, signedpower(cs_first_low40(cs_quantile_q25(LogFloatShares), day_std(Volume))))` — ablation,自身 score +0.99(所在 head +0.99)
7. `signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))` — enrichment,均值差 +1.98,p 0.001
8. `cs_first_low40(LogFloatShares, day_std(Volume))` — enrichment,均值差 +1.95,p 0.000
9. `cs_first_low40(day_std(Volume), day_std(Volume))` — enrichment,均值差 +1.94,p 0.001
10. `day_centroid(Volume)` — enrichment,均值差 +1.42,p 0.000
11. `day_std(Volume)` — enrichment,均值差 +1.26,p 0.000
12. `abs_(LogFloatShares)` — enrichment,均值差 +1.18,p 0.001
13. `cross_mean(day_gini(Volume), 30)` — enrichment,均值差 +1.12,p 0.001
14. `ts_autocorr_s1(day_argmax(Vwap), 20)` — enrichment,均值差 +0.96,p 0.053
15. `cs_rank(cross_mean(day_gini(Volume), 30))` — enrichment,均值差 +0.90,p 0.007
16. `cs_bucket_zscore(LogFloatShares, day_std(Volume))` — enrichment,均值差 +0.86,p 0.094
17. `day_gini(Volume)` — enrichment,均值差 +0.83,p 0.003
18. `day_var(in_skew_full(Volume))` — enrichment,均值差 +0.59,p 0.085
19. `day_var(in_mean_full(Volume))` — enrichment,均值差 +0.57,p 0.036
20. `pow_2(day_std(Volume))` — enrichment,均值差 +0.37,p 0.068

## 本组之前各轮的任务

- `prods907Pr1a_Na`:核心 `—`;评分 83,过线 1,入 heads 1;采样计数 {}
  - score +0.51(train +0.51 valid +1.35):`div(day_last(Close), div(ts_cov(day_durbin_watson(Close), day_distinct_ratio(Close), 50), FloatShares))`
  - score -0.13(train -0.13 valid +1.20):`ts_cov(day_durbin_watson(Close), day_durbin_watson(Close), 50)`
  - score -0.18(train -0.09 valid -0.18):`div(day_last(Close), div(FloatCap, FloatShares))`
  - score -0.19(train -0.19 valid -0.03):`cs_bucket_rank(div(day_last(Close), div(FloatCap, FloatShares)), LogFloatCap)`
  - score -0.21(train -0.21 valid +0.61):`sqrt(cross_ema(cs_last_low05(day_kurt(Ret), day_close(High)), 30))`
- `prods907Pr1b_Nb`:核心 `—`;评分 89,过线 14,入 heads 5;采样计数 {}
  - score +1.57(train +1.71 valid +1.57):`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cross_mean(day_gini(Volume), 30))`
  - score +1.17(train +1.17 valid +1.43):`sub(cs_rank(cross_mean(cross_mean(day_centroid(Volume), 30), 30)), cross_mean(day_gini(Volume), 30))`
  - score +0.99(train +0.99 valid +1.25):`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(ts_hurst(ts_autocorr_s1(day_argmax(Vwap), 10), 20)))`
  - score +0.96(train +1.65 valid +0.96):`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cs_rank(cross_mean(day_gini(Amt), 30))))`
  - score +0.96(train +1.65 valid +0.96):`sub(cs_rank(cross_mean(day_centroid(Volume), 30)), cs_rank(cross_mean(day_gini(Amt), 30)))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.34(knockout cs_quantile_q25(LogFloatShares)):`signedpower(cs_first_low40(LogFloatShares, signedpower(cs_first_low40(LogFloatShares, day_std(Volume)))))`
