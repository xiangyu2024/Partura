# 定位:种子 2055,P 组,第 1 轮(只含 train / valid)

快照:prods2055M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.74 | -0.82 | -1.74 | +1 | 5 | prods2055M1_I0_open_search | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), 30)` |
| -1.83 | -1.62 | -1.83 | +1 | 5 | prods2055M1_I0_open_search | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))), 30)` |
| -2.19 | -1.02 | -2.19 | +1 | 20 | prods2055M1_I0_open_search | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` |

## 共性:20 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.39 | 0.067 | 13 | -2.51 / -3.90 | `pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))` |
| +0.86 | 0.153 | 5 | -2.35 / -3.21 | `sigmoid(pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))))))` |
| +0.86 | 0.153 | 5 | -2.35 / -3.21 | `pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))))` |
| +0.86 | 0.153 | 5 | -2.35 / -3.21 | `sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))))` |
| +0.80 | 0.219 | 4 | -2.35 / -3.16 | `sigmoid(sigmoid(pow_2(sigmoid(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))))))` |

## 拆解(17 次评估)

### head score -1.74:`ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3)))` | -1.76 | -1.49 | -1.76 | — | (子树本身) |
| sufficiency | `day_kurt(nt_ts_autocorr_s1(Low, 3))` | -1.51 | -1.48 | -1.51 | — | (子树本身) |
| knockout | `pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3)))` | -1.99 | -1.99 | -1.83 | +0.26 | `ts_quantile_q75(day_kurt(nt_ts_autocorr_s1(Low, 3)), 30)` |
| swap | `Low->High` | -1.72 | -0.82 | -1.72 | — | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(High, 3))), 30)` |
| window | `ts_quantile_q75@30->15` | -1.26 | -0.83 | -1.26 | — | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), 15)` |
| window | `ts_quantile_q75@30->60` | -1.75 | -0.92 | -1.75 | — | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), 60)` |

### head score -1.83:`ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3)))` | -1.95 | -1.68 | -1.95 | — | (子树本身) |
| sufficiency | `day_kurt(nt_ts_autocorr_s1(Open, 3))` | -1.51 | -1.48 | -1.51 | — | (子树本身) |
| knockout | `pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3)))` | -2.13 | -2.13 | -2.05 | +0.30 | `ts_quantile_q75(day_kurt(nt_ts_autocorr_s1(Open, 3)), 30)` |
| swap | `Open->Close` | -2.19 | -1.56 | -2.19 | — | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Close, 3))), 30)` |
| window | `ts_quantile_q75@30->15` | -1.93 | -1.66 | -1.93 | — | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))), 15)` |
| window | `ts_quantile_q75@30->60` | -2.16 | -1.70 | -2.16 | — | `ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Open, 3))), 60)` |

### head score -2.19:`cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))` | -2.75 | -1.36 | -2.75 | — | (子树本身) |
| sufficiency | `day_kurt(nt_ts_autocorr_s1(Ret, 3))` | -4.33 | -2.37 | -4.33 | — | (子树本身) |
| knockout | `pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))` | -4.86 | -3.22 | -4.86 | +2.68 | `cross_sum(day_kurt(nt_ts_autocorr_s1(Ret, 3)), 15)` |
| window | `cross_sum@15->7` | -2.21 | -1.00 | -2.21 | — | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 7)` |
| window | `cross_sum@15->30` | -1.89 | -0.98 | -1.89 | — | `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3)))` — enrichment,均值差 +1.39,p 0.067

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.48(window ts_quantile_q75@30->15):`ts_quantile_q75(pow_2(day_kurt(nt_ts_autocorr_s1(Low, 3))), 15)`
- 增益 +0.30(window cross_sum@15->30):`cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 30)`
