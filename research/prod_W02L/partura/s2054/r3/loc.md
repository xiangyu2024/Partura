# 定位:种子 2054,P 组,第 3 轮(只含 train / valid)

快照:prods2054M1_I0_open_search, prods2054M2_I0_open_search, prods2054M3_I0_open_search, prods2054Pr1a_Na, prods2054Pr1b_Nb, prods2054Pr2a_Ea, prods2054Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.37 | -0.37 | -0.37 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15)), pow_1_5(Ret), 10), sigmoid(sqrt(Close)), 15), 5)))` |
| -0.41 | -0.38 | -0.41 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 5), sigmoid(sqrt(Close)), 15), 5)))` |
| -0.45 | -0.26 | -0.45 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(High), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 3)))` |
| -1.26 | -1.26 | -1.06 | -1 | 5 | prods2054M2_I0_open_search | `ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 40)` |
| -1.37 | -1.37 | -1.12 | +1 | 5 | prods2054M2_I0_open_search | `cross_regbeta(day_corr(signedpower(Vwap), Low), cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)), 60)` |
| -1.91 | -1.91 | -0.65 | +1 | 20 | prods2054M2_I0_open_search | `day_durbin_watson(cross_regbeta(signedpower(nt_ts_kurt(Low, 60)), nt_ts_argmin(signedpower(Close), 10), 241))` |
| -2.40 | -2.29 | -2.40 | +1 | 20 | prods2054M3_I0_open_search | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3))))))` |
| -2.47 | -2.39 | -2.47 | +1 | 5 | prods2054M3_I0_open_search | `ts_quantile_q75(day_q_stat_std(nt_ts_autocorr_s1(nt_ts_autocorr_s1(Ret, 3), 3)), 40)` |
| -2.55 | -2.40 | -2.55 | +1 | 20 | prods2054M3_I0_open_search | `sigmoid(day_durbin_watson(nt_ts_autocorr_s1(Ret, 3)))` |

## 共性:265 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.89 | 0.000 | 9 | -0.79 / -2.68 | `day_cov(Vwap, Vwap)` |
| +1.87 | 0.001 | 7 | -0.79 / -2.66 | `cross_regbeta(day_cov(Vwap, Vwap), day_at_max_ratio(High), 241)` |
| +1.81 | 0.000 | 11 | -0.88 / -2.69 | `day_at_max_ratio(High)` |
| +1.71 | 0.002 | 6 | -0.94 / -2.65 | `pow_05(cross_regbeta(day_cov(Vwap, Vwap), day_at_max_ratio(High), 241))` |
| +1.61 | 0.000 | 10 | -1.06 / -2.67 | `day_cov(Vwap, Close)` |
| +1.59 | 0.009 | 5 | -1.05 / -2.64 | `pow_05(cross_regbeta(day_cov(Vwap, Close), day_q_stat_std(High), 241))` |
| +1.58 | 0.003 | 7 | -1.07 / -2.65 | `cross_regbeta(day_cov(Vwap, Close), day_q_stat_std(High), 241)` |
| +1.55 | 0.000 | 23 | -1.20 / -2.75 | `day_q_stat_std(High)` |
| +1.52 | 0.001 | 9 | -1.14 / -2.66 | `day_topw_mean(Vwap, Close)` |
| +1.19 | 0.054 | 4 | -1.44 / -2.63 | `cross_regbeta(day_topw_mean(Vwap, Close), day_q_stat_std(High), 241)` |
| +1.05 | 0.083 | 4 | -1.57 / -2.63 | `cs_regres(day_argmax(High), day_last(High))` |
| +0.99 | 0.001 | 32 | -1.74 / -2.73 | `day_std(Ret)` |
| +0.98 | 0.070 | 6 | -1.65 / -2.63 | `day_corr(Ret, Volume)` |
| +0.98 | 0.024 | 13 | -1.68 / -2.66 | `day_wmean(Ret, Volume)` |
| +0.95 | 0.105 | 4 | -1.68 / -2.63 | `day_sum(High)` |
| +0.95 | 0.068 | 8 | -1.70 / -2.64 | `sub(day_wmean(Ret, Volume), day_mean(Ret))` |
| +0.80 | 0.042 | 8 | -1.84 / -2.64 | `day_last(High)` |
| +0.40 | 0.244 | 21 | -2.24 / -2.64 | `day_mean(Ret)` |
| +0.24 | 0.412 | 7 | -2.38 / -2.62 | `cs_regres(cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), day_mean(Ret))` |
| +0.20 | 0.441 | 4 | -2.42 / -2.62 | `cross_scale(cs_bucket_rank(cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), day_first(Volume)), 10)` |

