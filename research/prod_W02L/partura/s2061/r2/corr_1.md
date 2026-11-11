# 相关度表:种子 2061,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 5 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.24 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.14 | 0.14 | 0.08 | 0.03 | 0.15 | 0.06 | `cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)` |
| slot a seed 1 | 过 | 0.26 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.16 | 0.13 | 0.06 | 0.00 | 0.14 | 0.06 | `cross_ema(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), 20)` |
| slot a seed 2 | 过 | 0.03 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.02 | 0.01 | 0.04 | 0.05 | 0.02 | 0.06 | `cross_zscore(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), 120)` |
| slot a seed 3 | 过 | 0.20 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.13 | 0.01 | 0.02 | 0.01 | 0.01 | 0.11 | `sub(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), cross_reg_fvalue(pow_3(LogFloatCap), day_close(Amt), 241))` |
| slot a seed 4 | 过 | 0.24 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.14 | 0.14 | 0.08 | 0.03 | 0.15 | 0.06 | `cs_winsor(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` |
| slot a seed 5 | 过 | 0.24 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.14 | 0.14 | 0.08 | 0.03 | 0.15 | 0.06 | `cs_robust_z(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` |
| slot a seed 6 | 过 | 0.20 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.12 | 0.13 | 0.09 | 0.02 | 0.14 | 0.05 | `cs_mask_top_replace_mean_neg(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` |
| slot a seed 7 | 过 | 0.23 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.14 | 0.18 | 0.08 | 0.03 | 0.19 | 0.01 | `cs_bucket_demean(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), day_mean(Low))` |
| slot a seed 8 | 过 | 0.04 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.05 | 0.05 | 0.02 | 0.09 | 0.05 | 0.06 | `cross_delta(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), 20)` |
| slot a seed 9 | 过 | 0.25 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.14 | 0.14 | 0.08 | 0.01 | 0.15 | 0.06 | `cross_mean(cs_robust_z(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)), 20)` |
| slot a seed 10 | 过 | 0.26 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.15 | 0.15 | 0.08 | 0.00 | 0.16 | 0.06 | `cross_tail_mean_q75(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), 60)` |
| slot a seed 11 | 过 | 0.23 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.13 | 0.20 | 0.08 | 0.03 | 0.21 | 0.01 | `cs_bucket_zscore(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), day_mean(Low))` |
| slot a seed 12 | 过 | 0.21 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.12 | 0.03 | 0.04 | 0.02 | 0.04 | 0.15 | `sub(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), cross_reg_fvalue(LogFloatCap, day_open(Amt), 241))` |
| slot b seed 1 | 过 | 0.28 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.15 | 0.22 | 0.26 | 0.06 | 0.29 | 0.07 | `cross_mean(div(day_open(Amt), day_sum(Amt)), 60)` |
| slot b seed 2 | 过 | 0.34 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.21 | 0.19 | 0.24 | 0.06 | 0.26 | 0.10 | `cross_ema(div(day_open(Amt), day_sum(Amt)), 40)` |
| slot b seed 3 | 过 | 0.04 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.06 | 0.00 | 0.07 | 0.16 | 0.02 | 0.01 | `cross_zscore(div(day_open(Amt), day_sum(Amt)), 120)` |
| slot b seed 4 | 过 | 0.19 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.18 | 0.22 | 0.19 | 0.13 | 0.23 | 0.09 | `cross_mean(sub(div(day_open(Amt), day_sum(Amt)), div(day_open(Volume), day_sum(Volume))), 60)` |
| slot b seed 5 | 过 | 0.02 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.02 | 0.07 | 0.02 | 0.07 | 0.07 | 0.03 | `cross_corr(div(day_open(Amt), day_sum(Amt)), day_sum(Ret), 60)` |
| slot b seed 6 | 过 | 0.14 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.10 | 0.08 | 0.23 | 0.03 | 0.12 | 0.16 | `cross_autocorr(div(day_open(Amt), day_sum(Amt)), 60, 1)` |
| slot b seed 7 | 过 | 0.25 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.12 | 0.38 | 0.28 | 0.06 | 0.43 | 0.07 | `cs_bucket_demean(cross_mean(div(day_open(Amt), day_sum(Amt)), 60), day_mean(Low))` |
| slot b seed 8 | 过 | 0.11 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.17 | 0.12 | 0.18 | 0.24 | 0.15 | 0.11 | `sub(cross_ema(div(day_open(Amt), day_sum(Amt)), 10), cross_ema(div(day_open(Amt), day_sum(Amt)), 60))` |
| slot b seed 9 | 过 | 0.29 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.15 | 0.22 | 0.26 | 0.06 | 0.29 | 0.07 | `cross_mean(div(day_open(Volume), day_sum(Volume)), 60)` |
| slot b seed 10 | 过 | 0.25 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.14 | 0.02 | 0.25 | 0.08 | 0.10 | 0.24 | `cross_tail_mean_q75(div(day_open(Amt), day_sum(Amt)), 60)` |
| slot b seed 11 | 废品 | nan | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.00 | nan | nan | nan | nan | nan | `cross_corr(div(day_open(Amt), day_sum(Amt)), day_open(Ret), 60)` |
| R 1 variant 1 | 过 | 0.80 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.77 | 0.11 | 0.05 | 0.01 | 0.13 | 0.15 | `cross_mean(day_pdf_quantile_single(Ret, Amt, 0.95, True), 240)` |
| R 1 variant 2 | 过 | 0.89 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.87 | 0.13 | 0.06 | 0.03 | 0.15 | 0.15 | `cross_ema(day_pdf_quantile_single(Ret, Volume, 0.95, True), 120)` |
| R 1 variant 3 | 过 | 0.88 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.85 | 0.13 | 0.06 | 0.03 | 0.15 | 0.15 | `cross_ema(day_pdf_quantile_single(Ret, Amt, 0.95, True), 120)` |
| R 1 variant 4 | 过 | 0.62 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.55 | 0.07 | 0.03 | 0.01 | 0.09 | 0.18 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.9, True), 240)` |
| R 1 variant 5 | 过 | 0.59 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.52 | 0.12 | 0.05 | 0.02 | 0.14 | 0.09 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.99, True), 240)` |
| R 1 variant 6 | 过 | 0.89 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.87 | 0.12 | 0.06 | 0.02 | 0.14 | 0.13 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 180)` |
| R 2 variant 1 | 过 | 0.31 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.24 | 0.70 | 0.15 | 0.08 | 0.67 | 0.22 | `cross_mean(day_ar1_coefficient(Volume), 120)` |
| R 2 variant 2 | 过 | 0.31 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.24 | 0.73 | 0.17 | 0.06 | 0.71 | 0.23 | `cross_ema(day_ar1_coefficient(Volume), 60)` |
| R 2 variant 3 | 过 | 0.31 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True),` | 0.24 | 0.70 | 0.15 | 0.08 | 0.67 | 0.22 | `cross_mean(day_ar1_coefficient(Amt), 120)` |
| R 2 variant 4 | 过 | 0.16 | `cross_argmax(day_ar1_coefficient(Volume), 241)` | 0.27 | 0.17 | 0.27 | 0.32 | 0.20 | 0.07 | `cross_zscore(day_ar1_coefficient(Volume), 241)` |
