# 定位:种子 909,P 组,第 3 轮(只含 train / valid)

快照:prods909M1_I0_open_search, prods909M2_I0_open_search, prods909M3_I0_open_search, prods909Pr1a_Na, prods909Pr1b_Nb, prods909Pr2a_Ea, prods909Pr2b_Eb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.51 | +1.51 | +2.41 | +1 | 20 | prods909Pr2a_Ea | `add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))` |
| +1.29 | +1.29 | +1.33 | +1 | 20 | prods909Pr2a_Ea | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))), ListAge)` |
| +1.22 | +1.22 | +2.74 | +1 | 20 | prods909M2_I0_open_search | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))))` |
| +1.11 | +1.11 | +2.60 | +1 | 5 | prods909Pr2a_Ea | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), ListAge)` |
| +0.99 | +0.99 | +2.76 | -1 | 5 | prods909M2_I0_open_search | `cs_last_high40(day_quantile(inv(Vwap)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` |
| +0.89 | +0.89 | +1.18 | -1 | 20 | prods909Pr2a_Ea | `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Volume), 1)), 1), 20))` |
| +0.67 | +0.67 | +2.71 | +1 | 20 | prods909Pr2a_Ea | `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Close), ts_delay(day_last(Close), 5)), 1), 20))` |
| +0.66 | +0.66 | +2.11 | +1 | 5 | prods909M2_I0_open_search | `cs_last_high40(day_quantile(inv(Vwap)), cs_first_high20(1, day_quantile(inv(Vwap))))` |
| +0.58 | +0.58 | +1.51 | +1 | 5 | prods909Pr1b_Nb | `cross_mean(day_wmean(is_lt(in_index(is_lt(in_index(Amt), 0.125)), 0.125), Amt), 30)` |
| +0.55 | +0.55 | +0.80 | -1 | 20 | prods909Pr2a_Ea | `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Close), ts_delay(ListAge, 1)), 1), 20))` |

## 共性:550 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.63 | 0.000 | 7 | +0.70 / -0.93 | `day_first(Close)` |
| +1.63 | 0.000 | 14 | +0.67 / -0.95 | `cs_rank(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` |
| +1.51 | 0.000 | 84 | +0.37 / -1.14 | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` |
| +1.43 | 0.000 | 100 | +0.25 / -1.17 | `day_quantile(inv(Vwap))` |
| +1.23 | 0.000 | 130 | +0.03 / -1.20 | `day_first(Volume)` |
| +1.21 | 0.005 | 5 | +0.29 / -0.92 | `cross_mean(abs_(day_min(Ret)), 20)` |
| +1.20 | 0.000 | 14 | +0.25 / -0.94 | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close)))` |
| +1.15 | 0.000 | 12 | +0.21 / -0.94 | `cross_mean(day_wmean(is_lt(in_index(Amt), 0.125), Amt), 30)` |
| +1.13 | 0.034 | 4 | +0.20 / -0.92 | `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))` |
| +1.10 | 0.018 | 4 | +0.17 / -0.92 | `abs_(day_quantile(inv(Close)))` |
| +1.05 | 0.000 | 19 | +0.10 / -0.95 | `day_quantile(inv(Close))` |
| +0.97 | 0.026 | 6 | +0.05 / -0.92 | `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` |
| +0.68 | 0.103 | 10 | -0.25 / -0.93 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |
| +0.62 | 0.056 | 15 | -0.31 / -0.93 | `day_first(Open)` |
| +0.52 | 0.000 | 59 | -0.45 / -0.97 | `day_wmean(is_lt(in_index(Amt), 0.125), Amt)` |
| +0.41 | 0.287 | 6 | -0.51 / -0.92 | `neg(cs_rank(neg(LogFloatShares)))` |
| +0.40 | 0.164 | 4 | -0.52 / -0.92 | `day_skew(Close)` |
| +0.39 | 0.085 | 13 | -0.53 / -0.92 | `day_es_ratio_lo(Close)` |
| +0.39 | 0.099 | 12 | -0.53 / -0.92 | `add(LogFloatShares, day_es_ratio_lo(Close))` |
| +0.39 | 0.208 | 6 | -0.53 / -0.92 | `ts_quantile_q50(add(LogFloatShares, day_es_ratio_lo(Close)), 5)` |

## 拆解(40 次评估)

### head score +1.51:`add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))` | +0.91 | +0.91 | +2.66 | — | (子树本身) |
| sufficiency | `cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30))` | -1.84 | -1.33 | -1.84 | — | (子树本身) |
| sufficiency | `cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)` | -1.84 | -1.33 | -1.84 | — | (子树本身) |
| sufficiency | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | +0.85 | +0.85 | +2.44 | — | (子树本身) |
| knockout | `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))` | +0.66 | +0.66 | +2.23 | +0.85 | `add(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))` |
| knockout | `mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5)` | -2.03 | -0.17 | -2.03 | +3.54 | `add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)))` |
| knockout | `cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30))` | +0.92 | +0.92 | +2.68 | +0.59 | `add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), mul(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30), 0.5))` |
| knockout | `sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)` | +1.51 | +1.51 | +2.41 | -0.00 | `add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(div(day_first(Open), ts_delay(day_last(Close), 1)), 20)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))` |
| swap | `Volume->Amt` | +1.07 | +1.07 | +2.69 | — | `add(cs_first_high20(cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))` |
| swap | `Vwap->Close` | +1.03 | +1.03 | +2.69 | — | `add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Close), 30)), 0.5))` |
| window | `cross_mean@20->10` | +1.05 | +1.05 | +2.70 | — | `add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 10)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))` |
| window | `cross_mean@20->40` | +1.67 | +1.67 | +1.93 | — | `add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))` |

### head score +1.29:`cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)))` | +1.41 | +1.41 | +1.69 | — | (子树本身) |
| sufficiency | `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))` | +0.91 | +0.91 | +2.66 | — | (子树本身) |
| sufficiency | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | +0.85 | +0.85 | +2.44 | — | (子树本身) |
| sufficiency | `div(day_first(Open), ts_delay(day_last(Close), 1))` | -3.94 | -1.84 | -3.94 | — | (子树本身) |
| knockout | `cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)))` | +1.44 | +1.44 | +2.06 | -0.16 | `cs_last_low20(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), ListAge)` |
| knockout | `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))` | +1.11 | +1.11 | +2.60 | +0.18 | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))), ListAge)` |
| knockout | `sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)` | +1.29 | +1.29 | +1.32 | +0.00 | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(div(day_first(Open), ts_delay(day_last(Close), 1)), 20))), ListAge)` |
| knockout | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | +1.29 | +1.29 | +1.33 | +0.00 | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(day_quantile(inv(Vwap)), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))), ListAge)` |
| swap | `Volume->Amt` | +1.19 | +1.19 | +1.36 | — | `cs_last_low20(cs_first_high20(mul(day_first(Amt), 1), cs_first_high20(cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))), ListAge)` |
| swap | `Vwap->Close` | +1.29 | +1.29 | +1.33 | — | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))), ListAge)` |
| window | `cross_mean@20->10` | +0.61 | +0.61 | +0.92 | — | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 10))), ListAge)` |
| window | `cross_mean@20->40` | +1.92 | +2.06 | +1.92 | — | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40))), ListAge)` |

### head score +1.22:`cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap))))` | +0.74 | +0.74 | +2.29 | — | (子树本身) |
| sufficiency | `cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))` | +0.91 | +0.91 | +2.69 | — | (子树本身) |
| sufficiency | `abs_(day_min(Ret))` | -2.96 | -1.98 | -2.96 | — | (子树本身) |
| knockout | `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap))))` | -1.65 | -1.65 | -0.96 | +2.87 | `cs_last_high40(abs_(day_min(Ret)), abs_(day_min(Ret)))` |
| knockout | `cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))` | -2.43 | -0.80 | -2.43 | +3.65 | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), day_quantile(inv(Vwap))))` |
| knockout | `abs_(day_min(Ret))` | -0.23 | -0.23 | +1.13 | +1.45 | `cs_last_high40(day_min(Ret), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))))` |
| knockout | `abs_(day_min(Ret))` | -0.61 | -0.61 | +0.66 | +1.83 | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(day_min(Ret), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))))` |
| swap | `Amt->Volume` | +1.10 | +1.10 | +2.41 | — | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))))` |
| swap | `Vwap->Close` | +1.21 | +1.21 | +2.73 | — | `cs_last_high40(abs_(day_min(Ret)), cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Close)))))` |

