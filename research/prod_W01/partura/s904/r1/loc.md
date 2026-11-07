# 定位:种子 904,P 组,第 1 轮(只含 train / valid)

快照:prods904M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(0 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|

## 共性:124 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.00 | 0.010 | 4 | -0.57 / -1.58 | `day_topw_mean(Amt, Amt)` |
| +0.85 | 0.011 | 10 | -0.77 / -1.61 | `abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30))` |
| +0.81 | 0.018 | 6 | -0.78 / -1.59 | `abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40))` |
| +0.80 | 0.027 | 5 | -0.78 / -1.58 | `pow_05(abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)))` |
| +0.76 | 0.051 | 6 | -0.82 / -1.58 | `pow_05(abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)))` |
| +0.69 | 0.000 | 43 | -1.10 / -1.79 | `ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)` |
| +0.65 | 0.002 | 56 | -1.19 / -1.84 | `day_topw_mean(Ret, Amt)` |
| +0.65 | 0.002 | 17 | -0.99 / -1.64 | `ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)` |
| +0.47 | 0.068 | 7 | -1.10 / -1.57 | `pow_05(cross_ema(day_sum(Ret), 241))` |
| +0.43 | 0.097 | 8 | -1.14 / -1.57 | `cross_ema(day_sum(Ret), 241)` |
| +0.28 | 0.092 | 17 | -1.31 / -1.58 | `day_sum(Ret)` |
| +0.24 | 0.424 | 4 | -1.31 / -1.55 | `day_quantile_q25(Vwap)` |
| +0.16 | 0.615 | 5 | -1.39 / -1.55 | `pow_3(day_quantile_q25(Amt))` |
| +0.16 | 0.615 | 5 | -1.39 / -1.55 | `day_quantile_q25(Amt)` |
| -0.02 | 0.707 | 11 | -1.56 / -1.54 | `day_q_stat_std(Low)` |
| -0.03 | 0.841 | 4 | -1.58 / -1.55 | `cross_reg_tvalue(day_skew(Vwap), day_first(Volume), 10)` |
| -0.03 | 0.841 | 4 | -1.58 / -1.55 | `day_skew(Vwap)` |
| -0.03 | 0.841 | 4 | -1.58 / -1.55 | `day_first(Volume)` |
| -0.10 | 0.795 | 7 | -1.64 / -1.54 | `day_min(Low)` |

## 拆解(0 次评估)

## 机械核心卡(B0 按这个顺序取)

1. `day_topw_mean(Amt, Amt)` — enrichment,均值差 +1.00,p 0.010
2. `abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30))` — enrichment,均值差 +0.85,p 0.011
3. `abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40))` — enrichment,均值差 +0.81,p 0.018
4. `pow_05(abs_(ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)))` — enrichment,均值差 +0.80,p 0.027
5. `pow_05(abs_(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)))` — enrichment,均值差 +0.76,p 0.051
6. `ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30)` — enrichment,均值差 +0.69,p 0.000
7. `day_topw_mean(Ret, Amt)` — enrichment,均值差 +0.65,p 0.002
8. `ts_sum(ts_reg_tvalue(day_topw_mean(Ret, Amt), ListAge, 30), 40)` — enrichment,均值差 +0.65,p 0.002
9. `pow_05(cross_ema(day_sum(Ret), 241))` — enrichment,均值差 +0.47,p 0.068
10. `cross_ema(day_sum(Ret), 241)` — enrichment,均值差 +0.43,p 0.097
11. `day_sum(Ret)` — enrichment,均值差 +0.28,p 0.092

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

(没有)
