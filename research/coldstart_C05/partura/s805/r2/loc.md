# 定位:种子 805,B 组,第 2 轮(只含 train / valid)

快照:c05s805M1_I0_open_search, c05s805M2_I0_open_search, c05s805Br1a_Ea, c05s805Br1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.55 | +1.55 | +2.11 | -1 | 5 | c05s805Br1a_Ea | `cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))` |
| +0.91 | +0.91 | +1.16 | +1 | 20 | c05s805Br1a_Ea | `cs_last_high20(LogFloatShares, day_centroid(Volume))` |
| +0.84 | +0.84 | +2.20 | -1 | 5 | c05s805M2_I0_open_search | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| +0.83 | +0.83 | +1.24 | -1 | 5 | c05s805Br1a_Ea | `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 20)` |
| +0.81 | +0.81 | +2.58 | -1 | 5 | c05s805M2_I0_open_search | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| +0.64 | +1.01 | +0.64 | -1 | 20 | c05s805M2_I0_open_search | `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), ts_argmax(day_first(High), 1))` |
| +0.58 | +0.58 | +0.66 | -1 | 20 | c05s805M2_I0_open_search | `cs_last_low20(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), ts_argmax(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), 20))` |
| +0.53 | +0.53 | +0.96 | +1 | 5 | c05s805Br1b_Nb | `cross_mean(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 3), 20)` |
| +0.53 | +0.97 | +0.53 | -1 | 20 | c05s805Br1a_Ea | `cs_bucket_zscore(cross_mean(cross_mean(sub(day_centroid(Volume), pow_3(day_centroid(Volume))), 20), 20), day_centroid(Ret))` |

## 共性:303 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.87 | 0.001 | 4 | +1.15 / -0.72 | `cross_mean(day_flat_ratio(Close), 20)` |
| +1.78 | 0.000 | 7 | +1.04 / -0.74 | `day_flat_ratio(Close)` |
| +1.34 | 0.001 | 7 | +0.62 / -0.73 | `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` |
| +1.31 | 0.000 | 53 | +0.38 / -0.92 | `sub(day_pos_ratio(High), LogFloatShares)` |
| +1.30 | 0.005 | 5 | +0.58 / -0.72 | `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` |
| +1.26 | 0.011 | 4 | +0.55 / -0.71 | `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)` |
| +1.21 | 0.025 | 4 | +0.50 / -0.71 | `day_first(abs_(sub(1, Open)))` |
| +1.21 | 0.025 | 4 | +0.50 / -0.71 | `ts_argmax(day_first(abs_(sub(1, Open))), 1)` |
| +1.19 | 0.000 | 28 | +0.39 / -0.80 | `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` |
| +1.18 | 0.000 | 70 | +0.21 / -0.97 | `day_pos_ratio(High)` |
| +1.05 | 0.000 | 22 | +0.28 / -0.77 | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` |
| +1.03 | 0.038 | 8 | +0.31 / -0.72 | `cross_mean(day_corr(Ret, Volume), 20)` |
| +1.02 | 0.017 | 7 | +0.30 / -0.72 | `cs_mean(day_distinct_ratio(Close))` |
| +0.99 | 0.000 | 52 | +0.12 / -0.86 | `day_first(High)` |
| +0.98 | 0.000 | 27 | +0.20 / -0.78 | `day_first(abs_(sub(-1, Open)))` |
| +0.93 | 0.000 | 30 | +0.14 / -0.79 | `ts_argmax(day_first(High), 1)` |
| +0.92 | 0.136 | 5 | +0.21 / -0.71 | `cross_mean(cross_mean(day_corr(Ret, Volume), 20), 20)` |
| +0.79 | 0.167 | 8 | +0.08 / -0.72 | `pow_1_5(day_centroid(Volume))` |
| +0.77 | 0.004 | 13 | +0.04 / -0.73 | `day_centroid(Ret)` |
| +0.77 | 0.184 | 20 | +0.02 / -0.74 | `pow_2_5(day_centroid(Volume))` |

## 拆解(26 次评估)

### head score +1.55:`cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_centroid(Volume), 20)` | +1.24 | +1.24 | +1.72 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | -0.09 | -0.09 | +0.54 | — | (子树本身) |
| sufficiency | `day_centroid(Ret)` | -1.38 | -1.38 | -0.48 | — | (子树本身) |
| knockout | `cross_mean(day_centroid(Volume), 20)` | +0.71 | +0.71 | +1.57 | +0.83 | `cs_bucket_zscore(day_centroid(Volume), day_centroid(Ret))` |
| swap | `Volume->Amt` | +1.50 | +1.50 | +2.09 | — | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), day_centroid(Ret))` |
| window | `cross_mean@20->10` | +1.52 | +1.52 | +2.10 | — | `cs_bucket_zscore(cross_mean(day_centroid(Volume), 10), day_centroid(Ret))` |
| window | `cross_mean@20->40` | +1.25 | +1.25 | +1.91 | — | `cs_bucket_zscore(cross_mean(day_centroid(Volume), 40), day_centroid(Ret))` |

### head score +0.91:`cs_last_high20(LogFloatShares, day_centroid(Volume))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Volume)` | -0.09 | -0.09 | +0.54 | — | (子树本身) |
| swap | `Volume->Amt` | +0.87 | +0.87 | +1.20 | — | `cs_last_high20(LogFloatShares, day_centroid(Amt))` |

