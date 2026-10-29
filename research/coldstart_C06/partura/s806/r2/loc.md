# 定位:种子 806,C 组,第 2 轮(只含 train / valid)

快照:c05s806M1_I0_open_search, c05s806M2_I0_open_search, c06s806Cr1a_Ea, c06s806Cr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(8 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.78 | +2.05 | +1.78 | +1 | 20 | c05s806M2_I0_open_search | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))` |
| +1.40 | +1.40 | +3.15 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))` |
| +1.32 | +1.32 | +3.02 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))` |
| +1.22 | +1.22 | +1.34 | -1 | 5 | c05s806M2_I0_open_search | `sqrt(ts_quantile_q50(day_centroid(Amt), 20))` |
| +1.18 | +1.18 | +2.76 | +1 | 20 | c05s806M2_I0_open_search | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))` |
| +1.13 | +1.30 | +1.13 | +1 | 0 | c05s806M2_I0_open_search | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3))` |
| +0.82 | +0.82 | +1.29 | -1 | 20 | c05s806M2_I0_open_search | `cs_mask_top_replace_mean_neg(ts_quantile_q50(cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)), 10))` |
| +0.81 | +0.81 | +2.58 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(cs_normalize(day_open(Open)), cs_normalize(day_open(Open)))` |

## 共性:292 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.61 | 0.000 | 15 | +0.47 / -1.15 | `ts_quantile_q50(day_centroid(Amt), 10)` |
| +1.58 | 0.005 | 4 | +0.50 / -1.08 | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` |
| +1.41 | 0.002 | 9 | +0.31 / -1.11 | `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)` |
| +1.41 | 0.000 | 31 | +0.20 / -1.21 | `day_centroid(Amt)` |
| +1.38 | 0.001 | 12 | +0.26 / -1.12 | `log(day_open(Low))` |
| +1.36 | 0.009 | 5 | +0.27 / -1.09 | `cs_last_low40(LogFloatCap, day_quantile(Vwap))` |
| +1.27 | 0.024 | 7 | +0.18 / -1.09 | `day_quantile_q75(Amt)` |
| +1.26 | 0.001 | 16 | +0.13 / -1.13 | `day_open(Low)` |
| +1.21 | 0.026 | 4 | +0.13 / -1.08 | `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Vwap)), 3)` |
| +1.19 | 0.026 | 6 | +0.11 / -1.09 | `cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10))` |
| +1.18 | 0.005 | 10 | +0.08 / -1.10 | `day_quantile_q75(pow_2_5(Close))` |
| +0.95 | 0.005 | 20 | -0.18 / -1.13 | `day_open(Open)` |
| +0.74 | 0.113 | 10 | -0.34 / -1.09 | `cs_normalize(day_open(Open))` |
| +0.63 | 0.063 | 6 | -0.44 / -1.08 | `day_quantile(Vwap)` |
| +0.50 | 0.074 | 6 | -0.58 / -1.07 | `add(LimitWidth, add(LimitWidth, day_cov(Vwap, Ret)))` |
| +0.46 | 0.092 | 5 | -0.61 / -1.07 | `ts_min(add(LimitWidth, day_cov(Vwap, Ret)), 20)` |
| +0.42 | 0.012 | 18 | -0.67 / -1.09 | `add(LimitWidth, day_cov(Vwap, Ret))` |
| +0.28 | 0.061 | 19 | -0.80 / -1.08 | `add(LimitWidth, day_cov(High, Ret))` |
| +0.26 | 0.062 | 17 | -0.81 / -1.08 | `day_signed_ratio(Ret, Volume)` |
| +0.25 | 0.076 | 22 | -0.83 / -1.08 | `day_cov(High, Ret)` |

## 拆解(28 次评估)

### head score +1.78:`sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3)` | -2.08 | -0.49 | -2.08 | — | (子树本身) |
| sufficiency | `cs_last_low40(LogFloatCap, day_quantile_q75(Amt))` | -2.08 | -0.30 | -2.08 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Amt)` | -1.19 | -1.19 | +0.47 | — | (子树本身) |
| knockout | `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3)` | +2.11 | +2.11 | +2.39 | -0.33 | `sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))` |
| knockout | `cs_last_low40(LogFloatCap, day_quantile_q75(Amt))` | -3.01 | -1.93 | -3.01 | +4.80 | `sqrt(cross_quantile_q25(LogFloatCap, 3))` |
| swap | `Amt->Volume` | -0.03 | +1.33 | -0.03 | — | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Volume)), 3))` |
| window | `cross_quantile_q25@3->2` | +1.92 | +2.06 | +1.92 | — | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 2))` |
| window | `cross_quantile_q25@3->6` | +1.09 | +1.81 | +1.09 | — | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 6))` |

### head score +1.40:`cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(day_open(Open))` | -1.19 | -1.19 | -0.44 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Amt)` | -1.19 | -1.19 | +0.47 | — | (子树本身) |
| sufficiency | `day_open(Open)` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| knockout | `log(day_open(Open))` | +1.40 | +1.40 | +3.15 | -0.00 | `cs_first_low20(day_quantile_q75(Amt), day_open(Open))` |
| swap | `Amt->Volume` | +1.38 | +1.38 | +2.97 | — | `cs_first_low20(day_quantile_q75(Volume), log(day_open(Open)))` |
| swap | `Open->Close` | +1.39 | +1.39 | +3.15 | — | `cs_first_low20(day_quantile_q75(Amt), log(day_open(Close)))` |

