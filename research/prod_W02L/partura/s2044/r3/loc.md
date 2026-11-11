# 定位:种子 2044,P 组,第 3 轮(只含 train / valid)

快照:prods2044M1_I0_open_search, prods2044M2_I0_open_search, prods2044M3_I0_open_search, prods2044Pr1a_Ea, prods2044Pr1b_Nb, prods2044Pr2a_Ea, prods2044Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.61 | +0.61 | +0.93 | +1 | 5 | prods2044M1_I0_open_search | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` |
| +0.58 | +0.59 | +0.58 | +1 | 5 | prods2044M1_I0_open_search | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` |
| -0.45 | -0.45 | -0.38 | +1 | 0 | prods2044M3_I0_open_search | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)` |
| -0.84 | -0.84 | -0.57 | +1 | 20 | prods2044M1_I0_open_search | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` |
| -1.20 | -0.19 | -1.20 | -1 | 5 | prods2044M2_I0_open_search | `ts_min(ts_regres(day_corr(Close, High), ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50), 30), 50)` |
| -1.59 | -1.19 | -1.59 | -1 | 20 | prods2044M2_I0_open_search | `cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50), 241)` |
| -1.68 | -0.63 | -1.68 | -1 | 5 | prods2044M2_I0_open_search | `ts_min(ts_regres(day_corr(Close, Ret), day_durbin_watson(Ret), 40), 50)` |
| -1.97 | -1.18 | -1.97 | +1 | 5 | prods2044M3_I0_open_search | `ts_max(ts_std(day_corr(Ret, Ret), 40), 40)` |
| -2.06 | -1.98 | -2.06 | +1 | 5 | prods2044M3_I0_open_search | `ts_min(ts_std(day_corr(Ret, Volume), 40), 5)` |

## 共性:231 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.12 | 0.006 | 6 | -1.36 / -2.48 | `cs_demean(day_std(Ret))` |
| +1.12 | 0.006 | 6 | -1.36 / -2.48 | `day_std(Ret)` |
| +1.01 | 0.018 | 5 | -1.46 / -2.47 | `cs_demean(cs_demean(day_std(Ret)))` |
| +0.95 | 0.000 | 25 | -1.60 / -2.55 | `cs_demean(day_corr(Ret, Volume))` |
| +0.87 | 0.013 | 8 | -1.61 / -2.48 | `ts_delay(cs_demean(day_corr(Ret, Volume)), 1)` |
| +0.87 | 0.013 | 8 | -1.61 / -2.48 | `cs_demean(ts_delay(cs_demean(day_corr(Ret, Volume)), 1))` |
| +0.82 | 0.023 | 7 | -1.65 / -2.47 | `cross_ema(cs_demean(day_corr(Ret, Volume)), 120)` |
| +0.66 | 0.028 | 12 | -1.82 / -2.48 | `cs_demean(ts_delay(day_corr(Ret, Volume), 1))` |
| +0.56 | 0.178 | 4 | -1.90 / -2.46 | `ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40)` |
| +0.53 | 0.122 | 7 | -1.94 / -2.47 | `day_corr(Close, Volume)` |
| +0.51 | 0.225 | 4 | -1.94 / -2.46 | `cs_demean(cross_ema(cross_ema(cs_demean(day_corr(Ret, Volume)), 120), 120))` |
| +0.51 | 0.225 | 4 | -1.94 / -2.46 | `cross_ema(cross_ema(cs_demean(day_corr(Ret, Volume)), 120), 120)` |
| +0.50 | 0.052 | 17 | -1.98 / -2.49 | `ts_delay(day_corr(Ret, Volume), 1)` |
| +0.49 | 0.128 | 13 | -1.99 / -2.48 | `day_quantile_q25(Open)` |
| +0.41 | 0.000 | 70 | -2.17 / -2.57 | `day_corr(Ret, Volume)` |
| +0.28 | 0.345 | 6 | -2.18 / -2.46 | `cs_demean(day_sum(Ret))` |
| +0.19 | 0.395 | 29 | -2.28 / -2.47 | `day_sum(Ret)` |
| +0.17 | 0.275 | 5 | -2.28 / -2.45 | `day_es_ratio_hi(Amt)` |
| +0.17 | 0.381 | 10 | -2.29 / -2.46 | `ts_delay(day_signed_ratio(Ret, Amt), 1)` |
| -0.03 | 0.459 | 12 | -2.48 / -2.45 | `day_durbin_watson(Ret)` |

## 拆解(28 次评估)

