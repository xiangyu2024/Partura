# 定位:种子 2076,P 组,第 1 轮(只含 train / valid)

快照:prods2076M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.25 | -0.25 | +0.07 | +1 | 0 | prods2076M1_I0_open_search | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)` |
| -0.65 | -0.65 | +0.20 | +1 | 0 | prods2076M1_I0_open_search | `cs_mask_top_replace_mean_neg(cross_max(day_quantile_q75(in_median(Low)), 15))` |
| -1.21 | -1.21 | -0.63 | +1 | 20 | prods2076M1_I0_open_search | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Amt)), 20)` |

## 共性:55 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.01 | 0.505 | 8 | -2.51 / -2.52 | `day_std(Low)` |
| -0.04 | 0.593 | 4 | -2.55 / -2.52 | `day_first(Open)` |
| -0.17 | 0.678 | 6 | -2.67 / -2.50 | `day_cov(Low, Ret)` |
| -0.38 | 0.806 | 4 | -2.87 / -2.49 | `mul(day_autocorr_n1(High), day_std(Low))` |
| -0.38 | 0.806 | 4 | -2.87 / -2.49 | `day_autocorr_n1(High)` |

## 拆解(15 次评估)

### head score -0.25:`cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10)` | -2.26 | -2.21 | -2.26 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(pow_2_5(Ret)))` | -2.90 | -2.28 | -2.90 | — | (子树本身) |
| knockout | `ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10)` | -0.31 | -0.31 | +0.22 | +0.06 | `cross_sum(day_var(pow_2_5(pow_2_5(Ret))), 241)` |
| window | `cross_sum@241->120` | -0.58 | -0.58 | +0.23 | — | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 120)` |
| window | `cross_sum@241->482` | -1.34 | -1.34 | -0.74 | — | `cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))), 10), 482)` |

### head score -0.65:`cs_mask_top_replace_mean_neg(cross_max(day_quantile_q75(in_median(Low)), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_max(day_quantile_q75(in_median(Low)), 15)` | -2.44 | -1.64 | -2.44 | — | (子树本身) |
| sufficiency | `day_quantile_q75(in_median(Low))` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `cross_max(day_quantile_q75(in_median(Low)), 15)` | -0.58 | -0.58 | +0.15 | -0.07 | `cs_mask_top_replace_mean_neg(day_quantile_q75(in_median(Low)))` |
| swap | `Low->High` | -0.64 | -0.64 | +0.25 | — | `cs_mask_top_replace_mean_neg(cross_max(day_quantile_q75(in_median(High)), 15))` |
| window | `cross_max@15->7` | -0.62 | -0.62 | +0.25 | — | `cs_mask_top_replace_mean_neg(cross_max(day_quantile_q75(in_median(Low)), 7))` |
| window | `cross_max@15->30` | -0.57 | -0.57 | +0.05 | — | `cs_mask_top_replace_mean_neg(cross_max(day_quantile_q75(in_median(Low)), 30))` |

### head score -1.21:`cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Amt)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Amt))` | -2.96 | -2.65 | -2.96 | — | (子树本身) |
| swap | `Amt->Volume` | -1.20 | -1.20 | -0.51 | — | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Volume)), 20)` |
| window | `cross_stddev@20->10` | -1.44 | -1.44 | -1.33 | — | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Amt)), 10)` |
| window | `cross_stddev@20->40` | -1.03 | -0.76 | -1.03 | — | `cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Amt)), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(window cross_stddev@20->40):`cross_stddev(day_corr(in_stddev_rolling(in_stddev_rolling(delete_open_close(Ret), 5), 5), delete_open_close(Amt)), 40)`
