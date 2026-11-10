# 定位:种子 2009,P 组,第 3 轮(只含 train / valid)

快照:prods2009M1_I0_open_search, prods2009M2_I0_open_search, prods2009M3_I0_open_search, prods2009Pr1a_Ea, prods2009Pr1b_Nb, prods2009Pr2a_Ea, prods2009Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(9 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.92 | -0.45 | -0.92 | +1 | 5 | prods2009M2_I0_open_search | `ts_max(day_durbin_watson(Close), 80)` |
| -2.11 | -1.65 | -2.11 | +1 | 5 | prods2009M2_I0_open_search | `ts_max(day_durbin_watson(Close), 30)` |
| -2.23 | -1.65 | -2.23 | +1 | 20 | prods2009M1_I0_open_search | `ts_sum(log(log(day_durbin_watson(Volume))), 10)` |
| -2.27 | -1.92 | -2.27 | +1 | 20 | prods2009M1_I0_open_search | `ts_sum(log(log(day_durbin_watson(Volume))), 5)` |
| -2.35 | -2.20 | -2.35 | +1 | 20 | prods2009M1_I0_open_search | `cross_fangzheng(log(log(day_durbin_watson(Volume))), 10)` |
| -2.73 | -2.31 | -2.73 | +1 | 5 | prods2009M2_I0_open_search | `ts_max(day_durbin_watson(Close), 20)` |
| -3.21 | -2.91 | -3.21 | +1 | 20 | prods2009M3_I0_open_search | `ts_quantile_q75(sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3)))), 30)` |
| -3.27 | -3.27 | -2.35 | +1 | 20 | prods2009M3_I0_open_search | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), sigmoid(day_durbin_watson(Low))), 241)` |
| -3.49 | -3.49 | -3.35 | -1 | 20 | prods2009M3_I0_open_search | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret))))), 3)` |

## 共性:231 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.55 | 0.005 | 5 | -0.81 / -2.36 | `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241)` |
| +1.48 | 0.000 | 11 | -0.92 / -2.40 | `sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret))` |
| +1.44 | 0.000 | 15 | -0.98 / -2.42 | `sub(day_wmean(Ret, Amt), day_mean(Ret))` |
| +1.23 | 0.000 | 39 | -1.30 / -2.53 | `day_mean(Ret)` |
| +1.21 | 0.018 | 5 | -1.15 / -2.35 | `cross_mean(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret)), 241)` |
| +1.03 | 0.000 | 30 | -1.43 / -2.46 | `day_wmean(Ret, Amt)` |
| +0.80 | 0.000 | 34 | -1.64 / -2.44 | `day_wmean(Ret, div(Amt, cross_mean(Amt, 20)))` |
| +0.54 | 0.112 | 11 | -1.81 / -2.35 | `log(cross_mean(log(log(day_durbin_watson(Volume))), 120))` |
| +0.32 | 0.241 | 14 | -2.02 / -2.35 | `cross_mean(log(log(day_durbin_watson(Volume))), 120)` |
| -0.10 | 0.728 | 12 | -2.42 / -2.32 | `ts_delay(day_sum(Ret), 1)` |
| -0.15 | 0.510 | 4 | -2.48 / -2.32 | `log(log(log(log(day_durbin_watson(Volume)))))` |
| -0.22 | 0.862 | 22 | -2.53 / -2.31 | `day_sum(Ret)` |
| -0.27 | 0.719 | 8 | -2.59 / -2.32 | `log(log(log(day_durbin_watson(Volume))))` |
| -0.28 | 0.786 | 9 | -2.59 / -2.32 | `cross_mean(log(log(day_durbin_watson(Volume))), 10)` |
| -0.29 | 0.687 | 4 | -2.61 / -2.32 | `cross_delta(cross_mean(log(log(day_durbin_watson(Volume))), 10), 20)` |
| -0.30 | 0.973 | 59 | -2.55 / -2.25 | `log(day_durbin_watson(Volume))` |
| -0.30 | 0.973 | 59 | -2.55 / -2.25 | `log(log(day_durbin_watson(Volume)))` |
| -0.34 | 0.984 | 60 | -2.58 / -2.24 | `day_durbin_watson(Volume)` |
| -0.49 | 0.884 | 5 | -2.81 / -2.32 | `cross_corr(log(log(day_durbin_watson(Volume))), ts_delay(day_sum(Ret), 1), 40)` |
| -1.09 | 0.999 | 11 | -3.36 / -2.27 | `day_durbin_watson(Close)` |

