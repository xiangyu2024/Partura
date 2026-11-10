# 定位:种子 2027,P 组,第 1 轮(只含 train / valid)

快照:prods2027M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.34 | -1.34 | -0.83 | +1 | 5 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)` |
| -1.47 | -1.47 | -0.95 | +1 | 5 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)` |
| -1.85 | -1.73 | -1.85 | +1 | 0 | prods2027M1_I0_open_search | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)` |

## 共性:10 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(9 次评估)

### head score -1.34:`ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(in_slice(Ret, 11, 230))` | -4.56 | -4.56 | -4.32 | — | (子树本身) |
| window | `ts_stddev@15->7` | -1.98 | -1.75 | -1.98 | — | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 7)` |
| window | `ts_stddev@15->30` | -1.30 | -1.30 | -1.19 | — | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 30)` |

### head score -1.47:`ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(in_slice(Ret, 11, 230), 10)` | -3.63 | -3.54 | -3.63 | — | (子树本身) |
| window | `ts_stddev@15->7` | -2.16 | -2.16 | -1.99 | — | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 7)` |
| window | `ts_stddev@15->30` | -1.34 | -1.34 | -0.78 | — | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 30)` |

### head score -1.85:`ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_q_stat_std(in_slice(Ret, 11, 230), 5)` | -4.22 | -4.22 | -4.05 | — | (子树本身) |
| window | `ts_stddev@15->7` | -2.86 | -2.86 | -2.43 | — | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 7)` |
| window | `ts_stddev@15->30` | -1.70 | -1.70 | -1.09 | — | `ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 30)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.15(window ts_stddev@15->30):`ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 5), 30)`
- 增益 +0.12(window ts_stddev@15->30):`ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230), 10), 30)`
