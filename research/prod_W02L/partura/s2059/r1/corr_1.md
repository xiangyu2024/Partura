# 相关度表:种子 2059,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a seed 1 | 过 | 0.60 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.48 | 0.53 | 0.57 | 0.02 | 0.52 | 0.11 | `cross_mean(cs_regres(day_min(Low), day_max(High)), 60)` |
| slot a seed 2 | 过 | 0.59 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.43 | 0.48 | 0.46 | 0.06 | 0.46 | 0.11 | `cross_mean(cs_regres(day_min(Low), day_max(High)), 120)` |
| slot a seed 3 | 过 | 0.08 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.30 | 0.07 | 0.18 | 0.33 | 0.09 | 0.05 | `cross_zscore(cs_regres(day_min(Low), day_max(High)), 120)` |
| slot a seed 4 | 过 | 0.58 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.48 | 0.31 | 0.63 | 0.03 | 0.32 | 0.21 | `cross_mean(cs_regres(log(day_min(Low)), log(day_max(High))), 90)` |
| slot a seed 5 | 过 | 0.17 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.11 | 0.26 | 0.31 | 0.08 | 0.28 | 0.06 | `cross_regbeta(day_min(Low), day_max(High), 60)` |
| slot a seed 6 | 过 | 0.08 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.13 | 0.13 | 0.13 | 0.04 | 0.14 | 0.10 | `cross_regbeta(log(day_min(Low)), log(day_max(High)), 120)` |
| slot a seed 7 | 过 | 0.19 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.39 | 0.15 | 0.06 | 0.17 | 0.14 | 0.07 | `cross_regres(day_min(Low), day_max(High), 60)` |
| slot a seed 8 | 过 | 0.04 | `cross_min(day_max(nt_cs_regres(Ret, Low)), 60)` | 0.08 | 0.01 | 0.09 | 0.20 | 0.02 | 0.03 | `cross_mean(log(div(sub(day_max(High), day_mean(Vwap)), sub(day_mean(Vwap), day_min(Low)))), 60)` |
| slot a seed 9 | 过 | 0.03 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.06 | 0.03 | 0.08 | 0.13 | 0.03 | 0.04 | `cross_mean(log(div(sub(day_max(High), day_mean(Vwap)), sub(day_mean(Vwap), day_min(Low)))), 120)` |
| slot a seed 10 | 过 | 0.03 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.04 | 0.02 | 0.04 | 0.06 | 0.02 | 0.02 | `cross_zscore(log(div(sub(day_max(High), day_mean(Vwap)), sub(day_mean(Vwap), day_min(Low)))), 90)` |
| slot a seed 11 | 过 | 0.55 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.47 | 0.49 | 0.56 | 0.03 | 0.49 | 0.04 | `cs_bucket_zscore(cross_mean(cs_regres(day_min(Low), day_max(High)), 60), LogFloatCap)` |
| slot a seed 12 | 过 | 0.06 | `cross_min(day_max(nt_cs_regres(Ret, Low)), 60)` | 0.09 | 0.03 | 0.06 | 0.19 | 0.02 | 0.00 | `cs_bucket_zscore(cross_mean(log(div(sub(day_max(High), day_mean(Vwap)), sub(day_mean(Vwap), day_min(Low)))), 60), cross_mean(day_std(Amt), 30))` |
| slot b seed 1 | 过 | 0.13 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.07 | 0.02 | 0.02 | 0.06 | 0.00 | 0.11 | `cross_mean(sub(day_es_ratio_lo(Ret), day_es_ratio_hi(Ret)), 20)` |
| slot b seed 2 | 过 | 0.19 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.11 | 0.03 | 0.03 | 0.03 | 0.01 | 0.17 | `cross_mean(sub(day_es_ratio_lo(Ret), day_es_ratio_hi(Ret)), 60)` |
| slot b seed 3 | 过 | 0.01 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.01 | 0.00 | 0.01 | 0.01 | 0.00 | 0.01 | `cross_zscore(sub(day_es_ratio_lo(Ret), day_es_ratio_hi(Ret)), 60)` |
| slot b seed 4 | 过 | 0.08 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.07 | 0.17 | 0.16 | 0.14 | 0.21 | 0.19 | `cross_mean(day_skew(Ret), 40)` |
| slot b seed 5 | 过 | 0.29 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.09 | 0.21 | 0.14 | 0.01 | 0.19 | 0.32 | `cross_mean(day_es_ratio_lo(Ret), 40)` |
| slot b seed 6 | 过 | 0.33 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.13 | 0.18 | 0.12 | 0.04 | 0.14 | 0.34 | `cross_mean(day_es_ratio_hi(Ret), 40)` |
| slot b seed 7 | 过 | 0.03 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.01 | 0.02 | 0.04 | 0.01 | 0.03 | 0.02 | `sub(cross_semistd_neg(day_sum(Ret), 40), cross_semistd_pos(day_sum(Ret), 40))` |
| slot b seed 8 | 过 | 0.03 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.02 | 0.02 | 0.04 | 0.00 | 0.03 | 0.02 | `log(div(cross_semistd_neg(day_sum(Ret), 60), cross_semistd_pos(day_sum(Ret), 60)))` |
| slot b seed 9 | 过 | 0.03 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.02 | 0.02 | 0.04 | 0.00 | 0.03 | 0.02 | `div(sub(cross_semistd_neg(day_sum(Ret), 60), cross_semistd_pos(day_sum(Ret), 60)), add(cross_semistd_neg(day_sum(Ret), 60), cross_semistd_pos(day_sum(Ret), 60)))` |
| slot b seed 10 | 过 | 0.45 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.18 | 0.76 | 0.01 | 0.08 | 0.68 | 0.57 | `cross_mean(sub(day_es_ratio_lo(Amt), day_es_ratio_hi(Amt)), 40)` |
| slot b seed 11 | 过 | 0.10 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.09 | 0.08 | 0.04 | 0.04 | 0.10 | 0.00 | `cs_bucket_zscore(cross_mean(sub(day_es_ratio_lo(Ret), day_es_ratio_hi(Ret)), 40), LogFloatCap)` |
| slot b seed 12 | 过 | 0.15 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.07 | 0.04 | 0.08 | 0.12 | 0.01 | 0.33 | `cs_bucket_zscore(cross_mean(day_skew(Ret), 40), cross_mean(day_std(Amt), 30))` |