### head score -0.45:`cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(day_corr(Ret, Volume), 40)` | -2.14 | -1.69 | -2.14 | — | (子树本身) |
| sufficiency | `day_corr(Ret, Volume)` | -3.39 | -3.39 | -2.98 | — | (子树本身) |
| knockout | `ts_std(day_corr(Ret, Volume), 40)` | -0.59 | -0.59 | -0.22 | +0.14 | `cross_fangzheng(day_corr(Ret, Volume), 241)` |
| swap | `Volume->Amt` | -0.46 | -0.46 | -0.43 | — | `cross_fangzheng(ts_std(day_corr(Ret, Amt), 40), 241)` |
| window | `cross_fangzheng@241->120` | -1.15 | -0.88 | -1.15 | — | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 120)` |
| window | `cross_fangzheng@241->482` | -0.75 | -0.43 | -0.75 | — | `cross_fangzheng(ts_std(day_corr(Ret, Volume), 40), 482)` |

### head score -1.59:`cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50)` | -1.65 | -0.60 | -1.65 | — | (子树本身) |
| sufficiency | `ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40)` | -5.33 | -3.99 | -5.33 | — | (子树本身) |
| sufficiency | `day_corr(Close, High)` | -2.70 | -2.70 | -1.80 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Ret)` | -3.54 | -3.54 | -3.41 | — | (子树本身) |
| knockout | `ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50)` | -2.78 | -1.54 | -2.78 | +1.19 | `cross_sum(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 241)` |
| knockout | `ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40)` | -1.76 | -1.76 | -1.15 | +0.17 | `cross_sum(ts_min(day_corr(Close, High), 50), 241)` |
| swap | `Close->Vwap` | -1.47 | -1.05 | -1.47 | — | `cross_sum(ts_min(ts_regres(day_corr(Vwap, High), day_durbin_watson(Ret), 40), 50), 241)` |
| swap | `High->Low` | -1.37 | -0.94 | -1.37 | — | `cross_sum(ts_min(ts_regres(day_corr(Close, Low), day_durbin_watson(Ret), 40), 50), 241)` |
| window | `cross_sum@241->120` | -2.32 | -1.43 | -2.32 | — | `cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50), 120)` |
| window | `cross_sum@241->482` | -1.18 | -1.18 | -0.63 | — | `cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50), 482)` |

