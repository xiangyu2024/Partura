# 定位:种子 2072,P 组,第 2 轮(只含 train / valid)

快照:prods2072M1_I0_open_search, prods2072M2_I0_open_search, prods2072Pr1a_Ea, prods2072Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.81 | -0.81 | -0.72 | +1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(log(add(day_last(Volume), day_std(Vwap))), day_std(Vwap))), ts_hurst(day_last(Volume), 20)), 50)` |
| -1.33 | -0.90 | -1.33 | +1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(div(day_last(Volume), ts_mean(mul(log(add(day_open(Ret), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)), 20)), 20)` |
| -1.45 | -1.35 | -1.45 | -1 | 0 | prods2072M1_I0_open_search | `ts_mean(mul(log(add(day_last(Volume), day_std(Vwap))), ts_hurst(log(day_quantile(in_max(Ret))), 20)), 50)` |
| -1.47 | -1.43 | -1.47 | +1 | 0 | prods2072M2_I0_open_search | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)` |
| -2.18 | -1.65 | -2.18 | -1 | 20 | prods2072M2_I0_open_search | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 60)), 5)` |
| -2.36 | -1.82 | -2.36 | -1 | 20 | prods2072M2_I0_open_search | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 15)), 1)` |

## 共性:131 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.79 | 0.001 | 19 | -1.23 / -2.01 | `day_quantile_q25(Low)` |
| +0.79 | 0.001 | 19 | -1.23 / -2.01 | `pow_05(day_quantile_q25(Low))` |
| +0.70 | 0.008 | 8 | -1.24 / -1.94 | `inv(ts_hurst(day_last(Volume), 20))` |
| +0.66 | 0.017 | 7 | -1.28 / -1.93 | `pow_05(inv(ts_hurst(day_last(Volume), 20)))` |
| +0.64 | 0.004 | 13 | -1.32 / -1.96 | `pow_3(LimitWidth)` |
| +0.55 | 0.034 | 8 | -1.38 / -1.93 | `abs_(ts_hurst(day_last(Volume), 20))` |
| +0.55 | 0.153 | 4 | -1.37 / -1.91 | `pow_05(LimitWidth)` |
| +0.50 | 0.018 | 18 | -1.47 / -1.97 | `day_es_ratio_hi(Vwap)` |
| +0.45 | 0.019 | 18 | -1.51 / -1.96 | `cs_winsor(ts_hurst(day_last(Volume), 20))` |
| +0.40 | 0.224 | 10 | -1.53 / -1.93 | `day_wstd(High, Amt)` |
| +0.39 | 0.241 | 5 | -1.52 / -1.91 | `cs_last_low20(day_es_ratio_hi(Vwap), day_wstd(High, Amt))` |
| +0.35 | 0.418 | 4 | -1.56 / -1.91 | `day_quantile_q25(Vwap)` |
| +0.30 | 0.019 | 69 | -1.75 / -2.06 | `ts_hurst(day_last(Volume), 20)` |
| +0.29 | 0.629 | 5 | -1.62 / -1.91 | `day_std(High)` |
| +0.28 | 0.046 | 75 | -1.78 / -2.06 | `day_last(Volume)` |
| +0.26 | 0.136 | 10 | -1.66 / -1.92 | `day_wstd(Close, Amt)` |
| +0.17 | 0.233 | 4 | -1.73 / -1.90 | `cs_first_low40(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_3(LimitWidth))` |
| +0.09 | 0.300 | 8 | -1.81 / -1.90 | `cs_last_low20(day_es_ratio_hi(Vwap), day_wstd(Close, Amt))` |
| +0.06 | 0.796 | 10 | -1.85 / -1.90 | `day_sum(Ret)` |
| +0.02 | 0.720 | 4 | -1.88 / -1.90 | `cs_last_low40(cs_last_high20(day_centroid(High), day_sum(Ret)), ts_hurst(day_last(Volume), 20))` |

## 拆解(27 次评估)

### head score -1.47:`ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_cov(day_mean(Vwap), day_quantile(Amt), 15)` | -2.24 | -2.24 | -1.99 | — | (子树本身) |
| sufficiency | `day_mean(Vwap)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_quantile(Amt)` | -3.56 | -3.10 | -3.56 | — | (子树本身) |
| knockout | `cross_cov(day_mean(Vwap), day_quantile(Amt), 15)` | -2.32 | -1.59 | -2.32 | +0.86 | `ts_sum(day_mean(Vwap), 50)` |
| swap | `Vwap->Close` | -1.45 | -1.43 | -1.45 | — | `ts_sum(cross_cov(day_mean(Close), day_quantile(Amt), 15), 50)` |
| swap | `Amt->Volume` | -1.66 | -0.94 | -1.66 | — | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Volume), 15), 50)` |
| window | `ts_sum@50->25` | -2.22 | -1.54 | -2.22 | — | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 25)` |
| window | `ts_sum@50->100` | -1.34 | -1.34 | -1.28 | — | `ts_sum(cross_cov(day_mean(Vwap), day_quantile(Amt), 15), 100)` |

### head score -2.18:`ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 60)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 60))` | -2.14 | -1.62 | -2.14 | — | (子树本身) |
| sufficiency | `cross_cov(day_mean(Vwap), day_quantile(High), 60)` | -2.14 | -1.61 | -2.14 | — | (子树本身) |
| sufficiency | `day_mean(Vwap)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_quantile(High)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| knockout | `pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 60))` | -2.13 | -1.65 | -2.13 | -0.04 | `ts_quantile_q75(cross_cov(day_mean(Vwap), day_quantile(High), 60), 5)` |
| knockout | `cross_cov(day_mean(Vwap), day_quantile(High), 60)` | -2.39 | -1.60 | -2.39 | +0.21 | `ts_quantile_q75(pow_1_5(day_mean(Vwap)), 5)` |
| swap | `Vwap->Close` | -2.13 | -1.65 | -2.13 | — | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Close), day_quantile(High), 60)), 5)` |
| swap | `High->Low` | -2.13 | -1.65 | -2.13 | — | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(Low), 60)), 5)` |
| window | `ts_quantile_q75@5->2` | -2.12 | -1.63 | -2.12 | — | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 60)), 2)` |
| window | `ts_quantile_q75@5->10` | -2.19 | -1.62 | -2.19 | — | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 60)), 10)` |

