# 定位:种子 2018,P 组,第 3 轮(只含 train / valid)

快照:prods2018M1_I0_open_search, prods2018M2_I0_open_search, prods2018M3_I0_open_search, prods2018Pr1a_Ea, prods2018Pr1b_Nb, prods2018Pr2a_Ea, prods2018Pr2b_Nb;已生效的 R 替换 4 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.39 | -0.39 | -0.14 | +1 | 20 | prods2018M2_I0_open_search | `cross_mean(day_skew(Ret), 160)` |
| -0.71 | -0.43 | -0.71 | +1 | 0 | prods2018M2_I0_open_search | `ts_stddev(day_skew(Vwap), 160)` |
| -0.88 | -0.88 | -0.61 | +1 | 0 | prods2018M2_I0_open_search | `cross_mean(cross_stddev(day_skew(Open), 10), 241)` |
| -1.58 | -1.58 | -1.31 | +1 | 20 | prods2018M1_I0_open_search | `ts_std(cross_argmax(day_quantile(Vwap), 60), 25)` |
| -1.70 | -1.08 | -1.70 | +1 | 0 | prods2018M3_I0_open_search | `signedpower(signedpower(cross_quantile_q75(cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60), 30)))` |
| -1.80 | -1.80 | -1.61 | +1 | 5 | prods2018M3_I0_open_search | `signedpower(cross_quantile_q75(cross_corr(day_skew(Vwap), mul(day_mean(High), day_skew(High)), 10), 241))` |
| -2.00 | -1.67 | -2.00 | -1 | 0 | prods2018M3_I0_open_search | `pow_2(cross_product(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), 241))` |

## 共性:267 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.68 | 0.003 | 4 | -0.42 / -2.11 | `div(day_close(Close), cross_delay(cross_delay(day_close(Close), 1), 1))` |
| +1.68 | 0.003 | 4 | -0.42 / -2.11 | `cross_delay(cross_delay(day_close(Close), 1), 1)` |
| +1.42 | 0.000 | 141 | -1.41 / -2.83 | `day_close(Close)` |
| +1.26 | 0.000 | 65 | -1.13 / -2.39 | `div(day_close(Close), cross_delay(day_close(Close), 1))` |
| +1.22 | 0.000 | 83 | -1.24 / -2.46 | `cross_delay(day_close(Close), 1)` |
| +1.05 | 0.000 | 110 | -1.46 / -2.51 | `day_quantile(Open)` |
| +1.05 | 0.000 | 110 | -1.46 / -2.51 | `cross_argmax(day_quantile(Open), 60)` |
| +1.00 | 0.042 | 5 | -1.09 / -2.10 | `cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120))` |
| +0.88 | 0.023 | 5 | -1.21 / -2.10 | `cs_scale(day_durbin_watson(High))` |
| +0.71 | 0.040 | 7 | -1.39 / -2.10 | `day_durbin_watson(High)` |
| +0.66 | 0.071 | 4 | -1.43 / -2.09 | `ts_sum(cs_scale(day_durbin_watson(High)), 5)` |
| +0.54 | 0.175 | 4 | -1.55 / -2.09 | `cross_ema(cross_argmax(day_quantile(Open), 60), 60)` |
| +0.46 | 0.128 | 11 | -1.64 / -2.10 | `div(day_close(Close), day_open(Open))` |
| +0.45 | 0.109 | 15 | -1.65 / -2.11 | `day_open(Open)` |
| +0.44 | 0.157 | 8 | -1.65 / -2.09 | `sub(log(day_close(Close)), cross_delay(log(day_close(Close)), 120))` |
| +0.44 | 0.157 | 8 | -1.65 / -2.09 | `cross_delay(log(day_close(Close)), 120)` |
| +0.43 | 0.255 | 14 | -1.67 / -2.10 | `cs_quantile_q25(LogFloatShares)` |
| +0.42 | 0.263 | 5 | -1.67 / -2.09 | `log(cross_semistd_pos(day_close(Close), 60))` |
| +0.35 | 0.201 | 12 | -1.74 / -2.10 | `log(day_close(Close))` |
| +0.31 | 0.402 | 5 | -1.77 / -2.09 | `day_sum(Amt)` |

