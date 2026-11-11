# 定位:种子 2022,P 组,第 3 轮(只含 train / valid)

快照:prods2022M1_I0_open_search, prods2022M2_I0_open_search, prods2022M3_I0_open_search, prods2022Pr1a_Ea, prods2022Pr1b_Nb, prods2022Pr2b_Nb;已生效的 R 替换 3 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.02 | -2.02 | -1.96 | -1 | 5 | prods2022M1_I0_open_search | `ts_pearson(day_argmin(Low), 20)` |
| -2.49 | -2.34 | -2.49 | -1 | 20 | prods2022M1_I0_open_search | `ts_pearson(mul(log(day_argmin(Low)), 1), 10)` |
| -2.58 | -2.17 | -2.58 | -1 | 20 | prods2022M1_I0_open_search | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)` |

## 共性:172 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.18 | 0.013 | 5 | -1.12 / -2.30 | `day_argmin(sub(day_argmin(Low), Volume))` |
| +1.03 | 0.000 | 36 | -1.45 / -2.48 | `day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))` |
| +0.86 | 0.000 | 34 | -1.57 / -2.43 | `day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237)))` |
| +0.77 | 0.033 | 7 | -1.52 / -2.29 | `day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241))` |
| +0.74 | 0.001 | 42 | -1.70 / -2.44 | `day_argmax(in_slice(High, 2, 237))` |
| +0.61 | 0.002 | 64 | -1.88 / -2.49 | `day_argmin(in_slice(Low, 2, 237))` |
| +0.57 | 0.011 | 43 | -1.84 / -2.40 | `day_mean(in_slice(Amt, 2, 237))` |
| +0.28 | 0.114 | 57 | -2.07 / -2.36 | `day_argmin(Low)` |
| +0.23 | 0.358 | 6 | -2.04 / -2.27 | `cs_rank(day_argmax(in_slice(Amt, 2, 237)))` |
| +0.23 | 0.320 | 15 | -2.05 / -2.28 | `day_gini(Vwap)` |
| +0.14 | 0.445 | 9 | -2.13 / -2.27 | `log(day_gini(Vwap))` |
| +0.09 | 0.468 | 6 | -2.18 / -2.26 | `cs_rank(day_argmin(in_slice(Low, 2, 237)))` |
| +0.06 | 0.458 | 4 | -2.20 / -2.26 | `sub(day_locate(in_slice(Close, 2, 237), add(day_argmin(in_slice(Low, 2, 237)), 10)), day_min(in_slice(Low, 2, 237)))` |
| +0.06 | 0.458 | 4 | -2.20 / -2.26 | `day_locate(in_slice(Close, 2, 237), add(day_argmin(in_slice(Low, 2, 237)), 10))` |
| +0.06 | 0.458 | 4 | -2.20 / -2.26 | `div(sub(day_locate(in_slice(Close, 2, 237), add(day_argmin(in_slice(Low, 2, 237)), 10)), day_min(in_slice(Low, 2, 237))), sub(day_max(in_slice(High, 2, 237)), day_min(in_slice(Low, 2, 237))))` |
| +0.00 | 0.525 | 7 | -2.26 / -2.26 | `day_max(in_slice(High, 2, 237))` |
| +0.00 | 0.525 | 7 | -2.26 / -2.26 | `day_min(in_slice(Low, 2, 237))` |
| +0.00 | 0.525 | 7 | -2.26 / -2.26 | `sub(day_max(in_slice(High, 2, 237)), day_min(in_slice(Low, 2, 237)))` |
| -0.04 | 0.589 | 37 | -2.29 / -2.25 | `day_argmax(in_slice(Amt, 2, 237))` |
| -0.11 | 0.685 | 4 | -2.37 / -2.26 | `day_argmax(High)` |

## 拆解(4 次评估)

### head score -2.02:`ts_pearson(day_argmin(Low), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_argmin(Low)` | — | — | — | — | 门槛废品 |
| swap | `Low->High` | -1.91 | -1.91 | -1.85 | — | `ts_pearson(day_argmin(High), 20)` |
| window | `ts_pearson@20->10` | -2.35 | -2.25 | -2.35 | — | `ts_pearson(day_argmin(Low), 10)` |
| window | `ts_pearson@20->40` | -2.26 | -2.26 | -2.16 | — | `ts_pearson(day_argmin(Low), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_argmin(sub(day_argmin(Low), Volume))` — enrichment,均值差 +1.18,p 0.013
2. `day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))` — enrichment,均值差 +1.03,p 0.000
3. `day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237)))` — enrichment,均值差 +0.86,p 0.000
4. `day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241))` — enrichment,均值差 +0.77,p 0.033
5. `day_argmax(in_slice(High, 2, 237))` — enrichment,均值差 +0.74,p 0.001
6. `day_argmin(in_slice(Low, 2, 237))` — enrichment,均值差 +0.61,p 0.002
7. `day_mean(in_slice(Amt, 2, 237))` — enrichment,均值差 +0.57,p 0.011

## 本组之前各轮的任务

- `prods2022Pr1a_Ea`:核心 `day_argmin(Low)`;评分 95,过线 0,入 heads 0;采样计数 {'c05_skeleton': 594, 'c05_no_core': 1231}
  - score -1.06(train -1.06 valid -0.69):`day_mean(cross_cov(sub(day_pos_ratio(sub(day_argmin(Low), Volume)), Volume), pow_1_5(Low), 241))`
  - score -1.07(train -1.07 valid -0.69):`day_mean(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241))`
  - score -1.08(train -1.08 valid -0.70):`day_mean(cross_cov(sub(day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 5)), Volume), pow_1_5(Low), 241))`
  - score -1.08(train -1.08 valid -0.68):`day_mean(cross_cov(sub(day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241)), Volume), pow_1_5(Low), 241))`
  - score -1.08(train -1.08 valid -0.67):`day_mean(cross_cov(sub(day_argmin(cross_cov(sub(day_argmin(cross_cov(sub(day_argmin(Low), sub(day_argmin(cross_cov(sub(day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241)), Volume), pow_1_5(Low), 241)), Volume)), pow_1_5(Low), 241)), sub(day_argmin(cross_cov(sub(day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241)), Volume), pow_1_5(Low), 241)), Volume)), pow_1_5(Low), 241)), sub(day_argmin(cross_cov(sub(day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241)), Volume), pow_1_5(Low), 241)), Volume)), pow_1_5(Low), 241))`
- `prods2022Pr1b_Nb`:核心 `—`;评分 93,过线 0,入 heads 0;采样计数 {'c05_skeleton': 3}
  - score -0.36(train -0.36 valid -0.35):`cross_mean(sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 5))))))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 5)))), 120)`
  - score -0.36(train -0.36 valid -0.35):`cross_mean(sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 2))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 5))))))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 5)))), 120)`
  - score -0.36(train -0.36 valid -0.36):`cross_mean(sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), day_argmin(Amt)))))))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), day_argmin(Amt))))), 120)`
  - score -0.36(train -0.36 valid -0.36):`cross_mean(sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), sub(pow_05(sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1))))))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1))))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1))))))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1)))), 120)`
  - score -0.37(train -0.37 valid -0.36):`cross_mean(sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), sub(pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1))))))), pow_05(div(day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237))), add(day_mean(in_slice(Amt, 2, 237)), 1)))), 120)`
- `prods2022Pr2b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.70(train -0.56 valid -0.70):`cross_corr(day_argmax(in_slice(Amt, 2, 237)), day_gini(Vwap), 10)`
  - score -0.76(train -0.61 valid -0.76):`cross_corr(day_argmax(in_slice(Amt, 2, 237)), day_gini(Low), 10)`
  - score -0.94(train -0.73 valid -0.94):`cross_stddev(sub(cs_rank(day_argmax(in_slice(Amt, 2, 237))), cs_rank(day_argmin(in_slice(Low, 2, 237)))), 120)`
  - score -0.99(train -0.46 valid -0.99):`cross_corr(day_argmax(in_slice(Volume, 2, 237)), day_gini(Vwap), 10)`
  - score -1.13(train -0.73 valid -1.13):`cross_corr(day_argmax(in_slice(Amt, 2, 237)), day_argmin(in_slice(Low, 2, 237)), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.11(swap Low->High):`ts_pearson(day_argmin(High), 20)`
