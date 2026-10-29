# 定位:种子 801,B 组,第 1 轮(只含 train / valid)

快照:c05s801M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.50 | +0.50 | +0.79 | -1 | 20 | c05s801M1_I0_open_search | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` |

## 共性:90 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.44 | 0.000 | 28 | +0.48 / -0.96 | `pow_3(LogFloatShares)` |
| +1.15 | 0.006 | 12 | +0.48 / -0.67 | `pow_05(pow_3(LogFloatShares))` |
| +1.12 | 0.000 | 10 | +0.48 / -0.64 | `pow_3(pow_3(LogFloatShares))` |
| +1.06 | 0.035 | 6 | +0.48 / -0.58 | `pow_3(pow_05(pow_3(LogFloatShares)))` |
| +1.05 | 0.072 | 5 | +0.48 / -0.57 | `pow_05(LogFloatShares)` |
| +1.05 | 0.122 | 5 | +0.48 / -0.57 | `pow_2_5(LogFloatShares)` |
| +1.04 | 0.028 | 4 | +0.48 / -0.56 | `pow_05(pow_3(pow_3(LogFloatShares)))` |
| +1.04 | 0.157 | 4 | +0.48 / -0.56 | `pow_05(pow_2_5(LogFloatShares))` |

## 拆解(4 次评估)

### head score +0.50:`inv(pow_3(pow_3(pow_3(LogFloatShares))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_3(pow_3(pow_3(LogFloatShares)))` | +0.47 | +0.47 | +0.78 | — | (子树本身) |
| sufficiency | `pow_3(pow_3(LogFloatShares))` | +0.48 | +0.48 | +0.77 | — | (子树本身) |
| sufficiency | `pow_3(LogFloatShares)` | +0.48 | +0.48 | +0.77 | — | (子树本身) |
| knockout | `pow_3(pow_3(pow_3(LogFloatShares)))` | +0.48 | +0.48 | +0.79 | +0.02 | `inv(pow_3(pow_3(LogFloatShares)))` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_3(LogFloatShares)` — enrichment,均值差 +1.44,p 0.000
2. `pow_05(pow_3(LogFloatShares))` — enrichment,均值差 +1.15,p 0.006
3. `pow_3(pow_3(LogFloatShares))` — enrichment,均值差 +1.12,p 0.000
4. `pow_3(pow_05(pow_3(LogFloatShares)))` — enrichment,均值差 +1.06,p 0.035
5. `pow_05(LogFloatShares)` — enrichment,均值差 +1.05,p 0.072
6. `pow_05(pow_3(pow_3(LogFloatShares)))` — enrichment,均值差 +1.04,p 0.028

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
