# 定位:种子 2075,P 组,第 2 轮(只含 train / valid)

快照:prods2075M1_I0_open_search, prods2075M2_I0_open_search, prods2075Pr1a_Ea, prods2075Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.12 | +0.03 | -0.12 | +1 | 5 | prods2075M2_I0_open_search | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)` |
| -0.53 | -0.53 | +0.01 | -1 | 20 | prods2075M1_I0_open_search | `abs_(cs_demean(cs_rank(div(ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5), ts_sum(day_sum(Volume), 5)))))` |
| -0.86 | -0.86 | -0.66 | +1 | 20 | prods2075M1_I0_open_search | `cross_autocorr_s1(day_cov(Ret, Volume), 482)` |
| -0.88 | -0.27 | -0.88 | +1 | 20 | prods2075M2_I0_open_search | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 20)` |
| -1.09 | -1.09 | -1.07 | -1 | 0 | prods2075M2_I0_open_search | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0))))), 20)` |
| -1.46 | -1.46 | -0.73 | +1 | 5 | prods2075M1_I0_open_search | `add(sigmoid(sqrt(cross_quantile_q75(day_var(High), 15))), ts_autocorr_s1(ts_scale(cross_hurst(day_durbin_watson(Ret), 5), 20), 40))` |

## 共性:149 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.90 | 0.000 | 12 | -0.76 / -2.66 | `sub(day_wmean(Ret, Volume), day_mean(Ret))` |
| +1.84 | 0.001 | 5 | -0.73 / -2.57 | `cross_ema(day_wmean(Ret, Volume), 20)` |
| +1.72 | 0.004 | 4 | -0.83 / -2.55 | `cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)` |
| +1.71 | 0.000 | 23 | -1.06 / -2.77 | `day_wmean(Ret, Volume)` |
| +1.57 | 0.000 | 15 | -1.09 / -2.67 | `day_mean(Ret)` |
| +1.56 | 0.002 | 5 | -1.00 / -2.56 | `cross_ema(day_std(Ret), 20)` |
| +1.54 | 0.001 | 7 | -1.04 / -2.58 | `day_std(Ret)` |
| +0.78 | 0.046 | 6 | -1.75 / -2.54 | `day_topw_mean(Ret, Amt)` |
| +0.44 | 0.147 | 6 | -2.08 / -2.52 | `day_topw_mean(Ret, Volume)` |
| +0.21 | 0.409 | 4 | -2.30 / -2.51 | `day_cov(Amt, Low)` |
| +0.21 | 0.373 | 8 | -2.31 / -2.52 | `day_last(Close)` |
| -0.07 | 0.594 | 5 | -2.58 / -2.50 | `day_close(Amt)` |
| -0.09 | 0.657 | 4 | -2.59 / -2.50 | `day_sum(Volume)` |
| -0.33 | 0.739 | 4 | -2.83 / -2.50 | `day_max(High)` |
| -0.37 | 0.768 | 7 | -2.86 / -2.49 | `day_durbin_watson(Open)` |
| -0.66 | 0.916 | 4 | -3.15 / -2.49 | `day_first(Open)` |
| -1.31 | 0.992 | 5 | -3.77 / -2.46 | `day_durbin_watson(Vwap)` |

## 拆解(25 次评估)

### head score -0.12:`cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1))` | -0.20 | -0.10 | -0.20 | — | (子树本身) |
| sufficiency | `ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)` | -3.65 | -3.16 | -3.65 | — | (子树本身) |
| sufficiency | `pow_3(ts_std(day_close(Amt), 50))` | -0.52 | -0.52 | -0.39 | — | (子树本身) |
| sufficiency | `signedpower(day_durbin_watson(cross_decay_linear(Amt, 30)))` | -3.65 | -3.16 | -3.65 | — | (子树本身) |
| knockout | `mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1))` | -0.45 | -0.45 | -0.35 | +0.33 | `cross_max(pow_3(ts_std(day_close(Amt), 50)), 5)` |
| knockout | `ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)` | -0.07 | +0.03 | -0.07 | -0.04 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), signedpower(day_durbin_watson(cross_decay_linear(Amt, 30)))), 5)` |
| knockout | `pow_3(ts_std(day_close(Amt), 50))` | -0.35 | -0.07 | -0.35 | +0.24 | `cross_max(mul(ts_std(day_close(Amt), 50), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)` |
| knockout | `signedpower(day_durbin_watson(cross_decay_linear(Amt, 30)))` | -0.19 | -0.12 | -0.19 | +0.07 | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(day_durbin_watson(cross_decay_linear(Amt, 30)), 1)), 5)` |
| swap | `Amt->Volume` | -1.42 | -1.08 | -1.42 | — | `cross_max(mul(pow_3(ts_std(day_close(Volume), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Volume, 30))), 1)), 5)` |
| window | `cross_max@5->2` | -0.20 | -0.03 | -0.20 | — | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 2)` |
| window | `cross_max@5->10` | +0.00 | +0.00 | +0.05 | — | `cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 10)` |

