# 定位:种子 2059,P 组,第 2 轮(只含 train / valid)

快照:prods2059M1_I0_open_search, prods2059M2_I0_open_search, prods2059Pr1a_Na, prods2059Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.45 | -1.24 | -1.45 | -1 | 20 | prods2059M2_I0_open_search | `cross_min(day_last(nt_cs_regres(Amt, Low)), 5)` |
| -1.48 | -1.46 | -1.48 | -1 | 20 | prods2059M2_I0_open_search | `cross_min(day_autocorr_n1(nt_cs_regres(Low, Low)), 5)` |
| -1.90 | -1.20 | -1.90 | +1 | 20 | prods2059M2_I0_open_search | `cross_min(day_first(nt_cs_regres(Amt, Low)), 15)` |
| -1.92 | -1.76 | -1.92 | -1 | 5 | prods2059M1_I0_open_search | `cross_min(day_max(nt_cs_regres(High, Low)), 15)` |
| -2.28 | -1.32 | -2.28 | -1 | 5 | prods2059M1_I0_open_search | `cross_min(day_max(nt_cs_regres(Ret, Low)), 60)` |
| -2.39 | -2.28 | -2.39 | -1 | 20 | prods2059M1_I0_open_search | `cross_min(cross_min(day_max(nt_cs_regres(Ret, Low)), 15), 15)` |

## 共性:121 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.91 | 0.002 | 6 | -1.39 / -2.30 | `ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40)` |
| +0.89 | 0.013 | 4 | -1.39 / -2.28 | `sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret))` |
| +0.84 | 0.009 | 15 | -1.52 / -2.36 | `day_es_ratio_lo(Open)` |
| +0.71 | 0.008 | 9 | -1.60 / -2.31 | `day_wmean(Vwap, Volume)` |
| +0.71 | 0.008 | 9 | -1.60 / -2.31 | `pow_2_5(day_wmean(Vwap, Volume))` |
| +0.68 | 0.063 | 4 | -1.60 / -2.28 | `cross_mean(day_es_ratio_lo(Ret), 30)` |
| +0.41 | 0.037 | 26 | -1.93 / -2.34 | `day_max(High)` |
| +0.40 | 0.206 | 5 | -1.87 / -2.27 | `log(day_max(High))` |
| +0.32 | 0.008 | 24 | -2.00 / -2.32 | `day_es_ratio_hi(Ret)` |
| +0.14 | 0.088 | 21 | -2.14 / -2.28 | `day_es_ratio_lo(Ret)` |
| +0.13 | 0.525 | 4 | -2.13 / -2.26 | `day_es_ratio_hi(Open)` |
| +0.13 | 0.447 | 24 | -2.15 / -2.28 | `day_min(Low)` |
| -0.15 | 0.810 | 4 | -2.39 / -2.25 | `ts_sum(ts_sum(day_argmin(High), 1), 5)` |
| -0.15 | 0.810 | 4 | -2.39 / -2.25 | `ts_sum(day_argmin(High), 1)` |
| -0.15 | 0.810 | 4 | -2.39 / -2.25 | `day_argmin(High)` |
| -0.40 | 0.182 | 6 | -2.64 / -2.23 | `sub(day_es_ratio_lo(Ret), day_es_ratio_hi(Ret))` |
| -0.66 | 0.994 | 6 | -2.88 / -2.22 | `day_max(nt_cs_regres(Ret, Low))` |
| -0.97 | 0.999 | 5 | -3.18 / -2.21 | `day_max(nt_cs_regres(Amt, Low))` |
| -1.19 | 0.943 | 4 | -3.40 / -2.21 | `log(div(sub(day_max(High), day_mean(Vwap)), sub(day_mean(Vwap), day_min(Low))))` |
| -1.19 | 0.943 | 4 | -3.40 / -2.21 | `day_mean(Vwap)` |

## 拆解(14 次评估)

### head score -1.45:`cross_min(day_last(nt_cs_regres(Amt, Low)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_last(nt_cs_regres(Amt, Low))` | -1.63 | -1.41 | -1.63 | — | (子树本身) |
| swap | `Amt->Volume` | -1.70 | -1.20 | -1.70 | — | `cross_min(day_last(nt_cs_regres(Volume, Low)), 5)` |
| swap | `Low->High` | -1.45 | -1.24 | -1.45 | — | `cross_min(day_last(nt_cs_regres(Amt, High)), 5)` |
| window | `cross_min@5->2` | -1.45 | -1.24 | -1.45 | — | `cross_min(day_last(nt_cs_regres(Amt, Low)), 2)` |
| window | `cross_min@5->10` | -1.52 | -1.28 | -1.52 | — | `cross_min(day_last(nt_cs_regres(Amt, Low)), 10)` |

