# 定位:种子 2066,P 组,第 3 轮(只含 train / valid)

快照:prods2066M1_I0_open_search, prods2066M2_I0_open_search, prods2066M3_I0_open_search, prods2066Pr1a_Na, prods2066Pr1b_Nb, prods2066Pr2a_Ea, prods2066Pr2b_Eb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.14 | -0.76 | -1.14 | -1 | 20 | prods2066M1_I0_open_search | `pow_2(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30))))` |
| -1.14 | -0.76 | -1.14 | -1 | 20 | prods2066M1_I0_open_search | `sigmoid(abs_(day_mean(nt_cs_normalize(in_cov(Ret, Close, 30)))))` |
| -1.15 | -0.83 | -1.15 | -1 | 20 | prods2066M1_I0_open_search | `pow_2(pow_05(day_mean(nt_cs_normalize(in_cov(Ret, Close, 15)))))` |
| -2.19 | -1.77 | -2.19 | +1 | 0 | prods2066M3_I0_open_search | `day_autocorr_n1(nt_ts_min(signedpower(cross_med(nt_ts_min(signedpower(cross_med(Ret, 60)), 3), 60)), 3))` |
| -2.23 | -2.23 | -1.15 | +1 | 5 | prods2066M3_I0_open_search | `day_autocorr_n1(signedpower(cross_med(Ret, 60)))` |
| -2.31 | -2.31 | -1.87 | +1 | 5 | prods2066M2_I0_open_search | `cross_stddev(day_skew(div(Volume, in_sum(Volume))), 20)` |
| -2.34 | -2.34 | -2.12 | +1 | 5 | prods2066M2_I0_open_search | `cross_stddev(day_kurt(div(Volume, in_sum(Volume))), 20)` |
| -2.45 | -1.14 | -2.45 | +1 | 5 | prods2066M3_I0_open_search | `cross_stddev(day_var(cross_med(Ret, 60)), 60)` |
| -3.86 | -3.61 | -3.86 | -1 | 20 | prods2066M2_I0_open_search | `cross_stddev(div(day_skew(div(Volume, in_sum(Volume))), day_kurt(div(Volume, in_sum(Volume)))), 20)` |

## 共性:214 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.46 | 0.003 | 6 | -0.90 / -2.36 | `pow_3(day_hurst(cross_ema(pow_1_5(Volume), 60)))` |
| +1.39 | 0.000 | 62 | -1.33 / -2.73 | `day_hurst(cross_ema(pow_1_5(Volume), 60))` |
| +1.29 | 0.052 | 4 | -1.06 / -2.35 | `day_hurst(pow_1_5(Volume))` |
| +1.19 | 0.072 | 5 | -1.16 / -2.35 | `day_hurst(Volume)` |
| +0.53 | 0.023 | 39 | -1.89 / -2.42 | `day_centroid(pow_3(pow_1_5(Volume)))` |
| +0.12 | 0.535 | 5 | -2.20 / -2.33 | `day_centroid(Amt)` |
| +0.02 | 0.693 | 11 | -2.31 / -2.32 | `day_var(Open)` |
| -0.08 | 0.714 | 7 | -2.40 / -2.32 | `cross_delay(day_var(Open), 60)` |
| -0.14 | 0.709 | 17 | -2.45 / -2.31 | `day_signed_ratio(Ret, Open)` |
| -0.17 | 0.792 | 6 | -2.48 / -2.32 | `cross_mean(day_centroid(pow_3(pow_1_5(Volume))), 5)` |
| -0.79 | 0.887 | 7 | -3.08 / -2.30 | `day_signed_ratio(Close, Low)` |
| -1.08 | 0.926 | 6 | -3.37 / -2.29 | `day_centroid(Ret)` |
| -1.27 | 0.986 | 9 | -3.53 / -2.27 | `day_es_ratio_lo(Ret)` |
| -1.49 | 0.993 | 5 | -3.78 / -2.29 | `day_kurt(div(Volume, in_sum(Volume)))` |
| -1.61 | 0.994 | 5 | -3.89 / -2.28 | `day_skew(div(Volume, in_sum(Volume)))` |
| -1.66 | 1.000 | 15 | -3.86 / -2.21 | `day_q_stat_std(Vwap)` |
| -1.81 | 1.000 | 12 | -4.03 / -2.22 | `inv(day_q_stat_std(Vwap))` |
| -1.89 | 1.000 | 9 | -4.13 / -2.24 | `day_signed_ratio(Ret, Amt)` |

## 拆解(7 次评估)

### head score -2.19:`day_autocorr_n1(nt_ts_min(signedpower(cross_med(nt_ts_min(signedpower(cross_med(Ret, 60)), 3), 60)), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| window | `nt_ts_min@3->2` | -2.18 | -1.78 | -2.18 | — | `day_autocorr_n1(nt_ts_min(signedpower(cross_med(nt_ts_min(signedpower(cross_med(Ret, 60)), 3), 60)), 2))` |
| window | `nt_ts_min@3->6` | -1.92 | -1.79 | -1.92 | — | `day_autocorr_n1(nt_ts_min(signedpower(cross_med(nt_ts_min(signedpower(cross_med(Ret, 60)), 3), 60)), 6))` |

