# 定位:种子 2060,P 组,第 1 轮(只含 train / valid)

快照:prods2060M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -3.05 | -3.05 | -2.35 | +1 | 5 | prods2060M1_I0_open_search | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5))), 5)` |
| -3.11 | -2.86 | -3.11 | +1 | 20 | prods2060M1_I0_open_search | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)))), 5)` |
| -3.17 | -2.89 | -3.17 | +1 | 20 | prods2060M1_I0_open_search | `ts_decay_linear(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)), 5)` |

## 共性:8 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.18 | 0.036 | 5 | -3.18 / -3.36 | `ts_decay_linear(day_ar1_coefficient(Volume), 5)` |
| +0.18 | 0.036 | 5 | -3.18 / -3.36 | `cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))` |

## 拆解(30 次评估)

### head score -3.05:`ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5)))` | -3.27 | -3.21 | -3.27 | — | (子树本身) |
| sufficiency | `cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5))` | -3.27 | -3.21 | -3.27 | — | (子树本身) |
| sufficiency | `ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5)` | -3.27 | -3.21 | -3.27 | — | (子树本身) |
| sufficiency | `pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5)))` | -3.39 | -3.05 | -3.39 | — | (子树本身) |
| knockout | `sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5)))` | -3.04 | -3.04 | -2.27 | -0.02 | `ts_decay_linear(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5)), 5)` |
| knockout | `cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5))` | -3.08 | -3.08 | -2.38 | +0.02 | `ts_decay_linear(sigmoid(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5)), 5)` |
| knockout | `ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5)` | -3.20 | -3.20 | -2.34 | +0.15 | `ts_decay_linear(sigmoid(cs_rank(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))))), 5)` |
| knockout | `pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5)))` | -3.02 | -3.02 | -2.40 | -0.04 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5)), 5))), 5)` |
| swap | `Volume->Amt` | -3.11 | -3.11 | -2.31 | — | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Amt), 5))), 5))), 5))), 5)` |
| window | `ts_decay_linear@5->2` | -3.14 | -3.14 | -2.38 | — | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5))), 2)` |
| window | `ts_decay_linear@5->10` | -3.16 | -3.16 | -2.18 | — | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(pow_2(pow_05(ts_min(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5))), 5))), 10)` |

### head score -3.11:`ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))))` | -3.31 | -2.85 | -3.31 | — | (子树本身) |
| sufficiency | `pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)))` | -3.31 | -2.85 | -3.31 | — | (子树本身) |
| sufficiency | `cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))` | -3.31 | -2.85 | -3.31 | — | (子树本身) |
| sufficiency | `ts_decay_linear(day_ar1_coefficient(Volume), 5)` | -3.31 | -2.85 | -3.31 | — | (子树本身) |
| knockout | `sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))))` | -3.11 | -2.85 | -3.11 | +0.00 | `ts_decay_linear(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5)` |
| knockout | `pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)))` | -3.23 | -2.86 | -3.23 | +0.12 | `ts_decay_linear(sigmoid(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5)` |
| knockout | `cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))` | -3.11 | -2.86 | -3.11 | -0.00 | `ts_decay_linear(sigmoid(pow_2(ts_decay_linear(day_ar1_coefficient(Volume), 5))), 5)` |
| knockout | `ts_decay_linear(day_ar1_coefficient(Volume), 5)` | -3.14 | -2.61 | -3.14 | +0.03 | `ts_decay_linear(sigmoid(pow_2(cs_rank(day_ar1_coefficient(Volume)))), 5)` |
| swap | `Volume->Amt` | -3.12 | -2.83 | -3.12 | — | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Amt), 5)))), 5)` |
| window | `ts_decay_linear@5->2` | -3.21 | -2.82 | -3.21 | — | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)))), 2)` |
| window | `ts_decay_linear@5->10` | -3.11 | -3.00 | -3.11 | — | `ts_decay_linear(sigmoid(pow_2(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)))), 10)` |

### head score -3.17:`ts_decay_linear(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))` | -3.31 | -2.85 | -3.31 | — | (子树本身) |
| sufficiency | `ts_decay_linear(day_ar1_coefficient(Volume), 5)` | -3.31 | -2.85 | -3.31 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))` | -3.21 | -2.90 | -3.21 | +0.04 | `ts_decay_linear(ts_decay_linear(day_ar1_coefficient(Volume), 5), 5)` |
| knockout | `ts_decay_linear(day_ar1_coefficient(Volume), 5)` | -3.23 | -2.88 | -3.23 | +0.06 | `ts_decay_linear(cs_rank(day_ar1_coefficient(Volume)), 5)` |
| swap | `Volume->Amt` | -3.19 | -2.89 | -3.19 | — | `ts_decay_linear(cs_rank(ts_decay_linear(day_ar1_coefficient(Amt), 5)), 5)` |
| window | `ts_decay_linear@5->2` | -3.25 | -2.83 | -3.25 | — | `ts_decay_linear(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)), 2)` |
| window | `ts_decay_linear@5->10` | -3.08 | -3.03 | -3.08 | — | `ts_decay_linear(cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5)), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_decay_linear(day_ar1_coefficient(Volume), 5)` — enrichment,均值差 +0.18,p 0.036
2. `cs_rank(ts_decay_linear(day_ar1_coefficient(Volume), 5))` — enrichment,均值差 +0.18,p 0.036

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
