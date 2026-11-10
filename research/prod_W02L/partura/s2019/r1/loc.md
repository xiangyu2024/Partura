# 定位:种子 2019,P 组,第 1 轮(只含 train / valid)

快照:prods2019M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.20 | -0.20 | +0.11 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.29 | -0.29 | +0.14 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| -0.56 | -0.56 | -0.03 | +1 | 0 | prods2019M1_I0_open_search | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 241))` |

## 共性:25 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.47 | 0.000 | 14 | -1.39 / -2.87 | `day_skew(Volume)` |
| +1.46 | 0.000 | 13 | -1.34 / -2.80 | `mul(day_mean(High), day_skew(Volume))` |
| +1.28 | 0.004 | 5 | -1.02 / -2.30 | `day_quantile(Vwap)` |
| +1.14 | 0.015 | 4 | -1.09 / -2.22 | `cross_delta(day_quantile(Vwap), 3)` |
| +1.14 | 0.015 | 4 | -1.09 / -2.22 | `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` |
| -0.83 | 0.975 | 6 | -2.67 / -1.84 | `mul(day_mean(High), day_skew(Vwap))` |
| -0.83 | 0.975 | 6 | -2.67 / -1.84 | `day_skew(Vwap)` |
| -1.35 | 0.994 | 4 | -3.18 / -1.83 | `day_skew(High)` |

## 拆解(36 次评估)

### head score -0.20:`signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -0.20 | -0.20 | +0.13 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -0.45 | -0.45 | +0.13 | — | (子树本身) |
| sufficiency | `cross_delta(day_quantile(Vwap), 3)` | -4.67 | -4.67 | -3.99 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), day_skew(Volume))` | -2.16 | -1.61 | -2.16 | — | (子树本身) |
| knockout | `cross_quantile_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -0.45 | -0.45 | +0.13 | +0.26 | `signedpower(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10))` |
| knockout | `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -2.79 | -1.65 | -2.79 | +2.59 | `signedpower(cross_quantile_q75(cross_delta(day_quantile(Vwap), 3), 241))` |
| knockout | `cross_delta(day_quantile(Vwap), 3)` | -0.83 | -0.83 | -0.05 | +0.63 | `signedpower(cross_quantile_q75(cross_corr(day_quantile(Vwap), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| knockout | `mul(day_mean(High), day_skew(Volume))` | -2.73 | -2.73 | -1.69 | +2.54 | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), day_mean(High), 10), 241))` |
| swap | `Vwap->Close` | -0.15 | -0.15 | +0.08 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile(Close), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| swap | `High->Low` | -0.20 | -0.20 | +0.17 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(Low), day_skew(Volume)), 10), 241))` |
| window | `cross_quantile_q75@241->120` | -0.19 | -0.02 | -0.19 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))` |
| window | `cross_quantile_q75@241->482` | -0.93 | -0.93 | +0.10 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10), 482))` |

### head score -0.29:`signedpower(cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -0.29 | -0.29 | +0.16 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -0.34 | -0.34 | +0.05 | — | (子树本身) |
| sufficiency | `cross_delta(day_sum(Open), 3)` | -4.61 | -4.61 | -3.98 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), day_skew(Volume))` | -2.16 | -1.61 | -2.16 | — | (子树本身) |
| knockout | `cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 241)` | -0.34 | -0.34 | +0.05 | +0.05 | `signedpower(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10))` |
| knockout | `cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10)` | -2.79 | -1.63 | -2.79 | +2.50 | `signedpower(cross_quantile_q75(cross_delta(day_sum(Open), 3), 241))` |
| knockout | `cross_delta(day_sum(Open), 3)` | -0.64 | -0.64 | -0.09 | +0.35 | `signedpower(cross_quantile_q75(cross_corr(day_sum(Open), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| knockout | `mul(day_mean(High), day_skew(Volume))` | -2.24 | -2.24 | -1.33 | +1.95 | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), day_mean(High), 10), 241))` |
| swap | `Open->Close` | -0.27 | -0.27 | +0.28 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_sum(Close), 3), mul(day_mean(High), day_skew(Volume)), 10), 241))` |
| swap | `High->Low` | -0.30 | -0.30 | +0.20 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(Low), day_skew(Volume)), 10), 241))` |
| window | `cross_quantile_q75@241->120` | -0.18 | -0.09 | -0.18 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))` |
| window | `cross_quantile_q75@241->482` | -0.95 | -0.95 | +0.20 | — | `signedpower(cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 482))` |

### head score -0.56:`signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 241)` | -0.56 | -0.56 | -0.06 | — | (子树本身) |
| sufficiency | `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10)` | -0.51 | -0.51 | -0.10 | — | (子树本身) |
| sufficiency | `mul(day_mean(High), mul(day_mean(High), day_skew(Volume)))` | -2.30 | -1.62 | -2.30 | — | (子树本身) |
| sufficiency | `cross_delta(day_quantile_q75(Vwap), 3)` | -4.67 | -4.67 | -4.06 | — | (子树本身) |
| knockout | `cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 241)` | -0.51 | -0.51 | -0.10 | -0.05 | `signedpower(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10))` |
| knockout | `cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10)` | -2.10 | -2.10 | -1.59 | +1.54 | `signedpower(cross_mean(cross_delta(day_quantile_q75(Vwap), 3), 241))` |
| knockout | `mul(day_mean(High), mul(day_mean(High), day_skew(Volume)))` | -2.95 | -2.54 | -2.95 | +2.39 | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), day_mean(High), 10), 241))` |
| knockout | `cross_delta(day_quantile_q75(Vwap), 3)` | -1.22 | -1.22 | -0.48 | +0.66 | `signedpower(cross_mean(cross_corr(day_quantile_q75(Vwap), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 241))` |
| swap | `Vwap->Close` | -0.59 | -0.59 | -0.15 | — | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Close), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 241))` |
| swap | `High->Low` | -0.55 | -0.55 | -0.10 | — | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(Low), mul(day_mean(Low), day_skew(Volume))), 10), 241))` |
| window | `cross_mean@241->120` | -0.50 | -0.50 | -0.23 | — | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 120))` |
| window | `cross_mean@241->482` | -1.04 | -1.04 | +0.21 | — | `signedpower(cross_mean(cross_corr(cross_delta(day_quantile_q75(Vwap), 3), mul(day_mean(High), mul(day_mean(High), day_skew(Volume))), 10), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_skew(Volume)` — enrichment,均值差 +1.47,p 0.000
2. `mul(day_mean(High), day_skew(Volume))` — enrichment,均值差 +1.46,p 0.000
3. `day_quantile(Vwap)` — enrichment,均值差 +1.28,p 0.004
4. `cross_delta(day_quantile(Vwap), 3)` — enrichment,均值差 +1.14,p 0.015
5. `cross_corr(cross_delta(day_quantile(Vwap), 3), mul(day_mean(High), day_skew(Volume)), 10)` — enrichment,均值差 +1.14,p 0.015

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.11(window cross_quantile_q75@241->120):`signedpower(cross_quantile_q75(cross_corr(cross_delta(day_sum(Open), 3), mul(day_mean(High), day_skew(Volume)), 10), 120))`
