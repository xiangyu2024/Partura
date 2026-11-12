# 定位:种子 2079,P 组,第 2 轮(只含 train / valid)

快照:prods2079M1_I0_open_search, prods2079M2_I0_open_search, prods2079Pr1a_Ea, prods2079Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.14 | +0.16 | -0.14 | +1 | 5 | prods2079M2_I0_open_search | `ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 20)` |
| -0.26 | +0.18 | -0.26 | +1 | 0 | prods2079M2_I0_open_search | `ts_max(log(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)), 20)` |
| -0.36 | -0.12 | -0.36 | +1 | 5 | prods2079M2_I0_open_search | `ts_max(ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10)), 20), 20)` |
| -0.78 | -0.78 | -0.60 | +1 | 20 | prods2079M1_I0_open_search | `sub(ts_var(ts_mean(cross_cov(day_close(Amt), day_hurst(Open), 30), 40), 5), signedpower(day_ar1_coefficient(in_shift(Low, 15))))` |
| -1.35 | -1.35 | -1.29 | +1 | 5 | prods2079M1_I0_open_search | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100)` |
| -1.52 | -1.52 | -1.06 | +1 | 5 | prods2079M1_I0_open_search | `ts_max(cross_regbeta(day_quantile_q25(Low), day_var(Low), 241), 20)` |

## 共性:187 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.04 | 0.000 | 4 | -0.41 / -2.45 | `ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 1)` |
| +1.57 | 0.001 | 4 | -0.87 / -2.44 | `log(cross_cov(day_last(Amt), day_last(Amt), 10))` |
| +1.57 | 0.001 | 4 | -0.87 / -2.44 | `cross_cov(day_last(Amt), day_last(Amt), 10)` |
| +1.19 | 0.000 | 10 | -1.28 / -2.47 | `day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239))` |
| +1.11 | 0.000 | 14 | -1.37 / -2.49 | `day_last(Amt)` |
| +0.91 | 0.024 | 4 | -1.52 / -2.42 | `log(cross_regbeta(log(day_last(Amt)), day_last(Amt), 10))` |
| +0.90 | 0.012 | 5 | -1.52 / -2.43 | `log(day_last(Amt))` |
| +0.90 | 0.012 | 5 | -1.52 / -2.43 | `cross_regbeta(log(day_last(Amt)), day_last(Amt), 10)` |
| +0.82 | 0.025 | 4 | -1.61 / -2.42 | `cross_regbeta(day_quantile_q25(Low), day_var(Low), 241)` |
| +0.79 | 0.018 | 5 | -1.63 / -2.43 | `day_quantile_q25(Low)` |
| +0.72 | 0.020 | 6 | -1.71 / -2.43 | `day_var(Low)` |
| +0.63 | 0.026 | 8 | -1.80 / -2.43 | `div(ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20), ts_delay(day_last(Close), 1))` |
| +0.50 | 0.122 | 4 | -1.91 / -2.42 | `cross_corr(day_skew(Ret), day_last(Ret), 10)` |
| +0.50 | 0.122 | 4 | -1.91 / -2.42 | `ts_quantile_q75(cross_corr(day_skew(Ret), day_last(Ret), 10), 1)` |
| +0.49 | 0.065 | 9 | -1.94 / -2.43 | `ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20)` |
| +0.46 | 0.151 | 4 | -1.96 / -2.41 | `day_close(High)` |
| +0.39 | 0.121 | 9 | -2.04 / -2.42 | `inv(day_sum(Ret))` |
| +0.31 | 0.216 | 7 | -2.10 / -2.42 | `cross_tail_mean_q75(inv(day_sum(Ret)), 5)` |
| +0.24 | 0.246 | 11 | -2.18 / -2.42 | `day_sum(Ret)` |
| +0.10 | 0.430 | 44 | -2.33 / -2.43 | `ts_delay(day_last(Close), 1)` |

## 拆解(41 次评估)

### head score -0.14:`ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)` | -0.82 | -0.82 | -0.62 | — | (子树本身) |
| sufficiency | `log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10))` | -1.63 | -1.63 | -0.42 | — | (子树本身) |
| sufficiency | `cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)` | -1.63 | -1.63 | -0.42 | — | (子树本身) |
| sufficiency | `log(day_open(Amt))` | -2.06 | -2.06 | -1.04 | — | (子树本身) |
| knockout | `log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10))` | -0.11 | +0.16 | -0.11 | -0.03 | `ts_max(ts_max(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10), 20), 20)` |
| knockout | `cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)` | -0.18 | -0.18 | +0.03 | +0.04 | `ts_max(ts_max(log(log(day_open(Amt))), 20), 20)` |
| knockout | `log(day_open(Amt))` | — | — | — | — | `ts_max(ts_max(log(cross_regbeta(day_open(Amt), day_open(Amt), 10)), 20), 20)` |
| swap | `Amt->Volume` | -1.97 | -0.92 | -1.97 | — | `ts_max(ts_max(log(cross_regbeta(log(day_open(Volume)), day_open(Volume), 10)), 20), 20)` |
| window | `ts_max@20->10` | -0.20 | -0.20 | -0.14 | — | `ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)` |
| window | `ts_max@20->40` | +0.11 | +0.32 | +0.11 | — | `ts_max(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 40)` |

### head score -0.26:`ts_max(log(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10))` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)` | — | — | — | — | 门槛废品 |
| sufficiency | `log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20))` | -0.82 | -0.82 | -0.62 | — | (子树本身) |
| sufficiency | `ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)` | -0.82 | -0.82 | -0.62 | — | (子树本身) |
| knockout | `log(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10))` | -0.23 | +0.18 | -0.23 | -0.03 | `ts_max(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10), 20)` |
| knockout | `cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)` | -0.11 | +0.16 | -0.11 | -0.14 | `ts_max(log(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20))), 20)` |
| knockout | `log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20))` | — | — | — | — | `ts_max(log(cross_regbeta(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)), 20)` |
| knockout | `ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)` | -0.42 | -0.42 | -0.39 | +0.16 | `ts_max(log(cross_regbeta(log(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10))), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)), 20)` |
| swap | `Amt->Volume` | -2.10 | -0.98 | -2.10 | — | `ts_max(log(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Volume)), day_open(Volume), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Volume)), day_open(Volume), 10)), 20), 10)), 20)` |
| window | `ts_max@20->10` | -0.81 | -0.81 | -0.80 | — | `ts_max(log(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)), 10)` |
| window | `ts_max@20->40` | -0.08 | +0.16 | -0.08 | — | `ts_max(log(cross_regbeta(log(ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20)), ts_max(log(cross_regbeta(log(day_open(Amt)), day_open(Amt), 10)), 20), 10)), 40)` |

