# 定位:种子 2045,P 组,第 2 轮(只含 train / valid)

快照:prods2045M1_I0_open_search, prods2045M2_I0_open_search, prods2045Pr1a_Ea, prods2045Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.40 | +0.40 | +0.94 | +1 | 0 | prods2045M1_I0_open_search | `add(ts_quantile_q50(day_cov(Amt, cross_delta(Amt, 30)), 40), ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50))` |
| -0.24 | -0.24 | +0.85 | +1 | 0 | prods2045M1_I0_open_search | `ts_sum(cross_stddev(cross_max(day_cov(cross_delta(Amt, 241), Amt), 3), 241), 5)` |
| -0.34 | -0.34 | -0.34 | +1 | 0 | prods2045M2_I0_open_search | `ts_sum(cross_stddev(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30)))), 60), 5)` |
| -1.11 | -0.69 | -1.11 | +1 | 0 | prods2045M1_I0_open_search | `ts_std(ts_cov(day_mean(Volume), day_close(cross_delta(High, 10)), 50), 40)` |
| -1.25 | -1.25 | -1.12 | +1 | 5 | prods2045M2_I0_open_search | `ts_cov(day_median(pow_2(nt_cs_rank(cross_delta(Open, 241)))), day_close(High), 50)` |
| -1.58 | -1.26 | -1.58 | +1 | 0 | prods2045M2_I0_open_search | `ts_std(ts_cov(day_quantile_q25(Ret), day_median(pow_2(nt_cs_rank(cross_delta(High, 30)))), 50), 40)` |

## 共性:156 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.29 | 0.000 | 5 | +0.21 / -2.07 | `cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241)` |
| +2.15 | 0.000 | 13 | -0.03 / -2.18 | `cross_mean(day_cov(Amt, Amt), 241)` |
| +2.01 | 0.000 | 18 | -0.22 / -2.23 | `day_cov(Amt, Amt)` |
| +1.48 | 0.000 | 49 | -0.98 / -2.47 | `cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60)` |
| +1.48 | 0.000 | 49 | -0.98 / -2.47 | `day_cov(Amt, cross_delta(Amt, 30))` |
| +1.48 | 0.000 | 49 | -0.98 / -2.47 | `ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50)` |
| +0.17 | 0.337 | 4 | -1.83 / -2.00 | `cross_mean(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), 241)` |
| +0.07 | 0.419 | 7 | -1.94 / -2.00 | `day_close(cross_delta(High, 10))` |
| -0.01 | 0.480 | 4 | -2.01 / -2.00 | `ts_cov(day_quantile_q25(Ret), day_close(cross_delta(High, 10)), 50)` |
| -0.03 | 0.512 | 9 | -2.03 / -2.00 | `day_close(High)` |
| -0.03 | 0.544 | 5 | -2.03 / -2.00 | `day_close(cross_delta(High, 30))` |
| -0.20 | 0.751 | 11 | -2.19 / -1.99 | `day_quantile_q25(Ret)` |
| -0.26 | 0.667 | 5 | -2.25 / -1.99 | `day_kurt(High)` |
| -0.31 | 0.738 | 30 | -2.25 / -1.94 | `day_wstd(High, Vwap)` |
| -0.35 | 0.952 | 24 | -2.29 / -1.95 | `day_q_stat_std(Close)` |
| -0.42 | 0.882 | 8 | -2.40 / -1.98 | `day_close(Open)` |
| -0.44 | 0.972 | 18 | -2.39 / -1.95 | `cross_sum(day_q_stat_std(Close), 3)` |
| -0.67 | 0.967 | 7 | -2.64 / -1.97 | `cross_tail_mean_q25(cross_sum(day_q_stat_std(Close), 3), 10)` |
| -0.74 | 0.896 | 4 | -2.72 / -1.98 | `pow_05(cross_tail_mean_q25(cross_sum(day_q_stat_std(Close), 3), 10))` |
| -0.79 | 0.947 | 5 | -2.77 / -1.98 | `day_q_stat_std(Vwap)` |

## 拆解(19 次评估)

### head score -0.34:`ts_sum(cross_stddev(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30)))), 60), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_stddev(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30)))), 60)` | -0.34 | -0.34 | -0.08 | — | (子树本身) |
| sufficiency | `day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30))))` | -2.23 | -1.85 | -2.23 | — | (子树本身) |
| knockout | `cross_stddev(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30)))), 60)` | -2.18 | -1.72 | -2.18 | +1.84 | `ts_sum(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30)))), 5)` |
| swap | `Amt->Volume` | -0.85 | -0.01 | -0.85 | — | `ts_sum(cross_stddev(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Volume, 30)))), 60), 5)` |
| window | `ts_sum@5->2` | -0.29 | -0.29 | -0.13 | — | `ts_sum(cross_stddev(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30)))), 60), 2)` |
| window | `ts_sum@5->10` | -0.55 | -0.55 | -0.44 | — | `ts_sum(cross_stddev(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(Amt, 30)))), 60), 10)` |

