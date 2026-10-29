# 定位:种子 802,B 组,第 3 轮(只含 train / valid)

快照:c05s802M1_I0_open_search, c05s802M2_I0_open_search, c05s802M3_I0_open_search, c05s802Br1a_Ea, c05s802Br1b_Nb, c05s802Br2a_Ea, c05s802Br2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(23 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.67 | +1.67 | +2.26 | -1 | 5 | c05s802Br1b_Nb | `cross_mean(day_mean(in_logchg(Volume, 60)), 20)` |
| +1.45 | +1.45 | +3.20 | -1 | 20 | c05s802M2_I0_open_search | `pow_2(pow_2_5(day_durbin_watson(High)))` |
| +1.34 | +1.34 | +3.26 | -1 | 20 | c05s802M3_I0_open_search | `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 3)` |
| +1.29 | +1.29 | +1.56 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_high10(signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))), day_max(Volume))` |
| +1.23 | +1.23 | +1.24 | -1 | 20 | c05s802Br2b_Nb | `div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60))` |
| +1.16 | +1.16 | +1.66 | +1 | 5 | c05s802M1_I0_open_search | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))` |
| +1.14 | +1.14 | +2.70 | +1 | 20 | c05s802M1_I0_open_search | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 40))` |
| +1.09 | +1.09 | +1.25 | +1 | 5 | c05s802M2_I0_open_search | `cs_last_high10(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3), day_gini(Volume))` |
| +1.07 | +1.07 | +2.01 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))` |
| +1.03 | +1.03 | +2.76 | +1 | 5 | c05s802M2_I0_open_search | `cs_last_high10(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), day_gini(Volume))` |
| +0.96 | +0.96 | +2.43 | +1 | 20 | c05s802M1_I0_open_search | `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 40))` |
| +0.90 | +0.90 | +1.81 | -1 | 5 | c05s802M3_I0_open_search | `cross_cov(day_max(Ret), day_cov(Ret, Ret), 30)` |
| +0.89 | +0.89 | +2.97 | +1 | 20 | c05s802M1_I0_open_search | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))` |
| +0.86 | +0.86 | +1.42 | +1 | 20 | c05s802M2_I0_open_search | `cs_last_high10(cs_last_high10(LogFloatShares, day_durbin_watson(High)), day_durbin_watson(Vwap))` |
| +0.83 | +1.09 | +0.83 | -1 | 5 | c05s802M1_I0_open_search | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))` |
| +0.72 | +0.72 | +1.45 | -1 | 5 | c05s802Br1b_Nb | `cross_mean(div(div(day_last(Amt), day_sum(Volume)), day_sum(High)), 20)` |
| +0.67 | +0.67 | +1.36 | -1 | 20 | c05s802M3_I0_open_search | `cross_cov(day_wmean(Ret, Ret), day_wmean(Ret, Ret), 5)` |
| +0.66 | +0.66 | +2.02 | -1 | 5 | c05s802Br1b_Nb | `cross_mean(day_mean(in_scale_rolling(Volume, 60)), 20)` |
| +0.61 | +0.61 | +1.17 | -1 | 20 | c05s802Br2b_Nb | `div(cross_tail_mean_q75(day_std(Ret), 20), cross_mean(day_std(Ret), 20))` |
| +0.56 | +0.56 | +0.82 | +1 | 5 | c05s802M2_I0_open_search | `cross_quantile_q25(cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open))), 241)` |
| +0.54 | +0.54 | +1.26 | +1 | 20 | c05s802M1_I0_open_search | `day_mean(neg(in_delta(Volume, 60)))` |
| +0.52 | +0.52 | +0.55 | -1 | 0 | c05s802Br1b_Nb | `cross_mean(cross_mean(div(div(day_last(Amt), day_sum(Volume)), day_sum(Volume)), 3), 20)` |
| +0.51 | +0.51 | +0.93 | -1 | 0 | c05s802Br1b_Nb | `cross_mean(cross_mean(div(day_last(Amt), day_sum(Amt)), 20), 20)` |

