# 定位:种子 2018,P 组,第 2 轮(只含 train / valid)

快照:prods2018M1_I0_open_search, prods2018M2_I0_open_search, prods2018Pr1a_Ea, prods2018Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(4 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.46 | -1.46 | -1.00 | +1 | 20 | prods2018M2_I0_open_search | `cross_mean(day_skew(Ret), 20)` |
| -1.50 | -1.35 | -1.50 | +1 | 20 | prods2018M2_I0_open_search | `ts_stddev(day_skew(Vwap), 20)` |
| -1.57 | -1.39 | -1.57 | +1 | 5 | prods2018M2_I0_open_search | `signedpower(cross_quantile_q75(cross_reg_fvalue(day_skew(Open), day_skew(Open), 10), 241))` |
| -1.58 | -1.58 | -1.31 | +1 | 20 | prods2018M1_I0_open_search | `ts_std(cross_argmax(day_quantile(Vwap), 60), 25)` |

## 共性:139 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.32 | 0.007 | 5 | -1.09 / -2.41 | `cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120))` |
| +1.30 | 0.000 | 13 | -1.18 / -2.49 | `cross_delay(day_close(Close), 1)` |
| +1.20 | 0.000 | 58 | -1.66 / -2.87 | `day_close(Close)` |
| +1.11 | 0.002 | 10 | -1.34 / -2.44 | `div(day_close(Close), cross_delay(day_close(Close), 1))` |
| +1.03 | 0.000 | 51 | -1.71 / -2.74 | `cross_argmax(day_quantile(Open), 60)` |
| +1.03 | 0.000 | 51 | -1.71 / -2.74 | `day_quantile(Open)` |
| +0.84 | 0.042 | 4 | -1.55 / -2.39 | `cross_ema(cross_argmax(day_quantile(Open), 60), 60)` |
| +0.77 | 0.042 | 14 | -1.67 / -2.44 | `cs_quantile_q25(LogFloatShares)` |
| +0.76 | 0.013 | 8 | -1.65 / -2.41 | `sub(log(day_close(Close)), cross_delay(log(day_close(Close)), 120))` |
| +0.76 | 0.013 | 8 | -1.65 / -2.41 | `cross_delay(log(day_close(Close)), 120)` |
| +0.72 | 0.064 | 5 | -1.67 / -2.39 | `log(cross_semistd_pos(day_close(Close), 60))` |
| +0.66 | 0.016 | 19 | -1.80 / -2.45 | `cross_semistd_pos(day_close(Close), 120)` |
| +0.61 | 0.027 | 11 | -1.80 / -2.41 | `log(day_close(Close))` |
| +0.53 | 0.144 | 6 | -1.86 / -2.39 | `cross_semistd_pos(day_close(Close), 60)` |
| +0.51 | 0.199 | 4 | -1.87 / -2.38 | `cs_rank(cross_argmax(day_quantile(Open), 60))` |
| +0.50 | 0.143 | 4 | -1.88 / -2.38 | `abs_(cross_delta(log(day_close(Close)), 1))` |
| +0.50 | 0.143 | 4 | -1.88 / -2.38 | `cross_delta(log(day_close(Close)), 1)` |
| +0.41 | 0.365 | 5 | -1.97 / -2.38 | `add(cross_semistd_pos(day_close(Close), 120), cross_semistd_neg(day_close(Close), 120))` |
| +0.19 | 0.411 | 10 | -2.19 / -2.38 | `cross_semistd_neg(day_close(Close), 120)` |
| -0.57 | 0.965 | 8 | -2.90 / -2.33 | `day_skew(Vwap)` |

## 拆解(21 次评估)

### head score -1.46:`cross_mean(day_skew(Ret), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_skew(Ret)` | -3.46 | -3.46 | -2.74 | — | (子树本身) |
| window | `cross_mean@20->10` | -1.76 | -1.76 | -0.81 | — | `cross_mean(day_skew(Ret), 10)` |
| window | `cross_mean@20->40` | -1.16 | -1.16 | -0.79 | — | `cross_mean(day_skew(Ret), 40)` |

### head score -1.50:`ts_stddev(day_skew(Vwap), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_skew(Vwap)` | -4.89 | -4.89 | -3.99 | — | (子树本身) |
| swap | `Vwap->Close` | -1.42 | -1.42 | -1.41 | — | `ts_stddev(day_skew(Close), 20)` |
| window | `ts_stddev@20->10` | -1.65 | -1.65 | -1.35 | — | `ts_stddev(day_skew(Vwap), 10)` |
| window | `ts_stddev@20->40` | -1.73 | -1.10 | -1.73 | — | `ts_stddev(day_skew(Vwap), 40)` |

### head score -1.57:`signedpower(cross_quantile_q75(cross_reg_fvalue(day_skew(Open), day_skew(Open), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_quantile_q75(cross_reg_fvalue(day_skew(Open), day_skew(Open), 10), 241)` | -1.50 | -1.39 | -1.50 | — | (子树本身) |
| sufficiency | `cross_reg_fvalue(day_skew(Open), day_skew(Open), 10)` | -1.79 | -1.79 | -1.74 | — | (子树本身) |
| sufficiency | `day_skew(Open)` | -4.84 | -4.84 | -3.72 | — | (子树本身) |
| knockout | `cross_quantile_q75(cross_reg_fvalue(day_skew(Open), day_skew(Open), 10), 241)` | -1.79 | -1.79 | -1.74 | +0.22 | `signedpower(cross_reg_fvalue(day_skew(Open), day_skew(Open), 10))` |
| knockout | `cross_reg_fvalue(day_skew(Open), day_skew(Open), 10)` | -2.54 | -2.54 | -2.52 | +0.97 | `signedpower(cross_quantile_q75(day_skew(Open), 241))` |
| swap | `Open->Close` | -1.47 | -1.25 | -1.47 | — | `signedpower(cross_quantile_q75(cross_reg_fvalue(day_skew(Close), day_skew(Close), 10), 241))` |
| window | `cross_quantile_q75@241->120` | -1.68 | -1.56 | -1.68 | — | `signedpower(cross_quantile_q75(cross_reg_fvalue(day_skew(Open), day_skew(Open), 10), 120))` |
| window | `cross_quantile_q75@241->482` | -1.88 | -1.88 | -1.63 | — | `signedpower(cross_quantile_q75(cross_reg_fvalue(day_skew(Open), day_skew(Open), 10), 482))` |

### head score -1.58:`ts_std(cross_argmax(day_quantile(Vwap), 60), 25)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_argmax(day_quantile(Vwap), 60)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_quantile(Vwap)` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `cross_argmax(day_quantile(Vwap), 60)` | -2.27 | -1.80 | -2.27 | +0.69 | `ts_std(day_quantile(Vwap), 25)` |
| swap | `Vwap->Close` | -1.61 | -1.61 | -1.21 | — | `ts_std(cross_argmax(day_quantile(Close), 60), 25)` |
| window | `ts_std@25->12` | — | — | — | — | `ts_std(cross_argmax(day_quantile(Vwap), 60), 12)` |
| window | `ts_std@25->50` | -2.07 | -1.50 | -2.07 | — | `ts_std(cross_argmax(day_quantile(Vwap), 60), 50)` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120))` — enrichment,均值差 +1.32,p 0.007
2. `cross_delay(day_close(Close), 1)` — enrichment,均值差 +1.30,p 0.000
3. `day_close(Close)` — enrichment,均值差 +1.20,p 0.000
4. `div(day_close(Close), cross_delay(day_close(Close), 1))` — enrichment,均值差 +1.11,p 0.002
5. `cross_argmax(day_quantile(Open), 60)` — enrichment,均值差 +1.03,p 0.000
6. `day_quantile(Open)` — enrichment,均值差 +1.03,p 0.000
7. `cross_ema(cross_argmax(day_quantile(Open), 60), 60)` — enrichment,均值差 +0.84,p 0.042
8. `sub(log(day_close(Close)), cross_delay(log(day_close(Close)), 120))` — enrichment,均值差 +0.76,p 0.013
9. `cross_delay(log(day_close(Close)), 120)` — enrichment,均值差 +0.76,p 0.013
10. `log(cross_semistd_pos(day_close(Close), 60))` — enrichment,均值差 +0.72,p 0.064
11. `cross_semistd_pos(day_close(Close), 120)` — enrichment,均值差 +0.66,p 0.016
12. `log(day_close(Close))` — enrichment,均值差 +0.61,p 0.027

## 本组之前各轮的任务

- `prods2018Pr1a_Ea`:核心 `cross_argmax(day_quantile(Open), 60)`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 659, 'c05_no_core': 1326, 'mutation_refused': 3}
  - score -0.39(train -0.39 valid -0.36):`cross_regbeta(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_min(day_close(Close), 3)), 1), 120)`
  - score -0.40(train -0.40 valid -0.23):`cross_regbeta(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Open), cross_delay(day_close(Close), 1)), 1), 120)`
  - score -0.41(train -0.41 valid -0.24):`cross_regbeta(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 120)`
  - score -0.41(train -0.41 valid -0.24):`cross_regbeta(cross_argmax(day_quantile(Open), 60), div(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 120)`
  - score -0.46(train -0.24 valid -0.46):`cross_regbeta(cross_argmax(day_quantile(Open), 60), sub(day_es_ratio_lo(div(Vwap, Ret)), 1), 120)`
- `prods2018Pr1b_Nb`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.81(train -0.70 valid -0.81):`sub(2, cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120)))`
  - score -0.81(train -0.70 valid -0.81):`sub(-2, cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120)))`
  - score -0.81(train -0.70 valid -0.81):`cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120))`
  - score -0.81(train -0.70 valid -0.81):`sub(0.5, cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120)))`
  - score -0.81(train -0.70 valid -0.81):`sub(sub(2, cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120))), cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120)))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.30(window cross_mean@20->40):`cross_mean(day_skew(Ret), 40)`
