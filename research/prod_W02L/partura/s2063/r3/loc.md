# 定位:种子 2063,P 组,第 3 轮(只含 train / valid)

快照:prods2063M1_I0_open_search, prods2063M2_I0_open_search, prods2063M3_I0_open_search, prods2063Pr1a_Ea, prods2063Pr1b_Nb, prods2063Pr2a_Ea, prods2063Pr2b_Eb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.70 | +0.07 | -0.70 | +1 | 20 | prods2063M3_I0_open_search | `cross_fangzheng(day_ar1_coefficient(sqrt(nt_cs_mask_top_replace_mean(inv(Low)))), 30)` |
| -1.18 | -1.18 | -1.00 | -1 | 5 | prods2063M1_I0_open_search | `pow_05(day_var(nt_ts_min(Volume, 30)))` |
| -1.33 | -1.33 | -1.26 | +1 | 20 | prods2063M1_I0_open_search | `add(day_min(nt_ts_med(nt_ts_min(Amt, 3), 5)), day_cov(Ret, Low))` |
| -1.40 | -1.30 | -1.40 | +1 | 5 | prods2063M2_I0_open_search | `ts_max(log(ts_max(ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 20), 20)), 20)` |
| -1.54 | -1.54 | -1.53 | +1 | 5 | prods2063M2_I0_open_search | `ts_max(ts_max(ts_max(day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5)), 20), 20), 30)` |
| -1.72 | -1.54 | -1.72 | +1 | 5 | prods2063M3_I0_open_search | `day_sum(pow_05(in_rank(pow_2_5(inv(Ret)))))` |
| -1.74 | -1.32 | -1.74 | -1 | 5 | prods2063M3_I0_open_search | `day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(High), 3), 241))` |
| -1.77 | -1.77 | -1.05 | -1 | 20 | prods2063M2_I0_open_search | `ts_max(log(cross_regbeta(ts_max(day_cov(nt_ts_delta(High, 60), nt_ts_cov(Open, Vwap, 5)), 20), day_var(Low), 241)), 20)` |
| -2.02 | -2.02 | -1.53 | -1 | 20 | prods2063M1_I0_open_search | `add(day_quantile(in_min_rolling(nt_ts_min(Volume, 10), 15)), ts_hurst(cs_normalize(day_autocorr_n1(Low)), 30))` |

## 共性:224 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.49 | 0.000 | 11 | -0.70 / -2.19 | `cross_corr(day_var(Ret), day_sum(Ret), 60)` |
| +1.06 | 0.001 | 14 | -1.12 / -2.18 | `sub(LogFloatCap, LogFloatShares)` |
| +1.03 | 0.000 | 41 | -1.27 / -2.30 | `day_sum(Ret)` |
| +1.01 | 0.000 | 72 | -1.43 / -2.44 | `day_var(Ret)` |
| +0.85 | 0.030 | 6 | -1.29 / -2.14 | `cross_corr(day_var(Ret), day_sum(Ret), 120)` |
| +0.79 | 0.000 | 61 | -1.54 / -2.33 | `ts_delta(LogFloatShares, 50)` |
| +0.77 | 0.004 | 17 | -1.41 / -2.17 | `cross_mean(ts_delta(LogFloatShares, 50), 250)` |
| +0.69 | 0.030 | 11 | -1.46 / -2.15 | `ts_delta(ts_delta(LogFloatShares, 50), 50)` |
| +0.65 | 0.118 | 5 | -1.48 / -2.13 | `cs_first_high20(cs_first_high20(day_var(Ret), day_sum(Open)), day_sum(Open))` |
| +0.62 | 0.008 | 26 | -1.57 / -2.18 | `day_sum(Open)` |
| +0.58 | 0.029 | 17 | -1.58 / -2.16 | `cs_first_high20(day_var(Ret), day_sum(Open))` |
| +0.48 | 0.227 | 6 | -1.65 / -2.13 | `sub(ts_delta(LogFloatShares, 50), cross_mean(ts_delta(LogFloatShares, 50), 250))` |
| +0.46 | 0.185 | 6 | -1.67 / -2.13 | `day_signed_ratio(Close, Volume)` |
| +0.46 | 0.185 | 6 | -1.67 / -2.13 | `cs_first_high20(day_var(Ret), cs_mean(day_signed_ratio(Close, Volume)))` |
| +0.46 | 0.185 | 6 | -1.67 / -2.13 | `cs_mean(day_signed_ratio(Close, Volume))` |
| +0.33 | 0.354 | 6 | -1.79 / -2.12 | `ts_argmin(sigmoid(day_cov(Ret, Low)), 50)` |
| +0.30 | 0.433 | 4 | -1.82 / -2.12 | `day_cov(nt_ts_delta(Amt, 60), nt_ts_cov(Open, Vwap, 5))` |
| +0.23 | 0.460 | 9 | -1.90 / -2.12 | `sigmoid(day_cov(Ret, Low))` |
| +0.17 | 0.502 | 4 | -1.95 / -2.12 | `cs_last_high20(cs_first_high20(day_var(Ret), cs_mean(day_signed_ratio(Close, Volume))), ts_delta(LogFloatShares, 50))` |
| +0.12 | 0.454 | 12 | -2.00 / -2.12 | `day_sum(Low)` |