## 拆解(23 次评估)

### head score -0.39:`cross_mean(day_skew(Ret), 160)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_skew(Ret)` | -3.46 | -3.46 | -2.74 | — | (子树本身) |
| window | `cross_mean@160->80` | -0.58 | -0.58 | -0.39 | — | `cross_mean(day_skew(Ret), 80)` |
| window | `cross_mean@160->320` | -0.47 | -0.47 | +0.19 | — | `cross_mean(day_skew(Ret), 320)` |

### head score -0.71:`ts_stddev(day_skew(Vwap), 160)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_skew(Vwap)` | -4.89 | -4.89 | -3.99 | — | (子树本身) |
| swap | `Vwap->Close` | -0.88 | -0.34 | -0.88 | — | `ts_stddev(day_skew(Close), 160)` |
| window | `ts_stddev@160->80` | -1.33 | -1.00 | -1.33 | — | `ts_stddev(day_skew(Vwap), 80)` |
| window | `ts_stddev@160->320` | -0.48 | -0.28 | -0.48 | — | `ts_stddev(day_skew(Vwap), 320)` |

### head score -0.88:`cross_mean(cross_stddev(day_skew(Open), 10), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(day_skew(Open), 10)` | -1.84 | -1.84 | -1.72 | — | (子树本身) |
| sufficiency | `day_skew(Open)` | -4.84 | -4.84 | -3.72 | — | (子树本身) |
| knockout | `cross_stddev(day_skew(Open), 10)` | -2.60 | -2.60 | -1.44 | +1.73 | `cross_mean(day_skew(Open), 241)` |
| swap | `Open->Close` | -0.50 | -0.50 | -0.30 | — | `cross_mean(cross_stddev(day_skew(Close), 10), 241)` |
| window | `cross_mean@241->120` | -1.17 | -1.17 | -1.15 | — | `cross_mean(cross_stddev(day_skew(Open), 10), 120)` |
| window | `cross_mean@241->482` | -1.34 | -1.34 | -1.02 | — | `cross_mean(cross_stddev(day_skew(Open), 10), 482)` |

### head score -1.70:`signedpower(signedpower(cross_quantile_q75(cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60), 30)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `signedpower(cross_quantile_q75(cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60), 30))` | -1.62 | -1.04 | -1.62 | — | (子树本身) |
| sufficiency | `cross_quantile_q75(cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60), 30)` | -1.62 | -1.04 | -1.62 | — | (子树本身) |
| sufficiency | `cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60)` | -1.85 | -1.01 | -1.85 | — | (子树本身) |
| sufficiency | `cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10)` | -2.92 | -2.36 | -2.92 | — | (子树本身) |
| knockout | `cross_quantile_q75(cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60), 30)` | -1.85 | -1.01 | -1.85 | +0.15 | `signedpower(signedpower(cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60)))` |
| knockout | `cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60)` | -2.86 | -2.59 | -2.86 | +1.16 | `signedpower(signedpower(cross_quantile_q75(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), 30)))` |
| knockout | `cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10)` | -3.41 | -2.11 | -3.41 | +1.71 | `signedpower(signedpower(cross_quantile_q75(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 60), 30)))` |
| swap | `High->Low` | -1.49 | -0.83 | -1.49 | — | `signedpower(signedpower(cross_quantile_q75(cross_corr(cross_corr(day_skew(Low), mul(day_mean(Low), day_skew(Low)), 10), mul(day_mean(Low), day_skew(Low)), 60), 30)))` |
| window | `cross_quantile_q75@30->15` | -2.16 | -1.12 | -2.16 | — | `signedpower(signedpower(cross_quantile_q75(cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60), 15)))` |
| window | `cross_quantile_q75@30->60` | -2.08 | -1.32 | -2.08 | — | `signedpower(signedpower(cross_quantile_q75(cross_corr(cross_corr(day_skew(High), mul(day_mean(High), day_skew(High)), 10), mul(day_mean(High), day_skew(High)), 60), 60)))` |