## 拆解(34 次评估)

### head score -0.92:`ts_max(day_durbin_watson(Close), 80)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Close)` | -4.03 | -4.03 | -3.83 | — | (子树本身) |
| swap | `Close->Vwap` | -0.96 | -0.72 | -0.96 | — | `ts_max(day_durbin_watson(Vwap), 80)` |
| window | `ts_max@80->40` | -1.80 | -1.37 | -1.80 | — | `ts_max(day_durbin_watson(Close), 40)` |
| window | `ts_max@80->160` | -1.30 | +0.34 | -1.30 | — | `ts_max(day_durbin_watson(Close), 160)` |

### head score -3.21:`ts_quantile_q75(sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3)))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3))))` | -3.66 | -3.66 | -2.86 | — | (子树本身) |
| sufficiency | `sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3)))` | -3.66 | -3.66 | -2.86 | — | (子树本身) |
| sufficiency | `pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3))` | -3.66 | -3.66 | -2.86 | — | (子树本身) |
| sufficiency | `cross_mean(sigmoid(day_durbin_watson(Amt)), 3)` | -3.66 | -3.66 | -2.86 | — | (子树本身) |
| knockout | `sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3))))` | -3.15 | -2.91 | -3.15 | -0.06 | `ts_quantile_q75(sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3))), 30)` |
| knockout | `pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3))` | -3.15 | -2.91 | -3.15 | -0.06 | `ts_quantile_q75(sigmoid(sigmoid(cross_mean(sigmoid(day_durbin_watson(Amt)), 3))), 30)` |
| knockout | `cross_mean(sigmoid(day_durbin_watson(Amt)), 3)` | -3.22 | -3.07 | -3.22 | +0.01 | `ts_quantile_q75(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Amt))))), 30)` |
| swap | `Amt->Volume` | -3.15 | -2.91 | -3.15 | — | `ts_quantile_q75(sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Volume)), 3)))), 30)` |
| window | `ts_quantile_q75@30->15` | -3.35 | -3.35 | -3.13 | — | `ts_quantile_q75(sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3)))), 15)` |
| window | `ts_quantile_q75@30->60` | -3.43 | -2.57 | -3.43 | — | `ts_quantile_q75(sigmoid(sigmoid(pow_2(cross_mean(sigmoid(day_durbin_watson(Amt)), 3)))), 60)` |

