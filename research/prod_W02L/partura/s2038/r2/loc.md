# 定位:种子 2038,P 组,第 2 轮(只含 train / valid)

快照:prods2038M1_I0_open_search, prods2038M2_I0_open_search, prods2038Pr1a_Na, prods2038Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.41 | -0.41 | -0.19 | +1 | 20 | prods2038M1_I0_open_search | `signedpower(div(day_open(Amt), add(cross_mean(day_sum(Amt), 20), 1)))` |
| -0.43 | +0.11 | -0.43 | +1 | 0 | prods2038M1_I0_open_search | `ts_max(ts_max(log(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 20), 50)` |
| -1.01 | -1.01 | -0.66 | +1 | 20 | prods2038M2_I0_open_search | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_autocorr_n1(Volume), 60), 50), 15), 15)` |
| -1.14 | -1.14 | -1.03 | -1 | 5 | prods2038M1_I0_open_search | `ts_decay_linear(day_open(Volume), 5)` |
| -1.52 | -1.52 | -0.83 | -1 | 5 | prods2038M2_I0_open_search | `ts_std(cross_quantile_q25(ts_std(day_autocorr_n1(Low), 50), 241), 50)` |
| -1.87 | -1.07 | -1.87 | +1 | 20 | prods2038M2_I0_open_search | `cross_hurst(day_autocorr_n1(Amt), 60)` |

## 共性:177 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.25 | 0.001 | 8 | -0.99 / -2.24 | `cross_regbeta(day_last(Amt), day_open(Amt), 10)` |
| +1.16 | 0.003 | 7 | -1.07 / -2.23 | `cs_rank(cross_regbeta(day_last(Amt), day_open(Amt), 10))` |
| +1.14 | 0.006 | 4 | -1.07 / -2.21 | `cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)), 10)` |
| +1.12 | 0.000 | 16 | -1.17 / -2.29 | `day_open(Amt)` |
| +1.07 | 0.000 | 34 | -1.32 / -2.39 | `day_last(Amt)` |
| +1.06 | 0.000 | 13 | -1.21 / -2.26 | `cross_min(day_last(Close), 482)` |
| +0.99 | 0.003 | 7 | -1.23 / -2.22 | `cross_min(cross_mean(day_last(Close), 10), 482)` |
| +0.99 | 0.003 | 7 | -1.23 / -2.22 | `cross_mean(day_last(Close), 10)` |
| +0.97 | 0.010 | 5 | -1.24 / -2.21 | `sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares))` |
| +0.96 | 0.000 | 52 | -1.51 / -2.47 | `cross_mean(LogFloatShares, 10)` |
| +0.89 | 0.000 | 44 | -1.52 / -2.41 | `cross_min(cross_mean(LogFloatShares, 10), 482)` |
| +0.86 | 0.000 | 41 | -1.53 / -2.38 | `sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482))` |
| +0.83 | 0.000 | 58 | -1.63 / -2.46 | `day_last(Close)` |
| +0.73 | 0.000 | 53 | -1.67 / -2.40 | `log(day_last(Close))` |
| +0.71 | 0.029 | 7 | -1.50 / -2.21 | `sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)` |
| +0.59 | 0.003 | 23 | -1.67 / -2.26 | `cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)` |
| +0.59 | 0.049 | 8 | -1.62 / -2.21 | `sub(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482))` |
| +0.55 | 0.001 | 45 | -1.77 / -2.33 | `sub(LogFloatCap, LogFloatShares)` |
| +0.54 | 0.002 | 43 | -1.78 / -2.32 | `sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares))` |
| +0.48 | 0.005 | 39 | -1.81 / -2.29 | `cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10)` |

## 拆解(30 次评估)

### head score -0.41:`signedpower(div(day_open(Amt), add(cross_mean(day_sum(Amt), 20), 1)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_sum(Amt), 20)` | -3.63 | -2.77 | -3.63 | — | (子树本身) |
| sufficiency | `day_open(Amt)` | -1.30 | -1.30 | -0.79 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| knockout | `div(day_open(Amt), add(cross_mean(day_sum(Amt), 20), 1))` | -1.30 | -1.30 | -0.79 | +0.89 | `signedpower(day_open(Amt))` |
| knockout | `add(cross_mean(day_sum(Amt), 20), 1)` | -0.41 | -0.41 | -0.19 | -0.00 | `signedpower(div(day_open(Amt), cross_mean(day_sum(Amt), 20)))` |
| knockout | `cross_mean(day_sum(Amt), 20)` | -0.48 | -0.48 | -0.19 | +0.07 | `signedpower(div(day_open(Amt), add(day_sum(Amt), 1)))` |
| swap | `Amt->Volume` | -0.39 | -0.39 | -0.24 | — | `signedpower(div(day_open(Volume), add(cross_mean(day_sum(Volume), 20), 1)))` |
| window | `cross_mean@20->10` | -0.42 | -0.42 | -0.23 | — | `signedpower(div(day_open(Amt), add(cross_mean(day_sum(Amt), 10), 1)))` |
| window | `cross_mean@20->40` | -0.64 | -0.61 | -0.64 | — | `signedpower(div(day_open(Amt), add(cross_mean(day_sum(Amt), 40), 1)))` |

### head score -1.01:`cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_autocorr_n1(Volume), 60), 50), 15), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q25(ts_min(cross_max(day_autocorr_n1(Volume), 60), 50), 15)` | -0.96 | -0.96 | -0.76 | — | (子树本身) |
| sufficiency | `ts_min(cross_max(day_autocorr_n1(Volume), 60), 50)` | -1.40 | -1.15 | -1.40 | — | (子树本身) |
| sufficiency | `cross_max(day_autocorr_n1(Volume), 60)` | -0.19 | +0.53 | -0.19 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Volume)` | -3.18 | -2.53 | -3.18 | — | (子树本身) |
| knockout | `ts_min(cross_max(day_autocorr_n1(Volume), 60), 50)` | -1.04 | -0.20 | -1.04 | +0.04 | `cross_quantile_q25(cross_quantile_q25(cross_max(day_autocorr_n1(Volume), 60), 15), 15)` |
| knockout | `cross_max(day_autocorr_n1(Volume), 60)` | -3.16 | -2.69 | -3.16 | +2.15 | `cross_quantile_q25(cross_quantile_q25(ts_min(day_autocorr_n1(Volume), 50), 15), 15)` |
| swap | `Volume->Amt` | -1.13 | -1.09 | -1.13 | — | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_autocorr_n1(Amt), 60), 50), 15), 15)` |
| window | `cross_quantile_q25@15->7` | -1.06 | -1.06 | -0.73 | — | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_autocorr_n1(Volume), 60), 50), 15), 7)` |
| window | `cross_quantile_q25@15->30` | -1.09 | -1.09 | -0.99 | — | `cross_quantile_q25(cross_quantile_q25(ts_min(cross_max(day_autocorr_n1(Volume), 60), 50), 15), 30)` |

