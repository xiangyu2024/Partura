# 定位:种子 905,P 组,第 2 轮(只含 train / valid)

快照:prods905M1_I0_open_search, prods905M2_I0_open_search, prods905Pr1a_Na, prods905Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(2 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.80 | +1.48 | +0.80 | -1 | 20 | prods905Pr1b_Nb | `pow_2_5(cross_mean(day_centroid(Amt), 3))` |
| +0.66 | +0.66 | +0.78 | -1 | 20 | prods905Pr1b_Nb | `cross_zscore(cross_mean(day_centroid(Amt), 20), 120)` |

## 共性:312 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.50 | 0.001 | 4 | +0.28 / -1.22 | `pow_2_5(day_centroid(Volume))` |
| +1.33 | 0.000 | 8 | +0.09 / -1.24 | `day_centroid(Amt)` |
| +1.32 | 0.000 | 8 | +0.09 / -1.24 | `day_centroid(Volume)` |
| +0.76 | 0.023 | 6 | -0.46 / -1.22 | `cross_valid_count(day_argmax(Low), 30)` |
| +0.73 | 0.000 | 14 | -0.50 / -1.23 | `cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap)))` |
| +0.72 | 0.000 | 20 | -0.53 / -1.25 | `cs_rank(sub(LogTotalCap, LogFloatCap))` |
| +0.70 | 0.004 | 26 | -0.56 / -1.26 | `pow_2(LogFloatShares)` |
| +0.68 | 0.007 | 15 | -0.55 / -1.23 | `inv(LogFloatShares)` |
| +0.68 | 0.000 | 23 | -0.57 / -1.25 | `sub(LogTotalCap, LogFloatCap)` |
| +0.67 | 0.065 | 5 | -0.54 / -1.21 | `cs_rank(cross_valid_count(day_argmax(Low), 30))` |
| +0.67 | 0.027 | 12 | -0.56 / -1.23 | `pow_3(pow_2(LogFloatShares))` |
| +0.66 | 0.068 | 7 | -0.56 / -1.22 | `ts_quantile_q50(inv(LogFloatShares), 30)` |
| +0.66 | 0.084 | 6 | -0.55 / -1.21 | `pow_3(pow_3(pow_2(LogFloatShares)))` |
| +0.66 | 0.110 | 4 | -0.55 / -1.21 | `pow_3(LogFloatShares)` |
| +0.66 | 0.173 | 11 | -0.57 / -1.23 | `cross_min(LogFloatShares, 30)` |
| +0.65 | 0.006 | 13 | -0.57 / -1.23 | `day_zero_ratio(Volume)` |
| +0.65 | 0.192 | 4 | -0.56 / -1.21 | `ts_quantile_q50(pow_2(LogFloatShares), 30)` |
| +0.64 | 0.287 | 4 | -0.57 / -1.21 | `pow_2(cross_min(LogFloatShares, 30))` |
| +0.61 | 0.028 | 11 | -0.61 / -1.22 | `signedpower(day_zero_ratio(Volume))` |
| +0.56 | 0.056 | 12 | -0.67 / -1.22 | `day_var(Vwap)` |

## 拆解(12 次评估)

### head score +0.80:`pow_2_5(cross_mean(day_centroid(Amt), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_centroid(Amt), 3)` | +0.80 | +1.48 | +0.80 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `cross_mean(day_centroid(Amt), 3)` | +0.41 | +1.05 | +0.41 | +0.39 | `pow_2_5(day_centroid(Amt))` |
| swap | `Amt->Volume` | +0.76 | +1.43 | +0.76 | — | `pow_2_5(cross_mean(day_centroid(Volume), 3))` |
| window | `cross_mean@3->2` | +0.69 | +1.30 | +0.69 | — | `pow_2_5(cross_mean(day_centroid(Amt), 2))` |
| window | `cross_mean@3->6` | +0.85 | +1.60 | +0.85 | — | `pow_2_5(cross_mean(day_centroid(Amt), 6))` |

### head score +0.66:`cross_zscore(cross_mean(day_centroid(Amt), 20), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `cross_mean(day_centroid(Amt), 20)` | -1.16 | -1.16 | -0.21 | +1.82 | `cross_zscore(day_centroid(Amt), 120)` |
| swap | `Amt->Volume` | +0.60 | +0.60 | +0.77 | — | `cross_zscore(cross_mean(day_centroid(Volume), 20), 120)` |
| window | `cross_zscore@120->60` | +0.09 | +0.09 | +0.73 | — | `cross_zscore(cross_mean(day_centroid(Amt), 20), 60)` |
| window | `cross_zscore@120->240` | +0.90 | +1.26 | +0.90 | — | `cross_zscore(cross_mean(day_centroid(Amt), 20), 240)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(day_centroid(Amt), 20)` — ablation,自身 score +1.34(所在 head +0.66)
2. `cross_mean(day_centroid(Amt), 3)` — ablation,自身 score +0.80(所在 head +0.80)
3. `pow_2_5(day_centroid(Volume))` — enrichment,均值差 +1.50,p 0.001
4. `day_centroid(Amt)` — enrichment,均值差 +1.33,p 0.000
5. `day_centroid(Volume)` — enrichment,均值差 +1.32,p 0.000
6. `cross_valid_count(day_argmax(Low), 30)` — enrichment,均值差 +0.76,p 0.023
7. `cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap)))` — enrichment,均值差 +0.73,p 0.000
8. `cs_rank(sub(LogTotalCap, LogFloatCap))` — enrichment,均值差 +0.72,p 0.000
9. `pow_2(LogFloatShares)` — enrichment,均值差 +0.70,p 0.004
10. `inv(LogFloatShares)` — enrichment,均值差 +0.68,p 0.007
11. `sub(LogTotalCap, LogFloatCap)` — enrichment,均值差 +0.68,p 0.000
12. `cs_rank(cross_valid_count(day_argmax(Low), 30))` — enrichment,均值差 +0.67,p 0.065
13. `pow_3(pow_2(LogFloatShares))` — enrichment,均值差 +0.67,p 0.027
14. `ts_quantile_q50(inv(LogFloatShares), 30)` — enrichment,均值差 +0.66,p 0.068
15. `pow_3(pow_3(pow_2(LogFloatShares)))` — enrichment,均值差 +0.66,p 0.084
16. `day_zero_ratio(Volume)` — enrichment,均值差 +0.65,p 0.006
17. `signedpower(day_zero_ratio(Volume))` — enrichment,均值差 +0.61,p 0.028
18. `day_var(Vwap)` — enrichment,均值差 +0.56,p 0.056
19. `ts_skew(day_flat_run_max(High), 50)` — enrichment,均值差 +0.51,p 0.051
20. `day_flat_run_max(High)` — enrichment,均值差 +0.49,p 0.046
21. `day_argmax(Low)` — enrichment,均值差 +0.43,p 0.046

## 本组之前各轮的任务

- `prods905Pr1a_Na`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {}
  - score -0.35(train -0.35 valid +0.37):`sub(LogTotalCap, LogFloatCap)`
  - score -0.40(train -0.40 valid +0.53):`add(cs_rank(sub(cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap))), LogFloatShares)), cs_rank(sub(LogTotalCap, LogFloatCap)))`
  - score -0.42(train -0.42 valid +0.16):`add(ts_quantile_q75(sub(LogTotalCap, LogFloatCap), 50), cs_rank(ts_quantile_q75(sub(LogTotalCap, LogFloatCap), 50)))`
  - score -0.48(train -0.48 valid +0.15):`add(cs_median(sub(LogFloatCap, LogFloatShares)), cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap))))`
  - score -0.48(train -0.48 valid +0.15):`add(cs_median(add(LogFloatCap, cs_rank(sub(LogTotalCap, LogFloatCap)))), cs_rank(cs_rank(sub(LogTotalCap, LogFloatCap))))`
- `prods905Pr1b_Nb`:核心 `—`;评分 87,过线 3,入 heads 2;采样计数 {}
  - score +0.80(train +1.48 valid +0.80):`pow_2_5(cross_mean(day_centroid(Amt), 3))`
  - score +0.66(train +0.66 valid +0.78):`cross_zscore(cross_mean(day_centroid(Amt), 20), 120)`
  - score +0.61(train +0.61 valid +0.76):`cross_zscore(cross_mean(day_centroid(Volume), 20), 120)`
  - score +0.48(train +0.48 valid +0.75):`cross_zscore(cross_mean(day_centroid(Amt), 10), 120)`
  - score +0.44(train +1.09 valid +0.44):`pow_2_5(day_centroid(Volume))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(window cross_zscore@120->240):`cross_zscore(cross_mean(day_centroid(Amt), 20), 240)`
