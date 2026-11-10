# 定位:种子 2029,P 组,第 1 轮(只含 train / valid)

快照:prods2029M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.03 | +0.15 | -0.03 | +1 | 0 | prods2029M1_I0_open_search | `ts_std(ts_std(ts_max(ts_std(day_mean(Amt), 40), 40), 40), 40)` |
| -0.11 | -0.11 | +0.11 | +1 | 0 | prods2029M1_I0_open_search | `ts_max(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` |
| -0.21 | -0.06 | -0.21 | +1 | 0 | prods2029M1_I0_open_search | `ts_max(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)` |

## 共性:13 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.48 | 0.090 | 6 | -0.43 / -0.91 | `ts_std(ts_std(day_mean(Amt), 40), 40)` |

## 拆解(24 次评估)

### head score -0.03:`ts_std(ts_std(ts_max(ts_std(day_mean(Amt), 40), 40), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(ts_max(ts_std(day_mean(Amt), 40), 40), 40)` | -0.18 | -0.18 | +0.58 | — | (子树本身) |
| sufficiency | `ts_max(ts_std(day_mean(Amt), 40), 40)` | -0.59 | -0.59 | -0.13 | — | (子树本身) |
| sufficiency | `ts_std(day_mean(Amt), 40)` | -0.77 | -0.72 | -0.77 | — | (子树本身) |
| sufficiency | `day_mean(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `ts_max(ts_std(day_mean(Amt), 40), 40)` | -0.29 | -0.29 | -0.10 | +0.26 | `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` |
| knockout | `ts_std(day_mean(Amt), 40)` | -0.28 | -0.28 | +0.00 | +0.26 | `ts_std(ts_std(ts_max(day_mean(Amt), 40), 40), 40)` |
| swap | `Amt->Volume` | -2.40 | -1.13 | -2.40 | — | `ts_std(ts_std(ts_max(ts_std(day_mean(Volume), 40), 40), 40), 40)` |
| window | `ts_std@40->20` | -0.30 | -0.14 | -0.30 | — | `ts_std(ts_std(ts_max(ts_std(day_mean(Amt), 40), 40), 40), 20)` |
| window | `ts_std@40->80` | -0.04 | -0.04 | +0.01 | — | `ts_std(ts_std(ts_max(ts_std(day_mean(Amt), 40), 40), 40), 80)` |

### head score -0.11:`ts_max(ts_std(ts_std(day_mean(Amt), 40), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(ts_std(day_mean(Amt), 40), 40)` | -0.43 | -0.43 | +0.56 | — | (子树本身) |
| sufficiency | `ts_std(day_mean(Amt), 40)` | -0.77 | -0.72 | -0.77 | — | (子树本身) |
| sufficiency | `day_mean(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `ts_std(ts_std(day_mean(Amt), 40), 40)` | -0.59 | -0.59 | -0.13 | +0.48 | `ts_max(ts_std(day_mean(Amt), 40), 40)` |
| swap | `Amt->Volume` | -2.42 | -1.02 | -2.42 | — | `ts_max(ts_std(ts_std(day_mean(Volume), 40), 40), 40)` |
| window | `ts_max@40->20` | -0.16 | -0.16 | +0.09 | — | `ts_max(ts_std(ts_std(day_mean(Amt), 40), 40), 20)` |
| window | `ts_max@40->80` | +0.10 | +0.10 | +0.10 | — | `ts_max(ts_std(ts_std(day_mean(Amt), 40), 40), 80)` |

### head score -0.21:`ts_max(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` | -0.29 | -0.29 | -0.10 | — | (子树本身) |
| sufficiency | `ts_std(ts_std(day_mean(Amt), 40), 40)` | -0.43 | -0.43 | +0.56 | — | (子树本身) |
| sufficiency | `ts_std(day_mean(Amt), 40)` | -0.77 | -0.72 | -0.77 | — | (子树本身) |
| sufficiency | `day_mean(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` | -0.12 | -0.12 | +0.08 | -0.09 | `ts_max(ts_std(ts_std(day_mean(Amt), 40), 40), 40)` |
| swap | `Amt->Volume` | -2.66 | -1.26 | -2.66 | — | `ts_max(ts_std(ts_std(ts_std(day_mean(Volume), 40), 40), 40), 40)` |
| window | `ts_max@40->20` | -0.32 | -0.21 | -0.32 | — | `ts_max(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 20)` |
| window | `ts_max@40->80` | -0.26 | -0.09 | -0.26 | — | `ts_max(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_std(ts_std(day_mean(Amt), 40), 40)` — enrichment,均值差 +0.48,p 0.090

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