## 拆解(7 次评估)

### head score -0.70:`cross_fangzheng(day_ar1_coefficient(sqrt(nt_cs_mask_top_replace_mean(inv(Low)))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(sqrt(nt_cs_mask_top_replace_mean(inv(Low))))` | -0.18 | -0.10 | -0.18 | — | (子树本身) |
| swap | `Low->High` | -0.06 | -0.06 | +0.04 | — | `cross_fangzheng(day_ar1_coefficient(sqrt(nt_cs_mask_top_replace_mean(inv(High)))), 30)` |
| window | `cross_fangzheng@30->15` | +0.07 | +0.32 | +0.07 | — | `cross_fangzheng(day_ar1_coefficient(sqrt(nt_cs_mask_top_replace_mean(inv(Low)))), 15)` |
| window | `cross_fangzheng@30->60` | -0.82 | -0.04 | -0.82 | — | `cross_fangzheng(day_ar1_coefficient(sqrt(nt_cs_mask_top_replace_mean(inv(Low)))), 60)` |

### head score -1.72:`day_sum(pow_05(in_rank(pow_2_5(inv(Ret)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|

### head score -1.74:`day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(High), 3), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `High->Low` | -1.58 | -1.28 | -1.58 | — | `day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(Low), 3), 241))` |
| window | `cross_quantile_q50@241->120` | -1.69 | -1.36 | -1.69 | — | `day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(High), 3), 120))` |
| window | `cross_quantile_q50@241->482` | -1.93 | -1.49 | -1.93 | — | `day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(High), 3), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_corr(day_var(Ret), day_sum(Ret), 60)` — enrichment,均值差 +1.49,p 0.000
2. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +1.06,p 0.001
3. `day_sum(Ret)` — enrichment,均值差 +1.03,p 0.000
4. `day_var(Ret)` — enrichment,均值差 +1.01,p 0.000
5. `cross_corr(day_var(Ret), day_sum(Ret), 120)` — enrichment,均值差 +0.85,p 0.030
6. `ts_delta(LogFloatShares, 50)` — enrichment,均值差 +0.79,p 0.000
7. `cross_mean(ts_delta(LogFloatShares, 50), 250)` — enrichment,均值差 +0.77,p 0.004
8. `ts_delta(ts_delta(LogFloatShares, 50), 50)` — enrichment,均值差 +0.69,p 0.030
9. `day_sum(Open)` — enrichment,均值差 +0.62,p 0.008
10. `cs_first_high20(day_var(Ret), day_sum(Open))` — enrichment,均值差 +0.58,p 0.029

## 本组之前各轮的任务

