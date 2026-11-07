# 定位:种子 910,P 组,第 1 轮(只含 train / valid)

快照:prods910M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(2 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.85 | +1.85 | +2.58 | -1 | 5 | prods910M1_I0_open_search | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` |
| +0.63 | +0.63 | +1.95 | -1 | 0 | prods910M1_I0_open_search | `cs_first_low20(LogFloatCap, day_last(High))` |

## 共性:111 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.13 | 0.005 | 9 | +1.52 / -0.61 | `ts_quantile_q75(LogFloatCap, 10)` |
| +1.84 | 0.004 | 6 | +1.30 / -0.53 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 1)` |
| +1.84 | 0.060 | 5 | +1.32 / -0.52 | `cross_fangzheng(ts_quantile_q75(LogFloatCap, 10), 3)` |
| +1.82 | 0.008 | 4 | +1.32 / -0.50 | `cross_fangzheng(LogFloatCap, 3)` |
| +1.79 | 0.000 | 22 | +1.00 / -0.79 | `ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)` |
| +1.79 | 0.000 | 39 | +0.72 / -1.06 | `ts_quantile_q75(LogFloatCap, 1)` |
| +1.37 | 0.008 | 9 | +0.82 / -0.55 | `cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3)` |
| +1.05 | 0.092 | 4 | +0.57 / -0.47 | `cs_first_low20(cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3), ts_quantile_q75(LogFloatCap, 1))` |
| +1.04 | 0.043 | 6 | +0.55 / -0.49 | `cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3)` |
| -0.87 | 0.852 | 5 | -1.26 / -0.40 | `div(day_median(Amt), day_std(High))` |
| -0.87 | 0.852 | 5 | -1.26 / -0.40 | `ts_regbeta(cross_product(LogFloatCap, 15), div(day_median(Amt), day_std(High)), 40)` |
| -0.88 | 0.831 | 4 | -1.28 / -0.40 | `day_quantile_q75(Open)` |
| -0.88 | 0.862 | 6 | -1.26 / -0.39 | `day_median(Amt)` |
| -0.98 | 0.955 | 8 | -1.34 / -0.37 | `cross_product(LogFloatCap, 15)` |
| -0.98 | 0.954 | 7 | -1.35 / -0.37 | `day_std(High)` |
| -1.01 | 0.924 | 5 | -1.40 / -0.39 | `day_mean(Low)` |
| -1.01 | 0.924 | 5 | -1.40 / -0.39 | `cross_fangzheng(day_mean(Low), 3)` |

## 拆解(10 次评估)

### head score +1.85:`cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3)` | -4.83 | -3.32 | -4.83 | — | (子树本身) |
| sufficiency | `cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3)` | -4.86 | -3.45 | -4.86 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)` | -5.03 | -3.60 | -5.03 | — | (子树本身) |
| knockout | `cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3)` | +1.82 | +1.82 | +2.59 | +0.03 | `cs_first_low20(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` |
| knockout | `ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)` | +1.85 | +1.85 | +2.58 | -0.00 | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3), 3), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` |
| knockout | `ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)` | +1.85 | +1.85 | +2.58 | -0.00 | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 3), ts_quantile_q75(LogFloatCap, 1))` |
| window | `cross_fangzheng@3->2` | +1.84 | +1.84 | +2.61 | — | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 2), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` |
| window | `cross_fangzheng@3->6` | +1.81 | +1.81 | +2.59 | — | `cs_first_low20(cross_fangzheng(cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3), 6), ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1))` |

### head score +0.63:`cs_first_low20(LogFloatCap, day_last(High))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_last(High)` | -1.34 | -1.34 | -0.40 | — | (子树本身) |
| swap | `High->Low` | +0.62 | +0.62 | +1.91 | — | `cs_first_low20(LogFloatCap, day_last(Low))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_quantile_q75(LogFloatCap, 10)` — enrichment,均值差 +2.13,p 0.005
2. `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 1)` — enrichment,均值差 +1.84,p 0.004
3. `cross_fangzheng(ts_quantile_q75(LogFloatCap, 10), 3)` — enrichment,均值差 +1.84,p 0.060
4. `cross_fangzheng(LogFloatCap, 3)` — enrichment,均值差 +1.82,p 0.008
5. `ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1)` — enrichment,均值差 +1.79,p 0.000
6. `ts_quantile_q75(LogFloatCap, 1)` — enrichment,均值差 +1.79,p 0.000
7. `cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3)` — enrichment,均值差 +1.37,p 0.008
8. `cs_first_low20(cross_fangzheng(ts_quantile_q75(LogFloatCap, 1), 3), ts_quantile_q75(LogFloatCap, 1))` — enrichment,均值差 +1.05,p 0.092
9. `cross_fangzheng(ts_quantile_q75(ts_quantile_q75(LogFloatCap, 1), 1), 3)` — enrichment,均值差 +1.04,p 0.043

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
