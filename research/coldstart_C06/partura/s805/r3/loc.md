# 定位:种子 805,C 组,第 3 轮(只含 train / valid)

快照:c05s805M1_I0_open_search, c05s805M2_I0_open_search, c05s805M3_I0_open_search, c06s805Cr1a_Ea, c06s805Cr1b_Nb, c06s805Cr2a_Na, c06s805Cr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(11 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.28 | +1.28 | +1.33 | -1 | 5 | c06s805Cr1a_Ea | `log(cs_bucket_rank(cross_ema(day_centroid(Volume), 10), cross_mean(cross_mean(cross_mean(day_sum(Amt), 30), 30), 30)))` |
| +1.13 | +1.13 | +2.48 | +1 | 20 | c06s805Cr2b_Nb | `cs_bucket_rank(cross_mean(day_first(Amt), 241), cross_mean(cross_mean(day_first(Amt), 241), 30))` |
| +0.94 | +0.94 | +2.54 | -1 | 5 | c05s805M2_I0_open_search | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), day_first(abs_(sub(-1, Open))))` |
| +0.93 | +0.93 | +1.61 | -1 | 20 | c06s805Cr2a_Na | `day_kurt(in_slice(Ret, 1, 236))` |
| +0.88 | +0.88 | +1.18 | +1 | 20 | c05s805M3_I0_open_search | `ts_skew(day_wstd(Volume, Vwap), 50)` |
| +0.84 | +0.84 | +2.20 | -1 | 5 | c05s805M2_I0_open_search | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High)), ts_argmax(day_first(abs_(sub(-1, Open))), 1))` |
| +0.64 | +1.01 | +0.64 | -1 | 20 | c05s805M2_I0_open_search | `cs_bucket_demean(sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares), ts_argmax(day_first(High), 1))` |
| +0.63 | +0.63 | +1.59 | +1 | 5 | c06s805Cr2b_Nb | `cs_bucket_rank(cross_mean(cross_mean(day_first(Amt), 20), 20), cross_mean(cross_mean(cross_mean(day_first(Amt), 20), 20), 30))` |
| +0.63 | +0.63 | +0.78 | -1 | 20 | c05s805M3_I0_open_search | `ts_skew(day_corr(Volume, Vwap), 50)` |
| +0.58 | +0.58 | +0.66 | -1 | 20 | c05s805M2_I0_open_search | `cs_last_low20(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), ts_argmax(sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares), 20))` |
| +0.51 | +0.51 | +0.80 | +1 | 5 | c06s805Cr1a_Ea | `sub(LogFloatShares, cross_ema(day_centroid(Volume), 40))` |

## 共性:482 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.79 | 0.001 | 5 | +0.82 / -0.97 | `cross_mean(cross_mean(day_sum(Amt), 30), 30)` |
| +1.60 | 0.000 | 7 | +0.62 / -0.98 | `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` |
| +1.56 | 0.001 | 5 | +0.59 / -0.97 | `day_kurt(in_slice(Ret, 1, 236))` |
| +1.56 | 0.001 | 5 | +0.58 / -0.97 | `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` |
| +1.52 | 0.003 | 4 | +0.55 / -0.97 | `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)` |
| +1.50 | 0.000 | 53 | +0.38 / -1.12 | `sub(day_pos_ratio(High), LogFloatShares)` |
| +1.46 | 0.006 | 4 | +0.50 / -0.97 | `ts_argmax(day_first(abs_(sub(1, Open))), 1)` |
| +1.46 | 0.006 | 4 | +0.50 / -0.97 | `day_first(abs_(sub(1, Open)))` |
| +1.43 | 0.000 | 28 | +0.39 / -1.04 | `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` |
| +1.37 | 0.000 | 70 | +0.21 / -1.15 | `day_pos_ratio(High)` |
| +1.30 | 0.000 | 22 | +0.28 / -1.02 | `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` |
| +1.28 | 0.002 | 7 | +0.30 / -0.97 | `cs_mean(day_distinct_ratio(Close))` |
| +1.23 | 0.000 | 27 | +0.20 / -1.02 | `day_first(abs_(sub(-1, Open)))` |
| +1.21 | 0.000 | 52 | +0.12 / -1.09 | `day_first(High)` |
| +1.17 | 0.000 | 30 | +0.14 / -1.03 | `ts_argmax(day_first(High), 1)` |
| +1.05 | 0.013 | 8 | +0.08 / -0.97 | `pow_1_5(day_centroid(Volume))` |
| +1.02 | 0.001 | 20 | +0.02 / -1.00 | `pow_2_5(day_centroid(Volume))` |
| +0.97 | 0.009 | 12 | -0.01 / -0.98 | `pow_1_5(pow_2_5(day_centroid(Volume)))` |
| +0.97 | 0.058 | 4 | +0.01 / -0.96 | `ts_argmax(day_first(Open), 1)` |
| +0.97 | 0.058 | 4 | +0.01 / -0.96 | `day_first(Open)` |

