# 定位:种子 2075,P 组,第 3 轮(只含 train / valid)

快照:prods2075M1_I0_open_search, prods2075M2_I0_open_search, prods2075M3_I0_open_search, prods2075Pr1a_Ea, prods2075Pr1b_Nb, prods2075Pr2a_I0_open_search, prods2075Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.12 | +0.03 | -0.12 | +1 | 5 | prods2075M2_I0_open_search | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)` |
| -0.51 | -0.07 | -0.51 | +1 | 5 | prods2075M2_I0_open_search | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 60)` |
| -0.53 | -0.53 | +0.01 | -1 | 20 | prods2075M1_I0_open_search | `abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5)))))` |
| -0.86 | -0.86 | -0.66 | +1 | 20 | prods2075M1_I0_open_search | `cross_autocorr_s1(day_cov(Ret, Volume), 482)` |
| -1.09 | -1.09 | -1.07 | -1 | 0 | prods2075M2_I0_open_search | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0))))), 20)` |
| -1.46 | -1.46 | -0.73 | +1 | 5 | prods2075M1_I0_open_search | `add(sigmoid(sqrt(cross_quantile_q75(day_var(High), 15))), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))` |
| -1.58 | -1.55 | -1.58 | -1 | 20 | prods2075M3_I0_open_search | `cross_mean(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15)), 60)` |
| -1.80 | -1.72 | -1.80 | -1 | 5 | prods2075M3_I0_open_search | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 20)` |
| -2.06 | -2.06 | -1.81 | +1 | 20 | prods2075M3_I0_open_search | `cross_regres(day_argmax(Open), day_quantile_q75(Open), 60)` |

## 共性:280 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.69 | 0.000 | 12 | -0.76 / -2.46 | `sub(day_wmean(Ret, Volume), day_mean(Ret))` |
| +1.69 | 0.001 | 5 | -0.73 / -2.41 | `cross_ema(day_wmean(Ret, Volume), 20)` |
| +1.57 | 0.003 | 4 | -0.83 / -2.41 | `cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)` |
| +1.48 | 0.000 | 7 | -0.94 / -2.42 | `cross_tail_mean_q25(day_durbin_watson(Vwap), 3)` |
| +1.44 | 0.000 | 23 | -1.06 / -2.50 | `day_wmean(Ret, Volume)` |
| +1.41 | 0.003 | 5 | -1.00 / -2.41 | `cross_ema(day_std(Ret), 20)` |
| +1.38 | 0.001 | 7 | -1.04 / -2.42 | `day_std(Ret)` |
| +1.36 | 0.000 | 15 | -1.09 / -2.46 | `day_mean(Ret)` |
| +1.12 | 0.000 | 40 | -1.43 / -2.54 | `day_last(in_top_quantile_flag_q10(Ret))` |
| +1.08 | 0.004 | 8 | -1.33 / -2.41 | `day_last(Vwap)` |
| +1.07 | 0.018 | 5 | -1.33 / -2.40 | `mul(day_at_min_ratio(Ret), BoardCode)` |
| +0.92 | 0.001 | 14 | -1.51 / -2.43 | `cross_tail_mean_q25(day_durbin_watson(Vwap), 60)` |
| +0.90 | 0.001 | 18 | -1.54 / -2.44 | `mul(day_at_min_ratio(Low), BoardCode)` |
| +0.89 | 0.033 | 6 | -1.52 / -2.40 | `day_at_min_ratio(Ret)` |
| +0.88 | 0.000 | 23 | -1.57 / -2.46 | `day_at_min_ratio(Low)` |
| +0.78 | 0.048 | 5 | -1.61 / -2.40 | `sub(mul(day_at_min_ratio(Low), BoardCode), cross_tail_mean_q25(day_durbin_watson(Vwap), 60))` |
| +0.74 | 0.000 | 36 | -1.74 / -2.48 | `day_durbin_watson(Vwap)` |
| +0.64 | 0.074 | 6 | -1.75 / -2.40 | `day_topw_mean(Ret, Amt)` |
| +0.49 | 0.042 | 24 | -1.94 / -2.42 | `day_last(Close)` |
| +0.48 | 0.139 | 6 | -1.92 / -2.39 | `cross_tail_mean_q25(day_durbin_watson(Vwap), 30)` |

