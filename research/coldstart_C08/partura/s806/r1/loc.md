# 定位:种子 806,P 组,第 1 轮(只含 train / valid)

快照:c07s806M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:115 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.06 | 0.000 | 14 | -0.51 / -1.57 | `cross_max(cross_product(day_max(Ret), 3), 30)` |
| +1.04 | 0.000 | 9 | -0.48 / -1.52 | `abs_(cross_max(cross_product(day_max(Ret), 3), 30))` |
| +1.03 | 0.000 | 6 | -0.47 / -1.50 | `cross_max(abs_(cross_max(cross_product(day_max(Ret), 3), 30)), 30)` |
| +0.97 | 0.000 | 17 | -0.62 / -1.59 | `cross_product(day_max(Ret), 3)` |
| +0.86 | 0.000 | 24 | -0.76 / -1.62 | `day_max(Ret)` |
| +0.22 | 0.098 | 20 | -1.26 / -1.48 | `day_max(Close)` |
| +0.19 | 0.365 | 7 | -1.26 / -1.45 | `cs_first_high40(day_close(Vwap), LimitWidth)` |
| +0.18 | 0.228 | 11 | -1.28 / -1.46 | `cross_product(day_max(Close), 3)` |
| +0.18 | 0.540 | 15 | -1.28 / -1.47 | `day_close(Vwap)` |
| +0.14 | 0.381 | 6 | -1.31 / -1.45 | `cross_max(cross_product(day_max(Close), 3), 30)` |
| +0.13 | 0.689 | 5 | -1.32 / -1.45 | `day_std(Low)` |
| +0.11 | 0.473 | 4 | -1.33 / -1.45 | `cross_product(cross_max(cross_product(day_max(Close), 3), 30), 3)` |
| +0.11 | 0.667 | 5 | -1.34 / -1.45 | `day_es_ratio_lo(High)` |
| -0.02 | 0.203 | 4 | -1.46 / -1.44 | `add(LimitWidth, day_cov(High, Ret))` |
| -0.11 | 0.577 | 6 | -1.54 / -1.44 | `day_close(Ret)` |
| -0.19 | 0.316 | 11 | -1.62 / -1.42 | `day_cov(High, Ret)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `cross_max(cross_product(day_max(Ret), 3), 30)` — enrichment,均值差 +1.06,p 0.000
2. `abs_(cross_max(cross_product(day_max(Ret), 3), 30))` — enrichment,均值差 +1.04,p 0.000
3. `cross_max(abs_(cross_max(cross_product(day_max(Ret), 3), 30)), 30)` — enrichment,均值差 +1.03,p 0.000
4. `cross_product(day_max(Ret), 3)` — enrichment,均值差 +0.97,p 0.000
5. `day_max(Ret)` — enrichment,均值差 +0.86,p 0.000
6. `day_max(Close)` — enrichment,均值差 +0.22,p 0.098

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
