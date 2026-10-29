# 定位:种子 807,B 组,第 1 轮(只含 train / valid)

快照:c05s807M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.18 | +1.18 | +1.35 | -1 | 20 | c05s807M1_I0_open_search | `pow_2(pow_2(day_wmean(Ret, Ret)))` |

## 共性:66 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.27 | 0.000 | 5 | +0.99 / -1.27 | `pow_2(day_wmean(Ret, Ret))` |
| +1.87 | 0.000 | 12 | +0.42 / -1.44 | `day_wmean(Ret, Ret)` |
| +0.62 | 0.021 | 10 | -0.57 / -1.20 | `ts_cov(day_median(Vwap), day_var(Ret), 20)` |
| +0.57 | 0.026 | 13 | -0.65 / -1.21 | `day_var(Ret)` |
| +0.44 | 0.047 | 14 | -0.76 / -1.20 | `day_median(Vwap)` |
| +0.39 | 0.170 | 4 | -0.73 / -1.13 | `day_quantile_q75(Low)` |
| +0.33 | 0.197 | 7 | -0.81 / -1.14 | `day_quantile_q75(Volume)` |
| -0.04 | 0.510 | 5 | -1.14 / -1.10 | `inv(day_std(Close))` |
| -0.04 | 0.510 | 5 | -1.14 / -1.10 | `day_std(Close)` |

## 拆解(2 次评估)

### head score +1.18:`pow_2(pow_2(day_wmean(Ret, Ret)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_wmean(Ret, Ret))` | +0.89 | +0.89 | +1.66 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Ret)` | -0.19 | -0.15 | -0.19 | — | (子树本身) |

## 机械核心卡(B0 按这个顺序取)

1. `pow_2(day_wmean(Ret, Ret))` — ablation,自身 score +0.89(所在 head +1.18)
2. `day_wmean(Ret, Ret)` — enrichment,均值差 +1.87,p 0.000
3. `ts_cov(day_median(Vwap), day_var(Ret), 20)` — enrichment,均值差 +0.62,p 0.021
4. `day_var(Ret)` — enrichment,均值差 +0.57,p 0.026
5. `day_median(Vwap)` — enrichment,均值差 +0.44,p 0.047

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
