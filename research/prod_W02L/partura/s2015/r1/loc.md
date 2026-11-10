# 定位:种子 2015,P 组,第 1 轮(只含 train / valid)

快照:prods2015M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.30 | -0.30 | +0.62 | +1 | 0 | prods2015M1_I0_open_search | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 50)` |
| -0.42 | -0.42 | -0.12 | +1 | 5 | prods2015M1_I0_open_search | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 40)` |
| -0.71 | -0.71 | -0.31 | +1 | 20 | prods2015M1_I0_open_search | `ts_std(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 10)` |

## 共性:13 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.62 | 0.001 | 7 | -0.81 / -2.43 | `cross_stddev(day_quantile_q25(Amt), 60)` |
| +1.62 | 0.001 | 7 | -0.81 / -2.43 | `day_quantile_q25(Amt)` |
| -1.15 | 0.975 | 4 | -2.36 / -1.20 | `day_quantile_q25(Low)` |
| -1.15 | 0.975 | 4 | -2.36 / -1.20 | `cross_stddev(day_quantile_q25(Low), 60)` |

## 拆解(19 次评估)

### head score -0.30:`ts_std(cross_stddev(day_quantile_q25(Amt), 60), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(day_quantile_q25(Amt), 60)` | -1.11 | -1.11 | -0.50 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Amt)` | -3.42 | -3.33 | -3.42 | — | (子树本身) |
| knockout | `cross_stddev(day_quantile_q25(Amt), 60)` | -1.12 | -1.12 | -0.65 | +0.82 | `ts_std(day_quantile_q25(Amt), 50)` |
| swap | `Amt->Volume` | -1.93 | -1.19 | -1.93 | — | `ts_std(cross_stddev(day_quantile_q25(Volume), 60), 50)` |
| window | `ts_std@50->25` | -0.51 | -0.44 | -0.51 | — | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 25)` |
| window | `ts_std@50->100` | -0.31 | -0.26 | -0.31 | — | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 100)` |

### head score -0.42:`ts_std(cross_stddev(day_quantile_q25(Amt), 60), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(day_quantile_q25(Amt), 60)` | -1.11 | -1.11 | -0.50 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Amt)` | -3.42 | -3.33 | -3.42 | — | (子树本身) |
| knockout | `cross_stddev(day_quantile_q25(Amt), 60)` | -1.29 | -1.29 | -1.00 | +0.87 | `ts_std(day_quantile_q25(Amt), 40)` |
| swap | `Amt->Volume` | -1.73 | -1.16 | -1.73 | — | `ts_std(cross_stddev(day_quantile_q25(Volume), 60), 40)` |
| window | `ts_std@40->20` | -0.56 | -0.56 | -0.52 | — | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 20)` |
| window | `ts_std@40->80` | -0.44 | -0.32 | -0.44 | — | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 80)` |

### head score -0.71:`ts_std(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60)` | -0.36 | -0.36 | +0.17 | — | (子树本身) |
| sufficiency | `cross_stddev(day_quantile_q25(Amt), 60)` | -1.11 | -1.11 | -0.50 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Amt)` | -3.42 | -3.33 | -3.42 | — | (子树本身) |
| knockout | `cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60)` | -0.93 | -0.93 | -0.16 | +0.23 | `ts_std(cross_stddev(day_quantile_q25(Amt), 60), 10)` |
| swap | `Amt->Volume` | -2.35 | -1.48 | -2.35 | — | `ts_std(cross_stddev(cross_stddev(day_quantile_q25(Volume), 60), 60), 10)` |
| window | `ts_std@10->5` | -0.79 | -0.79 | -0.18 | — | `ts_std(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 5)` |
| window | `ts_std@10->20` | -0.69 | -0.67 | -0.69 | — | `ts_std(cross_stddev(cross_stddev(day_quantile_q25(Amt), 60), 60), 20)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_stddev(day_quantile_q25(Amt), 60)` — enrichment,均值差 +1.62,p 0.001
2. `day_quantile_q25(Amt)` — enrichment,均值差 +1.62,p 0.001

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
