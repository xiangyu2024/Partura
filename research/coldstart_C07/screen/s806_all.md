# 验证材料:种子 806(train 与 valid)

候选因子库 8 个 head(主搜索第 1–4 批,然后补充搜索第 1–3 轮)。秩相关 |ρ| 用 train,每 5 天一天,不分方向。

| # | 来源 | 方向 | 半衰期 | train 夏普 | valid 夏普 | 最像的其他 head(\|ρ\|, #) | 流动性 | 波动 | 反转 | 已知族 | 市值 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | c07s806M2 | -1 | 5 | +1.49 | +1.35 | 0.10 (#3), 0.07 (#7), 0.07 (#6) | 0.47 | 0.39 | 0.19 | 0.49 | 0.15 | `ts_quantile_q50(day_centroid(Amt), 20)` |
| 2 | c07s806Ar2a | -1 | 20 | +1.04 | +1.40 | 0.27 (#5), 0.21 (#4), 0.15 (#6) | 0.06 | 0.07 | 0.01 | 0.07 | 0.00 | `cross_corr(cross_reg_fvalue(day_mean(Open), day_centroid(High), 5), pow_2_5(pow_1_5(day_quantile_q75(Volume))), 30)` |
| 3 | c07s806Ar2a | +1 | 5 | +0.99 | +1.64 | 0.19 (#7), 0.10 (#1), 0.06 (#2) | 0.12 | 0.14 | 0.02 | 0.15 | 0.04 | `cross_corr(ts_regres(cross_reg_fvalue(day_mean(Open), day_mean(Open), 5), day_es_ratio_lo(Vwap), 20), pow_2_5(pow_1_5(day_quantile_q75(Volume))), 30)` |
| 4 | c07s806Ar2a | -1 | 5 | +0.81 | +0.74 | 0.21 (#2), 0.14 (#5), 0.04 (#6) | 0.05 | 0.03 | 0.02 | 0.05 | 0.01 | `cross_corr(ts_regres(cross_reg_fvalue(cs_last_low10(day_pos_ratio(High), day_at_min_ratio(Vwap)), day_centroid(High), 5), cross_reg_fvalue(cross_corr(cross_reg_fvalue(day_mean(Open), day_centroid(High), 5), pow_2_5(pow_1_5(day_quantile_q75(Volume))), 30), day_centroid(High), 5), 20), pow_2_5(pow_1_5(day_quantile_q75(Volume))), 30)` |
| 5 | c07s806Ar2a | -1 | 20 | +0.71 | +0.75 | 0.27 (#2), 0.14 (#4), 0.04 (#6) | 0.03 | 0.03 | 0.01 | 0.03 | 0.01 | `cross_corr(ts_regres(cross_reg_fvalue(cs_last_low10(day_pos_ratio(High), day_at_min_ratio(Vwap)), cross_reg_fvalue(day_mean(Open), day_centroid(High), 5), 5), cross_reg_fvalue(day_mean(Open), cross_reg_fvalue(day_mean(Open), day_centroid(High), 5), 5), 20), pow_2_5(pow_1_5(day_quantile_q75(Volume))), 30)` |
| 6 | c07s806Ar2a | +1 | 20 | +0.64 | +1.40 | 0.15 (#2), 0.07 (#1), 0.04 (#5) | 0.10 | 0.06 | 0.04 | 0.10 | 0.06 | `cross_corr(ts_regres(cross_reg_fvalue(day_es_ratio_lo(Vwap), day_argmax(High), 5), cross_reg_fvalue(day_mean(Open), day_argmax(High), 5), 20), pow_2_5(pow_1_5(day_quantile_q75(Volume))), 30)` |
| 7 | c07s806Ar2a | -1 | 20 | +0.55 | +0.58 | 0.19 (#3), 0.07 (#1), 0.05 (#2) | 0.08 | 0.01 | 0.11 | 0.10 | 0.11 | `cross_corr(day_centroid(High), pow_2_5(pow_1_5(day_quantile_q75(Volume))), 30)` |
| 8 | c07s806Ar3b | +1 | 5 | +0.59 | +2.76 | 0.06 (#1), 0.02 (#3), 0.01 (#7) | 0.17 | 0.00 | 0.04 | 0.15 | 0.11 | `cs_first_high20(sqrt(add(day_quantile_q25(Open), add(day_quantile_q25(Open), sqrt(pow_3(day_close(Open)))))), div(cs_first_high20(pow_3(day_close(Open)), div(add(day_quantile_q25(Open), sqrt(add(day_quantile_q25(Open), add(day_quantile_q25(Open), sqrt(pow_3(day_close(Open))))))), -5)), -5))` |
