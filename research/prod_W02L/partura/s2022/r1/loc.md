# 定位:种子 2022,P 组,第 1 轮(只含 train / valid)

快照:prods2022M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.49 | -2.34 | -2.49 | -1 | 20 | prods2022M1_I0_open_search | `ts_pearson(mul(log(day_argmin(Low)), 0.5), 10)` |
| -2.49 | -2.34 | -2.49 | -1 | 20 | prods2022M1_I0_open_search | `ts_pearson(mul(log(day_argmin(Low)), 1), 10)` |
| -2.84 | -2.24 | -2.84 | -1 | 20 | prods2022M1_I0_open_search | `ts_quantile_q75(mul(log(day_argmin(Low)), 5), 10)` |

## 共性:6 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(21 次评估)

### head score -2.49:`ts_pearson(mul(log(day_argmin(Low)), 0.5), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(day_argmin(Low))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_argmin(Low)` | — | — | — | — | 门槛废品 |
| knockout | `mul(log(day_argmin(Low)), 0.5)` | -2.45 | -2.34 | -2.45 | -0.04 | `ts_pearson(log(day_argmin(Low)), 10)` |
| knockout | `log(day_argmin(Low))` | -2.35 | -2.26 | -2.35 | -0.14 | `ts_pearson(mul(day_argmin(Low), 0.5), 10)` |
| swap | `Low->High` | -2.66 | -2.66 | -2.59 | — | `ts_pearson(mul(log(day_argmin(High)), 0.5), 10)` |
| window | `ts_pearson@10->5` | -2.72 | -2.64 | -2.72 | — | `ts_pearson(mul(log(day_argmin(Low)), 0.5), 5)` |
| window | `ts_pearson@10->20` | -2.18 | -2.18 | -2.05 | — | `ts_pearson(mul(log(day_argmin(Low)), 0.5), 20)` |

### head score -2.49:`ts_pearson(mul(log(day_argmin(Low)), 1), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(day_argmin(Low))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_argmin(Low)` | — | — | — | — | 门槛废品 |
| knockout | `mul(log(day_argmin(Low)), 1)` | -2.45 | -2.34 | -2.45 | -0.04 | `ts_pearson(log(day_argmin(Low)), 10)` |
| knockout | `log(day_argmin(Low))` | -2.35 | -2.26 | -2.35 | -0.14 | `ts_pearson(mul(day_argmin(Low), 1), 10)` |
| swap | `Low->High` | -2.66 | -2.66 | -2.59 | — | `ts_pearson(mul(log(day_argmin(High)), 1), 10)` |
| window | `ts_pearson@10->5` | -2.72 | -2.65 | -2.72 | — | `ts_pearson(mul(log(day_argmin(Low)), 1), 5)` |
| window | `ts_pearson@10->20` | -2.18 | -2.18 | -2.05 | — | `ts_pearson(mul(log(day_argmin(Low)), 1), 20)` |

### head score -2.84:`ts_quantile_q75(mul(log(day_argmin(Low)), 5), 10)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `log(day_argmin(Low))` | — | — | — | — | 门槛废品 |
| sufficiency | `day_argmin(Low)` | — | — | — | — | 门槛废品 |
| knockout | `mul(log(day_argmin(Low)), 5)` | -2.79 | -2.24 | -2.79 | -0.05 | `ts_quantile_q75(log(day_argmin(Low)), 10)` |
| knockout | `log(day_argmin(Low))` | — | — | — | — | `ts_quantile_q75(mul(day_argmin(Low), 5), 10)` |
| swap | `Low->High` | -3.28 | -3.28 | -1.51 | — | `ts_quantile_q75(mul(log(day_argmin(High)), 5), 10)` |
| window | `ts_quantile_q75@10->5` | — | — | — | — | `ts_quantile_q75(mul(log(day_argmin(Low)), 5), 5)` |
| window | `ts_quantile_q75@10->20` | -2.63 | -2.20 | -2.63 | — | `ts_quantile_q75(mul(log(day_argmin(Low)), 5), 20)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.31(window ts_pearson@10->20):`ts_pearson(mul(log(day_argmin(Low)), 1), 20)`
- 增益 +0.30(window ts_pearson@10->20):`ts_pearson(mul(log(day_argmin(Low)), 0.5), 20)`
- 增益 +0.21(window ts_quantile_q75@10->20):`ts_quantile_q75(mul(log(day_argmin(Low)), 5), 20)`
- 增益 +0.14(knockout log(day_argmin(Low))):`ts_pearson(mul(day_argmin(Low), 0.5), 10)`
- 增益 +0.14(knockout log(day_argmin(Low))):`ts_pearson(mul(day_argmin(Low), 1), 10)`
