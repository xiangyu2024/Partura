# 定位:种子 2024,P 组,第 2 轮(只含 train / valid)

快照:prods2024M1_I0_open_search, prods2024M2_I0_open_search, prods2024Pr1a_Ea, prods2024Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.78 | -1.78 | -1.33 | +1 | 5 | prods2024M2_I0_open_search | `ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` |
| -1.79 | -1.79 | -1.39 | +1 | 5 | prods2024M2_I0_open_search | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| -1.81 | -1.81 | -1.45 | +1 | 5 | prods2024M2_I0_open_search | `ts_stddev(day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` |
| -2.05 | -2.05 | -1.80 | -1 | 20 | prods2024M1_I0_open_search | `abs_(ts_pearson(day_quantile_q75(Ret), 10))` |
| -2.89 | -2.89 | -2.89 | +1 | 20 | prods2024M1_I0_open_search | `sub(abs_(cs_mean(ts_pearson(day_quantile_q75(Ret), 5))), ts_pearson(day_quantile_q75(Ret), 5))` |
| -3.42 | -2.86 | -3.42 | -1 | 20 | prods2024M1_I0_open_search | `div(cross_mean(day_last(Volume), 40), cross_mean(day_sum(Volume), 40))` |

## 共性:164 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.61 | 0.001 | 4 | -0.97 / -2.58 | `ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20)` |
| +1.15 | 0.000 | 16 | -1.50 / -2.65 | `day_close(Amt)` |
| +0.74 | 0.001 | 10 | -1.84 / -2.58 | `signedpower(day_close(Amt))` |
| +0.68 | 0.039 | 4 | -1.88 / -2.55 | `cross_stddev(cross_zscore(day_sum(Volume), 60), 20)` |
| +0.67 | 0.005 | 7 | -1.90 / -2.57 | `ts_reg_fvalue(day_quantile_q75(Ret), signedpower(day_close(Amt)), 20)` |
| +0.38 | 0.116 | 6 | -2.17 / -2.55 | `day_q_stat_std(High)` |
| +0.35 | 0.012 | 107 | -2.41 / -2.77 | `day_quantile_q75(Ret)` |
| +0.33 | 0.165 | 5 | -2.22 / -2.55 | `div(cross_stddev(cs_mean(day_quantile_q75(Vwap)), 20), cs_mean(cross_stddev(day_quantile_q75(Ret), 20)))` |
| +0.28 | 0.239 | 4 | -2.27 / -2.54 | `day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` |
| +0.28 | 0.190 | 7 | -2.27 / -2.55 | `cs_mean(day_quantile_q75(Vwap))` |
| +0.28 | 0.190 | 7 | -2.27 / -2.55 | `day_quantile_q75(Vwap)` |
| +0.28 | 0.190 | 7 | -2.27 / -2.55 | `cross_stddev(cs_mean(day_quantile_q75(Vwap)), 20)` |
| +0.27 | 0.123 | 19 | -2.30 / -2.57 | `cross_zscore(day_sum(Volume), 60)` |
| +0.27 | 0.131 | 23 | -2.30 / -2.58 | `day_sum(Volume)` |
| +0.25 | 0.288 | 4 | -2.29 / -2.54 | `day_q_stat_std(in_slice(Ret, 11, 230))` |
| +0.25 | 0.291 | 4 | -2.29 / -2.54 | `day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))` |
| +0.23 | 0.329 | 4 | -2.32 / -2.54 | `mul(cs_state_rank(cs_mean(cross_corr(day_quantile_q75(Ret), cs_mean(day_quantile_q75(Ret)), 20)), 120), cs_rank(cross_corr(day_quantile_q75(Ret), cs_mean(day_quantile_q75(Ret)), 60)))` |
| +0.23 | 0.329 | 4 | -2.32 / -2.54 | `cs_state_rank(cs_mean(cross_corr(day_quantile_q75(Ret), cs_mean(day_quantile_q75(Ret)), 20)), 120)` |
| +0.15 | 0.308 | 12 | -2.40 / -2.55 | `cross_corr(day_quantile_q75(Ret), cs_mean(day_quantile_q75(Ret)), 20)` |
| +0.13 | 0.401 | 4 | -2.41 / -2.54 | `day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))), 10)` |

## 拆解(22 次评估)

### head score -1.78:`ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` | -3.43 | -3.43 | -2.96 | — | (子树本身) |
| swap | `Volume->Amt` | -1.81 | -1.81 | -1.42 | — | `ts_stddev(day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)` |
| window | `ts_stddev@15->7` | -2.95 | -2.95 | -2.66 | — | `ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 7)` |
| window | `ts_stddev@15->30` | -1.41 | -1.41 | -0.85 | — | `ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 30)` |

