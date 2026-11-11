# 定位:种子 2046,P 组,第 3 轮(只含 train / valid)

快照:prods2046M1_I0_open_search, prods2046M2_I0_open_search, prods2046M3_I0_open_search, prods2046Pr1a_Ea, prods2046Pr1b_Nb, prods2046Pr2a_Ea, prods2046Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(18 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.28 | +1.28 | +1.28 | -1 | 0 | prods2046Pr2b_Nb | `cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_mean(replace_small_with_nan(Volume)), 240)` |
| +1.17 | +1.17 | +1.17 | +1 | 0 | prods2046Pr2a_Ea | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_mean(replace_small_with_nan(Amt)), 240)` |
| +1.06 | +1.25 | +1.06 | -1 | 0 | prods2046Pr2b_Nb | `cross_corr(cross_delay(log(cross_delay(log(day_gini(Amt)), 1)), 1), day_var(replace_small_with_nan(Amt)), 240)` |
| +0.88 | +1.36 | +0.88 | +1 | 0 | prods2046Pr1b_Nb | `cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(replace_small_with_nan(Amt)), 120)` |
| +0.64 | +0.64 | +0.72 | +1 | 5 | prods2046Pr2a_Ea | `cross_corr(cross_delay(log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)), 1), day_var(Ret), 240)` |
| +0.61 | +0.61 | +0.61 | +1 | 5 | prods2046Pr2a_Ea | `cs_regres(cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(Close)), 240), abs_(cross_mean(day_mean(replace_small_with_nan(Close)), 10)))` |
| +0.60 | +0.60 | +0.96 | +1 | 5 | prods2046Pr2b_Nb | `cross_corr(cross_delay(log(day_gini(replace_small_with_nan(Amt))), 1), day_var(Ret), 240)` |
| +0.58 | +0.58 | +0.73 | +1 | 5 | prods2046Pr2b_Nb | `cross_corr(cross_delay(day_gini(replace_small_with_nan(Amt)), 1), day_var(replace_small_with_nan(High)), 240)` |
| +0.58 | +0.58 | +0.75 | +1 | 5 | prods2046Pr2b_Nb | `cross_corr(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), day_var(replace_small_with_nan(Amt)), 240)` |
| +0.18 | +1.14 | +0.18 | +1 | 0 | prods2046M1_I0_open_search | `cs_regres(log(ts_sum(day_var(Amt), 100)), log(ts_sum(day_mean(Amt), 100)))` |
| -0.67 | -0.67 | -0.63 | +1 | 20 | prods2046M1_I0_open_search | `ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 2)` |
| -0.77 | -0.74 | -0.77 | +1 | 5 | prods2046M1_I0_open_search | `ts_max(cross_corr(ts_max(day_last(Amt), 20), log(day_var(Low)), 241), 20)` |
| -1.15 | -1.15 | -0.76 | +1 | 5 | prods2046M2_I0_open_search | `div(add(div(day_var(Ret), day_max(High)), cross_max(day_cov(Amt, Close), 60)), log(ts_sum(day_argmin(Amt), 50)))` |
| -1.22 | -0.72 | -1.22 | +1 | 5 | prods2046M3_I0_open_search | `add(div(day_var(Ret), day_max(High)), cross_max(ts_quantile_q75(pow_1_5(cross_cov(day_max(High), day_var(Ret), 15)), 5), 15))` |
| -1.26 | -0.48 | -1.26 | +1 | 5 | prods2046M2_I0_open_search | `div(add(div(day_var(Amt), day_max(High)), cross_max(day_cov(Close, Close), 15)), log(ts_sum(day_argmin(Amt), 50)))` |
| -1.26 | -1.13 | -1.26 | +1 | 5 | prods2046M3_I0_open_search | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(div(day_open(Amt), day_max(High)), cross_max(ts_quantile_q75(pow_1_5(cross_cov(day_max(High), day_var(Amt), 15)), 5), 15))), 20), 5)` |
| -1.45 | -1.45 | -1.01 | -1 | 0 | prods2046M3_I0_open_search | `ts_quantile_q75(ts_quantile_q75(pow_1_5(add(div(day_close(Ret), day_max(High)), cross_max(ts_quantile_q75(pow_1_5(cross_cov(day_max(High), day_var(Ret), 15)), 5), 15))), 20), 5)` |
| -1.57 | -1.57 | -1.17 | -1 | 20 | prods2046M2_I0_open_search | `div(add(div(day_var(Ret), day_max(High)), cross_max(day_cov(Close, Close), 15)), log(day_cov(Close, Close)))` |