## 拆解(22 次评估)

### head score +1.13:`cs_bucket_rank(cross_mean(day_first(Amt), 241), cross_mean(cross_mean(day_first(Amt), 241), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(cross_mean(day_first(Amt), 241), 30)` | -0.24 | -0.24 | +0.95 | — | (子树本身) |
| sufficiency | `cross_mean(day_first(Amt), 241)` | +0.12 | +0.12 | +1.53 | — | (子树本身) |
| sufficiency | `day_first(Amt)` | -1.29 | -0.91 | -1.29 | — | (子树本身) |
| knockout | `cross_mean(cross_mean(day_first(Amt), 241), 30)` | -0.28 | -0.28 | +1.45 | +1.41 | `cs_bucket_rank(cross_mean(day_first(Amt), 241), cross_mean(day_first(Amt), 241))` |
| knockout | `cross_mean(day_first(Amt), 241)` | -0.75 | -0.75 | +0.02 | +1.88 | `cs_bucket_rank(day_first(Amt), cross_mean(cross_mean(day_first(Amt), 241), 30))` |
| knockout | `cross_mean(day_first(Amt), 241)` | -0.90 | -0.90 | +0.35 | +2.03 | `cs_bucket_rank(cross_mean(day_first(Amt), 241), cross_mean(day_first(Amt), 30))` |
| swap | `Amt->Volume` | +1.32 | +1.32 | +2.10 | — | `cs_bucket_rank(cross_mean(day_first(Volume), 241), cross_mean(cross_mean(day_first(Volume), 241), 30))` |
| window | `cross_mean@241->120` | +0.84 | +1.09 | +0.84 | — | `cs_bucket_rank(cross_mean(day_first(Amt), 120), cross_mean(cross_mean(day_first(Amt), 241), 30))` |
| window | `cross_mean@241->482` | +0.40 | +1.11 | +0.40 | — | `cs_bucket_rank(cross_mean(day_first(Amt), 482), cross_mean(cross_mean(day_first(Amt), 241), 30))` |

### head score +0.94:`cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), day_first(abs_(sub(-1, Open))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High))` | +0.81 | +0.81 | +2.58 | — | (子树本身) |
| sufficiency | `sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open))))))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open))))))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| sufficiency | `day_first(abs_(sub(-2, abs_(sub(-1, Open)))))` | -1.15 | -1.15 | -0.46 | — | (子树本身) |
| knockout | `cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High))` | +0.81 | +0.81 | +2.58 | +0.13 | `cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-1, Open))))` |
| knockout | `sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open))))))` | +0.94 | +0.94 | +2.54 | +0.00 | `cs_last_low20(cs_last_low20(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High)), day_first(abs_(sub(-1, Open))))` |
| swap | `High->Low` | +0.94 | +0.94 | +2.54 | — | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(Low), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(Low)), day_first(abs_(sub(-1, Open))))` |
| swap | `Open->Close` | +0.94 | +0.94 | +2.54 | — | `cs_last_low20(cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Close)))))), day_first(abs_(sub(-2, abs_(sub(-1, Close)))))), day_first(High)), day_first(abs_(sub(-1, Close))))` |

### head score +0.93:`day_kurt(in_slice(Ret, 1, 236))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|

