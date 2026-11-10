# 定位:种子 2007,P 组,第 2 轮(只含 train / valid)

快照:prods2007M1_I0_open_search, prods2007M2_I0_open_search, prods2007Pr1a_Ea, prods2007Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.39 | -0.39 | -0.10 | +1 | 5 | prods2007M2_I0_open_search | `abs_(ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 10), 40))` |
| -0.56 | -0.56 | -0.55 | +1 | 5 | prods2007M2_I0_open_search | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` |
| -0.58 | -0.58 | -0.49 | +1 | 5 | prods2007M2_I0_open_search | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1)), 5)` |
| -1.07 | -1.07 | -0.63 | +1 | 5 | prods2007M1_I0_open_search | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)` |
| -2.06 | -2.06 | -1.72 | +1 | 0 | prods2007M1_I0_open_search | `cross_sum(day_durbin_watson(Close), 60)` |
| -3.13 | -3.13 | -2.71 | +1 | 20 | prods2007M1_I0_open_search | `log(day_durbin_watson(Vwap))` |

## 共性:177 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.73 | 0.001 | 4 | -0.81 / -2.54 | `ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40)` |
| +1.24 | 0.004 | 6 | -1.30 / -2.54 | `ts_scale(day_sum(Amt), 30)` |
| +1.22 | 0.000 | 12 | -1.36 / -2.58 | `day_close(cross_decay_linear(Amt, 30))` |
| +1.18 | 0.005 | 6 | -1.36 / -2.54 | `day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3))` |
| +0.98 | 0.003 | 13 | -1.59 / -2.57 | `day_sum(Amt)` |
| +0.97 | 0.040 | 5 | -1.55 / -2.53 | `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` |
| +0.96 | 0.029 | 6 | -1.57 / -2.53 | `day_sum(Vwap)` |
| +0.91 | 0.096 | 4 | -1.61 / -2.52 | `ts_scale(day_sum(Amt), 10)` |
| +0.85 | 0.021 | 11 | -1.70 / -2.55 | `day_sum(Ret)` |
| +0.73 | 0.175 | 4 | -1.79 / -2.52 | `cross_corr(day_centroid(in_slice(Ret, 1, 240)), day_centroid(Amt), 60)` |
| +0.56 | 0.262 | 4 | -1.95 / -2.51 | `pow_3(day_durbin_watson(Open))` |
| +0.54 | 0.189 | 5 | -1.98 / -2.52 | `div(day_first(Open), ts_delay(day_last(Close), 1))` |
| +0.44 | 0.225 | 30 | -2.14 / -2.57 | `day_centroid(in_slice(Ret, 1, 240))` |
| +0.41 | 0.280 | 8 | -2.11 / -2.52 | `day_last(Close)` |
| +0.41 | 0.280 | 8 | -2.11 / -2.52 | `ts_delay(day_last(Close), 1)` |
| +0.40 | 0.315 | 6 | -2.12 / -2.51 | `day_last(Open)` |
| +0.36 | 0.347 | 5 | -2.15 / -2.51 | `ts_delay(day_last(Open), 1)` |
| +0.32 | 0.439 | 18 | -2.21 / -2.53 | `day_centroid(Amt)` |
| +0.29 | 0.361 | 18 | -2.24 / -2.53 | `day_first(Open)` |
| +0.28 | 0.537 | 4 | -2.23 / -2.51 | `log(day_durbin_watson(in_slice(Vwap, 1, 120)))` |

## 拆解(29 次评估)

### head score -0.39:`abs_(ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 10), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 10), 40)` | -0.39 | -0.39 | -0.07 | — | (子树本身) |
| sufficiency | `ts_std(day_close(cross_decay_linear(Amt, 30)), 10)` | -1.21 | -1.21 | -1.02 | — | (子树本身) |
| sufficiency | `day_close(cross_decay_linear(Amt, 30))` | -3.52 | -2.79 | -3.52 | — | (子树本身) |
| knockout | `ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 10), 40)` | -1.21 | -1.21 | -1.02 | +0.83 | `abs_(ts_std(day_close(cross_decay_linear(Amt, 30)), 10))` |
| knockout | `ts_std(day_close(cross_decay_linear(Amt, 30)), 10)` | -0.56 | -0.56 | -0.53 | +0.17 | `abs_(ts_std(day_close(cross_decay_linear(Amt, 30)), 40))` |
| swap | `Amt->Volume` | -1.89 | -1.23 | -1.89 | — | `abs_(ts_std(ts_std(day_close(cross_decay_linear(Volume, 30)), 10), 40))` |
| window | `ts_std@40->20` | -0.69 | -0.69 | -0.54 | — | `abs_(ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 10), 20))` |
| window | `ts_std@40->80` | -0.07 | -0.07 | +0.14 | — | `abs_(ts_std(ts_std(day_close(cross_decay_linear(Amt, 30)), 10), 80))` |

### head score -0.56:`ts_std(day_close(cross_decay_linear(Amt, 30)), 40)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_close(cross_decay_linear(Amt, 30))` | -3.52 | -2.79 | -3.52 | — | (子树本身) |
| swap | `Amt->Volume` | -1.55 | -1.20 | -1.55 | — | `ts_std(day_close(cross_decay_linear(Volume, 30)), 40)` |
| window | `ts_std@40->20` | -0.91 | -0.91 | -0.81 | — | `ts_std(day_close(cross_decay_linear(Amt, 30)), 20)` |
| window | `ts_std@40->80` | -0.39 | -0.39 | -0.16 | — | `ts_std(day_close(cross_decay_linear(Amt, 30)), 80)` |

### head score -0.58:`cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1))` | -0.58 | -0.58 | -0.48 | — | (子树本身) |
| sufficiency | `ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1)` | -0.48 | -0.48 | -0.47 | — | (子树本身) |
| sufficiency | `pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5))` | -0.48 | -0.48 | -0.47 | — | (子树本身) |
| sufficiency | `cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)` | -0.48 | -0.48 | -0.47 | — | (子树本身) |
| knockout | `mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1))` | -3.79 | -3.79 | -3.61 | +3.22 | `cross_max(day_close(in_kurt_full(Amt)), 5)` |
| knockout | `ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1)` | -0.58 | -0.58 | -0.46 | -0.00 | `cross_max(mul(day_close(in_kurt_full(Amt)), pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5))), 5)` |
| knockout | `pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5))` | -0.74 | -0.66 | -0.74 | +0.17 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5), 1)), 5)` |
| knockout | `cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)` | -0.51 | -0.51 | -0.48 | -0.06 | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40)), 1)), 5)` |
| swap | `Amt->Volume` | -2.47 | -1.44 | -2.47 | — | `cross_max(mul(day_close(in_kurt_full(Volume)), ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Volume, 30), 3)), 40), 5)), 1)), 5)` |
| window | `cross_max@5->2` | -0.63 | -0.63 | -0.40 | — | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1)), 2)` |
| window | `cross_max@5->10` | -0.81 | -0.81 | -0.33 | — | `cross_max(mul(day_close(in_kurt_full(Amt)), ts_min(pow_3(cross_max(ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40), 5)), 1)), 10)` |

