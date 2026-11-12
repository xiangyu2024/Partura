# 定位:种子 2067,P 组,第 3 轮(只含 train / valid)

快照:prods2067M1_I0_open_search, prods2067M2_I0_open_search, prods2067M3_I0_open_search, prods2067Pr1a_Ea, prods2067Pr1b_Nb, prods2067Pr2a_Ea, prods2067Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.62 | -1.51 | -1.62 | -1 | 5 | prods2067M2_I0_open_search | `pow_2(cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5), 1)))` |
| -1.86 | -1.85 | -1.86 | -1 | 20 | prods2067M2_I0_open_search | `ts_var(day_q_stat_std(abs_(Low)), 60)` |
| -2.66 | -2.34 | -2.66 | +1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 5)), Volume)` |
| -2.70 | -2.34 | -2.70 | +1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 5)), Amt)` |
| -2.81 | -2.81 | -1.76 | +1 | 20 | prods2067M3_I0_open_search | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 1)), in_slice(in_zscore_rolling(Amt, 21), 11, 230))` |
| -2.82 | -2.82 | -1.70 | +1 | 20 | prods2067M3_I0_open_search | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 1)), in_slice(in_zscore_rolling(Volume, 21), 11, 230))` |
| -2.89 | -2.63 | -2.89 | -1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` |
| -2.96 | -2.69 | -2.96 | +1 | 20 | prods2067M3_I0_open_search | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 5)), in_slice(Amt, 11, 230))` |
| -2.99 | -2.30 | -2.99 | +1 | 20 | prods2067M2_I0_open_search | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(Amt, 5))))))` |

## 共性:234 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.20 | 0.000 | 5 | -0.80 / -3.00 | `sub(day_durbin_watson(Amt), day_durbin_watson(Volume))` |
| +1.37 | 0.000 | 15 | -1.67 / -3.04 | `day_corr(in_delay(Ret, 5), Volume)` |
| +1.29 | 0.006 | 5 | -1.69 / -2.98 | `cross_age(day_durbin_watson(Amt))` |
| +1.27 | 0.016 | 5 | -1.71 / -2.98 | `sub(day_corr(in_delay(Ret, 5), Volume), day_corr(Ret, in_delay(Volume, 5)))` |
| +1.19 | 0.003 | 7 | -1.80 / -2.99 | `sub(day_product(in_delay(Ret, 5)), day_durbin_watson(Amt))` |
| +1.17 | 0.000 | 18 | -1.87 / -3.04 | `sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap)` |
| +1.17 | 0.000 | 14 | -1.86 / -3.02 | `day_durbin_watson(Volume)` |
| +1.14 | 0.000 | 11 | -1.87 / -3.01 | `day_product(in_delay(Ret, 5))` |
| +1.02 | 0.019 | 5 | -1.96 / -2.97 | `day_product(Ret)` |
| +0.92 | 0.006 | 12 | -2.08 / -3.00 | `day_corr(Ret, in_delay(Volume, 5))` |
| +0.82 | 0.079 | 4 | -2.15 / -2.97 | `day_corr(abs_(Ret), in_zscore_rolling(abs_(Ret), 5))` |
| +0.72 | 0.000 | 31 | -2.33 / -3.05 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` |
| +0.64 | 0.023 | 15 | -2.35 / -2.99 | `day_corr(Volume, in_delay(Volume, 5))` |
| +0.64 | 0.130 | 6 | -2.33 / -2.97 | `day_durbin_watson(abs_(Ret))` |
| +0.63 | 0.054 | 8 | -2.34 / -2.97 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 20)` |
| +0.62 | 0.000 | 44 | -2.45 / -3.07 | `day_durbin_watson(Amt)` |
| +0.60 | 0.148 | 4 | -2.37 / -2.96 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 120)` |
| +0.31 | 0.311 | 5 | -2.65 / -2.96 | `cross_mean(day_durbin_watson(Amt), 40)` |
| +0.13 | 0.450 | 6 | -2.82 / -2.96 | `day_corr(abs_(Ret), in_delay(abs_(Ret), 5))` |
| +0.12 | 0.469 | 4 | -2.84 / -2.95 | `sub(day_durbin_watson(Amt), cross_mean(day_durbin_watson(Amt), 40))` |

## 拆解(11 次评估)