## 共性:309 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.75 | 0.002 | 6 | +0.40 / -1.36 | `day_gini(Amt)` |
| +1.71 | 0.000 | 16 | +0.30 / -1.41 | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(Amt)), 240)` |
| +1.71 | 0.015 | 4 | +0.36 / -1.35 | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(replace_small_with_nan(Amt))), 240)` |
| +1.59 | 0.008 | 5 | +0.24 / -1.35 | `cross_delay(log(day_gini(Amt)), 1)` |
| +1.59 | 0.008 | 5 | +0.24 / -1.35 | `log(day_gini(Amt))` |
| +1.45 | 0.018 | 5 | +0.11 / -1.35 | `day_mean(Amt)` |
| +1.38 | 0.008 | 7 | +0.02 / -1.35 | `log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1))` |
| +1.37 | 0.056 | 4 | +0.03 / -1.34 | `cross_delay(day_gini(replace_small_with_nan(Amt)), 1)` |
| +1.36 | 0.000 | 149 | -0.62 / -1.98 | `day_var(replace_small_with_nan(Amt))` |
| +1.29 | 0.003 | 10 | -0.07 / -1.37 | `day_var(replace_small_with_nan(replace_small_with_nan(Amt)))` |
| +1.21 | 0.032 | 5 | -0.13 / -1.34 | `cross_delay(log(day_gini(replace_small_with_nan(Amt))), 1)` |
| +1.21 | 0.054 | 4 | -0.13 / -1.34 | `pow_2(day_mean(Amt))` |
| +1.03 | 0.046 | 4 | -0.30 / -1.34 | `log(day_var(replace_small_with_nan(Amt)))` |
| +0.96 | 0.000 | 74 | -0.60 / -1.55 | `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)` |
| +0.91 | 0.022 | 9 | -0.44 / -1.35 | `cross_autocorr_s1(day_durbin_watson(High), 3)` |
| +0.91 | 0.022 | 9 | -0.44 / -1.35 | `pow_05(cross_autocorr_s1(day_durbin_watson(High), 3))` |
| +0.91 | 0.000 | 99 | -0.70 / -1.62 | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` |
| +0.90 | 0.053 | 4 | -0.44 / -1.34 | `cross_zscore(log(day_var(Ret)), 60)` |
| +0.90 | 0.053 | 4 | -0.44 / -1.34 | `cross_delay(cross_zscore(log(day_var(Ret)), 60), 1)` |
| +0.88 | 0.049 | 7 | -0.46 / -1.34 | `day_mean(replace_small_with_nan(replace_small_with_nan(Amt)))` |

## 拆解(45 次评估)

### head score +1.28:`cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_mean(replace_small_with_nan(Volume)), 240)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1)` | -4.18 | -3.42 | -4.18 | — | (子树本身) |
| sufficiency | `sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))))` | -3.94 | -3.32 | -3.94 | — | (子树本身) |
| sufficiency | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` | -3.71 | -3.36 | -3.71 | — | (子树本身) |
| sufficiency | `ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40)` | -2.05 | -0.84 | -2.05 | — | (子树本身) |
| knockout | `cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1)` | +0.77 | +0.93 | +0.77 | +0.51 | `cross_corr(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), day_mean(replace_small_with_nan(Volume)), 240)` |
| knockout | `sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))))` | -1.53 | -1.35 | -1.53 | +2.81 | `cross_corr(cross_delay(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), 1), day_mean(replace_small_with_nan(Volume)), 240)` |
| knockout | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` | +1.30 | +1.30 | +1.33 | -0.02 | `cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_mean(replace_small_with_nan(Volume)), 240)` |
| knockout | `ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40)` | +1.12 | +1.25 | +1.12 | +0.15 | `cross_corr(cross_delay(sub(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_mean(replace_small_with_nan(Volume)), 240)` |
| swap | `High->Low` | +1.16 | +1.43 | +1.16 | — | `cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(Low), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_mean(replace_small_with_nan(Volume)), 240)` |
| swap | `Amt->Volume` | +1.21 | +1.21 | +1.28 | — | `cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Volume)), pow_2(day_mean(replace_small_with_nan(Volume)))))), 1), day_mean(replace_small_with_nan(Volume)), 240)` |
| window | `cross_corr@240->120` | +0.80 | +1.13 | +0.80 | — | `cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_mean(replace_small_with_nan(Volume)), 120)` |
| window | `cross_corr@240->480` | +0.71 | +0.71 | +1.02 | — | `cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_mean(replace_small_with_nan(Volume)), 480)` |

### head score +1.17:`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_mean(replace_small_with_nan(Amt)), 240)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)` | -3.83 | -3.59 | -3.83 | — | (子树本身) |
| sufficiency | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` | -3.71 | -3.36 | -3.71 | — | (子树本身) |
| sufficiency | `div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))` | -3.71 | -3.36 | -3.71 | — | (子树本身) |
| sufficiency | `pow_2(day_mean(replace_small_with_nan(Amt)))` | -3.19 | -2.61 | -3.19 | — | (子树本身) |
| knockout | `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)` | +0.69 | +0.69 | +0.74 | +0.47 | `cross_corr(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), day_mean(replace_small_with_nan(Amt)), 240)` |
| knockout | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` | +1.11 | +1.35 | +1.11 | +0.06 | `cross_corr(cross_delay(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))), 1), day_mean(replace_small_with_nan(Amt)), 240)` |
| knockout | `div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))` | -0.43 | -0.43 | -0.35 | +1.60 | `cross_corr(cross_delay(log(day_var(replace_small_with_nan(Amt))), 1), day_mean(replace_small_with_nan(Amt)), 240)` |
| knockout | `pow_2(day_mean(replace_small_with_nan(Amt)))` | -0.10 | -0.10 | +0.31 | +1.26 | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), day_mean(replace_small_with_nan(Amt)))), 1), day_mean(replace_small_with_nan(Amt)), 240)` |
| swap | `Amt->Volume` | +1.16 | +1.17 | +1.16 | — | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Volume)), pow_2(day_mean(replace_small_with_nan(Volume))))), 1), day_mean(replace_small_with_nan(Volume)), 240)` |
| window | `cross_corr@240->120` | +0.66 | +1.22 | +0.66 | — | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_mean(replace_small_with_nan(Amt)), 120)` |
| window | `cross_corr@240->480` | +0.85 | +0.96 | +0.85 | — | `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_mean(replace_small_with_nan(Amt)), 480)` |

