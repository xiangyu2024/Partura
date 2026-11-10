# 定位:种子 2012,P 组,第 1 轮(只含 train / valid)

快照:prods2012M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.99 | -2.99 | -2.97 | +1 | 20 | prods2012M1_I0_open_search | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)))))), 5)` |
| -3.01 | -2.83 | -3.01 | +1 | 20 | prods2012M1_I0_open_search | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)))` |
| -3.02 | -2.84 | -3.02 | +1 | 20 | prods2012M1_I0_open_search | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)` |

## 共性:14 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.09 | 0.091 | 6 | -3.06 / -3.15 | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))` |
| -0.05 | 0.741 | 9 | -3.13 / -3.08 | `ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)` |
| -0.05 | 0.741 | 9 | -3.13 / -3.08 | `cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))` |

## 拆解(30 次评估)

### head score -2.99:`ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)))))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40))))))` | -3.05 | -3.04 | -3.05 | — | (子树本身) |
| sufficiency | `pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)))))` | -3.08 | -3.02 | -3.08 | — | (子树本身) |
| sufficiency | `pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40))))` | -3.08 | -3.02 | -3.08 | — | (子树本身) |
| sufficiency | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)))` | -3.08 | -3.02 | -3.08 | — | (子树本身) |
| knockout | `sigmoid(pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40))))))` | -3.04 | -2.98 | -3.04 | +0.05 | `ts_decay_linear(pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40))))), 5)` |
| knockout | `pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)))))` | -3.07 | -3.01 | -3.07 | +0.09 | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40))))), 5)` |
| swap | `Volume->Amt` | -3.05 | -2.99 | -3.05 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Amt))), 40)))))), 5)` |
| window | `ts_decay_linear@5->2` | -3.07 | -3.06 | -3.07 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)))))), 2)` |
| window | `ts_decay_linear@5->10` | -3.20 | -2.85 | -3.20 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 40)))))), 10)` |

### head score -3.01:`pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5))` | -3.01 | -2.83 | -3.01 | — | (子树本身) |
| sufficiency | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)` | -3.02 | -2.84 | -3.02 | — | (子树本身) |
| sufficiency | `sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))))` | -3.29 | -2.86 | -3.29 | — | (子树本身) |
| sufficiency | `pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))` | -3.31 | -2.87 | -3.31 | — | (子树本身) |
| knockout | `cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5))` | -3.02 | -2.84 | -3.02 | +0.01 | `pow_2(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5))` |
| knockout | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)` | -3.29 | -2.86 | -3.29 | +0.28 | `pow_2(cs_rank(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))))))` |
| knockout | `sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))))` | -3.02 | -2.83 | -3.02 | +0.01 | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))), 5)))` |
| knockout | `pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))` | -3.08 | -2.81 | -3.08 | +0.07 | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))), 5)))` |
| swap | `Volume->Amt` | -3.02 | -2.85 | -3.02 | — | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Amt))), 5))))), 5)))` |
| window | `ts_decay_linear@5->2` | -3.17 | -2.81 | -3.17 | — | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 2)))` |
| window | `ts_decay_linear@5->10` | -2.95 | -2.88 | -2.95 | — | `pow_2(cs_rank(ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 10)))` |

### head score -3.02:`ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))))` | -3.29 | -2.86 | -3.29 | — | (子树本身) |
| sufficiency | `pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))` | -3.31 | -2.87 | -3.31 | — | (子树本身) |
| sufficiency | `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))` | -3.31 | -2.87 | -3.31 | — | (子树本身) |
| sufficiency | `cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))` | -3.31 | -2.87 | -3.31 | — | (子树本身) |
| knockout | `sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))))` | -3.02 | -2.83 | -3.02 | +0.00 | `ts_decay_linear(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))), 5)` |
| knockout | `pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))` | -3.09 | -2.81 | -3.09 | +0.07 | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))), 5)` |
| knockout | `cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))` | -3.05 | -2.84 | -3.05 | +0.03 | `ts_decay_linear(sigmoid(pow_2(pow_2(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))), 5)` |
| swap | `Volume->Amt` | -3.03 | -2.85 | -3.03 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Amt))), 5))))), 5)` |
| window | `ts_decay_linear@5->2` | -3.17 | -2.82 | -3.17 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 2)` |
| window | `ts_decay_linear@5->10` | -2.95 | -2.88 | -2.95 | — | `ts_decay_linear(sigmoid(pow_2(pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5))))), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_2(cs_rank(ts_decay_linear(pow_2(pow_05(day_ar1_coefficient(Volume))), 5)))` — enrichment,均值差 +0.09,p 0.091

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
