# 定位:种子 2003,P 组,第 3 轮(只含 train / valid)

快照:prods2003M1_I0_open_search, prods2003M2_I0_open_search, prods2003M3_I0_open_search, prods2003Pr1a_Ea, prods2003Pr2a_Ea, prods2003Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.22 | -0.14 | -0.22 | +1 | 0 | prods2003M1_I0_open_search | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 241)` |
| -1.17 | -1.17 | +0.02 | +1 | 20 | prods2003M3_I0_open_search | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 50)` |
| -1.23 | -1.11 | -1.23 | +1 | 0 | prods2003M1_I0_open_search | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume)), 50)` |
| -1.35 | -1.35 | -0.39 | +1 | 20 | prods2003M3_I0_open_search | `ts_quantile_q75(ts_sum(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 40)` |
| -1.56 | -1.56 | -0.72 | +1 | 20 | prods2003M3_I0_open_search | `ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50)` |
| -1.57 | -1.56 | -1.57 | -1 | 0 | prods2003M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| -2.58 | -1.85 | -2.58 | -1 | 0 | prods2003M2_I0_open_search | `cross_mean(day_max(Ret), 60)` |
| -2.70 | -2.10 | -2.70 | -1 | 20 | prods2003M2_I0_open_search | `pow_2(sigmoid(sigmoid(day_max(Ret))))` |
| -2.70 | -2.10 | -2.70 | -1 | 20 | prods2003M2_I0_open_search | `pow_2(pow_2(sigmoid(sigmoid(day_max(Ret)))))` |

## 共性:176 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.29 | 0.001 | 7 | -1.11 / -2.40 | `cross_semistd_pos(sub(LogFloatCap, cs_scale(day_sum(Low))), 241)` |
| +1.08 | 0.001 | 11 | -1.33 / -2.42 | `sub(LogFloatCap, cs_scale(day_sum(Low)))` |
| +1.04 | 0.017 | 5 | -1.34 / -2.38 | `abs_(day_durbin_watson(Volume))` |
| +0.94 | 0.000 | 17 | -1.50 / -2.44 | `day_sum(Low)` |
| +0.88 | 0.001 | 16 | -1.55 / -2.43 | `cs_scale(day_sum(Low))` |
| +0.86 | 0.040 | 4 | -1.51 / -2.37 | `ts_sum(day_q_stat_std(Volume), 50)` |
| +0.73 | 0.045 | 8 | -1.65 / -2.38 | `day_autocorr_n1(Volume)` |
| +0.63 | 0.026 | 16 | -1.78 / -2.41 | `day_durbin_watson(Volume)` |
| +0.46 | 0.136 | 7 | -1.91 / -2.37 | `day_last(Volume)` |
| +0.44 | 0.097 | 6 | -1.93 / -2.36 | `pow_3(day_wstd(Close, Ret))` |
| +0.43 | 0.193 | 6 | -1.93 / -2.36 | `log(add(day_q_stat_std(Vwap), day_std(Vwap)))` |
| +0.43 | 0.193 | 6 | -1.93 / -2.36 | `add(day_q_stat_std(Vwap), day_std(Vwap))` |
| +0.42 | 0.098 | 7 | -1.95 / -2.37 | `day_wstd(Close, Ret)` |
| +0.38 | 0.241 | 5 | -1.99 / -2.36 | `cross_corr(day_q_stat_std(Vwap), abs_(day_sum(Ret)), 60)` |
| +0.35 | 0.235 | 6 | -2.01 / -2.36 | `abs_(day_sum(Ret))` |
| +0.34 | 0.243 | 6 | -2.03 / -2.36 | `div(day_last(Volume), day_max(Low))` |
| +0.33 | 0.264 | 5 | -2.03 / -2.36 | `cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 20)` |
| +0.30 | 0.249 | 9 | -2.07 / -2.37 | `day_sum(Ret)` |
| +0.28 | 0.212 | 4 | -2.07 / -2.36 | `sub(pow_3(day_wstd(Close, Ret)), cs_scale(day_sum(Low)))` |
| +0.26 | 0.329 | 8 | -2.10 / -2.36 | `day_std(Vwap)` |

## 拆解(35 次评估)

### head score -0.22:`ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.29 | -0.98 | -1.29 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), day_max(Low))` | -1.55 | -1.55 | -1.50 | — | (子树本身) |
| sufficiency | `day_last(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| sufficiency | `day_max(Low)` | -2.38 | -1.59 | -2.38 | — | (子树本身) |
| knockout | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -2.02 | -2.02 | -1.90 | +1.80 | `ts_mean(div(day_last(Volume), day_max(Low)), 241)` |
| knockout | `div(day_last(Volume), day_max(Low))` | -0.53 | -0.53 | -0.35 | +0.31 | `ts_mean(ts_hurst(day_last(Volume), 20), 241)` |
| swap | `Volume->Amt` | -0.63 | -0.63 | -0.55 | — | `ts_mean(ts_hurst(div(day_last(Amt), day_max(Low)), 20), 241)` |
| swap | `Low->High` | -0.18 | -0.18 | -0.12 | — | `ts_mean(ts_hurst(div(day_last(Volume), day_max(High)), 20), 241)` |
| window | `ts_mean@241->120` | -1.62 | -0.66 | -1.62 | — | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 120)` |
| window | `ts_mean@241->482` | — | — | — | — | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 482)` |

