# 定位:种子 808,B 组,第 2 轮(只含 train / valid)

快照:c05s808M1_I0_open_search, c05s808M2_I0_open_search, c05s808Br1a_Ea, c05s808Br1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.45 | +1.47 | +1.45 | +1 | 20 | c05s808M2_I0_open_search | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)` |
| +0.82 | +0.82 | +1.36 | -1 | 5 | c05s808M2_I0_open_search | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)` |
| +0.74 | +0.74 | +0.76 | -1 | 0 | c05s808M2_I0_open_search | `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)` |
| +0.61 | +0.61 | +0.95 | +1 | 20 | c05s808Br1a_Ea | `div(LogFloatCap, inv(LogFloatShares))` |
| +0.56 | +0.74 | +0.56 | -1 | 0 | c05s808M2_I0_open_search | `ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), LogFloatCap), 40)), 40)` |
| +0.56 | +0.56 | +0.79 | +1 | 5 | c05s808Br1b_Nb | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241), 15)` |

## 共性:320 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.60 | 0.000 | 6 | +1.04 / -0.56 | `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` |
| +1.33 | 0.000 | 11 | +0.75 / -0.57 | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` |
| +1.25 | 0.000 | 14 | +0.66 / -0.58 | `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` |
| +1.23 | 0.038 | 4 | +0.69 / -0.54 | `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` |
| +1.13 | 0.000 | 26 | +0.51 / -0.62 | `cross_tail_mean_q75(LogFloatShares, 15)` |
| +1.09 | 0.000 | 10 | +0.53 / -0.56 | `cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15)` |
| +1.08 | 0.001 | 6 | +0.53 / -0.55 | `cross_quantile_q50(cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15), 241)` |
| +1.08 | 0.000 | 14 | +0.50 / -0.57 | `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)` |
| +1.08 | 0.001 | 6 | +0.53 / -0.55 | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15)` |
| +1.05 | 0.018 | 4 | +0.51 / -0.54 | `cross_mean(LogFloatShares, 15)` |
| +1.05 | 0.004 | 8 | +0.50 / -0.55 | `sqrt(inv(LogFloatShares))` |
| +1.03 | 0.027 | 5 | +0.49 / -0.54 | `ts_decay_linear(LogFloatShares, 50)` |
| +1.02 | 0.090 | 4 | +0.48 / -0.54 | `abs_(LogFloatShares)` |
| +1.02 | 0.104 | 4 | +0.48 / -0.54 | `log(LogFloatShares)` |
| +1.01 | 0.221 | 4 | +0.47 / -0.54 | `log(inv(LogFloatShares))` |
| +1.01 | 0.244 | 4 | +0.47 / -0.54 | `pow_2(LogFloatShares)` |
| +1.01 | 0.269 | 5 | +0.47 / -0.54 | `ts_max(LogFloatShares, 50)` |
| +0.98 | 0.016 | 4 | +0.44 / -0.54 | `cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15)` |
| +0.87 | 0.007 | 9 | +0.32 / -0.55 | `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` |
| +0.81 | 0.001 | 9 | +0.26 / -0.55 | `div(LogFloatCap, inv(LogFloatShares))` |

## 拆解(23 次评估)

### head score +1.45:`ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)` | +1.17 | +1.17 | +2.01 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` | +0.58 | +0.58 | +0.90 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` | — | — | — | — | 门槛废品 |
| knockout | `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` | — | — | — | — | `ts_max(ts_max(day_distinct_ratio(Ret), 40), 40)` |
| knockout | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` | +0.35 | +0.91 | +0.35 | +1.10 | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)), 40), 40)` |
| knockout | `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` | -0.73 | -0.25 | -0.73 | +2.19 | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(day_distinct_ratio(Ret), 40)), 40), 40)` |
| window | `ts_max@40->20` | +1.27 | +1.27 | +1.71 | — | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 20)` |
| window | `ts_max@40->80` | +1.16 | +1.66 | +1.16 | — | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 80)` |

### head score +0.82:`ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` | +0.58 | +0.58 | +0.90 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_distinct_ratio(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` | — | — | — | — | `ts_max(ts_max(day_distinct_ratio(Ret), 40), 40)` |
| window | `ts_max@40->20` | +0.79 | +0.79 | +1.17 | — | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 20)` |
| window | `ts_max@40->80` | +0.86 | +0.86 | +1.71 | — | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 80)` |