### head score -0.36:`ts_max(ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10)), 20), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10)), 20)` | -1.25 | -1.25 | +0.05 | — | (子树本身) |
| sufficiency | `log(cross_cov(day_last(Amt), day_last(Amt), 10))` | -2.98 | -2.98 | -1.32 | — | (子树本身) |
| sufficiency | `cross_cov(day_last(Amt), day_last(Amt), 10)` | -3.22 | -3.22 | -1.01 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| knockout | `log(cross_cov(day_last(Amt), day_last(Amt), 10))` | -0.32 | -0.12 | -0.32 | -0.05 | `ts_max(ts_max(cross_cov(day_last(Amt), day_last(Amt), 10), 20), 20)` |
| knockout | `cross_cov(day_last(Amt), day_last(Amt), 10)` | -0.78 | -0.78 | -0.42 | +0.42 | `ts_max(ts_max(log(day_last(Amt)), 20), 20)` |
| swap | `Amt->Volume` | -1.51 | -1.16 | -1.51 | — | `ts_max(ts_max(log(cross_cov(day_last(Volume), day_last(Volume), 10)), 20), 20)` |
| window | `ts_max@20->10` | -0.90 | -0.90 | -0.17 | — | `ts_max(ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10)), 20), 10)` |
| window | `ts_max@20->40` | -0.30 | -0.25 | -0.30 | — | `ts_max(ts_max(log(cross_cov(day_last(Amt), day_last(Amt), 10)), 20), 40)` |

### head score -1.35:`ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 100)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_max(High), ts_delay(day_last(Close), 1))` | -2.74 | -2.74 | -2.70 | — | (子树本身) |
| sufficiency | `ts_delay(day_last(Close), 1)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| sufficiency | `day_max(High)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| sufficiency | `day_last(Close)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1)` | -1.35 | -1.35 | -1.29 | -0.00 | `ts_stddev(div(day_max(High), ts_delay(day_last(Close), 1)), 100)` |
| knockout | `div(day_max(High), ts_delay(day_last(Close), 1))` | -2.16 | -1.71 | -2.16 | +0.80 | `ts_stddev(sub(day_max(High), 1), 100)` |
| knockout | `ts_delay(day_last(Close), 1)` | -2.25 | -2.25 | -1.91 | +0.89 | `ts_stddev(sub(div(day_max(High), day_last(Close)), 1), 100)` |
| swap | `High->Low` | -1.46 | -1.40 | -1.46 | — | `ts_stddev(sub(div(day_max(Low), ts_delay(day_last(Close), 1)), 1), 100)` |
| swap | `Close->Vwap` | -1.34 | -1.34 | -1.25 | — | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Vwap), 1)), 1), 100)` |
| window | `ts_stddev@100->50` | -1.54 | -1.45 | -1.54 | — | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 50)` |
| window | `ts_stddev@100->200` | -1.08 | -0.98 | -1.08 | — | `ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 200)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_quantile_q75(day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239)), 1)` — enrichment,均值差 +2.04,p 0.000
2. `log(cross_cov(day_last(Amt), day_last(Amt), 10))` — enrichment,均值差 +1.57,p 0.001
3. `cross_cov(day_last(Amt), day_last(Amt), 10)` — enrichment,均值差 +1.57,p 0.001
4. `day_corr(in_slice(Amt, 2, 240), in_slice(Ret, 1, 239))` — enrichment,均值差 +1.19,p 0.000
5. `day_last(Amt)` — enrichment,均值差 +1.11,p 0.000
6. `log(cross_regbeta(log(day_last(Amt)), day_last(Amt), 10))` — enrichment,均值差 +0.91,p 0.024
7. `log(day_last(Amt))` — enrichment,均值差 +0.90,p 0.012
8. `cross_regbeta(log(day_last(Amt)), day_last(Amt), 10)` — enrichment,均值差 +0.90,p 0.012
9. `cross_regbeta(day_quantile_q25(Low), day_var(Low), 241)` — enrichment,均值差 +0.82,p 0.025
10. `day_quantile_q25(Low)` — enrichment,均值差 +0.79,p 0.018
11. `day_var(Low)` — enrichment,均值差 +0.72,p 0.020
12. `div(ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20), ts_delay(day_last(Close), 1))` — enrichment,均值差 +0.63,p 0.026
13. `ts_max(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 20)` — enrichment,均值差 +0.49,p 0.065

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.28(window ts_stddev@100->200):`ts_stddev(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), 200)`
