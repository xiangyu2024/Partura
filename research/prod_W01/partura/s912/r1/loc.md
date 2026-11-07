# 定位:种子 912,P 组,第 1 轮(只含 train / valid)

快照:prods912M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.58 | +0.58 | +1.66 | -1 | 5 | prods912M1_I0_open_search | `cs_first_high40(ts_var(day_durbin_watson(Vwap), 1), ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |

## 共性:112 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.46 | 0.000 | 32 | +0.02 / -1.44 | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` |
| +1.44 | 0.000 | 49 | -0.21 / -1.66 | `sqrt(day_durbin_watson(Vwap))` |
| +1.44 | 0.000 | 18 | +0.18 / -1.25 | `pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |
| +1.35 | 0.009 | 4 | +0.27 / -1.07 | `day_durbin_watson(Low)` |
| +1.35 | 0.009 | 4 | +0.27 / -1.07 | `sqrt(day_durbin_watson(Low))` |
| +1.32 | 0.000 | 57 | -0.37 / -1.70 | `day_durbin_watson(Vwap)` |
| +1.26 | 0.017 | 4 | +0.19 / -1.07 | `ts_var(ts_var(day_corr(Low, Low), 1), 1)` |
| +1.07 | 0.023 | 5 | -0.00 / -1.07 | `ts_var(day_corr(Vwap, Low), 1)` |
| +0.91 | 0.080 | 4 | -0.15 / -1.06 | `cs_first_high40(day_pos_ratio(Vwap), pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10)))` |
| +0.80 | 0.016 | 18 | -0.36 / -1.15 | `day_pos_ratio(Vwap)` |
| +0.58 | 0.044 | 28 | -0.59 / -1.17 | `day_corr(Low, Low)` |
| +0.57 | 0.050 | 23 | -0.57 / -1.14 | `ts_var(day_corr(Low, Low), 1)` |
| +0.55 | 0.098 | 11 | -0.53 / -1.08 | `day_corr(Low, Vwap)` |
| +0.55 | 0.098 | 11 | -0.53 / -1.08 | `ts_var(day_corr(Low, Vwap), 1)` |
| +0.47 | 0.164 | 8 | -0.59 / -1.06 | `day_corr(Vwap, Low)` |
| -0.29 | 0.774 | 4 | -1.30 / -1.01 | `day_var(Open)` |
| -0.40 | 0.895 | 5 | -1.40 / -1.01 | `pow_2_5(day_sum(Open))` |
| -0.40 | 0.895 | 5 | -1.40 / -1.01 | `day_sum(Open)` |
| -0.44 | 0.911 | 5 | -1.45 / -1.00 | `day_at_max_ratio(Low)` |
| -0.45 | 0.883 | 4 | -1.46 / -1.01 | `cs_last_low40(day_at_max_ratio(Low), LogFloatCap)` |

## 拆解(9 次评估)

### head score +0.58:`cs_first_high40(ts_var(day_durbin_watson(Vwap), 1), ts_var(sqrt(day_durbin_watson(Vwap)), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | +0.07 | +0.07 | +1.04 | — | (子树本身) |
| sufficiency | `ts_var(day_durbin_watson(Vwap), 1)` | — | — | — | — | 门槛废品 |
| sufficiency | `sqrt(day_durbin_watson(Vwap))` | -3.24 | -2.43 | -3.24 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.27 | -2.37 | -3.27 | — | (子树本身) |
| knockout | `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` | -3.01 | -1.38 | -3.01 | +3.59 | `cs_first_high40(ts_var(day_durbin_watson(Vwap), 1), sqrt(day_durbin_watson(Vwap)))` |
| knockout | `ts_var(day_durbin_watson(Vwap), 1)` | -1.75 | -1.75 | -0.13 | +2.33 | `cs_first_high40(day_durbin_watson(Vwap), ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |
| knockout | `sqrt(day_durbin_watson(Vwap))` | +0.40 | +0.40 | +1.52 | +0.18 | `cs_first_high40(ts_var(day_durbin_watson(Vwap), 1), ts_var(day_durbin_watson(Vwap), 10))` |
| swap | `Vwap->Close` | +0.24 | +0.24 | +1.48 | — | `cs_first_high40(ts_var(day_durbin_watson(Close), 1), ts_var(sqrt(day_durbin_watson(Close)), 10))` |
| window | `ts_var@1->2` | -0.85 | -0.85 | +1.25 | — | `cs_first_high40(ts_var(day_durbin_watson(Vwap), 2), ts_var(sqrt(day_durbin_watson(Vwap)), 10))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_var(sqrt(day_durbin_watson(Vwap)), 10)` — enrichment,均值差 +1.46,p 0.000
2. `sqrt(day_durbin_watson(Vwap))` — enrichment,均值差 +1.44,p 0.000
3. `pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10))` — enrichment,均值差 +1.44,p 0.000
4. `day_durbin_watson(Low)` — enrichment,均值差 +1.35,p 0.009
5. `sqrt(day_durbin_watson(Low))` — enrichment,均值差 +1.35,p 0.009
6. `day_durbin_watson(Vwap)` — enrichment,均值差 +1.32,p 0.000
7. `ts_var(ts_var(day_corr(Low, Low), 1), 1)` — enrichment,均值差 +1.26,p 0.017
8. `ts_var(day_corr(Vwap, Low), 1)` — enrichment,均值差 +1.07,p 0.023
9. `cs_first_high40(day_pos_ratio(Vwap), pow_2_5(ts_var(sqrt(day_durbin_watson(Vwap)), 10)))` — enrichment,均值差 +0.91,p 0.080
10. `day_pos_ratio(Vwap)` — enrichment,均值差 +0.80,p 0.016
11. `day_corr(Low, Low)` — enrichment,均值差 +0.58,p 0.044
12. `ts_var(day_corr(Low, Low), 1)` — enrichment,均值差 +0.57,p 0.050
13. `day_corr(Low, Vwap)` — enrichment,均值差 +0.55,p 0.098
14. `ts_var(day_corr(Low, Vwap), 1)` — enrichment,均值差 +0.55,p 0.098

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