### head score +0.88:`ts_skew(day_wstd(Volume, Vwap), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_wstd(Volume, Vwap)` | -1.56 | +0.15 | -1.56 | — | (子树本身) |
| swap | `Volume->Amt` | +0.48 | +0.48 | +0.92 | — | `ts_skew(day_wstd(Amt, Vwap), 50)` |
| swap | `Vwap->Close` | +0.76 | +1.06 | +0.76 | — | `ts_skew(day_wstd(Volume, Close), 50)` |
| window | `ts_skew@50->25` | -0.30 | +0.46 | -0.30 | — | `ts_skew(day_wstd(Volume, Vwap), 25)` |
| window | `ts_skew@50->100` | +0.53 | +0.87 | +0.53 | — | `ts_skew(day_wstd(Volume, Vwap), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_low20(sub(sub(day_pos_ratio(High), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(abs_(sub(-2, abs_(sub(-1, Open)))))), day_first(High))` — ablation,自身 score +0.81(所在 head +0.94)
2. `cross_mean(cross_mean(day_sum(Amt), 30), 30)` — enrichment,均值差 +1.79,p 0.001
3. `cs_last_low20(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), day_first(High))` — enrichment,均值差 +1.60,p 0.000
4. `day_kurt(in_slice(Ret, 1, 236))` — enrichment,均值差 +1.56,p 0.001
5. `sub(ts_argmax(day_first(abs_(sub(-1, Open))), 1), LogFloatShares)` — enrichment,均值差 +1.56,p 0.001
6. `sub(sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares), LogFloatShares)` — enrichment,均值差 +1.52,p 0.003
7. `sub(day_pos_ratio(High), LogFloatShares)` — enrichment,均值差 +1.50,p 0.000
8. `ts_argmax(day_first(abs_(sub(1, Open))), 1)` — enrichment,均值差 +1.46,p 0.006
9. `day_first(abs_(sub(1, Open)))` — enrichment,均值差 +1.46,p 0.006
10. `sub(sub(day_pos_ratio(High), LogFloatShares), LogFloatShares)` — enrichment,均值差 +1.43,p 0.000
11. `day_pos_ratio(High)` — enrichment,均值差 +1.37,p 0.000
12. `ts_argmax(day_first(abs_(sub(-1, Open))), 1)` — enrichment,均值差 +1.30,p 0.000
13. `cs_mean(day_distinct_ratio(Close))` — enrichment,均值差 +1.28,p 0.002
14. `day_first(abs_(sub(-1, Open)))` — enrichment,均值差 +1.23,p 0.000
15. `day_first(High)` — enrichment,均值差 +1.21,p 0.000
16. `ts_argmax(day_first(High), 1)` — enrichment,均值差 +1.17,p 0.000
17. `pow_1_5(day_centroid(Volume))` — enrichment,均值差 +1.05,p 0.013
18. `pow_2_5(day_centroid(Volume))` — enrichment,均值差 +1.02,p 0.001
19. `pow_1_5(pow_2_5(day_centroid(Volume)))` — enrichment,均值差 +0.97,p 0.009
20. `ts_argmax(day_first(Open), 1)` — enrichment,均值差 +0.97,p 0.058
21. `day_first(Open)` — enrichment,均值差 +0.97,p 0.058
22. `pow_1_5(pow_1_5(pow_2_5(day_centroid(Volume))))` — enrichment,均值差 +0.94,p 0.069
23. `cross_ema(day_centroid(Volume), 10)` — enrichment,均值差 +0.91,p 0.000
24. `day_centroid(Volume)` — enrichment,均值差 +0.80,p 0.000
25. `day_distinct_ratio(Close)` — enrichment,均值差 +0.79,p 0.032
26. `cross_mean(day_sum(Amt), 30)` — enrichment,均值差 +0.65,p 0.010
27. `day_sum(Amt)` — enrichment,均值差 +0.56,p 0.015

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
- `c06s805Cr2a_Na`:核心 `—`;评分 61,过线 5,入 heads 1;采样计数 {}
  - score +0.93(train +0.93 valid +1.61):`day_kurt(in_slice(Ret, 1, 236))`
  - score +0.73(train +0.73 valid +1.50):`cross_ema(day_kurt(in_slice(Ret, 1, 236)), 15)`
  - score +0.72(train +0.72 valid +1.58):`cross_ema(day_kurt(in_slice(Ret, 1, 236)), 5)`
  - score +0.60(train +0.60 valid +1.48):`cross_ema(cross_ema(day_kurt(in_slice(Ret, 1, 236)), 5), 5)`
  - score +0.58(train +0.58 valid +1.61):`cross_fangzheng(cross_ema(day_kurt(in_slice(Ret, 1, 236)), 5), 3)`
- `c06s805Cr2b_Nb`:核心 `—`;评分 83,过线 2,入 heads 2;采样计数 {}
  - score +1.13(train +1.13 valid +2.48):`cs_bucket_rank(cross_mean(day_first(Amt), 241), cross_mean(cross_mean(day_first(Amt), 241), 30))`
  - score +0.63(train +0.63 valid +1.59):`cs_bucket_rank(cross_mean(cross_mean(day_first(Amt), 20), 20), cross_mean(cross_mean(cross_mean(day_first(Amt), 20), 20), 30))`
  - score +0.42(train +0.42 valid +2.38):`cs_bucket_rank(cross_mean(day_first(Amt), 20), cross_mean(cross_mean(day_first(Amt), 20), 30))`
  - score +0.36(train +0.36 valid +0.72):`cs_bucket_rank(cs_bucket_rank(cross_mean(day_sum(Amt), 20), cross_mean(day_sum(Amt), 241)), cross_mean(day_sum(Amt), 241))`
  - score +0.22(train +0.22 valid +1.23):`cs_bucket_rank(cross_mean(day_sum(Amt), 20), cross_mean(day_sum(Amt), 30))`

## 比原 head 好的拆解变体(R 候选)

(没有)
