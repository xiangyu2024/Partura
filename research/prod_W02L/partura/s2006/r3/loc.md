# 定位:种子 2006,P 组,第 3 轮(只含 train / valid)

快照:prods2006M1_I0_open_search, prods2006M2_I0_open_search, prods2006M3_I0_open_search, prods2006Pr2a_Ea, prods2006Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.03 | +0.03 | +1.52 | -1 | 20 | prods2006M1_I0_open_search | `sub(0.5, cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30)), LogFloatCap))` |
| +0.01 | +0.01 | +0.28 | +1 | 0 | prods2006M3_I0_open_search | `ts_std(cross_stddev(ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50), 60), 50)` |
| -0.03 | -0.03 | +0.84 | +1 | 0 | prods2006M3_I0_open_search | `ts_sum(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` |
| -0.15 | -0.15 | +0.94 | +1 | 0 | prods2006M3_I0_open_search | `ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50)` |
| -1.41 | -1.41 | -1.28 | -1 | 5 | prods2006M2_I0_open_search | `cs_bucket_zscore(cross_min(cross_min(day_cov(Low, Ret), 15), 15), sub(LogFloatCap, LogFloatShares))` |
| -1.44 | -1.27 | -1.44 | +1 | 5 | prods2006M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Ret, Amt), day_last(Volume), 50)))` |
| -1.51 | -1.27 | -1.51 | +1 | 5 | prods2006M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Amt, Vwap), day_last(Volume), 50)))` |
| -1.63 | -1.63 | -1.63 | +1 | 0 | prods2006M2_I0_open_search | `cross_sum(cross_sum(neg(cross_cov(cross_min(day_cov(Low, Ret), 15), mul(day_autocorr_n1(High), day_std(Low)), 10)), 30), 60)` |
| -1.72 | -1.72 | -1.53 | -1 | 5 | prods2006M2_I0_open_search | `cross_min(cross_cov(cross_min(cross_min(day_cov(Low, Ret), 15), 15), mul(day_autocorr_n1(High), day_std(Low)), 10), 15)` |

## 共性:77 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.18 | 0.000 | 9 | -0.47 / -2.65 | `cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241)` |
| +2.18 | 0.000 | 9 | -0.47 / -2.65 | `cross_max(day_cov(Amt, Amt), 3)` |
| +1.98 | 0.000 | 11 | -0.70 / -2.68 | `day_cov(Amt, Amt)` |
| +1.17 | 0.002 | 6 | -1.31 / -2.49 | `day_cov(Amt, Open)` |
| +0.82 | 0.052 | 10 | -1.68 / -2.50 | `day_at_max_ratio(Vwap)` |
| +0.81 | 0.067 | 5 | -1.63 / -2.45 | `mul(mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap))` |
| +0.81 | 0.058 | 9 | -1.68 / -2.49 | `mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap))` |
| +0.68 | 0.009 | 13 | -1.83 / -2.51 | `day_last(Volume)` |
| +0.66 | 0.107 | 13 | -1.85 / -2.51 | `day_autocorr_n1(Open)` |
| +0.15 | 0.613 | 12 | -2.27 / -2.42 | `day_cov(Low, Ret)` |
| +0.13 | 0.609 | 9 | -2.28 / -2.41 | `cross_min(day_cov(Low, Ret), 15)` |
| -0.02 | 0.613 | 4 | -2.41 / -2.39 | `day_autocorr_n1(High)` |
| -0.50 | 0.751 | 4 | -2.87 / -2.37 | `day_cov(Open, Open)` |

## 拆解(42 次评估)

