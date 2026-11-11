# 定位:种子 2019,P 组,第 3 轮(只含 train / valid)

快照:prods2019M1_I0_open_search, prods2019M2_I0_open_search, prods2019M3_I0_open_search, prods2019Pr1a_Ea, prods2019Pr1b_Nb, prods2019Pr2a_Ea, prods2019Pr2b_Nb;已生效的 R 替换 5 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(12 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.05 | +1.05 | +1.14 | +1 | 5 | prods2019Pr2a_Ea | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), 1), day_sum(Ret), 241)` |
| +0.95 | +0.95 | +0.99 | +1 | 20 | prods2019Pr2a_Ea | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), 1), day_sum(Ret), 241)` |
| +0.70 | +0.70 | +0.83 | +1 | 5 | prods2019Pr2a_Ea | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_sum(Ret), 60)` |
| +0.21 | +0.43 | +0.21 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 150))` |
| +0.20 | +0.20 | +0.31 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 150))` |
| +0.07 | +0.07 | +0.54 | +1 | 0 | prods2019M2_I0_open_search | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.27 | -0.27 | +0.23 | +1 | 5 | prods2019M2_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.31 | +0.05 | -0.31 | +1 | 0 | prods2019M2_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.46 | -0.46 | +0.04 | +1 | 0 | prods2019M3_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(day_mean(High), mul(day_mean(High), signedpower(cross_quantile_q75(cross_corr(day_mean(High), mul(day_mean(High), day_skew(Volume)), 10), 241))), 10), 241))` |
| -0.47 | -0.47 | -0.36 | +1 | 5 | prods2019M3_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(day_mean(High), mul(day_mean(High), day_skew(Volume)), 5), 241))` |
| -0.56 | -0.56 | -0.03 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 241))` |
| -0.64 | -0.64 | -0.18 | +1 | 0 | prods2019M3_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(day_mean(Vwap), mul(day_mean(High), day_skew(Volume)), 10), 241))` |

## 共性:307 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.38 | 0.000 | 13 | +0.41 / -1.97 | `day_last(Volume)` |
| +2.14 | 0.000 | 9 | +0.21 / -1.93 | `mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume))` |
| +1.75 | 0.003 | 6 | -0.15 / -1.91 | `cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1)` |
| +1.73 | 0.000 | 32 | -0.33 / -2.05 | `cross_mean(mul(day_mean(High), day_skew(Volume)), 5)` |
| +1.70 | 0.000 | 27 | -0.32 / -2.02 | `cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1)` |
| +1.49 | 0.000 | 97 | -0.85 / -2.34 | `mul(day_mean(High), day_skew(Volume))` |
| +1.41 | 0.013 | 4 | -0.48 / -1.89 | `mul(cross_delay(mul(day_mean(High), day_skew(Volume)), 1), day_skew(Volume))` |
| +1.28 | 0.000 | 70 | -0.88 / -2.16 | `day_sum(Ret)` |
| +1.14 | 0.000 | 115 | -1.16 / -2.30 | `day_mean(High)` |
| +1.11 | 0.000 | 22 | -0.84 / -1.95 | `cross_delay(mul(day_mean(High), day_skew(Volume)), 1)` |
| +1.08 | 0.000 | 207 | -1.52 / -2.60 | `day_skew(Volume)` |
| +0.97 | 0.023 | 7 | -0.92 / -1.89 | `day_flat_run_max(Ret)` |
| +0.95 | 0.061 | 4 | -0.93 / -1.88 | `day_open(Close)` |
| +0.89 | 0.056 | 5 | -0.99 / -1.89 | `div(day_close(Close), cross_delay(day_close(Close), 5))` |
| +0.87 | 0.058 | 5 | -1.02 / -1.89 | `day_quantile(Vwap)` |
| +0.85 | 0.010 | 11 | -1.05 / -1.90 | `day_argmin(Open)` |
| +0.80 | 0.098 | 4 | -1.09 / -1.88 | `cross_delta(day_quantile(Vwap), 3)` |
| +0.80 | 0.098 | 4 | -1.09 / -1.88 | `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` |
| +0.77 | 0.138 | 4 | -1.11 / -1.88 | `div(day_open(Open), cross_delay(day_close(Close), 5))` |
| +0.71 | 0.038 | 11 | -1.18 / -1.90 | `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` |

## 拆解(48 次评估)

### head score +1.05:`cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), 1), day_sum(Ret), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), 1)` | -1.55 | -1.39 | -1.55 | — | (子树本身) |
| sufficiency | `mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume))` | -1.49 | -1.37 | -1.49 | — | (子树本身) |
| sufficiency | `cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1)` | -1.89 | -0.88 | -1.89 | — | (子树本身) |
| sufficiency | `mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume))` | -1.82 | -0.84 | -1.82 | — | (子树本身) |
| knockout | `cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), 1)` | +0.08 | +0.95 | +0.08 | +0.97 | `cross_regbeta(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), day_sum(Ret), 241)` |
| knockout | `mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume))` | +0.73 | +0.78 | +0.73 | +0.32 | `cross_regbeta(cross_delay(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), 1), day_sum(Ret), 241)` |
| knockout | `cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1)` | +0.95 | +0.95 | +1.16 | +0.10 | `cross_regbeta(cross_delay(mul(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), day_last(Volume)), 1), day_sum(Ret), 241)` |
| knockout | `mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume))` | +0.89 | +0.89 | +1.26 | +0.17 | `cross_regbeta(cross_delay(mul(cross_delay(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), 1), day_last(Volume)), 1), day_sum(Ret), 241)` |
| swap | `High->Low` | +1.06 | +1.06 | +1.13 | — | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(Low), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), 1), day_sum(Ret), 241)` |
| swap | `Volume->Amt` | +1.13 | +1.44 | +1.13 | — | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Amt)), 5), 1), day_last(Amt)), 1), day_last(Amt)), 1), day_sum(Ret), 241)` |
| window | `cross_regbeta@241->120` | +0.96 | +0.96 | +0.97 | — | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), 1), day_sum(Ret), 120)` |
| window | `cross_regbeta@241->482` | +0.96 | +0.96 | +1.19 | — | `cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), 1), day_sum(Ret), 482)` |

