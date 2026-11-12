# 定位:种子 2073,P 组,第 2 轮(只含 train / valid)

快照:prods2073M1_I0_open_search, prods2073M2_I0_open_search, prods2073Pr1a_Ea, prods2073Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.47 | -1.26 | -1.47 | -1 | 5 | prods2073M2_I0_open_search | `day_quantile_q75(cross_sum(pow_1_5(Volume), 3))` |
| -1.56 | -1.56 | -0.83 | +1 | 5 | prods2073M2_I0_open_search | `ts_max(day_corr(pow_1_5(Ret), Vwap), 40)` |
| -2.21 | -1.54 | -2.21 | -1 | 20 | prods2073M1_I0_open_search | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` |
| -2.41 | -1.60 | -2.41 | -1 | 5 | prods2073M2_I0_open_search | `pow_2(day_max(pow_1_5(Vwap)))` |
| -2.41 | -1.61 | -2.41 | -1 | 20 | prods2073M1_I0_open_search | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 60), in_sum(Low)), cross_scale(ts_scale(day_cov(Low, High), 30), 15)))` |
| -2.48 | -2.48 | -1.41 | +1 | 5 | prods2073M1_I0_open_search | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` |

## 共性:120 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.61 | 0.000 | 5 | -0.92 / -2.54 | `div(day_mean(Close), day_mean(Close))` |
| +1.61 | 0.000 | 5 | -0.92 / -2.54 | `div(day_cov(Low, High), div(day_mean(Close), day_mean(Close)))` |
| +1.54 | 0.002 | 4 | -0.98 / -2.52 | `cross_zscore(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), 120)` |
| +1.47 | 0.003 | 4 | -1.05 / -2.52 | `day_cov(Low, Close)` |
| +1.35 | 0.000 | 15 | -1.29 / -2.64 | `day_mean(Close)` |
| +1.08 | 0.010 | 5 | -1.43 / -2.52 | `day_sum(Low)` |
| +1.08 | 0.021 | 4 | -1.43 / -2.51 | `div(day_cov(Low, High), mul(day_mean(Close), day_mean(Close)))` |
| +1.08 | 0.011 | 4 | -1.43 / -2.51 | `cross_corr(day_cov(Low, High), day_sum(Amt), 60)` |
| +1.05 | 0.012 | 5 | -1.46 / -2.52 | `mul(day_mean(Close), day_mean(Close))` |
| +1.04 | 0.000 | 49 | -1.86 / -2.90 | `day_cov(Low, High)` |
| +0.89 | 0.022 | 4 | -1.61 / -2.50 | `ts_skew(day_cov(Low, High), 40)` |
| +0.58 | 0.052 | 7 | -1.92 / -2.51 | `ts_med(day_topw_mean(Ret, Volume), 10)` |
| +0.53 | 0.084 | 6 | -1.97 / -2.50 | `ts_max(ts_med(day_topw_mean(Ret, Volume), 10), 10)` |
| +0.18 | 0.503 | 4 | -2.30 / -2.48 | `cross_mean(day_sum(Amt), 30)` |
| +0.17 | 0.283 | 13 | -2.32 / -2.49 | `day_sum(Amt)` |
| +0.14 | 0.329 | 12 | -2.34 / -2.49 | `day_topw_mean(Ret, Volume)` |
| +0.14 | 0.531 | 6 | -2.34 / -2.48 | `day_topw_mean(Ret, Ret)` |
| -0.36 | 0.634 | 4 | -2.82 / -2.46 | `day_cov(Close, Close)` |
| -0.88 | 0.445 | 4 | -3.33 / -2.44 | `day_distinct_ratio(Open)` |
| -0.88 | 0.445 | 4 | -3.33 / -2.44 | `abs_(day_distinct_ratio(Open))` |

## 拆解(9 次评估)

### head score -1.47:`day_quantile_q75(cross_sum(pow_1_5(Volume), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.54 | -2.74 | -3.54 | — | `day_quantile_q75(cross_sum(pow_1_5(Amt), 3))` |
| window | `cross_sum@3->2` | -1.58 | -1.36 | -1.58 | — | `day_quantile_q75(cross_sum(pow_1_5(Volume), 2))` |
| window | `cross_sum@3->6` | -1.60 | -1.30 | -1.60 | — | `day_quantile_q75(cross_sum(pow_1_5(Volume), 6))` |

### head score -1.56:`ts_max(day_corr(pow_1_5(Ret), Vwap), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(pow_1_5(Ret), Vwap)` | -3.82 | -3.82 | -2.63 | — | (子树本身) |
| swap | `Vwap->Close` | -1.28 | -0.74 | -1.28 | — | `ts_max(day_corr(pow_1_5(Ret), Close), 40)` |
| window | `ts_max@40->20` | -1.67 | -1.67 | -0.84 | — | `ts_max(day_corr(pow_1_5(Ret), Vwap), 20)` |
| window | `ts_max@40->80` | -2.07 | -2.07 | -1.38 | — | `ts_max(day_corr(pow_1_5(Ret), Vwap), 80)` |

### head score -2.41:`pow_2(day_max(pow_1_5(Vwap)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_max(pow_1_5(Vwap))` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| swap | `Vwap->Close` | -2.37 | -1.60 | -2.37 | — | `pow_2(day_max(pow_1_5(Close)))` |

## 机械核心卡(B0 按这个顺序取)

1. `div(day_mean(Close), day_mean(Close))` — enrichment,均值差 +1.61,p 0.000
2. `div(day_cov(Low, High), div(day_mean(Close), day_mean(Close)))` — enrichment,均值差 +1.61,p 0.000
3. `cross_zscore(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), 120)` — enrichment,均值差 +1.54,p 0.002
4. `day_cov(Low, Close)` — enrichment,均值差 +1.47,p 0.003
5. `day_mean(Close)` — enrichment,均值差 +1.35,p 0.000
6. `day_sum(Low)` — enrichment,均值差 +1.08,p 0.010
7. `div(day_cov(Low, High), mul(day_mean(Close), day_mean(Close)))` — enrichment,均值差 +1.08,p 0.021
8. `cross_corr(day_cov(Low, High), day_sum(Amt), 60)` — enrichment,均值差 +1.08,p 0.011
9. `mul(day_mean(Close), day_mean(Close))` — enrichment,均值差 +1.05,p 0.012
10. `day_cov(Low, High)` — enrichment,均值差 +1.04,p 0.000
11. `ts_skew(day_cov(Low, High), 40)` — enrichment,均值差 +0.89,p 0.022
12. `ts_med(day_topw_mean(Ret, Volume), 10)` — enrichment,均值差 +0.58,p 0.052
13. `ts_max(ts_med(day_topw_mean(Ret, Volume), 10), 10)` — enrichment,均值差 +0.53,p 0.084

## 本组之前各轮的任务

- `prods2073Pr1a_Ea`:核心 `day_cov(Low, High)`;评分 90,过线 0,入 heads 0;采样计数 {'c05_no_core': 1543, 'c05_skeleton': 819}
  - score -0.66(train +0.09 valid -0.66):`cross_corr(day_cov(Low, High), cross_zscore(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), 120), 60)`
  - score -0.70(train -0.70 valid -0.12):`cross_corr(day_cov(Low, High), day_sum(Low), 60)`
  - score -0.70(train -0.70 valid -0.12):`cross_corr(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), day_sum(Low), 60)`
  - score -0.73(train +0.06 valid -0.73):`cross_corr(day_cov(Low, Close), cross_zscore(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), 120), 60)`
  - score -0.76(train -0.76 valid -0.50):`cross_corr(day_cov(Low, High), day_sum(Amt), 60)`
- `prods2073Pr1b_Nb`:核心 `—`;评分 90,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -1.50(train -1.50 valid -1.38):`cross_mean(ts_med(day_wmean(Ret, Volume), 10), 20)`
  - score -1.56(train -1.50 valid -1.56):`cross_madz(sqrt(ts_max(ts_med(day_topw_mean(Ret, Volume), 10), 10)), 241)`
  - score -1.58(train -1.58 valid -1.45):`cross_madz(sqrt(ts_max(ts_max(ts_max(ts_med(day_topw_mean(Ret, Ret), 5), 10), 5), 10)), 241)`
  - score -1.59(train -1.06 valid -1.59):`cross_madz(sqrt(ts_max(ts_max(ts_max(ts_med(day_topw_mean(Ret, Volume), 10), 10), 5), 10)), 241)`
  - score -1.66(train -1.66 valid -1.30):`cross_mean(ts_med(day_topw_mean(Ret, Volume), 10), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.28(swap Vwap->Close):`ts_max(day_corr(pow_1_5(Ret), Close), 40)`
