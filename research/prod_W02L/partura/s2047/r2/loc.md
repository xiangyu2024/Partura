# 定位:种子 2047,P 组,第 2 轮(只含 train / valid)

快照:prods2047M1_I0_open_search, prods2047M2_I0_open_search, prods2047Pr1a_Na, prods2047Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.71 | -0.71 | -0.68 | +1 | 5 | prods2047M1_I0_open_search | `cross_corr(day_min(High), day_mean(Amt), 60)` |
| -1.34 | -1.34 | -1.19 | +1 | 20 | prods2047M1_I0_open_search | `pow_3(cross_hurst(neg(day_min(Ret)), 15))` |
| -2.35 | -1.56 | -2.35 | -1 | 20 | prods2047M1_I0_open_search | `add(day_min(Ret), day_var(Open))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M2_I0_open_search | `sqrt(sqrt(sigmoid(day_min(Ret))))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M2_I0_open_search | `sqrt(sigmoid(day_min(Ret)))` |
| -2.82 | -2.19 | -2.82 | +1 | 20 | prods2047M2_I0_open_search | `pow_1_5(pow_2(sqrt(sigmoid(day_min(Ret)))))` |

## 共性:168 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.09 | 0.019 | 5 | -1.25 / -2.34 | `day_centroid(mul(2, cross_delta(Close, 30)))` |
| +0.98 | 0.000 | 48 | -1.61 / -2.59 | `day_sum(Ret)` |
| +0.91 | 0.017 | 7 | -1.44 / -2.35 | `ts_med(day_ar1_coefficient(Close), 1)` |
| +0.91 | 0.017 | 7 | -1.44 / -2.35 | `cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20)` |
| +0.87 | 0.000 | 24 | -1.57 / -2.43 | `cross_delay(day_min(Ret), 1)` |
| +0.83 | 0.079 | 4 | -1.50 / -2.33 | `sub(day_max(Low), cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20))` |
| +0.81 | 0.015 | 12 | -1.56 / -2.37 | `day_max(Low)` |
| +0.80 | 0.023 | 8 | -1.55 / -2.35 | `day_ar1_coefficient(Close)` |
| +0.80 | 0.030 | 4 | -1.53 / -2.33 | `log(div(day_max(High), day_min(Low)))` |
| +0.80 | 0.030 | 4 | -1.53 / -2.33 | `div(day_max(High), day_min(Low))` |
| +0.77 | 0.053 | 5 | -1.56 / -2.33 | `day_at_max_ratio(Open)` |
| +0.65 | 0.027 | 7 | -1.69 / -2.33 | `cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_sum(Ret))), 120)` |
| +0.57 | 0.035 | 11 | -1.77 / -2.34 | `pow_2(day_argmin(High))` |
| +0.57 | 0.049 | 21 | -1.81 / -2.38 | `sub(day_last(Close), day_min(Low))` |
| +0.53 | 0.015 | 16 | -1.82 / -2.36 | `sub(day_sum(Ret), cs_mean(day_sum(Ret)))` |
| +0.48 | 0.115 | 4 | -1.83 / -2.32 | `log(day_sum(Vwap))` |
| +0.48 | 0.059 | 12 | -1.86 / -2.34 | `day_argmin(High)` |
| +0.45 | 0.036 | 25 | -1.92 / -2.37 | `day_max(High)` |
| +0.35 | 0.032 | 21 | -2.00 / -2.35 | `cs_mean(day_sum(Ret))` |
| +0.31 | 0.230 | 14 | -2.02 / -2.33 | `day_max(Close)` |

## 拆解(20 次评估)

