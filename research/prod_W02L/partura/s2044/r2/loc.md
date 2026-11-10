# 定位:种子 2044,P 组,第 2 轮(只含 train / valid)

快照:prods2044M1_I0_open_search, prods2044M2_I0_open_search, prods2044Pr1a_Ea, prods2044Pr1b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.61 | +0.61 | +0.93 | +1 | 5 | prods2044M1_I0_open_search | `ts_max(cs_demean(day_corr(Ret, Volume)), 120)` |
| +0.58 | +0.59 | +0.58 | +1 | 5 | prods2044M1_I0_open_search | `ts_max(ts_max(day_corr(Ret, Amt), 40), 120)` |
| -0.84 | -0.84 | -0.57 | +1 | 20 | prods2044M1_I0_open_search | `log(neg(cross_med(day_corr(Vwap, Amt), 241)))` |
| -1.20 | -0.19 | -1.20 | -1 | 5 | prods2044M2_I0_open_search | `ts_min(ts_regres(day_corr(Close, High), ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50), 30), 50)` |
| -1.59 | -1.19 | -1.59 | -1 | 20 | prods2044M2_I0_open_search | `cross_sum(ts_min(ts_regres(day_corr(Close, High), day_durbin_watson(Ret), 40), 50), 241)` |
| -1.68 | -0.63 | -1.68 | -1 | 5 | prods2044M2_I0_open_search | `ts_min(ts_regres(day_corr(Close, Ret), day_durbin_watson(Ret), 40), 50)` |

## 共性:180 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.15 | 0.003 | 6 | -1.36 / -2.50 | `day_std(Ret)` |
| +1.15 | 0.003 | 6 | -1.36 / -2.50 | `cs_demean(day_std(Ret))` |
| +1.04 | 0.013 | 5 | -1.46 / -2.49 | `cs_demean(cs_demean(day_std(Ret)))` |
| +1.00 | 0.000 | 25 | -1.60 / -2.60 | `cs_demean(day_corr(Ret, Volume))` |
| +0.90 | 0.008 | 8 | -1.61 / -2.51 | `ts_delay(cs_demean(day_corr(Ret, Volume)), 1)` |
| +0.90 | 0.008 | 8 | -1.61 / -2.51 | `cs_demean(ts_delay(cs_demean(day_corr(Ret, Volume)), 1))` |
| +0.84 | 0.015 | 7 | -1.65 / -2.50 | `cross_ema(cs_demean(day_corr(Ret, Volume)), 120)` |
| +0.69 | 0.020 | 12 | -1.82 / -2.51 | `cs_demean(ts_delay(day_corr(Ret, Volume), 1))` |
| +0.57 | 0.170 | 4 | -1.90 / -2.48 | `ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40)` |
| +0.55 | 0.114 | 7 | -1.94 / -2.49 | `day_corr(Close, Volume)` |
| +0.53 | 0.041 | 17 | -1.98 / -2.52 | `ts_delay(day_corr(Ret, Volume), 1)` |
| +0.53 | 0.216 | 4 | -1.94 / -2.48 | `cs_demean(cross_ema(cross_ema(cs_demean(day_corr(Ret, Volume)), 120), 120))` |
| +0.53 | 0.216 | 4 | -1.94 / -2.48 | `cross_ema(cross_ema(cs_demean(day_corr(Ret, Volume)), 120), 120)` |
| +0.52 | 0.121 | 13 | -1.99 / -2.50 | `day_quantile_q25(Open)` |
| +0.43 | 0.000 | 67 | -2.19 / -2.63 | `day_corr(Ret, Volume)` |
| +0.30 | 0.350 | 6 | -2.18 / -2.48 | `cs_demean(day_sum(Ret))` |
| +0.22 | 0.393 | 29 | -2.28 / -2.50 | `day_sum(Ret)` |
| +0.19 | 0.257 | 5 | -2.28 / -2.47 | `day_es_ratio_hi(Amt)` |
| +0.19 | 0.367 | 10 | -2.29 / -2.48 | `ts_delay(day_signed_ratio(Ret, Amt), 1)` |
| -0.01 | 0.435 | 12 | -2.48 / -2.46 | `day_durbin_watson(Ret)` |

## 拆解(32 次评估)

### head score +0.61:`ts_max(cs_demean(day_corr(Ret, Volume)), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_demean(day_corr(Ret, Volume))` | -3.39 | -3.39 | -2.98 | — | (子树本身) |
| sufficiency | `day_corr(Ret, Volume)` | -3.39 | -3.39 | -2.98 | — | (子树本身) |
| knockout | `cs_demean(day_corr(Ret, Volume))` | +0.51 | +0.67 | +0.51 | +0.10 | `ts_max(day_corr(Ret, Volume), 120)` |
| swap | `Volume->Amt` | +0.58 | +0.58 | +0.75 | — | `ts_max(cs_demean(day_corr(Ret, Amt)), 120)` |
| window | `ts_max@120->60` | -0.00 | -0.00 | +0.52 | — | `ts_max(cs_demean(day_corr(Ret, Volume)), 60)` |
| window | `ts_max@120->240` | +0.53 | +0.53 | +0.55 | — | `ts_max(cs_demean(day_corr(Ret, Volume)), 240)` |

