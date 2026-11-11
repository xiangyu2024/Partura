# 定位:种子 2073,P 组,第 1 轮(只含 train / valid)

快照:prods2073M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.21 | -1.54 | -2.21 | -1 | 20 | prods2073M1_I0_open_search | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` |
| -2.41 | -1.61 | -2.41 | -1 | 20 | prods2073M1_I0_open_search | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 60), in_sum(Low)), cross_scale(ts_scale(day_cov(Low, High), 30), 15)))` |
| -2.48 | -2.48 | -1.41 | +1 | 5 | prods2073M1_I0_open_search | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` |

## 共性:10 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(17 次评估)

### head score -2.21:`pow_05(day_max(nt_ts_stddev(Vwap, 30)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_max(nt_ts_stddev(Vwap, 30))` | -2.17 | -1.54 | -2.17 | — | (子树本身) |
| swap | `Vwap->Close` | -2.13 | -1.58 | -2.13 | — | `pow_05(day_max(nt_ts_stddev(Close, 30)))` |
| window | `nt_ts_stddev@30->15` | -2.20 | -1.59 | -2.20 | — | `pow_05(day_max(nt_ts_stddev(Vwap, 15)))` |
| window | `nt_ts_stddev@30->60` | -2.23 | -1.57 | -2.23 | — | `pow_05(day_max(nt_ts_stddev(Vwap, 60)))` |

### head score -2.41:`day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 60), in_sum(Low)), cross_scale(ts_scale(day_cov(Low, High), 30), 15)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_scale(ts_scale(day_cov(Low, High), 30), 15)` | -5.70 | -5.70 | -5.00 | — | (子树本身) |
| sufficiency | `ts_scale(day_cov(Low, High), 30)` | -3.34 | -3.34 | -3.15 | — | (子树本身) |
| sufficiency | `day_cov(Low, High)` | -2.31 | -1.56 | -2.31 | — | (子树本身) |
| knockout | `cross_scale(ts_scale(day_cov(Low, High), 30), 15)` | -2.38 | -1.61 | -2.38 | -0.03 | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 60), in_sum(Low)), ts_scale(day_cov(Low, High), 30)))` |
| knockout | `ts_scale(day_cov(Low, High), 30)` | -2.38 | -1.61 | -2.38 | -0.03 | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 60), in_sum(Low)), cross_scale(day_cov(Low, High), 15)))` |
| swap | `Close->Vwap` | -2.38 | -1.61 | -2.38 | — | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Vwap, 60), in_sum(Low)), cross_scale(ts_scale(day_cov(Low, High), 30), 15)))` |
| swap | `Low->High` | -2.37 | -1.61 | -2.37 | — | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 60), in_sum(High)), cross_scale(ts_scale(day_cov(High, High), 30), 15)))` |
| window | `nt_ts_stddev@60->30` | -2.38 | -1.61 | -2.38 | — | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 30), in_sum(Low)), cross_scale(ts_scale(day_cov(Low, High), 30), 15)))` |
| window | `nt_ts_stddev@60->120` | -2.38 | -1.61 | -2.38 | — | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 120), in_sum(Low)), cross_scale(ts_scale(day_cov(Low, High), 30), 15)))` |

### head score -2.48:`ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(nt_ts_stddev(Amt, 3))` | -3.51 | -2.96 | -3.51 | — | (子树本身) |
| swap | `Amt->Volume` | -1.27 | -1.21 | -1.27 | — | `ts_stddev(day_sum(nt_ts_stddev(Volume, 3)), 20)` |
| window | `ts_stddev@20->10` | -3.29 | -3.29 | -1.69 | — | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 10)` |
| window | `ts_stddev@20->40` | -0.96 | -0.96 | -0.85 | — | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
