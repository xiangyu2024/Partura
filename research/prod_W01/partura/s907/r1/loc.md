# 定位:种子 907,P 组,第 1 轮(只含 train / valid)

快照:prods907M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:109 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.99 | 0.000 | 53 | -0.59 / -1.58 | `day_std(Volume)` |
| +0.89 | 0.000 | 49 | -0.61 / -1.49 | `day_var(in_skew_full(Open))` |
| +0.80 | 0.000 | 9 | -0.37 / -1.16 | `day_var(in_mean_full(Volume))` |
| +0.79 | 0.007 | 4 | -0.34 / -1.13 | `day_var(in_skew_full(Volume))` |
| +0.73 | 0.000 | 34 | -0.59 / -1.33 | `pow_2(day_std(Volume))` |
| +0.71 | 0.013 | 6 | -0.43 / -1.14 | `day_var(in_mean_full(Open))` |
| +0.64 | 0.026 | 7 | -0.50 / -1.14 | `abs_(abs_(pow_2(day_std(Volume))))` |
| +0.57 | 0.149 | 4 | -0.55 / -1.12 | `cs_last_high05(day_var(in_skew_full(Open)), pow_2(day_std(Volume)))` |
| +0.57 | 0.014 | 14 | -0.60 / -1.17 | `pow_3(pow_2(day_std(Volume)))` |
| +0.56 | 0.019 | 11 | -0.59 / -1.15 | `abs_(pow_2(day_std(Volume)))` |
| +0.55 | 0.047 | 10 | -0.59 / -1.15 | `pow_3(day_std(Volume))` |
| +0.40 | 0.514 | 5 | -0.71 / -1.12 | `day_std(Open)` |
| +0.39 | 0.558 | 4 | -0.72 / -1.11 | `pow_2(day_std(Open))` |
| -0.56 | 0.978 | 4 | -1.64 / -1.08 | `day_var(Open)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `day_std(Volume)` — enrichment,均值差 +0.99,p 0.000
2. `day_var(in_skew_full(Open))` — enrichment,均值差 +0.89,p 0.000
3. `day_var(in_mean_full(Volume))` — enrichment,均值差 +0.80,p 0.000
4. `day_var(in_skew_full(Volume))` — enrichment,均值差 +0.79,p 0.007
5. `pow_2(day_std(Volume))` — enrichment,均值差 +0.73,p 0.000
6. `day_var(in_mean_full(Open))` — enrichment,均值差 +0.71,p 0.013
7. `abs_(abs_(pow_2(day_std(Volume))))` — enrichment,均值差 +0.64,p 0.026
8. `pow_3(pow_2(day_std(Volume)))` — enrichment,均值差 +0.57,p 0.014
9. `abs_(pow_2(day_std(Volume)))` — enrichment,均值差 +0.56,p 0.019
10. `pow_3(day_std(Volume))` — enrichment,均值差 +0.55,p 0.047

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
