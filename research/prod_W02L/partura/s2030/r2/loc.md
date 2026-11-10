# 定位:种子 2030,P 组,第 2 轮(只含 train / valid)

快照:prods2030M1_I0_open_search, prods2030M2_I0_open_search, prods2030Pr1a_Ea, prods2030Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.22 | +0.57 | +0.22 | +1 | 5 | prods2030M2_I0_open_search | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Volume)), 60)` |
| -0.04 | +0.33 | -0.04 | +1 | 5 | prods2030M2_I0_open_search | `abs_(ts_std(day_first(Amt), 50))` |
| -0.17 | -0.13 | -0.17 | +1 | 5 | prods2030M1_I0_open_search | `pow_2(cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 90))` |
| -0.19 | -0.19 | +0.06 | +1 | 5 | prods2030M1_I0_open_search | `pow_2(ts_max(pow_2(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 30)), 10), 20)), 30))` |
| -0.20 | -0.20 | -0.15 | +1 | 0 | prods2030M1_I0_open_search | `pow_2(cross_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 90))` |
| -1.10 | -1.10 | -1.02 | +1 | 0 | prods2030M2_I0_open_search | `ts_mean(sub(day_ar1_coefficient(Amt), day_first(Volume)), 40)` |

## 共性:135 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.91 | 0.001 | 5 | -0.24 / -2.15 | `div(day_sum(Amt), cross_mean(day_sum(Amt), 30))` |
| +1.91 | 0.001 | 5 | -0.24 / -2.15 | `cross_mean(day_sum(Amt), 30)` |
| +1.75 | 0.002 | 5 | -0.40 / -2.14 | `cross_max(cs_demean(sub(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), 0.5)), 90)` |
| +1.60 | 0.001 | 6 | -0.54 / -2.15 | `cs_demean(sub(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), 0.5))` |
| +1.45 | 0.000 | 12 | -0.76 / -2.20 | `cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90)` |
| +1.15 | 0.000 | 22 | -1.11 / -2.26 | `cs_demean(ts_delta(log(day_last(Close)), 1))` |
| +1.07 | 0.057 | 4 | -1.04 / -2.11 | `day_first(Amt)` |
| +1.04 | 0.000 | 24 | -1.22 / -2.26 | `ts_delta(log(day_last(Close)), 1)` |
| +0.99 | 0.000 | 34 | -1.33 / -2.33 | `day_sum(Amt)` |
| +0.99 | 0.000 | 28 | -1.29 / -2.28 | `log(day_last(Close))` |
| +0.93 | 0.061 | 5 | -1.18 / -2.11 | `mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 60)), cs_demean(ts_delta(log(day_last(Close)), 1)))` |
| +0.81 | 0.006 | 22 | -1.40 / -2.21 | `cross_mean(day_sum(Amt), 60)` |
| +0.80 | 0.008 | 21 | -1.40 / -2.20 | `div(day_sum(Amt), cross_mean(day_sum(Amt), 60))` |
| +0.77 | 0.002 | 31 | -1.48 / -2.25 | `day_last(Close)` |
| +0.36 | 0.184 | 8 | -1.74 / -2.10 | `cross_ema(cross_argmax(cs_demean(sub(day_mean(Ret), 0.5)), 120), 20)` |
| +0.31 | 0.197 | 10 | -1.79 / -2.10 | `cross_argmax(cs_demean(sub(day_mean(Ret), 0.5)), 120)` |
| +0.28 | 0.370 | 13 | -1.82 / -2.10 | `cross_min(cs_demean(sub(day_mean(Ret), 0.5)), 90)` |
| +0.14 | 0.464 | 6 | -1.94 / -2.08 | `cross_ema(cross_argmin(cs_demean(sub(day_mean(Ret), 0.5)), 120), 20)` |
| +0.12 | 0.483 | 8 | -1.97 / -2.08 | `cross_argmin(cs_demean(sub(day_mean(Ret), 0.5)), 120)` |
| -0.05 | 0.612 | 64 | -2.10 / -2.05 | `day_mean(Ret)` |

## 拆解(33 次评估)

### head score +0.22:`cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Volume)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(day_ar1_coefficient(Amt), day_first(Volume))` | -1.24 | -1.24 | -1.16 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Amt)` | -3.40 | -2.82 | -3.40 | — | (子树本身) |
| sufficiency | `day_first(Volume)` | — | — | — | — | 门槛废品 |
| knockout | `sub(day_ar1_coefficient(Amt), day_first(Volume))` | -1.94 | -1.46 | -1.94 | +2.16 | `cross_autocorr_s1(day_ar1_coefficient(Amt), 60)` |
| swap | `Amt->Volume` | +0.21 | +0.57 | +0.21 | — | `cross_autocorr_s1(sub(day_ar1_coefficient(Volume), day_first(Volume)), 60)` |
| swap | `Volume->Amt` | +0.28 | +0.63 | +0.28 | — | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Amt)), 60)` |
| window | `cross_autocorr_s1@60->30` | -0.66 | +0.27 | -0.66 | — | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Volume)), 30)` |
| window | `cross_autocorr_s1@60->120` | +0.13 | +0.57 | +0.13 | — | `cross_autocorr_s1(sub(day_ar1_coefficient(Amt), day_first(Volume)), 120)` |

