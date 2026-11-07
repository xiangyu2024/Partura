# 定位:种子 908,P 组,第 2 轮(只含 train / valid)

快照:prods908M1_I0_open_search, prods908M2_I0_open_search, prods908Pr1a_Ea, prods908Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.81 | +1.94 | +1.81 | -1 | 5 | prods908Pr1b_Nb | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)` |
| +1.58 | +1.69 | +1.58 | -1 | 5 | prods908Pr1a_Ea | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)` |
| +1.02 | +1.04 | +1.02 | +1 | 5 | prods908M1_I0_open_search | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 50)` |
| +0.96 | +0.98 | +0.96 | -1 | 20 | prods908Pr1a_Ea | `ts_min(day_centroid(Amt), 20)` |
| +0.93 | +0.93 | +1.42 | +1 | 20 | prods908Pr1b_Nb | `sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centroid(Volume))` |
| +0.85 | +0.85 | +1.12 | -1 | 20 | prods908Pr1a_Ea | `cs_first_low40(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)` |
| +0.73 | +0.73 | +0.89 | +1 | 5 | prods908M1_I0_open_search | `cs_bucket_zscore(day_median(High), day_wmean(Open, Amt))` |

## 共性:276 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.30 | 0.024 | 4 | +0.11 / -1.19 | `day_at_max_ratio(in_slice(Amt, 211, 240))` |
| +1.30 | 0.007 | 5 | +0.10 / -1.20 | `cs_regres(ListAge, day_centroid(Amt))` |
| +1.30 | 0.036 | 8 | +0.09 / -1.21 | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)` |
| +1.22 | 0.000 | 75 | -0.29 / -1.50 | `day_centroid(Amt)` |
| +1.21 | 0.006 | 8 | -0.00 / -1.21 | `cs_regres(ListAge, pow_3(day_centroid(Amt)))` |
| +1.16 | 0.004 | 11 | -0.06 / -1.22 | `day_centroid(Volume)` |
| +1.11 | 0.070 | 4 | -0.08 / -1.19 | `sub(day_centroid(Ret), day_centroid(Volume))` |
| +1.00 | 0.008 | 12 | -0.21 / -1.22 | `pow_3(day_centroid(Amt))` |
| +0.84 | 0.080 | 4 | -0.35 / -1.19 | `cs_regres(ListAge, LogFloatShares)` |
| +0.79 | 0.023 | 17 | -0.43 / -1.22 | `cross_mean(day_centroid(Amt), 20)` |
| +0.66 | 0.090 | 10 | -0.54 / -1.20 | `day_centroid(Ret)` |
| +0.65 | 0.159 | 9 | -0.55 / -1.19 | `day_sum(in_slice(Amt, 211, 240))` |
| +0.49 | 0.227 | 4 | -0.69 / -1.18 | `cs_bucket_rank(sub(day_first(High), 1), cs_normalize(day_sum(Amt)))` |
| +0.49 | 0.227 | 4 | -0.69 / -1.18 | `cs_normalize(cs_bucket_rank(sub(day_first(High), 1), cs_normalize(day_sum(Amt))))` |
| +0.40 | 0.244 | 8 | -0.78 / -1.18 | `cs_normalize(cs_normalize(day_sum(Amt)))` |
| +0.37 | 0.224 | 7 | -0.81 / -1.18 | `cs_normalize(day_sum(High))` |
| +0.36 | 0.354 | 6 | -0.83 / -1.18 | `day_min(Close)` |
| +0.33 | 0.394 | 5 | -0.85 / -1.18 | `pow_3(day_min(Close))` |
| +0.31 | 0.171 | 36 | -0.91 / -1.21 | `day_first(High)` |
| +0.27 | 0.379 | 5 | -0.91 / -1.18 | `cs_bucket_rank(2, cs_normalize(day_sum(High)))` |

## 拆解(27 次评估)

### head score +1.81:`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` | +0.28 | +0.98 | +0.28 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Amt, 211, 240))` | -1.92 | -1.92 | -1.76 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -2.78 | -2.78 | -1.73 | — | (子树本身) |
| knockout | `div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt))` | -1.80 | -1.64 | -1.80 | +3.61 | `cross_mean(day_sum(in_slice(Amt, 211, 240)), 20)` |
| swap | `Amt->Volume` | +1.70 | +1.91 | +1.70 | — | `cross_mean(div(day_sum(in_slice(Volume, 211, 240)), day_sum(Volume)), 20)` |
| window | `cross_mean@20->10` | +1.53 | +1.53 | +1.65 | — | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 10)` |
| window | `cross_mean@20->40` | +1.31 | +1.31 | +2.00 | — | `cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 40)` |

### head score +1.58:`cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)` | +1.57 | +1.69 | +1.57 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)` | +1.73 | +1.73 | +1.83 | -0.15 | `cs_regres(cross_mean(day_centroid(Amt), 20), LogFloatShares)` |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +0.51 | +1.12 | +0.51 | +1.06 | `cs_regres(cs_bucket_zscore(day_centroid(Amt), LogFloatShares), LogFloatShares)` |
| swap | `Amt->Volume` | +1.54 | +1.64 | +1.54 | — | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Volume), 20), LogFloatShares), LogFloatShares)` |
| window | `cross_mean@20->10` | +1.09 | +1.63 | +1.09 | — | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 10), LogFloatShares), LogFloatShares)` |
| window | `cross_mean@20->40` | +1.31 | +1.31 | +1.61 | — | `cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 40), LogFloatShares), LogFloatShares)` |

