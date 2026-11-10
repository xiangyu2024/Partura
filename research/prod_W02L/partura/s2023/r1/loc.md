# 定位:种子 2023,P 组,第 1 轮(只含 train / valid)

快照:prods2023M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.36 | -1.16 | -1.36 | -1 | 0 | prods2023M1_I0_open_search | `ts_max(day_quantile_q75(Volume), 40)` |
| -1.48 | -1.40 | -1.48 | -1 | 5 | prods2023M1_I0_open_search | `ts_stddev(day_quantile_q75(Volume), 10)` |
| -1.56 | -1.39 | -1.56 | +1 | 5 | prods2023M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50)))` |

## 共性:37 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.81 | 0.004 | 7 | -1.99 / -2.80 | `day_quantile_q75(Volume)` |
| +0.62 | 0.131 | 4 | -2.09 / -2.71 | `day_quantile_q75(Low)` |
| +0.37 | 0.164 | 5 | -2.32 / -2.69 | `day_quantile_q75(Ret)` |
| +0.16 | 0.663 | 6 | -2.51 / -2.67 | `day_quantile_q75(Open)` |
| -0.13 | 0.720 | 6 | -2.75 / -2.62 | `day_quantile_q75(Close)` |

## 拆解(18 次评估)

### head score -1.36:`ts_max(day_quantile_q75(Volume), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q75(Volume)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.24 | -1.24 | -0.96 | — | `ts_max(day_quantile_q75(Amt), 40)` |
| window | `ts_max@40->20` | -1.79 | -1.23 | -1.79 | — | `ts_max(day_quantile_q75(Volume), 20)` |
| window | `ts_max@40->80` | -1.48 | -1.21 | -1.48 | — | `ts_max(day_quantile_q75(Volume), 80)` |

### head score -1.48:`ts_stddev(day_quantile_q75(Volume), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q75(Volume)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -4.51 | -3.03 | -4.51 | — | `ts_stddev(day_quantile_q75(Amt), 10)` |
| window | `ts_stddev@10->5` | -1.59 | -1.38 | -1.59 | — | `ts_stddev(day_quantile_q75(Volume), 5)` |
| window | `ts_stddev@10->20` | -1.69 | -1.24 | -1.69 | — | `ts_stddev(day_quantile_q75(Volume), 20)` |

### head score -1.56:`sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50))` | -1.61 | -1.39 | -1.61 | — | (子树本身) |
| sufficiency | `ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50)` | -3.20 | -2.29 | -3.20 | — | (子树本身) |
| sufficiency | `day_cov(Close, Open)` | -2.28 | -1.56 | -2.28 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `abs_(ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50))` | -3.20 | -2.29 | -3.20 | +1.64 | `sub(0.5, ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50))` |
| knockout | `ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50)` | -2.28 | -1.55 | -2.28 | +0.73 | `sub(0.5, abs_(day_cov(Close, Open)))` |
| swap | `Close->Vwap` | -1.60 | -1.41 | -1.60 | — | `sub(0.5, abs_(ts_regres(day_cov(Vwap, Open), day_quantile_q75(Volume), 50)))` |
| swap | `Open->Close` | -1.61 | -1.42 | -1.61 | — | `sub(0.5, abs_(ts_regres(day_cov(Close, Close), day_quantile_q75(Volume), 50)))` |
| window | `ts_regres@50->25` | -1.73 | -1.50 | -1.73 | — | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 25)))` |
| window | `ts_regres@50->100` | -1.65 | -1.42 | -1.65 | — | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 100)))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_quantile_q75(Volume)` — enrichment,均值差 +0.81,p 0.004

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
