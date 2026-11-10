# 定位:种子 2016,P 组,第 3 轮(只含 train / valid)

快照:prods2016M1_I0_open_search, prods2016M2_I0_open_search, prods2016M3_I0_open_search, prods2016Pr1b_Nb, prods2016Pr2a_Ea, prods2016Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.17 | -1.17 | -0.09 | +1 | 5 | prods2016M3_I0_open_search | `pow_2(ts_max(day_hurst(Low), 30))` |
| -1.30 | -1.27 | -1.30 | +1 | 20 | prods2016M1_I0_open_search | `cross_reg_tvalue(day_quantile_q25(Open), day_kurt(Volume), 30)` |
| -1.39 | -1.39 | -0.63 | -1 | 20 | prods2016M3_I0_open_search | `cross_med(ts_max(cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15), 5), 60)` |
| -1.54 | -1.54 | -0.48 | -1 | 20 | prods2016M3_I0_open_search | `ts_max(day_hurst(Vwap), 50)` |
| -2.35 | -1.59 | -2.35 | +1 | 20 | prods2016M1_I0_open_search | `sub(day_kurt(Ret), day_quantile_q25(Open))` |
| -2.39 | -1.59 | -2.39 | -1 | 5 | prods2016M2_I0_open_search | `pow_05(day_close(Close))` |
| -2.39 | -1.60 | -2.39 | -1 | 5 | prods2016M2_I0_open_search | `pow_05(day_close(Vwap))` |
| -2.42 | -1.61 | -2.42 | -1 | 5 | prods2016M1_I0_open_search | `abs_(day_quantile_q25(Open))` |
| -2.74 | -2.08 | -2.74 | +1 | 20 | prods2016M2_I0_open_search | `pow_2(pow_05(pow_05(ts_quantile_q50(inv(pow_05(day_close(Amt))), 40))))` |

## 共性:223 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.32 | 0.000 | 6 | -0.24 / -2.56 | `cs_last_low10(cross_mean(sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60), sub(LogFloatCap, LogFloatShares))` |
| +2.06 | 0.000 | 10 | -0.53 / -2.59 | `sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60))` |
| +2.03 | 0.000 | 9 | -0.55 / -2.58 | `cross_mean(sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60)` |
| +1.91 | 0.000 | 18 | -0.74 / -2.65 | `sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret))` |
| +1.83 | 0.000 | 16 | -0.80 / -2.63 | `cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)` |
| +1.51 | 0.000 | 24 | -1.14 / -2.66 | `ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5)` |
| +1.49 | 0.000 | 26 | -1.18 / -2.67 | `day_pos_ratio(Volume)` |
| +1.13 | 0.000 | 38 | -1.56 / -2.69 | `sub(LogFloatCap, LogFloatShares)` |
| +0.92 | 0.023 | 5 | -1.60 / -2.52 | `div(day_es_ratio_hi(Open), ListAge)` |
| +0.84 | 0.000 | 79 | -1.95 / -2.80 | `sub(day_topw_mean(Ret, Amt), day_mean(Ret))` |
| +0.82 | 0.000 | 80 | -1.97 / -2.79 | `day_topw_mean(Ret, Amt)` |
| +0.78 | 0.016 | 7 | -1.75 / -2.52 | `day_first(Close)` |
| +0.72 | 0.041 | 6 | -1.80 / -2.52 | `day_signed_ratio(sub(Close, day_first(Open)), Close)` |
| +0.69 | 0.000 | 87 | -2.07 / -2.77 | `day_mean(Ret)` |
| +0.68 | 0.001 | 25 | -1.89 / -2.57 | `cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 60)` |
| +0.67 | 0.041 | 6 | -1.85 / -2.51 | `day_signed_ratio(sub(Close, day_first(Close)), Amt)` |
| +0.51 | 0.111 | 10 | -2.01 / -2.52 | `day_es_ratio_hi(Open)` |
| +0.44 | 0.171 | 7 | -2.07 / -2.51 | `cs_last_low10(cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 60), sub(LogFloatCap, LogFloatShares))` |
| +0.41 | 0.145 | 8 | -2.10 / -2.51 | `div(day_last(Close), day_first(Open))` |
| +0.35 | 0.075 | 31 | -2.20 / -2.54 | `day_first(Open)` |

## 拆解(22 次评估)

