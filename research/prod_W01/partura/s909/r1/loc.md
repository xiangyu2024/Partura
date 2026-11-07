# 定位:种子 909,P 组,第 1 轮(只含 train / valid)

快照:prods909M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:90 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.77 | 0.144 | 27 | -0.60 / -1.38 | `neg(LogFloatShares)` |
| +0.68 | 0.318 | 6 | -0.51 / -1.19 | `neg(cs_rank(neg(LogFloatShares)))` |
| +0.68 | 0.031 | 9 | -0.54 / -1.21 | `neg(neg(LogFloatShares))` |
| +0.60 | 0.000 | 13 | -0.63 / -1.23 | `pow_1_5(LogFloatShares)` |
| +0.57 | 0.603 | 13 | -0.66 / -1.23 | `cs_rank(neg(LogFloatShares))` |
| +0.48 | 0.008 | 9 | -0.71 / -1.19 | `cs_rank(pow_1_5(LogFloatShares))` |
| +0.31 | 0.078 | 5 | -0.86 / -1.16 | `cs_rank(cs_rank(pow_1_5(LogFloatShares)))` |
| +0.18 | 0.257 | 7 | -0.98 / -1.16 | `cs_rank(LogFloatShares)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `neg(neg(LogFloatShares))` — enrichment,均值差 +0.68,p 0.031
2. `pow_1_5(LogFloatShares)` — enrichment,均值差 +0.60,p 0.000
3. `cs_rank(pow_1_5(LogFloatShares))` — enrichment,均值差 +0.48,p 0.008
4. `cs_rank(cs_rank(pow_1_5(LogFloatShares)))` — enrichment,均值差 +0.31,p 0.078

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
