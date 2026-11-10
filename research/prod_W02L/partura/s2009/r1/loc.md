# 定位:种子 2009,P 组,第 1 轮(只含 train / valid)

快照:prods2009M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.23 | -1.65 | -2.23 | +1 | 20 | prods2009M1_I0_open_search | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` |
| -2.27 | -1.92 | -2.27 | +1 | 20 | prods2009M1_I0_open_search | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` |
| -2.35 | -2.20 | -2.35 | +1 | 20 | prods2009M1_I0_open_search | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` |

## 共性:14 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.93 | 0.042 | 5 | -2.67 / -3.61 | `day_durbin_watson(Volume)` |
| +0.93 | 0.042 | 5 | -2.67 / -3.61 | `log(day_durbin_watson(Volume))` |
| +0.93 | 0.042 | 5 | -2.67 / -3.61 | `log(log(day_durbin_watson(Volume)))` |
| -0.93 | 0.970 | 9 | -3.61 / -2.67 | `log(log(day_durbin_watson(Vwap)))` |
| -0.93 | 0.970 | 9 | -3.61 / -2.67 | `log(day_durbin_watson(Vwap))` |
| -0.93 | 0.970 | 9 | -3.61 / -2.67 | `day_durbin_watson(Vwap)` |

## 拆解(21 次评估)

### head score -2.23:`ts_sum(log(log(day_durbin_watson(Volume))), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(log(day_durbin_watson(Volume)))` | -2.32 | -2.08 | -2.32 | — | (子树本身) |
| sufficiency | `log(day_durbin_watson(Volume))` | -4.21 | -3.69 | -4.21 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Volume)` | -4.21 | -3.69 | -4.21 | — | (子树本身) |
| knockout | `log(log(day_durbin_watson(Volume)))` | -3.84 | -3.84 | -3.01 | +1.61 | `ts_sum(log(day_durbin_watson(Volume)), 10)` |
| swap | `Volume->Amt` | -2.25 | -1.61 | -2.25 | — | `ts_sum(log(log(day_durbin_watson(Amt))), 10)` |
| window | `ts_sum@10->5` | -2.26 | -1.92 | -2.26 | — | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` |
| window | `ts_sum@10->20` | -2.23 | -1.95 | -2.23 | — | `ts_sum(log(log(day_durbin_watson(Volume))), 20)` |

### head score -2.27:`ts_sum(log(log(day_durbin_watson(Volume))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(log(day_durbin_watson(Volume)))` | -2.32 | -2.08 | -2.32 | — | (子树本身) |
| sufficiency | `log(day_durbin_watson(Volume))` | -4.21 | -3.69 | -4.21 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Volume)` | -4.21 | -3.69 | -4.21 | — | (子树本身) |
| knockout | `log(log(day_durbin_watson(Volume)))` | -3.79 | -3.79 | -2.90 | +1.52 | `ts_sum(log(day_durbin_watson(Volume)), 5)` |
| swap | `Volume->Amt` | -2.25 | -1.85 | -2.25 | — | `ts_sum(log(log(day_durbin_watson(Amt))), 5)` |
| window | `ts_sum@5->2` | -2.31 | -1.99 | -2.31 | — | `ts_sum(log(log(day_durbin_watson(Volume))), 2)` |
| window | `ts_sum@5->10` | -2.21 | -1.65 | -2.21 | — | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` |

### head score -2.35:`cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(log(day_durbin_watson(Volume)))` | -2.32 | -2.08 | -2.32 | — | (子树本身) |
| sufficiency | `log(day_durbin_watson(Volume))` | -4.21 | -3.69 | -4.21 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Volume)` | -4.21 | -3.69 | -4.21 | — | (子树本身) |
| knockout | `log(log(day_durbin_watson(Volume)))` | -3.56 | -3.56 | -3.23 | +1.21 | `cross_fangzheng(log(day_durbin_watson(Volume)), 10)` |
| swap | `Volume->Amt` | -2.31 | -2.27 | -2.31 | — | `cross_fangzheng(log(log(day_durbin_watson(Amt))), 10)` |
| window | `cross_fangzheng@10->5` | -2.64 | -2.01 | -2.64 | — | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 5)` |
| window | `cross_fangzheng@10->20` | -2.03 | -2.03 | -2.03 | — | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 20)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_durbin_watson(Volume)` — enrichment,均值差 +0.93,p 0.042
2. `log(day_durbin_watson(Volume))` — enrichment,均值差 +0.93,p 0.042
3. `log(log(day_durbin_watson(Volume)))` — enrichment,均值差 +0.93,p 0.042

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