### head score -1.17:`pow_2(ts_max(day_hurst(Low), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(day_hurst(Low), 30)` | -1.16 | -1.16 | -0.09 | — | (子树本身) |
| sufficiency | `day_hurst(Low)` | -5.19 | -5.19 | -5.08 | — | (子树本身) |
| knockout | `ts_max(day_hurst(Low), 30)` | -5.19 | -5.19 | -5.08 | +4.03 | `pow_2(day_hurst(Low))` |
| swap | `Low->High` | -0.94 | -0.94 | -0.33 | — | `pow_2(ts_max(day_hurst(High), 30))` |
| window | `ts_max@30->15` | -2.02 | -2.02 | -0.62 | — | `pow_2(ts_max(day_hurst(Low), 15))` |
| window | `ts_max@30->60` | +0.10 | +0.10 | +0.30 | — | `pow_2(ts_max(day_hurst(Low), 60))` |

### head score -1.39:`cross_med(ts_max(cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15), 5), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15), 5)` | -2.41 | -1.87 | -2.41 | — | (子树本身) |
| sufficiency | `cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15)` | -2.36 | -1.77 | -2.36 | — | (子树本身) |
| sufficiency | `ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5)` | -2.48 | -1.80 | -2.48 | — | (子树本身) |
| sufficiency | `cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60)` | -2.48 | -1.85 | -2.48 | — | (子树本身) |
| knockout | `ts_max(cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15), 5)` | -1.60 | -1.60 | -0.78 | +0.21 | `cross_med(cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15), 60)` |
| knockout | `cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15)` | -1.75 | -1.75 | -0.65 | +0.35 | `cross_med(ts_max(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 5), 60)` |
| knockout | `ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5)` | -1.58 | -1.58 | -0.75 | +0.19 | `cross_med(ts_max(cross_med(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 15), 5), 60)` |
| knockout | `cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60)` | -1.86 | -1.86 | -1.49 | +0.47 | `cross_med(ts_max(cross_med(ts_max(ts_cov(day_hurst(Open), day_quantile(Close), 50), 5), 15), 5), 60)` |
| swap | `Open->Close` | -1.33 | -1.33 | -0.58 | — | `cross_med(ts_max(cross_med(ts_max(cross_med(ts_cov(day_hurst(Close), day_quantile(Close), 50), 60), 5), 15), 5), 60)` |
| swap | `Close->Vwap` | -1.40 | -1.40 | -0.69 | — | `cross_med(ts_max(cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Vwap), 50), 60), 5), 15), 5), 60)` |
| window | `cross_med@60->30` | -2.72 | -1.73 | -2.72 | — | `cross_med(ts_max(cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15), 5), 30)` |
| window | `cross_med@60->120` | -1.39 | -1.39 | -0.85 | — | `cross_med(ts_max(cross_med(ts_max(cross_med(ts_cov(day_hurst(Open), day_quantile(Close), 50), 60), 5), 15), 5), 120)` |

### head score -1.54:`ts_max(day_hurst(Vwap), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_hurst(Vwap)` | — | — | — | — | 门槛废品 |
| swap | `Vwap->Close` | -0.03 | -0.03 | +0.17 | — | `ts_max(day_hurst(Close), 50)` |
| window | `ts_max@50->25` | -2.46 | -1.27 | -2.46 | — | `ts_max(day_hurst(Vwap), 25)` |
| window | `ts_max@50->100` | -1.74 | -1.74 | -0.61 | — | `ts_max(day_hurst(Vwap), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_last_low10(cross_mean(sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60), sub(LogFloatCap, LogFloatShares))` — enrichment,均值差 +2.32,p 0.000
2. `sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60))` — enrichment,均值差 +2.06,p 0.000
3. `cross_mean(sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60)` — enrichment,均值差 +2.03,p 0.000
4. `sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret))` — enrichment,均值差 +1.91,p 0.000
5. `cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)` — enrichment,均值差 +1.83,p 0.000
6. `ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5)` — enrichment,均值差 +1.51,p 0.000
7. `day_pos_ratio(Volume)` — enrichment,均值差 +1.49,p 0.000
8. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +1.13,p 0.000
9. `div(day_es_ratio_hi(Open), ListAge)` — enrichment,均值差 +0.92,p 0.023
10. `sub(day_topw_mean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +0.84,p 0.000
11. `day_topw_mean(Ret, Amt)` — enrichment,均值差 +0.82,p 0.000
12. `day_first(Close)` — enrichment,均值差 +0.78,p 0.016
13. `day_signed_ratio(sub(Close, day_first(Open)), Close)` — enrichment,均值差 +0.72,p 0.041
14. `day_mean(Ret)` — enrichment,均值差 +0.69,p 0.000
15. `cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 60)` — enrichment,均值差 +0.68,p 0.001
16. `day_signed_ratio(sub(Close, day_first(Close)), Amt)` — enrichment,均值差 +0.67,p 0.041
17. `day_first(Open)` — enrichment,均值差 +0.35,p 0.075

## 本组之前各轮的任务

- `prods2016Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.71(train -0.71 valid -0.46):`cross_mean(day_wmean(Ret, Ret), 60)`
  - score -0.71(train -0.71 valid -0.70):`cross_corr(cross_mean(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), 60), sub(div(day_last(Close), cross_delay(day_last(Close), 1)), 1), 60)`
  - score -1.14(train -1.14 valid -0.31):`cross_mean(sub(day_signed_ratio(sub(Close, day_first(Close)), Ret), day_signed_ratio(sub(Close, day_first(Ret)), Close)), 241)`
  - score -1.14(train -1.14 valid -0.61):`cross_mean(sub(day_signed_ratio(sub(Close, day_first(Open)), Amt), day_signed_ratio(sub(Close, day_first(Ret)), Close)), 241)`
  - score -1.14(train -1.14 valid -0.61):`cross_mean(sub(day_signed_ratio(sub(Close, day_first(Close)), Amt), day_signed_ratio(sub(Close, day_first(Ret)), Close)), 241)`
