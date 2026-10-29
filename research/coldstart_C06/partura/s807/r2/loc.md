# 定位:种子 807,C 组,第 2 轮(只含 train / valid)

快照:c05s807M1_I0_open_search, c05s807M2_I0_open_search, c06s807Cr1a_Ea, c06s807Cr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(8 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.78 | +1.78 | +2.69 | -1 | 20 | c05s807M2_I0_open_search | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)` |
| +1.49 | +1.49 | +2.45 | -1 | 20 | c06s807Cr1a_Ea | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)` |
| +1.18 | +1.18 | +1.35 | -1 | 20 | c05s807M1_I0_open_search | `pow_2(pow_2(day_wmean(Ret, Ret)))` |
| +1.10 | +1.10 | +2.05 | -1 | 0 | c05s807M2_I0_open_search | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` |
| +0.83 | +0.83 | +1.35 | -1 | 5 | c06s807Cr1a_Ea | `ts_mean(pow_2(day_wmean(Ret, Ret)), 50)` |
| +0.59 | +0.59 | +1.83 | -1 | 20 | c06s807Cr1a_Ea | `cross_mean(cross_min(pow_2(pow_2(day_wmean(Ret, Ret))), 30), 5)` |
| +0.55 | +0.55 | +0.73 | -1 | 5 | c06s807Cr1a_Ea | `cross_mean(cs_winsor(pow_2(day_wmean(Ret, Ret))), 10)` |
| +0.52 | +0.52 | +0.84 | +1 | 0 | c05s807M2_I0_open_search | `ts_sum(LogFloatShares, 30)` |

## 共性:301 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.57 | 0.000 | 16 | +0.84 / -0.73 | `ts_sum(pow_3(day_durbin_watson(High)), 1)` |
| +1.55 | 0.000 | 7 | +0.86 / -0.68 | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` |
| +1.41 | 0.000 | 30 | +0.62 / -0.79 | `pow_3(day_durbin_watson(High))` |
| +1.34 | 0.011 | 4 | +0.67 / -0.66 | `pow_2(pow_2(day_wmean(Ret, Ret)))` |
| +1.31 | 0.012 | 4 | +0.64 / -0.66 | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` |
| +1.17 | 0.002 | 12 | +0.47 / -0.69 | `pow_2_5(LogFloatShares)` |
| +1.16 | 0.022 | 4 | +0.50 / -0.66 | `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` |
| +1.15 | 0.000 | 57 | +0.29 / -0.87 | `day_durbin_watson(High)` |
| +1.14 | 0.022 | 6 | +0.47 / -0.67 | `cross_fangzheng(pow_2_5(LogFloatShares), 60)` |
| +1.14 | 0.040 | 4 | +0.48 / -0.66 | `pow_3(pow_2_5(LogFloatShares))` |
| +1.05 | 0.002 | 12 | +0.36 / -0.69 | `cross_stddev(day_durbin_watson(High), 60)` |
| +0.82 | 0.000 | 69 | -0.02 / -0.83 | `day_wmean(Ret, Ret)` |
| +0.79 | 0.000 | 62 | -0.02 / -0.81 | `pow_2(day_wmean(Ret, Ret))` |
| +0.74 | 0.020 | 14 | +0.06 / -0.68 | `cs_normalize(pow_2(day_wmean(Ret, Ret)))` |
| +0.49 | 0.093 | 19 | -0.18 / -0.68 | `day_var(Ret)` |
| +0.38 | 0.329 | 4 | -0.27 / -0.65 | `cross_mean(day_std(Ret), 20)` |
| +0.08 | 0.570 | 10 | -0.57 / -0.65 | `ts_cov(day_median(Vwap), day_var(Ret), 20)` |
| +0.07 | 0.563 | 5 | -0.58 / -0.65 | `day_wmean(abs_(Ret), Ret)` |
| +0.07 | 0.563 | 5 | -0.58 / -0.65 | `pow_2(day_wmean(abs_(Ret), Ret))` |
| +0.07 | 0.563 | 5 | -0.58 / -0.65 | `div(pow_2(day_wmean(Ret, Ret)), pow_2(day_wmean(abs_(Ret), Ret)))` |

## 拆解(28 次评估)

### head score +1.78:`ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 1)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` | +1.78 | +1.78 | +2.66 | — | (子树本身) |
| sufficiency | `ts_sum(pow_3(day_durbin_watson(High)), 1)` | +0.96 | +0.96 | +2.64 | — | (子树本身) |
| sufficiency | `pow_3(day_durbin_watson(High))` | +0.96 | +0.96 | +2.64 | — | (子树本身) |
| sufficiency | `day_durbin_watson(High)` | -1.17 | -1.17 | +0.58 | — | (子树本身) |
| knockout | `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` | +0.96 | +0.96 | +2.64 | +0.81 | `ts_sum(ts_sum(pow_3(day_durbin_watson(High)), 1), 1)` |
| knockout | `ts_sum(pow_3(day_durbin_watson(High)), 1)` | +1.78 | +1.78 | +2.67 | -0.00 | `ts_sum(pow_2_5(pow_3(day_durbin_watson(High))), 1)` |
| knockout | `pow_3(day_durbin_watson(High))` | +0.72 | +0.72 | +2.36 | +1.06 | `ts_sum(pow_2_5(ts_sum(day_durbin_watson(High), 1)), 1)` |
| swap | `High->Low` | +1.54 | +1.54 | +2.77 | — | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(Low)), 1)), 1)` |
| window | `ts_sum@1->2` | +1.90 | +1.90 | +2.69 | — | `ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 2)` |