## 机械核心卡(B0 按这个顺序取)

1. `div(day_close(Close), cross_delay(cross_delay(day_close(Close), 1), 1))` — enrichment,均值差 +1.68,p 0.003
2. `cross_delay(cross_delay(day_close(Close), 1), 1)` — enrichment,均值差 +1.68,p 0.003
3. `day_close(Close)` — enrichment,均值差 +1.42,p 0.000
4. `div(day_close(Close), cross_delay(day_close(Close), 1))` — enrichment,均值差 +1.26,p 0.000
5. `cross_delay(day_close(Close), 1)` — enrichment,均值差 +1.22,p 0.000
6. `day_quantile(Open)` — enrichment,均值差 +1.05,p 0.000
7. `cross_argmax(day_quantile(Open), 60)` — enrichment,均值差 +1.05,p 0.000
8. `cs_first_high40(cs_quantile_q25(LogFloatShares), cross_semistd_pos(day_close(Close), 120))` — enrichment,均值差 +1.00,p 0.042
9. `cs_scale(day_durbin_watson(High))` — enrichment,均值差 +0.88,p 0.023
10. `day_durbin_watson(High)` — enrichment,均值差 +0.71,p 0.040
11. `ts_sum(cs_scale(day_durbin_watson(High)), 5)` — enrichment,均值差 +0.66,p 0.071

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
- `prods2018Pr2a_Ea`:核心 `cross_argmax(day_quantile(Open), 60)`;评分 99,过线 0,入 heads 0;采样计数 {'c05_no_core': 1415, 'c05_skeleton': 712, 'c05_periphery_seen': 3, 'mutation_refused': 1}
  - score +0.06(train +0.09 valid +0.06):`div(cross_regalpha(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 120), add(cross_stddev(sub(div(day_close(Close), cross_delay(day_quantile(Open), 1)), -5), 120), 0.0001))`
  - score +0.00(train +0.67 valid +0.00):`div(cross_regalpha(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 120), add(cross_stddev(sub(div(day_close(Close), cross_delay(cross_argmax(day_quantile(Open), 60), 1)), -5), 120), 0.5))`
  - score -0.03(train +0.01 valid -0.03):`div(cross_regalpha(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_delay(cross_delay(day_close(Close), 1), 1)), 1), 120), add(cross_stddev(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), -5), 120), 0.0001))`
  - score -0.05(train +0.08 valid -0.05):`div(cross_regalpha(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 120), add(cross_stddev(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), -5), 120), add(cross_stddev(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), -5), 120), 0.0001)))`
  - score -0.05(train +0.09 valid -0.05):`div(cross_regalpha(cross_argmax(day_quantile(Open), 60), sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), 120), add(cross_stddev(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), -5), 120), 0.0001))`
- `prods2018Pr2b_Nb`:核心 `—`;评分 77,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1}
  - score +0.10(train +0.31 valid +0.10):`cross_max(sub(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LimitWidth), 60)`
  - score +0.00(train +0.75 valid +0.00):`cross_max(cross_max(div(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LimitWidth), 60), 60)`
  - score -0.22(train +0.47 valid -0.22):`cross_max(cross_max(div(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LimitWidth), 5), 60)`
  - score -0.26(train +0.01 valid -0.26):`cross_max(cross_max(div(cross_max(div(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LimitWidth), 60), LimitWidth), 60), 60)`
  - score -0.32(train -0.01 valid -0.32):`cross_max(div(sub(div(day_close(Close), cross_delay(day_close(Close), 1)), 1), LimitWidth), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.38(swap Open->Close):`cross_mean(cross_stddev(day_skew(Close), 10), 241)`
- 增益 +0.23(window ts_stddev@160->320):`ts_stddev(day_skew(Vwap), 320)`
- 增益 +0.21(swap High->Low):`signedpower(signedpower(cross_quantile_q75(cross_corr(cross_corr(day_skew(Low), mul(day_mean(Low), day_skew(Low)), 10), mul(day_mean(Low), day_skew(Low)), 60), 30)))`