### head score +0.84:`cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` | +0.80 | +0.80 | +1.99 | — | (子树本身) |
| sufficiency | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` | — | — | — | — | 门槛废品 |
| sufficiency | `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` | +0.48 | +0.48 | +0.77 | — | (子树本身) |
| sufficiency | `day_first(abs_(sub(-1, Open)))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| knockout | `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` | +0.48 | +0.48 | +0.77 | +0.36 | `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| knockout | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` | +0.82 | +0.82 | +1.89 | +0.02 | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), day_first(abs_(sub(-1, Open))))` |
| knockout | `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` | +0.84 | +0.84 | +2.20 | -0.00 | `cs_last_low20(cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| swap | `High->Low` | +0.83 | +0.83 | +2.20 | — | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(Low), LogFloatShares), LogFloatShares), day_first(Low)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| swap | `Open->Close` | +0.84 | +0.84 | +2.20 | — | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Close))), 1))` |
| window | `ts_argmax@1->2` | +0.66 | +0.66 | +1.87 | — | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 2))` |

### head score +0.83:`cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(day_centroid(Volume), day_centroid(Ret))` | +0.88 | +0.88 | +1.05 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | -0.09 | -0.09 | +0.54 | — | (子树本身) |
| sufficiency | `day_centroid(Ret)` | -1.38 | -1.38 | -0.48 | — | (子树本身) |
| knockout | `sub(day_centroid(Volume), day_centroid(Ret))` | +1.24 | +1.24 | +1.72 | -0.42 | `cross_mean(day_centroid(Volume), 20)` |
| swap | `Volume->Amt` | +0.83 | +0.83 | +1.25 | — | `cross_mean(sub(day_centroid(Amt), day_centroid(Ret)), 20)` |
| window | `cross_mean@20->10` | +0.84 | +0.84 | +1.25 | — | `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 10)` |
| window | `cross_mean@20->40` | +0.83 | +0.83 | +1.39 | — | `cross_mean(sub(day_centroid(Volume), day_centroid(Ret)), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(day_centroid(Volume), 20)` — ablation,自身 score +1.24(所在 head +1.55)
2. `sub(day_centroid(Volume), day_centroid(Ret))` — ablation,自身 score +0.88(所在 head +0.83)
3. `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` — ablation,自身 score +0.80(所在 head +0.84)
4. `cross_mean(day_flat_ratio(Close), 20)` — enrichment,均值差 +1.87,p 0.001
5. `day_flat_ratio(Close)` — enrichment,均值差 +1.78,p 0.000
6. `sub(day_pos_ratio(High), LogFloatShares)` — enrichment,均值差 +1.31,p 0.000
7. `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` — enrichment,均值差 +1.30,p 0.005
8. `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)` — enrichment,均值差 +1.26,p 0.011
9. `day_first(abs_(sub(1, Open)))` — enrichment,均值差 +1.21,p 0.025
10. `ts_argmax(day_first(abs_(sub(1, Open))), 1)` — enrichment,均值差 +1.21,p 0.025
11. `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` — enrichment,均值差 +1.19,p 0.000
12. `day_pos_ratio(High)` — enrichment,均值差 +1.18,p 0.000
13. `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` — enrichment,均值差 +1.05,p 0.000
14. `cross_mean(day_corr(Ret, Volume), 20)` — enrichment,均值差 +1.03,p 0.038
15. `cs_mean(day_distinct_ratio(Close))` — enrichment,均值差 +1.02,p 0.017
16. `day_first(High)` — enrichment,均值差 +0.99,p 0.000
17. `day_first(abs_(sub(-1, Open)))` — enrichment,均值差 +0.98,p 0.000
18. `ts_argmax(day_first(High), 1)` — enrichment,均值差 +0.93,p 0.000
19. `day_centroid(Ret)` — enrichment,均值差 +0.77,p 0.004
20. `day_corr(Ret, Volume)` — enrichment,均值差 +0.75,p 0.080
21. `pow_3(day_centroid(Volume))` — enrichment,均值差 +0.68,p 0.038
22. `day_centroid(Volume)` — enrichment,均值差 +0.28,p 0.033

## 本组之前各轮的任务

- `c05s805Br1a_Ea`:核心 `day_centroid(Volume)`;评分 82,过线 23,入 heads 4;采样计数 {'c05_no_core': 737, 'c05_periphery_seen': 7}
  - score +1.55(train +1.55 valid +2.11):`cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), day_centroid(Ret))`
  - score +1.52(train +1.52 valid +2.11):`cs_bucket_zscore(cross_mean(day_centroid(Volume), 10), day_centroid(Ret))`
  - score +1.52(train +1.52 valid +1.67):`cs_bucket_zscore(cross_mean(sub(day_centroid(Volume), pow_3(day_centroid(Volume))), 20), day_centroid(Ret))`
  - score +1.42(train +1.42 valid +2.76):`cross_mean(sub(day_centroid(Volume), pow_3(cs_bucket_rank(day_centroid(Volume), cross_mean(day_flat_ratio(Close), 20)))), 20)`
  - score +1.40(train +1.40 valid +1.40):`cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), cross_mean(day_flat_ratio(Close), 20))`
- `c05s805Br1b_Nb`:核心 `—`;评分 69,过线 2,入 heads 1;采样计数 {}
  - score +0.53(train +0.53 valid +0.96):`cross_mean(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 3), 20)`
  - score +0.52(train +0.52 valid +0.97):`cross_mean(cross_mean(cross_mean(day_corr(Ret, Volume), 20), 20), 3)`
  - score +0.46(train +0.46 valid +1.10):`cross_mean(cross_mean(day_corr(Ret, Volume), 20), 20)`
  - score +0.44(train +0.44 valid +1.05):`cross_mean(cross_mean(day_corr(Ret, Amt), 20), 20)`
  - score +0.39(train +0.39 valid +0.94):`cross_mean(cross_sum(cross_mean(day_corr(Ret, Volume), 20), 15), 20)`

## 比原 head 好的拆解变体(R 候选)

(没有)
