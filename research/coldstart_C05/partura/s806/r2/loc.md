# 定位:种子 806,B 组,第 2 轮(只含 train / valid)

快照:c05s806M1_I0_open_search, c05s806M2_I0_open_search, c05s806Br1a_Ea, c05s806Br1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.78 | +2.05 | +1.78 | +1 | 20 | c05s806M2_I0_open_search | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3))` |
| +1.40 | +1.40 | +3.15 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(day_quantile_q75(Amt), log(day_open(Open)))` |
| +1.32 | +1.32 | +3.02 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(cs_normalize(day_open(Open)), cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close))))` |
| +1.22 | +1.22 | +1.34 | -1 | 5 | c05s806M2_I0_open_search | `sqrt(ts_quantile_q50(day_centroid(Amt), 20))` |
| +1.18 | +1.18 | +2.76 | +1 | 20 | c05s806M2_I0_open_search | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Amt)))` |
| +1.13 | +1.30 | +1.13 | +1 | 0 | c05s806M2_I0_open_search | `sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Low)), 3))` |
| +0.97 | +0.97 | +1.54 | -1 | 20 | c05s806Br1b_Nb | `day_kurt(Ret)` |
| +0.82 | +0.82 | +1.29 | -1 | 20 | c05s806M2_I0_open_search | `cs_mask_top_replace_mean_neg(ts_quantile_q50(cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)), 10))` |
| +0.81 | +0.81 | +2.58 | +1 | 5 | c05s806M2_I0_open_search | `cs_first_low20(cs_normalize(day_open(Open)), cs_normalize(day_open(Open)))` |

## 共性:293 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.59 | 0.000 | 15 | +0.47 / -1.12 | `ts_quantile_q50(day_centroid(Amt), 10)` |
| +1.56 | 0.008 | 4 | +0.50 / -1.06 | `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` |
| +1.47 | 0.012 | 4 | +0.41 / -1.06 | `cross_mean(day_kurt(Ret), 30)` |
| +1.39 | 0.002 | 9 | +0.31 / -1.08 | `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)` |
| +1.39 | 0.000 | 31 | +0.20 / -1.19 | `day_centroid(Amt)` |
| +1.36 | 0.001 | 12 | +0.26 / -1.10 | `log(day_open(Low))` |
| +1.33 | 0.010 | 5 | +0.27 / -1.06 | `cs_last_low40(LogFloatCap, day_quantile(Vwap))` |
| +1.25 | 0.022 | 7 | +0.18 / -1.07 | `day_quantile_q75(Amt)` |
| +1.23 | 0.001 | 16 | +0.13 / -1.11 | `day_open(Low)` |
| +1.19 | 0.029 | 4 | +0.13 / -1.06 | `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Vwap)), 3)` |
| +1.17 | 0.025 | 6 | +0.11 / -1.06 | `cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10))` |
| +1.16 | 0.006 | 10 | +0.08 / -1.08 | `day_quantile_q75(pow_2_5(Close))` |
| +0.93 | 0.006 | 9 | -0.14 / -1.07 | `day_kurt(Ret)` |
| +0.93 | 0.004 | 20 | -0.18 / -1.10 | `day_open(Open)` |
| +0.86 | 0.011 | 7 | -0.20 / -1.06 | `day_corr(in_index(Ret), Ret)` |
| +0.72 | 0.102 | 10 | -0.34 / -1.06 | `cs_normalize(day_open(Open))` |
| +0.61 | 0.069 | 6 | -0.44 / -1.05 | `day_quantile(Vwap)` |
| +0.47 | 0.098 | 6 | -0.58 / -1.05 | `add(LimitWidth, add(LimitWidth, day_cov(Vwap, Ret)))` |
| +0.44 | 0.122 | 5 | -0.61 / -1.05 | `ts_min(add(LimitWidth, day_cov(Vwap, Ret)), 20)` |
| +0.40 | 0.025 | 18 | -0.67 / -1.06 | `add(LimitWidth, day_cov(Vwap, Ret))` |

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
2. `ts_quantile_q50(day_centroid(Amt), 10)` — enrichment,均值差 +1.59,p 0.000
3. `cs_mask_top_replace_mean_neg(day_quantile_q75(pow_2_5(Close)))` — enrichment,均值差 +1.56,p 0.008
4. `cross_mean(day_kurt(Ret), 30)` — enrichment,均值差 +1.47,p 0.012
5. `ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10)` — enrichment,均值差 +1.39,p 0.002
6. `day_centroid(Amt)` — enrichment,均值差 +1.39,p 0.000
7. `log(day_open(Low))` — enrichment,均值差 +1.36,p 0.001
8. `cs_last_low40(LogFloatCap, day_quantile(Vwap))` — enrichment,均值差 +1.33,p 0.010
9. `day_quantile_q75(Amt)` — enrichment,均值差 +1.25,p 0.022
10. `day_open(Low)` — enrichment,均值差 +1.23,p 0.001
11. `cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile(Vwap)), 3)` — enrichment,均值差 +1.19,p 0.029
12. `cs_mask_top_replace_mean_neg(ts_quantile_q50(ts_quantile_q50(day_centroid(Amt), 10), 10))` — enrichment,均值差 +1.17,p 0.025
13. `day_quantile_q75(pow_2_5(Close))` — enrichment,均值差 +1.16,p 0.006
14. `day_kurt(Ret)` — enrichment,均值差 +0.93,p 0.006
15. `day_open(Open)` — enrichment,均值差 +0.93,p 0.004
16. `day_corr(in_index(Ret), Ret)` — enrichment,均值差 +0.86,p 0.011
17. `day_quantile(Vwap)` — enrichment,均值差 +0.61,p 0.069
18. `add(LimitWidth, add(LimitWidth, day_cov(Vwap, Ret)))` — enrichment,均值差 +0.47,p 0.098
19. `add(LimitWidth, day_cov(Vwap, Ret))` — enrichment,均值差 +0.40,p 0.025
20. `add(LimitWidth, day_cov(High, Ret))` — enrichment,均值差 +0.26,p 0.086