### head score -1.07:`cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_scale(day_durbin_watson(Vwap), 10)` | -5.65 | -5.65 | -4.46 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Vwap)` | -3.20 | -3.20 | -2.89 | — | (子树本身) |
| knockout | `ts_scale(day_durbin_watson(Vwap), 10)` | -1.99 | -1.63 | -1.99 | +0.92 | `cross_fangzheng(day_durbin_watson(Vwap), 60)` |
| swap | `Vwap->Close` | -3.00 | -1.09 | -3.00 | — | `cross_fangzheng(ts_scale(day_durbin_watson(Close), 10), 60)` |
| window | `cross_fangzheng@60->30` | -1.82 | -1.82 | -0.38 | — | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 30)` |
| window | `cross_fangzheng@60->120` | -1.36 | -1.36 | -0.73 | — | `cross_fangzheng(ts_scale(day_durbin_watson(Vwap), 10), 120)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_std(day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3)), 40)` — enrichment,均值差 +1.73,p 0.001
2. `ts_scale(day_sum(Amt), 30)` — enrichment,均值差 +1.24,p 0.004
3. `day_close(cross_decay_linear(Amt, 30))` — enrichment,均值差 +1.22,p 0.000
4. `day_close(cross_decay_linear(cross_decay_linear(Amt, 30), 3))` — enrichment,均值差 +1.18,p 0.005
5. `day_sum(Amt)` — enrichment,均值差 +0.98,p 0.003
6. `ts_std(day_close(cross_decay_linear(Amt, 30)), 40)` — enrichment,均值差 +0.97,p 0.040
7. `day_sum(Vwap)` — enrichment,均值差 +0.96,p 0.029
8. `ts_scale(day_sum(Amt), 10)` — enrichment,均值差 +0.91,p 0.096
9. `day_sum(Ret)` — enrichment,均值差 +0.85,p 0.021
10. `ts_scale(day_durbin_watson(Vwap), 10)` — enrichment,均值差 +0.27,p 0.002
11. `day_durbin_watson(Vwap)` — enrichment,均值差 +0.06,p 0.030

## 本组之前各轮的任务

- `prods2007Pr1a_Ea`:核心 `ts_scale(day_durbin_watson(Vwap), 10)`;评分 86,过线 0,入 heads 0;采样计数 {'c05_no_core': 646, 'c05_skeleton': 318, 'c05_periphery_seen': 5, 'mutation_refused': 2}
  - score -0.70(train -0.05 valid -0.70):`cross_corr(ts_scale(day_durbin_watson(Vwap), 10), ts_scale(day_sum(Volume), 30), 60)`
  - score -0.70(train -0.70 valid -0.03):`cross_cov(ts_scale(day_durbin_watson(Vwap), 10), day_sum(Ret), 60)`
  - score -0.71(train -0.71 valid -0.46):`cross_corr(ts_scale(day_durbin_watson(Vwap), 10), day_sum(Ret), 60)`
  - score -0.77(train -0.13 valid -0.77):`cross_corr(ts_scale(day_durbin_watson(Vwap), 10), ts_scale(day_sum(Amt), 30), 60)`
  - score -0.78(train -0.61 valid -0.78):`cross_corr(ts_scale(day_durbin_watson(Vwap), 10), day_quantile_q25(Low), 60)`
- `prods2007Pr1b_Nb`:核心 `—`;评分 59,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -0.90(train -0.04 valid -0.90):`cross_corr(day_centroid(in_slice(Ret, 1, 240)), day_centroid(Amt), 60)`
  - score -1.07(train -0.11 valid -1.07):`cross_mean(cross_corr(day_centroid(in_slice(Ret, 1, 240)), day_centroid(Amt), 60), 40)`
  - score -1.65(train -1.65 valid -0.73):`cross_mean(sub(log(day_durbin_watson(in_slice(Vwap, 1, 120))), log(day_durbin_watson(in_slice(Vwap, 121, 240)))), 40)`
  - score -1.73(train -0.15 valid -1.73):`cross_corr(day_centroid(in_slice(Ret, 1, 240)), sub(div(day_first(Open), ts_delay(day_last(Open), 1)), 1), 60)`
  - score -1.73(train -0.14 valid -1.73):`cross_corr(day_centroid(in_slice(Ret, 1, 240)), sub(div(day_first(Open), ts_delay(day_last(Open), 1)), -1), 60)`

## 比原 head 好的拆解变体(R 候选)

(没有)
