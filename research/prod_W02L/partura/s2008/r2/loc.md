# 定位:种子 2008,P 组,第 2 轮(只含 train / valid)

快照:prods2008M1_I0_open_search, prods2008M2_I0_open_search, prods2008Pr1a_Ea, prods2008Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.09 | -0.07 | -0.09 | +1 | 0 | prods2008M1_I0_open_search | `cross_stddev(ts_sum(log(day_durbin_watson(Vwap)), 10), 241)` |
| -1.10 | -1.10 | -0.69 | +1 | 0 | prods2008M2_I0_open_search | `cross_fangzheng(day_durbin_watson(Vwap), 241)` |
| -1.51 | -1.51 | -0.78 | +1 | 0 | prods2008M2_I0_open_search | `cross_fangzheng(ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10), 10)` |
| -1.69 | -1.69 | -0.21 | +1 | 5 | prods2008M1_I0_open_search | `ts_std(log(day_durbin_watson(Vwap)), 40)` |
| -1.79 | -1.79 | -1.78 | -1 | 0 | prods2008M2_I0_open_search | `ts_sum(log(log(cross_fangzheng(day_durbin_watson(Vwap), 60))), 10)` |
| -2.50 | -1.07 | -2.50 | +1 | 20 | prods2008M1_I0_open_search | `div(cross_hurst(ts_sum(log(day_durbin_watson(Vwap)), 10), 30), add(day_hurst(nt_ts_quantile_q75(High, 30)), pow_2(cs_sum(day_autocorr_n1(Amt)))))` |

## 共性:119 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.89 | 0.021 | 4 | -1.26 / -2.15 | `sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap)))` |
| +0.81 | 0.000 | 20 | -1.44 / -2.25 | `sub(LogFloatCap, LogFloatShares)` |
| +0.64 | 0.051 | 10 | -1.53 / -2.17 | `cross_stddev(log(day_durbin_watson(Vwap)), 120)` |
| +0.62 | 0.037 | 6 | -1.53 / -2.15 | `log(log(day_durbin_watson(Vwap)))` |
| +0.43 | 0.012 | 70 | -1.94 / -2.37 | `log(day_durbin_watson(Vwap))` |
| +0.42 | 0.280 | 4 | -1.71 / -2.13 | `log(day_sum(Amt))` |
| +0.42 | 0.280 | 4 | -1.71 / -2.13 | `day_sum(Amt)` |
| +0.22 | 0.532 | 8 | -1.91 / -2.13 | `day_durbin_watson(Close)` |
| +0.10 | 0.706 | 6 | -2.02 / -2.12 | `sub(log(day_durbin_watson(Close)), log(day_durbin_watson(Vwap)))` |
| +0.10 | 0.706 | 6 | -2.02 / -2.12 | `log(day_durbin_watson(Close))` |
| -0.93 | 0.940 | 4 | -3.02 / -2.09 | `cross_fangzheng(ts_sum(log(day_durbin_watson(Vwap)), 10), 10)` |
| -1.08 | 0.995 | 7 | -3.14 / -2.05 | `ts_sum(log(day_durbin_watson(Vwap)), 10)` |
| -1.60 | 1.000 | 7 | -3.63 / -2.02 | `day_durbin_watson(Volume)` |
| -1.69 | 0.998 | 4 | -3.75 / -2.06 | `log(day_durbin_watson(Volume))` |
| -1.77 | 0.999 | 4 | -3.83 / -2.06 | `cross_fangzheng(day_durbin_watson(Vwap), 10)` |

## 拆解(26 次评估)

### head score -0.09:`cross_stddev(ts_sum(log(day_durbin_watson(Vwap)), 10), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(log(day_durbin_watson(Vwap)), 10)` | -3.56 | -3.56 | -2.11 | — | (子树本身) |
| sufficiency | `log(day_durbin_watson(Vwap))` | -3.14 | -3.14 | -2.83 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `ts_sum(log(day_durbin_watson(Vwap)), 10)` | -0.93 | -0.93 | +0.07 | +0.85 | `cross_stddev(log(day_durbin_watson(Vwap)), 241)` |
| knockout | `log(day_durbin_watson(Vwap))` | -0.15 | -0.15 | -0.10 | +0.06 | `cross_stddev(ts_sum(day_durbin_watson(Vwap), 10), 241)` |
| swap | `Vwap->Close` | -0.00 | +0.05 | -0.00 | — | `cross_stddev(ts_sum(log(day_durbin_watson(Close)), 10), 241)` |
| window | `cross_stddev@241->120` | -0.60 | +0.06 | -0.60 | — | `cross_stddev(ts_sum(log(day_durbin_watson(Vwap)), 10), 120)` |
| window | `cross_stddev@241->482` | -0.92 | -0.92 | -0.55 | — | `cross_stddev(ts_sum(log(day_durbin_watson(Vwap)), 10), 482)` |

### head score -1.10:`cross_fangzheng(day_durbin_watson(Vwap), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| swap | `Vwap->Close` | -1.08 | -1.08 | -0.31 | — | `cross_fangzheng(day_durbin_watson(Close), 241)` |
| window | `cross_fangzheng@241->120` | -1.39 | -0.81 | -1.39 | — | `cross_fangzheng(day_durbin_watson(Vwap), 120)` |
| window | `cross_fangzheng@241->482` | -2.10 | -2.10 | -0.72 | — | `cross_fangzheng(day_durbin_watson(Vwap), 482)` |