## 本组之前各轮的任务

- `c05s806Br1a_Ea`:核心 `day_cov(Vwap, Ret)`;评分 73,过线 0,入 heads 0;采样计数 {'c05_no_core': 1269, 'c05_periphery_seen': 8}
  - score +0.01(train +0.01 valid +0.19):`ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 40)`
  - score -0.25(train -0.25 valid +1.18):`inv(ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 20))`
  - score -0.30(train -0.30 valid +0.48):`inv(cross_decay_linear(ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 40), 241))`
  - score -0.36(train -0.36 valid +0.96):`inv(ts_corr(pow_2(day_cov(Vwap, Ret)), day_min(Close), 40))`
  - score -0.65(train -0.65 valid -0.00):`cs_last_low40(day_cov(Vwap, Ret), day_wmean(High, Vwap))`
- `c05s806Br1b_Nb`:核心 `—`;评分 68,过线 2,入 heads 1;采样计数 {}
  - score +0.97(train +0.97 valid +1.54):`day_kurt(Ret)`
  - score +0.61(train +0.61 valid +1.25):`cross_mean(day_kurt(Ret), 30)`
  - score +0.46(train +0.46 valid +2.03):`cross_mean(cross_mean(cross_ema(cross_mean(day_kurt(Ret), 20), 10), 20), 20)`
  - score +0.46(train +0.46 valid +1.99):`cross_mean(cross_mean(day_kurt(Ret), 30), 30)`
  - score +0.46(train +0.46 valid +1.89):`cross_mean(cross_mean(cross_mean(day_kurt(Ret), 30), 20), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.33(knockout cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 3)):`sqrt(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)))`
- 增益 +0.14(window cross_quantile_q25@3->2):`sqrt(cross_quantile_q25(cs_last_low40(LogFloatCap, day_quantile_q75(Amt)), 2))`
