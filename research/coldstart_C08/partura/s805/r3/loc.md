# 定位:种子 805,P 组,第 3 轮(只含 train / valid)

快照:c07s805M1_I0_open_search, c07s805M2_I0_open_search, c07s805M3_I0_open_search, c08s805Pr1a_Ea, c08s805Pr1b_Nb, c08s805Pr2a_Ea, c08s805Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(5 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.18 | +1.18 | +1.59 | +1 | 5 | c08s805Pr1b_Nb | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), cross_mean(day_corr(Ret, Volume), 3)), 60)` |
| +0.93 | +0.93 | +1.42 | -1 | 20 | c08s805Pr1a_Ea | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_centroid(Volume)))` |
| +0.83 | +0.83 | +3.36 | -1 | 5 | c08s805Pr1a_Ea | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_open_close(Volume))), 30)` |
| +0.54 | +0.54 | +1.92 | -1 | 5 | c08s805Pr2a_Ea | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(Ret, Volume), 60))` |
| +0.53 | +0.53 | +0.53 | -1 | 5 | c07s805M3_I0_open_search | `ts_skew(day_corr(Volume, Vwap), 50)` |

## 共性:473 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.90 | 0.000 | 15 | +0.44 / -1.46 | `pow_2_5(day_centroid(Volume))` |
| +1.87 | 0.000 | 8 | +0.44 / -1.43 | `pow_2_5(pow_2_5(day_centroid(Volume)))` |
| +1.85 | 0.001 | 5 | +0.43 / -1.42 | `pow_1_5(day_centroid(Volume))` |
| +1.72 | 0.000 | 8 | +0.30 / -1.43 | `day_centroid(abs_(Ret))` |
| +1.62 | 0.001 | 7 | +0.20 / -1.42 | `sub(day_centroid(Volume), day_centroid(delete_open_close(Volume)))` |
| +1.55 | 0.000 | 86 | -0.13 / -1.68 | `day_centroid(Volume)` |
| +1.54 | 0.014 | 4 | +0.13 / -1.41 | `day_quantile_q25(Ret)` |
| +1.54 | 0.014 | 4 | +0.13 / -1.41 | `pow_3(day_quantile_q25(Ret))` |
| +1.51 | 0.000 | 9 | +0.09 / -1.43 | `day_centroid(delete_open_close(Volume))` |
| +1.48 | 0.001 | 9 | +0.05 / -1.43 | `cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), ts_max(day_first(High), 1))` |
| +1.45 | 0.020 | 4 | +0.04 / -1.41 | `cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), ts_max(day_first(High), 5))` |
| +1.44 | 0.019 | 4 | +0.03 / -1.41 | `sub(day_centroid(abs_(Ret)), day_centroid(Volume))` |
| +1.30 | 0.000 | 41 | -0.21 / -1.51 | `sub(day_pos_ratio(High), LogFloatShares)` |
| +1.25 | 0.009 | 8 | -0.17 / -1.42 | `ts_max(ts_max(day_first(High), 1), 1)` |
| +1.23 | 0.000 | 58 | -0.32 / -1.55 | `day_pos_ratio(High)` |
| +1.18 | 0.058 | 4 | -0.23 / -1.41 | `sub(day_pos_ratio(High), day_first(High))` |
| +1.04 | 0.010 | 13 | -0.38 / -1.43 | `ts_max(day_first(High), 5)` |
| +1.03 | 0.000 | 33 | -0.44 / -1.47 | `ts_max(day_first(High), 1)` |
| +1.02 | 0.000 | 66 | -0.52 / -1.54 | `day_first(High)` |
| +0.99 | 0.053 | 4 | -0.41 / -1.41 | `sigmoid(day_centroid(Volume))` |

## 拆解(14 次评估)

