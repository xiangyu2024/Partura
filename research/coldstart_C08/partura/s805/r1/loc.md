# 定位:种子 805,P 组,第 1 轮(只含 train / valid)

快照:c07s805M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:62 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.74 | 0.000 | 29 | +0.44 / -2.31 | `day_centroid(Volume)` |
| +1.93 | 0.000 | 15 | +0.44 / -1.49 | `pow_2_5(day_centroid(Volume))` |
| +1.68 | 0.001 | 8 | +0.44 / -1.24 | `pow_2_5(pow_2_5(day_centroid(Volume)))` |
| +1.58 | 0.111 | 5 | +0.43 / -1.15 | `pow_1_5(day_centroid(Volume))` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `day_centroid(Volume)` — enrichment,均值差 +2.74,p 0.000
2. `pow_2_5(day_centroid(Volume))` — enrichment,均值差 +1.93,p 0.000
3. `pow_2_5(pow_2_5(day_centroid(Volume)))` — enrichment,均值差 +1.68,p 0.001

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
