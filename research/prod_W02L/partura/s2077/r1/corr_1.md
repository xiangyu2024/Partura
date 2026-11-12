# 相关度表:种子 2077,P 组,第 1 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 1.00 | `day_median(div(abs_(Ret), Amt))` | 1.00 | 0.45 | 0.08 | 0.03 | 0.47 | 0.54 | `day_median(div(abs_(Ret), Amt))` |
| slot a seed 1 | 过 | 0.33 | `day_median(div(abs_(Ret), Amt))` | 0.23 | 0.09 | 0.00 | 0.14 | 0.08 | 0.03 | `sub(day_median(div(abs_(Ret), Amt)), cross_mean(day_median(div(abs_(Ret), Amt)), 20))` |
| slot a seed 2 | 过 | 0.58 | `day_median(div(abs_(Ret), Amt))` | 0.50 | 0.05 | 0.13 | 0.14 | 0.02 | 0.05 | `div(day_median(div(abs_(Ret), Amt)), cross_mean(day_median(div(abs_(Ret), Amt)), 60))` |
| slot a seed 3 | 过 | 0.37 | `day_median(div(abs_(Ret), Amt))` | 0.21 | 0.04 | 0.07 | 0.21 | 0.03 | 0.01 | `cross_zscore(day_median(div(abs_(Ret), Amt)), 40)` |
| slot a seed 4 | 过 | 0.28 | `day_median(div(abs_(Ret), Amt))` | 0.17 | 0.01 | 0.00 | 0.10 | 0.00 | 0.03 | `cross_delta(day_median(div(abs_(Ret), Amt)), 10)` |
| slot a seed 5 | 过 | 0.18 | `day_median(div(abs_(Ret), Amt))` | 0.21 | 0.07 | 0.16 | 0.37 | 0.06 | 0.17 | `cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Ret), 20)` |
| slot a seed 6 | 过 | 0.66 | `day_median(div(abs_(Ret), Amt))` | 0.54 | 0.78 | 0.13 | 0.04 | 0.77 | 0.68 | `cross_stddev(day_median(div(abs_(Ret), Amt)), 20)` |
| slot a seed 7 | 过 | 0.35 | `day_median(div(abs_(Ret), Amt))` | 0.31 | 0.01 | 0.17 | 0.16 | 0.04 | 0.06 | `div(cross_mean(day_median(div(abs_(Ret), Amt)), 5), cross_mean(day_median(div(abs_(Ret), Amt)), 60))` |
| slot a seed 8 | 过 | 0.79 | `day_median(div(abs_(Ret), Amt))` | 0.82 | 0.68 | 0.09 | 0.04 | 0.68 | 0.69 | `cross_tail_mean_q75(day_median(div(abs_(Ret), Amt)), 40)` |
| slot a seed 9 | 过 | 0.63 | `day_median(div(abs_(Ret), Amt))` | 0.89 | 0.14 | 0.16 | 0.03 | 0.17 | 0.18 | `cs_bucket_demean(day_median(div(abs_(Ret), Amt)), LogFloatCap)` |
| slot a seed 10 | 过 | 0.34 | `day_median(div(abs_(Ret), Amt))` | 0.20 | 0.07 | 0.00 | 0.15 | 0.06 | 0.01 | `cs_bucket_demean(cross_zscore(day_median(div(abs_(Ret), Amt)), 20), cross_mean(day_sum(Amt), 20))` |
| slot a seed 11 | 过 | 0.60 | `day_median(div(abs_(Ret), Amt))` | 0.42 | 0.79 | 0.12 | 0.04 | 0.77 | 0.66 | `sub(cross_max(day_median(div(abs_(Ret), Amt)), 20), cross_mean(day_median(div(abs_(Ret), Amt)), 20))` |
| slot a seed 12 | 过 | 0.29 | `day_median(div(abs_(Ret), Amt))` | 0.61 | 0.35 | 0.11 | 0.01 | 0.30 | 0.13 | `cross_corr(day_median(div(abs_(Ret), Amt)), day_sum(Amt), 40)` |
| slot b seed 1 | 过 | 0.31 | `day_open(in_delta(Volume, 60))` | 0.30 | 0.12 | 0.17 | 0.14 | 0.14 | 0.04 | `div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt))` |
| slot b seed 2 | 过 | 0.22 | `day_open(in_delta(Volume, 60))` | 0.05 | 0.03 | 0.04 | 0.06 | 0.03 | 0.02 | `sub(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), cross_mean(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), 20))` |
| slot b seed 3 | 过 | 0.04 | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), n` | 0.09 | 0.05 | 0.01 | 0.08 | 0.05 | 0.01 | `cross_corr(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), day_sum(Ret), 20)` |
| slot b seed 4 | 过 | 0.04 | `day_open(in_delta(Volume, 60))` | 0.02 | 0.01 | 0.00 | 0.10 | 0.01 | 0.03 | `day_corr(in_slice(Ret, 1, 60), in_slice(Volume, 1, 60))` |
| slot b seed 5 | 过 | 0.07 | `day_open(in_delta(Volume, 60))` | 0.03 | 0.04 | 0.11 | 0.41 | 0.05 | 0.06 | `cross_mean(day_corr(in_slice(Ret, 1, 60), in_slice(Amt, 1, 60)), 20)` |
| slot b seed 6 | 过 | 0.11 | `day_open(in_delta(Volume, 60))` | 0.06 | 0.18 | 0.21 | 0.49 | 0.20 | 0.08 | `cross_mean(sub(day_sum(in_slice(Ret, 1, 30)), day_sum(in_slice(Ret, 211, 240))), 20)` |
| slot b seed 7 | 过 | 0.55 | `day_median(div(abs_(Ret), Amt))` | 0.44 | 0.87 | 0.14 | 0.16 | 0.86 | 0.67 | `div(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(in_slice(Amt, 1, 30)))` |
| slot b seed 8 | 过 | 0.53 | `day_median(div(abs_(Ret), Amt))` | 0.50 | 0.95 | 0.12 | 0.02 | 0.93 | 0.71 | `cross_mean(div(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(in_slice(Amt, 1, 30))), 20)` |
| slot b seed 9 | 过 | 0.25 | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), n` | 0.50 | 0.27 | 0.09 | 0.09 | 0.25 | 0.03 | `div(day_std(in_slice(Ret, 1, 30)), day_std(in_slice(Ret, 211, 240)))` |
| slot b seed 10 | 废品 | 0.35 | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), n` | 0.54 | 0.39 | 0.15 | 0.00 | 0.36 | 0.01 | `cross_mean(div(day_std(in_slice(Ret, 1, 30)), day_std(in_slice(Ret, 211, 240))), 20)` |
| slot b seed 11 | 过 | 0.45 | `day_median(div(abs_(Ret), Amt))` | 0.30 | 0.75 | 0.12 | 0.11 | 0.69 | 0.68 | `cross_corr(div(day_sum(in_slice(Amt, 1, 30)), day_sum(Amt)), div(day_sum(abs_(in_slice(Ret, 1, 30))), day_sum(in_slice(Amt, 1, 30))), 40)` |
| slot b seed 12 | 过 | 0.01 | `day_median(div(abs_(Ret), Amt))` | 0.01 | 0.00 | 0.01 | 0.00 | 0.00 | 0.01 | `cross_mean(day_corr(in_slice(Ret, 1, 30), in_slice(Ret, 211, 240)), 20)` |
