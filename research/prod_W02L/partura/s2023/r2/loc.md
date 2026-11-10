# 定位:种子 2023,P 组,第 2 轮(只含 train / valid)

快照:prods2023M1_I0_open_search, prods2023M2_I0_open_search, prods2023Pr1a_Ea, prods2023Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.11 | -0.86 | -1.11 | -1 | 5 | prods2023M2_I0_open_search | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241), 30))` |
| -1.36 | -1.16 | -1.36 | -1 | 0 | prods2023M1_I0_open_search | `ts_max(day_quantile_q75(Volume), 40)` |
| -1.48 | -1.40 | -1.48 | -1 | 5 | prods2023M1_I0_open_search | `ts_stddev(day_quantile_q75(Volume), 10)` |
| -1.52 | -1.52 | -1.51 | +1 | 20 | prods2023M2_I0_open_search | `ts_sum(cross_corr(day_median(Amt), day_first(Amt), 15), 10)` |
| -1.55 | -1.26 | -1.55 | -1 | 20 | prods2023M2_I0_open_search | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` |
| -1.56 | -1.39 | -1.56 | +1 | 5 | prods2023M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50)))` |

## 共性:166 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.03 | 0.000 | 101 | -1.73 / -2.76 | `day_quantile_q75(Volume)` |
| +0.99 | 0.013 | 6 | -1.18 / -2.17 | `day_sum(Volume)` |
| +0.92 | 0.000 | 34 | -1.40 / -2.33 | `day_std(Ret)` |
| +0.81 | 0.008 | 10 | -1.38 / -2.19 | `day_sum(Ret)` |
| +0.47 | 0.113 | 8 | -1.69 / -2.16 | `day_wmean(Ret, is_lt(Volume, day_quantile_q75(Volume)))` |
| +0.46 | 0.172 | 6 | -1.69 / -2.15 | `sub(day_wmean(Ret, is_gt(Volume, day_quantile_q75(Volume))), day_wmean(Ret, is_lt(Volume, day_quantile_q75(Volume))))` |
| +0.25 | 0.146 | 18 | -1.91 / -2.16 | `day_wmean(Ret, is_gt(Volume, day_quantile_q75(Volume)))` |
| -0.07 | 0.720 | 6 | -2.21 / -2.13 | `day_median(Vwap)` |
| -0.08 | 0.705 | 5 | -2.22 / -2.13 | `day_quantile_q75(Low)` |
| -0.14 | 0.644 | 10 | -2.27 / -2.13 | `day_quantile_q75(Ret)` |
| -0.39 | 0.929 | 6 | -2.51 / -2.12 | `day_quantile_q75(Open)` |
| -0.64 | 0.951 | 6 | -2.75 / -2.11 | `day_quantile_q75(Close)` |
| -0.77 | 0.979 | 4 | -2.88 / -2.12 | `ts_min(day_median(Amt), 30)` |
| -0.82 | 0.999 | 13 | -2.89 / -2.07 | `day_median(Amt)` |
| -1.73 | 0.993 | 4 | -3.82 / -2.10 | `day_quantile_q75(Amt)` |

## 拆解(23 次评估)

### head score -1.11:`cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241), 30)` | -1.16 | -0.85 | -1.16 | — | (子树本身) |
| sufficiency | `cross_regbeta(day_autocorr_n1(High), day_median(Close), 241)` | -1.15 | -0.91 | -1.15 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(High)` | -2.75 | -2.75 | -2.13 | — | (子树本身) |
| sufficiency | `day_median(Close)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `cross_mean(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241), 30)` | -1.15 | -0.91 | -1.15 | +0.04 | `cs_demean(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241))` |
| knockout | `cross_regbeta(day_autocorr_n1(High), day_median(Close), 241)` | -2.53 | -2.53 | -2.39 | +1.42 | `cs_demean(cross_mean(day_autocorr_n1(High), 30))` |
| swap | `High->Low` | -1.08 | -0.74 | -1.08 | — | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(Low), day_median(Close), 241), 30))` |
| swap | `Close->Vwap` | -1.18 | -0.87 | -1.18 | — | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), day_median(Vwap), 241), 30))` |
| window | `cross_mean@30->15` | -1.19 | -0.92 | -1.19 | — | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241), 15))` |
| window | `cross_mean@30->60` | -1.14 | -0.87 | -1.14 | — | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241), 60))` |

### head score -1.52:`ts_sum(cross_corr(day_median(Amt), day_first(Amt), 15), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_corr(day_median(Amt), day_first(Amt), 15)` | -1.44 | -1.24 | -1.44 | — | (子树本身) |
| sufficiency | `day_median(Amt)` | -3.56 | -3.10 | -3.56 | — | (子树本身) |
| sufficiency | `day_first(Amt)` | -1.30 | -1.30 | -0.79 | — | (子树本身) |
| knockout | `cross_corr(day_median(Amt), day_first(Amt), 15)` | -4.06 | -2.77 | -4.06 | +2.54 | `ts_sum(day_median(Amt), 10)` |
| swap | `Amt->Volume` | -1.88 | -1.88 | -1.68 | — | `ts_sum(cross_corr(day_median(Volume), day_first(Volume), 15), 10)` |
| window | `ts_sum@10->5` | -1.54 | -1.37 | -1.54 | — | `ts_sum(cross_corr(day_median(Amt), day_first(Amt), 15), 5)` |
| window | `ts_sum@10->20` | -1.39 | -1.39 | -1.28 | — | `ts_sum(cross_corr(day_median(Amt), day_first(Amt), 15), 20)` |

### head score -1.55:`ts_cov(day_kurt(Vwap), day_median(Amt), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(Vwap)` | -3.90 | -3.24 | -3.90 | — | (子树本身) |
| sufficiency | `day_median(Amt)` | -3.56 | -3.10 | -3.56 | — | (子树本身) |
| swap | `Vwap->Close` | -1.87 | -1.41 | -1.87 | — | `ts_cov(day_kurt(Close), day_median(Amt), 20)` |
| swap | `Amt->Volume` | -1.22 | -0.49 | -1.22 | — | `ts_cov(day_kurt(Vwap), day_median(Volume), 20)` |
| window | `ts_cov@20->10` | -1.45 | -1.45 | -1.33 | — | `ts_cov(day_kurt(Vwap), day_median(Amt), 10)` |
| window | `ts_cov@20->40` | -2.04 | -1.42 | -2.04 | — | `ts_cov(day_kurt(Vwap), day_median(Amt), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_quantile_q75(Volume)` — enrichment,均值差 +1.03,p 0.000
2. `day_sum(Volume)` — enrichment,均值差 +0.99,p 0.013
3. `day_std(Ret)` — enrichment,均值差 +0.92,p 0.000
4. `day_sum(Ret)` — enrichment,均值差 +0.81,p 0.008

## 本组之前各轮的任务

- `prods2023Pr1a_Ea`:核心 `day_quantile_q75(Volume)`;评分 95,过线 0,入 heads 0;采样计数 {'c05_no_core': 1290, 'c05_skeleton': 626}
  - score -0.43(train -0.08 valid -0.43):`cross_corr(sub(log(add(day_quantile_q75(Volume), 100)), cross_corr(day_quantile_q75(Volume), day_sum(Volume), 10)), day_std(Ret), 241)`
  - score -0.53(train -0.53 valid -0.49):`cross_corr(sub(log(add(day_quantile_q75(Volume), sub(log(add(day_quantile_q75(Volume), 100)), LogFloatShares))), LogFloatShares), day_std(Ret), 241)`
  - score -0.54(train -0.51 valid -0.54):`cross_corr(sub(log(add(day_quantile_q75(Volume), sub(log(add(day_quantile_q75(Volume), add(day_quantile_q75(Volume), sub(log(add(day_quantile_q75(Volume), -2)), cross_corr(day_quantile_q75(Volume), day_sum(Volume), 241))))), LogFloatShares))), LogFloatShares), day_std(Ret), 241)`
  - score -0.54(train -0.54 valid -0.41):`cross_corr(log(add(day_quantile_q75(Volume), 100)), day_std(Ret), 241)`
  - score -0.57(train -0.57 valid -0.49):`cross_corr(sub(log(add(day_quantile_q75(Volume), add(day_quantile_q75(Volume), sub(log(add(day_quantile_q75(Volume), -5)), LogFloatShares)))), LogFloatShares), day_std(Ret), 241)`
- `prods2023Pr1b_Nb`:核心 `—`;评分 83,过线 0,入 heads 0;采样计数 {'c05_skeleton': 8}
  - score +0.44(train +0.44 valid +1.01):`cross_mean(day_wmean(Ret, log(Ret)), 241)`
  - score -0.39(train -0.39 valid +0.72):`cross_mean(div(sub(day_wmean(Ret, cross_mean(Volume, 20)), day_wmean(Ret, is_lt(Ret, day_quantile_q75(Volume)))), add(day_std(Ret), 2)), 241)`
  - score -0.88(train -0.88 valid +0.08):`cross_mean(day_wmean(Ret, is_gt(Volume, day_quantile_q75(is_gt(Volume, day_quantile_q75(Volume))))), 241)`
  - score -0.88(train -0.88 valid +0.08):`cross_mean(day_wmean(Ret, is_gt(Volume, day_quantile_q75(Ret))), 241)`
  - score -0.88(train -0.88 valid +0.08):`cross_mean(day_wmean(Ret, is_gt(Volume, day_quantile_q75(is_gt(Volume, day_wmean(Ret, is_lt(Ret, day_quantile_q75(Volume))))))), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.33(swap Amt->Volume):`ts_cov(day_kurt(Vwap), day_median(Volume), 20)`
- 增益 +0.12(window ts_sum@10->20):`ts_sum(cross_corr(day_median(Amt), day_first(Amt), 15), 20)`
- 增益 +0.10(window ts_cov@20->10):`ts_cov(day_kurt(Vwap), day_median(Amt), 10)`
