# 定位:种子 808,C 组,第 3 轮(只含 train / valid)

快照:c05s808M1_I0_open_search, c05s808M2_I0_open_search, c05s808M3_I0_open_search, c06s808Cr1a_Na, c06s808Cr1b_Nb, c06s808Cr2a_Ea, c06s808Cr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(8 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.45 | +1.47 | +1.45 | +1 | 20 | c05s808M2_I0_open_search | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)), 40), 40)` |
| +1.16 | +1.16 | +1.46 | -1 | 5 | c05s808M2_I0_open_search | `ts_max(ts_max(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_zero_ratio(Ret)), 40), 40)` |
| +1.10 | +1.10 | +1.49 | +1 | 20 | c06s808Cr2a_Ea | `sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 241), day_kurt(Ret))` |
| +0.79 | +0.85 | +0.79 | +1 | 0 | c06s808Cr1a_Na | `sub(LogFloatShares, day_flat_run_max(Open))` |
| +0.74 | +0.74 | +0.76 | -1 | 0 | c05s808M2_I0_open_search | `ts_max(ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40), 40)` |
| +0.64 | +0.64 | +0.77 | +1 | 20 | c05s808M3_I0_open_search | `cross_quantile_q50(cross_quantile_q50(cross_delay(cross_quantile_q50(LogFloatShares, 60), 60), 60), 60)` |
| +0.57 | +0.57 | +0.90 | +1 | 20 | c06s808Cr1b_Nb | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 15)` |
| +0.56 | +0.74 | +0.56 | -1 | 0 | c05s808M2_I0_open_search | `ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), ts_max(cs_bucket_zscore(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), LogFloatCap), 40)), 40)` |

## 共性:485 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.65 | 0.000 | 6 | +1.04 / -0.61 | `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` |
| +1.56 | 0.001 | 4 | +0.95 / -0.60 | `cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), sub(log(day_sum(Amt)), LogFloatCap)), 40)` |
| +1.55 | 0.000 | 38 | +0.84 / -0.71 | `day_kurt(Ret)` |
| +1.52 | 0.000 | 6 | +0.91 / -0.61 | `cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_kurt(Ret))` |
| +1.37 | 0.000 | 11 | +0.75 / -0.62 | `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` |
| +1.34 | 0.000 | 8 | +0.73 / -0.61 | `cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), sub(log(day_sum(Amt)), LogFloatCap))` |
| +1.29 | 0.039 | 4 | +0.69 / -0.60 | `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` |
| +1.15 | 0.000 | 14 | +0.53 / -0.62 | `cross_tail_mean_q75(LogFloatShares, 15)` |
| +1.15 | 0.000 | 11 | +0.54 / -0.61 | `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)` |
| +1.15 | 0.000 | 8 | +0.54 / -0.61 | `cross_quantile_q50(LogFloatShares, 241)` |
| +1.15 | 0.000 | 16 | +0.52 / -0.63 | `cross_quantile_q50(LogFloatShares, 60)` |
| +1.13 | 0.001 | 13 | +0.51 / -0.62 | `pow_05(LogFloatShares)` |
| +1.12 | 0.011 | 5 | +0.52 / -0.60 | `cross_mean(LogFloatShares, 15)` |
| +1.11 | 0.006 | 6 | +0.51 / -0.60 | `pow_05(cross_quantile_q50(LogFloatShares, 60))` |
| +1.11 | 0.014 | 5 | +0.51 / -0.60 | `cross_quantile_q50(cross_quantile_q50(LogFloatShares, 60), 60)` |
| +1.10 | 0.018 | 14 | +0.48 / -0.62 | `inv(LogFloatShares)` |
| +1.09 | 0.048 | 5 | +0.49 / -0.60 | `ts_decay_linear(LogFloatShares, 50)` |
| +1.08 | 0.109 | 4 | +0.48 / -0.60 | `abs_(LogFloatShares)` |
| +1.08 | 0.115 | 4 | +0.48 / -0.60 | `log(LogFloatShares)` |
| +1.07 | 0.188 | 4 | +0.47 / -0.60 | `log(inv(LogFloatShares))` |

