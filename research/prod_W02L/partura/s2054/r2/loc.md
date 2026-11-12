# 定位:种子 2054,P 组,第 2 轮(只含 train / valid)

快照:prods2054M1_I0_open_search, prods2054M2_I0_open_search, prods2054Pr1a_Na, prods2054Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.37 | -0.37 | -0.37 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15)), pow_1_5(Ret), 10), sigmoid(sqrt(Close)), 15), 5)))` |
| -0.41 | -0.38 | -0.41 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(Close), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 5), sigmoid(sqrt(Close)), 15), 5)))` |
| -0.45 | -0.26 | -0.45 | +1 | 5 | prods2054M1_I0_open_search | `day_median(pow_2(nt_ts_regalpha(nt_cs_mask_top_replace_mean_neg(High), nt_ts_corr(in_r2(signedpower(Vwap), pow_1_5(Ret), 30), sigmoid(sqrt(Close)), 15), 3)))` |
| -1.26 | -1.26 | -1.06 | -1 | 5 | prods2054M2_I0_open_search | `ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 40)` |
| -1.37 | -1.37 | -1.12 | +1 | 5 | prods2054M2_I0_open_search | `cross_regbeta(day_corr(signedpower(Vwap), Low), cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)), 60)` |
| -1.91 | -1.91 | -0.65 | +1 | 20 | prods2054M2_I0_open_search | `day_durbin_watson(cross_regbeta(signedpower(nt_ts_kurt(Low, 60)), nt_ts_argmin(signedpower(Close), 10), 241))` |

## 共性:111 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.99 | 0.069 | 4 | -1.19 / -2.19 | `cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High))` |
| +0.81 | 0.012 | 30 | -1.56 / -2.37 | `day_std(Ret)` |
| +0.60 | 0.261 | 4 | -1.57 / -2.17 | `cs_regres(day_argmax(High), day_last(High))` |
| +0.59 | 0.103 | 17 | -1.65 / -2.24 | `cs_regres(day_argmax(High), day_es_ratio_lo(High))` |
| +0.54 | 0.097 | 13 | -1.68 / -2.22 | `day_wmean(Ret, Volume)` |
| +0.53 | 0.231 | 6 | -1.65 / -2.18 | `day_corr(Ret, Volume)` |
| +0.49 | 0.173 | 8 | -1.70 / -2.19 | `sub(day_wmean(Ret, Volume), day_mean(Ret))` |
| +0.35 | 0.186 | 25 | -1.88 / -2.23 | `day_es_ratio_lo(High)` |
| +0.34 | 0.185 | 8 | -1.84 / -2.18 | `day_last(High)` |
| +0.25 | 0.213 | 35 | -1.98 / -2.23 | `day_argmax(High)` |
| +0.01 | 0.581 | 12 | -2.14 / -2.15 | `day_mean(Ret)` |
| -0.53 | 0.862 | 5 | -2.66 / -2.13 | `day_sum(in_slice(Ret, 11, 60))` |
| -0.53 | 0.862 | 5 | -2.66 / -2.13 | `day_sum(in_slice(Ret, 181, 230))` |

## 拆解(25 次评估)

