# 定位:种子 2036,P 组,第 3 轮(只含 train / valid)

快照:prods2036M1_I0_open_search, prods2036M2_I0_open_search, prods2036M3_I0_open_search, prods2036Pr1a_Ea, prods2036Pr1b_Nb, prods2036Pr2a_Ea, prods2036Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.54 | -0.29 | -0.54 | +1 | 0 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 180)` |
| -1.11 | -1.11 | -0.67 | +1 | 5 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.95, False), 20)` |
| -1.55 | -1.55 | -1.06 | +1 | 5 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, True), 20)` |
| -2.69 | -2.69 | -1.80 | +1 | 5 | prods2036M3_I0_open_search | `cross_stddev(energy_ratio_topm(delete_open_close(Volume), 5, False), 20)` |
| -2.78 | -2.78 | -2.24 | -1 | 20 | prods2036M3_I0_open_search | `cross_stddev(energy_ratio_topm(delete_open_close(Ret), 20, False), 20)` |
| -2.85 | -2.85 | -2.38 | -1 | 20 | prods2036M3_I0_open_search | `cross_stddev(energy_ratio_topm(delete_open_close(Ret), 5, False), 20)` |

## 共性:237 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.60 | 0.002 | 6 | -0.15 / -1.75 | `cross_max(cross_max(day_last(Close), 241), 241)` |
| +1.53 | 0.000 | 46 | -0.47 / -2.01 | `cross_max(day_last(Close), 241)` |
| +1.52 | 0.000 | 61 | -0.58 / -2.10 | `day_last(Close)` |
| +1.45 | 0.000 | 20 | -0.38 / -1.83 | `div(day_last(Close), cross_max(day_last(Close), 241))` |
| +1.44 | 0.000 | 40 | -0.51 / -1.95 | `cross_mean(day_sum(Ret), 20)` |
| +1.43 | 0.018 | 4 | -0.30 / -1.73 | `div(day_last(Close), cross_max(cross_max(day_last(Close), 241), 241))` |
| +1.33 | 0.000 | 18 | -0.48 / -1.81 | `div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241))` |
| +1.29 | 0.000 | 65 | -0.77 / -2.06 | `day_sum(Ret)` |
| +1.22 | 0.000 | 28 | -0.63 / -1.85 | `cross_mean(day_last(Close), 20)` |
| +1.20 | 0.015 | 6 | -0.54 / -1.74 | `day_std(delete_open_close(Volume))` |
| +1.17 | 0.025 | 6 | -0.57 / -1.74 | `cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241)))` |
| +1.00 | 0.073 | 5 | -0.73 / -1.73 | `cross_mean(cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241))), 20)` |
| +0.92 | 0.031 | 10 | -0.83 / -1.75 | `cs_first_low20(cross_mean(day_sum(Ret), 20), day_quantile_q75(Vwap))` |
| +0.75 | 0.082 | 8 | -0.99 / -1.73 | `cross_max(day_quantile(Close), 241)` |
| +0.68 | 0.226 | 4 | -1.04 / -1.72 | `cross_mean(day_std(Ret), 60)` |
| +0.64 | 0.013 | 61 | -1.23 / -1.87 | `day_quantile_q75(Vwap)` |
| +0.64 | 0.125 | 9 | -1.10 / -1.73 | `day_quantile(Close)` |
| +0.62 | 0.049 | 8 | -1.11 / -1.73 | `day_std(Volume)` |
| +0.61 | 0.132 | 11 | -1.13 / -1.74 | `cross_zscore(day_quantile_q75(Vwap), 241)` |
| +0.56 | 0.232 | 4 | -1.16 / -1.72 | `div(day_last(Close), cross_max(day_quantile(Close), 241))` |

## 拆解(14 次评估)

### head score -0.54:`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 180)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_n(delete_open_close(Volume), 0.9, False)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -0.62 | -0.29 | -0.62 | — | `cross_stddev(energy_ratio_n(delete_open_close(Amt), 0.9, False), 180)` |
| window | `cross_stddev@180->90` | -0.90 | -0.72 | -0.90 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 90)` |
| window | `cross_stddev@180->360` | -0.67 | -0.67 | -0.18 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 360)` |

