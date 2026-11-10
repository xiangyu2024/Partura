# 相关度表:种子 2048,P 组,第 2 轮(train 20210701 ~ 20230807 每 5 天一天;|ρ| 不分方向;不是评分)

快照里 3 个 head。「原始」= 两者日度秩的 |ρ|,与 GP 库禁令同一个量(≥ 0.7 会被拒绝);「残差」= 对 5 个控制取残差后的 |ρ|(head 按它的方向与半衰期);控制列 = 原始秩与该控制的 |ρ|(≥ 0.5 = 控制变量换个写法)。

| 位置 | 门槛 | 与 head 最大 \|ρ\|:原始 | 最像的 head | 残差 | liq | vol | rev | known | size | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| slot a core | 过 | 0.12 | `cross_mean(day_std(Volume), 20)` | 0.30 | 0.35 | 0.03 | 0.03 | 0.32 | 0.25 | `cs_first_low20(LogTotalCap, ListAge)` |
| slot a seed 1 | 过 | 0.12 | `cross_mean(day_std(Volume), 20)` | 0.30 | 0.35 | 0.03 | 0.03 | 0.32 | 0.25 | `cs_first_low20(LogTotalCap, ListAge)` |
| slot a seed 2 | 过 | 0.08 | `cross_mean(day_std(Volume), 20)` | 0.26 | 0.34 | 0.09 | 0.09 | 0.32 | 0.24 | `add(cs_first_low20(LogTotalCap, ListAge), div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot a seed 3 | 过 | 0.16 | `cross_mean(day_std(Volume), 20)` | 0.30 | 0.31 | 0.03 | 0.14 | 0.28 | 0.20 | `sub(cs_first_low20(LogTotalCap, ListAge), div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot a seed 4 | 过 | 0.14 | `cross_mean(day_std(Volume), 20)` | 0.24 | 0.25 | 0.04 | 0.15 | 0.22 | 0.15 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot a seed 5 | 过 | 0.03 | `day_std(Volume)` | 0.21 | 0.30 | 0.14 | 0.23 | 0.29 | 0.23 | `cs_first_high20(cs_first_low20(LogTotalCap, ListAge), div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot a seed 6 | 过 | 0.07 | `day_std(Volume)` | 0.17 | 0.19 | 0.14 | 0.28 | 0.16 | 0.19 | `cs_first_low20(div(day_close(Close), cross_max(day_close(Close), 241)), cs_first_low20(LogTotalCap, ListAge))` |
| slot a seed 7 | 过 | 0.19 | `cross_mean(day_std(Volume), 20)` | 0.33 | 0.29 | 0.02 | 0.08 | 0.26 | 0.20 | `cross_ema(cs_first_low20(LogTotalCap, ListAge), 60)` |
| slot a seed 8 | 过 | 0.20 | `cross_mean(day_std(Volume), 20)` | 0.26 | 0.14 | 0.10 | 0.18 | 0.11 | 0.15 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60))` |
| slot a seed 9 | 过 | 0.33 | `cross_mean(day_std(Volume), 20)` | 0.05 | 0.35 | 0.01 | 0.03 | 0.34 | 0.58 | `cs_first_low40(cs_first_low20(LogTotalCap, ListAge), LogTotalCap)` |
| slot a seed 10 | 过 | 0.12 | `cross_mean(day_std(Volume), 20)` | 0.30 | 0.35 | 0.02 | 0.03 | 0.32 | 0.25 | `add(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 120))` |
| slot a seed 11 | 过 | 0.08 | `cross_mean(day_std(Volume), 20)` | 0.21 | 0.49 | 0.31 | 0.12 | 0.48 | 0.20 | `cs_first_high20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60))` |
| slot a seed 12 | 过 | 0.03 | `day_std(Volume)` | 0.11 | 0.22 | 0.05 | 0.23 | 0.21 | 0.24 | `cs_last_low20(cs_first_low20(LogTotalCap, ListAge), div(day_close(Close), cross_max(day_close(Close), 120)))` |
| slot b seed 1 | 过 | 0.13 | `cross_mean(day_std(Volume), 20)` | 0.17 | 0.43 | 0.08 | 0.14 | 0.40 | 0.53 | `cs_first_low20(LogTotalCap, div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot b seed 2 | 过 | 0.40 | `cross_mean(day_std(Volume), 20)` | 0.44 | 0.21 | 0.16 | 0.16 | 0.21 | 0.45 | `cs_first_low20(LogFloatShares, div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot b seed 3 | 过 | 0.04 | `cross_mean(day_std(Volume), 20)` | 0.12 | 0.30 | 0.14 | 0.24 | 0.26 | 0.36 | `cs_first_low40(LogTotalCap, div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot b seed 4 | 过 | 0.33 | `day_std(Volume)` | 0.15 | 0.54 | 0.11 | 0.24 | 0.52 | 0.67 | `cs_first_high20(LogTotalCap, div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot b seed 5 | 过 | 0.17 | `cross_mean(day_std(Volume), 20)` | 0.17 | 0.51 | 0.03 | 0.20 | 0.47 | 0.55 | `cs_first_low20(LogTotalCap, div(day_close(Close), cross_max(day_close(Close), 120)))` |
| slot b seed 6 | 过 | 0.14 | `cross_mean(day_std(Volume), 20)` | 0.11 | 0.34 | 0.21 | 0.17 | 0.31 | 0.57 | `cs_first_low20(LogTotalCap, div(day_close(Close), cross_min(day_close(Close), 241)))` |
| slot b seed 7 | 过 | 0.09 | `cross_mean(day_std(Volume), 20)` | 0.04 | 0.25 | 0.25 | 0.05 | 0.26 | 0.02 | `cs_first_low20(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot b seed 8 | 过 | 0.25 | `cross_mean(day_std(Volume), 20)` | 0.10 | 0.28 | 0.30 | 0.21 | 0.30 | 0.10 | `cs_first_low20(sub(cross_mean(sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 120), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 120)), div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot b seed 9 | 过 | 0.14 | `day_std(Volume)` | 0.14 | 0.29 | 0.01 | 0.12 | 0.27 | 0.32 | `cs_first_low20(div(cross_delay(day_close(Close), 20), cross_max(day_close(Close), 241)), LogTotalCap)` |
| slot b seed 10 | 过 | 0.07 | `cross_mean(day_std(Volume), 20)` | 0.14 | 0.27 | 0.11 | 0.27 | 0.24 | 0.32 | `cs_first_low20(div(day_close(Close), cross_max(day_close(Close), 241)), LogTotalCap)` |
| slot b seed 11 | 过 | 0.36 | `cross_mean(day_std(Volume), 20)` | 0.19 | 0.63 | 0.20 | 0.14 | 0.62 | 0.66 | `cs_first_high20(LogTotalCap, div(cross_max(day_close(Close), 20), cross_max(day_close(Close), 241)))` |
| slot b seed 12 | 过 | 0.14 | `cross_mean(day_std(Volume), 20)` | 0.13 | 0.38 | 0.16 | 0.27 | 0.34 | 0.50 | `cs_last_high20(LogTotalCap, div(day_close(Close), cross_max(day_close(Close), 241)))` |
| slot b seed 13 | 过 | 0.12 | `day_std(Volume)` | 0.28 | 0.43 | 0.12 | 0.01 | 0.39 | 0.63 | `cs_first_low20(LogTotalCap, day_es_ratio_hi(inv(cross_max(Open, 241))))` |