### head score -1.25:`ts_cov(day_median(pow_2(nt_cs_rank(cross_delta(Open, 241)))), day_close(High), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_median(pow_2(nt_cs_rank(cross_delta(Open, 241))))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_close(High)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| swap | `Open->Close` | -1.24 | -1.24 | -1.09 | — | `ts_cov(day_median(pow_2(nt_cs_rank(cross_delta(Close, 241)))), day_close(High), 50)` |
| swap | `High->Low` | -1.26 | -1.26 | -1.10 | — | `ts_cov(day_median(pow_2(nt_cs_rank(cross_delta(Open, 241)))), day_close(Low), 50)` |
| window | `ts_cov@50->25` | -1.82 | -1.82 | -1.13 | — | `ts_cov(day_median(pow_2(nt_cs_rank(cross_delta(Open, 241)))), day_close(High), 25)` |
| window | `ts_cov@50->100` | -1.20 | -1.20 | -1.10 | — | `ts_cov(day_median(pow_2(nt_cs_rank(cross_delta(Open, 241)))), day_close(High), 100)` |

### head score -1.58:`ts_std(ts_cov(day_quantile_q25(Ret), day_median(pow_2(nt_cs_rank(cross_delta(High, 30)))), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_quantile_q25(Ret), day_median(pow_2(nt_cs_rank(cross_delta(High, 30)))), 50)` | -1.64 | -0.42 | -1.64 | — | (子树本身) |
| sufficiency | `day_median(pow_2(nt_cs_rank(cross_delta(High, 30))))` | -2.69 | -2.17 | -2.69 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `ts_cov(day_quantile_q25(Ret), day_median(pow_2(nt_cs_rank(cross_delta(High, 30)))), 50)` | -2.16 | -1.34 | -2.16 | +0.58 | `ts_std(day_quantile_q25(Ret), 40)` |
| swap | `High->Low` | -1.65 | -1.29 | -1.65 | — | `ts_std(ts_cov(day_quantile_q25(Ret), day_median(pow_2(nt_cs_rank(cross_delta(Low, 30)))), 50), 40)` |
| window | `ts_std@40->20` | -1.99 | -1.38 | -1.99 | — | `ts_std(ts_cov(day_quantile_q25(Ret), day_median(pow_2(nt_cs_rank(cross_delta(High, 30)))), 50), 20)` |
| window | `ts_std@40->80` | -2.59 | -1.36 | -2.59 | — | `ts_std(ts_cov(day_quantile_q25(Ret), day_median(pow_2(nt_cs_rank(cross_delta(High, 30)))), 50), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241)` — enrichment,均值差 +2.29,p 0.000
2. `cross_mean(day_cov(Amt, Amt), 241)` — enrichment,均值差 +2.15,p 0.000
3. `day_cov(Amt, Amt)` — enrichment,均值差 +2.01,p 0.000
4. `cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60)` — enrichment,均值差 +1.48,p 0.000
5. `day_cov(Amt, cross_delta(Amt, 30))` — enrichment,均值差 +1.48,p 0.000
6. `ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50)` — enrichment,均值差 +1.48,p 0.000

## 本组之前各轮的任务

- `prods2045Pr1a_Ea`:核心 `ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50)`;评分 99,过线 0,入 heads 0;采样计数 {'c05_no_core': 2078, 'c05_skeleton': 1097, 'c05_periphery_seen': 9, 'mutation_refused': 7}
  - score +0.31(train +0.31 valid +0.96):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), add(cross_quantile_q25(day_cov(Amt, cross_delta(Amt, 30)), 241), -2))`
  - score +0.30(train +0.30 valid +0.35):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), add(cross_quantile_q25(day_cov(Amt, Amt), 241), -2))`
  - score +0.25(train +0.27 valid +0.25):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), add(cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241), add(cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241), 1)))`
  - score +0.25(train +0.27 valid +0.25):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), mul(cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241), 1))`
  - score +0.25(train +0.27 valid +0.25):`div(ts_std(cross_stddev(day_cov(Amt, cross_delta(Amt, 30)), 60), 50), add(cross_mean(day_cov(Amt, cross_delta(Amt, 30)), 241), 2))`
- `prods2045Pr1b_Nb`:核心 `—`;评分 96,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2}
  - score -1.11(train -1.11 valid -1.07):`mul(cross_reg_fvalue(cross_sum(day_q_stat_std(Close), 3), day_wstd(High, Vwap), 15), 1)`
  - score -1.11(train -1.11 valid -1.07):`cross_reg_fvalue(cross_sum(day_q_stat_std(Close), 3), day_wstd(High, Vwap), 15)`
  - score -1.14(train -1.14 valid -1.07):`mul(cross_reg_fvalue(cross_sum(day_q_stat_std(Close), 3), day_wstd(High, Vwap), 15), -5)`
  - score -1.14(train -1.14 valid -1.07):`mul(cross_reg_fvalue(cross_sum(day_q_stat_std(Close), 3), day_wstd(Open, Vwap), 15), 1)`
  - score -1.56(train -1.56 valid -1.15):`mul(cross_reg_fvalue(cross_sum(day_q_stat_std(Vwap), 3), day_wstd(High, Vwap), 15), -5)`

## 比原 head 好的拆解变体(R 候选)

(没有)
