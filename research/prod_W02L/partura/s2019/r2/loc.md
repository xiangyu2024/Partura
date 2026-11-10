# 定位:种子 2019,P 组,第 2 轮(只含 train / valid)

快照:prods2019M1_I0_open_search, prods2019M2_I0_open_search, prods2019Pr1a_Ea, prods2019Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.03 | +0.68 | +0.03 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))` |
| +0.01 | +0.01 | +0.29 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.24 | -0.24 | +0.40 | +1 | 5 | prods2019M2_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.27 | -0.27 | +0.23 | +1 | 5 | prods2019M2_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.31 | +0.05 | -0.31 | +1 | 0 | prods2019M2_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.56 | -0.56 | -0.03 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 241))` |

## 共性:174 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.34 | 0.014 | 4 | -0.93 / -2.27 | `day_open(Close)` |
| +1.28 | 0.011 | 5 | -0.99 / -2.28 | `div(day_close(Close), cross_delay(day_close(Close), 5))` |
| +1.27 | 0.000 | 11 | -1.05 / -2.32 | `day_argmin(Open)` |
| +1.26 | 0.009 | 5 | -1.02 / -2.28 | `day_quantile(Vwap)` |
| +1.18 | 0.021 | 4 | -1.09 / -2.27 | `cross_delta(day_quantile(Vwap), 3)` |
| +1.18 | 0.021 | 4 | -1.09 / -2.27 | `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` |
| +1.17 | 0.000 | 25 | -1.24 / -2.41 | `mul(day_mean(High), day_skew(Volume))` |
| +1.16 | 0.050 | 4 | -1.11 / -2.27 | `div(day_open(Open), cross_delay(day_close(Close), 5))` |
| +1.13 | 0.003 | 11 | -1.18 / -2.31 | `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` |
| +1.12 | 0.005 | 10 | -1.18 / -2.31 | `cross_delay(day_close(Close), 5)` |
| +1.08 | 0.000 | 34 | -1.38 / -2.45 | `day_close(Close)` |
| +1.03 | 0.051 | 4 | -1.24 / -2.27 | `day_close(Open)` |
| +0.92 | 0.003 | 18 | -1.41 / -2.34 | `cross_delta(day_quantile_q75(Vwap), 3)` |
| +0.92 | 0.001 | 16 | -1.40 / -2.33 | `cross_delay(day_close(Close), 1)` |
| +0.88 | 0.050 | 5 | -1.39 / -2.27 | `cross_delay(day_skew(Volume), 1)` |
| +0.85 | 0.005 | 20 | -1.49 / -2.34 | `day_quantile_q75(Vwap)` |
| +0.77 | 0.095 | 4 | -1.49 / -2.26 | `div(day_close(Close), day_open(Open))` |
| +0.76 | 0.003 | 26 | -1.60 / -2.35 | `day_open(Open)` |
| +0.54 | 0.117 | 8 | -1.73 / -2.27 | `div(day_open(Open), cross_delay(day_close(Close), 1))` |
| +0.49 | 0.062 | 41 | -1.87 / -2.36 | `day_mean(High)` |

## 拆解(48 次评估)

### head score +0.03:`signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 120)` | +0.03 | +0.67 | +0.03 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -0.34 | -0.34 | +0.05 | — | (子树本身) |
| sufficiency | `cross_delta(day_sum(Open), 3)` | -4.61 | -4.61 | -3.98 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), day_skew(Volume))` | -2.16 | -1.61 | -2.16 | — | (子树本身) |
| knockout | `cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 120)` | -0.34 | -0.34 | +0.05 | +0.38 | `signedpower(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10))` |
| knockout | `cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -2.52 | -1.65 | -2.52 | +2.55 | `signedpower(cross_tail_mean_q75(cross_delta(day_sum(Open), 3), 120))` |
| knockout | `cross_delta(day_sum(Open), 3)` | -0.21 | -0.03 | -0.21 | +0.25 | `signedpower(cross_tail_mean_q75(cross_corr(day_sum(Open), mul(day_mean(High), day_skew(Volume)), 10), 120))` |
| knockout | `mul(day_mean(High), day_skew(Volume))` | -1.06 | -1.06 | -0.76 | +1.09 | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), day_mean(High), 10), 120))` |
| swap | `Open->Close` | -0.03 | +0.67 | -0.03 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Close), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))` |
| swap | `High->Low` | -0.00 | +0.70 | -0.00 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(Low), day_skew(Volume)), 10), 120))` |
| window | `cross_tail_mean_q75@120->60` | -0.66 | +0.49 | -0.66 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 60))` |
| window | `cross_tail_mean_q75@120->240` | +0.04 | +0.15 | +0.04 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 240))` |

### head score +0.01:`signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | +0.01 | +0.01 | +0.30 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -0.45 | -0.45 | +0.13 | — | (子树本身) |
| sufficiency | `cross_delta(day_quantile(Vwap), 3)` | -4.67 | -4.67 | -3.99 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), day_skew(Volume))` | -2.16 | -1.61 | -2.16 | — | (子树本身) |
| knockout | `cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -0.45 | -0.45 | +0.13 | +0.46 | `signedpower(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10))` |
| knockout | `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -2.50 | -1.75 | -2.50 | +2.51 | `signedpower(cross_tail_mean_q75(cross_delta(day_quantile(Vwap), 3), 241))` |
| knockout | `cross_delta(day_quantile(Vwap), 3)` | -0.25 | -0.25 | +0.02 | +0.26 | `signedpower(cross_tail_mean_q75(cross_corr(day_quantile(Vwap), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| knockout | `mul(day_mean(High), day_skew(Volume))` | -1.38 | -0.94 | -1.38 | +1.38 | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), day_mean(High), 10), 241))` |
| swap | `Vwap->Close` | +0.06 | +0.06 | +0.27 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Close), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| swap | `High->Low` | -0.02 | -0.02 | +0.28 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(Low), day_skew(Volume)), 10), 241))` |
| window | `cross_tail_mean_q75@241->120` | +0.04 | +0.65 | +0.04 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))` |
| window | `cross_tail_mean_q75@241->482` | -0.66 | -0.66 | +0.29 | — | `signedpower(cross_tail_mean_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 482))` |

### head score -0.24:`signedpower(cross_quantile_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -0.24 | -0.24 | +0.40 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -1.30 | -1.30 | -1.01 | — | (子树本身) |
| sufficiency | `cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3)` | -7.24 | -7.24 | -7.11 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -0.67 | -0.67 | -0.10 | — | (子树本身) |
| knockout | `cross_quantile_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -1.30 | -1.30 | -1.01 | +1.05 | `signedpower(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10))` |
| knockout | `cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -2.37 | -1.66 | -2.37 | +2.13 | `signedpower(cross_quantile_q75(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), 241))` |
| knockout | `cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3)` | -0.25 | +0.05 | -0.25 | +0.01 | `signedpower(cross_quantile_q75(cross_corr(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| knockout | `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -0.38 | -0.12 | -0.38 | +0.14 | `signedpower(cross_quantile_q75(cross_corr(cross_delta(cross_delta(day_quantile_q75(Vwap), 3), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| swap | `Vwap->Close` | -0.23 | -0.23 | +0.44 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Close), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| swap | `High->Low` | -0.22 | -0.22 | +0.41 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(Low), day_skew(Volume)), 10), 3), mul(day_mean(Low), day_skew(Volume)), 10), 241))` |
| window | `cross_quantile_q75@241->120` | -0.55 | -0.55 | -0.26 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))` |
| window | `cross_quantile_q75@241->482` | -0.84 | -0.84 | -0.00 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 3), mul(day_mean(High), day_skew(Volume)), 10), 482))` |

