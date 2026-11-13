# W02L 新合成(头部边际贡献)的样本内描述(2026 未读)

做法见 SYNTH_PLAN.md。下面全是描述，不是检验;检验要等 2026-09-16 以后的新数据。

## S:拟合 20180102 ~ 20251231,收了 13 个 head(候选 79)

| 步 | |t| | 收 | head |
|---|---|---|---|
| 1 | 3.75 | 是 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), cs_last_low20(pow_05(sub(day_hurst(cross_ema(Volume, ` |
| 2 | 3.52 | 是 | `sub(cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), day_sum(Ret), 120)` |
| 3 | 3.50 | 是 | `mul(day_distinct_ratio(Volume), cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last` |
| 4 | 3.54 | 是 | `cs_last_low10(neg(sub(log(ts_mean(day_mean(Amt), 60)), LogFloatCap)), ts_std(ts_std(ts_std(day_mean(` |
| 5 | 3.42 | 是 | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), mul(cross_delay(cross_mean(` |
| 6 | 3.36 | 是 | `sub(mul(day_at_min_ratio(Ret), day_centroid(Amt)), cross_fangzheng(day_es_ratio_lo(Low), 241))` |
| 7 | 3.09 | 是 | `cs_first_low20(LogTotalCap, div(day_close(Close), cs_first_low20(LogTotalCap, div(day_close(Close), ` |
| 8 | 2.75 | 是 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(cs_first_low20(cs` |
| 9 | 3.95 | 是 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(cs_first_low20(Lo` |
| 10 | 3.31 | 是 | `cs_first_low20(LogTotalCap, div(cs_first_low20(LogTotalCap, div(day_close(Close), cross_max(cross_ma` |
| 11 | 2.94 | 是 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_corr(day_sum(Ret), cs_r` |
| 12 | 2.10 | 是 | `cs_first_low20(LogTotalCap, div(cs_first_low20(LogTotalCap, day_es_ratio_hi(inv(cross_max(Open, 241)` |
| 13 | 2.11 | 是 | `cross_regbeta(mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1)), day_sum(Ret), 120)` |
| 14 | 1.86 | 否 | `cross_corr(cross_delay(log(log(div(day_var(replace_small_with_nan(Amt)), pow_2(day_mean(replace_smal` |

权重(相对 B):+0.101;-0.142;+0.292;-0.146;-0.111;-0.194;-0.183;-0.207;+0.226;-0.235;+0.127;+0.119;+0.055

## S_nested:拟合 20180102 ~ 20230807,收了 15 个 head(候选 79)

| 步 | |t| | 收 | head |
|---|---|---|---|
| 1 | 4.31 | 是 | `sub(day_hurst(cross_ema(pow_1_5(Volume), 60)), cs_last_low20(pow_05(sub(day_hurst(cross_ema(Volume, ` |
| 2 | 3.49 | 是 | `mul(day_distinct_ratio(Volume), cs_first_low20(cross_mean(day_sum(Ret), 20), div(cross_mean(day_last` |
| 3 | 3.34 | 是 | `cross_regbeta(cross_delay(mul(cross_delay(cross_mean(mul(day_mean(High), mul(cross_delay(cross_mean(` |
| 4 | 3.26 | 是 | `cs_first_low20(LogTotalCap, div(day_close(Close), cs_first_low20(LogTotalCap, div(day_close(Close), ` |
| 5 | 2.76 | 是 | `cs_last_low10(neg(sub(log(ts_mean(day_mean(Amt), 60)), LogFloatCap)), ts_std(ts_std(ts_std(day_mean(` |
| 6 | 2.58 | 是 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(cs_first_low20(cs` |
| 7 | 3.88 | 是 | `cs_first_low20(cs_first_low20(LogTotalCap, ListAge), cross_mean(cross_mean(sub(div(cs_first_low20(Lo` |
| 8 | 3.50 | 是 | `cs_first_low20(LogTotalCap, div(cs_first_low20(LogTotalCap, div(day_close(Close), cross_max(cross_ma` |
| 9 | 2.55 | 是 | `sub(mul(day_at_min_ratio(Ret), day_centroid(Amt)), cross_fangzheng(day_es_ratio_lo(Low), 241))` |
| 10 | 2.51 | 是 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_corr(day_sum(Ret), cs_r` |
| 11 | 2.22 | 是 | `sub(cross_regbeta(mul(day_sum(Amt), cross_delay(day_ar1_coefficient(Volume), 1)), day_sum(Ret), 120)` |
| 12 | 2.27 | 是 | `cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_corr(day_sum(Volume), d` |
| 13 | 2.04 | 是 | `cross_regbeta(day_sum(Volume), ts_mean(day_skew(Volume), 10), 120)` |
| 14 | 2.13 | 是 | `cross_regbeta(mul(day_sum(Amt), cross_delay(cross_zscore(day_sum(Amt), 60), 1)), day_sum(Ret), 120)` |
| 15 | 2.10 | 是 | `div(cs_bucket_zscore(log(cross_stddev(ts_stddev(cross_fangzheng(cross_max(day_cov(Amt, Amt), 3), 241` |
| 16 | 1.90 | 否 | `cross_regbeta(day_sum(Amt), cross_regbeta(cross_delay(cross_delay(day_sum(Amt), 1), 1), day_max(cros` |

权重(相对 B):+0.126;+0.295;-0.121;-0.180;-0.136;-0.249;+0.285;-0.221;-0.182;+0.135;-0.118;+0.129;+0.095;+0.049;-0.082


## S 与 C_LX(都拟合到 2025-12-31)

| 信号 | hl | 段 | 纯多头净超额 | 夏普 | 回撤 |
|---|---|---|---|---|---|
| C_LX | 60 | insample | +21.3% | 3.53 | -9.2% |
| C_LX | 60 | valid | +21.5% | 2.57 | -9.2% |
| S | 5 | insample | +27.1% | 3.39 | -16.9% |
| S | 5 | valid | +24.7% | 2.20 | -16.9% |

成对差(纯多头逐日净超额):insample +5.83%(t +3.81);valid +3.19%(t +0.97)
多空成对差:insample +2.62%(t +4.54);valid +2.36%(t +2.30)


## S_nested(头部层拟合到 2023-08-07)与 C_LX,valid 段(偏向新 head)

| 信号 | hl | 段 | 纯多头净超额 | 夏普 | 回撤 |
|---|---|---|---|---|---|
| C_LX | 10 | train | +24.3% | 4.59 | -5.2% |
| C_LX | 10 | valid | +22.3% | 2.36 | -10.9% |
| S_nested | 10 | train | +28.4% | 4.69 | -7.0% |
| S_nested | 10 | valid | +24.5% | 2.23 | -16.7% |

成对差(纯多头逐日净超额):valid +2.25%(t +1.02)
多空成对差:valid +1.99%(t +1.86)


## 风险诊断(截短视窗，不碰 2026;`scripts/w02l_synth_diag.py`)

| 信号 | hl | 多头持仓平均流通市值分位(全段 / valid) | 最大回撤及区间 | valid 最差三天 |
|---|---|---|---|---|
| C_LX | 60 | 0.354 / 0.296 | −9.2%,2024-01-16 ~ 02-06 | 04-12 −4.1%;02-02 −2.8%;02-27 −2.6% |
| S | 5 | 0.272 / 0.246 | −16.9%,同一区间 | 04-12 −4.9%;02-02 −4.7%;02-27 −3.6% |
| S_nested | 10 | 0.276 / 0.251 | −16.7%,同一区间 | 04-12 −5.0%;02-02 −4.5%;02-27 −3.5% |

**读法:** 新合成多出来的 2–3 个点净超额，相当一部分来自更小的市值(收进来的 13 个 head 里 5 个是 `cs_first_low20(LogTotalCap, …)` 一类)。代价是 2024 年初微盘踩踏时回撤几乎翻倍，夏普没有提高(valid 2.20 / 2.23 对 2.57 / 2.36)。尺子 D 在挑 head 时扣掉了市值十分位，但新合成在池内重排时又把市值暴露带了回来。
