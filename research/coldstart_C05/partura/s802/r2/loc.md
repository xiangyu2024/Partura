# 定位:种子 802,B 组,第 2 轮(只含 train / valid)

快照:c05s802M1_I0_open_search, c05s802M2_I0_open_search, c05s802Br1a_Ea, c05s802Br1b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(18 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.67 | +1.67 | +2.26 | -1 | 5 | c05s802Br1b_Nb | `cross_mean(day_mean(in_logchg(Volume, 60)), 20)` |
| +1.45 | +1.45 | +3.20 | -1 | 20 | c05s802M2_I0_open_search | `pow_2(pow_2_5(day_durbin_watson(High)))` |
| +1.29 | +1.29 | +1.56 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Volume))` |
| +1.16 | +1.16 | +1.66 | +1 | 5 | c05s802M1_I0_open_search | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))` |
| +1.14 | +1.14 | +2.70 | +1 | 20 | c05s802M1_I0_open_search | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 40))` |
| +1.09 | +1.09 | +1.25 | +1 | 5 | c05s802M2_I0_open_search | `cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))` |
| +1.07 | +1.07 | +2.01 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))` |
| +1.03 | +1.03 | +2.76 | +1 | 5 | c05s802M2_I0_open_search | `cs_last_high10(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), day_gini(Volume))` |
| +0.96 | +0.96 | +2.43 | +1 | 20 | c05s802M1_I0_open_search | `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 40))` |
| +0.89 | +0.89 | +2.97 | +1 | 20 | c05s802M1_I0_open_search | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))` |
| +0.86 | +0.86 | +1.42 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_high10(cs_last_high10(LogFloatShares, day_durbin_watson(High)), day_durbin_watson(Vwap))` |
| +0.83 | +1.09 | +0.83 | -1 | 5 | c05s802M1_I0_open_search | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))` |
| +0.72 | +0.72 | +1.45 | -1 | 5 | c05s802Br1b_Nb | `cross_mean(div(div(day_last(Amt), day_sum(Volume)), day_sum(High)), 20)` |
| +0.66 | +0.66 | +2.02 | -1 | 5 | c05s802Br1b_Nb | `cross_mean(day_mean(in_scale_rolling(Volume, 60)), 20)` |
| +0.56 | +0.56 | +0.82 | +1 | 5 | c05s802M2_I0_open_search | `cross_quantile_q25(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), 241)` |
| +0.54 | +0.54 | +1.26 | +1 | 20 | c05s802M1_I0_open_search | `day_mean(neg(in_delta(Volume, 60)))` |
| +0.52 | +0.52 | +0.55 | -1 | 0 | c05s802Br1b_Nb | `cross_mean(cross_mean(div(div(day_last(Amt), day_sum(Volume)), day_sum(Volume)), 3), 20)` |
| +0.51 | +0.51 | +0.93 | -1 | 0 | c05s802Br1b_Nb | `cross_mean(cross_mean(div(day_last(Amt), day_sum(Amt)), 20), 20)` |

## 共性:281 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.49 | 0.000 | 8 | +0.60 / -0.89 | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` |
| +1.39 | 0.001 | 12 | +0.48 / -0.91 | `inv(LogFloatShares)` |
| +1.36 | 0.008 | 6 | +0.48 / -0.88 | `ts_decay_linear(inv(LogFloatShares), 40)` |
| +1.35 | 0.029 | 4 | +0.48 / -0.87 | `ts_decay_linear(LogFloatShares, 40)` |
| +1.31 | 0.000 | 12 | +0.40 / -0.90 | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` |
| +1.26 | 0.035 | 4 | +0.39 / -0.86 | `div(day_last(Amt), day_sum(Volume))` |
| +1.25 | 0.037 | 4 | +0.38 / -0.86 | `cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` |
| +1.23 | 0.006 | 8 | +0.35 / -0.88 | `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` |
| +1.21 | 0.000 | 32 | +0.22 / -0.98 | `cross_quantile_q25(LogFloatShares, 241)` |
| +1.18 | 0.034 | 5 | +0.31 / -0.87 | `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` |
| +1.00 | 0.020 | 10 | +0.12 / -0.88 | `sqrt(day_quantile_q25(Open))` |
| +1.00 | 0.117 | 5 | +0.13 / -0.86 | `cross_decay_linear(LogFloatShares, 3)` |
| +0.98 | 0.030 | 9 | +0.10 / -0.88 | `day_last(Amt)` |
| +0.94 | 0.023 | 8 | +0.07 / -0.87 | `day_gini(Volume)` |
| +0.93 | 0.162 | 4 | +0.07 / -0.86 | `pow_2_5(cross_decay_linear(LogFloatShares, 3))` |
| +0.91 | 0.002 | 18 | +0.01 / -0.91 | `day_max(Volume)` |
| +0.73 | 0.014 | 12 | -0.14 / -0.88 | `day_durbin_watson(Vwap)` |
| +0.68 | 0.254 | 6 | -0.19 / -0.86 | `ts_argmin(cross_quantile_q25(LogFloatShares, 241), 40)` |
| +0.66 | 0.138 | 7 | -0.20 / -0.86 | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 30)` |
| +0.51 | 0.068 | 20 | -0.37 / -0.88 | `day_durbin_watson(High)` |

