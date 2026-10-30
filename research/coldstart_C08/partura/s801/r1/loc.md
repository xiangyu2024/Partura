# 定位:种子 801,P 组,第 1 轮(只含 train / valid)

快照:c07s801M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:95 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.80 | 0.033 | 4 | -0.54 / -1.34 | `pow_3(LogFloatShares)` |
| +0.76 | 0.000 | 46 | -0.91 / -1.67 | `day_durbin_watson(Volume)` |
| +0.73 | 0.012 | 8 | -0.64 / -1.36 | `pow_2_5(pow_2_5(day_durbin_watson(Volume)))` |
| +0.72 | 0.049 | 4 | -0.61 / -1.33 | `cross_cov(pow_2_5(pow_2_5(day_durbin_watson(Volume))), ts_med(day_first(Volume), 30), 15)` |
| +0.72 | 0.049 | 4 | -0.61 / -1.33 | `pow_05(cross_cov(pow_2_5(pow_2_5(day_durbin_watson(Volume))), ts_med(day_first(Volume), 30), 15))` |
| +0.71 | 0.001 | 44 | -0.92 / -1.63 | `pow_2_5(day_durbin_watson(Volume))` |
| +0.62 | 0.034 | 10 | -0.75 / -1.37 | `cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_skew(Volume), 30), 15)` |
| +0.61 | 0.040 | 9 | -0.76 / -1.36 | `pow_05(cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_skew(Volume), 30), 15))` |
| +0.58 | 0.014 | 15 | -0.81 / -1.40 | `ts_med(day_skew(Volume), 30)` |
| +0.55 | 0.205 | 5 | -0.79 / -1.33 | `cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_ar1_coefficient(Vwap), 30), 15)` |
| +0.54 | 0.084 | 6 | -0.80 / -1.34 | `pow_3(pow_05(cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_skew(Volume), 30), 15)))` |
| +0.37 | 0.144 | 22 | -1.02 / -1.39 | `ts_med(day_ar1_coefficient(Vwap), 30)` |
| +0.33 | 0.412 | 6 | -0.99 / -1.32 | `day_sum(Vwap)` |
| +0.27 | 0.263 | 25 | -1.10 / -1.38 | `day_ar1_coefficient(Vwap)` |
| +0.21 | 0.066 | 18 | -1.13 / -1.34 | `day_skew(Volume)` |
| +0.00 | 0.360 | 6 | -1.30 / -1.30 | `cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_ar1_coefficient(Vwap), 30), 60)` |
| -0.02 | 0.471 | 8 | -1.32 / -1.30 | `ts_med(day_first(Volume), 30)` |
| -0.07 | 0.598 | 9 | -1.36 / -1.30 | `day_first(Volume)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `pow_3(LogFloatShares)` — enrichment,均值差 +0.80,p 0.033
2. `day_durbin_watson(Volume)` — enrichment,均值差 +0.76,p 0.000
3. `pow_2_5(pow_2_5(day_durbin_watson(Volume)))` — enrichment,均值差 +0.73,p 0.012
4. `cross_cov(pow_2_5(pow_2_5(day_durbin_watson(Volume))), ts_med(day_first(Volume), 30), 15)` — enrichment,均值差 +0.72,p 0.049
5. `pow_05(cross_cov(pow_2_5(pow_2_5(day_durbin_watson(Volume))), ts_med(day_first(Volume), 30), 15))` — enrichment,均值差 +0.72,p 0.049
6. `pow_2_5(day_durbin_watson(Volume))` — enrichment,均值差 +0.71,p 0.001
7. `cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_skew(Volume), 30), 15)` — enrichment,均值差 +0.62,p 0.034
8. `pow_05(cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_skew(Volume), 30), 15))` — enrichment,均值差 +0.61,p 0.040
9. `ts_med(day_skew(Volume), 30)` — enrichment,均值差 +0.58,p 0.014
10. `pow_3(pow_05(cross_cov(pow_2_5(day_durbin_watson(Volume)), ts_med(day_skew(Volume), 30), 15)))` — enrichment,均值差 +0.54,p 0.084
11. `day_skew(Volume)` — enrichment,均值差 +0.21,p 0.066

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
