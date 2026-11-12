# 定位:种子 2067,P 组,第 2 轮(只含 train / valid)

快照:prods2067M1_I0_open_search, prods2067M2_I0_open_search, prods2067Pr1a_Ea, prods2067Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.62 | -1.51 | -1.62 | -1 | 5 | prods2067M2_I0_open_search | `pow_2(cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5), 1)))` |
| -2.66 | -2.34 | -2.66 | +1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 5)), Volume)` |
| -2.70 | -2.34 | -2.70 | +1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 5)), Amt)` |
| -2.89 | -2.63 | -2.89 | -1 | 20 | prods2067M1_I0_open_search | `day_corr(abs_(in_delay(Ret, 1)), log(Amt))` |
| -2.99 | -2.30 | -2.99 | +1 | 20 | prods2067M2_I0_open_search | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(Amt, 5))))))` |
| -3.13 | -2.03 | -3.13 | -1 | 20 | prods2067M2_I0_open_search | `ts_var(day_q_stat_std(abs_(High)), 20)` |

## 共性:122 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.26 | 0.000 | 15 | -1.67 / -2.93 | `day_corr(in_delay(Ret, 5), Volume)` |
| +1.12 | 0.032 | 5 | -1.71 / -2.82 | `sub(day_corr(in_delay(Ret, 5), Volume), day_corr(Ret, in_delay(Volume, 5)))` |
| +1.06 | 0.000 | 18 | -1.87 / -2.93 | `sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap)` |
| +1.05 | 0.032 | 4 | -1.77 / -2.81 | `day_durbin_watson(Volume)` |
| +1.04 | 0.007 | 7 | -1.80 / -2.84 | `sub(day_product(in_delay(Ret, 5)), day_durbin_watson(Amt))` |
| +1.00 | 0.002 | 11 | -1.87 / -2.87 | `day_product(in_delay(Ret, 5))` |
| +0.96 | 0.001 | 14 | -1.93 / -2.89 | `day_durbin_watson(Amt)` |
| +0.86 | 0.043 | 5 | -1.96 / -2.81 | `day_product(Ret)` |
| +0.77 | 0.027 | 12 | -2.08 / -2.85 | `day_corr(Ret, in_delay(Volume, 5))` |
| +0.60 | 0.000 | 31 | -2.33 / -2.93 | `day_corr(abs_(in_delay(Ret, 5)), Amt)` |
| +0.47 | 0.149 | 8 | -2.34 / -2.81 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 20)` |
| +0.43 | 0.273 | 4 | -2.37 / -2.79 | `cross_mean(day_corr(abs_(in_delay(Ret, 5)), Amt), 120)` |
| -1.36 | 0.982 | 4 | -4.10 / -2.73 | `day_corr(abs_(Ret), in_delay(Volume, 5))` |
| -1.36 | 0.982 | 4 | -4.10 / -2.73 | `day_corr(abs_(in_delay(Ret, 5)), Volume)` |

## 拆解(18 次评估)

### head score -1.62:`pow_2(cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5), 1)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5), 1))` | -1.57 | -1.51 | -1.57 | — | (子树本身) |
| sufficiency | `ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5), 1)` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_max(cs_rank(day_hurst(abs_(Low))), 20)` | -0.86 | -0.86 | -0.73 | — | (子树本身) |
| sufficiency | `cs_rank(day_hurst(abs_(Low)))` | -5.18 | -5.18 | -5.08 | — | (子树本身) |
| knockout | `cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5), 1))` | — | — | — | — | `pow_2(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5), 1))` |
| knockout | `div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5)` | -1.57 | -1.51 | -1.57 | -0.05 | `pow_2(cs_rank(ts_argmax(ts_max(cs_rank(day_hurst(abs_(Low))), 20), 1)))` |
| knockout | `ts_max(cs_rank(day_hurst(abs_(Low))), 20)` | -1.57 | -1.50 | -1.57 | -0.04 | `pow_2(cs_rank(ts_argmax(div(cs_rank(day_hurst(abs_(Low))), -0.5), 1)))` |
| knockout | `cs_rank(day_hurst(abs_(Low)))` | -1.57 | -1.51 | -1.57 | -0.05 | `pow_2(cs_rank(ts_argmax(div(ts_max(day_hurst(abs_(Low)), 20), -0.5), 1)))` |
| swap | `Low->High` | -1.57 | -1.51 | -1.57 | — | `pow_2(cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(High))), 20), -0.5), 1)))` |
| window | `ts_argmax@1->2` | -1.61 | -1.56 | -1.61 | — | `pow_2(cs_rank(ts_argmax(div(ts_max(cs_rank(day_hurst(abs_(Low))), 20), -0.5), 2)))` |

### head score -2.99:`cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(Amt, 5))))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(Amt, 5)))))` | -3.00 | -2.30 | -3.00 | — | (子树本身) |
| swap | `Amt->Volume` | -2.73 | -2.02 | -2.73 | — | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(Volume, 5))))))` |
| window | `in_delay@5->2` | -3.02 | -2.39 | -3.02 | — | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(Amt, 2))))))` |
| window | `in_delay@5->10` | -3.00 | -2.32 | -3.00 | — | `cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(Amt, 10))))))` |

### head score -3.13:`ts_var(day_q_stat_std(abs_(High)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(abs_(High))` | -3.84 | -3.84 | -3.37 | — | (子树本身) |
| swap | `High->Low` | -2.56 | -2.24 | -2.56 | — | `ts_var(day_q_stat_std(abs_(Low)), 20)` |
| window | `ts_var@20->10` | -3.27 | -2.49 | -3.27 | — | `ts_var(day_q_stat_std(abs_(High)), 10)` |
| window | `ts_var@20->40` | -2.77 | -1.88 | -2.77 | — | `ts_var(day_q_stat_std(abs_(High)), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_corr(in_delay(Ret, 5), Volume)` — enrichment,均值差 +1.26,p 0.000
2. `sub(day_corr(in_delay(Ret, 5), Volume), day_corr(Ret, in_delay(Volume, 5)))` — enrichment,均值差 +1.12,p 0.032
3. `sub(day_corr(abs_(in_delay(Ret, 5)), Amt), LogTotalCap)` — enrichment,均值差 +1.06,p 0.000
4. `day_durbin_watson(Volume)` — enrichment,均值差 +1.05,p 0.032
5. `sub(day_product(in_delay(Ret, 5)), day_durbin_watson(Amt))` — enrichment,均值差 +1.04,p 0.007
6. `day_product(in_delay(Ret, 5))` — enrichment,均值差 +1.00,p 0.002
7. `day_durbin_watson(Amt)` — enrichment,均值差 +0.96,p 0.001
8. `day_product(Ret)` — enrichment,均值差 +0.86,p 0.043
9. `day_corr(Ret, in_delay(Volume, 5))` — enrichment,均值差 +0.77,p 0.027
10. `day_corr(abs_(in_delay(Ret, 5)), Amt)` — enrichment,均值差 +0.60,p 0.000

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.57(swap High->Low):`ts_var(day_q_stat_std(abs_(Low)), 20)`
- 增益 +0.37(window ts_var@20->40):`ts_var(day_q_stat_std(abs_(High)), 40)`
- 增益 +0.27(swap Amt->Volume):`cs_scale(day_autocorr_n1(pow_2(in_rank(nt_cs_rank(in_delay(Volume, 5))))))`
