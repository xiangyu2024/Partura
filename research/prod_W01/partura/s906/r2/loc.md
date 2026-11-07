# 定位:种子 906,P 组,第 2 轮(只含 train / valid)

快照:prods906M1_I0_open_search, prods906M2_I0_open_search, prods906Pr1a_Ea, prods906Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(13 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.80 | +1.80 | +2.56 | -1 | 5 | prods906Pr1b_Nb | `cs_first_low20(LogFloatCap, LogFloatCap)` |
| +1.62 | +1.81 | +1.62 | -1 | 5 | prods906Pr1a_Ea | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +1.50 | +1.50 | +3.04 | -1 | 5 | prods906Pr1a_Ea | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 20))` |
| +1.30 | +1.30 | +3.56 | -1 | 5 | prods906Pr1a_Ea | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +1.20 | +1.20 | +2.53 | -1 | 5 | prods906Pr1b_Nb | `cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Open)))` |
| +0.94 | +0.94 | +2.69 | -1 | 5 | prods906Pr1b_Nb | `cs_first_low20(cs_first_low20(LogFloatCap, day_last(Open)), cs_first_low20(LogFloatCap, day_last(Open)))` |
| +0.73 | +0.73 | +0.92 | +1 | 20 | prods906Pr1a_Ea | `cs_last_low20(cross_mean(day_gini(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +0.72 | +0.72 | +3.15 | -1 | 5 | prods906M1_I0_open_search | `pow_2(cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)), cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High)))))` |
| +0.70 | +0.70 | +2.29 | +1 | 5 | prods906Pr1b_Nb | `cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Open))))` |
| +0.68 | +0.68 | +1.94 | -1 | 0 | prods906Pr1b_Nb | `cs_first_low20(LogFloatCap, day_sum(Low))` |
| +0.66 | +0.66 | +2.33 | +1 | 5 | prods906Pr1a_Ea | `cs_last_low05(cs_first_low20(day_last(Vwap), day_last(Vwap)), day_centroid(Amt))` |
| +0.54 | +0.54 | +1.35 | -1 | 0 | prods906Pr1a_Ea | `sigmoid(cs_first_low20(cs_first_low20(cross_mean(day_first(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), day_last(Vwap)))` |
| +0.50 | +0.50 | +1.86 | +1 | 20 | prods906Pr1a_Ea | `cs_first_low20(cross_mean(day_signed_ratio(Ret, Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |

## 共性:284 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.87 | 0.000 | 5 | +1.16 / -0.71 | `cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +1.75 | 0.000 | 15 | +0.97 / -0.77 | `cross_mean(day_centroid(Amt), 20)` |
| +1.67 | 0.000 | 26 | +0.84 / -0.84 | `day_centroid(Amt)` |
| +1.56 | 0.006 | 4 | +0.86 / -0.70 | `cross_mean(day_centroid(Amt), 3)` |
| +1.41 | 0.000 | 134 | +0.06 / -1.35 | `day_last(Vwap)` |
| +1.21 | 0.045 | 4 | +0.51 / -0.70 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| +1.20 | 0.015 | 5 | +0.50 / -0.70 | `cs_first_low20(LogFloatCap, day_last(Open))` |
| +1.20 | 0.006 | 6 | +0.49 / -0.71 | `day_last(High)` |
| +1.17 | 0.000 | 75 | +0.18 / -0.99 | `cs_first_low20(day_last(Vwap), day_last(Vwap))` |
| +1.17 | 0.015 | 6 | +0.46 / -0.71 | `day_last(Open)` |
| +1.11 | 0.000 | 22 | +0.34 / -0.77 | `cs_first_low20(day_last(Vwap), day_quantile(High))` |
| +1.10 | 0.022 | 6 | +0.40 / -0.71 | `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` |
| +1.09 | 0.051 | 5 | +0.39 / -0.70 | `day_quantile(Vwap)` |
| +1.05 | 0.100 | 4 | +0.35 / -0.70 | `cs_first_low20(day_last(Vwap), day_quantile(Vwap))` |
| +1.03 | 0.038 | 6 | +0.33 / -0.70 | `cs_first_low20(day_quantile(High), day_quantile(High))` |
| +0.91 | 0.028 | 8 | +0.20 / -0.71 | `pow_2(cs_first_low20(day_last(Vwap), day_quantile(High)))` |
| +0.89 | 0.000 | 44 | +0.07 / -0.82 | `day_quantile(High)` |
| +0.73 | 0.052 | 4 | +0.04 / -0.69 | `cross_mean(day_centroid(Amt), 15)` |
| +0.57 | 0.183 | 4 | -0.12 / -0.69 | `day_last(Close)` |
| +0.12 | 0.661 | 17 | -0.57 / -0.69 | `sub(LogFloatCap, LogFloatShares)` |

## 拆解(32 次评估)

### head score +1.80:`cs_first_low20(LogFloatCap, LogFloatCap)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|

### head score +1.62:`cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20)` | +1.32 | +1.32 | +3.22 | — | (子树本身) |
| sufficiency | `cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap)))` | +1.13 | +1.13 | +2.89 | — | (子树本身) |
| sufficiency | `cs_first_low20(day_last(Vwap), day_last(Vwap))` | +0.41 | +0.41 | +2.22 | — | (子树本身) |
| knockout | `cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20)` | +0.41 | +0.43 | +0.41 | +1.21 | `cs_first_low20(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| knockout | `cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap)))` | +1.48 | +1.48 | +1.75 | +0.14 | `cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| knockout | `cs_first_low20(day_last(Vwap), day_last(Vwap))` | +0.78 | +0.78 | +2.43 | +0.84 | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), day_last(Vwap)), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| knockout | `cs_first_low20(day_last(Vwap), day_last(Vwap))` | +1.19 | +1.19 | +3.40 | +0.43 | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20), day_last(Vwap))` |
| swap | `Amt->Volume` | +1.64 | +1.83 | +1.64 | — | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Volume), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| swap | `Vwap->Close` | +1.68 | +1.80 | +1.68 | — | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Close), day_last(Close))), 20), cs_first_low20(day_last(Close), day_last(Close)))` |
| window | `cross_mean@20->10` | +1.27 | +1.43 | +1.27 | — | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 10), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| window | `cross_mean@20->40` | +1.38 | +1.38 | +2.53 | — | `cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 40), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |

### head score +1.50:`cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 20))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(day_last(Vwap), day_last(Vwap))` | +0.41 | +0.41 | +2.22 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `day_last(Vwap)` | -1.33 | -1.33 | -0.41 | — | (子树本身) |
| knockout | `cs_first_low20(day_last(Vwap), day_last(Vwap))` | +0.68 | +0.68 | +1.93 | +0.81 | `cs_first_high40(day_last(Vwap), cross_mean(day_centroid(Amt), 20))` |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +0.56 | +0.56 | +2.23 | +0.93 | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), day_centroid(Amt))` |
| swap | `Vwap->Close` | +1.50 | +1.50 | +3.03 | — | `cs_first_high40(cs_first_low20(day_last(Close), day_last(Close)), cross_mean(day_centroid(Amt), 20))` |
| swap | `Amt->Volume` | +1.46 | +1.46 | +2.99 | — | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Volume), 20))` |
| window | `cross_mean@20->10` | +1.28 | +1.28 | +2.47 | — | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 10))` |
| window | `cross_mean@20->40` | +1.25 | +1.25 | +3.16 | — | `cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 40))` |

