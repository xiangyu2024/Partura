# 定位:种子 801,C 组,第 3 轮(只含 train / valid)

快照:c05s801M1_I0_open_search, c05s801M2_I0_open_search, c05s801M3_I0_open_search, c06s801Cr1a_Na, c06s801Cr1b_Nb, c06s801Cr2a_Ea, c06s801Cr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(13 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.56 | +1.56 | +2.60 | -1 | 20 | c05s801M3_I0_open_search | `signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50))` |
| +1.53 | +1.53 | +3.39 | -1 | 5 | c05s801M2_I0_open_search | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))), 241), cs_last_high10(cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))), log(day_first(Open))))` |
| +1.44 | +1.44 | +2.06 | -1 | 0 | c05s801M3_I0_open_search | `ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 50)` |
| +1.22 | +1.30 | +1.22 | -1 | 20 | c06s801Cr1b_Nb | `cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 20)` |
| +0.91 | +0.91 | +1.66 | -1 | 5 | c06s801Cr2a_Ea | `cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)` |
| +0.76 | +0.76 | +1.07 | +1 | 20 | c06s801Cr2b_Nb | `div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60))` |
| +0.75 | +0.75 | +1.66 | -1 | 0 | c05s801M2_I0_open_search | `cs_first_high40(cross_corr(inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50)))), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))), 241), cs_last_high10(cs_state_rank(day_es_ratio_hi(Vwap), 50), log(cs_state_rank(day_es_ratio_hi(High), 50))))` |
| +0.67 | +0.67 | +2.63 | -1 | 0 | c05s801M3_I0_open_search | `ts_std(ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 50), 50)` |
| +0.65 | +0.65 | +1.31 | +1 | 20 | c06s801Cr2b_Nb | `div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10), cross_stddev(log(div(day_last(Close), day_first(Open))), 60))` |
| +0.61 | +0.61 | +2.61 | +1 | 20 | c06s801Cr1a_Na | `cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15)` |
| +0.56 | +0.56 | +2.23 | -1 | 5 | c05s801M3_I0_open_search | `cs_last_high10(LimitWidth, day_open(Open))` |
| +0.51 | +0.51 | +1.87 | -1 | 5 | c06s801Cr2a_Ea | `cross_corr(cross_delay(div(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), day_std(Ret)), 1), log(div(day_last(Close), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)` |
| +0.50 | +0.50 | +0.79 | -1 | 20 | c05s801M1_I0_open_search | `inv(pow_3(pow_3(pow_3(LogFloatShares))))` |

## 共性:582 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.76 | 0.000 | 7 | +0.87 / -0.89 | `signedpower(ts_stddev(day_durbin_watson(Close), 20))` |
| +1.72 | 0.000 | 7 | +0.84 / -0.89 | `ts_stddev(signedpower(day_durbin_watson(Close)), 20)` |
| +1.67 | 0.003 | 4 | +0.79 / -0.88 | `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` |
| +1.47 | 0.000 | 16 | +0.56 / -0.91 | `signedpower(day_durbin_watson(Close))` |
| +1.46 | 0.001 | 7 | +0.57 / -0.88 | `day_sum(pow_3(Volume))` |
| +1.42 | 0.000 | 28 | +0.48 / -0.93 | `pow_3(LogFloatShares)` |
| +1.38 | 0.000 | 46 | +0.41 / -0.98 | `day_durbin_watson(Close)` |
| +1.38 | 0.000 | 12 | +0.48 / -0.89 | `pow_05(pow_3(LogFloatShares))` |
| +1.37 | 0.008 | 4 | +0.50 / -0.88 | `cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))` |
| +1.37 | 0.000 | 10 | +0.48 / -0.89 | `pow_3(pow_3(LogFloatShares))` |
| +1.37 | 0.000 | 20 | +0.45 / -0.91 | `ts_stddev(day_durbin_watson(Close), 20)` |
| +1.36 | 0.003 | 6 | +0.48 / -0.88 | `pow_3(pow_05(pow_3(LogFloatShares)))` |
| +1.36 | 0.006 | 5 | +0.48 / -0.88 | `pow_05(LogFloatShares)` |
| +1.36 | 0.007 | 5 | +0.48 / -0.88 | `pow_2_5(LogFloatShares)` |
| +1.36 | 0.010 | 4 | +0.48 / -0.88 | `pow_05(pow_3(pow_3(LogFloatShares)))` |
| +1.36 | 0.015 | 4 | +0.48 / -0.88 | `pow_05(pow_2_5(LogFloatShares))` |
| +1.35 | 0.013 | 4 | +0.47 / -0.88 | `cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)` |
| +1.34 | 0.006 | 5 | +0.47 / -0.88 | `cs_state_rank(log(day_first(Open)), 50)` |
| +1.32 | 0.015 | 4 | +0.44 / -0.87 | `mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))` |
| +1.27 | 0.009 | 4 | +0.39 / -0.87 | `sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))` |

## 拆解(40 次评估)

### head score +1.56:`signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50)` | +0.95 | +0.95 | +2.24 | — | (子树本身) |
| sufficiency | `signedpower(signedpower(day_durbin_watson(Close)))` | +1.26 | +1.26 | +3.19 | — | (子树本身) |
| sufficiency | `signedpower(day_durbin_watson(Close))` | -0.21 | -0.21 | +1.92 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Close)` | -1.85 | -1.85 | -0.03 | — | (子树本身) |
| knockout | `ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50)` | — | — | — | — | `signedpower(signedpower(signedpower(day_durbin_watson(Close))))` |
| knockout | `signedpower(signedpower(day_durbin_watson(Close)))` | +0.75 | +0.75 | +2.22 | +0.81 | `signedpower(ts_std(signedpower(day_durbin_watson(Close)), 50))` |
| swap | `Close->Vwap` | +1.39 | +1.39 | +3.23 | — | `signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Vwap))), 50))` |
| window | `ts_std@50->25` | +1.68 | +1.68 | +2.59 | — | `signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 25))` |
| window | `ts_std@50->100` | +1.59 | +1.59 | +2.24 | — | `signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 100))` |