### head score -0.04:`abs_(ts_std(day_first(Amt), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(day_first(Amt), 50)` | -0.01 | +0.33 | -0.01 | — | (子树本身) |
| sufficiency | `day_first(Amt)` | -1.30 | -1.30 | -0.79 | — | (子树本身) |
| knockout | `ts_std(day_first(Amt), 50)` | -1.30 | -1.30 | -0.79 | +1.26 | `abs_(day_first(Amt))` |
| swap | `Amt->Volume` | -1.83 | -0.89 | -1.83 | — | `abs_(ts_std(day_first(Volume), 50))` |
| window | `ts_std@50->25` | -1.12 | -1.12 | -0.55 | — | `abs_(ts_std(day_first(Amt), 25))` |
| window | `ts_std@50->100` | +0.39 | +0.39 | +0.57 | — | `abs_(ts_std(day_first(Amt), 100))` |

### head score -0.17:`pow_2(cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 90))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 90)` | -0.33 | -0.12 | -0.33 | — | (子树本身) |
| sufficiency | `ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40)` | -1.41 | -0.84 | -1.41 | — | (子树本身) |
| sufficiency | `cs_demean(sub(day_mean(Ret), 0.5))` | -4.34 | -4.34 | -3.69 | — | (子树本身) |
| sufficiency | `day_mean(Ret)` | -4.33 | -4.33 | -3.69 | — | (子树本身) |
| knockout | `cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 90)` | -1.37 | -0.81 | -1.37 | +1.20 | `pow_2(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40))` |
| knockout | `ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40)` | -0.17 | -0.17 | -0.11 | +0.00 | `pow_2(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90))` |
| knockout | `sub(day_mean(Ret), 0.5)` | -0.33 | -0.12 | -0.33 | +0.16 | `pow_2(cross_max(ts_max(cs_demean(day_mean(Ret)), 40), 90))` |
| window | `cross_max@90->45` | -0.25 | -0.25 | +0.08 | — | `pow_2(cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 45))` |
| window | `cross_max@90->180` | -0.16 | +0.40 | -0.16 | — | `pow_2(cross_max(ts_max(cs_demean(sub(day_mean(Ret), 0.5)), 40), 180))` |

