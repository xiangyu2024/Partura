# 定位:种子 2021,P 组,第 1 轮(只含 train / valid)

快照:prods2021M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.20 | -1.54 | -2.20 | +1 | 5 | prods2021M1_I0_open_search | `add(div(pow_1_5(day_argmin(Amt)), day_max(High)), cross_max(day_cov(Close, Close), 15))` |
| -2.50 | -2.50 | -2.14 | +1 | 5 | prods2021M1_I0_open_search | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 20), 5)` |
| -2.90 | -2.90 | -2.89 | +1 | 5 | prods2021M1_I0_open_search | `ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 20), 5)` |

## 共性:4 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(31 次评估)

### head score -2.20:`add(div(pow_1_5(day_argmin(Amt)), day_max(High)), cross_max(day_cov(Close, Close), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(pow_1_5(day_argmin(Amt)), day_max(High))` | -2.22 | -1.58 | -2.22 | — | (子树本身) |
| sufficiency | `pow_1_5(day_argmin(Amt))` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_max(day_cov(Close, Close), 15)` | -2.41 | -1.61 | -2.41 | — | (子树本身) |
| sufficiency | `day_argmin(Amt)` | — | — | — | — | 门槛废品 |
| knockout | `div(pow_1_5(day_argmin(Amt)), day_max(High))` | -3.06 | -3.06 | -1.62 | +0.86 | `add(pow_1_5(day_argmin(Amt)), cross_max(day_cov(Close, Close), 15))` |
| knockout | `pow_1_5(day_argmin(Amt))` | -0.92 | -0.48 | -0.92 | -1.28 | `add(div(day_argmin(Amt), day_max(High)), cross_max(day_cov(Close, Close), 15))` |
| knockout | `cross_max(day_cov(Close, Close), 15)` | -2.21 | -1.81 | -2.21 | +0.01 | `add(div(pow_1_5(day_argmin(Amt)), day_max(High)), day_cov(Close, Close))` |
| swap | `Amt->Volume` | -2.17 | -1.52 | -2.17 | — | `add(div(pow_1_5(day_argmin(Volume)), day_max(High)), cross_max(day_cov(Close, Close), 15))` |
| swap | `High->Low` | -2.16 | -1.53 | -2.16 | — | `add(div(pow_1_5(day_argmin(Amt)), day_max(Low)), cross_max(day_cov(Close, Close), 15))` |
| window | `cross_max@15->7` | -2.21 | -1.59 | -2.21 | — | `add(div(pow_1_5(day_argmin(Amt)), day_max(High)), cross_max(day_cov(Close, Close), 7))` |
| window | `cross_max@15->30` | -2.20 | -1.59 | -2.20 | — | `add(div(pow_1_5(day_argmin(Amt)), day_max(High)), cross_max(day_cov(Close, Close), 30))` |

### head score -2.50:`ts_quantile_q75(ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 20), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 20)` | -2.41 | -2.41 | -2.34 | — | (子树本身) |
| sufficiency | `pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15)))` | -2.79 | -2.79 | -1.63 | — | (子树本身) |
| sufficiency | `add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))` | -2.79 | -2.79 | -1.63 | — | (子树本身) |
| sufficiency | `add(day_open(Close), pow_1_5(day_argmin(Amt)))` | -2.79 | -2.79 | -1.66 | — | (子树本身) |
| knockout | `ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 20)` | -2.68 | -2.68 | -2.03 | +0.18 | `ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 5)` |
| knockout | `pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15)))` | -2.48 | -2.48 | -2.15 | -0.02 | `ts_quantile_q75(ts_quantile_q75(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15)), 20), 5)` |
| knockout | `add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))` | -2.45 | -2.45 | -2.01 | -0.05 | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(day_open(Close), pow_1_5(day_argmin(Amt)))), 20), 5)` |
| knockout | `add(day_open(Close), pow_1_5(day_argmin(Amt)))` | -2.53 | -1.61 | -2.53 | +0.03 | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(day_open(Close), cross_max(day_cov(Close, Close), 15))), 20), 5)` |
| swap | `Close->Vwap` | -2.48 | -2.48 | -2.16 | — | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(add(day_open(Vwap), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Vwap, Vwap), 15))), 20), 5)` |
| swap | `Amt->Volume` | -2.51 | -2.51 | -2.15 | — | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Volume))), cross_max(day_cov(Close, Close), 15))), 20), 5)` |
| window | `ts_quantile_q75@5->2` | -2.44 | -2.44 | -2.29 | — | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 20), 2)` |
| window | `ts_quantile_q75@5->10` | -2.63 | -2.63 | -2.30 | — | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(add(day_open(Close), pow_1_5(day_argmin(Amt))), cross_max(day_cov(Close, Close), 15))), 20), 10)` |

### head score -2.90:`ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 20), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_var(pow_1_5(day_argmin(Amt)), 20)` | -2.97 | -2.91 | -2.97 | — | (子树本身) |
| sufficiency | `pow_1_5(day_argmin(Amt))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_argmin(Amt)` | — | — | — | — | 门槛废品 |
| knockout | `ts_var(pow_1_5(day_argmin(Amt)), 20)` | — | — | — | — | `ts_quantile_q75(pow_1_5(day_argmin(Amt)), 5)` |
| knockout | `pow_1_5(day_argmin(Amt))` | -2.80 | -2.61 | -2.80 | -0.10 | `ts_quantile_q75(ts_var(day_argmin(Amt), 20), 5)` |
| swap | `Amt->Volume` | -2.95 | -2.95 | -2.90 | — | `ts_quantile_q75(ts_var(pow_1_5(day_argmin(Volume)), 20), 5)` |
| window | `ts_quantile_q75@5->2` | -2.91 | -2.89 | -2.91 | — | `ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 20), 2)` |
| window | `ts_quantile_q75@5->10` | -2.89 | -2.89 | -2.11 | — | `ts_quantile_q75(ts_var(pow_1_5(day_argmin(Amt)), 20), 10)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
