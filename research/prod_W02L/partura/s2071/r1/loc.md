# 定位:种子 2071,P 组,第 1 轮(只含 train / valid)

快照:prods2071M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.64 | -1.62 | -1.64 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret)), 20)` |
| -1.72 | -1.71 | -1.72 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 20)` |
| -1.77 | -1.77 | -1.66 | -1 | 0 | prods2071M1_I0_open_search | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret))), 20)` |

## 共性:23 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.23 | 0.306 | 4 | -2.73 / -2.95 | `day_std(Ret)` |
| +0.17 | 0.362 | 4 | -2.77 / -2.94 | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret)))` |
| +0.16 | 0.319 | 5 | -2.79 / -2.95 | `day_sum(abs_(Ret))` |

## 拆解(33 次评估)

### head score -1.64:`ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret)), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret))` | -2.87 | -2.87 | -2.53 | — | (子树本身) |
| sufficiency | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.91 | -1.70 | -1.91 | — | (子树本身) |
| sufficiency | `sub(day_max(High), day_min(Low))` | -2.18 | -1.53 | -2.18 | — | (子树本身) |
| sufficiency | `day_max(High)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| knockout | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret))` | -1.34 | -1.21 | -1.34 | -0.29 | `ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)` |
| knockout | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.70 | -1.20 | -1.70 | +0.06 | `ts_mean(mul(sub(day_max(High), day_min(Low)), day_std(Ret)), 20)` |
| knockout | `sub(day_max(High), day_min(Low))` | -3.78 | -3.49 | -3.78 | +2.14 | `ts_mean(mul(div(day_max(High), day_open(Open)), day_std(Ret)), 20)` |
| swap | `High->Low` | -1.68 | -1.61 | -1.68 | — | `ts_mean(mul(div(sub(day_max(Low), day_min(Low)), day_open(Open)), day_std(Ret)), 20)` |
| swap | `Low->High` | -1.67 | -1.58 | -1.67 | — | `ts_mean(mul(div(sub(day_max(High), day_min(High)), day_open(Open)), day_std(Ret)), 20)` |
| window | `ts_mean@20->10` | -2.14 | -2.14 | -2.03 | — | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret)), 10)` |
| window | `ts_mean@20->40` | -2.13 | -2.13 | -1.40 | — | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret)), 40)` |

### head score -1.72:`ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1)))` | -3.69 | -3.55 | -3.69 | — | (子树本身) |
| sufficiency | `day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))` | -4.22 | -2.32 | -4.22 | — | (子树本身) |
| sufficiency | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.91 | -1.70 | -1.91 | — | (子树本身) |
| sufficiency | `sub(day_max(High), day_min(Low))` | -2.18 | -1.53 | -2.18 | — | (子树本身) |
| knockout | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1)))` | -1.34 | -1.21 | -1.34 | -0.38 | `ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)` |
| knockout | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.42 | -1.07 | -1.42 | -0.30 | `ts_mean(mul(sub(day_max(High), day_min(Low)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 20)` |
| knockout | `sub(day_max(High), day_min(Low))` | -2.81 | -1.46 | -2.81 | +1.09 | `ts_mean(mul(div(day_max(High), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 20)` |
| swap | `High->Low` | -1.74 | -1.74 | -1.62 | — | `ts_mean(mul(div(sub(day_max(Low), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 20)` |
| swap | `Low->High` | -1.68 | -1.64 | -1.68 | — | `ts_mean(mul(div(sub(day_max(High), day_min(High)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 20)` |
| window | `ts_mean@20->10` | -2.43 | -2.31 | -2.43 | — | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 10)` |
| window | `ts_mean@20->40` | -2.25 | -2.25 | -1.66 | — | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1))), 40)` |

### head score -1.77:`ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret)))` | -2.86 | -2.86 | -2.41 | — | (子树本身) |
| sufficiency | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.91 | -1.70 | -1.91 | — | (子树本身) |
| sufficiency | `sub(day_max(High), day_min(Low))` | -2.18 | -1.53 | -2.18 | — | (子树本身) |
| sufficiency | `day_sum(abs_(Ret))` | -4.44 | -4.25 | -4.44 | — | (子树本身) |
| knockout | `mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret)))` | -1.34 | -1.21 | -1.34 | -0.43 | `ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)` |
| knockout | `div(sub(day_max(High), day_min(Low)), day_open(Open))` | -1.67 | -1.11 | -1.67 | -0.10 | `ts_mean(mul(sub(day_max(High), day_min(Low)), day_sum(abs_(Ret))), 20)` |
| knockout | `sub(day_max(High), day_min(Low))` | -3.82 | -3.63 | -3.82 | +2.05 | `ts_mean(mul(div(day_max(High), day_open(Open)), day_sum(abs_(Ret))), 20)` |
| swap | `High->Low` | -1.80 | -1.80 | -1.61 | — | `ts_mean(mul(div(sub(day_max(Low), day_min(Low)), day_open(Open)), day_sum(abs_(Ret))), 20)` |
| swap | `Low->High` | -1.77 | -1.77 | -1.75 | — | `ts_mean(mul(div(sub(day_max(High), day_min(High)), day_open(Open)), day_sum(abs_(Ret))), 20)` |
| window | `ts_mean@20->10` | -2.12 | -2.12 | -1.86 | — | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret))), 10)` |
| window | `ts_mean@20->40` | -2.27 | -2.27 | -1.43 | — | `ts_mean(mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret))), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.43(knockout mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_sum(abs_(Ret)))):`ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)`
- 增益 +0.38(knockout mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_mean(in_sustain_stddev(is_gt(abs_(delete_open_close(Ret)), in_mean_full(abs_(delete_open_close(Ret)))), delete_open_close(Ret), 5, 1, 1)))):`ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)`
- 增益 +0.29(knockout mul(div(sub(day_max(High), day_min(Low)), day_open(Open)), day_std(Ret))):`ts_mean(div(sub(day_max(High), day_min(Low)), day_open(Open)), 20)`