### head score +0.58:`ts_max(ts_max(day_corr(Ret, Amt), 40), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(day_corr(Ret, Amt), 40)` | -0.27 | -0.27 | +0.41 | — | (子树本身) |
| sufficiency | `day_corr(Ret, Amt)` | -3.37 | -3.37 | -2.97 | — | (子树本身) |
| knockout | `ts_max(day_corr(Ret, Amt), 40)` | +0.53 | +0.64 | +0.53 | +0.06 | `ts_max(day_corr(Ret, Amt), 120)` |
| swap | `Amt->Volume` | +0.54 | +0.54 | +0.54 | — | `ts_max(ts_max(day_corr(Ret, Volume), 40), 120)` |
| window | `ts_max@120->60` | +0.58 | +0.63 | +0.58 | — | `ts_max(ts_max(day_corr(Ret, Amt), 40), 60)` |
| window | `ts_max@120->240` | +0.37 | +0.37 | +0.61 | — | `ts_max(ts_max(day_corr(Ret, Amt), 40), 240)` |

### head score -0.84:`log(neg(cross_med(day_corr(Vwap, Amt), 241)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_med(day_corr(Vwap, Amt), 241))` | -1.09 | -1.09 | -0.69 | — | (子树本身) |
| sufficiency | `cross_med(day_corr(Vwap, Amt), 241)` | -1.09 | -1.09 | -0.69 | — | (子树本身) |
| sufficiency | `day_corr(Vwap, Amt)` | -4.35 | -4.35 | -3.06 | — | (子树本身) |
| knockout | `neg(cross_med(day_corr(Vwap, Amt), 241))` | -0.84 | -0.84 | -0.57 | -0.00 | `log(cross_med(day_corr(Vwap, Amt), 241))` |
| knockout | `cross_med(day_corr(Vwap, Amt), 241)` | -3.79 | -3.79 | -1.99 | +2.95 | `log(neg(day_corr(Vwap, Amt)))` |
| swap | `Vwap->Close` | -0.91 | -0.91 | -0.85 | — | `log(neg(cross_med(day_corr(Close, Amt), 241)))` |
| swap | `Amt->Volume` | -0.82 | -0.82 | -0.75 | — | `log(neg(cross_med(day_corr(Vwap, Volume), 241)))` |
| window | `cross_med@241->120` | -1.17 | -1.17 | -0.95 | — | `log(neg(cross_med(day_corr(Vwap, Amt), 120)))` |
| window | `cross_med@241->482` | -1.46 | -1.46 | -0.42 | — | `log(neg(cross_med(day_corr(Vwap, Amt), 482)))` |

### head score -1.20:`ts_min(ts_regres(day_corr(Close, High), ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50), 30), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_regres(day_corr(Close, High), ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50), 30)` | -1.87 | -1.87 | -1.43 | — | (子树本身) |
| sufficiency | `ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50)` | -1.68 | -0.51 | -1.68 | — | (子树本身) |
| sufficiency | `ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40)` | -5.55 | -3.39 | -5.55 | — | (子树本身) |
| sufficiency | `day_corr(Close, High)` | -2.70 | -2.70 | -1.80 | — | (子树本身) |
| knockout | `ts_regres(day_corr(Close, High), ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50), 30)` | -2.46 | -2.46 | -1.94 | +1.25 | `ts_min(day_corr(Close, High), 50)` |
| knockout | `ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50)` | -1.38 | -0.61 | -1.38 | +0.17 | `ts_min(ts_regres(day_corr(Close, High), ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 30), 50)` |
| knockout | `ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40)` | -2.10 | -0.19 | -2.10 | +0.90 | `ts_min(ts_regres(day_corr(Close, High), ts_min(day_corr(Close, Volume), 50), 30), 50)` |
| swap | `Close->Vwap` | -1.34 | -0.02 | -1.34 | — | `ts_min(ts_regres(day_corr(Vwap, High), ts_min(ts_regres(day_corr(Vwap, Volume), day_durbin_watson(Ret), 40), 50), 30), 50)` |
| swap | `High->Low` | -1.15 | -0.06 | -1.15 | — | `ts_min(ts_regres(day_corr(Close, Low), ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50), 30), 50)` |
| window | `ts_min@50->25` | -1.67 | -0.70 | -1.67 | — | `ts_min(ts_regres(day_corr(Close, High), ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50), 30), 25)` |
| window | `ts_min@50->100` | -1.50 | +0.44 | -1.50 | — | `ts_min(ts_regres(day_corr(Close, High), ts_min(ts_regres(day_corr(Close, Volume), day_durbin_watson(Ret), 40), 50), 30), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_std(Ret)` — enrichment,均值差 +1.15,p 0.003
2. `cs_demean(day_std(Ret))` — enrichment,均值差 +1.15,p 0.003
3. `cs_demean(cs_demean(day_std(Ret)))` — enrichment,均值差 +1.04,p 0.013
4. `cs_demean(day_corr(Ret, Volume))` — enrichment,均值差 +1.00,p 0.000
5. `ts_delay(cs_demean(day_corr(Ret, Volume)), 1)` — enrichment,均值差 +0.90,p 0.008
6. `cs_demean(ts_delay(cs_demean(day_corr(Ret, Volume)), 1))` — enrichment,均值差 +0.90,p 0.008
7. `cross_ema(cs_demean(day_corr(Ret, Volume)), 120)` — enrichment,均值差 +0.84,p 0.015
8. `cs_demean(ts_delay(day_corr(Ret, Volume), 1))` — enrichment,均值差 +0.69,p 0.020
9. `ts_delay(day_corr(Ret, Volume), 1)` — enrichment,均值差 +0.53,p 0.041
10. `day_corr(Ret, Volume)` — enrichment,均值差 +0.43,p 0.000

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

## 比原 head 好的拆解变体(R 候选)

(没有)
