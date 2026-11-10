# 定位:种子 2013,P 组,第 1 轮(只含 train / valid)

快照:prods2013M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.98 | -2.98 | -2.97 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(cs_rank(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)` |
| -3.15 | -3.06 | -3.15 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))), 5)` |
| -3.15 | -3.06 | -3.15 | +1 | 20 | prods2013M1_I0_open_search | `ts_min(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)` |

## 共性:9 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(33 次评估)

### head score -2.98:`ts_min(cs_rank(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| knockout | `cs_rank(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))` | -3.13 | -3.06 | -3.13 | +0.15 | `ts_min(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)` |
| knockout | `sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))` | -2.98 | -2.98 | -2.95 | +0.00 | `ts_min(cs_rank(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)` |
| knockout | `pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -2.99 | -2.99 | -2.95 | +0.00 | `ts_min(cs_rank(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)` |
| knockout | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -2.92 | -2.92 | -2.89 | -0.06 | `ts_min(cs_rank(sigmoid(pow_05(pow_05(day_ar1_coefficient(Volume))))), 5)` |
| swap | `Volume->Amt` | -2.99 | -2.93 | -2.99 | — | `ts_min(cs_rank(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Amt)))))), 5)` |
| window | `ts_min@5->2` | -3.31 | -2.90 | -3.31 | — | `ts_min(cs_rank(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 2)` |
| window | `ts_min@5->10` | -2.41 | -2.41 | -2.17 | — | `ts_min(cs_rank(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 10)` |

### head score -3.15:`ts_min(sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))))` | -3.40 | -2.83 | -3.40 | — | (子树本身) |
| sufficiency | `pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| knockout | `sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))))` | -3.13 | -3.06 | -3.13 | -0.02 | `ts_min(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)` |
| knockout | `pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))` | -3.13 | -3.06 | -3.13 | -0.02 | `ts_min(sigmoid(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)` |
| knockout | `sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))` | -3.13 | -3.06 | -3.13 | -0.02 | `ts_min(sigmoid(pow_05(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)` |
| knockout | `pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.13 | -3.06 | -3.13 | -0.02 | `ts_min(sigmoid(pow_05(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))))), 5)` |
| swap | `Volume->Amt` | -3.21 | -3.08 | -3.21 | — | `ts_min(sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Amt))))))), 5)` |
| window | `ts_min@5->2` | -3.24 | -3.06 | -3.24 | — | `ts_min(sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))), 2)` |
| window | `ts_min@5->10` | -2.70 | -2.70 | -2.42 | — | `ts_min(sigmoid(pow_05(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))))), 10)` |

### head score -3.15:`ts_min(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -3.39 | -2.83 | -3.39 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))))` | -3.13 | -3.06 | -3.13 | -0.02 | `ts_min(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)` |
| knockout | `pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))` | -3.13 | -3.06 | -3.13 | -0.02 | `ts_min(sigmoid(pow_2(pow_05(day_ar1_coefficient(Volume)))), 5)` |
| knockout | `pow_2(pow_05(day_ar1_coefficient(Volume)))` | -3.13 | -3.04 | -3.13 | -0.02 | `ts_min(sigmoid(pow_05(pow_05(day_ar1_coefficient(Volume)))), 5)` |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -3.13 | -3.06 | -3.13 | -0.02 | `ts_min(sigmoid(pow_05(pow_2(day_ar1_coefficient(Volume)))), 5)` |
| swap | `Volume->Amt` | -3.21 | -3.08 | -3.21 | — | `ts_min(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Amt))))), 5)` |
| window | `ts_min@5->2` | -3.24 | -3.06 | -3.24 | — | `ts_min(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 2)` |
| window | `ts_min@5->10` | -2.70 | -2.70 | -2.42 | — | `ts_min(sigmoid(pow_05(pow_2(pow_05(day_ar1_coefficient(Volume))))), 10)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
