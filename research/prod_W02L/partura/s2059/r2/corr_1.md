# 相关度表:种子 2059,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.20 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.34 | 0.07 | 0.35 | 0.21 | 0.11 | 0.00 | `day_es_ratio_lo(Open)` |
| slot a seed 1 | 过 | 0.42 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.25 | 0.37 | 0.59 | 0.21 | 0.40 | 0.05 | `cross_stddev(day_es_ratio_lo(Open), 30)` |
| slot a seed 2 | 过 | 0.44 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.30 | 0.36 | 0.56 | 0.08 | 0.39 | 0.08 | `cross_stddev(day_es_ratio_lo(Open), 60)` |
| slot a seed 3 | 过 | 0.32 | `cross_min(day_first(nt_cs_regres(Amt, Low)), 15)` | 0.41 | 0.00 | 0.35 | 0.08 | 0.06 | 0.02 | `cross_tail_mean_q75(day_es_ratio_lo(Open), 60)` |
| slot a seed 4 | 过 | 0.56 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.39 | 0.37 | 0.72 | 0.09 | 0.41 | 0.07 | `cross_tail_mean_q25(day_es_ratio_lo(Open), 60)` |
| slot a seed 5 | 过 | 0.30 | `cross_min(day_first(nt_cs_regres(Amt, Low)), 15)` | 0.42 | 0.08 | 0.20 | 0.11 | 0.02 | 0.02 | `cross_max(day_es_ratio_lo(Open), 20)` |
| slot a seed 6 | 过 | 0.16 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.10 | 0.19 | 0.21 | 0.13 | 0.19 | 0.07 | `cross_corr(day_es_ratio_lo(Open), day_sum(Ret), 40)` |
| slot a seed 7 | 过 | 0.09 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.07 | 0.13 | 0.03 | 0.07 | 0.12 | 0.08 | `cross_corr(day_es_ratio_lo(Open), day_sum(Amt), 40)` |
| slot a seed 8 | 过 | 0.62 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.37 | 0.31 | 0.85 | 0.07 | 0.37 | 0.07 | `cross_mean(sub(day_es_ratio_lo(Open), day_es_ratio_hi(Open)), 40)` |
| slot a seed 9 | 过 | 0.62 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.37 | 0.31 | 0.85 | 0.07 | 0.37 | 0.07 | `cross_mean(div(day_es_ratio_lo(Open), day_es_ratio_hi(Open)), 40)` |
| slot a seed 10 | 过 | 0.05 | `cross_min(day_max(nt_cs_regres(Ret, Low)), 60)` | 0.28 | 0.01 | 0.03 | 0.17 | 0.00 | 0.01 | `cross_zscore(day_es_ratio_lo(Open), 60)` |
| slot a seed 11 | 过 | 0.50 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.29 | 0.26 | 0.80 | 0.33 | 0.33 | 0.03 | `cross_decay_linear(day_es_ratio_lo(Open), 30)` |
| slot a seed 12 | 过 | 0.04 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.02 | 0.00 | 0.09 | 0.02 | 0.02 | 0.03 | `cross_regbeta(day_es_ratio_lo(Open), day_es_ratio_lo(Ret), 60)` |
| slot a seed 13 | 过 | 0.12 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.47 | 0.11 | 0.05 | 0.37 | 0.10 | 0.05 | `cross_regres(day_es_ratio_lo(Open), day_std(Ret), 40)` |
| slot a seed 14 | 过 | 0.13 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.13 | 0.07 | 0.27 | 0.38 | 0.10 | 0.19 | `cross_mean(mul(day_es_ratio_lo(Open), day_signed_ratio(Ret, Amt)), 40)` |
| slot b seed 1 | 过 | 0.26 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.08 | 0.24 | 0.41 | 0.64 | 0.26 | 0.05 | `cross_mean(day_topw_mean(Ret, Volume), 20)` |
| slot b seed 2 | 过 | 0.43 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.27 | 0.41 | 0.52 | 0.23 | 0.42 | 0.06 | `cross_mean(day_topw_mean(Ret, Volume), 60)` |
| slot b seed 3 | 过 | 0.40 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.20 | 0.37 | 0.51 | 0.35 | 0.39 | 0.05 | `cross_mean(day_topw_mean(Ret, Amt), 40)` |
| slot b seed 4 | 过 | 0.14 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.11 | 0.09 | 0.26 | 0.39 | 0.11 | 0.19 | `cross_mean(day_signed_ratio(Ret, Amt), 40)` |
| slot b seed 5 | 过 | 0.06 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.13 | 0.00 | 0.16 | 0.61 | 0.02 | 0.15 | `cross_mean(day_signed_ratio(Ret, Volume), 20)` |
| slot b seed 6 | 过 | 0.06 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.12 | 0.00 | 0.16 | 0.57 | 0.02 | 0.15 | `cross_decay_linear(day_signed_ratio(Ret, Amt), 30)` |
| slot b seed 7 | 过 | 0.33 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.13 | 0.19 | 0.49 | 0.30 | 0.24 | 0.12 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 40)` |
| slot b seed 8 | 过 | 0.03 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.11 | 0.02 | 0.00 | 0.09 | 0.01 | 0.00 | `cross_zscore(sub(day_topw_mean(Ret, Amt), day_wmean(Ret, Amt)), 60)` |
| slot b seed 9 | 过 | 0.40 | `cross_min(day_first(nt_cs_regres(Amt, Low)), 15)` | 0.23 | 0.50 | 0.47 | 0.06 | 0.53 | 0.04 | `cross_mean(day_centroid(Amt), 40)` |
| slot b seed 10 | 过 | 0.11 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.07 | 0.08 | 0.16 | 0.04 | 0.09 | 0.06 | `cross_regbeta(day_centroid(Amt), day_topw_mean(Ret, Volume), 60)` |
| slot b seed 11 | 过 | 0.11 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.10 | 0.10 | 0.12 | 0.02 | 0.12 | 0.11 | `cross_corr(day_signed_ratio(Ret, Amt), day_centroid(Amt), 40)` |
| slot b seed 12 | 过 | 0.40 | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15` | 0.19 | 0.34 | 0.50 | 0.34 | 0.35 | 0.01 | `cs_bucket_zscore(cross_mean(day_topw_mean(Ret, Volume), 40), LogFloatCap)` |
| slot b seed 13 | 过 | 0.42 | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` | 0.10 | 0.80 | 0.06 | 0.07 | 0.72 | 0.63 | `cross_mean(day_gini(Amt), 40)` |
