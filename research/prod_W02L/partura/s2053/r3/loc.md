# 定位:种子 2053,P 组,第 3 轮(只含 train / valid)

快照:prods2053M1_I0_open_search, prods2053M2_I0_open_search, prods2053M3_I0_open_search, prods2053Pr1a_Na, prods2053Pr2a_Ea, prods2053Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.52 | -0.52 | +0.96 | +1 | 0 | prods2053M2_I0_open_search | `day_first(cross_sum(Amt, 241))` |
| -0.98 | -0.98 | -0.64 | +1 | 5 | prods2053M2_I0_open_search | `day_first(cross_sum(Amt, 30))` |
| -1.33 | -1.19 | -1.33 | -1 | 5 | prods2053M2_I0_open_search | `day_sum(cross_sum(Volume, 3))` |
| -1.63 | -1.63 | -0.46 | +1 | 20 | prods2053M3_I0_open_search | `ts_std(ts_cov(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241)))), day_close(High), 50), 40)` |
| -1.83 | -1.63 | -1.83 | -1 | 20 | prods2053M3_I0_open_search | `day_median(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 60))))` |
| -2.15 | -1.46 | -2.15 | +1 | 0 | prods2053M3_I0_open_search | `ts_std(ts_cov(day_quantile_q25(Ret), day_close(cross_delta(nt_cs_rank(cross_sum(Open, 30)), 30)), 50), 40)` |

## 共性:179 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.51 | 0.004 | 4 | -0.78 / -2.29 | `cross_regbeta(cross_sum(cross_sum(day_mean(Ret), 10), 15), day_topw_mean(Ret, Close), 241)` |
| +1.36 | 0.001 | 7 | -0.95 / -2.31 | `cross_sum(cross_sum(day_mean(Ret), 10), 15)` |
| +1.26 | 0.003 | 6 | -1.04 / -2.30 | `log(cross_regbeta(cross_sum(day_mean(Ret), 15), day_topw_mean(Ret, Close), 241))` |
| +1.26 | 0.001 | 8 | -1.05 / -2.31 | `cross_sum(day_mean(Ret), 10)` |
| +1.24 | 0.000 | 19 | -1.15 / -2.39 | `cross_sum(day_mean(Ret), 15)` |
| +1.16 | 0.000 | 30 | -1.29 / -2.45 | `day_mean(Ret)` |
| +1.12 | 0.000 | 12 | -1.22 / -2.33 | `cross_regbeta(cross_sum(day_mean(Ret), 15), day_topw_mean(Ret, Close), 241)` |
| +0.55 | 0.100 | 8 | -1.73 / -2.28 | `ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30)` |
| +0.49 | 0.074 | 17 | -1.82 / -2.30 | `cross_semistd_neg(day_topw_mean(Ret, Close), 3)` |
| +0.48 | 0.055 | 10 | -1.80 / -2.28 | `day_topw_mean(Ret, Ret)` |
| +0.45 | 0.137 | 8 | -1.83 / -2.28 | `day_topw_mean(Ret, in_demean(Close))` |
| +0.44 | 0.192 | 6 | -1.83 / -2.27 | `cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30))` |
| +0.34 | 0.042 | 77 | -2.06 / -2.40 | `day_topw_mean(Ret, Close)` |
| +0.30 | 0.421 | 4 | -1.97 / -2.26 | `cross_regbeta(day_topw_mean(Ret, Close), day_hurst(High), 15)` |
| +0.06 | 0.512 | 9 | -2.20 / -2.26 | `ts_min(day_durbin_watson(Close), 50)` |
| -0.04 | 0.643 | 10 | -2.29 / -2.25 | `day_durbin_watson(Close)` |
| -0.11 | 0.722 | 6 | -2.36 / -2.25 | `day_topw_mean(Ret, Volume)` |
| -0.18 | 0.771 | 6 | -2.43 / -2.25 | `day_hurst(High)` |
| -0.44 | 0.912 | 5 | -2.68 / -2.24 | `day_quantile_q25(Ret)` |