### head score +1.11:`cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), ListAge)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | +0.85 | +0.85 | +2.44 | — | (子树本身) |
| sufficiency | `day_quantile(inv(Vwap))` | -1.35 | -1.35 | -0.41 | — | (子树本身) |
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` | -0.93 | -0.93 | +0.87 | +2.04 | `cs_last_low20(day_quantile(inv(Vwap)), ListAge)` |
| knockout | `mul(day_first(Volume), 1)` | +1.11 | +1.11 | +2.60 | +0.00 | `cs_last_low20(cs_first_high20(day_first(Volume), day_quantile(inv(Vwap))), ListAge)` |
| swap | `Volume->Amt` | +1.22 | +1.22 | +2.84 | — | `cs_last_low20(cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap))), ListAge)` |
| swap | `Vwap->Close` | +1.09 | +1.09 | +2.59 | — | `cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close))), ListAge)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)))` — ablation,自身 score +1.41(所在 head +1.29)
2. `cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap)))` — ablation,自身 score +0.91(所在 head +1.22)
3. `cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))` — ablation,自身 score +0.91(所在 head +1.51)
4. `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))` — ablation,自身 score +0.85(所在 head +1.29)
5. `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap))))` — ablation,自身 score +0.74(所在 head +1.22)
6. `day_first(Close)` — enrichment,均值差 +1.63,p 0.000
7. `cs_rank(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` — enrichment,均值差 +1.63,p 0.000
8. `day_quantile(inv(Vwap))` — enrichment,均值差 +1.43,p 0.000
9. `day_first(Volume)` — enrichment,均值差 +1.23,p 0.000
10. `cross_mean(abs_(day_min(Ret)), 20)` — enrichment,均值差 +1.21,p 0.005
11. `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Close)))` — enrichment,均值差 +1.20,p 0.000
12. `cross_mean(day_wmean(is_lt(in_index(Amt), 0.125), Amt), 30)` — enrichment,均值差 +1.15,p 0.000
13. `abs_(day_quantile(inv(Close)))` — enrichment,均值差 +1.10,p 0.018
14. `day_quantile(inv(Close))` — enrichment,均值差 +1.05,p 0.000
15. `cs_last_high40(abs_(day_min(Ret)), cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))))` — enrichment,均值差 +0.97,p 0.026
16. `day_first(Open)` — enrichment,均值差 +0.62,p 0.056
17. `day_wmean(is_lt(in_index(Amt), 0.125), Amt)` — enrichment,均值差 +0.52,p 0.000
18. `day_es_ratio_lo(Close)` — enrichment,均值差 +0.39,p 0.085
19. `add(LogFloatShares, day_es_ratio_lo(Close))` — enrichment,均值差 +0.39,p 0.099

## 本组之前各轮的任务

- `prods909Pr1a_Na`:核心 `—`;评分 95,过线 0,入 heads 0;采样计数 {}
  - score +0.37(train +0.37 valid +0.47):`div(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), cross_mean(day_max(in_pct(Close, 60)), 60))`
  - score +0.20(train +0.20 valid +0.46):`div(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), cross_mean(day_max(in_pct(Close, 5)), 60))`
  - score +0.20(train +0.20 valid +0.45):`div(cross_mean(day_max(in_pct(Close, 5)), 60), ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50))`
  - score -0.01(train -0.01 valid +0.08):`div(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), ts_std(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50))`
  - score -0.16(train -0.16 valid +0.09):`mul(ts_max(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), 50), cross_mean(day_max(in_pct(Close, 5)), 60))`
- `prods909Pr1b_Nb`:核心 `—`;评分 82,过线 9,入 heads 1;采样计数 {}
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(is_lt(in_index(Amt), 0.125)), 0.125), Amt), 30)`
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(in_index(Amt)), 0.125), Amt), 30)`
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(cross_quantile_q50(Open, 30)), 0.125), Amt), 30)`
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(Close), 0.125), Amt), 30)`
  - score +0.58(train +0.58 valid +1.51):`cross_mean(day_wmean(is_lt(in_index(in_median(Amt)), 0.125), Amt), 30)`
- `prods909Pr2a_Ea`:核心 `cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))`;评分 95,过线 47,入 heads 6;采样计数 {'c05_no_core': 1193, 'mutation_refused': 8, 'c05_periphery_seen': 8}
  - score +1.51(train +1.51 valid +2.41):`add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))`
  - score +1.29(train +1.29 valid +1.33):`cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20))), ListAge)`
  - score +1.15(train +1.15 valid +2.12):`add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), mul(cs_rank(cross_mean(day_wmean(is_lt(in_index(Amt), 0.125), Amt), 30)), 0.5))`
  - score +1.11(train +1.11 valid +2.60):`cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), ListAge)`
  - score +1.11(train +1.11 valid +2.60):`cs_last_low20(cs_first_high20(mul(cs_rank(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap)))), 1), day_quantile(inv(Vwap))), ListAge)`
- `prods909Pr2b_Eb`:核心 `day_wmean(is_lt(in_index(Amt), 0.125), Amt)`;评分 70,过线 0,入 heads 0;采样计数 {'c05_no_core': 835, 'c05_periphery_seen': 11}
  - score +0.21(train +0.21 valid +1.95):`cs_first_high20(cross_mean(day_wmean(is_lt(in_index(Amt), 0.125), Amt), 30), day_quantile(inv(Vwap)))`
  - score +0.21(train +0.21 valid +1.95):`log(pow_2(cs_first_high20(cross_mean(day_wmean(is_lt(in_index(Amt), 0.125), Amt), 30), day_quantile(inv(Vwap)))))`
  - score +0.21(train +0.21 valid +1.78):`cs_first_high20(cross_mean(day_wmean(is_lt(in_index(Amt), 0.125), Amt), 3), day_quantile(inv(Vwap)))`
  - score +0.14(train +0.14 valid +0.22):`log(log(day_wmean(is_lt(in_index(Amt), 0.125), Amt)))`
  - score +0.14(train +0.14 valid +0.22):`log(pow_2(log(pow_2(day_wmean(is_lt(in_index(Amt), 0.125), Amt)))))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.63(window cross_mean@20->40):`cs_last_low20(cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40))), ListAge)`
- 增益 +0.17(window cross_mean@20->40):`add(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 40)), mul(cs_rank(cross_quantile_q75(day_wmean(is_lt(in_index(Amt), 0.125), Vwap), 30)), 0.5))`
- 增益 +0.16(knockout cs_first_high20(mul(day_first(Volume), 1), cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)))):`cs_last_low20(cs_first_high20(cs_first_high20(mul(day_first(Volume), 1), day_quantile(inv(Vwap))), cross_mean(sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1), 20)), ListAge)`
- 增益 +0.11(swap Volume->Amt):`cs_last_low20(cs_first_high20(mul(day_first(Amt), 1), day_quantile(inv(Vwap))), ListAge)`
