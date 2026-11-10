# 定位:种子 2014,P 组,第 3 轮(只含 train / valid)

快照:prods2014M1_I0_open_search, prods2014M2_I0_open_search, prods2014M3_I0_open_search, prods2014Pr1a_Ea, prods2014Pr1b_Nb, prods2014Pr2a_Na, prods2014Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.71 | -0.71 | -0.41 | -1 | 5 | prods2014M2_I0_open_search | `cs_bucket_zscore(ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 80), cross_mean(day_std(Ret), 20))` |
| -0.88 | -0.43 | -0.88 | +1 | 20 | prods2014M1_I0_open_search | `ts_std(day_quantile_q25(Ret), 5)` |
| -1.20 | -1.20 | +0.29 | +1 | 0 | prods2014M1_I0_open_search | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), 241), 5)` |
| -1.22 | -1.22 | -0.28 | +1 | 5 | prods2014M1_I0_open_search | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)), 20)` |
| -1.49 | -1.38 | -1.49 | +1 | 5 | prods2014M3_I0_open_search | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(Ret), 50), 40)` |
| -1.60 | -1.42 | -1.60 | -1 | 20 | prods2014M2_I0_open_search | `ts_stddev(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 5)` |
| -1.71 | -1.71 | -1.68 | +1 | 0 | prods2014M2_I0_open_search | `ts_med(ts_cov(ts_med(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), day_close(High), 50), 40)` |
| -2.28 | -1.59 | -2.28 | -1 | 20 | prods2014M3_I0_open_search | `ts_med(ts_cov(day_quantile(pow_3(Open)), day_close(High), 50), 40)` |
| -2.30 | -1.57 | -2.30 | -1 | 20 | prods2014M3_I0_open_search | `ts_decay_linear(day_std(sub(nt_ts_stddev(nt_ts_quantile_q50(pow_3(Open), 5), 5), cross_scale(Open, 30))), 5)` |

## 共性:219 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.05 | 0.002 | 4 | -1.08 / -2.13 | `cs_regres(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), LogFloatCap)` |
| +0.85 | 0.000 | 19 | -1.34 / -2.18 | `cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241)` |
| +0.82 | 0.001 | 10 | -1.32 / -2.15 | `cross_mean(day_sum(Amt), 60)` |
| +0.82 | 0.001 | 10 | -1.32 / -2.15 | `day_sum(Amt)` |
| +0.77 | 0.024 | 5 | -1.35 / -2.13 | `cross_semistd_pos(day_close(Close), 120)` |
| +0.77 | 0.024 | 5 | -1.35 / -2.13 | `add(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120))` |
| +0.77 | 0.024 | 5 | -1.35 / -2.13 | `sub(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120))` |
| +0.77 | 0.024 | 5 | -1.35 / -2.13 | `cross_semistd_neg(day_close(Close), 120)` |
| +0.77 | 0.009 | 9 | -1.37 / -2.14 | `day_gini(Low)` |
| +0.74 | 0.051 | 4 | -1.39 / -2.12 | `div(sub(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120)), add(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120)))` |
| +0.68 | 0.001 | 19 | -1.49 / -2.17 | `day_distinct_ratio(Open)` |
| +0.67 | 0.046 | 5 | -1.46 / -2.13 | `sub(LogTotalCap, LogFloatShares)` |
| +0.62 | 0.032 | 7 | -1.51 / -2.13 | `div(LogFloatCap, day_distinct_ratio(Open))` |
| +0.62 | 0.000 | 26 | -1.57 / -2.18 | `cross_delta(sub(log(day_close(Close)), LogFloatCap), 1)` |
| +0.58 | 0.000 | 32 | -1.62 / -2.20 | `sub(log(day_close(Close)), LogFloatCap)` |
| +0.56 | 0.000 | 48 | -1.67 / -2.23 | `day_close(Close)` |
| +0.50 | 0.000 | 38 | -1.70 / -2.20 | `log(day_close(Close))` |
| +0.43 | 0.202 | 7 | -1.70 / -2.12 | `cross_sum(cross_delta(sub(LogTotalCap, LogFloatCap), 1), 241)` |
| +0.41 | 0.186 | 6 | -1.71 / -2.12 | `abs_(day_quantile_q25(Ret))` |
| +0.39 | 0.155 | 22 | -1.76 / -2.15 | `sub(LogTotalCap, LogFloatCap)` |

## 拆解(28 次评估)

### head score -0.71:`cs_bucket_zscore(ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 80), cross_mean(day_std(Ret), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 80)` | -1.27 | -1.27 | -0.50 | — | (子树本身) |
| sufficiency | `ts_cov(day_quantile_q25(Ret), day_close(Ret), 50)` | -1.76 | -1.76 | -1.23 | — | (子树本身) |
| sufficiency | `cross_mean(day_std(Ret), 20)` | -3.64 | -3.46 | -3.64 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 80)` | -1.30 | -1.05 | -1.30 | +0.59 | `cs_bucket_zscore(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), cross_mean(day_std(Ret), 20))` |
| knockout | `ts_cov(day_quantile_q25(Ret), day_close(Ret), 50)` | -2.09 | -1.17 | -2.09 | +1.38 | `cs_bucket_zscore(ts_med(day_quantile_q25(Ret), 80), cross_mean(day_std(Ret), 20))` |
| knockout | `cross_mean(day_std(Ret), 20)` | -0.99 | -0.99 | -0.28 | +0.29 | `cs_bucket_zscore(ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 80), day_std(Ret))` |
| window | `ts_med@80->40` | -0.93 | -0.93 | -0.57 | — | `cs_bucket_zscore(ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 40), cross_mean(day_std(Ret), 20))` |
| window | `ts_med@80->160` | -0.73 | -0.71 | -0.73 | — | `cs_bucket_zscore(ts_med(ts_cov(day_quantile_q25(Ret), day_close(Ret), 50), 160), cross_mean(day_std(Ret), 20))` |

