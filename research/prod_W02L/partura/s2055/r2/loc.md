# 定位:种子 2055,P 组,第 2 轮(只含 train / valid)

快照:prods2055M1_I0_open_search, prods2055M2_I0_open_search, prods2055Pr1a_Na;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.94 | -0.76 | -0.94 | +1 | 5 | prods2055M1_I0_open_search | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)` |
| -1.82 | -1.78 | -1.82 | +1 | 5 | prods2055M2_I0_open_search | `ts_std(day_var(nt_ts_var(Low, 3)), 50)` |
| -1.83 | -1.62 | -1.83 | +1 | 5 | prods2055M1_I0_open_search | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))), 30)` |
| -1.89 | -0.98 | -1.89 | +1 | 5 | prods2055M1_I0_open_search | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)` |
| -1.94 | -1.76 | -1.94 | -1 | 20 | prods2055M2_I0_open_search | `ts_std(day_last(pow_2_5(nt_ts_var(Low, 3))), 50)` |
| -2.02 | -2.02 | -1.62 | +1 | 5 | prods2055M2_I0_open_search | `ts_std(neg(cross_sum(ts_sum(cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3)))), 10), 241), 10), 30)), 50)` |

## 共性:68 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.22 | 0.000 | 10 | -1.66 / -2.87 | `day_kurt(in_autocorr(Ret, 10, 1))` |
| +0.77 | 0.074 | 4 | -1.97 / -2.74 | `day_kurt(in_autocorr(in_pct(Vwap, 1), 10, 1))` |
| +0.62 | 0.118 | 4 | -2.11 / -2.73 | `day_argmax(Amt)` |
| +0.57 | 0.158 | 4 | -2.16 / -2.73 | `day_var(pow_2_5(pow_2_5(nt_ts_var(Low, 3))))` |
| +0.37 | 0.407 | 5 | -2.35 / -2.72 | `sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))))` |
| +0.37 | 0.407 | 5 | -2.35 / -2.72 | `sigmoid(pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))))))` |
| +0.37 | 0.407 | 5 | -2.35 / -2.72 | `pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))))` |
| +0.36 | 0.433 | 4 | -2.35 / -2.72 | `sigmoid(sigmoid(pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))))))` |
| +0.30 | 0.419 | 6 | -2.42 / -2.72 | `day_median(Open)` |
| +0.29 | 0.425 | 5 | -2.43 / -2.72 | `cross_age(day_median(Open))` |
| +0.23 | 0.568 | 13 | -2.51 / -2.74 | `pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))` |
| -0.59 | 0.987 | 18 | -3.13 / -2.54 | `day_kurt(nt_ts_autocorr_s1(Ret, 3))` |
| -1.62 | 0.996 | 4 | -4.22 / -2.60 | `day_kurt(Ret)` |

## 拆解(19 次评估)

### head score -0.94:`ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_kurt(in_autocorr(Low, 3, 1)))` | -1.76 | -1.49 | -1.76 | — | (子树本身) |
| sufficiency | `day_kurt(in_autocorr(Low, 3, 1))` | -1.51 | -1.48 | -1.51 | — | (子树本身) |
| knockout | `pow_2(day_kurt(in_autocorr(Low, 3, 1)))` | -2.16 | -2.16 | -1.95 | +1.22 | `ts_mean(day_kurt(in_autocorr(Low, 3, 1)), 15)` |
| swap | `Low->High` | -1.04 | -0.77 | -1.04 | — | `ts_mean(pow_2(day_kurt(in_autocorr(High, 3, 1))), 15)` |
| window | `ts_mean@15->7` | -1.14 | -0.95 | -1.14 | — | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 7)` |
| window | `ts_mean@15->30` | -1.28 | -0.71 | -1.28 | — | `ts_mean(pow_2(day_kurt(in_autocorr(Low, 3, 1))), 30)` |

### head score -1.82:`ts_std(day_var(nt_ts_var(Low, 3)), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_var(nt_ts_var(Low, 3))` | -2.12 | -1.59 | -2.12 | — | (子树本身) |
| swap | `Low->High` | -1.82 | -1.82 | -1.82 | — | `ts_std(day_var(nt_ts_var(High, 3)), 50)` |
| window | `ts_std@50->25` | -1.75 | -1.75 | -1.46 | — | `ts_std(day_var(nt_ts_var(Low, 3)), 25)` |
| window | `ts_std@50->100` | -1.78 | -1.78 | -1.67 | — | `ts_std(day_var(nt_ts_var(Low, 3)), 100)` |

### head score -1.89:`cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_kurt(in_autocorr(Ret, 3, 1)))` | -2.75 | -1.36 | -2.75 | — | (子树本身) |
| sufficiency | `day_kurt(in_autocorr(Ret, 3, 1))` | -4.33 | -2.37 | -4.33 | — | (子树本身) |
| knockout | `pow_2(day_kurt(in_autocorr(Ret, 3, 1)))` | -5.60 | -3.45 | -5.60 | +3.71 | `cross_sum(day_kurt(in_autocorr(Ret, 3, 1)), 30)` |
| window | `cross_sum@30->15` | -2.15 | -1.02 | -2.15 | — | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 15)` |
| window | `cross_sum@30->60` | -1.32 | -0.22 | -1.32 | — | `cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 60)` |

### head score -1.94:`ts_std(day_last(pow_2_5(nt_ts_var(Low, 3))), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_last(pow_2_5(nt_ts_var(Low, 3)))` | — | — | — | — | 门槛废品 |
| swap | `Low->High` | -1.92 | -1.92 | -1.85 | — | `ts_std(day_last(pow_2_5(nt_ts_var(High, 3))), 50)` |
| window | `ts_std@50->25` | -1.80 | -1.70 | -1.80 | — | `ts_std(day_last(pow_2_5(nt_ts_var(Low, 3))), 25)` |
| window | `ts_std@50->100` | -2.07 | -1.88 | -2.07 | — | `ts_std(day_last(pow_2_5(nt_ts_var(Low, 3))), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_kurt(in_autocorr(Ret, 10, 1))` — enrichment,均值差 +1.22,p 0.000
2. `day_kurt(in_autocorr(in_pct(Vwap, 1), 10, 1))` — enrichment,均值差 +0.77,p 0.074

## 本组之前各轮的任务

- `prods2055Pr1a_Na`:核心 `—`;评分 64,过线 0,入 heads 0;采样计数 {'c05_skeleton': 4}
  - score -1.04(train -1.04 valid -0.92):`ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 30)`
  - score -1.12(train -1.12 valid -0.98):`ts_quantile_q75(ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 20), 20)`
  - score -1.14(train -1.01 valid -1.14):`ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 50)`
  - score -1.15(train -1.15 valid -0.54):`ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 20)`
  - score -1.26(train -1.06 valid -1.26):`ts_quantile_q75(ts_quantile_q75(day_kurt(in_autocorr(Ret, 10, 1)), 20), 30)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.56(window cross_sum@30->60):`cross_sum(pow_2(day_kurt(in_autocorr(Ret, 3, 1))), 60)`
- 增益 +0.15(window ts_std@50->25):`ts_std(day_last(pow_2_5(nt_ts_var(Low, 3))), 25)`
