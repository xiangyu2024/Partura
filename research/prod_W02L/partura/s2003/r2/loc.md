# 定位:种子 2003,P 组,第 2 轮(只含 train / valid)

快照:prods2003M1_I0_open_search, prods2003M2_I0_open_search, prods2003Pr1a_Ea;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.20 | -0.96 | -1.20 | +1 | 20 | prods2003M1_I0_open_search | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 25)` |
| -1.23 | -1.11 | -1.23 | +1 | 0 | prods2003M1_I0_open_search | `ts_mean(mul(log(ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 40)), day_std(Vwap))), ts_hurst(div(day_last(Volume), day_max(Volume)), 20)), 50)), day_max(Volume)), 50)` |
| -1.57 | -1.56 | -1.57 | -1 | 0 | prods2003M1_I0_open_search | `ts_mean(mul(log(add(mul(log(add(day_q_stat_std(Vwap), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), day_std(Volume))), ts_hurst(div(day_last(Volume), day_max(Low)), 20)), 50)` |
| -2.70 | -2.10 | -2.70 | -1 | 20 | prods2003M2_I0_open_search | `sigmoid(sigmoid(day_max(Ret)))` |
| -2.70 | -2.10 | -2.70 | -1 | 20 | prods2003M2_I0_open_search | `pow_2(sigmoid(sigmoid(day_max(Ret))))` |
| -2.70 | -2.10 | -2.70 | -1 | 20 | prods2003M2_I0_open_search | `pow_2(pow_2(sigmoid(sigmoid(day_max(Ret)))))` |

## 共性:58 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.94 | 0.005 | 7 | -1.91 / -2.85 | `day_last(Volume)` |
| +0.90 | 0.017 | 6 | -1.93 / -2.83 | `log(add(day_q_stat_std(Vwap), day_std(Vwap)))` |
| +0.90 | 0.017 | 6 | -1.93 / -2.83 | `add(day_q_stat_std(Vwap), day_std(Vwap))` |
| +0.79 | 0.018 | 6 | -2.03 / -2.82 | `div(day_last(Volume), day_max(Low))` |
| +0.73 | 0.024 | 8 | -2.10 / -2.84 | `day_std(Vwap)` |
| +0.71 | 0.016 | 9 | -2.13 / -2.85 | `day_max(Low)` |
| +0.69 | 0.048 | 5 | -2.11 / -2.80 | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` |
| +0.41 | 0.086 | 17 | -2.45 / -2.86 | `day_q_stat_std(Volume)` |
| +0.40 | 0.188 | 5 | -2.37 / -2.77 | `cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 60)` |
| +0.04 | 0.682 | 6 | -2.70 / -2.74 | `day_max(Ret)` |
| +0.04 | 0.651 | 5 | -2.70 / -2.74 | `sigmoid(day_max(Ret))` |
| -0.90 | 0.984 | 4 | -3.58 / -2.67 | `cross_mean(day_q_stat_std(Vwap), 30)` |

## 拆解(21 次评估)

### head score -1.20:`ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 25)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.29 | -0.98 | -1.29 | — | (子树本身) |
| sufficiency | `div(day_last(Volume), day_max(Low))` | -1.55 | -1.55 | -1.50 | — | (子树本身) |
| sufficiency | `day_last(Volume)` | -1.61 | -1.18 | -1.61 | — | (子树本身) |
| sufficiency | `day_max(Low)` | -2.38 | -1.59 | -2.38 | — | (子树本身) |
| knockout | `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` | -1.62 | -1.50 | -1.62 | +0.42 | `ts_mean(div(day_last(Volume), day_max(Low)), 25)` |
| knockout | `div(day_last(Volume), day_max(Low))` | -1.28 | -0.83 | -1.28 | +0.09 | `ts_mean(ts_hurst(day_last(Volume), 20), 25)` |
| swap | `Volume->Amt` | -1.37 | -0.77 | -1.37 | — | `ts_mean(ts_hurst(div(day_last(Amt), day_max(Low)), 20), 25)` |
| swap | `Low->High` | -1.14 | -0.99 | -1.14 | — | `ts_mean(ts_hurst(div(day_last(Volume), day_max(High)), 20), 25)` |
| window | `ts_mean@25->12` | -1.32 | -0.95 | -1.32 | — | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 12)` |
| window | `ts_mean@25->50` | -1.01 | -1.00 | -1.01 | — | `ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 50)` |

### head score -2.70:`sigmoid(sigmoid(day_max(Ret)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(day_max(Ret))` | -2.65 | -2.10 | -2.65 | — | (子树本身) |
| sufficiency | `day_max(Ret)` | -2.65 | -2.11 | -2.65 | — | (子树本身) |

### head score -2.70:`pow_2(sigmoid(sigmoid(day_max(Ret))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sigmoid(sigmoid(day_max(Ret)))` | -2.65 | -2.10 | -2.65 | — | (子树本身) |
| sufficiency | `sigmoid(day_max(Ret))` | -2.65 | -2.10 | -2.65 | — | (子树本身) |
| sufficiency | `day_max(Ret)` | -2.65 | -2.11 | -2.65 | — | (子树本身) |
| knockout | `sigmoid(sigmoid(day_max(Ret)))` | -2.65 | -2.10 | -2.65 | -0.05 | `pow_2(sigmoid(day_max(Ret)))` |

### head score -2.70:`pow_2(pow_2(sigmoid(sigmoid(day_max(Ret)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(sigmoid(sigmoid(day_max(Ret))))` | -2.65 | -2.10 | -2.65 | — | (子树本身) |
| sufficiency | `sigmoid(sigmoid(day_max(Ret)))` | -2.65 | -2.10 | -2.65 | — | (子树本身) |
| sufficiency | `sigmoid(day_max(Ret))` | -2.65 | -2.10 | -2.65 | — | (子树本身) |
| sufficiency | `day_max(Ret)` | -2.65 | -2.11 | -2.65 | — | (子树本身) |
| knockout | `sigmoid(sigmoid(day_max(Ret)))` | -2.65 | -2.10 | -2.65 | -0.05 | `pow_2(pow_2(sigmoid(day_max(Ret))))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_last(Volume)` — enrichment,均值差 +0.94,p 0.005
2. `log(add(day_q_stat_std(Vwap), day_std(Vwap)))` — enrichment,均值差 +0.90,p 0.017
3. `add(day_q_stat_std(Vwap), day_std(Vwap))` — enrichment,均值差 +0.90,p 0.017
4. `div(day_last(Volume), day_max(Low))` — enrichment,均值差 +0.79,p 0.018
5. `day_std(Vwap)` — enrichment,均值差 +0.73,p 0.024
6. `day_max(Low)` — enrichment,均值差 +0.71,p 0.016
7. `ts_hurst(div(day_last(Volume), day_max(Low)), 20)` — enrichment,均值差 +0.69,p 0.048
8. `day_q_stat_std(Volume)` — enrichment,均值差 +0.41,p 0.086

## 本组之前各轮的任务

- `prods2003Pr1a_Ea`:核心 `day_q_stat_std(Vwap)`;评分 69,过线 0,入 heads 0;采样计数 {'c05_no_core': 1031, 'c05_skeleton': 492}
  - score -0.90(train -0.90 valid -0.77):`cross_corr(day_q_stat_std(Vwap), day_autocorr_n1(Volume), 60)`
  - score -0.98(train -0.90 valid -0.98):`cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 15)`
  - score -1.34(train -1.34 valid -1.04):`cross_corr(cross_corr(day_q_stat_std(Vwap), cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 5), 60), cross_corr(cross_corr(day_q_stat_std(Vwap), cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 5), 60), day_q_stat_std(Volume), 60), 60)`
  - score -1.64(train -0.83 valid -1.64):`cross_corr(day_q_stat_std(Vwap), day_q_stat_std(Volume), 60)`
  - score -1.78(train -1.38 valid -1.78):`cross_corr(day_q_stat_std(Vwap), day_sum(Ret), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(window ts_mean@25->50):`ts_mean(ts_hurst(div(day_last(Volume), day_max(Low)), 20), 50)`
