# 定位:种子 2007,P 组,第 3 轮(只含 train / valid)

快照:prods2007M1_I0_open_search, prods2007M2_I0_open_search, prods2007M3_I0_open_search, prods2007Pr1a_Ea, prods2007Pr1b_Nb, prods2007Pr2a_Ea, prods2007Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.39 | -0.39 | -0.10 | +1 | 5 | prods2007M2_I0_open_search | `abs_(ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 10), 40))` |
| -0.56 | -0.56 | -0.55 | +1 | 5 | prods2007M2_I0_open_search | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` |
| -0.58 | -0.58 | -0.49 | +1 | 5 | prods2007M2_I0_open_search | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1)), 5)` |
| -1.04 | -0.82 | -1.04 | +1 | 5 | prods2007M3_I0_open_search | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1)), 5)` |
| -1.07 | -1.07 | -0.63 | +1 | 5 | prods2007M1_I0_open_search | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` |
| -1.14 | -1.07 | -1.14 | +1 | 5 | prods2007M3_I0_open_search | `ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 40)` |
| -1.45 | -0.60 | -1.45 | +1 | 5 | prods2007M3_I0_open_search | `abs_(ts_std(ts_min(pow_3(day_durbin_watson(Open)), 1), 50))` |
| -2.06 | -2.06 | -1.72 | +1 | 0 | prods2007M1_I0_open_search | `cross_sum(day_durbin_watson(Close), 60)` |
| -3.13 | -3.13 | -2.71 | +1 | 20 | prods2007M1_I0_open_search | `log(day_durbin_watson(Vwap))` |

