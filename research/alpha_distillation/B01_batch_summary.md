# B01 批量研究总表(批量扫描 → 市场解剖 → 综合 → 第二批假设 → 按写死规则读测试段)

口径同用户的表:训练 20180102–20230807,测试 20230808–20251231;前 10% 纯多头书减有信号有标签股票的等权,扣 15bp;
方向与半衰期在用户训练段上定(半衰期按纯多头书选)。候选**只用 train / valid 按写死的规则选出**,再读测试段:
本因子自己的候选 = 各类变体里用户训练段纯多头夏普最高、过门槛(cov ≥ 0.95、dist ≥ 0.5)、train 与 valid 多头腿都为正的,取最好的 3 类各 1 个;
建在已知族上的候选(叠加 / 筛子)单列。测试段的噪声约为净超额 ±3 个点、夏普 ±0.3。


## 0. 最值得看的(两张榜都**按用户训练段的纯多头夏普排序**,没有用测试段挑)

对照:已知成交额族 `cross_mean(day_std(Amt), 30)` 训练 / 测试 +15.4% / +14.1%,纯多头夏普 +2.22 / +1.51,测试段最大回撤 -14.6%。

### A. 与已知成交额族相关低于 0.5 的(独立的新东西)

这些可以和已知族并列持有。测试段上单个数字有 ±3 个点 / ±0.3 夏普的噪声,而且一共读了约一百个候选,榜首的数字有向上的选择偏差 —— 看逐年是否稳定比看单个数字可靠。

| 来自 | 表达式 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 训练 / 测试 | 日换手 | 测试段最大回撤 | ρ已知族 | 逐年 2018…2025 |
|---|---|---|---|---|---|---|---|---|
| F107 #613 | `add(cs_rank(cross_ema(abs_(cs_demean(day_std(Ret))), 30)), mul(cs_rank(cross_ema(abs_(cs_demean(day_gini(Low)…` | 1 | **+13.6% / +12.5%** | +3.74 / +2.39 | 4.2% | -8.0% | +0.29 | +14% +20% +20% +9% +8% +10% +7% +17% |
| F113 #1375 | `cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30))` | 20 | **+11.2% / +6.0%** | +3.21 / +1.26 | 1.8% | -5.1% | +0.06 | +5% +9% +11% +12% +18% +10% +6% +6% |
| F102 #3961 | `cs_bucket_rank(cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 60), cross_age(day_last(Close)))` | 5 | **+10.7% / +5.8%** | +2.93 / +1.24 | 2.7% | -4.3% | +0.24 | +8% +12% +11% +13% +11% +9% +7% +3% |
| F101 day_shine_retstd | `add(cs_rank(abs_(cs_demean(day_std(in_slice(Ret, 2, 237))))), cs_rank(abs_(cs_demean(day_std(in_pct(in_slice(…` | 60 | **+10.8% / +11.7%** | +2.91 / +2.55 | 2.7% | -3.2% | +0.48 | +10% +15% +8% +13% +7% +10% +10% +14% |
| F105 #25 | `cs_last_high20(neg(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)), cross_max(day_zero_r…` | 5 | **+13.6% / +10.1%** | +2.77 / +1.20 | 6.1% | -14.6% | +0.38 | +16% +12% +6% +12% +23% +16% +5% +11% |
| F111 #953 | `cs_last_high20(ts_pearson(day_last(Close), 20), cross_max(day_zero_ratio(Ret), 15))` | 10 | **+15.2% / +8.0%** | +2.75 / +1.08 | 4.7% | -10.0% | +0.14 | +21% +14% +7% +15% +16% +14% +8% +8% |
| F101 day_shine_retstd | `abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Amt, 2, 237), in_delay(in_slice(Volume, 2, 237),…` | 20 | **+9.7% / +7.2%** | +2.68 / +1.60 | 5.2% | -4.7% | +0.16 | +4% +13% +13% +9% +9% +8% +11% +3% |
| F114 #1421 | `cs_last_high20(neg(cross_ema(cross_quantile_q25(day_close(Ret), 60), 30)), cross_max(day_zero_ratio(Ret), 15))` | 5 | **+9.2% / +3.7%** | +2.44 / +0.68 | 2.5% | -10.2% | +0.03 | +8% +8% +5% +13% +12% +8% +7% -1% |
| F111 #953 | `cs_last_high20(ts_spearman(day_quantile(Close), 10), cross_max(day_zero_ratio(Ret), 15))` | 20 | **+13.3% / +7.8%** | +2.41 / +1.07 | 4.3% | -8.9% | +0.12 | +16% +13% +4% +16% +12% +13% +12% +5% |
| F102 #3961 | `cross_mean(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | 5 | **+10.2% / +3.2%** | +2.32 / +0.59 | 5.3% | -6.5% | +0.27 | +10% +12% +10% +8% +11% +9% +1% +3% |
| F103 #820 | `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_semistd_neg(Amt, 30))), 1)), 5)` | 40 | **+12.4% / +10.3%** | +2.29 / +1.41 | 1.5% | -9.1% | +0.58 | +8% +10% +9% +9% +25% +16% +3% +13% |
| F111 #953 | `ts_spearman(day_close(Close), 10)` | 20 | **+13.2% / +6.8%** | +2.29 / +0.95 | 4.0% | -8.9% | +0.40 | +19% +8% +2% +15% +17% +14% +9% +5% |

### B. 建在已知族上的、或实质落在这一族里的(已知族的升级版)

筛子 = 已知族剔掉某类票;分段 = 只在低流动性 40% 里按本因子选;叠加 = 已知族的秩加上本因子的秩。它们和已知族高度相关,是替换而不是并列。

