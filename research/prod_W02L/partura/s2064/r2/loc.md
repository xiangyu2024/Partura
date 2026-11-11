# 定位:种子 2064,P 组,第 2 轮(只含 train / valid)

快照:prods2064M1_I0_open_search, prods2064M2_I0_open_search, prods2064Pr1a_Ea, prods2064Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.35 | -0.35 | -0.18 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 25)` |
| -0.50 | -0.28 | -0.50 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 10), 30)), 50)` |
| -0.63 | -0.63 | +0.25 | +1 | 0 | prods2064M1_I0_open_search | `ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 241)), 50)` |
| -1.22 | -1.22 | +0.03 | -1 | 5 | prods2064M2_I0_open_search | `neg(cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)), 241))` |
| -1.73 | -1.73 | -1.55 | -1 | 0 | prods2064M2_I0_open_search | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10), 241))` |
| -2.05 | -2.00 | -2.05 | -1 | 20 | prods2064M2_I0_open_search | `day_durbin_watson(nt_ts_max(nt_ts_max(Vwap, 5), 5))` |

## 共性:91 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.56 | 0.001 | 5 | -0.25 / -1.81 | `ts_delay(day_last(High), 1)` |
| +1.56 | 0.001 | 5 | -0.25 / -1.81 | `day_last(High)` |
| +1.48 | 0.000 | 32 | -0.76 / -2.24 | `div(day_max(High), ts_delay(day_last(Close), 1))` |
| +1.45 | 0.004 | 4 | -0.33 / -1.79 | `div(day_max(High), ts_delay(day_last(High), 1))` |
| +1.43 | 0.000 | 36 | -0.86 / -2.29 | `day_max(High)` |
| +1.35 | 0.000 | 39 | -0.95 / -2.30 | `day_last(Close)` |
| +1.33 | 0.000 | 38 | -0.95 / -2.28 | `ts_delay(day_last(Close), 1)` |
| +1.01 | 0.000 | 25 | -0.99 / -2.00 | `div(day_last(Close), ts_delay(day_last(Close), 1))` |
| +0.07 | 0.524 | 5 | -1.66 / -1.73 | `day_var(pow_2_5(neg(Ret)))` |
| +0.02 | 0.667 | 25 | -1.71 / -1.73 | `day_var(pow_2_5(Ret))` |
| -1.26 | 0.994 | 6 | -2.90 / -1.64 | `day_close(pow_2_5(Amt))` |

## 拆解(31 次评估)

### head score -0.35:`ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 25)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30))` | -1.21 | -0.76 | -1.21 | — | (子树本身) |
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)` | -1.21 | -0.76 | -1.21 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(Ret)), 40)` | -1.31 | -1.12 | -1.31 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(Ret))` | -3.10 | -2.51 | -3.10 | — | (子树本身) |
| knockout | `neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30))` | -0.35 | -0.35 | -0.18 | -0.00 | `ts_std(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30), 25)` |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)` | -0.83 | -0.55 | -0.83 | +0.48 | `ts_std(neg(ts_sum(day_var(pow_2_5(Ret)), 40)), 25)` |
| knockout | `ts_sum(day_var(pow_2_5(Ret)), 40)` | -1.25 | -0.94 | -1.25 | +0.90 | `ts_std(neg(cross_sum(day_var(pow_2_5(Ret)), 30)), 25)` |
| window | `ts_std@25->12` | -0.58 | -0.58 | -0.48 | — | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 12)` |
| window | `ts_std@25->50` | -0.46 | -0.46 | -0.40 | — | `ts_std(neg(cross_sum(ts_sum(day_var(pow_2_5(Ret)), 40), 30)), 50)` |

