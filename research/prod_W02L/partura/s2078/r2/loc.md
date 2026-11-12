# 定位:种子 2078,P 组,第 2 轮(只含 train / valid)

快照:prods2078M1_I0_open_search, prods2078M2_I0_open_search, prods2078Pr1a_Ea, prods2078Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.23 | +0.01 | -0.23 | +1 | 5 | prods2078M1_I0_open_search | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 60), cross_mean(day_std(Ret), 60))` |
| -0.64 | -0.00 | -0.64 | +1 | 20 | prods2078M2_I0_open_search | `sigmoid(ts_regbeta(day_quantile(High), day_skew(Volume), 30))` |
| -0.98 | -0.98 | -0.40 | +1 | 20 | prods2078M2_I0_open_search | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)), 30))` |
| -1.26 | -1.26 | -1.25 | -1 | 5 | prods2078M2_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10), 241))` |
| -1.34 | -1.19 | -1.34 | -1 | 5 | prods2078M1_I0_open_search | `pow_05(cs_normalize(day_mean(Volume)))` |
| -1.80 | -1.47 | -1.80 | -1 | 20 | prods2078M1_I0_open_search | `pow_2(day_cov(Amt, Vwap))` |

## 共性:165 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.24 | 0.001 | 4 | -0.30 / -2.55 | `cs_last_low05(day_flat_run_max(Volume), LogTotalCap)` |
| +1.80 | 0.000 | 8 | -0.78 / -2.58 | `day_flat_run_max(Volume)` |
| +1.46 | 0.000 | 43 | -1.42 / -2.87 | `cs_demean(div(day_mean(Ret), 2))` |
| +1.46 | 0.000 | 43 | -1.42 / -2.87 | `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)` |
| +1.45 | 0.000 | 9 | -1.12 / -2.57 | `day_sum(Vwap)` |
| +1.39 | 0.000 | 48 | -1.51 / -2.90 | `day_mean(Ret)` |
| +1.28 | 0.007 | 6 | -1.26 / -2.54 | `cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241)` |
| +1.28 | 0.005 | 7 | -1.27 / -2.55 | `day_quantile_q75(Close)` |
| +1.12 | 0.001 | 15 | -1.47 / -2.60 | `ts_stddev(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30)` |
| +0.51 | 0.170 | 5 | -2.00 / -2.51 | `cross_delay(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30)` |
| +0.27 | 0.299 | 5 | -2.23 / -2.50 | `day_mean(High)` |
| +0.23 | 0.393 | 5 | -2.27 / -2.50 | `day_skew(Volume)` |
| -0.48 | 0.860 | 5 | -2.95 / -2.48 | `day_skew(Vwap)` |
| -0.53 | 0.769 | 4 | -3.01 / -2.48 | `day_skew(High)` |
| -0.85 | 0.999 | 17 | -3.25 / -2.41 | `day_ar1_coefficient(Volume)` |
| -0.92 | 0.947 | 7 | -3.38 / -2.45 | `day_last(Close)` |

## 拆解(38 次评估)

### head score -0.23:`div(ts_max(cs_demean(div(day_mean(Ret), 2)), 60), cross_mean(day_std(Ret), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_demean(div(day_mean(Ret), 2)), 60)` | -0.45 | -0.45 | -0.41 | — | (子树本身) |
| sufficiency | `cs_demean(div(day_mean(Ret), 2))` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Ret), 60)` | -3.49 | -2.88 | -3.49 | — | (子树本身) |
| sufficiency | `day_mean(Ret)` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| knockout | `ts_max(cs_demean(div(day_mean(Ret), 2)), 60)` | -3.83 | -3.83 | -3.12 | +3.60 | `div(cs_demean(div(day_mean(Ret), 2)), cross_mean(day_std(Ret), 60))` |
| knockout | `div(day_mean(Ret), 2)` | -0.23 | +0.01 | -0.23 | +0.00 | `div(ts_max(cs_demean(day_mean(Ret)), 60), cross_mean(day_std(Ret), 60))` |
| knockout | `cross_mean(day_std(Ret), 60)` | -1.18 | -1.18 | -1.11 | +0.96 | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 60), day_std(Ret))` |
| window | `ts_max@60->30` | -1.38 | -1.01 | -1.38 | — | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), cross_mean(day_std(Ret), 60))` |
| window | `ts_max@60->120` | -0.17 | -0.17 | +0.05 | — | `div(ts_max(cs_demean(div(day_mean(Ret), 2)), 120), cross_mean(day_std(Ret), 60))` |