## 拆解(35 次评估)

### head score -0.51:`cross_mean(div(day_skew(Ret), day_kurt(Ret)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_skew(Ret), day_kurt(Ret))` | -2.48 | -2.48 | -2.19 | — | (子树本身) |
| sufficiency | `day_skew(Ret)` | -3.46 | -3.46 | -2.74 | — | (子树本身) |
| sufficiency | `day_kurt(Ret)` | -3.81 | -2.76 | -3.81 | — | (子树本身) |
| knockout | `div(day_skew(Ret), day_kurt(Ret))` | -0.87 | -0.68 | -0.87 | +0.37 | `cross_mean(day_skew(Ret), 60)` |
| window | `cross_mean@60->30` | -0.73 | -0.15 | -0.73 | — | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 30)` |
| window | `cross_mean@60->120` | -0.51 | +0.01 | -0.51 | — | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 120)` |

### head score -1.58:`cross_mean(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15))` | -2.11 | -2.11 | -2.07 | — | (子树本身) |
| sufficiency | `cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15)` | -2.11 | -2.11 | -2.07 | — | (子树本身) |
| sufficiency | `cross_min(neg(day_cov(Low, Close)), 15)` | -2.44 | -1.61 | -2.44 | — | (子树本身) |
| sufficiency | `neg(day_cov(Low, Close))` | -2.28 | -1.54 | -2.28 | — | (子树本身) |
| knockout | `neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15))` | -1.63 | -1.55 | -1.63 | +0.04 | `cross_mean(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15), 60)` |
| knockout | `cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15)` | -2.41 | -1.61 | -2.41 | +0.83 | `cross_mean(neg(cross_min(neg(day_cov(Low, Close)), 15)), 60)` |
| knockout | `cross_min(neg(day_cov(Low, Close)), 15)` | -1.70 | -1.70 | -1.69 | +0.12 | `cross_mean(neg(cross_cov(neg(day_cov(Low, Close)), cross_mean(day_corr(Low, Ret), 60), 15)), 60)` |
| knockout | `neg(day_cov(Low, Close))` | -1.29 | -1.29 | -1.05 | -0.29 | `cross_mean(neg(cross_cov(cross_min(day_cov(Low, Close), 15), cross_mean(day_corr(Low, Ret), 60), 15)), 60)` |
| swap | `Low->High` | -1.89 | -1.89 | -1.46 | — | `cross_mean(neg(cross_cov(cross_min(neg(day_cov(High, Close)), 15), cross_mean(day_corr(High, Ret), 60), 15)), 60)` |
| swap | `Close->Vwap` | -1.66 | -1.66 | -1.58 | — | `cross_mean(neg(cross_cov(cross_min(neg(day_cov(Low, Vwap)), 15), cross_mean(day_corr(Low, Ret), 60), 15)), 60)` |
| window | `cross_mean@60->30` | -1.95 | -1.72 | -1.95 | — | `cross_mean(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15)), 30)` |
| window | `cross_mean@60->120` | -1.43 | -1.43 | -1.08 | — | `cross_mean(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15)), 120)` |

