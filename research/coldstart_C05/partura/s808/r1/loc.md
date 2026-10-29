# 定位:种子 808,B 组,第 1 轮(只含 train / valid)

快照:c05s808M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:91 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.11 | 0.010 | 14 | +0.48 / -0.63 | `inv(LogFloatShares)` |
| +1.00 | 0.003 | 5 | +0.49 / -0.52 | `ts_decay_linear(LogFloatShares, 50)` |
| +0.98 | 0.051 | 4 | +0.48 / -0.50 | `abs_(LogFloatShares)` |
| +0.98 | 0.059 | 4 | +0.48 / -0.50 | `log(LogFloatShares)` |
| +0.98 | 0.596 | 5 | +0.47 / -0.51 | `ts_max(LogFloatShares, 50)` |
| +0.97 | 0.382 | 4 | +0.47 / -0.50 | `log(inv(LogFloatShares))` |
| +0.97 | 0.442 | 4 | +0.47 / -0.50 | `pow_2(LogFloatShares)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `inv(LogFloatShares)` — enrichment,均值差 +1.11,p 0.010
2. `ts_decay_linear(LogFloatShares, 50)` — enrichment,均值差 +1.00,p 0.003
3. `abs_(LogFloatShares)` — enrichment,均值差 +0.98,p 0.051
4. `log(LogFloatShares)` — enrichment,均值差 +0.98,p 0.059

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
