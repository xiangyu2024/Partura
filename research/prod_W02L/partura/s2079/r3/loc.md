# 定位:种子 2079,P 组,第 3 轮(只含 train / valid)

快照:prods2079M1_I0_open_search, prods2079M2_I0_open_search, prods2079M3_I0_open_search, prods2079Pr1a_Ea, prods2079Pr1b_Nb, prods2079Pr2a_Ea, prods2079Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.14 | +0.16 | -0.14 | +1 | 5 | prods2079M2_I0_open_search | `ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 20)` |
| -0.26 | +0.18 | -0.26 | +1 | 0 | prods2079M2_I0_open_search | `ts_max(log(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)), 20)` |
| -0.36 | -0.12 | -0.36 | +1 | 5 | prods2079M2_I0_open_search | `ts_max(ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10)), 20), 20)` |
| -0.73 | -0.49 | -0.73 | +1 | 0 | prods2079M3_I0_open_search | `ts_quantile_q25(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30), 10)` |
| -0.78 | -0.78 | -0.60 | +1 | 20 | prods2079M1_I0_open_search | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| -1.21 | -1.21 | -0.63 | +1 | 5 | prods2079M3_I0_open_search | `ts_quantile_q75(add(cross_max(day_cov(Amt, Close), 60), cross_max(day_cov(Close, Close), 5)), 5)` |
| -1.35 | -1.35 | -1.29 | +1 | 5 | prods2079M1_I0_open_search | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100)` |
| -1.45 | -1.12 | -1.45 | -1 | 0 | prods2079M3_I0_open_search | `ts_mean(day_last(Volume), 50)` |
| -1.52 | -1.52 | -1.06 | +1 | 5 | prods2079M1_I0_open_search | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 241), 20)` |

## 共性:307 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.41 | 0.000 | 6 | +0.00 / -2.41 | `ts_max(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 40)` |
| +1.98 | 0.001 | 4 | -0.41 / -2.38 | `ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 1)` |
| +1.51 | 0.003 | 4 | -0.87 / -2.38 | `cross_cov(day_last(Amt), day_last(Amt), 10)` |
| +1.51 | 0.003 | 4 | -0.87 / -2.38 | `log(cross_cov(day_last(Amt), day_last(Amt), 10))` |
| +1.16 | 0.001 | 11 | -1.24 / -2.40 | `day_wmean(Ret, Amt)` |
| +1.03 | 0.000 | 14 | -1.37 / -2.41 | `day_last(Amt)` |
| +0.95 | 0.008 | 9 | -1.44 / -2.39 | `sub(day_wmean(Ret, Amt), day_mean(Ret))` |
| +0.85 | 0.038 | 4 | -1.52 / -2.37 | `log(cross_regbeta(log(day_last(Amt)), day_last(Amt), 10))` |
| +0.85 | 0.023 | 5 | -1.52 / -2.37 | `log(day_last(Amt))` |
| +0.85 | 0.023 | 5 | -1.52 / -2.37 | `cross_regbeta(log(day_last(Amt)), day_last(Amt), 10)` |
| +0.84 | 0.000 | 52 | -1.66 / -2.50 | `day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239))` |
| +0.76 | 0.042 | 4 | -1.61 / -2.37 | `cross_regbeta(day_quantile_q25(Low), day_var(Low), 241)` |
| +0.74 | 0.033 | 5 | -1.63 / -2.37 | `day_quantile_q25(Low)` |
| +0.66 | 0.035 | 6 | -1.71 / -2.37 | `day_var(Low)` |
| +0.57 | 0.049 | 8 | -1.80 / -2.37 | `div(ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20), ts_delay(day_last(Close), 1))` |
| +0.45 | 0.095 | 14 | -1.93 / -2.38 | `day_mean(Ret)` |
| +0.45 | 0.149 | 4 | -1.91 / -2.36 | `cross_corr(day_skew(Ret), day_last(Ret), 10)` |
| +0.45 | 0.149 | 4 | -1.91 / -2.36 | `ts_quantile_q75(cross_corr(day_skew(Ret), day_last(Ret), 10), 1)` |
| +0.44 | 0.141 | 6 | -1.93 / -2.37 | `day_last(Volume)` |
| +0.43 | 0.106 | 9 | -1.94 / -2.37 | `ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20)` |

## 拆解(22 次评估)