## 共性:307 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.70 | 0.009 | 4 | -0.63 / -2.33 | `day_close(in_kurt_full(Open))` |
| +1.52 | 0.004 | 4 | -0.81 / -2.33 | `ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40)` |
| +1.43 | 0.000 | 14 | -0.94 / -2.38 | `cross_stddev(ts_scale(day_sum(Amt), 30), 120)` |
| +1.34 | 0.000 | 10 | -1.01 / -2.36 | `ts_scale(ts_scale(day_sum(Amt), 30), 30)` |
| +1.34 | 0.005 | 5 | -0.99 / -2.33 | `cross_stddev(ts_scale(ts_scale(day_sum(Amt), 30), 30), 120)` |
| +1.25 | 0.022 | 5 | -1.08 / -2.33 | `day_close(in_kurt_full(Ret))` |
| +1.23 | 0.000 | 34 | -1.22 / -2.45 | `ts_scale(day_sum(Amt), 30)` |
| +1.15 | 0.000 | 44 | -1.33 / -2.48 | `day_sum(Amt)` |
| +1.12 | 0.007 | 7 | -1.21 / -2.34 | `ts_delay(day_close(in_kurt_full(Amt)), 1)` |
| +0.99 | 0.004 | 12 | -1.36 / -2.35 | `day_close(cross_decay_linear(Amt, 30))` |
| +0.97 | 0.002 | 14 | -1.38 / -2.36 | `sub(LogFloatCap, LogFloatShares)` |
| +0.97 | 0.013 | 6 | -1.36 / -2.33 | `day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3))` |
| +0.96 | 0.009 | 11 | -1.39 / -2.35 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |
| +0.86 | 0.069 | 5 | -1.47 / -2.33 | `ts_scale(day_sum(Amt), 10)` |
| +0.80 | 0.009 | 20 | -1.56 / -2.36 | `day_last(Close)` |
| +0.77 | 0.097 | 5 | -1.55 / -2.32 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` |
| +0.77 | 0.000 | 52 | -1.67 / -2.44 | `day_close(in_kurt_full(Amt))` |
| +0.76 | 0.086 | 6 | -1.57 / -2.33 | `day_sum(Vwap)` |
| +0.72 | 0.016 | 18 | -1.63 / -2.35 | `day_sum(Ret)` |
| +0.68 | 0.033 | 18 | -1.67 / -2.35 | `ts_delay(day_last(Close), 1)` |

## 拆解(33 次评估)

### head score -1.04:`cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1))` | -1.30 | -0.88 | -1.30 | — | (子树本身) |
| sufficiency | `ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1)` | -0.80 | -0.74 | -0.80 | — | (子树本身) |
| sufficiency | `pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50))` | -0.80 | -0.74 | -0.80 | — | (子树本身) |
| sufficiency | `ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)` | -0.80 | -0.74 | -0.80 | — | (子树本身) |
| knockout | `mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1))` | -2.28 | -2.28 | -2.19 | +1.24 | `cross_max(cross_max(cross_max(day_cov(Amt, Low), 5), 5), 5)` |
| knockout | `ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1)` | -1.04 | -0.82 | -1.04 | +0.01 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50))), 5)` |
| knockout | `pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50))` | -1.67 | -1.65 | -1.67 | +0.63 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), ts_min(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50), 1)), 5)` |
| knockout | `ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)` | -3.82 | -3.62 | -3.82 | +2.78 | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), ts_min(pow_3(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1))), 1)), 5)` |
| swap | `Amt->Volume` | -0.86 | -0.61 | -0.86 | — | `cross_max(mul(cross_max(cross_max(day_cov(Volume, Low), 5), 5), ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Volume)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1)), 5)` |
| swap | `Low->High` | -0.94 | -0.80 | -0.94 | — | `cross_max(mul(cross_max(cross_max(day_cov(Amt, High), 5), 5), ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1)), 5)` |
| window | `cross_max@5->2` | -1.18 | -0.89 | -1.18 | — | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1)), 2)` |
| window | `cross_max@5->10` | -0.93 | -0.82 | -0.93 | — | `cross_max(mul(cross_max(cross_max(day_cov(Amt, Low), 5), 5), ts_min(pow_3(ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 50)), 1)), 10)` |

### head score -1.14:`ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1))` | -4.16 | -3.37 | -4.16 | — | (子树本身) |
| sufficiency | `ts_min(pow_3(day_durbin_watson(Open)), 1)` | -4.18 | -4.18 | -3.92 | — | (子树本身) |
| sufficiency | `day_close(in_relative_distance_m(Amt))` | -3.83 | -2.95 | -3.83 | — | (子树本身) |
| sufficiency | `pow_3(day_durbin_watson(Open))` | -4.18 | -4.18 | -3.92 | — | (子树本身) |
| knockout | `mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1))` | -0.75 | -0.75 | -0.52 | -0.39 | `ts_std(day_close(in_relative_distance_m(Amt)), 40)` |
| knockout | `ts_min(pow_3(day_durbin_watson(Open)), 1)` | -1.16 | -1.07 | -1.16 | +0.03 | `ts_std(mul(day_close(in_relative_distance_m(Amt)), pow_3(day_durbin_watson(Open))), 40)` |
| knockout | `pow_3(day_durbin_watson(Open))` | -0.97 | -0.97 | -0.87 | -0.17 | `ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(day_durbin_watson(Open), 1)), 40)` |
| swap | `Amt->Volume` | -1.13 | -1.09 | -1.13 | — | `ts_std(mul(day_close(in_relative_distance_m(Volume)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 40)` |
| swap | `Open->Close` | -1.23 | -1.17 | -1.23 | — | `ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Close)), 1)), 40)` |
| window | `ts_std@40->20` | -2.71 | -2.71 | -2.16 | — | `ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 20)` |
| window | `ts_std@40->80` | -0.55 | -0.28 | -0.55 | — | `ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 80)` |

### head score -1.45:`abs_(ts_std(ts_min(pow_3(day_durbin_watson(Open)), 1), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(ts_min(pow_3(day_durbin_watson(Open)), 1), 50)` | -1.46 | -0.61 | -1.46 | — | (子树本身) |
| sufficiency | `ts_min(pow_3(day_durbin_watson(Open)), 1)` | -4.18 | -4.18 | -3.92 | — | (子树本身) |
| sufficiency | `pow_3(day_durbin_watson(Open))` | -4.18 | -4.18 | -3.92 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Open)` | -4.18 | -4.18 | -3.92 | — | (子树本身) |
| knockout | `ts_std(ts_min(pow_3(day_durbin_watson(Open)), 1), 50)` | -4.18 | -4.18 | -3.92 | +2.73 | `abs_(ts_min(pow_3(day_durbin_watson(Open)), 1))` |
| knockout | `ts_min(pow_3(day_durbin_watson(Open)), 1)` | -1.46 | -0.61 | -1.46 | +0.01 | `abs_(ts_std(pow_3(day_durbin_watson(Open)), 50))` |
| knockout | `pow_3(day_durbin_watson(Open))` | -1.66 | -0.88 | -1.66 | +0.21 | `abs_(ts_std(ts_min(day_durbin_watson(Open), 1), 50))` |
| swap | `Open->Close` | -1.32 | -0.83 | -1.32 | — | `abs_(ts_std(ts_min(pow_3(day_durbin_watson(Close)), 1), 50))` |
| window | `ts_std@50->25` | -2.63 | -1.98 | -2.63 | — | `abs_(ts_std(ts_min(pow_3(day_durbin_watson(Open)), 1), 25))` |
| window | `ts_std@50->100` | -1.23 | +0.24 | -1.23 | — | `abs_(ts_std(ts_min(pow_3(day_durbin_watson(Open)), 1), 100))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_close(in_kurt_full(Open))` — enrichment,均值差 +1.70,p 0.009
2. `ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40)` — enrichment,均值差 +1.52,p 0.004
3. `cross_stddev(ts_scale(day_sum(Amt), 30), 120)` — enrichment,均值差 +1.43,p 0.000
4. `ts_scale(ts_scale(day_sum(Amt), 30), 30)` — enrichment,均值差 +1.34,p 0.000
5. `cross_stddev(ts_scale(ts_scale(day_sum(Amt), 30), 30), 120)` — enrichment,均值差 +1.34,p 0.005
6. `day_close(in_kurt_full(Ret))` — enrichment,均值差 +1.25,p 0.022
7. `ts_scale(day_sum(Amt), 30)` — enrichment,均值差 +1.23,p 0.000
8. `day_sum(Amt)` — enrichment,均值差 +1.15,p 0.000
9. `ts_delay(day_close(in_kurt_full(Amt)), 1)` — enrichment,均值差 +1.12,p 0.007
10. `day_close(cross_decay_linear(Amt, 30))` — enrichment,均值差 +0.99,p 0.004
11. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.97,p 0.002
12. `day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3))` — enrichment,均值差 +0.97,p 0.013
13. `div(day_first(Open), ts_delay(day_last(Close), 1))` — enrichment,均值差 +0.96,p 0.009
14. `ts_scale(day_sum(Amt), 10)` — enrichment,均值差 +0.86,p 0.069
15. `day_last(Close)` — enrichment,均值差 +0.80,p 0.009
16. `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` — enrichment,均值差 +0.77,p 0.097
17. `day_close(in_kurt_full(Amt))` — enrichment,均值差 +0.77,p 0.000
18. `day_sum(Vwap)` — enrichment,均值差 +0.76,p 0.086
19. `day_sum(Ret)` — enrichment,均值差 +0.72,p 0.016
20. `ts_delay(day_last(Close), 1)` — enrichment,均值差 +0.68,p 0.033
21. `day_first(Open)` — enrichment,均值差 +0.58,p 0.035

## 本组之前各轮的任务

- `prods2007Pr1a_Ea`:核心 `ts_scale(day_durbin_watson(Vwap), 10)`;评分 86,过线 0,入 heads 0;采样计数 {'c05_no_core': 646, 'c05_skeleton': 318, 'c05_periphery_seen': 5, 'mutation_refused': 2}
  - score -0.70(train -0.05 valid -0.70):`cross_corr(ts_scale(day_durbin_watson(Vwap), 10), ts_scale(day_sum(Volume), 30), 60)`
  - score -0.70(train -0.70 valid -0.03):`cross_cov(ts_scale(day_durbin_watson(Vwap), 10), day_sum(Ret), 60)`
  - score -0.71(train -0.71 valid -0.46):`cross_corr(ts_scale(day_durbin_watson(Vwap), 10), day_sum(Ret), 60)`
  - score -0.77(train -0.13 valid -0.77):`cross_corr(ts_scale(day_durbin_watson(Vwap), 10), ts_scale(day_sum(Amt), 30), 60)`
  - score -0.78(train -0.61 valid -0.78):`cross_corr(ts_scale(day_durbin_watson(Vwap), 10), day_quantile_q25(Low), 60)`
- `prods2007Pr1b_Nb`:核心 `—`;评分 59,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.90(train -0.04 valid -0.90):`cross_corr(day_centroid(in_slice(Ret, 1, 240)), day_centroid(Amt), 60)`
  - score -1.07(train -0.11 valid -1.07):`cross_mean(cross_corr(day_centroid(in_slice(Ret, 1, 240)), day_centroid(Amt), 60), 40)`
  - score -1.65(train -1.65 valid -0.73):`cross_mean(sub(log(day_durbin_watson(in_slice(Vwap, 1, 120))), log(day_durbin_watson(in_slice(Vwap, 121, 240)))), 40)`
  - score -1.73(train -0.15 valid -1.73):`cross_corr(day_centroid(in_slice(Ret, 1, 240)), sub(div(day_first(Open), ts_delay(day_last(Open), 1)), 1), 60)`
  - score -1.73(train -0.14 valid -1.73):`cross_corr(day_centroid(in_slice(Ret, 1, 240)), sub(div(day_first(Open), ts_delay(day_last(Open), 1)), -1), 60)`
- `prods2007Pr2a_Ea`:核心 `day_close(in_kurt_full(Amt))`;评分 104,过线 0,入 heads 0;采样计数 {'c05_no_core': 1656, 'c05_skeleton': 857, 'c05_periphery_seen': 10}
  - score +0.37(train +0.37 valid +0.64):`cross_corr(day_close(in_kurt_full(Amt)), abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 241)`
  - score +0.20(train +0.82 valid +0.20):`cross_corr(day_close(in_kurt_full(Amt)), abs_(sub(ts_delay(day_close(in_kurt_full(Open)), 1), 1)), 241)`
  - score -0.04(train +0.37 valid -0.04):`cross_corr(day_close(in_kurt_full(Amt)), ts_delay(day_close(in_kurt_full(Ret)), 1), 120)`
  - score -0.07(train -0.07 valid -0.07):`cross_corr(day_close(in_kurt_full(Amt)), abs_(sub(div(day_first(Open), ts_delay(day_last(Close), 40)), 1)), 241)`
  - score -0.08(train -0.08 valid -0.08):`cross_corr(day_close(in_kurt_full(Amt)), abs_(sub(div(day_first(Open), ts_delay(day_first(Open), 40)), 1)), 241)`
- `prods2007Pr2b_Nb`:核心 `—`;评分 82,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score +0.14(train +0.14 valid +0.26):`cs_bucket_zscore(cross_stddev(cs_bucket_zscore(cross_stddev(ts_scale(day_sum(Amt), 30), 120), sub(LogFloatCap, LogFloatShares)), 120), sub(LogFloatCap, LogFloatShares))`
  - score -0.48(train +0.57 valid -0.48):`cs_bucket_zscore(cross_stddev(ts_scale(ts_scale(day_sum(Amt), 30), 30), 120), sub(LogFloatCap, LogFloatShares))`
  - score -0.49(train +0.81 valid -0.49):`cs_bucket_zscore(cross_stddev(ts_scale(day_sum(Amt), 30), 120), sub(LogFloatCap, LogFloatShares))`
  - score -0.67(train +0.74 valid -0.67):`cross_stddev(ts_scale(day_sum(Amt), 30), 120)`
  - score -0.70(train +0.23 valid -0.70):`cs_bucket_zscore(cross_stddev(ts_scale(day_sum(Amt), 30), 120), sub(cross_stddev(ts_scale(day_sum(Amt), 30), 120), LogFloatShares))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.59(window ts_std@40->80):`ts_std(mul(day_close(in_relative_distance_m(Amt)), ts_min(pow_3(day_durbin_watson(Open)), 1)), 80)`
- 增益 +0.22(window ts_std@50->100):`abs_(ts_std(ts_min(pow_3(day_durbin_watson(Open)), 1), 100))`
- 增益 +0.13(swap Open->Close):`abs_(ts_std(ts_min(pow_3(day_durbin_watson(Close)), 1), 50))`
