# 相关度表:种子 2030,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.11 | `abs_(ts_std(day_first(Amt), 50))` | 0.34 | 0.06 | 0.01 | 0.48 | 0.06 | 0.08 | `div(day_sum(Amt), cross_mean(day_sum(Amt), 30))` |
| slot a seed 1 | 过 | 0.20 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.16 | 0.02 | 0.07 | 0.10 | 0.01 | 0.05 | `cross_corr(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), cs_demean(day_mean(Ret)), 120)` |
| slot a seed 2 | 过 | 0.45 | `pow_2(cross_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(da` | 0.33 | 0.11 | 0.26 | 0.10 | 0.14 | 0.14 | `cross_corr(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), ts_delay(cs_demean(ts_delta(log(day_last(Close)), 1)), 1), 120)` |
| slot a seed 3 | 过 | 0.62 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.42 | 0.31 | 0.50 | 0.25 | 0.33 | 0.08 | `cross_ema(mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), cs_demean(day_mean(Ret))), 60)` |
| slot a seed 4 | 过 | 0.42 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.35 | 0.04 | 0.27 | 0.12 | 0.01 | 0.25 | `cross_stddev(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 120)` |
| slot a seed 5 | 过 | 0.37 | `pow_2(cross_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(da` | 0.27 | 0.06 | 0.17 | 0.02 | 0.07 | 0.18 | `cross_autocorr_s1(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 120)` |
| slot a seed 6 | 过 | 0.18 | `abs_(ts_std(day_first(Amt), 50))` | 0.18 | 0.09 | 0.12 | 0.06 | 0.10 | 0.01 | `cross_ema(cross_argmax(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 120), 20)` |
| slot a seed 7 | 过 | 0.38 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.36 | 0.00 | 0.23 | 0.18 | 0.05 | 0.16 | `sub(cross_max(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 60), cross_ema(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 60))` |
| slot a seed 8 | 过 | 0.45 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.33 | 0.09 | 0.36 | 0.16 | 0.14 | 0.15 | `cross_tail_mean_q75(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 120)` |
| slot a seed 9 | 过 | 0.42 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.29 | 0.14 | 0.43 | 0.23 | 0.19 | 0.16 | `cross_ema(is_gt(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 2), 60)` |
| slot a seed 10 | 过 | 0.20 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.23 | 0.22 | 0.02 | 0.05 | 0.19 | 0.21 | `ts_skew(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 120)` |
| slot a seed 11 | 过 | 0.39 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.16 | 0.29 | 0.40 | 0.17 | 0.30 | 0.02 | `div(cross_sum(mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), sign(cs_demean(day_mean(Ret)))), 120), add(cross_sum(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), 120), 0.0000001))` |
| slot a seed 12 | 过 | 0.14 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.19 | 0.03 | 0.06 | 0.04 | 0.04 | 0.03 | `cross_corr(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), abs_(cs_demean(ts_delta(log(day_last(Close)), 1))), 120)` |
| slot b seed 1 | 过 | 0.60 | `ts_mean(sub(day_ar1_coefficient(Amt), day_first(Volume)), 40` | 0.54 | 0.17 | 0.22 | 0.04 | 0.24 | 0.11 | `cross_ema(div(day_first(Amt), day_sum(Amt)), 60)` |
| slot b seed 2 | 过 | 0.28 | `ts_mean(sub(day_ar1_coefficient(Amt), day_first(Volume)), 40` | 0.55 | 0.16 | 0.20 | 0.05 | 0.09 | 0.36 | `cross_stddev(div(day_first(Amt), day_sum(Amt)), 100)` |
| slot b seed 3 | 过 | 0.32 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.44 | 0.16 | 0.26 | 0.13 | 0.10 | 0.30 | `cross_stddev(div(day_first(Amt), cross_mean(day_first(Amt), 30)), 100)` |
| slot b seed 4 | 过 | 0.22 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.41 | 0.30 | 0.09 | 0.06 | 0.25 | 0.39 | `div(cross_stddev(day_first(Amt), 100), cross_mean(day_first(Amt), 100))` |
| slot b seed 5 | 过 | 0.69 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.65 | 0.08 | 0.23 | 0.03 | 0.12 | 0.16 | `cross_autocorr_s1(div(day_first(Amt), day_sum(Amt)), 60)` |
| slot b seed 6 | 过 | 0.02 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.04 | 0.03 | 0.00 | 0.00 | 0.03 | 0.04 | `cross_corr(ts_delay(div(day_first(Amt), day_sum(Amt)), 1), cs_demean(day_mean(Ret)), 100)` |
| slot b seed 7 | 过 | 0.29 | `abs_(ts_std(day_first(Amt), 50))` | 0.22 | 0.16 | 0.21 | 0.17 | 0.19 | 0.09 | `sub(cross_ema(div(day_first(Amt), day_sum(Amt)), 20), cross_ema(div(day_first(Amt), day_sum(Amt)), 120))` |
| slot b seed 8 | 过 | 0.27 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.41 | 0.14 | 0.18 | 0.10 | 0.09 | 0.23 | `cross_max(div(day_first(Amt), cross_mean(day_first(Amt), 30)), 100)` |
| slot b seed 9 | 过 | 0.28 | `ts_mean(sub(day_ar1_coefficient(Amt), day_first(Volume)), 40` | 0.55 | 0.16 | 0.20 | 0.05 | 0.09 | 0.36 | `cross_stddev(div(day_first(Volume), day_sum(Volume)), 100)` |
| slot b seed 10 | 过 | 0.38 | `abs_(ts_std(day_first(Amt), 50))` | 0.58 | 0.03 | 0.17 | 0.02 | 0.04 | 0.24 | `div(cross_stddev(day_first(Amt), 100), cross_stddev(day_sum(Amt), 100))` |
| slot b seed 11 | 过 | 0.53 | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Vo` | 0.47 | 0.14 | 0.17 | 0.04 | 0.17 | 0.14 | `cross_corr(day_first(Amt), day_sum(Amt), 100)` |
| slot b seed 12 | 过 | 0.33 | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(` | 0.34 | 0.11 | 0.34 | 0.16 | 0.05 | 0.28 | `cross_tail_mean_q75(div(day_first(Amt), cross_mean(day_first(Amt), 30)), 120)` |