### head score -0.64:`sigmoid(ts_regbeta(day_quantile(High), day_skew(Volume), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_regbeta(day_quantile(High), day_skew(Volume), 30)` | -0.59 | +0.01 | -0.59 | — | (子树本身) |
| sufficiency | `day_quantile(High)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| sufficiency | `day_skew(Volume)` | -5.21 | -4.17 | -5.21 | — | (子树本身) |
| knockout | `ts_regbeta(day_quantile(High), day_skew(Volume), 30)` | — | — | — | — | `sigmoid(day_quantile(High))` |
| swap | `High->Low` | -0.57 | +0.04 | -0.57 | — | `sigmoid(ts_regbeta(day_quantile(Low), day_skew(Volume), 30))` |
| swap | `Volume->Amt` | -0.65 | -0.09 | -0.65 | — | `sigmoid(ts_regbeta(day_quantile(High), day_skew(Amt), 30))` |
| window | `ts_regbeta@30->15` | -1.24 | -0.39 | -1.24 | — | `sigmoid(ts_regbeta(day_quantile(High), day_skew(Volume), 15))` |
| window | `ts_regbeta@30->60` | -0.52 | +0.34 | -0.52 | — | `sigmoid(ts_regbeta(day_quantile(High), day_skew(Volume), 60))` |

### head score -0.98:`pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)), 30)` | -1.42 | -1.42 | -0.40 | — | (子树本身) |
| sufficiency | `cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5))` | -3.38 | -3.38 | -2.23 | — | (子树本身) |
| sufficiency | `day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10))` | -3.38 | -3.38 | -2.23 | — | (子树本身) |
| knockout | `ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)), 30)` | -6.74 | -5.04 | -6.74 | +5.76 | `pow_2(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)))` |
| knockout | `sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)` | -0.98 | -0.98 | -0.37 | -0.00 | `pow_2(ts_max(cs_demean(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10))), 30))` |
| swap | `Low->High` | -1.41 | -1.41 | -0.63 | — | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(High, Amt, 15), in_argmin(Volume, 10)), 5)), 30))` |
| swap | `Amt->Volume` | -2.78 | -1.77 | -2.78 | — | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Volume, 15), in_argmin(Volume, 10)), 5)), 30))` |
| window | `ts_max@30->15` | -1.93 | -1.93 | -1.11 | — | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)), 15))` |
| window | `ts_max@30->60` | +0.28 | +0.28 | +0.47 | — | `pow_2(ts_max(cs_demean(sub(day_cov(nt_ts_regres(Low, Amt, 15), in_argmin(Volume, 10)), 5)), 60))` |

