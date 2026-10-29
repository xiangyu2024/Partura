# 定位:种子 803,C 组,第 2 轮(只含 train / valid)

快照:c05s803M1_I0_open_search, c05s803M2_I0_open_search, c06s803Cr1a_Ea, c06s803Cr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.56 | +1.56 | +2.07 | -1 | 20 | c05s803M2_I0_open_search | `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 3)` |
| +1.23 | +1.23 | +2.29 | -1 | 5 | c05s803M2_I0_open_search | `ts_skew(day_durbin_watson(Open), 50)` |
| +0.99 | +0.99 | +1.86 | +1 | 20 | c06s803Cr1a_Ea | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)` |
| +0.97 | +0.97 | +1.54 | -1 | 20 | c05s803M1_I0_open_search | `day_kurt(Ret)` |
| +0.86 | +0.86 | +1.06 | +1 | 20 | c06s803Cr1b_Nb | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))` |
| +0.65 | +0.65 | +0.97 | -1 | 5 | c06s803Cr1a_Ea | `cross_mean(mul(add(day_kurt(Ret), 3), add(day_kurt(Ret), 3)), 15)` |

## 共性:227 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.59 | 0.000 | 11 | +0.65 / -0.94 | `ts_skew(day_durbin_watson(Open), 50)` |
| +1.55 | 0.006 | 4 | +0.66 / -0.89 | `ts_med(sub(day_hurst(Ret), day_kurt(Ret)), 40)` |
| +1.54 | 0.003 | 5 | +0.64 / -0.90 | `sub(day_hurst(Ret), day_kurt(Ret))` |
| +1.51 | 0.000 | 65 | +0.21 / -1.29 | `day_kurt(Ret)` |
| +1.45 | 0.002 | 8 | +0.54 / -0.91 | `ts_med(sub(day_hurst(Close), day_kurt(Ret)), 40)` |
| +1.43 | 0.021 | 4 | +0.54 / -0.89 | `ts_quantile_q50(day_kurt(Ret), 40)` |
| +1.42 | 0.000 | 14 | +0.47 / -0.95 | `sub(day_hurst(Close), day_kurt(Ret))` |
| +1.41 | 0.000 | 15 | +0.46 / -0.96 | `day_hurst(Close)` |
| +1.17 | 0.032 | 5 | +0.28 / -0.89 | `ts_skew(day_durbin_watson(Open), 40)` |
| +1.15 | 0.000 | 25 | +0.16 / -0.99 | `day_durbin_watson(Open)` |
| +1.06 | 0.001 | 22 | +0.10 / -0.97 | `day_zero_ratio(Ret)` |
| +0.86 | 0.029 | 6 | -0.03 / -0.89 | `day_hurst(Ret)` |
| +0.74 | 0.074 | 9 | -0.15 / -0.89 | `neg(day_centroid(Amt))` |
| +0.64 | 0.076 | 15 | -0.27 / -0.90 | `day_centroid(Amt)` |
| -0.37 | 0.880 | 4 | -1.23 / -0.86 | `day_quantile_q25(Open)` |

## 拆解(26 次评估)

### head score +1.56:`cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 3)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `ts_skew(ts_skew(day_durbin_watson(Open), 50), 50)` | — | — | — | — | 门槛废品 |
| sufficiency | `ts_skew(day_durbin_watson(Open), 50)` | +1.18 | +1.18 | +2.26 | — | (子树本身) |
| sufficiency | `day_durbin_watson(Open)` | -2.13 | -2.13 | -0.11 | — | (子树本身) |
| knockout | `ts_skew(ts_skew(day_durbin_watson(Open), 50), 50)` | +1.56 | +1.56 | +2.06 | +0.01 | `cross_autocorr_s1(ts_skew(day_durbin_watson(Open), 50), 3)` |
| swap | `Open->Close` | +1.33 | +1.33 | +2.39 | — | `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Close), 50), 50), 3)` |
| window | `cross_autocorr_s1@3->2` | +1.44 | +1.44 | +2.01 | — | `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 2)` |
| window | `cross_autocorr_s1@3->6` | +1.61 | +1.61 | +2.17 | — | `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 6)` |

### head score +1.23:`ts_skew(day_durbin_watson(Open), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_durbin_watson(Open)` | -2.13 | -2.13 | -0.11 | — | (子树本身) |
| swap | `Open->Close` | +1.43 | +1.43 | +2.23 | — | `ts_skew(day_durbin_watson(Close), 50)` |
| window | `ts_skew@50->25` | +1.06 | +1.06 | +1.64 | — | `ts_skew(day_durbin_watson(Open), 25)` |
| window | `ts_skew@50->100` | +1.28 | +1.28 | +2.47 | — | `ts_skew(day_durbin_watson(Open), 100)` |

