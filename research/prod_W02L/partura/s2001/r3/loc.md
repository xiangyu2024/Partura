# 定位:种子 2001,P 组,第 3 轮(只含 train / valid)

快照:prods2001M1_I0_open_search, prods2001M2_I0_open_search, prods2001M3_I0_open_search, prods2001Pr2a_Ea, prods2001Pr2b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.43 | -0.33 | -0.43 | +1 | 20 | prods2001M2_I0_open_search | `cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 40), cross_mean(log(day_sum(Amt)), 120))` |
| -0.62 | -0.62 | -0.54 | +1 | 5 | prods2001M2_I0_open_search | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 40)` |
| -0.67 | -0.67 | -0.40 | +1 | 0 | prods2001M2_I0_open_search | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 50), 40)` |
| -0.86 | -0.86 | -0.74 | -1 | 5 | prods2001M3_I0_open_search | `ts_quantile_q75(ts_sum(ts_kurt(day_q_stat_std(Volume), 50), 50), 50)` |
| -1.11 | -1.10 | -1.11 | -1 | 5 | prods2001M1_I0_open_search | `day_max(Volume)` |
| -1.11 | -1.10 | -1.11 | -1 | 5 | prods2001M1_I0_open_search | `pow_1_5(day_max(Volume))` |
| -1.13 | -0.67 | -1.13 | +1 | 5 | prods2001M3_I0_open_search | `ts_var(day_q_stat_std(Volume), 50)` |
| -1.51 | -1.51 | +0.02 | +1 | 20 | prods2001M1_I0_open_search | `ts_autocorr_s1(cross_delay(ts_quantile_q50(day_max(Amt), 20), 241), 20)` |
| -1.63 | -1.50 | -1.63 | +1 | 5 | prods2001M3_I0_open_search | `ts_autocorr_s1(day_q_stat_std(Volume), 50)` |

## 共性:229 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.42 | 0.001 | 6 | -1.06 / -2.48 | `log(day_sum(Amt))` |
| +1.35 | 0.006 | 5 | -1.12 / -2.47 | `div(div(ListAge, day_topw_mean(Open, High)), day_topw_mean(Open, High))` |
| +1.33 | 0.006 | 5 | -1.14 / -2.47 | `div(ListAge, day_topw_mean(Open, Volume))` |
| +1.33 | 0.006 | 5 | -1.14 / -2.47 | `day_topw_mean(Open, Volume)` |
| +1.30 | 0.000 | 8 | -1.18 / -2.49 | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` |
| +1.10 | 0.000 | 11 | -1.40 / -2.50 | `ts_quantile_q75(day_q_stat_std(Volume), 50)` |
| +1.08 | 0.000 | 113 | -1.90 / -2.97 | `day_q_stat_std(Volume)` |
| +1.08 | 0.000 | 13 | -1.43 / -2.50 | `ts_quantile_q75(day_q_stat_std(Volume), 40)` |
| +1.07 | 0.023 | 4 | -1.39 / -2.46 | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 50), 40)` |
| +1.05 | 0.002 | 11 | -1.45 / -2.49 | `day_sum(Amt)` |
| +1.03 | 0.006 | 9 | -1.46 / -2.48 | `div(ListAge, day_topw_mean(Open, High))` |
| +0.85 | 0.003 | 16 | -1.66 / -2.50 | `day_topw_mean(Open, High)` |
| +0.73 | 0.016 | 8 | -1.73 / -2.47 | `ts_quantile_q75(day_q_stat_std(Volume), 5)` |
| +0.56 | 0.108 | 7 | -1.90 / -2.46 | `cross_mean(day_q_stat_std(Volume), 120)` |
| +0.54 | 0.185 | 5 | -1.91 / -2.46 | `cross_mean(day_sum(Amt), 60)` |
| +0.50 | 0.082 | 10 | -1.97 / -2.47 | `day_q_stat_std(div(Volume, cross_mean(Volume, 20)))` |
| +0.40 | 0.087 | 19 | -2.08 / -2.48 | `log(day_q_stat_std(Volume))` |
| -0.03 | 0.465 | 5 | -2.47 / -2.44 | `day_max(Volume)` |
| -0.13 | 0.752 | 10 | -2.56 / -2.44 | `day_std(Ret)` |
| -0.23 | 0.827 | 4 | -2.67 / -2.44 | `cross_delay(day_max(High), 60)` |

