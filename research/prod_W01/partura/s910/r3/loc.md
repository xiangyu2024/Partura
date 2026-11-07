# 定位:种子 910,P 组,第 3 轮(只含 train / valid)

快照:prods910M1_I0_open_search, prods910M2_I0_open_search, prods910M3_I0_open_search, prods910Pr1a_Na, prods910Pr1b_Eb, prods910Pr2a_Na, prods910Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(22 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.85 | +1.85 | +2.58 | -1 | 5 | prods910M1_I0_open_search | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` |
| +1.58 | +1.58 | +2.62 | -1 | 0 | prods910Pr2a_Na | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 241)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares))), ListAge)` |
| +1.53 | +1.53 | +2.40 | -1 | 20 | prods910Pr1b_Eb | `cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))` |
| +1.50 | +1.50 | +2.21 | -1 | 5 | prods910Pr2a_Na | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares)), ListAge)` |
| +1.50 | +1.50 | +2.58 | -1 | 5 | prods910Pr2b_Nb | `cs_first_high20(LogFloatCap, sub(sub(LogTotalCap, LogFloatCap), LogFloatCap))` |
| +1.45 | +1.45 | +1.82 | -1 | 5 | prods910Pr1a_Na | `cs_first_low20(cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap), ListAge)` |
| +1.44 | +1.44 | +2.17 | -1 | 5 | prods910Pr2a_Na | `cs_first_low20(cs_first_low20(LogFloatCap, day_sum(Volume)), ListAge)` |
| +1.42 | +1.42 | +2.62 | -1 | 5 | prods910M1_I0_open_search | `cs_first_low20(cs_first_low20(LogFloatCap, day_last(High)), ListAge)` |
| +1.38 | +1.38 | +2.44 | -1 | 0 | prods910Pr1a_Na | `cs_first_low20(cs_first_low20(cross_mean(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60)), ListAge)` |
| +1.34 | +1.34 | +2.50 | +1 | 0 | prods910Pr1a_Na | `cs_first_low20(cross_mean(LogFloatCap, 60), cross_mean(day_sum(Amt), 60))` |
| +1.19 | +1.19 | +2.51 | -1 | 0 | prods910Pr2b_Nb | `cs_first_high20(LogFloatCap, sub(LogTotalCap, LogFloatCap))` |
| +1.07 | +1.07 | +2.92 | -1 | 0 | prods910Pr2a_Na | `cs_first_low20(cs_first_low20(LogFloatCap, sub(log(cross_mean(cross_mean(day_sum(Volume), 60), 3)), LogFloatShares)), ListAge)` |
| +0.95 | +0.95 | +2.47 | -1 | 0 | prods910Pr2a_Na | `cs_first_low20(cs_first_low20(LogFloatCap, sub(log(cross_mean(cross_mean(day_sum(Volume), 60), 60)), LogFloatShares)), sub(log(cross_mean(cross_mean(day_sum(Volume), 60), 3)), LogFloatShares))` |
| +0.94 | +0.94 | +1.94 | -1 | 5 | prods910Pr2a_Na | `cs_first_low20(cs_first_low20(cs_first_low40(LogFloatCap, day_sum(Volume)), sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares)), ListAge)` |
| +0.80 | +0.80 | +1.83 | -1 | 20 | prods910Pr1b_Eb | `cs_first_low20(cs_first_high20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_stddev(log(ts_regres(day_skew(Ret), cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), 10)), 10))` |
| +0.79 | +0.79 | +1.63 | +1 | 5 | prods910Pr2b_Nb | `cs_first_low20(LogFloatCap, sub(LogFloatCap, LogFloatShares))` |
| +0.76 | +0.84 | +0.76 | -1 | 20 | prods910Pr2a_Na | `cs_first_low20(cs_first_low20(day_sum(Volume), sub(log(cross_mean(cross_mean(day_sum(Volume), 60), 60)), LogFloatShares)), ListAge)` |
| +0.76 | +0.83 | +0.76 | +1 | 20 | prods910Pr1a_Na | `cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), day_sum(Amt))` |
| +0.72 | +0.72 | +1.21 | +1 | 5 | prods910Pr1a_Na | `cs_first_low20(cross_mean(day_sum(Amt), 60), cross_mean(day_es_ratio_lo(Amt), 60))` |
| +0.70 | +0.70 | +0.97 | -1 | 0 | prods910Pr2b_Nb | `cs_first_high20(LogFloatCap, cs_flip_by_state(LogFloatCap, sub(LogTotalCap, LogFloatCap)))` |
| +0.60 | +0.60 | +1.42 | +1 | 5 | prods910Pr2a_Na | `cs_first_low20(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares)), sub(LogFloatCap, LogFloatShares))` |
| +0.55 | +0.55 | +3.11 | -1 | 5 | prods910Pr1b_Eb | `cs_first_low20(cs_first_high20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_delta(log(LogFloatCap), 60))` |

## 共性:587 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.24 | 0.000 | 9 | +1.52 / -0.71 | `ts_quantile_q75(LogFloatCap, 10)` |
| +2.01 | 0.002 | 5 | +1.32 / -0.69 | `cross_fangzheng(ts_quantile_q75(LogFloatCap, 10), 3)` |
| +2.01 | 0.003 | 4 | +1.32 / -0.69 | `cross_fangzheng(LogFloatCap, 3)` |
| +2.00 | 0.000 | 6 | +1.30 / -0.70 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 1)` |
| +1.52 | 0.002 | 9 | +0.82 / -0.70 | `cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3)` |
| +1.38 | 0.018 | 4 | +0.69 / -0.69 | `cs_regres(day_q_stat_std(Amt), day_hurst(Close))` |
| +1.38 | 0.018 | 4 | +0.69 / -0.69 | `cs_regres(day_q_stat_std(Amt), pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close))))` |
| +1.38 | 0.018 | 4 | +0.69 / -0.69 | `pow_05(cs_regres(day_q_stat_std(Amt), pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close)))))` |
| +1.38 | 0.018 | 4 | +0.69 / -0.69 | `pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close)))` |
| +1.37 | 0.005 | 6 | +0.68 / -0.69 | `sub(log(cross_mean(cross_mean(day_sum(Volume), 60), 60)), LogFloatShares)` |
| +1.37 | 0.005 | 6 | +0.68 / -0.69 | `cross_mean(cross_mean(day_sum(Volume), 60), 60)` |
| +1.37 | 0.005 | 6 | +0.68 / -0.69 | `log(cross_mean(cross_mean(day_sum(Volume), 60), 60))` |
| +1.26 | 0.044 | 4 | +0.57 / -0.68 | `cs_first_low20(cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3), ts_quantile_q75(LogFloatCap, 1))` |
| +1.24 | 0.035 | 4 | +0.56 / -0.68 | `cs_regres(day_durbin_watson(Amt), ts_delta(log(day_last(Close)), 60))` |
| +1.24 | 0.035 | 4 | +0.56 / -0.68 | `pow_2(cs_regres(day_durbin_watson(Amt), ts_delta(log(day_last(Close)), 60)))` |
| +1.24 | 0.015 | 6 | +0.55 / -0.69 | `cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))` |
| +1.23 | 0.000 | 41 | +0.47 / -0.76 | `day_sum(Volume)` |
| +1.14 | 0.018 | 6 | +0.45 / -0.69 | `day_q_stat_std(Amt)` |
| +1.10 | 0.000 | 21 | +0.38 / -0.72 | `day_hurst(Close)` |
| +1.08 | 0.015 | 6 | +0.39 / -0.69 | `cs_first_high40(day_durbin_watson(Amt), day_hurst(Close))` |