### head score +0.03:`sub(0.5, cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30)), LogFloatCap))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30)), LogFloatCap)` | +0.03 | +0.03 | +1.52 | — | (子树本身) |
| sufficiency | `cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30))` | -0.21 | -0.21 | +1.46 | — | (子树本身) |
| sufficiency | `abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200))` | -0.24 | -0.24 | +0.98 | — | (子树本身) |
| sufficiency | `ts_regres(day_cov(Amt, Open), day_last(Amt), 200)` | -2.63 | -2.63 | -1.26 | — | (子树本身) |
| knockout | `cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30)), LogFloatCap)` | -0.21 | -0.21 | +1.46 | +0.24 | `sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30)))` |
| knockout | `cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), cross_mean(day_std(Amt), 30))` | -0.06 | -0.06 | +1.08 | +0.09 | `sub(0.5, cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200)), LogFloatCap))` |
| knockout | `abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 200))` | -2.04 | -2.04 | -0.89 | +2.07 | `sub(0.5, cs_bucket_zscore(cs_bucket_zscore(ts_regres(day_cov(Amt, Open), day_last(Amt), 200), cross_mean(day_std(Amt), 30)), LogFloatCap))` |
| knockout | `ts_regres(day_cov(Amt, Open), day_last(Amt), 200)` | -2.44 | -2.44 | -2.18 | +2.48 | `sub(0.5, cs_bucket_zscore(cs_bucket_zscore(abs_(day_cov(Amt, Open)), cross_mean(day_std(Amt), 30)), LogFloatCap))` |
| swap | `Amt->Volume` | -0.89 | -0.89 | +1.32 | — | `sub(0.5, cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Volume, Open), day_last(Volume), 200)), cross_mean(day_std(Volume), 30)), LogFloatCap))` |
| swap | `Open->Close` | -0.07 | -0.07 | +1.52 | — | `sub(0.5, cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Close), day_last(Amt), 200)), cross_mean(day_std(Amt), 30)), LogFloatCap))` |
| window | `ts_regres@200->100` | -0.02 | -0.01 | -0.02 | — | `sub(0.5, cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100)), cross_mean(day_std(Amt), 30)), LogFloatCap))` |
| window | `ts_regres@200->400` | +0.33 | +0.33 | +1.55 | — | `sub(0.5, cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 400)), cross_mean(day_std(Amt), 30)), LogFloatCap))` |

### head score +0.01:`ts_std(cross_stddev(ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50), 60), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50), 60)` | -0.15 | -0.15 | +0.52 | — | (子树本身) |
| sufficiency | `ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50)` | -0.15 | -0.15 | +0.98 | — | (子树本身) |
| sufficiency | `cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60)` | +0.33 | +0.33 | +1.14 | — | (子树本身) |
| sufficiency | `ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | -0.67 | -0.67 | +0.20 | — | (子树本身) |
| knockout | `cross_stddev(ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50), 60)` | -0.34 | -0.34 | +0.39 | +0.35 | `ts_std(ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50), 50)` |
| knockout | `ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50)` | -0.04 | -0.04 | +0.56 | +0.06 | `ts_std(cross_stddev(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 60), 50)` |
| knockout | `cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60)` | -0.25 | -0.25 | +0.34 | +0.26 | `ts_std(cross_stddev(ts_std(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 50), 60), 50)` |
| knockout | `ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | -0.40 | -0.23 | -0.40 | +0.41 | `ts_std(cross_stddev(ts_std(cross_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 60), 50), 60), 50)` |
| swap | `Amt->Volume` | -2.46 | -1.82 | -2.46 | — | `ts_std(cross_stddev(ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Volume, Volume), 3), 241), 5), 60), 50), 60), 50)` |
| window | `ts_std@50->25` | +0.18 | +0.19 | +0.18 | — | `ts_std(cross_stddev(ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50), 60), 25)` |
| window | `ts_std@50->100` | -0.42 | -0.42 | -0.19 | — | `ts_std(cross_stddev(ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50), 60), 100)` |

### head score -0.03:`ts_sum(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241)` | +0.14 | +0.14 | +0.89 | — | (子树本身) |
| sufficiency | `cross_max(day_cov(Amt, Amt), 3)` | -3.83 | -3.22 | -3.83 | — | (子树本身) |
| sufficiency | `day_cov(Amt, Amt)` | -3.75 | -2.98 | -3.75 | — | (子树本身) |
| knockout | `cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241)` | -4.38 | -3.32 | -4.38 | +4.34 | `ts_sum(cross_max(day_cov(Amt, Amt), 3), 5)` |
| knockout | `cross_max(day_cov(Amt, Amt), 3)` | +0.00 | +0.00 | +0.92 | -0.04 | `ts_sum(cross_fangzheng(day_cov(Amt, Amt), 241), 5)` |
| swap | `Amt->Volume` | -2.27 | -1.60 | -2.27 | — | `ts_sum(cross_fangzheng(cross_max(day_cov(Volume, Volume), 3), 241), 5)` |
| window | `ts_sum@5->2` | +0.14 | +0.14 | +0.86 | — | `ts_sum(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 2)` |
| window | `ts_sum@5->10` | -0.15 | -0.15 | +0.74 | — | `ts_sum(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 10)` |

