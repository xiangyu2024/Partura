# 定位:种子 903,P 组,第 1 轮(只含 train / valid)

快照:prods903M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.63 | +0.63 | +1.13 | +1 | 5 | prods903M1_I0_open_search | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)), sqrt(day_centroid(Open)))` |

## 共性:117 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.08 | 0.000 | 76 | -0.27 / -1.35 | `day_open(Open)` |
| +1.05 | 0.000 | 69 | -0.22 / -1.27 | `cs_mask_top_replace_mean_neg(day_open(Open))` |
| +0.76 | 0.001 | 10 | +0.04 / -0.71 | `day_centroid(Amt)` |
| +0.75 | 0.030 | 7 | +0.06 / -0.69 | `pow_3(cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3))))` |
| +0.69 | 0.013 | 6 | +0.00 / -0.69 | `sqrt(day_centroid(Amt))` |
| +0.64 | 0.002 | 51 | -0.29 / -0.93 | `pow_3(cs_mask_top_replace_mean_neg(day_open(Open)))` |
| +0.63 | 0.027 | 15 | -0.10 / -0.73 | `cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3)))` |
| +0.55 | 0.004 | 41 | -0.30 / -0.84 | `day_quantile_q75(cross_valid_count(Open, 3))` |
| +0.45 | 0.156 | 5 | -0.22 / -0.67 | `day_quantile_q75(cross_valid_count(Open, 30))` |
| +0.41 | 0.173 | 4 | -0.25 / -0.66 | `day_quantile_q75(cross_valid_count(Volume, 241))` |
| +0.41 | 0.256 | 4 | -0.26 / -0.66 | `day_quantile_q75(cross_valid_count(Open, 60))` |
| +0.24 | 0.221 | 21 | -0.45 / -0.69 | `day_quantile_q75(cross_valid_count(Open, 241))` |

## 拆解(7 次评估)

### head score +0.63:`cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)), sqrt(day_centroid(Open)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_mask_top_replace_mean_neg(day_open(Open))` | +0.29 | +0.29 | +0.85 | — | (子树本身) |
| sufficiency | `sqrt(day_centroid(Open))` | -3.27 | -2.96 | -3.27 | — | (子树本身) |
| sufficiency | `day_open(Open)` | -1.35 | -1.35 | -0.40 | — | (子树本身) |
| sufficiency | `day_centroid(Open)` | -3.27 | -2.96 | -3.27 | — | (子树本身) |
| knockout | `cs_mask_top_replace_mean_neg(day_open(Open))` | -1.22 | -1.22 | -0.29 | +1.84 | `cs_last_high05(day_open(Open), sqrt(day_centroid(Open)))` |
| knockout | `sqrt(day_centroid(Open))` | +0.63 | +0.63 | +1.12 | -0.00 | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Open)), day_centroid(Open))` |
| swap | `Open->Close` | +0.62 | +0.62 | +1.17 | — | `cs_last_high05(cs_mask_top_replace_mean_neg(day_open(Close)), sqrt(day_centroid(Close)))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_open(Open)` — enrichment,均值差 +1.08,p 0.000
2. `cs_mask_top_replace_mean_neg(day_open(Open))` — enrichment,均值差 +1.05,p 0.000
3. `day_centroid(Amt)` — enrichment,均值差 +0.76,p 0.001
4. `pow_3(cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3))))` — enrichment,均值差 +0.75,p 0.030
5. `sqrt(day_centroid(Amt))` — enrichment,均值差 +0.69,p 0.013
6. `pow_3(cs_mask_top_replace_mean_neg(day_open(Open)))` — enrichment,均值差 +0.64,p 0.002
7. `cs_last_high05(pow_3(cs_mask_top_replace_mean_neg(day_open(Open))), day_quantile_q75(cross_valid_count(Open, 3)))` — enrichment,均值差 +0.63,p 0.027
8. `day_quantile_q75(cross_valid_count(Open, 3))` — enrichment,均值差 +0.55,p 0.004

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
