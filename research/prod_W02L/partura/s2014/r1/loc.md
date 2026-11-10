# 定位:种子 2014,P 组,第 1 轮(只含 train / valid)

快照:prods2014M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.13 | -0.93 | -1.13 | +1 | 5 | prods2014M1_I0_open_search | `ts_std(day_quantile_q25(Ret), 10)` |
| -1.20 | -1.20 | +0.29 | +1 | 0 | prods2014M1_I0_open_search | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), 241), 5)` |
| -1.22 | -1.22 | -0.28 | +1 | 5 | prods2014M1_I0_open_search | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)), 20)` |

## 共性:22 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.70 | 0.161 | 8 | -2.44 / -3.14 | `day_quantile_q25(Ret)` |
| -0.72 | 0.891 | 7 | -3.38 / -2.66 | `day_quantile_q25(High)` |

## 拆解(23 次评估)

### head score -1.13:`ts_std(day_quantile_q25(Ret), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_quantile_q25(Ret)` | — | — | — | — | 门槛废品 |
| window | `ts_std@10->5` | -0.88 | -0.43 | -0.88 | — | `ts_std(day_quantile_q25(Ret), 5)` |
| window | `ts_std@10->20` | -1.19 | -1.19 | -1.17 | — | `ts_std(day_quantile_q25(Ret), 20)` |

### head score -1.20:`ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), 241), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), 241)` | -1.11 | -1.11 | +0.43 | — | (子树本身) |
| sufficiency | `cross_max(day_quantile_q25(Amt), 3)` | -3.51 | -3.07 | -3.51 | — | (子树本身) |
| sufficiency | `day_quantile_q25(Amt)` | -3.42 | -3.33 | -3.42 | — | (子树本身) |
| knockout | `cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), 241)` | -3.77 | -2.89 | -3.77 | +2.56 | `ts_sum(cross_max(day_quantile_q25(Amt), 3), 5)` |
| knockout | `cross_max(day_quantile_q25(Amt), 3)` | -1.25 | -1.25 | +0.29 | +0.04 | `ts_sum(cross_fangzheng(day_quantile_q25(Amt), 241), 5)` |
| swap | `Amt->Volume` | -2.00 | -1.90 | -2.00 | — | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Volume), 3), 241), 5)` |
| window | `ts_sum@5->2` | -1.12 | -1.12 | +0.38 | — | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), 241), 2)` |
| window | `ts_sum@5->10` | -1.37 | -1.37 | +0.11 | — | `ts_sum(cross_fangzheng(cross_max(day_quantile_q25(Amt), 3), 241), 10)` |

### head score -1.22:`ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10))` | -2.64 | -2.64 | -1.56 | — | (子树本身) |
| sufficiency | `cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)` | -3.90 | -3.90 | -3.87 | — | (子树本身) |
| sufficiency | `cs_sum(signedpower(day_quantile_q25(Low)))` | — | — | — | — | 门槛废品 |
| sufficiency | `signedpower(day_quantile_q25(Low))` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10))` | -2.02 | -2.02 | -0.80 | +0.79 | `ts_max(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10), 20)` |
| knockout | `cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)` | — | — | — | — | `ts_max(log(cs_sum(signedpower(day_quantile_q25(Low)))), 20)` |
| knockout | `cs_sum(signedpower(day_quantile_q25(Low)))` | -2.15 | -1.51 | -2.15 | +0.93 | `ts_max(log(cross_regbeta(signedpower(day_quantile_q25(Low)), day_last(Amt), 10)), 20)` |
| knockout | `signedpower(day_quantile_q25(Low))` | -1.02 | -1.02 | -0.11 | -0.20 | `ts_max(log(cross_regbeta(cs_sum(day_quantile_q25(Low)), day_last(Amt), 10)), 20)` |
| swap | `Low->High` | -1.22 | -1.22 | -0.14 | — | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(High))), day_last(Amt), 10)), 20)` |
| swap | `Amt->Volume` | -1.59 | -1.40 | -1.59 | — | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Volume), 10)), 20)` |
| window | `ts_max@20->10` | -2.05 | -2.05 | -0.56 | — | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)), 10)` |
| window | `ts_max@20->40` | -0.54 | -0.54 | +0.07 | — | `ts_max(log(cross_regbeta(cs_sum(signedpower(day_quantile_q25(Low))), day_last(Amt), 10)), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.26(window ts_std@10->5):`ts_std(day_quantile_q25(Ret), 5)`