### head score -1.26:`ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241)` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3)` | -9.98 | -9.98 | -8.76 | — | (子树本身) |
| sufficiency | `cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5)` | -3.41 | -3.16 | -3.41 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(signedpower(Ret))` | — | — | — | — | 门槛废品 |
| knockout | `cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241)` | -2.31 | -2.01 | -2.31 | +1.06 | `ts_pearson(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), 40)` |
| knockout | `cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3)` | -1.06 | -1.06 | -1.04 | -0.20 | `ts_pearson(cross_regres(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), day_ar1_coefficient(signedpower(Ret)), 241), 40)` |
| knockout | `cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5)` | -1.24 | -1.24 | -0.97 | -0.02 | `ts_pearson(cross_regres(cross_scale(day_argmax(High), 3), day_ar1_coefficient(signedpower(Ret)), 241), 40)` |
| swap | `High->Low` | -1.23 | -1.23 | -1.04 | — | `ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(Low), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 40)` |
| swap | `Low->High` | -1.08 | -1.08 | -0.99 | — | `ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(High), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 40)` |
| window | `ts_pearson@40->20` | -1.92 | -1.92 | -1.24 | — | `ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 20)` |
| window | `ts_pearson@40->80` | -1.12 | -1.12 | -1.05 | — | `ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 80)` |

### head score -1.37:`cross_regbeta(day_corr(signedpower(Vwap), Low), cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241))` | -1.05 | -1.05 | -0.80 | — | (子树本身) |
| sufficiency | `day_corr(signedpower(Vwap), Low)` | -2.77 | -2.28 | -2.77 | — | (子树本身) |
| sufficiency | `cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)` | -1.05 | -1.05 | -0.80 | — | (子树本身) |
| sufficiency | `day_ar1_coefficient(Volume)` | -3.44 | -2.83 | -3.44 | — | (子树本身) |
| knockout | `cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241))` | -1.20 | -1.20 | -1.20 | -0.17 | `cross_regbeta(day_corr(signedpower(Vwap), Low), cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241), 60)` |
| knockout | `cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)` | -1.82 | -1.43 | -1.82 | +0.45 | `cross_regbeta(day_corr(signedpower(Vwap), Low), cs_scale(day_ar1_coefficient(Volume)), 60)` |
| swap | `Vwap->Close` | -1.49 | -1.36 | -1.49 | — | `cross_regbeta(day_corr(signedpower(Close), Low), cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)), 60)` |
| swap | `Low->High` | -1.45 | -1.45 | -1.41 | — | `cross_regbeta(day_corr(signedpower(Vwap), High), cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)), 60)` |
| window | `cross_regbeta@60->30` | -1.72 | -1.33 | -1.72 | — | `cross_regbeta(day_corr(signedpower(Vwap), Low), cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)), 30)` |
| window | `cross_regbeta@60->120` | -1.50 | -1.11 | -1.50 | — | `cross_regbeta(day_corr(signedpower(Vwap), Low), cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241)), 120)` |

### head score -1.91:`day_durbin_watson(cross_regbeta(signedpower(nt_ts_kurt(Low, 60)), nt_ts_argmin(signedpower(Close), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Low->High` | -2.12 | -2.12 | -1.54 | — | `day_durbin_watson(cross_regbeta(signedpower(nt_ts_kurt(High, 60)), nt_ts_argmin(signedpower(Close), 10), 241))` |
| swap | `Close->Vwap` | -2.88 | -2.32 | -2.88 | — | `day_durbin_watson(cross_regbeta(signedpower(nt_ts_kurt(Low, 60)), nt_ts_argmin(signedpower(Vwap), 10), 241))` |
| window | `cross_regbeta@241->120` | -2.01 | -2.01 | -0.31 | — | `day_durbin_watson(cross_regbeta(signedpower(nt_ts_kurt(Low, 60)), nt_ts_argmin(signedpower(Close), 10), 120))` |
| window | `cross_regbeta@241->482` | -2.17 | -2.17 | -1.63 | — | `day_durbin_watson(cross_regbeta(signedpower(nt_ts_kurt(Low, 60)), nt_ts_argmin(signedpower(Close), 10), 482))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High))` — enrichment,均值差 +0.99,p 0.069
2. `day_std(Ret)` — enrichment,均值差 +0.81,p 0.012
3. `day_wmean(Ret, Volume)` — enrichment,均值差 +0.54,p 0.097

## 本组之前各轮的任务

- `prods2054Pr1a_Na`:核心 `—`;评分 67,过线 0,入 heads 0;采样计数 {'c05_skeleton': 14}
  - score -0.09(train -0.04 valid -0.09):`cross_mean(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_mean(Ret)), 60)`
  - score -0.18(train -0.18 valid -0.06):`cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 60)`
  - score -0.24(train -0.24 valid -0.16):`cross_mean(day_wmean(Ret, Volume), 60)`
  - score -0.24(train -0.24 valid -0.16):`cross_mean(sub(sub(day_wmean(Ret, Volume), day_wmean(Ret, Volume)), day_wmean(Ret, Volume)), 60)`
  - score -0.56(train -0.55 valid -0.56):`cross_mean(sub(sub(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_mean(Ret)), day_mean(Ret)), day_mean(Ret)), 60)`
- `prods2054Pr1b_Nb`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 10}
  - score -0.36(train -0.36 valid -0.33):`cross_corr(day_std(High), ts_mean(inv(ts_decay_linear(day_at_max_ratio(Close), 40)), 40), 241)`
  - score -0.52(train -0.44 valid -0.52):`cross_corr(day_std(Ret), cs_regres(day_argmax(Vwap), day_last(High)), 241)`
  - score -0.66(train -0.51 valid -0.66):`cross_corr(day_std(Ret), cs_regres(day_argmax(High), day_last(High)), 241)`
  - score -0.68(train -0.55 valid -0.68):`cross_corr(day_std(Ret), cs_regres(cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), day_last(High)), 241)`
  - score -0.70(train -0.47 valid -0.70):`cross_reg_tvalue(day_std(Ret), cs_regres(cs_regres(day_argmax(High), day_es_ratio_lo(High)), day_es_ratio_lo(High)), 241)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.20(knockout cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3)):`ts_pearson(cross_regres(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), day_ar1_coefficient(signedpower(Ret)), 241), 40)`
- 增益 +0.18(swap Low->High):`ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(High), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 40)`
- 增益 +0.17(knockout cs_scale(cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241))):`cross_regbeta(day_corr(signedpower(Vwap), Low), cross_cov(day_ar1_coefficient(Volume), day_open(Open), 241), 60)`
- 增益 +0.14(window ts_pearson@40->80):`ts_pearson(cross_regres(cross_scale(cross_cov(day_argmax(High), day_ar1_coefficient(Low), 5), 3), day_ar1_coefficient(signedpower(Ret)), 241), 80)`
