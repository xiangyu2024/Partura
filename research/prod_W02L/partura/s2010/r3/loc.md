# 定位:种子 2010,P 组,第 3 轮(只含 train / valid)

快照:prods2010M1_I0_open_search, prods2010M2_I0_open_search, prods2010M3_I0_open_search, prods2010Pr1b_Nb, prods2010Pr2a_Ea, prods2010Pr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(10 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.51 | +0.70 | +0.51 | +1 | 5 | prods2010Pr2a_Ea | `cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1), 241)` |
| +0.04 | +0.04 | +0.53 | +1 | 0 | prods2010M1_I0_open_search | `cross_stddev(sub(ts_sum(day_durbin_watson(Vwap), 10), cs_mean(ts_sum(day_durbin_watson(Vwap), 10))), 241)` |
| -1.89 | -1.67 | -1.89 | -1 | 5 | prods2010M1_I0_open_search | `cross_zscore(ts_sum(day_durbin_watson(Volume), 20), 120)` |
| -2.09 | -2.09 | -2.08 | +1 | 20 | prods2010M3_I0_open_search | `cross_decay_linear(day_ar1_coefficient(Vwap), 10)` |
| -2.13 | -2.02 | -2.13 | +1 | 20 | prods2010M3_I0_open_search | `cross_min(day_ar1_coefficient(Close), 3)` |
| -2.13 | -2.13 | -1.96 | +1 | 20 | prods2010M2_I0_open_search | `ts_min(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(High))), 5), 5)` |
| -2.19 | -2.11 | -2.19 | +1 | 5 | prods2010M3_I0_open_search | `cross_med(cross_decay_linear(day_ar1_coefficient(Close), 15), 60)` |
| -2.33 | -2.11 | -2.33 | +1 | 0 | prods2010M2_I0_open_search | `ts_quantile_q75(pow_2(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5)))), 50)` |
| -2.34 | -2.11 | -2.34 | +1 | 0 | prods2010M2_I0_open_search | `ts_quantile_q75(pow_2(cs_rank(ts_decay_linear(sigmoid(pow_05(day_ar1_coefficient(Volume))), 5))), 50)` |
| -2.39 | -2.39 | -2.35 | -1 | 0 | prods2010M1_I0_open_search | `ts_sum(day_durbin_watson(High), 20)` |

## 共性:221 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.63 | 0.002 | 6 | -0.71 / -2.34 | `cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1)` |
| +1.32 | 0.009 | 4 | -1.00 / -2.32 | `cross_delay(day_durbin_watson(in_slice(Vwap, 211, 240)), 1)` |
| +1.26 | 0.000 | 13 | -1.11 / -2.37 | `cross_delay(day_sum(in_slice(Ret, 1, 210)), 1)` |
| +0.98 | 0.000 | 70 | -1.62 / -2.60 | `day_durbin_watson(in_slice(Vwap, 211, 240))` |
| +0.93 | 0.003 | 9 | -1.40 / -2.33 | `cs_rank(day_durbin_watson(in_slice(Vwap, 211, 240)))` |
| +0.92 | 0.000 | 45 | -1.56 / -2.48 | `day_sum(in_slice(Ret, 1, 210))` |
| +0.86 | 0.000 | 18 | -1.50 / -2.36 | `div(day_open(Open), cross_delay(day_close(Close), 1))` |
| +0.86 | 0.007 | 8 | -1.47 / -2.32 | `cross_delay(cs_rank(day_durbin_watson(in_slice(Vwap, 211, 240))), 1)` |
| +0.79 | 0.024 | 5 | -1.52 / -2.31 | `day_sum(Ret)` |
| +0.74 | 0.000 | 25 | -1.63 / -2.38 | `cross_delay(day_close(Close), 1)` |
| +0.74 | 0.000 | 29 | -1.65 / -2.39 | `day_close(Close)` |
| +0.68 | 0.000 | 26 | -1.69 / -2.37 | `day_open(Open)` |
| +0.68 | 0.100 | 4 | -1.62 / -2.31 | `day_sum(in_slice(Vwap, 1, 210))` |
| +0.66 | 0.015 | 11 | -1.66 / -2.33 | `day_durbin_watson(in_slice(Vwap, 1, 30))` |
| +0.65 | 0.001 | 20 | -1.70 / -2.35 | `cross_delay(day_sum(in_slice(Ret, 211, 240)), 1)` |
| +0.63 | 0.068 | 6 | -1.68 / -2.31 | `log(day_durbin_watson(in_slice(Vwap, 1, 30)))` |
| +0.59 | 0.022 | 11 | -1.73 / -2.32 | `log(day_durbin_watson(in_slice(Vwap, 211, 240)))` |
| +0.38 | 0.153 | 4 | -1.92 / -2.30 | `cs_rank(day_sum(in_slice(Ret, 1, 210)))` |
| +0.31 | 0.015 | 32 | -2.02 / -2.34 | `day_sum(in_slice(Ret, 211, 240))` |
| +0.24 | 0.281 | 4 | -2.06 / -2.30 | `cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 241)` |

## 拆解(26 次评估)

### head score +0.51:`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1)` | -5.35 | -5.35 | -5.11 | — | (子树本身) |
| sufficiency | `cross_delay(day_sum(in_slice(Ret, 1, 210)), 1)` | -5.86 | -5.86 | -4.96 | — | (子树本身) |
| sufficiency | `day_durbin_watson(in_slice(Vwap, 211, 240))` | -2.54 | -2.54 | -0.41 | — | (子树本身) |
| sufficiency | `day_sum(in_slice(Ret, 1, 210))` | -4.36 | -4.36 | -3.89 | — | (子树本身) |
| knockout | `cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1)` | +0.20 | +0.35 | +0.20 | +0.30 | `cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 241)` |
| swap | `Vwap->Close` | +0.33 | +0.46 | +0.33 | — | `cross_corr(day_durbin_watson(in_slice(Close, 211, 240)), cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1), 241)` |
| window | `cross_corr@241->120` | -1.25 | +0.23 | -1.25 | — | `cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1), 120)` |
| window | `cross_corr@241->482` | +0.28 | +0.30 | +0.28 | — | `cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1), 482)` |

### head score +0.04:`cross_stddev(sub(ts_sum(day_durbin_watson(Vwap), 10), cs_mean(ts_sum(day_durbin_watson(Vwap), 10))), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(ts_sum(day_durbin_watson(Vwap), 10), cs_mean(ts_sum(day_durbin_watson(Vwap), 10)))` | -3.48 | -3.48 | -2.33 | — | (子树本身) |
| sufficiency | `cs_mean(ts_sum(day_durbin_watson(Vwap), 10))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_sum(day_durbin_watson(Vwap), 10)` | -3.48 | -3.48 | -2.33 | — | (子树本身) |
| knockout | `sub(ts_sum(day_durbin_watson(Vwap), 10), cs_mean(ts_sum(day_durbin_watson(Vwap), 10)))` | -0.15 | -0.15 | -0.10 | +0.19 | `cross_stddev(ts_sum(day_durbin_watson(Vwap), 10), 241)` |
| knockout | `cs_mean(ts_sum(day_durbin_watson(Vwap), 10))` | — | — | — | — | `cross_stddev(sub(ts_sum(day_durbin_watson(Vwap), 10), ts_sum(day_durbin_watson(Vwap), 10)), 241)` |
| knockout | `ts_sum(day_durbin_watson(Vwap), 10)` | -1.01 | -1.01 | +0.09 | +1.05 | `cross_stddev(sub(day_durbin_watson(Vwap), cs_mean(ts_sum(day_durbin_watson(Vwap), 10))), 241)` |
| knockout | `ts_sum(day_durbin_watson(Vwap), 10)` | -0.11 | -0.11 | -0.11 | +0.15 | `cross_stddev(sub(ts_sum(day_durbin_watson(Vwap), 10), cs_mean(day_durbin_watson(Vwap))), 241)` |
| swap | `Vwap->Close` | +0.07 | +0.07 | +0.56 | — | `cross_stddev(sub(ts_sum(day_durbin_watson(Close), 10), cs_mean(ts_sum(day_durbin_watson(Close), 10))), 241)` |
| window | `cross_stddev@241->120` | -0.26 | +0.04 | -0.26 | — | `cross_stddev(sub(ts_sum(day_durbin_watson(Vwap), 10), cs_mean(ts_sum(day_durbin_watson(Vwap), 10))), 120)` |
| window | `cross_stddev@241->482` | -1.05 | -1.05 | -0.10 | — | `cross_stddev(sub(ts_sum(day_durbin_watson(Vwap), 10), cs_mean(ts_sum(day_durbin_watson(Vwap), 10))), 482)` |

### head score -2.09:`cross_decay_linear(day_ar1_coefficient(Vwap), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(Vwap)` | -3.09 | -2.76 | -3.09 | — | (子树本身) |
| swap | `Vwap->Close` | -2.35 | -1.97 | -2.35 | — | `cross_decay_linear(day_ar1_coefficient(Close), 10)` |
| window | `cross_decay_linear@10->5` | -2.15 | -2.15 | -1.99 | — | `cross_decay_linear(day_ar1_coefficient(Vwap), 5)` |
| window | `cross_decay_linear@10->20` | -2.26 | -2.04 | -2.26 | — | `cross_decay_linear(day_ar1_coefficient(Vwap), 20)` |

### head score -2.13:`cross_min(day_ar1_coefficient(Close), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(Close)` | -2.44 | -2.44 | -2.34 | — | (子树本身) |
| swap | `Close->Vwap` | -1.93 | -1.93 | -1.84 | — | `cross_min(day_ar1_coefficient(Vwap), 3)` |
| window | `cross_min@3->2` | -2.17 | -2.17 | -2.16 | — | `cross_min(day_ar1_coefficient(Close), 2)` |
| window | `cross_min@3->6` | -2.01 | -2.01 | -2.01 | — | `cross_min(day_ar1_coefficient(Close), 6)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1)` — enrichment,均值差 +1.63,p 0.002
2. `cross_delay(day_durbin_watson(in_slice(Vwap, 211, 240)), 1)` — enrichment,均值差 +1.32,p 0.009
3. `cross_delay(day_sum(in_slice(Ret, 1, 210)), 1)` — enrichment,均值差 +1.26,p 0.000
4. `day_durbin_watson(in_slice(Vwap, 211, 240))` — enrichment,均值差 +0.98,p 0.000
5. `cs_rank(day_durbin_watson(in_slice(Vwap, 211, 240)))` — enrichment,均值差 +0.93,p 0.003
6. `day_sum(in_slice(Ret, 1, 210))` — enrichment,均值差 +0.92,p 0.000
7. `div(day_open(Open), cross_delay(day_close(Close), 1))` — enrichment,均值差 +0.86,p 0.000
8. `cross_delay(cs_rank(day_durbin_watson(in_slice(Vwap, 211, 240))), 1)` — enrichment,均值差 +0.86,p 0.007
9. `day_sum(Ret)` — enrichment,均值差 +0.79,p 0.024
10. `cross_delay(day_close(Close), 1)` — enrichment,均值差 +0.74,p 0.000
11. `day_close(Close)` — enrichment,均值差 +0.74,p 0.000
12. `day_open(Open)` — enrichment,均值差 +0.68,p 0.000
13. `day_sum(in_slice(Vwap, 1, 210))` — enrichment,均值差 +0.68,p 0.100
14. `day_durbin_watson(in_slice(Vwap, 1, 30))` — enrichment,均值差 +0.66,p 0.015
15. `cross_delay(day_sum(in_slice(Ret, 211, 240)), 1)` — enrichment,均值差 +0.65,p 0.001
16. `log(day_durbin_watson(in_slice(Vwap, 1, 30)))` — enrichment,均值差 +0.63,p 0.068
17. `log(day_durbin_watson(in_slice(Vwap, 211, 240)))` — enrichment,均值差 +0.59,p 0.022
18. `day_sum(in_slice(Ret, 211, 240))` — enrichment,均值差 +0.31,p 0.015

## 本组之前各轮的任务

- `prods2010Pr1b_Nb`:核心 `—`;评分 70,过线 0,入 heads 0;采样计数 {'c05_skeleton': 20}
  - score +0.13(train +0.40 valid +0.13):`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), day_sum(in_slice(Ret, 1, 210)), 241)`
  - score -0.23(train +0.27 valid -0.23):`cross_corr(day_durbin_watson(in_slice(in_forward_valid_part(High), 211, 240)), day_sum(in_slice(Ret, 1, 210)), 120)`
  - score -0.52(train -0.52 valid -0.31):`cross_corr(day_durbin_watson(in_slice(in_forward_valid_part(High), 211, 240)), day_sum(in_slice(in_forward_valid_part(High), 1, 210)), 120)`
  - score -0.53(train -0.53 valid -0.30):`cross_corr(day_durbin_watson(in_slice(in_forward_valid_part(High), 211, 240)), day_sum(in_slice(High, 1, 210)), 120)`
  - score -0.53(train +0.68 valid -0.53):`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), day_topw_mean(Amt, in_forward_valid_part(High)), 120)`
- `prods2010Pr2a_Ea`:核心 `day_durbin_watson(in_slice(Vwap, 211, 240))`;评分 87,过线 1,入 heads 1;采样计数 {'c05_no_core': 807, 'c05_skeleton': 384, 'c05_periphery_seen': 4}
  - score +0.51(train +0.70 valid +0.51):`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1), 241)`
  - score +0.36(train +0.92 valid +0.36):`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1), 1), 241)`
  - score +0.25(train +0.25 valid +0.70):`cross_cov(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 1), 241)`
  - score +0.19(train +0.31 valid +0.19):`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_delay(day_sum(in_slice(Ret, 1, 210)), 1), 241)`
  - score -0.16(train -0.16 valid +0.15):`cross_corr(day_durbin_watson(in_slice(Vwap, 211, 240)), cross_med(day_sum(in_slice(Ret, 1, 210)), 10), 241)`
- `prods2010Pr2b_Nb`:核心 `—`;评分 76,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.75(train -0.17 valid -0.75):`cross_corr(cross_delay(day_sum(in_slice(Ret, 211, 240)), 1), sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 241)`
  - score -0.75(train -0.17 valid -0.75):`cross_corr(cross_delay(day_sum(in_slice(Ret, 211, 240)), 1), sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 0.5), 241)`
  - score -0.84(train -0.64 valid -0.84):`cross_corr(cross_delay(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), sub(div(day_open(Open), cross_delay(day_close(Close), 1)), 1), 241)`
  - score -1.22(train -1.22 valid -0.92):`cross_corr(cross_delay(day_sum(in_slice(Ret, 211, 240)), 1), sub(day_sum(in_slice(Ret, 211, 240)), 1), 241)`
  - score -1.22(train -1.22 valid -0.91):`cross_corr(cross_delay(day_sum(in_slice(Ret, 211, 240)), 1), sub(day_sum(in_slice(Ret, 211, 240)), BoardCode), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.20(swap Close->Vwap):`cross_min(day_ar1_coefficient(Vwap), 3)`
- 增益 +0.12(window cross_min@3->6):`cross_min(day_ar1_coefficient(Close), 6)`