### head score +0.95:`cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), 1), day_sum(Ret), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), 1)` | -1.85 | -0.85 | -1.85 | — | (子树本身) |
| sufficiency | `mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume))` | -1.76 | -0.85 | -1.76 | — | (子树本身) |
| sufficiency | `cross_mean(mul(day_mean(High), day_skew(Volume)), 5)` | -2.20 | -1.66 | -2.20 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), day_skew(Volume))` | -2.16 | -1.61 | -2.16 | — | (子树本身) |
| knockout | `cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), 1)` | +0.08 | +0.99 | +0.08 | +0.87 | `cross_regbeta(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), day_sum(Ret), 241)` |
| knockout | `mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume))` | +0.25 | +0.44 | +0.25 | +0.70 | `cross_regbeta(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_sum(Ret), 241)` |
| knockout | `cross_mean(mul(day_mean(High), day_skew(Volume)), 5)` | +0.76 | +0.76 | +1.45 | +0.20 | `cross_regbeta(cross_delay(mul(mul(day_mean(High), day_skew(Volume)), day_last(Volume)), 1), day_sum(Ret), 241)` |
| knockout | `mul(day_mean(High), day_skew(Volume))` | +0.91 | +0.91 | +1.10 | +0.04 | `cross_regbeta(cross_delay(mul(cross_mean(day_mean(High), 5), day_last(Volume)), 1), day_sum(Ret), 241)` |
| swap | `High->Low` | +0.97 | +0.97 | +0.98 | — | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(Low), day_skew(Volume)), 5), day_last(Volume)), 1), day_sum(Ret), 241)` |
| swap | `Volume->Amt` | +1.12 | +1.16 | +1.12 | — | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Amt)), 5), day_last(Amt)), 1), day_sum(Ret), 241)` |
| window | `cross_regbeta@241->120` | +0.79 | +0.79 | +1.27 | — | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), 1), day_sum(Ret), 120)` |
| window | `cross_regbeta@241->482` | +0.92 | +0.92 | +1.24 | — | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), 1), day_sum(Ret), 482)` |

### head score +0.70:`cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_sum(Ret), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1)` | -1.89 | -0.88 | -1.89 | — | (子树本身) |
| sufficiency | `mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume))` | -1.82 | -0.84 | -1.82 | — | (子树本身) |
| sufficiency | `cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1)` | -2.20 | -1.64 | -2.20 | — | (子树本身) |
| sufficiency | `cross_mean(mul(day_mean(High), day_skew(Volume)), 5)` | -2.20 | -1.66 | -2.20 | — | (子树本身) |
| knockout | `cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1)` | +0.10 | +0.10 | +0.35 | +0.60 | `cross_regbeta(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), day_sum(Ret), 60)` |
| knockout | `mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume))` | -0.56 | -0.56 | -0.09 | +1.27 | `cross_regbeta(cross_delay(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), 1), day_sum(Ret), 60)` |
| knockout | `cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1)` | +0.63 | +0.63 | +0.68 | +0.08 | `cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), 1), day_sum(Ret), 60)` |
| knockout | `cross_mean(mul(day_mean(High), day_skew(Volume)), 5)` | +0.77 | +0.77 | +0.92 | -0.06 | `cross_regbeta(cross_delay(mul(cross_delay(mul(day_mean(High), day_skew(Volume)), 1), day_last(Volume)), 1), day_sum(Ret), 60)` |
| swap | `High->Low` | +0.71 | +0.71 | +0.80 | — | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(Low), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_sum(Ret), 60)` |
| swap | `Volume->Amt` | +0.68 | +1.10 | +0.68 | — | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Amt)), 5), 1), day_last(Amt)), 1), day_sum(Ret), 60)` |
| window | `cross_regbeta@60->30` | +0.05 | +0.05 | +0.31 | — | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_sum(Ret), 30)` |
| window | `cross_regbeta@60->120` | +0.78 | +0.78 | +1.34 | — | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_sum(Ret), 120)` |

### head score +0.21:`signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 150))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 150)` | +0.21 | +0.43 | +0.21 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -0.34 | -0.34 | +0.05 | — | (子树本身) |
| sufficiency | `cross_delta(day_sum(Open), 3)` | -4.61 | -4.61 | -3.98 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), day_skew(Volume))` | -2.16 | -1.61 | -2.16 | — | (子树本身) |
| knockout | `cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 150)` | -0.34 | -0.34 | +0.05 | +0.56 | `signedpower(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10))` |
| knockout | `cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -2.48 | -1.69 | -2.48 | +2.69 | `signedpower(cross_tail_mean_q75(cross_delta(day_sum(Open), 3), 150))` |
| knockout | `cross_delta(day_sum(Open), 3)` | -0.34 | -0.34 | +0.09 | +0.55 | `signedpower(cross_tail_mean_q75(cross_corr(day_sum(Open), mul(day_mean(High), day_skew(Volume)), 10), 150))` |
| knockout | `mul(day_mean(High), day_skew(Volume))` | -1.23 | -1.23 | -1.10 | +1.44 | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), day_mean(High), 10), 150))` |
| swap | `Open->Close` | +0.22 | +0.43 | +0.22 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Close), 3), mul(day_mean(High), day_skew(Volume)), 10), 150))` |
| swap | `High->Low` | +0.22 | +0.45 | +0.22 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(Low), day_skew(Volume)), 10), 150))` |
| window | `cross_tail_mean_q75@150->75` | -0.24 | +0.48 | -0.24 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 75))` |
| window | `cross_tail_mean_q75@150->300` | -0.47 | -0.47 | +0.51 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 300))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_last(Volume)` — enrichment,均值差 +2.38,p 0.000
2. `mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume))` — enrichment,均值差 +2.14,p 0.000
3. `cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1)` — enrichment,均值差 +1.75,p 0.003
4. `cross_mean(mul(day_mean(High), day_skew(Volume)), 5)` — enrichment,均值差 +1.73,p 0.000
5. `cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1)` — enrichment,均值差 +1.70,p 0.000
6. `mul(day_mean(High), day_skew(Volume))` — enrichment,均值差 +1.49,p 0.000
7. `mul(cross_delay(mul(day_mean(High), day_skew(Volume)), 1), day_skew(Volume))` — enrichment,均值差 +1.41,p 0.013
8. `day_sum(Ret)` — enrichment,均值差 +1.28,p 0.000
9. `day_mean(High)` — enrichment,均值差 +1.14,p 0.000
10. `cross_delay(mul(day_mean(High), day_skew(Volume)), 1)` — enrichment,均值差 +1.11,p 0.000
11. `day_skew(Volume)` — enrichment,均值差 +1.08,p 0.000
12. `day_flat_run_max(Ret)` — enrichment,均值差 +0.97,p 0.023
13. `day_open(Close)` — enrichment,均值差 +0.95,p 0.061
14. `div(day_close(Close), cross_delay(day_close(Close), 5))` — enrichment,均值差 +0.89,p 0.056
15. `day_quantile(Vwap)` — enrichment,均值差 +0.87,p 0.058
16. `day_argmin(Open)` — enrichment,均值差 +0.85,p 0.010
17. `cross_delta(day_quantile(Vwap), 3)` — enrichment,均值差 +0.80,p 0.098
18. `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` — enrichment,均值差 +0.80,p 0.098
19. `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` — enrichment,均值差 +0.71,p 0.038
20. `cross_delay(day_close(Close), 5)` — enrichment,均值差 +0.71,p 0.054
21. `day_close(Close)` — enrichment,均值差 +0.59,p 0.005
22. `cross_delay(day_close(Close), 1)` — enrichment,均值差 +0.51,p 0.044
23. `cross_delta(day_quantile_q75(Vwap), 3)` — enrichment,均值差 +0.49,p 0.078

