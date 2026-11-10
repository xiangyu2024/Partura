# 定位:种子 2052,P 组,第 1 轮(只含 train / valid)

快照:prods2052M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.09 | -2.09 | -1.66 | +1 | 5 | prods2052M1_I0_open_search | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 60), 5)` |
| -2.20 | -1.90 | -2.20 | +1 | 5 | prods2052M1_I0_open_search | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 5), 40)` |
| -2.24 | -2.24 | -2.19 | +1 | 5 | prods2052M1_I0_open_search | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5), 30), 60), 5)` |

## 共性:25 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.44 | 0.070 | 7 | -2.82 / -3.26 | `ts_max(day_ar1_coefficient(High), 5)` |
| +0.25 | 0.185 | 12 | -3.01 / -3.25 | `day_ar1_coefficient(High)` |
| -0.32 | 0.909 | 12 | -3.30 / -2.98 | `day_ar1_coefficient(Close)` |
| -0.40 | 0.952 | 7 | -3.42 / -3.02 | `ts_max(day_ar1_coefficient(Close), 5)` |

## 拆解(30 次评估)

### head score -2.09:`ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 60), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 60)` | -1.90 | -1.90 | -1.75 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(day_ar1_coefficient(High), 5), 30)` | -3.08 | -2.67 | -3.08 | — | (子树本身) |
| sufficiency | `ts_max(day_ar1_coefficient(High), 5)` | -3.63 | -3.63 | -2.54 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(High)` | -2.64 | -2.64 | -2.30 | — | (子树本身) |
| knockout | `cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 60)` | -3.43 | -2.33 | -3.43 | +1.34 | `ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 5)` |
| knockout | `ts_max(ts_max(day_ar1_coefficient(High), 5), 30)` | -2.27 | -2.27 | -2.03 | +0.18 | `ts_max(cross_med(ts_max(day_ar1_coefficient(High), 5), 60), 5)` |
| knockout | `ts_max(day_ar1_coefficient(High), 5)` | -2.68 | -2.68 | -1.48 | +0.59 | `ts_max(cross_med(ts_max(day_ar1_coefficient(High), 30), 60), 5)` |
| swap | `High->Low` | -1.55 | -1.55 | -1.51 | — | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 60), 5)` |
| window | `ts_max@5->2` | -1.97 | -1.97 | -1.63 | — | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 60), 2)` |
| window | `ts_max@5->10` | -2.06 | -2.06 | -1.71 | — | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 60), 10)` |

### head score -2.20:`ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 5), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 5)` | -3.43 | -2.33 | -3.43 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(day_ar1_coefficient(High), 5), 30)` | -3.08 | -2.67 | -3.08 | — | (子树本身) |
| sufficiency | `ts_max(day_ar1_coefficient(High), 5)` | -3.63 | -3.63 | -2.54 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(High)` | -2.64 | -2.64 | -2.30 | — | (子树本身) |
| knockout | `ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 5)` | -2.14 | -1.78 | -2.14 | -0.05 | `ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 40)` |
| knockout | `ts_max(ts_max(day_ar1_coefficient(High), 5), 30)` | -3.22 | -2.22 | -3.22 | +1.02 | `ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 5), 40)` |
| knockout | `ts_max(day_ar1_coefficient(High), 5)` | -2.13 | -1.78 | -2.13 | -0.07 | `ts_max(ts_max(ts_max(day_ar1_coefficient(High), 30), 5), 40)` |
| swap | `High->Low` | -1.47 | -1.47 | -1.47 | — | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 5), 40)` |
| window | `ts_max@40->20` | -3.00 | -1.76 | -3.00 | — | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 5), 20)` |
| window | `ts_max@40->80` | -1.89 | -1.89 | -1.66 | — | `ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 5), 80)` |

### head score -2.24:`ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5), 30), 60), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5), 30), 60)` | -2.18 | -2.11 | -2.18 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(day_ar1_coefficient(Close), 5), 30)` | -4.26 | -2.97 | -4.26 | — | (子树本身) |
| sufficiency | `ts_max(day_ar1_coefficient(Close), 5)` | -3.30 | -3.30 | -2.83 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Close)` | -2.44 | -2.44 | -2.34 | — | (子树本身) |
| knockout | `cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5), 30), 60)` | -4.08 | -3.08 | -4.08 | +1.84 | `ts_max(ts_max(ts_max(day_ar1_coefficient(Close), 5), 30), 5)` |
| knockout | `ts_max(ts_max(day_ar1_coefficient(Close), 5), 30)` | -2.11 | -1.92 | -2.11 | -0.13 | `ts_max(cross_med(ts_max(day_ar1_coefficient(Close), 5), 60), 5)` |
| knockout | `ts_max(day_ar1_coefficient(Close), 5)` | -2.61 | -2.51 | -2.61 | +0.37 | `ts_max(cross_med(ts_max(day_ar1_coefficient(Close), 30), 60), 5)` |
| swap | `Close->Vwap` | -2.42 | -2.42 | -0.80 | — | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Vwap), 5), 30), 60), 5)` |
| window | `ts_max@5->2` | -2.24 | -2.24 | -2.08 | — | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5), 30), 60), 2)` |
| window | `ts_max@5->10` | -2.07 | -2.06 | -2.07 | — | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5), 30), 60), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_max(day_ar1_coefficient(High), 5)` — enrichment,均值差 +0.44,p 0.070

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.73(swap High->Low):`ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 5), 40)`
- 增益 +0.54(swap High->Low):`ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Low), 5), 30), 60), 5)`
- 增益 +0.31(window ts_max@40->80):`ts_max(ts_max(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 5), 80)`
- 增益 +0.17(window ts_max@5->10):`ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(Close), 5), 30), 60), 10)`
- 增益 +0.12(window ts_max@5->2):`ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5), 30), 60), 2)`
