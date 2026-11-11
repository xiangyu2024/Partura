# 定位:种子 2048,P 组,第 3 轮(只含 train / valid)

快照:prods2048M1_I0_open_search, prods2048M2_I0_open_search, prods2048M3_I0_open_search, prods2048Pr1a_Na, prods2048Pr1b_Nb, prods2048Pr2a_Ea;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(12 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.07 | +1.14 | +1.07 | -1 | 0 | prods2048Pr2a_Ea | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60))` |
| +1.07 | +1.20 | +1.07 | -1 | 0 | prods2048Pr2a_Ea | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 241))` |
| +1.01 | +1.23 | +1.01 | -1 | 0 | prods2048Pr2a_Ea | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60)), 60))` |
| +0.95 | +0.97 | +0.95 | -1 | 0 | prods2048Pr2a_Ea | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), LogTotalCap), 1), 60))` |
| +0.67 | +1.20 | +0.67 | -1 | 0 | prods2048Pr2a_Ea | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_ema(cross_mean(sub(div(cs_first_low20(LogTotalCap, ListAge), day_open(Open)), 1), 60), 60))` |
| +0.58 | +0.58 | +0.92 | -1 | 0 | prods2048Pr2a_Ea | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60))` |
| -1.13 | -0.96 | -1.13 | -1 | 0 | prods2048M2_I0_open_search | `cross_mean(day_std(Volume), 20)` |
| -1.16 | -1.10 | -1.16 | -1 | 5 | prods2048M2_I0_open_search | `day_std(Volume)` |
| -1.16 | -1.10 | -1.16 | -1 | 5 | prods2048M2_I0_open_search | `day_std(Volume)` |
| -1.28 | -1.28 | -1.22 | +1 | 5 | prods2048M3_I0_open_search | `ts_var(ts_mean(cross_cov(neg(neg(sigmoid(day_std(Low)))), day_hurst(Open), 30), 40), 5)` |
| -2.27 | -1.50 | -2.27 | -1 | 20 | prods2048M3_I0_open_search | `signedpower(neg(neg(sigmoid(day_std(Open)))))` |
| -2.31 | -1.52 | -2.31 | -1 | 20 | prods2048M3_I0_open_search | `ts_decay_linear(sigmoid(ts_decay_linear(sigmoid(day_std(Low)), 5)), 5)` |

## 共性:184 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.41 | 0.001 | 4 | +0.65 / -1.76 | `div(cs_first_low20(LogTotalCap, ListAge), day_open(Open))` |
| +2.38 | 0.001 | 5 | +0.61 / -1.77 | `div(day_close(Close), LogTotalCap)` |
| +2.11 | 0.000 | 48 | -0.15 / -2.26 | `cs_first_low20(LogTotalCap, ListAge)` |
| +1.79 | 0.006 | 4 | +0.05 / -1.75 | `div(day_close(Open), day_open(Open))` |
| +1.30 | 0.005 | 7 | -0.46 / -1.76 | `day_close(Open)` |
| +1.25 | 0.000 | 68 | -0.92 / -2.17 | `day_open(Open)` |
| +1.06 | 0.000 | 52 | -0.95 / -2.01 | `div(day_close(Close), day_open(Open))` |
| +1.01 | 0.000 | 97 | -1.23 / -2.24 | `day_close(Close)` |
| +0.41 | 0.208 | 4 | -1.31 / -1.72 | `cross_min(cs_first_low20(LogTotalCap, ListAge), 241)` |
| +0.40 | 0.286 | 4 | -1.32 / -1.72 | `div(day_close(Close), cross_max(day_close(Close), 241))` |
| +0.27 | 0.244 | 7 | -1.45 / -1.72 | `cross_delay(day_close(Close), 20)` |
| +0.17 | 0.363 | 13 | -1.55 / -1.72 | `cross_max(day_close(Close), 241)` |
| +0.11 | 0.232 | 8 | -1.61 / -1.71 | `div(day_open(Open), day_open(Open))` |
| -0.23 | 0.765 | 20 | -1.91 / -1.68 | `cross_delay(day_close(Close), 1)` |
| -0.24 | 0.767 | 19 | -1.92 / -1.68 | `div(day_open(Open), cross_delay(day_close(Close), 1))` |
| -0.25 | 0.500 | 5 | -1.95 / -1.70 | `day_std(Volume)` |
| -0.32 | 0.698 | 5 | -2.02 / -1.70 | `cross_min(day_close(Close), 241)` |
| -0.38 | 0.810 | 4 | -2.08 / -1.70 | `neg(neg(sigmoid(day_std(Low))))` |
| -0.51 | 0.942 | 7 | -2.20 / -1.69 | `neg(sigmoid(day_std(Low)))` |
| -0.53 | 0.953 | 8 | -2.21 / -1.69 | `sigmoid(day_std(Low))` |

