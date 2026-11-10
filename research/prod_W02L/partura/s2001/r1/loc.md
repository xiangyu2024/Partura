# 定位:种子 2001,P 组,第 1 轮(只含 train / valid)

快照:prods2001M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.11 | -1.10 | -1.11 | -1 | 5 | prods2001M1_I0_open_search | `day_max(Volume)` |
| -1.11 | -1.10 | -1.11 | -1 | 5 | prods2001M1_I0_open_search | `pow_1_5(day_max(Volume))` |
| -1.51 | -1.51 | +0.02 | +1 | 20 | prods2001M1_I0_open_search | `ts_autocorr_s1(cross_delay(ts_quantile_q50(day_max(Amt), 20), 241), 20)` |

## 共性:40 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.36 | 0.393 | 4 | -2.71 / -3.07 | `day_max(Volume)` |
| +0.35 | 0.462 | 6 | -2.74 / -3.09 | `day_max(Ret)` |
| -0.15 | 0.325 | 4 | -3.17 / -3.02 | `day_max(Vwap)` |
| -0.98 | 1.000 | 15 | -3.65 / -2.67 | `day_max(Amt)` |

## 拆解(11 次评估)

### head score -1.11:`day_max(Volume)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.66 | -3.25 | -3.66 | — | `day_max(Amt)` |

### head score -1.11:`pow_1_5(day_max(Volume))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_max(Volume)` | -1.16 | -1.10 | -1.16 | — | (子树本身) |
| swap | `Volume->Amt` | -3.66 | -3.25 | -3.66 | — | `pow_1_5(day_max(Amt))` |

### head score -1.51:`ts_autocorr_s1(cross_delay(ts_quantile_q50(day_max(Amt), 20), 241), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(ts_quantile_q50(day_max(Amt), 20), 241)` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_quantile_q50(day_max(Amt), 20)` | -3.72 | -2.99 | -3.72 | — | (子树本身) |
| sufficiency | `day_max(Amt)` | -3.66 | -3.25 | -3.66 | — | (子树本身) |
| knockout | `cross_delay(ts_quantile_q50(day_max(Amt), 20), 241)` | -2.59 | -0.67 | -2.59 | +1.08 | `ts_autocorr_s1(ts_quantile_q50(day_max(Amt), 20), 20)` |
| knockout | `ts_quantile_q50(day_max(Amt), 20)` | -2.58 | -2.58 | -0.55 | +1.07 | `ts_autocorr_s1(cross_delay(day_max(Amt), 241), 20)` |
| swap | `Amt->Volume` | -1.83 | -1.83 | -0.50 | — | `ts_autocorr_s1(cross_delay(ts_quantile_q50(day_max(Volume), 20), 241), 20)` |
| window | `ts_autocorr_s1@20->10` | -2.23 | -2.23 | -0.21 | — | `ts_autocorr_s1(cross_delay(ts_quantile_q50(day_max(Amt), 20), 241), 10)` |
| window | `ts_autocorr_s1@20->40` | -2.11 | -2.11 | -0.43 | — | `ts_autocorr_s1(cross_delay(ts_quantile_q50(day_max(Amt), 20), 241), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