## 拆解(18 次评估)

### head score -1.63:`ts_std(ts_cov(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241)))), day_close(High), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241)))), day_close(High), 50)` | -1.43 | -1.43 | -1.35 | — | (子树本身) |
| sufficiency | `day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241))))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_close(High)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `ts_cov(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241)))), day_close(High), 50)` | -2.00 | -2.00 | -1.38 | +0.36 | `ts_std(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241)))), 40)` |
| swap | `Open->Close` | -1.65 | -1.65 | -0.49 | — | `ts_std(ts_cov(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Close, 241)), 241)))), day_close(High), 50), 40)` |
| swap | `High->Low` | -1.64 | -1.64 | -0.48 | — | `ts_std(ts_cov(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241)))), day_close(Low), 50), 40)` |
| window | `ts_std@40->20` | -1.77 | -1.77 | -0.79 | — | `ts_std(ts_cov(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241)))), day_close(High), 50), 20)` |
| window | `ts_std@40->80` | -1.67 | -1.67 | -0.46 | — | `ts_std(ts_cov(day_quantile_q25(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 241)))), day_close(High), 50), 80)` |

### head score -1.83:`day_median(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 60))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Open->Close` | -1.79 | -1.63 | -1.79 | — | `day_median(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Close, 241)), 60))))` |
| window | `cross_delta@60->30` | -1.84 | -1.76 | -1.84 | — | `day_median(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 30))))` |
| window | `cross_delta@60->120` | -1.96 | -1.54 | -1.96 | — | `day_median(pow_2(nt_cs_rank(cross_delta(nt_cs_rank(cross_sum(Open, 241)), 120))))` |

### head score -2.15:`ts_std(ts_cov(day_quantile_q25(Ret), day_close(cross_delta(nt_cs_rank(cross_sum(Open, 30)), 30)), 50), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_cov(day_quantile_q25(Ret), day_close(cross_delta(nt_cs_rank(cross_sum(Open, 30)), 30)), 50)` | -1.64 | -1.64 | -1.29 | — | (子树本身) |
| sufficiency | `day_close(cross_delta(nt_cs_rank(cross_sum(Open, 30)), 30))` | -2.51 | -1.82 | -2.51 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| knockout | `ts_cov(day_quantile_q25(Ret), day_close(cross_delta(nt_cs_rank(cross_sum(Open, 30)), 30)), 50)` | -2.16 | -1.34 | -2.16 | +0.00 | `ts_std(day_quantile_q25(Ret), 40)` |
| swap | `Open->Close` | -2.18 | -1.42 | -2.18 | — | `ts_std(ts_cov(day_quantile_q25(Ret), day_close(cross_delta(nt_cs_rank(cross_sum(Close, 30)), 30)), 50), 40)` |
| window | `ts_std@40->20` | -2.24 | -1.42 | -2.24 | — | `ts_std(ts_cov(day_quantile_q25(Ret), day_close(cross_delta(nt_cs_rank(cross_sum(Open, 30)), 30)), 50), 20)` |
| window | `ts_std@40->80` | -2.26 | -1.62 | -2.26 | — | `ts_std(ts_cov(day_quantile_q25(Ret), day_close(cross_delta(nt_cs_rank(cross_sum(Open, 30)), 30)), 50), 80)` |

## 机械核心卡(B0 按这个顺序取)

1. `cross_regbeta(cross_sum(cross_sum(day_mean(Ret), 10), 15), day_topw_mean(Ret, Close), 241)` — enrichment,均值差 +1.51,p 0.004
2. `cross_sum(cross_sum(day_mean(Ret), 10), 15)` — enrichment,均值差 +1.36,p 0.001
3. `log(cross_regbeta(cross_sum(day_mean(Ret), 15), day_topw_mean(Ret, Close), 241))` — enrichment,均值差 +1.26,p 0.003
4. `cross_sum(day_mean(Ret), 10)` — enrichment,均值差 +1.26,p 0.001
5. `cross_sum(day_mean(Ret), 15)` — enrichment,均值差 +1.24,p 0.000
6. `day_mean(Ret)` — enrichment,均值差 +1.16,p 0.000
7. `cross_regbeta(cross_sum(day_mean(Ret), 15), day_topw_mean(Ret, Close), 241)` — enrichment,均值差 +1.12,p 0.000
8. `cross_semistd_neg(day_topw_mean(Ret, Close), 3)` — enrichment,均值差 +0.49,p 0.074
9. `day_topw_mean(Ret, Ret)` — enrichment,均值差 +0.48,p 0.055
10. `day_topw_mean(Ret, Close)` — enrichment,均值差 +0.34,p 0.042

## 本组之前各轮的任务

- `prods2053Pr1a_Na`:核心 `—`;评分 84,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.74(train -0.74 valid -0.55):`cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30))`
  - score -0.74(train -0.74 valid -0.55):`cs_demean(cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30)))`
  - score -0.74(train -0.74 valid -0.55):`ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 30)`
  - score -0.76(train -0.76 valid -0.62):`cs_demean(ts_stddev(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 40))`
  - score -0.87(train -0.87 valid -0.86):`cs_demean(ts_stddev(ts_quantile_q50(cross_semistd_neg(day_topw_mean(Ret, Close), 3), 5), 40))`
- `prods2053Pr2a_Ea`:核心 `day_topw_mean(Ret, Close)`;评分 84,过线 0,入 heads 0;采样计数 {'c05_no_core': 1212, 'c05_skeleton': 633, 'c05_periphery_seen': 4}
  - score -0.16(train -0.10 valid -0.16):`log(cross_regbeta(cross_sum(cross_sum(day_mean(Ret), 10), 15), day_topw_mean(Ret, Close), 241))`
  - score -0.22(train -0.22 valid +0.05):`log(cross_regbeta(log(cross_regbeta(cross_sum(cross_sum(day_mean(Ret), 10), 15), day_topw_mean(Ret, Close), 241)), day_topw_mean(Ret, Close), 241))`
  - score -0.34(train -0.34 valid +0.29):`log(cross_regbeta(log(cross_regbeta(cross_sum(day_mean(Ret), 15), day_topw_mean(Ret, Close), 241)), day_topw_mean(Ret, Close), 241))`
  - score -0.35(train -0.15 valid -0.35):`log(log(cross_regbeta(cross_sum(day_mean(Ret), 15), day_topw_mean(Ret, Close), 241)))`
  - score -0.38(train -0.05 valid -0.38):`log(cross_regbeta(cross_sum(day_mean(Ret), 15), day_topw_mean(Ret, Close), 241))`
- `prods2053Pr2b_Nb`:核心 `—`;评分 90,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1}
  - score -0.49(train -0.37 valid -0.49):`cross_mean(day_topw_mean(Ret, in_demean(Close)), 241)`
  - score -1.09(train -1.09 valid -0.79):`cross_ema(cs_first_high20(cross_ema(day_topw_mean(Ret, in_first(Close)), 10), ts_min(day_durbin_watson(Close), 50)), 10)`
  - score -1.20(train -1.20 valid -0.96):`cs_first_high20(cross_ema(day_topw_mean(Ret, in_first(Close)), 10), ts_min(day_durbin_watson(Close), 50))`
  - score -1.21(train -1.21 valid -0.78):`cs_first_high20(cross_ema(day_topw_mean(Ret, in_demean(abs_(in_delta(Close, 15)))), 10), ts_min(day_durbin_watson(Close), 50))`
  - score -1.28(train -0.82 valid -1.28):`cross_ema(day_topw_mean(Ret, in_demean(Close)), 10)`

## 比原 head 好的拆解变体(R 候选)

(没有)