### head score +1.44:`ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `signedpower(ts_stddev(day_durbin_watson(Close), 20))` | +0.49 | +0.49 | +2.59 | — | (子树本身) |
| sufficiency | `ts_stddev(day_durbin_watson(Close), 20)` | +0.29 | +0.29 | +1.73 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Close)` | -1.85 | -1.85 | -0.03 | — | (子树本身) |
| knockout | `signedpower(ts_stddev(day_durbin_watson(Close), 20))` | +1.13 | +1.13 | +1.38 | +0.31 | `ts_std(ts_stddev(day_durbin_watson(Close), 20), 50)` |
| knockout | `ts_stddev(day_durbin_watson(Close), 20)` | +0.59 | +0.59 | +1.80 | +0.85 | `ts_std(signedpower(day_durbin_watson(Close)), 50)` |
| swap | `Close->Vwap` | +1.33 | +1.33 | +2.04 | — | `ts_std(signedpower(ts_stddev(day_durbin_watson(Vwap), 20)), 50)` |
| window | `ts_std@50->25` | +0.94 | +0.94 | +2.21 | — | `ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 25)` |
| window | `ts_std@50->100` | +0.90 | +0.90 | +2.73 | — | `ts_std(signedpower(ts_stddev(day_durbin_watson(Close), 20)), 100)` |

### head score +0.91:`cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1)))` | -2.22 | -2.22 | -1.38 | — | (子树本身) |
| sufficiency | `div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))` | -1.42 | -1.42 | -0.20 | — | (子树本身) |
| sufficiency | `cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1)` | -4.41 | -4.41 | -3.58 | — | (子树本身) |
| sufficiency | `div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1))` | -1.87 | -0.69 | -1.87 | — | (子树本身) |
| knockout | `log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1)))` | -1.56 | +1.03 | -1.56 | +2.47 | `cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1)), 120)` |
| knockout | `div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))` | — | — | — | — | `cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1))), 120)` |
| knockout | `cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1)` | -1.09 | -1.09 | -1.07 | +2.00 | `cross_corr(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)` |
| knockout | `div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1))` | +0.81 | +0.81 | +1.28 | +0.09 | `cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(day_last(Close), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)` |
| swap | `Amt->Volume` | +0.97 | +0.97 | +1.84 | — | `cross_corr(cross_delay(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_std(Ret)), 1), log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Volume), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_std(Ret)), 1))), 120)` |
| swap | `Close->Vwap` | +0.91 | +0.91 | +1.64 | — | `cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(div(day_last(Vwap), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)` |
| window | `cross_corr@120->60` | +0.79 | +0.79 | +1.40 | — | `cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 60)` |
| window | `cross_corr@120->240` | +0.99 | +0.99 | +2.65 | — | `cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 240)` |

### head score +0.76:`div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10)` | -0.58 | -0.58 | +0.84 | — | (子树本身) |
| sufficiency | `cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60)` | -0.57 | -0.57 | -0.32 | — | (子树本身) |
| sufficiency | `log(div(day_first(Open), ts_delay(day_last(Close), 1)))` | -3.64 | -2.23 | -3.64 | — | (子树本身) |
| sufficiency | `cross_stddev(log(div(day_last(Close), day_first(Open))), 60)` | -0.61 | -0.61 | -0.02 | — | (子树本身) |
| knockout | `cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10)` | -3.42 | -2.06 | -3.42 | +4.18 | `div(log(div(day_first(Open), ts_delay(day_last(Close), 1))), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60))` |
| knockout | `cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60)` | +0.65 | +0.65 | +1.31 | +0.12 | `div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10), cross_stddev(log(div(day_last(Close), day_first(Open))), 60))` |
| knockout | `log(div(day_first(Open), ts_delay(day_last(Close), 1)))` | +0.80 | +0.80 | +1.09 | -0.03 | `div(cross_stddev(div(day_first(Open), ts_delay(day_last(Close), 1)), 10), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60))` |
| swap | `Open->Close` | +0.77 | +0.77 | +1.06 | — | `div(cross_stddev(log(div(day_first(Close), ts_delay(day_last(Close), 1))), 10), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Close))), 60), 60))` |
| swap | `Close->Vwap` | +0.76 | +0.76 | +1.15 | — | `div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Vwap), 1))), 10), cross_stddev(cross_stddev(log(div(day_last(Vwap), day_first(Open))), 60), 60))` |
| window | `cross_stddev@10->5` | +0.52 | +0.52 | +1.05 | — | `div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 5), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60))` |
| window | `cross_stddev@10->20` | +0.93 | +0.93 | +1.46 | — | `div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `signedpower(signedpower(day_durbin_watson(Close)))` — ablation,自身 score +1.26(所在 head +1.56)
2. `ts_std(signedpower(signedpower(day_durbin_watson(Close))), 50)` — ablation,自身 score +0.95(所在 head +1.56)
3. `signedpower(ts_stddev(day_durbin_watson(Close), 20))` — enrichment,均值差 +1.76,p 0.000
4. `ts_stddev(signedpower(day_durbin_watson(Close)), 20)` — enrichment,均值差 +1.72,p 0.000
5. `inv(cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))))` — enrichment,均值差 +1.67,p 0.003
6. `signedpower(day_durbin_watson(Close))` — enrichment,均值差 +1.47,p 0.000
7. `day_sum(pow_3(Volume))` — enrichment,均值差 +1.46,p 0.001
8. `pow_3(LogFloatShares)` — enrichment,均值差 +1.42,p 0.000
9. `day_durbin_watson(Close)` — enrichment,均值差 +1.38,p 0.000
10. `pow_05(pow_3(LogFloatShares))` — enrichment,均值差 +1.38,p 0.000
11. `cs_last_high10(cs_state_rank(log(day_first(Open)), 50), log(day_first(Open)))` — enrichment,均值差 +1.37,p 0.008
12. `pow_3(pow_3(LogFloatShares))` — enrichment,均值差 +1.37,p 0.000
13. `ts_stddev(day_durbin_watson(Close), 20)` — enrichment,均值差 +1.37,p 0.000
14. `pow_3(pow_05(pow_3(LogFloatShares)))` — enrichment,均值差 +1.36,p 0.003
15. `pow_05(LogFloatShares)` — enrichment,均值差 +1.36,p 0.006
16. `pow_2_5(LogFloatShares)` — enrichment,均值差 +1.36,p 0.007
17. `pow_05(pow_3(pow_3(LogFloatShares)))` — enrichment,均值差 +1.36,p 0.010
18. `pow_05(pow_2_5(LogFloatShares))` — enrichment,均值差 +1.36,p 0.015
19. `cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)` — enrichment,均值差 +1.35,p 0.013
20. `cs_state_rank(log(day_first(Open)), 50)` — enrichment,均值差 +1.34,p 0.006
21. `mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))` — enrichment,均值差 +1.32,p 0.015
22. `sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))` — enrichment,均值差 +1.27,p 0.009
23. `cross_corr(inv(day_pos_ratio(Volume)), cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open))), 241)` — enrichment,均值差 +1.25,p 0.017
24. `cs_last_high10(cs_state_rank(day_es_ratio_hi(High), 50), log(day_first(Open)))` — enrichment,均值差 +1.17,p 0.000
25. `ts_std(ts_stddev(day_durbin_watson(Close), 20), 20)` — enrichment,均值差 +1.16,p 0.004
26. `day_zero_ratio(Vwap)` — enrichment,均值差 +1.10,p 0.054
27. `cs_state_rank(day_es_ratio_hi(Vwap), 50)` — enrichment,均值差 +1.07,p 0.034
28. `day_es_ratio_hi(Vwap)` — enrichment,均值差 +1.07,p 0.034
29. `cs_state_rank(day_es_ratio_hi(High), 50)` — enrichment,均值差 +1.01,p 0.000
30. `ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)` — enrichment,均值差 +0.99,p 0.066
31. `cross_ema(day_corr(Ret, Amt), 10)` — enrichment,均值差 +0.94,p 0.028
32. `day_corr(Ret, Amt)` — enrichment,均值差 +0.76,p 0.027
33. `day_open(Open)` — enrichment,均值差 +0.72,p 0.091
34. `log(day_first(Open))` — enrichment,均值差 +0.71,p 0.000
35. `day_es_ratio_hi(High)` — enrichment,均值差 +0.54,p 0.004
36. `ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1)` — enrichment,均值差 +0.46,p 0.060
37. `day_pos_ratio(Volume)` — enrichment,均值差 +0.24,p 0.098