### head score +1.06:`cross_corr(cross_delay(log(cross_delay(log(day_gini(Amt)), 1)), 1), day_var(replace_small_with_nan(Amt)), 240)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(log(cross_delay(log(day_gini(Amt)), 1)), 1)` | -3.95 | -3.82 | -3.95 | — | (子树本身) |
| sufficiency | `log(cross_delay(log(day_gini(Amt)), 1))` | -3.89 | -3.80 | -3.89 | — | (子树本身) |
| sufficiency | `cross_delay(log(day_gini(Amt)), 1)` | -3.89 | -3.80 | -3.89 | — | (子树本身) |
| sufficiency | `log(day_gini(Amt))` | -3.86 | -3.68 | -3.86 | — | (子树本身) |
| knockout | `cross_delay(log(cross_delay(log(day_gini(Amt)), 1)), 1)` | +1.42 | +1.42 | +1.50 | -0.35 | `cross_corr(log(cross_delay(log(day_gini(Amt)), 1)), day_var(replace_small_with_nan(Amt)), 240)` |
| knockout | `log(cross_delay(log(day_gini(Amt)), 1))` | +1.12 | +1.12 | +1.33 | -0.05 | `cross_corr(cross_delay(cross_delay(log(day_gini(Amt)), 1), 1), day_var(replace_small_with_nan(Amt)), 240)` |
| knockout | `cross_delay(log(day_gini(Amt)), 1)` | +1.42 | +1.42 | +1.50 | -0.35 | `cross_corr(cross_delay(log(log(day_gini(Amt))), 1), day_var(replace_small_with_nan(Amt)), 240)` |
| knockout | `log(day_gini(Amt))` | +1.12 | +1.12 | +1.33 | -0.05 | `cross_corr(cross_delay(log(cross_delay(day_gini(Amt), 1)), 1), day_var(replace_small_with_nan(Amt)), 240)` |
| swap | `Amt->Volume` | +1.14 | +1.14 | +1.25 | — | `cross_corr(cross_delay(log(cross_delay(log(day_gini(Volume)), 1)), 1), day_var(replace_small_with_nan(Volume)), 240)` |
| window | `cross_corr@240->120` | +0.03 | +1.30 | +0.03 | — | `cross_corr(cross_delay(log(cross_delay(log(day_gini(Amt)), 1)), 1), day_var(replace_small_with_nan(Amt)), 120)` |
| window | `cross_corr@240->480` | +0.98 | +1.20 | +0.98 | — | `cross_corr(cross_delay(log(cross_delay(log(day_gini(Amt)), 1)), 1), day_var(replace_small_with_nan(Amt)), 480)` |