## 拆解(37 次评估)

### head score +1.16:`ts_max(ts_max(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_zero_ratio(Ret)), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_zero_ratio(Ret)), 40)` | +0.96 | +0.96 | +1.54 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_zero_ratio(Ret))` | +0.56 | +0.56 | +1.78 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_distinct_ratio(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_zero_ratio(Ret))` | +0.82 | +0.82 | +1.36 | +0.34 | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40), 40)` |
| knockout | `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` | +0.30 | +0.30 | +0.98 | +0.86 | `ts_max(ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), day_zero_ratio(Ret)), 40), 40)` |
| window | `ts_max@40->20` | +0.98 | +0.98 | +1.35 | — | `ts_max(ts_max(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_zero_ratio(Ret)), 40), 20)` |
| window | `ts_max@40->80` | +1.02 | +1.02 | +1.35 | — | `ts_max(ts_max(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_zero_ratio(Ret)), 40), 80)` |

### head score +1.10:`sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 241), day_kurt(Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 241)` | -1.55 | -0.24 | -1.55 | — | (子树本身) |
| sufficiency | `cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap))` | +0.24 | +0.73 | +0.24 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap)))` | -1.09 | -1.09 | -0.62 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap)` | -1.77 | -1.47 | -1.77 | — | (子树本身) |
| knockout | `cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 241)` | +1.05 | +1.05 | +1.53 | +0.05 | `sub(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), day_kurt(Ret))` |
| knockout | `cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap))` | +1.12 | +1.12 | +1.31 | -0.02 | `sub(cross_mean(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), 241), day_kurt(Ret))` |
| knockout | `cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap)))` | +1.03 | +1.03 | +1.53 | +0.07 | `sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), sub(log(day_sum(Amt)), LogFloatCap)), 241), day_kurt(Ret))` |
| knockout | `cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap)` | +1.03 | +1.03 | +1.50 | +0.07 | `sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 241), day_kurt(Ret))` |
| swap | `Amt->Volume` | +0.82 | +0.82 | +1.54 | — | `sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Volume), day_sum(Volume))), LogFloatCap), div(day_sum(Volume), sub(log(day_sum(Volume)), LogFloatCap))), sub(log(day_sum(Volume)), LogFloatCap)), 241), day_kurt(Ret))` |
| swap | `Volume->Amt` | +0.86 | +0.86 | +1.55 | — | `sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Amt))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 241), day_kurt(Ret))` |
| window | `cross_mean@241->120` | +1.09 | +1.09 | +1.44 | — | `sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 120), day_kurt(Ret))` |
| window | `cross_mean@241->482` | +1.09 | +1.09 | +1.41 | — | `sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 482), day_kurt(Ret))` |

### head score +0.64:`cross_quantile_q50(cross_quantile_q50(cross_delay(cross_quantile_q50(LogFloatShares, 60), 60), 60), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q50(cross_delay(cross_quantile_q50(LogFloatShares, 60), 60), 60)` | +0.57 | +0.57 | +0.77 | — | (子树本身) |
| sufficiency | `cross_delay(cross_quantile_q50(LogFloatShares, 60), 60)` | +0.56 | +0.56 | +0.77 | — | (子树本身) |
| sufficiency | `cross_quantile_q50(LogFloatShares, 60)` | +0.50 | +0.50 | +0.76 | — | (子树本身) |
| knockout | `cross_delay(cross_quantile_q50(LogFloatShares, 60), 60)` | +0.52 | +0.52 | +0.76 | +0.13 | `cross_quantile_q50(cross_quantile_q50(cross_quantile_q50(LogFloatShares, 60), 60), 60)` |
| knockout | `cross_quantile_q50(LogFloatShares, 60)` | +0.57 | +0.57 | +0.77 | +0.08 | `cross_quantile_q50(cross_quantile_q50(cross_delay(LogFloatShares, 60), 60), 60)` |
| window | `cross_quantile_q50@60->30` | +0.64 | +0.64 | +0.74 | — | `cross_quantile_q50(cross_quantile_q50(cross_delay(cross_quantile_q50(LogFloatShares, 60), 60), 60), 30)` |
| window | `cross_quantile_q50@60->120` | +0.67 | +0.67 | +0.78 | — | `cross_quantile_q50(cross_quantile_q50(cross_delay(cross_quantile_q50(LogFloatShares, 60), 60), 60), 120)` |

