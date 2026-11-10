# 定位:种子 2045,P 组,第 1 轮(只含 train / valid)

快照:prods2045M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.40 | +0.40 | +0.94 | +1 | 0 | prods2045M1_I0_open_search | `add(ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 40), ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50))` |
| -0.24 | -0.24 | +0.85 | +1 | 0 | prods2045M1_I0_open_search | `ts_sum(cross_stddev(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 241), 5)` |
| -1.11 | -0.69 | -1.11 | +1 | 0 | prods2045M1_I0_open_search | `ts_std(ts_cov(day_mean(Volume), day_close(cross_delta(High, 10)), 50), 40)` |

## 共性:29 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.02 | 0.278 | 5 | -1.90 / -1.92 | `day_close(High)` |
| -0.00 | 0.346 | 4 | -1.92 / -1.92 | `day_kurt(High)` |
| -0.02 | 0.354 | 7 | -1.94 / -1.91 | `day_close(cross_delta(High, 10))` |
| -0.10 | 0.464 | 4 | -2.01 / -1.91 | `ts_cov(day_quantile_q25(Ret), day_close(cross_delta(High, 10)), 50)` |
| -0.13 | 0.556 | 5 | -2.03 / -1.90 | `day_close(cross_delta(High, 30))` |
| -0.40 | 0.759 | 5 | -2.25 / -1.85 | `day_quantile_q25(Ret)` |

## 拆解(26 次评估)

### head score +0.40:`add(ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 40), ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50)` | +0.47 | +0.47 | +1.26 | — | (子树本身) |
| sufficiency | `ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 40)` | -3.15 | -2.38 | -3.15 | — | (子树本身) |
| sufficiency | `cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60)` | -0.03 | -0.03 | -0.03 | — | (子树本身) |
| sufficiency | `day_cov(Amt, cross_delta(Amt, 30))` | -4.19 | -3.52 | -4.19 | — | (子树本身) |
| knockout | `ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50)` | -0.10 | -0.08 | -0.10 | +0.50 | `add(ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 40), cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60))` |
| knockout | `ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 40)` | +0.58 | +0.58 | +1.12 | -0.18 | `add(day_cov(Amt, cross_delta(Amt, 30)), ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50))` |
| knockout | `cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60)` | -0.33 | -0.17 | -0.33 | +0.73 | `add(ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 40), ts_std(day_cov(Amt, cross_delta(Amt, 30)), 50))` |
| swap | `Amt->Volume` | -2.02 | -1.06 | -2.02 | — | `add(ts_quantile_q50(day_cov(Volume, cross_delta(Volume, 30)), 40), ts_std(cross_stddev(day_cov(Volume, cross_delta(Volume, 30)), 60), 50))` |
| window | `ts_quantile_q50@40->20` | +0.48 | +0.48 | +1.19 | — | `add(ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 20), ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50))` |
| window | `ts_quantile_q50@40->80` | +0.39 | +0.39 | +0.90 | — | `add(ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 80), ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50))` |

### head score -0.24:`ts_sum(cross_stddev(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 241), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 241)` | -0.18 | -0.18 | +0.87 | — | (子树本身) |
| sufficiency | `cross_max(day_cov(cross_delta(Amt, 241), Amt), 3)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_cov(cross_delta(Amt, 241), Amt)` | — | — | — | — | 门槛废品 |
| knockout | `cross_stddev(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 241)` | — | — | — | — | `ts_sum(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 5)` |
| knockout | `cross_max(day_cov(cross_delta(Amt, 241), Amt), 3)` | -0.08 | -0.08 | +0.86 | -0.16 | `ts_sum(cross_stddev(day_cov(cross_delta(Amt, 241), Amt), 241), 5)` |
| swap | `Amt->Volume` | -2.20 | -2.07 | -2.20 | — | `ts_sum(cross_stddev(cross_max(day_cov(cross_delta(Volume, 241), Volume), 3), 241), 5)` |
| window | `ts_sum@5->2` | -0.16 | -0.16 | +0.87 | — | `ts_sum(cross_stddev(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 241), 2)` |
| window | `ts_sum@5->10` | -0.40 | -0.40 | +0.75 | — | `ts_sum(cross_stddev(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 241), 10)` |

### head score -1.11:`ts_std(ts_cov(day_mean(Volume), day_close(cross_delta(High, 10)), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_mean(Volume), day_close(cross_delta(High, 10)), 50)` | -1.27 | -0.79 | -1.27 | — | (子树本身) |
| sufficiency | `day_close(cross_delta(High, 10))` | -4.00 | -3.83 | -4.00 | — | (子树本身) |
| sufficiency | `day_mean(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| knockout | `ts_cov(day_mean(Volume), day_close(cross_delta(High, 10)), 50)` | -1.22 | -1.05 | -1.22 | +0.11 | `ts_std(day_mean(Volume), 40)` |
| swap | `Volume->Amt` | -1.38 | -1.38 | -0.65 | — | `ts_std(ts_cov(day_mean(Amt), day_close(cross_delta(High, 10)), 50), 40)` |
| swap | `High->Low` | -1.10 | -0.67 | -1.10 | — | `ts_std(ts_cov(day_mean(Volume), day_close(cross_delta(Low, 10)), 50), 40)` |
| window | `ts_std@40->20` | -1.12 | -0.62 | -1.12 | — | `ts_std(ts_cov(day_mean(Volume), day_close(cross_delta(High, 10)), 50), 20)` |
| window | `ts_std@40->80` | -1.11 | -0.38 | -1.11 | — | `ts_std(ts_cov(day_mean(Volume), day_close(cross_delta(High, 10)), 50), 80)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