### head score +0.54:`sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(Ret, Volume), 60))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_min(day_corr(Ret, Ret), 60)` | — | — | — | — | 门槛废品 |
| sufficiency | `cross_mean(day_corr(Ret, Volume), 60)` | +0.10 | +0.10 | +0.56 | — | (子树本身) |
| sufficiency | `day_corr(Ret, Ret)` | — | — | — | — | 门槛废品 |
| sufficiency | `day_corr(Ret, Volume)` | -1.98 | -1.98 | -0.53 | — | (子树本身) |
| knockout | `cross_min(day_corr(Ret, Ret), 60)` | +0.17 | +0.17 | +0.58 | +0.37 | `sub(day_corr(Ret, Ret), cross_mean(day_corr(Ret, Volume), 60))` |
| knockout | `cross_mean(day_corr(Ret, Volume), 60)` | -0.46 | -0.46 | +0.30 | +0.99 | `sub(cross_min(day_corr(Ret, Ret), 60), day_corr(Ret, Volume))` |
| swap | `Volume->Amt` | +0.56 | +0.56 | +1.87 | — | `sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(Ret, Amt), 60))` |
| window | `cross_min@60->30` | +0.46 | +0.46 | +1.73 | — | `sub(cross_min(day_corr(Ret, Ret), 30), cross_mean(day_corr(Ret, Volume), 60))` |
| window | `cross_min@60->120` | +0.87 | +0.87 | +1.73 | — | `sub(cross_min(day_corr(Ret, Ret), 120), cross_mean(day_corr(Ret, Volume), 60))` |

### head score +0.53:`ts_skew(day_corr(Volume, Vwap), 50)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_corr(Volume, Vwap)` | -6.23 | -3.38 | -6.23 | — | (子树本身) |
| swap | `Volume->Amt` | +0.47 | +0.47 | +0.61 | — | `ts_skew(day_corr(Amt, Vwap), 50)` |
| swap | `Vwap->Close` | +0.10 | +0.10 | +0.62 | — | `ts_skew(day_corr(Volume, Close), 50)` |
| window | `ts_skew@50->25` | +0.11 | +0.11 | +0.16 | — | `ts_skew(day_corr(Volume, Vwap), 25)` |
| window | `ts_skew@50->100` | +0.45 | +0.45 | +1.15 | — | `ts_skew(day_corr(Volume, Vwap), 100)` |

## 机械核心卡(B0 按这个顺序取)

1. `pow_2_5(day_centroid(Volume))` — enrichment,均值差 +1.90,p 0.000
2. `pow_2_5(pow_2_5(day_centroid(Volume)))` — enrichment,均值差 +1.87,p 0.000
3. `pow_1_5(day_centroid(Volume))` — enrichment,均值差 +1.85,p 0.001
4. `day_centroid(abs_(Ret))` — enrichment,均值差 +1.72,p 0.000
5. `sub(day_centroid(Volume), day_centroid(delete_open_close(Volume)))` — enrichment,均值差 +1.62,p 0.001
6. `day_centroid(Volume)` — enrichment,均值差 +1.55,p 0.000
7. `day_quantile_q25(Ret)` — enrichment,均值差 +1.54,p 0.014
8. `pow_3(day_quantile_q25(Ret))` — enrichment,均值差 +1.54,p 0.014
9. `day_centroid(delete_open_close(Volume))` — enrichment,均值差 +1.51,p 0.000
10. `cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), ts_max(day_first(High), 1))` — enrichment,均值差 +1.48,p 0.001
11. `cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), ts_max(day_first(High), 5))` — enrichment,均值差 +1.45,p 0.020
12. `sub(day_centroid(abs_(Ret)), day_centroid(Volume))` — enrichment,均值差 +1.44,p 0.019
13. `sub(day_pos_ratio(High), LogFloatShares)` — enrichment,均值差 +1.30,p 0.000
14. `ts_max(ts_max(day_first(High), 1), 1)` — enrichment,均值差 +1.25,p 0.009
15. `day_pos_ratio(High)` — enrichment,均值差 +1.23,p 0.000
16. `sub(day_pos_ratio(High), day_first(High))` — enrichment,均值差 +1.18,p 0.058
17. `ts_max(day_first(High), 5)` — enrichment,均值差 +1.04,p 0.010
18. `ts_max(day_first(High), 1)` — enrichment,均值差 +1.03,p 0.000
19. `day_first(High)` — enrichment,均值差 +1.02,p 0.000
20. `sigmoid(day_centroid(Volume))` — enrichment,均值差 +0.99,p 0.053
21. `cross_mean(day_corr(Ret, Volume), 60)` — enrichment,均值差 +0.59,p 0.061

