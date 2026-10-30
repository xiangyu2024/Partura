# 定位:种子 804,P 组,第 1 轮(只含 train / valid)

快照:c07s804M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:117 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.69 | 0.000 | 31 | -0.58 / -1.28 | `day_pos_ratio(Open)` |
| +0.64 | 0.003 | 10 | -0.51 / -1.15 | `cs_last_high20(day_pos_ratio(Open), cs_normalize(BoardCode))` |
| +0.58 | 0.018 | 8 | -0.55 / -1.13 | `pow_05(LogFloatShares)` |
| +0.56 | 0.074 | 5 | -0.55 / -1.12 | `ts_var(LogFloatShares, 10)` |
| +0.55 | 0.297 | 4 | -0.57 / -1.11 | `pow_05(cross_ema(LogFloatShares, 241))` |
| +0.48 | 0.319 | 17 | -0.68 / -1.16 | `cross_ema(LogFloatShares, 241)` |
| +0.44 | 0.024 | 4 | -0.67 / -1.11 | `cs_last_high20(day_pos_ratio(Open), cs_normalize(day_gini(High)))` |
| +0.25 | 0.224 | 6 | -0.86 / -1.11 | `cross_ema(LogFloatShares, 3)` |
| +0.21 | 0.063 | 20 | -0.92 / -1.13 | `cs_normalize(BoardCode)` |
| -0.01 | 0.061 | 8 | -1.10 / -1.09 | `cs_normalize(day_gini(High))` |
| -0.11 | 0.761 | 14 | -1.19 / -1.08 | `ts_var(day_gini(High), 10)` |
| -0.18 | 0.617 | 27 | -1.23 / -1.05 | `day_gini(High)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `day_pos_ratio(Open)` — enrichment,均值差 +0.69,p 0.000
2. `cs_last_high20(day_pos_ratio(Open), cs_normalize(BoardCode))` — enrichment,均值差 +0.64,p 0.003
3. `pow_05(LogFloatShares)` — enrichment,均值差 +0.58,p 0.018
4. `ts_var(LogFloatShares, 10)` — enrichment,均值差 +0.56,p 0.074
5. `cs_last_high20(day_pos_ratio(Open), cs_normalize(day_gini(High)))` — enrichment,均值差 +0.44,p 0.024
6. `cs_normalize(BoardCode)` — enrichment,均值差 +0.21,p 0.063

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
