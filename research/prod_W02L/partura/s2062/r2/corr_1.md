# 相关度表:种子 2062,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.44 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.12 | 0.90 | 0.26 | 0.20 | 0.88 | 0.64 | `day_median(Amt)` |
| slot a seed 1 | 过 | 0.22 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.13 | 0.75 | 0.08 | 0.09 | 0.66 | 0.58 | `cross_mean(div(day_median(Amt), add(day_mean(Amt), 1)), 20)` |
| slot a seed 2 | 过 | 0.21 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.13 | 0.72 | 0.14 | 0.08 | 0.63 | 0.60 | `cross_mean(div(day_median(Amt), add(day_mean(Amt), 1)), 60)` |
| slot a seed 3 | 过 | 0.15 | `day_pdf_tail_sum_m(Ret, Volume, 50, False)` | 0.05 | 0.20 | 0.15 | 0.03 | 0.21 | 0.08 | `cross_regres(day_median(Amt), day_mean(Amt), 60)` |
| slot a seed 4 | 过 | 0.21 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.13 | 0.01 | 0.70 | 0.04 | 0.06 | 0.07 | `cross_regalpha(day_median(Amt), day_std(Ret), 60)` |
| slot a seed 5 | 过 | 0.23 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.08 | 0.71 | 0.04 | 0.06 | 0.67 | 0.74 | `cross_regbeta(day_median(Amt), day_std(Ret), 60)` |
| slot a seed 6 | 过 | 0.18 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.11 | 0.31 | 0.19 | 0.09 | 0.31 | 0.01 | `cross_corr(day_median(Amt), day_std(Ret), 60)` |
| slot a seed 7 | 过 | 0.02 | `ts_mean(day_kurt(div(in_regres(Ret, in_mean_full(Ret), 20), ` | 0.06 | 0.10 | 0.06 | 0.13 | 0.07 | 0.04 | `cross_corr(day_median(Amt), day_sum(Ret), 60)` |
| slot a seed 8 | 过 | 0.18 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.08 | 0.06 | 0.28 | 0.51 | 0.02 | 0.06 | `sub(cross_mean(day_median(Amt), 10), cross_mean(day_median(Amt), 60))` |
| slot a seed 9 | 过 | 0.40 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.09 | 0.94 | 0.25 | 0.01 | 0.92 | 0.58 | `cross_stddev(day_median(Amt), 60)` |
| slot a seed 10 | 过 | 0.23 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.02 | 0.14 | 0.33 | 0.47 | 0.17 | 0.04 | `cross_zscore(day_median(Amt), 120)` |
| slot a seed 11 | 过 | 0.39 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.16 | 0.40 | 0.43 | 0.05 | 0.41 | 0.26 | `cs_bucket_demean(cross_mean(day_median(Amt), 20), LogFloatCap)` |
| slot a seed 12 | 过 | 0.20 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.15 | 0.10 | 0.28 | 0.04 | 0.11 | 0.54 | `cs_regres(cross_mean(day_median(Amt), 30), LogFloatCap)` |
| slot b seed 1 | 过 | 0.25 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.09 | 0.80 | 0.06 | 0.07 | 0.72 | 0.63 | `cross_mean(day_gini(Amt), 40)` |
| slot b seed 2 | 过 | 0.72 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.73 | 0.50 | 0.47 | 0.06 | 0.53 | 0.04 | `cross_mean(day_centroid(Amt), 40)` |
| slot b seed 3 | 过 | 0.33 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.30 | 0.09 | 0.26 | 0.07 | 0.14 | 0.07 | `cross_mean(sub(day_centroid(Amt), day_centroid(abs_(Ret))), 40)` |
| slot b seed 4 | 过 | 0.20 | `day_pdf_tail_sum_m(Ret, Volume, 50, False)` | 0.11 | 0.07 | 0.02 | 0.40 | 0.06 | 0.07 | `cross_regres(day_gini(Amt), day_std(Ret), 60)` |
| slot b seed 5 | 过 | 0.08 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.19 | 0.15 | 0.13 | 0.01 | 0.19 | 0.01 | `cross_corr(day_gini(Amt), day_sum(Ret), 60)` |
| slot b seed 6 | 过 | 0.19 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.07 | 0.51 | 0.03 | 0.12 | 0.43 | 0.01 | `cs_bucket_demean(cross_mean(day_gini(Amt), 30), LogFloatCap)` |
| slot b seed 7 | 过 | 0.24 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.04 | 0.61 | 0.11 | 0.07 | 0.57 | 0.47 | `cross_regbeta(day_gini(Amt), day_median(Amt), 241)` |
| slot b seed 8 | 过 | 0.24 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.07 | 0.70 | 0.05 | 0.05 | 0.63 | 0.58 | `cross_mean(day_gini(abs_(Ret)), 40)` |
| slot b seed 9 | 过 | 0.16 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.04 | 0.17 | 0.24 | 0.18 | 0.17 | 0.03 | `sub(cross_mean(day_gini(Amt), 10), cross_mean(day_gini(Amt), 60))` |
| slot b seed 10 | 过 | 0.70 | `day_pdf_tail_sum_m(Ret, Volume, 50, False)` | 0.31 | 0.01 | 0.07 | 0.16 | 0.02 | 0.00 | `cross_zscore(day_centroid(Amt), 120)` |
| slot b seed 11 | 过 | 0.22 | `cross_mean(day_pdf_tail_sum_m(Ret, Volume, 50, False, 'rank'` | 0.27 | 0.26 | 0.30 | 0.00 | 0.22 | 0.13 | `cs_regres(cross_mean(day_distinct_ratio(Close), 20), LogFloatCap)` |
| slot b seed 12 | 过 | 0.12 | `rank(day_pdf_tail_sum_m(abs_(div(in_regres(Ret, in_mean_full` | 0.17 | 0.14 | 0.31 | 0.09 | 0.07 | 0.33 | `cross_stddev(day_centroid(Amt), 60)` |
