# 定位:种子 807,B 组,第 2 轮(只含 train / valid)

快照:c05s807M1_I0_open_search, c05s807M2_I0_open_search, c05s807Br1a_Ea, c05s807Br1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(12 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.78 | +2.45 | +1.78 | +1 | 0 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 241)` |
| +1.78 | +1.78 | +2.69 | -1 | 20 | c05s807M2_I0_open_search | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)` |
| +1.75 | +1.76 | +1.75 | -1 | 0 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 60)` |
| +1.71 | +1.71 | +2.50 | -1 | 20 | c05s807M1_I0_open_search | `pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 5)))` |
| +1.21 | +1.21 | +1.60 | -1 | 5 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)` |
| +1.10 | +1.10 | +2.05 | -1 | 0 | c05s807M2_I0_open_search | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` |
| +1.00 | +1.00 | +2.71 | +1 | 20 | c05s807Br1a_Ea | `cross_corr(pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret)))), day_flat_ratio(Ret), 20)` |
| +0.71 | +2.02 | +0.71 | +1 | 20 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret))))), 20)` |
| +0.68 | +0.68 | +1.62 | -1 | 20 | c05s807Br1b_Nb | `pow_2(pow_2(pow_2(day_topw_mean(Ret, Amt))))` |
| +0.67 | +0.67 | +1.17 | +1 | 20 | c05s807Br1a_Ea | `cross_corr(pow_2(day_signed_ratio(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)` |
| +0.61 | +0.82 | +0.61 | -1 | 5 | c05s807Br1a_Ea | `cross_corr(pow_2(day_wmean(Ret, Low)), pow_2(day_wmean(Ret, Ret)), 20)` |
| +0.52 | +0.52 | +0.84 | +1 | 0 | c05s807M2_I0_open_search | `ts_sum(LogFloatShares, 30)` |

## 共性:279 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.67 | 0.000 | 16 | +0.84 / -0.83 | `ts_sum(pow_3(day_durbin_watson(High)), 1)` |
| +1.64 | 0.000 | 7 | +0.86 / -0.77 | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` |
| +1.52 | 0.000 | 30 | +0.62 / -0.90 | `pow_3(day_durbin_watson(High))` |
| +1.40 | 0.012 | 4 | +0.64 / -0.75 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` |
| +1.28 | 0.000 | 57 | +0.29 / -1.00 | `day_durbin_watson(High)` |
| +1.26 | 0.001 | 12 | +0.47 / -0.79 | `pow_2_5(LogFloatShares)` |
| +1.25 | 0.023 | 4 | +0.50 / -0.75 | `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` |
| +1.23 | 0.018 | 6 | +0.47 / -0.76 | `cross_fangzheng(pow_2_5(LogFloatShares), 60)` |
| +1.23 | 0.033 | 4 | +0.48 / -0.75 | `pow_3(pow_2_5(LogFloatShares))` |
| +1.19 | 0.013 | 7 | +0.42 / -0.76 | `pow_2(pow_2(day_wmean(Ret, Ret)))` |
| +1.14 | 0.002 | 12 | +0.36 / -0.78 | `cross_stddev(day_durbin_watson(High), 60)` |
| +0.64 | 0.001 | 55 | -0.22 / -0.86 | `day_wmean(Ret, Ret)` |
| +0.60 | 0.071 | 6 | -0.15 / -0.75 | `pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret))))` |
| +0.57 | 0.002 | 48 | -0.26 / -0.83 | `pow_2(day_wmean(Ret, Ret))` |
| +0.32 | 0.177 | 7 | -0.42 / -0.74 | `cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret)))` |
| +0.18 | 0.396 | 7 | -0.56 / -0.74 | `day_flat_ratio(Close)` |
| +0.17 | 0.515 | 10 | -0.57 / -0.74 | `ts_cov(day_median(Vwap), day_var(Ret), 20)` |
| +0.09 | 0.621 | 13 | -0.65 / -0.74 | `day_var(Ret)` |
| -0.02 | 0.711 | 14 | -0.76 / -0.73 | `day_median(Vwap)` |
| -0.08 | 0.708 | 7 | -0.81 / -0.73 | `day_quantile_q75(Volume)` |

