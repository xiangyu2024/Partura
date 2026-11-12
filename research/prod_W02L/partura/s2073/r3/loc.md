# 定位:种子 2073,P 组,第 3 轮(只含 train / valid)

快照:prods2073M1_I0_open_search, prods2073M2_I0_open_search, prods2073M3_I0_open_search, prods2073Pr1a_Ea, prods2073Pr1b_Nb, prods2073Pr2a_Ea, prods2073Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.14 | +0.04 | -0.14 | +1 | 5 | prods2073M3_I0_open_search | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 60)` |
| -0.52 | -0.46 | -0.52 | +1 | 5 | prods2073M3_I0_open_search | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_durbin_watson(Open), 1)), 5)` |
| -0.57 | -0.47 | -0.57 | +1 | 20 | prods2073M3_I0_open_search | `abs_(ts_std(ts_std(day_close(Amt), 40), 40))` |
| -1.25 | -0.50 | -1.25 | +1 | 0 | prods2073M2_I0_open_search | `ts_max(day_corr(pow_1_5(Ret), Close), 60)` |
| -1.47 | -1.26 | -1.47 | -1 | 5 | prods2073M2_I0_open_search | `day_quantile_q75(cross_sum(pow_1_5(Volume), 3))` |
| -2.21 | -1.54 | -2.21 | -1 | 20 | prods2073M1_I0_open_search | `pow_05(day_max(nt_ts_stddev(Vwap, 30)))` |
| -2.41 | -1.60 | -2.41 | -1 | 5 | prods2073M2_I0_open_search | `pow_2(day_max(pow_1_5(Vwap)))` |
| -2.41 | -1.61 | -2.41 | -1 | 20 | prods2073M1_I0_open_search | `day_quantile_q75(add(in_sorted_cumsum_backward(nt_ts_stddev(Close, 60), in_sum(Low)), cross_scale(ts_scale(day_cov(Low, High), 30), 15)))` |
| -2.48 | -2.48 | -1.41 | +1 | 5 | prods2073M1_I0_open_search | `ts_stddev(day_sum(nt_ts_stddev(Amt, 3)), 20)` |

## 共性:238 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.50 | 0.000 | 9 | -0.76 / -2.26 | `day_close(Amt)` |
| +1.44 | 0.000 | 7 | -0.80 / -2.24 | `ts_std(day_close(Amt), 50)` |
| +1.44 | 0.000 | 7 | -0.80 / -2.24 | `pow_3(ts_std(day_close(Amt), 50))` |
| +1.33 | 0.001 | 7 | -0.91 / -2.24 | `day_durbin_watson(Open)` |
| +1.30 | 0.002 | 5 | -0.92 / -2.23 | `div(day_cov(Low, High), div(day_mean(Close), day_mean(Close)))` |
| +1.30 | 0.002 | 5 | -0.92 / -2.23 | `div(day_mean(Close), day_mean(Close))` |
| +1.24 | 0.008 | 4 | -0.98 / -2.22 | `cross_zscore(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), 120)` |
| +1.19 | 0.011 | 4 | -1.03 / -2.22 | `mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(Open)), 1))` |
| +1.08 | 0.010 | 5 | -1.14 / -2.22 | `signedpower(day_durbin_watson(Open))` |
| +1.08 | 0.010 | 5 | -1.14 / -2.22 | `ts_min(signedpower(day_durbin_watson(Open)), 1)` |
| +1.01 | 0.000 | 17 | -1.26 / -2.27 | `cs_bucket_demean(day_mean(Close), day_first(Close))` |
| +0.93 | 0.000 | 53 | -1.47 / -2.41 | `day_mean(Close)` |
| +0.79 | 0.073 | 4 | -1.43 / -2.21 | `div(day_cov(Low, High), mul(day_mean(Close), day_mean(Close)))` |
| +0.79 | 0.055 | 4 | -1.43 / -2.21 | `cross_corr(day_cov(Low, High), day_sum(Amt), 60)` |
| +0.78 | 0.050 | 5 | -1.43 / -2.22 | `day_sum(Low)` |
| +0.69 | 0.117 | 4 | -1.52 / -2.21 | `day_mean(Low)` |
| +0.69 | 0.059 | 6 | -1.52 / -2.22 | `mul(day_mean(Close), day_mean(Close))` |
| +0.68 | 0.004 | 22 | -1.59 / -2.26 | `day_first(Close)` |
| +0.61 | 0.000 | 49 | -1.72 / -2.33 | `day_cov(Low, Close)` |
| +0.60 | 0.109 | 4 | -1.61 / -2.21 | `ts_skew(day_cov(Low, High), 40)` |

