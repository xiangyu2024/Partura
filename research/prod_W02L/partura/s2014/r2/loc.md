# 定位:种子 2014,P 组,第 2 轮(只含 train / valid)

快照:prods2014M1_I0_open_search, prods2014M2_I0_open_search, prods2014Pr1a_Ea, prods2014Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.88 | -0.43 | -0.88 | +1 | 20 | prods2014M1_I0_open_search | `ts_std(day_quantile_q25(Ret), 5)` |
| -1.20 | -1.20 | +0.29 | +1 | 0 | prods2014M1_I0_open_search | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), 241), 5)` |
| -1.22 | -1.22 | -0.28 | +1 | 5 | prods2014M1_I0_open_search | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)), 20)` |
| -1.48 | -1.48 | -0.76 | -1 | 5 | prods2014M2_I0_open_search | `ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 40)` |
| -1.60 | -1.42 | -1.60 | -1 | 20 | prods2014M2_I0_open_search | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 5)` |
| -1.71 | -1.71 | -1.68 | +1 | 0 | prods2014M2_I0_open_search | `ts_med(ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), day_close(High), 50), 40)` |

## 共性:114 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.01 | 0.000 | 19 | -1.49 / -2.50 | `day_distinct_ratio(Open)` |
| +0.92 | 0.008 | 5 | -1.46 / -2.37 | `sub(LogTotalCap, LogFloatShares)` |
| +0.88 | 0.007 | 7 | -1.51 / -2.39 | `div(LogFloatCap, day_distinct_ratio(Open))` |
| +0.66 | 0.056 | 6 | -1.71 / -2.37 | `abs_(day_quantile_q25(Ret))` |
| +0.61 | 0.077 | 7 | -1.76 / -2.37 | `sub(LogTotalCap, LogFloatCap)` |
| +0.38 | 0.082 | 22 | -2.03 / -2.41 | `sub(LogFloatCap, LogFloatShares)` |
| +0.26 | 0.606 | 32 | -2.15 / -2.41 | `day_quantile_q25(Ret)` |
| +0.17 | 0.789 | 18 | -2.19 / -2.36 | `day_close(High)` |
| +0.17 | 0.757 | 15 | -2.19 / -2.36 | `ts_cov(day_quantile_q25(Ret), day_close(High), 50)` |
| +0.10 | 0.289 | 22 | -2.25 / -2.35 | `log(day_quantile_q25(High))` |
| +0.09 | 0.466 | 10 | -2.25 / -2.34 | `sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares))` |
| +0.06 | 0.588 | 4 | -2.28 / -2.34 | `day_distinct_ratio(Close)` |
| -0.09 | 0.808 | 4 | -2.42 / -2.33 | `ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40)` |
| -0.21 | 0.522 | 5 | -2.53 / -2.33 | `cross_delta(log(day_quantile_q25(High)), 120)` |
| -0.28 | 0.777 | 4 | -2.60 / -2.32 | `day_close(Ret)` |
| -0.40 | 0.962 | 39 | -2.60 / -2.20 | `day_quantile_q25(High)` |

## 拆解(26 次评估)

### head score -0.88:`ts_std(day_quantile_q25(Ret), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| window | `ts_std@5->2` | -1.89 | -1.81 | -1.89 | — | `ts_std(day_quantile_q25(Ret), 2)` |
| window | `ts_std@5->10` | -1.10 | -0.93 | -1.10 | — | `ts_std(day_quantile_q25(Ret), 10)` |

### head score -1.48:`ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_quantile_q25(Ret), day_close(Ret), 50)` | -1.76 | -1.76 | -1.23 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_close(Ret)` | -4.27 | -4.27 | -3.25 | — | (子树本身) |
| knockout | `ts_cov(day_quantile_q25(Ret), day_close(Ret), 50)` | — | — | — | — | `ts_med(day_quantile_q25(Ret), 40)` |
| window | `ts_med@40->20` | -1.35 | -1.35 | -1.29 | — | `ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 20)` |
| window | `ts_med@40->80` | -1.27 | -1.27 | -0.50 | — | `ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 80)` |

### head score -1.60:`ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | -2.24 | -1.15 | -2.24 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_close(High)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | -0.88 | -0.43 | -0.88 | -0.72 | `ts_stddev(day_quantile_q25(Ret), 5)` |
| swap | `High->Low` | -1.54 | -1.40 | -1.54 | — | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(Low), 50), 5)` |
| window | `ts_stddev@5->2` | -1.69 | -1.56 | -1.69 | — | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 2)` |
| window | `ts_stddev@5->10` | -1.58 | -1.58 | -1.58 | — | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 10)` |

### head score -1.71:`ts_med(ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), day_close(High), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), day_close(High), 50)` | -1.88 | -1.63 | -1.88 | — | (子树本身) |
| sufficiency | `ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40)` | -2.94 | -1.67 | -2.94 | — | (子树本身) |
| sufficiency | `ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | -2.24 | -1.15 | -2.24 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), day_close(High), 50)` | -2.83 | -1.85 | -2.83 | +1.12 | `ts_med(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), 40)` |
| knockout | `ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40)` | -1.83 | -1.83 | -1.80 | +0.12 | `ts_med(ts_cov(ts_cov(day_quantile_q25(Ret), day_close(High), 50), day_close(High), 50), 40)` |
| knockout | `ts_cov(day_quantile_q25(Ret), day_close(High), 50)` | -1.97 | -1.88 | -1.97 | +0.26 | `ts_med(ts_cov(ts_med(day_quantile_q25(Ret), 40), day_close(High), 50), 40)` |
| swap | `High->Low` | -1.72 | -1.72 | -1.70 | — | `ts_med(ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(Low), 50), 40), day_close(Low), 50), 40)` |
| window | `ts_med@40->20` | -1.78 | -1.43 | -1.78 | — | `ts_med(ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), day_close(High), 50), 20)` |
| window | `ts_med@40->80` | -1.45 | -1.44 | -1.45 | — | `ts_med(ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), day_close(High), 50), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_distinct_ratio(Open)` — enrichment,均值差 +1.01,p 0.000
2. `sub(LogTotalCap, LogFloatShares)` — enrichment,均值差 +0.92,p 0.008
3. `div(LogFloatCap, day_distinct_ratio(Open))` — enrichment,均值差 +0.88,p 0.007
4. `abs_(day_quantile_q25(Ret))` — enrichment,均值差 +0.66,p 0.056
5. `sub(LogTotalCap, LogFloatCap)` — enrichment,均值差 +0.61,p 0.077
6. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.38,p 0.082

## 本组之前各轮的任务

- `prods2014Pr1a_Ea`:核心 `day_quantile_q25(High)`;评分 105,过线 0,入 heads 0;采样计数 {'c05_no_core': 1641, 'c05_skeleton': 855}
  - score -1.36(train -1.08 valid -1.36):`cs_bucket_rank(sub(LogFloatCap, LogFloatShares), day_quantile_q25(High))`
  - score -1.44(train -1.44 valid -1.15):`sub(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), cs_bucket_rank(sub(LogFloatCap, LogFloatShares), day_q_stat_std(High)))`
  - score -1.50(train -1.45 valid -1.50):`sub(log(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares))), sub(LogFloatCap, LogFloatShares))`
  - score -1.65(train -1.65 valid -1.45):`sub(sub(log(log(day_quantile_q25(High))), sub(LogFloatCap, LogFloatShares)), sub(LogTotalCap, LogFloatCap))`
  - score -1.65(train -1.51 valid -1.65):`sub(sub(log(day_quantile_q25(High)), sub(LogFloatCap, sub(LogFloatCap, LogFloatShares))), sub(LogTotalCap, LogFloatCap))`
- `prods2014Pr1b_Nb`:核心 `—`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score -0.86(train -0.17 valid -0.86):`cs_last_low40(div(LogFloatCap, day_distinct_ratio(Open)), day_var(Low))`
  - score -0.91(train -0.15 valid -0.91):`cs_last_low40(div(LogFloatCap, day_distinct_ratio(Open)), day_var(Open))`
  - score -1.19(train -1.13 valid -1.19):`div(sub(LogTotalCap, div(LogFloatCap, day_distinct_ratio(Open))), day_distinct_ratio(Open))`
  - score -1.19(train -1.11 valid -1.19):`div(LogFloatCap, day_distinct_ratio(Open))`
  - score -1.20(train -1.20 valid -1.17):`mul(mul(abs_(day_quantile_q25(Ret)), day_distinct_ratio(Open)), day_distinct_ratio(Open))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.26(window ts_med@40->80):`ts_med(ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), day_close(High), 50), 80)`
- 增益 +0.21(window ts_med@40->80):`ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 80)`
- 增益 +0.13(window ts_med@40->20):`ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 20)`
