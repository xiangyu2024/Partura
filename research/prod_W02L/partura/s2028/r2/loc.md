# 定位:种子 2028,P 组,第 2 轮(只含 train / valid)

快照:prods2028M1_I0_open_search, prods2028M2_I0_open_search, prods2028Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.73 | +0.73 | +0.82 | -1 | 20 | prods2028Pr1b_Nb | `div(cs_first_low40(LogTotalCap, day_close(Low)), day_kurt(Volume))` |
| -0.67 | -0.67 | -0.34 | +1 | 5 | prods2028M2_I0_open_search | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 30))` |
| -1.91 | -1.91 | -1.55 | -1 | 20 | prods2028M2_I0_open_search | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)), 30))` |

## 共性:49 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +0.93 | 0.090 | 24 | -1.20 / -2.13 | `pow_2_5(LogTotalCap)` |
| +0.93 | 0.014 | 22 | -1.16 / -2.09 | `day_close(Low)` |
| +0.80 | 0.022 | 15 | -1.12 / -1.92 | `cs_last_high05(LogTotalCap, day_close(Low))` |
| +0.75 | 0.101 | 8 | -1.05 / -1.80 | `cs_last_high05(LogTotalCap, LogTotalCap)` |
| +0.46 | 0.276 | 5 | -1.26 / -1.72 | `cs_first_low40(cs_last_high05(LogTotalCap, day_close(Low)), pow_2_5(LogTotalCap))` |

## 拆解(27 次评估)

### head score +0.73:`div(cs_first_low40(LogTotalCap, day_close(Low)), day_kurt(Volume))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low40(LogTotalCap, day_close(Low))` | +0.02 | +0.02 | +0.56 | — | (子树本身) |
| sufficiency | `day_close(Low)` | -2.35 | -1.59 | -2.35 | — | (子树本身) |
| sufficiency | `day_kurt(Volume)` | -4.93 | -4.22 | -4.93 | — | (子树本身) |
| knockout | `cs_first_low40(LogTotalCap, day_close(Low))` | -4.89 | -4.01 | -4.89 | +5.62 | `div(LogTotalCap, day_kurt(Volume))` |
| swap | `Low->High` | +0.75 | +0.75 | +0.82 | — | `div(cs_first_low40(LogTotalCap, day_close(High)), day_kurt(Volume))` |
| swap | `Volume->Amt` | +0.74 | +0.74 | +0.84 | — | `div(cs_first_low40(LogTotalCap, day_close(Low)), day_kurt(Amt))` |

### head score -0.67:`pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 30)` | -0.66 | -0.66 | -0.38 | — | (子树本身) |
| sufficiency | `ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10)` | — | — | — | — | 门槛废品 |
| sufficiency | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10))` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)` | -2.10 | -2.10 | -2.06 | — | (子树本身) |
| knockout | `ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 30)` | — | — | — | — | `pow_1_5(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10))` |
| knockout | `ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10)` | — | — | — | — | `pow_1_5(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 30))` |
| knockout | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10))` | — | — | — | — | `pow_1_5(ts_max(ts_max(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10), 10), 30))` |
| knockout | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)` | — | — | — | — | `pow_1_5(ts_max(ts_max(pow_2(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2))), 10), 30))` |
| window | `ts_max@30->15` | — | — | — | — | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 15))` |
| window | `ts_max@30->60` | -0.19 | -0.19 | +0.09 | — | `pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 60))` |

### head score -1.91:`pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)), 30)` | -2.61 | -1.69 | -2.61 | — | (子树本身) |
| sufficiency | `cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5))` | -2.51 | -1.65 | -2.51 | — | (子树本身) |
| sufficiency | `ts_max(cs_demean(sub(day_mean(Close), 5)), 30)` | -2.51 | -1.65 | -2.51 | — | (子树本身) |
| sufficiency | `cs_demean(sub(day_mean(Close), 5))` | -2.38 | -1.61 | -2.38 | — | (子树本身) |
| knockout | `ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)), 30)` | -1.88 | -1.88 | -1.52 | -0.02 | `pow_2(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)))` |
| knockout | `sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)` | -1.91 | -1.91 | -1.56 | +0.00 | `pow_2(ts_max(cs_demean(ts_max(cs_demean(sub(day_mean(Close), 5)), 30)), 30))` |
| knockout | `ts_max(cs_demean(sub(day_mean(Close), 5)), 30)` | -1.84 | -1.84 | -1.54 | -0.06 | `pow_2(ts_max(cs_demean(sub(cs_demean(sub(day_mean(Close), 5)), 5)), 30))` |
| knockout | `sub(day_mean(Close), 5)` | -1.91 | -1.91 | -1.56 | +0.00 | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(day_mean(Close)), 30), 5)), 30))` |
| swap | `Close->Vwap` | -1.89 | -1.89 | -1.56 | — | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Vwap), 5)), 30), 5)), 30))` |
| window | `ts_max@30->15` | -1.88 | -1.88 | -1.58 | — | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)), 15))` |
| window | `ts_max@30->60` | -1.91 | -1.91 | -1.61 | — | `pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Close), 5)), 30), 5)), 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_2_5(LogTotalCap)` — enrichment,均值差 +0.93,p 0.090
2. `day_close(Low)` — enrichment,均值差 +0.93,p 0.014
3. `cs_last_high05(LogTotalCap, day_close(Low))` — enrichment,均值差 +0.80,p 0.022

## 本组之前各轮的任务

- `prods2028Pr1b_Nb`:核心 `—`;评分 71,过线 2,入 heads 1;采样计数 {'c05_skeleton': 2}
  - score +0.73(train +0.73 valid +0.82):`div(cs_first_low40(LogTotalCap, day_close(Low)), day_kurt(Volume))`
  - score +0.58(train +0.58 valid +0.77):`div(cs_first_low40(cs_last_high05(LogTotalCap, cs_first_low40(cs_last_high05(LogTotalCap, day_close(Low)), day_close(Low))), day_close(Low)), day_kurt(Volume))`
  - score -0.44(train -0.44 valid +0.15):`div(cs_first_low40(cs_last_high05(LogTotalCap, LogTotalCap), cs_mask_top_replace_mean_neg(LogTotalCap)), -5)`
  - score -0.59(train -0.59 valid +0.16):`div(cs_first_low40(cs_last_high05(cs_last_high05(pow_2_5(LogTotalCap), day_close(Low)), cs_last_high05(pow_2_5(LogTotalCap), day_close(Low))), cs_last_high05(cs_last_high05(pow_2_5(LogTotalCap), day_close(Low)), cs_last_high05(pow_2_5(LogTotalCap), day_close(Low)))), -5)`
  - score -0.59(train -0.59 valid +0.16):`div(cs_first_low40(cs_last_high05(cs_last_high05(LogTotalCap, day_close(Low)), cs_last_high05(LogTotalCap, day_close(Low))), cs_last_high05(cs_last_high05(LogTotalCap, day_close(Low)), cs_last_high05(LogTotalCap, day_close(Low)))), -5)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.48(window ts_max@30->60):`pow_1_5(ts_max(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(cs_demean(sub(day_mean(Ret), 2)), 10), 2)), 10)), 10), 60))`
