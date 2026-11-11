# 定位:种子 2023,P 组,第 3 轮(只含 train / valid)

快照:prods2023M1_I0_open_search, prods2023M2_I0_open_search, prods2023M3_I0_open_search, prods2023Pr1a_Ea, prods2023Pr1b_Nb, prods2023Pr2a_Ea, prods2023Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.64 | +0.64 | +1.16 | +1 | 0 | prods2023Pr2b_Nb | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)` |
| -1.11 | -0.86 | -1.11 | -1 | 5 | prods2023M2_I0_open_search | `cs_demean(cross_mean(cross_regbeta(day_autocorr_n1(High), day_median(Close), 241), 30))` |
| -1.36 | -1.16 | -1.36 | -1 | 0 | prods2023M1_I0_open_search | `ts_max(day_quantile_q75(Volume), 40)` |
| -1.48 | -1.40 | -1.48 | -1 | 5 | prods2023M1_I0_open_search | `ts_stddev(day_quantile_q75(Volume), 10)` |
| -1.52 | -1.52 | -1.51 | +1 | 20 | prods2023M2_I0_open_search | `ts_sum(cross_corr(day_median(Amt), day_first(Amt), 15), 10)` |
| -1.55 | -1.26 | -1.55 | -1 | 20 | prods2023M2_I0_open_search | `ts_cov(day_kurt(Vwap), day_median(Amt), 20)` |
| -1.56 | -1.39 | -1.56 | +1 | 5 | prods2023M1_I0_open_search | `sub(0.5, abs_(ts_regres(day_cov(Close, Open), day_quantile_q75(Volume), 50)))` |

## 共性:253 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.10 | 0.053 | 4 | -1.03 / -2.13 | `day_wmean(Ret, log(abs_(Ret)))` |
| +0.95 | 0.021 | 6 | -1.18 / -2.13 | `day_sum(Volume)` |
| +0.82 | 0.000 | 34 | -1.40 / -2.22 | `day_std(Ret)` |
| +0.70 | 0.033 | 9 | -1.43 / -2.14 | `cross_mean(mul(pow_2(day_sum(Ret)), is_gt(day_sum(Ret), 0)), 241)` |
| +0.63 | 0.000 | 101 | -1.73 / -2.36 | `day_quantile_q75(Volume)` |
| +0.49 | 0.057 | 14 | -1.65 / -2.14 | `mul(pow_2(day_sum(Ret)), is_gt(day_sum(Ret), 0))` |
| +0.44 | 0.128 | 8 | -1.69 / -2.13 | `day_wmean(Ret, is_lt(Volume, day_quantile_q75(Volume)))` |
| +0.43 | 0.184 | 6 | -1.69 / -2.12 | `sub(day_wmean(Ret, is_gt(Volume, day_quantile_q75(Volume))), day_wmean(Ret, is_lt(Volume, day_quantile_q75(Volume))))` |
| +0.41 | 0.190 | 5 | -1.71 / -2.12 | `day_flat_run_max(High)` |
| +0.36 | 0.249 | 4 | -1.75 / -2.12 | `abs_(day_flat_run_max(High))` |
| +0.36 | 0.086 | 19 | -1.78 / -2.14 | `is_gt(day_sum(Ret), 0)` |
| +0.21 | 0.170 | 18 | -1.91 / -2.13 | `day_wmean(Ret, is_gt(Volume, day_quantile_q75(Volume)))` |
| -0.06 | 0.496 | 58 | -2.15 / -2.10 | `day_sum(Ret)` |
| -0.06 | 0.515 | 28 | -2.16 / -2.11 | `pow_2(day_sum(Ret))` |
| -0.06 | 0.450 | 15 | -2.17 / -2.11 | `cross_mean(pow_2(day_sum(Ret)), 241)` |
| -0.10 | 0.636 | 6 | -2.21 / -2.11 | `day_median(Vwap)` |
| -0.11 | 0.629 | 5 | -2.22 / -2.11 | `day_quantile_q75(Low)` |
| -0.17 | 0.609 | 10 | -2.27 / -2.10 | `day_quantile_q75(Ret)` |
| -0.41 | 0.877 | 6 | -2.51 / -2.10 | `day_quantile_q75(Open)` |
| -0.66 | 0.929 | 6 | -2.75 / -2.10 | `day_quantile_q75(Close)` |

## 拆解(3 次评估)

### head score +0.64:`cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_wmean(Ret, log(log(abs_(Ret))))` | -3.80 | -3.80 | -2.98 | — | (子树本身) |
| window | `cross_mean@241->120` | +0.16 | +0.16 | +0.86 | — | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 120)` |
| window | `cross_mean@241->482` | +0.18 | +0.18 | +1.03 | — | `cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 482)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_wmean(Ret, log(abs_(Ret)))` — enrichment,均值差 +1.10,p 0.053
2. `day_sum(Volume)` — enrichment,均值差 +0.95,p 0.021
3. `day_std(Ret)` — enrichment,均值差 +0.82,p 0.000
4. `cross_mean(mul(pow_2(day_sum(Ret)), is_gt(day_sum(Ret), 0)), 241)` — enrichment,均值差 +0.70,p 0.033
5. `day_quantile_q75(Volume)` — enrichment,均值差 +0.63,p 0.000
6. `mul(pow_2(day_sum(Ret)), is_gt(day_sum(Ret), 0))` — enrichment,均值差 +0.49,p 0.057
7. `is_gt(day_sum(Ret), 0)` — enrichment,均值差 +0.36,p 0.086

