# 定位:种子 901,P 组,第 3 轮(只含 train / valid)

快照:prods901M1_I0_open_search, prods901M2_I0_open_search, prods901M3_I0_open_search, prods901Pr1a_Ea, prods901Pr1b_Nb, prods901Pr2a_Ea, prods901Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.63 | +1.63 | +1.79 | -1 | 5 | prods901Pr2b_Nb | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), sub(sub(LogFloatCap, LogFloatShares), LogFloatShares))` |
| +1.56 | +1.78 | +1.56 | -1 | 5 | prods901Pr2b_Nb | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares)` |
| +1.09 | +1.09 | +1.61 | -1 | 20 | prods901Pr2b_Nb | `cs_bucket_zscore(cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), 20), LogFloatShares)` |
| +0.82 | +1.17 | +0.82 | -1 | 5 | prods901Pr2a_Ea | `ts_stddev(signedpower(day_argmax(Amt)), 40)` |
| +0.69 | +0.69 | +1.42 | -1 | 20 | prods901Pr2a_Ea | `cs_bucket_rank(cross_mean(day_argmax(Amt), 20), day_max(Close))` |
| +0.64 | +0.64 | +1.47 | -1 | 20 | prods901Pr2b_Nb | `cs_last_high40(cross_mean(cross_mean(day_centroid(Amt), 5), 5), LogFloatShares)` |

## 共性:503 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.19 | 0.001 | 4 | +1.00 / -1.19 | `cross_mean(cross_mean(day_centroid(Amt), 5), 5)` |
| +1.65 | 0.000 | 13 | +0.44 / -1.22 | `cross_mean(day_centroid(Amt), 5)` |
| +1.47 | 0.000 | 15 | +0.25 / -1.22 | `cross_mean(day_centroid(Amt), 20)` |
| +1.46 | 0.000 | 33 | +0.19 / -1.27 | `day_centroid(Amt)` |
| +1.28 | 0.009 | 8 | +0.09 / -1.20 | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` |
| +1.26 | 0.001 | 13 | +0.05 / -1.21 | `day_sum(Amt)` |
| +1.22 | 0.010 | 10 | +0.02 / -1.20 | `day_sum(in_slice(Amt, 211, 240))` |
| +1.20 | 0.027 | 7 | +0.01 / -1.19 | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| +1.16 | 0.007 | 4 | -0.02 / -1.18 | `cs_mask_top_replace_mean_neg(day_median(Close))` |
| +1.05 | 0.057 | 4 | -0.14 / -1.18 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares)` |
| +0.83 | 0.010 | 13 | -0.36 / -1.20 | `sub(LogFloatCap, LogFloatShares)` |
| +0.83 | 0.047 | 7 | -0.36 / -1.19 | `day_var(High)` |
| +0.72 | 0.038 | 4 | -0.46 / -1.18 | `cross_semistd_neg(day_last(Close), 60)` |
| +0.72 | 0.038 | 4 | -0.46 / -1.18 | `cross_semistd_pos(day_last(Close), 60)` |
| +0.72 | 0.038 | 4 | -0.46 / -1.18 | `sub(cross_semistd_pos(day_last(Close), 60), cross_semistd_neg(day_last(Close), 60))` |
| +0.67 | 0.036 | 8 | -0.52 / -1.19 | `sub(day_hurst(High), LogFloatShares)` |
| +0.63 | 0.080 | 4 | -0.55 / -1.18 | `cross_sum(ts_quantile_q25(day_at_max_ratio(Amt), 40), 30)` |
| +0.62 | 0.012 | 16 | -0.57 / -1.19 | `signedpower(day_argmax(Amt))` |
| +0.60 | 0.113 | 4 | -0.58 / -1.18 | `cross_sum(day_at_max_ratio(Amt), 30)` |
| +0.59 | 0.006 | 23 | -0.61 / -1.20 | `cross_mean(day_argmax(Amt), 20)` |

## 拆解(35 次评估)

