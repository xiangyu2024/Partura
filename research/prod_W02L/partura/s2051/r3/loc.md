# 定位:种子 2051,P 组,第 3 轮(只含 train / valid)

快照:prods2051M1_I0_open_search, prods2051M2_I0_open_search, prods2051M3_I0_open_search, prods2051Pr1a_Na, prods2051Pr1b_Nb, prods2051Pr2a_Ea, prods2051Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(11 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.00 | +1.47 | +1.00 | +1 | 5 | prods2051Pr2a_Ea | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 60)` |
| +0.65 | +1.56 | +0.65 | +1 | 5 | prods2051Pr2a_Ea | `cross_regbeta(day_sum(Volume), day_kurt(Volume), 60)` |
| -0.58 | -0.58 | -0.53 | +1 | 20 | prods2051M1_I0_open_search | `day_skew(nt_ts_kurt(Low, 10))` |
| -1.70 | -1.70 | -1.35 | +1 | 20 | prods2051M3_I0_open_search | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60), 5), 5), 30)` |
| -1.87 | -1.86 | -1.87 | +1 | 20 | prods2051M1_I0_open_search | `day_max(nt_ts_kurt(Vwap, 10))` |
| -2.13 | -2.13 | -1.47 | +1 | 20 | prods2051M3_I0_open_search | `ts_max(cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50), 60), 5)` |
| -2.23 | -2.23 | -1.67 | +1 | 20 | prods2051M3_I0_open_search | `cross_med(cross_med(day_ar1_coefficient(Close), 60), 60)` |
| -2.23 | -2.23 | -1.00 | -1 | 20 | prods2051M2_I0_open_search | `pow_05(day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 15)))))` |
| -2.80 | -2.80 | -1.19 | -1 | 20 | prods2051M2_I0_open_search | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 10))))` |
| -2.86 | -2.86 | -1.32 | -1 | 20 | prods2051M2_I0_open_search | `day_max(pow_1_5(pow_2(nt_ts_kurt(Vwap, 30))))` |
| -2.95 | -2.95 | -1.89 | -1 | 20 | prods2051M1_I0_open_search | `day_max(nt_ts_kurt(Vwap, 30))` |

## 共性:285 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.07 | 0.001 | 4 | +0.00 / -2.07 | `day_std(abs_(Close))` |
| +1.39 | 0.004 | 4 | -0.67 / -2.06 | `day_argmax(Volume)` |
| +0.79 | 0.042 | 7 | -1.27 / -2.06 | `day_min(cross_argmax(Volume, 30))` |
| +0.75 | 0.018 | 9 | -1.31 / -2.06 | `day_min(Vwap)` |
| +0.75 | 0.051 | 6 | -1.31 / -2.06 | `cross_mean(mul(day_sum(Ret), cross_zscore(day_sum(Amt), 20)), 60)` |
| +0.73 | 0.049 | 6 | -1.32 / -2.05 | `day_min(Close)` |
| +0.67 | 0.017 | 13 | -1.40 / -2.07 | `day_open(Open)` |
| +0.62 | 0.127 | 4 | -1.43 / -2.05 | `cross_argmax(day_sum(Volume), 60)` |
| +0.61 | 0.000 | 82 | -1.61 / -2.21 | `day_kurt(Volume)` |
| +0.56 | 0.004 | 45 | -1.56 / -2.13 | `day_sum(Volume)` |
| +0.56 | 0.082 | 8 | -1.49 / -2.05 | `day_std(in_top_quantile_flag_q10(Vwap))` |
| +0.45 | 0.043 | 28 | -1.64 / -2.08 | `day_sum(Amt)` |
| +0.40 | 0.124 | 13 | -1.66 / -2.06 | `mul(day_sum(Ret), cross_zscore(day_sum(Amt), 20))` |
| +0.35 | 0.011 | 62 | -1.76 / -2.12 | `day_sum(Ret)` |
| +0.33 | 0.245 | 7 | -1.72 / -2.05 | `cross_argmax(day_sum(Ret), 60)` |
| +0.32 | 0.141 | 21 | -1.75 / -2.06 | `cross_zscore(day_sum(Amt), 20)` |
| +0.18 | 0.346 | 5 | -1.86 / -2.04 | `day_kurt(Vwap)` |
| +0.17 | 0.276 | 10 | -1.87 / -2.05 | `day_var(Open)` |
| +0.12 | 0.403 | 15 | -1.92 / -2.05 | `day_argmax(Vwap)` |
| +0.10 | 0.443 | 6 | -1.95 / -2.04 | `cross_corr(day_sum(Ret), day_sum(Volume), 120)` |

## 拆解(32 次评估)

### head score +1.00:`cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_mean(day_kurt(Volume), 5)` | -4.29 | -3.92 | -4.29 | — | (子树本身) |
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_kurt(Volume)` | -4.93 | -4.22 | -4.93 | — | (子树本身) |
| knockout | `ts_mean(day_kurt(Volume), 5)` | +0.65 | +1.56 | +0.65 | +0.35 | `cross_regbeta(day_sum(Volume), day_kurt(Volume), 60)` |
| swap | `Volume->Amt` | +0.74 | +1.49 | +0.74 | — | `cross_regbeta(day_sum(Amt), ts_mean(day_kurt(Amt), 5), 60)` |
| window | `cross_regbeta@60->30` | +0.52 | +0.52 | +0.64 | — | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 30)` |
| window | `cross_regbeta@60->120` | +1.20 | +1.25 | +1.20 | — | `cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 120)` |

### head score +0.65:`cross_regbeta(day_sum(Volume), day_kurt(Volume), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(Volume)` | -1.40 | -1.19 | -1.40 | — | (子树本身) |
| sufficiency | `day_kurt(Volume)` | -4.93 | -4.22 | -4.93 | — | (子树本身) |
| swap | `Volume->Amt` | +0.37 | +1.52 | +0.37 | — | `cross_regbeta(day_sum(Amt), day_kurt(Amt), 60)` |
| window | `cross_regbeta@60->30` | +0.29 | +0.97 | +0.29 | — | `cross_regbeta(day_sum(Volume), day_kurt(Volume), 30)` |
| window | `cross_regbeta@60->120` | -0.12 | +1.13 | -0.12 | — | `cross_regbeta(day_sum(Volume), day_kurt(Volume), 120)` |

### head score -1.70:`ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60), 5), 5), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60), 5), 5)` | -2.55 | -2.55 | -2.10 | — | (子树本身) |
| sufficiency | `ts_max(cross_med(day_ar1_coefficient(Amt), 60), 5)` | -2.68 | -2.68 | -2.23 | — | (子树本身) |
| sufficiency | `cross_med(day_ar1_coefficient(Amt), 60)` | -2.97 | -2.79 | -2.97 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Amt)` | -3.40 | -2.82 | -3.40 | — | (子树本身) |
| knockout | `ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60), 5), 5)` | -1.79 | -1.79 | -1.46 | +0.08 | `ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60), 5), 30)` |
| knockout | `cross_med(day_ar1_coefficient(Amt), 60)` | -1.23 | -0.69 | -1.23 | -0.47 | `ts_max(ts_max(ts_max(day_ar1_coefficient(Amt), 5), 5), 30)` |
| swap | `Amt->Volume` | -1.76 | -1.76 | -1.34 | — | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Volume), 60), 5), 5), 30)` |
| window | `ts_max@30->15` | -1.99 | -1.99 | -1.73 | — | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60), 5), 5), 15)` |
| window | `ts_max@30->60` | -1.18 | -1.18 | -1.16 | — | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(Amt), 60), 5), 5), 60)` |

### head score -2.13:`ts_max(cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50), 60), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50), 60)` | -2.14 | -2.14 | -1.67 | — | (子树本身) |
| sufficiency | `ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50)` | -3.74 | -2.28 | -3.74 | — | (子树本身) |
| sufficiency | `ts_max(cross_med(day_ar1_coefficient(High), 60), 5)` | -2.35 | -2.35 | -2.28 | — | (子树本身) |
| sufficiency | `cross_med(day_ar1_coefficient(High), 60)` | -2.32 | -2.32 | -2.17 | — | (子树本身) |
| knockout | `cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50), 60)` | -3.70 | -2.26 | -3.70 | +1.57 | `ts_max(ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50), 5)` |
| knockout | `ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50)` | -3.74 | -2.28 | -3.74 | +1.61 | `ts_max(cross_med(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 60), 5)` |
| knockout | `ts_max(cross_med(day_ar1_coefficient(High), 60), 5)` | -2.14 | -2.14 | -1.71 | +0.00 | `ts_max(cross_med(ts_max(cross_med(day_ar1_coefficient(High), 60), 50), 60), 5)` |
| knockout | `cross_med(day_ar1_coefficient(High), 60)` | -1.90 | -1.90 | -1.41 | -0.24 | `ts_max(cross_med(ts_max(ts_max(day_ar1_coefficient(High), 5), 50), 60), 5)` |
| swap | `High->Low` | -2.03 | -2.03 | -1.45 | — | `ts_max(cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient(Low), 60), 5), 50), 60), 5)` |
| window | `ts_max@5->2` | -2.15 | -2.15 | -1.66 | — | `ts_max(cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50), 60), 2)` |
| window | `ts_max@5->10` | -2.07 | -2.07 | -1.54 | — | `ts_max(cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient(High), 60), 5), 50), 60), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_std(abs_(Close))` — enrichment,均值差 +2.07,p 0.001
2. `day_argmax(Volume)` — enrichment,均值差 +1.39,p 0.004
3. `day_min(cross_argmax(Volume, 30))` — enrichment,均值差 +0.79,p 0.042
4. `day_min(Vwap)` — enrichment,均值差 +0.75,p 0.018
5. `cross_mean(mul(day_sum(Ret), cross_zscore(day_sum(Amt), 20)), 60)` — enrichment,均值差 +0.75,p 0.051
6. `day_min(Close)` — enrichment,均值差 +0.73,p 0.049
7. `day_open(Open)` — enrichment,均值差 +0.67,p 0.017
8. `day_kurt(Volume)` — enrichment,均值差 +0.61,p 0.000
9. `day_sum(Volume)` — enrichment,均值差 +0.56,p 0.004
10. `day_std(in_top_quantile_flag_q10(Vwap))` — enrichment,均值差 +0.56,p 0.082
11. `day_sum(Amt)` — enrichment,均值差 +0.45,p 0.043
12. `day_sum(Ret)` — enrichment,均值差 +0.35,p 0.011

## 本组之前各轮的任务

- `prods2051Pr1a_Na`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 18}
  - score +0.09(train +0.26 valid +0.09):`cross_corr(day_kurt(in_delta(in_delta(Vwap, 1), 1)), day_kurt(Volume), 241)`
  - score +0.07(train +0.07 valid +0.12):`cross_corr(day_kurt(in_delta(in_delta(in_delta(Vwap, 60), 1), 1)), day_kurt(Volume), 241)`
  - score -0.07(train +0.11 valid -0.07):`cross_corr(day_kurt(in_delta(Open, 1)), day_kurt(Volume), 60)`
  - score -0.10(train +0.57 valid -0.10):`cross_corr(day_kurt(in_delta(in_delta(Open, 1), 1)), day_kurt(Volume), 60)`
  - score -0.21(train -0.00 valid -0.21):`cross_corr(day_kurt(in_delta(Vwap, 15)), day_kurt(Volume), 60)`
- `prods2051Pr1b_Nb`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score +0.07(train +0.07 valid +0.13):`cross_regbeta(day_min(cross_argmax(Volume, 30)), day_std(in_top_quantile_flag_q10(Volume)), 60)`
  - score -0.01(train -0.01 valid +0.41):`cross_regbeta(day_skew(cross_argmax(Volume, 30)), day_std(in_top_quantile_flag_q10(Volume)), 60)`
  - score -0.53(train +0.05 valid -0.53):`cross_regbeta(day_min(cross_argmax(in_top_quantile_flag_q10(Vwap), 30)), day_argmax(Vwap), 60)`
  - score -0.54(train -0.28 valid -0.54):`cross_regbeta(day_min(Vwap), day_argmax(Volume), 60)`
  - score -0.59(train -0.10 valid -0.59):`cross_regbeta(day_min(Vwap), cross_regbeta(day_min(Vwap), day_argmax(Volume), 60), 60)`
- `prods2051Pr2a_Ea`:核心 `day_kurt(Volume)`;评分 80,过线 2,入 heads 2;采样计数 {'c05_skeleton': 658, 'c05_no_core': 1320, 'c05_periphery_seen': 1}
  - score +1.00(train +1.47 valid +1.00):`cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 60)`
  - score +0.65(train +1.56 valid +0.65):`cross_regbeta(day_sum(Volume), day_kurt(Volume), 60)`
  - score +0.46(train +0.78 valid +0.46):`cross_regbeta(day_std(pow_1_5(Close)), day_kurt(Volume), 60)`
  - score +0.45(train +0.45 valid +0.64):`cross_regbeta(ts_regbeta(cs_robust_z(day_flat_ratio(Amt)), pow_2_5(day_wstd(Volume, Open)), 20), day_kurt(Volume), 60)`
  - score +0.43(train +0.70 valid +0.43):`cross_regbeta(day_std(abs_(Close)), day_kurt(Volume), 60)`
- `prods2051Pr2b_Nb`:核心 `—`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.47(train -0.34 valid -0.47):`cross_corr(day_sum(Ret), day_var(Ret), 120)`
  - score -0.60(train -0.60 valid -0.55):`cs_bucket_demean(cross_mean(mul(day_sum(Ret), cross_zscore(day_sum(Amt), 20)), 60), day_open(Open))`
  - score -0.79(train -0.79 valid -0.54):`cross_corr(cross_argmax(day_sum(Ret), 60), day_sum(Amt), 120)`
  - score -0.81(train -0.81 valid -0.43):`cs_bucket_demean(cross_mean(mul(day_sum(Ret), cross_zscore(day_sum(Amt), 20)), 60), LogFloatCap)`
  - score -0.85(train -0.85 valid -0.76):`cs_bucket_demean(cross_mean(mul(day_sum(Ret), cross_zscore(day_sum(Amt), 20)), 60), cross_corr(cross_argmax(day_sum(Ret), 60), day_sum(Volume), 120))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.20(window cross_regbeta@60->120):`cross_regbeta(day_sum(Volume), ts_mean(day_kurt(Volume), 5), 120)`
- 增益 +0.11(swap High->Low):`ts_max(cross_med(ts_max(ts_max(cross_med(day_ar1_coefficient(Low), 60), 5), 50), 60), 5)`