### head score -0.71:`cross_corr(day_min(High), day_mean(Amt), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_min(High)` | -2.37 | -1.61 | -2.37 | — | (子树本身) |
| sufficiency | `day_mean(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| swap | `High->Low` | -0.74 | -0.74 | -0.67 | — | `cross_corr(day_min(Low), day_mean(Amt), 60)` |
| swap | `Amt->Volume` | -0.82 | -0.82 | -0.63 | — | `cross_corr(day_min(High), day_mean(Volume), 60)` |
| window | `cross_corr@60->30` | -0.98 | -0.28 | -0.98 | — | `cross_corr(day_min(High), day_mean(Amt), 30)` |
| window | `cross_corr@60->120` | -1.13 | -1.13 | -0.93 | — | `cross_corr(day_min(High), day_mean(Amt), 120)` |

### head score -2.82:`sqrt(sqrt(sigmoid(day_min(Ret))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sqrt(sigmoid(day_min(Ret)))` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| sufficiency | `sigmoid(day_min(Ret))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `day_min(Ret)` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| knockout | `sigmoid(day_min(Ret))` | -2.77 | -2.19 | -2.77 | -0.05 | `sqrt(sqrt(day_min(Ret)))` |

### head score -2.82:`sqrt(sigmoid(day_min(Ret)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(day_min(Ret))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `day_min(Ret)` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| knockout | `sigmoid(day_min(Ret))` | -2.77 | -2.19 | -2.77 | -0.05 | `sqrt(day_min(Ret))` |

### head score -2.82:`pow_1_5(pow_2(sqrt(sigmoid(day_min(Ret)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(sqrt(sigmoid(day_min(Ret))))` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| sufficiency | `sqrt(sigmoid(day_min(Ret)))` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| sufficiency | `sigmoid(day_min(Ret))` | -2.77 | -2.18 | -2.77 | — | (子树本身) |
| sufficiency | `day_min(Ret)` | -2.77 | -2.19 | -2.77 | — | (子树本身) |
| knockout | `pow_2(sqrt(sigmoid(day_min(Ret))))` | -2.77 | -2.19 | -2.77 | -0.05 | `pow_1_5(sqrt(sigmoid(day_min(Ret))))` |
| knockout | `sqrt(sigmoid(day_min(Ret)))` | -2.77 | -2.18 | -2.77 | -0.05 | `pow_1_5(pow_2(sigmoid(day_min(Ret))))` |
| knockout | `sigmoid(day_min(Ret))` | -2.77 | -2.19 | -2.77 | -0.05 | `pow_1_5(pow_2(sqrt(day_min(Ret))))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_centroid(mul(2, cross_delta(Close, 30)))` — enrichment,均值差 +1.09,p 0.019
2. `day_sum(Ret)` — enrichment,均值差 +0.98,p 0.000
3. `ts_med(day_ar1_coefficient(Close), 1)` — enrichment,均值差 +0.91,p 0.017
4. `cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20)` — enrichment,均值差 +0.91,p 0.017
5. `cross_delay(day_min(Ret), 1)` — enrichment,均值差 +0.87,p 0.000
6. `sub(day_max(Low), cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20))` — enrichment,均值差 +0.83,p 0.079
7. `day_max(Low)` — enrichment,均值差 +0.81,p 0.015
8. `day_ar1_coefficient(Close)` — enrichment,均值差 +0.80,p 0.023
9. `log(div(day_max(High), day_min(Low)))` — enrichment,均值差 +0.80,p 0.030
10. `div(day_max(High), day_min(Low))` — enrichment,均值差 +0.80,p 0.030
11. `day_at_max_ratio(Open)` — enrichment,均值差 +0.77,p 0.053
12. `cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_sum(Ret))), 120)` — enrichment,均值差 +0.65,p 0.027
13. `pow_2(day_argmin(High))` — enrichment,均值差 +0.57,p 0.035
14. `sub(day_last(Close), day_min(Low))` — enrichment,均值差 +0.57,p 0.049
15. `sub(day_sum(Ret), cs_mean(day_sum(Ret)))` — enrichment,均值差 +0.53,p 0.015
16. `day_argmin(High)` — enrichment,均值差 +0.48,p 0.059
17. `day_max(High)` — enrichment,均值差 +0.45,p 0.036
18. `cs_mean(day_sum(Ret))` — enrichment,均值差 +0.35,p 0.032

## 本组之前各轮的任务

- `prods2047Pr1a_Na`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.32(train +0.11 valid -0.32):`cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_sum(Ret))), 120)`
  - score -0.49(train -0.24 valid -0.49):`cross_regbeta(cross_delay(day_min(Ret), 1), day_sum(Ret), 120)`
  - score -0.57(train -0.10 valid -0.57):`cross_reg_tvalue(cross_delay(day_min(Ret), 1), day_sum(Ret), 120)`
  - score -0.67(train -0.41 valid -0.67):`cross_reg_tvalue(cross_delay(day_min(Ret), 1), sub(day_sum(Ret), cs_mean(day_min(Ret))), 120)`
  - score -0.69(train -0.21 valid -0.69):`cross_corr(cross_delay(day_min(Ret), 1), day_sum(Ret), 120)`
- `prods2047Pr1b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1}
  - score -0.20(train +0.31 valid -0.20):`cross_regbeta(cross_delay(div(sub(day_last(Close), day_min(Low)), sub(day_centroid(mul(-0.5, cross_delta(Close, 30))), cross_mean(ts_med(day_ar1_coefficient(Close), 1), 20))), 1), day_sum(Ret), 120)`
  - score -0.21(train +0.14 valid -0.21):`cross_regbeta(cross_delay(mul(sub(day_last(Close), day_min(Low)), sub(day_max(Low), sub(day_max(High), day_min(Low)))), 1), day_sum(Ret), 120)`
  - score -0.43(train -0.43 valid -0.41):`cross_regbeta(day_max(High), sub(day_centroid(mul(2, cross_delta(Close, 30))), 1), 120)`
  - score -0.43(train -0.43 valid -0.41):`cross_regbeta(day_max(High), sub(day_centroid(mul(-0.5, cross_delta(Close, 30))), 1), 120)`
  - score -0.49(train -0.49 valid -0.30):`cross_regbeta(cross_delay(day_max(High), 1), sub(day_centroid(mul(2, cross_delta(Close, 30))), 1), 120)`

## 比原 head 好的拆解变体(R 候选)

(没有)
