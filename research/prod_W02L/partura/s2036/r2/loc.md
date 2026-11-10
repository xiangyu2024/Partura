# 定位:种子 2036,P 组,第 2 轮(只含 train / valid)

快照:prods2036M1_I0_open_search, prods2036M2_I0_open_search, prods2036Pr1a_Ea, prods2036Pr1b_Nb;已生效的 R 替换 2 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -0.70 | -0.49 | -0.70 | +1 | 0 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 120)` |
| -1.11 | -1.11 | -0.67 | +1 | 5 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.95, False), 20)` |
| -1.55 | -1.55 | -1.06 | +1 | 5 | prods2036M1_I0_open_search | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, True), 20)` |

## 共性:90 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.64 | 0.002 | 6 | -0.54 / -2.18 | `day_std(delete_open_close(Volume))` |
| +0.92 | 0.022 | 10 | -1.26 / -2.18 | `cs_first_low20(BoardCode, day_quantile_q75(Vwap))` |
| +0.91 | 0.018 | 12 | -1.29 / -2.19 | `day_quantile_q75(Vwap)` |
| +0.84 | 0.039 | 7 | -1.30 / -2.14 | `day_std(Volume)` |
| +0.58 | 0.226 | 6 | -1.53 / -2.11 | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 120)` |
| +0.49 | 0.316 | 5 | -1.61 / -2.10 | `day_std(Ret)` |
| +0.32 | 0.439 | 5 | -1.77 / -2.09 | `day_sum(Ret)` |
| +0.21 | 0.050 | 43 | -1.96 / -2.17 | `energy_ratio_n(delete_open_close(Volume), 0.9, False)` |
| -1.08 | 0.980 | 5 | -3.09 / -2.01 | `cs_rank(energy_ratio_n(in_slice(Volume, 181, 237), 0.9, False))` |
| -1.35 | 0.995 | 6 | -3.33 / -1.98 | `energy_ratio_n(in_slice(Volume, 181, 237), 0.9, False)` |
| -1.46 | 0.994 | 4 | -3.47 / -2.01 | `sub(cs_rank(energy_ratio_n(in_slice(Volume, 181, 237), 0.9, False)), cs_rank(energy_ratio_n(in_slice(Volume, 2, 61), 0.9, False)))` |
| -1.46 | 0.994 | 4 | -3.47 / -2.01 | `cs_rank(energy_ratio_n(in_slice(Volume, 2, 61), 0.9, False))` |
| -1.71 | 0.999 | 5 | -3.69 / -1.98 | `energy_ratio_n(in_slice(Volume, 2, 61), 0.9, False)` |

## 拆解(8 次评估)

### head score -0.70:`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 120)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_n(delete_open_close(Volume), 0.9, False)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -0.69 | -0.53 | -0.69 | — | `cross_stddev(energy_ratio_n(delete_open_close(Amt), 0.9, False), 120)` |
| window | `cross_stddev@120->60` | -1.03 | -0.74 | -1.03 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 60)` |
| window | `cross_stddev@120->240` | -0.53 | -0.53 | -0.22 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 240)` |

### head score -1.11:`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.95, False), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `energy_ratio_n(delete_open_close(Volume), 0.95, False)` | — | — | — | — | 门槛废品 |
| swap | `Volume->Amt` | -1.07 | -1.07 | -0.72 | — | `cross_stddev(energy_ratio_n(delete_open_close(Amt), 0.95, False), 20)` |
| window | `cross_stddev@20->10` | -1.49 | -1.49 | -1.13 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.95, False), 10)` |
| window | `cross_stddev@20->40` | -0.75 | -0.75 | -0.66 | — | `cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.95, False), 40)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_std(delete_open_close(Volume))` — enrichment,均值差 +1.64,p 0.002
2. `cs_first_low20(BoardCode, day_quantile_q75(Vwap))` — enrichment,均值差 +0.92,p 0.022
3. `day_quantile_q75(Vwap)` — enrichment,均值差 +0.91,p 0.018
4. `day_std(Volume)` — enrichment,均值差 +0.84,p 0.039
5. `energy_ratio_n(delete_open_close(Volume), 0.9, False)` — enrichment,均值差 +0.21,p 0.050

## 本组之前各轮的任务

- `prods2036Pr1a_Ea`:核心 `energy_ratio_n(delete_open_close(Volume), 0.9, False)`;评分 85,过线 0,入 heads 0;采样计数 {'c05_no_core': 1371, 'c05_skeleton': 747}
  - score +0.04(train +0.43 valid +0.04):`cross_regbeta(day_std(Volume), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120)`
  - score +0.01(train +0.01 valid +0.34):`cross_regbeta(day_std(Volume), cross_regbeta(day_std(delete_open_close(Volume)), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120), 120)`
  - score -0.01(train -0.01 valid +0.43):`cross_regbeta(day_std(delete_open_close(Volume)), cross_regbeta(day_std(delete_open_close(Volume)), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120), 120)`
  - score -0.01(train -0.01 valid +0.59):`cross_regbeta(day_std(Volume), cross_regbeta(day_std(Volume), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120), 120)`
  - score -0.13(train +0.48 valid -0.13):`cross_regbeta(day_std(delete_open_close(Volume)), energy_ratio_n(delete_open_close(Volume), 0.9, False), 120)`
- `prods2036Pr1b_Nb`:核心 `—`;评分 75,过线 0,入 heads 0;采样计数 {'c05_skeleton': 6}
  - score +0.37(train +0.37 valid +0.48):`cs_first_low20(cs_first_low20(day_sum(Vwap), day_sum(Vwap)), cs_first_low20(day_sum(Vwap), day_sum(Vwap)))`
  - score +0.35(train +0.35 valid +0.45):`cs_first_low40(day_sum(Vwap), day_sum(Vwap))`
  - score +0.06(train +0.06 valid +0.80):`cs_first_low20(day_sum(Vwap), day_sum(Vwap))`
  - score +0.01(train +0.01 valid +0.26):`cs_first_low20(cs_first_low20(day_std(Vwap), day_std(Vwap)), cs_first_low20(day_std(Vwap), day_std(Vwap)))`
  - score -0.01(train -0.01 valid +0.19):`cs_first_low20(day_var(Close), day_var(Close))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.17(window cross_stddev@120->240):`cross_stddev(energy_ratio_n(delete_open_close(Volume), 0.9, False), 240)`