## 拆解(31 次评估)

### head score +1.67:`cross_mean(day_mean(in_logchg(Volume, 60)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_mean(in_logchg(Volume, 60))` | +0.55 | +0.55 | +0.76 | — | (子树本身) |
| swap | `Volume->Amt` | +1.64 | +1.64 | +2.11 | — | `cross_mean(day_mean(in_logchg(Amt, 60)), 20)` |
| window | `cross_mean@20->10` | +1.44 | +1.47 | +1.44 | — | `cross_mean(day_mean(in_logchg(Volume, 60)), 10)` |
| window | `cross_mean@20->40` | +1.45 | +1.45 | +1.71 | — | `cross_mean(day_mean(in_logchg(Volume, 60)), 40)` |

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

## 机械核心卡(B0 按这个顺序取)

1. `pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))))` — ablation,自身 score +1.21(所在 head +1.16)
2. `inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))` — ablation,自身 score +1.20(所在 head +1.16)
3. `sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100)))))` — ablation,自身 score +1.15(所在 head +1.16)
4. `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))` — ablation,自身 score +0.89(所在 head +1.16)
5. `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` — enrichment,均值差 +1.49,p 0.000
6. `inv(LogFloatShares)` — enrichment,均值差 +1.39,p 0.001
7. `ts_decay_linear(inv(LogFloatShares), 40)` — enrichment,均值差 +1.36,p 0.008
8. `ts_decay_linear(LogFloatShares, 40)` — enrichment,均值差 +1.35,p 0.029
9. `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` — enrichment,均值差 +1.31,p 0.000
10. `div(day_last(Amt), day_sum(Volume))` — enrichment,均值差 +1.26,p 0.035
11. `cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` — enrichment,均值差 +1.25,p 0.037
12. `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` — enrichment,均值差 +1.23,p 0.006
13. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +1.21,p 0.000
14. `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` — enrichment,均值差 +1.18,p 0.034
15. `sqrt(day_quantile_q25(Open))` — enrichment,均值差 +1.00,p 0.020
16. `day_last(Amt)` — enrichment,均值差 +0.98,p 0.030
17. `day_gini(Volume)` — enrichment,均值差 +0.94,p 0.023
18. `day_max(Volume)` — enrichment,均值差 +0.91,p 0.002
19. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.73,p 0.014
20. `day_durbin_watson(High)` — enrichment,均值差 +0.51,p 0.068

## 本组之前各轮的任务

- `c05s802Br1a_Ea`:核心 `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))`;评分 92,过线 0,入 heads 0;采样计数 {'c05_no_core': 3012, 'c05_periphery_seen': 11, 'mutation_refused': 6}
  - score -0.14(train -0.14 valid +1.64):`mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_centroid(Volume))`
  - score -0.15(train -0.15 valid +0.49):`mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_centroid(Volume)), 50)), day_distinct_ratio(Volume))`
  - score -0.17(train -0.17 valid +1.19):`mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_distinct_ratio(Volume))`
  - score -0.81(train +0.13 valid -0.81):`ts_corr(mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_at_max_ratio(Vwap)), day_flat_run_max(Close), 60)`
  - score -0.86(train -0.47 valid -0.86):`ts_corr(mul(sigmoid(ts_corr(mul(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), day_at_max_ratio(Vwap)), day_flat_run_max(Close), 60)), day_at_max_ratio(Vwap)), day_flat_run_max(Close), 60)`
- `c05s802Br1b_Nb`:核心 `—`;评分 81,过线 8,入 heads 5;采样计数 {}
  - score +1.67(train +1.67 valid +2.26):`cross_mean(day_mean(in_logchg(Volume, 60)), 20)`
  - score +1.64(train +1.64 valid +2.11):`cross_mean(day_mean(in_logchg(Amt, 60)), 20)`
  - score +1.43(train +1.43 valid +2.20):`cross_mean(cross_mean(day_mean(in_logchg(Volume, 60)), 20), 20)`
  - score +0.72(train +0.72 valid +1.45):`cross_mean(div(div(day_last(Amt), day_sum(Volume)), day_sum(High)), 20)`
  - score +0.66(train +0.66 valid +2.02):`cross_mean(day_mean(in_scale_rolling(Volume, 60)), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(window ts_regbeta@100->200):`inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 200))))))))`