### head score +0.99:`cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret)))))))` | +1.01 | +1.01 | +1.38 | — | (子树本身) |
| sufficiency | `cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))` | +0.67 | +0.67 | +1.40 | — | (子树本身) |
| sufficiency | `sub(day_hurst(Close), day_kurt(Ret))` | +0.97 | +0.97 | +1.56 | — | (子树本身) |
| knockout | `sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret)))))` | +0.95 | +0.95 | +1.83 | +0.04 | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret)))))), 20)` |
| knockout | `add(sub(day_hurst(Close), day_kurt(Ret)), 0.5)` | +0.97 | +0.97 | +1.86 | +0.02 | `cross_ema(cs_winsor(mul(sub(day_hurst(Close), day_kurt(Ret)), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)` |
| knockout | `add(sub(day_hurst(Close), day_kurt(Ret)), 0.5)` | +0.98 | +0.98 | +1.86 | +0.01 | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(sub(day_hurst(Close), day_kurt(Ret)), sub(1, day_zero_ratio(Ret))))))), 20)` |
| knockout | `sub(day_hurst(Close), day_kurt(Ret))` | +0.67 | +0.67 | +1.41 | +0.32 | `cross_ema(cs_winsor(mul(add(day_hurst(Close), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)` |
| swap | `Close->Vwap` | — | — | — | — | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Vwap), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Vwap), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)` |
| window | `cross_ema@20->10` | +0.85 | +0.85 | +1.73 | — | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 10)` |
| window | `cross_ema@20->40` | +0.99 | +0.99 | +1.88 | — | `cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 40)` |

### head score +0.86:`cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `neg(day_centroid(Amt))` | -0.08 | -0.08 | +0.58 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | -0.08 | -0.08 | +0.58 | — | (子树本身) |
| knockout | `mul(0.5, neg(day_centroid(Amt)))` | +0.86 | +0.86 | +1.06 | +0.00 | `cs_mask_top_replace_mean(neg(day_centroid(Amt)))` |
| knockout | `neg(day_centroid(Amt))` | -0.59 | +0.06 | -0.59 | +1.46 | `cs_mask_top_replace_mean(mul(0.5, day_centroid(Amt)))` |
| swap | `Amt->Volume` | +0.90 | +0.90 | +1.16 | — | `cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Volume))))` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_skew(day_durbin_watson(Open), 50)` — ablation,自身 score +1.18(所在 head +1.56)
2. `cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret)))))))` — ablation,自身 score +1.01(所在 head +0.99)
3. `sub(day_hurst(Close), day_kurt(Ret))` — ablation,自身 score +0.97(所在 head +0.99)
4. `cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))` — ablation,自身 score +0.67(所在 head +0.99)
5. `ts_med(sub(day_hurst(Ret), day_kurt(Ret)), 40)` — enrichment,均值差 +1.55,p 0.006
6. `sub(day_hurst(Ret), day_kurt(Ret))` — enrichment,均值差 +1.54,p 0.003
7. `day_kurt(Ret)` — enrichment,均值差 +1.51,p 0.000
8. `ts_med(sub(day_hurst(Close), day_kurt(Ret)), 40)` — enrichment,均值差 +1.45,p 0.002
9. `ts_quantile_q50(day_kurt(Ret), 40)` — enrichment,均值差 +1.43,p 0.021
10. `day_hurst(Close)` — enrichment,均值差 +1.41,p 0.000
11. `ts_skew(day_durbin_watson(Open), 40)` — enrichment,均值差 +1.17,p 0.032
12. `day_durbin_watson(Open)` — enrichment,均值差 +1.15,p 0.000
13. `day_zero_ratio(Ret)` — enrichment,均值差 +1.06,p 0.001
14. `day_hurst(Ret)` — enrichment,均值差 +0.86,p 0.029
15. `neg(day_centroid(Amt))` — enrichment,均值差 +0.74,p 0.074
16. `day_centroid(Amt)` — enrichment,均值差 +0.64,p 0.076

## 本组之前各轮的任务

- `c06s803Cr1a_Ea`:核心 `day_kurt(Ret)`;评分 104,过线 41,入 heads 2;采样计数 {'c05_no_core': 1974, 'c05_skeleton': 36}
  - score +0.99(train +0.99 valid +1.86):`cross_ema(cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, cs_winsor(mul(add(sub(day_hurst(Close), day_kurt(Ret)), 0.5), sub(1, day_zero_ratio(Ret))))))), 20)`
  - score +0.95(train +0.95 valid +1.75):`cross_ema(cs_winsor(mul(add(sub(day_skew(Low), day_kurt(Ret)), 3), sub(1, cs_winsor(mul(add(sub(day_skew(Low), day_kurt(Ret)), 3), sub(1, day_zero_ratio(Ret))))))), 20)`
  - score +0.94(train +0.94 valid +1.84):`cross_ema(cs_winsor(mul(add(day_kurt(Ret), 3), sub(1, cs_winsor(mul(add(day_kurt(Ret), 3), sub(1, day_zero_ratio(Ret))))))), 20)`
  - score +0.82(train +0.82 valid +1.79):`cross_ema(cs_winsor(mul(add(day_kurt(Ret), -5), sub(3, day_zero_ratio(Ret)))), 20)`
  - score +0.82(train +0.82 valid +1.66):`cross_ema(sub(day_hurst(Close), day_kurt(Ret)), 20)`
- `c06s803Cr1b_Nb`:核心 `—`;评分 59,过线 2,入 heads 1;采样计数 {}
  - score +0.86(train +0.86 valid +1.06):`cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt))))`
  - score +0.86(train +0.86 valid +1.06):`neg(cs_mask_top_replace_mean(mul(0.5, neg(day_centroid(Amt)))))`
  - score +0.48(train +0.48 valid +0.76):`neg(LogFloatShares)`
  - score +0.48(train +0.48 valid +0.77):`pow_2_5(LogFloatShares)`
  - score +0.38(train +0.38 valid +0.42):`neg(cs_mask_top_replace_mean(mul(LogTotalCap, neg(LogFloatShares))))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.21(swap Open->Close):`ts_skew(day_durbin_watson(Close), 50)`