### head score -0.20:`pow_2(cross_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 90))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 90)` | -0.19 | -0.19 | -0.15 | — | (子树本身) |
| sufficiency | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30)` | -1.47 | -0.96 | -1.47 | — | (子树本身) |
| sufficiency | `cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5))` | -2.35 | -2.35 | -2.19 | — | (子树本身) |
| sufficiency | `ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10)` | -2.35 | -2.35 | -2.19 | — | (子树本身) |
| knockout | `cross_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 90)` | -1.26 | -1.13 | -1.26 | +1.06 | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30))` |
| knockout | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30)` | -0.20 | -0.20 | +0.03 | -0.01 | `pow_2(cross_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 90))` |
| knockout | `sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)` | -0.19 | -0.19 | -0.15 | -0.01 | `pow_2(cross_max(ts_max(cs_demean(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10)), 30), 90))` |
| knockout | `ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10)` | -0.20 | +0.01 | -0.20 | -0.00 | `pow_2(cross_max(ts_max(cs_demean(sub(cs_demean(sub(day_mean(Ret), -0.5)), -0.5)), 30), 90))` |
| window | `cross_max@90->45` | -0.23 | -0.23 | -0.01 | — | `pow_2(cross_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 45))` |
| window | `cross_max@90->180` | -0.24 | +0.33 | -0.24 | — | `pow_2(cross_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), -0.5)), 10), -0.5)), 30), 180))` |

## 机械核心卡(B0 按这个顺序取)

1. `div(day_sum(Amt), cross_mean(day_sum(Amt), 30))` — enrichment,均值差 +1.91,p 0.001
2. `cross_mean(day_sum(Amt), 30)` — enrichment,均值差 +1.91,p 0.001
3. `cross_max(cs_demean(sub(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), 0.5)), 90)` — enrichment,均值差 +1.75,p 0.002
4. `cs_demean(sub(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), 0.5))` — enrichment,均值差 +1.60,p 0.001
5. `cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90)` — enrichment,均值差 +1.45,p 0.000
6. `cs_demean(ts_delta(log(day_last(Close)), 1))` — enrichment,均值差 +1.15,p 0.000
7. `day_first(Amt)` — enrichment,均值差 +1.07,p 0.057
8. `ts_delta(log(day_last(Close)), 1)` — enrichment,均值差 +1.04,p 0.000
9. `day_sum(Amt)` — enrichment,均值差 +0.99,p 0.000
10. `log(day_last(Close))` — enrichment,均值差 +0.99,p 0.000
11. `mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 60)), cs_demean(ts_delta(log(day_last(Close)), 1)))` — enrichment,均值差 +0.93,p 0.061
12. `cross_mean(day_sum(Amt), 60)` — enrichment,均值差 +0.81,p 0.006
13. `div(day_sum(Amt), cross_mean(day_sum(Amt), 60))` — enrichment,均值差 +0.80,p 0.008
14. `day_last(Close)` — enrichment,均值差 +0.77,p 0.002

## 本组之前各轮的任务

- `prods2030Pr1a_Ea`:核心 `cs_demean(sub(day_mean(Ret), 0.5))`;评分 88,过线 0,入 heads 0;采样计数 {'c05_no_core': 776, 'c05_skeleton': 393, 'mutation_refused': 4}
  - score -0.13(train +0.05 valid -0.13):`add(cross_max(cs_demean(sub(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), 0.5)), 90), day_mean(Ret))`
  - score -0.13(train +0.06 valid -0.13):`add(cross_max(cs_demean(sub(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), 0.5)), 90), cs_demean(sub(day_mean(Ret), 0.5)))`
  - score -0.35(train -0.35 valid +0.62):`add(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), cross_min(cross_min(cs_demean(sub(day_mean(Ret), 0.5)), 90), 15))`
  - score -0.40(train -0.40 valid +0.77):`add(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), cross_min(cs_demean(sub(day_mean(Ret), -2)), 90))`
  - score -0.40(train -0.40 valid +0.26):`add(cross_max(cs_demean(sub(cross_max(cs_demean(sub(add(cross_max(cs_demean(sub(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), 0.5)), 90), cross_min(cs_demean(sub(day_mean(Ret), 0.5)), 90)), 0.5)), 90), 0.5)), 90), add(cross_max(cs_demean(sub(cross_max(cs_demean(sub(day_mean(Ret), 0.5)), 90), 0.5)), 90), cross_min(cs_demean(sub(day_mean(Ret), 0.5)), 90)))`
- `prods2030Pr1b_Nb`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score +0.09(train +0.14 valid +0.09):`cross_max(mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), cs_demean(ts_delta(log(day_last(Close)), 1)))), 60)`
  - score +0.08(train +0.08 valid +0.57):`cross_max(mul(div(day_sum(Amt), cross_mean(cs_demean(ts_delta(log(day_last(Close)), 1)), 60)), cs_demean(ts_delta(log(day_last(Close)), 1))), 60)`
  - score +0.05(train +0.30 valid +0.05):`cross_max(mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), cs_demean(ts_delta(log(day_last(Close)), 1))), 60)`
  - score +0.05(train +0.29 valid +0.05):`cross_max(mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 30)), cs_demean(cs_demean(ts_delta(log(day_last(Close)), 1)))), 60)`
  - score -0.03(train -0.03 valid +0.08):`cross_max(mul(div(day_sum(Amt), cross_mean(day_sum(Amt), 60)), cs_demean(ts_delta(log(day_last(Close)), 1))), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