### head score -1.86:`ts_var(day_q_stat_std(abs_(Low)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(abs_(Low))` | -3.93 | -3.93 | -3.37 | — | (子树本身) |
| swap | `Low->High` | -2.53 | -1.72 | -2.53 | — | `ts_var(day_q_stat_std(abs_(High)), 60)` |
| window | `ts_var@60->30` | -2.42 | -2.29 | -2.42 | — | `ts_var(day_q_stat_std(abs_(Low)), 30)` |
| window | `ts_var@60->120` | -2.15 | -2.15 | -2.13 | — | `ts_var(day_q_stat_std(abs_(Low)), 120)` |

### head score -2.81:`day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 1)), in_slice(in_zscore_rolling(Amt, 21), 11, 230))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -2.82 | -2.82 | -1.69 | — | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 1)), in_slice(in_zscore_rolling(Volume, 21), 11, 230))` |
| window | `in_delay@1->2` | -4.10 | -4.10 | -2.82 | — | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 2)), in_slice(in_zscore_rolling(Amt, 21), 11, 230))` |

### head score -2.82:`day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 1)), in_slice(in_zscore_rolling(Volume, 21), 11, 230))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -2.81 | -2.81 | -1.76 | — | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 1)), in_slice(in_zscore_rolling(Amt, 21), 11, 230))` |
| window | `in_delay@1->2` | -4.12 | -4.12 | -2.76 | — | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 2)), in_slice(in_zscore_rolling(Volume, 21), 11, 230))` |

### head score -2.96:`day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 5)), in_slice(Amt, 11, 230))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -3.12 | -2.75 | -3.12 | — | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 5)), in_slice(Volume, 11, 230))` |
| window | `in_delay@5->2` | -3.44 | -3.39 | -3.44 | — | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 2)), in_slice(Amt, 11, 230))` |
| window | `in_delay@5->10` | -2.69 | -2.69 | -2.50 | — | `day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 10)), in_slice(Amt, 11, 230))` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_durbin_watson(Amt), day_durbin_watson(Volume))` — enrichment,均值差 +2.20,p 0.000
2. `day_corr(in_delay(Ret, 5), Volume)` — enrichment,均值差 +1.37,p 0.000
3. `cross_age(day_durbin_watson(Amt))` — enrichment,均值差 +1.29,p 0.006
4. `sub(day_corr(in_delay(Ret, 5), Volume), day_corr(Ret, in_delay(Volume, 5)))` — enrichment,均值差 +1.27,p 0.016
5. `sub(day_product(in_delay(Ret, 5)), day_durbin_watson(Amt))` — enrichment,均值差 +1.19,p 0.003
6. `sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap)` — enrichment,均值差 +1.17,p 0.000
7. `day_durbin_watson(Volume)` — enrichment,均值差 +1.17,p 0.000
8. `day_product(in_delay(Ret, 5))` — enrichment,均值差 +1.14,p 0.000
9. `day_product(Ret)` — enrichment,均值差 +1.02,p 0.019
10. `day_corr(Ret, in_delay(Volume, 5))` — enrichment,均值差 +0.92,p 0.006
11. `day_corr(abs_(Ret), in_zscore_rolling(abs_(Ret), 5))` — enrichment,均值差 +0.82,p 0.079
12. `day_corr(abs_(in_delay(Ret, 5)), Amt)` — enrichment,均值差 +0.72,p 0.000
13. `day_corr(Volume, in_delay(Volume, 5))` — enrichment,均值差 +0.64,p 0.023
14. `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 20)` — enrichment,均值差 +0.63,p 0.054
15. `day_durbin_watson(Amt)` — enrichment,均值差 +0.62,p 0.000

## 本组之前各轮的任务

- `prods2067Pr1a_Ea`:核心 `day_corr(abs_(in_delay(Ret, 5)), Amt)`;评分 110,过线 0,入 heads 0;采样计数 {'c05_no_core': 2775, 'c05_skeleton': 1439, 'mutation_refused': 2}
  - score -1.42(train -1.42 valid -1.09):`cross_argmax(sub(sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap), sub(cross_argmax(div(sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap), sub(day_product(in_delay(Ret, 5)), day_durbin_watson(Amt))), 241), day_durbin_watson(Volume))), 241)`
  - score -1.52(train -1.38 valid -1.52):`cross_argmax(sub(sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap), sub(day_product(Ret), day_durbin_watson(Amt))), 241)`
  - score -1.52(train -1.38 valid -1.52):`cross_argmax(sub(sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap), sub(day_product(in_delay(Ret, 5)), day_durbin_watson(Amt))), 241)`
  - score -1.59(train -1.58 valid -1.59):`cross_argmax(sub(sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap), sub(cs_last_high10(day_mean(Open), day_signed_ratio(Amt, Vwap)), day_durbin_watson(Amt))), 241)`
  - score -1.61(train -1.42 valid -1.61):`cross_argmax(sub(sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap), sub(day_product(in_delay(Ret, 5)), day_durbin_watson(Volume))), 241)`