### head score -2.36:`ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 15)), 1)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 15))` | -2.32 | -1.82 | -2.32 | — | (子树本身) |
| sufficiency | `cross_cov(day_mean(Vwap), day_quantile(High), 15)` | -2.32 | -1.82 | -2.32 | — | (子树本身) |
| sufficiency | `day_mean(Vwap)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_quantile(High)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| knockout | `pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 15))` | -2.32 | -1.82 | -2.32 | -0.04 | `ts_quantile_q75(cross_cov(day_mean(Vwap), day_quantile(High), 15), 1)` |
| knockout | `cross_cov(day_mean(Vwap), day_quantile(High), 15)` | -2.38 | -1.61 | -2.38 | +0.02 | `ts_quantile_q75(pow_1_5(day_mean(Vwap)), 1)` |
| swap | `Vwap->Close` | -2.33 | -1.82 | -2.33 | — | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Close), day_quantile(High), 15)), 1)` |
| swap | `High->Low` | -2.33 | -1.81 | -2.33 | — | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(Low), 15)), 1)` |
| window | `ts_quantile_q75@1->2` | -2.31 | -1.80 | -2.31 | — | `ts_quantile_q75(pow_1_5(cross_cov(day_mean(Vwap), day_quantile(High), 15)), 2)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_quantile_q25(Low)` — enrichment,均值差 +0.79,p 0.001
2. `pow_05(day_quantile_q25(Low))` — enrichment,均值差 +0.79,p 0.001
3. `inv(ts_hurst(day_last(Volume), 20))` — enrichment,均值差 +0.70,p 0.008
4. `pow_05(inv(ts_hurst(day_last(Volume), 20)))` — enrichment,均值差 +0.66,p 0.017
5. `pow_3(LimitWidth)` — enrichment,均值差 +0.64,p 0.004
6. `abs_(ts_hurst(day_last(Volume), 20))` — enrichment,均值差 +0.55,p 0.034
7. `day_es_ratio_hi(Vwap)` — enrichment,均值差 +0.50,p 0.018
8. `cs_winsor(ts_hurst(day_last(Volume), 20))` — enrichment,均值差 +0.45,p 0.019
9. `ts_hurst(day_last(Volume), 20)` — enrichment,均值差 +0.30,p 0.019
10. `day_last(Volume)` — enrichment,均值差 +0.28,p 0.046

## 本组之前各轮的任务

- `prods2072Pr1a_Ea`:核心 `ts_hurst(day_last(Volume), 20)`;评分 93,过线 0,入 heads 0;采样计数 {'c05_no_core': 1166, 'c05_skeleton': 599, 'mutation_refused': 6, 'c05_periphery_seen': 6}
  - score -0.58(train -0.58 valid -0.44):`cs_scale(cs_mask_top_replace_mean_neg(cs_bucket_zscore(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_3(LimitWidth))))`
  - score -0.58(train -0.58 valid -0.44):`cs_mask_top_replace_mean_neg(cs_bucket_zscore(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_3(LimitWidth)))`
  - score -0.69(train -0.69 valid -0.30):`cs_scale(cs_mask_top_replace_mean_neg(cs_bucket_zscore(cs_first_low40(abs_(ts_hurst(day_last(Volume), 20)), pow_05(inv(ts_hurst(day_last(Volume), 20)))), pow_3(LimitWidth))))`
  - score -0.73(train -0.70 valid -0.73):`cs_mask_top_replace_mean_neg(cs_first_low40(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_3(LimitWidth)))`
  - score -0.73(train -0.70 valid -0.73):`cs_mask_top_replace_mean_neg(cs_first_low40(cs_winsor(ts_hurst(day_last(Volume), 20)), pow_05(LimitWidth)))`
- `prods2072Pr1b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.20(train -0.20 valid +0.32):`cross_regbeta(div(pow_05(day_quantile_q25(Low)), -1), cs_last_low20(day_mean(Vwap), day_wstd(Amt, Amt)), 30)`
  - score -0.39(train -0.39 valid -0.03):`cross_regbeta(div(pow_05(day_quantile_q25(Amt)), -1), cs_last_low20(day_es_ratio_hi(Vwap), day_wstd(Close, Amt)), 30)`
  - score -0.65(train -0.53 valid -0.65):`cross_regbeta(div(pow_05(day_quantile_q25(Low)), -1), cs_last_low20(day_es_ratio_hi(Amt), day_wstd(High, Amt)), 30)`
  - score -0.71(train -0.49 valid -0.71):`cross_regbeta(div(pow_05(day_quantile_q25(Low)), -1), cs_last_low20(day_es_ratio_hi(Vwap), day_quantile_q25(Low)), 30)`
  - score -0.84(train -0.76 valid -0.84):`cross_regbeta(div(pow_05(day_quantile_q25(Low)), 5), cs_last_low20(day_es_ratio_hi(Low), day_wstd(Close, Amt)), 241)`

## 比原 head 好的拆解变体(R 候选)

(没有)
