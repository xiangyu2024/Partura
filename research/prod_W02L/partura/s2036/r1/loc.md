# 定位:种子 2036,P 组,第 1 轮(只含 train / valid)

快照:prods2036M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.55 | -1.55 | -1.06 | +1 | 5 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, True), 20)` |
| -1.56 | -1.56 | -1.05 | +1 | 20 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 20)` |
| -3.17 | -3.17 | -2.96 | +1 | 20 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.8, False), 20)` |

## 共性:8 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(12 次评估)

### head score -1.55:`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, True), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_n(delete_open_close(Volume), 0.9, True)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.46 | -1.46 | -1.04 | — | `cross_stddev(energy_ratio_n(delete_open_close(Amt), 0.9, True), 20)` |
| window | `cross_stddev@20->10` | -1.74 | -1.74 | -1.14 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, True), 10)` |
| window | `cross_stddev@20->40` | -1.00 | -1.00 | -0.97 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, True), 40)` |

### head score -1.56:`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_n(delete_open_close(Volume), 0.9, False)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.62 | -1.62 | -0.92 | — | `cross_stddev(energy_ratio_n(delete_open_close(Amt), 0.9, False), 20)` |
| window | `cross_stddev@20->10` | -1.54 | -1.54 | -1.10 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 10)` |
| window | `cross_stddev@20->40` | -0.77 | -0.77 | -0.54 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 40)` |

### head score -3.17:`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.8, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_n(delete_open_close(Volume), 0.8, False)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -3.11 | -3.11 | -2.91 | — | `cross_stddev(energy_ratio_n(delete_open_close(Amt), 0.8, False), 20)` |
| window | `cross_stddev@20->10` | -3.10 | -3.10 | -3.07 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.8, False), 10)` |
| window | `cross_stddev@20->40` | -3.03 | -2.78 | -3.03 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.8, False), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.79(window cross_stddev@20->40):`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 40)`
- 增益 +0.55(window cross_stddev@20->40):`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, True), 40)`
- 增益 +0.14(window cross_stddev@20->40):`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.8, False), 40)`
