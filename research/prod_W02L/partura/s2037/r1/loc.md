# 定位:种子 2037,P 组,第 1 轮(只含 train / valid)

快照:prods2037M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.86 | -0.86 | -0.81 | +1 | 5 | prods2037M1_I0_open_search | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 20, 5, False), 20)` |
| -0.98 | -0.98 | -0.97 | +1 | 5 | prods2037M1_I0_open_search | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 20)` |
| -1.69 | -1.69 | -0.91 | +1 | 20 | prods2037M1_I0_open_search | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 10, False), 20)` |

## 共性:18 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|

## 拆解(12 次评估)

### head score -0.86:`cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 20, 5, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_topm_minus_q(delete_open_close(Volume), 20, 5, False)` | -4.80 | -4.80 | -4.70 | — | (子树本身) |
| swap | `Volume->Amt` | -0.90 | -0.80 | -0.90 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Amt), 20, 5, False), 20)` |
| window | `cross_stddev@20->10` | -2.11 | -1.19 | -2.11 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 20, 5, False), 10)` |
| window | `cross_stddev@20->40` | -1.44 | -0.61 | -1.44 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 20, 5, False), 40)` |

### head score -0.98:`cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False)` | -4.09 | -4.06 | -4.09 | — | (子树本身) |
| swap | `Volume->Amt` | -0.92 | -0.92 | -0.90 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Amt), 50, 5, False), 20)` |
| window | `cross_stddev@20->10` | -1.10 | -1.10 | -0.94 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 10)` |
| window | `cross_stddev@20->40` | -0.58 | -0.37 | -0.58 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 40)` |

### head score -1.69:`cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 10, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 10, False)` | -4.00 | -4.00 | -3.77 | — | (子树本身) |
| swap | `Volume->Amt` | -1.61 | -1.61 | -1.16 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Amt), 50, 10, False), 20)` |
| window | `cross_stddev@20->10` | -1.53 | -1.53 | -0.97 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 10, False), 10)` |
| window | `cross_stddev@20->40` | -1.08 | -1.03 | -1.08 | — | `cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 10, False), 40)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.61(window cross_stddev@20->40):`cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 10, False), 40)`
- 增益 +0.41(window cross_stddev@20->40):`cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 5, False), 40)`
- 增益 +0.16(window cross_stddev@20->10):`cross_stddev(energy_ratio_topm_minus_q(delete_open_close(Volume), 50, 10, False), 10)`