### head score -1.52:`ts_std(cross_quantile_q25(ts_std(day_autocorr_n1(Low), 50), 241), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q25(ts_std(day_autocorr_n1(Low), 50), 241)` | -1.93 | -1.93 | -0.96 | — | (子树本身) |
| sufficiency | `ts_std(day_autocorr_n1(Low), 50)` | -2.27 | -2.27 | -2.11 | — | (子树本身) |
| sufficiency | `day_autocorr_n1(Low)` | -2.98 | -2.98 | -2.32 | — | (子树本身) |
| knockout | `cross_quantile_q25(ts_std(day_autocorr_n1(Low), 50), 241)` | -1.83 | -1.83 | -1.29 | +0.31 | `ts_std(ts_std(day_autocorr_n1(Low), 50), 50)` |
| knockout | `ts_std(day_autocorr_n1(Low), 50)` | -2.45 | -2.45 | -1.44 | +0.93 | `ts_std(cross_quantile_q25(day_autocorr_n1(Low), 241), 50)` |
| swap | `Low->High` | -3.49 | -1.79 | -3.49 | — | `ts_std(cross_quantile_q25(ts_std(day_autocorr_n1(High), 50), 241), 50)` |
| window | `ts_std@50->25` | -1.22 | -1.22 | -0.57 | — | `ts_std(cross_quantile_q25(ts_std(day_autocorr_n1(Low), 50), 241), 25)` |
| window | `ts_std@50->100` | -1.67 | -1.67 | -0.29 | — | `ts_std(cross_quantile_q25(ts_std(day_autocorr_n1(Low), 50), 241), 100)` |