- `prods2016Pr2a_Ea`:核心 `sub(day_topw_mean(Ret, Amt), day_mean(Ret))`;评分 100,过线 0,入 heads 0;采样计数 {'c05_no_core': 1005, 'c05_skeleton': 494, 'c05_periphery_seen': 6}
  - score +0.16(train +0.20 valid +0.16):`cs_last_high05(cs_last_low10(cross_mean(sub(day_flat_ratio(Low), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60), sub(LogFloatCap, LogFloatShares)), day_flat_ratio(Low))`
  - score -0.04(train +0.20 valid -0.04):`cs_last_high05(cs_last_low10(cross_mean(sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60), sub(LogFloatCap, LogFloatShares)), day_topw_mean(Ret, Amt))`
  - score -0.12(train -0.12 valid -0.08):`cs_last_high05(cs_last_low10(cross_mean(sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 15)), 60), sub(LogFloatCap, LogFloatShares)), day_topw_mean(Ret, Amt))`
  - score -0.14(train +0.15 valid -0.14):`cs_last_high05(cs_last_low10(cross_mean(sub(day_topw_mean(Ret, Volume), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60), sub(LogFloatCap, LogFloatShares)), day_topw_mean(Ret, Volume))`
  - score -0.20(train -0.20 valid -0.06):`cs_last_high05(cs_last_low10(cross_mean(sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(cs_last_low10(cross_mean(sub(day_topw_mean(Ret, Amt), cross_mean(sub(ts_regbeta(sub(day_topw_mean(Ret, Amt), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60), sub(LogFloatCap, LogFloatShares)), day_mean(Ret)), day_pos_ratio(Volume), 5), day_mean(Ret)), 60)), 60), sub(LogFloatCap, LogFloatShares)), day_topw_mean(Ret, Amt))`
- `prods2016Pr2b_Nb`:核心 `—`;评分 60,过线 0,入 heads 0;采样计数 {}
  - score -1.10(train -1.10 valid -0.70):`div(div(day_es_ratio_hi(Open), ListAge), ListAge)`
  - score -1.10(train -1.10 valid -0.70):`div(div(day_es_ratio_hi(Open), div(day_es_ratio_hi(Open), ListAge)), div(day_es_ratio_hi(Open), ListAge))`
  - score -1.10(train -1.10 valid -0.70):`div(day_es_ratio_hi(Open), ListAge)`
  - score -1.10(train -1.10 valid -0.70):`div(div(div(day_es_ratio_hi(Open), ListAge), ListAge), ListAge)`
  - score -1.26(train -1.26 valid -1.22):`cross_mean(sub(sub(div(day_last(Close), day_first(Open)), 1), sub(div(day_first(Open), cross_delay(day_last(Close), 1)), 1)), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.27(window ts_max@30->60):`pow_2(ts_max(day_hurst(Low), 60))`
- 增益 +0.23(swap Low->High):`pow_2(ts_max(day_hurst(High), 30))`