### head score -2.23:`day_autocorr_n1(signedpower(cross_med(Ret, 60)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| window | `cross_med@60->30` | -2.11 | -2.11 | -1.03 | — | `day_autocorr_n1(signedpower(cross_med(Ret, 30)))` |
| window | `cross_med@60->120` | -1.85 | -1.85 | -0.57 | — | `day_autocorr_n1(signedpower(cross_med(Ret, 120)))` |

### head score -2.45:`cross_stddev(day_var(cross_med(Ret, 60)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_var(cross_med(Ret, 60))` | -3.01 | -2.42 | -3.01 | — | (子树本身) |
| window | `cross_stddev@60->30` | -2.84 | -0.99 | -2.84 | — | `cross_stddev(day_var(cross_med(Ret, 60)), 30)` |
| window | `cross_stddev@60->120` | -2.05 | -1.28 | -2.05 | — | `cross_stddev(day_var(cross_med(Ret, 60)), 120)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_3(day_hurst(cross_ema(pow_1_5(Volume), 60)))` — enrichment,均值差 +1.46,p 0.003
2. `day_hurst(cross_ema(pow_1_5(Volume), 60))` — enrichment,均值差 +1.39,p 0.000
3. `day_hurst(pow_1_5(Volume))` — enrichment,均值差 +1.29,p 0.052
4. `day_hurst(Volume)` — enrichment,均值差 +1.19,p 0.072
5. `day_centroid(pow_3(pow_1_5(Volume)))` — enrichment,均值差 +0.53,p 0.023

## 本组之前各轮的任务

- `prods2066Pr1a_Na`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.34(train -0.34 valid -0.12):`cross_min(cross_semistd_pos(day_centroid(pow_3(pow_1_5(Volume))), 10), 10)`
  - score -0.38(train -0.21 valid -0.38):`cross_min(day_hurst(cross_ema(pow_1_5(cross_ema(pow_1_5(Volume), 60)), 60)), 10)`
  - score -0.47(train -0.19 valid -0.47):`cross_min(cross_min(day_centroid(pow_3(pow_1_5(Volume))), 10), 10)`
  - score -0.50(train -0.50 valid -0.12):`cross_min(day_centroid(pow_3(pow_1_5(Volume))), 10)`
  - score -0.55(train -0.55 valid +0.06):`cross_min(cross_min(day_centroid(pow_3(pow_1_5(Volume))), 10), 241)`
- `prods2066Pr1b_Nb`:核心 `—`;评分 85,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -1.25(train -0.93 valid -1.25):`cross_regbeta(cross_delay(day_var(Open), 60), inv(day_es_ratio_lo(Ret)), 10)`
  - score -1.39(train -0.81 valid -1.39):`cross_regbeta(cross_delay(day_var(Open), 3), day_es_ratio_lo(Ret), 10)`
  - score -1.44(train -1.44 valid -1.19):`cross_regbeta(cross_delay(day_var(Open), 60), inv(day_q_stat_std(Vwap)), 10)`
  - score -1.63(train -1.53 valid -1.63):`cross_regbeta(cross_delay(day_var(Open), 60), day_signed_ratio(Ret, Open), 10)`
  - score -2.03(train -2.03 valid -1.96):`mul(day_signed_ratio(Close, Low), day_signed_ratio(Ret, Open))`
- `prods2066Pr2a_Ea`:核心 `day_centroid(pow_3(pow_1_5(Volume)))`;评分 78,过线 0,入 heads 0;采样计数 {'c05_skeleton': 971, 'c05_no_core': 2044, 'c05_periphery_seen': 5}
  - score -0.24(train +0.80 valid -0.24):`ts_min(ts_min(day_centroid(pow_3(pow_1_5(Volume))), 30), 30)`
  - score -0.35(train +0.46 valid -0.35):`ts_min(day_centroid(pow_3(pow_1_5(Volume))), 50)`
  - score -0.47(train -0.19 valid -0.47):`ts_min(ts_min(day_centroid(pow_3(pow_1_5(Volume))), 10), 10)`
  - score -0.50(train -0.50 valid -0.12):`ts_min(day_centroid(pow_3(pow_1_5(Volume))), 10)`
  - score -0.52(train -0.28 valid -0.52):`ts_min(day_centroid(pow_3(pow_1_5(Volume))), 30)`
- `prods2066Pr2b_Eb`:核心 `day_hurst(cross_ema(pow_1_5(Volume), 60))`;评分 71,过线 0,入 heads 0;采样计数 {'c05_no_core': 667, 'c05_skeleton': 336, 'c05_periphery_seen': 6, 'mutation_refused': 5}
  - score +0.27(train +1.23 valid +0.27):`sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Volume))`
  - score +0.27(train +1.21 valid +0.27):`div(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Volume))`
  - score +0.22(train +1.16 valid +0.22):`sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(pow_1_5(Volume)))`
  - score +0.21(train +1.05 valid +0.21):`div(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(pow_1_5(Volume)))`
  - score +0.04(train +0.18 valid +0.04):`sub(sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), day_hurst(Volume)), day_hurst(Volume))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.39(window cross_stddev@60->120):`cross_stddev(day_var(cross_med(Ret, 60)), 120)`
- 增益 +0.27(window nt_ts_min@3->6):`day_autocorr_n1(nt_ts_min(signedpower(cross_med(nt_ts_min(signedpower(cross_med(Ret, 60)), 3), 60)), 6))`
- 增益 +0.11(window cross_med@60->30):`day_autocorr_n1(signedpower(cross_med(Ret, 30)))`
