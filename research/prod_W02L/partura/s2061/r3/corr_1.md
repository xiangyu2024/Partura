# 相关度表:种子 2061,P 组,第 3 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.11 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.13 | 0.47 | 0.06 | 0.03 | 0.43 | 0.44 | `day_mean(Low)` |
| slot a seed 1 | 过 | 0.10 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.06 | 0.10 | 0.21 | 0.40 | 0.12 | 0.14 | `div(day_mean(Low), cross_max(day_mean(Low), 241))` |
| slot a seed 2 | 过 | 0.18 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.14 | 0.39 | 0.53 | 0.33 | 0.40 | 0.13 | `div(day_mean(Low), cross_min(day_mean(Low), 241))` |
| slot a seed 3 | 过 | 0.15 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.12 | 0.24 | 0.44 | 0.56 | 0.27 | 0.08 | `div(day_mean(Low), cross_mean(day_mean(Low), 120))` |
| slot a seed 4 | 废品 | 0.18 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.15 | 0.30 | 0.46 | 0.48 | 0.32 | 0.09 | `cross_rank(day_mean(Low), 241)` |
| slot a seed 5 | 过 | 0.02 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.12 | 0.02 | 0.12 | 0.00 | 0.03 | 0.27 | `cs_bucket_demean(day_mean(Low), LogFloatCap)` |
| slot a seed 6 | 过 | 0.06 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.12 | 0.18 | 0.11 | 0.01 | 0.16 | 0.01 | `cs_bucket_zscore(day_mean(Low), LogFloatCap)` |
| slot a seed 7 | 过 | 0.17 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.13 | 0.27 | 0.42 | 0.43 | 0.29 | 0.15 | `div(sub(day_mean(Low), cross_min(day_mean(Low), 241)), sub(cross_max(day_mean(Low), 241), cross_min(day_mean(Low), 241)))` |
| slot a seed 8 | 过 | 0.13 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.09 | 0.28 | 0.38 | 0.07 | 0.29 | 0.08 | `sub(cross_ema(day_mean(Low), 20), cross_ema(day_mean(Low), 120))` |
| slot a seed 9 | 过 | 0.27 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.16 | 0.14 | 0.18 | 0.12 | 0.16 | 0.15 | `cross_corr(day_mean(Low), day_sum(Amt), 60)` |
| slot a seed 10 | 过 | 0.09 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.06 | 0.11 | 0.21 | 0.37 | 0.12 | 0.13 | `cs_mask_top_replace_mean_neg(div(day_mean(Low), cross_max(day_mean(Low), 241)))` |
| slot a seed 11 | 过 | 0.19 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.16 | 0.31 | 0.47 | 0.45 | 0.33 | 0.10 | `cross_zscore(day_mean(Low), 241)` |
| slot a seed 12 | 过 | 0.15 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.10 | 0.24 | 0.31 | 0.07 | 0.26 | 0.09 | `div(cross_max(day_mean(Low), 60), cross_max(day_mean(Low), 241))` |
| slot b seed 1 | 过 | 0.28 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.13 | 0.49 | 0.44 | 0.02 | 0.52 | 0.04 | `cross_mean(day_centroid(Amt), 60)` |
| slot b seed 2 | 过 | 0.31 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.17 | 0.51 | 0.43 | 0.03 | 0.54 | 0.04 | `cross_ema(day_centroid(Volume), 40)` |
| slot b seed 3 | 过 | 0.06 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.04 | 0.78 | 0.09 | 0.08 | 0.70 | 0.63 | `cross_mean(day_gini(Amt), 60)` |
| slot b seed 4 | 过 | 0.05 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.6, True), ` | 0.08 | 0.12 | 0.23 | 0.29 | 0.14 | 0.06 | `cross_mean(sub(day_centroid(Amt), day_centroid(Volume)), 60)` |
| slot b seed 5 | 过 | 0.05 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.04 | 0.10 | 0.14 | 0.00 | 0.11 | 0.10 | `cross_corr(day_centroid(Amt), day_sum(Ret), 60)` |
| slot b seed 6 | 过 | 0.03 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.8, True), ` | 0.09 | 0.01 | 0.07 | 0.16 | 0.02 | 0.00 | `cross_zscore(day_centroid(Amt), 120)` |
| slot b seed 7 | 过 | 0.22 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.11 | 0.72 | 0.28 | 0.03 | 0.70 | 0.29 | `cross_mean(day_corr(in_index(Amt), Amt), 60)` |
| slot b seed 8 | 过 | 0.20 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.10 | 0.50 | 0.23 | 0.03 | 0.49 | 0.19 | `cross_tail_mean_q75(day_centroid(Amt), 60)` |
| slot b seed 9 | 过 | 0.28 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.13 | 0.49 | 0.43 | 0.01 | 0.52 | 0.02 | `cs_bucket_demean(cross_mean(day_centroid(Amt), 60), LogFloatCap)` |
| slot b seed 10 | 过 | 0.32 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.19 | 0.46 | 0.36 | 0.02 | 0.48 | 0.04 | `cross_mean(day_centroid(Amt), 120)` |
| slot b seed 11 | 过 | 0.12 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.12 | 0.04 | 0.18 | 0.03 | 0.08 | 0.13 | `cross_autocorr(day_centroid(Amt), 60, 1)` |
| slot b seed 12 | 过 | 0.14 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.12 | 0.17 | 0.33 | 0.28 | 0.20 | 0.02 | `sub(cross_ema(day_centroid(Amt), 10), cross_ema(day_centroid(Amt), 60))` |
| R 1 variant 1 | 过 | 0.06 | `pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret),` | 0.09 | 0.32 | 0.04 | 0.07 | 0.27 | 0.01 | `cross_mean(day_ar1_coefficient(Ret), 120)` |
| R 1 variant 2 | 过 | 0.04 | `pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret),` | 0.10 | 0.32 | 0.04 | 0.06 | 0.27 | 0.00 | `cross_ema(day_ar1_coefficient(Ret), 60)` |
| R 1 variant 3 | 过 | 0.06 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.09 | 0.26 | 0.09 | 0.07 | 0.21 | 0.02 | `cross_mean(day_ar1_coefficient(Ret), 241)` |
| R 1 variant 4 | 过 | 0.10 | `pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret),` | 0.10 | 0.29 | 0.02 | 0.07 | 0.25 | 0.03 | `cross_tail_mean_q75(day_ar1_coefficient(Ret), 120)` |
| R 1 variant 5 | 过 | 0.04 | `pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret),` | 0.09 | 0.34 | 0.06 | 0.07 | 0.28 | 0.05 | `cross_tail_mean_q25(day_ar1_coefficient(Ret), 120)` |
| R 1 variant 6 | 过 | 0.04 | `pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret),` | 0.09 | 0.31 | 0.04 | 0.07 | 0.26 | 0.01 | `cross_quantile(day_ar1_coefficient(Ret), 0.5, 120)` |