### head score -0.15:`ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60)` | +0.33 | +0.33 | +1.14 | — | (子树本身) |
| sufficiency | `ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | -0.67 | -0.67 | +0.20 | — | (子树本身) |
| sufficiency | `cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241)` | +0.14 | +0.14 | +0.89 | — | (子树本身) |
| sufficiency | `cross_max(day_cov(Amt, Amt), 3)` | -3.83 | -3.22 | -3.83 | — | (子树本身) |
| knockout | `cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60)` | +0.41 | +0.41 | +1.52 | -0.56 | `ts_std(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 50)` |
| knockout | `ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | -0.39 | -0.39 | +0.45 | +0.24 | `ts_std(cross_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 60), 50)` |
| knockout | `cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241)` | +0.36 | +0.36 | +0.98 | -0.51 | `ts_std(cross_stddev(ts_stddev(cross_max(day_cov(Amt, Amt), 3), 5), 60), 50)` |
| knockout | `cross_max(day_cov(Amt, Amt), 3)` | -0.02 | -0.02 | +1.17 | -0.13 | `ts_std(cross_stddev(ts_stddev(cross_fangzheng(day_cov(Amt, Amt), 241), 5), 60), 50)` |
| swap | `Amt->Volume` | -1.41 | -0.93 | -1.41 | — | `ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Volume, Volume), 3), 241), 5), 60), 50)` |
| window | `ts_std@50->25` | -0.24 | -0.24 | +1.66 | — | `ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 25)` |
| window | `ts_std@50->100` | -0.20 | -0.20 | +0.51 | — | `ts_std(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5), 60), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241)` — enrichment,均值差 +2.18,p 0.000
2. `cross_max(day_cov(Amt, Amt), 3)` — enrichment,均值差 +2.18,p 0.000
3. `day_cov(Amt, Amt)` — enrichment,均值差 +1.98,p 0.000
4. `day_cov(Amt, Open)` — enrichment,均值差 +1.17,p 0.002
5. `day_at_max_ratio(Vwap)` — enrichment,均值差 +0.82,p 0.052
6. `mul(mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap))` — enrichment,均值差 +0.81,p 0.067
7. `mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap))` — enrichment,均值差 +0.81,p 0.058
8. `day_last(Volume)` — enrichment,均值差 +0.68,p 0.009

## 本组之前各轮的任务

- `prods2006Pr2a_Ea`:核心 `abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 100))`;评分 53,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3457, 'c05_no_core': 5464}
  - score -2.31(train -2.31 valid -2.24):`day_q_stat_std(Amt)`
  - score -2.36(train -2.36 valid -2.21):`day_q_stat_std(Volume)`
  - score -2.68(train -2.42 valid -2.68):`day_es_ratio_hi(Open)`
  - score -2.75(train -2.75 valid -2.58):`day_es_ratio_lo(Close)`
  - score -2.77(train -2.19 valid -2.77):`day_min(Ret)`
- `prods2006Pr2b_Nb`:核心 `—`;评分 56,过线 0,入 heads 0;采样计数 {'c05_skeleton': 11}
  - score -1.58(train -1.58 valid -0.66):`pow_05(log(mul(mul(mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap))))`
  - score -1.65(train -1.65 valid -0.72):`pow_05(pow_3(log(mul(mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap)))))`
  - score -1.65(train -1.65 valid -0.72):`pow_05(sigmoid(log(mul(mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap)))))`
  - score -1.65(train -1.65 valid -0.72):`log(mul(mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap)))`
  - score -1.65(train -1.65 valid -0.72):`pow_05(log(mul(mul(day_autocorr_n1(Open), day_at_max_ratio(Vwap)), day_at_max_ratio(Vwap))))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.29(window ts_regres@200->400):`sub(0.5, cs_bucket_zscore(cs_bucket_zscore(abs_(ts_regres(day_cov(Amt, Open), day_last(Amt), 400)), cross_mean(day_std(Amt), 30)), LogFloatCap))`
