# 定位:种子 2056,P 组,第 2 轮(只含 train / valid)

快照:prods2056M1_I0_open_search, prods2056M2_I0_open_search, prods2056Pr1a_Ea, prods2056Pr1b_Nb;已生效的 R 替换 1 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(7 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.52 | +0.70 | +0.52 | +1 | 5 | prods2056Pr1b_Nb | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 60)` |
| -0.20 | -0.02 | -0.20 | +1 | 5 | prods2056M1_I0_open_search | `day_max(cross_corr(Amt, Ret, 180))` |
| -0.88 | -0.44 | -0.88 | +1 | 5 | prods2056M1_I0_open_search | `cross_min(day_max(cross_corr(Amt, Ret, 60)), 15)` |
| -1.66 | -1.43 | -1.66 | -1 | 5 | prods2056M1_I0_open_search | `day_max(cross_corr(Ret, Ret, 15))` |
| -1.68 | -1.68 | -1.21 | -1 | 20 | prods2056M2_I0_open_search | `cross_max(day_skew(cross_corr(Vwap, Amt, 30)), 5)` |
| -1.72 | -1.30 | -1.72 | -1 | 5 | prods2056M2_I0_open_search | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), 30))` |
| -1.80 | -1.59 | -1.80 | +1 | 5 | prods2056M2_I0_open_search | `cross_min(day_argmax(cross_corr(Amt, Ret, 60)), 15)` |

## 共性:98 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.25 | 0.000 | 6 | -0.62 / -1.87 | `day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60))` |
| +0.89 | 0.006 | 5 | -0.94 / -1.84 | `cross_delay(day_std(Amt), 1)` |
| +0.83 | 0.014 | 6 | -1.01 / -1.84 | `cross_delay(div(day_std(Amt), day_first(Open)), 1)` |
| +0.80 | 0.000 | 24 | -1.18 / -1.99 | `day_max(cross_corr(Amt, Ret, 60))` |
| +0.69 | 0.021 | 8 | -1.15 / -1.85 | `div(day_std(Amt), day_first(Open))` |
| +0.57 | 0.015 | 19 | -1.33 / -1.90 | `day_first(Open)` |
| +0.48 | 0.037 | 21 | -1.41 / -1.89 | `day_std(Amt)` |
| +0.47 | 0.039 | 41 | -1.52 / -1.98 | `day_sum(Amt)` |
| +0.39 | 0.232 | 6 | -1.43 / -1.81 | `div(day_last(Close), day_first(Open))` |
| +0.38 | 0.292 | 4 | -1.43 / -1.81 | `cross_delay(div(day_last(Close), day_first(Open)), 1)` |
| +0.23 | 0.370 | 9 | -1.58 / -1.81 | `day_min(Ret)` |
| +0.14 | 0.490 | 9 | -1.66 / -1.80 | `day_last(Close)` |
| -0.41 | 0.764 | 6 | -2.17 / -1.76 | `day_min(Low)` |
| -0.70 | 0.977 | 7 | -2.44 / -1.74 | `day_max(High)` |
| -1.35 | 0.998 | 4 | -3.09 / -1.73 | `day_max(nt_cs_regres(Amt, cross_corr(Ret, Ret, 60)))` |

## 拆解(19 次评估)

