# 定位:种子 802,B 组,第 1 轮(只含 train / valid)

快照:c05s802M1_I0_open_search;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.14 | +1.14 | +2.70 | +1 | 20 | c05s802M1_I0_open_search | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 40))` |
| +0.83 | +0.83 | +1.00 | +1 | 5 | c05s802M1_I0_open_search | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))))))` |
| +0.83 | +1.09 | +0.83 | -1 | 5 | c05s802M1_I0_open_search | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))` |
| +0.73 | +0.73 | +1.38 | -1 | 20 | c05s802M1_I0_open_search | `inv(ts_decay_linear(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 40))` |
| +0.71 | +0.81 | +0.71 | +1 | 5 | c05s802M1_I0_open_search | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))` |
| +0.54 | +0.54 | +1.26 | +1 | 20 | c05s802M1_I0_open_search | `day_mean(neg(in_delta(Volume, 60)))` |

## 共性:77 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.36 | 0.000 | 8 | +0.60 / -0.76 | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` |
| +1.33 | 0.000 | 11 | +0.53 / -0.81 | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` |
| +1.30 | 0.001 | 12 | +0.48 / -0.82 | `inv(LogFloatShares)` |
| +1.20 | 0.011 | 6 | +0.48 / -0.71 | `ts_decay_linear(inv(LogFloatShares), 40)` |
| +1.16 | 0.048 | 4 | +0.48 / -0.68 | `ts_decay_linear(LogFloatShares, 40)` |
| +0.99 | 0.001 | 15 | +0.18 / -0.81 | `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` |
| +0.91 | 0.002 | 18 | +0.08 / -0.83 | `day_durbin_watson(Volume)` |
| +0.78 | 0.007 | 21 | -0.05 / -0.83 | `day_flat_run_max(Vwap)` |
| -0.06 | 0.750 | 6 | -0.67 / -0.61 | `day_durbin_watson(in_delta(Volume, 60))` |
| -0.13 | 0.743 | 5 | -0.74 / -0.61 | `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(in_delta(Volume, 60)), 50)` |

## 拆解(47 次评估)

### head score +1.14:`inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 40)` | +0.51 | +0.79 | +0.51 | — | (子树本身) |
| sufficiency | `inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))` | +0.72 | +0.72 | +0.89 | — | (子树本身) |
| sufficiency | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))` | +0.71 | +0.81 | +0.71 | — | (子树本身) |
| sufficiency | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` | +0.33 | +0.63 | +0.33 | — | (子树本身) |
| knockout | `ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 40)` | +0.71 | +0.81 | +0.71 | +0.43 | `inv(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))))` |
| knockout | `inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))` | +0.43 | +0.77 | +0.43 | +0.71 | `inv(ts_decay_linear(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))), 40))` |
| knockout | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))` | +0.96 | +0.96 | +2.43 | +0.18 | `inv(ts_decay_linear(inv(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))), 40))` |
| knockout | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` | +0.43 | +0.77 | +0.43 | +0.71 | `inv(ts_decay_linear(inv(pow_1_5(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))), 40))` |
| swap | `Vwap->Close` | +0.50 | +0.50 | +2.02 | — | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Close), day_durbin_watson(Volume), 50))))), 40))` |
| swap | `Volume->Amt` | +1.11 | +1.11 | +2.60 | — | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 50))))), 40))` |
| window | `ts_decay_linear@40->20` | +1.11 | +1.11 | +2.01 | — | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 20))` |
| window | `ts_decay_linear@40->80` | +1.24 | +1.24 | +2.62 | — | `inv(ts_decay_linear(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))), 80))` |

### head score +0.83:`inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))))` | +0.76 | +0.76 | +0.89 | — | (子树本身) |
| sufficiency | `inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))))` | +0.73 | +0.73 | +0.94 | — | (子树本身) |
| sufficiency | `sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))` | +0.82 | +0.82 | +1.04 | — | (子树本身) |
| sufficiency | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))` | +0.71 | +0.81 | +0.71 | — | (子树本身) |
| knockout | `pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))))` | +0.82 | +0.82 | +1.04 | +0.02 | `inv(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))))` |
| knockout | `inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))))` | +0.76 | +0.76 | +0.89 | +0.08 | `inv(pow_1_5(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))))` |
| knockout | `sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))` | +0.56 | +0.56 | +0.95 | +0.27 | `inv(pow_1_5(inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))))` |
| knockout | `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))` | +0.93 | +0.93 | +1.38 | -0.10 | `inv(pow_1_5(inv(sigmoid(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))))` |
| swap | `Vwap->Close` | +0.70 | +0.70 | +1.32 | — | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Close), day_durbin_watson(Volume), 50))))))))` |
| swap | `Volume->Amt` | +0.82 | +0.82 | +0.90 | — | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 50))))))))` |
| window | `ts_regbeta@50->25` | +0.40 | +0.79 | +0.40 | — | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 25))))))))` |
| window | `ts_regbeta@50->100` | +1.16 | +1.16 | +1.66 | — | `inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))` |