### head score -1.79:`add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` | -1.78 | -1.78 | -1.30 | — | (子树本身) |
| sufficiency | `day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))` | -3.43 | -3.43 | -2.96 | — | (子树本身) |
| sufficiency | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | -1.34 | -1.34 | -0.79 | — | (子树本身) |
| sufficiency | `day_q_stat_std(in_slice(Ret, 11, 230))` | -4.56 | -4.56 | -4.32 | — | (子树本身) |
| knockout | `ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` | -3.08 | -3.08 | -2.75 | +1.29 | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))))` |
| knockout | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` | -1.82 | -1.82 | -1.31 | +0.03 | `add(day_q_stat_std(in_slice(Ret, 11, 230)), ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| swap | `Volume->Amt` | -1.94 | -1.94 | -1.33 | — | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), ts_stddev(day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15))` |
| window | `ts_stddev@15->7` | -1.74 | -1.74 | -1.31 | — | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 7), ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |
| window | `ts_stddev@15->30` | -1.86 | -1.86 | -1.31 | — | `add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 30), ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))` |

### head score -1.81:`ts_stddev(day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))` | -3.42 | -3.42 | -2.94 | — | (子树本身) |
| swap | `Amt->Volume` | -1.78 | -1.78 | -1.30 | — | `ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)` |
| window | `ts_stddev@15->7` | -3.00 | -3.00 | -2.75 | — | `ts_stddev(day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 7)` |
| window | `ts_stddev@15->30` | -1.39 | -1.39 | -0.86 | — | `ts_stddev(day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230)))), 30)` |

### head score -2.05:`abs_(ts_pearson(day_quantile_q75(Ret), 10))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_pearson(day_quantile_q75(Ret), 10)` | -2.32 | -2.21 | -2.32 | — | (子树本身) |
| sufficiency | `day_quantile_q75(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `ts_pearson(day_quantile_q75(Ret), 10)` | — | — | — | — | `abs_(day_quantile_q75(Ret))` |
| window | `ts_pearson@10->5` | -2.35 | -1.80 | -2.35 | — | `abs_(ts_pearson(day_quantile_q75(Ret), 5))` |
| window | `ts_pearson@10->20` | -2.15 | -2.15 | -1.69 | — | `abs_(ts_pearson(day_quantile_q75(Ret), 20))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20)` — enrichment,均值差 +1.61,p 0.001
2. `day_close(Amt)` — enrichment,均值差 +1.15,p 0.000
3. `signedpower(day_close(Amt))` — enrichment,均值差 +0.74,p 0.001
4. `cross_stddev(cross_zscore(day_sum(Volume), 60), 20)` — enrichment,均值差 +0.68,p 0.039
5. `ts_reg_fvalue(day_quantile_q75(Ret), signedpower(day_close(Amt)), 20)` — enrichment,均值差 +0.67,p 0.005
6. `day_quantile_q75(Ret)` — enrichment,均值差 +0.35,p 0.012

## 本组之前各轮的任务

- `prods2024Pr1a_Ea`:核心 `day_quantile_q75(Ret)`;评分 79,过线 0,入 heads 0;采样计数 {'c05_skeleton': 416, 'c05_no_core': 807}
  - score -0.43(train -0.31 valid -0.43):`ts_reg_fvalue(ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20), day_close(Amt), 20)`
  - score -0.53(train -0.53 valid -0.52):`ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20)`
  - score -0.61(train -0.49 valid -0.61):`ts_reg_fvalue(ts_reg_fvalue(day_quantile_q75(Ret), signedpower(day_close(Amt)), 20), signedpower(day_close(Amt)), 20)`
  - score -0.80(train -0.56 valid -0.80):`ts_reg_fvalue(day_quantile_q75(Ret), signedpower(day_close(Amt)), 20)`
  - score -0.97(train -0.94 valid -0.97):`ts_reg_fvalue(ts_reg_fvalue(ts_reg_fvalue(day_quantile_q75(Ret), day_close(Amt), 20), day_close(Amt), 20), day_close(Amt), 20)`
- `prods2024Pr1b_Nb`:核心 `—`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.91(train -0.52 valid -0.91):`cross_regalpha(day_sum(Close), day_close(Ret), 30)`
  - score -1.10(train -1.10 valid -0.89):`cross_regalpha(day_sum(Volume), day_close(Ret), 30)`
  - score -1.46(train -1.46 valid -1.39):`cs_flip_by_state(cross_corr(cross_zscore(day_sum(Volume), 60), cs_mean(cross_zscore(day_sum(Volume), 60)), 60), div(cross_stddev(cs_mean(day_quantile_q75(Ret)), 20), cs_mean(day_quantile_q75(Ret))))`
  - score -1.55(train -1.55 valid -1.06):`cs_flip_by_state(cross_corr(cross_zscore(day_sum(Volume), 60), cs_mean(cross_zscore(day_sum(Volume), 60)), 60), div(cross_stddev(cs_mean(day_quantile_q75(Ret)), 20), cs_mean(cross_stddev(day_quantile_q75(Ret), 20))))`
  - score -1.55(train -1.55 valid -1.20):`cross_regalpha(day_q_stat_std(High), day_close(Ret), 241)`

## 比原 head 好的拆解变体(R 候选)

(没有)