## 拆解(29 次评估)

### head score +1.78:`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(pow_2(day_wmean(Ret, Ret)))` | +1.18 | +1.18 | +1.35 | — | (子树本身) |
| sufficiency | `pow_2(day_wmean(Ret, Ret))` | +0.89 | +0.89 | +1.66 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Ret)` | -0.19 | -0.15 | -0.19 | — | (子树本身) |
| knockout | `pow_2(pow_2(day_wmean(Ret, Ret)))` | +1.09 | +1.09 | +1.25 | +0.69 | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 241)` |
| knockout | `pow_2(day_wmean(Ret, Ret))` | -0.27 | +0.04 | -0.27 | +2.05 | `cross_corr(day_wmean(Ret, Ret), pow_2(pow_2(day_wmean(Ret, Ret))), 241)` |
| window | `cross_corr@241->120` | +1.22 | +1.22 | +1.89 | — | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 120)` |
| window | `cross_corr@241->482` | +0.16 | +0.30 | +0.16 | — | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 482)` |

### head score +1.78:`ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` | +1.78 | +1.78 | +2.66 | — | (子树本身) |
| sufficiency | `ts_sum(pow_3(day_durbin_watson(High)), 1)` | +0.96 | +0.96 | +2.64 | — | (子树本身) |
| sufficiency | `pow_3(day_durbin_watson(High))` | +0.96 | +0.96 | +2.64 | — | (子树本身) |
| sufficiency | `day_durbin_watson(High)` | -1.17 | -1.17 | +0.58 | — | (子树本身) |
| knockout | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` | +0.96 | +0.96 | +2.64 | +0.81 | `ts_sum(ts_sum(pow_3(day_durbin_watson(High)), 1), 1)` |
| knockout | `ts_sum(pow_3(day_durbin_watson(High)), 1)` | +1.78 | +1.78 | +2.67 | -0.00 | `ts_sum(pow_2_5(pow_3(day_durbin_watson(High))), 1)` |
| knockout | `pow_3(day_durbin_watson(High))` | +0.72 | +0.72 | +2.36 | +1.06 | `ts_sum(pow_2_5(ts_sum(day_durbin_watson(High), 1)), 1)` |
| swap | `High->Low` | +1.54 | +1.54 | +2.77 | — | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(Low)), 1)), 1)` |
| window | `ts_sum@1->2` | +1.90 | +1.90 | +2.69 | — | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 2)` |

### head score +1.75:`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(pow_2(day_wmean(Ret, Ret)))` | +1.18 | +1.18 | +1.35 | — | (子树本身) |
| sufficiency | `pow_2(day_wmean(Ret, Ret))` | +0.89 | +0.89 | +1.66 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Ret)` | -0.19 | -0.15 | -0.19 | — | (子树本身) |
| knockout | `pow_2(pow_2(day_wmean(Ret, Ret)))` | +0.88 | +0.99 | +0.88 | +0.87 | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 60)` |
| knockout | `pow_2(day_wmean(Ret, Ret))` | +0.19 | +0.26 | +0.19 | +1.56 | `cross_corr(day_wmean(Ret, Ret), pow_2(pow_2(day_wmean(Ret, Ret))), 60)` |
| window | `cross_corr@60->30` | +0.84 | +0.84 | +1.02 | — | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 30)` |
| window | `cross_corr@60->120` | +1.22 | +1.22 | +1.89 | — | `cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 120)` |

