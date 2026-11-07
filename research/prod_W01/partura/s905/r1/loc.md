# 定位:种子 905,P 组,第 1 轮(只含 train / valid)

快照:prods905M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:109 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.40 | 0.075 | 26 | -0.56 / -0.96 | `pow_2(LogFloatShares)` |
| +0.36 | 0.013 | 15 | -0.55 / -0.91 | `inv(LogFloatShares)` |
| +0.35 | 0.096 | 12 | -0.56 / -0.90 | `pow_3(pow_2(LogFloatShares))` |
| +0.33 | 0.896 | 11 | -0.57 / -0.90 | `cross_min(LogFloatShares, 30)` |
| +0.33 | 0.149 | 7 | -0.56 / -0.88 | `ts_quantile_q50(inv(LogFloatShares), 30)` |
| +0.33 | 0.159 | 6 | -0.55 / -0.88 | `pow_3(pow_3(pow_2(LogFloatShares)))` |
| +0.32 | 0.147 | 4 | -0.55 / -0.87 | `pow_3(LogFloatShares)` |
| +0.31 | 0.487 | 4 | -0.56 / -0.87 | `ts_quantile_q50(pow_2(LogFloatShares), 30)` |
| +0.31 | 0.766 | 4 | -0.57 / -0.87 | `pow_2(cross_min(LogFloatShares, 30))` |
| +0.08 | 0.145 | 6 | -0.79 / -0.87 | `ts_quantile_q75(LogFloatShares, 30)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `pow_2(LogFloatShares)` — enrichment,均值差 +0.40,p 0.075
2. `inv(LogFloatShares)` — enrichment,均值差 +0.36,p 0.013
3. `pow_3(pow_2(LogFloatShares))` — enrichment,均值差 +0.35,p 0.096

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