### head score -3.27:`cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), sigmoid(day_durbin_watson(Low))), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(ts_regres(day_mean(High), day_close(Amt), 50), sigmoid(day_durbin_watson(Low)))` | -3.65 | -3.65 | -3.38 | — | (子树本身) |
| sufficiency | `ts_regres(day_mean(High), day_close(Amt), 50)` | -3.87 | -3.87 | -3.66 | — | (子树本身) |
| sufficiency | `sigmoid(day_durbin_watson(Low))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_mean(High)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| knockout | `mul(ts_regres(day_mean(High), day_close(Amt), 50), sigmoid(day_durbin_watson(Low)))` | -3.24 | -3.24 | -2.28 | -0.03 | `cross_mean(ts_regres(day_mean(High), day_close(Amt), 50), 241)` |
| knockout | `ts_regres(day_mean(High), day_close(Amt), 50)` | -2.36 | -1.65 | -2.36 | -0.91 | `cross_mean(mul(day_mean(High), sigmoid(day_durbin_watson(Low))), 241)` |
| knockout | `sigmoid(day_durbin_watson(Low))` | -1.84 | -1.84 | -0.42 | -1.44 | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), day_durbin_watson(Low)), 241)` |
| swap | `High->Low` | -3.34 | -3.34 | -2.25 | — | `cross_mean(mul(ts_regres(day_mean(Low), day_close(Amt), 50), sigmoid(day_durbin_watson(Low))), 241)` |
| swap | `Amt->Volume` | -2.63 | -2.63 | -2.57 | — | `cross_mean(mul(ts_regres(day_mean(High), day_close(Volume), 50), sigmoid(day_durbin_watson(Low))), 241)` |
| window | `cross_mean@241->120` | -3.13 | -3.13 | -2.60 | — | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), sigmoid(day_durbin_watson(Low))), 120)` |
| window | `cross_mean@241->482` | -3.08 | -3.08 | -2.07 | — | `cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), sigmoid(day_durbin_watson(Low))), 482)` |

### head score -3.49:`cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret))))), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret)))))` | -3.53 | -3.53 | -3.42 | — | (子树本身) |
| sufficiency | `sigmoid(pow_2(sigmoid(day_durbin_watson(Ret))))` | -3.54 | -3.54 | -3.41 | — | (子树本身) |
| sufficiency | `pow_2(sigmoid(day_durbin_watson(Ret)))` | -3.54 | -3.54 | -3.41 | — | (子树本身) |
| sufficiency | `sigmoid(day_durbin_watson(Ret))` | -3.54 | -3.54 | -3.41 | — | (子树本身) |
| knockout | `sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret)))))` | -3.48 | -3.48 | -3.38 | -0.00 | `cross_mean(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret)))), 3)` |
| knockout | `pow_2(sigmoid(day_durbin_watson(Ret)))` | -3.49 | -3.49 | -3.41 | +0.01 | `cross_mean(sigmoid(sigmoid(sigmoid(day_durbin_watson(Ret)))), 3)` |
| knockout | `sigmoid(day_durbin_watson(Ret))` | -3.73 | -3.51 | -3.73 | +0.25 | `cross_mean(sigmoid(sigmoid(pow_2(day_durbin_watson(Ret)))), 3)` |
| window | `cross_mean@3->2` | -3.47 | -3.47 | -3.44 | — | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret))))), 2)` |
| window | `cross_mean@3->6` | -3.44 | -3.44 | -3.38 | — | `cross_mean(sigmoid(sigmoid(pow_2(sigmoid(day_durbin_watson(Ret))))), 6)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241)` — enrichment,均值差 +1.55,p 0.005
2. `sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret))` — enrichment,均值差 +1.48,p 0.000
3. `sub(day_wmean(Ret, Amt), day_mean(Ret))` — enrichment,均值差 +1.44,p 0.000
4. `day_mean(Ret)` — enrichment,均值差 +1.23,p 0.000
5. `cross_mean(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret)), 241)` — enrichment,均值差 +1.21,p 0.018
6. `day_wmean(Ret, Amt)` — enrichment,均值差 +1.03,p 0.000
7. `day_wmean(Ret, div(Amt, cross_mean(Amt, 20)))` — enrichment,均值差 +0.80,p 0.000

## 本组之前各轮的任务