### head score -0.86:`cross_autocorr_s1(day_cov(Ret, Volume), 482)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_cov(Ret, Volume)` | -3.37 | -3.37 | -2.66 | — | (子树本身) |
| swap | `Volume->Amt` | -1.06 | -1.06 | -0.60 | — | `cross_autocorr_s1(day_cov(Ret, Amt), 482)` |
| window | `cross_autocorr_s1@482->241` | -1.12 | -1.12 | -0.75 | — | `cross_autocorr_s1(day_cov(Ret, Volume), 241)` |
| window | `cross_autocorr_s1@482->964` | -1.67 | -1.03 | -1.67 | — | `cross_autocorr_s1(day_cov(Ret, Volume), 964)` |

### head score -0.88:`cross_mean(div(day_skew(Ret), day_kurt(Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_skew(Ret), day_kurt(Ret))` | -2.48 | -2.48 | -2.19 | — | (子树本身) |
| sufficiency | `day_skew(Ret)` | -3.46 | -3.46 | -2.74 | — | (子树本身) |
| sufficiency | `day_kurt(Ret)` | -3.81 | -2.76 | -3.81 | — | (子树本身) |
| knockout | `div(day_skew(Ret), day_kurt(Ret))` | -1.47 | -1.47 | -1.00 | +0.59 | `cross_mean(day_skew(Ret), 20)` |
| window | `cross_mean@20->10` | -0.99 | -0.86 | -0.99 | — | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 10)` |
| window | `cross_mean@20->40` | -0.78 | -0.15 | -0.78 | — | `cross_mean(div(day_skew(Ret), day_kurt(Ret)), 40)` |

### head score -1.09:`cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0))))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0)))))` | -1.20 | -1.16 | -1.20 | — | (子树本身) |
| swap | `Volume->Amt` | -4.62 | -3.47 | -4.62 | — | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Amt, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0))))), 20)` |
| window | `cross_mean@20->10` | -1.52 | -1.22 | -1.52 | — | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0))))), 10)` |
| window | `cross_mean@20->40` | -1.33 | -1.16 | -1.33 | — | `cross_mean(day_sum(div(add(select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Ret, 1, 50), 0), select_where(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0), False), in_slice(Volume, 1, 50), create_like(in_slice(Ret, 1, 50), 0))), in_sum(is_gt(in_slice(Ret, 1, 50), create_like(in_slice(Ret, 1, 50), 0))))), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_wmean(Ret, Volume), day_mean(Ret))` — enrichment,均值差 +1.90,p 0.000
2. `cross_ema(day_wmean(Ret, Volume), 20)` — enrichment,均值差 +1.84,p 0.001
3. `cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)` — enrichment,均值差 +1.72,p 0.004
4. `day_wmean(Ret, Volume)` — enrichment,均值差 +1.71,p 0.000
5. `day_mean(Ret)` — enrichment,均值差 +1.57,p 0.000
6. `cross_ema(day_std(Ret), 20)` — enrichment,均值差 +1.56,p 0.002
7. `day_std(Ret)` — enrichment,均值差 +1.54,p 0.001
8. `day_topw_mean(Ret, Amt)` — enrichment,均值差 +0.78,p 0.046

## 本组之前各轮的任务

- `prods2075Pr1a_Ea`:核心 `ts_sum(mul(sign(sub(div(add(day_last(Close), ts_delay(day_last(Close), 1)), 2), div(day_sum(Amt), day_sum(Volume)))), day_sum(Volume)), 5)`;评分 46,过线 0,入 heads 0;采样计数 {'c05_skeleton': 2815, 'c05_no_core': 4665}
  - score -2.31(train -2.31 valid -2.24):`day_q_stat_std(Amt)`
  - score -2.55(train -2.47 valid -2.55):`day_signed_ratio(Ret, Vwap)`
  - score -2.77(train -2.17 valid -2.77):`day_centroid(Ret)`
  - score -3.08(train -2.24 valid -3.08):`day_es_ratio_hi(Close)`
  - score -3.93(train -3.93 valid -3.13):`day_cov(Ret, Amt)`
- `prods2075Pr1b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {'c05_skeleton': 5}
  - score -0.44(train -0.18 valid -0.44):`div(cross_ema(day_wmean(Ret, Volume), 20), cross_ema(day_std(Ret), 20))`
  - score -0.48(train -0.46 valid -0.48):`cs_demean(cross_ema(sub(cs_demean(cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 15)), day_mean(Ret)), 20))`
  - score -0.48(train -0.37 valid -0.48):`cross_ema(sub(sub(day_wmean(Ret, Volume), day_mean(Ret)), day_mean(Ret)), 20)`
  - score -0.49(train -0.22 valid -0.49):`div(cross_ema(cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 15), 20), cross_ema(day_std(Ret), 20))`
  - score -0.49(train -0.30 valid -0.49):`cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 20)`

## 比原 head 好的拆解变体(R 候选)

(没有)