- `prods2063Pr1a_Ea`:核心 `day_cov(Ret, Low)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 778, 'c05_no_core': 1454}
  - score -0.42(train -0.42 valid +0.18):`cross_corr(div(ts_argmin(sigmoid(day_cov(Ret, Low)), 50), day_mean(Low)), day_at_max_ratio(Low), 60)`
  - score -0.50(train -0.50 valid +0.07):`cross_corr(mul(day_cov(Ret, Low), day_at_max_ratio(Low)), day_sum(Ret), 60)`
  - score -0.72(train -0.19 valid -0.72):`cross_corr(div(ts_argmin(sigmoid(day_cov(Ret, Low)), 50), day_mean(Low)), day_sum(Ret), 60)`
  - score -0.75(train -0.75 valid -0.60):`cross_corr(mul(day_cov(Ret, Low), day_mean(Low)), cross_corr(mul(day_cov(Ret, Low), day_at_max_ratio(Low)), day_sum(Ret), 60), 60)`
  - score -0.98(train -0.98 valid -0.98):`cross_corr(mul(mul(day_cov(Ret, Low), day_mean(Low)), day_mean(Low)), day_sum(Low), 60)`
- `prods2063Pr1b_Nb`:核心 `—`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 11}
  - score -0.96(train -0.84 valid -0.96):`cs_last_high20(cs_first_high20(day_var(Ret), day_sum(Open)), LogFloatShares)`
  - score -0.99(train -0.86 valid -0.99):`cs_last_high20(cs_first_high20(day_var(Ret), day_first(Open)), LogFloatShares)`
  - score -1.10(train -1.10 valid +0.04):`cs_last_high20(cs_first_high20(day_var(Ret), cs_mean(day_signed_ratio(Close, Volume))), ts_delta(LogFloatShares, 50))`
  - score -1.10(train -1.10 valid +0.04):`cs_last_high20(cs_first_high20(day_var(Ret), ts_delta(LogFloatShares, 50)), ts_delta(LogFloatShares, 50))`
  - score -1.10(train -1.10 valid +0.04):`cs_last_high20(cs_first_high20(cs_first_high20(day_var(Ret), day_var(Ret)), day_var(Ret)), ts_delta(LogFloatShares, 50))`
- `prods2063Pr2a_Ea`:核心 `day_var(Ret)`;评分 95,过线 0,入 heads 0;采样计数 {'c05_no_core': 1808, 'c05_skeleton': 878}
  - score -0.01(train -0.01 valid +0.18):`cs_bucket_zscore(cross_corr(day_var(Ret), day_sum(Ret), 241), sub(LogFloatCap, LogFloatShares))`
  - score -0.06(train +0.09 valid -0.06):`cs_bucket_zscore(cross_cov(day_var(Ret), day_sum(Ret), 60), sub(LogFloatCap, LogFloatShares))`
  - score -0.29(train -0.29 valid -0.09):`cross_cov(day_var(Ret), day_sum(Ret), 60)`
  - score -0.39(train -0.39 valid -0.28):`cs_bucket_zscore(cross_corr(day_var(Ret), day_sum(Ret), 60), sub(LogFloatCap, LogFloatShares))`
  - score -0.41(train -0.23 valid -0.41):`cross_cov(day_var(Ret), LogFloatCap, 60)`
- `prods2063Pr2b_Eb`:核心 `ts_delta(LogFloatShares, 50)`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1045, 'c05_no_core': 2064, 'c05_periphery_seen': 7, 'mutation_refused': 1}
  - score -0.83(train -0.83 valid +0.04):`sub(ts_delta(ts_delta(LogFloatShares, 50), 50), cross_mean(ts_delta(LogFloatShares, 50), 250))`
  - score -0.84(train -0.84 valid +0.01):`sub(sub(ts_delta(ts_delta(LogFloatShares, 50), 50), cross_mean(ts_delta(LogFloatShares, 50), 250)), cross_mean(ts_delta(LogFloatShares, 50), 250))`
  - score -0.88(train -0.88 valid -0.03):`sub(sub(ts_delta(LogFloatShares, 50), cross_mean(ts_delta(LogFloatShares, 50), 250)), cross_mean(ts_delta(LogFloatShares, 50), 250))`
  - score -0.88(train -0.88 valid -0.28):`sub(sub(ts_delta(ts_delta(LogFloatShares, 50), 50), cross_mean(ts_quantile_q75(LogFloatShares, 50), 250)), cross_mean(sub(ts_delta(ts_delta(LogFloatShares, 50), 50), cross_mean(ts_quantile_q75(LogFloatShares, 50), 250)), 250))`
  - score -0.89(train -0.89 valid -0.31):`sub(ts_delta(ts_delta(LogFloatShares, 50), 30), cross_mean(ts_delta(LogFloatShares, 50), 250))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.77(window cross_fangzheng@30->15):`cross_fangzheng(day_ar1_coefficient(sqrt(nt_cs_mask_top_replace_mean(inv(Low)))), 15)`
- 增益 +0.64(swap Low->High):`cross_fangzheng(day_ar1_coefficient(sqrt(nt_cs_mask_top_replace_mean(inv(High)))), 30)`
- 增益 +0.16(swap High->Low):`day_quantile_q75(cross_quantile_q50(nt_ts_stddev(inv(Low), 3), 241))`
