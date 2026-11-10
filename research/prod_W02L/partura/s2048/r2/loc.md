# 定位:种子 2048,P 组,第 2 轮(只含 train / valid)

快照:prods2048M1_I0_open_search, prods2048M2_I0_open_search, prods2048Pr1a_Na, prods2048Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| -1.13 | -0.96 | -1.13 | -1 | 0 | prods2048M2_I0_open_search | `cross_mean(day_std(Volume), 20)` |
| -1.16 | -1.10 | -1.16 | -1 | 5 | prods2048M2_I0_open_search | `day_std(Volume)` |
| -1.16 | -1.10 | -1.16 | -1 | 5 | prods2048M2_I0_open_search | `day_std(Volume)` |

## 共性:126 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.31 | 0.002 | 5 | -0.96 / -2.26 | `day_close(Open)` |
| +0.93 | 0.039 | 4 | -1.31 / -2.24 | `cs_first_low20(LogTotalCap, ListAge)` |
| +0.93 | 0.039 | 4 | -1.31 / -2.24 | `cross_min(cs_first_low20(LogTotalCap, ListAge), 241)` |
| +0.81 | 0.038 | 7 | -1.45 / -2.26 | `cross_delay(day_close(Close), 20)` |
| +0.67 | 0.002 | 66 | -1.89 / -2.56 | `day_close(Close)` |
| +0.65 | 0.024 | 8 | -1.61 / -2.25 | `div(day_open(Open), day_open(Open))` |
| +0.61 | 0.002 | 32 | -1.75 / -2.37 | `div(day_close(Close), day_open(Open))` |
| +0.54 | 0.187 | 10 | -1.72 / -2.25 | `cross_max(day_close(Close), 241)` |
| +0.53 | 0.004 | 40 | -1.85 / -2.38 | `day_open(Open)` |
| +0.35 | 0.197 | 20 | -1.91 / -2.27 | `cross_delay(day_close(Close), 1)` |
| +0.34 | 0.211 | 19 | -1.92 / -2.26 | `div(day_open(Open), cross_delay(day_close(Close), 1))` |
| +0.27 | 0.194 | 5 | -1.95 / -2.22 | `day_std(Volume)` |
| +0.20 | 0.490 | 5 | -2.02 / -2.22 | `cross_min(day_close(Close), 241)` |
| -0.06 | 0.829 | 5 | -2.27 / -2.21 | `day_std(High)` |
| -0.97 | 0.975 | 4 | -3.15 / -2.18 | `day_std(Ret)` |

## 拆解(6 次评估)

### head score -1.13:`cross_mean(day_std(Volume), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_std(Volume)` | -1.21 | -1.10 | -1.21 | — | (子树本身) |
| swap | `Volume->Amt` | -4.16 | -3.18 | -4.16 | — | `cross_mean(day_std(Amt), 20)` |
| window | `cross_mean@20->10` | -1.06 | -1.06 | -1.01 | — | `cross_mean(day_std(Volume), 10)` |
| window | `cross_mean@20->40` | -1.33 | -1.05 | -1.33 | — | `cross_mean(day_std(Volume), 40)` |

### head score -1.16:`day_std(Volume)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.75 | -2.98 | -3.75 | — | `day_std(Amt)` |

### head score -1.16:`day_std(Volume)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| swap | `Volume->Amt` | -3.75 | -2.98 | -3.75 | — | `day_std(Amt)` |

## 机械核心卡(B0 按这个顺序取)

1. `day_close(Open)` — enrichment,均值差 +1.31,p 0.002
2. `cs_first_low20(LogTotalCap, ListAge)` — enrichment,均值差 +0.93,p 0.039
3. `cross_min(cs_first_low20(LogTotalCap, ListAge), 241)` — enrichment,均值差 +0.93,p 0.039
4. `cross_delay(day_close(Close), 20)` — enrichment,均值差 +0.81,p 0.038
5. `day_close(Close)` — enrichment,均值差 +0.67,p 0.002
6. `div(day_open(Open), day_open(Open))` — enrichment,均值差 +0.65,p 0.024
7. `div(day_close(Close), day_open(Open))` — enrichment,均值差 +0.61,p 0.002
8. `day_open(Open)` — enrichment,均值差 +0.53,p 0.004

## 本组之前各轮的任务

- `prods2048Pr1a_Na`:核心 `—`;评分 87,过线 0,入 heads 0;采样计数 {'c05_skeleton': 13}
  - score +0.38(train +0.41 valid +0.38):`cs_first_low20(LogTotalCap, day_es_ratio_hi(inv(cross_max(Close, 241))))`
  - score -0.48(train -0.23 valid -0.48):`day_es_ratio_hi(inv(cross_max(Open, 241)))`
  - score -0.63(train -0.26 valid -0.63):`day_es_ratio_hi(inv(cross_max(Close, 241)))`
  - score -0.83(train -0.68 valid -0.83):`div(cross_delay(day_close(Close), 20), cross_max(day_close(Open), 241))`
  - score -0.83(train -0.69 valid -0.83):`div(cross_delay(day_close(Close), 20), cross_max(day_close(Close), 241))`
- `prods2048Pr1b_Nb`:核心 `—`;评分 83,过线 0,入 heads 0;采样计数 {'c05_skeleton': 9}
  - score -0.65(train -0.65 valid +0.21):`sub(cross_mean(sub(div(day_open(Open), day_open(Vwap)), 1), 241), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 241))`
  - score -0.70(train -0.70 valid +0.12):`cross_mean(sub(div(day_close(Open), day_open(Open)), 1), 241)`
  - score -0.71(train -0.71 valid +0.13):`sub(cross_mean(sub(div(day_open(Open), day_open(Open)), 1), 241), cross_mean(sub(div(day_close(Open), day_open(Open)), -0.5), 241))`
  - score -0.72(train -0.72 valid +0.09):`sub(cross_mean(-2, 241), cross_mean(sub(div(day_close(Close), day_open(Open)), -2), 241))`
  - score -0.72(train -0.72 valid +0.09):`cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 241)`

## 比原 head 好的拆解变体(R 候选)

(没有)