### head score +1.49:`ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | +1.48 | +1.48 | +2.72 | — | (子树本身) |
| sufficiency | `mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))` | +1.10 | +1.10 | +2.44 | — | (子树本身) |
| sufficiency | `pow_2(day_wmean(Ret, Ret))` | +0.89 | +0.89 | +1.66 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Ret)` | -0.19 | -0.15 | -0.19 | — | (子树本身) |
| knockout | `pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` | +0.88 | +0.88 | +2.05 | +0.62 | `ts_mean(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)), 30)` |
| knockout | `mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))` | +1.32 | +1.32 | +1.54 | +0.17 | `ts_mean(pow_2(pow_2(day_wmean(Ret, Ret))), 30)` |
| knockout | `pow_2(day_wmean(Ret, Ret))` | +1.24 | +1.24 | +2.61 | +0.26 | `ts_mean(pow_2(mul(day_wmean(Ret, Ret), day_var(Ret))), 30)` |
| window | `ts_mean@30->15` | +1.75 | +1.75 | +2.48 | — | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 15)` |
| window | `ts_mean@30->60` | +1.51 | +1.51 | +2.19 | — | `ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 60)` |

### head score +1.10:`ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(day_durbin_watson(High), 60)` | +1.10 | +1.10 | +2.04 | — | (子树本身) |
| sufficiency | `day_durbin_watson(High)` | -1.17 | -1.17 | +0.58 | — | (子树本身) |
| knockout | `cross_stddev(day_durbin_watson(High), 60)` | -1.18 | -1.18 | +0.56 | +2.28 | `ts_sum(day_durbin_watson(High), 1)` |
| swap | `High->Low` | +0.92 | +0.92 | +1.99 | — | `ts_sum(cross_stddev(day_durbin_watson(Low), 60), 1)` |
| window | `ts_sum@1->2` | +0.88 | +0.88 | +1.95 | — | `ts_sum(cross_stddev(day_durbin_watson(High), 60), 2)` |