### head score -0.73:`ts_quantile_q25(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30)` | -0.58 | -0.28 | -0.58 | — | (子树本身) |
| sufficiency | `ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30)` | -3.19 | -3.08 | -3.19 | — | (子树本身) |
| sufficiency | `day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt)))` | — | — | — | — | 门槛废品 |
| knockout | `ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30)` | -3.45 | -3.13 | -3.45 | +2.72 | `ts_quantile_q25(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 10)` |
| swap | `Amt->Volume` | -0.34 | +0.10 | -0.34 | — | `ts_quantile_q25(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Volume))), 30), 30), 10)` |
| window | `ts_quantile_q25@10->5` | -0.43 | -0.43 | -0.43 | — | `ts_quantile_q25(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30), 5)` |
| window | `ts_quantile_q25@10->20` | -2.06 | -1.89 | -2.06 | — | `ts_quantile_q25(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30), 20)` |

### head score -1.21:`ts_quantile_q75(add(cross_max(day_cov(Amt, Close), 60), cross_max(day_cov(Close, Close), 5)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `add(cross_max(day_cov(Amt, Close), 60), cross_max(day_cov(Close, Close), 5))` | -1.21 | -1.21 | -0.76 | — | (子树本身) |
| sufficiency | `cross_max(day_cov(Amt, Close), 60)` | -1.21 | -1.21 | -0.76 | — | (子树本身) |
| sufficiency | `cross_max(day_cov(Close, Close), 5)` | -2.32 | -1.51 | -2.32 | — | (子树本身) |
| sufficiency | `day_cov(Amt, Close)` | -4.91 | -4.91 | -3.60 | — | (子树本身) |
| knockout | `add(cross_max(day_cov(Amt, Close), 60), cross_max(day_cov(Close, Close), 5))` | -1.21 | -1.21 | -0.62 | +0.00 | `ts_quantile_q75(cross_max(day_cov(Amt, Close), 60), 5)` |
| knockout | `cross_max(day_cov(Amt, Close), 60)` | -2.85 | -2.85 | -2.48 | +1.63 | `ts_quantile_q75(add(day_cov(Amt, Close), cross_max(day_cov(Close, Close), 5)), 5)` |
| knockout | `cross_max(day_cov(Close, Close), 5)` | -1.21 | -1.21 | -0.62 | +0.00 | `ts_quantile_q75(add(cross_max(day_cov(Amt, Close), 60), day_cov(Close, Close)), 5)` |
| swap | `Amt->Volume` | -0.84 | -0.35 | -0.84 | — | `ts_quantile_q75(add(cross_max(day_cov(Volume, Close), 60), cross_max(day_cov(Close, Close), 5)), 5)` |
| swap | `Close->Vwap` | -1.32 | -1.32 | -0.54 | — | `ts_quantile_q75(add(cross_max(day_cov(Amt, Vwap), 60), cross_max(day_cov(Vwap, Vwap), 5)), 5)` |
| window | `ts_quantile_q75@5->2` | -1.17 | -1.17 | -0.66 | — | `ts_quantile_q75(add(cross_max(day_cov(Amt, Close), 60), cross_max(day_cov(Close, Close), 5)), 2)` |
| window | `ts_quantile_q75@5->10` | -1.29 | -1.29 | -0.72 | — | `ts_quantile_q75(add(cross_max(day_cov(Amt, Close), 60), cross_max(day_cov(Close, Close), 5)), 10)` |