## 拆解(35 次评估)

### head score -0.14:`cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1))` | -0.73 | -0.56 | -0.73 | — | (子树本身) |
| sufficiency | `ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)` | -0.52 | -0.52 | -0.39 | — | (子树本身) |
| sufficiency | `pow_3(ts_std(day_close(Amt), 50))` | -0.52 | -0.52 | -0.39 | — | (子树本身) |
| sufficiency | `ts_std(day_durbin_watson(Open), 40)` | -2.42 | -1.15 | -2.42 | — | (子树本身) |
| knockout | `mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1))` | -1.21 | -0.06 | -1.21 | +1.08 | `cross_max(ts_std(day_durbin_watson(Open), 40), 60)` |
| knockout | `ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)` | -0.17 | +0.04 | -0.17 | +0.03 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), pow_3(ts_std(day_close(Amt), 50))), 60)` |
| knockout | `pow_3(ts_std(day_close(Amt), 50))` | -0.21 | +0.27 | -0.21 | +0.07 | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(ts_std(day_close(Amt), 50), 1)), 60)` |
| knockout | `ts_std(day_durbin_watson(Open), 40)` | -0.37 | -0.37 | -0.24 | +0.23 | `cross_max(mul(day_durbin_watson(Open), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 60)` |
| swap | `Open->Close` | -0.02 | -0.01 | -0.02 | — | `cross_max(mul(ts_std(day_durbin_watson(Close), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 60)` |
| swap | `Amt->Volume` | -1.91 | -0.80 | -1.91 | — | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Volume), 50)), 1)), 60)` |
| window | `cross_max@60->30` | -0.36 | -0.36 | -0.22 | — | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 30)` |
| window | `cross_max@60->120` | +0.21 | +0.21 | +0.33 | — | `cross_max(mul(ts_std(day_durbin_watson(Open), 40), ts_min(pow_3(ts_std(day_close(Amt), 50)), 1)), 120)` |

### head score -0.52:`cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_durbin_watson(Open), 1)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_durbin_watson(Open), 1))` | -0.43 | -0.20 | -0.43 | — | (子树本身) |
| sufficiency | `pow_3(ts_std(day_close(Amt), 50))` | -0.52 | -0.52 | -0.39 | — | (子树本身) |
| sufficiency | `ts_std(day_close(Amt), 50)` | -0.52 | -0.52 | -0.39 | — | (子树本身) |
| sufficiency | `ts_min(day_durbin_watson(Open), 1)` | -4.18 | -4.18 | -3.92 | — | (子树本身) |
| knockout | `mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_durbin_watson(Open), 1))` | -0.45 | -0.45 | -0.35 | -0.07 | `cross_max(pow_3(ts_std(day_close(Amt), 50)), 5)` |
| knockout | `pow_3(ts_std(day_close(Amt), 50))` | -1.24 | -0.93 | -1.24 | +0.73 | `cross_max(mul(ts_std(day_close(Amt), 50), ts_min(day_durbin_watson(Open), 1)), 5)` |
| knockout | `ts_std(day_close(Amt), 50)` | -3.15 | -3.15 | -1.94 | +2.63 | `cross_max(mul(pow_3(day_close(Amt)), ts_min(day_durbin_watson(Open), 1)), 5)` |
| knockout | `ts_min(day_durbin_watson(Open), 1)` | -0.46 | -0.46 | -0.46 | -0.06 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), day_durbin_watson(Open)), 5)` |
| swap | `Amt->Volume` | -1.28 | -1.01 | -1.28 | — | `cross_max(mul(pow_3(ts_std(day_close(Volume), 50)), ts_min(day_durbin_watson(Open), 1)), 5)` |
| swap | `Open->Close` | -0.46 | -0.46 | -0.45 | — | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_durbin_watson(Close), 1)), 5)` |
| window | `cross_max@5->2` | -0.46 | -0.34 | -0.46 | — | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_durbin_watson(Open), 1)), 2)` |
| window | `cross_max@5->10` | -0.48 | -0.47 | -0.48 | — | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_durbin_watson(Open), 1)), 10)` |

