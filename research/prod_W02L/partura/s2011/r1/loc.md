# 定位:种子 2011,P 组,第 1 轮(只含 train / valid)

快照:prods2011M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.80 | -1.36 | -1.80 | +1 | 20 | prods2011M1_I0_open_search | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)` |
| -1.98 | -1.95 | -1.98 | +1 | 20 | prods2011M1_I0_open_search | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)` |
| -2.11 | -1.98 | -2.11 | +1 | 5 | prods2011M1_I0_open_search | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)), 5)` |

## 共性:18 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(22 次评估)

### head score -1.80:`cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -1.80 | -1.42 | -1.80 | +0.01 | `cross_autocorr_s1(day_ar1_coefficient(Volume), 30)` |
| swap | `Volume->Amt` | -1.74 | -1.38 | -1.74 | — | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Amt)), 30)` |
| window | `cross_autocorr_s1@30->15` | -1.72 | -1.72 | -1.49 | — | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 15)` |
| window | `cross_autocorr_s1@30->60` | -1.93 | -1.22 | -1.93 | — | `cross_autocorr_s1(pow_05(day_ar1_coefficient(Volume)), 60)` |

### head score -1.98:`ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -2.02 | -1.96 | -2.02 | +0.04 | `ts_quantile_q75(day_ar1_coefficient(Volume), 50)` |
| swap | `Volume->Amt` | -2.04 | -2.04 | -1.98 | — | `ts_quantile_q75(pow_05(day_ar1_coefficient(Amt)), 50)` |
| window | `ts_quantile_q75@50->25` | -2.57 | -2.57 | -2.29 | — | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 25)` |
| window | `ts_quantile_q75@50->100` | -1.65 | -1.65 | -1.61 | — | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 100)` |

### head score -2.11:`ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50))` | -2.01 | -1.95 | -2.01 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)` | -2.01 | -1.95 | -2.01 | — | (子树本身) |
| sufficiency | `pow_05(day_ar1_coefficient(Volume))` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50))` | -2.12 | -1.98 | -2.12 | +0.00 | `ts_decay_linear(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50), 5)` |
| knockout | `ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)` | -3.41 | -2.91 | -3.41 | +1.30 | `ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)` |
| knockout | `pow_05(day_ar1_coefficient(Volume))` | -2.14 | -1.98 | -2.14 | +0.03 | `ts_decay_linear(sigmoid(ts_quantile_q75(day_ar1_coefficient(Volume), 50)), 5)` |
| swap | `Volume->Amt` | -2.13 | -2.01 | -2.13 | — | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Amt)), 50)), 5)` |
| window | `ts_decay_linear@5->2` | -2.03 | -1.96 | -2.03 | — | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)), 2)` |
| window | `ts_decay_linear@5->10` | -2.05 | -2.00 | -2.05 | — | `ts_decay_linear(sigmoid(ts_quantile_q75(pow_05(day_ar1_coefficient(Volume)), 50)), 10)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