### head score -1.22:`neg(cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)), 241)` | -1.22 | -1.22 | -0.02 | — | (子树本身) |
| sufficiency | `neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241))` | -0.91 | -0.91 | -0.53 | — | (子树本身) |
| sufficiency | `cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)` | -0.91 | -0.91 | -0.53 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10)` | -1.81 | -1.27 | -1.81 | — | (子树本身) |
| knockout | `cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)), 241)` | -0.91 | -0.91 | -0.53 | -0.32 | `neg(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)))` |
| knockout | `neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241))` | -1.22 | -1.22 | -0.02 | -0.00 | `neg(cross_sum(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241), 241))` |
| knockout | `cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)` | -0.91 | -0.91 | -0.53 | -0.32 | `neg(cross_sum(neg(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10)), 241))` |
| knockout | `ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10)` | -1.32 | -1.32 | -0.18 | +0.09 | `neg(cross_sum(neg(cross_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 241)), 241))` |
| swap | `Amt->Volume` | -1.01 | -1.01 | +0.07 | — | `neg(cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Volume, 15), 241), 15)), 10), 241)), 241))` |
| window | `cross_sum@241->120` | -1.31 | -1.31 | -0.21 | — | `neg(cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)), 120))` |
| window | `cross_sum@241->482` | -1.30 | -1.30 | -0.30 | — | `neg(cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)), 482))` |

### head score -1.73:`neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10), 241)` | -1.73 | -1.73 | -1.59 | — | (子树本身) |
| sufficiency | `ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10)` | -2.44 | -1.78 | -2.44 | — | (子树本身) |
| sufficiency | `day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3)))` | -2.11 | -1.59 | -2.11 | — | (子树本身) |
| knockout | `cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10), 241)` | -2.44 | -1.78 | -2.44 | +0.71 | `neg(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10))` |
| knockout | `ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10)` | -1.76 | -1.76 | -1.51 | +0.03 | `neg(cross_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 241))` |
| swap | `Low->High` | -1.92 | -1.92 | -1.75 | — | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(High, 3), 3))), 10), 241))` |
| window | `cross_sum@241->120` | -1.93 | -1.86 | -1.93 | — | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10), 120))` |
| window | `cross_sum@241->482` | -2.07 | -2.07 | -1.80 | — | `neg(cross_sum(ts_sum(day_var(pow_2_5(nt_ts_var(nt_ts_max(Low, 3), 3))), 10), 482))` |

### head score -2.05:`day_durbin_watson(nt_ts_max(nt_ts_max(Vwap, 5), 5))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Vwap->Close` | -2.80 | -2.80 | -2.62 | — | `day_durbin_watson(nt_ts_max(nt_ts_max(Close, 5), 5))` |
| window | `nt_ts_max@5->2` | -2.12 | -2.12 | -2.05 | — | `day_durbin_watson(nt_ts_max(nt_ts_max(Vwap, 5), 2))` |
| window | `nt_ts_max@5->10` | -2.00 | -1.97 | -2.00 | — | `day_durbin_watson(nt_ts_max(nt_ts_max(Vwap, 5), 10))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_delay(day_last(High), 1)` — enrichment,均值差 +1.56,p 0.001
2. `day_last(High)` — enrichment,均值差 +1.56,p 0.001
3. `div(day_max(High), ts_delay(day_last(Close), 1))` — enrichment,均值差 +1.48,p 0.000
4. `div(day_max(High), ts_delay(day_last(High), 1))` — enrichment,均值差 +1.45,p 0.004
5. `day_max(High)` — enrichment,均值差 +1.43,p 0.000
6. `day_last(Close)` — enrichment,均值差 +1.35,p 0.000
7. `ts_delay(day_last(Close), 1)` — enrichment,均值差 +1.33,p 0.000
8. `div(day_last(Close), ts_delay(day_last(Close), 1))` — enrichment,均值差 +1.01,p 0.000

## 本组之前各轮的任务

- `prods2064Pr1a_Ea`:核心 `day_var(pow_2_5(Ret))`;评分 65,过线 0,入 heads 0;采样计数 {'c05_skeleton': 1028, 'c05_no_core': 2295, 'c05_periphery_seen': 8}
  - score -0.63(train -0.63 valid +0.20):`cross_autocorr(day_var(pow_2_5(Ret)), 120, 1)`
  - score -0.82(train -0.82 valid -0.41):`cross_corr(day_var(pow_2_5(Ret)), day_var(pow_2_5(neg(Ret))), 120)`
  - score -1.02(train -1.02 valid -0.32):`cross_corr(day_var(pow_2_5(Ret)), cross_delay(day_last(Close), 1), 120)`
  - score -1.52(train -1.47 valid -1.52):`cs_first_low20(cross_flat_ratio(day_es_ratio_lo(Open), 10), cross_tail_mean_q75(day_var(pow_2_5(Ret)), 10))`
  - score -1.56(train -1.56 valid +0.04):`div(cross_mean(day_var(pow_2_5(Ret)), 60), cross_mean(day_var(pow_2_5(neg(Ret))), 60))`
- `prods2064Pr1b_Nb`:核心 `—`;评分 60,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score +0.09(train +0.28 valid +0.09):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(High), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth))), 120)`
  - score +0.09(train +0.28 valid +0.09):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(High), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95)), LimitWidth))), 120)`
  - score +0.09(train +0.12 valid +0.09):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(Low), 1)), 1), LimitWidth))), 120)`
  - score +0.09(train +0.23 valid +0.09):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(Close), 1)), 1), LimitWidth))), 120)`
  - score +0.08(train +0.43 valid +0.08):`cross_mean(mul(is_gt(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), 0.95), sub(div(sub(div(day_max(High), ts_delay(day_last(Close), 1)), 1), LimitWidth), div(sub(div(day_last(Close), ts_delay(day_last(High), 1)), 1), LimitWidth))), 120)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.32(knockout cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)), 241)):`neg(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)))`
- 增益 +0.32(knockout cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10), 241)):`neg(cross_sum(neg(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Amt, 15), 241), 15)), 10)), 241))`
- 增益 +0.22(swap Amt->Volume):`neg(cross_sum(neg(cross_sum(ts_sum(day_var(in_quantile_q50(cross_rank(nt_ts_max(Volume, 15), 241), 15)), 10), 241)), 241))`
