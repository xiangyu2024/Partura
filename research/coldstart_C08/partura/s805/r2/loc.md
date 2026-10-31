# 定位:种子 805,P 组,第 2 轮(只含 train / valid)

快照:c07s805M1_I0_open_search, c07s805M2_I0_open_search, c08s805Pr1a_Ea, c08s805Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(3 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.18 | +1.18 | +1.59 | +1 | 5 | c08s805Pr1b_Nb | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), cross_mean(day_corr(Ret, Volume), 3)), 60)` |
| +0.93 | +0.93 | +1.42 | -1 | 20 | c08s805Pr1a_Ea | `sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_centroid(Volume)))` |
| +0.83 | +0.83 | +3.36 | -1 | 5 | c08s805Pr1a_Ea | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_open_close(Volume))), 30)` |

## 共性:311 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.60 | 0.000 | 15 | +0.44 / -1.16 | `pow_2_5(day_centroid(Volume))` |
| +1.56 | 0.000 | 8 | +0.44 / -1.13 | `pow_2_5(pow_2_5(day_centroid(Volume)))` |
| +1.54 | 0.003 | 5 | +0.43 / -1.11 | `pow_1_5(day_centroid(Volume))` |
| +1.42 | 0.000 | 8 | +0.30 / -1.12 | `day_centroid(abs_(Ret))` |
| +1.33 | 0.000 | 86 | -0.13 / -1.45 | `day_centroid(Volume)` |
| +1.32 | 0.001 | 7 | +0.20 / -1.12 | `sub(day_centroid(Volume), day_centroid(delete_open_close(Volume)))` |
| +1.23 | 0.041 | 4 | +0.13 / -1.10 | `day_quantile_q25(Ret)` |
| +1.23 | 0.041 | 4 | +0.13 / -1.10 | `pow_3(day_quantile_q25(Ret))` |
| +1.21 | 0.002 | 9 | +0.09 / -1.12 | `day_centroid(delete_open_close(Volume))` |
| +1.18 | 0.009 | 9 | +0.05 / -1.12 | `cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), ts_max(day_first(High), 1))` |
| +1.14 | 0.057 | 4 | +0.04 / -1.10 | `cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), ts_max(day_first(High), 5))` |
| +1.13 | 0.025 | 4 | +0.03 / -1.10 | `sub(day_centroid(abs_(Ret)), day_centroid(Volume))` |
| +1.01 | 0.000 | 41 | -0.21 / -1.22 | `sub(day_pos_ratio(High), LogFloatShares)` |
| +0.94 | 0.046 | 8 | -0.17 / -1.11 | `ts_max(ts_max(day_first(High), 1), 1)` |
| +0.94 | 0.000 | 58 | -0.32 / -1.26 | `day_pos_ratio(High)` |
| +0.87 | 0.132 | 4 | -0.23 / -1.10 | `sub(day_pos_ratio(High), day_first(High))` |
| +0.77 | 0.123 | 7 | -0.34 / -1.10 | `day_corr(Ret, Volume)` |
| +0.74 | 0.066 | 13 | -0.38 / -1.12 | `ts_max(day_first(High), 5)` |
| +0.72 | 0.010 | 33 | -0.44 / -1.16 | `ts_max(day_first(High), 1)` |
| +0.72 | 0.002 | 66 | -0.52 / -1.24 | `day_first(High)` |

## 拆解(21 次评估)

### head score +1.18:`cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), cross_mean(day_corr(Ret, Volume), 3)), 60)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cross_mean(day_corr(Ret, Volume), 3)` | -1.22 | -1.22 | +0.31 | — | (子树本身) |
| sufficiency | `day_corr(Ret, Volume)` | -1.98 | -1.98 | -0.53 | — | (子树本身) |
| knockout | `add(add(5, cross_mean(day_corr(Ret, Volume), 3)), cross_mean(day_corr(Ret, Volume), 3))` | +1.18 | +1.18 | +1.59 | -0.00 | `cross_max(cross_mean(day_corr(Ret, Volume), 3), 60)` |
| knockout | `add(5, cross_mean(day_corr(Ret, Volume), 3))` | +1.18 | +1.18 | +1.59 | -0.00 | `cross_max(add(cross_mean(day_corr(Ret, Volume), 3), cross_mean(day_corr(Ret, Volume), 3)), 60)` |
| knockout | `cross_mean(day_corr(Ret, Volume), 3)` | +0.54 | +0.54 | +1.36 | +0.64 | `cross_max(add(add(5, day_corr(Ret, Volume)), cross_mean(day_corr(Ret, Volume), 3)), 60)` |
| knockout | `cross_mean(day_corr(Ret, Volume), 3)` | +0.54 | +0.54 | +1.36 | +0.64 | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), day_corr(Ret, Volume)), 60)` |
| swap | `Volume->Amt` | +1.16 | +1.16 | +1.48 | — | `cross_max(add(add(5, cross_mean(day_corr(Ret, Amt), 3)), cross_mean(day_corr(Ret, Amt), 3)), 60)` |
| window | `cross_max@60->30` | +0.79 | +0.79 | +1.38 | — | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), cross_mean(day_corr(Ret, Volume), 3)), 30)` |
| window | `cross_max@60->120` | +1.00 | +1.00 | +1.99 | — | `cross_max(add(add(5, cross_mean(day_corr(Ret, Volume), 3)), cross_mean(day_corr(Ret, Volume), 3)), 120)` |