### head score -1.80:`cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4))))` | -2.15 | -2.00 | -2.15 | — | (子树本身) |
| sufficiency | `add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))` | -2.20 | -2.07 | -2.20 | — | (子树本身) |
| sufficiency | `mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4))` | -6.17 | -6.17 | -5.19 | — | (子树本身) |
| sufficiency | `mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6))` | -1.91 | -1.70 | -1.91 | — | (子树本身) |
| knockout | `pow(abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))), 1.5)` | -1.89 | -1.89 | -1.86 | +0.09 | `cross_mean(div(abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))), add(pow(day_sum(Amt), 0.7), 5000000)), 20)` |
| knockout | `abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4))))` | -1.74 | -1.74 | -1.72 | -0.07 | `cross_mean(div(pow(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 20)` |
| knockout | `add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))` | -1.47 | -1.29 | -1.47 | -0.33 | `cross_mean(div(pow(abs_(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 20)` |
| knockout | `mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4))` | -2.16 | -2.16 | -2.09 | +0.35 | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 20)` |
| swap | `High->Low` | -1.84 | -1.84 | -1.81 | — | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(Low), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 20)` |
| swap | `Low->High` | -1.81 | -1.73 | -1.81 | — | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_min(High)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 20)` |
| window | `cross_mean@20->10` | -1.79 | -1.63 | -1.79 | — | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 10)` |
| window | `cross_mean@20->40` | -1.78 | -1.78 | -1.64 | — | `cross_mean(div(pow(abs_(add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 40)` |

### head score -2.06:`cross_regres(day_argmax(Open), day_quantile_q75(Open), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_argmax(Open)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile_q75(Open)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| swap | `Open->Close` | -2.13 | -2.13 | -1.73 | — | `cross_regres(day_argmax(Close), day_quantile_q75(Close), 60)` |
| window | `cross_regres@60->30` | -3.32 | -3.04 | -3.32 | — | `cross_regres(day_argmax(Open), day_quantile_q75(Open), 30)` |
| window | `cross_regres@60->120` | -2.00 | -2.00 | -1.70 | — | `cross_regres(day_argmax(Open), day_quantile_q75(Open), 120)` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_wmean(Ret, Volume), day_mean(Ret))` — enrichment,均值差 +1.69,p 0.000
2. `cross_ema(day_wmean(Ret, Volume), 20)` — enrichment,均值差 +1.69,p 0.001
3. `cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)` — enrichment,均值差 +1.57,p 0.003
4. `cross_tail_mean_q25(day_durbin_watson(Vwap), 3)` — enrichment,均值差 +1.48,p 0.000
5. `day_wmean(Ret, Volume)` — enrichment,均值差 +1.44,p 0.000
6. `cross_ema(day_std(Ret), 20)` — enrichment,均值差 +1.41,p 0.003
7. `day_std(Ret)` — enrichment,均值差 +1.38,p 0.001
8. `day_mean(Ret)` — enrichment,均值差 +1.36,p 0.000
9. `day_last(in_top_quantile_flag_q10(Ret))` — enrichment,均值差 +1.12,p 0.000
10. `day_last(Vwap)` — enrichment,均值差 +1.08,p 0.004
11. `mul(day_at_min_ratio(Ret), BoardCode)` — enrichment,均值差 +1.07,p 0.018
12. `cross_tail_mean_q25(day_durbin_watson(Vwap), 60)` — enrichment,均值差 +0.92,p 0.001
13. `mul(day_at_min_ratio(Low), BoardCode)` — enrichment,均值差 +0.90,p 0.001
14. `day_at_min_ratio(Ret)` — enrichment,均值差 +0.89,p 0.033
15. `day_at_min_ratio(Low)` — enrichment,均值差 +0.88,p 0.000
16. `sub(mul(day_at_min_ratio(Low), BoardCode), cross_tail_mean_q25(day_durbin_watson(Vwap), 60))` — enrichment,均值差 +0.78,p 0.048
17. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.74,p 0.000
18. `day_topw_mean(Ret, Amt)` — enrichment,均值差 +0.64,p 0.074
19. `day_last(Close)` — enrichment,均值差 +0.49,p 0.042

## 本组之前各轮的任务

- `prods2075Pr1a_Ea`:核心 `ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5)`;评分 46,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2815, 'c05_no_core': 4665}
  - score -2.31(train -2.31 valid -2.24):`day_q_stat_std(Amt)`
  - score -2.55(train -2.47 valid -2.55):`day_signed_ratio(Ret, Vwap)`
  - score -2.77(train -2.17 valid -2.77):`day_centroid(Ret)`
  - score -3.08(train -2.24 valid -3.08):`day_es_ratio_hi(Close)`
  - score -3.93(train -3.93 valid -3.13):`day_cov(Ret, Amt)`
- `prods2075Pr1b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.44(train -0.18 valid -0.44):`div(cross_ema(day_wmean(Ret, Volume), 20), cross_ema(day_std(Ret), 20))`
  - score -0.48(train -0.46 valid -0.48):`cs_demean(cross_ema(sub(cs_demean(cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 15)), day_mean(Ret)), 20))`
  - score -0.48(train -0.37 valid -0.48):`cross_ema(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_mean(Ret)), 20)`
  - score -0.49(train -0.22 valid -0.49):`div(cross_ema(cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 15), 20), cross_ema(day_std(Ret), 20))`
  - score -0.49(train -0.30 valid -0.49):`cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)`
