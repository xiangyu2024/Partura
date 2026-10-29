# 定位:种子 802,C 组,第 2 轮(只含 train / valid)

快照:c05s802M1_I0_open_search, c05s802M2_I0_open_search, c06s802Cr1a_Ea, c06s802Cr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(16 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.45 | +1.45 | +3.20 | -1 | 20 | c05s802M2_I0_open_search | `pow_2(pow_2_5(day_durbin_watson(High)))` |
| +1.29 | +1.29 | +1.56 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Volume))` |
| +1.16 | +1.16 | +1.66 | +1 | 5 | c05s802M1_I0_open_search | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))` |
| +1.14 | +1.14 | +2.70 | +1 | 20 | c05s802M1_I0_open_search | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 40))` |
| +1.09 | +1.09 | +1.25 | +1 | 5 | c05s802M2_I0_open_search | `cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))` |
| +1.07 | +1.07 | +2.01 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))` |
| +1.05 | +1.05 | +1.25 | +1 | 0 | c05s802M1_I0_open_search | `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)), 40))` |
| +1.03 | +1.03 | +2.76 | +1 | 5 | c05s802M2_I0_open_search | `cs_last_high10(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), day_gini(Volume))` |
| +0.89 | +0.89 | +1.85 | +1 | 5 | c06s802Cr1b_Nb | `ts_decay_linear(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20), 40)` |
| +0.86 | +0.86 | +1.42 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_high10(cs_last_high10(LogFloatShares, day_durbin_watson(High)), day_durbin_watson(Vwap))` |
| +0.83 | +1.09 | +0.83 | -1 | 5 | c05s802M1_I0_open_search | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))` |
| +0.79 | +1.27 | +0.79 | -1 | 5 | c06s802Cr1a_Ea | `sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)), 60))` |
| +0.72 | +0.72 | +0.75 | -1 | 0 | c06s802Cr1a_Ea | `sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(sub(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)), day_durbin_watson(Volume), 50)), 60))` |
| +0.71 | +0.81 | +0.71 | +1 | 5 | c05s802M1_I0_open_search | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))` |
| +0.56 | +0.56 | +0.82 | +1 | 5 | c05s802M2_I0_open_search | `cross_quantile_q25(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), 241)` |
| +0.54 | +0.54 | +1.26 | +1 | 20 | c05s802M1_I0_open_search | `day_mean(neg(in_delta(Volume, 60)))` |

## 共性:300 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.20 | 0.000 | 12 | +0.48 / -0.72 | `inv(LogFloatShares)` |
| +1.18 | 0.005 | 6 | +0.48 / -0.69 | `ts_decay_linear(inv(LogFloatShares), 40)` |
| +1.17 | 0.021 | 4 | +0.48 / -0.68 | `ts_decay_linear(LogFloatShares, 40)` |
| +1.12 | 0.001 | 12 | +0.40 / -0.71 | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` |
| +1.11 | 0.001 | 10 | +0.41 / -0.71 | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` |
| +1.06 | 0.035 | 4 | +0.38 / -0.68 | `cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` |
| +1.04 | 0.008 | 8 | +0.35 / -0.70 | `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` |
| +1.00 | 0.000 | 32 | +0.22 / -0.77 | `cross_quantile_q25(LogFloatShares, 241)` |
| +1.00 | 0.041 | 5 | +0.31 / -0.69 | `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` |
| +0.86 | 0.058 | 5 | +0.18 / -0.68 | `ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)` |
| +0.82 | 0.103 | 5 | +0.13 / -0.68 | `cross_decay_linear(LogFloatShares, 3)` |
| +0.81 | 0.023 | 10 | +0.12 / -0.70 | `sqrt(day_quantile_q25(Open))` |
| +0.76 | 0.081 | 7 | +0.07 / -0.69 | `ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)` |
| +0.75 | 0.032 | 8 | +0.07 / -0.69 | `day_gini(Volume)` |
| +0.75 | 0.153 | 4 | +0.07 / -0.68 | `pow_2_5(cross_decay_linear(LogFloatShares, 3))` |
| +0.72 | 0.003 | 18 | +0.01 / -0.71 | `day_max(Volume)` |
| +0.69 | 0.151 | 4 | +0.02 / -0.68 | `ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)), 60)` |
| +0.69 | 0.151 | 4 | +0.02 / -0.68 | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))` |
| +0.59 | 0.009 | 13 | -0.11 / -0.69 | `day_durbin_watson(Vwap)` |
| +0.52 | 0.211 | 4 | -0.15 / -0.68 | `cs_regres(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_sum(Ret))` |

