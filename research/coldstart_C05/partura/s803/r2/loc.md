# 定位:种子 803,B 组,第 2 轮(只含 train / valid)

快照:c05s803M1_I0_open_search, c05s803M2_I0_open_search, c05s803Br1a_Ea, c05s803Br1b_Nb;已生效的 R 替换 0 个。score = train 与 valid 残差纯多头书净夏普中较差的(≥ 0.5 为发现)。

## heads(6 个)

| score | train | valid | 方向 | 半衰期 | 来源 | 表达式 |
|---|---|---|---|---|---|---|
| +1.56 | +1.56 | +2.07 | -1 | 20 | c05s803M2_I0_open_search | `cross_autocorr_s1(ts_skew(ts_skew(day_durbin_watson(Open), 50), 50), 3)` |
| +1.23 | +1.23 | +2.29 | -1 | 5 | c05s803M2_I0_open_search | `ts_skew(day_durbin_watson(Open), 50)` |
| +0.97 | +0.97 | +1.54 | -1 | 20 | c05s803M1_I0_open_search | `day_kurt(Ret)` |
| +0.90 | +0.90 | +1.05 | -1 | 20 | c05s803Br1b_Nb | `sub(day_centroid(Amt), day_centroid(Ret))` |
| +0.73 | +0.73 | +2.30 | +1 | 5 | c05s803Br1a_Ea | `cross_corr(day_kurt(Ret), day_gini(Ret), 241)` |
| +0.53 | +0.53 | +0.78 | -1 | 20 | c05s803Br1b_Nb | `sub(day_centroid(Amt), LogFloatShares)` |

## 共性:210 个已评分候选里的子树(按均值差排,前 20)

| 均值差 | p | 含它的候选数 | 含 / 不含 | 子树 |
|---|---|---|---|---|
| +2.35 | 0.000 | 11 | +0.65 / -1.70 | `ts_skew(day_durbin_watson(Open), 50)` |
| +2.10 | 0.005 | 4 | +0.48 / -1.62 | `neg(LogFloatShares)` |
| +1.98 | 0.000 | 25 | +0.16 / -1.81 | `day_durbin_watson(Open)` |
| +1.91 | 0.010 | 5 | +0.28 / -1.62 | `ts_skew(day_durbin_watson(Open), 40)` |
| +1.33 | 0.009 | 10 | -0.32 / -1.64 | `day_centroid(Amt)` |
| +0.67 | 0.118 | 10 | -0.94 / -1.61 | `day_centroid(Ret)` |
| -0.00 | 0.412 | 5 | -1.58 / -1.58 | `day_gini(Amt)` |
| -0.37 | 0.597 | 4 | -1.94 / -1.57 | `cross_fangzheng(day_kurt(Ret), 15)` |
| -0.42 | 0.629 | 4 | -1.99 / -1.57 | `day_kurt(Amt)` |
| -0.68 | 0.812 | 4 | -2.25 / -1.57 | `day_sum(Amt)` |
| -0.83 | 0.995 | 55 | -2.19 / -1.36 | `day_kurt(Ret)` |
| -1.64 | 0.996 | 10 | -3.14 / -1.50 | `day_argmin(High)` |
| -2.41 | 0.998 | 5 | -3.93 / -1.52 | `div(day_argmin(High), day_kurt(Ret))` |

## 拆解(18 次评估)

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

### head score +0.90:`sub(day_centroid(Amt), day_centroid(Ret))`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_centroid(Amt)` | -0.08 | -0.08 | +0.58 | — | (子树本身) |
| sufficiency | `day_centroid(Ret)` | -1.38 | -1.38 | -0.48 | — | (子树本身) |
| swap | `Amt->Volume` | +0.88 | +0.88 | +1.05 | — | `sub(day_centroid(Volume), day_centroid(Ret))` |

### head score +0.73:`cross_corr(day_kurt(Ret), day_gini(Ret), 241)`

| 类型 | 改了什么 | score | train | valid | 必要性 | 变体 |
|---|---|---|---|---|---|---|
| sufficiency | `day_kurt(Ret)` | +0.97 | +0.97 | +1.54 | — | (子树本身) |
| sufficiency | `day_gini(Ret)` | -0.27 | -0.27 | +0.23 | — | (子树本身) |
| window | `cross_corr@241->120` | -0.23 | -0.23 | +2.30 | — | `cross_corr(day_kurt(Ret), day_gini(Ret), 120)` |
| window | `cross_corr@241->482` | -1.14 | -0.26 | -1.14 | — | `cross_corr(day_kurt(Ret), day_gini(Ret), 482)` |

## 机械核心卡(B0 按这个顺序取)

1. `ts_skew(day_durbin_watson(Open), 50)` — ablation,自身 score +1.18(所在 head +1.56)
2. `day_kurt(Ret)` — ablation,自身 score +0.97(所在 head +0.73)
3. `neg(LogFloatShares)` — enrichment,均值差 +2.10,p 0.005
4. `day_durbin_watson(Open)` — enrichment,均值差 +1.98,p 0.000
5. `ts_skew(day_durbin_watson(Open), 40)` — enrichment,均值差 +1.91,p 0.010
6. `day_centroid(Amt)` — enrichment,均值差 +1.33,p 0.009

## 本组之前各轮的任务

- `c05s803Br1a_Ea`:核心 `day_kurt(Ret)`;评分 80,过线 1,入 heads 1;采样计数 {'c05_no_core': 1322, 'c05_skeleton': 30}
  - score +0.73(train +0.73 valid +2.30):`cross_corr(day_kurt(Ret), day_gini(Ret), 241)`
  - score -0.03(train -0.03 valid +1.50):`div(cross_fangzheng(day_kurt(Ret), 3), day_kurt(Ret))`
  - score -0.04(train +0.35 valid -0.04):`div(day_argmin(High), cross_corr(day_kurt(Ret), day_gini(Close), 20))`
  - score -0.14(train +0.20 valid -0.14):`cross_fangzheng(cross_fangzheng(cross_fangzheng(day_kurt(Ret), 15), 30), 15)`
  - score -0.16(train -0.16 valid +0.95):`div(day_argmin(Ret), day_kurt(Ret))`
- `c05s803Br1b_Nb`:核心 `—`;评分 65,过线 6,入 heads 2;采样计数 {}
  - score +0.90(train +0.90 valid +1.05):`sub(day_centroid(Amt), day_centroid(Ret))`
  - score +0.90(train +0.90 valid +1.05):`neg(sub(day_centroid(Amt), day_centroid(Ret)))`
  - score +0.90(train +0.90 valid +1.05):`neg(neg(sub(day_centroid(Amt), day_centroid(Ret))))`
  - score +0.53(train +0.53 valid +0.78):`sub(day_centroid(Amt), LogFloatShares)`
  - score +0.52(train +0.52 valid +0.84):`sub(neg(LogFloatShares), day_centroid(Ret))`

## 比原 head 好的拆解变体(R 候选)

- 增益 +0.21(swap Open->Close):`ts_skew(day_durbin_watson(Close), 50)`