### head score -2.69:`cross_stddev(energy_ratio_topm(delete_open_close(Volume), 5, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_topm(delete_open_close(Volume), 5, False)` | -3.83 | -3.83 | -3.52 | — | (子树本身) |
| swap | `Volume->Amt` | -2.47 | -2.47 | -1.63 | — | `cross_stddev(energy_ratio_topm(delete_open_close(Amt), 5, False), 20)` |
| window | `cross_stddev@20->10` | -2.36 | -2.36 | -1.78 | — | `cross_stddev(energy_ratio_topm(delete_open_close(Volume), 5, False), 10)` |
| window | `cross_stddev@20->40` | -2.59 | -2.59 | -2.10 | — | `cross_stddev(energy_ratio_topm(delete_open_close(Volume), 5, False), 40)` |

### head score -2.78:`cross_stddev(energy_ratio_topm(delete_open_close(Ret), 20, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_topm(delete_open_close(Ret), 20, False)` | -3.92 | -3.92 | -3.80 | — | (子树本身) |
| window | `cross_stddev@20->10` | -2.74 | -2.74 | -2.31 | — | `cross_stddev(energy_ratio_topm(delete_open_close(Ret), 20, False), 10)` |
| window | `cross_stddev@20->40` | -2.84 | -2.84 | -2.19 | — | `cross_stddev(energy_ratio_topm(delete_open_close(Ret), 20, False), 40)` |

### head score -2.85:`cross_stddev(energy_ratio_topm(delete_open_close(Ret), 5, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_topm(delete_open_close(Ret), 5, False)` | -4.32 | -4.06 | -4.32 | — | (子树本身) |
| window | `cross_stddev@20->10` | -2.91 | -2.91 | -2.69 | — | `cross_stddev(energy_ratio_topm(delete_open_close(Ret), 5, False), 10)` |
| window | `cross_stddev@20->40` | -2.77 | -2.77 | -2.32 | — | `cross_stddev(energy_ratio_topm(delete_open_close(Ret), 5, False), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_max(cross_max(day_last(Close), 241), 241)` — enrichment,均值差 +1.60,p 0.002
2. `cross_max(day_last(Close), 241)` — enrichment,均值差 +1.53,p 0.000
3. `day_last(Close)` — enrichment,均值差 +1.52,p 0.000
4. `div(day_last(Close), cross_max(day_last(Close), 241))` — enrichment,均值差 +1.45,p 0.000
5. `cross_mean(day_sum(Ret), 20)` — enrichment,均值差 +1.44,p 0.000
6. `div(day_last(Close), cross_max(cross_max(day_last(Close), 241), 241))` — enrichment,均值差 +1.43,p 0.018
7. `div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241))` — enrichment,均值差 +1.33,p 0.000
8. `day_sum(Ret)` — enrichment,均值差 +1.29,p 0.000
9. `cross_mean(day_last(Close), 20)` — enrichment,均值差 +1.22,p 0.000
10. `day_std(delete_open_close(Volume))` — enrichment,均值差 +1.20,p 0.015
11. `cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241)))` — enrichment,均值差 +1.17,p 0.025
12. `cross_mean(cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241))), 20)` — enrichment,均值差 +1.00,p 0.073
13. `cs_first_low20(cross_mean(day_sum(Ret), 20), day_quantile_q75(Vwap))` — enrichment,均值差 +0.92,p 0.031
14. `cross_max(day_quantile(Close), 241)` — enrichment,均值差 +0.75,p 0.082
15. `day_quantile_q75(Vwap)` — enrichment,均值差 +0.64,p 0.013
16. `day_std(Volume)` — enrichment,均值差 +0.62,p 0.049

## 本组之前各轮的任务