## 拆解(35 次评估)

### head score +1.45:`pow_2(pow_2_5(day_durbin_watson(High)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2_5(day_durbin_watson(High))` | +0.72 | +0.72 | +2.36 | — | (子树本身) |
| sufficiency | `day_durbin_watson(High)` | -1.17 | -1.17 | +0.58 | — | (子树本身) |
| knockout | `pow_2_5(day_durbin_watson(High))` | +0.27 | +0.27 | +1.96 | +1.18 | `pow_2(day_durbin_watson(High))` |
| swap | `High->Low` | +1.28 | +1.28 | +2.80 | — | `pow_2(pow_2_5(day_durbin_watson(Low)))` |

### head score +1.29:`cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Volume))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` | +0.56 | +0.56 | +0.78 | — | (子树本身) |
| sufficiency | `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` | +0.55 | +0.55 | +0.78 | — | (子树本身) |
| sufficiency | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` | +0.56 | +0.56 | +0.78 | — | (子树本身) |
| sufficiency | `cross_quantile_q25(LogFloatShares, 241)` | +0.56 | +0.56 | +0.78 | — | (子树本身) |
| knockout | `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` | +1.29 | +1.29 | +1.56 | +0.00 | `cs_last_high10(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)), day_max(Volume))` |
| knockout | `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` | +1.29 | +1.29 | +1.56 | +0.00 | `cs_last_high10(signedpower(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)), day_max(Volume))` |
| knockout | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` | +1.29 | +1.29 | +1.54 | +0.00 | `cs_last_high10(signedpower(pow_2_5(cross_quantile_q25(LogFloatShares, 241))), day_max(Volume))` |
| knockout | `cross_quantile_q25(LogFloatShares, 241)` | +1.14 | +1.14 | +1.68 | +0.15 | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(LogFloatShares, 3))), day_max(Volume))` |
| swap | `Volume->Amt` | -0.17 | -0.17 | +0.35 | — | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Amt))` |
| window | `cross_decay_linear@3->2` | +1.30 | +1.30 | +1.57 | — | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 2))), day_max(Volume))` |
| window | `cross_decay_linear@3->6` | +1.28 | +1.28 | +1.56 | — | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 6))), day_max(Volume))` |

### head score +1.16:`inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))` | +1.21 | +1.21 | +1.66 | — | (子树本身) |
| sufficiency | `inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))` | +1.20 | +1.20 | +1.69 | — | (子树本身) |
| sufficiency | `sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))` | +1.15 | +1.15 | +1.66 | — | (子树本身) |
| sufficiency | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))` | +0.89 | +0.89 | +2.97 | — | (子树本身) |
| knockout | `pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))` | +1.15 | +1.15 | +1.66 | +0.01 | `inv(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))` |
| knockout | `inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))` | +1.21 | +1.21 | +1.66 | -0.05 | `inv(pow_1_5(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))` |
| knockout | `sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))` | +0.81 | +0.81 | +2.44 | +0.35 | `inv(pow_1_5(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))` |
| knockout | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))` | +1.12 | +1.12 | +2.13 | +0.04 | `inv(pow_1_5(inv(sigmoid(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))` |
| swap | `Vwap->Close` | +1.01 | +1.01 | +2.65 | — | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Close), day_durbin_watson(Volume), 100))))))))` |
| swap | `Volume->Amt` | +1.09 | +1.09 | +1.73 | — | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 100))))))))` |
| window | `ts_regbeta@100->50` | +0.83 | +0.83 | +0.98 | — | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))))))` |
| window | `ts_regbeta@100->200` | +1.39 | +1.39 | +2.42 | — | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200))))))))` |

