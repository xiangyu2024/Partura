# 定位:种子 807,P 组,第 2 轮(只含 train / valid)

快照:c07s807M1_I0_open_search, c07s807M2_I0_open_search, c08s807Pr1a_Ea, c08s807Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.43 | +1.43 | +2.97 | +1 | 0 | c07s807M1_I0_open_search | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 60)` |
| +1.05 | +1.31 | +1.05 | +1 | 5 | c07s807M1_I0_open_search | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 60)` |
| +0.91 | +1.11 | +0.91 | -1 | 20 | c07s807M1_I0_open_search | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 241)` |
| +0.84 | +0.84 | +1.63 | -1 | 0 | c08s807Pr1b_Nb | `cross_stddev(log(log(log(day_std(Ret)))), 120)` |
| +0.79 | +0.89 | +0.79 | +1 | 5 | c08s807Pr1a_Ea | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)` |
| +0.69 | +1.18 | +0.69 | +1 | 5 | c08s807Pr1a_Ea | `cross_corr(ts_var(ts_var(LogFloatCap, 20), 20), log(day_sum(Amt)), 60)` |

## 共性:345 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.99 | 0.000 | 6 | +0.62 / -1.36 | `log(log(log(day_std(Ret))))` |
| +1.66 | 0.001 | 5 | +0.30 / -1.35 | `cs_mean(day_median(Close))` |
| +1.39 | 0.001 | 6 | +0.04 / -1.35 | `ts_var(LogFloatCap, 40)` |
| +1.26 | 0.000 | 17 | -0.13 / -1.39 | `log(log(day_std(Ret)))` |
| +1.19 | 0.002 | 9 | -0.17 / -1.36 | `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), LimitWidth)` |
| +1.18 | 0.000 | 20 | -0.22 / -1.40 | `log(day_std(Ret))` |
| +1.04 | 0.025 | 6 | -0.31 / -1.35 | `cross_stddev(log(log(day_std(Ret))), 120)` |
| +1.02 | 0.000 | 66 | -0.51 / -1.52 | `day_quantile_q75(Volume)` |
| +0.95 | 0.000 | 25 | -0.45 / -1.40 | `day_std(Ret)` |
| +0.92 | 0.000 | 60 | -0.57 / -1.49 | `cs_median(day_pos_ratio(Open))` |
| +0.92 | 0.000 | 60 | -0.57 / -1.49 | `day_pos_ratio(Open)` |
| +0.81 | 0.004 | 16 | -0.56 / -1.37 | `ts_var(LogFloatCap, 50)` |
| +0.76 | 0.012 | 13 | -0.60 / -1.36 | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 50))` |
| +0.74 | 0.000 | 39 | -0.67 / -1.41 | `cs_median(LimitWidth)` |
| +0.73 | 0.027 | 7 | -0.62 / -1.34 | `day_median(Close)` |
| +0.69 | 0.002 | 32 | -0.71 / -1.39 | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20))` |
| +0.66 | 0.216 | 4 | -0.68 / -1.34 | `cross_max(day_sum(Amt), 60)` |
| +0.66 | 0.216 | 4 | -0.68 / -1.34 | `log(cross_max(day_sum(Amt), 60))` |
| +0.60 | 0.167 | 6 | -0.73 / -1.34 | `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), signedpower(cs_median(LimitWidth)))` |
| +0.60 | 0.226 | 4 | -0.74 / -1.34 | `ts_cov(LogFloatCap, day_wmean(Ret, Volume), 1)` |

## 拆解(29 次评估)

### head score +1.43:`cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth)` | -0.86 | -0.86 | +0.45 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Amt)` | -3.22 | -3.22 | -2.02 | — | (子树本身) |
| sufficiency | `ts_var(LogFloatCap, 20)` | -2.71 | -2.71 | -1.62 | — | (子树本身) |
| knockout | `cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth)` | +1.42 | +1.42 | +2.75 | +0.00 | `cross_regbeta(day_quantile_q75(Amt), ts_var(LogFloatCap, 20), 60)` |
| knockout | `ts_var(LogFloatCap, 20)` | +0.47 | +0.47 | +0.82 | +0.95 | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(LogFloatCap, LimitWidth), 60)` |
| swap | `Amt->Volume` | +1.02 | +1.20 | +1.02 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 60)` |
| window | `cross_regbeta@60->30` | +1.11 | +1.11 | +3.06 | — | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 30)` |
| window | `cross_regbeta@60->120` | +1.70 | +1.70 | +2.89 | — | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 120)` |

### head score +1.05:`cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth)` | -1.46 | -1.46 | +0.33 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Volume)` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_var(LogTotalCap, 30)` | -2.54 | -2.54 | -0.69 | — | (子树本身) |
| knockout | `cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth)` | +0.24 | +0.94 | +0.24 | +0.81 | `cross_regbeta(day_quantile_q75(Volume), ts_var(LogTotalCap, 30), 60)` |
| knockout | `ts_var(LogTotalCap, 30)` | -1.66 | +0.33 | -1.66 | +2.71 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(LogTotalCap, LimitWidth), 60)` |
| swap | `Volume->Amt` | +1.63 | +1.63 | +2.16 | — | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 60)` |
| window | `cross_regbeta@60->30` | +0.73 | +0.73 | +1.37 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 30)` |
| window | `cross_regbeta@60->120` | +0.79 | +1.41 | +0.79 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 120)` |