## 本组之前各轮的任务

- `prods2019Pr1a_Ea`:核心 `day_skew(Volume)`;评分 88,过线 0,入 heads 0;采样计数 {'c05_no_core': 775, 'c05_skeleton': 422}
  - score -0.06(train -0.06 valid +0.06):`cross_regbeta(day_skew(Volume), div(div(day_open(Open), cross_delay(day_close(Close), 5)), cross_delay(div(day_open(Open), cross_delay(day_close(Close), 5)), 5)), 60)`
  - score -0.30(train +0.06 valid -0.30):`cross_corr(day_skew(Volume), div(day_open(Open), cross_delay(day_close(Open), 5)), 60)`
  - score -0.30(train +0.20 valid -0.30):`cross_corr(day_skew(Volume), div(day_close(Close), cross_delay(day_close(Close), 5)), 60)`
  - score -0.30(train -0.04 valid -0.30):`cross_corr(day_skew(Volume), div(day_open(Open), cross_delay(day_close(Close), 5)), 60)`
  - score -0.35(train -0.16 valid -0.35):`cross_corr(day_skew(Volume), div(day_open(Close), cross_delay(day_first(Close), 1)), 60)`
- `prods2019Pr1b_Nb`:核心 `—`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.72(train -0.72 valid -0.64):`cs_last_low20(cs_bucket_zscore(cross_ema(day_skew(Volume), 20), cross_ema(day_skew(Volume), 241)), ListAge)`
  - score -1.16(train -1.16 valid -0.90):`cs_last_low20(cs_bucket_zscore(cross_ema(cross_ema(day_skew(Volume), 20), 20), cross_ema(sub(log(day_sum(Volume)), LogFloatShares), 20)), ListAge)`
  - score -1.42(train -1.42 valid -0.66):`cs_last_low20(cs_bucket_zscore(cross_ema(day_skew(Volume), 20), cross_ema(sub(log(day_sum(Volume)), log(day_sum(Volume))), 20)), ListAge)`
  - score -1.44(train -1.44 valid -0.80):`cs_bucket_rank(cs_last_low20(cs_bucket_zscore(cross_ema(day_skew(Volume), 241), cross_ema(sub(log(day_sum(Volume)), LogFloatShares), 20)), ListAge), day_skew(Ret))`
  - score -1.47(train -1.47 valid -0.88):`cs_bucket_rank(cs_last_low20(cs_bucket_zscore(cross_ema(day_skew(Volume), 20), cross_ema(sub(log(day_sum(Volume)), LogFloatShares), 20)), ListAge), day_skew(Ret))`