## 拆解(42 次评估)

### head score +1.07:`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_close(Close), day_open(Open))` | -4.39 | -4.39 | -3.61 | — | (子树本身) |
| sufficiency | `cs_first_low20(LogTotalCap, ListAge)` | -0.10 | -0.10 | +1.04 | — | (子树本身) |
| sufficiency | `day_close(Close)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| sufficiency | `day_open(Open)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| knockout | `sub(div(day_close(Close), day_open(Open)), 1)` | +1.07 | +1.14 | +1.07 | -0.00 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(div(day_close(Close), day_open(Open)), 60), 60))` |
| knockout | `div(day_close(Close), day_open(Open))` | +0.91 | +0.91 | +0.96 | +0.17 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(day_close(Close), 1), 60), 60))` |
| knockout | `cs_first_low20(LogTotalCap, ListAge)` | +0.91 | +0.91 | +0.99 | +0.16 | `cs_first_low20(LogTotalCap, cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60))` |
| swap | `Close->Vwap` | +1.09 | +1.09 | +1.10 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Vwap), day_open(Open)), 1), 60), 60))` |
| swap | `Open->Close` | +1.07 | +1.11 | +1.07 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Close)), 1), 60), 60))` |
| window | `cross_mean@60->30` | +0.95 | +0.95 | +1.06 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 30))` |
| window | `cross_mean@60->120` | +0.95 | +0.95 | +0.96 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 120))` |

### head score +1.07:`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 241))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_close(Close), day_open(Open))` | -4.39 | -4.39 | -3.61 | — | (子树本身) |
| sufficiency | `cs_first_low20(LogTotalCap, ListAge)` | -0.10 | -0.10 | +1.04 | — | (子树本身) |
| sufficiency | `day_close(Close)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| sufficiency | `day_open(Open)` | -2.37 | -1.60 | -2.37 | — | (子树本身) |
| knockout | `sub(div(day_close(Close), day_open(Open)), 1)` | +1.07 | +1.20 | +1.07 | -0.00 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(div(day_close(Close), day_open(Open)), 241))` |
| knockout | `div(day_close(Close), day_open(Open))` | +0.98 | +1.04 | +0.98 | +0.09 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(day_close(Close), 1), 241))` |
| knockout | `cs_first_low20(LogTotalCap, ListAge)` | +1.02 | +1.09 | +1.02 | +0.05 | `cs_first_low20(LogTotalCap, cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 241))` |
| swap | `Close->Vwap` | +1.08 | +1.21 | +1.08 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Vwap), day_open(Open)), 1), 241))` |
| swap | `Open->Close` | +1.07 | +1.23 | +1.07 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Close)), 1), 241))` |
| window | `cross_mean@241->120` | +0.90 | +0.90 | +1.02 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 120))` |
| window | `cross_mean@241->482` | +1.25 | +1.25 | +1.27 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 482))` |

### head score +1.01:`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60)), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60))` | +1.07 | +1.14 | +1.07 | — | (子树本身) |
| sufficiency | `div(day_close(Close), day_open(Open))` | -4.39 | -4.39 | -3.61 | — | (子树本身) |
| sufficiency | `cs_first_low20(LogTotalCap, ListAge)` | -0.10 | -0.10 | +1.04 | — | (子树本身) |
| knockout | `sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60))` | +1.01 | +1.20 | +1.01 | +0.00 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), 60))` |
| knockout | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60))` | +0.47 | +0.53 | +0.47 | +0.54 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60)), 60))` |
| knockout | `sub(div(day_close(Close), day_open(Open)), 1)` | +1.01 | +1.23 | +1.01 | +0.00 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(div(day_close(Close), day_open(Open)), 60), 60)), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60)), 60))` |
| knockout | `sub(div(day_close(Close), day_open(Open)), 5)` | +1.01 | +1.23 | +1.01 | +0.00 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), cross_mean(div(day_close(Close), day_open(Open)), 60)), 60))` |
| swap | `Close->Vwap` | +1.00 | +1.20 | +1.00 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Vwap), day_open(Open)), 1), 60), 60)), cross_mean(sub(div(day_close(Vwap), day_open(Open)), 5), 60)), 60))` |
| swap | `Open->Close` | +1.01 | +1.21 | +1.01 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Close)), 1), 60), 60)), cross_mean(sub(div(day_close(Close), day_open(Close)), 5), 60)), 60))` |
| window | `cross_mean@60->30` | +1.01 | +1.15 | +1.01 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60)), 30))` |
| window | `cross_mean@60->120` | +0.97 | +0.97 | +1.06 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60)), 120))` |

