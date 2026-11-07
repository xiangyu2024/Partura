# 定位:种子 911,P 组,第 1 轮(只含 train / valid)

快照:prods911M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:98 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.50 | 0.000 | 7 | -0.06 / -1.56 | `cross_scale(LogFloatCap, 241)` |
| +1.07 | 0.017 | 7 | -0.46 / -1.53 | `abs_(LogFloatShares)` |
| +0.95 | 0.119 | 5 | -0.55 / -1.50 | `cross_scale(day_wstd(Low, Open), 241)` |
| +0.28 | 0.511 | 7 | -1.19 / -1.47 | `day_centroid(Volume)` |
| +0.10 | 0.370 | 9 | -1.36 / -1.46 | `cs_rank(day_pos_ratio(Volume))` |
| +0.10 | 0.495 | 11 | -1.37 / -1.46 | `day_pos_ratio(Volume)` |
| -0.07 | 0.769 | 5 | -1.52 / -1.45 | `cross_scale(day_centroid(Volume), 241)` |
| -0.79 | 0.703 | 12 | -2.14 / -1.35 | `day_wstd(Low, Open)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `cross_scale(LogFloatCap, 241)` — enrichment,均值差 +1.50,p 0.000
2. `abs_(LogFloatShares)` — enrichment,均值差 +1.07,p 0.017

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
