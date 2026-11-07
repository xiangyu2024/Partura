# 定位:种子 908,P 组,第 1 轮(只含 train / valid)

快照:prods908M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(2 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.75 | +1.46 | +0.75 | +1 | 20 | prods908M1_I0_open_search | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt))), 10)` |
| +0.58 | +0.73 | +0.58 | +1 | 5 | prods908M1_I0_open_search | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt))` |

## 共性:86 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.31 | 0.007 | 5 | +0.10 / -1.21 | `cs_regres(ListAge, day_centroid(Amt))` |
| +1.26 | 0.000 | 26 | -0.25 / -1.51 | `day_centroid(Amt)` |
| +1.25 | 0.002 | 8 | -0.00 / -1.25 | `cs_regres(ListAge, pow_3(day_centroid(Amt)))` |
| +1.06 | 0.002 | 12 | -0.21 / -1.28 | `pow_3(day_centroid(Amt))` |
| +0.82 | 0.074 | 4 | -0.35 / -1.17 | `cs_regres(ListAge, LogFloatShares)` |
| -0.45 | 0.892 | 5 | -1.55 / -1.10 | `day_max(Ret)` |

## 拆解(12 次评估)

### head score +0.75:`ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt))), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_regres(ListAge, pow_3(day_centroid(Amt)))` | -0.37 | -0.37 | -0.33 | — | (子树本身) |
| sufficiency | `pow_3(day_centroid(Amt))` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `cs_regres(ListAge, pow_3(day_centroid(Amt)))` | — | — | — | — | `ts_quantile_q75(ListAge, 10)` |
| knockout | `pow_3(day_centroid(Amt))` | +0.66 | +1.30 | +0.66 | +0.09 | `ts_quantile_q75(cs_regres(ListAge, day_centroid(Amt)), 10)` |
| swap | `Amt->Volume` | +0.82 | +1.50 | +0.82 | — | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Volume))), 10)` |
| window | `ts_quantile_q75@10->5` | +0.51 | +1.10 | +0.51 | — | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt))), 5)` |
| window | `ts_quantile_q75@10->20` | +0.90 | +1.61 | +0.90 | — | `ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt))), 20)` |

### head score +0.58:`cs_bucket_zscore(day_quantile_q25(High), day_wmean(Open, Amt))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q25(High)` | -1.35 | -1.35 | -0.40 | — | (子树本身) |
| sufficiency | `day_wmean(Open, Amt)` | -1.33 | -1.33 | -0.40 | — | (子树本身) |
| swap | `High->Low` | +0.49 | +0.63 | +0.49 | — | `cs_bucket_zscore(day_quantile_q25(Low), day_wmean(Open, Amt))` |
| swap | `Open->Close` | +0.49 | +0.68 | +0.49 | — | `cs_bucket_zscore(day_quantile_q25(High), day_wmean(Close, Amt))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_regres(ListAge, day_centroid(Amt))` — enrichment,均值差 +1.31,p 0.007
2. `day_centroid(Amt)` — enrichment,均值差 +1.26,p 0.000
3. `cs_regres(ListAge, pow_3(day_centroid(Amt)))` — enrichment,均值差 +1.25,p 0.002
4. `pow_3(day_centroid(Amt))` — enrichment,均值差 +1.06,p 0.002
5. `cs_regres(ListAge, LogFloatShares)` — enrichment,均值差 +0.82,p 0.074

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.15(window ts_quantile_q75@10->20):`ts_quantile_q75(cs_regres(ListAge, pow_3(day_centroid(Amt))), 20)`