### head score +1.32:`cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` | +0.45 | +0.45 | +1.51 | — | (子树本身) |
| sufficiency | `cs_normalize(day_open(Open))` | -1.15 | -1.15 | -0.47 | — | (子树本身) |
| sufficiency | `day_quantile_q75(pow_2_5(Close))` | -1.16 | -1.16 | -0.43 | — | (子树本身) |
| sufficiency | `day_open(Open)` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| knockout | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` | +0.87 | +0.87 | +2.65 | +0.45 | `cs_first_low20(cs_normalize(day_open(Open)), day_quantile_q75(pow_2_5(Close)))` |
| knockout | `cs_normalize(day_open(Open))` | +1.32 | +1.32 | +3.02 | -0.00 | `cs_first_low20(day_open(Open), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))` |
| swap | `Open->Close` | +1.32 | +1.32 | +3.02 | — | `cs_first_low20(cs_normalize(day_open(Close)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))` |
| swap | `Close->Vwap` | +1.29 | +1.29 | +3.01 | — | `cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Vwap))))` |

### head score +1.22:`sqrt(ts_quantile_q50(day_centroid(Amt), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q50(day_centroid(Amt), 20)` | +1.21 | +1.21 | +1.27 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | -0.08 | -0.08 | +0.58 | — | (子树本身) |
| knockout | `ts_quantile_q50(day_centroid(Amt), 20)` | -0.51 | -0.51 | +0.43 | +1.73 | `sqrt(day_centroid(Amt))` |
| swap | `Amt->Volume` | +1.21 | +1.25 | +1.21 | — | `sqrt(ts_quantile_q50(day_centroid(Volume), 20))` |
| window | `ts_quantile_q50@20->10` | +0.98 | +1.08 | +0.98 | — | `sqrt(ts_quantile_q50(day_centroid(Amt), 10))` |
| window | `ts_quantile_q50@20->40` | +1.22 | +1.22 | +1.35 | — | `sqrt(ts_quantile_q50(day_centroid(Amt), 40))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_quantile_q50(day_centroid(Amt), 20)` — ablation,自身 score +1.21(所在 head +1.22)
2. `ts_quantile_q50(day_centroid(Amt), 10)` — enrichment,均值差 +1.61,p 0.000
3. `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` — enrichment,均值差 +1.58,p 0.005
4. `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)` — enrichment,均值差 +1.41,p 0.002
5. `day_centroid(Amt)` — enrichment,均值差 +1.41,p 0.000
6. `log(day_open(Low))` — enrichment,均值差 +1.38,p 0.001
7. `cs_last_low40(LogFloatCap, day_quantile(Vwap))` — enrichment,均值差 +1.36,p 0.009
8. `day_quantile_q75(Amt)` — enrichment,均值差 +1.27,p 0.024
9. `day_open(Low)` — enrichment,均值差 +1.26,p 0.001
10. `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Vwap)), 3)` — enrichment,均值差 +1.21,p 0.026
11. `cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10))` — enrichment,均值差 +1.19,p 0.026
12. `day_quantile_q75(pow_2_5(Close))` — enrichment,均值差 +1.18,p 0.005
13. `day_open(Open)` — enrichment,均值差 +0.95,p 0.005
14. `day_quantile(Vwap)` — enrichment,均值差 +0.63,p 0.063
15. `add(LimitWidth, add(LimitWidth, day_cov(Vwap, Ret)))` — enrichment,均值差 +0.50,p 0.074
16. `ts_min(add(LimitWidth, day_cov(Vwap, Ret)), 20)` — enrichment,均值差 +0.46,p 0.092
17. `add(LimitWidth, day_cov(Vwap, Ret))` — enrichment,均值差 +0.42,p 0.012
18. `add(LimitWidth, day_cov(High, Ret))` — enrichment,均值差 +0.28,p 0.061
19. `day_signed_ratio(Ret, Volume)` — enrichment,均值差 +0.26,p 0.062
20. `day_cov(High, Ret)` — enrichment,均值差 +0.25,p 0.076

## 本组之前各轮的任务

- `c06s806Cr1a_Ea`:核心 `day_cov(Vwap, Ret)`;评分 77,过线 0,入 heads 0;采样计数 {'c05_no_core': 1616, 'c05_periphery_seen': 9}
  - score -0.09(train +0.10 valid -0.09):`ts_corr(day_cov(Vwap, Ret), cross_reg_fvalue(cross_autocorr_s1(day_cov(Vwap, Ret), 241), day_cov(Vwap, Ret), 3), 40)`
  - score -0.10(train -0.10 valid -0.05):`ts_corr(day_cov(Vwap, Ret), cross_reg_fvalue(day_q_stat_std(Low), day_cov(Vwap, Ret), 3), 40)`
  - score -0.36(train -0.36 valid +0.10):`inv(cross_autocorr_s1(day_cov(Vwap, Ret), 241))`
  - score -0.38(train -0.38 valid +0.63):`inv(cross_decay_linear(day_cov(Vwap, Ret), 10))`
  - score -0.40(train -0.40 valid +1.50):`inv(cross_decay_linear(day_cov(Vwap, Ret), 30))`
- `c06s806Cr1b_Nb`:核心 `—`;评分 62,过线 0,入 heads 0;采样计数 {}
  - score +0.12(train +0.12 valid +1.34):`cross_mean(sub(cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Amt, Ret)), 20), day_signed_ratio(Amt, Ret)), 20)`
  - score +0.06(train +0.06 valid +2.33):`cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), 60)`
  - score -0.12(train -0.12 valid +1.93):`cross_mean(sub(cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), 20), day_signed_ratio(Ret, Ret)), 20)`
  - score -0.13(train -0.13 valid +2.26):`cross_mean(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), 20)`
  - score -0.21(train -0.21 valid +2.31):`cross_mean(sub(sub(day_signed_ratio(Ret, Volume), day_signed_ratio(Ret, Ret)), day_signed_ratio(Ret, Ret)), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.33(knockout cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3)):`sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))`
- 增益 +0.14(window cross_quantile_q25@3->2):`sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 2))`