### head score +1.71:`pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 5)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(cross_mean(day_wmean(Ret, Ret), 5))` | +1.05 | +1.05 | +1.94 | — | (子树本身) |
| sufficiency | `cross_mean(day_wmean(Ret, Ret), 5)` | +0.15 | +0.15 | +0.30 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Ret)` | -0.19 | -0.15 | -0.19 | — | (子树本身) |
| knockout | `cross_mean(day_wmean(Ret, Ret), 5)` | +1.18 | +1.18 | +1.35 | +0.53 | `pow_2(pow_2(day_wmean(Ret, Ret)))` |
| window | `cross_mean@5->2` | +1.49 | +1.49 | +1.98 | — | `pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 2)))` |
| window | `cross_mean@5->10` | +1.40 | +1.40 | +2.49 | — | `pow_2(pow_2(cross_mean(day_wmean(Ret, Ret), 10)))` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` — ablation,自身 score +1.78(所在 head +1.78)
2. `pow_2(pow_2(day_wmean(Ret, Ret)))` — ablation,自身 score +1.18(所在 head +1.78)
3. `pow_2(cross_mean(day_wmean(Ret, Ret), 5))` — ablation,自身 score +1.05(所在 head +1.71)
4. `ts_sum(pow_3(day_durbin_watson(High)), 1)` — enrichment,均值差 +1.67,p 0.000
5. `pow_3(day_durbin_watson(High))` — enrichment,均值差 +1.52,p 0.000
6. `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` — enrichment,均值差 +1.40,p 0.012
7. `day_durbin_watson(High)` — enrichment,均值差 +1.28,p 0.000
8. `pow_2_5(LogFloatShares)` — enrichment,均值差 +1.26,p 0.001
9. `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` — enrichment,均值差 +1.25,p 0.023
10. `cross_fangzheng(pow_2_5(LogFloatShares), 60)` — enrichment,均值差 +1.23,p 0.018
11. `pow_3(pow_2_5(LogFloatShares))` — enrichment,均值差 +1.23,p 0.033
12. `cross_stddev(day_durbin_watson(High), 60)` — enrichment,均值差 +1.14,p 0.002
13. `day_wmean(Ret, Ret)` — enrichment,均值差 +0.64,p 0.001
14. `pow_2(cs_mask_top_replace_mean_neg(pow_2(day_wmean(Ret, Ret))))` — enrichment,均值差 +0.60,p 0.071
15. `pow_2(day_wmean(Ret, Ret))` — enrichment,均值差 +0.57,p 0.002

## 本组之前各轮的任务

- `c05s807Br1a_Ea`:核心 `pow_2(day_wmean(Ret, Ret))`;评分 76,过线 13,入 heads 7;采样计数 {'c05_no_core': 2452, 'c05_skeleton': 3, 'c05_periphery_seen': 13}
  - score +1.78(train +2.45 valid +1.78):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 241)`
  - score +1.75(train +1.76 valid +1.75):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 60)`
  - score +1.64(train +1.64 valid +1.74):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 60)`
  - score +1.57(train +1.57 valid +2.53):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(pow_2(day_wmean(Ret, Ret))), 20)`
  - score +1.21(train +1.21 valid +1.60):`cross_corr(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(Ret, Ret)), 20)`
- `c05s807Br1b_Nb`:核心 `—`;评分 66,过线 1,入 heads 1;采样计数 {}
  - score +0.68(train +0.68 valid +1.62):`pow_2(pow_2(pow_2(day_topw_mean(Ret, Amt))))`
  - score +0.26(train +0.26 valid +0.36):`pow_2(pow_2(day_mean(Ret)))`
  - score +0.14(train +0.14 valid +0.86):`pow_2(pow_2(day_topw_mean(Ret, Amt)))`
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(cross_quantile_q75(cs_rank(day_mean(Ret)), 241), 10)`
  - score -0.30(train -0.30 valid +0.57):`pow_2(day_topw_mean(Ret, Amt))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(window ts_sum@1->2):`ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 2)`
