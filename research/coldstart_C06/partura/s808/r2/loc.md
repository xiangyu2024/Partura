# 定位:种子 808,C 组,第 2 轮(只含 train / valid)

快照:c05s808M1_I0_open_search, c05s808M2_I0_open_search, c06s808Cr1a_Na, c06s808Cr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.45 | +1.47 | +1.45 | +1 | 20 | c05s808M2_I0_open_search | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)` |
| +0.82 | +0.82 | +1.36 | -1 | 5 | c05s808M2_I0_open_search | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)` |
| +0.79 | +0.85 | +0.79 | +1 | 0 | c06s808Cr1a_Na | `sub(LogFloatShares, day_flat_run_max(Open))` |
| +0.74 | +0.74 | +0.76 | -1 | 0 | c05s808M2_I0_open_search | `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)` |
| +0.57 | +0.57 | +0.90 | +1 | 20 | c06s808Cr1b_Nb | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 15)` |
| +0.56 | +0.74 | +0.56 | -1 | 0 | c05s808M2_I0_open_search | `ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), LogFloatCap), 40)), 40)` |

## 共性:293 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.63 | 0.000 | 6 | +1.04 / -0.60 | `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` |
| +1.37 | 0.000 | 11 | +0.75 / -0.61 | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` |
| +1.29 | 0.000 | 14 | +0.66 / -0.62 | `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` |
| +1.27 | 0.034 | 4 | +0.69 / -0.58 | `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` |
| +1.15 | 0.000 | 14 | +0.53 / -0.62 | `cross_tail_mean_q75(LogFloatShares, 15)` |
| +1.14 | 0.000 | 11 | +0.54 / -0.61 | `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)` |
| +1.10 | 0.003 | 5 | +0.52 / -0.58 | `cross_mean(LogFloatShares, 15)` |
| +1.09 | 0.004 | 14 | +0.48 / -0.61 | `inv(LogFloatShares)` |
| +1.07 | 0.015 | 5 | +0.49 / -0.58 | `ts_decay_linear(LogFloatShares, 50)` |
| +1.06 | 0.056 | 4 | +0.48 / -0.58 | `abs_(LogFloatShares)` |
| +1.06 | 0.060 | 4 | +0.48 / -0.58 | `log(LogFloatShares)` |
| +1.05 | 0.137 | 4 | +0.47 / -0.58 | `log(inv(LogFloatShares))` |
| +1.05 | 0.152 | 5 | +0.47 / -0.58 | `ts_max(LogFloatShares, 50)` |
| +1.05 | 0.150 | 4 | +0.47 / -0.58 | `pow_2(LogFloatShares)` |
| +0.91 | 0.008 | 9 | +0.32 / -0.59 | `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` |
| +0.86 | 0.004 | 34 | +0.20 / -0.66 | `day_distinct_ratio(Ret)` |
| +0.79 | 0.015 | 18 | +0.18 / -0.61 | `cs_last_high05(LogFloatCap, LogFloatCap)` |
| +0.38 | 0.685 | 7 | -0.19 / -0.57 | `cs_last_high05(day_distinct_ratio(Ret), LogFloatCap)` |
| +0.34 | 0.674 | 5 | -0.23 / -0.57 | `sub(LogFloatCap, LogFloatShares)` |
| +0.28 | 0.673 | 4 | -0.29 / -0.57 | `cs_bucket_rank(sub(LogFloatCap, LogFloatShares), LogFloatCap)` |

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

### head score +0.79:`sub(LogFloatShares, day_flat_run_max(Open))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_flat_run_max(Open)` | — | — | — | — | 门槛废品 |
| swap | `Open->Close` | +0.83 | +0.84 | +0.83 | — | `sub(LogFloatShares, day_flat_run_max(Close))` |

### head score +0.74:`ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` | +0.58 | +1.10 | +0.58 | — | (子树本身) |
| sufficiency | `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` | +0.40 | +1.40 | +0.40 | — | (子树本身) |
| sufficiency | `cs_last_high05(LogFloatCap, LogFloatCap)` | +0.19 | +1.19 | +0.19 | — | (子树本身) |
| knockout | `cs_last_high05(LogFloatCap, LogFloatCap)` | -0.03 | -0.03 | +0.40 | +0.77 | `ts_max(ts_max(ts_max(LogFloatCap, 40), 40), 40)` |
| window | `ts_max@40->20` | +0.71 | +0.98 | +0.71 | — | `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 20)` |
| window | `ts_max@40->80` | +0.35 | +0.35 | +0.75 | — | `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40)` — ablation,自身 score +1.17(所在 head +1.45)
2. `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` — ablation,自身 score +0.58(所在 head +0.82)
3. `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` — ablation,自身 score +0.58(所在 head +0.74)
4. `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` — enrichment,均值差 +1.63,p 0.000
5. `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` — enrichment,均值差 +1.29,p 0.000
6. `cross_tail_mean_q75(LogFloatShares, 15)` — enrichment,均值差 +1.15,p 0.000
7. `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)` — enrichment,均值差 +1.14,p 0.000
8. `cross_mean(LogFloatShares, 15)` — enrichment,均值差 +1.10,p 0.003
9. `inv(LogFloatShares)` — enrichment,均值差 +1.09,p 0.004
10. `ts_decay_linear(LogFloatShares, 50)` — enrichment,均值差 +1.07,p 0.015
11. `abs_(LogFloatShares)` — enrichment,均值差 +1.06,p 0.056
12. `log(LogFloatShares)` — enrichment,均值差 +1.06,p 0.060
13. `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` — enrichment,均值差 +0.91,p 0.008
14. `day_distinct_ratio(Ret)` — enrichment,均值差 +0.86,p 0.004
15. `cs_last_high05(LogFloatCap, LogFloatCap)` — enrichment,均值差 +0.79,p 0.015

## 本组之前各轮的任务

- `c06s808Cr1a_Na`:核心 `—`;评分 77,过线 9,入 heads 1;采样计数 {}
  - score +0.79(train +0.85 valid +0.79):`sub(LogFloatShares, day_flat_run_max(Open))`
  - score +0.60(train +0.60 valid +0.87):`cross_sum(div(LogFloatShares, 5), 5)`
  - score +0.60(train +0.60 valid +0.87):`cross_sum(div(LogFloatShares, 1), 5)`
  - score +0.60(train +0.60 valid +0.87):`cross_sum(mul(LogFloatShares, 1), 5)`
  - score +0.60(train +0.60 valid +0.89):`cross_sum(sub(LogFloatShares, 5), 5)`
- `c06s808Cr1b_Nb`:核心 `—`;评分 67,过线 21,入 heads 1;采样计数 {}
  - score +0.57(train +0.57 valid +0.90):`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 15)`
  - score +0.56(train +0.56 valid +0.79):`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241), 15)`
  - score +0.55(train +0.55 valid +0.81):`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_mean(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 15), 241), 15)`
  - score +0.55(train +0.55 valid +0.78):`cross_mean(cross_quantile_q50(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 60), 15)`
  - score +0.55(train +0.55 valid +0.86):`cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241), 15), 241)`

## 比原 head 好的拆解变体(R 候选)

(没有)
