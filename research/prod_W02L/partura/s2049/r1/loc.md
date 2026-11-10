# 定位:种子 2049,P 组,第 1 轮(只含 train / valid)

快照:prods2049M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -2.34 | -2.34 | -2.33 | +1 | 20 | prods2049M1_I0_open_search | `ts_min(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 5)` |
| -2.54 | -2.54 | -2.12 | -1 | 20 | prods2049M1_I0_open_search | `ts_min(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 5)` |
| -3.06 | -3.06 | -2.11 | +1 | 5 | prods2049M1_I0_open_search | `ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20), 5)` |

## 共性:9 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| -0.74 | 0.905 | 4 | -3.74 / -3.00 | `ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20)` |

## 拆解(24 次评估)

### head score -2.34:`ts_min(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20)` | -1.94 | -1.94 | -1.50 | — | (子树本身) |
| sufficiency | `day_std(Volume)` | -1.21 | -1.10 | -1.21 | — | (子树本身) |
| sufficiency | `day_cov(Volume, Low)` | -4.21 | -4.21 | -3.77 | — | (子树本身) |
| knockout | `ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20)` | -1.53 | -1.18 | -1.53 | -0.81 | `ts_min(day_std(Volume), 5)` |
| swap | `Volume->Amt` | -2.35 | -2.35 | -2.08 | — | `ts_min(ts_reg_fvalue(day_std(Amt), day_cov(Amt, Low), 20), 5)` |
| swap | `Low->High` | -2.13 | -2.13 | -2.12 | — | `ts_min(ts_reg_fvalue(day_std(Volume), day_cov(Volume, High), 20), 5)` |
| window | `ts_min@5->2` | -2.30 | -2.30 | -2.10 | — | `ts_min(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 2)` |
| window | `ts_min@5->10` | -2.45 | -2.45 | -1.80 | — | `ts_min(ts_reg_fvalue(day_std(Volume), day_cov(Volume, Low), 20), 10)` |

### head score -2.54:`ts_min(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40)` | -2.07 | -2.07 | -1.16 | — | (子树本身) |
| sufficiency | `day_std(High)` | -2.27 | -1.55 | -2.27 | — | (子树本身) |
| sufficiency | `day_cov(Volume, Low)` | -4.21 | -4.21 | -3.77 | — | (子树本身) |
| knockout | `ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40)` | -2.19 | -1.47 | -2.19 | -0.35 | `ts_min(day_std(High), 5)` |
| swap | `High->Low` | -2.52 | -2.52 | -2.20 | — | `ts_min(ts_reg_fvalue(day_std(Low), day_cov(Volume, Low), 40), 5)` |
| swap | `Volume->Amt` | -2.68 | -2.68 | -1.72 | — | `ts_min(ts_reg_fvalue(day_std(High), day_cov(Amt, Low), 40), 5)` |
| window | `ts_min@5->2` | -2.33 | -2.33 | -1.26 | — | `ts_min(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 2)` |
| window | `ts_min@5->10` | -2.16 | -2.16 | -1.86 | — | `ts_min(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 10)` |

### head score -3.06:`ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20)` | -3.49 | -3.49 | -2.21 | — | (子树本身) |
| sufficiency | `day_std(High)` | -2.27 | -1.55 | -2.27 | — | (子树本身) |
| sufficiency | `day_cov(Volume, Low)` | -4.21 | -4.21 | -3.77 | — | (子树本身) |
| knockout | `ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20)` | -2.31 | -1.55 | -2.31 | -0.75 | `ts_decay_linear(day_std(High), 5)` |
| swap | `High->Low` | -2.86 | -2.86 | -1.35 | — | `ts_decay_linear(ts_reg_fvalue(day_std(Low), day_cov(Volume, Low), 20), 5)` |
| swap | `Volume->Amt` | -2.68 | -2.68 | -2.35 | — | `ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Amt, Low), 20), 5)` |
| window | `ts_decay_linear@5->2` | -3.37 | -3.37 | -2.12 | — | `ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20), 2)` |
| window | `ts_decay_linear@5->10` | -2.87 | -2.87 | -1.72 | — | `ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20), 10)` |

## 机械核心卡(B0 按这个顺序取)


## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.38(swap Volume->Amt):`ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Amt, Low), 20), 5)`
- 增益 +0.38(window ts_min@5->10):`ts_min(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 40), 10)`
- 增益 +0.20(swap Low->High):`ts_min(ts_reg_fvalue(day_std(Volume), day_cov(Volume, High), 20), 5)`
- 增益 +0.19(swap High->Low):`ts_decay_linear(ts_reg_fvalue(day_std(Low), day_cov(Volume, Low), 20), 5)`
- 增益 +0.18(window ts_decay_linear@5->10):`ts_decay_linear(ts_reg_fvalue(day_std(High), day_cov(Volume, Low), 20), 10)`