### head score -1.49:`ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(Ret), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(Ret), 50)` | -1.33 | -1.33 | -1.29 | — | (子树本身) |
| sufficiency | `day_std(pow_3(Open))` | -2.36 | -1.55 | -2.36 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(Ret), 50)` | -2.31 | -1.55 | -2.31 | +0.82 | `ts_med(day_std(pow_3(Open)), 40)` |
| swap | `Open->Close` | -1.61 | -1.39 | -1.61 | — | `ts_med(ts_reg_tvalue(day_std(pow_3(Close)), day_quantile_q25(Ret), 50), 40)` |
| window | `ts_med@40->20` | -1.59 | -1.42 | -1.59 | — | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(Ret), 50), 20)` |
| window | `ts_med@40->80` | -1.35 | -1.11 | -1.35 | — | `ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(Ret), 50), 80)` |

### head score -2.28:`ts_med(ts_cov(day_quantile(pow_3(Open)), day_close(High), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_quantile(pow_3(Open)), day_close(High), 50)` | -2.27 | -1.65 | -2.27 | — | (子树本身) |
| sufficiency | `day_quantile(pow_3(Open))` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_close(High)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `ts_cov(day_quantile(pow_3(Open)), day_close(High), 50)` | -2.38 | -1.61 | -2.38 | +0.10 | `ts_med(day_quantile(pow_3(Open)), 40)` |
| swap | `Open->Close` | -2.24 | -1.59 | -2.24 | — | `ts_med(ts_cov(day_quantile(pow_3(Close)), day_close(High), 50), 40)` |
| swap | `High->Low` | -2.23 | -1.59 | -2.23 | — | `ts_med(ts_cov(day_quantile(pow_3(Open)), day_close(Low), 50), 40)` |
| window | `ts_med@40->20` | -2.20 | -1.55 | -2.20 | — | `ts_med(ts_cov(day_quantile(pow_3(Open)), day_close(High), 50), 20)` |
| window | `ts_med@40->80` | -2.30 | -1.72 | -2.30 | — | `ts_med(ts_cov(day_quantile(pow_3(Open)), day_close(High), 50), 80)` |

### head score -2.30:`ts_decay_linear(day_std(sub(nt_ts_stddev(nt_ts_quantile_q50(pow_3(Open), 5), 5), cross_scale(Open, 30))), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(sub(nt_ts_stddev(nt_ts_quantile_q50(pow_3(Open), 5), 5), cross_scale(Open, 30)))` | -2.23 | -1.56 | -2.23 | — | (子树本身) |
| swap | `Open->Close` | -2.27 | -1.58 | -2.27 | — | `ts_decay_linear(day_std(sub(nt_ts_stddev(nt_ts_quantile_q50(pow_3(Close), 5), 5), cross_scale(Close, 30))), 5)` |
| window | `ts_decay_linear@5->2` | -2.23 | -1.57 | -2.23 | — | `ts_decay_linear(day_std(sub(nt_ts_stddev(nt_ts_quantile_q50(pow_3(Open), 5), 5), cross_scale(Open, 30))), 2)` |
| window | `ts_decay_linear@5->10` | -2.33 | -1.60 | -2.33 | — | `ts_decay_linear(day_std(sub(nt_ts_stddev(nt_ts_quantile_q50(pow_3(Open), 5), 5), cross_scale(Open, 30))), 10)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_regres(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), LogFloatCap)` — enrichment,均值差 +1.05,p 0.002
2. `cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241)` — enrichment,均值差 +0.85,p 0.000
3. `cross_mean(day_sum(Amt), 60)` — enrichment,均值差 +0.82,p 0.001
4. `day_sum(Amt)` — enrichment,均值差 +0.82,p 0.001
5. `cross_semistd_pos(day_close(Close), 120)` — enrichment,均值差 +0.77,p 0.024
6. `add(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120))` — enrichment,均值差 +0.77,p 0.024
7. `sub(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120))` — enrichment,均值差 +0.77,p 0.024
8. `cross_semistd_neg(day_close(Close), 120)` — enrichment,均值差 +0.77,p 0.024
9. `day_gini(Low)` — enrichment,均值差 +0.77,p 0.009
10. `div(sub(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120)), add(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120)))` — enrichment,均值差 +0.74,p 0.051
11. `day_distinct_ratio(Open)` — enrichment,均值差 +0.68,p 0.001
12. `sub(LogTotalCap, LogFloatShares)` — enrichment,均值差 +0.67,p 0.046
13. `div(LogFloatCap, day_distinct_ratio(Open))` — enrichment,均值差 +0.62,p 0.032
14. `cross_delta(sub(log(day_close(Close)), LogFloatCap), 1)` — enrichment,均值差 +0.62,p 0.000
15. `sub(log(day_close(Close)), LogFloatCap)` — enrichment,均值差 +0.58,p 0.000
16. `day_close(Close)` — enrichment,均值差 +0.56,p 0.000
17. `log(day_close(Close))` — enrichment,均值差 +0.50,p 0.000