## 拆解(14 次评估)

### head score -2.40:`signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3))))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3)))))` | -2.47 | -2.29 | -2.47 | — | (子树本身) |
| sufficiency | `neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3))))` | -2.47 | -2.29 | -2.47 | — | (子树本身) |
| sufficiency | `sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3)))` | -2.47 | -2.29 | -2.47 | — | (子树本身) |
| sufficiency | `day_std(nt_ts_autocorr_s1(Ret, 3))` | -2.47 | -2.29 | -2.47 | — | (子树本身) |
| knockout | `neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3)))))` | -2.47 | -2.29 | -2.47 | +0.07 | `signedpower(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3)))))` |
| knockout | `sigmoid(day_std(nt_ts_autocorr_s1(Ret, 3)))` | -2.47 | -2.29 | -2.47 | +0.07 | `signedpower(neg(neg(day_std(nt_ts_autocorr_s1(Ret, 3)))))` |
| window | `nt_ts_autocorr_s1@3->2` | -1.51 | -1.39 | -1.51 | — | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 2))))))` |
| window | `nt_ts_autocorr_s1@3->6` | -3.66 | -2.84 | -3.66 | — | `signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 6))))))` |

### head score -2.47:`ts_quantile_q75(day_q_stat_std(nt_ts_autocorr_s1(nt_ts_autocorr_s1(Ret, 3), 3)), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(nt_ts_autocorr_s1(nt_ts_autocorr_s1(Ret, 3), 3))` | -6.80 | -6.01 | -6.80 | — | (子树本身) |
| window | `ts_quantile_q75@40->20` | -2.72 | -2.45 | -2.72 | — | `ts_quantile_q75(day_q_stat_std(nt_ts_autocorr_s1(nt_ts_autocorr_s1(Ret, 3), 3)), 20)` |
| window | `ts_quantile_q75@40->80` | -4.19 | -2.24 | -4.19 | — | `ts_quantile_q75(day_q_stat_std(nt_ts_autocorr_s1(nt_ts_autocorr_s1(Ret, 3), 3)), 80)` |

### head score -2.55:`sigmoid(day_durbin_watson(nt_ts_autocorr_s1(Ret, 3)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(nt_ts_autocorr_s1(Ret, 3))` | -2.61 | -2.40 | -2.61 | — | (子树本身) |
| window | `nt_ts_autocorr_s1@3->2` | -2.27 | -1.97 | -2.27 | — | `sigmoid(day_durbin_watson(nt_ts_autocorr_s1(Ret, 2)))` |
| window | `nt_ts_autocorr_s1@3->6` | -2.85 | -2.59 | -2.85 | — | `sigmoid(day_durbin_watson(nt_ts_autocorr_s1(Ret, 6)))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_cov(Vwap, Vwap)` — enrichment,均值差 +1.89,p 0.000
2. `cross_regbeta(day_cov(Vwap, Vwap), day_at_max_ratio(High), 241)` — enrichment,均值差 +1.87,p 0.001
3. `day_at_max_ratio(High)` — enrichment,均值差 +1.81,p 0.000
4. `pow_05(cross_regbeta(day_cov(Vwap, Vwap), day_at_max_ratio(High), 241))` — enrichment,均值差 +1.71,p 0.002
5. `day_cov(Vwap, Close)` — enrichment,均值差 +1.61,p 0.000
6. `pow_05(cross_regbeta(day_cov(Vwap, Close), day_q_stat_std(High), 241))` — enrichment,均值差 +1.59,p 0.009
7. `cross_regbeta(day_cov(Vwap, Close), day_q_stat_std(High), 241)` — enrichment,均值差 +1.58,p 0.003
8. `day_q_stat_std(High)` — enrichment,均值差 +1.55,p 0.000
9. `day_topw_mean(Vwap, Close)` — enrichment,均值差 +1.52,p 0.001
10. `cross_regbeta(day_topw_mean(Vwap, Close), day_q_stat_std(High), 241)` — enrichment,均值差 +1.19,p 0.054
11. `cs_regres(day_argmax(High), day_last(High))` — enrichment,均值差 +1.05,p 0.083
12. `day_std(Ret)` — enrichment,均值差 +0.99,p 0.001
13. `day_corr(Ret, Volume)` — enrichment,均值差 +0.98,p 0.070
14. `day_wmean(Ret, Volume)` — enrichment,均值差 +0.98,p 0.024
15. `sub(day_wmean(Ret, Volume), day_mean(Ret))` — enrichment,均值差 +0.95,p 0.068
16. `day_last(High)` — enrichment,均值差 +0.80,p 0.042

## 本组之前各轮的任务

- `prods2054Pr1a_Na`:核心 `—`;评分 67,过线 0,入 heads 0;采样计数 {'c05_skeleton': 14}
  - score -0.09(train -0.04 valid -0.09):`cross_mean(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_mean(Ret)), 60)`
  - score -0.18(train -0.18 valid -0.06):`cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 60)`
  - score -0.24(train -0.24 valid -0.16):`cross_mean(day_wmean(Ret, Volume), 60)`
  - score -0.24(train -0.24 valid -0.16):`cross_mean(sub(sub(day_wmean(Ret, Volume), day_wmean(Ret, Volume)), day_wmean(Ret, Volume)), 60)`
  - score -0.56(train -0.55 valid -0.56):`cross_mean(sub(sub(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_mean(Ret)), day_mean(Ret)), day_mean(Ret)), 60)`
- `prods2054Pr1b_Nb`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 10}
  - score -0.36(train -0.36 valid -0.33):`cross_corr(day_std(High), ts_mean(inv(ts_decay_linear(day_at_max_ratio(Close), 40)), 40), 241)`
  - score -0.52(train -0.44 valid -0.52):`cross_corr(day_std(Ret), cs_regres(day_argmax(Vwap), day_last(High)), 241)`
  - score -0.66(train -0.51 valid -0.66):`cross_corr(day_std(Ret), cs_regres(day_argmax(High), day_last(High)), 241)`
  - score -0.68(train -0.55 valid -0.68):`cross_corr(day_std(Ret), cs_regres(cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), day_last(High)), 241)`
  - score -0.70(train -0.47 valid -0.70):`cross_reg_tvalue(day_std(Ret), cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), 241)`
- `prods2054Pr2a_Ea`:核心 `cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High))`;评分 87,过线 0,入 heads 0;采样计数 {'c05_no_core': 388, 'c05_skeleton': 189, 'c05_periphery_seen': 2}
  - score -0.87(train -0.87 valid -0.79):`cross_regbeta(cs_regres(cs_regres(cross_mean(cs_regres(cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), day_mean(Ret)), 40), day_es_ratio_lo(High)), day_es_ratio_lo(High)), day_sum(High), 60)`
  - score -1.27(train -1.27 valid -0.34):`ts_regalpha(cross_mean(day_es_ratio_lo(High), 15), cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), 10)`
  - score -1.65(train -1.65 valid -1.40):`cross_regbeta(cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), day_sum(High), 241)`
  - score -1.73(train -1.61 valid -1.73):`cross_fangzheng(cross_fangzheng(cross_regbeta(cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), day_es_ratio_hi(Ret), 60), 10), 10)`
  - score -1.76(train -1.76 valid -1.48):`ts_regalpha(cs_last_low10(day_argmax(High), day_wstd(Close, Close)), cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), 10)`
- `prods2054Pr2b_Nb`:核心 `—`;评分 94,过线 0,入 heads 0;采样计数 {'c05_skeleton': 8}
  - score +0.17(train +0.44 valid +0.17):`pow_05(cross_regbeta(day_cov(Vwap, Amt), pow_05(cross_regbeta(day_cov(Vwap, Amt), day_q_stat_std(High), 241)), 241))`
  - score +0.09(train +0.13 valid +0.09):`pow_05(cross_regbeta(day_cov(Vwap, Vwap), day_at_max_ratio(High), 241))`
  - score -0.06(train +0.06 valid -0.06):`pow_05(cross_regbeta(day_cov(Vwap, Close), pow_05(cross_regbeta(day_cov(Vwap, Close), pow_05(cross_regbeta(day_cov(Vwap, Close), day_q_stat_std(High), 241)), 241)), 241))`
  - score -0.12(train -0.12 valid +0.20):`pow_05(cross_regbeta(day_cov(Vwap, Close), pow_05(cross_regbeta(day_cov(Vwap, Close), day_q_stat_std(High), 241)), 241))`
  - score -0.13(train -0.13 valid +0.20):`pow_05(cross_regbeta(day_cov(Vwap, High), pow_05(cross_regbeta(day_cov(Vwap, High), day_q_stat_std(High), 241)), 241))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.89(window nt_ts_autocorr_s1@3->2):`signedpower(neg(neg(sigmoid(day_std(nt_ts_autocorr_s1(Ret, 2))))))`
- 增益 +0.28(window nt_ts_autocorr_s1@3->2):`sigmoid(day_durbin_watson(nt_ts_autocorr_s1(Ret, 2)))`