## 共性:458 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.64 | 0.000 | 8 | +0.60 / -1.03 | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` |
| +1.56 | 0.009 | 4 | +0.55 / -1.02 | `cross_valid_count(day_std(Ret), 60)` |
| +1.53 | 0.000 | 12 | +0.48 / -1.05 | `inv(LogFloatShares)` |
| +1.51 | 0.003 | 6 | +0.48 / -1.02 | `ts_decay_linear(inv(LogFloatShares), 40)` |
| +1.50 | 0.014 | 4 | +0.48 / -1.02 | `ts_decay_linear(LogFloatShares, 40)` |
| +1.45 | 0.000 | 12 | +0.40 / -1.04 | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` |
| +1.41 | 0.019 | 4 | +0.39 / -1.02 | `div(day_last(Amt), day_sum(Volume))` |
| +1.40 | 0.020 | 4 | +0.38 / -1.02 | `cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` |
| +1.38 | 0.002 | 8 | +0.35 / -1.03 | `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` |
| +1.36 | 0.001 | 10 | +0.32 / -1.03 | `day_kurt(Ret)` |
| +1.33 | 0.016 | 5 | +0.31 / -1.02 | `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` |
| +1.32 | 0.000 | 32 | +0.22 / -1.10 | `cross_quantile_q25(LogFloatShares, 241)` |
| +1.15 | 0.043 | 5 | +0.13 / -1.02 | `cross_decay_linear(LogFloatShares, 3)` |
| +1.15 | 0.006 | 10 | +0.12 / -1.03 | `sqrt(day_quantile_q25(Open))` |
| +1.13 | 0.009 | 9 | +0.10 / -1.03 | `day_last(Amt)` |
| +1.09 | 0.071 | 4 | +0.07 / -1.01 | `pow_2_5(cross_decay_linear(LogFloatShares, 3))` |
| +0.91 | 0.002 | 19 | -0.13 / -1.04 | `day_max(Volume)` |
| +0.88 | 0.008 | 12 | -0.14 / -1.03 | `day_durbin_watson(Vwap)` |
| +0.83 | 0.116 | 6 | -0.19 / -1.02 | `ts_argmin(cross_quantile_q25(LogFloatShares, 241), 40)` |
| +0.82 | 0.075 | 7 | -0.20 / -1.02 | `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 30)` |

## 拆解(27 次评估)

### head score +1.34:`cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_cov(day_max(Ret), day_cov(Ret, Ret), 3)` | +0.85 | +0.85 | +2.05 | — | (子树本身) |
| sufficiency | `day_max(Ret)` | -0.27 | -0.27 | +1.36 | — | (子树本身) |
| sufficiency | `day_cov(Ret, Ret)` | -1.55 | -1.55 | +0.13 | — | (子树本身) |
| knockout | `cross_cov(day_max(Ret), day_cov(Ret, Ret), 3)` | -1.96 | -1.96 | -0.88 | +3.31 | `cross_cov(day_max(Ret), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 3)` |
| knockout | `cross_cov(day_max(Ret), day_cov(Ret, Ret), 3)` | -1.96 | -1.96 | -0.88 | +3.31 | `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), day_max(Ret), 3)` |
| window | `cross_cov@3->2` | +1.41 | +1.41 | +3.20 | — | `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 2)` |
| window | `cross_cov@3->6` | +1.22 | +1.22 | +2.98 | — | `cross_cov(cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), cross_cov(day_max(Ret), day_cov(Ret, Ret), 3), 6)` |

### head score +1.23:`div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_valid_count(day_std(Ret), 60)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_kurt(Ret)` | +0.97 | +0.97 | +1.54 | — | (子树本身) |
| sufficiency | `day_std(Ret)` | -2.56 | -2.56 | -2.40 | — | (子树本身) |
| knockout | `cross_valid_count(day_std(Ret), 60)` | +0.21 | +0.21 | +1.59 | +1.03 | `div(day_kurt(Ret), day_std(Ret))` |
| window | `cross_valid_count@60->30` | +1.23 | +1.23 | +1.29 | — | `div(day_kurt(Ret), cross_valid_count(day_std(Ret), 30))` |
| window | `cross_valid_count@60->120` | +1.26 | +1.26 | +1.30 | — | `div(day_kurt(Ret), cross_valid_count(day_std(Ret), 120))` |

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

### head score +1.07:`cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Vwap))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q25(LogFloatShares, 241)` | +0.56 | +0.56 | +0.78 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -0.74 | -0.74 | +1.07 | — | (子树本身) |
| knockout | `cross_quantile_q25(LogFloatShares, 241)` | +0.82 | +0.82 | +1.91 | +0.25 | `cs_last_low20(LogFloatShares, day_durbin_watson(Vwap))` |
| swap | `Vwap->Close` | +0.66 | +0.66 | +2.04 | — | `cs_last_low20(cross_quantile_q25(LogFloatShares, 241), day_durbin_watson(Close))` |
| window | `cross_quantile_q25@241->120` | +1.01 | +1.01 | +1.91 | — | `cs_last_low20(cross_quantile_q25(LogFloatShares, 120), day_durbin_watson(Vwap))` |
| window | `cross_quantile_q25@241->482` | +0.98 | +0.98 | +2.05 | — | `cs_last_low20(cross_quantile_q25(LogFloatShares, 482), day_durbin_watson(Vwap))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_kurt(Ret)` — ablation,自身 score +0.97(所在 head +1.23)
2. `cross_cov(day_max(Ret), day_cov(Ret, Ret), 3)` — ablation,自身 score +0.85(所在 head +1.34)
3. `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` — enrichment,均值差 +1.64,p 0.000
4. `cross_valid_count(day_std(Ret), 60)` — enrichment,均值差 +1.56,p 0.009
5. `inv(LogFloatShares)` — enrichment,均值差 +1.53,p 0.000
6. `ts_decay_linear(inv(LogFloatShares), 40)` — enrichment,均值差 +1.51,p 0.003
7. `ts_decay_linear(LogFloatShares, 40)` — enrichment,均值差 +1.50,p 0.014
8. `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)` — enrichment,均值差 +1.45,p 0.000
9. `div(day_last(Amt), day_sum(Volume))` — enrichment,均值差 +1.41,p 0.019
10. `cs_bucket_zscore(day_quantile_q25(Open), sqrt(day_quantile_q25(Open)))` — enrichment,均值差 +1.40,p 0.020
11. `pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3))` — enrichment,均值差 +1.38,p 0.002
12. `signedpower(pow_2_5(cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 3)))` — enrichment,均值差 +1.33,p 0.016
13. `cross_quantile_q25(LogFloatShares, 241)` — enrichment,均值差 +1.32,p 0.000
14. `cross_decay_linear(LogFloatShares, 3)` — enrichment,均值差 +1.15,p 0.043
15. `sqrt(day_quantile_q25(Open))` — enrichment,均值差 +1.15,p 0.006
16. `day_last(Amt)` — enrichment,均值差 +1.13,p 0.009
17. `pow_2_5(cross_decay_linear(LogFloatShares, 3))` — enrichment,均值差 +1.09,p 0.071
18. `day_max(Volume)` — enrichment,均值差 +0.91,p 0.002
19. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.88,p 0.008
20. `cross_decay_linear(cross_quantile_q25(LogFloatShares, 241), 30)` — enrichment,均值差 +0.82,p 0.075
21. `log(day_mean(Low))` — enrichment,均值差 +0.73,p 0.086
22. `day_gini(Volume)` — enrichment,均值差 +0.72,p 0.051
23. `day_mean(Low)` — enrichment,均值差 +0.71,p 0.074
24. `day_durbin_watson(High)` — enrichment,均值差 +0.66,p 0.021
25. `day_cov(Ret, Ret)` — enrichment,均值差 +0.62,p 0.013
26. `day_quantile_q25(Open)` — enrichment,均值差 +0.61,p 0.040
27. `day_max(Ret)` — enrichment,均值差 +0.43,p 0.092

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
- `c05s802Br2a_Ea`:核心 `day_mean(in_logchg(Volume, 60))`;评分 84,过线 0,入 heads 0;采样计数 {'c05_no_core': 2209, 'c05_periphery_seen': 9, 'c05_skeleton': 1, 'mutation_refused': 6}
  - score +0.25(train +0.25 valid +0.55):`cross_corr(day_mean(in_logchg(Volume, 60)), day_mean(Low), 60)`
  - score +0.22(train +0.22 valid +0.50):`cross_corr(day_mean(in_logchg(Volume, 60)), log(log(day_mean(Open))), 60)`
  - score +0.19(train +0.19 valid +0.57):`cross_corr(day_mean(in_logchg(Volume, 60)), log(day_mean(Open)), 60)`
  - score +0.17(train +0.17 valid +2.41):`cross_corr(day_mean(in_logchg(Volume, 60)), day_open(cross_delta(Close, 3)), 60)`
  - score +0.16(train +0.16 valid +0.58):`cross_corr(day_mean(in_logchg(Volume, 60)), log(log(day_mean(Low))), 60)`
- `c05s802Br2b_Nb`:核心 `—`;评分 74,过线 6,入 heads 2;采样计数 {'c05_skeleton': 1}
  - score +1.23(train +1.23 valid +1.24):`div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60))`
  - score +1.21(train +1.21 valid +1.25):`div(day_kurt(Ret), cross_valid_count(day_kurt(Ret), 60))`
  - score +1.07(train +1.07 valid +1.38):`div(div(day_kurt(Ret), cross_valid_count(day_std(Ret), 60)), cross_valid_count(day_std(Ret), 60))`
  - score +0.97(train +0.97 valid +1.54):`day_kurt(Ret)`
  - score +0.61(train +0.61 valid +1.17):`div(cross_tail_mean_q75(day_std(Ret), 20), cross_mean(day_std(Ret), 20))`

## 比原 head 好的拆解变体(R 候选)

(没有)