### head score +0.52:`cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_delay(div(day_std(Amt), day_sum(Amt)), 1)` | -4.02 | -3.97 | -4.02 | — | (子树本身) |
| sufficiency | `div(day_std(Amt), day_sum(Amt))` | -3.90 | -3.90 | -3.85 | — | (子树本身) |
| sufficiency | `day_sum(Amt)` | -3.47 | -2.76 | -3.47 | — | (子树本身) |
| sufficiency | `day_std(Amt)` | -3.75 | -2.98 | -3.75 | — | (子树本身) |
| knockout | `cross_delay(div(day_std(Amt), day_sum(Amt)), 1)` | +0.52 | +0.65 | +0.52 | -0.00 | `cross_corr(day_sum(Amt), div(day_std(Amt), day_sum(Amt)), 60)` |
| knockout | `div(day_std(Amt), day_sum(Amt))` | -0.59 | -0.17 | -0.59 | +1.11 | `cross_corr(day_sum(Amt), cross_delay(day_std(Amt), 1), 60)` |
| swap | `Amt->Volume` | +0.55 | +0.55 | +0.72 | — | `cross_corr(day_sum(Volume), cross_delay(div(day_std(Volume), day_sum(Volume)), 1), 60)` |
| window | `cross_corr@60->30` | -0.32 | -0.32 | +0.45 | — | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 30)` |
| window | `cross_corr@60->120` | +0.76 | +1.53 | +0.76 | — | `cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 120)` |

### head score -0.20:`day_max(cross_corr(Amt, Ret, 180))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Amt->Volume` | -0.13 | +0.11 | -0.13 | — | `day_max(cross_corr(Volume, Ret, 180))` |
| window | `cross_corr@180->90` | -0.47 | -0.04 | -0.47 | — | `day_max(cross_corr(Amt, Ret, 90))` |
| window | `cross_corr@180->360` | -0.27 | +0.14 | -0.27 | — | `day_max(cross_corr(Amt, Ret, 360))` |

### head score -1.68:`cross_max(day_skew(cross_corr(Vwap, Amt, 30)), 5)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_skew(cross_corr(Vwap, Amt, 30))` | -1.47 | -1.47 | -0.96 | — | (子树本身) |
| swap | `Vwap->Close` | -2.70 | -1.72 | -2.70 | — | `cross_max(day_skew(cross_corr(Close, Amt, 30)), 5)` |
| swap | `Amt->Volume` | -1.84 | -1.84 | -1.71 | — | `cross_max(day_skew(cross_corr(Vwap, Volume, 30)), 5)` |
| window | `cross_max@5->2` | -1.54 | -1.54 | -1.04 | — | `cross_max(day_skew(cross_corr(Vwap, Amt, 30)), 2)` |
| window | `cross_max@5->10` | -1.96 | -1.96 | -1.86 | — | `cross_max(day_skew(cross_corr(Vwap, Amt, 30)), 10)` |

### head score -1.72:`day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), 30))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| window | `cross_corr@30->15` | — | — | — | — | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), 15))` |
| window | `cross_corr@30->60` | — | — | — | — | `day_max(cross_corr(nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), nt_cs_regres(Ret, cross_corr(Ret, Ret, 30)), 60))` |

## 机械核心卡(B0 按这个顺序取)

1. `day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60))` — enrichment,均值差 +1.25,p 0.000
2. `cross_delay(day_std(Amt), 1)` — enrichment,均值差 +0.89,p 0.006
3. `cross_delay(div(day_std(Amt), day_first(Open)), 1)` — enrichment,均值差 +0.83,p 0.014
4. `day_max(cross_corr(Amt, Ret, 60))` — enrichment,均值差 +0.80,p 0.000
5. `div(day_std(Amt), day_first(Open))` — enrichment,均值差 +0.69,p 0.021
6. `day_first(Open)` — enrichment,均值差 +0.57,p 0.015
7. `day_std(Amt)` — enrichment,均值差 +0.48,p 0.037
8. `day_sum(Amt)` — enrichment,均值差 +0.47,p 0.039

## 本组之前各轮的任务

- `prods2056Pr1a_Ea`:核心 `day_max(cross_corr(Amt, Ret, 60))`;评分 86,过线 0,入 heads 0;采样计数 {'c05_skeleton': 959, 'c05_no_core': 1909, 'mutation_refused': 2}
  - score -0.08(train -0.08 valid +0.16):`mul(sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), mul(sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60))), day_max(cross_corr(Amt, Ret, 60)))), mul(sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60))), day_max(cross_corr(Amt, Ret, 60))))`
  - score -0.20(train -0.20 valid +0.09):`mul(sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60))), day_max(cross_corr(Amt, Ret, 60)))`
  - score -0.53(train -0.53 valid -0.23):`mul(sub(day_max(in_slice(cross_corr(Volume, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60))), day_max(cross_corr(Amt, Ret, 60)))`
  - score -0.70(train -0.70 valid -0.55):`sub(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), day_max(cross_corr(Amt, Ret, 60)))`
  - score -0.75(train -0.75 valid -0.72):`sub(day_max(cross_corr(Amt, Ret, 60)), cross_mean(day_max(in_slice(cross_corr(Amt, Ret, 60), 1, 60)), 60))`
- `prods2056Pr1b_Nb`:核心 `—`;评分 86,过线 1,入 heads 1;采样计数 {'c05_skeleton': 5}
  - score +0.52(train +0.70 valid +0.52):`cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 60)`
  - score -0.20(train +0.01 valid -0.20):`cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_first(Open)), 1), 60)`
  - score -0.59(train -0.16 valid -0.59):`cross_corr(day_sum(Amt), cross_delay(day_std(Amt), 1), 60)`
  - score -0.66(train +0.27 valid -0.66):`cross_corr(day_std(Amt), day_min(Ret), 60)`
  - score -0.82(train -0.65 valid -0.82):`cross_corr(cross_corr(day_sum(Amt), cross_delay(day_std(Amt), 1), 60), cross_delay(day_std(Amt), 1), 60)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.24(window cross_corr@60->120):`cross_corr(day_sum(Amt), cross_delay(div(day_std(Amt), day_sum(Amt)), 1), 120)`
- 增益 +0.14(window cross_max@5->2):`cross_max(day_skew(cross_corr(Vwap, Amt, 30)), 2)`