### head score -1.17:`ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50)` | -1.56 | -1.56 | -0.77 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50)` | -1.91 | -1.91 | -1.24 | — | (子树本身) |
| sufficiency | `ts_sum(day_q_stat_std(Volume), 50)` | -1.81 | -1.81 | -1.70 | — | (子树本身) |
| sufficiency | `day_q_stat_std(Volume)` | -2.36 | -2.36 | -2.21 | — | (子树本身) |
| knockout | `ts_sum(day_q_stat_std(Volume), 50)` | -1.18 | -1.18 | -0.86 | +0.01 | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 50), 50), 50)` |
| swap | `Volume->Amt` | -1.14 | -1.14 | -0.05 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Amt), 50), 50), 50), 50)` |
| window | `ts_quantile_q75@50->25` | -1.30 | -1.30 | -0.53 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 25)` |
| window | `ts_quantile_q75@50->100` | -1.12 | -1.12 | -0.25 | — | `ts_quantile_q75(ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 100)` |

### head score -1.35:`ts_quantile_q75(ts_sum(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_sum(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50)` | -1.71 | -1.71 | -0.72 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50)` | -1.91 | -1.91 | -1.24 | — | (子树本身) |
| sufficiency | `ts_sum(day_q_stat_std(Volume), 50)` | -1.81 | -1.81 | -1.70 | — | (子树本身) |
| sufficiency | `day_q_stat_std(Volume)` | -2.36 | -2.36 | -2.21 | — | (子树本身) |
| knockout | `ts_sum(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50)` | -1.55 | -1.55 | -0.99 | +0.20 | `ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 40)` |
| knockout | `ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50)` | -1.76 | -1.76 | -0.83 | +0.41 | `ts_quantile_q75(ts_sum(ts_sum(day_q_stat_std(Volume), 50), 50), 40)` |
| knockout | `ts_sum(day_q_stat_std(Volume), 50)` | -1.30 | -1.30 | -0.89 | -0.05 | `ts_quantile_q75(ts_sum(ts_quantile_q75(day_q_stat_std(Volume), 50), 50), 40)` |
| swap | `Volume->Amt` | -1.33 | -1.33 | -0.42 | — | `ts_quantile_q75(ts_sum(ts_quantile_q75(ts_sum(day_q_stat_std(Amt), 50), 50), 50), 40)` |
| window | `ts_quantile_q75@40->20` | -1.62 | -1.62 | -0.54 | — | `ts_quantile_q75(ts_sum(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 20)` |
| window | `ts_quantile_q75@40->80` | -1.24 | -1.24 | -0.21 | — | `ts_quantile_q75(ts_sum(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 80)` |

### head score -1.56:`ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50)` | -1.91 | -1.91 | -1.24 | — | (子树本身) |
| sufficiency | `ts_sum(day_q_stat_std(Volume), 50)` | -1.81 | -1.81 | -1.70 | — | (子树本身) |
| sufficiency | `day_q_stat_std(Volume)` | -2.36 | -2.36 | -2.21 | — | (子树本身) |
| knockout | `ts_sum(day_q_stat_std(Volume), 50)` | -1.59 | -1.27 | -1.59 | +0.02 | `ts_quantile_q75(ts_quantile_q75(day_q_stat_std(Volume), 50), 50)` |
| swap | `Volume->Amt` | -1.57 | -1.57 | -0.78 | — | `ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Amt), 50), 50), 50)` |
| window | `ts_quantile_q75@50->25` | -1.70 | -1.70 | -1.25 | — | `ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 25)` |
| window | `ts_quantile_q75@50->100` | -1.15 | -1.15 | -0.67 | — | `ts_quantile_q75(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_semistd_pos(sub(LogFloatCap, cs_scale(day_sum(Low))), 241)` — enrichment,均值差 +1.29,p 0.001
2. `sub(LogFloatCap, cs_scale(day_sum(Low)))` — enrichment,均值差 +1.08,p 0.001
3. `abs_(day_durbin_watson(Volume))` — enrichment,均值差 +1.04,p 0.017
4. `day_sum(Low)` — enrichment,均值差 +0.94,p 0.000
5. `cs_scale(day_sum(Low))` — enrichment,均值差 +0.88,p 0.001
6. `ts_sum(day_q_stat_std(Volume), 50)` — enrichment,均值差 +0.86,p 0.040
7. `day_autocorr_n1(Volume)` — enrichment,均值差 +0.73,p 0.045
8. `day_durbin_watson(Volume)` — enrichment,均值差 +0.63,p 0.026
9. `pow_3(day_wstd(Close, Ret))` — enrichment,均值差 +0.44,p 0.097
10. `day_wstd(Close, Ret)` — enrichment,均值差 +0.42,p 0.098

## 本组之前各轮的任务

- `prods2003Pr1a_Ea`:核心 `day_q_stat_std(Vwap)`;评分 69,过线 0,入 heads 0;采样计数 {'c05_no_core': 1031, 'c05_skeleton': 492}
  - score -0.90(train -0.90 valid -0.77):`cross_corr(day_q_stat_std(Vwap), day_autocorr_n1(Volume), 60)`
  - score -0.98(train -0.90 valid -0.98):`cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 15)`
  - score -1.34(train -1.34 valid -1.04):`cross_corr(cross_corr(day_q_stat_std(Vwap), cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 5), 60), cross_corr(cross_corr(day_q_stat_std(Vwap), cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 5), 60), day_q_stat_std(Volume), 60), 60)`
  - score -1.64(train -0.83 valid -1.64):`cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 60)`
  - score -1.78(train -1.38 valid -1.78):`cross_corr(day_q_stat_std(Vwap), day_sum(Ret), 60)`
- `prods2003Pr2a_Ea`:核心 `day_q_stat_std(Vwap)`;评分 93,过线 0,入 heads 0;采样计数 {'c05_no_core': 874, 'c05_skeleton': 466, 'c05_periphery_seen': 4}
  - score -0.78(train -0.68 valid -0.78):`cross_max(cross_corr(day_q_stat_std(Vwap), day_durbin_watson(Volume), 30), 30)`
  - score -0.80(train -0.80 valid -0.73):`cross_ema(cross_mean(cross_corr(day_q_stat_std(Vwap), abs_(day_durbin_watson(Volume)), 15), 120), 40)`
  - score -0.80(train -0.80 valid -0.66):`cross_ema(cross_corr(day_q_stat_std(Vwap), day_durbin_watson(Volume), 60), 40)`
  - score -0.81(train -0.81 valid -0.24):`cross_corr(day_q_stat_std(Vwap), day_durbin_watson(Volume), 30)`
  - score -0.81(train -0.81 valid -0.24):`cross_corr(day_q_stat_std(Vwap), abs_(day_durbin_watson(Volume)), 30)`
- `prods2003Pr2b_Nb`:核心 `—`;评分 91,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score -0.64(train -0.15 valid -0.64):`cross_semistd_pos(sub(LogFloatCap, cs_quantile_q50(day_sum(Vwap))), 241)`
  - score -0.66(train -0.01 valid -0.66):`cross_semistd_pos(sub(LogFloatCap, cs_quantile_q50(day_sum(Low))), 241)`
  - score -0.66(train -0.66 valid -0.14):`cross_semistd_pos(sub(LogFloatCap, cross_semistd_pos(cross_semistd_pos(sub(LogFloatCap, cs_scale(day_sum(Low))), 241), 241)), 241)`
  - score -0.66(train -0.66 valid -0.04):`cross_semistd_pos(sub(sub(LogFloatCap, cs_scale(day_sum(Low))), cs_scale(day_sum(Low))), 241)`
  - score -0.68(train -0.68 valid -0.05):`cross_semistd_pos(sub(LogFloatCap, cs_scale(day_sum(Low))), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.11(window ts_quantile_q75@40->80):`ts_quantile_q75(ts_sum(ts_quantile_q75(ts_sum(day_q_stat_std(Volume), 50), 50), 50), 80)`