### head score +1.63:`cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), sub(sub(LogFloatCap, LogFloatShares), LogFloatShares))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `sub(sub(LogFloatCap, LogFloatShares), LogFloatShares)` | -2.07 | -0.55 | -2.07 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| sufficiency | `sub(LogFloatCap, LogFloatShares)` | -2.30 | -0.77 | -2.30 | — | (子树本身) |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +0.52 | +1.36 | +0.52 | +1.11 | `cs_bucket_zscore(day_centroid(Amt), sub(sub(LogFloatCap, LogFloatShares), LogFloatShares))` |
| knockout | `sub(sub(LogFloatCap, LogFloatShares), LogFloatShares)` | +1.34 | +1.72 | +1.34 | +0.29 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), sub(LogFloatCap, LogFloatShares))` |
| swap | `Amt->Volume` | +1.63 | +1.63 | +1.84 | — | `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), sub(sub(LogFloatCap, LogFloatShares), LogFloatShares))` |
| window | `cross_mean@20->10` | +1.03 | +1.91 | +1.03 | — | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 10), sub(sub(LogFloatCap, LogFloatShares), LogFloatShares))` |
| window | `cross_mean@20->40` | +1.54 | +1.54 | +1.94 | — | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 40), sub(sub(LogFloatCap, LogFloatShares), LogFloatShares))` |

### head score +1.56:`cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` | +1.81 | +1.94 | +1.81 | — | (子树本身) |
| sufficiency | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` | +0.28 | +0.98 | +0.28 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Amt, 211, 240))` | -1.92 | -1.92 | -1.76 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` | -0.17 | +0.93 | -0.17 | +1.73 | `cs_bucket_zscore(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), LogFloatShares)` |
| knockout | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` | -0.94 | -0.94 | -0.71 | +2.51 | `cs_bucket_zscore(cross_mean(day_sum(in_slice(Amt, 211, 240)), 20), LogFloatShares)` |
| swap | `Amt->Volume` | +1.56 | +1.80 | +1.56 | — | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Volume, 211, 240)), day_sum(Volume)), 20), LogFloatShares)` |
| window | `cross_mean@20->10` | +0.48 | +1.56 | +0.48 | — | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 10), LogFloatShares)` |
| window | `cross_mean@20->40` | +1.25 | +1.25 | +1.72 | — | `cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 40), LogFloatShares)` |

### head score +1.09:`cs_bucket_zscore(cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), 20), LogFloatShares)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), 20)` | +1.41 | +1.41 | +2.80 | — | (子树本身) |
| sufficiency | `div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt))` | +1.64 | +1.64 | +2.47 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares)` | +1.17 | +1.73 | +1.17 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Amt), 5)` | +0.90 | +1.64 | +0.90 | — | (子树本身) |
| knockout | `cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), 20)` | +1.29 | +1.29 | +1.77 | -0.21 | `cs_bucket_zscore(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), LogFloatShares)` |
| knockout | `div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt))` | +1.49 | +1.49 | +1.73 | -0.40 | `cs_bucket_zscore(cross_mean(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), 20), LogFloatShares)` |
| knockout | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares)` | -2.87 | -1.21 | -2.87 | +3.95 | `cs_bucket_zscore(cross_mean(div(cross_mean(day_centroid(Amt), 5), day_sum(Amt)), 20), LogFloatShares)` |
| knockout | `cross_mean(day_centroid(Amt), 5)` | +1.14 | +1.14 | +1.62 | -0.05 | `cs_bucket_zscore(cross_mean(div(cs_bucket_zscore(day_centroid(Amt), LogFloatShares), day_sum(Amt)), 20), LogFloatShares)` |
| swap | `Amt->Volume` | +0.88 | +1.22 | +0.88 | — | `cs_bucket_zscore(cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Volume), 5), LogFloatShares), day_sum(Volume)), 20), LogFloatShares)` |
| window | `cross_mean@20->10` | +1.10 | +1.10 | +1.81 | — | `cs_bucket_zscore(cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), 10), LogFloatShares)` |
| window | `cross_mean@20->40` | +0.78 | +0.78 | +1.30 | — | `cs_bucket_zscore(cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), 40), LogFloatShares)` |