### head score +0.95:`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), LogTotalCap), 1), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `div(day_close(Close), LogTotalCap)` | -2.43 | -1.64 | -2.43 | — | (子树本身) |
| sufficiency | `cs_first_low20(LogTotalCap, ListAge)` | -0.10 | -0.10 | +1.04 | — | (子树本身) |
| sufficiency | `day_close(Close)` | -2.35 | -1.60 | -2.35 | — | (子树本身) |
| knockout | `sub(div(day_close(Close), LogTotalCap), 1)` | +0.95 | +0.97 | +0.95 | +0.00 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(div(day_close(Close), LogTotalCap), 60))` |
| knockout | `div(day_close(Close), LogTotalCap)` | +0.91 | +0.96 | +0.91 | +0.04 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(day_close(Close), 1), 60))` |
| knockout | `cs_first_low20(LogTotalCap, ListAge)` | +0.49 | +0.53 | +0.49 | +0.46 | `cs_first_low20(LogTotalCap, cross_mean(sub(div(day_close(Close), LogTotalCap), 1), 60))` |
| swap | `Close->Vwap` | +0.95 | +0.97 | +0.95 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Vwap), LogTotalCap), 1), 60))` |
| window | `cross_mean@60->30` | +0.95 | +1.03 | +0.95 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), LogTotalCap), 1), 30))` |
| window | `cross_mean@60->120` | +0.95 | +0.99 | +0.95 | — | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), LogTotalCap), 1), 120))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60))` — ablation,自身 score +1.07(所在 head +1.01)
2. `div(cs_first_low20(LogTotalCap, ListAge), day_open(Open))` — enrichment,均值差 +2.41,p 0.001
3. `div(day_close(Close), LogTotalCap)` — enrichment,均值差 +2.38,p 0.001
4. `cs_first_low20(LogTotalCap, ListAge)` — enrichment,均值差 +2.11,p 0.000
5. `div(day_close(Open), day_open(Open))` — enrichment,均值差 +1.79,p 0.006
6. `day_close(Open)` — enrichment,均值差 +1.30,p 0.005
7. `day_open(Open)` — enrichment,均值差 +1.25,p 0.000
8. `div(day_close(Close), day_open(Open))` — enrichment,均值差 +1.06,p 0.000
9. `day_close(Close)` — enrichment,均值差 +1.01,p 0.000

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
- `prods2048Pr2a_Ea`:核心 `cs_first_low20(LogTotalCap, ListAge)`;评分 102,过线 21,入 heads 6;采样计数 {'c05_skeleton': 1003, 'c05_no_core': 2015}
  - score +1.07(train +1.14 valid +1.07):`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60))`
  - score +1.07(train +1.20 valid +1.07):`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 241))`
  - score +1.06(train +1.07 valid +1.06):`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Open), day_open(Open)), 1), 60), 60))`
  - score +1.01(train +1.23 valid +1.01):`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), cross_mean(sub(div(day_close(Close), day_open(Open)), 5), 60)), 60))`
  - score +1.01(train +1.20 valid +1.01):`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 60), 60)), 5), 60))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.18(window cross_mean@241->482):`cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(sub(div(day_close(Close), day_open(Open)), 1), 482))`
