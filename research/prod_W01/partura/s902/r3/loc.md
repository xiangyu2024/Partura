# 定位:种子 902,P 组,第 3 轮(只含 train / valid)

快照:prods902M1_I0_open_search, prods902M2_I0_open_search, prods902M3_I0_open_search, prods902Pr1a_Na, prods902Pr1b_Nb, prods902Pr2a_Ea, prods902Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(5 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.23 | +2.21 | +1.23 | -1 | 5 | prods902Pr2b_Nb | `cross_ema(cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))), 20)` |
| +0.89 | +0.89 | +1.64 | +1 | 5 | prods902Pr2a_Ea | `cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 60)` |
| +0.62 | +0.62 | +0.91 | +1 | 0 | prods902Pr2b_Nb | `cross_ema(cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)), 20)` |
| +0.59 | +0.59 | +1.52 | +1 | 5 | prods902Pr2b_Nb | `cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 30)` |
| +0.56 | +0.56 | +0.58 | +1 | 5 | prods902Pr2a_Ea | `ts_max(div(day_first(Amt), day_sum(Amt)), 40)` |

## 共性:491 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.52 | 0.000 | 22 | +0.44 / -1.08 | `day_centroid(Volume)` |
| +1.48 | 0.000 | 7 | +0.44 / -1.04 | `abs_(day_centroid(Volume))` |
| +1.47 | 0.001 | 4 | +0.44 / -1.03 | `pow_1_5(day_centroid(Volume))` |
| +1.47 | 0.001 | 4 | +0.44 / -1.03 | `cs_scale(day_centroid(Volume))` |
| +1.46 | 0.003 | 4 | +0.43 / -1.03 | `day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30))` |
| +1.13 | 0.024 | 4 | +0.11 / -1.03 | `cs_last_low40(add(LogFloatShares, 0.5), sub(day_sum(Vwap), 0.5))` |
| +1.07 | 0.014 | 6 | +0.04 / -1.03 | `cs_last_low40(add(LogFloatShares, -5), sub(day_sum(Vwap), 0.5))` |
| +1.04 | 0.003 | 10 | -0.00 / -1.04 | `cs_last_low40(add(LogFloatShares, -2), sub(day_sum(Vwap), 0.5))` |
| +1.02 | 0.015 | 8 | -0.01 / -1.03 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 15)` |
| +1.00 | 0.021 | 6 | -0.03 / -1.03 | `cross_min(cs_last_low40(add(LogFloatShares, -2), sub(day_sum(Vwap), 0.5)), 5)` |
| +0.96 | 0.046 | 5 | -0.06 / -1.03 | `cs_last_low40(add(LogFloatShares, add(LogFloatShares, -5)), sub(day_sum(Vwap), 0.5))` |
| +0.88 | 0.006 | 12 | -0.16 / -1.04 | `cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap)` |
| +0.84 | 0.000 | 55 | -0.27 / -1.11 | `day_sum(Vwap)` |
| +0.75 | 0.091 | 4 | -0.27 / -1.02 | `cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 60)` |
| +0.71 | 0.070 | 8 | -0.32 / -1.03 | `cs_bucket_rank(day_max(High), day_quantile_q25(Open))` |
| +0.53 | 0.000 | 81 | -0.57 / -1.10 | `day_sum(Amt)` |
| +0.51 | 0.071 | 9 | -0.52 / -1.03 | `day_sum(in_slice(Amt, 211, 240))` |
| +0.49 | 0.001 | 64 | -0.59 / -1.08 | `div(day_first(Amt), day_sum(Amt))` |
| +0.46 | 0.002 | 66 | -0.62 / -1.08 | `day_first(Amt)` |
| +0.44 | 0.176 | 8 | -0.58 / -1.02 | `day_first(High)` |

## 拆解(33 次评估)

### head score +1.23:`cross_ema(cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)))` | +0.28 | +0.98 | +0.28 | — | (子树本身) |
| sufficiency | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` | +0.28 | +0.98 | +0.28 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Amt, 211, 240))` | -1.92 | -1.92 | -1.76 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)))` | +1.74 | +1.74 | +1.93 | -0.51 | `cross_ema(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| knockout | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` | -1.55 | -1.55 | -1.34 | +2.79 | `cross_ema(cs_rank(day_sum(in_slice(Amt, 211, 240))), 20)` |
| swap | `Amt->Volume` | +1.29 | +2.10 | +1.29 | — | `cross_ema(cs_rank(div(day_sum(in_slice(Volume, 211, 240)), day_sum(Volume))), 20)` |
| window | `cross_ema@20->10` | +1.31 | +2.04 | +1.31 | — | `cross_ema(cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))), 10)` |
| window | `cross_ema@20->40` | +0.64 | +1.73 | +0.64 | — | `cross_ema(cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))), 40)` |

