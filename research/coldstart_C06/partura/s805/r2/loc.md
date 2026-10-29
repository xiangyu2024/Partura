# 定位:种子 805,C 组,第 2 轮(只含 train / valid)

快照:c05s805M1_I0_open_search, c05s805M2_I0_open_search, c06s805Cr1a_Ea, c06s805Cr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.28 | +1.28 | +1.33 | -1 | 5 | c06s805Cr1a_Ea | `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))` |
| +0.84 | +0.84 | +2.20 | -1 | 5 | c05s805M2_I0_open_search | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| +0.81 | +0.81 | +2.58 | -1 | 5 | c05s805M2_I0_open_search | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| +0.64 | +1.01 | +0.64 | -1 | 20 | c05s805M2_I0_open_search | `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), ts_argmax(day_first(High), 1))` |
| +0.58 | +0.58 | +0.66 | -1 | 20 | c05s805M2_I0_open_search | `cs_last_low20(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), ts_argmax(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), 20))` |
| +0.51 | +0.51 | +0.80 | +1 | 5 | c06s805Cr1a_Ea | `sub(LogFloatShares, cross_ema(day_centroid(Volume), 40))` |

## 共性:320 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.84 | 0.000 | 4 | +1.10 / -0.74 | `cross_mean(cross_mean(day_sum(Amt), 30), 30)` |
| +1.53 | 0.000 | 11 | +0.76 / -0.77 | `cross_mean(day_sum(Amt), 30)` |
| +1.37 | 0.000 | 7 | +0.62 / -0.75 | `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` |
| +1.34 | 0.000 | 14 | +0.56 / -0.78 | `day_sum(Amt)` |
| +1.32 | 0.002 | 5 | +0.58 / -0.74 | `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` |
| +1.32 | 0.000 | 53 | +0.38 / -0.94 | `sub(day_pos_ratio(High), LogFloatShares)` |
| +1.28 | 0.005 | 4 | +0.55 / -0.74 | `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)` |
| +1.23 | 0.011 | 4 | +0.50 / -0.73 | `ts_argmax(day_first(abs_(sub(1, Open))), 1)` |
| +1.23 | 0.011 | 4 | +0.50 / -0.73 | `day_first(abs_(sub(1, Open)))` |
| +1.21 | 0.000 | 28 | +0.39 / -0.83 | `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` |
| +1.19 | 0.000 | 70 | +0.21 / -0.98 | `day_pos_ratio(High)` |
| +1.07 | 0.000 | 22 | +0.28 / -0.79 | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` |
| +1.05 | 0.007 | 7 | +0.30 / -0.74 | `cs_mean(day_distinct_ratio(Close))` |
| +1.01 | 0.000 | 52 | +0.12 / -0.88 | `day_first(High)` |
| +1.00 | 0.000 | 27 | +0.20 / -0.80 | `day_first(abs_(sub(-1, Open)))` |
| +0.95 | 0.000 | 30 | +0.14 / -0.81 | `ts_argmax(day_first(High), 1)` |
| +0.82 | 0.068 | 8 | +0.08 / -0.74 | `pow_1_5(day_centroid(Volume))` |
| +0.79 | 0.041 | 20 | +0.02 / -0.77 | `pow_2_5(day_centroid(Volume))` |
| +0.74 | 0.112 | 12 | -0.01 / -0.75 | `pow_1_5(pow_2_5(day_centroid(Volume)))` |
| +0.74 | 0.116 | 4 | +0.01 / -0.73 | `ts_argmax(day_first(Open), 1)` |

## 拆解(41 次评估)

### head score +1.28:`log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30))` | +1.31 | +1.36 | +1.31 | — | (子树本身) |
| sufficiency | `cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)` | -1.82 | -1.71 | -1.82 | — | (子树本身) |
| sufficiency | `cross_mean(cross_mean(day_sum(Amt), 30), 30)` | -2.14 | -2.14 | -1.82 | — | (子树本身) |
| sufficiency | `cross_ema(day_centroid(Volume), 10)` | +1.31 | +1.31 | +1.58 | — | (子树本身) |
| knockout | `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30))` | +1.27 | +1.27 | +1.63 | +0.00 | `log(cross_ema(day_centroid(Volume), 10))` |
| knockout | `cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)` | +1.06 | +1.20 | +1.06 | +0.21 | `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(day_sum(Amt), 30), 30)))` |
| knockout | `cross_ema(day_centroid(Volume), 10)` | -0.60 | +0.00 | -0.60 | +1.88 | `log(cs_bucket_rank(day_centroid(Volume), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))` |
| swap | `Volume->Amt` | +1.37 | +1.37 | +1.39 | — | `log(cs_bucket_rank(cross_ema(day_centroid(Amt), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))` |
| swap | `Amt->Volume` | +0.29 | +0.91 | +0.29 | — | `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Volume), 30), 30), 30)))` |
| window | `cross_ema@10->5` | +0.54 | +1.05 | +0.54 | — | `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 5), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))` |
| window | `cross_ema@10->20` | +1.22 | +1.22 | +1.27 | — | `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 20), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))` |

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

### head score +0.81:`cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High))` | +0.81 | +0.81 | +2.58 | — | (子树本身) |
| sufficiency | `sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open))))))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open))))))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `day_first(abs_(sub(-2, abs_(sub(-1, Open)))))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| knockout | `cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High))` | -1.15 | -1.15 | -0.46 | +1.96 | `cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| knockout | `sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open))))))` | +0.81 | +0.81 | +2.58 | +0.00 | `cs_last_low20(cs_last_low20(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| knockout | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` | +0.94 | +0.94 | +2.54 | -0.13 | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), day_first(abs_(sub(-1, Open))))` |
| swap | `High->Low` | +0.81 | +0.81 | +2.58 | — | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(Low), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(Low)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| swap | `Open->Close` | +0.81 | +0.81 | +2.58 | — | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Close)))))), day_first(abs_(sub(-2, abs_(sub(-1, Close)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Close))), 1))` |
| window | `ts_argmax@1->2` | +0.62 | +0.62 | +2.12 | — | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 2))` |

### head score +0.64:`cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), ts_argmax(day_first(High), 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` | +0.48 | +0.48 | +0.76 | — | (子树本身) |
| sufficiency | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_first(abs_(sub(-1, Open)))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `ts_argmax(day_first(High), 1)` | — | — | — | — | 门槛废品 |
| knockout | `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` | — | — | — | — | `cs_bucket_demean(ts_argmax(day_first(abs_(sub(-1, Open))), 1), ts_argmax(day_first(High), 1))` |
| knockout | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` | -2.15 | -1.08 | -2.15 | +2.79 | `cs_bucket_demean(sub(day_first(abs_(sub(-1, Open))), LogFloatShares), ts_argmax(day_first(High), 1))` |
| knockout | `ts_argmax(day_first(High), 1)` | +0.25 | +0.25 | +0.74 | +0.39 | `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), day_first(High))` |
| swap | `Open->Close` | +0.64 | +1.01 | +0.64 | — | `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Close))), 1), LogFloatShares), ts_argmax(day_first(High), 1))` |
| swap | `High->Low` | +0.64 | +1.01 | +0.64 | — | `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), ts_argmax(day_first(Low), 1))` |
| window | `ts_argmax@1->2` | +0.55 | +1.07 | +0.55 | — | `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 2), LogFloatShares), ts_argmax(day_first(High), 1))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_ema(day_centroid(Volume), 10)` — ablation,自身 score +1.31(所在 head +1.28)
2. `cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30))` — ablation,自身 score +1.31(所在 head +1.28)
3. `cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High))` — ablation,自身 score +0.81(所在 head +0.81)
4. `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` — ablation,自身 score +0.80(所在 head +0.84)
5. `cross_mean(cross_mean(day_sum(Amt), 30), 30)` — enrichment,均值差 +1.84,p 0.000
6. `cross_mean(day_sum(Amt), 30)` — enrichment,均值差 +1.53,p 0.000
7. `day_sum(Amt)` — enrichment,均值差 +1.34,p 0.000
8. `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` — enrichment,均值差 +1.32,p 0.002
9. `sub(day_pos_ratio(High), LogFloatShares)` — enrichment,均值差 +1.32,p 0.000
10. `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)` — enrichment,均值差 +1.28,p 0.005
11. `ts_argmax(day_first(abs_(sub(1, Open))), 1)` — enrichment,均值差 +1.23,p 0.011
12. `day_first(abs_(sub(1, Open)))` — enrichment,均值差 +1.23,p 0.011
13. `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` — enrichment,均值差 +1.21,p 0.000
14. `day_pos_ratio(High)` — enrichment,均值差 +1.19,p 0.000
15. `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` — enrichment,均值差 +1.07,p 0.000
16. `cs_mean(day_distinct_ratio(Close))` — enrichment,均值差 +1.05,p 0.007
17. `day_first(High)` — enrichment,均值差 +1.01,p 0.000
18. `day_first(abs_(sub(-1, Open)))` — enrichment,均值差 +1.00,p 0.000
19. `ts_argmax(day_first(High), 1)` — enrichment,均值差 +0.95,p 0.000
20. `pow_1_5(day_centroid(Volume))` — enrichment,均值差 +0.82,p 0.068
21. `pow_2_5(day_centroid(Volume))` — enrichment,均值差 +0.79,p 0.041
22. `day_centroid(Volume)` — enrichment,均值差 +0.57,p 0.002
23. `day_distinct_ratio(Close)` — enrichment,均值差 +0.55,p 0.078

## 本组之前各轮的任务

- `c06s805Cr1a_Ea`:核心 `day_centroid(Volume)`;评分 87,过线 13,入 heads 2;采样计数 {'c05_no_core': 890, 'c05_periphery_seen': 3}
  - score +1.28(train +1.28 valid +1.33):`log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))`
  - score +1.15(train +1.25 valid +1.15):`log(log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30))))`
  - score +1.10(train +1.51 valid +1.10):`cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30))`
  - score +1.09(train +1.33 valid +1.09):`cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(day_sum(Amt), 30), 30))`
  - score +1.08(train +1.30 valid +1.08):`log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(day_sum(Amt), 30)))`
- `c06s805Cr1b_Nb`:核心 `—`;评分 83,过线 0,入 heads 0;采样计数 {}
  - score +0.27(train +0.57 valid +0.27):`cross_ema(sub(day_signed_ratio(Ret, mul(Volume, in_index(Volume))), day_signed_ratio(Ret, mul(Volume, sub(1, in_index(Volume))))), 5)`
  - score +0.01(train +0.01 valid +1.16):`cross_ema(sub(day_signed_ratio(Ret, mul(Close, in_index(Volume))), day_signed_ratio(Ret, mul(Volume, sub(1, in_index(Volume))))), 5)`
  - score -0.09(train -0.09 valid +2.09):`cross_ema(sub(ts_autocorr_s1(day_flat_run_max(Ret), 40), day_signed_ratio(Ret, mul(Volume, sub(1, in_index(Volume))))), 5)`
  - score -0.14(train -0.14 valid +1.31):`ts_quantile_q25(pow_2(cross_hurst(cs_rank(sigmoid(day_wmean(Volume, Open))), 15)), 20)`
  - score -0.32(train -0.32 valid +1.14):`ts_quantile_q25(pow_3(cross_hurst(cs_rank(sigmoid(day_wmean(Volume, Open))), 15)), 20)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.13(knockout ts_argmax(day_first(abs_(sub(-1, Open))), 1)):`cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), day_first(abs_(sub(-1, Open))))`