- `prods2067Pr1b_Nb`:核心 `—`;评分 78,过线 0,入 heads 0;采样计数 {'c05_skeleton': 8}
  - score -0.59(train -0.22 valid -0.59):`cross_mean(sub(day_corr(in_delay(Ret, 5), Volume), day_corr(Ret, Ret)), 30)`
  - score -0.69(train -0.69 valid -0.51):`cross_mean(sub(day_corr(in_delay(Ret, 5), Volume), day_corr(in_delay(Volume, 5), in_delay(Volume, 5))), 15)`
  - score -0.69(train -0.69 valid -0.51):`cross_mean(day_corr(in_delay(Ret, 5), Volume), 15)`
  - score -0.71(train -0.45 valid -0.71):`cross_mean(sub(day_corr(in_delay(Ret, 5), Volume), day_corr(Ret, in_delay(Volume, 5))), 15)`
  - score -0.84(train -0.84 valid -0.30):`cross_mean(sub(day_corr(in_delay(Ret, 5), Volume), day_corr(Ret, in_delay(in_delay(Ret, 5), 5))), 15)`
- `prods2067Pr2a_Ea`:核心 `day_durbin_watson(Amt)`;评分 86,过线 0,入 heads 0;采样计数 {'c05_no_core': 1589, 'c05_skeleton': 742}
  - score -0.29(train -0.29 valid +0.35):`cross_mean(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 30)`
  - score -0.41(train -0.41 valid -0.15):`cross_mean(cross_mean(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 30), 30)`
  - score -0.78(train -0.78 valid -0.69):`cross_mean(cross_mean(cross_mean(sub(day_durbin_watson(Amt), day_durbin_watson(Volume)), 30), 30), 30)`
  - score -1.04(train -1.04 valid +0.03):`cross_regalpha(day_q_stat_std(Amt), cross_age(sub(day_durbin_watson(Amt), day_durbin_watson(abs_(Ret)))), 241)`
  - score -1.09(train -1.09 valid +0.05):`cross_regalpha(day_q_stat_std(Amt), cross_age(day_durbin_watson(Amt)), 241)`
- `prods2067Pr2b_Nb`:核心 `—`;评分 103,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -1.61(train -1.61 valid -1.52):`sub(sub(day_corr(Volume, in_delay(in_delay(Volume, 5), 5)), day_corr(abs_(Ret), in_zscore_rolling(abs_(Ret), 5))), day_corr(abs_(Ret), in_zscore_rolling(abs_(Ret), 5)))`
  - score -1.62(train -0.99 valid -1.62):`sub(ts_quantile_q50(day_es_ratio_hi(Volume), 40), ts_quantile_q50(day_flat_ratio(Low), 1))`
  - score -1.64(train -1.63 valid -1.64):`sub(sub(day_corr(Volume, in_delay(Volume, 5)), day_corr(abs_(Ret), in_zscore_rolling(abs_(Ret), 5))), day_corr(abs_(Ret), in_zscore_rolling(abs_(Ret), 5)))`
  - score -1.69(train -1.69 valid -1.55):`sub(sub(day_corr(Volume, in_delay(in_delay(abs_(Ret), 5), 5)), day_corr(abs_(Ret), in_zscore_rolling(abs_(Ret), 5))), day_corr(abs_(Ret), in_zscore_rolling(abs_(Ret), 5)))`
  - score -1.73(train -1.23 valid -1.73):`sub(sub(day_corr(Volume, in_delay(Volume, 5)), day_corr(abs_(Volume), in_zscore_rolling(abs_(Ret), 5))), day_corr(abs_(Volume), in_zscore_rolling(abs_(Ret), 5)))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.27(window in_delay@5->10):`day_corr(abs_(in_delay(in_slice(Ret, 11, 230), 10)), in_slice(Amt, 11, 230))`
