# 定位:种子 806,B 组,第 1 轮(只含 train / valid)

快照:c05s806M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:85 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.80 | 0.000 | 18 | -0.67 / -1.47 | `add(LimitWidth, day_cov(Vwap, Ret))` |
| +0.78 | 0.004 | 6 | -0.58 / -1.35 | `add(LimitWidth, add(LimitWidth, day_cov(Vwap, Ret)))` |
| +0.73 | 0.011 | 5 | -0.61 / -1.34 | `ts_min(add(LimitWidth, day_cov(Vwap, Ret)), 20)` |
| +0.64 | 0.001 | 19 | -0.80 / -1.44 | `add(LimitWidth, day_cov(High, Ret))` |
| +0.63 | 0.000 | 22 | -0.83 / -1.46 | `day_cov(Vwap, Ret)` |
| +0.63 | 0.001 | 22 | -0.83 / -1.46 | `day_cov(High, Ret)` |
| +0.43 | 0.042 | 4 | -0.89 / -1.32 | `add(add(LimitWidth, day_cov(Vwap, Ret)), day_cov(Vwap, Ret))` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `add(LimitWidth, day_cov(Vwap, Ret))` — enrichment,均值差 +0.80,p 0.000
2. `add(LimitWidth, add(LimitWidth, day_cov(Vwap, Ret)))` — enrichment,均值差 +0.78,p 0.004
3. `ts_min(add(LimitWidth, day_cov(Vwap, Ret)), 20)` — enrichment,均值差 +0.73,p 0.011
4. `add(LimitWidth, day_cov(High, Ret))` — enrichment,均值差 +0.64,p 0.001
5. `day_cov(Vwap, Ret)` — enrichment,均值差 +0.63,p 0.000
6. `day_cov(High, Ret)` — enrichment,均值差 +0.63,p 0.001
7. `add(add(LimitWidth, day_cov(Vwap, Ret)), day_cov(Vwap, Ret))` — enrichment,均值差 +0.43,p 0.042

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
