# 定位:种子 2022,P 组,第 2 轮(只含 train / valid)

快照:prods2022M1_I0_open_search, prods2022M2_I0_open_search, prods2022Pr1a_Ea, prods2022Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.26 | -2.26 | -2.16 | -1 | 5 | prods2022M1_I0_open_search | `ts_pearson(mul(day_argmin(Low), 0.5), 40)` |
| -2.49 | -2.34 | -2.49 | -1 | 20 | prods2022M1_I0_open_search | `ts_pearson(mul(log(day_argmin(Low)), 1), 10)` |
| -2.58 | -2.17 | -2.58 | -1 | 20 | prods2022M1_I0_open_search | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)` |

## 共性:116 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.06 | 0.045 | 5 | -1.12 / -2.18 | `day_argmin(sub(day_argmin(Low), Volume))` |
| +0.99 | 0.000 | 36 | -1.45 / -2.44 | `day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))` |
| +0.79 | 0.000 | 34 | -1.57 / -2.37 | `day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237)))` |
| +0.70 | 0.001 | 41 | -1.68 / -2.38 | `day_argmin(in_slice(Low, 2, 237))` |
| +0.67 | 0.003 | 42 | -1.70 / -2.38 | `day_argmax(in_slice(High, 2, 237))` |
| +0.65 | 0.069 | 7 | -1.52 / -2.17 | `day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241))` |
| +0.47 | 0.021 | 43 | -1.84 / -2.31 | `day_mean(in_slice(Amt, 2, 237))` |
| +0.12 | 0.465 | 57 | -2.07 / -2.19 | `day_argmin(Low)` |
| -0.07 | 0.521 | 4 | -2.20 / -2.13 | `div(sub(day_locate(in_slice(Close, 2, 237), add(day_argmin(in_slice(Low, 2, 237)), 10)), day_min(in_slice(Low, 2, 237))), sub(day_max(in_slice(High, 2, 237)), day_min(in_slice(Low, 2, 237))))` |
| -0.07 | 0.521 | 4 | -2.20 / -2.13 | `sub(day_locate(in_slice(Close, 2, 237), add(day_argmin(in_slice(Low, 2, 237)), 10)), day_min(in_slice(Low, 2, 237)))` |
| -0.07 | 0.521 | 4 | -2.20 / -2.13 | `day_locate(in_slice(Close, 2, 237), add(day_argmin(in_slice(Low, 2, 237)), 10))` |
| -0.14 | 0.605 | 7 | -2.26 / -2.12 | `day_min(in_slice(Low, 2, 237))` |
| -0.14 | 0.605 | 7 | -2.26 / -2.12 | `day_max(in_slice(High, 2, 237))` |
| -0.14 | 0.605 | 7 | -2.26 / -2.12 | `sub(day_max(in_slice(High, 2, 237)), day_min(in_slice(Low, 2, 237)))` |
| -0.59 | 0.925 | 5 | -2.70 / -2.11 | `log(day_argmin(Low))` |
| -0.85 | 0.959 | 5 | -2.95 / -2.10 | `cs_rank(day_argmin(Low))` |

## 拆解(12 次评估)

### head score -2.26:`ts_pearson(mul(day_argmin(Low), 0.5), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_argmin(Low)` | — | — | — | — | 门槛废品 |
| knockout | `mul(day_argmin(Low), 0.5)` | -2.26 | -2.26 | -2.16 | +0.00 | `ts_pearson(day_argmin(Low), 40)` |
| swap | `Low->High` | -2.43 | -2.43 | -2.10 | — | `ts_pearson(mul(day_argmin(High), 0.5), 40)` |
| window | `ts_pearson@40->20` | -2.02 | -2.02 | -1.96 | — | `ts_pearson(mul(day_argmin(Low), 0.5), 20)` |
| window | `ts_pearson@40->80` | -2.65 | -2.65 | -1.91 | — | `ts_pearson(mul(day_argmin(Low), 0.5), 80)` |

### head score -2.58:`ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_05(day_argmin(Low))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_argmin(Low)` | — | — | — | — | 门槛废品 |
| knockout | `mul(pow_05(day_argmin(Low)), 5)` | -2.58 | -2.17 | -2.58 | +0.00 | `ts_quantile_q75(pow_05(day_argmin(Low)), 20)` |
| knockout | `pow_05(day_argmin(Low))` | — | — | — | — | `ts_quantile_q75(mul(day_argmin(Low), 5), 20)` |
| swap | `Low->High` | -3.19 | -2.67 | -3.19 | — | `ts_quantile_q75(mul(pow_05(day_argmin(High)), 5), 20)` |
| window | `ts_quantile_q75@20->10` | -3.05 | -2.57 | -3.05 | — | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 10)` |
| window | `ts_quantile_q75@20->40` | -2.85 | -1.99 | -2.85 | — | `ts_quantile_q75(mul(pow_05(day_argmin(Low)), 5), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_argmin(sub(day_argmin(Low), Volume))` — enrichment,均值差 +1.06,p 0.045
2. `day_locate(in_slice(Amt, 2, 237), day_argmax(in_slice(High, 2, 237)))` — enrichment,均值差 +0.99,p 0.000
3. `day_locate(in_slice(Amt, 2, 237), day_argmin(in_slice(Low, 2, 237)))` — enrichment,均值差 +0.79,p 0.000
4. `day_argmin(in_slice(Low, 2, 237))` — enrichment,均值差 +0.70,p 0.001
5. `day_argmax(in_slice(High, 2, 237))` — enrichment,均值差 +0.67,p 0.003
6. `day_argmin(cross_cov(sub(day_argmin(Low), Volume), pow_1_5(Low), 241))` — enrichment,均值差 +0.65,p 0.069
7. `day_mean(in_slice(Amt, 2, 237))` — enrichment,均值差 +0.47,p 0.021

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

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(window ts_pearson@40->20):`ts_pearson(mul(day_argmin(Low), 0.5), 20)`