## 本组之前各轮的任务

- `c06s801Cr1a_Na`:核心 `—`;评分 86,过线 1,入 heads 1;采样计数 {}
  - score +0.61(train +0.61 valid +2.61):`cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15)`
  - score +0.50(train +0.50 valid +2.90):`cross_ema(cross_mean(cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10), 15), 10)`
  - score +0.48(train +0.48 valid +2.34):`cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 10)`
  - score +0.44(train +0.44 valid +2.21):`cross_mean(div(cross_ema(day_corr(Ret, Amt), 10), day_std(Ret)), 15)`
  - score +0.43(train +0.43 valid +2.45):`cross_ema(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 15)`
- `c06s801Cr1b_Nb`:核心 `—`;评分 83,过线 4,入 heads 1;采样计数 {}
  - score +1.22(train +1.30 valid +1.22):`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), day_sum(pow_3(Volume)))), 20)`
  - score +0.79(train +0.79 valid +1.28):`cross_mean(div(day_sum(mul(mul(Ret, in_logchg(Close, 1)), Ret)), mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))), 20)`
  - score +0.72(train +0.72 valid +1.64):`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(mul(Ret, Ret), Ret))))), 20)`
  - score +0.55(train +0.55 valid +1.47):`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))), 20)`
  - score +0.38(train +0.38 valid +1.38):`cross_mean(div(day_sum(mul(mul(Ret, Ret), Ret)), mul(day_sum(pow_3(Volume)), sqrt(day_sum(mul(in_logchg(Close, 1), Ret))))), 60)`