## 本组之前各轮的任务

- `prods2023Pr1a_Ea`:核心 `day_quantile_q75(Volume)`;评分 95,过线 0,入 heads 0;采样计数 {'c05_no_core': 1290, 'c05_skeleton': 626}
  - score -0.43(train -0.08 valid -0.43):`cross_corr(sub(log(add(day_quantile_q75(Volume), 100)), cross_corr(day_quantile_q75(Volume), day_sum(Volume), 10)), day_std(Ret), 241)`
  - score -0.53(train -0.53 valid -0.49):`cross_corr(sub(log(add(day_quantile_q75(Volume), sub(log(add(day_quantile_q75(Volume), 100)), LogFloatShares))), LogFloatShares), day_std(Ret), 241)`
  - score -0.54(train -0.51 valid -0.54):`cross_corr(sub(log(add(day_quantile_q75(Volume), sub(log(add(day_quantile_q75(Volume), add(day_quantile_q75(Volume), sub(log(add(day_quantile_q75(Volume), -2)), cross_corr(day_quantile_q75(Volume), day_sum(Volume), 241))))), LogFloatShares))), LogFloatShares), day_std(Ret), 241)`
  - score -0.54(train -0.54 valid -0.41):`cross_corr(log(add(day_quantile_q75(Volume), 100)), day_std(Ret), 241)`
  - score -0.57(train -0.57 valid -0.49):`cross_corr(sub(log(add(day_quantile_q75(Volume), add(day_quantile_q75(Volume), sub(log(add(day_quantile_q75(Volume), -5)), LogFloatShares)))), LogFloatShares), day_std(Ret), 241)`
- `prods2023Pr1b_Nb`:核心 `—`;评分 83,过线 0,入 heads 0;采样计数 {'c05_skeleton': 8}
  - score +0.44(train +0.44 valid +1.01):`cross_mean(day_wmean(Ret, log(Ret)), 241)`
  - score -0.39(train -0.39 valid +0.72):`cross_mean(div(sub(day_wmean(Ret, cross_mean(Volume, 20)), day_wmean(Ret, is_lt(Ret, day_quantile_q75(Volume)))), add(day_std(Ret), 2)), 241)`
  - score -0.88(train -0.88 valid +0.08):`cross_mean(day_wmean(Ret, is_gt(Volume, day_quantile_q75(is_gt(Volume, day_quantile_q75(Volume))))), 241)`
  - score -0.88(train -0.88 valid +0.08):`cross_mean(day_wmean(Ret, is_gt(Volume, day_quantile_q75(Ret))), 241)`
  - score -0.88(train -0.88 valid +0.08):`cross_mean(day_wmean(Ret, is_gt(Volume, day_quantile_q75(is_gt(Volume, day_wmean(Ret, is_lt(Ret, day_quantile_q75(Volume))))))), 241)`
- `prods2023Pr2a_Ea`:核心 `day_sum(Ret)`;评分 81,过线 0,入 heads 0;采样计数 {'c05_no_core': 1178, 'c05_skeleton': 512}
  - score -0.51(train -0.51 valid -0.33):`div(cross_mean(mul(pow_2(day_sum(Ret)), is_gt(day_sum(Ret), 0)), 241), add(cross_mean(pow_2(day_sum(Ret)), 241), 1e-06))`
  - score -0.51(train -0.51 valid -0.33):`div(cross_mean(mul(mul(pow_2(day_sum(Ret)), is_gt(day_sum(Ret), 0)), is_gt(day_sum(Ret), 0)), 241), add(cross_mean(pow_2(day_sum(Ret)), 241), 1e-06))`
  - score -0.54(train -0.54 valid -0.22):`div(cross_mean(mul(pow_2(day_sum(Ret)), day_ar1_coefficient(Vwap)), 241), add(cross_mean(mul(pow_2(day_sum(Ret)), is_gt(day_sum(Ret), 0)), 241), 1e-06))`
  - score -0.72(train -0.47 valid -0.72):`cross_corr(day_sum(Ret), sub(day_sum(Ret), abs_(day_flat_run_max(High))), 60)`
  - score -0.83(train -0.79 valid -0.83):`div(cross_mean(day_sum(Ret), 241), add(cross_mean(pow_2(day_sum(Ret)), 241), 1e-06))`
- `prods2023Pr2b_Nb`:核心 `—`;评分 76,过线 4,入 heads 1;采样计数 {}
  - score +0.64(train +0.64 valid +1.16):`cross_mean(day_wmean(Ret, log(log(abs_(Ret)))), 241)`
  - score +0.64(train +0.64 valid +1.16):`cross_mean(day_wmean(Ret, log(abs_(log(abs_(Ret))))), 241)`
  - score +0.64(train +0.64 valid +1.16):`cross_mean(day_wmean(Ret, log(log(Ret))), 241)`
  - score +0.64(train +0.64 valid +1.16):`cross_mean(day_wmean(Ret, log(abs_(abs_(log(abs_(Ret)))))), 241)`
  - score +0.44(train +0.44 valid +1.01):`cross_mean(day_wmean(Ret, log(abs_(Ret))), 241)`

## 比原 head 好的拆解变体(R 候选)

(没有)
