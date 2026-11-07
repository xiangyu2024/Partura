# 定位:种子 904,P 组,第 2 轮(只含 train / valid)

快照:prods904M1_I0_open_search, prods904M2_I0_open_search, prods904Pr1a_Ea, prods904Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.92 | +0.97 | +0.92 | +1 | 5 | prods904M2_I0_open_search | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)` |

## 共性:337 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.17 | 0.000 | 14 | -0.42 / -1.59 | `div(cs_robust_z(day_mean(Low)), day_first(Open))` |
| +1.14 | 0.000 | 15 | -0.44 / -1.59 | `cs_robust_z(day_mean(Low))` |
| +1.12 | 0.000 | 10 | -0.45 / -1.57 | `log(div(cs_robust_z(day_mean(Low)), day_first(Open)))` |
| +0.98 | 0.000 | 18 | -0.61 / -1.59 | `day_mean(Low)` |
| +0.97 | 0.012 | 4 | -0.57 / -1.55 | `day_topw_mean(Amt, Amt)` |
| +0.92 | 0.033 | 4 | -0.63 / -1.55 | `sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(cs_robust_z(day_mean(Low)), day_first(Open))))` |
| +0.79 | 0.014 | 10 | -0.77 / -1.56 | `abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30))` |
| +0.77 | 0.015 | 6 | -0.78 / -1.55 | `abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40))` |
| +0.77 | 0.023 | 5 | -0.78 / -1.55 | `pow_05(abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)))` |
| +0.73 | 0.063 | 6 | -0.82 / -1.55 | `pow_05(abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)))` |
| +0.62 | 0.172 | 4 | -0.93 / -1.54 | `cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15), 15)` |
| +0.59 | 0.004 | 36 | -1.01 / -1.60 | `day_gini(Volume)` |
| +0.58 | 0.015 | 16 | -0.99 / -1.56 | `cross_zscore(day_topw_mean(Ret, Amt), 60)` |
| +0.58 | 0.003 | 17 | -0.99 / -1.57 | `ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)` |
| +0.54 | 0.066 | 11 | -1.02 / -1.55 | `cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15)` |
| +0.50 | 0.001 | 43 | -1.10 / -1.60 | `ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)` |
| +0.44 | 0.072 | 7 | -1.10 / -1.55 | `pow_05(cross_ema(day_sum(Ret), 241))` |
| +0.42 | 0.178 | 6 | -1.12 / -1.54 | `ts_regbeta(day_gini(Volume), day_kurt(Open), 30)` |
| +0.42 | 0.189 | 5 | -1.12 / -1.54 | `ts_regbeta(day_gini(Volume), day_kurt(Open), 50)` |
| +0.40 | 0.103 | 8 | -1.14 / -1.55 | `cross_ema(day_sum(Ret), 241)` |

## 拆解(6 次评估)

### head score +0.92:`ts_regbeta(day_gini(Volume), day_kurt(Vwap), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_gini(Volume)` | -2.76 | -2.76 | -2.31 | — | (子树本身) |
| sufficiency | `day_kurt(Vwap)` | -3.38 | -3.38 | -2.72 | — | (子树本身) |
| swap | `Volume->Amt` | +0.88 | +0.92 | +0.88 | — | `ts_regbeta(day_gini(Amt), day_kurt(Vwap), 50)` |
| swap | `Vwap->Close` | +0.32 | +0.32 | +1.02 | — | `ts_regbeta(day_gini(Volume), day_kurt(Close), 50)` |
| window | `ts_regbeta@50->25` | +0.04 | +0.25 | +0.04 | — | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 25)` |
| window | `ts_regbeta@50->100` | +0.54 | +0.54 | +1.52 | — | `ts_regbeta(day_gini(Volume), day_kurt(Vwap), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `div(cs_robust_z(day_mean(Low)), day_first(Open))` — enrichment,均值差 +1.17,p 0.000
2. `cs_robust_z(day_mean(Low))` — enrichment,均值差 +1.14,p 0.000
3. `log(div(cs_robust_z(day_mean(Low)), day_first(Open)))` — enrichment,均值差 +1.12,p 0.000
4. `day_mean(Low)` — enrichment,均值差 +0.98,p 0.000
5. `day_topw_mean(Amt, Amt)` — enrichment,均值差 +0.97,p 0.012
6. `sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(cs_robust_z(day_mean(Low)), day_first(Open))))` — enrichment,均值差 +0.92,p 0.033
7. `abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30))` — enrichment,均值差 +0.79,p 0.014
8. `abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40))` — enrichment,均值差 +0.77,p 0.015
9. `pow_05(abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)))` — enrichment,均值差 +0.77,p 0.023
10. `pow_05(abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)))` — enrichment,均值差 +0.73,p 0.063
11. `day_gini(Volume)` — enrichment,均值差 +0.59,p 0.004
12. `cross_zscore(day_topw_mean(Ret, Amt), 60)` — enrichment,均值差 +0.58,p 0.015
13. `ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)` — enrichment,均值差 +0.58,p 0.003
14. `cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15)` — enrichment,均值差 +0.54,p 0.066
15. `ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)` — enrichment,均值差 +0.50,p 0.001
16. `pow_05(cross_ema(day_sum(Ret), 241))` — enrichment,均值差 +0.44,p 0.072
17. `day_first(Open)` — enrichment,均值差 +0.34,p 0.008
18. `day_kurt(Open)` — enrichment,均值差 +0.34,p 0.054
19. `day_topw_mean(Ret, Amt)` — enrichment,均值差 +0.34,p 0.008
20. `day_last(Close)` — enrichment,均值差 +0.27,p 0.052
21. `ts_delay(day_last(Close), 1)` — enrichment,均值差 +0.26,p 0.091

## 本组之前各轮的任务

- `prods904Pr1a_Ea`:核心 `day_topw_mean(Ret, Amt)`;评分 65,过线 0,入 heads 0;采样计数 {'c05_no_core': 868, 'c05_periphery_seen': 2}
  - score +0.17(train +0.17 valid +0.86):`cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15), 15)`
  - score +0.12(train +0.12 valid +0.83):`cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15), 10)`
  - score +0.09(train +0.09 valid +1.08):`cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 30)`
  - score +0.05(train +0.05 valid +1.15):`cross_ema(cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 60), 15), 15), 15)`
  - score +0.02(train +0.02 valid +2.36):`cross_ema(cross_ema(cross_zscore(day_topw_mean(Ret, Amt), 10), 15), 15)`
- `prods904Pr1b_Nb`:核心 `—`;评分 99,过线 0,入 heads 0;采样计数 {}
  - score +0.29(train +0.29 valid +0.65):`cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), abs_(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60)`
  - score -0.01(train -0.01 valid +0.73):`log(div(cs_robust_z(day_mean(Low)), day_first(Open)))`
  - score -0.16(train -0.16 valid +0.10):`cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 10))), log(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60)`
  - score -0.21(train -0.21 valid +0.06):`cross_mean(cs_winsor(sub(log(div(day_min(Open), ts_delay(day_last(Close), 1))), log(cs_winsor(sub(log(div(day_min(Open), ts_delay(day_last(Close), 1))), log(div(cs_robust_z(day_mean(Low)), day_first(Open)))))))), 60)`
  - score -0.21(train -0.21 valid -0.02):`cross_mean(cs_winsor(sub(log(div(day_first(Open), ts_delay(day_last(Close), 1))), log(div(cs_robust_z(day_mean(Low)), day_first(Open))))), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