### head score +0.82:`ts_stddev(signedpower(day_argmax(Amt)), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `signedpower(day_argmax(Amt))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_argmax(Amt)` | — | — | — | — | 门槛废品 |
| knockout | `signedpower(day_argmax(Amt))` | -0.47 | +0.41 | -0.47 | +1.28 | `ts_stddev(day_argmax(Amt), 40)` |
| swap | `Amt->Volume` | +0.62 | +1.12 | +0.62 | — | `ts_stddev(signedpower(day_argmax(Volume)), 40)` |
| window | `ts_stddev@40->20` | +0.05 | +1.10 | +0.05 | — | `ts_stddev(signedpower(day_argmax(Amt)), 20)` |
| window | `ts_stddev@40->80` | -0.48 | +0.79 | -0.48 | — | `ts_stddev(signedpower(day_argmax(Amt)), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` — ablation,自身 score +1.81(所在 head +1.56)
2. `div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt))` — ablation,自身 score +1.64(所在 head +1.09)
3. `cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), 20)` — ablation,自身 score +1.41(所在 head +1.09)
4. `cross_mean(day_centroid(Amt), 20)` — ablation,自身 score +1.34(所在 head +1.63)
5. `cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares)` — ablation,自身 score +1.17(所在 head +1.09)
6. `cross_mean(day_centroid(Amt), 5)` — ablation,自身 score +0.90(所在 head +1.09)
7. `cross_mean(cross_mean(day_centroid(Amt), 5), 5)` — enrichment,均值差 +2.19,p 0.001
8. `day_centroid(Amt)` — enrichment,均值差 +1.46,p 0.000
9. `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` — enrichment,均值差 +1.28,p 0.009
10. `day_sum(Amt)` — enrichment,均值差 +1.26,p 0.001
11. `day_sum(in_slice(Amt, 211, 240))` — enrichment,均值差 +1.22,p 0.010
12. `cs_mask_top_replace_mean_neg(day_median(Close))` — enrichment,均值差 +1.16,p 0.007
13. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.83,p 0.010
14. `day_var(High)` — enrichment,均值差 +0.83,p 0.047
15. `cross_semistd_neg(day_last(Close), 60)` — enrichment,均值差 +0.72,p 0.038
16. `cross_semistd_pos(day_last(Close), 60)` — enrichment,均值差 +0.72,p 0.038
17. `sub(cross_semistd_pos(day_last(Close), 60), cross_semistd_neg(day_last(Close), 60))` — enrichment,均值差 +0.72,p 0.038
18. `sub(day_hurst(High), LogFloatShares)` — enrichment,均值差 +0.67,p 0.036
19. `cross_sum(ts_quantile_q25(day_at_max_ratio(Amt), 40), 30)` — enrichment,均值差 +0.63,p 0.080
20. `signedpower(day_argmax(Amt))` — enrichment,均值差 +0.62,p 0.012
21. `cross_mean(day_argmax(Amt), 20)` — enrichment,均值差 +0.59,p 0.006
22. `sub(day_wmean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +0.59,p 0.036
23. `day_argmax(Amt)` — enrichment,均值差 +0.57,p 0.000
24. `day_argmax(Volume)` — enrichment,均值差 +0.55,p 0.024
25. `day_wmean(Ret, Amt)` — enrichment,均值差 +0.54,p 0.025
26. `day_median(Close)` — enrichment,均值差 +0.53,p 0.099
27. `ts_quantile_q25(day_at_max_ratio(Amt), 40)` — enrichment,均值差 +0.53,p 0.014
28. `day_at_max_ratio(Amt)` — enrichment,均值差 +0.48,p 0.006
29. `cross_sum(LogFloatShares, 30)` — enrichment,均值差 +0.47,p 0.058
30. `cs_demean(day_last(Close))` — enrichment,均值差 +0.33,p 0.083

## 本组之前各轮的任务

- `prods901Pr1a_Ea`:核心 `day_last(Close)`;评分 79,过线 0,入 heads 0;采样计数 {'c05_no_core': 712, 'c05_periphery_seen': 3}
  - score +0.18(train +0.18 valid +0.62):`sub(log(day_last(Close)), sub(day_hurst(Close), LogFloatShares))`
  - score +0.16(train +0.16 valid +0.61):`sub(log(day_last(Close)), sub(day_hurst(High), LogFloatShares))`
  - score +0.13(train +0.13 valid +0.57):`sub(log(sub(log(day_last(Close)), sub(log(day_last(Close)), sub(day_hurst(High), LogFloatShares)))), sub(log(day_last(Close)), sub(day_hurst(High), LogFloatShares)))`
  - score +0.08(train +0.08 valid +0.55):`sub(log(day_last(Close)), sub(day_centroid(Vwap), LogFloatShares))`
  - score -0.06(train -0.06 valid +0.28):`sub(log(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares))), sub(LogFloatCap, LogFloatShares))`
- `prods901Pr1b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {}
  - score +0.11(train +0.11 valid +0.88):`cross_mean(sub(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 3), day_mean(Ret)), 120)`
  - score -0.01(train -0.01 valid +0.91):`cross_mean(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_mean(Ret)), 120)`
  - score -0.05(train -0.05 valid +1.14):`cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)`
  - score -0.06(train -0.00 valid -0.06):`cross_mean(sub(sub(div(day_last(Close), day_first(Open)), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 120)`
  - score -0.06(train +0.05 valid -0.06):`cross_mean(sub(sub(div(day_last(Close), day_first(Close)), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 120)`