### head score -1.45:`ts_mean(day_last(Volume), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_last(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| swap | `Volume->Amt` | -1.93 | -1.93 | -1.29 | — | `ts_mean(day_last(Amt), 50)` |
| window | `ts_mean@50->25` | -1.56 | -1.12 | -1.56 | — | `ts_mean(day_last(Volume), 25)` |
| window | `ts_mean@50->100` | -1.69 | -1.21 | -1.69 | — | `ts_mean(day_last(Volume), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_max(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 40)` — enrichment,均值差 +2.41,p 0.000
2. `ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 1)` — enrichment,均值差 +1.98,p 0.001
3. `cross_cov(day_last(Amt), day_last(Amt), 10)` — enrichment,均值差 +1.51,p 0.003
4. `log(cross_cov(day_last(Amt), day_last(Amt), 10))` — enrichment,均值差 +1.51,p 0.003
5. `day_wmean(Ret, Amt)` — enrichment,均值差 +1.16,p 0.001
6. `day_last(Amt)` — enrichment,均值差 +1.03,p 0.000
7. `sub(day_wmean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +0.95,p 0.008
8. `log(cross_regbeta(log(day_last(Amt)), day_last(Amt), 10))` — enrichment,均值差 +0.85,p 0.038
9. `log(day_last(Amt))` — enrichment,均值差 +0.85,p 0.023
10. `cross_regbeta(log(day_last(Amt)), day_last(Amt), 10)` — enrichment,均值差 +0.85,p 0.023
11. `day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239))` — enrichment,均值差 +0.84,p 0.000
12. `cross_regbeta(day_quantile_q25(Low), day_var(Low), 241)` — enrichment,均值差 +0.76,p 0.042
13. `day_quantile_q25(Low)` — enrichment,均值差 +0.74,p 0.033
14. `day_var(Low)` — enrichment,均值差 +0.66,p 0.035
15. `div(ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20), ts_delay(day_last(Close), 1))` — enrichment,均值差 +0.57,p 0.049
16. `day_mean(Ret)` — enrichment,均值差 +0.45,p 0.095

## 本组之前各轮的任务

- `prods2079Pr1a_Ea`:核心 `sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_no_core': 1462, 'c05_skeleton': 671, 'c05_periphery_seen': 7, 'mutation_refused': 18}
  - score -0.98(train -0.71 valid -0.98):`ts_kurt(ts_max(sub(div(day_max(High), div(ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20), ts_delay(day_last(Close), 1))), 1), 1), 40)`
  - score -1.18(train -0.40 valid -1.18):`ts_hurst(ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 1), 40)`
  - score -1.19(train -0.40 valid -1.19):`ts_hurst(ts_max(sub(ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 1), 1), 1), 40)`
  - score -1.24(train -1.24 valid -0.87):`ts_autocorr_s1(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 10)`
  - score -1.35(train -1.35 valid -0.57):`ts_hurst(ts_max(div(div(ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20), ts_delay(day_last(Close), 1)), 1), 1), 40)`
- `prods2079Pr1b_Nb`:核心 `—`;评分 85,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.22(train -0.22 valid +0.23):`cross_ema(cross_ema(ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 1), 241), 241)`
  - score -0.22(train -0.22 valid +0.23):`cross_ema(ts_quantile_q75(cross_ema(ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 1), 241), 1), 241)`
  - score -0.51(train -0.51 valid +0.11):`cross_ema(ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 1), 241)`
  - score -0.68(train -0.68 valid +0.07):`cross_mean(cross_ema(ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 1), 241), 30)`
  - score -0.98(train -0.78 valid -0.98):`cross_mean(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 30)`
- `prods2079Pr2a_Ea`:核心 `day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239))`;评分 72,过线 0,入 heads 0;采样计数 {'c05_skeleton': 607, 'c05_no_core': 1284, 'c05_periphery_seen': 6}
  - score +0.41(train +0.46 valid +0.41):`ts_max(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 50)`
  - score +0.30(train +0.30 valid +0.40):`cross_decay_linear(ts_max(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 40), 30)`
  - score +0.30(train +0.30 valid +0.40):`ts_max(cross_decay_linear(ts_max(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 40), 30), 1)`
  - score +0.25(train +0.51 valid +0.25):`ts_max(ts_max(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 50), 50)`
  - score +0.19(train +0.19 valid +0.49):`ts_max(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 40)`
- `prods2079Pr2b_Nb`:核心 `—`;评分 68,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.27(train -0.15 valid -0.27):`cross_ema(day_wmean(Ret, Amt), 60)`
  - score -0.32(train -0.19 valid -0.32):`cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60)`
  - score -0.34(train -0.12 valid -0.34):`cross_ema(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 30), 30)`
  - score -0.39(train -0.29 valid -0.39):`cross_ema(day_wmean(Ret, Amt), 30)`
  - score -0.39(train -0.21 valid -0.39):`cross_ema(cross_ema(sub(day_wmean(Ret, Amt), day_mean(Ret)), 60), 30)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.39(swap Amt->Volume):`ts_quantile_q25(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Volume))), 30), 30), 10)`
- 增益 +0.30(window ts_quantile_q25@10->5):`ts_quantile_q25(ts_stddev(ts_stddev(day_sum(nt_cs_quantile_q25(nt_cs_quantile_q25(Amt))), 30), 30), 5)`