### head score +1.02:`ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_regres(ListAge, pow_3(day_centroid(Volume)))` | -0.34 | -0.34 | -0.10 | — | (子树本身) |
| sufficiency | `pow_3(day_centroid(Volume))` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `cs_regres(ListAge, pow_3(day_centroid(Volume)))` | — | — | — | — | `ts_quantile_q75(ListAge, 50)` |
| knockout | `pow_3(day_centroid(Volume))` | +0.82 | +1.13 | +0.82 | +0.21 | `ts_quantile_q75(cs_regres(ListAge, day_centroid(Volume)), 50)` |
| swap | `Volume->Amt` | +0.96 | +0.96 | +1.18 | — | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt))), 50)` |
| window | `ts_quantile_q75@50->25` | +0.14 | +1.48 | +0.14 | — | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 25)` |
| window | `ts_quantile_q75@50->100` | +0.43 | +0.43 | +0.74 | — | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 100)` |

### head score +0.96:`ts_min(day_centroid(Amt), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| swap | `Amt->Volume` | +0.84 | +1.03 | +0.84 | — | `ts_min(day_centroid(Volume), 20)` |
| window | `ts_min@20->10` | +0.48 | +1.16 | +0.48 | — | `ts_min(day_centroid(Amt), 10)` |
| window | `ts_min@20->40` | +0.43 | +0.43 | +0.68 | — | `ts_min(day_centroid(Amt), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)` — ablation,自身 score +1.57(所在 head +1.58)
2. `cross_mean(day_centroid(Amt), 20)` — ablation,自身 score +1.34(所在 head +1.58)
3. `day_at_max_ratio(in_slice(Amt, 211, 240))` — enrichment,均值差 +1.30,p 0.024
4. `cs_regres(ListAge, day_centroid(Amt))` — enrichment,均值差 +1.30,p 0.007
5. `day_centroid(Amt)` — enrichment,均值差 +1.22,p 0.000
6. `cs_regres(ListAge, pow_3(day_centroid(Amt)))` — enrichment,均值差 +1.21,p 0.006
7. `day_centroid(Volume)` — enrichment,均值差 +1.16,p 0.004
8. `sub(day_centroid(Ret), day_centroid(Volume))` — enrichment,均值差 +1.11,p 0.070
9. `pow_3(day_centroid(Amt))` — enrichment,均值差 +1.00,p 0.008
10. `cs_regres(ListAge, LogFloatShares)` — enrichment,均值差 +0.84,p 0.080
11. `day_centroid(Ret)` — enrichment,均值差 +0.66,p 0.090

## 本组之前各轮的任务

- `prods908Pr1a_Ea`:核心 `day_centroid(Amt)`;评分 78,过线 16,入 heads 3;采样计数 {'c05_periphery_seen': 7, 'c05_no_core': 1561}
  - score +1.58(train +1.69 valid +1.58):`cs_regres(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)`
  - score +1.58(train +1.69 valid +1.58):`cs_regres(cs_bucket_zscore(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares), LogFloatShares)`
  - score +1.57(train +1.69 valid +1.57):`cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares)`
  - score +1.57(train +1.69 valid +1.57):`cs_bucket_zscore(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares)`
  - score +1.57(train +1.69 valid +1.57):`cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cs_bucket_zscore(cross_mean(day_centroid(Amt), 20), LogFloatShares), LogFloatShares), LogFloatShares), LogFloatShares)`
- `prods908Pr1b_Nb`:核心 `—`;评分 77,过线 5,入 heads 2;采样计数 {}
  - score +1.81(train +1.94 valid +1.81):`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 20)`
  - score +1.81(train +1.94 valid +1.81):`cross_mean(div(sub(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), day_sum(Amt)), 20)`
  - score +1.19(train +1.69 valid +1.19):`cross_mean(div(day_sum(in_slice(Amt, 211, 240)), day_sum(Amt)), 15)`
  - score +0.93(train +0.93 valid +1.42):`sub(sub(day_centroid(Ret), day_centroid(Volume)), day_centroid(Volume))`
  - score +0.63(train +0.63 valid +0.73):`sub(day_centroid(Ret), day_centroid(Volume))`

## 比原 head 好的拆解变体(R 候选)

(没有)