### head score -1.87:`cross_hurst(day_autocorr_n1(Amt), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_autocorr_n1(Amt)` | -3.17 | -2.51 | -3.17 | — | (子树本身) |
| swap | `Amt->Volume` | -1.82 | -1.09 | -1.82 | — | `cross_hurst(day_autocorr_n1(Volume), 60)` |
| window | `cross_hurst@60->30` | -1.94 | -1.89 | -1.94 | — | `cross_hurst(day_autocorr_n1(Amt), 30)` |
| window | `cross_hurst@60->120` | -2.07 | -2.07 | -1.59 | — | `cross_hurst(day_autocorr_n1(Amt), 120)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_regbeta(day_last(Amt), day_open(Amt), 10)` — enrichment,均值差 +1.25,p 0.001
2. `cs_rank(cross_regbeta(day_last(Amt), day_open(Amt), 10))` — enrichment,均值差 +1.16,p 0.003
3. `cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)), 10)` — enrichment,均值差 +1.14,p 0.006
4. `day_open(Amt)` — enrichment,均值差 +1.12,p 0.000
5. `day_last(Amt)` — enrichment,均值差 +1.07,p 0.000
6. `cross_min(day_last(Close), 482)` — enrichment,均值差 +1.06,p 0.000
7. `cross_min(cross_mean(day_last(Close), 10), 482)` — enrichment,均值差 +0.99,p 0.003
8. `cross_mean(day_last(Close), 10)` — enrichment,均值差 +0.99,p 0.003
9. `sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares))` — enrichment,均值差 +0.97,p 0.010
10. `cross_mean(LogFloatShares, 10)` — enrichment,均值差 +0.96,p 0.000
11. `cross_min(cross_mean(LogFloatShares, 10), 482)` — enrichment,均值差 +0.89,p 0.000
12. `sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482))` — enrichment,均值差 +0.86,p 0.000
13. `day_last(Close)` — enrichment,均值差 +0.83,p 0.000
14. `log(day_last(Close))` — enrichment,均值差 +0.73,p 0.000
15. `sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)` — enrichment,均值差 +0.71,p 0.029
16. `cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)` — enrichment,均值差 +0.59,p 0.003
17. `sub(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482))` — enrichment,均值差 +0.59,p 0.049
18. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.55,p 0.001
19. `sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares))` — enrichment,均值差 +0.54,p 0.002
20. `cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10)` — enrichment,均值差 +0.48,p 0.005

## 本组之前各轮的任务

- `prods2038Pr1a_Na`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.52(train -0.52 valid -0.51):`cs_bucket_demean(sub(sub(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482))), LogFloatCap)`
  - score -0.75(train -0.61 valid -0.75):`cs_bucket_demean(sub(div(cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(LogFloatShares, 482)), LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 10), cross_min(LogFloatShares, 482))), LogFloatCap)`
  - score -0.94(train -0.94 valid -0.85):`cs_bucket_demean(sub(sub(cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482)), LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(LogFloatShares, 10), 482))), LogFloatCap)`
  - score -0.99(train -0.99 valid -0.83):`cs_bucket_demean(sub(sub(cross_mean(sub(log(day_last(Close)), sub(sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(cross_mean(LogFloatShares, 10), 10), 482)), LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 10), cross_min(cross_mean(cross_mean(LogFloatShares, 10), 10), 482))), LogFloatCap)`
  - score -1.04(train -0.59 valid -1.04):`cs_bucket_demean(sub(sub(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), cross_min(cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 10), 482)), sub(cross_mean(LogFloatShares, 241), cross_min(cross_mean(LogFloatShares, 10), 482))), LogFloatCap)`
- `prods2038Pr1b_Nb`:核心 `—`;评分 72,过线 0,入 heads 0;采样计数 {'c05_skeleton': 19}
  - score +0.48(train +0.75 valid +0.48):`cs_first_low20(day_last(Amt), LogFloatShares)`
  - score +0.48(train +0.75 valid +0.48):`cs_first_low20(cs_first_low20(day_last(Amt), LogFloatShares), LogFloatShares)`
  - score -0.09(train +0.02 valid -0.09):`cross_ema(cs_rank(cross_regbeta(day_last(Amt), cs_last_low10(day_autocorr_n1(Close), day_q_stat_std(Ret)), 10)), 60)`
  - score -0.18(train -0.18 valid +0.01):`cross_ema(cs_rank(cross_regbeta(day_last(Amt), day_open(Amt), 10)), 241)`
  - score -0.33(train -0.33 valid -0.27):`cs_first_low20(day_last(Amt), cs_first_low20(day_last(Amt), LogFloatShares))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.30(window ts_std@50->25):`ts_std(cross_quantile_q25(ts_std(day_autocorr_n1(Low), 50), 241), 25)`
