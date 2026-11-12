# 定位:种子 2080,P 组,第 1 轮(只含 train / valid)

快照:prods2080M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.11 | -0.74 | -1.11 | +1 | 20 | prods2080M1_I0_open_search | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15), 5)` |
| -1.13 | -0.78 | -1.13 | -1 | 5 | prods2080M1_I0_open_search | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)` |
| -1.26 | -0.82 | -1.26 | -1 | 20 | prods2080M1_I0_open_search | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Vwap), 3)), 20)` |

## 共性:45 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.05 | 0.018 | 4 | -1.89 / -2.94 | `day_q_stat_std(Volume)` |
| +0.81 | 0.054 | 4 | -2.11 / -2.92 | `day_max(High)` |
| +0.47 | 0.401 | 4 | -2.42 / -2.89 | `day_var(Ret)` |
| +0.47 | 0.401 | 4 | -2.42 / -2.89 | `cross_cov(day_var(Ret), day_var(Ret), 15)` |
| +0.43 | 0.181 | 4 | -2.46 / -2.89 | `day_open(Ret)` |
| +0.42 | 0.157 | 5 | -2.47 / -2.90 | `day_cov(Close, Close)` |
| +0.11 | 0.657 | 4 | -2.75 / -2.86 | `day_ar1_coefficient(Volume)` |
| -0.25 | 0.912 | 4 | -3.07 / -2.83 | `day_durbin_watson(Vwap)` |

## 拆解(22 次评估)

### head score -1.11:`ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15)` | -1.11 | -1.11 | -0.56 | — | (子树本身) |
| sufficiency | `ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5)` | -3.27 | -2.86 | -3.27 | — | (子树本身) |
| sufficiency | `pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15))` | -2.42 | -2.42 | -2.09 | — | (子树本身) |
| sufficiency | `cross_cov(day_var(Ret), day_var(Ret), 15)` | -2.42 | -2.42 | -2.09 | — | (子树本身) |
| knockout | `cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15)` | -2.42 | -1.62 | -2.42 | +1.31 | `ts_quantile_q75(day_max(High), 5)` |
| knockout | `ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5)` | -1.53 | -1.09 | -1.53 | +0.42 | `ts_quantile_q75(cross_cov(day_max(High), pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 15), 5)` |
| knockout | `pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15))` | -1.09 | -0.79 | -1.09 | -0.02 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(cross_cov(day_var(Ret), day_var(Ret), 15), 5), 15), 5)` |
| knockout | `cross_cov(day_var(Ret), day_var(Ret), 15)` | -2.41 | -1.72 | -2.41 | +1.30 | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(day_var(Ret)), 5), 15), 5)` |
| swap | `High->Low` | -1.21 | -0.81 | -1.21 | — | `ts_quantile_q75(cross_cov(day_max(Low), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15), 5)` |
| window | `ts_quantile_q75@5->2` | -0.94 | -0.94 | -0.68 | — | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15), 2)` |
| window | `ts_quantile_q75@5->10` | -1.53 | -0.77 | -1.53 | — | `ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15), 10)` |

### head score -1.13:`ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_kurt(day_q_stat_std(Volume), 50)` | -0.93 | -0.28 | -0.93 | — | (子树本身) |
| sufficiency | `day_q_stat_std(Volume)` | -2.36 | -2.36 | -2.21 | — | (子树本身) |
| knockout | `ts_kurt(day_q_stat_std(Volume), 50)` | -1.96 | -1.96 | -1.80 | +0.83 | `ts_quantile_q75(day_q_stat_std(Volume), 50)` |
| swap | `Volume->Amt` | -1.20 | -0.77 | -1.20 | — | `ts_quantile_q75(ts_kurt(day_q_stat_std(Amt), 50), 50)` |
| window | `ts_quantile_q75@50->25` | -1.03 | -0.71 | -1.03 | — | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 25)` |
| window | `ts_quantile_q75@50->100` | -1.30 | -0.60 | -1.30 | — | `ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 100)` |

### head score -1.26:`ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Vwap), 3)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Vwap), 3))` | -3.79 | -3.79 | -1.91 | — | (子树本身) |
| swap | `Low->High` | -1.84 | -1.16 | -1.84 | — | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(High, Vwap), 3)), 20)` |
| swap | `Vwap->Close` | -1.70 | -1.48 | -1.70 | — | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Close), 3)), 20)` |
| window | `ts_quantile_q75@20->10` | -1.74 | -0.77 | -1.74 | — | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Vwap), 3)), 10)` |
| window | `ts_quantile_q75@20->40` | -1.06 | -0.63 | -1.06 | — | `ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Vwap), 3)), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_q_stat_std(Volume)` — enrichment,均值差 +1.05,p 0.018
2. `day_max(High)` — enrichment,均值差 +0.81,p 0.054

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.20(window ts_quantile_q75@20->40):`ts_quantile_q75(day_ar1_coefficient(nt_ts_scale(in_topk_masked_p5(Low, Vwap), 3)), 40)`
- 增益 +0.18(window ts_quantile_q75@5->2):`ts_quantile_q75(cross_cov(day_max(High), ts_quantile_q75(pow_1_5(cross_cov(day_var(Ret), day_var(Ret), 15)), 5), 15), 2)`
- 增益 +0.10(window ts_quantile_q75@50->25):`ts_quantile_q75(ts_kurt(day_q_stat_std(Volume), 50), 25)`