### head score +0.89:`cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap)` | -1.11 | -1.11 | +1.10 | — | (子树本身) |
| sufficiency | `div(day_first(Amt), day_sum(Amt))` | -0.95 | -0.95 | +0.98 | — | (子树本身) |
| sufficiency | `day_first(Amt)` | -1.39 | -1.39 | -0.14 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap)` | +0.29 | +0.29 | +1.32 | +0.59 | `cross_mean(div(day_first(Amt), day_sum(Amt)), 60)` |
| knockout | `div(day_first(Amt), day_sum(Amt))` | -1.15 | -0.40 | -1.15 | +2.04 | `cross_mean(cs_bucket_demean(day_first(Amt), LogFloatCap), 60)` |
| swap | `Amt->Volume` | +0.90 | +0.90 | +1.64 | — | `cross_mean(cs_bucket_demean(div(day_first(Volume), day_sum(Volume)), LogFloatCap), 60)` |
| window | `cross_mean@60->30` | +0.32 | +0.32 | +1.59 | — | `cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 30)` |
| window | `cross_mean@60->120` | +0.43 | +0.43 | +1.38 | — | `cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 120)` |

### head score +0.62:`cross_ema(cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30))` | +0.58 | +0.58 | +0.89 | — | (子树本身) |
| sufficiency | `cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)` | +0.57 | +0.57 | +0.89 | — | (子树本身) |
| sufficiency | `day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30))` | -2.36 | -2.36 | -1.40 | — | (子树本身) |
| knockout | `cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30))` | +0.38 | +0.38 | +0.71 | +0.24 | `cross_ema(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30), 20)` |
| knockout | `cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)` | +0.16 | +0.16 | +0.87 | +0.46 | `cross_ema(cs_rank(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30))), 20)` |
| swap | `Amt->Volume` | +0.63 | +0.63 | +0.94 | — | `cross_ema(cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Volume, 1, 30)), 30)), 20)` |
| window | `cross_ema@20->10` | +0.50 | +0.50 | +0.91 | — | `cross_ema(cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)), 10)` |
| window | `cross_ema@20->40` | +0.19 | +0.19 | +0.48 | — | `cross_ema(cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)), 40)` |

### head score +0.59:`cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt))` | -0.05 | -0.05 | +0.06 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Amt, 1, 30))` | -2.90 | -2.37 | -2.90 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt))` | -2.33 | -2.33 | -1.20 | +2.92 | `cross_mean(day_sum(in_slice(Amt, 1, 30)), 30)` |
| swap | `Amt->Volume` | +0.56 | +0.56 | +1.55 | — | `cross_mean(div(day_sum(in_slice(Volume, 1, 30)), day_sum(Volume)), 30)` |
| window | `cross_mean@30->15` | +0.47 | +0.47 | +0.73 | — | `cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 15)` |
| window | `cross_mean@30->60` | +0.25 | +0.25 | +0.36 | — | `cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30))` — ablation,自身 score +0.58(所在 head +0.62)
2. `cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)` — ablation,自身 score +0.57(所在 head +0.62)
3. `day_centroid(Volume)` — enrichment,均值差 +1.52,p 0.000
4. `abs_(day_centroid(Volume))` — enrichment,均值差 +1.48,p 0.000
5. `pow_1_5(day_centroid(Volume))` — enrichment,均值差 +1.47,p 0.001
6. `cs_scale(day_centroid(Volume))` — enrichment,均值差 +1.47,p 0.001
7. `day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30))` — enrichment,均值差 +1.46,p 0.003
8. `cs_last_low40(add(LogFloatShares, 0.5), sub(day_sum(Vwap), 0.5))` — enrichment,均值差 +1.13,p 0.024
9. `cs_last_low40(add(LogFloatShares, -5), sub(day_sum(Vwap), 0.5))` — enrichment,均值差 +1.07,p 0.014
10. `cs_last_low40(add(LogFloatShares, -2), sub(day_sum(Vwap), 0.5))` — enrichment,均值差 +1.04,p 0.003
11. `cross_mean(div(day_first(Amt), day_sum(Amt)), 15)` — enrichment,均值差 +1.02,p 0.015
12. `cross_min(cs_last_low40(add(LogFloatShares, -2), sub(day_sum(Vwap), 0.5)), 5)` — enrichment,均值差 +1.00,p 0.021
13. `cs_last_low40(add(LogFloatShares, add(LogFloatShares, -5)), sub(day_sum(Vwap), 0.5))` — enrichment,均值差 +0.96,p 0.046
14. `cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap)` — enrichment,均值差 +0.88,p 0.006
15. `day_sum(Vwap)` — enrichment,均值差 +0.84,p 0.000
16. `cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 60)` — enrichment,均值差 +0.75,p 0.091
17. `cs_bucket_rank(day_max(High), day_quantile_q25(Open))` — enrichment,均值差 +0.71,p 0.070
18. `day_sum(Amt)` — enrichment,均值差 +0.53,p 0.000
19. `day_sum(in_slice(Amt, 211, 240))` — enrichment,均值差 +0.51,p 0.071
20. `div(day_first(Amt), day_sum(Amt))` — enrichment,均值差 +0.49,p 0.001
21. `day_first(Amt)` — enrichment,均值差 +0.46,p 0.002

## 本组之前各轮的任务

- `prods902Pr1a_Na`:核心 `—`;评分 83,过线 0,入 heads 0;采样计数 {}
  - score +0.21(train +0.21 valid +1.21):`cross_mean(cross_mean(div(day_first(Amt), day_sum(Amt)), 15), 30)`
  - score +0.15(train +0.15 valid +1.26):`cross_mean(div(day_first(Amt), day_sum(Amt)), 30)`
  - score +0.14(train +0.14 valid +1.45):`cross_mean(cross_mean(div(day_first(Amt), day_sum(Amt)), 15), 20)`
  - score +0.11(train +0.11 valid +1.43):`cross_mean(cross_mean(cross_mean(div(day_first(Amt), day_sum(Amt)), 15), 30), 30)`
  - score +0.11(train +0.11 valid +1.19):`cross_mean(cross_mean(cross_mean(div(day_first(Amt), day_sum(Amt)), 15), 15), 20)`
- `prods902Pr1b_Nb`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {}
  - score +0.47(train +0.47 valid +0.77):`cs_last_high05(cs_bucket_rank(day_max(High), day_max(High)), div(day_first(High), -5))`
  - score +0.47(train +0.47 valid +0.77):`cs_last_high05(cs_bucket_rank(day_max(High), day_max(High)), div(day_first(High), -2))`
  - score +0.43(train +0.43 valid +0.77):`cs_last_high05(cs_bucket_rank(day_max(High), day_max(High)), div(day_quantile_q25(Open), -5))`
  - score +0.42(train +0.42 valid +0.75):`cs_bucket_rank(day_max(High), day_max(High))`
  - score +0.41(train +0.41 valid +0.92):`cs_last_high05(cs_bucket_rank(day_max(High), day_quantile_q25(Open)), div(day_first(Close), -2))`
- `prods902Pr2a_Ea`:核心 `div(day_first(Amt), day_sum(Amt))`;评分 84,过线 3,入 heads 2;采样计数 {'c05_no_core': 1307, 'c05_periphery_seen': 8}
  - score +0.89(train +0.89 valid +1.64):`cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 60)`
  - score +0.80(train +0.80 valid +1.44):`cross_fangzheng(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 60)`
  - score +0.56(train +0.56 valid +0.58):`ts_max(div(day_first(Amt), day_sum(Amt)), 40)`
  - score +0.47(train +0.47 valid +1.59):`ts_max(cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 60), 40)`
  - score +0.34(train +0.34 valid +1.44):`cross_mean(cs_bucket_demean(cross_mean(cs_bucket_demean(div(day_first(Amt), day_sum(Amt)), LogFloatCap), 60), LogFloatCap), 60)`
- `prods902Pr2b_Nb`:核心 `—`;评分 81,过线 5,入 heads 3;采样计数 {}
  - score +1.23(train +2.21 valid +1.23):`cross_ema(cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))), 20)`
  - score +0.62(train +0.62 valid +0.91):`cross_ema(cs_rank(cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)), 20)`
  - score +0.59(train +0.59 valid +1.52):`cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 30)`
  - score +0.57(train +0.57 valid +0.89):`cross_mean(day_signed_ratio(in_slice(Ret, 1, 30), in_slice(Amt, 1, 30)), 30)`
  - score +0.57(train +2.13 valid +0.57):`cross_ema(cs_rank(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))), 5)`

## 比原 head 好的拆解变体(R 候选)

(没有)