### head score -0.57:`abs_(ts_std(ts_std(day_close(Amt), 40), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(ts_std(day_close(Amt), 40), 40)` | -0.58 | -0.47 | -0.58 | — | (子树本身) |
| sufficiency | `ts_std(day_close(Amt), 40)` | -0.65 | -0.65 | -0.52 | — | (子树本身) |
| sufficiency | `day_close(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| knockout | `ts_std(ts_std(day_close(Amt), 40), 40)` | -0.65 | -0.65 | -0.52 | +0.08 | `abs_(ts_std(day_close(Amt), 40))` |
| swap | `Amt->Volume` | -1.85 | -1.24 | -1.85 | — | `abs_(ts_std(ts_std(day_close(Volume), 40), 40))` |
| window | `ts_std@40->20` | -0.38 | -0.38 | +0.23 | — | `abs_(ts_std(ts_std(day_close(Amt), 40), 20))` |
| window | `ts_std@40->80` | -0.04 | -0.04 | +0.11 | — | `abs_(ts_std(ts_std(day_close(Amt), 40), 80))` |

### head score -1.25:`ts_max(day_corr(pow_1_5(Ret), Close), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(pow_1_5(Ret), Close)` | -4.39 | -4.39 | -3.76 | — | (子树本身) |
| swap | `Close->Vwap` | -1.79 | -1.79 | -0.96 | — | `ts_max(day_corr(pow_1_5(Ret), Vwap), 60)` |
| window | `ts_max@60->30` | -1.06 | -0.77 | -1.06 | — | `ts_max(day_corr(pow_1_5(Ret), Close), 30)` |
| window | `ts_max@60->120` | -0.52 | -0.43 | -0.52 | — | `ts_max(day_corr(pow_1_5(Ret), Close), 120)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_close(Amt)` — enrichment,均值差 +1.50,p 0.000
2. `ts_std(day_close(Amt), 50)` — enrichment,均值差 +1.44,p 0.000
3. `pow_3(ts_std(day_close(Amt), 50))` — enrichment,均值差 +1.44,p 0.000
4. `day_durbin_watson(Open)` — enrichment,均值差 +1.33,p 0.001
5. `div(day_cov(Low, High), div(day_mean(Close), day_mean(Close)))` — enrichment,均值差 +1.30,p 0.002
6. `div(day_mean(Close), day_mean(Close))` — enrichment,均值差 +1.30,p 0.002
7. `cross_zscore(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), 120)` — enrichment,均值差 +1.24,p 0.008
8. `mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(Open)), 1))` — enrichment,均值差 +1.19,p 0.011
9. `signedpower(day_durbin_watson(Open))` — enrichment,均值差 +1.08,p 0.010
10. `ts_min(signedpower(day_durbin_watson(Open)), 1)` — enrichment,均值差 +1.08,p 0.010
11. `cs_bucket_demean(day_mean(Close), day_first(Close))` — enrichment,均值差 +1.01,p 0.000
12. `day_mean(Close)` — enrichment,均值差 +0.93,p 0.000
13. `div(day_cov(Low, High), mul(day_mean(Close), day_mean(Close)))` — enrichment,均值差 +0.79,p 0.073
14. `cross_corr(day_cov(Low, High), day_sum(Amt), 60)` — enrichment,均值差 +0.79,p 0.055
15. `day_sum(Low)` — enrichment,均值差 +0.78,p 0.050
16. `mul(day_mean(Close), day_mean(Close))` — enrichment,均值差 +0.69,p 0.059
17. `day_first(Close)` — enrichment,均值差 +0.68,p 0.004
18. `day_cov(Low, Close)` — enrichment,均值差 +0.61,p 0.000
19. `cross_quantile_q75(day_es_ratio_lo(Ret), 60)` — enrichment,均值差 +0.54,p 0.058
20. `day_cov(Low, High)` — enrichment,均值差 +0.44,p 0.004

## 本组之前各轮的任务

- `prods2073Pr1a_Ea`:核心 `day_cov(Low, High)`;评分 90,过线 0,入 heads 0;采样计数 {'c05_no_core': 1543, 'c05_skeleton': 819}
  - score -0.66(train +0.09 valid -0.66):`cross_corr(day_cov(Low, High), cross_zscore(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), 120), 60)`
  - score -0.70(train -0.70 valid -0.12):`cross_corr(day_cov(Low, High), day_sum(Low), 60)`
  - score -0.70(train -0.70 valid -0.12):`cross_corr(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), day_sum(Low), 60)`
  - score -0.73(train +0.06 valid -0.73):`cross_corr(day_cov(Low, Close), cross_zscore(div(day_cov(Low, High), div(day_mean(Close), day_mean(Close))), 120), 60)`
  - score -0.76(train -0.76 valid -0.50):`cross_corr(day_cov(Low, High), day_sum(Amt), 60)`
- `prods2073Pr1b_Nb`:核心 `—`;评分 90,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -1.50(train -1.50 valid -1.38):`cross_mean(ts_med(day_wmean(Ret, Volume), 10), 20)`
  - score -1.56(train -1.50 valid -1.56):`cross_madz(sqrt(ts_max(ts_med(day_topw_mean(Ret, Volume), 10), 10)), 241)`
  - score -1.58(train -1.58 valid -1.45):`cross_madz(sqrt(ts_max(ts_max(ts_max(ts_med(day_topw_mean(Ret, Ret), 5), 10), 5), 10)), 241)`
  - score -1.59(train -1.06 valid -1.59):`cross_madz(sqrt(ts_max(ts_max(ts_max(ts_med(day_topw_mean(Ret, Volume), 10), 10), 5), 10)), 241)`
  - score -1.66(train -1.66 valid -1.30):`cross_mean(ts_med(day_topw_mean(Ret, Volume), 10), 20)`
- `prods2073Pr2a_Ea`:核心 `day_cov(Low, Close)`;评分 82,过线 0,入 heads 0;采样计数 {'c05_skeleton': 747, 'c05_no_core': 1556}
  - score -0.40(train -0.36 valid -0.40):`cross_corr(day_cov(Low, Close), day_gini(Close), 60)`
  - score -0.65(train -0.34 valid -0.65):`cross_corr(day_cov(Low, Close), cross_corr(day_cov(Low, Close), day_mean(Close), 10), 60)`
  - score -0.66(train -0.36 valid -0.66):`cross_corr(day_cov(Low, Close), cross_corr(day_cov(Low, Close), day_mean(Low), 10), 60)`
  - score -0.69(train -0.69 valid -0.13):`cross_corr(day_cov(Low, Close), day_mean(Close), 60)`
  - score -0.70(train -0.70 valid -0.14):`cross_corr(day_cov(Low, Close), day_mean(Low), 60)`
- `prods2073Pr2b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.42(train -0.42 valid -0.41):`cross_quantile_q25(cs_last_high40(cs_bucket_rank(cross_quantile_q75(day_es_ratio_lo(Ret), 60), BoardCode), cs_last_high10(cross_quantile_q25(cs_last_high40(cs_bucket_rank(cross_quantile_q75(day_es_ratio_lo(Ret), 60), BoardCode), cs_bucket_demean(day_mean(Close), day_first(Close))), 15), day_first(Close))), 15)`
  - score -0.55(train -0.55 valid -0.15):`cross_quantile_q25(cs_last_high40(cs_bucket_rank(cross_quantile_q75(BoardCode, 60), BoardCode), cs_bucket_demean(day_mean(Close), day_first(Close))), 15)`
  - score -0.59(train -0.30 valid -0.59):`cross_quantile_q25(cs_last_high40(cs_bucket_rank(cross_quantile_q75(cs_bucket_demean(day_mean(Close), day_first(Close)), 60), BoardCode), cs_bucket_demean(day_mean(Close), day_first(Close))), 15)`
  - score -0.64(train -0.64 valid -0.19):`cross_quantile_q25(cs_last_high40(cs_bucket_rank(cross_quantile_q75(day_es_ratio_lo(Ret), 60), day_first(Close)), cs_bucket_demean(day_mean(Close), day_first(Close))), 15)`
  - score -0.71(train -0.41 valid -0.71):`cross_quantile_q25(cs_last_high40(cs_bucket_rank(day_close(High), day_close(High)), cs_bucket_demean(day_mean(Close), day_first(Close))), 15)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.73(window ts_max@60->120):`ts_max(day_corr(pow_1_5(Ret), Close), 120)`
- 增益 +0.19(window ts_max@60->30):`ts_max(day_corr(pow_1_5(Ret), Close), 30)`