### head score +0.84:`cross_stddev(log(log(log(day_std(Ret)))), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(log(log(day_std(Ret))))` | -3.79 | -3.00 | -3.79 | — | (子树本身) |
| sufficiency | `log(log(day_std(Ret)))` | -3.79 | -3.00 | -3.79 | — | (子树本身) |
| sufficiency | `log(day_std(Ret))` | -3.80 | -3.00 | -3.80 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -3.94 | -3.59 | -3.94 | — | (子树本身) |
| knockout | `log(log(log(day_std(Ret))))` | +0.53 | +0.53 | +1.45 | +0.31 | `cross_stddev(log(log(day_std(Ret))), 120)` |
| window | `cross_stddev@120->60` | +0.25 | +0.25 | +0.67 | — | `cross_stddev(log(log(log(day_std(Ret)))), 60)` |
| window | `cross_stddev@120->240` | +0.76 | +1.07 | +0.76 | — | `cross_stddev(log(log(log(day_std(Ret)))), 240)` |

### head score +0.79:`cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_var(LogFloatCap, 20)` | -2.71 | -2.71 | -1.62 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `ts_var(LogFloatCap, 20)` | -1.18 | -1.18 | -0.09 | +1.97 | `cross_corr(LogFloatCap, day_sum(Amt), 60)` |
| swap | `Amt->Volume` | +1.13 | +1.13 | +1.20 | — | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)` |
| window | `cross_corr@60->30` | +0.77 | +0.82 | +0.77 | — | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 30)` |
| window | `cross_corr@60->120` | +0.67 | +0.67 | +0.81 | — | `cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 120)` |

## 机械核心卡(B0 按这个顺序取)

1. `log(log(log(day_std(Ret))))` — enrichment,均值差 +1.99,p 0.000
2. `cs_mean(day_median(Close))` — enrichment,均值差 +1.66,p 0.001
3. `ts_var(LogFloatCap, 40)` — enrichment,均值差 +1.39,p 0.001
4. `log(log(day_std(Ret)))` — enrichment,均值差 +1.26,p 0.000
5. `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), LimitWidth)` — enrichment,均值差 +1.19,p 0.002
6. `log(day_std(Ret))` — enrichment,均值差 +1.18,p 0.000
7. `cross_stddev(log(log(day_std(Ret))), 120)` — enrichment,均值差 +1.04,p 0.025
8. `day_quantile_q75(Volume)` — enrichment,均值差 +1.02,p 0.000
9. `day_std(Ret)` — enrichment,均值差 +0.95,p 0.000
10. `cs_median(day_pos_ratio(Open))` — enrichment,均值差 +0.92,p 0.000
11. `day_pos_ratio(Open)` — enrichment,均值差 +0.92,p 0.000
12. `ts_var(LogFloatCap, 50)` — enrichment,均值差 +0.81,p 0.004
13. `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 50))` — enrichment,均值差 +0.76,p 0.012
14. `cs_median(LimitWidth)` — enrichment,均值差 +0.74,p 0.000
15. `day_median(Close)` — enrichment,均值差 +0.73,p 0.027
16. `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20))` — enrichment,均值差 +0.69,p 0.002
17. `day_skew(Open)` — enrichment,均值差 +0.60,p 0.044
18. `signedpower(cs_median(LimitWidth))` — enrichment,均值差 +0.55,p 0.013
19. `day_sum(Amt)` — enrichment,均值差 +0.54,p 0.010
20. `ts_var(LogFloatCap, 20)` — enrichment,均值差 +0.53,p 0.000
21. `log(day_sum(Amt))` — enrichment,均值差 +0.40,p 0.079

## 本组之前各轮的任务

- `c08s807Pr1a_Ea`:核心 `ts_var(LogFloatCap, 20)`;评分 82,过线 5,入 heads 2;采样计数 {'c05_no_core': 966, 'mutation_refused': 4, 'c05_periphery_seen': 7}
  - score +0.79(train +0.89 valid +0.79):`cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 60)`
  - score +0.77(train +0.80 valid +0.77):`cross_corr(ts_var(LogFloatCap, 20), day_sum(Amt), 30)`
  - score +0.71(train +0.72 valid +0.71):`cross_corr(ts_var(LogFloatCap, 20), log(log(day_sum(Amt))), 60)`
  - score +0.69(train +1.18 valid +0.69):`cross_corr(ts_var(ts_var(LogFloatCap, 20), 20), log(day_sum(Amt)), 60)`
  - score +0.60(train +0.71 valid +0.60):`cross_corr(ts_var(LogFloatCap, 20), log(day_sum(Amt)), 60)`
- `c08s807Pr1b_Nb`:核心 `—`;评分 80,过线 10,入 heads 1;采样计数 {}
  - score +0.84(train +0.84 valid +1.63):`cross_stddev(log(log(log(day_std(Ret)))), 120)`
  - score +0.80(train +0.80 valid +1.67):`cross_tail_mean_q75(cross_stddev(log(log(log(day_std(Ret)))), 120), 3)`
  - score +0.80(train +0.80 valid +1.95):`cross_tail_mean_q75(cross_stddev(log(log(log(log(day_std(Ret))))), 120), 3)`
  - score +0.76(train +0.76 valid +1.96):`cross_stddev(log(log(log(log(day_std(Ret))))), 120)`
  - score +0.59(train +0.59 valid +0.91):`log(cross_stddev(log(log(day_std(Ret))), 120))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.58(swap Volume->Amt):`cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogTotalCap, 30), LimitWidth), 60)`
- 增益 +0.34(swap Amt->Volume):`cross_corr(ts_var(LogFloatCap, 20), day_sum(Volume), 60)`
- 增益 +0.27(window cross_regbeta@60->120):`cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(ts_var(LogFloatCap, 20), LimitWidth), 120)`
