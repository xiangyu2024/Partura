# 定位:种子 901,P 组,第 2 轮(只含 train / valid)

快照:prods901M1_I0_open_search, prods901M2_I0_open_search, prods901Pr1a_Ea, prods901Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:296 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.74 | 0.000 | 4 | +0.32 / -1.42 | `day_argmax(Amt)` |
| +0.95 | 0.013 | 4 | -0.46 / -1.41 | `cross_semistd_pos(day_last(Close), 60)` |
| +0.95 | 0.013 | 4 | -0.46 / -1.41 | `cross_semistd_neg(day_last(Close), 60)` |
| +0.95 | 0.013 | 4 | -0.46 / -1.41 | `sub(cross_semistd_pos(day_last(Close), 60), cross_semistd_neg(day_last(Close), 60))` |
| +0.90 | 0.008 | 8 | -0.52 / -1.42 | `sub(day_hurst(High), LogFloatShares)` |
| +0.78 | 0.004 | 9 | -0.64 / -1.42 | `day_argmax(Volume)` |
| +0.77 | 0.017 | 7 | -0.65 / -1.41 | `sub(day_wmean(Ret, Amt), day_mean(Ret))` |
| +0.74 | 0.005 | 12 | -0.68 / -1.42 | `day_wmean(Ret, Amt)` |
| +0.71 | 0.076 | 4 | -0.70 / -1.40 | `day_corr(Ret, Volume)` |
| +0.71 | 0.076 | 4 | -0.70 / -1.40 | `cs_rank(day_corr(Ret, Volume))` |
| +0.70 | 0.074 | 4 | -0.70 / -1.40 | `day_pos_ratio(pow_05(Close))` |
| +0.70 | 0.027 | 8 | -0.71 / -1.41 | `day_zero_ratio(Vwap)` |
| +0.63 | 0.039 | 12 | -0.79 / -1.42 | `day_hurst(High)` |
| +0.58 | 0.042 | 10 | -0.84 / -1.41 | `sub(LogFloatCap, LogFloatShares)` |
| +0.58 | 0.014 | 16 | -0.85 / -1.43 | `div(day_last(Close), day_first(Open))` |
| +0.57 | 0.006 | 21 | -0.86 / -1.44 | `cs_demean(day_last(Close))` |
| +0.56 | 0.008 | 23 | -0.88 / -1.44 | `day_first(Open)` |
| +0.51 | 0.044 | 15 | -0.91 / -1.42 | `ts_delay(day_last(Close), 1)` |
| +0.48 | 0.001 | 115 | -1.10 / -1.58 | `day_last(Close)` |
| +0.42 | 0.141 | 8 | -0.98 / -1.41 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `day_argmax(Amt)` — enrichment,均值差 +1.74,p 0.000
2. `cross_semistd_pos(day_last(Close), 60)` — enrichment,均值差 +0.95,p 0.013
3. `cross_semistd_neg(day_last(Close), 60)` — enrichment,均值差 +0.95,p 0.013
4. `sub(cross_semistd_pos(day_last(Close), 60), cross_semistd_neg(day_last(Close), 60))` — enrichment,均值差 +0.95,p 0.013
5. `sub(day_hurst(High), LogFloatShares)` — enrichment,均值差 +0.90,p 0.008
6. `day_argmax(Volume)` — enrichment,均值差 +0.78,p 0.004
7. `sub(day_wmean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +0.77,p 0.017
8. `day_wmean(Ret, Amt)` — enrichment,均值差 +0.74,p 0.005
9. `day_corr(Ret, Volume)` — enrichment,均值差 +0.71,p 0.076
10. `cs_rank(day_corr(Ret, Volume))` — enrichment,均值差 +0.71,p 0.076
11. `day_pos_ratio(pow_05(Close))` — enrichment,均值差 +0.70,p 0.074
12. `day_zero_ratio(Vwap)` — enrichment,均值差 +0.70,p 0.027
13. `day_hurst(High)` — enrichment,均值差 +0.63,p 0.039
14. `sub(LogFloatCap, LogFloatShares)` — enrichment,均值差 +0.58,p 0.042
15. `div(day_last(Close), day_first(Open))` — enrichment,均值差 +0.58,p 0.014
16. `cs_demean(day_last(Close))` — enrichment,均值差 +0.57,p 0.006
17. `day_first(Open)` — enrichment,均值差 +0.56,p 0.008
18. `ts_delay(day_last(Close), 1)` — enrichment,均值差 +0.51,p 0.044
19. `day_last(Close)` — enrichment,均值差 +0.48,p 0.001
20. `day_mean(Ret)` — enrichment,均值差 +0.39,p 0.096

## 本组之前各轮的任务

- `prods901Pr1a_Ea`:核心 `day_last(Close)`;评分 79,过线 0,入 heads 0;采样计数 {'c05_no_core': 712, 'c05_periphery_seen': 3}
  - score +0.18(train +0.18 valid +0.62):`sub(log(day_last(Close)), sub(day_hurst(Close), LogFloatShares))`
  - score +0.16(train +0.16 valid +0.61):`sub(log(day_last(Close)), sub(day_hurst(High), LogFloatShares))`
  - score +0.13(train +0.13 valid +0.57):`sub(log(sub(log(day_last(Close)), sub(log(day_last(Close)), sub(day_hurst(High), LogFloatShares)))), sub(log(day_last(Close)), sub(day_hurst(High), LogFloatShares)))`
  - score +0.08(train +0.08 valid +0.55):`sub(log(day_last(Close)), sub(day_centroid(Vwap), LogFloatShares))`
  - score -0.06(train -0.06 valid +0.28):`sub(log(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares))), sub(LogFloatCap, LogFloatShares))`
- `prods901Pr1b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {}
  - score +0.11(train +0.11 valid +0.88):`cross_mean(sub(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 3), day_mean(Ret)), 120)`
  - score -0.01(train -0.01 valid +0.91):`cross_mean(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_mean(Ret)), 120)`
  - score -0.05(train -0.05 valid +1.14):`cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 120)`
  - score -0.06(train -0.00 valid -0.06):`cross_mean(sub(sub(div(day_last(Close), day_first(Open)), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 120)`
  - score -0.06(train +0.05 valid -0.06):`cross_mean(sub(sub(div(day_last(Close), day_first(Close)), 1), sub(div(day_first(Open), ts_delay(day_last(Close), 1)), 1)), 120)`

## 比原 head 好的拆解变体(R 候选)

(没有)