### head score -1.48:`cross_min(day_autocorr_n1(nt_cs_regres(Low, Low)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_autocorr_n1(nt_cs_regres(Low, Low))` | — | — | — | — | 门槛废品 |
| swap | `Low->High` | — | — | — | — | `cross_min(day_autocorr_n1(nt_cs_regres(High, High)), 5)` |
| window | `cross_min@5->2` | — | — | — | — | `cross_min(day_autocorr_n1(nt_cs_regres(Low, Low)), 2)` |
| window | `cross_min@5->10` | — | — | — | — | `cross_min(day_autocorr_n1(nt_cs_regres(Low, Low)), 10)` |

### head score -1.90:`cross_min(day_first(nt_cs_regres(Amt, Low)), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_first(nt_cs_regres(Amt, Low))` | -1.33 | -0.82 | -1.33 | — | (子树本身) |
| swap | `Amt->Volume` | -1.93 | -1.51 | -1.93 | — | `cross_min(day_first(nt_cs_regres(Volume, Low)), 15)` |
| swap | `Low->High` | -1.88 | -1.20 | -1.88 | — | `cross_min(day_first(nt_cs_regres(Amt, High)), 15)` |
| window | `cross_min@15->7` | -1.64 | -1.15 | -1.64 | — | `cross_min(day_first(nt_cs_regres(Amt, Low)), 7)` |
| window | `cross_min@15->30` | -2.17 | -1.41 | -2.17 | — | `cross_min(day_first(nt_cs_regres(Amt, Low)), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40)` — enrichment,均值差 +0.91,p 0.002
2. `sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret))` — enrichment,均值差 +0.89,p 0.013
3. `day_es_ratio_lo(Open)` — enrichment,均值差 +0.84,p 0.009
4. `day_wmean(Vwap, Volume)` — enrichment,均值差 +0.71,p 0.008
5. `pow_2_5(day_wmean(Vwap, Volume))` — enrichment,均值差 +0.71,p 0.008
6. `cross_mean(day_es_ratio_lo(Ret), 30)` — enrichment,均值差 +0.68,p 0.063
7. `day_max(High)` — enrichment,均值差 +0.41,p 0.037
8. `day_es_ratio_hi(Ret)` — enrichment,均值差 +0.32,p 0.008
9. `day_es_ratio_lo(Ret)` — enrichment,均值差 +0.14,p 0.088

## 本组之前各轮的任务

- `prods2059Pr1a_Na`:核心 `—`;评分 81,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.43(train -0.08 valid -0.43):`cross_regbeta(day_max(Open), day_es_ratio_lo(Open), 60)`
  - score -0.44(train -0.04 valid -0.44):`cross_regbeta(day_max(High), day_es_ratio_lo(Open), 60)`
  - score -0.51(train -0.13 valid -0.51):`cross_regbeta(day_max(High), day_es_ratio_lo(High), 60)`
  - score -0.54(train -0.40 valid -0.54):`cross_regbeta(day_min(Low), day_es_ratio_lo(Open), 60)`
  - score -0.55(train -0.55 valid -0.46):`cross_regbeta(day_max(High), cross_regbeta(day_max(High), day_es_ratio_lo(Open), 60), 60)`
- `prods2059Pr1b_Nb`:核心 `—`;评分 90,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score -1.23(train -1.23 valid -1.19):`cross_mean(cs_bucket_zscore(cross_mean(sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret)), 15), LogFloatCap), 40)`
  - score -1.26(train -1.26 valid -1.20):`cs_bucket_zscore(cross_mean(sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret)), 40), LogFloatCap)`
  - score -1.26(train -1.26 valid -1.00):`cs_bucket_zscore(cross_mean(sub(cross_mean(day_es_ratio_lo(Ret), 10), day_es_ratio_hi(Ret)), 40), LogFloatCap)`
  - score -1.27(train -1.27 valid -1.19):`cs_bucket_zscore(cross_mean(sub(ts_skew(pow_2_5(day_wmean(Vwap, Vwap)), 40), day_es_ratio_hi(Ret)), 40), LogFloatCap)`
  - score -1.28(train -1.19 valid -1.28):`cross_mean(cs_bucket_zscore(cross_mean(sub(ts_skew(pow_2_5(day_wmean(Vwap, Volume)), 40), day_es_ratio_hi(Ret)), 40), LogFloatCap), 40)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.26(window cross_min@15->7):`cross_min(day_first(nt_cs_regres(Amt, Low)), 7)`
