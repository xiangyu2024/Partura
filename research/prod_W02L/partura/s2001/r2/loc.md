# 定位:种子 2001,P 组,第 2 轮(只含 train / valid)

快照:prods2001M1_I0_open_search, prods2001M2_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.67 | -0.67 | -0.40 | +1 | 0 | prods2001M2_I0_open_search | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 50), 40)` |
| -0.69 | -0.69 | -0.69 | +1 | 5 | prods2001M2_I0_open_search | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 40)` |
| -0.75 | -0.75 | -0.56 | +1 | 0 | prods2001M2_I0_open_search | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 20)` |
| -1.11 | -1.10 | -1.11 | -1 | 5 | prods2001M1_I0_open_search | `day_max(Volume)` |
| -1.11 | -1.10 | -1.11 | -1 | 5 | prods2001M1_I0_open_search | `pow_1_5(day_max(Volume))` |
| -1.51 | -1.51 | +0.02 | +1 | 20 | prods2001M1_I0_open_search | `ts_autocorr_s1(cross_delay(ts_quantile_q50(day_max(Amt), 20), 241), 20)` |

## 共性:87 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.38 | 0.000 | 42 | -1.60 / -2.98 | `day_q_stat_std(Volume)` |
| +1.25 | 0.000 | 8 | -1.18 / -2.43 | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` |
| +1.05 | 0.000 | 11 | -1.40 / -2.45 | `ts_quantile_q75(day_q_stat_std(Volume), 50)` |
| +1.04 | 0.000 | 13 | -1.43 / -2.47 | `ts_quantile_q75(day_q_stat_std(Volume), 40)` |
| +0.97 | 0.030 | 4 | -1.39 / -2.36 | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 50), 40)` |
| +0.64 | 0.024 | 8 | -1.73 / -2.37 | `ts_quantile_q75(day_q_stat_std(Volume), 5)` |
| -0.41 | 0.708 | 4 | -2.71 / -2.30 | `day_max(Volume)` |
| -0.45 | 0.983 | 6 | -2.74 / -2.28 | `day_max(Ret)` |
| -0.90 | 0.936 | 4 | -3.17 / -2.27 | `day_max(Vwap)` |
| -1.61 | 1.000 | 15 | -3.65 / -2.04 | `day_max(Amt)` |

## 拆解(29 次评估)

### head score -0.67:`ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 50)` | -0.73 | -0.67 | -0.73 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40)` | -0.73 | -0.68 | -0.73 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40)` | -1.26 | -1.07 | -1.26 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50)` | -1.31 | -1.31 | -1.29 | — | (子树本身) |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 50)` | -0.62 | -0.62 | -0.54 | -0.05 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 40)` |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40)` | -0.67 | -0.66 | -0.67 | +0.01 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 50), 40)` |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50)` | -0.62 | -0.62 | -0.56 | -0.05 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 40), 50), 40)` |
| swap | `Volume->Amt` | -0.59 | -0.59 | -0.25 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Amt), 40), 40), 50), 40), 40), 50), 40)` |
| window | `ts_quantile_q75@40->20` | -0.63 | -0.63 | -0.46 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 50), 20)` |
| window | `ts_quantile_q75@40->80` | -0.83 | -0.83 | -0.19 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 50), 80)` |

### head score -0.69:`ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50)` | -1.25 | -1.05 | -1.25 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40)` | -1.75 | -1.34 | -1.75 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` | -1.73 | -1.57 | -1.73 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(day_q_stat_std(Volume), 40)` | -2.32 | -2.01 | -2.32 | — | (子树本身) |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50)` | -1.37 | -0.99 | -1.37 | +0.68 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 40)` |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40)` | -1.26 | -1.07 | -1.26 | +0.56 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40)` |
| swap | `Volume->Amt` | -0.76 | -0.70 | -0.76 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Amt), 40), 40), 40), 50), 40)` |
| window | `ts_quantile_q75@40->20` | -1.06 | -0.84 | -1.06 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 20)` |
| window | `ts_quantile_q75@40->80` | -0.60 | -0.57 | -0.60 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 80)` |

### head score -0.75:`ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40)` | -0.73 | -0.68 | -0.73 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40)` | -1.26 | -1.07 | -1.26 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50)` | -1.31 | -1.31 | -1.29 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` | -1.73 | -1.57 | -1.73 | — | (子树本身) |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40)` | -1.05 | -0.85 | -1.05 | +0.30 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 20)` |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50)` | -1.14 | -0.97 | -1.14 | +0.39 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 40), 20)` |
| knockout | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` | -1.05 | -0.90 | -1.05 | +0.30 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 50), 40), 40), 20)` |
| swap | `Volume->Amt` | -0.75 | -0.75 | -0.64 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Amt), 40), 40), 50), 40), 40), 20)` |
| window | `ts_quantile_q75@20->10` | -0.66 | -0.66 | -0.65 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 10)` |
| window | `ts_quantile_q75@20->40` | -0.62 | -0.62 | -0.54 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_q_stat_std(Volume)` — enrichment,均值差 +1.38,p 0.000
2. `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` — enrichment,均值差 +1.25,p 0.000
3. `ts_quantile_q75(day_q_stat_std(Volume), 50)` — enrichment,均值差 +1.05,p 0.000
4. `ts_quantile_q75(day_q_stat_std(Volume), 40)` — enrichment,均值差 +1.04,p 0.000
5. `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 50), 40)` — enrichment,均值差 +0.97,p 0.030
6. `ts_quantile_q75(day_q_stat_std(Volume), 5)` — enrichment,均值差 +0.64,p 0.024

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(window ts_quantile_q75@20->40):`ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 40)`