- `prods2036Pr1a_Ea`:核心 `energy_ratio_n(delete_open_close(Volume), 0.9, False)`;评分 85,过线 0,入 heads 0;采样计数 {'c05_no_core': 1371, 'c05_skeleton': 747}
  - score +0.04(train +0.43 valid +0.04):`cross_regbeta(day_std(Volume), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120)`
  - score +0.01(train +0.01 valid +0.34):`cross_regbeta(day_std(Volume), cross_regbeta(day_std(delete_open_close(Volume)), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120), 120)`
  - score -0.01(train -0.01 valid +0.43):`cross_regbeta(day_std(delete_open_close(Volume)), cross_regbeta(day_std(delete_open_close(Volume)), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120), 120)`
  - score -0.01(train -0.01 valid +0.59):`cross_regbeta(day_std(Volume), cross_regbeta(day_std(Volume), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120), 120)`
  - score -0.13(train +0.48 valid -0.13):`cross_regbeta(day_std(delete_open_close(Volume)), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120)`
- `prods2036Pr1b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.37(train +0.37 valid +0.48):`cs_first_low20(cs_first_low20(day_sum(Vwap), day_sum(Vwap)), cs_first_low20(day_sum(Vwap), day_sum(Vwap)))`
  - score +0.35(train +0.35 valid +0.45):`cs_first_low40(day_sum(Vwap), day_sum(Vwap))`
  - score +0.06(train +0.06 valid +0.80):`cs_first_low20(day_sum(Vwap), day_sum(Vwap))`
  - score +0.01(train +0.01 valid +0.26):`cs_first_low20(cs_first_low20(day_std(Vwap), day_std(Vwap)), cs_first_low20(day_std(Vwap), day_std(Vwap)))`
  - score -0.01(train -0.01 valid +0.19):`cs_first_low20(day_var(Close), day_var(Close))`
- `prods2036Pr2a_Ea`:核心 `day_quantile_q75(Vwap)`;评分 95,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 1, 'c05_no_core': 1562, 'c05_skeleton': 741}
  - score -0.32(train -0.10 valid -0.32):`cs_first_low20(cross_mean(day_sum(Ret), 20), day_quantile_q75(Vwap))`
  - score -0.35(train -0.35 valid -0.27):`cs_first_low20(cross_mean(day_sum(Ret), 10), day_quantile_q75(Vwap))`
  - score -0.37(train -0.23 valid -0.37):`cs_first_low20(cross_mean(day_sum(Ret), 120), day_quantile_q75(Vwap))`
  - score -0.41(train -0.21 valid -0.41):`cs_first_low20(cross_stddev(day_sum(Ret), 60), day_quantile_q75(Vwap))`
  - score -0.41(train -0.28 valid -0.41):`cs_first_low20(cs_first_low20(cross_zscore(day_quantile_q75(Vwap), 241), day_quantile_q75(Close)), day_quantile_q75(Close))`
- `prods2036Pr2b_Nb`:核心 `—`;评分 97,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.46(train +0.46 valid +0.86):`cs_first_low20(div(day_last(Close), cross_max(cross_max(day_last(Close), 241), 241)), div(day_last(Close), cross_max(cross_max(day_last(Close), 241), 241)))`
  - score +0.46(train +0.46 valid +0.46):`cs_first_low20(cross_mean(day_sum(Ret), 15), div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241)))`
  - score +0.40(train +0.40 valid +0.44):`cs_first_low20(cross_mean(day_sum(Ret), 20), div(day_last(Close), cross_max(day_last(Close), 241)))`
  - score +0.38(train +0.38 valid +0.45):`cs_first_low20(cross_mean(day_sum(Ret), 20), div(day_last(Close), cross_max(day_last(Low), 241)))`
  - score +0.37(train +0.43 valid +0.37):`cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last(Close), 20), cross_max(day_last(Close), 241)))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.33(window cross_stddev@20->10):`cross_stddev(energy_ratio_topm(delete_open_close(Volume), 5, False), 10)`
- 增益 +0.22(swap Volume->Amt):`cross_stddev(energy_ratio_topm(delete_open_close(Amt), 5, False), 20)`