## 拆解(32 次评估)

### head score -0.43:`cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 40), cross_mean(log(day_sum(Amt)), 120))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 40)` | -0.75 | -0.69 | -0.75 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50)` | -1.25 | -1.05 | -1.25 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40)` | -1.75 | -1.34 | -1.75 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` | -1.73 | -1.57 | -1.73 | — | (子树本身) |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 40)` | -0.85 | -0.70 | -0.85 | +0.42 | `cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), cross_mean(log(day_sum(Amt)), 120))` |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50)` | -1.03 | -0.75 | -1.03 | +0.60 | `cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 40), cross_mean(log(day_sum(Amt)), 120))` |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40)` | -0.83 | -0.70 | -0.83 | +0.40 | `cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), cross_mean(log(day_sum(Amt)), 120))` |
| swap | `Volume->Amt` | -0.58 | -0.33 | -0.58 | — | `cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Amt), 40), 40), 40), 50), 40), cross_mean(log(day_sum(Amt)), 120))` |
| swap | `Amt->Volume` | -1.34 | -1.11 | -1.34 | — | `cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 40), cross_mean(log(day_sum(Volume)), 120))` |
| window | `ts_quantile_q75@40->20` | -0.67 | -0.51 | -0.67 | — | `cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 20), cross_mean(log(day_sum(Amt)), 120))` |
| window | `ts_quantile_q75@40->80` | -0.36 | -0.31 | -0.36 | — | `cs_regres(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 50), 80), cross_mean(log(day_sum(Amt)), 120))` |