### head score +1.30:`cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3)` | +1.32 | +1.32 | +3.53 | — | (子树本身) |
| sufficiency | `cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` | +1.29 | +1.29 | +3.58 | — | (子树本身) |
| sufficiency | `cross_mean(day_centroid(Amt), 20)` | +1.34 | +1.72 | +1.34 | — | (子树本身) |
| sufficiency | `cs_first_low20(day_last(Vwap), day_last(Vwap))` | +0.41 | +0.41 | +2.22 | — | (子树本身) |
| knockout | `cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3)` | +1.29 | +1.29 | +3.58 | +0.01 | `cs_last_low20(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| knockout | `cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` | +1.25 | +1.25 | +3.65 | +0.05 | `cs_last_low20(cross_mean(cross_mean(day_centroid(Amt), 20), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| knockout | `cross_mean(day_centroid(Amt), 20)` | +1.26 | +1.26 | +3.00 | +0.04 | `cs_last_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| knockout | `cs_first_low20(day_last(Vwap), day_last(Vwap))` | +0.29 | +0.29 | +1.70 | +1.01 | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), day_last(Vwap)), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| swap | `Amt->Volume` | +1.30 | +1.30 | +3.61 | — | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Volume), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| swap | `Vwap->Close` | +1.28 | +1.28 | +3.58 | — | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Close), day_last(Close))), 3), cs_first_low20(day_last(Close), day_last(Close)))` |
| window | `cross_mean@3->2` | +1.33 | +1.33 | +3.51 | — | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 2), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |
| window | `cross_mean@3->6` | +1.20 | +1.20 | +3.38 | — | `cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 6), cs_first_low20(day_last(Vwap), day_last(Vwap)))` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(day_centroid(Amt), 20)` — ablation,自身 score +1.34(所在 head +1.50)
2. `cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3)` — ablation,自身 score +1.32(所在 head +1.30)
3. `cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20)` — ablation,自身 score +1.32(所在 head +1.62)
4. `cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` — ablation,自身 score +1.29(所在 head +1.30)
5. `cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap)))` — ablation,自身 score +1.13(所在 head +1.62)
6. `day_centroid(Amt)` — enrichment,均值差 +1.67,p 0.000
7. `cross_mean(day_centroid(Amt), 3)` — enrichment,均值差 +1.56,p 0.006
8. `day_last(Vwap)` — enrichment,均值差 +1.41,p 0.000
9. `cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))` — enrichment,均值差 +1.21,p 0.045
10. `cs_first_low20(LogFloatCap, day_last(Open))` — enrichment,均值差 +1.20,p 0.015
11. `day_last(High)` — enrichment,均值差 +1.20,p 0.006
12. `cs_first_low20(day_last(Vwap), day_last(Vwap))` — enrichment,均值差 +1.17,p 0.000
13. `day_last(Open)` — enrichment,均值差 +1.17,p 0.015
14. `cs_first_low20(day_last(Vwap), day_quantile(High))` — enrichment,均值差 +1.11,p 0.000
15. `cs_first_low20(cs_first_low20(day_last(Vwap), day_quantile(High)), day_quantile(High))` — enrichment,均值差 +1.10,p 0.022
16. `day_quantile(Vwap)` — enrichment,均值差 +1.09,p 0.051
17. `cs_first_low20(day_last(Vwap), day_quantile(Vwap))` — enrichment,均值差 +1.05,p 0.100
18. `cs_first_low20(day_quantile(High), day_quantile(High))` — enrichment,均值差 +1.03,p 0.038
19. `pow_2(cs_first_low20(day_last(Vwap), day_quantile(High)))` — enrichment,均值差 +0.91,p 0.028
20. `day_quantile(High)` — enrichment,均值差 +0.89,p 0.000
21. `cross_mean(day_centroid(Amt), 15)` — enrichment,均值差 +0.73,p 0.052

## 本组之前各轮的任务

- `prods906Pr1a_Ea`:核心 `cs_first_low20(day_last(Vwap), day_last(Vwap))`;评分 82,过线 28,入 heads 7;采样计数 {'c05_no_core': 820, 'c05_periphery_seen': 5}
  - score +1.62(train +1.81 valid +1.62):`cs_first_low20(cross_mean(cs_last_low20(day_centroid(Amt), cs_first_low20(day_last(Vwap), day_last(Vwap))), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))`
  - score +1.50(train +1.50 valid +3.04):`cs_first_high40(cs_first_low20(day_last(Vwap), day_last(Vwap)), cross_mean(day_centroid(Amt), 20))`
  - score +1.48(train +1.48 valid +1.75):`cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap)))`
  - score +1.48(train +1.48 valid +1.75):`sqrt(cs_first_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))))`
  - score +1.30(train +1.30 valid +3.56):`cs_last_low20(cross_mean(cs_last_low20(cross_mean(day_centroid(Amt), 20), cs_first_low20(day_last(Vwap), day_last(Vwap))), 3), cs_first_low20(day_last(Vwap), day_last(Vwap)))`
- `prods906Pr1b_Nb`:核心 `—`;评分 69,过线 9,入 heads 5;采样计数 {}
  - score +1.80(train +1.80 valid +2.56):`cs_first_low20(LogFloatCap, LogFloatCap)`
  - score +1.20(train +1.20 valid +2.53):`cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Open)))`
  - score +1.19(train +1.19 valid +2.55):`cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Close)))`
  - score +1.18(train +1.18 valid +2.55):`cs_first_low20(LogFloatCap, cs_first_low20(LogFloatCap, day_last(Vwap)))`
  - score +0.94(train +0.94 valid +2.69):`cs_first_low20(cs_first_low20(LogFloatCap, day_last(Open)), cs_first_low20(LogFloatCap, day_last(Open)))`

## 比原 head 好的拆解变体(R 候选)

(没有)