### head score +0.64:`cross_corr(cross_delay(log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)), 1), day_var(Ret), 240)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)), 1)` | -4.26 | -4.26 | -3.79 | — | (子树本身) |
| sufficiency | `log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1))` | -4.13 | -4.13 | -3.63 | — | (子树本身) |
| sufficiency | `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)` | -3.83 | -3.59 | -3.83 | — | (子树本身) |
| sufficiency | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` | -3.71 | -3.36 | -3.71 | — | (子树本身) |
| knockout | `cross_delay(log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)), 1)` | +0.49 | +0.49 | +0.63 | +0.15 | `cross_corr(log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)), day_var(Ret), 240)` |
| knockout | `log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1))` | +0.69 | +0.81 | +0.69 | -0.05 | `cross_corr(cross_delay(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), 1), day_var(Ret), 240)` |
| knockout | `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)` | +0.49 | +0.49 | +0.63 | +0.15 | `cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(Ret), 240)` |
| knockout | `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` | +0.69 | +0.81 | +0.69 | -0.05 | `cross_corr(cross_delay(log(cross_delay(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))), 1)), 1), day_var(Ret), 240)` |
| swap | `Amt->Volume` | +0.55 | +0.55 | +0.62 | — | `cross_corr(cross_delay(log(cross_delay(log(div(day_var(replace_small_with_nan(Volume)), pow_2(day_mean(replace_small_with_nan(Volume))))), 1)), 1), day_var(Ret), 240)` |
| window | `cross_corr@240->120` | +0.10 | +0.52 | +0.10 | — | `cross_corr(cross_delay(log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)), 1), day_var(Ret), 120)` |
| window | `cross_corr@240->480` | +0.33 | +0.33 | +0.73 | — | `cross_corr(cross_delay(log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)), 1), day_var(Ret), 480)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_gini(Amt)` — enrichment,均值差 +1.75,p 0.002
2. `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(Amt)), 240)` — enrichment,均值差 +1.71,p 0.000
3. `cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(replace_small_with_nan(Amt))), 240)` — enrichment,均值差 +1.71,p 0.015
4. `cross_delay(log(day_gini(Amt)), 1)` — enrichment,均值差 +1.59,p 0.008
5. `log(day_gini(Amt))` — enrichment,均值差 +1.59,p 0.008
6. `day_mean(Amt)` — enrichment,均值差 +1.45,p 0.018
7. `log(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1))` — enrichment,均值差 +1.38,p 0.008
8. `cross_delay(day_gini(replace_small_with_nan(Amt)), 1)` — enrichment,均值差 +1.37,p 0.056
9. `day_var(replace_small_with_nan(Amt))` — enrichment,均值差 +1.36,p 0.000
10. `day_var(replace_small_with_nan(replace_small_with_nan(Amt)))` — enrichment,均值差 +1.29,p 0.003
11. `cross_delay(log(day_gini(replace_small_with_nan(Amt))), 1)` — enrichment,均值差 +1.21,p 0.032
12. `pow_2(day_mean(Amt))` — enrichment,均值差 +1.21,p 0.054
13. `log(day_var(replace_small_with_nan(Amt)))` — enrichment,均值差 +1.03,p 0.046
14. `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)` — enrichment,均值差 +0.96,p 0.000
15. `cross_autocorr_s1(day_durbin_watson(High), 3)` — enrichment,均值差 +0.91,p 0.022
16. `pow_05(cross_autocorr_s1(day_durbin_watson(High), 3))` — enrichment,均值差 +0.91,p 0.022
17. `log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))` — enrichment,均值差 +0.91,p 0.000
18. `cross_zscore(log(day_var(Ret)), 60)` — enrichment,均值差 +0.90,p 0.053
19. `cross_delay(cross_zscore(log(day_var(Ret)), 60), 1)` — enrichment,均值差 +0.90,p 0.053
20. `day_mean(replace_small_with_nan(replace_small_with_nan(Amt)))` — enrichment,均值差 +0.88,p 0.049
21. `log(log(day_var(Ret)))` — enrichment,均值差 +0.87,p 0.056
22. `div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))` — enrichment,均值差 +0.87,p 0.000
23. `pow_2(day_mean(replace_small_with_nan(Amt)))` — enrichment,均值差 +0.86,p 0.000
24. `ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40)` — enrichment,均值差 +0.85,p 0.039
25. `day_mean(replace_small_with_nan(Amt))` — enrichment,均值差 +0.85,p 0.000
26. `log(day_gini(replace_small_with_nan(Amt)))` — enrichment,均值差 +0.79,p 0.073
27. `day_gini(replace_small_with_nan(Amt))` — enrichment,均值差 +0.77,p 0.043
28. `day_var(replace_small_with_nan(Volume))` — enrichment,均值差 +0.60,p 0.054
29. `log(day_var(Ret))` — enrichment,均值差 +0.50,p 0.013

## 本组之前各轮的任务

- `prods2046Pr1a_Ea`:核心 `day_var(Low)`;评分 97,过线 0,入 heads 0;采样计数 {'c05_skeleton': 506, 'c05_no_core': 1097}
  - score -0.41(train -0.19 valid -0.41):`cross_reg_tvalue(cross_delay(day_var(Low), 1), cs_demean(day_sum(Ret)), 120)`
  - score -0.47(train -0.47 valid -0.46):`cross_corr(cross_delay(cross_zscore(log(day_var(Low)), 60), 1), day_sum(Ret), 120)`
  - score -0.53(train -0.53 valid +0.02):`cross_reg_tvalue(cross_delay(cross_zscore(log(day_var(Low)), 60), 1), cs_demean(day_sum(Ret)), 120)`
  - score -0.59(train -0.59 valid -0.59):`cross_reg_tvalue(cross_delay(day_var(Low), 1), day_sum(Ret), 120)`
  - score -0.61(train -0.53 valid -0.61):`cross_corr(cross_delay(day_var(Low), 1), day_sum(Ret), 120)`
- `prods2046Pr1b_Nb`:核心 `—`;评分 99,过线 3,入 heads 1;采样计数 {'c05_skeleton': 3}
  - score +0.88(train +1.36 valid +0.88):`cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_var(replace_small_with_nan(Amt)), 120)`
  - score +0.88(train +1.36 valid +0.88):`cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(replace_small_with_nan(Amt))))))), 1), day_var(replace_small_with_nan(Amt)), 120)`
  - score +0.75(train +1.18 valid +0.75):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(Amt)), 120)`
  - score +0.34(train +0.73 valid +0.34):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(Amt)))), 1), log(day_var(Ret)), 120)`
  - score +0.30(train +0.64 valid +0.30):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), log(day_var(replace_small_with_nan(Amt))), 120)`
