# 相关度表:种子 2071,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 6 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.12 | `pow_2(pow_2(day_q_stat_std(nt_cs_rank(High))))` | 0.17 | 0.04 | 0.03 | 0.06 | 0.04 | 0.02 | `abs_(day_corr(Volume, Ret))` |
| slot a seed 1 | 过 | 0.18 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.16 | 0.03 | 0.00 | 0.03 | 0.06 | 0.11 | `cross_max(abs_(day_corr(Volume, Ret)), 120)` |
| slot a seed 2 | 过 | 0.16 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.21 | 0.10 | 0.01 | 0.06 | 0.13 | 0.09 | `cross_max(abs_(day_corr(Volume, Ret)), 60)` |
| slot a seed 3 | 过 | 0.16 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.33 | 0.20 | 0.10 | 0.04 | 0.19 | 0.08 | `cross_quantile_q75(abs_(day_corr(Volume, Ret)), 60)` |
| slot a seed 4 | 过 | 0.20 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.17 | 0.00 | 0.01 | 0.03 | 0.03 | 0.11 | `ts_max(abs_(day_corr(Volume, Ret)), 160)` |
| slot a seed 5 | 过 | 0.17 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.17 | 0.09 | 0.01 | 0.03 | 0.06 | 0.09 | `sub(cross_max(abs_(day_corr(Volume, Ret)), 241), ts_mean(abs_(day_corr(Volume, Ret)), 20))` |
| slot a seed 6 | 过 | 0.07 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.15 | 0.11 | 0.15 | 0.03 | 0.06 | 0.02 | `div(cross_max(abs_(day_corr(Volume, Ret)), 120), ts_mean(abs_(day_corr(Volume, Ret)), 120))` |
| slot a seed 7 | 废品 | 0.11 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.10 | 0.07 | 0.07 | 0.08 | 0.09 | 0.01 | `cross_argmax(abs_(day_corr(Volume, Ret)), 120)` |
| slot a seed 8 | 废品 | 0.09 | `pow_2(pow_2(day_q_stat_std(nt_cs_rank(High))))` | 0.06 | 0.01 | 0.01 | 0.06 | 0.02 | 0.00 | `ts_rank(abs_(day_corr(Volume, Ret)), 120)` |
| slot a seed 9 | 过 | 0.23 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.29 | 0.15 | 0.13 | 0.02 | 0.15 | 0.11 | `cross_tail_mean_q75(abs_(day_corr(Volume, Ret)), 120)` |
| slot a seed 10 | 过 | 0.07 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.16 | 0.12 | 0.16 | 0.03 | 0.07 | 0.01 | `ts_skew(abs_(day_corr(Volume, Ret)), 120)` |
| slot a seed 11 | 过 | 0.20 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.36 | 0.19 | 0.13 | 0.05 | 0.19 | 0.11 | `cross_ema(abs_(day_corr(Volume, Ret)), 40)` |
| slot a seed 12 | 过 | 0.23 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.25 | 0.11 | 0.08 | 0.03 | 0.13 | 0.12 | `ts_std(abs_(day_corr(Volume, Ret)), 120)` |
| slot a seed 13 | 过 | 0.22 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.19 | 0.03 | 0.07 | 0.03 | 0.05 | 0.10 | `cross_max(ts_mean(abs_(day_corr(Volume, Ret)), 5), 241)` |
| slot a seed 14 | 过 | 0.20 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.27 | 0.11 | 0.23 | 0.00 | 0.09 | 0.12 | `cross_med(abs_(day_corr(Volume, Ret)), 241)` |
| slot b seed 1 | 废品 | 0.26 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.13 | 0.12 | 0.23 | 0.28 | 0.16 | 0.07 | `cross_argmax(day_sum(Amt), 60)` |
| slot b seed 2 | 废品 | 0.24 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.13 | 0.13 | 0.21 | 0.14 | 0.15 | 0.08 | `cross_argmax(div(sub(day_max(High), day_min(Low)), day_open(Open)), 120)` |
| slot b seed 3 | 废品 | 0.23 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.10 | 0.12 | 0.21 | 0.14 | 0.15 | 0.09 | `cross_argmax(day_std(Ret), 120)` |
| slot b seed 4 | 废品 | 0.02 | `day_median(pow_2(nt_cs_rank(Ret)))` | 0.03 | 0.02 | 0.00 | 0.02 | 0.03 | 0.02 | `sub(cross_argmax(day_sum(Amt), 120), cross_argmax(abs_(sub(day_close(Close), day_open(Open))), 120))` |
| slot b seed 5 | 废品 | 0.28 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.06 | 0.18 | 0.25 | 0.06 | 0.19 | 0.03 | `cross_argmin(day_sum(Amt), 120)` |
| slot b seed 6 | 过 | 0.09 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.08 | 0.14 | 0.07 | 0.12 | 0.10 | 0.26 | `div(cross_max(day_sum(Amt), 60), cross_mean(day_sum(Amt), 60))` |
| slot b seed 7 | 过 | 0.07 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.06 | 0.21 | 0.08 | 0.09 | 0.17 | 0.34 | `div(cross_max(day_sum(Amt), 120), cross_med(day_sum(Amt), 120))` |
| slot b seed 8 | 过 | 0.01 | `day_mean(pow_2(nt_cs_rank(Ret)))` | 0.01 | 0.01 | 0.01 | 0.02 | 0.01 | 0.01 | `cross_autocorr(day_sum(Ret), 20, 1)` |
| slot b seed 9 | 过 | 0.19 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.06 | 0.11 | 0.15 | 0.21 | 0.11 | 0.02 | `cross_corr(day_sum(Amt), day_sum(Ret), 40)` |
| slot b seed 10 | 废品 | 0.12 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.08 | 0.08 | 0.10 | 0.01 | 0.06 | 0.04 | `sub(cross_argmax(day_max(High), 120), cross_argmax(day_sum(Amt), 120))` |
| slot b seed 11 | 废品 | 0.10 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.09 | 0.06 | 0.07 | 0.08 | 0.07 | 0.03 | `cross_argmax(day_skew(Ret), 120)` |
| slot b seed 12 | 过 | 0.06 | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(O` | 0.10 | 0.14 | 0.06 | 0.06 | 0.11 | 0.21 | `div(cross_max(div(sub(day_max(High), day_min(Low)), day_open(Open)), 60), cross_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 60))` |