### head score +1.09:`cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` | +0.56 | +0.56 | +0.78 | — | (子树本身) |
| sufficiency | `cross_quantile_q25(LogFloatShares, 241)` | +0.56 | +0.56 | +0.78 | — | (子树本身) |
| sufficiency | `day_gini(Volume)` | -3.67 | -3.67 | -3.30 | — | (子树本身) |
| knockout | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` | +1.08 | +1.08 | +1.26 | +0.00 | `cs_last_high10(cross_quantile_q25(LogFloatShares, 241), day_gini(Volume))` |
| knockout | `cross_quantile_q25(LogFloatShares, 241)` | +1.02 | +1.02 | +1.26 | +0.07 | `cs_last_high10(cross_decay_linear(LogFloatShares, 3), day_gini(Volume))` |
| swap | `Volume->Amt` | +1.07 | +1.07 | +1.28 | — | `cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Amt))` |
| window | `cross_decay_linear@3->2` | +1.10 | +1.10 | +1.26 | — | `cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 2), day_gini(Volume))` |
| window | `cross_decay_linear@3->6` | +1.07 | +1.07 | +1.25 | — | `cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 6), day_gini(Volume))` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))` — ablation,自身 score +1.21(所在 head +1.16)
2. `inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))` — ablation,自身 score +1.20(所在 head +1.16)
3. `sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))` — ablation,自身 score +1.15(所在 head +1.16)
4. `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))` — ablation,自身 score +0.89(所在 head +1.16)
5. `inv(LogFloatShares)` — enrichment,均值差 +1.20,p 0.000
6. `ts_decay_linear(inv(LogFloatShares), 40)` — enrichment,均值差 +1.18,p 0.005
7. `ts_decay_linear(LogFloatShares, 40)` — enrichment,均值差 +1.17,p 0.021
8. `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` — enrichment,均值差 +1.12,p 0.001
9. `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` — enrichment,均值差 +1.11,p 0.001
10. `cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` — enrichment,均值差 +1.06,p 0.035
11. `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` — enrichment,均值差 +1.04,p 0.008
12. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +1.00,p 0.000
13. `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` — enrichment,均值差 +1.00,p 0.041
14. `ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)` — enrichment,均值差 +0.86,p 0.058
15. `sqrt(day_quantile_q25(Open))` — enrichment,均值差 +0.81,p 0.023
16. `ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)` — enrichment,均值差 +0.76,p 0.081
17. `day_gini(Volume)` — enrichment,均值差 +0.75,p 0.032
18. `day_max(Volume)` — enrichment,均值差 +0.72,p 0.003
19. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.59,p 0.009
20. `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` — enrichment,均值差 +0.34,p 0.062
21. `day_durbin_watson(Volume)` — enrichment,均值差 +0.33,p 0.079
22. `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` — enrichment,均值差 +0.31,p 0.096
23. `day_flat_run_max(Vwap)` — enrichment,均值差 +0.29,p 0.100

## 本组之前各轮的任务

- `c06s802Cr1a_Ea`:核心 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))`;评分 94,过线 2,入 heads 2;采样计数 {'c05_no_core': 2402, 'c05_periphery_seen': 6, 'mutation_refused': 2, 'c05_skeleton': 2}
  - score +0.79(train +1.27 valid +0.79):`sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)), 60))`
  - score +0.72(train +0.72 valid +0.75):`sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(sub(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)), day_durbin_watson(Volume), 50)), 60))`
  - score +0.42(train +0.42 valid +2.31):`sub(day_flat_run_max(Vwap), ts_decay_linear(sigmoid(ts_regbeta(sub(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 60)), day_durbin_watson(Volume), 50)), 60))`
  - score +0.34(train +1.21 valid +0.34):`sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 40)), 50)), 60))`
  - score +0.33(train +0.33 valid +0.73):`sub(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Vwap), 50)), 10), ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)), 60))`
- `c06s802Cr1b_Nb`:核心 `—`;评分 86,过线 5,入 heads 1;采样计数 {}
  - score +0.89(train +0.89 valid +1.85):`ts_decay_linear(ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20), 40)`
  - score +0.62(train +0.62 valid +2.63):`ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 40)`
  - score +0.62(train +0.62 valid +2.63):`ts_decay_linear(cs_regres(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_sum(Ret)), 40)`
  - score +0.52(train +0.52 valid +2.22):`ts_decay_linear(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), 20)`
  - score +0.52(train +0.52 valid +2.22):`ts_decay_linear(cs_regres(cs_regres(day_signed_ratio(Ret, Volume), day_sum(Ret)), day_sum(Ret)), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(window ts_regbeta@100->200):`inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200))))))))`
