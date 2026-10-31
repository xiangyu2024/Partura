# 定位:种子 803,P 组,第 2 轮(只含 train / valid)

快照:c07s803M1_I0_open_search, c07s803M2_I0_open_search, c08s803Pr1a_Na, c08s803Pr1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(1 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +0.56 | +0.97 | +0.56 | -1 | 20 | c08s803Pr1b_Nb | `neg(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))` |

## 共性:258 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +1.70 | 0.002 | 4 | +0.16 / -1.54 | `day_quantile_q25(Ret)` |
| +1.64 | 0.003 | 4 | +0.10 / -1.54 | `cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))` |
| +1.59 | 0.000 | 9 | +0.02 / -1.57 | `neg(day_centroid(Amt))` |
| +1.57 | 0.000 | 12 | -0.02 / -1.59 | `day_centroid(Amt)` |
| +1.48 | 0.008 | 4 | -0.06 / -1.54 | `day_corr(Ret, Volume)` |
| +1.47 | 0.016 | 4 | -0.07 / -1.54 | `cs_last_low40(cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open)), day_quantile_q25(Open))` |
| +1.27 | 0.007 | 7 | -0.28 / -1.55 | `day_wmean(Vwap, Vwap)` |
| +1.21 | 0.026 | 4 | -0.32 / -1.53 | `cs_last_low40(day_quantile_q25(Open), day_var(Low))` |
| +1.07 | 0.062 | 4 | -0.46 / -1.53 | `day_quantile(Open)` |
| +1.04 | 0.087 | 4 | -0.49 / -1.53 | `cs_scale(day_wmean(Vwap, Vwap))` |
| +0.99 | 0.022 | 11 | -0.57 / -1.56 | `cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open))` |
| +0.87 | 0.001 | 19 | -0.71 / -1.58 | `day_product(Ret)` |
| +0.82 | 0.003 | 30 | -0.79 / -1.61 | `day_quantile_q25(Open)` |
| +0.82 | 0.007 | 20 | -0.76 / -1.58 | `day_var(Low)` |
| +0.70 | 0.125 | 5 | -0.83 / -1.53 | `day_skew(mul(Ret, Amt))` |
| +0.63 | 0.032 | 12 | -0.91 / -1.54 | `cross_regres(ts_kurt(day_q_stat_std(High), 5), day_product(Ret), 15)` |
| +0.56 | 0.038 | 15 | -0.99 / -1.55 | `day_kurt(Ret)` |
| +0.45 | 0.292 | 8 | -1.08 / -1.53 | `day_max(Ret)` |
| +0.20 | 0.536 | 4 | -1.32 / -1.52 | `day_min(Ret)` |
| +0.18 | 0.605 | 4 | -1.34 / -1.52 | `inv(cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open)))` |

## 拆解(6 次评估)

### head score +0.56:`neg(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt)))))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))` | +0.56 | +0.97 | +0.56 | — | (子树本身) |
| sufficiency | `neg(day_centroid(Amt))` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| sufficiency | `day_centroid(Amt)` | +0.41 | +1.05 | +0.41 | — | (子树本身) |
| knockout | `mul(5, neg(day_centroid(Amt)))` | +0.56 | +0.97 | +0.56 | +0.00 | `neg(cs_mask_top_replace_mean(neg(day_centroid(Amt))))` |
| knockout | `neg(day_centroid(Amt))` | -0.37 | +1.01 | -0.37 | +0.93 | `neg(cs_mask_top_replace_mean(mul(5, day_centroid(Amt))))` |
| swap | `Amt->Volume` | +0.51 | +1.02 | +0.51 | — | `neg(cs_mask_top_replace_mean(mul(5, neg(day_centroid(Volume)))))` |

## 机械核心卡(B0 按这个顺序取)

1. `cs_mask_top_replace_mean(mul(5, neg(day_centroid(Amt))))` — ablation,自身 score +0.56(所在 head +0.56)
2. `day_quantile_q25(Ret)` — enrichment,均值差 +1.70,p 0.002
3. `neg(day_centroid(Amt))` — enrichment,均值差 +1.59,p 0.000
4. `day_centroid(Amt)` — enrichment,均值差 +1.57,p 0.000
5. `day_corr(Ret, Volume)` — enrichment,均值差 +1.48,p 0.008
6. `cs_last_low40(cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open)), day_quantile_q25(Open))` — enrichment,均值差 +1.47,p 0.016
7. `day_wmean(Vwap, Vwap)` — enrichment,均值差 +1.27,p 0.007
8. `cs_last_low40(day_quantile_q25(Open), day_var(Low))` — enrichment,均值差 +1.21,p 0.026
9. `day_quantile(Open)` — enrichment,均值差 +1.07,p 0.062
10. `cs_scale(day_wmean(Vwap, Vwap))` — enrichment,均值差 +1.04,p 0.087
11. `cs_last_low40(day_quantile_q25(Open), day_quantile_q25(Open))` — enrichment,均值差 +0.99,p 0.022
12. `day_product(Ret)` — enrichment,均值差 +0.87,p 0.001
13. `day_quantile_q25(Open)` — enrichment,均值差 +0.82,p 0.003
14. `day_var(Low)` — enrichment,均值差 +0.82,p 0.007
15. `cross_regres(ts_kurt(day_q_stat_std(High), 5), day_product(Ret), 15)` — enrichment,均值差 +0.63,p 0.032
16. `day_kurt(Ret)` — enrichment,均值差 +0.56,p 0.038

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

## 比原 head 好的拆解变体(R 候选)

(没有)