### head score -0.27:`signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -0.27 | -0.27 | +0.26 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -0.67 | -0.67 | -0.10 | — | (子树本身) |
| sufficiency | `cross_delta(day_quantile_q75(Vwap), 3)` | -4.67 | -4.67 | -4.06 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), day_skew(Volume))` | -2.16 | -1.61 | -2.16 | — | (子树本身) |
| knockout | `cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -0.67 | -0.67 | -0.10 | +0.41 | `signedpower(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10))` |
| knockout | `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -2.79 | -1.63 | -2.79 | +2.52 | `signedpower(cross_quantile_q75(cross_delta(day_quantile_q75(Vwap), 3), 241))` |
| knockout | `cross_delta(day_quantile_q75(Vwap), 3)` | -0.83 | -0.83 | -0.09 | +0.57 | `signedpower(cross_quantile_q75(cross_corr(day_quantile_q75(Vwap), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| knockout | `mul(day_mean(High), day_skew(Volume))` | -2.38 | -2.38 | -1.52 | +2.12 | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), day_mean(High), 10), 241))` |
| swap | `Vwap->Close` | -0.21 | -0.21 | +0.32 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Close), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| swap | `High->Low` | -0.28 | -0.28 | +0.27 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(Low), day_skew(Volume)), 10), 241))` |
| window | `cross_quantile_q75@241->120` | -0.23 | -0.23 | +0.05 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))` |
| window | `cross_quantile_q75@241->482` | -0.88 | -0.88 | -0.02 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_open(Close)` — enrichment,均值差 +1.34,p 0.014
2. `div(day_close(Close), cross_delay(day_close(Close), 5))` — enrichment,均值差 +1.28,p 0.011
3. `day_argmin(Open)` — enrichment,均值差 +1.27,p 0.000
4. `day_quantile(Vwap)` — enrichment,均值差 +1.26,p 0.009
5. `cross_delta(day_quantile(Vwap), 3)` — enrichment,均值差 +1.18,p 0.021
6. `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` — enrichment,均值差 +1.18,p 0.021
7. `mul(day_mean(High), day_skew(Volume))` — enrichment,均值差 +1.17,p 0.000
8. `div(day_open(Open), cross_delay(day_close(Close), 5))` — enrichment,均值差 +1.16,p 0.050
9. `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` — enrichment,均值差 +1.13,p 0.003
10. `cross_delay(day_close(Close), 5)` — enrichment,均值差 +1.12,p 0.005
11. `day_close(Close)` — enrichment,均值差 +1.08,p 0.000
12. `day_close(Open)` — enrichment,均值差 +1.03,p 0.051
13. `cross_delta(day_quantile_q75(Vwap), 3)` — enrichment,均值差 +0.92,p 0.003
14. `cross_delay(day_close(Close), 1)` — enrichment,均值差 +0.92,p 0.001
15. `cross_delay(day_skew(Volume), 1)` — enrichment,均值差 +0.88,p 0.050
16. `day_quantile_q75(Vwap)` — enrichment,均值差 +0.85,p 0.005
17. `div(day_close(Close), day_open(Open))` — enrichment,均值差 +0.77,p 0.095
18. `day_open(Open)` — enrichment,均值差 +0.76,p 0.003
19. `day_mean(High)` — enrichment,均值差 +0.49,p 0.062

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

## 比原 head 好的拆解变体(R 候选)

(没有)