- `c06s801Cr2a_Ea`:核心 `div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret))`;评分 94,过线 8,入 heads 2;采样计数 {'c05_no_core': 1711, 'c05_periphery_seen': 1}
  - score +0.91(train +0.91 valid +1.66):`cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(div(day_last(Close), ts_delay(sub(day_wmean(Ret, Amt), day_mean(Ret)), 1)), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)`
  - score +0.81(train +0.81 valid +1.28):`cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(day_last(Close), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)`
  - score +0.80(train +0.80 valid +1.27):`cross_corr(cross_delay(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(day_last(High), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)`
  - score +0.54(train +0.54 valid +1.60):`cross_corr(cross_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(day_last(Close), ts_delay(add(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), day_std(Ret)), 1))), 120)`
  - score +0.54(train +0.54 valid +1.67):`cross_corr(cross_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1), log(div(day_last(Close), ts_delay(div(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_std(Ret)), 1))), 120)`
- `c06s801Cr2b_Nb`:核心 `—`;评分 91,过线 5,入 heads 2;采样计数 {}
  - score +0.76(train +0.76 valid +1.07):`div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60))`
  - score +0.65(train +0.65 valid +1.31):`div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 10), cross_stddev(log(div(day_last(Close), day_first(Open))), 60))`
  - score +0.63(train +0.63 valid +0.97):`div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60), cross_stddev(log(div(day_last(Open), day_first(Open))), 60))`
  - score +0.61(train +0.61 valid +0.99):`div(cross_stddev(log(div(day_first(Close), ts_delay(day_last(Close), 1))), 60), cross_stddev(log(div(day_last(Close), day_first(Open))), 60))`
  - score +0.55(train +0.55 valid +0.99):`div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 60), cross_stddev(log(div(day_last(Close), day_first(Open))), 60))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.17(window cross_stddev@10->20):`div(cross_stddev(log(div(day_first(Open), ts_delay(day_last(Close), 1))), 20), cross_stddev(cross_stddev(log(div(day_last(Close), day_first(Open))), 60), 60))`
- 增益 +0.12(window ts_std@50->25):`signedpower(ts_std(signedpower(signedpower(day_durbin_watson(Close))), 25))`
