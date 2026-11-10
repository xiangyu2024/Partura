# 定位:种子 2045,P 组,第 3 轮(只含 train / valid)

快照:prods2045M1_I0_open_search, prods2045M2_I0_open_search, prods2045M3_I0_open_search, prods2045Pr1a_Ea, prods2045Pr1b_Nb, prods2045Pr2a_I0_open_search, prods2045Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.40 | +0.40 | +0.94 | +1 | 0 | prods2045M1_I0_open_search | `add(ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 40), ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50))` |
| -0.24 | -0.24 | +0.85 | +1 | 0 | prods2045M1_I0_open_search | `ts_sum(cross_stddev(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 241), 5)` |
| -0.34 | -0.34 | -0.34 | +1 | 0 | prods2045M2_I0_open_search | `ts_sum(cross_stddev(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30)))), 60), 5)` |
| -1.11 | -0.69 | -1.11 | +1 | 0 | prods2045M1_I0_open_search | `ts_std(ts_cov(day_mean(Volume), day_close(cross_delta(High, 10)), 50), 40)` |
| -1.25 | -1.25 | -1.12 | +1 | 5 | prods2045M2_I0_open_search | `ts_cov(day_median(pow_2(nt_cs_rank(cross_delta(Open, 241)))), day_close(High), 50)` |
| -1.58 | -1.26 | -1.58 | +1 | 0 | prods2045M2_I0_open_search | `ts_std(ts_cov(day_quantile_q25(Ret), day_median(pow_2(nt_cs_rank(cross_delta(High, 30)))), 50), 40)` |
| -1.95 | -1.81 | -1.95 | +1 | 0 | prods2045M3_I0_open_search | `ts_std(ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40)` |
| -2.25 | -1.75 | -2.25 | -1 | 5 | prods2045M3_I0_open_search | `ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40), 50), 40)` |
| -2.29 | -2.00 | -2.29 | -1 | 5 | prods2045M3_I0_open_search | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40)` |

## 共性:258 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.43 | 0.000 | 5 | +0.21 / -2.22 | `cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241)` |
| +2.26 | 0.000 | 13 | -0.03 / -2.28 | `cross_mean(day_cov(Amt, Amt), 241)` |
| +2.09 | 0.000 | 18 | -0.22 / -2.31 | `day_cov(Amt, Amt)` |
| +1.46 | 0.000 | 49 | -0.98 / -2.45 | `day_cov(Amt, cross_delta(Amt, 30))` |
| +1.46 | 0.000 | 49 | -0.98 / -2.45 | `cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60)` |
| +1.46 | 0.000 | 49 | -0.98 / -2.45 | `ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50)` |
| +0.84 | 0.020 | 4 | -1.34 / -2.18 | `sub(day_flat_ratio(Ret), day_zero_ratio(High))` |
| +0.82 | 0.034 | 4 | -1.36 / -2.18 | `cs_first_high20(mul(day_flat_ratio(Ret), day_zero_ratio(High)), ts_max(LogFloatCap, 1))` |
| +0.82 | 0.000 | 32 | -1.45 / -2.27 | `day_flat_ratio(Ret)` |
| +0.78 | 0.018 | 5 | -1.41 / -2.18 | `mul(day_flat_ratio(Ret), day_flat_ratio(Ret))` |
| +0.77 | 0.032 | 4 | -1.41 / -2.18 | `cs_first_high20(mul(day_flat_ratio(Ret), day_flat_ratio(Ret)), ts_max(LogFloatCap, 1))` |
| +0.77 | 0.022 | 6 | -1.41 / -2.19 | `mul(mul(day_flat_ratio(Ret), day_zero_ratio(High)), day_zero_ratio(High))` |
| +0.76 | 0.000 | 26 | -1.49 / -2.24 | `ts_max(LogFloatCap, 1)` |
| +0.67 | 0.003 | 18 | -1.54 / -2.21 | `mul(day_flat_ratio(Ret), day_zero_ratio(High))` |
| +0.52 | 0.001 | 27 | -1.70 / -2.22 | `day_zero_ratio(High)` |
| +0.34 | 0.238 | 4 | -1.83 / -2.17 | `cross_mean(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), 241)` |
| +0.24 | 0.337 | 7 | -1.94 / -2.17 | `day_close(cross_delta(High, 10))` |
| +0.16 | 0.466 | 4 | -2.01 / -2.17 | `ts_cov(day_quantile_q25(Ret), day_close(cross_delta(High, 10)), 50)` |
| +0.14 | 0.519 | 5 | -2.03 / -2.17 | `day_close(cross_delta(High, 30))` |
| +0.04 | 0.574 | 6 | -2.13 / -2.17 | `day_at_max_ratio(Open)` |

## 拆解(32 次评估)

### head score -1.95:`ts_std(ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50)` | -1.54 | -1.54 | -1.20 | — | (子树本身) |
| sufficiency | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40)` | -2.24 | -2.00 | -2.24 | — | (子树本身) |
| sufficiency | `ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50)` | -1.99 | -1.99 | -1.72 | — | (子树本身) |
| sufficiency | `day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low)` | -2.58 | -2.58 | -2.18 | — | (子树本身) |
| knockout | `ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50)` | -1.92 | -1.38 | -1.92 | -0.04 | `ts_std(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), 40)` |
| knockout | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40)` | -2.04 | -2.04 | -2.04 | +0.08 | `ts_std(ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 50), 40)` |
| knockout | `ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50)` | -1.95 | -1.84 | -1.95 | -0.01 | `ts_std(ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_std(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), 40), 50), 40)` |
| knockout | `ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40)` | -1.99 | -1.91 | -1.99 | +0.03 | `ts_std(ts_cov(ts_cov(day_quantile_q25(Ret), day_close(High), 50), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40)` |
| swap | `High->Low` | -1.95 | -1.82 | -1.95 | — | `ts_std(ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(Low), 50), 40), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(Low, 30))), Low), day_close(Low), 50), 40), 50), 40)` |
| swap | `Low->High` | -2.00 | -1.84 | -2.00 | — | `ts_std(ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), High), day_close(High), 50), 40), 50), 40)` |
| window | `ts_std@40->20` | -2.02 | -1.91 | -2.02 | — | `ts_std(ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 20)` |
| window | `ts_std@40->80` | -1.90 | -1.90 | -1.63 | — | `ts_std(ts_cov(ts_std(ts_cov(day_quantile_q25(Ret), day_close(High), 50), 40), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 80)` |

### head score -2.25:`ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40), 50)` | -1.92 | -1.92 | -0.91 | — | (子树本身) |
| sufficiency | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40)` | -2.34 | -1.98 | -2.34 | — | (子树本身) |
| sufficiency | `ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50)` | -1.56 | -1.56 | -1.13 | — | (子树本身) |
| sufficiency | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40)` | -2.24 | -2.00 | -2.24 | — | (子树本身) |
| knockout | `ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40), 50)` | -2.16 | -1.34 | -2.16 | -0.09 | `ts_std(day_quantile_q25(Ret), 40)` |
| knockout | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40)` | -2.12 | -1.87 | -2.12 | -0.13 | `ts_std(ts_cov(day_quantile_q25(Ret), ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 50), 40)` |
| knockout | `ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50)` | -1.66 | -1.66 | -1.40 | -0.59 | `ts_std(ts_cov(day_quantile_q25(Ret), ts_std(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), 40), 50), 40)` |
| knockout | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40)` | -2.06 | -1.79 | -2.06 | -0.19 | `ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 50), 40), 50), 40)` |
| swap | `High->Low` | -2.25 | -1.77 | -2.25 | — | `ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(Low, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(Low, 30))), Low), day_close(Low), 50), 40), 50), 40), 50), 40)` |
| swap | `Low->High` | -2.23 | -1.79 | -2.23 | — | `ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), High), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), High), day_close(High), 50), 40), 50), 40), 50), 40)` |
| window | `ts_std@40->20` | -2.13 | -1.84 | -2.13 | — | `ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40), 50), 20)` |
| window | `ts_std@40->80` | -2.25 | -1.83 | -2.25 | — | `ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40), 50), 80)` |

### head score -2.29:`ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50)` | -1.99 | -1.99 | -1.72 | — | (子树本身) |
| sufficiency | `day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low)` | -2.58 | -2.58 | -2.18 | — | (子树本身) |
| sufficiency | `day_close(High)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50)` | -2.62 | -2.07 | -2.62 | +0.34 | `ts_std(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), 40)` |
| swap | `High->Low` | -2.30 | -1.99 | -2.30 | — | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(Low, 30))), Low), day_close(Low), 50), 40)` |
| swap | `Low->High` | -2.33 | -1.99 | -2.33 | — | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), High), day_close(High), 50), 40)` |
| window | `ts_std@40->20` | -2.37 | -1.93 | -2.37 | — | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 20)` |
| window | `ts_std@40->80` | -2.20 | -1.98 | -2.20 | — | `ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241)` — enrichment,均值差 +2.43,p 0.000
2. `cross_mean(day_cov(Amt, Amt), 241)` — enrichment,均值差 +2.26,p 0.000
3. `day_cov(Amt, Amt)` — enrichment,均值差 +2.09,p 0.000
4. `day_cov(Amt, cross_delta(Amt, 30))` — enrichment,均值差 +1.46,p 0.000
5. `cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60)` — enrichment,均值差 +1.46,p 0.000
6. `ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50)` — enrichment,均值差 +1.46,p 0.000
7. `sub(day_flat_ratio(Ret), day_zero_ratio(High))` — enrichment,均值差 +0.84,p 0.020
8. `cs_first_high20(mul(day_flat_ratio(Ret), day_zero_ratio(High)), ts_max(LogFloatCap, 1))` — enrichment,均值差 +0.82,p 0.034
9. `day_flat_ratio(Ret)` — enrichment,均值差 +0.82,p 0.000
10. `mul(day_flat_ratio(Ret), day_flat_ratio(Ret))` — enrichment,均值差 +0.78,p 0.018
11. `cs_first_high20(mul(day_flat_ratio(Ret), day_flat_ratio(Ret)), ts_max(LogFloatCap, 1))` — enrichment,均值差 +0.77,p 0.032
12. `mul(mul(day_flat_ratio(Ret), day_zero_ratio(High)), day_zero_ratio(High))` — enrichment,均值差 +0.77,p 0.022
13. `ts_max(LogFloatCap, 1)` — enrichment,均值差 +0.76,p 0.000
14. `mul(day_flat_ratio(Ret), day_zero_ratio(High))` — enrichment,均值差 +0.67,p 0.003
15. `day_zero_ratio(High)` — enrichment,均值差 +0.52,p 0.001

