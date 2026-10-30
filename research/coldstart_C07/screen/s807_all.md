# 验证材料:种子 807(train 与 valid)

候选因子库 6 个 head(主搜索第 1–4 批,然后补充搜索第 1–3 轮)。秩相关 |ρ| 用 train,每 5 天一天,不分方向。

| # | 来源 | 方向 | 半衰期 | train 夏普 | valid 夏普 | 最像的其他 head(\|ρ\|, #) | 流动性 | 波动 | 反转 | 已知族 | 市值 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | c07s807M1 | -1 | 20 | +1.11 | +0.91 | 0.08 (#5), 0.02 (#4), 0.02 (#2) | 0.17 | 0.09 | 0.01 | 0.17 | 0.12 | `cross_regbeta(day_quantile_q75(Volume), cs_rank(pow_05(ts_regbeta(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 20)), cs_mean(day_median(Close)), 5))), 241)` |
| 2 | c07s807M1 | +1 | 20 | +0.79 | +1.32 | 0.63 (#3), 0.07 (#6), 0.02 (#5) | 0.10 | 0.13 | 0.04 | 0.12 | 0.02 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(day_pos_ratio(Open)), ts_var(LogFloatCap, 30)), LimitWidth), 30)` |
| 3 | c07s807M1 | +1 | 5 | +0.84 | +0.52 | 0.63 (#2), 0.09 (#6), 0.01 (#5) | 0.10 | 0.16 | 0.10 | 0.12 | 0.01 | `cross_regbeta(day_quantile_q75(Volume), cs_bucket_demean(add(cs_median(ts_var(LogFloatCap, 50)), ts_var(LogFloatCap, 20)), LimitWidth), 30)` |
| 4 | c07s807Ar3a | -1 | 0 | +0.83 | +2.17 | 0.08 (#5), 0.06 (#6), 0.02 (#1) | 0.06 | 0.03 | 0.01 | 0.04 | 0.01 | `cs_last_low05(day_zero_ratio(Open), LogTotalCap)` |
| 5 | c07s807Ar3a | -1 | 20 | +0.83 | +2.58 | 0.30 (#6), 0.08 (#4), 0.08 (#1) | 0.39 | 0.02 | 0.07 | 0.37 | 0.55 | `abs_(mul(cs_mask_top_replace_mean(day_corr(Ret, Open)), cs_last_low05(LogTotalCap, LogTotalCap)))` |
| 6 | c07s807Ar3a | -1 | 5 | +0.98 | +0.52 | 0.30 (#5), 0.09 (#3), 0.07 (#2) | 0.42 | 0.18 | 0.16 | 0.38 | 0.01 | `mul(day_zero_ratio(Ret), cs_last_low05(day_zero_ratio(Ret), LogTotalCap))` |