### head score +0.57:`cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241)` | +0.55 | +0.55 | +0.88 | — | (子树本身) |
| sufficiency | `cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15)` | +0.54 | +0.54 | +0.79 | — | (子树本身) |
| sufficiency | `cross_quantile_q50(cross_mean(LogFloatShares, 15), 241)` | +0.54 | +0.54 | +0.73 | — | (子树本身) |
| sufficiency | `cross_mean(LogFloatShares, 15)` | +0.49 | +0.49 | +0.79 | — | (子树本身) |
| knockout | `cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241)` | +0.53 | +0.53 | +0.78 | +0.04 | `cross_mean(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 15)` |
| knockout | `cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15)` | +0.58 | +0.58 | +0.88 | -0.01 | `cross_mean(cross_quantile_q50(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 241), 15)` |
| knockout | `cross_quantile_q50(cross_mean(LogFloatShares, 15), 241)` | +0.53 | +0.53 | +0.78 | +0.04 | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_mean(LogFloatShares, 15), 15), 241), 15)` |
| knockout | `cross_mean(LogFloatShares, 15)` | +0.54 | +0.54 | +0.88 | +0.02 | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(LogFloatShares, 241), 15), 241), 15)` |
| window | `cross_mean@15->7` | +0.57 | +0.57 | +0.90 | — | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 7)` |
| window | `cross_mean@15->30` | +0.58 | +0.58 | +0.92 | — | `cross_mean(cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_max(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_zero_ratio(Ret)), 40)` — ablation,自身 score +0.96(所在 head +1.16)
2. `cross_quantile_q50(cross_delay(cross_quantile_q50(LogFloatShares, 60), 60), 60)` — ablation,自身 score +0.57(所在 head +0.64)
3. `cross_delay(cross_quantile_q50(LogFloatShares, 60), 60)` — ablation,自身 score +0.56(所在 head +0.64)
4. `cross_quantile_q50(cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15), 241)` — ablation,自身 score +0.55(所在 head +0.57)
5. `cross_tail_mean_q75(cross_quantile_q50(cross_mean(LogFloatShares, 15), 241), 15)` — ablation,自身 score +0.54(所在 head +0.57)
6. `cross_quantile_q50(cross_mean(LogFloatShares, 15), 241)` — ablation,自身 score +0.54(所在 head +0.57)
7. `cross_quantile_q50(LogFloatShares, 60)` — ablation,自身 score +0.50(所在 head +0.64)
8. `cs_bucket_zscore(day_distinct_ratio(Ret), ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40))` — enrichment,均值差 +1.65,p 0.000
9. `cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), sub(log(day_sum(Amt)), LogFloatCap)), 40)` — enrichment,均值差 +1.56,p 0.001
10. `day_kurt(Ret)` — enrichment,均值差 +1.55,p 0.000
11. `cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_kurt(Ret))` — enrichment,均值差 +1.52,p 0.000
12. `ts_max(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), 40)` — enrichment,均值差 +1.37,p 0.000
13. `cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), sub(log(day_sum(Amt)), LogFloatCap))` — enrichment,均值差 +1.34,p 0.000
14. `ts_max(ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40), 40)` — enrichment,均值差 +1.29,p 0.039
15. `cross_tail_mean_q75(LogFloatShares, 15)` — enrichment,均值差 +1.15,p 0.000
16. `cross_quantile_q50(cross_tail_mean_q75(LogFloatShares, 15), 241)` — enrichment,均值差 +1.15,p 0.000
17. `cross_quantile_q50(LogFloatShares, 241)` — enrichment,均值差 +1.15,p 0.000
18. `pow_05(LogFloatShares)` — enrichment,均值差 +1.13,p 0.001
19. `cross_mean(LogFloatShares, 15)` — enrichment,均值差 +1.12,p 0.011
20. `pow_05(cross_quantile_q50(LogFloatShares, 60))` — enrichment,均值差 +1.11,p 0.006
21. `cross_quantile_q50(cross_quantile_q50(LogFloatShares, 60), 60)` — enrichment,均值差 +1.11,p 0.014
22. `inv(LogFloatShares)` — enrichment,均值差 +1.10,p 0.018
23. `ts_decay_linear(LogFloatShares, 50)` — enrichment,均值差 +1.09,p 0.048
24. `log(day_sum(Amt))` — enrichment,均值差 +0.95,p 0.000
25. `sub(log(day_sum(Amt)), LogFloatCap)` — enrichment,均值差 +0.93,p 0.000
26. `ts_max(cs_last_high05(LogFloatCap, LogFloatCap), 40)` — enrichment,均值差 +0.93,p 0.012
27. `day_sum(Volume)` — enrichment,均值差 +0.88,p 0.000
28. `day_sum(Amt)` — enrichment,均值差 +0.88,p 0.000
29. `cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume)))` — enrichment,均值差 +0.84,p 0.000
30. `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)` — enrichment,均值差 +0.81,p 0.000
31. `div(day_sum(Amt), day_sum(Volume))` — enrichment,均值差 +0.80,p 0.000
32. `day_distinct_ratio(Ret)` — enrichment,均值差 +0.80,p 0.000
33. `cs_last_high05(LogFloatCap, LogFloatCap)` — enrichment,均值差 +0.80,p 0.021

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
- `c06s808Cr2a_Ea`:核心 `cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)`;评分 119,过线 36,入 heads 1;采样计数 {'c05_no_core': 2582}
  - score +1.10(train +1.10 valid +1.49):`sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), LogFloatCap), div(day_sum(Amt), sub(log(day_sum(Amt)), LogFloatCap))), sub(log(day_sum(Amt)), LogFloatCap)), 241), day_kurt(Ret))`
  - score +1.05(train +1.05 valid +1.46):`sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap)), 10), day_kurt(Ret))`
  - score +1.01(train +1.01 valid +1.48):`sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), day_sum(Volume)), 40), day_kurt(Ret))`
  - score +1.00(train +1.00 valid +1.57):`sub(cross_mean(cs_flip_by_state(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), day_kurt(Ret)), sub(log(day_sum(Amt)), LogFloatCap)), 40), day_kurt(Ret))`
  - score +0.99(train +0.99 valid +1.48):`sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), sub(cross_mean(cs_last_low10(cs_bucket_zscore(cs_bucket_zscore(day_distinct_ratio(Ret), LogFloatCap), div(day_sum(Amt), day_sum(Volume))), sub(log(day_sum(Amt)), LogFloatCap)), 40), day_kurt(Ret)))), sub(log(day_sum(Amt)), LogFloatCap))), 241), day_kurt(Ret))`
- `c06s808Cr2b_Nb`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {}
  - score +0.22(train +0.22 valid +0.81):`cross_tail_mean_q75(day_skew(in_slice(Ret, 1, 237)), 3)`
  - score +0.14(train +0.14 valid +0.77):`cross_tail_mean_q75(day_skew(in_slice(Ret, 1, 237)), 10)`
  - score +0.11(train +0.11 valid +0.74):`cross_tail_mean_q75(day_skew(in_slice(Ret, 1, 237)), 5)`
  - score +0.05(train +0.05 valid +0.96):`cross_tail_mean_q75(day_skew(in_slice(Ret, 1, 237)), 15)`
  - score -0.17(train -0.17 valid +0.68):`cross_tail_mean_q75(cross_tail_mean_q75(day_skew(in_slice(Ret, 1, 237)), 10), 10)`

## 比原 head 好的拆解变体(R 候选)

(没有)