### head score +0.83:`ts_mean(pow_2(day_wmean(Ret, Ret)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_wmean(Ret, Ret))` | +0.89 | +0.89 | +1.66 | — | (子树本身) |
| sufficiency | `day_wmean(Ret, Ret)` | -0.19 | -0.15 | -0.19 | — | (子树本身) |
| knockout | `pow_2(day_wmean(Ret, Ret))` | +0.49 | +0.49 | +0.66 | +0.34 | `ts_mean(day_wmean(Ret, Ret), 50)` |
| window | `ts_mean@50->25` | +0.77 | +0.77 | +1.45 | — | `ts_mean(pow_2(day_wmean(Ret, Ret)), 25)` |
| window | `ts_mean@50->100` | +0.82 | +0.82 | +1.86 | — | `ts_mean(pow_2(day_wmean(Ret, Ret)), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1))` — ablation,自身 score +1.78(所在 head +1.78)
2. `pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)))` — ablation,自身 score +1.48(所在 head +1.49)
3. `cross_stddev(day_durbin_watson(High), 60)` — ablation,自身 score +1.10(所在 head +1.10)
4. `mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))` — ablation,自身 score +1.10(所在 head +1.49)
5. `pow_2(day_wmean(Ret, Ret))` — ablation,自身 score +0.89(所在 head +0.83)
6. `ts_sum(pow_3(day_durbin_watson(High)), 1)` — enrichment,均值差 +1.57,p 0.000
7. `pow_3(day_durbin_watson(High))` — enrichment,均值差 +1.41,p 0.000
8. `pow_2(pow_2(day_wmean(Ret, Ret)))` — enrichment,均值差 +1.34,p 0.011
9. `ts_sum(cross_stddev(day_durbin_watson(High), 60), 1)` — enrichment,均值差 +1.31,p 0.012
10. `pow_2_5(LogFloatShares)` — enrichment,均值差 +1.17,p 0.002
11. `cross_fangzheng(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 60)` — enrichment,均值差 +1.16,p 0.022
12. `day_durbin_watson(High)` — enrichment,均值差 +1.15,p 0.000
13. `cross_fangzheng(pow_2_5(LogFloatShares), 60)` — enrichment,均值差 +1.14,p 0.022
14. `pow_3(pow_2_5(LogFloatShares))` — enrichment,均值差 +1.14,p 0.040
15. `day_wmean(Ret, Ret)` — enrichment,均值差 +0.82,p 0.000
16. `cs_normalize(pow_2(day_wmean(Ret, Ret)))` — enrichment,均值差 +0.74,p 0.020
17. `day_var(Ret)` — enrichment,均值差 +0.49,p 0.093

## 本组之前各轮的任务

- `c06s807Cr1a_Ea`:核心 `pow_2(day_wmean(Ret, Ret))`;评分 84,过线 20,入 heads 4;采样计数 {'c05_no_core': 1519, 'c05_periphery_seen': 6}
  - score +1.49(train +1.49 valid +2.45):`ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 30)`
  - score +1.12(train +1.12 valid +1.64):`cross_decay_linear(cs_normalize(pow_2(day_wmean(Ret, Ret))), 5)`
  - score +1.08(train +1.08 valid +1.81):`cross_mean(cross_mean(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret)), 241), 5)`
  - score +1.06(train +1.06 valid +1.06):`ts_var(ts_var(pow_2(day_wmean(Ret, Ret)), 30), 30)`
  - score +1.03(train +1.03 valid +1.39):`ts_var(pow_2(day_wmean(Ret, Ret)), 50)`
- `c06s807Cr1b_Nb`:核心 `—`;评分 85,过线 0,入 heads 0;采样计数 {}
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(pow_2(cross_quantile_q75(cs_rank(day_mean(Ret)), 241)), 10)`
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(pow_2(cross_quantile_q75(cs_rank(cs_rank(day_mean(Ret))), 241)), 10)`
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(cross_quantile_q75(cs_rank(day_mean(Ret)), 241), 10)`
  - score -0.15(train -0.15 valid -0.11):`cross_semistd_pos(cross_quantile_q75(cs_rank(cs_rank(day_mean(Ret))), 241), 10)`
  - score -0.41(train -0.41 valid +1.08):`cross_semistd_pos(pow_2(cross_quantile_q75(day_mean(Ret), 241)), 10)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.25(window ts_mean@30->15):`ts_mean(pow_2(mul(pow_2(day_wmean(Ret, Ret)), day_var(Ret))), 15)`
- 增益 +0.13(window ts_sum@1->2):`ts_sum(pow_2_5(ts_sum(pow_3(day_durbin_watson(High)), 1)), 2)`