- `prods2046Pr2a_Ea`:核心 `cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1)`;评分 88,过线 29,入 heads 3;采样计数 {'c05_periphery_seen': 16, 'c05_skeleton': 503, 'c05_no_core': 1195, 'mutation_refused': 4}
  - score +1.17(train +1.17 valid +1.17):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_mean(replace_small_with_nan(Amt)), 240)`
  - score +1.10(train +1.10 valid +1.22):`cs_regres(cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(replace_small_with_nan(Amt))), 240), sqrt(cross_mean(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), 240)))`
  - score +1.08(train +1.08 valid +1.10):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_std(replace_small_with_nan(Amt)), 240)`
  - score +1.07(train +1.07 valid +1.32):`cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), pow_2(day_mean(replace_small_with_nan(Amt))), 240)`
  - score +1.06(train +1.08 valid +1.06):`cs_regres(cross_corr(cross_delay(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt))))), 1), day_var(replace_small_with_nan(Amt)), 240), abs_(cross_mean(day_mean(Volume), 10)))`
- `prods2046Pr2b_Nb`:核心 `—`;评分 85,过线 17,入 heads 5;采样计数 {'c05_skeleton': 2}
  - score +1.28(train +1.28 valid +1.28):`cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(Amt)))))), 1), day_mean(replace_small_with_nan(Volume)), 240)`
  - score +1.28(train +1.28 valid +1.28):`cross_corr(cross_delay(sub(ts_min(pow_05(cross_autocorr_s1(day_durbin_watson(High), 3)), 40), log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_small_with_nan(replace_small_with_nan(Amt))))))), 1), day_mean(replace_small_with_nan(Volume)), 240)`
  - score +1.25(train +1.25 valid +1.62):`cross_corr(cross_delay(log(day_gini(Amt)), 1), day_var(Amt), 240)`
  - score +1.21(train +1.21 valid +1.59):`cross_corr(cross_delay(log(day_gini(Amt)), 1), day_var(replace_small_with_nan(Amt)), 240)`
  - score +1.18(train +1.18 valid +1.62):`cross_corr(cross_delay(day_gini(Amt), 1), day_var(replace_small_with_nan(Amt)), 240)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.35(knockout cross_delay(log(cross_delay(log(day_gini(Amt)), 1)), 1)):`cross_corr(log(cross_delay(log(day_gini(Amt)), 1)), day_var(replace_small_with_nan(Amt)), 240)`
- 增益 +0.35(knockout cross_delay(log(day_gini(Amt)), 1)):`cross_corr(cross_delay(log(log(day_gini(Amt))), 1), day_var(replace_small_with_nan(Amt)), 240)`
