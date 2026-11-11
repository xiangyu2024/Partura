# 定位:种子 2061,P 组,第 2 轮(只含 train / valid)

快照:prods2061M1_I0_open_search, prods2061M2_I0_open_search, prods2061Pr1a_Ea, prods2061Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(5 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.33 | -0.33 | +0.00 | -1 | 5 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 120)` |
| -0.83 | -0.83 | +0.15 | -1 | 20 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.8, True), 20)` |
| -0.85 | -0.85 | -0.75 | -1 | 20 | prods2061M1_I0_open_search | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.6, True), 20)` |
| -2.27 | -2.27 | -2.17 | -1 | 5 | prods2061M2_I0_open_search | `cross_argmax(day_ar1_coefficient(Ret), 241)` |
| -3.30 | -1.63 | -3.30 | -1 | 20 | prods2061M2_I0_open_search | `cross_argmax(day_ar1_coefficient(Volume), 241)` |

## 共性:136 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.64 | 0.000 | 28 | -0.94 / -2.57 | `day_open(Amt)` |
| +1.40 | 0.006 | 8 | -0.92 / -2.32 | `cross_reg_tvalue(LogFloatCap, day_open(Amt), 241)` |
| +1.35 | 0.001 | 16 | -1.04 / -2.39 | `day_mean(Low)` |
| +1.34 | 0.006 | 8 | -0.97 / -2.31 | `cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True))` |
| +1.31 | 0.000 | 21 | -1.13 / -2.44 | `pow_3(LogFloatCap)` |
| +1.29 | 0.011 | 6 | -1.00 / -2.29 | `cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)` |
| +1.11 | 0.035 | 6 | -1.17 / -2.28 | `cross_mean(cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True)), 60)` |
| +1.10 | 0.049 | 4 | -1.16 / -2.27 | `cs_mask_top_replace_mean(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` |
| +1.08 | 0.002 | 23 | -1.34 / -2.42 | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60)` |
| +1.00 | 0.062 | 7 | -1.29 / -2.29 | `cross_mean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), 60)` |
| +0.92 | 0.055 | 6 | -1.36 / -2.28 | `cross_reg_tvalue(pow_3(LogFloatCap), day_open(Amt), 241)` |
| +0.44 | 0.249 | 4 | -1.81 / -2.25 | `cs_mask_top_replace_mean(cross_reg_tvalue(pow_3(LogFloatCap), day_open(Amt), 241))` |
| +0.17 | 0.426 | 4 | -2.07 / -2.24 | `cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), LogFloatCap)` |
| -0.20 | 0.747 | 60 | -2.35 / -2.14 | `day_pdf_quantile_single(Ret, Volume, 0.95, True)` |

## 拆解(11 次评估)

### head score -0.33:`cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_pdf_quantile_single(Ret, Volume, 0.95, True)` | -2.94 | -2.94 | -2.29 | — | (子树本身) |
| swap | `Volume->Amt` | -0.38 | -0.38 | -0.17 | — | `cross_mean(day_pdf_quantile_single(Ret, Amt, 0.95, True), 120)` |
| window | `cross_mean@120->60` | -0.47 | -0.47 | -0.13 | — | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60)` |
| window | `cross_mean@120->240` | -0.35 | -0.35 | +0.82 | — | `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 240)` |

### head score -2.27:`cross_argmax(day_ar1_coefficient(Ret), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(Ret)` | -3.57 | -3.57 | -3.45 | — | (子树本身) |
| window | `cross_argmax@241->120` | — | — | — | — | `cross_argmax(day_ar1_coefficient(Ret), 120)` |
| window | `cross_argmax@241->482` | — | — | — | — | `cross_argmax(day_ar1_coefficient(Ret), 482)` |

### head score -3.30:`cross_argmax(day_ar1_coefficient(Volume), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| swap | `Volume->Amt` | — | — | — | — | `cross_argmax(day_ar1_coefficient(Amt), 241)` |
| window | `cross_argmax@241->120` | — | — | — | — | `cross_argmax(day_ar1_coefficient(Volume), 120)` |
| window | `cross_argmax@241->482` | — | — | — | — | `cross_argmax(day_ar1_coefficient(Volume), 482)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_open(Amt)` — enrichment,均值差 +1.64,p 0.000
2. `cross_reg_tvalue(LogFloatCap, day_open(Amt), 241)` — enrichment,均值差 +1.40,p 0.006
3. `day_mean(Low)` — enrichment,均值差 +1.35,p 0.001
4. `cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True))` — enrichment,均值差 +1.34,p 0.006
5. `pow_3(LogFloatCap)` — enrichment,均值差 +1.31,p 0.000
6. `cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241)` — enrichment,均值差 +1.29,p 0.011
7. `cross_mean(cs_bucket_demean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), day_pdf_quantile_single(Ret, Volume, 0.95, True)), 60)` — enrichment,均值差 +1.11,p 0.035
8. `cs_mask_top_replace_mean(cross_reg_fvalue(pow_3(LogFloatCap), day_open(Amt), 241))` — enrichment,均值差 +1.10,p 0.049
9. `cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60)` — enrichment,均值差 +1.08,p 0.002
10. `cross_mean(cross_mean(day_pdf_quantile_single(Ret, Volume, 0.95, True), 60), 60)` — enrichment,均值差 +1.00,p 0.062
11. `cross_reg_tvalue(pow_3(LogFloatCap), day_open(Amt), 241)` — enrichment,均值差 +0.92,p 0.055

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

## 比原 head 好的拆解变体(R 候选)

(没有)