## 本组之前各轮的任务

- `c08s805Pr1a_Ea`:核心 `day_centroid(Volume)`;评分 89,过线 10,入 heads 2;采样计数 {'c05_no_core': 1123, 'c05_periphery_seen': 4}
  - score +0.93(train +0.93 valid +1.42):`sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_centroid(Volume)))`
  - score +0.93(train +0.93 valid +1.42):`sub(sub(day_centroid(abs_(Ret)), day_centroid(Volume)), day_centroid(Volume))`
  - score +0.83(train +0.83 valid +3.36):`cross_mean(sub(day_centroid(Volume), day_centroid(delete_open_close(Volume))), 30)`
  - score +0.63(train +0.63 valid +0.73):`sub(day_centroid(abs_(Ret)), day_centroid(Volume))`
  - score +0.63(train +0.63 valid +0.73):`pow_05(sub(day_centroid(abs_(Ret)), day_centroid(Volume)))`
- `c08s805Pr1b_Nb`:核心 `—`;评分 83,过线 1,入 heads 1;采样计数 {}
  - score +1.18(train +1.18 valid +1.59):`cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), cross_mean(day_corr(Ret, Volume), 3)), 60)`
  - score +0.43(train +0.43 valid +1.66):`cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 30)), cross_mean(day_corr(Ret, Volume), 30)), 60)`
  - score +0.23(train +0.23 valid +1.48):`ts_quantile_q25(pow_3(day_quantile_q25(Ret)), 20)`
  - score +0.23(train +0.23 valid +1.50):`ts_quantile_q25(pow_3(pow_3(day_quantile_q25(Ret))), 20)`
  - score +0.16(train +0.16 valid +1.37):`ts_quantile_q25(pow_3(pow_3(day_quantile_q25(Ret))), 10)`
- `c08s805Pr2a_Ea`:核心 `day_corr(Ret, Volume)`;评分 72,过线 1,入 heads 1;采样计数 {'c05_no_core': 1236, 'c05_periphery_seen': 6}
  - score +0.54(train +0.54 valid +1.92):`sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(Ret, Volume), 60))`
  - score +0.37(train +0.37 valid +1.54):`sub(cross_min(day_corr(Ret, Ret), 60), cross_mean(day_corr(Ret, Volume), 15))`
  - score +0.24(train +0.24 valid +0.86):`sub(cross_min(cross_mean(day_corr(Ret, Volume), 60), 60), cross_mean(day_corr(Ret, Volume), 60))`
  - score +0.15(train +0.15 valid +1.50):`sub(cross_min(day_corr(Ret, Ret), 60), cross_sum(day_corr(Ret, Volume), 60))`
  - score +0.10(train +0.10 valid +0.56):`sub(cross_min(day_signed_ratio(Open, Ret), 60), cross_mean(day_corr(Ret, Volume), 60))`
- `c08s805Pr2b_Nb`:核心 `—`;评分 62,过线 0,入 heads 0;采样计数 {}
  - score +0.26(train +0.26 valid +1.22):`ts_autocorr_s1(day_first(Amt), 50)`
  - score +0.16(train +0.16 valid +0.52):`ts_autocorr_s1(day_first(Amt), 30)`
  - score +0.06(train +0.06 valid +0.31):`ts_autocorr_s1(cross_zscore(day_first(Amt), 3), 30)`
  - score -0.29(train -0.29 valid +0.25):`ts_autocorr_s1(cross_zscore(day_first(Amt), 30), 10)`
  - score -0.31(train -0.31 valid -0.22):`ts_autocorr_s1(cross_zscore(day_first(Amt), 3), 10)`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.33(window cross_min@60->120):`sub(cross_min(day_corr(Ret, Ret), 120), cross_mean(day_corr(Ret, Volume), 60))`