- `prods2009Pr1a_Ea`:核心 `log(log(day_durbin_watson(Volume)))`;评分 99,过线 0,入 heads 0;采样计数 {'c05_no_core': 1562, 'c05_skeleton': 736, 'c05_periphery_seen': 3}
  - score -0.69(train -0.69 valid -0.37):`cross_stddev(log(cross_mean(log(log(day_durbin_watson(Volume))), 120)), 60)`
  - score -0.82(train -0.82 valid +0.34):`cross_stddev(cross_stddev(log(cross_mean(log(log(day_durbin_watson(Volume))), 120)), 60), 60)`
  - score -0.96(train -0.96 valid -0.59):`cross_stddev(log(cross_mean(log(log(day_durbin_watson(Volume))), 120)), 5)`
  - score -1.10(train -0.99 valid -1.10):`cross_stddev(log(cross_mean(log(log(log(log(day_durbin_watson(Volume))))), 120)), 60)`
  - score -1.18(train -1.18 valid +0.11):`cross_stddev(cross_stddev(log(cross_med(log(log(day_durbin_watson(Volume))), 60)), 60), 60)`
- `prods2009Pr1b_Nb`:核心 `—`;评分 88,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -0.03(train -0.03 valid +0.23):`cross_mean(cross_mean(day_wmean(Ret, div(Amt, cross_mean(Close, 20))), 20), 241)`
  - score -0.05(train -0.05 valid +0.20):`cross_mean(cross_mean(day_wmean(Ret, add(Amt, Amt)), 20), 241)`
  - score -0.38(train -0.38 valid -0.25):`cross_mean(cross_mean(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), 20), 241)`
  - score -0.48(train -0.48 valid +0.65):`cross_mean(day_corr(div(Volume, cross_mean(Amt, 20)), Amt), 241)`
  - score -0.55(train -0.55 valid -0.03):`cross_mean(day_corr(sub(in_delay(Ret, 1), cross_mean(Amt, 20)), in_delay(Ret, 1)), 241)`
- `prods2009Pr2a_Ea`:核心 `day_wmean(Ret, div(Amt, cross_mean(Amt, 20)))`;评分 70,过线 0,入 heads 0;采样计数 {'c05_periphery_seen': 6, 'c05_no_core': 1587, 'c05_skeleton': 739, 'mutation_refused': 5}
  - score -0.34(train -0.34 valid -0.19):`cross_mean(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret)), 241)`
  - score -0.47(train -0.27 valid -0.47):`cross_mean(sub(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret)), day_mean(Ret)), 241)`
  - score -0.52(train -0.31 valid -0.52):`cross_mean(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), cross_mean(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret)), 241)), 241)`
  - score -0.55(train -0.55 valid -0.15):`cross_mean(add(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_mean(Ret)), 241)`
  - score -0.60(train -0.60 valid +0.62):`cross_mean(sub(day_wmean(Ret, div(Amt, cross_mean(Amt, 20))), day_wmean(Ret, Amt)), 241)`
- `prods2009Pr2b_Nb`:核心 `—`;评分 68,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score +0.07(train +0.07 valid +0.40):`cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241)`
  - score +0.06(train +0.06 valid +0.41):`cross_mean(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 10), 241)`
  - score -0.04(train -0.04 valid +0.59):`cross_mean(cross_mean(sub(day_wmean(Ret, Amt), day_mean(Ret)), 241), 5)`
  - score -0.04(train -0.04 valid +0.49):`cross_mean(cross_mean(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_mean(Ret)), 241), 5)`
  - score -0.05(train -0.05 valid +0.32):`cross_mean(sub(sub(day_wmean(Ret, Amt), day_mean(Ret)), day_mean(Ret)), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.44(knockout sigmoid(day_durbin_watson(Low))):`cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), day_durbin_watson(Low)), 241)`
- 增益 +0.64(swap Amt->Volume):`cross_mean(mul(ts_regres(day_mean(High), day_close(Volume), 50), sigmoid(day_durbin_watson(Low))), 241)`
- 增益 +0.19(window cross_mean@241->482):`cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), sigmoid(day_durbin_watson(Low))), 482)`
- 增益 +0.15(window cross_mean@241->120):`cross_mean(mul(ts_regres(day_mean(High), day_close(Amt), 50), sigmoid(day_durbin_watson(Low))), 120)`