## 拆解(31 次评估)

### head score +1.58:`cs_first_low20(cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 241)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares))), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 241)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares)))` | +1.40 | +1.40 | +3.09 | — | (子树本身) |
| sufficiency | `add(log(cross_mean(day_sum(Volume), 241)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares))` | -2.59 | -1.01 | -2.59 | — | (子树本身) |
| sufficiency | `sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares)` | -1.82 | -1.82 | -1.58 | — | (子树本身) |
| sufficiency | `log(cross_mean(day_sum(Volume), 241))` | -0.82 | -0.82 | +0.11 | — | (子树本身) |
| knockout | `cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 241)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares)))` | +0.12 | +0.12 | +2.38 | +1.46 | `cs_first_low20(LogFloatCap, ListAge)` |
| knockout | `add(log(cross_mean(day_sum(Volume), 241)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares))` | +1.28 | +1.28 | +2.42 | +0.30 | `cs_first_low20(cs_first_low20(LogFloatCap, log(cross_mean(day_sum(Volume), 241))), ListAge)` |
| knockout | `sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares)` | +1.28 | +1.28 | +2.42 | +0.30 | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 241)), log(cross_mean(day_sum(Volume), 241)))), ListAge)` |
| knockout | `log(cross_mean(day_sum(Volume), 241))` | +1.28 | +1.28 | +2.42 | +0.30 | `cs_first_low20(cs_first_low20(LogFloatCap, add(cross_mean(day_sum(Volume), 241), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares))), ListAge)` |
| swap | `Volume->Amt` | +1.21 | +1.21 | +2.33 | — | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Amt), 241)), sub(log(cross_mean(day_sum(Amt), 241)), LogFloatShares))), ListAge)` |
| window | `cross_mean@241->120` | +1.55 | +1.55 | +2.44 | — | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 120)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares))), ListAge)` |
| window | `cross_mean@241->482` | +1.60 | +1.60 | +2.65 | — | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 482)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares))), ListAge)` |