- `prods901Pr2a_Ea`:核心 `day_argmax(Amt)`;评分 104,过线 6,入 heads 2;采样计数 {'c05_no_core': 1973, 'c05_periphery_seen': 9}
  - score +0.82(train +1.17 valid +0.82):`ts_stddev(signedpower(day_argmax(Amt)), 40)`
  - score +0.72(train +1.33 valid +0.72):`ts_stddev(signedpower(day_argmax(Amt)), 30)`
  - score +0.69(train +0.69 valid +1.42):`cs_bucket_rank(cross_mean(day_argmax(Amt), 20), day_max(Close))`
  - score +0.60(train +0.60 valid +0.69):`cs_bucket_rank(cross_mean(cs_bucket_rank(cross_mean(day_argmax(Amt), 20), day_var(High)), 20), day_var(High))`
  - score +0.60(train +0.60 valid +1.48):`cs_bucket_rank(cross_mean(day_argmax(Amt), 20), day_var(High))`
- `prods901Pr2b_Nb`:核心 `—`;评分 95,过线 27,入 heads 4;采样计数 {}
  - score +1.63(train +1.63 valid +1.79):`cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), sub(sub(LogFloatCap, LogFloatShares), LogFloatShares))`
  - score +1.57(train +1.69 valid +1.57):`cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)`
  - score +1.56(train +1.78 valid +1.56):`cs_bucket_zscore(cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20), LogFloatShares)`
  - score +1.51(train +1.51 valid +1.65):`cs_bucket_zscore(cross_mean(cross_mean(day_centroid(Amt), 20), 5), LogFloatShares)`
  - score +1.51(train +1.70 valid +1.51):`cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), sub(sub(day_centroid(Amt), LogFloatShares), LogFloatShares))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.40(knockout div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt))):`cs_bucket_zscore(cross_mean(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), 20), LogFloatShares)`
- 增益 +0.21(knockout cross_mean(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), 20)):`cs_bucket_zscore(div(cs_bucket_zscore(cross_mean(day_centroid(Amt), 5), LogFloatShares), day_sum(Amt)), LogFloatShares)`
