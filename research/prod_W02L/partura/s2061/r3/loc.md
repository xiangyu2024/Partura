# 定位:种子 2061,P 组,第 3 轮(只含 train / valid)

快照:prods2061M1_I0_open_search, prods2061M2_I0_open_search, prods2061M3_I0_open_search, prods2061Pr1a_Ea, prods2061Pr1b_Nb, prods2061Pr2a_Ea, prods2061Pr2b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.33 | -0.33 | +0.00 | -1 | 5 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 120)` |
| -0.83 | -0.83 | +0.15 | -1 | 20 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.8, True), 20)` |
| -0.85 | -0.85 | -0.75 | -1 | 20 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.6, True), 20)` |
| -2.27 | -2.27 | -2.17 | -1 | 5 | prods2061M2_I0_open_search | `cross_argmax(day_ar1_coefficient(Ret), 241)` |
| -2.27 | -2.27 | -2.17 | -1 | 5 | prods2061M3_I0_open_search | `pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 241)))))` |
| -3.30 | -1.63 | -3.30 | -1 | 20 | prods2061M2_I0_open_search | `cross_argmax(day_ar1_coefficient(Volume), 241)` |

## 共性:226 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.62 | 0.000 | 99 | -0.92 / -2.55 | `day_open(Amt)` |
| +1.46 | 0.000 | 10 | -0.44 / -1.90 | `pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` |
| +1.43 | 0.002 | 8 | -0.46 / -1.89 | `cross_reg_fvalue(pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)), day_open(Amt), 241)` |
| +1.39 | 0.000 | 76 | -0.92 / -2.30 | `pow_3(LogFloatCap)` |
| +1.35 | 0.000 | 61 | -0.85 / -2.20 | `cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)` |
| +1.25 | 0.066 | 4 | -0.61 / -1.86 | `log(cross_reg_fvalue(pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)), day_open(Amt), 241))` |
| +1.01 | 0.067 | 4 | -0.85 / -1.85 | `sigmoid(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` |
| +0.95 | 0.043 | 8 | -0.92 / -1.87 | `cross_reg_tvalue(LogFloatCap, day_open(Amt), 241)` |
| +0.95 | 0.004 | 18 | -0.96 / -1.91 | `day_mean(Low)` |
| +0.90 | 0.035 | 8 | -0.97 / -1.87 | `cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True))` |
| +0.75 | 0.078 | 13 | -1.13 / -1.88 | `div(day_open(Amt), day_sum(Amt))` |
| +0.75 | 0.145 | 5 | -1.10 / -1.85 | `sub(div(day_open(Amt), day_sum(Amt)), div(day_open(Volume), day_sum(Volume)))` |
| +0.73 | 0.084 | 13 | -1.14 / -1.88 | `day_sum(Volume)` |
| +0.73 | 0.100 | 8 | -1.13 / -1.86 | `div(day_open(Volume), day_sum(Volume))` |
| +0.69 | 0.124 | 4 | -1.16 / -1.85 | `cs_mask_top_replace_mean(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` |
| +0.68 | 0.113 | 6 | -1.17 / -1.85 | `cross_mean(cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True)), 60)` |
| +0.67 | 0.116 | 11 | -1.20 / -1.87 | `day_open(Volume)` |
| +0.65 | 0.117 | 16 | -1.23 / -1.88 | `day_sum(Amt)` |
| +0.56 | 0.223 | 7 | -1.29 / -1.85 | `cross_mean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), 60)` |
| +0.55 | 0.063 | 23 | -1.34 / -1.89 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60)` |

## 拆解(10 次评估)