### head score +0.93:`sub(day_centroid(Volume), sub(day_centroid(abs_(Ret)), day_centroid(Volume)))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(day_centroid(abs_(Ret)), day_centroid(Volume))` | +0.63 | +0.63 | +0.73 | — | (子树本身) |
| sufficiency | `day_centroid(abs_(Ret))` | -2.89 | -1.77 | -2.89 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `sub(day_centroid(abs_(Ret)), day_centroid(Volume))` | +0.63 | +0.63 | +0.73 | +0.29 | `sub(day_centroid(Volume), day_centroid(abs_(Ret)))` |
| swap | `Volume->Amt` | +0.88 | +0.88 | +1.43 | — | `sub(day_centroid(Amt), sub(day_centroid(abs_(Ret)), day_centroid(Amt)))` |

### head score +0.83:`cross_mean(sub(day_centroid(Volume), day_centroid(delete_open_close(Volume))), 30)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sub(day_centroid(Volume), day_centroid(delete_open_close(Volume)))` | -0.30 | -0.30 | +2.38 | — | (子树本身) |
| sufficiency | `day_centroid(delete_open_close(Volume))` | -0.17 | +1.12 | -0.17 | — | (子树本身) |
| sufficiency | `day_centroid(Volume)` | +0.44 | +1.09 | +0.44 | — | (子树本身) |
| knockout | `sub(day_centroid(Volume), day_centroid(delete_open_close(Volume)))` | +1.73 | +1.73 | +1.88 | -0.91 | `cross_mean(day_centroid(Volume), 30)` |
| swap | `Volume->Amt` | +0.85 | +0.85 | +3.35 | — | `cross_mean(sub(day_centroid(Amt), day_centroid(delete_open_close(Amt))), 30)` |
| window | `cross_mean@30->15` | +0.66 | +0.66 | +3.26 | — | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_open_close(Volume))), 15)` |
| window | `cross_mean@30->60` | +0.56 | +0.56 | +2.69 | — | `cross_mean(sub(day_centroid(Volume), day_centroid(delete_open_close(Volume))), 60)` |

## 机械核心卡(B0 按这个顺序取)

1. `sub(day_centroid(abs_(Ret)), day_centroid(Volume))` — ablation,自身 score +0.63(所在 head +0.93)
2. `pow_2_5(day_centroid(Volume))` — enrichment,均值差 +1.60,p 0.000
3. `pow_2_5(pow_2_5(day_centroid(Volume)))` — enrichment,均值差 +1.56,p 0.000
4. `pow_1_5(day_centroid(Volume))` — enrichment,均值差 +1.54,p 0.003
5. `day_centroid(abs_(Ret))` — enrichment,均值差 +1.42,p 0.000
6. `day_centroid(Volume)` — enrichment,均值差 +1.33,p 0.000
7. `sub(day_centroid(Volume), day_centroid(delete_open_close(Volume)))` — enrichment,均值差 +1.32,p 0.001
8. `day_quantile_q25(Ret)` — enrichment,均值差 +1.23,p 0.041
9. `pow_3(day_quantile_q25(Ret))` — enrichment,均值差 +1.23,p 0.041
10. `day_centroid(delete_open_close(Volume))` — enrichment,均值差 +1.21,p 0.002
11. `cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), ts_max(day_first(High), 1))` — enrichment,均值差 +1.18,p 0.009
12. `cs_last_low20(sub(day_pos_ratio(High), LogFloatShares), ts_max(day_first(High), 5))` — enrichment,均值差 +1.14,p 0.057
13. `sub(day_pos_ratio(High), LogFloatShares)` — enrichment,均值差 +1.01,p 0.000
14. `ts_max(ts_max(day_first(High), 1), 1)` — enrichment,均值差 +0.94,p 0.046
15. `day_pos_ratio(High)` — enrichment,均值差 +0.94,p 0.000
16. `ts_max(day_first(High), 5)` — enrichment,均值差 +0.74,p 0.066
17. `ts_max(day_first(High), 1)` — enrichment,均值差 +0.72,p 0.010
18. `day_first(High)` — enrichment,均值差 +0.72,p 0.002
19. `sigmoid(day_centroid(Volume))` — enrichment,均值差 +0.68,p 0.084

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

## 比原 head 好的拆解变体(R 候选)

(没有)