### head score -1.68:`ts_min(ts_regres(day_corr(Close, Ret), day_durbin_watson(Ret), 40), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_regres(day_corr(Close, Ret), day_durbin_watson(Ret), 40)` | -5.65 | -4.06 | -5.65 | — | (子树本身) |
| sufficiency | `day_corr(Close, Ret)` | -2.97 | -2.46 | -2.97 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Ret)` | -3.54 | -3.54 | -3.41 | — | (子树本身) |
| knockout | `ts_regres(day_corr(Close, Ret), day_durbin_watson(Ret), 40)` | -2.05 | -1.88 | -2.05 | +0.37 | `ts_min(day_corr(Close, Ret), 50)` |
| swap | `Close->Vwap` | -1.74 | -0.87 | -1.74 | — | `ts_min(ts_regres(day_corr(Vwap, Ret), day_durbin_watson(Ret), 40), 50)` |
| window | `ts_min@50->25` | -1.78 | -0.96 | -1.78 | — | `ts_min(ts_regres(day_corr(Close, Ret), day_durbin_watson(Ret), 40), 25)` |
| window | `ts_min@50->100` | -2.07 | -0.94 | -2.07 | — | `ts_min(ts_regres(day_corr(Close, Ret), day_durbin_watson(Ret), 40), 100)` |

### head score -1.97:`ts_max(ts_std(day_corr(Ret, Ret), 40), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(day_corr(Ret, Ret), 40)` | -3.97 | -2.54 | -3.97 | — | (子树本身) |
| sufficiency | `day_corr(Ret, Ret)` | — | — | — | — | 门槛废品 |
| knockout | `ts_std(day_corr(Ret, Ret), 40)` | — | — | — | — | `ts_max(day_corr(Ret, Ret), 40)` |
| window | `ts_max@40->20` | -3.28 | -1.56 | -3.28 | — | `ts_max(ts_std(day_corr(Ret, Ret), 40), 20)` |
| window | `ts_max@40->80` | -0.92 | -0.28 | -0.92 | — | `ts_max(ts_std(day_corr(Ret, Ret), 40), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_demean(day_std(Ret))` — enrichment,均值差 +1.12,p 0.006
2. `day_std(Ret)` — enrichment,均值差 +1.12,p 0.006
3. `cs_demean(cs_demean(day_std(Ret)))` — enrichment,均值差 +1.01,p 0.018
4. `cs_demean(day_corr(Ret, Volume))` — enrichment,均值差 +0.95,p 0.000
5. `ts_delay(cs_demean(day_corr(Ret, Volume)), 1)` — enrichment,均值差 +0.87,p 0.013
6. `cs_demean(ts_delay(cs_demean(day_corr(Ret, Volume)), 1))` — enrichment,均值差 +0.87,p 0.013
7. `cross_ema(cs_demean(day_corr(Ret, Volume)), 120)` — enrichment,均值差 +0.82,p 0.023
8. `cs_demean(ts_delay(day_corr(Ret, Volume), 1))` — enrichment,均值差 +0.66,p 0.028
9. `ts_delay(day_corr(Ret, Volume), 1)` — enrichment,均值差 +0.50,p 0.052
10. `day_corr(Ret, Volume)` — enrichment,均值差 +0.41,p 0.000

## 本组之前各轮的任务

- `prods2044Pr1a_Ea`:核心 `day_corr(Ret, Volume)`;评分 84,过线 0,入 heads 0;采样计数 {'c05_no_core': 1397, 'c05_skeleton': 712}
  - score -0.86(train -0.32 valid -0.86):`cross_regbeta(cs_demean(ts_delay(day_corr(Ret, Volume), 1)), cs_demean(cs_demean(day_std(Ret))), 120)`
  - score -0.86(train -0.32 valid -0.86):`cross_regbeta(cs_demean(ts_delay(cs_demean(day_corr(Ret, Volume)), 1)), cs_demean(day_std(Ret)), 120)`
  - score -1.07(train -1.07 valid -0.63):`cross_ema(cs_demean(day_corr(Ret, Volume)), 120)`
  - score -1.07(train -1.07 valid -0.63):`cross_ema(cs_demean(cs_demean(day_corr(Ret, Volume))), 120)`
  - score -1.08(train -1.08 valid -0.68):`cross_ema(cross_ema(cs_demean(day_corr(Ret, Volume)), 120), 120)`
- `prods2044Pr1b_Nb`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.00(train +0.14 valid -0.00):`cs_last_low10(day_es_ratio_hi(Amt), day_quantile_q25(Open))`
  - score -1.15(train -1.15 valid -0.89):`cs_last_low10(day_es_ratio_hi(Ret), day_quantile_q25(Open))`
  - score -1.16(train -1.16 valid -0.55):`cross_regbeta(ts_delay(cross_autocorr(day_es_ratio_hi(Open), 120, 1), 1), day_sum(Ret), 120)`
  - score -1.28(train -1.09 valid -1.28):`cross_autocorr(day_es_ratio_hi(Amt), 120, 1)`
  - score -1.31(train -1.14 valid -1.31):`cross_regbeta(ts_delay(cross_autocorr(cross_autocorr(day_signed_ratio(Ret, Amt), 120, 1), 120, 1), 1), day_sum(Ret), 120)`
- `prods2044Pr2a_Ea`:核心 `ts_max(cs_demean(day_corr(Ret, Volume)), 120)`;评分 49,过线 0,入 heads 0;采样计数 {'c05_no_core': 5658, 'c05_skeleton': 3652}
  - score -2.31(train -2.31 valid -2.24):`day_q_stat_std(Amt)`
  - score -2.99(train -2.42 valid -2.99):`day_es_ratio_hi(High)`
  - score -3.18(train -3.18 valid -2.66):`day_hurst(Amt)`
  - score -4.05(train -3.60 valid -4.05):`day_kurt(Open)`
  - score -4.09(train -4.09 valid -3.53):`day_centroid(Open)`
- `prods2044Pr2b_Nb`:核心 `—`;评分 71,过线 0,入 heads 0;采样计数 {'c05_skeleton': 11}
  - score -0.14(train +0.30 valid -0.14):`day_kurt(cross_regres(cross_regres(High, Amt, 30), Amt, 60))`
  - score -0.34(train +0.35 valid -0.34):`day_kurt(cross_regres(cross_regres(High, Amt, 60), Amt, 60))`
  - score -0.35(train +0.42 valid -0.35):`day_kurt(cross_regres(cross_regres(Low, Amt, 60), Amt, 60))`
  - score -0.42(train +0.37 valid -0.42):`day_kurt(cross_regres(cross_regres(High, Volume, 60), Volume, 60))`
  - score -0.55(train +0.12 valid -0.55):`day_kurt(cross_regres(cross_regres(High, cross_regres(cross_regres(High, Amt, 60), Amt, 60), 60), cross_regres(cross_regres(High, Amt, 60), Amt, 60), 60))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.04(window ts_max@40->80):`ts_max(ts_std(day_corr(Ret, Ret), 40), 80)`
- 增益 +0.41(window cross_sum@241->482):`cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50), 482)`
- 增益 +0.22(swap High->Low):`cross_sum(ts_min(ts_regres(day_corr(Close, Low), day_durbin_watson(Ret), 40), 50), 241)`
- 增益 +0.12(swap Close->Vwap):`cross_sum(ts_min(ts_regres(day_corr(Vwap, High), day_durbin_watson(Ret), 40), 50), 241)`
