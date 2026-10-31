# 定位:种子 803,P 组,第 3 轮(只含 train / valid)

快照:c07s803M1_I0_open_search, c07s803M2_I0_open_search, c07s803M3_I0_open_search, c08s803Pr1a_Na, c08s803Pr1b_Nb, c08s803Pr2a_Ea, c08s803Pr2b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(2 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.34 | +1.76 | +1.34 | -1 | 5 | c08s803Pr2a_Ea | `cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)))), 15)` |
| +0.56 | +0.97 | +0.56 | -1 | 20 | c08s803Pr1b_Nb | `neg(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))` |

## 共性:461 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.54 | 0.000 | 17 | +1.15 / -1.39 | `sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))` |
| +2.53 | 0.000 | 7 | +1.20 / -1.33 | `ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)` |
| +2.50 | 0.000 | 6 | +1.17 / -1.32 | `cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)))` |
| +2.19 | 0.001 | 4 | +0.88 / -1.31 | `neg(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))))` |
| +2.19 | 0.001 | 4 | +0.88 / -1.31 | `cs_mask_top_replace_mean(mul(5, neg(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))))))` |
| +2.16 | 0.001 | 4 | +0.85 / -1.31 | `ts_decay_linear(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))), 5)` |
| +1.64 | 0.000 | 62 | +0.12 / -1.51 | `neg(day_centroid(Amt))` |
| +1.63 | 0.000 | 65 | +0.11 / -1.52 | `day_centroid(Amt)` |
| +1.63 | 0.000 | 57 | +0.14 / -1.49 | `cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))` |
| +1.63 | 0.006 | 4 | +0.33 / -1.31 | `neg(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))` |
| +1.46 | 0.007 | 4 | +0.16 / -1.30 | `day_quantile_q25(Ret)` |
| +1.24 | 0.017 | 4 | -0.06 / -1.30 | `day_corr(Ret, Volume)` |
| +1.23 | 0.032 | 4 | -0.07 / -1.30 | `cs_last_low40(cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open)), day_quantile_q25(Open))` |
| +1.03 | 0.021 | 7 | -0.28 / -1.31 | `day_wmean(Vwap, Vwap)` |
| +0.98 | 0.047 | 4 | -0.32 / -1.30 | `cs_last_low40(day_quantile_q25(Open), day_var(Low))` |
| +0.84 | 0.122 | 4 | -0.46 / -1.30 | `day_quantile(Open)` |
| +0.81 | 0.146 | 4 | -0.49 / -1.30 | `cs_scale(day_wmean(Vwap, Vwap))` |
| +0.74 | 0.067 | 11 | -0.57 / -1.31 | `cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open))` |
| +0.73 | 0.012 | 14 | -0.59 / -1.31 | `cs_rank(cross_argmax(cs_rank(day_zero_ratio(Open)), 241))` |
| +0.69 | 0.094 | 5 | -0.61 / -1.30 | `sub(cross_mean(day_hurst(Ret), 10), cross_mean(day_hurst(Ret), 60))` |

## 拆解(11 次评估)

### head score +1.34:`cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)))), 15)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5))))` | +1.05 | +1.57 | +1.05 | — | (子树本身) |
| sufficiency | `cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)))` | +1.05 | +1.57 | +1.05 | — | (子树本身) |
| sufficiency | `ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)` | +1.25 | +1.40 | +1.25 | — | (子树本身) |
| sufficiency | `sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))` | +0.56 | +0.97 | +0.56 | — | (子树本身) |
| knockout | `sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5))))` | +1.36 | +1.74 | +1.36 | -0.01 | `cross_mean(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5))), 15)` |
| knockout | `mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5))` | +1.34 | +1.76 | +1.34 | +0.00 | `cross_mean(sqrt(cs_mask_top_replace_mean(ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5))), 15)` |
| knockout | `ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)` | +1.03 | +1.67 | +1.03 | +0.31 | `cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))))), 15)` |
| knockout | `sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))` | +1.02 | +1.02 | +2.35 | +0.32 | `cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))), 5)))), 15)` |
| swap | `Amt->Volume` | +1.35 | +1.70 | +1.35 | — | `cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Volume))))), 5)))), 15)` |
| window | `cross_mean@15->7` | +1.27 | +1.40 | +1.27 | — | `cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)))), 7)` |
| window | `cross_mean@15->30` | +1.16 | +1.78 | +1.16 | — | `cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)))), 30)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)` — ablation,自身 score +1.25(所在 head +1.34)
2. `cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)))` — ablation,自身 score +1.05(所在 head +1.34)
3. `sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5))))` — ablation,自身 score +1.05(所在 head +1.34)
4. `sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))` — enrichment,均值差 +2.54,p 0.000
5. `neg(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))))` — enrichment,均值差 +2.19,p 0.001
6. `cs_mask_top_replace_mean(mul(5, neg(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))))))` — enrichment,均值差 +2.19,p 0.001
7. `ts_decay_linear(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))), 5)` — enrichment,均值差 +2.16,p 0.001
8. `neg(day_centroid(Amt))` — enrichment,均值差 +1.64,p 0.000
9. `day_centroid(Amt)` — enrichment,均值差 +1.63,p 0.000
10. `cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))` — enrichment,均值差 +1.63,p 0.000
11. `neg(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))` — enrichment,均值差 +1.63,p 0.006
12. `day_quantile_q25(Ret)` — enrichment,均值差 +1.46,p 0.007
13. `day_corr(Ret, Volume)` — enrichment,均值差 +1.24,p 0.017
14. `cs_last_low40(cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open)), day_quantile_q25(Open))` — enrichment,均值差 +1.23,p 0.032
15. `day_wmean(Vwap, Vwap)` — enrichment,均值差 +1.03,p 0.021
16. `cs_last_low40(day_quantile_q25(Open), day_var(Low))` — enrichment,均值差 +0.98,p 0.047
17. `cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open))` — enrichment,均值差 +0.74,p 0.067
18. `cs_rank(cross_argmax(cs_rank(day_zero_ratio(Open)), 241))` — enrichment,均值差 +0.73,p 0.012
19. `sub(cross_mean(day_hurst(Ret), 10), cross_mean(day_hurst(Ret), 60))` — enrichment,均值差 +0.69,p 0.094
20. `day_zero_ratio(Amt)` — enrichment,均值差 +0.69,p 0.001
21. `day_product(Ret)` — enrichment,均值差 +0.61,p 0.006
22. `cross_argmax(cs_rank(cross_argmax(cs_rank(day_zero_ratio(Open)), 241)), 241)` — enrichment,均值差 +0.55,p 0.073
23. `day_var(Low)` — enrichment,均值差 +0.55,p 0.035
24. `day_quantile_q25(Open)` — enrichment,均值差 +0.54,p 0.028
25. `day_zero_ratio(Open)` — enrichment,均值差 +0.51,p 0.017
26. `cs_rank(day_zero_ratio(Open))` — enrichment,均值差 +0.46,p 0.039
27. `cross_argmax(cs_rank(day_zero_ratio(Open)), 241)` — enrichment,均值差 +0.45,p 0.070
28. `cross_regres(ts_kurt(day_q_stat_std(High), 5), day_product(Ret), 15)` — enrichment,均值差 +0.39,p 0.072
29. `cross_mean(day_hurst(Ret), 10)` — enrichment,均值差 +0.39,p 0.081

## 本组之前各轮的任务

- `c08s803Pr1a_Na`:核心 `—`;评分 71,过线 0,入 heads 0;采样计数 {}
  - score -0.14(train -0.14 valid +0.50):`cross_mean(day_kurt(Ret), 60)`
  - score -0.19(train -0.19 valid +0.55):`day_kurt(Ret)`
  - score -0.23(train -0.23 valid +0.69):`cross_mean(day_kurt(Ret), 5)`
  - score -0.25(train -0.25 valid +0.72):`cross_mean(day_kurt(Ret), 3)`
  - score -0.27(train -0.27 valid +0.97):`cross_mean(div(day_max(Ret), day_kurt(Ret)), 20)`
- `c08s803Pr1b_Nb`:核心 `—`;评分 72,过线 2,入 heads 1;采样计数 {}
  - score +0.56(train +0.97 valid +0.56):`neg(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))`
  - score +0.56(train +0.97 valid +0.56):`cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))`
  - score +0.44(train +1.10 valid +0.44):`day_centroid(Volume)`
  - score +0.44(train +1.09 valid +0.44):`neg(day_centroid(Volume))`
  - score +0.41(train +1.05 valid +0.41):`day_centroid(Amt)`
- `c08s803Pr2a_Ea`:核心 `cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))`;评分 88,过线 34,入 heads 1;采样计数 {'c05_no_core': 1817, 'mutation_refused': 6, 'c05_periphery_seen': 2}
  - score +1.34(train +1.76 valid +1.34):`cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)))), 15)`
  - score +1.34(train +1.34 valid +1.34):`ts_decay_linear(ts_decay_linear(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5), 5)`
  - score +1.33(train +1.45 valid +1.33):`ts_decay_linear(sqrt(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))), 5)`
  - score +1.29(train +1.43 valid +1.29):`cross_mean(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)`
  - score +1.29(train +1.43 valid +1.29):`ts_mean(sqrt(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))), 5)`
- `c08s803Pr2b_Nb`:核心 `—`;评分 92,过线 0,入 heads 0;采样计数 {}
  - score +0.09(train +0.09 valid +1.27):`cs_bucket_demean(sub(cross_mean(day_hurst(Ret), 10), cross_mean(pow_3(cross_mean(day_hurst(Ret), 10)), 60)), div(day_sum(Amt), day_sum(Volume)))`
  - score +0.01(train +0.01 valid +1.61):`cs_bucket_demean(sub(cross_mean(day_hurst(Ret), 10), cross_mean(cross_mean(pow_3(cs_last_high20(day_close(Ret), LimitWidth)), 60), 60)), div(day_sum(Amt), day_sum(Volume)))`
  - score -0.09(train -0.09 valid +1.67):`cs_bucket_demean(sub(cross_mean(day_hurst(Ret), 10), cross_mean(pow_3(cross_mean(day_hurst(Ret), 10)), 60)), cross_mean(day_hurst(Ret), 60))`
  - score -0.12(train -0.12 valid +0.55):`cs_bucket_demean(sub(cross_mean(day_hurst(Ret), 10), cross_mean(pow_3(cs_last_high20(day_close(Ret), LimitWidth)), 60)), div(day_sum(Amt), day_sum(Volume)))`
  - score -0.12(train -0.12 valid +0.97):`sub(cross_mean(day_hurst(Ret), 10), cross_mean(cross_mean(day_hurst(Ret), 60), 60))`

## 比原 head 好的拆解变体(R 候选)

(没有)