## 本组之前各轮的任务

- `prods2045Pr1a_Ea`:核心 `ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50)`;评分 99,过线 0,入 heads 0;采样计数 {'c05_no_core': 2078, 'c05_skeleton': 1097, 'c05_periphery_seen': 9, 'mutation_refused': 7}
  - score +0.31(train +0.31 valid +0.96):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), add(cross_quantile_q25(day_cov(Amt, cross_delta(Amt, 30)), 241), -2))`
  - score +0.30(train +0.30 valid +0.35):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), add(cross_quantile_q25(day_cov(Amt, Amt), 241), -2))`
  - score +0.25(train +0.27 valid +0.25):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), add(cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241), add(cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241), 1)))`
  - score +0.25(train +0.27 valid +0.25):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), mul(cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241), 1))`
  - score +0.25(train +0.27 valid +0.25):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), add(cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241), 2))`
- `prods2045Pr1b_Nb`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score -1.11(train -1.11 valid -1.07):`mul(cross_reg_fvalue(cross_sum(day_q_stat_std(Close), 3), day_wstd(High, Vwap), 15), 1)`
  - score -1.11(train -1.11 valid -1.07):`cross_reg_fvalue(cross_sum(day_q_stat_std(Close), 3), day_wstd(High, Vwap), 15)`
  - score -1.14(train -1.14 valid -1.07):`mul(cross_reg_fvalue(cross_sum(day_q_stat_std(Close), 3), day_wstd(High, Vwap), 15), -5)`
  - score -1.14(train -1.14 valid -1.07):`mul(cross_reg_fvalue(cross_sum(day_q_stat_std(Close), 3), day_wstd(Open, Vwap), 15), 1)`
  - score -1.56(train -1.56 valid -1.15):`mul(cross_reg_fvalue(cross_sum(day_q_stat_std(Vwap), 3), day_wstd(High, Vwap), 15), -5)`
- `prods2045Pr2a_I0_open_search`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score -0.79(train -0.65 valid -0.79):`cs_first_high20(mul(day_flat_ratio(Ret), day_sum(Low)), ts_max(LogFloatCap, 1))`
  - score -1.22(train -1.15 valid -1.22):`cs_first_high20(cs_first_high20(sub(day_flat_ratio(Ret), day_zero_ratio(High)), cs_first_high20(mul(day_flat_ratio(Ret), day_zero_ratio(High)), ts_max(LogFloatCap, 1))), ts_max(cs_first_high20(mul(day_flat_ratio(Ret), day_zero_ratio(High)), ts_max(LogFloatCap, 1)), 40))`
  - score -1.23(train -1.12 valid -1.23):`cs_first_high20(day_flat_ratio(Ret), ts_max(LogFloatCap, 40))`
  - score -1.33(train -1.11 valid -1.33):`cs_first_high20(cs_first_high20(sub(day_flat_ratio(Ret), day_zero_ratio(High)), LogFloatCap), ts_max(LogFloatCap, 40))`
  - score -1.36(train -1.05 valid -1.36):`cs_first_high20(mul(day_flat_ratio(Ret), ts_max(LogFloatCap, 1)), LogFloatCap)`
- `prods2045Pr2b_Nb`:核心 `—`;评分 77,过线 0,入 heads 0;采样计数 {'c05_skeleton': 24}
  - score -0.07(train -0.07 valid +0.17):`cross_autocorr_s1(day_at_max_ratio(Open), 15)`
  - score -1.30(train -0.27 valid -1.30):`cross_hurst(day_at_max_ratio(in_quantile_q25(Open, 3)), 15)`
  - score -1.31(train -1.31 valid -0.57):`cross_hurst(day_at_max_ratio(in_quantile_q25(in_quantile_q25(Open, 3), 3)), 30)`
  - score -1.32(train -0.68 valid -1.32):`cross_hurst(day_at_max_ratio(Open), 15)`
  - score -1.41(train -0.78 valid -1.41):`cross_hurst(day_at_max_ratio(in_quantile_q25(in_quantile_q25(Open, 3), 3)), 15)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.19(knockout ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40)):`ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 50), 40), 50), 40)`
- 增益 +0.13(knockout ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40)):`ts_std(ts_cov(day_quantile_q25(Ret), ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 50), 40)`
- 增益 +0.12(window ts_std@40->20):`ts_std(ts_cov(day_quantile_q25(Ret), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), ts_std(ts_cov(day_cov(pow_2(nt_cs_rank(cross_delta(High, 30))), Low), day_close(High), 50), 40), 50), 40), 50), 20)`
