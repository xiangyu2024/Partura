# 定位:种子 2057,P 组,第 1 轮(只含 train / valid)

快照:prods2057M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.35 | -1.05 | -1.35 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10), 20)` |
| -1.62 | -1.06 | -1.62 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 50)` |
| -1.62 | -1.07 | -1.62 | +1 | 5 | prods2057M1_I0_open_search | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20), 20)` |

## 共性:13 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.43 | 0.252 | 4 | -2.38 / -2.81 | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10)` |

## 拆解(21 次评估)

### head score -1.35:`ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10)` | -3.12 | -2.66 | -3.12 | — | (子树本身) |
| sufficiency | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20)` | -3.28 | -3.28 | -3.08 | — | (子树本身) |
| sufficiency | `day_sum(nt_cs_quantile_q25(Amt))` | — | — | — | — | 门槛废品 |
| knockout | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10)` | -1.91 | -1.54 | -1.91 | +0.56 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 20)` |
| knockout | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20)` | -2.92 | -2.92 | -2.36 | +1.57 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20)` |
| swap | `Amt->Volume` | -0.55 | +0.45 | -0.55 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Volume)), 20), 10), 20)` |
| window | `ts_stddev@20->10` | -2.47 | -2.09 | -2.47 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10), 10)` |
| window | `ts_stddev@20->40` | -1.19 | -0.57 | -1.19 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10), 40)` |

### head score -1.62:`ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10)` | -3.12 | -2.90 | -3.12 | — | (子树本身) |
| sufficiency | `day_sum(nt_cs_quantile_q25(Amt))` | — | — | — | — | 门槛废品 |
| knockout | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10)` | -2.93 | -2.56 | -2.93 | +1.31 | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 50)` |
| swap | `Amt->Volume` | -0.71 | +0.65 | -0.71 | — | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Volume)), 10), 50)` |
| window | `ts_stddev@50->25` | -2.47 | -2.45 | -2.47 | — | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 25)` |
| window | `ts_stddev@50->100` | -0.81 | -0.54 | -0.81 | — | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 100)` |

### head score -1.62:`ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20)` | -2.92 | -2.92 | -2.36 | — | (子树本身) |
| sufficiency | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10)` | -3.12 | -2.90 | -3.12 | — | (子树本身) |
| sufficiency | `day_sum(nt_cs_quantile_q25(Amt))` | — | — | — | — | 门槛废品 |
| knockout | `ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10)` | -1.91 | -1.54 | -1.91 | +0.29 | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 20)` |
| swap | `Amt->Volume` | -0.46 | +0.35 | -0.46 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Volume)), 10), 20), 20)` |
| window | `ts_stddev@20->10` | -3.12 | -2.28 | -3.12 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20), 10)` |
| window | `ts_stddev@20->40` | -0.67 | +0.20 | -0.67 | — | `ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.15(swap Amt->Volume):`ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Volume)), 10), 20), 20)`
- 增益 +0.95(window ts_stddev@20->40):`ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 20), 40)`
- 增益 +0.90(swap Amt->Volume):`ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Volume)), 10), 50)`
- 增益 +0.81(window ts_stddev@50->100):`ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 10), 100)`
- 增益 +0.80(swap Amt->Volume):`ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Volume)), 20), 10), 20)`
- 增益 +0.16(window ts_stddev@20->40):`ts_stddev(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(Amt)), 20), 10), 40)`
