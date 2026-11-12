# 相关度表:种子 2077,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.12 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.15 | 0.00 | 0.01 | 0.18 | 0.00 | 0.04 | `day_sum(Ret)` |
| slot a seed 1 | 过 | 0.10 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.06 | 0.11 | 0.17 | 0.30 | 0.11 | 0.02 | `cross_corr(day_sum(Ret), day_sum(Volume), 30)` |
| slot a seed 2 | 过 | 0.13 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.04 | 0.07 | 0.16 | 0.40 | 0.08 | 0.02 | `cross_corr(day_sum(Ret), day_std(Amt), 20)` |
| slot a seed 3 | 废品 | nan | `day_median(div(abs_(Ret), Amt))` | 0.00 | nan | nan | nan | nan | nan | `cross_corr(day_sum(Ret), day_zero_ratio(Low), 20)` |
| slot a seed 4 | 过 | 0.15 | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), cre` | 0.15 | 0.09 | 0.02 | 0.05 | 0.10 | 0.01 | `cross_corr(day_sum(Ret), day_corr(Ret, Volume), 20)` |
| slot a seed 5 | 过 | 0.22 | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), cre` | 0.14 | 0.19 | 0.15 | 0.01 | 0.23 | 0.06 | `cross_corr(day_sum(Ret), day_gini(sqrt(Volume)), 30)` |
| slot a seed 6 | 过 | 0.14 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.07 | 0.13 | 0.17 | 0.33 | 0.14 | 0.01 | `cross_corr(day_sum(Ret), day_std(Ret), 20)` |
| slot a seed 7 | 过 | 0.05 | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), n` | 0.05 | 0.00 | 0.07 | 0.03 | 0.01 | 0.07 | `cross_corr(day_sum(Ret), day_sum(in_slice(Ret, 1, 30)), 20)` |
| slot a seed 8 | 过 | 0.01 | `day_open(in_delta(Volume, 60))` | 0.03 | 0.01 | 0.01 | 0.02 | 0.01 | 0.01 | `cross_corr(day_sum(Ret), cross_delay(day_sum(Ret), 1), 20)` |
| slot a seed 9 | 过 | 0.10 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.05 | 0.07 | 0.14 | 0.43 | 0.06 | 0.03 | `cross_reg_tvalue(day_sum(Ret), day_sum(Amt), 20)` |
| slot a seed 10 | 过 | 0.09 | `day_quantile_q75(div(nt_ts_delay(in_r2(Ret, High, 3), 10), n` | 0.33 | 0.17 | 0.08 | 0.25 | 0.17 | 0.05 | `cross_regres(day_sum(Ret), day_sum(Volume), 20)` |
| slot a seed 11 | 过 | 0.18 | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 50), cre` | 0.15 | 0.09 | 0.14 | 0.01 | 0.12 | 0.04 | `cross_cov(day_sum(Ret), day_kurt(Amt), 40)` |
| slot a seed 12 | 过 | 0.05 | `day_median(div(abs_(Ret), Amt))` | 0.08 | 0.04 | 0.05 | 0.01 | 0.03 | 0.08 | `cross_corr(abs_(day_sum(Ret)), day_sum(Amt), 20)` |
| slot b seed 1 | 算不出:KeyError: 'x' | | | | | | | | | `day_corr(in_slice(Ret, 2, 241), in_slice(Volume, 1, 240))` |
| slot b seed 2 | 算不出:KeyError: 'x' | | | | | | | | | `cross_mean(day_corr(in_slice(Ret, 2, 241), in_slice(Amt, 1, 240)), 20)` |
| slot b seed 3 | 算不出:KeyError: 'x' | | | | | | | | | `cross_mean(day_corr(in_slice(Ret, 2, 241), in_slice(Ret, 1, 240)), 20)` |
| slot b seed 4 | 过 | 0.24 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.14 | 0.11 | 0.41 | 0.55 | 0.16 | 0.09 | `cross_mean(sub(div(day_sum(mul(Ret, Amt)), day_sum(Amt)), day_mean(Ret)), 20)` |
| slot b seed 5 | 过 | 0.17 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.07 | 0.03 | 0.04 | 0.17 | 0.03 | 0.02 | `sub(div(day_sum(mul(Ret, Amt)), day_sum(Amt)), day_mean(Ret))` |
| slot b seed 6 | 废品 | 0.21 | `day_sum(div(add(select_where(is_lt(in_slice(Ret, 1, 20), cre` | 0.12 | 0.45 | 0.20 | 0.16 | 0.44 | 0.12 | `cross_mean(sub(day_argmax(Amt), day_argmin(Low)), 20)` |
| slot b seed 7 | 废品 | 0.22 | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), cre` | 0.22 | 0.14 | 0.08 | 0.16 | 0.14 | 0.06 | `sub(day_argmax(Amt), day_argmax(Vwap))` |
| slot b seed 8 | 算不出:KeyError: 'x' | | | | | | | | | `cross_mean(day_corr(in_slice(Volume, 1, 120), in_slice(Volume, 122, 241)), 20)` |
| slot b seed 9 | 算不出:KeyError: 'x' | | | | | | | | | `day_cov(in_slice(Ret, 1, 120), in_slice(Ret, 122, 241))` |
| slot b seed 10 | 算不出:KeyError: 'x' | | | | | | | | | `cross_mean(day_cov(in_slice(Ret, 1, 120), in_slice(Ret, 122, 241)), 30)` |