### head score +0.74:`ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` | +0.58 | +1.10 | +0.58 | — | (子树本身) |
| sufficiency | `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` | +0.40 | +1.40 | +0.40 | — | (子树本身) |
| sufficiency | `cs_last_high05(LogFloatCap, LogFloatCap)` | +0.19 | +1.19 | +0.19 | — | (子树本身) |
| knockout | `cs_last_high05(LogFloatCap, LogFloatCap)` | -0.03 | -0.03 | +0.40 | +0.77 | `ts_max(ts_max(ts_max(LogFloatCap, 40), 40), 40)` |
| window | `ts_max@40->20` | +0.71 | +0.98 | +0.71 | — | `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 20)` |
| window | `ts_max@40->80` | +0.35 | +0.35 | +0.75 | — | `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 80)` |

### head score +0.61:`div(LogFloatCap, inv(LogFloatShares))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `inv(LogFloatShares)` | +0.48 | +0.48 | +0.77 | — | (子树本身) |
| knockout | `inv(LogFloatShares)` | -2.00 | -0.15 | -2.00 | +2.61 | `div(LogFloatCap, LogFloatShares)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)` — ablation,自身 score +1.17(所在 head +1.45)
2. `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` — ablation,自身 score +0.58(所在 head +0.82)
3. `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` — ablation,自身 score +0.58(所在 head +0.74)
4. `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` — enrichment,均值差 +1.60,p 0.000
5. `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` — enrichment,均值差 +1.25,p 0.000
6. `cross_tail_mean_q75(LogFloatShares, 15)` — enrichment,均值差 +1.13,p 0.000
7. `cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15)` — enrichment,均值差 +1.09,p 0.000
8. `cross_quantile_q50(cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15), 241)` — enrichment,均值差 +1.08,p 0.001
9. `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)` — enrichment,均值差 +1.08,p 0.000
10. `cross_mean(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15)` — enrichment,均值差 +1.08,p 0.001
11. `cross_mean(LogFloatShares, 15)` — enrichment,均值差 +1.05,p 0.018
12. `sqrt(inv(LogFloatShares))` — enrichment,均值差 +1.05,p 0.004
13. `ts_decay_linear(LogFloatShares, 50)` — enrichment,均值差 +1.03,p 0.027
14. `abs_(LogFloatShares)` — enrichment,均值差 +1.02,p 0.090
15. `cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15)` — enrichment,均值差 +0.98,p 0.016
16. `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` — enrichment,均值差 +0.87,p 0.007
17. `div(LogFloatCap, inv(LogFloatShares))` — enrichment,均值差 +0.81,p 0.001
18. `day_distinct_ratio(Ret)` — enrichment,均值差 +0.81,p 0.005
19. `cs_last_high05(LogFloatCap, LogFloatCap)` — enrichment,均值差 +0.75,p 0.017
20. `sqrt(div(LogFloatCap, inv(LogFloatShares)))` — enrichment,均值差 +0.47,p 0.038
21. `inv(LogFloatShares)` — enrichment,均值差 +0.43,p 0.021

## 本组之前各轮的任务

- `c05s808Br1a_Ea`:核心 `inv(LogFloatShares)`;评分 84,过线 9,入 heads 1;采样计数 {'c05_no_core': 1289, 'c05_periphery_seen': 13}
  - score +0.61(train +0.61 valid +0.95):`div(LogFloatCap, inv(LogFloatShares))`
  - score +0.60(train +0.60 valid +0.86):`ts_mean(inv(sqrt(div(LogFloatCap, inv(LogFloatShares)))), 20)`
  - score +0.60(train +0.60 valid +0.86):`ts_mean(sqrt(div(LogFloatCap, inv(LogFloatShares))), 20)`
  - score +0.60(train +0.60 valid +0.79):`sqrt(inv(ts_mean(inv(sqrt(div(LogFloatCap, inv(LogFloatShares)))), 1)))`
  - score +0.59(train +0.59 valid +0.98):`div(LogFloatCap, inv(div(LogFloatCap, inv(LogFloatShares))))`
- `c05s808Br1b_Nb`:核心 `—`;评分 84,过线 31,入 heads 1;采样计数 {}
  - score +0.56(train +0.56 valid +0.79):`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241), 15)`
  - score +0.55(train +0.55 valid +0.79):`cross_mean(cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_mean(LogFloatShares, 15), 15), 241), 15), 15)`
  - score +0.55(train +0.55 valid +0.81):`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(cross_tail_mean_q75(LogFloatShares, 15), 15), 241), 15), 241), 15)`
  - score +0.55(train +0.55 valid +0.81):`cross_quantile_q50(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 241)`
  - score +0.55(train +0.55 valid +0.81):`cross_mean(cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241), 15), 15)`

## 比原 head 好的拆解变体(R 候选)

(没有)
