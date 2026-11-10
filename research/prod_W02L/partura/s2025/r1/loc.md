# 定位:种子 2025,P 组,第 1 轮(只含 train / valid)

快照:prods2025M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.26 | -1.76 | -2.26 | -1 | 20 | prods2025M1_I0_open_search | `sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))` |
| -2.42 | -2.42 | -1.87 | +1 | 5 | prods2025M1_I0_open_search | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 20)` |
| -2.47 | -2.00 | -2.47 | +1 | 5 | prods2025M1_I0_open_search | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` |

## 共性:13 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.22 | 0.262 | 5 | -3.15 / -3.37 | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` |

## 拆解(8 次评估)

### head score -2.26:`sub(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` | -4.06 | -4.06 | -3.84 | — | (子树本身) |
| sufficiency | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))` | -2.49 | -1.96 | -2.49 | — | (子树本身) |
| swap | `Volume->Amt` | -2.19 | -1.72 | -2.19 | — | `sub(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10)), day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10, False)))` |

### head score -2.42:`ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10))` | -4.06 | -4.06 | -3.84 | — | (子树本身) |
| swap | `Volume->Amt` | -2.50 | -2.50 | -1.83 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10)), 20)` |
| window | `ts_stddev@20->10` | -3.21 | -3.21 | -2.48 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 10)` |
| window | `ts_stddev@20->40` | -1.37 | -1.37 | -1.34 | — | `ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 40)` |

### head score -2.47:`day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10, False))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -2.47 | -1.94 | -2.47 | — | `day_std(in_topk_masked(in_slice(Amt, 11, 240), in_slice(Ret, 11, 240), 10, False))` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +1.05(window ts_stddev@20->40):`ts_stddev(day_std(in_topk_masked(in_slice(Volume, 11, 240), in_slice(Ret, 11, 240), 10)), 40)`