### head score -2.27:`pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 241)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 241))))` | — | — | — | — | 门槛废品 |
| sufficiency | `pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 241)))` | — | — | — | — | 门槛废品 |
| sufficiency | `abs_(cross_argmax(day_ar1_coefficient(Ret), 241))` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_argmax(day_ar1_coefficient(Ret), 241)` | — | — | — | — | 门槛废品 |
| knockout | `neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 241))))` | — | — | — | — | `pow_2(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 241))))` |
| knockout | `pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 241)))` | — | — | — | — | `pow_2(neg(abs_(cross_argmax(day_ar1_coefficient(Ret), 241))))` |
| knockout | `abs_(cross_argmax(day_ar1_coefficient(Ret), 241))` | — | — | — | — | `pow_2(neg(pow_05(cross_argmax(day_ar1_coefficient(Ret), 241))))` |
| knockout | `cross_argmax(day_ar1_coefficient(Ret), 241)` | -3.40 | -3.40 | -3.19 | +1.13 | `pow_2(neg(pow_05(abs_(day_ar1_coefficient(Ret)))))` |
| window | `cross_argmax@241->120` | — | — | — | — | `pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 120)))))` |
| window | `cross_argmax@241->482` | — | — | — | — | `pow_2(neg(pow_05(abs_(cross_argmax(day_ar1_coefficient(Ret), 482)))))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_open(Amt)` — enrichment,均值差 +1.62,p 0.000
2. `pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` — enrichment,均值差 +1.46,p 0.000
3. `cross_reg_fvalue(pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)), day_open(Amt), 241)` — enrichment,均值差 +1.43,p 0.002
4. `pow_3(LogFloatCap)` — enrichment,均值差 +1.39,p 0.000
5. `cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)` — enrichment,均值差 +1.35,p 0.000
6. `log(cross_reg_fvalue(pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)), day_open(Amt), 241))` — enrichment,均值差 +1.25,p 0.066
7. `sigmoid(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` — enrichment,均值差 +1.01,p 0.067
8. `cross_reg_tvalue(LogFloatCap, day_open(Amt), 241)` — enrichment,均值差 +0.95,p 0.043
9. `day_mean(Low)` — enrichment,均值差 +0.95,p 0.004
10. `cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True))` — enrichment,均值差 +0.90,p 0.035
11. `div(day_open(Amt), day_sum(Amt))` — enrichment,均值差 +0.75,p 0.078
12. `day_sum(Volume)` — enrichment,均值差 +0.73,p 0.084
13. `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60)` — enrichment,均值差 +0.55,p 0.063

## 本组之前各轮的任务

- `prods2061Pr1a_Ea`:核心 `day_pdf_quantile_single(Ret, Volume, 0.95, True)`;评分 82,过线 0,入 heads 0;采样计数 {'c05_no_core': 901, 'c05_skeleton': 440, 'c05_periphery_seen': 1}
  - score -0.24(train -0.24 valid +0.11):`cs_bucket_demean(cross_mean(cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True)), 60), day_mean(Low))`
  - score -0.24(train -0.24 valid -0.17):`cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), LogFloatCap)`
  - score -0.25(train -0.25 valid -0.13):`cs_bucket_demean(cross_mean(cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 15), day_pdf_quantile_single(Ret, Volume, 0.95, True)), 60), day_mean(Low))`
  - score -0.31(train -0.31 valid +0.02):`cs_bucket_demean(cross_mean(cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True)), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True))`
  - score -0.33(train -0.33 valid +0.10):`cs_bucket_demean(cross_mean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), 60), day_mean(Low))`
- `prods2061Pr1b_Nb`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 7}
  - score +0.13(train +0.13 valid +0.16):`cs_mask_top_replace_mean(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))`
  - score +0.12(train +0.15 valid +0.12):`cs_mask_top_replace_mean(cross_reg_fvalue(LogFloatCap, day_open(Amt), 241))`
  - score +0.05(train +0.05 valid +0.44):`cs_mask_top_replace_mean(cs_mask_top_replace_mean(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)))`
  - score -0.09(train -0.09 valid +0.02):`cs_mask_top_replace_mean(cross_reg_fvalue(cross_reg_tvalue(LogFloatCap, day_open(Amt), 241), day_open(Amt), 241))`
  - score -0.14(train -0.14 valid -0.13):`cs_mask_top_replace_mean(cs_mask_top_replace_mean(cs_mask_top_replace_mean(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))))`
- `prods2061Pr2a_Ea`:核心 `cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)`;评分 74,过线 0,入 heads 0;采样计数 {'c05_no_core': 801, 'c05_skeleton': 305, 'mutation_refused': 5, 'c05_periphery_seen': 3}
  - score +0.06(train +0.17 valid +0.06):`log(cross_reg_fvalue(pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)), day_open(Amt), 241))`
  - score +0.00(train +0.20 valid +0.00):`cs_mask_top_replace_mean_neg(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))`
  - score -0.04(train -0.04 valid +0.62):`ts_autocorr_s1(mul(-5, sigmoid(cross_reg_fvalue(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241), day_open(Amt), 241))), 10)`
  - score -0.05(train -0.05 valid -0.01):`cs_mask_top_replace_mean_neg(cross_reg_fvalue(pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)), day_open(Amt), 241))`
  - score -0.05(train -0.05 valid -0.01):`cs_mask_top_replace_mean_neg(cross_reg_fvalue(pow_3(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)), day_first(Amt), 241))`
- `prods2061Pr2b_Nb`:核心 `—`;评分 79,过线 0,入 heads 0;采样计数 {'c05_skeleton': 13}
  - score -0.10(train +0.06 valid -0.10):`cross_autocorr(div(sub(div(day_open(Amt), day_sum(Amt)), div(day_open(Volume), day_sum(Volume))), day_sum(Amt)), 60, 1)`
  - score -0.22(train -0.22 valid -0.13):`cross_autocorr(div(day_open(Volume), day_sum(Volume)), 60, 1)`
  - score -0.27(train -0.27 valid -0.21):`cross_autocorr(div(day_open(Amt), day_sum(Amt)), 60, 1)`
  - score -0.46(train +0.03 valid -0.46):`cross_stddev(sub(div(day_open(Amt), day_sum(Amt)), div(day_open(Volume), day_sum(Volume))), 60)`
  - score -0.47(train -0.47 valid +0.14):`cross_mean(sub(div(day_open(Amt), day_sum(Amt)), div(day_open(Volume), day_sum(Volume))), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