- `prods2075Pr2a_I0_open_search`:核心 `—`;评分 99,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score +0.31(train +0.31 valid +0.48):`cross_reg_fvalue(day_last(in_top_quantile_flag_q10(Ret)), sub(mul(day_at_min_ratio(Low), BoardCode), cross_tail_mean_q25(day_durbin_watson(in_top_quantile_flag_q10(Ret)), 3)), 241)`
  - score -0.50(train +0.10 valid -0.50):`cross_reg_fvalue(day_last(in_top_quantile_flag_q10(Ret)), sub(mul(day_at_min_ratio(Ret), BoardCode), cross_tail_mean_q25(day_durbin_watson(Vwap), 3)), 241)`
  - score -0.59(train -0.59 valid -0.37):`cross_reg_fvalue(day_last(in_top_quantile_flag_q10(Ret)), sub(mul(day_at_min_ratio(Low), BoardCode), day_last(in_top_quantile_flag_q10(Ret))), 60)`
  - score -0.63(train -0.63 valid -0.14):`cross_reg_fvalue(day_last(in_top_quantile_flag_q10(Ret)), sub(mul(BoardCode, BoardCode), cross_tail_mean_q25(day_durbin_watson(Vwap), 3)), 241)`
  - score -0.69(train -0.69 valid -0.63):`cross_reg_fvalue(day_last(in_top_quantile_flag_q10(Ret)), sub(mul(day_median(Low), BoardCode), cross_tail_mean_q25(day_durbin_watson(Vwap), 3)), 241)`
- `prods2075Pr2b_Nb`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.39(train -0.39 valid -0.30):`cross_reg_fvalue(day_last(Close), day_last(Vwap), 30)`
  - score -0.73(train -0.61 valid -0.73):`cross_reg_fvalue(day_distinct_ratio(High), day_last(High), 241)`
  - score -0.74(train -0.60 valid -0.74):`cross_reg_fvalue(day_distinct_ratio(High), day_last(Vwap), 241)`
  - score -0.74(train -0.59 valid -0.74):`cross_reg_fvalue(day_distinct_ratio(High), day_last(Close), 241)`
  - score -0.82(train -0.82 valid +0.05):`cross_reg_fvalue(day_last(Close), day_last(Vwap), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.33(knockout add(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6)), mul(sub(div(cross_delay(day_first(Open), 1), day_first(Open)), create_like(day_first(Open), 1)), create_like(day_first(Open), 0.4)))):`cross_mean(div(pow(abs_(mul(div(sub(day_max(High), day_min(Low)), day_first(Open)), create_like(day_first(Open), 0.6))), 1.5), add(pow(day_sum(Amt), 0.7), 5000000)), 20)`
- 增益 +0.15(window cross_mean@60->120):`cross_mean(neg(cross_cov(cross_min(neg(day_cov(Low, Close)), 15), cross_mean(day_corr(Low, Ret), 60), 15)), 120)`
