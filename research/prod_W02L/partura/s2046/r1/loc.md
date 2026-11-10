# 定位:种子 2046,P 组,第 1 轮(只含 train / valid)

快照:prods2046M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.60 | -0.60 | -0.58 | +1 | 5 | prods2046M1_I0_open_search | `ts_sum(day_var(Amt), 50)` |
| -0.95 | -0.95 | -0.90 | +1 | 5 | prods2046M1_I0_open_search | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 241), 20)` |
| -1.12 | -0.53 | -1.12 | +1 | 20 | prods2046M1_I0_open_search | `ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(Low)), 20), 20), 5)` |

## 共性:31 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.44 | 0.120 | 9 | -1.98 / -2.43 | `day_var(Low)` |
| -0.42 | 0.972 | 4 | -2.67 / -2.25 | `day_var(Open)` |
| -0.52 | 0.751 | 4 | -2.75 / -2.23 | `day_var(Ret)` |

## 拆解(25 次评估)

### head score -0.60:`ts_sum(day_var(Amt), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_var(Amt)` | -3.75 | -2.98 | -3.75 | — | (子树本身) |
| swap | `Amt->Volume` | -1.13 | -1.02 | -1.13 | — | `ts_sum(day_var(Volume), 50)` |
| window | `ts_sum@50->25` | -3.10 | -3.10 | -2.39 | — | `ts_sum(day_var(Amt), 25)` |
| window | `ts_sum@50->100` | -0.28 | -0.28 | +0.24 | — | `ts_sum(day_var(Amt), 100)` |

### head score -0.95:`ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 241), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 241)` | -0.94 | -0.94 | -0.91 | — | (子树本身) |
| sufficiency | `ts_max(day_last(Amt), 20)` | -1.89 | -1.89 | -0.54 | — | (子树本身) |
| sufficiency | `day_last(Amt)` | -3.83 | -3.16 | -3.83 | — | (子树本身) |
| sufficiency | `day_var(Low)` | -2.27 | -1.53 | -2.27 | — | (子树本身) |
| knockout | `cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 241)` | -0.78 | -0.78 | -0.42 | -0.17 | `ts_max(ts_max(day_last(Amt), 20), 20)` |
| knockout | `ts_max(day_last(Amt), 20)` | -1.42 | -1.42 | -0.98 | +0.47 | `ts_max(cross_cov(day_last(Amt), day_var(Low), 241), 20)` |
| swap | `Amt->Volume` | -0.93 | -0.93 | -0.85 | — | `ts_max(cross_cov(ts_max(day_last(Volume), 20), day_var(Low), 241), 20)` |
| swap | `Low->High` | -0.95 | -0.95 | -0.90 | — | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(High), 241), 20)` |
| window | `ts_max@20->10` | -0.92 | -0.88 | -0.92 | — | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 241), 10)` |
| window | `ts_max@20->40` | -1.07 | -1.07 | -0.82 | — | `ts_max(cross_cov(ts_max(day_last(Amt), 20), day_var(Low), 241), 40)` |

### head score -1.12:`ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(Low)), 20), 20), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(Low)), 20), 20)` | -1.15 | -0.47 | -1.15 | — | (子树本身) |
| sufficiency | `ts_std(pow_2_5(day_var(Low)), 20)` | -2.43 | -1.59 | -2.43 | — | (子树本身) |
| sufficiency | `pow_2_5(day_var(Low))` | -2.27 | -1.53 | -2.27 | — | (子树本身) |
| sufficiency | `day_std(High)` | -2.27 | -1.55 | -2.27 | — | (子树本身) |
| knockout | `ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(Low)), 20), 20)` | -2.19 | -1.47 | -2.19 | +1.07 | `ts_min(day_std(High), 5)` |
| knockout | `ts_std(pow_2_5(day_var(Low)), 20)` | -1.83 | -1.60 | -1.83 | +0.71 | `ts_min(ts_reg_fvalue(day_std(High), pow_2_5(day_var(Low)), 20), 5)` |
| knockout | `pow_2_5(day_var(Low))` | -0.89 | -0.68 | -0.89 | -0.23 | `ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 5)` |
| swap | `High->Low` | -1.18 | -0.71 | -1.18 | — | `ts_min(ts_reg_fvalue(day_std(Low), ts_std(pow_2_5(day_var(Low)), 20), 20), 5)` |
| swap | `Low->High` | -1.18 | -0.82 | -1.18 | — | `ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(High)), 20), 20), 5)` |
| window | `ts_min@5->2` | -0.99 | -0.39 | -0.99 | — | `ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(Low)), 20), 20), 2)` |
| window | `ts_min@5->10` | -1.09 | -0.82 | -1.09 | — | `ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(Low)), 20), 20), 10)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.23(knockout pow_2_5(day_var(Low))):`ts_min(ts_reg_fvalue(day_std(High), ts_std(day_var(Low), 20), 20), 5)`
- 增益 +0.13(window ts_min@5->2):`ts_min(ts_reg_fvalue(day_std(High), ts_std(pow_2_5(day_var(Low)), 20), 20), 2)`