### head score -1.26:`signedpower(cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10), 241)` | -1.26 | -1.26 | -1.26 | — | (子树本身) |
| sufficiency | `cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10)` | -0.73 | -0.66 | -0.73 | — | (子树本身) |
| sufficiency | `mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume))` | -2.13 | -1.66 | -2.13 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), day_skew(Volume))` | -2.16 | -1.61 | -2.16 | — | (子树本身) |
| knockout | `cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10), 241)` | -0.73 | -0.66 | -0.73 | -0.53 | `signedpower(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10))` |
| knockout | `cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10)` | -2.32 | -1.65 | -2.32 | +1.06 | `signedpower(cross_quantile_q75(mul(day_mean(High), day_skew(Volume)), 241))` |
| knockout | `mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume))` | — | — | — | — | `signedpower(cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| knockout | `mul(day_mean(High), day_skew(Volume))` | -0.74 | -0.74 | +0.06 | -0.52 | `signedpower(cross_quantile_q75(cross_corr(day_mean(High), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10), 241))` |
| swap | `High->Low` | -1.26 | -1.26 | -1.22 | — | `signedpower(cross_quantile_q75(cross_corr(mul(day_mean(Low), day_skew(Volume)), mul(mul(day_mean(Low), day_skew(Volume)), day_skew(Volume)), 10), 241))` |
| swap | `Volume->Amt` | -1.25 | -1.25 | -1.14 | — | `signedpower(cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Amt)), mul(mul(day_mean(High), day_skew(Amt)), day_skew(Amt)), 10), 241))` |
| window | `cross_quantile_q75@241->120` | -1.79 | -1.31 | -1.79 | — | `signedpower(cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10), 120))` |
| window | `cross_quantile_q75@241->482` | -1.72 | -1.72 | -1.37 | — | `signedpower(cross_quantile_q75(cross_corr(mul(day_mean(High), day_skew(Volume)), mul(mul(day_mean(High), day_skew(Volume)), day_skew(Volume)), 10), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_low05(day_flat_run_max(Volume), LogTotalCap)` — enrichment,均值差 +2.24,p 0.001
2. `day_flat_run_max(Volume)` — enrichment,均值差 +1.80,p 0.000
3. `cs_demean(div(day_mean(Ret), 2))` — enrichment,均值差 +1.46,p 0.000
4. `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)` — enrichment,均值差 +1.46,p 0.000
5. `day_sum(Vwap)` — enrichment,均值差 +1.45,p 0.000
6. `day_mean(Ret)` — enrichment,均值差 +1.39,p 0.000
7. `cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241)` — enrichment,均值差 +1.28,p 0.007
8. `day_quantile_q75(Close)` — enrichment,均值差 +1.28,p 0.005
9. `ts_stddev(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30)` — enrichment,均值差 +1.12,p 0.001

## 本组之前各轮的任务

- `prods2078Pr1a_Ea`:核心 `ts_max(cs_demean(div(day_mean(Ret), 2)), 30)`;评分 96,过线 0,入 heads 0;采样计数 {'c05_no_core': 2722, 'c05_skeleton': 1277, 'mutation_refused': 11, 'c05_periphery_seen': 4}
  - score -0.03(train -0.03 valid +0.14):`cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241)`
  - score -0.07(train -0.07 valid +0.07):`cross_regbeta(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241)`
  - score -0.41(train -0.41 valid -0.35):`cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241), 241)`
  - score -0.44(train -0.44 valid +0.38):`cs_bucket_zscore(cross_reg_tvalue(cs_demean(div(day_mean(Ret), 2)), ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 241), ts_stddev(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30))`
  - score -0.58(train -0.58 valid -0.08):`ts_stddev(ts_max(cs_demean(div(ts_stddev(ts_max(cs_demean(div(day_mean(Ret), 2)), 30), 30), 2)), 30), 30)`
- `prods2078Pr1b_Nb`:核心 `—`;评分 61,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.09(train -0.02 valid -0.09):`cs_last_low05(day_flat_ratio(Volume), LogTotalCap)`
  - score -0.09(train -0.02 valid -0.09):`cs_last_low05(cs_last_low05(day_flat_ratio(Volume), LogTotalCap), LogTotalCap)`
  - score -0.09(train -0.02 valid -0.09):`cs_last_low05(day_flat_ratio(Volume), cs_last_low05(day_flat_ratio(Volume), LogTotalCap))`
  - score -0.24(train +0.35 valid -0.24):`cs_last_low05(day_flat_run_max(Volume), LogTotalCap)`
  - score -0.24(train +0.35 valid -0.24):`cs_last_low05(cs_last_low05(day_flat_run_max(Volume), LogTotalCap), LogTotalCap)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.12(window ts_regbeta@30->60):`sigmoid(ts_regbeta(day_quantile(High), day_skew(Volume), 60))`