### head score -1.51:`cross_fangzheng(ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10)` | -1.40 | -1.40 | -0.77 | — | (子树本身) |
| sufficiency | `cross_fangzheng(day_durbin_watson(Vwap), 241)` | -1.08 | -1.08 | -0.79 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10)` | -1.17 | -1.17 | -0.62 | -0.34 | `cross_fangzheng(cross_fangzheng(day_durbin_watson(Vwap), 241), 10)` |
| knockout | `cross_fangzheng(day_durbin_watson(Vwap), 241)` | -3.72 | -3.72 | -2.64 | +2.21 | `cross_fangzheng(ts_sum(day_durbin_watson(Vwap), 10), 10)` |
| swap | `Vwap->Close` | -1.69 | -1.69 | -0.51 | — | `cross_fangzheng(ts_sum(cross_fangzheng(day_durbin_watson(Close), 241), 10), 10)` |
| window | `cross_fangzheng@10->5` | -1.40 | -1.40 | -0.76 | — | `cross_fangzheng(ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10), 5)` |
| window | `cross_fangzheng@10->20` | -1.63 | -1.63 | -0.94 | — | `cross_fangzheng(ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10), 20)` |

### head score -1.69:`ts_std(log(day_durbin_watson(Vwap)), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(day_durbin_watson(Vwap))` | -3.14 | -3.14 | -2.83 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `log(day_durbin_watson(Vwap))` | -1.99 | -1.37 | -1.99 | +0.31 | `ts_std(day_durbin_watson(Vwap), 40)` |
| swap | `Vwap->Close` | -3.97 | -2.16 | -3.97 | — | `ts_std(log(day_durbin_watson(Close)), 40)` |
| window | `ts_std@40->20` | -2.05 | -2.05 | -0.22 | — | `ts_std(log(day_durbin_watson(Vwap)), 20)` |
| window | `ts_std@40->80` | -1.38 | -1.38 | -0.44 | — | `ts_std(log(day_durbin_watson(Vwap)), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap)))` — enrichment,均值差 +0.89,p 0.021
2. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.81,p 0.000
3. `cross_stddev(log(day_durbin_watson(Vwap)), 120)` — enrichment,均值差 +0.64,p 0.051
4. `log(log(day_durbin_watson(Vwap)))` — enrichment,均值差 +0.62,p 0.037
5. `log(day_durbin_watson(Vwap))` — enrichment,均值差 +0.43,p 0.012

## 本组之前各轮的任务

- `prods2008Pr1a_Ea`:核心 `day_durbin_watson(Vwap)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 685, 'c05_no_core': 1379}
  - score -0.06(train -0.06 valid +0.04):`cs_bucket_zscore(cross_stddev(cs_bucket_zscore(cross_stddev(log(day_durbin_watson(Vwap)), 120), LogFloatCap), 120), LogFloatCap)`
  - score -0.67(train -0.22 valid -0.67):`cross_corr(day_durbin_watson(Vwap), log(day_durbin_watson(Vwap)), 120)`
  - score -0.73(train -0.73 valid -0.02):`cs_bucket_zscore(cross_stddev(log(day_durbin_watson(Vwap)), 120), LogFloatCap)`
  - score -0.82(train -0.82 valid +0.09):`cs_bucket_zscore(cross_stddev(cs_bucket_zscore(cross_stddev(log(day_durbin_watson(Vwap)), 3), LogFloatCap), 120), LogFloatCap)`
  - score -1.14(train -0.52 valid -1.14):`cross_corr(day_durbin_watson(Vwap), log(LogFloatCap), 120)`
- `prods2008Pr1b_Nb`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.67(train -0.06 valid -0.67):`cross_regbeta(log(day_durbin_watson(Vwap)), sub(sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap))), cross_regbeta(log(day_durbin_watson(Vwap)), sub(sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap))), LogFloatShares), 241)), 241)`
  - score -0.78(train -0.78 valid -0.68):`sub(sub(LogFloatCap, LogFloatShares), log(day_durbin_watson(Vwap)))`
  - score -1.02(train -0.32 valid -1.02):`cross_regbeta(log(log(log(log(day_durbin_watson(Vwap))))), sub(LogFloatCap, LogFloatShares), 241)`
  - score -1.04(train -0.32 valid -1.04):`cross_regbeta(log(day_durbin_watson(Vwap)), sub(LogFloatCap, cross_regbeta(log(day_durbin_watson(Vwap)), sub(LogFloatCap, LogFloatShares), 241)), 241)`
  - score -1.04(train -0.40 valid -1.04):`cross_regbeta(log(pow_05(day_durbin_watson(Vwap))), sub(LogFloatCap, LogFloatShares), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.34(knockout ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10)):`cross_fangzheng(cross_fangzheng(day_durbin_watson(Vwap), 241), 10)`
- 增益 +0.31(window ts_std@40->80):`ts_std(log(day_durbin_watson(Vwap)), 80)`
- 增益 +0.11(window cross_fangzheng@10->5):`cross_fangzheng(ts_sum(cross_fangzheng(day_durbin_watson(Vwap), 241), 10), 5)`