### head score +0.83:`sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)` | +0.55 | +0.83 | +0.55 | — | (子树本身) |
| sufficiency | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` | +0.80 | +0.80 | +1.14 | — | (子树本身) |
| sufficiency | `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` | -0.14 | +0.45 | -0.14 | — | (子树本身) |
| sufficiency | `day_flat_run_max(Vwap)` | — | — | — | — | 门槛废品 |
| knockout | `ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)` | — | — | — | — | `sigmoid(day_flat_run_max(Vwap))` |
| knockout | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` | — | — | — | — | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50), 50))` |
| knockout | `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` | — | — | — | — | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(day_flat_run_max(Vwap)), 50))` |
| swap | `Vwap->Close` | -1.03 | +0.23 | -1.03 | — | `sigmoid(ts_regbeta(day_flat_run_max(Close), sigmoid(ts_regbeta(day_flat_run_max(Close), day_durbin_watson(Volume), 50)), 50))` |
| swap | `Volume->Amt` | +0.96 | +1.06 | +0.96 | — | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 50)), 50))` |
| window | `ts_regbeta@50->25` | -0.05 | +0.77 | -0.05 | — | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 25))` |
| window | `ts_regbeta@50->100` | +0.47 | +0.56 | +0.47 | — | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 100))` |

### head score +0.73:`inv(ts_decay_linear(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 40))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_decay_linear(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 40)` | -0.09 | +0.67 | -0.09 | — | (子树本身) |
| sufficiency | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` | +0.33 | +0.63 | +0.33 | — | (子树本身) |
| sufficiency | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` | +0.80 | +0.80 | +1.14 | — | (子树本身) |
| sufficiency | `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` | -0.14 | +0.45 | -0.14 | — | (子树本身) |
| knockout | `ts_decay_linear(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 40)` | +0.80 | +0.80 | +1.14 | -0.07 | `inv(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))` |
| knockout | `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` | +0.96 | +0.96 | +2.43 | -0.23 | `inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 40))` |
| knockout | `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` | -0.07 | +0.67 | -0.07 | +0.80 | `inv(ts_decay_linear(inv(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 40))` |
| knockout | `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` | -2.57 | -2.51 | -2.57 | +3.30 | `inv(ts_decay_linear(inv(sigmoid(day_flat_run_max(Vwap))), 40))` |
| swap | `Vwap->Close` | +0.32 | +0.32 | +0.84 | — | `inv(ts_decay_linear(inv(sigmoid(ts_regbeta(day_flat_run_max(Close), day_durbin_watson(Volume), 50))), 40))` |
| swap | `Volume->Amt` | +0.74 | +0.74 | +1.35 | — | `inv(ts_decay_linear(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 50))), 40))` |
| window | `ts_decay_linear@40->20` | +0.81 | +0.81 | +1.35 | — | `inv(ts_decay_linear(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 20))` |
| window | `ts_decay_linear@40->80` | +0.68 | +0.68 | +1.46 | — | `inv(ts_decay_linear(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))), 80))` |

## 机械核心卡(B0 按这个顺序取)

1. `sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))` — ablation,自身 score +0.82(所在 head +0.83)
2. `sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))` — ablation,自身 score +0.80(所在 head +0.83)
3. `pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))))` — ablation,自身 score +0.76(所在 head +0.83)
4. `inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))))` — ablation,自身 score +0.73(所在 head +0.83)
5. `inv(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))))` — ablation,自身 score +0.72(所在 head +1.14)
6. `pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50))))` — ablation,自身 score +0.71(所在 head +1.14)
7. `ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 50)` — ablation,自身 score +0.55(所在 head +0.83)
8. `inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))` — enrichment,均值差 +1.36,p 0.000
9. `inv(LogFloatShares)` — enrichment,均值差 +1.30,p 0.001
10. `ts_decay_linear(inv(LogFloatShares), 40)` — enrichment,均值差 +1.20,p 0.011
11. `ts_decay_linear(LogFloatShares, 40)` — enrichment,均值差 +1.16,p 0.048
12. `ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)` — enrichment,均值差 +0.99,p 0.001
13. `day_durbin_watson(Volume)` — enrichment,均值差 +0.91,p 0.002
14. `day_flat_run_max(Vwap)` — enrichment,均值差 +0.78,p 0.007

## 本组之前各轮的任务

(第 1 轮,还没有)

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.32(window ts_regbeta@50->100):`inv(pow_1_5(inv(sigmoid(pow_1_5(inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 100))))))))`
- 增益 +0.23(knockout inv(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)))):`inv(ts_decay_linear(sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Volume), 50)), 40))`
- 增益 +0.13(swap Volume->Amt):`sigmoid(ts_regbeta(day_flat_run_max(Vwap), sigmoid(ts_regbeta(day_flat_run_max(Vwap), day_durbin_watson(Amt), 50)), 50))`