## 本组之前各轮的任务

- `prods2014Pr1a_Ea`:核心 `day_quantile_q25(High)`;评分 105,过线 0,入 heads 0;采样计数 {'c05_no_core': 1641, 'c05_skeleton': 855}
  - score -1.36(train -1.08 valid -1.36):`cs_bucket_rank(sub(LogFloatCap, LogFloatShares), day_quantile_q25(High))`
  - score -1.44(train -1.44 valid -1.15):`sub(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares)), cs_bucket_rank(sub(LogFloatCap, LogFloatShares), day_q_stat_std(High)))`
  - score -1.50(train -1.45 valid -1.50):`sub(log(sub(log(day_quantile_q25(High)), sub(LogFloatCap, LogFloatShares))), sub(LogFloatCap, LogFloatShares))`
  - score -1.65(train -1.65 valid -1.45):`sub(sub(log(log(day_quantile_q25(High))), sub(LogFloatCap, LogFloatShares)), sub(LogTotalCap, LogFloatCap))`
  - score -1.65(train -1.51 valid -1.65):`sub(sub(log(day_quantile_q25(High)), sub(LogFloatCap, sub(LogFloatCap, LogFloatShares))), sub(LogTotalCap, LogFloatCap))`
- `prods2014Pr1b_Nb`:核心 `—`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score -0.86(train -0.17 valid -0.86):`cs_last_low40(div(LogFloatCap, day_distinct_ratio(Open)), day_var(Low))`
  - score -0.91(train -0.15 valid -0.91):`cs_last_low40(div(LogFloatCap, day_distinct_ratio(Open)), day_var(Open))`
  - score -1.19(train -1.13 valid -1.19):`div(sub(LogTotalCap, div(LogFloatCap, day_distinct_ratio(Open))), day_distinct_ratio(Open))`
  - score -1.19(train -1.11 valid -1.19):`div(LogFloatCap, day_distinct_ratio(Open))`
  - score -1.20(train -1.20 valid -1.17):`mul(mul(abs_(day_quantile_q25(Ret)), day_distinct_ratio(Open)), day_distinct_ratio(Open))`
- `prods2014Pr2a_Na`:核心 `—`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.59(train -0.59 valid +0.25):`cross_ema(cross_delta(sub(log(sub(LogTotalCap, LogFloatCap)), LogFloatCap), 1), 120)`
  - score -0.66(train -0.66 valid -0.50):`cs_regres(cross_sum(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), 241), LogFloatCap)`
  - score -0.77(train -0.77 valid -0.12):`cs_bucket_zscore(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), cross_mean(day_sum(Amt), 60))`
  - score -0.86(train -0.86 valid -0.86):`cs_bucket_zscore(cross_sum(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), 241), cross_mean(day_sum(Amt), 60))`
  - score -0.98(train -0.98 valid +0.18):`cs_regres(cross_sum(cross_delta(cs_regres(cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241), LogFloatCap), 1), 241), LogFloatCap)`
- `prods2014Pr2b_Nb`:核心 `—`;评分 53,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1}
  - score -0.01(train -0.01 valid +0.12):`cross_semistd_pos(day_gini(Low), 241)`
  - score -0.35(train +0.03 valid -0.35):`day_close(cross_regbeta(pow_1_5(High), sub(-5, Ret), 60))`
  - score -0.48(train -0.48 valid +0.25):`cross_semistd_pos(day_gini(Ret), 241)`
  - score -0.82(train +0.04 valid -0.82):`add(cs_rank(div(sub(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120)), add(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120)))), cs_rank(cross_mean(sub(day_es_ratio_hi(Ret), day_es_ratio_lo(Ret)), 120)))`
  - score -0.93(train -0.93 valid -0.09):`cross_semistd_pos(cross_semistd_pos(day_gini(Low), 30), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.14(window ts_med@40->80):`ts_med(ts_reg_tvalue(day_std(pow_3(Open)), day_quantile_q25(Ret), 50), 80)`
