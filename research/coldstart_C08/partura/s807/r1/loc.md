# 定位:种子 807,P 组,第 1 轮(只含 train / valid)

快照:c07s807M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.91 | +1.11 | +0.91 | -1 | 20 | c07s807M1_I0_open_search | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 241)` |
| +0.79 | +0.79 | +1.32 | +1 | 20 | c07s807M1_I0_open_search | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 30)` |
| +0.52 | +0.84 | +0.52 | +1 | 5 | c07s807M1_I0_open_search | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 30)` |

## 共性:114 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.33 | 0.001 | 5 | +0.30 / -1.03 | `cs_mean(day_median(Close))` |
| +1.11 | 0.000 | 66 | -0.51 / -1.61 | `day_quantile_q75(Volume)` |
| +1.07 | 0.004 | 6 | +0.04 / -1.03 | `ts_var(LogFloatCap, 40)` |
| +0.87 | 0.014 | 9 | -0.17 / -1.04 | `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), LimitWidth)` |
| +0.86 | 0.000 | 60 | -0.57 / -1.42 | `day_pos_ratio(Open)` |
| +0.86 | 0.000 | 60 | -0.57 / -1.42 | `cs_median(day_pos_ratio(Open))` |
| +0.75 | 0.001 | 48 | -0.54 / -1.29 | `ts_var(LogFloatCap, 20)` |
| +0.48 | 0.058 | 16 | -0.56 / -1.04 | `ts_var(LogFloatCap, 50)` |
| +0.46 | 0.097 | 39 | -0.67 / -1.13 | `cs_median(LimitWidth)` |
| +0.42 | 0.123 | 13 | -0.60 / -1.02 | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 50))` |
| +0.38 | 0.049 | 7 | -0.62 / -1.00 | `day_median(Close)` |
| +0.37 | 0.148 | 32 | -0.71 / -1.08 | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20))` |
| +0.25 | 0.530 | 6 | -0.73 / -0.99 | `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), signedpower(cs_median(LimitWidth)))` |
| +0.25 | 0.050 | 5 | -0.74 / -0.98 | `day_skew(Open)` |
| +0.19 | 0.476 | 30 | -0.83 / -1.02 | `signedpower(cs_median(LimitWidth))` |
| -0.24 | 0.731 | 4 | -1.21 / -0.96 | `cross_regbeta(day_quantile_q75(Volume), LogFloatShares, 241)` |

## 拆解(35 次评估)

### head score +0.91:`cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5)))` | -3.67 | -3.67 | -3.06 | — | (子树本身) |
| sufficiency | `pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))` | -3.67 | -3.67 | -3.06 | — | (子树本身) |
| sufficiency | `ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5)` | -3.67 | -3.67 | -3.06 | — | (子树本身) |
| sufficiency | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20))` | -2.71 | -2.71 | -1.63 | — | (子树本身) |
| knockout | `cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5)))` | +0.93 | +0.96 | +0.93 | -0.02 | `cross_regbeta(day_quantile_q75(Volume), pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5)), 241)` |
| knockout | `pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))` | +0.91 | +1.11 | +0.91 | -0.00 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5)), 241)` |
| knockout | `ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5)` | -1.99 | +0.20 | -1.99 | +2.90 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)))), 241)` |
| knockout | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20))` | — | — | — | — | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(cs_median(day_pos_ratio(Open)), cs_mean(day_median(Close)), 5))), 241)` |
| swap | `Volume->Amt` | +0.64 | +0.64 | +1.47 | — | `cross_regbeta(day_quantile_q75(Amt), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 241)` |
| swap | `Open->Close` | +0.91 | +1.11 | +0.91 | — | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Close)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 241)` |
| window | `cross_regbeta@241->120` | +0.83 | +0.83 | +0.91 | — | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 120)` |
| window | `cross_regbeta@241->482` | +0.33 | +0.92 | +0.33 | — | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 482)` |

### head score +0.79:`cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth)` | -0.72 | -0.72 | +1.56 | — | (子树本身) |
| sufficiency | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30))` | -2.13 | -2.13 | -0.35 | — | (子树本身) |
| sufficiency | `cs_median(day_pos_ratio(Open))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile_q75(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth)` | +0.35 | +0.35 | +1.20 | +0.44 | `cross_regbeta(day_quantile_q75(Volume), add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), 30)` |
| knockout | `add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30))` | — | — | — | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(cs_median(day_pos_ratio(Open)), LimitWidth), 30)` |
| knockout | `cs_median(day_pos_ratio(Open))` | +0.79 | +0.79 | +1.32 | -0.00 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(day_pos_ratio(Open), ts_var(LogFloatCap, 30)), LimitWidth), 30)` |
| knockout | `ts_var(LogFloatCap, 30)` | -0.55 | +0.25 | -0.55 | +1.34 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), LogFloatCap), LimitWidth), 30)` |
| swap | `Volume->Amt` | +0.83 | +0.83 | +2.20 | — | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 30)` |
| swap | `Open->Close` | +0.79 | +0.79 | +1.32 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Close)), ts_var(LogFloatCap, 30)), LimitWidth), 30)` |
| window | `cross_regbeta@30->15` | +0.03 | +0.03 | +1.05 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 15)` |
| window | `cross_regbeta@30->60` | +1.02 | +1.20 | +1.02 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 60)` |

### head score +0.52:`cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth)` | -0.86 | -0.86 | +0.45 | — | (子树本身) |
| sufficiency | `add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20))` | -2.71 | -2.71 | -1.62 | — | (子树本身) |
| sufficiency | `cs_median(ts_var(LogFloatCap, 50))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile_q75(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth)` | +0.19 | +0.19 | +0.62 | +0.33 | `cross_regbeta(day_quantile_q75(Volume), add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), 30)` |
| knockout | `add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20))` | -0.13 | -0.01 | -0.13 | +0.65 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(cs_median(ts_var(LogFloatCap, 50)), LimitWidth), 30)` |
| knockout | `cs_median(ts_var(LogFloatCap, 50))` | +0.76 | +0.76 | +1.61 | -0.24 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(ts_var(LogFloatCap, 50), ts_var(LogFloatCap, 20)), LimitWidth), 30)` |
| knockout | `ts_var(LogFloatCap, 50)` | +0.51 | +0.84 | +0.51 | +0.01 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(LogFloatCap), ts_var(LogFloatCap, 20)), LimitWidth), 30)` |
| swap | `Volume->Amt` | +1.11 | +1.11 | +3.06 | — | `cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 30)` |
| window | `cross_regbeta@30->15` | +0.60 | +0.60 | +0.77 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 15)` |
| window | `cross_regbeta@30->60` | +1.02 | +1.20 | +1.02 | — | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_mean(day_median(Close))` — enrichment,均值差 +1.33,p 0.001
2. `day_quantile_q75(Volume)` — enrichment,均值差 +1.11,p 0.000
3. `ts_var(LogFloatCap, 40)` — enrichment,均值差 +1.07,p 0.004
4. `cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), LimitWidth)` — enrichment,均值差 +0.87,p 0.014
5. `day_pos_ratio(Open)` — enrichment,均值差 +0.86,p 0.000
6. `cs_median(day_pos_ratio(Open))` — enrichment,均值差 +0.86,p 0.000
7. `ts_var(LogFloatCap, 20)` — enrichment,均值差 +0.75,p 0.001
8. `ts_var(LogFloatCap, 50)` — enrichment,均值差 +0.48,p 0.058
9. `cs_median(LimitWidth)` — enrichment,均值差 +0.46,p 0.097
10. `day_median(Close)` — enrichment,均值差 +0.38,p 0.049
11. `day_skew(Open)` — enrichment,均值差 +0.25,p 0.050

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.59(swap Volume->Amt):`cross_regbeta(day_quantile_q75(Amt), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 30)`
- 增益 +0.50(window cross_regbeta@30->60):`cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 60)`
- 增益 +0.24(knockout cs_median(ts_var(LogFloatCap, 50))):`cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(ts_var(LogFloatCap, 50), ts_var(LogFloatCap, 20)), LimitWidth), 30)`
- 增益 +0.23(window cross_regbeta@30->60):`cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 60)`