### head score -0.62:`ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40)` | -0.73 | -0.68 | -0.73 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40)` | -1.26 | -1.07 | -1.26 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50)` | -1.31 | -1.31 | -1.29 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` | -1.73 | -1.57 | -1.73 | — | (子树本身) |
| knockout | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50)` | -0.96 | -0.67 | -0.96 | +0.34 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 40), 40), 40)` |
| knockout | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` | -0.87 | -0.70 | -0.87 | +0.25 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 50), 40), 40), 40)` |
| swap | `Volume->Amt` | -0.68 | -0.68 | -0.51 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Amt), 40), 40), 50), 40), 40), 40)` |
| window | `ts_quantile_q75@40->20` | -0.75 | -0.75 | -0.63 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 20)` |
| window | `ts_quantile_q75@40->80` | -0.58 | -0.58 | -0.46 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40), 50), 40), 40), 80)` |

### head score -0.86:`ts_quantile_q75(ts_sum(ts_kurt(day_q_stat_std(Volume), 50), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(ts_kurt(day_q_stat_std(Volume), 50), 50)` | -1.11 | -0.69 | -1.11 | — | (子树本身) |
| sufficiency | `ts_kurt(day_q_stat_std(Volume), 50)` | -0.93 | -0.28 | -0.93 | — | (子树本身) |
| sufficiency | `day_q_stat_std(Volume)` | -2.36 | -2.36 | -2.21 | — | (子树本身) |
| knockout | `ts_sum(ts_kurt(day_q_stat_std(Volume), 50), 50)` | -1.16 | -0.78 | -1.16 | +0.29 | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` |
| knockout | `ts_kurt(day_q_stat_std(Volume), 50)` | -1.91 | -1.91 | -1.24 | +1.05 | `ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50)` |
| swap | `Volume->Amt` | -0.91 | -0.82 | -0.91 | — | `ts_quantile_q75(ts_sum(ts_kurt(day_q_stat_std(Amt), 50), 50), 50)` |
| window | `ts_quantile_q75@50->25` | -0.89 | -0.67 | -0.89 | — | `ts_quantile_q75(ts_sum(ts_kurt(day_q_stat_std(Volume), 50), 50), 25)` |
| window | `ts_quantile_q75@50->100` | -0.91 | -0.91 | -0.60 | — | `ts_quantile_q75(ts_sum(ts_kurt(day_q_stat_std(Volume), 50), 50), 100)` |

### head score -1.13:`ts_var(day_q_stat_std(Volume), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(Volume)` | -2.36 | -2.36 | -2.21 | — | (子树本身) |
| swap | `Volume->Amt` | -1.08 | -0.77 | -1.08 | — | `ts_var(day_q_stat_std(Amt), 50)` |
| window | `ts_var@50->25` | -1.60 | -1.43 | -1.60 | — | `ts_var(day_q_stat_std(Volume), 25)` |
| window | `ts_var@50->100` | -1.16 | -0.68 | -1.16 | — | `ts_var(day_q_stat_std(Volume), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `log(day_sum(Amt))` — enrichment,均值差 +1.42,p 0.001
2. `div(div(ListAge, day_topw_mean(Open, High)), day_topw_mean(Open, High))` — enrichment,均值差 +1.35,p 0.006
3. `div(ListAge, day_topw_mean(Open, Volume))` — enrichment,均值差 +1.33,p 0.006
4. `day_topw_mean(Open, Volume)` — enrichment,均值差 +1.33,p 0.006
5. `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 40), 40)` — enrichment,均值差 +1.30,p 0.000
6. `ts_quantile_q75(day_q_stat_std(Volume), 50)` — enrichment,均值差 +1.10,p 0.000
7. `day_q_stat_std(Volume)` — enrichment,均值差 +1.08,p 0.000
8. `ts_quantile_q75(day_q_stat_std(Volume), 40)` — enrichment,均值差 +1.08,p 0.000
9. `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 50), 40)` — enrichment,均值差 +1.07,p 0.023
10. `day_sum(Amt)` — enrichment,均值差 +1.05,p 0.002
11. `div(ListAge, day_topw_mean(Open, High))` — enrichment,均值差 +1.03,p 0.006
12. `day_topw_mean(Open, High)` — enrichment,均值差 +0.85,p 0.003
13. `ts_quantile_q75(day_q_stat_std(Volume), 5)` — enrichment,均值差 +0.73,p 0.016
14. `day_q_stat_std(div(Volume, cross_mean(Volume, 20)))` — enrichment,均值差 +0.50,p 0.082
15. `log(day_q_stat_std(Volume))` — enrichment,均值差 +0.40,p 0.087

## 本组之前各轮的任务

- `prods2001Pr2a_Ea`:核心 `day_q_stat_std(Volume)`;评分 98,过线 0,入 heads 0;采样计数 {'c05_no_core': 652, 'c05_skeleton': 302}
  - score -0.04(train +0.66 valid -0.04):`add(day_q_stat_std(Volume), div(div(ListAge, day_topw_mean(Open, High)), day_topw_mean(Open, High)))`
  - score -0.05(train +0.66 valid -0.05):`add(day_q_stat_std(Volume), div(div(ListAge, day_topw_mean(High, High)), day_topw_mean(High, High)))`
  - score -0.20(train +0.09 valid -0.20):`cross_regbeta(log(day_sum(Amt)), log(day_q_stat_std(Volume)), 10)`
  - score -0.66(train -0.22 valid -0.66):`cross_regbeta(log(day_sum(Amt)), log(day_q_stat_std(Volume)), 120)`
  - score -0.68(train -0.68 valid -0.57):`add(day_q_stat_std(Volume), div(div(div(ListAge, day_topw_mean(Open, High)), day_topw_mean(Open, High)), day_topw_mean(Open, High)))`
- `prods2001Pr2b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.79(train -0.79 valid +0.71):`cross_corr(day_q_stat_std(div(Ret, cross_mean(Ret, 20))), day_std(Ret), 120)`
  - score -1.00(train -1.00 valid +0.26):`cross_corr(day_q_stat_std(div(Volume, cross_mean(Volume, 20))), day_std(cross_mean(Volume, 20)), 120)`
  - score -1.05(train -0.91 valid -1.05):`cross_corr(day_q_stat_std(div(Volume, cross_mean(Volume, 20))), pow_1_5(day_mean(Low)), 60)`
  - score -1.06(train -1.06 valid -0.94):`cross_semistd_pos(cross_delay(day_max(div(Volume, cross_mean(Volume, 20))), 30), 60)`
  - score -1.39(train -1.12 valid -1.39):`cross_reg_tvalue(day_q_stat_std(div(Volume, cross_mean(Volume, 20))), pow_1_5(day_mean(Volume)), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