- `prods2019Pr2a_Ea`:核心 `mul(day_mean(High), day_skew(Volume))`;评分 110,过线 10,入 heads 3;采样计数 {'c05_no_core': 1491, 'c05_skeleton': 763}
  - score +1.05(train +1.05 valid +1.14):`cross_regbeta(cross_delay(mul(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_last(Volume)), 1), day_sum(Ret), 241)`
  - score +1.01(train +1.01 valid +1.28):`cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 5), 1), day_last(Volume)), 1), day_sum(Ret), 241)`
  - score +0.95(train +0.95 valid +0.99):`cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), day_last(Volume)), 1), day_sum(Ret), 241)`
  - score +0.95(train +0.95 valid +1.25):`cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume))), 5), 1), day_last(Volume)), 1), day_sum(Ret), 241)`
  - score +0.93(train +0.96 valid +0.93):`cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), day_skew(Volume)), 5), 1), day_last(Volume)), 1), day_sum(Ret), 241)`
- `prods2019Pr2b_Nb`:核心 `—`;评分 71,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.25(train +0.41 valid +0.25):`cross_corr(day_topw_mean(Volume, Volume), day_flat_run_max(Ret), 120)`
  - score +0.08(train +0.08 valid +0.38):`cross_corr(day_topw_mean(sqrt(Volume), Volume), day_flat_run_max(Ret), 120)`
  - score -0.25(train +0.04 valid -0.25):`cross_corr(day_sum(Ret), day_flat_run_max(Ret), 120)`
  - score -0.60(train +0.27 valid -0.60):`cross_corr(day_topw_mean(sqrt(Volume), Ret), day_flat_run_max(Ret), 120)`
  - score -0.89(train -0.89 valid -0.62):`cross_corr(day_topw_mean(sqrt(Volume), Volume), day_sum(Ret), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.17(swap Volume->Amt):`cross_regbeta(cross_delay(mul(cross_mean(mul(day_mean(High), day_skew(Amt)), 5), day_last(Amt)), 1), day_sum(Ret), 241)`