| 来自 | 表达式 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 训练 / 测试 | 日换手 | 测试段最大回撤 | ρ已知族 | 逐年 2018…2025 |
|---|---|---|---|---|---|---|---|---|
| F114 #1421 | `sub(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))), pow_3(cs_…` | 2 | **+19.5% / +14.7%** | +3.48 / +1.95 | 3.5% | -11.1% | +0.51 | +21% +17% +13% +20% +27% +21% +12% +14% |
| F114 #1421 | `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))), mul(cs_ra…` | 3 | **+19.3% / +13.7%** | +3.43 / +1.87 | 4.4% | -10.7% | +0.58 | +19% +16% +12% +22% +27% +21% +10% +13% |
| F107 #613 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15)), abs_(cs…` | 10 | **+18.4% / +15.0%** | +3.41 / +1.64 | 4.8% | -17.0% | +0.57 | +20% +18% +14% +18% +21% +22% +8% +18% |
| F107 #613 | `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(add(cs_rank(cross_ema(abs_(cs_demean(day_std(Ret))), 3…` | 0 | **+20.4% / +16.1%** | +3.35 / +1.75 | 4.0% | -16.4% | +0.93 | +26% +17% +13% +22% +24% +23% +8% +20% |
| F101 day_shine_retstd | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15)), abs_(cs…` | 10 | **+17.9% / +16.0%** | +3.34 / +1.70 | 4.4% | -17.3% | +0.54 | +19% +16% +13% +17% +23% +21% +10% +18% |
| F103 #820 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15)), cross_m…` | 3 | **+19.6% / +15.3%** | +3.34 / +1.63 | 3.3% | -15.0% | +0.72 | +26% +15% +13% +17% +26% +21% +12% +15% |
| F101 day_shine_retstd | `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))), cs_rank(n…` | 20 | **+16.8% / +17.9%** | +3.32 / +1.90 | 3.3% | -15.8% | +0.54 | +19% +15% +14% +16% +22% +19% +11% +21% |
| F105 #25 | `cs_last_high20(neg(cross_tail_mean_q75(day_cov(Amt, Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | 2 | **+19.0% / +14.6%** | +3.27 / +1.60 | 4.0% | -15.0% | +0.55 | +25% +16% +12% +16% +25% +20% +12% +14% |
| F113 #1375 | `cs_last_high20(neg(add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cs_bucket_rank(cross_mean(day_gini(…` | 3 | **+18.8% / +14.9%** | +3.26 / +1.56 | 3.3% | -16.2% | +0.55 | +20% +15% +13% +18% +27% +21% +12% +15% |
| F111 #953 | `cs_last_high20(neg(add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(ts_spearman(day_quantile(Close), 10…` | 3 | **+19.1% / +13.8%** | +3.23 / +1.44 | 4.6% | -16.2% | +0.57 | +26% +16% +12% +16% +26% +20% +10% +15% |
| F103 #820 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15)), neg(cro…` | 3 | **+18.4% / +15.3%** | +3.21 / +1.63 | 3.1% | -14.9% | +0.46 | +24% +14% +11% +15% +26% +21% +12% +15% |
| F110 ret_fair_log | `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))), mul(cs_ra…` | 3 | **+18.7% / +18.5%** | +3.12 / +1.67 | 3.6% | -17.5% | +0.63 | +26% +18% +10% +17% +23% +19% +20% +16% |
| F108 #3264 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15)), cross_m…` | 3 | **+17.7% / +15.1%** | +3.10 / +1.61 | 3.6% | -16.2% | +0.42 | +18% +14% +13% +17% +26% +21% +11% +15% |
| F104 #4190 | `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_flat_ratio(Close), 15))` | 3 | **+18.2% / +14.9%** | +3.08 / +1.62 | 3.1% | -14.8% | +0.57 | +24% +13% +11% +15% +25% +21% +12% +15% |

## 0.5 跨因子:这些候选是几个东西(只用用户训练段)

把 15 条因子按规则选出的 74 个候选放在一起。**同簇** = 逐日截面秩相关 ≥ 0.7 或多头书(前 10%)重合 ≥ 50%;簇按训练段纯多头夏普排,簇首是簇里夏普最高的。筛子把两成股票压到最底,秩相关会掉很多而持有的书几乎不变,所以要同时看重合度。

| 簇 | 类 | 簇首来自 | 簇首表达式 | 半衰期 | 多头净超额 训练 / 验证 | 纯多头夏普(训练段) | ρ已知族 / 多头书重合 | 成员 |
|---|---|---|---|---|---|---|---|---|
| 1 | **独立** | F107 | `add(cs_rank(cross_ema(abs_(cs_demean(day_std(Ret))), 30)), mul(cs_rank(cross_ema(abs_(cs_demean(day…` | 1 | +15.8% / +7.8% | +3.74 | +0.29 / 14% | 2 个:F101 F107 |
| 2 | 已知族 | F114 | `sub(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))),…` | 2 | +17.6% / +24.3% | +3.48 | +0.52 / 36% | 10 个:F102 F103 F105 F107 F108 F111 F114 基准 |
| 3 | 已知族 | F107 | `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(add(cs_rank(cross_ema(abs_(cs_demean(day_std…` | 0 | +19.4% / +22.8% | +3.35 | +0.93 / 57% | 22 个:F101 F102 F103 F104 F105 F107 F109 F111 F112 F113 F115 基准 |
| 4 | 已知族 | F101 | `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))),…` | 20 | +16.1% / +18.5% | +3.32 | +0.55 / 24% | 7 个:F101 F104 F108 F110 F113 |
| 5 | **独立** | F113 | `cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30))` | 20 | +9.1% / +16.1% | +3.21 | +0.09 / 24% | 1 个:F113 |
| 6 | **独立** | F102 | `cs_bucket_rank(cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 60), cross_age(day_last(Close)…` | 5 | +11.1% / +9.9% | +2.93 | +0.23 / 20% | 2 个:F102 |
| 7 | 已知族 | F108 | `cs_last_high40(neg(cross_mean(day_std(Amt), 30)), cross_max(day_flat_run_max(Close), 15))` | 2 | +14.5% / +17.8% | +2.82 | +0.42 / 31% | 2 个:F105 F108 |
| 8 | **独立** | F105 | `cs_last_high20(neg(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)), cross_max(…` | 5 | +11.4% / +18.9% | +2.77 | +0.38 / 28% | 1 个:F105 |
| 9 | **独立** | F111 | `cs_last_high20(ts_pearson(day_last(Close), 20), cross_max(day_zero_ratio(Ret), 15))` | 10 | +14.3% / +17.3% | +2.75 | +0.17 / 19% | 3 个:F111 |
| 10 | **独立** | F103 | `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_semistd_neg(Amt, 30))), 1)), 5)` | 40 | +9.4% / +20.0% | +2.29 | +0.58 / 36% | 1 个:F103 |
| 11 | 已知族 | F104 | `day_kurt(nt_cs_mask_top_replace_mean_neg(sqrt(Amt)))` | 20 | +12.2% / +18.8% | +2.18 | +0.59 / 65% | 1 个:F104 |
| 12 | **独立** | F106 | `sub(cs_rank(neg(cross_mean(day_zero_ratio(Ret), 30))), cs_rank(cross_mean(day_sum(Amt), 30)))` | 0 | +13.2% / +9.1% | +2.08 | +0.48 / 15% | 1 个:F106 |
| 13 | **独立** | F110 | `cs_last_low20(neg(cross_ema(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(div(day_las…` | 5 | +12.1% / +12.1% | +2.03 | +0.29 / 20% | 1 个:F110 |
| 14 | **独立** | F112 | `ts_scale(signedpower(cs_rank(add(day_quantile(Close), day_kurt(High)))), 50)` | 60 | +12.4% / +16.2% | +2.02 | +0.25 / 24% | 2 个:F112 |
| 15 | 已知族 | F114 | `cs_first_low40(neg(cross_quantile_q25(day_close(Ret), 15)), cross_mean(day_sum(Amt), 30))` | 60 | +8.9% / +20.0% | +1.94 | +0.72 / 43% | 7 个:F104 F106 F107 F108 F109 F110 F114 |
| 16 | **独立** | F112 | `signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High))))` | 10 | +6.3% / +13.7% | +1.85 | +0.41 / 22% | 1 个:F112 |
| 17 | **独立** | F115 | `cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mea…` | 10 | +7.5% / +5.4% | +1.77 | +0.21 / 20% | 2 个:F115 |
| 18 | **独立** | F107 | `cross_ema(abs_(cs_demean(day_skew(Low))), 30)` | 5 | +5.8% / +8.3% | +1.31 | +0.28 / 19% | 1 个:F107 |
| 19 | **独立** | F113 | `pow_1_5(ts_max(pow_2(cs_mask_top_replace_mean_neg(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_…` | 2 | +4.8% / +10.6% | +1.26 | +0.23 / 17% | 1 个:F113 |
| 20 | **独立** | F114 | `cross_max(cross_quantile_q25(day_close(Ret), 15), 30)` | 20 | +1.9% / +8.6% | +1.15 | +0.08 / 14% | 1 个:F114 |
| 21 | 已知族 | F109 | `cross_mean(sub(day_pos_ratio(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))), day_pos_r…` | 20 | +4.9% / +10.8% | +1.09 | +0.63 / 53% | 1 个:F109 |
| 22 | **独立** | F108 | `day_max(pow_1_5(pow_2(nt_ts_var(Close, 30))))` | 10 | +5.5% / +14.8% | +1.01 | +0.52 / 27% | 2 个:F108 F109 |
| 23 | **独立** | F110 | `cross_ema(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is…` | 5 | +3.9% / +9.0% | +0.92 | +0.38 / 20% | 1 个:F110 |
| 24 | **独立** | F106 | `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), a…` | 20 | +3.1% / +4.3% | +0.59 | +0.07 / 27% | 1 个:F106 |

原式各自落在哪:F101 → 簇首 `F107.h3_blend_own2_ema30`;F102 → 簇首 `F102.h3_age_bucket`;F103 → 不属于任何簇(最近 `F104.sub_A_sqrt` ρ +0.48);F104 → 簇首 `F104.sub_A_sqrt`;F105 → 簇首 `F105.seg_xfrozen_m`;F106 → 不属于任何簇(最近 `F106.abl_M` ρ +0.44);F107 → 簇首 `F107.mem_ema30`;F108 → 不属于任何簇(最近 `F113.h3_g6_bdemean` ρ +0.50);F109 → 不属于任何簇(最近 `F106.abl_M` ρ +0.48);F110 → 簇首 `F110.mem_ema30`;F111 → 不属于任何簇(最近 `F111.h3_best2` ρ +0.54);F112 → 簇首 `F112.h_csrank_w50`;F113 → 不属于任何簇(最近 `F113.sub_I_cs_mask_top_replace_mean_neg` ρ +0.44);F114 → 不属于任何簇(最近 `F114.mem_max30` ρ +0.57);F115 → 不属于任何簇(最近 `F115.h3_raw_amt` ρ +0.52)。

### 组合书(规则在看结果前写死:成员 z-rank 的等权均值;半衰期在用户训练段上再定)

`known_head` = 已知族里最好的簇首单独持有;`indep_eq` = 所有训练段夏普 ≥ 2 的独立簇首等权;`indep_top3` = 其中最好的三个;`all_eq` = 独立簇首 + 已知族簇首等权;`half_half` = 一半已知族簇首、一半独立簇首的均值。**测试段还没读**(等第三轮的候选定下来后只读一次)。

| 组合 | 成员 | 半衰期 | 多头净超额 训练 | 纯多头夏普 训练 | 日换手 | 最大回撤 训练 | 逐年 |
|---|---|---|---|---|---|---|---|
| `known_head` | 1 个:`F114.h3_xfr_plus_slowf` | 0 | **+19.5%** | +3.48 | 3.5% | -8.1% | +21% +17% +13% +20% +27% +19% |
| `indep_eq` | 9 个:`F107.h3_blend_own2_ema30` `F113.h3_g6_bdemean` `F102.h3_age_bucket` `F105.seg_xfrozen_m` `F111.h3_best2` `F103.nosc_B_cross_semistd_neg` `F106.h_zero_minus_liq` `F110.h3_cvx_xage` `F112.h_csrank_w50` | 0 | **+19.6%** | +3.79 | 3.0% | -6.4% | +22% +19% +16% +19% +24% +16% |
| `indep_top3` | 3 个:`F107.h3_blend_own2_ema30` `F113.h3_g6_bdemean` `F102.h3_age_bucket` | 0 | **+14.2%** | +3.98 | 2.8% | -2.8% | +8% +19% +21% +14% +11% +11% |
| `all_eq` | 10 个:`F107.h3_blend_own2_ema30` `F113.h3_g6_bdemean` `F102.h3_age_bucket` `F105.seg_xfrozen_m` `F111.h3_best2` `F103.nosc_B_cross_semistd_neg` `F106.h_zero_minus_liq` `F110.h3_cvx_xage` `F112.h_csrank_w50` `F114.h3_xfr_plus_slowf` | 0 | **+19.9%** | +3.78 | 3.0% | -7.0% | +23% +18% +15% +20% +25% +16% |
| `half_half` | 10 个:`F114.h3_xfr_plus_slowf` `F107.h3_blend_own2_ema30` `F113.h3_g6_bdemean` `F102.h3_age_bucket` `F105.seg_xfrozen_m` `F111.h3_best2` `F103.nosc_B_cross_semistd_neg` `F106.h_zero_minus_liq` `F110.h3_cvx_xage` `F112.h_csrank_w50` | 0 | **+21.1%** | +3.80 | 3.0% | -7.5% | +24% +20% +14% +23% +27% +18% |

`indep_eq` 里每个独立簇首带了多少(训练段;去掉它之后组合掉多少):

| 去掉的簇首 | 表达式 | 去掉后 净超额 / 夏普 | 它的贡献 净超额 / 夏普 | 与已知族簇首五五混合(训练段)净超额 / 夏普 |
|---|---|---|---|---|
| `F107.h3_blend_own2_ema30` | `add(cs_rank(cross_ema(abs_(cs_demean(day_std(Ret))), 30)), mul(cs_rank(cross_ema(abs_(cs_…` | +18.2% / +3.49 | +1.4% / +0.30 | +20.2% / +4.09 |
| `F113.h3_g6_bdemean` | `cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30))` | +20.0% / +3.84 | -0.4% / -0.05 | +16.1% / +3.32 |
| `F102.h3_age_bucket` | `cs_bucket_rank(cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 60), cross_age(day_l…` | +20.7% / +3.90 | -1.1% / -0.11 | +15.9% / +3.37 |
| `F105.seg_xfrozen_m` | `cs_last_high20(neg(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)), …` | +19.2% / +3.68 | +0.4% / +0.11 | +18.2% / +3.48 |
| `F111.h3_best2` | `cs_last_high20(ts_pearson(day_last(Close), 20), cross_max(day_zero_ratio(Ret), 15))` | +18.8% / +3.73 | +0.8% / +0.06 | +20.4% / +3.59 |
| `F103.nosc_B_cross_semistd_neg` | `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_semistd_neg(Amt, 30)))…` | +19.2% / +3.68 | +0.4% / +0.11 | +17.9% / +3.47 |
| `F106.h_zero_minus_liq` | `sub(cs_rank(neg(cross_mean(day_zero_ratio(Ret), 30))), cs_rank(cross_mean(day_sum(Amt), 3…` | +19.6% / +3.74 | +0.0% / +0.05 | +17.5% / +3.29 |
| `F110.h3_cvx_xage` | `cs_last_low20(neg(cross_ema(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(d…` | +19.7% / +3.90 | -0.0% / -0.11 | +17.3% / +3.00 |
| `F112.h_csrank_w50` | `ts_scale(signedpower(cs_rank(add(day_quantile(Close), day_kurt(High)))), 50)` | +19.3% / +3.96 | +0.3% / -0.17 | +16.7% / +2.70 |

## 1. 一张表(多头腿净超额 训练 / 测试;括号里是纯多头夏普)

| # | 因子 | 原式 | 本因子最好的版本 | 它的数字 | ρ原式 / ρ已知族 | 建在已知族上的最好版本 | 它的数字 |
|---|---|---|---|---|---|---|---|
| 1 | 手写 day_shine_retstd | +7.1% / +7.1%(+1.37 / +1.40) | `add(cs_rank(abs_(cs_demean(day_std(in_slice(Ret, 2, 237))))), cs_rank(abs_(cs_d…` hl 60 | **+10.8% / +11.7%**(+2.91 / +2.55) | +0.35 / +0.48 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_…` hl 10 | **+17.9% / +16.0%**(+3.34 / +1.70) |
| 2 | 挖掘 #3961 | +8.9% / +2.5%(+2.05 / +0.45) | `cs_bucket_rank(cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 60), cross…` hl 5 | **+10.7% / +5.8%**(+2.93 / +1.24) | +0.79 / +0.24 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_…` hl 3 | **+17.9% / +14.9%**(+3.08 / +1.62) |
| 3 | 挖掘 #820 | +8.1% / +7.2%(+1.49 / +1.26) | `cross_max(mul(day_topw_mean(Amt, Amt), day_std(in_pct(cross_decay_linear(Amt, 3…` hl 10 | **+15.6% / +13.5%**(+2.47 / +1.53) | +0.32 / +0.90 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_…` hl 3 | **+19.6% / +15.3%**(+3.34 / +1.63) |
| 4 | 挖掘 #4190 | +3.4% / +0.4%(+0.71 / +0.07) | `day_std(nt_cs_mask_top_replace_mean_neg(sqrt(Amt)))` hl 20 | **+15.1% / +12.6%**(+2.87 / +1.42) | +0.16 / +0.93 | `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_flat_ratio(Clos…` hl 3 | **+18.2% / +14.9%**(+3.08 / +1.62) |
| 5 | 挖掘 #25 | +11.8% / +8.9%(+1.96 / +1.04) | `cs_last_high20(neg(cross_tail_mean_q75(day_cov(Amt, Amt), 30)), cross_max(day_z…` hl 2 | **+19.0% / +14.6%**(+3.27 / +1.60) | +0.45 / +0.55 | `cs_last_high40(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret)…` hl 2 | **+14.8% / +15.4%**(+2.81 / +1.70) |
| 6 | 手写 erm_mag_gap_1m | -3.4% / -0.1%(-1.22 / -0.02) | `sub(cs_rank(neg(cross_mean(day_zero_ratio(Ret), 30))), cs_rank(cross_mean(day_s…` hl 0 | **+12.1% / +15.5%**(+2.08 / +1.70) | -0.00 / +0.46 | `cs_last_high40(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret)…` hl 2 | **+14.8% / +15.4%**(+2.81 / +1.70) |
| 7 | 挖掘 #613 | +4.3% / +4.7%(+0.90 / +1.18) | `add(cs_rank(cross_ema(abs_(cs_demean(day_std(Ret))), 30)), mul(cs_rank(cross_em…` hl 1 | **+13.6% / +12.5%**(+3.74 / +2.39) | +0.33 / +0.29 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_…` hl 10 | **+18.4% / +15.0%**(+3.41 / +1.64) |
| 8 | 挖掘 #3264 | +1.3% / -3.8%(+0.19 / -0.33) | `cs_last_high20(neg(day_max(pow_2(nt_ts_std(Amt, 30)))), cross_max(day_zero_rati…` hl 20 | **+15.2% / +13.3%**(+2.73 / +1.68) | +0.25 / +0.57 | `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_…` hl 3 | **+17.7% / +15.1%**(+3.10 / +1.61) |
| 9 | 手写 erm_mag_gap_5m_tsm20 | -1.7% / +2.1%(-0.73 / +0.81) | `cs_first_low40(neg(ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close…` hl 40 | **+10.6% / +7.3%**(+1.67 / +0.88) | +0.16 / +0.75 | `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cross_tail_mean_q75(div(…` hl 0 | **+17.0% / +12.6%**(+2.50 / +1.42) |
| 10 | 手写 ret_fair_log | +1.3% / -2.5%(+0.24 / -0.26) | `cs_last_low20(neg(cross_ema(mul(sub(div(day_last(Close), day_first(Open)), 1), …` hl 5 | **+12.1% / +11.4%**(+2.03 / +1.15) | +0.54 / +0.33 | `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zer…` hl 3 | **+18.7% / +18.5%**(+3.12 / +1.67) |
| 11 | 挖掘 #953 | +12.3% / +6.0%(+2.15 / +0.84) | `cs_last_high20(ts_pearson(day_last(Close), 20), cross_max(day_zero_ratio(Ret), …` hl 10 | **+15.2% / +8.0%**(+2.75 / +1.08) | +0.54 / +0.14 | `cs_last_high20(neg(add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(ts_sp…` hl 3 | **+19.1% / +13.8%**(+3.23 / +1.44) |
| 12 | 挖掘 #574 | +5.6% / +2.3%(+0.98 / +0.33) | `ts_scale(signedpower(cs_rank(add(day_quantile(Close), day_kurt(High)))), 50)` hl 60 | **+13.5% / +12.8%**(+2.02 / +1.58) | +0.74 / +0.30 | `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(div(day_median(Close), c…` hl 2 | **+15.1% / +15.4%**(+2.21 / +1.45) |
| 13 | 挖掘 #1375 | +0.7% / -0.6%(+0.17 / -0.15) | `cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30))` hl 20 | **+11.2% / +6.0%**(+3.21 / +1.26) | +0.09 / +0.06 | `cs_last_high20(neg(add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cs_bu…` hl 3 | **+18.8% / +14.9%**(+3.26 / +1.56) |
| 14 | 挖掘 #1421 | +4.5% / +0.4%(+0.83 / +0.05) | `cs_last_high20(neg(cross_ema(cross_quantile_q25(day_close(Ret), 60), 30)), cros…` hl 5 | **+9.2% / +3.7%**(+2.44 / +0.68) | +0.42 / +0.03 | `sub(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zer…` hl 2 | **+19.5% / +14.7%**(+3.48 / +1.95) |
| 15 | 手写 all_tide_mean_30 | +3.9% / +0.6%(+0.88 / +0.09) | `cs_first_low40(neg(cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), …` hl 10 | **+11.8% / +8.0%**(+2.01 / +0.93) | +0.62 / +0.78 | `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_mean(div(div(sub(day_lo…` hl 1 | **+15.2% / +12.6%**(+2.25 / +1.34) |
| — | _基准:已知成交额族_ `cross_mean(day_std(Amt), 30)` | +15.4% / +14.1%(+2.22 / +1.51) | | | | | |
| — | _通用筛子:已知族 + 剔除近 15 日冻结盘口最重的 20%_ | +18.5% / +15.0%(+3.13 / +1.61) | | | | | |

## 2. 逐条

### 1. 手写 day_shine_retstd(F101)

`abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1)), add(in_mean_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))), in_stddev_full(sub(in_slice(Volume, 2, 237), in_delay(in_slice(Volume, 2, 237), 1))))), in_sli…`

**它是什么(按算子定义)**:逐层:A=in_slice(Volume,2,237)(两端都含,241格取236,去掉开盘2格+收盘集合竞价3格);Δ_j=v_j−v_{j−1}(in_delay第一格NaN⇒j=0永不触发);阈值θ=mean_全天(Δ)+std_全天(Δ),而mean(Δ)=(v_235−v_0)/235≈0⇒θ实际就是1σ(Δ);掩码G=1{Δ_j>θ};in_sustain_stddev在每个G==1.0的分钟写出σ_j=总体std(r_j…r_{j+4})(窗口含触发分钟自己、朝后看、跑出行尾截短,其余分钟NaN);J=对触发点的nanmean(等权,与触发次数无关,T空则NaN);K=J−当天全市场J的均值;因子=|K|,sg=−1(多头=|K|最小)。名字骗人三处:(1)sustain不是"持续"而是"从触发点往后取一段",注册表给in_sustain_stddev打的boolean_output标签是错的(它输出连续std,真掩码是第一个操作数);(2)"放量"指相邻两分钟的增量超过当天自己的1σ,不是"这分钟量大",阈值按每票自己的σ定⇒掩码不带成交额尺度,每票每天约触发20次;(3)abs_单独是no-op(J是std≥0),abl_K(只去cs_demean)与iso_J(两个都去)逐位相同(−6.8%/+2.1%,Lshp−0.81/+0.28),abs_唯一作用是与cs_demean配成"在当天截面均值处的V形折叠";折叠中心也不是"中间",截面均值落在J的第65.6百分位。另:abl_G(删is_gt)的掩码实为"Δ恰好等于1"(内核只认mask==1.0),是个近乎任意的分钟采样器。

**承重的子结构**

- 截面V形折叠abs_(cs_demean(·))必须成对:abl_K≡iso_J逐位相同证明abs_单独无效;单调版iso_K/iso_J/sub_L_neg的Lshp(ut)全在−0.49~−0.52、Lnet(tr)−6.5~−6.8%
- 被测量必须是日内收益的离散度:换in_corr/in_cov/in_r2→Lshp(ut)−1.07/−0.19/−1.14;abl_I(删in_sustain_stddev,根变0/1掩码)dist 0.01✗、−1.43
- day_mean必须是全天平均的水平:换day_first/day_last/day_close→−0.12~−0.16;换day_skew/day_gini→−0.14/−0.93(必须是尺度不是形状)
- 折叠中心必须是当天截面均值:cs_demean→cs_normalize仍1.35(只改缩放),→cs_mean/cs_stddev_full/cs_quantile_q25全部dist 0.00退化
- 持久的截面水平:cross_zscore去掉水平后是全表最差(mem_zscore5/10 = −6.23/−4.17),信息不在日间变化里
- 长半衰期:稠密族一律选到网格上限hl=20(边界解),LTO从base的10.4%降到5.2%;rk(先cs_rank再EMA)单独值+0.47 Lshp

**多余的节点**

- 整台放量触发机器(B in_delay/C sub/D in_mean_full/E in_stddev_full/F add/G is_gt):不只多余,它就是样本外失效的那部分。阈值退化成≈0或掩码放稠密后valid从−1.6%跳到+8.9~+11.6%、Lshp(ut)1.37→2.4~2.7、LTO 10.4%→5.2%、最优hl 10→20(abl_F/sub_F_div/sub_F_sub/sub_E_in_kurt_full/nosc_E_in_skew_full/sub_C_mul/fld_Volume_Amt/abl_G八条互相逐位接近)
- 阈值里的μ+σ结构:任何量纲不匹配的小正数都等价(in_kurt_full/in_skew_full代入→2.45/2.42,比base的1.37好),因为它们相对Δ的尺度≈0
- 5分钟这个窗口:win_I 3/5/10/15→Lshp(ut)1.20/1.37/1.85/2.03单调上升无峰,15分钟重叠窗口已接近全天收益std
- Volume字段的身份:leaf_Volume_amt(触发字段换Amt)=1.40≈base 1.37;前研究也证实不用Volume的版本分不开
- in_slice切片(前研究s2_roll5_noslice)、cs_winsor(win=1.43≈base,折叠后的量本来不重尾)
- 给稀疏base加日轴记忆:mem_mean/ema/decay_linear把train推到2.4~2.8但valid全在0.4~1.3——在日轴上平均一个坏的日内估计量救不回来

**可互换的叶子**

- 触发字段 Volume ↔ Amt:完全等价(leaf_Volume_amt 1.40 ≈ base 1.37)
- 被测字段 Ret ↔ in_pct(Volume,1) / in_pct(Amt,1):仍有效且valid更好(leaf_Ret_volchg/amtchg valid +8.0%/+8.0%、Lshp 1.47/1.57,base是−0.38)——用户'分钟收益与量的变化率是同一类东西'的提示在这棵树上成立
- 不能换的被测字段:in_pct(Close,5)(−0.16)、in_pct(Vwap,1)(+0.25)、in_logchg(Volume,1)(−0.01)都回到base的样本外毛病
- 阈值项 in_stddev_full ↔ in_kurt_full ↔ in_skew_full(都退化成≈0的阈值);in_delay(V,1) ↔ in_delta/in_pct/in_logchg(sub(V,in_delta(V,1))其实就是上一分钟的量)
- 窗口 5 ↔ 10 ↔ 15:越宽越好,不是互换而是单调改善

**在哪类股票里有效**

- 按流通市值:小票里最强却几乎不买——最低20%(段等权+6.4%)段内+16.9% S+2.96(v_base)/+16.5% S+2.74(fld_Volume_Amt),但tilt −13.5/−11.4(只放了书的6%);最高20%段内+1.2% S+0.20而tilt +18.9。k_known正相反(最低市值段tilt +30.8%)
- 按20日成交额:只在活跃的一头有分辨力——最低20%(段等权+15.1%)段内仅+0.7% S+0.15,却占了书的16%仓位;最高20%(段等权−17.8%)段内+20.5% S+2.00/+18.0% S+2.15
- 按板块:科创板是唯一失效区,段内−19.4% S−1.01(v_base还超配+2.2%)、稠密族−4.8~−15.8%;沪深主板+创业板段内+7.6~+12.2%
- 按价格:中间三档最好(+9.3~+12.9%),最低价档只有+2.3~+5.0%(最小变动价位把低价票的分钟收益量化了)
- 次新(上市不足250日,7.1%人头,段等权−28.7%):段内+13.8~+17.5%且tilt −5.7~−6.4,既躲开又能选,不用动
- 冻结盘口(近15日有封板/停牌,6.5%人头,段等权−67.4%):所有变体只放1.5%仓位;但段内只有v_base行(+27.5% S+2.07),稠密族是−6.5~+8.4%——这是触发机器唯一有用的地方,对多头腿贡献≈0

**什么时候有效**

- 逐年:失效是base独有的,不是因子的。v_base 2018–2023 = +8.1/+12.4/+15.4/+1.6/+1.0/+2.0%;fld_Volume_Amt = +4.3/+13.0/+13.4/+9.4/+9.0/+8.8%;abl_F = +4.2/+11.2/+11.3/+10.4/+12.4/+7.8%。2021年之后只有稀疏触发版塌了
- 稠密族顺周期:放量日+13.6~+14.5% vs 缩量+5.9~+6.6%;截面离散度高+13.8~+14.3% vs 低+5.7%;市场近20日上涨+12.9~+14.1% vs 下跌+5.1~+5.9%
- v_base反而逆周期(上涨+4.9%、下跌+10.2%),与稠密族正好相反——两者可以互补,但base那一侧的钱太少
- 市场波动高/低几乎无差(稠密族+9.8%/+9.8~9.3%),所以起作用的是截面离散度和成交量,不是市场波动本身

**原因推断**:机制推断:折叠后的量=“这只票的日内收益离散度离当天全市场典型值有多远”,多头腿买“最典型”的那批。右尾(被躲开的)是投机性注意力集中的票——前研究实测空头十分位94~97%来自高侧、平均在换手率第80/20日波动第82百分位;左尾(也被躲开)几乎全是一字板/准停牌(J==0占0.47%,剔除后低侧只是浅坡)。所以它本质是**投机溢价的反向暴露 + 冻结盘口的排除**,不是“中庸”。这解释了三件事:(a) 为什么只在有投机的时段赚钱(放量日、截面离散度高的日子是缩量/低离散的两倍以上);(b) 为什么在20日成交额最高段段内+20.5%而该段等权−17.8%(那里才有投机溢价可躲),在最低段段内+0.15夏普(清淡票的日内std主要是最小变动价位噪声和零成交分钟,不是信息);(c) 为什么书被推进大票——折叠中心是全市场均值,而小票的日内波动系统性高于大票,“离全市场均值最近”就等于“选大票”,科创板因20%涨跌幅使板内分布整体右移而被整体错判(段内−19.4%)。2021年后稀疏版失效的推断:VWAP/TWAP切单与量化成交占比上升,分钟量的“跳升”越来越多来自算法切片而非事件,Δ>1σ选出的分钟从信息时刻退化成噪声子样本;稠密版测的是全天波动水平,不受影响。可检验推论已写进第二批:成交额加权的|Ret|(h_wmean_absret)应修好最低成交额段的零分辨力;按价格/成交额分桶做折叠(h_rv_fold_bk_price/bk_amt241)应让科创板段内由负转正、把书放回小票;每票每天的触发数及其截面离散度在2021后应有结构变化。

**相对已知成交额族**:相关性上是两回事(整族ρk只有+0.14~+0.18;res_known仍有+10.2%/+3.4%、Lshp 2.37/0.81),结构上也互补:k_known几乎没有段内分辨力(20日成交额五段段内−4.1/−5.3/−8.2/−5.2/+2.5%),它靠的是tilt(最低成交额段+80.3%、最低市值段+30.8%),是个纯粹的规模/流动性溢价收割器;F101族相反,tilt温和但在每个市值桶、每个价格桶里都有分辨力(S+0.8~+2.8)。**但增量没有被坐实**:ov_p10/p05/p025的utrain净超额+15.4/+15.5/+15.4%对已知族的+15.4%完全打平,夏普2.42/2.33/2.27对2.22(+0.20在±0.3噪声内),valid净超额反而被拖低(18.5/20.9/20.7对22.3);负权重更差(ov_m10=0.18)。关键空白:这三条overlay叠的是已经失效的v_base,不是稠密族。当前最诚实的结论——按净超额任何单体都打不过已知族(最好9.7%对15.4%),按纯多头夏普fld_Volume_Amt 2.68>2.22(差0.46>噪声),即“更稳但更小”;**作为独立因子对用户没有增量**,唯一还活着的用法是“桶内选股器叠在已知族的tilt上”,第二批D组(h_ov_k_rv_05/10、h_ov_k_fldamt_05、h_res_k_rv、h_bk_k_rv)就是去判这一条。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Volume, 2, 237), in_delay(in…` | base | 20 | +7.1% / +7.1% | +1.37 / +1.40 | 5.6% | +3.93 / +3.70 | +8% +12% +15% +1% +1% +3% +9% +6% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h_sum_rv_amtchg` `add(cs_rank(abs_(cs_demean(day_std(in_slice(Ret, 2, 237))))), cs_rank(abs_(cs_demean(day_…` | hypo | 60 | +10.8% / +11.7% | +2.91 / +2.55 | 2.7% | +3.18 / +1.82 | +10% +15% +8% +13% +7% +10% +10% +14% |
| `fld_Volume_Amt` `abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Amt, 2, 237), in_delay(in_sl…` | field | 20 | +9.7% / +7.2% | +2.68 / +1.60 | 5.2% | +3.65 / +3.26 | +4% +13% +13% +9% +9% +8% +11% +3% |
| `seg_lowliq_m` `cs_first_low40(neg(abs_(cs_demean(day_mean(in_sustain_stddev(is_gt(sub(in_slice(Volume, 2…` | segment | 20 | +16.0% / +15.6% | +2.67 / +2.03 | 3.9% | +3.52 / +2.08 | +20% +13% +7% +15% +27% +15% +10% +17% |
| `h3_scr_kx_xhi` `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio…` | hypo | 10 | +17.9% / +16.0% | +3.34 / +1.70 | 4.4% | +3.50 / +2.19 | +19% +16% +13% +17% +23% +21% +10% +18% |
| `h3_ov_kx_roll5` `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Re…` | hypo | 20 | +16.8% / +17.9% | +3.32 / +1.90 | 3.3% | +3.55 / +2.08 | +19% +15% +14% +16% +22% +19% +11% +21% |

综合全文:`notes/F101_day_shine_retstd/synthesis.md`;回测表与解剖:`./scripts/study.sh table F101_day_shine_retstd s4`。

### 2. 挖掘 #3961(F102)

`cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)`

**它是什么(按算子定义)**:按函数定义逐层:(1) `nt_ts_autocorr_s1(Ret, 3)` = `ts_corr(x[1:], x[:-1], 3)`,只用 4 根连续分钟收益算出的「滞后 1 相关」—— 样本量 3 的相关是 U 形的、质量堆在 ±1;而分母是 `sqrt(var_x·var_y) + EPS`,窗口内收益全相等(封板/停牌/无成交)时 var=0,值**恰好为 0**。(2) `day_kurt` = `C._kurt`,同族内核 `nankurt_last = m4/(var²+EPS) − 3`,是**超额**峰度(下界 −2、上界无穷),当天序列全常数时 NaN。(3) `pow_2 = pow_(x,2)`,`e>1` 走 `x**e` 分支,**不是**带符号幂 —— 因为超额峰度 ≥ −2,平方把薄尾侧硬顶在 ≤4、把尖峰侧放大到无穷,实质是 `max(kurt,0)` 的凸版本,即一个**折叠**。(4) `cross_sum(·,15)` 用 `nansum_last`,**NaN 当 0**。合起来:「近 15 日里有没有哪一天的分钟收益出现过『长段纹丝不动 + 几根孤立跳』的结构;有 = 不买」——一台封板/停牌/死盘口探测器,与任何意义上的「自相关」无关。名字与定义不一致的三处:pow_2 是折叠不是放大;day_kurt 是超额峰度可为负(`sub_C_pow_1_5` 的 cov 掉到 0.75,直接量出 25% 的股票-日为负);cross_sum 不是「累计」而是「求和 + 缺失日记 0」,在 sg=−1 下等于系统性**买进**历史不全的票。

**承重的子结构**

- pow_2 这个折叠:`abl_C` 删掉它 → ut −4.0%、夏普 −0.71,且与原式 rank 相关 ρo = **0.00**(`sub_C_neg` 同值)。峰度的水平毫无信息,只有绝对值有;`sub_C_pow_05`/`signedpower`(保号)−4.0%/−3.1%、`sub_C_inv` +1.5%,凡保号的全死
- 非负之外还要凸:`sub_C_abs_` ρo 0.96 但 +7.0%/夏普1.48(低近 2 点),`sub_C_log` +8.9%/1.89,`sub_C_sqrt` +5.0% → 折叠值约 13 个点、凸性再值 1.5~2 个点
- 3 分钟孔径,而且是刀尖、**没有平台**:`win_A_5` +1.5%(夏普0.42)、`win_A_10` −3.1%(valid −12.6%)。孔径一放宽,『var=0 → 恰好 0』这个退化出口就被稀释
- A 槽位(autocorr)不可替换:同窗口换 `nt_ts_scale` +6.6%、`argmax` +4.3%、`rank` +2.8%、`std/stddev` +3.1%、`skew` −1.4%、`kurt` −3.1%,ρo 全在 0.03~0.45;`abl_A`(整层删掉)+2.6%、ρo 0.09
- B 槽位(day_kurt)不可替换,而且读的**不是离散度**:`day_std` −6.0%(ρo −0.08)、`day_gini` +3.2%、`day_skew` +2.4%、`day_pos_ratio` −1.0%、`day_q_stat_std` −6.6%、`day_autocorr_n1`/`day_ar1` +1.6%/+1.3%
- 叶子 Ret 不可换(见 swappable_leaves):承重原子是分钟收益在 0 上的点质量,量的变化率没有这个原子

**多余的节点**

- 外层 `cross_sum` 几乎只是平滑:`iso_C`(D 层全删,只留单日 `pow_2(K)`,书 hl=20)= +8.0%/夏普1.61,只比原式(hl=5)低 0.9 点。**总平滑量守恒** —— `iso_C` hl20 / 原式 hl5 / `mem_mean60` hl0 都落在 +8~+11%
- D 窗口是平台,不是杠杆:5/10/15/30/60 → +10.0/+9.5/+8.9/+7.9/+8.7%,夏普 2.02/2.04/2.05/1.75/1.80
- `cross_sum` → `cross_mean` 是纯提纯(`sub_D_cross_mean` +10.2%/夏普2.32/ρo0.99):同结构同速度,只是不再把缺失日记 0;解剖证明它修好了科创板(段内 −28.5% → +3.0%)与次新(+7.1% → +23.5%)两段
- 真杠杆是换手:同窗口换聚合器就把日换手从 5.4% 压到 2.1~2.4% 而毛超额不掉 —— `cross_ema` +10.8%/LTO2.1%、`cross_decay_linear` +10.9%/2.4%、`cross_fangzheng` +9.6%/2.3%;约 2 个点净超额全部来自省下的费
- 伤害性改法(反面证据):`cross_zscore` −13.7%(LTO18.4%)、`cross_scale` −10.0%(LTO22.7%)、`cross_delta` −5.3%、截面折叠 `fold_sq`/`fold_mean` −17~−19%、`iso_B`(裸 day_kurt,sg+1)−27.1%

**可互换的叶子**

- 无 —— Ret 不可换,而且这是一条实质结论:`in_pct(Vwap,1)` ut +5.5%(train +1.5% / valid +14.4%,不稳)、ρo 0.25;`in_pct(Close,5)` +2.9%;`in_logchg(Volume,1)` +0.6%、ρo −0.01;`in_pct(Volume,1)` +0.2%、`in_pct(Amt,1)` +0.1%(两者 sg 还翻成 +1)。「分钟收益与量的变化率是同一类东西、可互换」在这棵树上**不成立**,因为承重的原子是 Ret 在 0 上的点质量(封板/停牌),量的变化率没有这个原子。表里没有 field 类变体,叶子替换只在 leaf 类里试过这 5 个。

**在哪类股票里有效**

- 流动性:段内预测力随成交额(20日)**单调上升** = −2.9 / −4.3 / −0.3 / +6.1 / **+12.4%**,而全市场多头书对最低分位**超配 +21.1 个点**、对最高分位低配 −11.0 —— 它把钱压在自己最没本事的一端
- 「超配 × 段等权超额」点乘:**原式 +5.5 个点来自跨成交额桶的倾斜(占 +8.9% 的六成)**,`k_known` 是 **+14.7 个点(占 +15.4% 的 95%)**;但不能简单剔掉不活跃票(最低成交额段的段等权超额 +15.1%,只做最高分位 = +12.4% − 17.8% = **−5.4%**)
- 冻结盘口段(近15日有封板/停牌,占 6.5%、段等权 **−67.4%**):原式低配 −5.0 个点 → **+3.6 个点**;`k_known` 只低配 −2.9 → +2.1 个点。无冻结的干净池内原式只 +5.5%、已知族 +14.1% → **它 ≈ 流动性倾斜(5.5)+ 封板规避(3.6),其余近 0**
- 科创板是唯一的大坑,根因是 cross_sum 的缺失日当 0:占 4.0%、段等权 +4.1%(本身不差),但原式**段内 −28.5%** 且**超配 +8.3 个点**(书里 12.3% 仓位压在这里);换 `cross_mean` → +3.0%,`cross_max` → −8.1%、`cross_fangzheng` → −9.1%
- 次新(上市不足250日,7.1%、段等权 −28.7%):原式段内 +7.1% → `cross_mean` **+23.5%** / `cross_decay_linear` +25.5% / `cross_fangzheng` +20.5% —— 与科创板同一个指纹
- 市值 / 价格:最高 20% 市值段内只 +1.7%、最高 20% 价格只 +3.7%,其余四个分位都 +6~+10% —— 大票、高价票上没有

**什么时候有效**

- 年度异常稳定、**无衰减**:2018→2023 = +8.1 / +11.1 / +9.3 / +5.6 / +10.3 / +9.3%;`k_known` 同期 +17.3 / +10.4 / +6.7 / +16.1 / +24.7 / +18.5% 摆动大得多 —— 稳定性是它夏普相对净超额偏高的原因
- 成交状态是最强的时间切分:放量(高于60日均)+13.3% vs 缩量 **+5.4%**
- 市场近20日上涨 +13.2% vs 下跌 **+3.8%**
- 市场波动高于中位 +10.3% vs 低于中位 +7.6%;截面离散度高 +10.1% vs 低 +7.9%(两条都弱于放量/涨跌这两条)

**原因推断**:机制推断:A 股的涨停/停牌会让分钟收益序列出现「长段恰好为 0 + 几根孤立跳」。`ts_corr` 在 var=0 时因分母 EPS 吐出恰好的 0,3 点窗口让这个退化出口最容易被走到;于是当天这条 autocorr 序列变成「一堆 0 + 几个 ±1」,超额峰度爆表。pow_2 把符号折掉后,因子就是「近期有没有封过板/停过牌」,sg=−1 = 不买这些票。为什么在**活跃票**里有信息、在**不活跃票**里没有:低成交额票的 Ret=0 大量来自「没成交」,`day_kurt` 读到的只是「薄」,而「薄」已经被流动性溢价定价了,没有残差;活跃票里 Ret=0 只可能来自封板,是一个真事件。为什么在**放量上涨**的行情里最值钱:封板和涨停的供给是顺周期的 —— 放量上涨时涨停票最多、事后回撤也最凶,规避它们的收益最大;缩量市里几乎没有封板可躲,因子只剩流动性倾斜(+5.4% vs +13.3%)。为什么**科创板/次新**是坑:它们在 15 日窗口里常有缺失日,`cross_sum` 把缺失日记 0 → 和数偏小 → sg=−1 下被当成「最干净」买进去(换 cross_mean 即修复,这是因果链上的直接证据)。可检验推论已全部写成假设:(i) 用 `day_zero_ratio(Ret)` / `day_flat_run_max(Close)` 直接写出这个状态,应能复现大部分,且两方向残差能定谁包含谁;(ii) 用 `cross_valid_count` 剔除有缺失日的票,应在 cross_sum 版本上大幅改善、在 cross_mean 版本上几乎无改善;(iii) 用个股自己的放量倍数做桶内排名,应比全市场排名更强;(iv) `in_madz` / `in_autocorr_s1` 若出现原式缺的窗口平台,说明机制真实、原式只是用了一个脆的估计量。

**相对已知成交额族**:ρk 只有 **+0.26**,结构上不是同一条;但剥掉已知族后剩得不多:`res_known` +3.7%/夏普0.77、`bk_known` +4.0%/0.98(dist 0.20 ✗)、`res_liq` +4.8%/1.01、`bk_liq` +5.0%/1.22(dist 0.20 ✗)。**作为独立纯多头因子它输给已知族**(ut +8.9%/2.05 vs +15.4%/2.22),原因是两者的大头是同一个流动性倾斜而已知族吃得更彻底(95% vs 62%)。**作为小权重配角有正增量,但在噪声边缘**:`ov_p025`/`ov_p05`/`ov_p10`(权重 0.25/0.5/1.0)= 净超额 +15.6/+15.3/+14.3%、夏普 **2.51/2.62/2.57**,对比已知族 +15.4%/2.22 —— 净超额持平、**夏普 +0.3~0.4**(刚到 ±0.3 噪声上沿),但三个权重同向、且反号叠加明确变坏(`ov_m025` 1.59、`ov_m05` 1.18),符号是对的。它真正的独家内容只有两处:(a) 封板规避比已知族多拿 1.5 个点(+3.6 vs +2.1);(b) 在活跃票里还有选股力(最高成交额分位段内 +12.4% vs 已知族 +2.5%;60–80% 分位 +6.1% vs −5.2%),而那正是已知族没东西的地方。诚实结论:**不是可独立上的因子,是已知族的减波动配角,价值约 +0.3 夏普。**

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | base | 5 | +8.9% / +2.5% | +2.05 / +0.45 | 5.4% | +3.71 / +2.56 | +8% +11% +9% +5% +10% +8% +1% +2% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_age_bucket` `cs_bucket_rank(cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 60), cross_age(day_l…` | hypo | 5 | +10.7% / +5.8% | +2.93 / +1.24 | 2.7% | +3.28 / +2.20 | +8% +12% +11% +13% +11% +9% +7% +3% |
| `seg_lowliq_m` `cs_first_low40(neg(cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)), cross_mean…` | segment | 3 | +12.9% / +10.2% | +2.45 / +1.47 | 4.8% | +3.59 / +3.07 | +13% +13% +9% +11% +16% +15% +6% +12% |
| `sub_D_cross_mean` `cross_mean(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` | substitute | 5 | +10.2% / +3.2% | +2.32 / +0.59 | 5.3% | +3.93 / +2.74 | +10% +12% +10% +8% +11% +9% +1% +3% |
| `h3_xfroz_max60` `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio…` | hypo | 3 | +17.9% / +14.9% | +3.08 / +1.62 | 3.2% | +4.17 / +3.75 | +22% +14% +11% +17% +24% +21% +12% +14% |
| `h3_max60_ov05` `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cross_max(pow_2(day_kurt(nt_ts_aut…` | hypo | 0 | +16.4% / +14.9% | +2.81 / +1.78 | 3.2% | +3.08 / +2.92 | +19% +14% +10% +15% +21% +22% +11% +15% |

综合全文:`notes/F102_kurt_autocorr/synthesis.md`;回测表与解剖:`./scripts/study.sh table F102_kurt_autocorr s4`。

### 3. 挖掘 #820(F103)

`cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))), 1)), 5)`

**它是什么(按算子定义)**:按算子定义逐层:立方体是(股票, 日 D, 分钟 M);`cross_*` 沿**交易日轴**逐分钟槽滚动,`day_*` 沿分钟轴折叠。(1) `cross_decay_linear(Amt,30)` = 对每一个分钟槽取近 30 日该槽成交额的线性衰减加权均值 → 一条「30 日平均日内成交额曲线」(**跨日平滑,不是日内衰减**);(2) `day_durbin_watson(·)` = `Σ(x_t−x_{t−1})² / (Σx_t² + 1e-8)`,**分母是 Σx² 而不是 Σ(x−x̄)²,所以它不是 Durbin–Watson 统计量**:对正值序列 ≈ `var(Δx)/(mean²+var(x))`,是一个**无尺度的「尖峰占比」读数**(曲线上一根独立尖峰 → 值≈2;平滑 → 值小),恒 ≥ 0(证据:`sub_D_abs_` 与 `abl_D` 逐列完全相同)。记为 C;(3) `pow_3` = `pow_(x,3)`,e>1 走 `x**3`,C≥0 故单调,它只改 C 在乘法里的权重曲线;(4) `ts_min(·,1)` = **窗口 1 的滚动最小 = 恒等式**(证据:`abl_E` 与 `v_base` 逐位相同、ρo 1.00,树里有一个纯摆设节点);(5) `day_close` = `day_last` = 当天最后一个非 NaN 分钟值 ⇒ **收盘那一分钟的成交额**,不是收盘价;(6) `cross_max(·,5)` = 日轴 5 日滚动最大(此时 M 维已折成 1),对慢变量近似恒等。合起来 = 「近 5 日里 (收盘分钟成交额 × 30 日平均日内成交曲线的尖峰占比³) 的最大值」,sg=−1 做多它的低端。名字与定义不一致处三个:day_durbin_watson 不是 DW、ts_min(·,1) 不是算子、day_close 不是价格。

**承重的子结构**

- 叶子 `day_close(Amt)`(金额水平):`iso_A` 单独 ut +13.4% / Lshp 1.90,**比完整原式 +8.1% / 1.49 更好**;删掉它之后 C 腿单独跑是死的 —— `only_F_R` valid −17.8% / ut Lshp +0.04,`iso_E` valid −18.6% / +0.05
- B 槽的 30 日跨日平滑 `cross_decay_linear(Amt,30)`:`abl_B`(DW 直接作用在单日原始分钟曲线)ut −3.3% / Lshp −0.60。单日曲线的尖峰占比是噪声,必须先按日平均。平滑**方式**不敏感(cross_max 版 +8.1%、60 日 +8.4%)
- `mul` 这个乘法本身(而不是两条腿的序):`rank_F`(两腿各自 cs_rank 后相乘)ut −0.1% / Lshp −0.01 ⇒ 起作用的是 Amt 的重尾**量级**,不是它的排序;`sub_F_add` / `sub_F_sub` 与 `abl_F`(删掉整个乘法)逐列相同,因为 Amt(1e7 量级)把 C³(≪1)完全压住

**多余的节点**

- `ts_min(·,1)`:窗口 1 = 恒等式。`abl_E` 与 `v_base` 在每一列上逐位相同、ρo 1.00
- 外层 `cross_max(·,5)` 整个 G 槽是自由参数:`iso_F`(删掉)ut +8.5% / 1.55 ≥ 原式 +8.1% / 1.49;`win_G_10` +8.5%、`win_G_15` +8.4%;`sub_G_cross_sum` +8.2%、`sub_G_cross_decay_linear` +8.4%、`sub_G_cross_min` +8.2%、`sub_G_cross_quantile_q25` +8.3%,全在噪声内(只有 cross_argmax/argmin 毁掉,dist 0.00 ✗)
- `pow_3` 不只是多余,是**净损害**:指数阶梯与 ρk 单调同向 —— pow_05 (ρk .90) ut +13.7% → pow_1 (.84) +12.8% → pow_1.5 (.73) +11.4% → pow_2 (.59) +10.0% → pow_2.5 (.46) +8.8% → pow_3 (.34) +8.1%;而 train Lshp 走反方向(1.64→1.96),是拟合在 train 上的节点
- 所有外层形状变换:`rk`(cs_rank)ut +7.6%、`win`(cs_winsor)+8.1%、`rel60`(除以自身 60 日均)+0.7%、`fold_sq` −22.3%、`fold_mean` −25.6%、`mem_zscore5/10` 为负且换手 11~14%;日轴记忆层也没用(`mem_max60` +8.5%、`mem_decay_linear60` +8.9%、`mem_mean10` +8.0%,全在原式 ±1 点内)

**可互换的叶子**

- A 槽的日度折叠算子完全可互换:`day_close` ↔ `day_mean` = `day_sum`(两者逐列相同,ut +10.0% / 1.99)↔ `day_quantile` = `day_median`(+10.0% / 1.94)。A 槽只需要「一个日成交额水平」,`day_close` 不特殊
- C 槽的形状读数可互换、且一次方比三次方好:`sub_C_day_gini`(pow_3 版)ut +12.2% / 1.98、`sub_C_day_close` +13.9% / 1.99、`sub_C_day_hurst` +12.1% / 1.71 —— 任何把 C 压扁或换成别的无尺度形状量的做法都把因子推回已知族(ρk 0.81~0.94)
- **不可互换**:`Amt → Volume` 死(`leaf_Amt_vol` valid −7.4% / ut Lshp 0.59;只换 A 腿的 `fld_Amt_Volume` valid −7.2%)⇒ 丢掉价格就没了,这条腿是金额(规模/流动性)而不是活跃度
- **不可互换**:`Amt → in_pct(Amt,1)` 死(`leaf_Amt_amtchg` ut +0.2%,方向翻成 +1)⇒ 用户提示的「Ret 与成交量变化率同类」在这棵树上不成立,这里要的是**水平**不是变化率

**在哪类股票里有效**

- **次新**(上市不足 250 日,占 7.1%,段等权超额 −28.7%):C 唯一真正发力的地方,且段内净超额随指数单调、**方向与全市场完全相反** —— pow_05 −2.7% < pow_1 +4.1% < pow_1.5 +15.0% < pow_2 +19.1% < **pow_3 +25.3%**(k_known +8.6%)。但全市场书只在该段超配 +4.2pp,所以被稀释到看不见
- **流动的一半**(成交额 20 日分档):`v_base` 段内 −6.4 / −2.0 / −0.1 / **+9.6 / +17.2%**(单调升),而 `k_known` 是 −4.1 / −5.3 / −8.2 / −5.2 / +2.5(几乎处处为零)。原式的桶内选股力恰好长在已知族没有分辨力的那一半
- **大市值端**:市值分档段内 `v_base` 是平的(+7.9 / +2.9 / +1.7 / +7.5 / +5.8),`k_known` 单调降到 **+0.7%** ⇒ 大票那一端(+5.8% 对 +0.7%)是原式唯一比已知族强的地方
- **冻结盘口段**(近 15 日有封板/停牌分钟,占 6.5%,段等权超额 **−67.4%**):原式是全表低配最多的变体(−4.5pp)也是段内唯一不亏的(+0.5%,k_known −10.9%)⇒ C 腿有一部分在兼职当一字板筛子
- **不工作的地方**:清淡档(成交额最低 20% 段内 −6.4%)、科创板(段内 +6.4%,全板块最差,而原式反而超配 +10.4pp —— 纯损失的倾斜)

**什么时候有效**

- **与已知族近乎反相的年份**:`v_base` 逐年 +4.0 / +15.8 / +15.4 / +2.5 / +8.2 / −1.4(2018→2023),`k_known` +17.3 / +10.4 / +6.7 / +16.1 / +24.7 / +18.5。原式的好年份(2019–2020,大票/成长主导)正是已知族最差的两年,反之亦然
- **跌市**:原式是全表唯一在市场近 20 日下跌时更好的变体(+10.4% 对上涨 +6.4%);`k_known` 完全相反(+6.0% 对 +23.0%)
- **高波动 / 高截面离散 / 放量**:+10.3% vs +5.9%(波动)、+10.0% vs +6.3%(离散)、+9.0% vs +7.3%(放量),但这三条所有变体同向,不是原式特有
- **2023 年失效**:原式 2023 年 −1.4%(同期 k_known +18.5%),这是 valid 段 Lshp 只有 0.73 的主要来源

**原因推断**:机制推断:C 读的是「30 日平均日内成交曲线的尖峰占比」,与前期研究「C 九成是开盘第一分钟成交占比」一致 —— 它是一个**投机热度的日内指纹**。(1) 为什么在次新有效:次新票第一年的日内成交曲线极端不稳(开盘巨量、一字板、游资炒作),尖峰占比在这群票里既有分散度又有含义 —— 最尖的那批是被游资追的投机壳,跌得最多,sg=−1 正好躲开;在成熟票里这个量退化成行业/市值的持久标签,没有增量。(2) 为什么在流动半边有桶内增量:成交额桶是按 20 日均分的,桶内挑「当前/收盘分钟成交额最低」= 挑**近期缩量**的票;流动票里缩量是真信息(资金撤出后的短期反转),清淡票里日成交额主要是最小变动价位噪声,所以符号翻转(−6.4% vs +17.2%)。(3) 为什么与已知族时间上反相:已知族挣的是流动性/小市值溢价,在涨市里兑现;C 挣的是投机热度退潮,在跌市/高波动里兑现 —— 这是**状态互补**而不是水平互补,所以低权重叠加(overlay)能略微提夏普却压低净超额。可检验推论:(i) C 的 rank IC 应集中在 `cross_valid_count(day_last(Close),241) < 241` 的子样本内(→ h_base_bk_age vs h_abl_bk_age);(ii) 把缩量显式写出来并限定到流动半边,应复制出 +9.6/+17.2 那一段(→ h_contract*, h_liq40_*);(iii) 把 C 换成显式冻结度 `cross_mean(day_zero_ratio(Ret),30)` 应复制出原式在冻结段/次新段的行为(→ h_C_as_frz)。

**相对已知成交额族**:**没有增量。** 三条独立证据:(1) **残差化**:`res_known`(对 `cs_rank(k_known)` 取截面秩残差)valid **−2.1%**、Lshp **−0.27**、ut 0.89 —— 正交于已知族的那一部分样本外多头腿是负的;`res_liq`(对流动性残差)valid −1.5%,`bk_liq`(流动性桶内秩)valid −1.4% 且 dist 0.20 ✗ 直接出局。(2) **overlay**:`ov_p025` ut +14.3% / 2.22(ρk 0.98,就是 k_known 本身)、`ov_p05` +13.6% / 2.22、`ov_p10` +12.5% / **2.25** —— 最好的一档夏普比 k_known 的 2.22 只高 **+0.03**(噪声带 ±0.3 的 1/10),而净超额低 **2.9 个点**、换手从 3.4% 翻到 **6.7%**,dist 掉到 0.81。(3) **指数阶梯**:表现是 ρk 的单调函数(ρk 0.90→0.34 对应 ut +13.7%→+8.1%),即「还剩多少已知成交额族」= 表现;126 个变体里**没有一个** ut Lnet 超过 k_known 的 +15.4%(最好的 `sub_D_pow_05` 是 +13.7%),也没有一个 ut Lshp 显著超过 2.22。ρk 只有 0.34 看起来独立,但这是个陷阱:低相关加上残差无效 = 正交部分是噪声,不是 alpha。结论:F103 = 「成交额水平族 × 一个在 train 上拟合的尖峰占比权重」,提纯的终点就是去掉权重,而去掉权重之后它就是已知族。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_decay_linear(Amt, 30))…` | base | 10 | +8.1% / +7.2% | +1.49 / +1.26 | 4.0% | +3.53 / +3.18 | +4% +16% +15% +2% +8% +3% +3% +11% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_A_topw_amt` `cross_max(mul(day_topw_mean(Amt, Amt), day_std(in_pct(cross_decay_linear(Amt, 30), 1))), …` | hypo | 10 | +15.6% / +13.5% | +2.47 / +1.53 | 3.8% | +2.96 / +2.34 | +21% +12% +7% +12% +24% +21% +10% +12% |
| `nosc_B_cross_semistd_neg` `cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_semistd_neg(Amt, 30)))…` | substitute | 40 | +12.4% / +10.3% | +2.29 / +1.41 | 1.5% | +2.73 / +1.73 | +8% +10% +9% +9% +25% +16% +3% +13% |
| `seg_lowliq_m` `cs_first_low40(neg(cross_max(mul(day_close(Amt), ts_min(pow_3(day_durbin_watson(cross_dec…` | segment | 10 | +12.0% / +11.0% | +2.25 / +1.90 | 4.0% | +2.87 / +2.59 | +16% +12% +6% +11% +16% +13% +6% +13% |
| `h3_xfrz_then_relstd` `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio…` | hypo | 3 | +19.6% / +15.3% | +3.34 / +1.63 | 3.3% | +3.38 / +2.63 | +26% +15% +13% +17% +26% +21% +12% +15% |
| `h_K_ex_both` `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio…` | hypo | 3 | +18.4% / +15.3% | +3.21 / +1.63 | 3.1% | +3.99 / +2.73 | +24% +14% +11% +15% +26% +21% +12% +15% |

综合全文:`notes/F103_amt_dw_decay/synthesis.md`;回测表与解剖:`./scripts/study.sh table F103_amt_dw_decay s4`。

### 4. 挖掘 #4190(F104)

`day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))`

**它是什么(按算子定义)**:day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt))) 逐层(按函数定义,不按名字):(1) abs_(Amt) 是空操作,Amt≥0 —— abl_A 与 v_base 全列逐位相同、ρo=1.00;(2) nt_cs_mask_top_replace_mean_neg 名字三处骗人:face=nt/axis=S 说明它是在每个(日,分钟)格子里沿**股票轴**做的;_neg 版 = -cs_mask_top_replace_mean(-x),遮的是**最低** 10%(docstring 自己写 "Bottom-band counterpart",名字里的 top 反了);替换值 _mean(x_masked) 且 -mean(-x)=mean(x),所以是**当分钟全市场成交额的截面均值** M[d,m] —— 一条所有股票共用的市场级时间序列。Amt 截面极度右偏,M 落在股票分布的 80~90 分位,对被遮的股票-分钟来说是往上插一根 10~100 倍的尖峰。因此这个算子实际是一个「带巨型旗标的指示函数」:被遮分钟写 M,其余写自己的 A;(3) day_kurt 对混合序列取当日分钟峰度 —— 从不被遮(活跃票)= 自身日内型态的峰度;只被遮几分钟(卡在底十分位门槛上)= 那几根 10~100 倍的离群点统治四阶矩 → 峰度极高;大半分钟被遮(极清淡)= 序列≈市场型态 + 几个很小的自有值 → 峰度回到中等。于是它是**流动性的驼峰型(非单调)函数**,且因为峰度是尺度无关的,**成交额水平被除掉了**。方向 sg=-1(买低峰度)= 买驼峰两端 ⇒ 书是成交额上的**杠铃**(最低档超配 +25.1pp、最高档 +6.1pp、中间三档 -7.3/-12.7/-11.1pp),解剖里完全证实。副作用:M 是市场共用序列,所以因子里还混着「这只票的死分钟与市场繁忙分钟对不对齐」。

**承重的子结构**

- mask 本身定符号:abl_B 删掉 nt_cs_mask_top_replace_mean_neg 后 ut 从 +1.8% 掉到 -5.0%、valid -19.2%,且 ρk 从 +0.26 翻到 -0.35;没有任何别的逐分钟截面算子能替代(nt_cs_winsor -5.6%、nt_cs_demean -5.1%、nt_cs_rank -16.7%、nt_cs_quantile_q50 -28.1%)——关键不是『把截面标准化』,而是『底十分位 → 一个市场尺度的大数』
- mask 之内叶子的压缩,是全表最大的杠杆:ut +1.8%(Amt) → +14.1%(sqrt/pow_05) → +10.0%(log),凸变换 pow_1_5 直接炸(-50.6%,cov 0.23 ✗);ρk 随压缩单调上行 0.26→0.60→0.82,说明压缩拉近 A 与 M、让峰度重新带上成交额水平
- 日轴 reducer 承重但方向与名字相反:换成保尺度统计量(day_std ut +13.0%/Lshp 2.85)或持续性统计量(day_ar1_coefficient +11.2%、day_autocorr_n1 +11.1%、day_q_stat_std +7.6%、day_hurst +4.8%)是原式的 3~7 倍;留着标准化高阶矩(kurt +1.8%、skew +3.3%)就是死的。而这些好替代 ρo 只有 +0.12/+0.04/+0.04/-0.09/-0.19 —— 不是同一条因子,是已知成交额族换了衣服(ρk 0.60~0.85)
- 记忆的核比窗口重要得多:cross_min 5/10/30/60 = +6.2/+6.6/+6.5/+5.8 是平台且唯一 valid 为正(+4.2/+8.1/+9.2/+9.3);cross_zscore 5/10/30/60 崩盘 -28.6~-10.8%、换手 12~33%(重尾量做自身历史标准化 = 纯尖峰探测器)

**多余的节点**

- abs_:Amt≥0,abl_A 与 v_base 逐位相同(+4.8/-5.8/+1.8%,ρo 1.00)
- 外层 cs_winsor:win +4.7/-6.0/+1.7%、Lshp 0.98/-1.27/0.35、ρo 0.99,与 base 无差别(1%/99% 缩尾改不动截面秩)
- 整个 mean / ema / decay_linear 记忆族(5~60 全部窗口):ut +3.1~+4.9%、ρo 0.87~0.99、valid 一律为负 -1.0~-3.8% —— 只降换手,不改对象
- 延长多头半衰期:大表 hlL 取到网格上限 20;旧 rev2 的网格外实验 hl 30/40/60/120 train +5.5/+5.8/+5.0/+3.9、valid -3.9/-2.8/-2.8/-1.1 —— 只省成本,救不活 valid

**可互换的叶子**

- Amt → Volume:ρo 0.72 但 ut -2.4%(leaf_Amt_vol)。认得出是同一个对象,但按股数算的底十分位偏向低价票,价格混淆把它弄坏了
- Amt → in_pct(Amt,1)(量的变化率):方向翻成 +1、ρo -0.16、ut -0.5%(leaf_Amt_amtchg)。这棵树要的是**水平**不是变化率 ——『Ret 与量的变化率同类可互换』在这里不成立,因为这个装置本质是一次截面流动性比较
- mask 内的单调变换是可换的、而且是改进:sqrt == pow_05(同一个算子,大表里重复占了两行,数字完全相同)、log 都保留并改善;唯一不能换的方向是凸变换
- 表里没试的叶子:|Ret|(底十分位变成『市场在动而它不动的分钟』,且 abs_ 在那里不再是空操作)、Close —— 已写进第二批 h_mask_ret_kurt / h_mask_ret_std

**在哪类股票里有效**

- 板块:主板专属 —— 沪主板段内 +4.9%、深主板 +6.9% 为正,创业板 -3.5%、科创板 -6.9% 为负;而已知族四板块全正(+14.8/+20.9/+18.9/+1.4)
- 成交额(20日)五档:段内 -4.0/-6.8/-6.9/-3.6/**+7.4%**,只有最活跃档为正;可书却超配最清淡档 +25.1pp。清淡档自带 +15.1% 段等权超额、最活跃档 -17.8% ⇒ 它在钱所在的段里选股是负的,唯一会选股的段自带 -17.8% 拖累
- 冻结盘口:近15日有冻结盘口的 6.5%(段等权 -67.4%)段内 **+12.1%**,而无冻结的 93.5% 段只有 -0.3% ⇒ 几乎全部选股力都在封板/停牌票里(与 F108『峰度类算子读到的其实是冻结状态』一致),但书对该段低配 -3.3pp
- 上市不足 250 日(7.1%,段等权 -28.7%):原式 -9.7%,有害;而已知族 +8.6%、候选 day_std 版 +7.6%
- 市值/价格:市值最低档 +4.2%、40-60 档 +3.8%,其余 -1.0~-2.5%,没有单调规律(不是规模故事);价格只有最低档 +7.9%

**什么时候有效**

- 逐年 +5.5/+6.4/+1.4/+5.8/-3.9/-8.7(2018→2023):2021 之后转负;同期已知族 17.3/10.4/6.7/16.1/24.7/18.5 稳定,候选 day_std 版 18.6/13.7/6.2/9.4/16.8/13.6 全正
- 成交状态:只在**缩量日**有效 +4.7%,放量日 -1.7% —— 与已知族完全相反(缩量 +11.8% vs 放量 +19.9%)。这是全解剖里最干净的一条状态差
- 截面离散度高 +2.9% / 低 +0.8%;市场上行 +2.6% / 下行 +1.1%;市场波动高 +1.6% / 低 +2.2% —— 这三组都在噪声量级,原式对市场方向和波动几乎不敏感,唯一真正的开关是成交量

**原因推断**:机制推断:mask 的门槛是**截面相对**的(当分钟全市场成交额最低 10%),被标记的人群随市场总成交量漂移 —— 清淡时底十分位确实是真死的盘口(信息),放量时连中等流动性的票也掉进去(噪声);同时替换幅度 M[d,m] 本身随市场量放大,同一只票在放量日峰度会因为**市场级的原因**上升,而尺度无关的统计量去不掉这个市场状态泄漏。这正好解释「只在缩量日有效」。2022–2023 的衰减对应人群变化:创业板/科创板占比上升、20% 涨跌幅与注册制改了封板人群,而原式正是靠封板票吃饭(6.5% 段 +12.1%)、在新板上亏钱(-3.5%/-6.9%)的那一条。更底层的一句话:**多头腿的钱全在 mask 漏进来的成交额水平里,而 day_kurt 的工作恰恰是把这个水平除掉** —— 所以保尺度/持续性的 reader 一换上就赢 3~7 倍,凹变换一加上就赢(它把水平放回来),而原式本身只剩下一个在 93.5% 的正常股票里值 -0.3% 的形态读数。可检验的推论已写进 synthesis.md §3:(a) 换成绝对的死分钟直读应复现 6.5% 段的选股力且不随市场量漂移;(b) 前置凹变换应单调把它推向纯水平因子(已被 sqrt/log/pow_1_5 证实);(c) 先按 nt_cs_rank(Amt) 做截面位置标准化,放量/缩量不对称应消失;(d) 死分钟应当做**剔除筛子**有用、做**排序**没用;(e) day_centroid(masked) 不应为零信息(死分钟与市场繁忙分钟的对齐)。

**相对已知成交额族**:原式:没有增量,确认 none_robust。ρk 只有 +0.26,但正交的那一部分在多头腿上是空的 —— 六条 overlay(已知族 + λ·原式,λ=+0.25/+0.5/+1.0/-0.25/-0.5/-1.0)ut = 13.1/12.4/11.5/10.8/9.0/3.7、Lshp 1.87/1.75/1.62/1.61/1.38/0.61,**全部严格低于基准 15.4/2.22,且随 |λ| 单调变差 ⇒ 任何权重、任何符号都是纯稀释**;res_known -0.4%(valid -7.3%)、res_liq +0.9%、bk_known -2.0% ✗、bk_liq -1.2% ✗。表里没有任何筛子形态。
但增量确实存在,来自 **mask,不来自 reader**:sub_C_day_std = day_std(nt_cs_mask_top_replace_mean_neg(abs_(Amt))),Lnet +12.0/+15.5/+13.0%(基准 +12.6/+22.3/+15.4,valid 低 6.8 点,超出 ±3 噪声,是它的弱点),**Lshp 2.49/3.98/2.85 对基准 1.78/3.46/2.22,两段都高 +0.71/+0.52,超出 ±0.3 噪声**,ρk 0.85、ρo 0.12,逐年全正。解剖给出了原因:mask 把最死的票的 day_std 抬高(大半分钟写着 M ≫ 自身水平),买低 std 的书把它们挤了出去 —— 书落在成交额**第二档**(超配 +43.9pp,最低档只 +5.9pp),而基准是全押最低档(+80.3pp);最低档段溢价最大(+15.1%)但波动与摩擦也最大,第二档 +8.9%。而且候选是解剖里**唯一**五个成交额档段内选股都不为负的一列(-1.5/+1.6/+0.3/+0.3/+1.9),基准是五档里四档为负(-4.1/-5.3/-8.2/-5.2/+2.5);市值五档段内 +13.6/+9.3/+13.0/+7.6/+2.0 也全正;上下行差 +17.2 vs +7.9(基准 +23.0 vs +6.0)⇒ 更少的市场 beta 味道。结论:mask 是一个**可交易的流动性下限**,产物应按「已知成交额族形状更好的一位成员」上报(ρk 0.85),不是一条新因子。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))` | base | 40 | +3.4% / +0.4% | +0.71 / +0.07 | 4.3% | +3.20 / +1.89 | +6% +9% +2% +6% -1% -2% +2% -3% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h_sqrt_std` `day_std(nt_cs_mask_top_replace_mean_neg(sqrt(Amt)))` | hypo | 20 | +15.1% / +12.6% | +2.87 / +1.42 | 3.8% | +2.42 / +2.11 | +20% +13% +7% +13% +21% +19% +9% +13% |
| `sub_A_sqrt` `day_kurt(nt_cs_mask_top_replace_mean_neg(sqrt(Amt)))` | substitute | 20 | +14.1% / +10.3% | +2.18 / +1.94 | 4.1% | +4.83 / +4.31 | +20% +9% +2% +17% +20% +20% +9% +6% |
| `seg_lowliq_m` `cs_first_low40(neg(day_kurt(nt_cs_mask_top_replace_mean_neg(abs_(Amt)))), cross_mean(day_…` | segment | 20 | +11.3% / +12.3% | +1.59 / +1.30 | 4.9% | +2.79 / +1.50 | +13% +5% -1% +12% +24% +19% +9% +11% |
| `h_known_nofrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_flat_ratio(Close), 15))` | hypo | 3 | +18.2% / +14.9% | +3.08 / +1.62 | 3.1% | +4.33 / +3.31 | +24% +13% +11% +15% +25% +21% +12% +15% |
| `h3_known_xlimitup` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_at_max_ratio(Close), 15))` | hypo | 2 | +17.2% / +14.7% | +2.67 / +1.56 | 2.9% | +3.40 / +3.02 | +22% +13% +9% +16% +25% +21% +11% +15% |

综合全文:`notes/F104_kurt_masktop_amt/synthesis.md`;回测表与解剖:`./scripts/study.sh table F104_kurt_masktop_amt s4`。

### 5. 挖掘 #25(F105)

`ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)`

**它是什么(按算子定义)**:按算子源码逐层:A = day_cov(Amt,Amt) —— 同一参数喂进二元协方差 = Σ(Amt−mean)²/count,就是**当日分钟成交额的方差**,库里本来就有 day_var,名字里的「cov」是假协方差;B = cross_max(A,3) 日轴近 3 日最大;C = cross_fangzheng(B,241) 按定义 = cross_mean(B,241)+cross_stddev(B,241),即**近一年均值+标准差的上轨**(布林上轨),不是名字暗示的正规化/标准化 —— 它不去尺度反而把尺度放大一倍,正数重尾序列的年度 std 与年内最大值同阶,所以 C 由过去一年成交额方差最大的那几天主导;D(根)= ts_stddev(C,5),与 cross_stddev 同一内核逐位相同,而 C 的日增量 ≈ (B[t]−B[t−241])/241 变得极慢,所以根读的是「过去一周这条年度上轨动了多少」= |ΔB| 的四重衰减版。合起来:一条绕了四层的**成交额水平**读数,sg=−1 → 多头书买低成交额/低流动性/小市值/低价股。名字与定义不一致两处:(甲) day_cov(x,x) ≡ day_var(x);(乙) cross_fangzheng 是上轨不是正规化。

**承重的子结构**

- Amt 叶子必须以**水平**进来:去掉水平的三族全死 —— rel60(除自身 60 日均值)+5.3%/ρo 0.36/ρk 0.19;mem_zscore 5/10/30/60 = −4.5/−3.0/−2.1/−0.1%;leaf_Amt_amtchg(叶子换成 in_pct(Amt,1) 这个无尺度的分钟变化率)−0.1% utrain 且 sg 翻成 +1。用户提示的「Ret↔量变化率可互换」在这棵树上是反例
- 根必须是**幅度型**归约:ts_stddev +11.8 ≈ ts_var +12.0(单调孪生 ρo 0.99);换成有号/形状型全死 —— ts_delta −9.1%、ts_argmax −1.7(dist ✗)、ts_kurt −14.9(cov 0.39 ✗)、ts_hurst −17.6、ts_pearson/ts_spearman ≈ 0
- 承重的是**原子本身**而不是树:iso_A = day_cov(Amt,Amt) 单独 +15.6/+23.3/+17.8%、Lshp +2.59、LTO 3.8%,是全表第一

**多余的节点**

- cross_max(·,3):abl_B 删掉它 +13.2%/Lshp 2.15(比原式 +1.4)。槽内所有保尺度的替代都落在 ±1 —— cross_sum 12.8 / cross_fangzheng 12.4 / cross_decay_linear 12.6 / q75 12.4 / q25 11.8 / med 11.1 / min 11.1;只有返回下标的 argmax/argmin 打死(−8.3/−4.4)。这个节点是自由参数
- cross_fangzheng(·,241):abl_C 删掉 +13.9%/2.13(比原式 +2.1);sub_C_cross_mean +12.3 ≈ 原式 → 方正里 +cross_stddev 那一半零贡献
- 根 ts_stddev(·,5):iso_C(留下全部下层、只删根)+12.3%/1.98 ≈ 原式 +11.8/1.96,而 LTO 从 3.6% 降到 1.4% —— 根只贡献换手
- isolate 阶梯全程单调下坡:iso_A +17.8/2.59 → iso_B +17.2/2.52 → iso_C +12.3/1.98 → v_base +11.8/1.96,上面每一层都在扣分
- cs_winsor 是 no-op(+11.9/1.97)→ 书顶不由重尾驱动
- 三条窗口梯子都没有平台:win_D 5/10/20 = 11.8/11.6/12.0;win_B 3/5/10 = 11.8/11.1/10.9;win_C 241/60/30 = 11.8/11.4/12.5(30 最好、ρk 0.72→0.83)。全在 ±3 噪声内 = 纯水平代理的签名
- memory 一族只是在替代半衰期:最好的 mem_max30 +12.8/2.17(hlL 10→1),只比原式 +1 点(噪声内)

**可互换的叶子**

- **结论:这棵树的叶子不可互换** —— 这是本次最干净的否定结果。用户提示的「分钟收益 Ret 与成交量变化率是同一类东西、很多时候可互换」在这里是反例:leaf_Amt_amtchg(把 Amt 换成 in_pct(Amt,1) 这个无尺度的分钟变化率)从 +11.8% 掉到 **−0.1% utrain 且 sg 翻成 +1**。因为这棵树要的不是日内动态,只是尺度
- Amt → Volume 退化但不死:leaf_Amt_vol(day_cov(Volume,Volume))+8.2/+3.8/**+6.9%**(valid 几乎归零);fld_Amt_Volume(day_cov(Volume,Amt))+8.6/+13.0/**+9.9%**,正好在中间 → Amt = 价×量 里「价」这一维贡献约一半的多头腿,与解剖里价格最低 20% 超配 +13.6pp / 该段等权超额 +7.0% 吻合
- B 槽的**算子**可互换(不是叶子):7 个保尺度的 3 日归约(cross_sum/fangzheng/decay_linear/q75/q25/med/min)全落在 +11.1~+12.8,与原式 +11.8 无法区分;只有返回下标的 cross_argmax/argmin 把它打死(−8.3/−4.4)
- D 槽只在**单调孪生**之间可换:ts_stddev ↔ ts_var(+11.8 vs +12.0,ρo 0.99)。其余全死
- 已提出但未验证的叶子替换(写进 hypo):h_leaf_logchg_var 用 in_logchg 替 in_pct(排除「in_pct 右尾无界、左尾止于 −1」这个替代解释)、h_leaf_ret_var_m30 = cross_mean(day_var(Ret),30)(经典特质波动,量「多头腿里有多少其实是低波动」)、h_leaf_close_var_m30(把 Amt 里的价那一维单独拎出来)

**在哪类股票里有效**

- 钱全在「段倾斜」不在段内选股:成交额(20日)最低桶超配 **+55.2pp**、该段等权超额 **+15.1%/年**(最高桶 −17.8%),而**段内**净超额 = −4.7/−2.9/−0.0/+4.2/+1.2 —— 低桶是负的。k_known(−4.1/−5.3/−8.2/−5.2/+2.5,超配 +80.3pp)与 iso_A 完全同形,整个成交额族共享这一点
- 流通市值五分桶的段内却处处为正(+5.4/+4.8/+9.0/+5.0/+2.9,超配 +15.4pp→−17.7pp)→ 两个效应叠加:(i) 小市值倾斜,(ii) 同市值内选低换手。(ii) 是唯一真实的段内能力,每桶值 +3~+9%/年。真实身份 = 一条披着流动性外衣的**换手率水平**因子
- 板块:深主板段内 +16.0(iso_A +22.5)> 创业板 +12.1 > 沪主板 +11.6 >> **科创板 −15.7%**(iso_A +4.9、k_known +1.4)
- 上市不足 250 日(占 7.1%,段等权超额 −28.7%):v_base **−23.2%** vs k_known +8.6% / iso_A +6.1% —— 差 30pp;近 15 日有冻结盘口(占 6.5%,段等权超额 −67.4%):v_base −11.5% vs iso_A +10.4% —— 差 22pp
- 价格:多头书超配价格最低 20%(+13.6pp),该段等权超额 +7.0% —— Amt = 价×量 里「价」这一维贡献约一半(leaf_Amt_vol 只 +6.9%/valid +3.8%,fld_Amt_Volume +9.9%)

**什么时候有效**

- 年:2018 +13.6 / 2019 +6.1 / 2020 **+3.2**(最差,核心资产年)/ 2021 +9.7 / 2022 **+26.1**(最好,微盘年)/ 2023 +11.9
- 市场近 20 日上涨 +18.0% vs 下跌 +4.2%;市场波动高于中位 +15.7% vs 低于中位 +8.0%;截面离散度高 +15.5% vs 低 +8.2%;放量 +16.5% vs 缩量 +7.9%
- **但这些状态依赖不属于这条因子**:k_known 的形状一模一样(2020 +6.7 / 2022 +24.7;涨 +23.0 vs 跌 +6.0;高波 +18.5 vs 低波 +12.4;放量 +19.9 vs 缩量 +11.8),其余八个被解剖的变体也一样 → 择时属于小盘/流动性溢价,不属于 F105。所以这一批**刻意不提市场状态门控**,那会是凑数

**原因推断**:机制推断(本次最有价值的发现):十个被解剖的变体里,次新/科创板/封板三段的损伤与**表达式是否含 ts_stddev(·,5)** 完全对应 —— 含它的 7 个全崩([0] −23.2/−15.7、[4] −18.9/−11.7、[5] −19.7/−5.2、[6] −15.9/−16.4、[7] −13.5/−22.2、[8] −20.4/−14.8、[9] −24.5/−10.2),不含它的 3 个全不崩([1] +8.6/+1.4、[2] +6.1/+4.9、[3] +6.1/+6.9),7比7 / 3比3。**不是 241 窗口的锅**:abl_C 根本没有 241 窗口,科创板却最差(−22.2%)。原因:ts_stddev(X,5) 量的是日间**抖动**;次新股(注意力阶段放量缩量)、科创板(20cm 涨跌幅 + 薄流通盘)、刚封板或停过牌的票(零成交日与巨量日交替),它们的日成交额方差序列本身就抖 → 抖动大 → sg=−1 把它们压到书底。但在这两段里**抖动大恰恰是「正在被炒」的标志**(A 股短期会延续),抖动小是「已经凉透还在继续凉」,所以段内抖动的排序方向与水平**相反**;水平(iso_A)能活是因为它仍主要在说「这只票有多大」,抖动只是一个把噪声放大的导数。次要机制:rolling_windows 左侧补 NaN、nanmean/nanstd 只用现有点,所以 k<241 个有效日的票年度上轨是 k 点估计、**每天都因重新估计而跳**,根量的正是这种跳(win_C_30 +12.5 与 abl_C +13.9 都与「窗口越短/没有越好」一致)。可检验推论已写成假设:(a) h_gate_newlist 用 cross_valid_count 剔短历史应得 +1.5~+2.5 点,若 <+1 点机制被否;(b) h_gate_both_atom 把同样剔除器加在 iso_A 上应几乎不涨(对照组,若也涨同样多说明剔除器只是个小盘筛子,机制故事不成立);(c) h_newlist_tilt_atom vs h_newlist_tilt_churn 在次新段内对打,差距应 ≈ 30pp = 方向反转的直接检验。

**相对已知成交额族**:**增量 = 0,按选拔口径应当否掉。** (1) ρk(v_base)=+0.72,而 v_base(+9.3/+18.2/+11.8%,Lshp 1.96)在 train、valid、两条腿、两个分段维度上全面输给 k_known(+12.6/+22.3/+15.4%,Lshp 2.22)。(2) 正交部分没有价值:res_known +2.3%/Lshp 0.51;bk_known +2.4%/0.50(dist 0.20 ✗);对流动性中性化同样是零:res_liq +3.8/0.85、bk_liq +3.0/0.64(dist 0.20 ✗)。(3) 叠加也不行:ov_p025 +15.0/2.20、ov_p05 +14.6/2.18、ov_p10 +14.5/2.19,**全部 ≤ k_known 单独的 +15.4/2.22**;负权重更差(ov_m025 +10.3、ov_m05 +5.9、ov_m10 −4.5)。**没有任何混合权重能改进已知族。** 全表里唯一值得记一笔的 iso_A = day_cov(Amt,Amt) ≡ day_var(Amt) = day_std(Amt)² 虽然 +17.8%/2.59 是全表第一(比 k_known 高 2.4 点,在 ±3 噪声内不构成改进),但 **ρk = 0.97 = 同一条因子换了个写法**(一个节点 vs 30 天平滑),也不是候选。一条方法论结论:中性化之所以全是零,很可能是**中性化错了对象** —— 全部分析指向「同市值内选低换手」,而立方体没有流通市值字段。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)` | base | 3 | +11.8% / +8.9% | +1.96 / +1.04 | 6.7% | +3.03 / +2.24 | +14% +6% +3% +10% +26% +16% +5% +8% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_xfrozen_tail75` `cs_last_high20(neg(cross_tail_mean_q75(day_cov(Amt, Amt), 30)), cross_max(day_zero_ratio(…` | hypo | 2 | +19.0% / +14.6% | +3.27 / +1.60 | 4.0% | +4.54 / +3.56 | +25% +16% +12% +16% +25% +20% +12% +14% |
| `seg_xfrozen_m` `cs_last_high20(neg(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241), 5)), …` | segment | 5 | +13.6% / +10.1% | +2.77 / +1.20 | 6.1% | +3.64 / +3.02 | +16% +12% +6% +12% +23% +16% +5% +11% |
| `iso_A` `day_cov(Amt, Amt)` | isolate | 10 | +17.8% / +14.0% | +2.59 / +1.54 | 3.5% | +2.97 / +2.71 | +24% +13% +8% +17% +26% +21% +10% +13% |
| `h3_xfrozen40_known` `cs_last_high40(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | hypo | 2 | +14.8% / +15.4% | +2.81 / +1.70 | 4.0% | +3.57 / +2.85 | +22% +16% +7% +13% +16% +16% +14% +16% |
| `h3_scr_atmax_known` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_at_max_ratio(Close), 15))` | hypo | 2 | +17.2% / +14.7% | +2.67 / +1.56 | 2.9% | +3.40 / +3.02 | +22% +13% +9% +16% +25% +21% +11% +15% |

综合全文:`notes/F105_std_fangzheng_covamt/synthesis.md`;回测表与解剖:`./scripts/study.sh table F105_std_fangzheng_covamt s4`。

### 6. 手写 erm_mag_gap_1m(F106)

`sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(…`

**它是什么(按算子定义)**:按算子定义(study.sh src)逐层:A=day_quantile(Ret,.95)、L=day_quantile(Ret,.05) 是当天 241 个分钟收益的 95%/5% 分位数(torch.nanquantile,沿分钟轴);B=is_gt(Ret,A)、M=is_lt(Ret,L) 是严格越界分钟的 0/1 掩码(is_gt 返回 .int() 不是 bool);E=day_sum(select_where(B,Ret,0))、P=day_sum(select_where(M,|Ret|,0)) 是尾内幅度和;F=day_sum(B)、Q=day_sum(M) 是尾内分钟数;I=E/(F+1e-6)、T=P/(Q+1e-6) 是 ES±;K=I/(A+1e-6)、W=T/(|L|+1e-6) 是 ES/VaR;X=K−W。名字与定义不一致四处:(1) 两个 +1e-6 写法相同、作用相反 —— 计数分母那个只是除零保护(|U|=0 时分子也是 0,读数 0/1e-6=0),分位数分母那个才是整条因子(上涨分钟 ≤5% 时 A=0,K=ES⁺×10⁶,这个 eps 带量纲、比一个 tick 小三个数量级);(2)「mag_gap」在它有方差的地方恰好不含幅度:常规区间 X 是齐次度 0 的无尺度量,被钉在高斯值 1.254 附近(std≈0.10),只有塌缩区间才变成齐次度 1、读「那几分钟跳多大」;(3)「1m」不是时间结构,树里没有任何日轴算子,真实回看 1 天,全部时间结构来自口径的因果 EMA(hl 20,一个 +2000 的塌缩日要约 250 个交易日才衰减回常规量级);(4) day_sum 写在该写均值的位置(靠后面除以计数变成均值),abs_ 纯属装饰。另:create_like(Ret,0) 的 dtype 由常数 0 推成 int64,create_like(q,1e-06) 推成 float32,两个常数叶子不是同一类型。

**承重的子结构**

- 分位数当分母 + 1e-6(节点 J 与 V):abl_G 把 A+1e-6 换成 A+A,结构一点没动、只抹平塌缩 → 公布的多空夏普 LS tr 从 +2.82 掉到 +0.06、ρo 变 −0.26、ut −3.6%;abl_J(除以 A)LS tr −1.59;abl_V(除以 |L|)LS tr −1.14;abl_R(1e-6 换成 L,|L|+L≈0)直接全 NaN、cov 0.00
- 口径的 EMA 半衰期(不在树里,但决定一切):v_base train 半衰期网格 [Lnet, Lshp, LS] hl0 [−67.2%, −19.51, −25.67] → hl3 [−25.8%, −8.16, +0.09] → hl20 [−6.9%, −2.15, +2.82],LS 在 hl≥3 才转正 → +2.82 是线性 EMA 把稀疏大数拖成缓慢状态造出来的,不是任何一天的信号;对照 k_known 网格单调相反(hl0 +12.6% → hl20 +8.4%),它才是真的日频持续状态
- select_where 的掩码必须带幅度而不是计数:abl_D(上尾分子 Σ 幅度→计数)ut −32.7%、Lshp −4.48、LS −3.56、ρo −0.52;abl_O(下尾同样)ut −27.6%、LS −2.49、ρo −0.14
- 幅度本身 —— 任何抹掉幅度的外层变换都塌:rk(EMA 前 cs_rank)ut −12.9%、换手 2.4%→15.3%;win(EMA 前 cs_winsor)−9.6%、换手 13.1%;rank_X(两腿各自排名再相减)−10.4%、LS tr −1.01 → 常规区间的尾部形状没有多头信息,全部内容是塌缩日的带符号幅度

**多余的节点**

- abs_ 的两处:sub_U_neg(abs_→neg)与 sub_N_neg,ρo = +1.00、Lnet/Lshp 与 v_base 逐位相同 —— 取绝对值的对象本来就是负的,不携带信息
- 计数分母的 +1e-6:sub_H_sub / sub_S_sub(+1e-6 → −1e-6)与 v_base 逐位相同;abl_H(整个删掉)ut −5.7%、ρo +0.98;abl_S ut −7.8%、ρo +0.84
- 整个计数分支都可以删:only_H_R(把 F+1e-6 换成 1e-6)、sub_F_day_first/last/close(计数的 day_sum 换成取某一分钟的掩码值)ut +1.5%、valid +10.4~+10.8%、ρo +0.57 —— 全表非 overlay 里最好的一族
- 两条腿是严格镜像构造:abl_N(分子去 abs_)与 sub_X_add(末端 sub→add)逐行相同(−3.2%/−3.3%/−3.2%、Lshp −0.51/−0.52/−0.51、ρo +0.47),代数上确实等价,是一个内部一致性校验
- 在 EMA 之上再加一层线性日轴记忆:cross_mean / cross_ema / cross_decay_linear(5/10/30/60)共 12 行 ρo +0.85~+0.99、ut −3.0~−5.4%,是同一条因子

**可互换的叶子**

- Ret → in_pct(Amt,1)(leaf_Ret_amtchg):方向翻正、Lnet tr/va/ut −1.7%/+9.4%/+1.5%、Lshp +0.20、ρo −0.10 而 ρk +0.69 —— 换完就走掉三分之二的路变成已知成交额族
- Ret → in_pct(Volume,1)(leaf_Ret_volchg):ut +1.1%、ρo −0.11、ρk +0.69,与上一条几乎同一条因子
- Ret → in_pct(Close,5)(leaf_Ret_ret5):ρo +0.57、ut −7.4%、Lshp −1.77,是同一条因子的稍差版本 → 不存在采样频率的平台
- Ret → in_pct(Vwap,1)(leaf_Ret_vwapchg):ρo +0.43、ut −9.4%
- Ret → in_logchg(Volume,1)(leaf_Ret_logvol):ut −10.1%、换手 13.5%、ρk 只剩 +0.38 → 带着 in_pct 无界右尾的那部分才是成交额族的内容,换成对数(有界左尾)就死掉
- 计数分支的 day_sum → day_first / day_last / day_close:三行数字完全相同(ut +1.5%),说明这一支取哪一分钟都一样

**在哪类股票里有效**

- 23 个股票段里 22 个段内为负;唯一的正数是「近 15 日有冻结盘口(封板/停牌)」:段内 +18.2%,该段占 6.5%、自身等权超额 −67.4%/年,而全市场多头书还超配它 +4.6pp —— 它唯一的选股力在一个不该进的段里
- 干净段(93.5%、自身等权 +3.7%)段内 −6.9%、书低配 −4.6pp —— 书的绝大部分在它主动做错的那个段里
- 不是规模/流动性/低价因子:流通市值五档段内 −5.8/−7.4/−13.1/−11.3/−7.8(书权重只在 −4.4~+4.3pp)、成交额(20日)五档 −5.3/−9.5/−9.7/−12.5/−6.9、价格五档 −5.3/−10.9/−10.6/−8.7/−8.5,全部为负且无单调倾斜
- 板块:科创板最差 −23.6%(占 4.0%,而该段自身等权超额是四个板块里最好的 +4.1%);沪主板 −6.9、深主板 −5.8、创业板 −7.8;次新(上市不足 250 日,7.1%,自身等权 −28.7%)−15.0%
- 机制推断:塌缩条件「某一侧分钟数 ≤5%」的现实对应物是封板钉价 / 停牌前后 / 3 元以下的 tick 网格(探针:日波动 0.6% 时 2 元股 92% 的日子右侧塌缩、3 元股 66%、5 元以上 0);sg=−1 → 多头腿买的是下跌侧塌缩的票 = 刚封过涨停板的票,它是一条彩票需求(MAX 效应)代理,对多头反、对空头对(底腿 tr −27.9%),而空头端次日买不进
- 可检验推论:干净段 −6.9% 来自 EMA 跨 250 天的记忆,排序由几周到几个月前的封板残留决定 → 买的是封板后的反转输家;冻结段 +18.2% 应当只来自「价钉住但成交额还在变」的封板排队子类,而不是停牌/无成交(已写成 h_flatdiff_m30)

**什么时候有效**

- 六年全负:2018 −9.2%、2019 −6.0%、2020 −8.5%、2021 −4.0%、2022 −0.6%、2023 −7.2%(年化净超额)
- 市场近 20 日上涨段(753 天)−7.2% 比下跌段(586 天)−3.7% 更差 —— 与「买刚封过板的票在涨势里反转最狠」一致
- 没有任何市场状态救得了它:市场波动高/低 −5.6%/−6.0%,截面离散度高/低 −6.2%/−5.3%,放量/缩量 −5.4%/−6.1%,全部落在 −5~−6%
- 对照:abl_M(全表唯一多头腿稳定为正的非 overlay 变体)六年全正(+1.9/+5.5/+4.1/+0.7/+3.7/+5.6),上涨段 +7.4% 对下跌段 −0.6%,但那是流动性倾斜不是选股(见 adds_over_known_family)

**原因推断**:原式是「最近有没有一天几乎只往一个方向走、那几分钟跳多大」的一年期线性记忆。承重的只有「分位数当分母 + 1e-6」这一个节点:上涨(下跌)分钟不足 5% 时分位数落到 0,读数被放大 10⁶ 倍,排序由这些塌缩日的带符号幅度决定;abl_G 只抹平这一件事(结构一点没动)就把公布的多空夏普 +2.82 变成 +0.06、ρo 变成 −0.26。塌缩日在 A 股就是封板钉价 / 停牌前后 / 低价股 tick 网格,所以这条因子等价于一个彩票需求(MAX 效应)代理:多头腿买刚封过板的票(反转输家),空头腿方向对但次日买不进。多头腿在 train/valid/utrain 三段全负(−6.9%/−3.2%/−5.8%,Lshp −1.91),半衰期网格每一点、毛和净全负,152 个变体里没有一个的多头腿接近基准 +15.4%。全市场 23 个段里它只在 6.5% 的冻结盘口段会选股(段内 +18.2%),而那个段一年亏 67.4%;在占书绝大部分的 93.5% 干净段里段内 −6.9%。结论类型 = 分辨,与前四轮一致,但「承重在哪一个节点」和「在市场的哪一段有效」这两件事从推断升级为了全市场实测。

**相对已知成交额族**:没有增量。(1) ρk 只有 +0.01(近乎正交),但六条 overlay 全部严格差于基准单独、且随 |w| 单调恶化:ov_p025 +12.6%(ΔLnet −2.8pp)、ov_p05 +11.6%、ov_p10 +10.3%、ov_m025 +10.7%、ov_m05 +9.0%、ov_m10 +6.2%(ΔLnet −9.2pp)—— 两个方向都伤、幅度随权重增大,是稀释不是方向搞反。(2) res_known −12.2%(Lshp −2.26)、bk_known −12.3%、res_liq −11.7%、bk_liq −12.1%,换手全从 2.4% 炸到 15.4%,正交化之后什么都没剩(bk_* 还因 dist 0.20 不过门槛)。(3) 本轮解剖给出的新事实解释了为什么:基准 k_known = cross_mean(day_std(Amt),30) 的多头腿本身是段间倾斜而不是段内选股 —— 它在成交额五档的段内是 −4.1/−5.3/−8.2/−5.2/+2.5(四档为负),靠超配最低成交额档 +80.3pp(该档自身等权超额 +15.1%/年)拿到 +15.4%。全表唯一多头腿稳定为正的非 overlay 变体 abl_M(ut +3.4%、Lshp +0.59、换手 2.2%、六年全正、ρk 只 +0.06)在成交额五档段内五档全负(−11.8/−8.5/−6.3/−2.8/−5.4),靠超配最低档 +26.2pp、次新 +16.9pp、科创板 +29.5pp 拿到正数 —— 同一个机制的更弱版本。所以在这里低 ρk 不等于有增量:能拿正数的 F106 变体都是在复制基准自己的低流动性倾斜,而不是在选股。推论(已写成第二批的 E 族):要对基准有增量,得加在低成交额桶内部,因为它在那儿不选股。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Re…` | base | 60 | -3.4% / -0.1% | -1.22 / -0.02 | 1.0% | +2.91 / +3.11 | -6% -2% -10% -1% +1% -3% +1% +0% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h_zero_minus_liq` `sub(cs_rank(neg(cross_mean(day_zero_ratio(Ret), 30))), cs_rank(cross_mean(day_sum(Amt), 3…` | hypo | 0 | +12.1% / +15.5% | +2.08 / +1.70 | 3.1% | +2.47 / +1.80 | +20% +16% +9% +7% +9% +12% +11% +20% |
| `seg_lowliq_m` `cs_first_low40(neg(sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), …` | segment | 60 | +10.1% / +9.3% | +1.57 / +1.18 | 2.1% | +1.60 / +0.78 | +8% +4% +0% +12% +23% +18% +2% +11% |
| `abl_M` `sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Re…` | ablate | 20 | +3.4% / +5.7% | +0.59 / +0.77 | 2.2% | +2.00 / +1.37 | +2% +5% +4% +1% +4% +8% +3% +5% |
| `h3_xfr_zero40` `cs_last_high40(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | hypo | 2 | +14.8% / +15.4% | +2.81 / +1.70 | 4.0% | +3.57 / +2.85 | +22% +16% +7% +13% +16% +16% +14% +16% |
| `h3_xfr_atmax` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_at_max_ratio(Close), 15))` | hypo | 2 | +17.2% / +14.7% | +2.67 / +1.56 | 2.9% | +3.40 / +3.02 | +22% +13% +9% +16% +25% +21% +11% +15% |

综合全文:`notes/F106_erm_mag_gap_1m/synthesis.md`;回测表与解剖:`./scripts/study.sh table F106_erm_mag_gap_1m s4`。

### 7. 挖掘 #613(F107)

`abs_(cs_demean(day_skew(Low)))`

**它是什么(按算子定义)**:abs_(cs_demean(day_skew(Low)))。逐层按代码:Low 是分钟 K 线最低价,是**价格水平**(正、日内相对离散只有 0.5%~5%),不是收益;day_skew(Low) 沿分钟轴取这 241 个价格水平的偏度 = **日内价格路径的形状不对称**(与下行尾部风险无关);cs_demean 减的是**全市场当日 nanmean 再广播**(nd_cs.py:113),中心不分板块不分市值;abs_ 取绝对值。所以信号 = 「这只票今天的日内路径形状离今天全市场平均形状有多远」,是个两侧对称的**异常度**;方向 −1 → **多头腿买「路径形状最平庸」的票**,本质是中心度 / 随大流筛子。名实不符四处:① 名字像下行尾部风险,实际是路径形状;② 名字里没有一个字说它是折叠出来的中心度因子,而这就是全部内容;③ pow_05(x)=sign(x)·abs(x)^0.5 保号(e≤1 分支),所以 sub_C_pow_05 其实是 iso 不是 sqrt,而 sqrt(x)=sqrt(abs(x))、log(x)=log(abs(x)) 都单调于信号;④ 最有后果的一处:day_gini 喂给正的、紧的价格水平时 ≈ c·σ/μ(近似高斯时 σ/(μ√π)),是**无尺度的日内相对波动,不是集中度**。

**承重的子结构**

- abs_(折叠)本身:去掉它 iso_B = cs_demean(day_skew(Low)) 塌到 −31.9% utrain / Lshp −4.25;且 iso 的空头腿 tr +11.0 / va −1.0 —— 原始偏度**两头都跑输、中间跑赢**,U 型是真的,折叠正是在吃这个
- 折叠绕的那个中心必须是当日截面均值:去掉 cs_demean → abl_B = abs_(day_skew(Low)) −5.4%,**比什么都不做更差**;abs_(cs_winsor(A)) −6.5% 复证
- 折叠只许做一次:fold_sq −1.4%、fold_mean −4.4%、fold_rank −7.9%,折已折过的距离全塌
- day_skew 这个原子本身**不承重也不出活**:换成 day_gini 变成另一条因子(+8.7%,ρo 0.27),换成路径形状家族里的任何别的算子全废(day_kurt −2.7 / day_hurst −5.0 / day_autocorr_n1 −4.9 / day_ar1 −5.7 / day_argmax −3.4 ✗ / day_argmin −5.2 ✗)

**多余的节点**

- 外层所有保序变换互相等价、全是同一件事:abs_ / pow_2 / sqrt 三者秩等价(v_base +1.7 / sub_C_pow_2 +2.3 / sub_C_sqrt +1.5,ρo 0.92~0.97)
- cs_normalize 的除以标准差是正仿射 → abs_(cs_normalize(A)) 与原式**完全秩相等**(+2.0%,ρo 0.99)。这四行合起来是本因子上的 ±3pp 噪声标尺,不是四个发现
- 输出端 cs_winsor(win +1.6%)和输出端 cs_rank(rk +0.7%)都在噪声内 = 多余
- 日轴记忆的窗口长度是多余的:cross_ema/mean/decay_linear 的 5/10/30/60 共 12 行全部落在 +5.0~+6.6%,窗口跨 12 倍数字不动 —— 这是**换手平台不是视界平台**,LTO 从 10.9% 降到 2.8~5.8%,+4~5pp 全是省下的成本
- 最小的诚实写法:A 离当日截面均值的距离,再也删不动

**可互换的叶子**

- Low → Close:+1.9%(ρo 0.95)
- Low → Open:+2.1%(ρo 0.95),五个里名义上最高的一个,仍在噪声内
- Low → High:+0.8%(ρo 0.93)
- Low → Vwap:−0.5%(ρo 0.95),最差,自洽:Vwap 是分钟内均价,把路径磨平了
- 结论:五个价格水平叶子**全可换、而且全接近零**(−0.5 ~ +2.1%),「Low」没有任何专属信息,它读的是路径不是最低价。真正没试过的互换是把价格水平换成变化率:day_skew(Ret)、day_skew(in_pct(Close,5))、day_skew(in_logchg(Amt,5)) —— 已写进第二批 G 组

**在哪类股票里有效**

- 哪儿都不真正有效:按成交额(20日)五档的**段内**净超额 = −8.1 / −6.4 / −3.7 / −1.6 / −2.4%,**每一档都是负的**,而全市场多头书 +1.7%。书对最低成交额档超配 +16.5pp,而该档的段等权超额是 +15.1% → **多头腿的净超额 100% 来自流动性倾斜,控住流动性后它在每个桶里都亏钱**
- 所以四行中性化一起翻负:bk_liq −2.5 / res_liq −2.7 / bk_known −3.3 / res_known −3.4%(train/valid 同号)
- 形状上是倒 U,在截面的「中间」还能看,两头崩:流通市值五档段内 +1.4 / +3.3 / +5.3 / −3.3 / −6.5;价格五档 −3.6 / +1.9 / +1.8 / +1.9 / −8.1
- 被主动毁掉的一段是科创板:段内 −24.3%(占 4.0%、段等权 +4.1%、书还超配 +0.8pp),所有变体在那儿都坏(gini −19.9、记忆 −11~−22、已知族只有 +1.4)
- 唯一真选到股的一段是冻结盘口(近 15 日有封板/停牌,占 6.5%,段等权 −67.4%):原式段内 **+8.5%**;但**所有记忆版在那一段 −23.7 ~ −40.5%**(已知族 −10.9%)
- gini 分支处处相反:成交额五档段内 +5.9 / +0.6 / +0.7 / +3.0 / **+10.7%**(全正、随流动性上升,倾斜很小);上市不足 250 日段内 **+14.8%**(全表最好,原式 −3.2);创业板段内 +10.8% 且是全表唯一超配创业板的书(+12.1pp)

**什么时候有效**

- 逐年无趋势、骑在零上:2018 +4.1 / 2019 +2.4 / 2020 +1.9 / 2021 **−3.9** / 2022 +0.6 / 2023 +7.1
- 它其实是个市场方向赌注:市场近 20 日上涨 +6.2% 对下跌 **−4.1%**;放量 +5.6% 对缩量 −1.5%;市场高波动 +4.0% 对低波动 −0.6%。一条超配低流动小票的多头书在涨势/放量里赚、在跌势里还回去 —— 流动性风险载荷的形状,不是 alpha
- 截面离散度高/低 +2.0 / +1.4 —— 无差别,说明它不是靠截面分散度吃饭
- gini 分支的时段特征完全不同、而且更像真东西:下跌市 **+7.7%**(全表唯一不塌的,原式 −4.1、记忆 −0.2~−1.6)、市场高波动 **+14.7%** 对低波动 +2.8%、放量 +13.3% 对缩量 +5.0%。与「相对波动」的读法一致:高波动/放量时截面相对波动分布被拉宽、信息量大
- 但 gini 逐年单调衰减:2019 +15.7 → 2020 +10.4 → 2021 +4.7 → 2022 +4.3,配合 train→valid 夏普 2.39 → 1.26(超出 ±0.3 带)

**原因推断**:机制推断:day_skew 作用在**稀疏的分钟价格路径**上,主要读的其实是「今天在几个价位上成交过」—— 薄票的分钟最低价序列是一条台阶,偏度由台阶份额决定,跟「路径形状」没关系。所以它在做一个嘈杂的**薄度排序**,把多头书推向低成交额的票;一旦流动性固定,剩下的「形状最像大盘」只是「今天跟着指数走、没有特异资金」,没有理由预测明天,还要为此付 10.9% 的日换手。科创板那一段的塌陷是同一条逻辑的另一面:科创板 20% 涨跌幅、价位高、票又新,而全局 cs_demean 的中心由 96% 的 10% 涨跌幅票定,「坐在全市场平均偏度上」的科创板票其实是一只**不典型**的科创板票 —— 中心错位。冻结盘口段原式 +8.5% 而记忆版 −23.7~−40.5%,也自洽:钉住的一天 day_skew 退化成极值、当天就被排出多头书,而 EMA 拿着一只现在已经钉住的票的「过去很平庸」评分继续持有。**可检验推论(已写进第二批 E 组)**:(1) 直接量薄度的原子(day_zero_ratio / day_flat_run_max / cross_valid_count)按同样方式折叠,应复现甚至超过原式;(2) 一条**裸的**薄度水平 cross_mean(day_zero_ratio(Ret), 30),不折叠,应能复现记忆家族的 +5~6%;(3) 若中心错位的推断成立,把全局中心换成流动性/价位条件中心(A 组)应同时抬高段内并杀掉倾斜。

**相对已知成交额族**:**零增量,四条彼此独立的证据。** ① ρk 只有 +0.28,它不是已知族本身;② 但剥掉已知族之后多头腿**翻负**:res_known −3.4%、bk_known −3.3%(两段同号),换裸流动性控制一样(res_liq −2.7、bk_liq −2.5);③ overlay 阶梯**从家族单独开始单调下坡**:k_known +15.4 → w=0.25 的 +13.6 → w=0.5 的 +13.1 → w=1.0 的 +12.5,负权重更差(+10.7 / +8.3 / +4.9),**没有任何权重让混合超过家族单独**,最好的 ov_p025 的 ρk 已经 0.96(就是家族掺了 4% 的水);④ 段内分解说明了为什么:家族的边**就是**那个流动性倾斜(k_known 对最低成交额档超配 **+80.3pp**、LTO 3.4%),原式是同一个倾斜的更弱、贵 3 倍的版本(LTO 10.9%)。这与上一轮留出段 f_m20K − f_K = −6.12pp 的判决从完全不同的路径复现了一遍。全表唯一有独立内容嫌疑的只有 gini 分支(ρk 0.33、utrain 夏普 2.07 对家族 2.22),但它 valid 净超额比家族低 17pp、夏普衰减超噪声带,**是线索不是候选**,其增量三件套已写进 H 组待测。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `abs_(cs_demean(day_skew(Low)))` | base | 60 | +4.3% / +4.7% | +0.90 / +1.18 | 4.5% | +2.89 / +2.46 | +6% +4% +3% -0% +3% +6% +11% +2% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_blend_own2_ema30` `add(cs_rank(cross_ema(abs_(cs_demean(day_std(Ret))), 30)), mul(cs_rank(cross_ema(abs_(cs_…` | hypo | 1 | +13.6% / +12.5% | +3.74 / +2.39 | 4.2% | +3.70 / +3.19 | +14% +20% +20% +9% +8% +10% +7% +17% |
| `seg_lowliq_m` `cs_first_low40(neg(abs_(cs_demean(day_skew(Low)))), cross_mean(day_sum(Amt), 30))` | segment | 60 | +11.4% / +8.1% | +1.73 / +1.01 | 2.1% | +1.32 / +1.21 | +11% +5% +3% +11% +23% +19% +0% +10% |
| `mem_ema30` `cross_ema(abs_(cs_demean(day_skew(Low))), 30)` | memory | 5 | +6.6% / +7.0% | +1.31 / +1.65 | 2.8% | +3.27 / +2.77 | +10% +4% +5% +5% +5% +7% +13% +3% |
| `h3_knownx_plus_stdret` `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio…` | hypo | 10 | +18.4% / +15.0% | +3.41 / +1.64 | 4.8% | +3.71 / +2.49 | +20% +18% +14% +18% +21% +22% +8% +18% |
| `h3_ov_blend_known_p05` `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(add(cs_rank(cross_ema(abs_(cs_deme…` | hypo | 0 | +20.4% / +16.1% | +3.35 / +1.75 | 4.0% | +3.32 / +2.68 | +26% +17% +13% +22% +24% +23% +8% +20% |

综合全文:`notes/F107_abs_demean_skew_low/synthesis.md`;回测表与解剖:`./scripts/study.sh table F107_abs_demean_skew_low s4`。

### 8. 挖掘 #3264(F108)

`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`

**它是什么(按算子定义)**:按源码逐层:nt_ts_kurt(Close,30) 是 NT 面(第 0 轴 = 日内分钟,不跨日)的 rolling_reduce + nankurt_last,所以「30」是 30 **分钟**不是 30 日;nankurt_last = m4/(var²+1e-9) − 3,且 var ≤ EPS 直接给 NaN(价格整窗封死 → NaN,被 day_max 跳过);pow_2 的 docstring 写 "signed power" 但那个分支只在 e ≤ 1 时生效,这里走普通 x**e,所以 pow_2 是树里唯一的 abs;pow_1_5 同理 = (K²)^1.5 = |K|³(单独作用在有符号 K 上会对负数给 NaN,abl_B 因此只在正超额峰度的分钟取 max);day_max = nanmax_last 吃当天全部 241 根分钟。合起来 = (max_m |K_m|)³,对 max|K| 严格保序 → 秩空间里只有一个自由度:「当天最孤立的那一分钟相对它前 29 分钟波动的信噪比」。机制不是收益肥尾,而是「价格被钉住 + 一次孤立跳动」(一字板/封板/极薄盘口);方向 sg = −1,多头腿 = 全天价格连续变动的大市值安静票。

**承重的子结构**

- nt_ts_kurt 这个算子本身:换成 nt_ts_var/std/delta 后 ρo 只剩 +0.09/+0.08/+0.04(≈不相关),ρk 跳到 +0.52/+0.55/+0.54 —— 按手册 §6.3 已经是另一条因子,不是提纯
- 窗口 30:没有平台。win_A_10 符号翻转(sg +1、ρo −0.38)、win_A_15 ut −2.9%(全表最差窗口)、30 为 +1.0%、win_A_60 valid −0.8%
- day_max 这个折叠:sub_D_day_close/day_last ut +0.6%(ρo +0.61)、sub_D_day_first/day_open 符号翻转 ut −6.0% / Lshp −1.20 / dist 0.50 ✗、sub_D_day_quantile ut −19.3%
- pow_2(树里唯一的 abs):删它 abl_B ut −0.6%、Lshp −0.09、LTO 从 4.7% 涨到 7.4%
- 截面水平本身(它是状态量不是事件量):cross_zscore 5/10/30/60 = −21.4/−16.2/−8.6/−5.0%,LTO 最高 29.7%;rel60(除自己 60 日均值)train +2.7/valid −2.3%

**多余的节点**

- pow_1_5 是死重:abl_C(day_max(pow_2(K))) ρo +0.97、ut +0.5% 对 base +1.0%,同一本书
- 外层 cs_winsor 是 no-op:win 行 ρo +1.00、ut +1.0%、Lshp +0.15,与 base 逐项相同
- signedpower 替 pow_1_5 等价:sub_C_signedpower ρo +0.99、ut +1.0%
- 28 条 memory 里的平滑一族(cross_mean / cross_ema / cross_decay_linear,窗口 5~60)全部 ρo +0.91~+0.99、ut 挤在 +2.4~+2.8%、Lshp +0.37~+0.46,且 hlL 从 20 掉到 1~3 —— 表达式内平滑与 EMA 半衰期是同一件事的替代品,统一比 base 高约 1.5pp,归因必须写「来自平滑」不是结构

**可互换的叶子**

- Close ↔ Open 可自由互换:leaf_Close_open ρo +0.96、ut +0.7%(base +1.0%)——「被钉住的那个报价」两者读到同一件事
- Low 不行:ρo +0.76、ut −0.6%、valid −4.5%
- Vwap 不行:ρo +0.79、ut −0.9% —— 这本身是机制证据,Vwap 只在有成交的分钟有定义,把冻结分钟抹平了
- High 没测(表里 leaf 组只有 Open/Low/Vwap),已写进第二批 h_kurt_high30:涨停钉住 High、跌停钉住 Low,不对称本身是机制检验

**在哪类股票里有效**

- 流通市值:段内多头净超额 +5.3/+5.4/+6.4/+5.7/−0.4%(最小四档都有 +5~6%,最大档为零),但全市场多头书超配最大市值档 +35.8pp、低配最小档 −16.6pp —— 桶内有选股力,排序把预算花在了零能力的那一桶。这是最主要的缺陷
- 成交额(20日):段内 −2.9/−3.5/−2.5/+6.4/+11.4%,只有最高 40% 为正(书也确实超配最高档 +18.4pp)。与市值方向相反 → 甜点是「小市值 × 高成交额」= 高换手率的投机票
- 冻结盘口段(近15日有封板/停牌,占 6.5%,段等权 −67.4%):段内 +37.3%(全解剖最大的数),而已知族 k_known 在这一段是 −10.9%;无冻结段(93.5%)段内 −3.1%(负)—— 全部截面选股力集中在 6.5% 的病态段,在其余 93.5% 的票上有害
- 次新段(上市不足250日,7.1%,段等权 −28.7%):原式 +5.0%、mem_min60 +12.8%、mem_min30/10 +9.4/+9.2%(k_known 只 +8.6%)
- 板块:沪/深主板/创业板 +1.0/+4.5/+2.7%,科创板(4.0%)−13.3% 且十列全负
- 价格:最低 20% 档段内 −6.7%(原式最差的价格档),其余四档 +1.5/+2.1/+4.5/+1.2%

**什么时候有效**

- 市场波动低于中位 +8.4% vs 高于中位 −6.4%(14.8pp,全解剖最大的时间切分)
- 成交放量 +2.6% vs 缩量 −0.4%
- 截面离散度高 +3.3% vs 低 −1.3%
- 市场近20日上涨 +2.2% vs 下跌 −1.3%
- 逐年:2019 +5.9 / 2020 +4.8 / 2023 +7.2 为正;2018 −4.1 / 2021 −5.2 / 2022 −0.2 为负 —— 没有任何一段能单独支撑可交易性

**原因推断**:三条推断,各带可检验推论。(1) 为什么只在高成交额里有用:峰度要有「30 分钟里 29 根不动、1 根跳」才有意义,最低成交额档里每只票都有大把死分钟,max|K| 饱和、截面上不再有区分度(段内 −2.9%)。推论:用 day_flat_ratio(Volume)(无成交分钟占比)当条件变量应该能把有用/无用的票分开;在成交额桶内中性化会抹掉信息(桶间符号相反),这正是 bk_liq/res_liq 两段反号(train −0.2/−1.0% 对 valid +9.2/+9.5%)的原因。(2) 为什么科创板失效:±20% 限幅、上市前 5 日无限幅 → 没有「一字板钉住」这种状态,max|K| 读到的是真实跳跃风险,而真实跳跃在科创板次日不被系统性惩罚。推论:因子强度应随价格限幅的紧度走,创业板 2020-08-24 改 ±20% 之后应变弱(2021 年 −5.2%,此前 2019/2020 是 +5.9/+4.8%,方向对但不干净,算未决)。(3) 为什么低价票失效:nankurt 分母的 EPS 是绝对值 1e-9,低价票一跳一个 tick、30 分钟价格 var ~1e-4、var² ~1e-8 与 EPS 同量级 → 峰度被人为压向 −3。推论:把叶子换成尺度远大于 EPS 的量(Amt、Volume),价格档的那个坡应该消失(h_kurt_amt30/h_kurt_vol30)。(4) 为什么高波动期失效:真跳变满地都是,max|K| 不再是「钉住的盘口」探测器而变成「波动大的票」的代理,后者在 A 股次日没有稳定负超额。

**相对已知成交额族**:没有(排序器口径),这是一个有证据的否定结论。ρk = −0.08 正交,但正交在这里不值钱,因为多头腿本身是零:v_base hlL20 Lnet +0.3/+2.5/+1.0%、Lshp +0.05/+0.46/+0.15,而底腿(最高 max|K| 十分位)毛超额 −30.6/−30.0%、LS +2.83/+2.53 —— 31pp 的多空差价里多头腿只拿到约 1pp,内容全在空头端。六条 overlay 全部严格差于家族单独:ov_p025 ut +14.1%(Lshp +2.03)、ov_p05 +13.9、ov_p10 +13.2、ov_m025 +10.9、ov_m05 +8.6、ov_m10 +4.7,对 k_known 的 +15.4%/+2.22;只有 valid 单看 ov_p10 +22.8% 比 +22.3% 高 0.5pp(噪声内),train 侧 +9.4% 比 +12.6% 低 3.2pp。中性化后也站不住:res_known train −1.2/valid +8.2%、res_liq train −1.0/valid +9.5%,两段反号、LTO 翻倍到 8.4%;bk_known/bk_liq 被 dist 0.20 判掉(疑似工具问题)。唯一打赢家族的地方是 6.5% 的冻结盘口段(+37.3% vs −10.9%)和 7.1% 的次新段 —— 那是**筛子**的用法而不是**混合**的用法,而 s1 表里一条筛子形态都没有(六条 overlay 全是线性混合)。另需记一笔:这与上一轮 R2 的头条结论冲突(R2 用 D30 = cross_mean(原式,30) 作载体 + 固定 hl0 量到结构增量 +1.2pp/+1.4pp),载体不同、s1 表缺 D30 那一行,h_ov_mean30_p025 专门去对齐。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))` | base | 40 | +1.3% / -3.8% | +0.19 / -0.33 | 2.8% | +2.82 / +2.04 | -2% +5% +4% -3% -1% +0% +8% -13% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_stdamt_xfroz` `cs_last_high20(neg(day_max(pow_2(nt_ts_std(Amt, 30)))), cross_max(day_zero_ratio(Ret), 15…` | hypo | 20 | +15.2% / +13.3% | +2.73 / +1.68 | 2.7% | +3.02 / +1.91 | +21% +12% +10% +12% +18% +20% +11% +13% |
| `seg_lowliq_m` `cs_first_low40(neg(day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))), cross_mean(day_sum(Am…` | segment | 20 | +12.7% / +7.0% | +1.88 / +0.82 | 4.9% | +2.66 / +1.66 | +9% +6% +6% +12% +29% +15% +5% +5% |
| `sub_A_nt_ts_var` `day_max(pow_1_5(pow_2(nt_ts_var(Close, 30))))` | substitute | 10 | +8.1% / +4.6% | +1.01 / +0.48 | 1.7% | +1.29 / +1.37 | +8% +4% -3% +12% +15% +11% +11% -2% |
| `h3_scr_dbl` `cs_last_high20(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio…` | hypo | 3 | +17.7% / +15.1% | +3.10 / +1.61 | 3.6% | +4.57 / +3.57 | +18% +14% +13% +17% +26% +21% +11% +15% |
| `h3_scr_40_flatrun` `cs_last_high40(neg(cross_mean(day_std(Amt), 30)), cross_max(day_flat_run_max(Close), 15))` | hypo | 2 | +15.5% / +14.6% | +2.82 / +1.59 | 4.6% | +2.97 / +2.72 | +20% +15% +11% +12% +19% +17% +12% +15% |

综合全文:`notes/F108_max_ntkurt_close/synthesis.md`;回测表与解剖:`./scripts/study.sh table F108_max_ntkurt_close s4`。

### 9. 手写 erm_mag_gap_5m_tsm20(F109)

`ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_quantile(Ret, 0.95)), sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), create_like(Close, 0))), add(day_sum(is_gt(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1)), day_…`

**它是什么(按算子定义)**:按算子定义逐层(SSA 记号本地重建,与 R1_propose_draft.txt 的 14 个锚点全部命中):D=r5=Close/Close[t-5]-1(5 分钟收益,前 5 根 NaN);E=q95、P=q05 是当天**1 分钟**收益 Ret 的 95/5% 分位;I=Σ r5·1[r5>q95]、J=#[r5>q95]、M=I/(J+1e-6)=up_mean、N=q95+1e-6、O=M/N=up_ratio;下侧 T=Σ|r5|·1[r5<q05]、U=#、W=U+1e-6、X=T/W=dn_mean、Y=|q05|、Z=Y+1e-6、AA=X/Z=dn_ratio;AB=O-AA=gap_d;AC=ts_mean(AB,20)。名字骗人四处:(1)「5m」只在被测量上,阈值是 1 分钟量——这个横向错配是承重件,把口径改自洽(leaf_Ret_ret5)反而 -6.3%;(2)「mag 幅度」只在下侧(abs_),上侧是带符号收益,两侧不对称,去掉下侧 abs_(abl_R)+3.4%;(3)两个 1e-6 不同质——计数分母上的完全惰性(sub_L_sub/sub_W_sub/sub_Y_neg/sub_R_neg 与原式逐位同分 ρo=1.00),只有分位数分母上的两个(N、Z)承重,封板/一路爬升到涨停的日子分位数恰为 0,比值被放大 1e3~1e5;(4)ts_mean(·,20) 不是平滑而是记忆——窗口 5/10/20/30/40 = -3.7/-3.4/-3.2/-3.1/-2.8% 完全平,一天的爆炸吃掉任何窗口。

**承重的子结构**

- D / H:5 分钟收益 r5 与 select_where 掩码核心——abl_D / sub_D_{add,div,mul} / abl_H 一律 -17.3~-17.4%(Lshp -2.55)
- N = q95 + 1e-6 上的 epsilon(上侧爆炸):sub_N_sub(q95-1e-6,翻转上侧爆炸符号)-19.1%;abl_N(去 eps)-4.9% 且 cov 0.94 ✗;sub_N_mul/div +2.5/+2.0% 但 cov 0.94 ✗
- A = in_delay(Close,5) 的 5 分钟孔径:win_A_3/10/15 = -8.1/-8.2/-10.4%(原式 -3.2%)——是尖峰、没有邻域平台
- 横向错配本身(5 分钟被测量 vs 1 分钟阈值):leaf_Ret_ret5 把阈值改成同口径 5 分钟 -6.3%,比原式更差

**多余的节点**

- 上侧计数归一化 L = J+1e-6 —— 删掉它是全表最大的一次结构收益:only_L_R = sub_J_day_first +5.1%(valid +14.0%、Lshp 0.58)、sub_L_mul +4.9%(Lshp 0.75)、sub_W_div +4.5%、sub_W_mul +4.4%,全部从原式的 -3.2% 翻正
- 整条下侧分支 AA:abl_AA / only_AA_R / sub_AA_mul / sub_AA_add / sub_AA_sub / abl_AB 六条同为 +2.6~+2.7%、Lshp 0.41~0.43、ρo 0.72 —— 换哪个算子都一样,它只是在 O 的 1e6 量级旁当噪声
- 下侧的 abs_(R 节点):abl_R(改用带符号 r5)+3.4%;sub_R_pow_2 +1.1%;sub_R_neg 与原式同分
- 外层 ts_mean 的窗口(AC):win_AC_5/10/20/30/40 全平;mem_mean/ema/decay_linear 全族与原式 ρo 0.92~1.00,再平滑无效
- AB 用 sub 还是 add:sub_AB_add +3.4% ≈ abl_R,只值约 1 点;abl_AB(连 sub 一起删)+2.7%
- 两个常数节点 C=1、G=0:abl_C +3.2%、abl_G +2.3%,但都是删常数后整棵树退化(不算结构发现)

**可互换的叶子**

- 价格字段完全可互换:leaf_Close_open / leaf_Close_low / leaf_Close_high / leaf_Close_vwap,ρo 0.84~0.96,Lnet -2.6~-4.7%(原式 -3.2%)——信息不在「收盘价」这个身份上
- 只换分子那一个 Close(fld_Close_Open/High/Low/Vwap)ρo 0.45~0.86、-3.2~-4.1%:也救不回来,但说明分子分母同时换才是无害的
- 外壳的折叠统计量可换成稳健/有界版本且小赚:sub_AC_ts_quantile_q25 +2.9%、nosc_J_day_gini +3.9%、sub_T_day_close/last +2.9%、sub_J_day_close/last +3.2%
- 反例(用户提示的「Ret 与量的变化率可互换」在这棵树上不成立):leaf_Ret_volchg / leaf_Ret_logvol / leaf_Ret_amtchg 三条 dist 0.00 ✗、LTO 0.3% —— 退化成常数,因为 Ret 在这里只作为阈值与价格收益比较

**在哪类股票里有效**

- 原式:全市场所有常规切分一律为负(四个板块 -3.8/-4.2/-4.1/-6.5%;流通市值五档 -1.1/-4.5/-11.1/-7.1/-2.3%;成交额五档 -3.8/-7.6/-7.8/-9.3/-3.3%;价格五档全负)
- 原式唯一为正的两个段都是病态段:「近 15 日有冻结盘口(封板/停牌)」占 6.5%、段等权 -67.4%、段内 +14.3%,而且全市场多头书超配它 +2.3pp(已知族段内 -10.9%、低配 -2.9pp)——这就是全市场 -3.2% 的来源;「上市不足 250 日」占 7.1%、段等权 -28.7%、段内 +5.0%
- 去掉爆炸后的结构变体(sub_L_mul / only_L_R)换了一片市场:创业板 +9.0/+11.6%、深主板 +6.1/+7.7%、沪主板 +3.9/+2.8%、科创板 +2.4/-20.5%
- 只在小市值:流通市值最低 20% +9.8/+12.0% → 最高 20% -0.5/+0.2%
- 只在活跃段:成交额(20 日)最高 20% +10.8/+3.6%、最低 20% -6.2/-7.4% —— 与已知族完全相反(k_known 把 +80.3pp 持仓压在成交额最低 20%,那一段段等权 +15.1%,所以已知族本质是「买不活跃的票」)

**什么时候有效**

- 原式:没有任何时段救得回来。逐年 2018~2023 = -6.9/-3.5/-5.8/-2.3/+0.5/-0.0%;市场近 20 日涨 -2.7% 跌 -3.5%;高波 -3.3% 低波 -3.1%;放量 -2.6% 缩量 -3.7%
- 结构变体(sub_L_mul / only_L_R)只在平静且上行的市场有效:市场近 20 日上涨 +8.2/+13.1% vs 下跌 +0.4/-4.6%;市场波动低于中位 +9.4/+9.0% vs 高于中位 +0.4/+1.4%(已知族相反:高波 +18.5% > 低波 +12.4%)
- 截面离散度高 +6.4/+9.1% vs 低 +3.5/+1.3%;逐年集中在 2022 +10.7/+17.1% 与 2023 +10.8/+9.1%,2019~2021 约为 0 —— 样本内的正号有一半是 valid 段的低价/低波风格年

**原因推断**:规则日上 O ≈ Σ r5·1[r5>q95] / q95 是尺度不变的(1 分钟收益为高斯随机游走时它约为常数),所以它只随三件事动:1 分钟收益的正自相关(资金把价格一级一级往上推)、跳跃、以及零收益分钟过多(薄盘)。方向 sg=-1,因此这条因子在卖掉「最近 20 天被日内推着走」的票。这正是 A 股创业板 + 小市值 + 高换手里游资拉抬的签名:那里价格由订单流而非信息驱动,拉抬后数日回吐;在大市值 / 科创板(20% 涨跌幅、机构持仓)这个机制弱,信号也随之消失(科创板 -20.5%)。时段上它只在平静且上行的市场有效,那正是投机资金主导小票定价的环境;高波 / 下跌时个股收益被 beta 吞掉。而原式之所以多头腿为负,是因为 1e-6 把这个反转信号和一个「近 20 日有没有封板」的事件标记焊在一起:后者的钱在空头腿(买不进),并且它住在已知族亏钱、段等权 -67.4% 的那 6.5% 里,原式还超配它 2.3pp。可检验推论已全部写进第二批:① 直接读「推」的量(day_signed_ratio(Ret,Amt)、day_wmean)应同向且更干净;② 「5 分钟为正占比 − 1 分钟为正占比」是正自相关的纯读数,应保留信息;③ 若只是活跃度倾斜,成交额桶内排名应全塌;④ 若机制为真,只在高成交额 40% 里做应接近段内 +10.8% 而不是全市场 +4.9%;⑤ 冻结盘口段应能被 day_zero_ratio / day_flat_run_max 直接复现甚至超过。

**相对已知成交额族**:没有增量。ρk:原式 +0.03,全部结构变体 +0.05~+0.41(相关低不等于有增量)。res_known(对已知族取截面秩残差)-0.3%;bk_known(已知族十分位桶内排名)+0.4%、bk_liq +0.4%,两条都因 dist 0.20 ✗ 不算候选。overlay 六档单调稀释、正负权重一样:ov_p025 +13.9%、ov_p05 +12.4%、ov_p10 +11.3%、ov_m025 +10.8%、ov_m05 +7.8%、ov_m10 +3.8%,没有一个打赢家族自己的 +15.4%。两点保留:(a) 表里的 overlay 叠的全是多头腿本身为负的原式,对去掉爆炸后的结构变体不是公平检验 → 第二批 h_f_blend_fix025 / h_g_res_spine / h_f_blend_calm 补上;(b) 唯一在机制上说得通的贡献形式是当筛子而不是混合——已知族在冻结盘口段 -10.9%、原式在同一段 +14.3% → h_g_fam_nofrozen / h_g_fam_norun / h_g_fam_nonew 三条(这也是上一轮 12_next.md 第 1 条的表达式化,若赢了应另开 fid,不算 F109 的产物)。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create…` | base | 60 | -1.7% / +2.1% | -0.73 / +0.81 | 0.7% | +2.77 / +2.28 | -6% +0% -5% -0% +2% -2% +5% +2% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `seg_lowliq_m` `cs_first_low40(neg(ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay…` | segment | 40 | +10.6% / +7.3% | +1.67 / +0.88 | 1.7% | +2.76 / +1.20 | +9% +5% +3% +10% +23% +18% +2% +7% |
| `h_d_pos_gap20` `cross_mean(sub(day_pos_ratio(sub(div(Close, in_delay(Close, 5)), create_like(Close, 1))),…` | hypo | 20 | +6.6% / +7.3% | +1.09 / +1.04 | 1.1% | +1.68 / +0.77 | +9% +0% +1% +9% +9% +17% +1% +8% |
| `sub_B_mul` `ts_mean(sub(div(div(day_sum(select_where(is_gt(sub(div(Close, in_delay(Close, 5)), create…` | substitute | 1 | +5.4% / +4.4% | +0.80 / +0.66 | 1.3% | +2.46 / +3.04 | +4% +2% -5% +11% +13% +6% +10% -1% |
| `h3_blend_tailq75` `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cross_tail_mean_q75(div(day_sum(se…` | hypo | 0 | +17.0% / +12.6% | +2.50 / +1.42 | 3.5% | +2.55 / +2.15 | +18% +13% +11% +17% +25% +21% +8% +12% |
| `h3_fam_x_tailq75` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_tail_mean_q75(div(day_sum(select_…` | hypo | 1 | +16.7% / +13.7% | +2.49 / +1.49 | 2.7% | +3.16 / +2.83 | +19% +12% +9% +16% +25% +22% +10% +13% |

综合全文:`notes/F109_erm_mag_gap_5m_tsm20/synthesis.md`;回测表与解剖:`./scripts/study.sh table F109_erm_mag_gap_5m_tsm20 s4`。

### 10. 手写 ret_fair_log(F110)

`mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)),…`

**它是什么(按算子定义)**:按源码逐层:D = day_last(Close)/day_first(Open) − 1 = 开盘→收盘的日内收益(day_first/day_last 取当天第一个/最后一个非 NaN 分钟,**不含隔夜**)。G = log(Volume) − in_forward_valid_part(log(Volume));log(x)=log|x| 且 |x|≤EPS 时 NaN,in_forward_valid_part 取「严格在 j 之前、最近一个非 0 且非 NaN」的值 —— **它确实是前向填充**(上一轮 notes 写「不是前向填充」是错的),所以 G ≈ in_logchg(Volume,1),副作用是 Volume 恰为 1(log=0)的分钟被当无效基数跳过。in_mean_full / in_stddev_full 是**整天**的均值/标准差再广播回每一分钟(不是滚动)⇒ 阈值是日级常数,并用到当天后面的分钟(日频下无未来信息,但「日内因果」不成立)。is_gt/is_lt 得到两张分钟掩码:放量 +1σ 与缩量 −1σ。in_sustain_stddev(mask, Ret, 5) 是**触发型 + 向前取窗**:在每个触发分钟 j 取 Ret[j:j+5] 的标准差,越过收盘用 NaN 补 ⇒ 收盘最后一分钟触发恰得 0,非触发分钟 NaN。day_mean 对触发点取 nan-均值 ⇒ U、Dn;S = |U − Dn|;根 = D × S。方向 sg = −1 ⇒ 多头 = 日内下跌 × 波动不对称大。一句话:**1 日日内反转,按一个日级波动尺度放大**。名字与定义不符:ret_fair_log 里没有 fair value,收益也没取对数(log 只作用在 Volume 支);"sustain" 不是「持续」而是「触发 + 向前取窗」。

**承重的子结构**

- 没有任何子结构是真正承重的 —— 这是本轮最强的结论。基线 v_base 多头净超额 −0.0/−0.6/−0.2%,Lshp −0.03;毛超额 +7.8% 被 10.5% 换手(≈8%/年成本)吃光,LS 夏普 +2.76、底腿 −43.3% ⇒ 钱全在空头腿
- 形式上唯一「一换就塌」的是 I = in_stddev_full(abl_I −62.9%/换手 83.4%/cov 0.19 ✗;sub_I_in_max −80.9% cov 0.19 ✗;sub_I_in_demean −57.2% cov 0.43 ✗),但那是算术退化:删掉 σ 后两条阈值都退成均值,上下两腿取到同一批分钟,R = M − Q 变成相减抵消后的数值噪声;三条都没过 cov 门槛,不算数
- 真正在起作用的是「外层平滑」这个结构性零件(不在原式里):mem_ema30 把净额从 −0.2% 推到 +5.4%/Lshp +0.92,是全表除已知族与叠加行之外最好的一族
- D 这一半里,起作用的其实是 div 扔掉的**价格水平**:abl_C(删 div)+4.4%/+0.56、only_C_R +4.4%、sub_C_mul +4.9%,而 iso_A = day_last(Close) 单独 +6.0%/Lshp +0.85/换手 1.1% 是全表最好的 isolate

**多余的节点**

- 整棵成交量事件机器(E..S):abl_E(删 log)/abl_G(删差分)/abl_J/abl_K/abl_N/abl_O 的 utrain 全在 −0.3 ~ +0.5%,与 base −0.2% 同在噪声(±3)内
- F/G 的差分节点是**效果上的 no-op**:sub_E_abs_、sub_E_pow_2、sub_G_add、sub_G_mul、sub_F_in_boxcox、sub_F_in_demean、abl_E、abl_G 给出**逐位相同的三段数字 −0.7/+1.1/−0.2%** ⇒ 「量的异常变化」掩码 = 「量的异常水平」掩码 = 当天成交量最大的那些分钟
- abs_:abl_S 与 sub_S_neg 都是 −2.8%,只差 2.6 点 ≈ 噪声 ⇒ 符号本来就没被用上
- 两条 in_sustain_stddev 互为冗余:abl_L −1.6%、abl_P −2.3%,删任一条都不塌
- 窗口没有平台:L 的 3/5/10/15 = −1.6/−0.2/+0.9/+0.6,P 的 3/5/10/15 = +1.9/−0.2/−0.8/−0.2,全幅 ≤ 3.5 点 ⇒ 5 分钟是任意的,不存在有邻域的真效应
- 机器各件单独都是负因子:iso_M −7.1%、iso_Q −7.3%(事件后波动水平本身对多头是负的)、iso_R −5.2%、only_T_R(S 本身)−2.0%

**可互换的叶子**

- 价格字段完全无差别:fld_Open_Low、fld_Open_High、leaf_Open_close、leaf_Close_vwap、leaf_Close_open 的 ρo = 0.99~1.00、Δ ≤ 0.6 点 ⇒ D 只需要「今天的日内收益」,不需要具体字段身份
- 流量字段近乎无差别:leaf_Volume_amt ρo 0.99;整支换 Volume→Amt(fld_Volume_Amt)ρo 0.78、Δ ≤ 0.6 点
- 用户提示的那一类互换成立且方向有利:leaf_Ret_amtchg(机器里的 Ret → in_pct(Amt,1))ρo 只 0.41、ρk 0.17、净 +1.6%、**毛超额 +9.3% > base 的 +7.8%** ⇒ 换成「量的变化率」得到的是另一条因子且毛额更高;leaf_Ret_volchg(in_pct(Volume,1))+0.8%、leaf_Ret_logvol −1.2%、leaf_Ret_ret5(in_pct(Close,5))−2.5% ⇒ 可换,但换成更长周期的收益会掉

**在哪类股票里有效**

- 流动性是最锐的一刀:20 日成交额五档的**段内**净超额 base −5.3/−6.7/−2.6/−6.1/**+1.5%**,mem_ema30 −2.1/−2.9/−1.9/−0.1/**+5.0%**(mem_decay_linear60 +6.4%、mem_ema10 +6.0%)⇒ **只在最流动的一档里选得出股票**,而那一档的段等权超额是 −17.8%(全解剖最差的段)
- 与已知族的工作方式不同(本轮最有价值的一条):k_known 的段内是 −4.1/−5.3/−8.2/−5.2/+2.5%,而它的多头书**超配最不流动的一档 +80.3%**(该段等权 +15.1%)⇒ 已知族的 +15.4% 几乎全是**段位倾斜**,本因子是**段内选股**
- 板块:沪主板 +1.3%、深主板 +2.2%、创业板 −4.9%、**科创板 −10.6%**(mem_ema30 +5.8/+9.2/+2.9/−11.0%),而全市场多头书**超配科创板 +11.4%(mem +10.5%)** ⇒ 把仓位推进唯一亏钱的板块,是最明确的倒贴
- **冻结盘口段是全解剖最大的一个数**:近 15 日有封板/停牌的 6.5% 股票(段等权 −67.4%),base 段内 **+19.2%**、mem_ema30 +19.7%、mem_mean30 +24.2%、mem_ema10 +24.1%、iso_A +24.5%,而 **k_known 在该段是 −10.9%**;书对该段只超配 +1.3% ⇒ 信息完全没被利用
- 价格:只在最便宜一档为正(base +3.7/−2.4/−4.2/−1.0/−0.4%);但它**不是**价格倾斜 —— iso_A 的段内是 −4.3/−18.0/−29.0/−27.0/−17.2% 却超配最便宜档 +79.9%(纯倾斜、零段内技能),本因子相反
- 市值没有故事:五档 base −3.7/−1.8/+0.0/−3.4/−2.3%、mem_ema30 +2.7/+3.5/+4.3/+2.0/+1.1%(书却超配最小一档 +8.0%,那一档为负)。次新(上市 <250 日,7.1%)base +2.6%、k_known +8.6% ⇒ 无特殊性

**什么时候有效**

- 年度:base −1.8/+6.7/−1.0/−4.0/+3.3/−6.9%(2018→2023,**六年无一稳定**);mem_ema30 +3.9/+10.7/−1.8/+2.6/+13.5/+1.8%(6 年里 5 年为正,最好的是 2019 与 2022);对照 k_known 六年全正 +6.7~+24.7%
- 市场波动高于中位 base **+5.6%** vs 低于中位 **−5.9%**(mem_ema30 +9.7% vs +1.1%)—— 全解剖最大的一条时段差
- 成交缩量 +3.0% vs 放量 −4.1%(mem_ema30 +7.1% vs +3.2%)
- 市场近 20 日上涨 +2.1% vs 下跌 −2.2%(mem_ema30 +9.0% vs +1.6%)
- 截面离散度高 +1.3% vs 低 −1.5%(影响最小的一条)

**原因推断**:机制读法收口为:**这是一条 1 日日内反转(sg = −1 作用在 D 上),再乘一个日级波动尺度**;成交量机器只是这个尺度的一种很差的估计方式(S 与波动相关,但三段数字证明换掉它不掉水平)。这一条读法同时解释了四件事:① 空头腿强、多头腿为零 —— 反转在 A 股集中在「昨天日内大涨」那一侧,而那一侧只能卖出兑现;② 制度画像 —— 反转在**过度反应相对漂移大**(高市场波动)、且**没有放量趋势**(放量 = 动量制度)时才赚钱;③ 换一个日级波动尺度(day_std(Ret)、|D| 自身)不应当掉水平;④ 低换手是重尾假象 —— EMA 记的是少数极端日的峰值而不是水平。
分段原因推断 + 可检验推论:
(a) **流动段内选股**:最流动的那一档噪声交易者密度最高、日内过度反应最大且次日纠正最快,同时该段等权跑输 −17.8%(拥挤),所以「在输家段里挑赢家」才有信息。推论:按流动性秩加权(**保留幅度**)应当把段内 +5% 搬到全市场;而分桶**排名**不应当提高净额,因为排名本身删掉幅度(rk 单独 −7.3% 已证)。
(b) **科创板倒贴**:20% 涨跌幅、合格投资者门槛、几乎没有零成交分钟 ⇒ 「当天 +1σ 放量」是常态,事件后 5 分钟波动整体抬高,S 的截面含义被破坏;宽幅限价下 1 日反转本身更弱。推论:按价格水平分桶中性(科创/创业板集中在高价档)应当抹掉这笔倒贴而不伤水平;若抹不掉,问题就不在板块而在波动水平。
(c) **冻结盘口段 +19.2%**:封板/停牌时 Ret 多数分钟恰为 0、Volume 冻结 ⇒ 两腿的事件后波动都 ≈ 0 ⇒ S ≈ 0、D ≈ 0,因子被推到截面中间;所以 +19% 来自**部分**冻结的票,S 实际在量「封板松动了多少、还有多少真实成交」。推论:day_flat_ratio(Close) 单独应能拿到这 +19% 的相当一部分;段内优势应集中在 flat_ratio 的**中间档**而非极端档;对它分桶中性或显式倾斜,应把书的超配从 +1.3% 推上去 —— 而已知族在该段是 −10.9%,这是最可能的增量来源。
(d) **平滑为什么有效**:mem_ema30 的毛超额 +7.9% 与 base 的 +7.8% 一致,换手 10.5%→3.3% ⇒ **100% 是省成本、0 是 alpha**,纯平滑的天花板 ≈ +5.4%。

**相对已知成交额族**:没有增量。三条证据,其中第三条带一个必须说出来的保留。① ρk(base) = +0.35 ⇒ 它不是已知族的改写,这一点成立。② **叠加行是最干净的否定**:ov_p025 +13.4% / ov_p05 +12.6% / ov_p10 +11.8% / ov_m025 +11.3% / ov_m05 +9.0% / ov_m10 +6.2%,**全部低于 k_known 单独的 +15.4%,且两个方向都随权重绝对值单调变差** ⇒ 以任何符号、任何权重加进去都只减分;ov_p025 的 ρk 已经 0.96,说明最好的叠加不过是「几乎还是已知族」。③ 残差/分桶:res_known −7.7%、res_liq −7.6%、bk_known −7.2%、bk_liq −7.0%(bk_* dist 0.20 ✗ 不算数)。**保留**:这四条都先做了截面排名,而 rk(只排名、不中性化)单独就是 −7.3%、换手从 10.5% 升到 17.3% ⇒ **这 −7% 是「排名删掉幅度」的锅,不是中性化的**。诚实版本:幅度一删,这条因子的多头腿就一文不值;在此之上中性化已知族不再改变任何事。另一面值得追:res_known 的多头腿**毛**超额仍有 **+5.3%**,是 17.2% 的换手把它做成 −7.7% ⇒ 「残差 + 平滑」是唯一还没被成本污染的增量测法,本轮没人测过,已写成 h_liq_res_ema / h_base_res_ema。补充一条正面的:解剖显示它与已知族**工作方式不同**(段内选股 vs 段位倾斜),且在已知族失效的冻结盘口段 +19.2% vs −10.9% —— 这是「无增量」这个结论唯一还可能被推翻的口子。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is…` | base | 60 | +1.3% / -2.5% | +0.24 / -0.26 | 4.6% | +2.81 / +1.69 | +2% +7% -5% -2% +4% +1% +4% -9% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_cvx_xage` `cs_last_low20(neg(cross_ema(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(d…` | hypo | 5 | +12.1% / +11.4% | +2.03 / +1.15 | 3.4% | +2.71 / +0.93 | +19% +16% +2% +10% +17% +2% +18% +9% |
| `seg_lowliq_m` `cs_first_low40(neg(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(i…` | segment | 60 | +10.9% / +9.9% | +1.70 / +1.19 | 2.1% | +1.26 / +0.87 | +10% +5% +1% +12% +24% +20% +1% +12% |
| `mem_ema30` `cross_ema(mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain…` | memory | 5 | +5.4% / +3.7% | +0.92 / +0.37 | 3.3% | +2.71 / +1.90 | +4% +11% -2% +2% +13% +3% +11% -4% |
| `h3_ov_xfroz_cvx` `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Re…` | hypo | 3 | +18.7% / +18.5% | +3.12 / +1.67 | 3.6% | +4.06 / +3.20 | +26% +18% +10% +17% +23% +19% +20% +16% |
| `h3_ov_xfroz_bkliq` `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Re…` | hypo | 5 | +17.3% / +17.9% | +2.97 / +1.62 | 3.5% | +3.73 / +3.19 | +24% +17% +11% +15% +20% +15% +21% +15% |

综合全文:`notes/F110_ret_fair_log/synthesis.md`;回测表与解剖:`./scripts/study.sh table F110_ret_fair_log s4`。

### 11. 挖掘 #953(F111)

`ts_spearman(day_quantile(Close), 10)`

**它是什么(按算子定义)**:ts_spearman(day_quantile(Close), 10)。两处名字与定义不一致:(a) day_quantile 注册时 q 默认 0.5,它**就是 day_median** —— 日内分钟价格的中位数,不是「收盘价的某个分位」(表里 sub_A_day_median 与 v_base 逐位相同、ρo=1.00);(b) ts_spearman 前缀是 ts_、声明 arity=1,但 nd_ts.py:483 的函数体里有 `for i in range(N)` 的**跨股票循环** —— 第二个操作数是股票轴本身。它对每只股票 i 和每个 10 日窗口,先把窗口内 10 个日值做**时间轴上的秩**(argsort(argsort(·, stable=True))),再与**所有其他股票 j** 的秩向量算 Spearman,对 j 取 nanmean。这一层可以精确化简:完整窗口上每只股票的秩向量都是 0..d−1 的一个排列,所以 σ_j 对所有 j 是同一个常数 sqrt((d²−1)/12),于是 mean_j corr(R_i,R_j) = <R̃_i, Σ_j R̃_j>/((N−1)σ²) ∝ corr(R_i, C),C = 各股票秩路径的**等权平均**(市场的共识秩路径)⇒ O(N²) 的两两配对里**没有配对信息**(上一轮已用逐日 Spearman=1.0000 坐实)。合起来:**f ≈ (自己 10 日价格路径的单调趋势) × (市场 10 日路径的方向)**,一条被市场方向翻符号的动量(上一轮:自己的趋势 ρ^time 单独 −5.60/−0.71%,乘 c(t) 后 +9.23/+18.62%)。另有一个真实现伪影:stable 排序把**并列按时间先后给秩**,所以 10 天中位价完全不动的股票(停牌/一字板/薄盘)拿到的秩路径是 (0,1,…,9),与完美单调上涨一模一样,在上涨窗口里被打满分 —— 「平」≡「完美上升」。

**承重的子结构**

- 根上的 ts_spearman 是唯一承重节点:换成 ND 面任何别的 ts 算子全塌 —— ts_skew +2.8% / ts_var +2.3% / ts_std +0.7% / ts_rank −3.4% / ts_argmin −3.3% / ts_argmax −11.5% / ts_kurt −13.0%(原式 +12.3% ut)
- 输入必须是一个「日价格水平」:换成非价格水平的日内统计量就塌 —— day_gini +6.1%(ρo 0.56)、day_skew +4.6%(ρo 0.52)
- 「水平」而不是「变化」:cross_zscore(f, 5/10/30/60) = −14.6/−10.3/−3.0/−1.0%,cross_stddev 四个窗口全负,rel60=div(f, cross_mean(f,60)) −3.9% ⇒ 它是一个持久的股票属性(像 beta/流动性),不是事件
- 单调、不折叠:pow_2(cs_demean(f)) −0.1%、abs_(cs_demean(f)) −2.7%、abs_(cs_demean(cs_rank(f))) −2.5%
- 共识必须由**秩**路径等权平均而成(σ_j 相等才成立):上一轮把共识换成价格水平平均 ts_corr(A, cs_mean(A), 10),相关只 0.742、valid 塌到 +4.9%

**多余的节点**

- 整层日内折叠:day_last/day_close +13.2%、day_quantile_q25 +12.8%、day_min +12.5%、day_first/day_open +12.2%、day_median=base +12.3%、day_max +11.4%,全在 ±3pp 噪声内(day_last 稳定高 0.9pp,可解释为中位价比收盘价更容易日间精确并列、更吃并列伪影)
- 外层日轴记忆一条都没超过原式:cross_decay_linear60 +12.2%、cross_ema30 +11.8%、cross_ema10 +11.7%、cross_mean60 +11.2%;这些行选到的 hlL 掉到 0~3,平滑只是替代了书的半衰期
- cs_winsor 在这里是恒等变换(+12.4% vs +12.3%):相关系数本来有界于 [−1,1],没有尾巴可缩
- cs_rank 外包装 +11.0%(比原式低 1.3pp,噪声内),保序变换不改变实质

**可互换的叶子**

- Close / Open / High / Low / Vwap 四个替换的 ρo 全是 1.00(+12.5 / +12.3 / +12.3 / +12.2%):日内中位数之后它们就是同一个价格水平,这不是鲁棒性,是同一条因子的四种写法
- day 折叠算子之间互换(day_last / day_close / day_median / day_quantile / day_quantile_q25 / day_min / day_first / day_open / day_max),ρo 0.95~1.00

**在哪类股票里有效**

- 按 20 日成交额,段内选股力随流动性**单调上升**:最低 20% −0.1%、20-40% −2.2%、40-60% +1.8%、60-80% +3.2%、最高 20% +9.5%;而全市场多头书在最低桶**超配 +30.3%**、在最高桶低配 −16.7% ⇒ 它把权重压在自己没有本事的一段
- 已知族 k_known 同一列是 −4.1/−5.3/−8.2/−5.2/+2.5%、最低桶超配 +80.3% ⇒ 两条因子重叠的部分(低流动性倾斜)恰恰是 f 自己没本事的部分,f 会选股的高成交额端正是已知族空白的地方
- 按流通市值:中小更好(最低 20% +9.9%、20-40% +9.1%、40-60% +10.4%),60-80% +2.5%、最高 20% +2.4%(低配 −13.0%)。与成交额合看,甜点是「中小市值 + 成交活跃」,不是「小而冷」
- 板块:创业板 +14.4%(超配 +3.3%)> 深主板 +13.5% > 沪主板 +11.2%(低配 −3.1%)>> 科创板 −3.6%(该段只占 4%、持仓差 +0.7%,信度低,只当线索)
- 价格:60-80% 最好 +12.0%,最高 20% 最差 +3.7%
- 次新(上市不足 250 日,7.1%):段等权 −28.7%(整段是陷阱)但**段内选股力最强 +16.9%**(win20 +23.1%),书仍低配 −2.1% —— IPO 泡沫消化是一条单调下跌路径,f 把它排到底部
- 近 15 日有冻结盘口(封板/停牌,6.5%):段等权 −67.4%,**段内 −38.7%** —— f 在这群票里系统性挑到最差的,正是并列伪影预测的失效点;书只低配 −3.0%,远不够

**什么时候有效**

- 逐年:2018 +16.9% / 2019 +7.8% / **2020 +1.6%** / 2021 +15.7% / 2022 +16.4% / 2023H1 +18.2%
- 市场近 20 日**上涨 +17.4% vs 下跌 +5.9%**
- **放量 +17.4% vs 缩量 +8.3%**(成交高于 60 日均)
- 截面离散度高 +15.1% vs 低 +9.6%
- 市场波动高 +13.7% vs 低 +10.9%(这一条差异最小)

**原因推断**:f 的符号由市场自己 10 日路径的方向给定,要赚钱需要两件事同时成立:(a) 市场方向在持有期内不翻 —— 否则 c(t) 变号、整条因子被反向打脸;(b) 截面上有足够离散度让排名分得开。2019–2020 正是方向反复翻的两年(2020 的二月暴跌 + V 型反弹 + 风格轮动),这解释了 2020 年只有 +1.6%;放量/高离散时更好,因为那时排名的信噪比高。上涨段(+17.4%)好于下跌段(+5.9%),因为 A 股上涨段里散户的趋势追逐让「涨得整齐」真的延续,而下跌段里 f 变成买跌得最整齐的票,只能吃反弹。创业板最好、沪主板最差与「散户趋势追逐」同向;科创板失效与它基本都是次新 + 20% 涨跌幅 + 机构定价一致。按流动性看选股力单调上升、而持仓压在最不流动端,是因为**低成交额的票价格天天不动、日间精确并列多,被并列伪影(平≡完美上升)系统性抬到排名顶端**,那部分排名不含信息(段内 −0.1%),书在那里赚到的只是该段 +15.1% 的段等权溢价 —— 也就是已知成交额族赚的同一笔钱。可检验的推论:(i) 把价格路径换成截面秩路径(抽掉市场共同成分)⇒ 条件化消失、应塌成无条件反转(h_relpath);(ii) 再乘一次市场方向应把条件化抵消、退回 −5.6% 的无条件反转(h_mkt_undo);(iii) 显式写「自己 10 日收益秩 × 居中后的市场 10 日收益」应能复现它且是 O(N)(h_mkt_explicit);(iv) 市场层面的「放量才有效」在个股层面也该成立(h_act_bucket/h_act_mul);(v) 冻结盘口段的 −38.7% 应被一个不动占比的剔除器救回(h_excl_flat/h_excl_zero);(vi) day_last 优于 day_quantile 的那 0.9pp 应在并列更少的载体上进一步兑现(h_wmean_carrier)。

**相对已知成交额族**:没有可量出的增量(否定结论,证据充分)。ρk = +0.42,不是同一条因子,但共享「安静、小、便宜」这条轴。叠加:ov_m025(已知族 + 0.25 权重的 f)+15.6% / 夏普 2.32,对 k_known 的 +15.4% / 2.22 只多 +0.2pp / +0.10 夏普,**全在噪声内**(±3pp / ±0.3);权重加大单调变差(ov_m05 2.30、ov_m10 2.23);把 f 的符号反过来掺则大幅变差(ov_p025 +9.4%/1.37、ov_p05 0.90、ov_p10 −0.03)⇒ **方向是真的、不是噪声,但边际贡献量不出来**。中性化:res_known +5.9%/1.09、bk_known +5.9%/1.10、res_liq +6.6%/1.22、bk_liq +6.3%/1.19 —— 原式 +12.3%/2.15 的**一半**在已知族张成里,另一半站得住但单独不可用;上一轮更强的证据是对 9 个标准控制变量**一起**中性化后多头腿毛超额 +13.6% → +0.1%。**但解剖给出一条没被利用的不对称**:f 在**每一个**成交额分桶里的桶内选股力都强于已知族(最高桶 +9.5% vs +2.5%,最低桶 −0.1% vs −4.1%),已知族赚的是流动性倾斜、f 赚的是桶内排序,二者原则上不重叠 —— 这是唯一值得再花一次服务器时间的口径(h_ov_bk / h_ov_bk05:已知族定倾斜 + f 只做桶内排序),全表没有量过。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `ts_spearman(day_quantile(Close), 10)` | base | 20 | +12.3% / +6.0% | +2.15 / +0.84 | 4.0% | +2.62 / +1.10 | +17% +8% +1% +16% +16% +12% +9% +4% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_best2` `cs_last_high20(ts_pearson(day_last(Close), 20), cross_max(day_zero_ratio(Ret), 15))` | hypo | 10 | +15.2% / +8.0% | +2.75 / +1.08 | 4.7% | +3.22 / +1.92 | +21% +14% +7% +15% +16% +14% +8% +8% |
| `seg_xfrozen_p` `cs_last_high20(ts_spearman(day_quantile(Close), 10), cross_max(day_zero_ratio(Ret), 15))` | segment | 20 | +13.3% / +7.8% | +2.41 / +1.07 | 4.3% | +2.59 / +0.63 | +16% +13% +4% +16% +12% +13% +12% +5% |
| `sub_A_day_close` `ts_spearman(day_close(Close), 10)` | substitute | 20 | +13.2% / +6.8% | +2.29 / +0.95 | 4.0% | +2.79 / +1.28 | +19% +8% +2% +15% +17% +14% +9% +5% |
| `h3_xfz_plus_f` `cs_last_high20(neg(add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(ts_spearman(day…` | hypo | 3 | +19.1% / +13.8% | +3.23 / +1.44 | 4.6% | +4.06 / +2.75 | +26% +16% +12% +16% +26% +20% +10% +15% |
| `scr_xhi_m` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), neg(ts_spearman(day_quantile(Close), 10…` | screen | 5 | +15.5% / +12.6% | +2.35 / +1.31 | 3.7% | +2.45 / +1.52 | +24% +9% +5% +15% +23% +20% +8% +13% |

综合全文:`notes/F111_spearman_qclose/synthesis.md`;回测表与解剖:`./scripts/study.sh table F111_spearman_qclose s4`。

### 12. 挖掘 #574(F112)

`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`

**它是什么(按算子定义)**:按源码逐层:A=`day_quantile(Close)` 默认 q=0.5 ⇒ 当天分钟价的**中位数**(单位:元,名字是 quantile 但默认就是中位数,`sub_A_day_median` 与 v_base 数字完全相同可证);B=`day_kurt(High)` 当天分钟 High 的峰度(无量纲,量级 1~20);C=`add(A,B)` 是「元 + 无量纲数」,两个加数量级差一个数量级以上 ⇒ **C ≈ A,B 只是扰动**(iso_A +5.8% 与 iso_C +6.3% 在噪声内);D=`cs_mask_top_replace_mean_neg` 源码是 `-cs_mask_top_replace_mean(-x)` ⇒ 遮的是截面**最低 10%**(名字里的 top 反了),方向 -1 下它正好抹掉多头腿自己的尾巴;E=`signedpower(e=2)` 在正值域上就是平方;F=`ts_scale(·,30)` = `x[t]/nansum(近30日 x)`,分母是每只股票自己的滚动**和**(不是均值)。

合起来,记 r = P_t/mean30(P)、cv = 窗口内价格变异系数,则 F(E(·)) = P²/ΣP² ≈ r²/(30·(1+cv²))。所以这棵树是「**这个月相对自己均价跌了多少 × 这个月价格自己抖得多厉害**」,再把最便宜的一成挖掉;sg=-1 ⇒ 多头 = 跌下来且月内波动大 ⇒ 一条 **1 个月反转**因子(state.md 记的 ρ(mom20)=+0.554 与此一致)。

两个源码级新发现:(1) **`signedpower` 不是保序冗余** —— 它把分母从算术均值推向偏向大值的幂均值,等价于多乘一个 1/(1+cv²),这就是 abl_E 掉 1.4pp、pow_3 与平方持平(指数是平台)的原因;(2) **`ts_scale` 的 nansum 分母是一个未被设计的暴露** —— 窗口里缺失日越多分母项数越少、取值越大,方向 -1 下被压到书底;解剖直接证实:**所有含 ts_scale 的变体对「上市不足 250 日」一律低配 -4.9%~-5.5%,不含的一律 -0.1%~-0.7%**。次新的回避是算子实现的副产品,不是选股。

**承重的子结构**

- A 这条价格叶子必须压倒 B:`only_C_R`(只留峰度)ut -4.8%/-1.48;`rank_C`(先把两个加数各自 cs_rank 再相加、强行等权)ut -10.8%/-2.72 且换手 24.4%;`sub_B_day_q_stat_std`(峰度换成量级可比的分钟 High 标准差)ut -21.9%/-3.30 ⇒ add 不是「组合」而是「价格 + 可忽略扰动」,第二项一旦拿到可比量级整棵树反过来塌掉
- F 这个比值决定了它是哪条因子:删掉 F 的 `iso_E` ut +8.4%/1.85 但 ρo 仅 0.17、在任何价格桶内部都 -9%~-26%(就是价格水平本身);保留 F 的 `abl_D` ut +7.8%/1.12 在每个价格桶内都正 ⇒ F 把一条价格水平 beta 换成了一条反转。把 F 换成平滑(`sub_F_ts_decay_linear` +8.2%/1.80,ρo 0.18)或 `ts_spearman`(方向翻成 +1,ρo 0.15)都是换成别的因子,不是同一条的变体
- C 的正值性是 E 能用的前提:`sub_D_cs_demean` ut -16.5%(去均值后有负数、平方变成折叠)
- E(平方)通过改变 ts_scale 的分母形状承重:`abl_E` ut +2.8%/0.50,比 v_base 低 1.4pp

**多余的节点**

- D(`cs_mask_top_replace_mean_neg`)是**有害**的,不只是多余:`abl_D` ut +7.8%/1.12 比原式 +4.2%/0.74 高 3.6pp、夏普 +0.38,换手不变(6.8% vs 6.6%)。`sub_D_cs_winsor` +7.8%/1.13 与 abl_D 几乎同一条(ρo 都 0.78)⇒ 损失**不是**离群值问题,就是「整体剔掉最便宜的一成」;最好的替代 `sub_D_cs_rank` ut +8.8%/1.35 是全表非 overlay / 非基准的最高
- B(`day_kurt(High)`)删了不掉:`abl_C` ut +3.9%/0.54 vs base +4.2%/0.74,在噪声内(±3pp / ±0.3)
- E 的指数是平台:`pow_2`(与原式逐位同)、`pow_2_5` +4.1%/0.72、`pow_3` +4.2%/0.74 三档无差别
- 所有外层形状都是负作用:`cs_rank` ut +2.0%/0.40、`abs_(cs_demean(·))` +1.9%/0.31、`abs_(cs_demean(cs_rank(·)))` +1.5%/0.24;28 条日轴记忆里只有平滑类帮一点(`cross_ema60` +5.4%/0.94、`cross_decay_linear5` +5.2%/0.92),`cross_zscore` 5/10 日 -15.1%/-14.1%、`cross_min` 30/60 日 -16.4%/-15.2% ⇒ 信号要的是比值的截面水平,换成「对自己历史是否异常」后符号整个反过来

**可互换的叶子**

- A 的字段随便换:Close→High/Open/Vwap 全在 ut +3.9%/0.69~0.70(原式 +4.2%/0.74)
- A 的折叠算子随便换:`day_median`(与原式逐位相同)、`day_close`/`day_last` +4.3%/0.76、`day_max` +4.3%/0.75 ⇒ A 只是「当天的价格水平」,用哪个摘法都一样
- B 的字段随便换:`day_kurt(Close)` +4.5%/0.79、`day_kurt(Open)` +3.9%/0.67(`fld_High_Open`)
- B 的**算子不能换**:换成量级更大的 `day_q_stat_std(High)` 直接 -21.9% ⇒ 可换的是身份,不可换的是量级
- F 的窗口是连续旋钮而非叶子:20/30/40/50 = +1.0%/0.18、+4.2%/0.74、+4.6%/0.83、+4.9%/0.90,单调向上、ts_* 池到 50 为止

**在哪类股票里有效**

- 必须先把两族分开读,否则会得出错误结论。**不含比值的 iso_E 族 = 低价/微盘 beta**:在价格五档内部 +0.5/-9.0/-25.7/-21.0/-19.6,持仓 +34.7% 全压在价格最低 20%、其余四档一律 -19.9%(几乎不持有)⇒ 把价差抽掉就什么都不剩;它的 +8.4% 是段 beta(价格最低 20%、流通市值最低 20%、成交额最低 20% 的段等权超额分别 +7.0%/+6.4%/+15.1%)
- **含比值的 abl_D 族在每个价格桶内都正**:+2.3/+5.3/+8.0/+5.1/+4.7,持仓只温和偏低价(+15.3%)⇒ 比值把价格水平约掉了,剩下的是真的截面信息;v_base 唯一的洞是价格最低 20%(-12.1%)
- 流动性:**比值族的信息集中在流动的一半** —— abl_D 成交额五档 -0.1/-2.1/-0.2/+4.2/**+12.4**(最高档最强);iso_E 正好相反(-14.5% 在最高档);而 `k_known` 五档 -4.1/-5.3/-8.2/-5.2/+2.5 却把 +80.3% 的持仓压在最低档
- 板块:创业板最强(v_base +9.8%、abl_D +11.0%)、深主板次之(+4.0%/+9.9%)、沪主板很弱(+0.6%/+5.6%)、科创板失效(+0.8%/-4.6%)
- 市值:单调递减 —— abl_D 流通市值五档 +9.4/+5.8/+5.4/+1.2/+0.7
- 两个被低配的富矿:上市不足 250 日(占 7.1%,段等权 -28.7%)段内书 v_base +11.2%、iso_D +17.2%,持仓却 -5.5%(= ts_scale 的 nansum 副产品);近 15 日有冻结盘口(占 6.5%,段等权 -67.4%)段内书 abl_D **+29.6%**、sub_D_cs_winsor +29.1%、v_base +14.8%,持仓 -3.2%,而 `k_known` 在这一段是 **-10.9%**

**什么时候有效**

- 市场波动是最大的时间开关:高于中位 v_base **+13.2%** vs 低于中位 **-4.7%**(abl_D +17.8% vs -2.0%);`k_known` 在两段都正(+18.5%/+12.4%)
- 市场近 20 日下跌 +8.0% vs 上涨 +1.4%(iso_E 正好相反:上涨 +12.0% vs 下跌 +3.9%,再次说明两族不同)
- 缩量 +5.9% vs 放量 +2.0%(abl_D +9.7% vs +5.4%);截面离散度高 +5.6% vs 低 +2.9%(较弱)
- 年度:2018 +12.3%、2022 +11.8% 最好(熊市/高波动),2020 -4.2%、2023 -5.3% 最差,2021 +0.9% 很弱 ⇒ 动量年亏、恐慌年赚;`k_known` 六年全正(+6.7%~+24.7%),没有这个脆弱性

**原因推断**:比值族是「跌下来 × 月内波动大」的反转,它赚的是**提供流动性的补偿**,所以它需要错价能被交易回去。(a) 成交额高的票里下跌多半是流动性冲击或情绪,做市资金愿意接、一个月内能收回;成交额最低两档里下跌往往是基本面或退市风险,跌了不回头 ⇒ 在那里失效(-4.4%/-2.1%)。(b) 价格最低 20% 失效(-12.1%)同理:便宜票的下跌是信息(ST、退市),而且价格落在 tick 网格上,比值本身也最吵。(c) 创业板好、沪主板差、科创板负:创业板 ±20% 涨跌幅 + 散户换手高 ⇒ 日内情绪定价的幅度最大、反转最强;沪主板更多指数/机构资金;科创板又小又贵、2019 才开板、机构持仓占比高。(d) 冻结盘口段里 +29.6%:连板之后价格远离自己一个月的均价,r 最极端、cv 最大,正是这棵树读得最准的状态(段等权 -67.4% 而段内书 +29.6% ⇒ 它在把「连板后要跌的」和「停牌/ST 的」分开)。(e) 只在高波动/下跌/缩量里有效:波动和恐慌就是流动性补偿的定价环境;2020 和 2021 是动量年(白酒、半导体、新能源成趋势),反转本来就该亏。

**若这些原因成立,还应该看到(已写进 hypo)**:① 把书限制在成交额高的 40%(h_liq_first40)应把 ut Lnet 推上去,而只剔掉最不流动的 20%(h_liq_excl20)只能拿到一部分;② 剔掉价格最低 20%(h_px_excl20)应直接消掉那 -12.1%;③ 用「一年里最大的单日 High/Low 比」当涨跌幅制度代理(±20% 板 ≈1.5、主板 ≈1.22、ST ≈1.1)聚焦高档(h_lim_first40)应复制「创业板好」那一段;④ 把 E 显式写成「跌幅秩 × 月内 cv 秩」(h_rev_x_cv)应复制 abl_E→v_base 的 +1.4pp;⑤ 把 nansum 分母换成真均值(h_div_mean30)后对次新的 -5.5% 低配应消失;⑥ 既然信息是「相对自己近期水平的偏离」而非水平,同一个比值形状套到成交额上(h_amt_ratio30)应也有信号,而把 k_known 自己去水平(h_amtstd_ratio30)应把它的 +15.4% 打掉。

**相对已知成交额族**:**全市场口径上没有增量,不建议纳入。** ρk 不高(v_base 0.25、abl_D 0.33、iso_E 0.41)但这不等于有增量:① **叠加一律减分且随权重单调变坏** —— ov_p025 ut +13.5%/2.00、p05 +12.4%/1.89、p10 +11.3%/1.81、m025 +11.0%、m05 +8.7%、m10 +5.4%,**全部低于 k_known 的 +15.4%/2.22**;② **对家族取秩残差后归零** —— `res_known` ut **+0.2%/+0.03**(train -1.0%、valid +3.0%,cov 1.00 / dist 1.00 过门槛);`bk_known` +0.9%、`bk_liq` +0.3% 方向一致(两行 dist 0.20 打 ✗,只作旁证)。与第 4 轮留出段一致(f_known +13.23% vs 最好的候选 f_nomask30 +11.12%)。

**但有一条还没被正确检验的口子。** 解剖显示 `k_known` 自己在成交额桶内部几乎没有信息(五档 -4.1/-5.3/-8.2/-5.2/+2.5),却把 **+80.3%** 的持仓压在成交额最低 20%(该段段等权超额 +15.1%)⇒ **家族的 +15.4% 主要是一条流动性/微盘 beta**。而比值族的 alpha 恰好在家族最弱、且几乎不持仓的地方:成交额最高档 abl_D **+12.4%** vs 家族 +2.5%(家族在该段低配 -20.3%);冻结盘口段 abl_D **+29.6%** vs 家族 **-10.9%**。全市场秩叠加(overlay)和线性秩残差(res_known)都测不到这种**分段互补**;还没试过的是把书限制在家族不去的那一段(`cs_first_high40(·, 成交额)`)。这是本轮留下的唯一活口,已落成 hypo 的 D 组(5 条)。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)…` | base | 60 | +5.6% / +2.3% | +0.98 / +0.33 | 4.3% | +2.59 / +2.63 | +12% +8% -2% +6% +11% -10% +17% -7% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h_csrank_w50` `ts_scale(signedpower(cs_rank(add(day_quantile(Close), day_kurt(High)))), 50)` | hypo | 60 | +13.5% / +12.8% | +2.02 / +1.58 | 3.9% | +2.96 / +2.49 | +20% +9% -0% +21% +21% +5% +26% +3% |
| `sub_D_cs_rank` `ts_scale(signedpower(cs_rank(add(day_quantile(Close), day_kurt(High)))), 30)` | substitute | 60 | +12.5% / +12.8% | +1.86 / +1.56 | 5.4% | +2.92 / +2.63 | +18% +8% -1% +17% +22% +4% +27% +3% |
| `iso_E` `signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High))))` | isolate | 10 | +8.4% / +7.9% | +1.85 / +1.53 | 2.2% | +0.99 / +0.95 | +9% +2% +2% +12% +16% +12% +6% +6% |
| `h3_ov_div60` `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(div(day_median(Close), cross_med(d…` | hypo | 2 | +15.1% / +15.4% | +2.21 / +1.45 | 3.6% | +2.16 / +1.90 | +20% +11% +5% +16% +21% +21% +13% +13% |
| `h3_state_w_down` `add(mul(cs_state_rank(neg(day_last(Close)), 20), cs_rank(neg(ts_scale(signedpower(add(day…` | hypo | 10 | +13.6% / +14.1% | +2.12 / +1.55 | 6.3% | +2.09 / +1.46 | +23% +6% +3% +16% +18% +17% +12% +14% |

综合全文:`notes/F112_scale_spow_masktop/synthesis.md`;回测表与解剖:`./scripts/study.sh table F112_scale_spow_masktop s4`。

### 13. 挖掘 #1375(F113)

`pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret), 5), -5)), 30)), 20), 5))), 30))`

**它是什么(按算子定义)**:按源码逐层(节点记号取自 iso_*/abl_* 的 why):A=day_mean(Ret) 当天全部分钟收益的等权均值(没成交的分钟 Ret=0 也占一票);B=ts_max(A,5);C=sub(B,-5) 实际是 B+5;D=cs_demean(C) 减当日截面均值(+5 被精确抵消,C 在信息上是 no-op);E=ts_max(D,30) 近约 34 日内相对市场最强的一次脉冲(带符号);F=pow_2(E) —— pow_(x,e) 只在 e<=1 时是 signed power,e=2 走 x**2,符号被毁,"大幅上冲"与"长期远低于市场"同值;G=ts_max(F,20) 实际是约 53 日极端幅度的平方;H=mul(G,5) 正常数,秩上无用;I=cs_demean(H) "我的 53 日极端幅度离市场典型值有多远";J=pow_2(I) 第二次折叠;K=ts_max(J,30) "30 天里偏离过多少";L=pow_1_5(K),K>=0 故保序、秩上无用。最终 sg=-1 ⇒ 多头腿 = 53 日极端脉冲幅度最接近市场典型值、且 30 天没偏离过的股票,即"最不起眼"的那批;空头腿同时拿两条尾巴,所以多空夏普 2.54、底腿 -25.2%,而多头腿只有 +0.7%。名字与定义不符四处:(1) pow_2 折叠符号、pow_1_5 对负数返回 NaN,而 pow_05/signedpower 保号;(2) sqrt(x)=sqrt(|x|)、log(x)=log(|x|) 都折叠;(3) sub(B,-5) 是加 5;(4) 表头的 dist 不是"与已知族的距离",是 diagnose.distinct_fraction(逐日"不同取值数/有值股票数"的中位数,即并列/量化程度)。

**承重的子结构**

- 第一次 cs_demean + 两层 ts_max(D→E→F→G)承载全部预测力:iso_F/iso_G/iso_H/iso_I 都是 ut +7.7% / Lshp 1.15~1.18,而原式只有 +0.7% / 0.17 —— 预测力在这一层就齐了,后面四层是净损害
- B=ts_max(·,5) 不能删:abl_B ut +0.2%、valid -8.2%(原式 +0.7% / -1.7%)
- G=ts_max(F,20) 不能删:abl_G ut -2.1%、valid -9.1%
- E=ts_max(D,30) 不能删:abl_E ut -0.7%
- K=ts_max(J,30) 是把折叠后的量排成'没偏离过'的唯一节点:abl_K 翻成 sg=+1 且 ut -20.7%(iso_J 同样 -21.0%)⇒ 原式的 +0.7% 全部来自'不拿两条尾巴'
- C=sub(x,-5) 在精度上反向承重:信息上是 no-op,却把 float32 截面分辨率砸掉 78%(iso_B dist 1.00 → iso_C dist 0.22,ut 与 ρk 逐格相同 -2.6% / +0.50),是整族好子树爆 dist 门槛的唯一原因

**多余的节点**

- C=sub(B,-5):abl_C ut +0.6%(原式 +0.7%)且 dist 从 0.58 回到 1.00 —— 删掉是白送的清理
- H=mul(G,5):abl_H 与 sub_H_div 都是 ut +0.7% / Lshp 0.17 / LTO 4.0%,与原式逐格相同
- L=pow_1_5(K):iso_K ut +0.8% / 0.20,与原式同格
- 顶层 cs_winsor(win +0.7%)与顶层 cs_rank(rk +1.1%)都在噪声带内 ⇒ 原式的信息已经是序信息,没有尾部依赖
- I+J 这一整层(第二次 demean + 第二次平方)不只是多余,是损害:abl_I ut +8.6% / 1.21(+7.9pp)、abl_J ut +12.4% / 2.38(+11.7pp);但 abl_I dist 0.28、abl_J cov 0.43,两条都爆门槛
- 28 条 mem_* 全 <= +1.2%,多数为负、valid 掉到 -10% 级 ⇒ 日轴记忆全是多余
- 15 条 win_* 全在 ut -2.6%~+2.1%,没有一条出噪声带 ⇒ 窗口没有平台

**可互换的叶子**

- day_mean → day_gini:nosc_A_day_gini ut +6.3% / Lshp +1.44(原式 +0.7% / 0.17),cov 1.00、dist 0.97、ρo +0.06、ρk +0.20、LTO 2.4% —— 全表唯一既过门槛又显著赢原式的变体
- A 位置的其它 day_* 折叠都不可换:day_skew -0.8、day_max -3.4、day_min -2.8、day_median -5.7、day_quantile_q25 -3.6、day_close/day_last +1.4
- Ret → in_pct(Volume,1) / in_pct(Amt,1) / in_logchg(Volume,1)(用户提示的'分钟收益与量的变化率同类'):ut +2.8 / +2.3 / +2.8%,sg 翻成 +1,ρo 只有 +0.02~+0.04、dist 0.99~1.00 —— 语法上可换,但换完是另一条因子,数值仍在噪声带内
- Ret → in_pct(Close,5)(5 分钟收益):ρo +0.81、ut -0.2% ⇒ 与分钟收益是同一个东西,不算真互换
- Ret → in_pct(Vwap,1):ut -2.1%、dist 0.42 ✗,不可换
- J 位置的算子按'折叠 vs 保号'二分可换:折叠的(abs_ +0.8%、sqrt +0.8%,cov 1.00)全等于原式;保号的(abl_J/pow_1_5/pow_05/signedpower/inv)全在 +11.8~+13.7% 但 cov 全是 0.43

**在哪类股票里有效**

- 成交额(20日)最高 20%:段内 +8.8%(全市场多头书超配 +4.8pp)—— 原式唯一真正有段内信息的流动性档
- 成交额其余四档全负:-7.3 / -2.9 / -3.3 / -1.3%(最低档被低配 -6.7pp)
- 近 15 日有冻结盘口(封板/停牌,占 6.5%):段内 +11.9%;近 15 日无冻结的 93.5%:段内 -2.3%
- 板块:沪主板 +0.5、深主板 +0.1、创业板 -1.5、科创板 -8.8%
- 市值五档 -0.9~+0.7%、价格五档 -2.0~+1.0%、上市不足 250 日 -2.3% —— 全无区分力
- 桶内中性后几乎归零:bk_known +2.8% / Lshp 0.89、bk_liq +2.7% / 0.89、res_liq +3.1% / 0.96(全在 ±3pp 噪声带内)
- 对照 day_gini 版(nosc_A_day_gini)的有效段完全不同:小市值 +5.8% → 大市值 -1.9% 单调下滑,上市不足 250 日 +17.9%,沪/深主板 +6.1 / +6.9%,科创板 -7.0%,有冻结盘口 -41.4%
- 对照已知族 k_known:段内在所有成交额档里都是负的(-4.1/-5.3/-8.2/-5.2/+2.5%),多头书超配最低成交额档 +80.3pp ⇒ 它的信息就是成交额分档本身

**什么时候有效**

- 逐年 2018-2023:-3.4 / +7.0 / +4.5 / -1.7 / +1.1 / -6.3% —— 6 年里 3 年为负,没有稳定性
- 市场近 20 日下跌 +3.8% vs 上涨 -1.4%:弱逆周期
- 截面离散度高 +2.2% vs 低 -0.8%
- 缩量 +1.3% vs 放量 -0.1%;市场波动高 +0.5% vs 低 +1.0%(无区分)
- 全部幅度都在 ±3pp 噪声带附近,时间维度上没有一个可依赖的时段
- 对照 day_gini 版:逐年 +13.0 / +4.5 / -3.8 / +7.8 / +9.6 / +7.0%(6 年 5 正),且状态依赖是**反**的 —— 上涨 +11.2% vs 下跌 +0.4%、放量 +7.6% vs 缩量 +5.2%
- 对照 k_known:逐年 6 年全正(+17.3 ~ +24.7%),上涨 +23.0% vs 下跌 +6.0%

**原因推断**:两条机制。(1)活跃度分类器:F=E^2 的截面均值由当日那一小撮极端票(多为小市值、低价、封板)决定,所以 I="离截面典型值的距离"实际在问"我和今天的极端票是不是同一个活跃度等级"——这解释了为什么它只在成交额最高档有段内信息(+8.8%),而在成交额/流动性桶内中性后只剩 +2.7~2.8% / Lshp<1。(2)冻结分钟探测器:盘口冻结时几乎每分钟 Ret=0 ⇒ A≈0 ⇒ D≈-mean(B) ⇒ E^2 稳定偏大 ⇒ J 长期远离均值 ⇒ 因子高 ⇒ sg=-1 把它做空,于是有冻结盘口的 6.5% 段内 +11.9%、无冻结的 93.5% 段内 -2.3%。这正是 docs/new_operators.md 记的 F108 教训(峰度类算子读到的其实是冻结状态)在本因子上的重演。可检验推论:(i) 叶子换成 day_flat_ratio(Ret) 应复现原式的大部分(h_f1/h_f2);(ii) 在成交额十分位内做桶内排名应把它打回零(h_q1/h_r3);(iii) 反过来用活跃度当放大器应更好(h_q2)。day_gini 为什么反而能用:它有界 [0,1] 且无尺度,双层折叠在它上面不再爆量纲,剩下的是"日内波动有多集中在少数分钟"=消息/散户脉冲强度,"30 天里一直接近典型值"于是选出日内行为稳定的票——这在次新(+17.9%)与小市值(+5.8%)里信息最多(报价稀疏、脉冲明显),在封板票上直接反向(-41.4%,gini→1 但那是坏事)。推论:其它有界/无尺度叶子(day_pos_ratio、day_centroid、day_signed_ratio)应更像 gini 而非 day_mean(h_b1~h_b3、h_v5);在冻结度桶内中性后 gini 若塌,说明它只是在躲封板票(h_f3)。

**相对已知成交额族**:没有增量。ρk(原式)=-0.02 看着正交,但正交不等于有增量:六条 overlay 里最好的 ov_p025 是 ut +14.8% / Lshp 2.27,已知族 k_known 自己是 +15.4% / 2.22(Δ -0.6pp / +0.05,两项都在噪声带 ±3pp / ±0.3 内);权重一加大就单调变差(ov_p05 +13.0 / 2.24、ov_p10 +10.7 / 2.19),负权同样单调(+14.3 → +13.1 → +10.8,Lshp 2.10 → 1.99 → 1.78)。正交残差本身很弱:res_known +2.6% / 0.76、bk_known +2.8% / 0.89、res_liq +3.1% / 0.96、bk_liq +2.7% / 0.89，全在噪声带内且 Lshp<1。更要命的是另一侧:这棵树里"有信息"的那段本身就有一半是已知族——iso_B 与 k_known 的 ρk=+0.50、iso_E~iso_I 族 ρk +0.42~+0.46，而力度只有已知族的一半(+7.7% vs +15.4%)。与第 3 轮读留出段得到的"负增量"(f_cb 在 holdout 掉到 +8.93%,低于 f_kf30 的 +14.10%)一致。唯一可能有增量的不是本因子,是它的叶子替换 day_gini(ρo 0.06、ρk 0.20),那应按新因子对待——h_k1/h_k2/h_k3 专门测它。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(ts_max(day_mean(Ret)…` | base | 1 | +0.7% / -0.6% | +0.17 / -0.15 | 4.0% | +2.54 / +1.09 | -3% +7% +4% -2% +1% -5% +1% -2% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_g6_bdemean` `cs_bucket_demean(cross_mean(day_gini(Ret), 30), cross_mean(day_sum(Amt), 30))` | hypo | 20 | +11.2% / +6.0% | +3.21 / +1.26 | 1.8% | +3.33 / +1.62 | +5% +9% +11% +12% +18% +10% +6% +6% |
| `seg_lowliq_m` `cs_first_low40(neg(pow_1_5(ts_max(pow_2(cs_demean(mul(ts_max(pow_2(ts_max(cs_demean(sub(t…` | segment | 10 | +10.7% / +13.3% | +2.09 / +1.86 | 2.5% | +2.74 / +2.04 | +8% +8% +0% +17% +18% +15% +10% +13% |
| `sub_I_cs_mask_top_replace_mean_neg` `pow_1_5(ts_max(pow_2(cs_mask_top_replace_mean_neg(mul(ts_max(pow_2(ts_max(cs_demean(sub(t…` | substitute | 2 | +6.5% / +3.6% | +1.26 / +0.52 | 3.5% | +2.27 / +0.80 | +5% +8% -0% +7% +13% +5% +6% +2% |
| `h3_ov_g6_xfrozen` `cs_last_high20(neg(add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cs_bucket_rank(…` | hypo | 3 | +18.8% / +14.9% | +3.26 / +1.56 | 3.3% | +4.41 / +3.20 | +20% +15% +13% +18% +27% +21% +12% +15% |
| `h3_ov_g6_025` `add(cs_rank(cross_mean(day_std(Amt), 30)), mul(cs_rank(cs_bucket_rank(cross_mean(day_gini…` | hypo | 0 | +17.8% / +13.8% | +2.78 / +1.37 | 4.4% | +3.25 / +2.70 | +20% +12% +10% +17% +29% +20% +10% +14% |

综合全文:`notes/F113_nested_tsmax_demean/synthesis.md`;回测表与解剖:`./scripts/study.sh table F113_nested_tsmax_demean s4`。

### 14. 挖掘 #1421(F114)

`cross_quantile_q25(day_close(Ret), 15)`

**它是什么(按算子定义)**:按函数定义逐层:① `Ret` = 分钟收益(241 根分钟轴);② `day_close(x)` 是 `day_last` 的**别名**,内核 `last_valid_last` = 取当天最后一个非 NaN 的分钟值 → 喂 `Ret` 得到的是「当天最后一个有效分钟**自己那一笔**分钟收益」,既不是收盘价也不是当日收益(`day_close` 这个名字和文件名 `q25_closeret` 都骗人);③ `cross_quantile_q25(x, 15)` = `torch.nanquantile(rolling_windows(x, 15, axis=0), 0.25)`,而 `rolling_windows` 的 axis=0 是**交易日轴**(因果、左侧 NaN 填充)→ 近 15 个交易日这 15 个「收盘分钟收益」的第 25 百分位。方向 sg = −1,所以交易信号 = −q25,多头书 = 近三周里收盘分钟跌得最深那天跌幅最大的票。恒等式 `−q25 = (scl − loc)/2`(四分位距与四分位中点 1:1 混比)。关键事实是**输入在 0 上有一个点质量**(封板 / 停牌 / 无收盘成交的分钟收益恰好为 0),q25 的真实作用是「伸到这个原子下面去」。

**承重的子结构**

- 叶子 + 孔径(day_close(Ret) 这一对不可替换):day_mean / day_sum → utrain −15.9%、Lshp −2.11、ρo 0.00、方向翻转(全表最彻底的塌陷);day_max −3.6%、day_min −4.8%
- 1 分钟的粒度:把孔径放宽到 5 分钟(leaf_Ret_ret5 = in_pct(Close,5))→ +0.1%(原式 +3.6%);in_pct(Vwap,1) → +0.7%。0 原子只在 1 分钟粒度上存在,放宽就溶解
- 日轴低通本身必需:不滚动的 iso_A 毛超额全研究最高但净 −2.0%、LTO 10.5%;任何滚动都把净超额救回来
- 持久的截面水平(不是时序事件):cross_zscore 四个窗口全塌(−7.1/−6.7/−4.8/−2.8)、rel60(除以自己 60 日均值)−5.4%
- 方向性(不是极端性):折叠成 abs/pow_2 全部破坏 —— fold_mean +1.7%、fold_sq +0.4%、fold_rank −2.7%,底腿转负

**多余的节点**

- 「必须是 q25」对多头腿未被证实:同槽位 cross_ema +1.8% / cross_mean +1.0% / cross_decay_linear +1.2% vs q25 +3.6%,差 ~2pp 在 ±3pp 噪声带内。需要下尾读数的是**空头腿**(底腿 +19.0% vs q50 的 +0.2%、LS +2.36 vs −0.02),而用户用不上
- 保序的外层变换是 no-op:cs_winsor +3.4%、cs_rank +3.2%(原式 +3.6%)→ 载重的是秩不是幅度
- 外记忆与内窗互为替代、不叠加:w60 的 hlL 自动从 20 掉到 3;慢化(w5→w60 +2.9→+5.1%,mem_ema30 +5.0%)一共只值 +1.4pp / +0.23 夏普,毛超额不随慢化上升 → 买到的全是换手,没有新信息

**可互换的叶子**

- 叶子基本不可换 —— 这正是本轮的发现。用户「分钟收益 Ret 和成交量的变化率是同一类东西」在这棵树上**不成立**:leaf_Ret_volchg / leaf_Ret_amtchg(in_pct(Volume/Amt, 1))dist **0.00**(完全退化),in_logchg(Volume,1) → −4.1% 且 ρk +0.37(变成一条纯流动性因子)。原因很具体:载重的是最后一分钟价格变动的**符号与幅度**,而量没有符号
- 可换的只有两处:① 保序外层变换(cs_rank / cs_winsor 互换、与原式等价);② 日轴平滑器家族内部(cross_mean / cross_ema / cross_decay_linear,在 ±3pp 内彼此可换;mem_* 一列 30/60 天四种写法全在 +4.8~+5.0%)
- day_durbin_watson 可以**替掉整个** day_close 孔径而不损失(+4.9%、valid +11.1%,ρo 只 +0.36、dist 1.00)—— 它不是「同一个东西的另一种写法」,而是一条独立支线,这是表里唯一值得接着做的结构替换

**在哪类股票里有效**

- **成交额桶内全是负的**:20 日成交额五分位的段内自建多头书 −0.7 / −2.7 / −6.5 / −4.2 / −5.1%,五个桶一个不剩。全市场 +3.6% 完全来自持仓倾斜(最低成交额桶超配 +10.7%、次低 +4.2%、最高 −10.2%;对应段等权超额 +15.1% … −17.8%)→ 多头腿的超额是跨桶的低流动性倾斜,不是桶内选股
- 旁证:bk_liq +1.6% / bk_known +1.2%(两者 dist 0.20 不算候选,方向一致)、res_known +1.8% / res_liq +1.8%(train 只 +0.4% / +0.1%,在噪声带内)
- 市值:流通市值最低 20% 段内 +10.9%(段等权 +6.4%),60–80% 段内 −7.9%、最高 20% −1.3% → 在中大盘活跃票上是负贡献
- 板块:创业板 +6.8%、科创板 +5.9%、深主板 +4.8%,沪主板只 +1.3%;价格最低 20% 段内 +2.7% 且持仓超配 +14.5%
- **唯一打赢已知族的地方 = 病态段**:近 15 日有冻结盘口(封板/停牌)段占 6.5%、段等权 −67.4%,这棵树段内 +7.7%(mem_min60 +21.6%),而 k_known 在这一段 **−10.9%**;上市不足 250 日段占 7.1%、段等权 −28.7%,这棵树 +18.1%(mem_min60 +21.8%),k_known +8.6%

**什么时候有效**

- 只有 2021 年以后:2018 +0.0% / 2019 −1.3% / 2020 −2.2% / 2021 +10.4% / 2022 +9.6% / 2023 +6.0%(k_known 六年全正,最差 +6.7%)
- 截面离散度:高 +7.3% vs 低 −0.0%(本轮最干净的状态切分)
- 成交量:放量(高于 60 日均)+7.9% vs 缩量 +0.1%
- 市场方向:近 20 日上涨 +8.5% vs 下跌 −2.4%(k_known 在下跌段仍 +6.0%)
- 市场波动:高于中位 +2.7% < 低于中位 +4.6% → **它不是波动率交易,是离散度 + 成交量交易**,即 2021–2023 的微盘/题材制度(与 H11 一致,留出段 20230808 以后只剩 +0.2~+2.1% 也印证)

**原因推断**:机制推断:封板、停牌、无收盘成交的票,其分钟收益恰好为 0 → 15 日「收盘分钟收益」的 q25 被钉在 ≈0,落在有符号信号的最高端,被排除出多头书;正常交易的票收盘分钟是噪声 ±,**越不流动,第 25 百分位越深**。所以 −q25 ≈(收盘分钟冲击幅度)−(收盘分钟漂移)= **一个带内置「冻结盘口」探测器的微观冲击计**。这一句同时解释了两件事:幅度那一半产生跨成交额桶的流动性倾斜(已知族做得更好、而且单调),原子那一半产生病态段里的避险能力(已知族在那儿反而亏钱)。可检验推论,前四条大表已证:① q50 应该死在原子上 → dist 0.16、底腿 +19.0→+0.2% ✓;② 孔径放宽到 5 分钟原子溶解、因子应该死 → +0.1% ✓;③ 优势应集中在封板/次新段 → +7.7% / +18.1% ✓;④ 量侧叶子因无符号而退化 → dist 0.00 ✓;⑤ 若它是冲击计,day_flat_ratio 应能复现原子那一半、day_wmean / day_signed_ratio 应做得更干净 → 未测(第二批 A/B 组);⑥ 若制度依赖是「离散度 + 放量」,把这个状态写进表达式当权重应比任何结构改动更有用 → 未测(第二批 H 组)。

**相对已知成交额族**:**没有增量,而且是负的(比上一轮的「wash」更强)**。ρk 只 +0.21、res_known 与家族相关 −0.04 且 rIC 保住 → 它**确实是别的东西**;但 6 个 overlay 权重点**全部严格低于家族单独**,且 |w| 单调向下:k_known +12.6/+22.3/**+15.4%**(train/valid/utrain,Lshp 2.22)vs ov_p025 +10.2/+19.7/**+12.9%**、ov_p05 +9.8/+17.7/**+12.5%**、ov_p10 +8.8/+18.3/**+11.5%**、ov_m025 +10.4%、ov_m05 +7.3%、ov_m10 +3.9% —— 两个分段同向,不是噪声。残差腿 res_known / res_liq 只 +1.8%(train +0.4% / +0.1%)在噪声带内。留出段再次印证:f_add(等权组合)+10.6% vs f_fam(家族单独)**+14.1%**,差 3.5pp。结构上的原因比统计上的更硬:成交额桶内五个全负 → 增量不是「小」,而是**根本不在桶内**。**唯一活口**:近 15 日有冻结盘口那 6.5% 的票,家族 −10.9% 而这棵树 +7.7% → 增量如果存在,只能以**单尾筛子**的形式(凸罚项 / 两秩相乘的软 AND),不能以线性混合的形式。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `cross_quantile_q25(day_close(Ret), 15)` | base | 40 | +4.5% / +0.4% | +0.83 / +0.05 | 2.0% | +2.36 / +0.91 | +3% -3% -3% +13% +10% +4% +9% -7% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `h3_xfr_own_slowf` `cs_last_high20(neg(cross_ema(cross_quantile_q25(day_close(Ret), 60), 30)), cross_max(day_…` | hypo | 5 | +9.2% / +3.7% | +2.44 / +0.68 | 2.5% | +4.68 / +2.46 | +8% +8% +5% +13% +12% +8% +7% -1% |
| `seg_lowliq_m` `cs_first_low40(neg(cross_quantile_q25(day_close(Ret), 15)), cross_mean(day_sum(Amt), 30))` | segment | 60 | +12.1% / +9.8% | +1.94 / +1.35 | 1.3% | +2.18 / +1.45 | +11% +8% +4% +12% +22% +19% +3% +11% |
| `mem_max30` `cross_max(cross_quantile_q25(day_close(Ret), 15), 30)` | memory | 20 | +3.8% / +1.3% | +1.15 / +0.19 | 2.4% | +1.22 / -0.43 | -3% +3% +1% +6% +7% +6% +8% -5% |
| `h3_xfr_plus_slowf` `sub(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Re…` | hypo | 2 | +19.5% / +14.7% | +3.48 / +1.95 | 3.5% | +4.23 / +3.01 | +21% +17% +13% +20% +27% +21% +12% +14% |
| `h3_xfr_plus_state` `add(cs_rank(cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Re…` | hypo | 3 | +19.3% / +13.7% | +3.43 / +1.87 | 4.4% | +3.62 / +2.58 | +19% +16% +12% +22% +27% +21% +10% +13% |

综合全文:`notes/F114_q25_closeret/synthesis.md`;回测表与解剖:`./scripts/study.sh table F114_q25_closeret s4`。

### 15. 手写 all_tide_mean_30(F115)

`cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211),…`

**它是什么(按算子定义)**:20 日平均的「盘中潮汐反转」。分钟轴是 241 列(第 0 列 = 09:30 集合竞价,1–120 上午,121–240 下午),in_slice 两端都含,所以 in_slice(·,31,211) = 约 10:00–14:30 的 181 分钟,恰好切掉开盘与尾盘各半小时。逐层:SM = in_local_mean(成交量, 5) 是**居中 9 分钟**均值(算子元数据 lookahead=True,半径 d−1=4);D = day_argmax(SM) = 盘中量峰的分钟下标;F = day_argmin(in_slice_to_end(SM, D)) = 峰**后**量最低那一分钟;I = day_argmin(in_slice_from_start(SM, D)) = 峰**前**量最低那一分钟;G / J = 这两分钟的 Close;K = G − J,L = K / J = 「峰前谷 → 峰后谷」的收益率;M = F − I = 两谷之间的分钟数;N = L / M = 每分钟平均收益;O = cross_mean(N, 20)。sign = −1 → 多头 = 这个分钟化收益最负的十分位,即 20 日日内反转。名字与定义不一致处:(1) 名字写 30,窗口其实是 **20**;(2) mean 指日轴而非日内;(3) 库里有 day_tide_change / day_tide_speed,但这棵树**没用**它们(那两个吃三个给定下标 a/b/c,这棵树自己从量曲线找 argmax/argmin,不等价);(4) **Volume 只贡献下标**,整棵树里成交量从不进入数值,只决定在哪一分钟读 Close(leaf_Volume_amt 的 ρo = +0.99);(5) in_slice_to_end 与 in_slice_from_start 在 D 这一列**重叠** → F ≥ D ≥ I,M ≥ 0 且量曲线单调时 M = 0 → 除零,这就是 abl_E / abl_H 一删就 cov = 0.00(+388.6% / −335.1% 的垃圾数)的原因:这两个节点是**结构必需、不携带信息**,不要读成「载重」。

**承重的子结构**

- F = 峰**后**那个读数点的位置(非对称承重):sub_F_*(把 F 换成 day_autocorr_n1 / day_ar1_coefficient / day_hurst)全塌且方向翻 −3.6/−12.5%、−3.3/−11.8%、−8.3/−4.0%;而对称位置的 sub_I_*(换峰**前**谷)完全不掉 +5.0/+2.2%、+4.9/+2.0%、+4.5/+1.3%
- ÷J(把价差变成收益率):abl_L(除 M 不除 J)+3.8/−4.3% 明显差于 abl_N(除 J 不除 M)+6.4/+2.0%
- K = sub(G, J) 这个差分本身(消掉价格水平):iso_G / iso_J 单独跑就是低价书(+3.7/+11.4%、+3.4/+10.8%,ρo 仅 +0.02、LTO 1.2%),去掉 sub 的 sub_L_add / sub_K_mul / sub_L_sub 全退化成 train≈0 / valid +6.7% / LTO 0.6% 的慢倾斜
- 最外层 cross_mean(·, 20)(日轴平均):iso_N(不平均)+0.0/−7.0%、LTO 14.2%、毛 +10.8% —— 平均把 21% 的换手压到 5%,原式 hl0 = −6.2% 全靠它变成 +5.6%
- 外层窗口有真平台:10/15/20/30/60 → ut +3.7/+4.0/+4.1/+4.4/+4.4%

**多余的节点**

- 分母 M = sub(F, I) 完全空转:sub→div +6.2/+2.3%、sub→mul +5.3/+0.9%(都 ≈ 原式);整条删掉(abl_N)反而更好 +6.4/+2.0% 且 LTO 5.1%→3.7%、hl20 最佳;算术上 abl_K 与 only_K_R 都塌成 cross_mean(1/M, 20)(1/M ~ 1e−2 压过 N ~ 1e−4),两者数字一致(−2.8/+7.2% 与 −2.4/+7.4%)
- I = 峰前谷的位置:把 day_argmin 换成值域 [−1,1] 的 autocorr/hurst/ar1(等于 M := F)后与 abl_M(+4.9/+0.8%)一致,全不掉
- 内层 in_local_mean 的 9 分钟平滑:win_C 3/5/10/15 → ut +4.5/+4.1/+5.2/+5.1%(非单调,没有平台),而**完全不平滑**(abl_C)+6.5% 最好 —— 这个参数是噪声,去掉是改进
- 幅度信息:rk(EMA 前先 cs_rank)+5.5/+0.3% 与原式逐位级一致 → 信息全在秩里;cs_winsor +5.5/+1.6% 也只是略好
- in_slice 的两端(abl_A / abl_B 各只改了一处,ρo = 1.00 / 1.00,+5.4/+0.3% 与 +4.4/+1.4%)—— 但注意这两行只动了 M 子树里的单个出现,不能据此说整个 10:00–14:30 口径多余(h_aperture_full 才是那个检验)

**可互换的叶子**

- Close → Low / Open / High(ut +4.2/+4.0/+4.2%,原式 +4.1%);Vwap 略差(+2.6%)
- Volume → Amt(ρo +0.99,ut +4.5%)—— 因为 Volume 只贡献下标,日内形状两者几乎相同
- in_local_mean → in_med / in_max_rolling(+5.3/+3.2%、+5.2/+2.1%)、→ in_pct(用户提示的「量的变化率」,+4.7/+3.2%,valid 比原式好)—— 但**不能**叠在平滑之外:leaf_Volume_volchg(先 in_pct(Volume,1) 再平滑)+4.0/−5.0%
- 注意不可换的:cross_mean → cross_med 掉到 +3.4/−4.1%(信息在尾部天数,中位数杀掉);→ cross_delta / cross_zscore / cross_argmax 全崩(−13.6 ~ −16.5%);日轴记忆里 cross_stddev / cross_zscore 全是 train 负 valid 正的符号不稳垃圾

**在哪类股票里有效**

- 板块:段内 沪主板 +3.8% / 深主板 +5.0% / 创业板 +2.0% / **科创板 −22.8%**(段等权 −0.3/−1.1/+1.8/+4.1%),十个变体在科创板全是 −17.6 ~ −33.7%,而全市场多头书却**超配科创板 +6.6pp**。顺序与日涨跌幅上限(10/10/20/20%)一致
- 成交额(20日)五档段内 −1.1/−4.6/−2.0/+2.7/**+7.2%** —— 选股力只在最活跃的两档;而段等权超额 +15.1/+8.9/+2.6/−6.0/**−17.8%** —— 溢价全在最清淡的两档。两边方向相反,这是纯多头的死结
- 流通市值五档段内 +1.6/+1.9/+3.3/+2.2/+1.9%(**平的**)→ 它不是规模/流动性因子;bk_liq 中性化不掉(+5.4/+0.7% ≈ 原式)。对比已知族 +9.3/+9.5/+9.2/+3.5/+0.7%(纯小盘)
- 价格:段内 +2.1/+2.3/**+8.3**/+1.4/−0.5%(中间档最好),段等权 +7.0/+4.3/+0.5/−6.1/−3.8% → 「价格 40–60% 档」是唯一段内与段等权同时非负的格子(+8.3 + 0.5)
- 次新(上市 < 250 日,占 7.1%)段内 **+12.4%**(abl_C +15.1%、sub_M_div +16.7%;但 rank_K −3.4%),段等权 **−28.7%** → 段内 + 段等权 = **净 −16%**,不可投
- 近 15 日有冻结盘口(封板/停牌,占 6.5%)段内 **+18.2%**(全表第一;sub_C_in_med +17.7%、abl_C +13.4%、rank_K +11.6%),段等权 **−67.4%** → 净 −49%,不可投

**什么时候有效**

- **市场波动高于中位 +10.4% vs 低于中位 −2.2%** —— 全表最强的时间切分,十个变体一致(+7.6 ~ +12.5% 对 −0.9 ~ +2.0%);已知族 +18.5 / +12.4%(几乎不挑)
- 市场近 20 日**下跌 +5.4% vs 上涨 +3.1%** —— 与已知族正好互补(已知族 涨市 +23.0% / 跌市 +6.0%,是个牛市因子)
- 逐年 2018→2023:原式 +6.4/+13.6/+2.8/−0.6/−0.4/+1.6%(2019 之后就死了);abl_C +14.7/+5.3/−0.2/+4.3/+6.2/+9.7%;rank_K +9.2/+6.0/−2.3/+8.4/+8.2/+12.4%(六年五正,2022–23 最好)—— **衰减不是它自己的,是内层加工造成的**
- 没有切分力的状态:截面离散度 高 +4.4 / 低 +3.9%;放量 +3.4 / 缩量 +4.7%

**原因推断**:机制推断:in_slice(·,31,211) 把开盘与尾盘各半小时切掉,强迫 day_argmax 找到的是**盘中**的成交量峰 —— 那不是开收盘集合竞价的机械放量,而是一次资金事件。因子读的是「这次事件前后价格漂了多少」,再按 20 日平均。它在上限 10% 的主板里有效,是因为那里盘中放量多是散户/恐慌驱动、次日反转;在上限 20% 的创业板/科创板失效(科创板还有 50 万门槛、机构占比高、分钟流动性薄),是因为量峰后的漂移更接近趋势延续,而且两个「谷底分钟」几乎没有成交,day_locate 读到的是噪声价。次新段(+12.4%)与冻结盘口段(+18.2%)选股力最强,因为那里的量曲线有真正尖锐的峰(炒作、封板瞬间的放量后冻结),事件越干净定位越准。只在高波动 / 跌市有效,也符合「放量 = 恐慌卖出 → 次日反转」;低波动时量峰只是流动性噪声。**可检验推论**:(i) 用「近 60 日单日最大毛涨幅」当涨跌幅上限代理分桶,段内差异应复现板块排序(h_bk_limit / h_sieve_limit);(ii) 科创板的 day_gini(Volume) 应更低、|rank IC| 更小;(iii) 若「薄分钟的价格读数是噪声」成立,把锚点挪到有成交的分钟(上午/下午各自的量峰)应更干净(h_amvol_pmvol);(iv) 若它只是净买压的噪声代理,day_signed_ratio(Ret, Amt) 应明显更强(h_signed_ratio);(v) day_gini / day_flat_ratio 越高段内 IC 越高。但**最根本的发现是半衰期曲线**:原式 hl0 = −6.2% → hl10 = +5.6%,而**毛**超额在 hl 0→20 走平(+9.8…+7.3%)→ 净超额**全部**是换手从 ~21% 压到 5% 换来的,毛 ~9% 封顶;已知族 hl0 就 +12.6%、LTO 3.4%、越平滑越差。**它的信息是日频、薄的;已知族的信息是慢、厚的** —— 这决定了它在扣 15bp 的纯多头口径里永远打不过。

**相对已知成交额族**:**没有增量,但不是「就是已知族」**,三条证据:(1) 六条固定权重 overlay 全部严格差于已知族单独,且单调:w = +0.25/+0.5/+1.0 → ut +14.2/+12.9/+11.9%,w = −0.25/−0.5/−1.0 → +10.9/+8.7/−3.6%,已知族 **+15.4%**;w = 0.25 的 −1.2pp 在 ±3pp 噪声带内 → 结论是「拿不到增量」,不是「掺进去会亏」。(2) ρk 只有 **+0.26**,且中性化**不掉**:bk_liq +5.4/+0.7%、bk_known +5.2/−0.4% 都 ≈ 原式 → 它是一条独立但更弱的信息,不是已知族换个写法;残差化(res_liq +4.4/−2.6%、res_known +3.7/−3.3%)会杀掉 valid → valid 里它剩下的那点东西本来就是与已知族重叠的部分。(3) **机制已查明**:倾斜方向相反 —— 已知族赚的是流动性溢价的**倾斜**(段内几乎为 0,却超配最低成交额档 **+80.3pp**),F115 的选股力在**活跃票**里(段内 +7.2% 在最高档),而它的书对倾斜几乎中性(最低档只超配 +3.0pp、最高档 −2.0pp)。线性混合是在同一个秩空间里打架。**表里没试过的那一格** = 倾斜交给已知族、F115 降级为桶内排序器:add(cs_rank(known), mul(cs_bucket_rank(F115, Amt), w)) —— 已写成 h_mix_known_bk025 / _bk05 / _bk_rk,是第二批的最高优先级。另一条未试的角度:两者在跌市互补(F115 跌 +5.4 / 涨 +3.1,已知族 跌 +6.0 / 涨 +23.0),固定权重失败 ≠ 条件权重失败 → h_regime_mix / _rk / _dn 用 sigmoid(z)+sigmoid(−z)≡1 做无字面常数的凸组合。

**测试段读数(候选按规则选出)**

| 候选 | 类 | 半衰期 | 多头净超额 训练 / 测试 | 纯多头夏普 | 日换手 | 多空夏普 | 逐年多头净超额 2018…2025 |
|---|---|---|---|---|---|---|---|
| `v_base` `cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in…` | base | 40 | +3.9% / +0.6% | +0.88 / +0.09 | 2.4% | +2.29 / +1.65 | +3% +12% +3% -2% +4% -0% +2% +2% |
| `k_known` `cross_mean(day_std(Amt), 30)` | bench | 0 | +15.4% / +14.1% | +2.22 / +1.51 | 3.2% | +2.33 / +1.94 | +17% +10% +7% +16% +25% +21% +9% +14% |
| `k_known_xfrozen` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))` | bench | 3 | +18.5% / +15.0% | +3.13 / +1.61 | 3.2% | +4.34 / +3.26 | +24% +14% +11% +17% +26% +21% +12% +15% |
| `seg_lowliq_m` `cs_first_low40(neg(cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin…` | segment | 10 | +11.8% / +8.0% | +2.01 / +0.93 | 4.1% | +2.55 / +1.76 | +15% +10% -1% +12% +19% +17% +4% +8% |
| `h3_raw_amt` `cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in…` | hypo | 10 | +6.9% / +3.8% | +1.77 / +0.62 | 4.6% | +2.31 / +1.55 | +11% +7% +4% +7% +4% +6% +0% +8% |
| `abl_C` `cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in…` | ablate | 10 | +6.5% / +5.9% | +1.49 / +0.85 | 4.5% | +2.32 / +1.48 | +15% +5% -0% +4% +6% +9% +1% +10% |
| `scr_xhi_p` `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_mean(div(div(sub(day_locate(in_sl…` | screen | 1 | +15.2% / +12.6% | +2.25 / +1.34 | 3.6% | +2.87 / +2.12 | +19% +10% +5% +15% +24% +21% +7% +13% |
| `h_regime_mix_rk` `add(mul(cs_rank(cross_mean(sub(cs_rank(day_locate(in_slice(Close, 31, 211), day_argmin(in…` | hypo | 2 | +12.5% / +10.4% | +2.23 / +1.23 | 7.8% | +2.65 / +2.10 | +20% +11% +1% +15% +15% +16% +7% +11% |

综合全文:`notes/F115_all_tide_mean_30/synthesis.md`;回测表与解剖:`./scripts/study.sh table F115_all_tide_mean_30 s4`。
