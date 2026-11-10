# 定位:种子 2024,P 组,第 1 轮(只含 train / valid)

快照:prods2024M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.43 | -1.76 | -2.43 | -1 | 20 | prods2024M1_I0_open_search | `sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 5))), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5))` |
| -2.89 | -2.89 | -2.89 | +1 | 20 | prods2024M1_I0_open_search | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), ts_pearson(day_quantile_q75(Ret), 5))` |
| -3.87 | -3.18 | -3.87 | +1 | 20 | prods2024M1_I0_open_search | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), day_last(Amt))` |

## 共性:3 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(30 次评估)

### head score -2.43:`sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 5))), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5)` | — | — | — | — | 门槛废品 |
| sufficiency | `abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 5)))` | -2.35 | -1.79 | -2.35 | — | (子树本身) |
| sufficiency | `cs_sum(cross_product(cross_stddev(day_var(High), 60), 60))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_scale(ts_pearson(day_quantile_q75(Ret), 5))` | -2.90 | -2.90 | -2.85 | — | (子树本身) |
| knockout | `cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5)` | — | — | — | — | `sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 5))), cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)))` |
| knockout | `abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 5)))` | -2.95 | -2.95 | -2.75 | +0.52 | `sub(cs_scale(ts_pearson(day_quantile_q75(Ret), 5)), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5))` |
| knockout | `cs_sum(cross_product(cross_stddev(day_var(High), 60), 60))` | -2.10 | -2.10 | -1.52 | -0.33 | `sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 5))), cross_argmax(cross_product(cross_stddev(day_var(High), 60), 60), 5))` |
| knockout | `cs_scale(ts_pearson(day_quantile_q75(Ret), 5))` | -2.35 | -1.75 | -2.35 | -0.08 | `sub(abs_(ts_pearson(day_quantile_q75(Ret), 5)), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5))` |
| swap | `High->Low` | -2.33 | -1.74 | -2.33 | — | `sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 5))), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(Low), 60), 60)), 5))` |
| window | `ts_pearson@5->2` | -2.15 | -1.66 | -2.15 | — | `sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 2))), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5))` |
| window | `ts_pearson@5->10` | -2.02 | -2.02 | -1.85 | — | `sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 10))), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5))` |

### head score -2.89:`sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), ts_pearson(day_quantile_q75(Ret), 5))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5)))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_mean(ts_pearson(day_quantile_q75(Ret), 5))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_pearson(day_quantile_q75(Ret), 5)` | -2.89 | -2.89 | -2.85 | — | (子树本身) |
| knockout | `abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5)))` | -2.89 | -2.89 | -2.82 | -0.01 | `sub(cs_mean(ts_pearson(day_quantile_q75(Ret), 5)), ts_pearson(day_quantile_q75(Ret), 5))` |
| knockout | `cs_mean(ts_pearson(day_quantile_q75(Ret), 5))` | — | — | — | — | `sub(abs_(ts_pearson(day_quantile_q75(Ret), 5)), ts_pearson(day_quantile_q75(Ret), 5))` |
| knockout | `ts_pearson(day_quantile_q75(Ret), 5)` | -2.89 | -2.89 | -2.82 | -0.01 | `sub(abs_(cs_mean(day_quantile_q75(Ret))), ts_pearson(day_quantile_q75(Ret), 5))` |
| knockout | `ts_pearson(day_quantile_q75(Ret), 5)` | — | — | — | — | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), day_quantile_q75(Ret))` |
| window | `ts_pearson@5->2` | -2.88 | -2.88 | -2.82 | — | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 2))), ts_pearson(day_quantile_q75(Ret), 5))` |
| window | `ts_pearson@5->10` | -2.88 | -2.88 | -2.82 | — | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 10))), ts_pearson(day_quantile_q75(Ret), 5))` |

### head score -3.87:`sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), day_last(Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5)))` | — | — | — | — | 门槛废品 |
| sufficiency | `cs_mean(ts_pearson(day_quantile_q75(Ret), 5))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_pearson(day_quantile_q75(Ret), 5)` | -2.89 | -2.89 | -2.85 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5)))` | -3.83 | -3.18 | -3.83 | -0.05 | `sub(cs_mean(ts_pearson(day_quantile_q75(Ret), 5)), day_last(Amt))` |
| knockout | `cs_mean(ts_pearson(day_quantile_q75(Ret), 5))` | -3.83 | -3.21 | -3.83 | -0.04 | `sub(abs_(ts_pearson(day_quantile_q75(Ret), 5)), day_last(Amt))` |
| knockout | `ts_pearson(day_quantile_q75(Ret), 5)` | -3.83 | -3.16 | -3.83 | -0.05 | `sub(abs_(cs_mean(day_quantile_q75(Ret))), day_last(Amt))` |
| swap | `Amt->Volume` | -1.61 | -1.19 | -1.61 | — | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), day_last(Volume))` |
| window | `ts_pearson@5->2` | -3.83 | -3.19 | -3.83 | — | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 2))), day_last(Amt))` |
| window | `ts_pearson@5->10` | -3.83 | -3.18 | -3.83 | — | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 10))), day_last(Amt))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.41(window ts_pearson@5->10):`sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 10))), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5))`
- 增益 +0.28(window ts_pearson@5->2):`sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 2))), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(High), 60), 60)), 5))`
- 增益 +0.10(swap High->Low):`sub(abs_(cs_scale(ts_pearson(day_quantile_q75(Ret), 5))), cross_argmax(cs_sum(cross_product(cross_stddev(day_var(Low), 60), 60)), 5))`