### head score +1.50:`cs_first_low20(cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares)), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares))` | +1.63 | +1.63 | +2.34 | — | (子树本身) |
| sufficiency | `add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares)` | -2.05 | -0.39 | -2.05 | — | (子树本身) |
| sufficiency | `log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares)))` | +0.86 | +0.86 | +2.66 | — | (子树本身) |
| sufficiency | `cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))` | +0.86 | +0.86 | +2.66 | — | (子树本身) |
| knockout | `cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares))` | +0.12 | +0.12 | +2.38 | +1.38 | `cs_first_low20(LogFloatCap, ListAge)` |
| knockout | `add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares)` | +2.04 | +2.04 | +2.28 | -0.54 | `cs_first_low20(cs_first_low20(LogFloatCap, log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares)))), ListAge)` |
| knockout | `log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares)))` | +1.24 | +1.24 | +2.29 | +0.26 | `cs_first_low20(cs_first_low20(LogFloatCap, add(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares)), LogFloatShares)), ListAge)` |
| knockout | `cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))` | +1.16 | +1.16 | +2.30 | +0.34 | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(LogFloatCap), LogFloatShares)), ListAge)` |
| swap | `Volume->Amt` | +1.44 | +1.44 | +2.34 | — | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Amt), 60)), LogFloatShares))), LogFloatShares)), ListAge)` |
| window | `cross_mean@60->30` | +1.44 | +1.44 | +2.17 | — | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 30)), LogFloatShares))), LogFloatShares)), ListAge)` |
| window | `cross_mean@60->120` | +1.52 | +1.52 | +2.24 | — | `cs_first_low20(cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 120)), LogFloatShares))), LogFloatShares)), ListAge)` |

### head score +1.50:`cs_first_high20(LogFloatCap, sub(sub(LogTotalCap, LogFloatCap), LogFloatCap))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(sub(LogTotalCap, LogFloatCap), LogFloatCap)` | -1.49 | -1.49 | -1.16 | — | (子树本身) |
| sufficiency | `sub(LogTotalCap, LogFloatCap)` | -0.35 | -0.35 | +0.37 | — | (子树本身) |
| knockout | `sub(sub(LogTotalCap, LogFloatCap), LogFloatCap)` | +1.19 | +1.19 | +2.51 | +0.31 | `cs_first_high20(LogFloatCap, sub(LogTotalCap, LogFloatCap))` |

### head score +1.45:`cs_first_low20(cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap)` | +0.89 | +0.89 | +1.59 | — | (子树本身) |
| sufficiency | `cs_last_low10(neg(LogFloatCap), LogFloatCap)` | +0.66 | +0.66 | +1.26 | — | (子树本身) |
| sufficiency | `neg(LogFloatCap)` | -5.03 | -3.60 | -5.03 | — | (子树本身) |
| knockout | `cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap)` | -1.99 | -0.08 | -1.99 | +3.44 | `cs_first_low20(cs_last_low10(neg(LogFloatCap), LogFloatCap), ListAge)` |
| knockout | `cs_last_low10(neg(LogFloatCap), LogFloatCap)` | +1.45 | +1.45 | +1.82 | +0.01 | `cs_first_low20(cs_bucket_rank(neg(LogFloatCap), LogFloatCap), ListAge)` |
| knockout | `neg(LogFloatCap)` | +0.39 | +0.39 | +1.88 | +1.06 | `cs_first_low20(cs_bucket_rank(cs_last_low10(LogFloatCap, LogFloatCap), LogFloatCap), ListAge)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares))` — ablation,自身 score +1.63(所在 head +1.50)
2. `cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 241)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares)))` — ablation,自身 score +1.40(所在 head +1.58)
3. `cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap)` — ablation,自身 score +0.89(所在 head +1.45)
4. `ts_quantile_q75(LogFloatCap, 10)` — enrichment,均值差 +2.24,p 0.000
5. `cross_fangzheng(ts_quantile_q75(LogFloatCap, 10), 3)` — enrichment,均值差 +2.01,p 0.002
6. `cross_fangzheng(LogFloatCap, 3)` — enrichment,均值差 +2.01,p 0.003
7. `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 1)` — enrichment,均值差 +2.00,p 0.000
8. `cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3)` — enrichment,均值差 +1.52,p 0.002
9. `cs_regres(day_q_stat_std(Amt), day_hurst(Close))` — enrichment,均值差 +1.38,p 0.018
10. `cs_regres(day_q_stat_std(Amt), pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close))))` — enrichment,均值差 +1.38,p 0.018
11. `pow_05(cs_regres(day_q_stat_std(Amt), pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close)))))` — enrichment,均值差 +1.38,p 0.018
12. `pow_05(cs_regres(day_q_stat_std(Amt), day_hurst(Close)))` — enrichment,均值差 +1.38,p 0.018
13. `sub(log(cross_mean(cross_mean(day_sum(Volume), 60), 60)), LogFloatShares)` — enrichment,均值差 +1.37,p 0.005
14. `cross_mean(cross_mean(day_sum(Volume), 60), 60)` — enrichment,均值差 +1.37,p 0.005
15. `log(cross_mean(cross_mean(day_sum(Volume), 60), 60))` — enrichment,均值差 +1.37,p 0.005
16. `cs_first_low20(cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3), ts_quantile_q75(LogFloatCap, 1))` — enrichment,均值差 +1.26,p 0.044
17. `cs_regres(day_durbin_watson(Amt), ts_delta(log(day_last(Close)), 60))` — enrichment,均值差 +1.24,p 0.035
18. `pow_2(cs_regres(day_durbin_watson(Amt), ts_delta(log(day_last(Close)), 60)))` — enrichment,均值差 +1.24,p 0.035
19. `cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))` — enrichment,均值差 +1.24,p 0.015
20. `day_sum(Volume)` — enrichment,均值差 +1.23,p 0.000
21. `day_q_stat_std(Amt)` — enrichment,均值差 +1.14,p 0.018
22. `day_hurst(Close)` — enrichment,均值差 +1.10,p 0.000
23. `cs_first_high40(day_durbin_watson(Amt), day_hurst(Close))` — enrichment,均值差 +1.08,p 0.015
24. `neg(LogFloatCap)` — enrichment,均值差 +1.07,p 0.012
25. `day_sum(Open)` — enrichment,均值差 +1.06,p 0.020
26. `cs_robust_z(day_sum(Open))` — enrichment,均值差 +1.06,p 0.020
27. `cs_first_low40(sqrt(day_quantile_q25(Open)), day_sum(High))` — enrichment,均值差 +1.06,p 0.036
28. `sqrt(day_sum(High))` — enrichment,均值差 +1.05,p 0.051
29. `cs_last_low10(neg(LogFloatCap), LogFloatCap)` — enrichment,均值差 +1.04,p 0.054
30. `cross_mean(day_sum(Volume), 60)` — enrichment,均值差 +1.04,p 0.000
31. `pow_05(cs_first_high40(day_durbin_watson(Amt), day_hurst(Close)))` — enrichment,均值差 +1.03,p 0.031
32. `cs_first_high20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` — enrichment,均值差 +1.00,p 0.034
33. `ts_quantile_q75(LogFloatCap, 1)` — enrichment,均值差 +1.00,p 0.000
34. `day_durbin_watson(Amt)` — enrichment,均值差 +0.96,p 0.002
35. `ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)` — enrichment,均值差 +0.91,p 0.000
36. `ts_delta(log(ts_regres(day_skew(Ret), day_autocorr_n1(Ret), 10)), 60)` — enrichment,均值差 +0.88,p 0.072
37. `log(ts_regres(day_skew(Ret), day_autocorr_n1(Ret), 10))` — enrichment,均值差 +0.88,p 0.072
38. `log(cross_mean(day_sum(Volume), 60))` — enrichment,均值差 +0.84,p 0.003
39. `ts_quantile_q75(ts_quantile_q75(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), 1), 1)` — enrichment,均值差 +0.78,p 0.095
40. `ts_quantile_q75(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), 1)` — enrichment,均值差 +0.78,p 0.095
41. `sub(LogTotalCap, LogFloatCap)` — enrichment,均值差 +0.78,p 0.018
42. `ts_regres(day_skew(Ret), day_autocorr_n1(Ret), 10)` — enrichment,均值差 +0.77,p 0.047
43. `sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares)` — enrichment,均值差 +0.76,p 0.015
44. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.67,p 0.049
45. `day_skew(Ret)` — enrichment,均值差 +0.66,p 0.014
46. `sqrt(sqrt(day_quantile_q25(Open)))` — enrichment,均值差 +0.63,p 0.088
47. `cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3)` — enrichment,均值差 +0.62,p 0.000
48. `cross_mean(day_sum(Amt), 60)` — enrichment,均值差 +0.61,p 0.086
49. `cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3)` — enrichment,均值差 +0.57,p 0.000
50. `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` — enrichment,均值差 +0.54,p 0.001
51. `sqrt(day_quantile_q25(Open))` — enrichment,均值差 +0.41,p 0.046
52. `day_autocorr_n1(Ret)` — enrichment,均值差 +0.41,p 0.084
53. `day_sum(High)` — enrichment,均值差 +0.36,p 0.066
54. `day_quantile_q25(Open)` — enrichment,均值差 +0.36,p 0.072

## 本组之前各轮的任务

- `prods910Pr1a_Na`:核心 `—`;评分 89,过线 10,入 heads 5;采样计数 {}
  - score +1.34(train +1.34 valid +2.50):`cs_first_low20(cross_mean(LogFloatCap, 60), cross_mean(day_sum(Amt), 60))`
  - score +0.89(train +0.89 valid +1.59):`cs_bucket_rank(cs_last_low10(neg(LogFloatCap), LogFloatCap), LogFloatCap)`
  - score +0.89(train +0.89 valid +1.59):`cs_bucket_rank(cs_last_low10(neg(LogFloatCap), cs_last_low10(neg(LogFloatCap), LogFloatCap)), LogFloatCap)`
  - score +0.88(train +0.88 valid +1.61):`cs_bucket_rank(LogFloatCap, LogFloatCap)`
  - score +0.83(train +0.83 valid +2.26):`cs_first_low20(cross_mean(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))`
- `prods910Pr1b_Eb`:核心 `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))`;评分 113,过线 29,入 heads 3;采样计数 {'c05_no_core': 1960, 'c05_skeleton': 8, 'mutation_refused': 3}
  - score +1.53(train +1.53 valid +2.40):`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), neg(cs_regres(day_skew(Ret), day_hurst(Close))))))`
  - score +1.46(train +1.46 valid +2.31):`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_first_high40(day_centroid(Close), day_hurst(Close))))`
  - score +1.46(train +1.46 valid +2.46):`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_last_high20(day_durbin_watson(Amt), day_hurst(Close))))`
  - score +1.39(train +1.39 valid +2.16):`cs_last_low20(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_regres(day_skew(Ret), pow_05(cs_regres(day_skew(Ret), day_hurst(Volume))))))`
  - score +1.36(train +1.36 valid +2.16):`cs_last_low20(cs_first_low20(cross_fangzheng(cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)), pow_05(cs_first_high40(day_centroid(Close), day_zero_ratio(Close))))`
- `prods910Pr2a_Na`:核心 `—`;评分 102,过线 27,入 heads 8;采样计数 {}
  - score +1.58(train +1.58 valid +2.62):`cs_first_low20(cs_first_low20(LogFloatCap, add(log(cross_mean(day_sum(Volume), 241)), sub(log(cross_mean(day_sum(Volume), 241)), LogFloatShares))), ListAge)`
  - score +1.50(train +1.50 valid +2.21):`cs_first_low20(cs_first_low20(LogFloatCap, add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares)), ListAge)`
  - score +1.44(train +1.44 valid +2.17):`cs_first_low20(cs_first_low20(LogFloatCap, day_sum(Volume)), ListAge)`
  - score +1.34(train +1.34 valid +2.59):`cs_first_low20(cs_first_low20(LogFloatCap, sub(cross_mean(day_sum(Volume), 60), LogFloatShares)), ListAge)`
  - score +1.22(train +1.22 valid +2.52):`cs_first_low20(LogFloatCap, day_sum(Volume))`
- `prods910Pr2b_Nb`:核心 `—`;评分 76,过线 11,入 heads 4;采样计数 {}
  - score +1.50(train +1.50 valid +2.58):`cs_first_high20(LogFloatCap, sub(sub(LogTotalCap, LogFloatCap), LogFloatCap))`
  - score +1.50(train +1.50 valid +2.58):`cs_first_high20(cs_first_high20(LogFloatCap, sub(sub(LogTotalCap, LogFloatCap), LogFloatCap)), sub(sub(LogTotalCap, LogFloatCap), LogFloatCap))`
  - score +1.50(train +1.50 valid +2.58):`cs_first_high20(LogFloatCap, cs_first_high20(LogFloatCap, sub(sub(LogTotalCap, LogFloatCap), LogFloatCap)))`
  - score +1.26(train +1.26 valid +2.48):`cs_first_high20(LogFloatCap, sub(cs_first_high20(LogFloatCap, sub(LogTotalCap, LogFloatCap)), LogFloatCap))`
  - score +1.19(train +1.19 valid +2.51):`cs_first_high20(LogFloatCap, sub(LogTotalCap, LogFloatCap))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.54(knockout add(log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares))), LogFloatShares)):`cs_first_low20(cs_first_low20(LogFloatCap, log(cs_first_low20(LogFloatCap, sub(log(cross_mean(day_sum(Volume), 60)), LogFloatShares)))), ListAge)`
