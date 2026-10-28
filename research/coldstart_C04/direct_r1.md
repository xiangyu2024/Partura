# C02 直接检验(第 1 轮):5 个假设、64 个变体(= B 组 64 次付费评估)

score = 纯多头十分位书扣 15bp 的 train 与 valid 夏普中较差的;发现 = score ≥ 0.5 且未被相关度拒绝(|ρ已知| ≥ 0.5);门槛:覆盖率 ≥ 0.9、取值离散度 ≥ 0.5。

## H1_net_payout

> 谁跑赢:过去一年把现金还给股东(分红、回购注销)而且没有大额增发的公司 —— 多头腿是派现方,不是不派现方。 恒等式 P = log(后复权收盘) − LogTotalCap = log(复权因子) − log(总股本):未复权价在两项里严格相消 (E1 在玩具数据上 float64 核过,最大误差 3.6e-15),所以 P 只在分红、送转、增发、回购注销当天跳变; 送转同时抬高复权因子和总股本,在 P 里抵消(E1 的 E-a:分红股票跳 +0.0303 ≈ +D/r,增发股票跳 −0.1814 ≈ −log1.2, 送转股票不动,只有 1.9e-6 的噪声)。于是 ΔP = 股息率 − 净增发率,即 Daniel–Titman 2006 composite issuance 的相反数。 机制:管理层在股价低估时回购、在高估时增发,市场对这个管理层私有信息反应不足 (Daniel–Ti

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -2.47 | +0.10 | -2.47 | -1.0 | 20.0 | +0.034 | -0.06 | 未过线 | `sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241))` |
| v15 | core | -2.49 | +0.12 | -2.49 | -1.0 | 20.0 | +0.033 | -0.06 | 未过线 | `sub(cross_mean(sub(log(day_last(Close)), LogTotalCap), 5), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241))` |
| v3 | core | -2.75 | -0.09 | -2.75 | -1.0 | 20.0 | +0.029 | -0.04 | 未过线 | `cs_bucket_demean(sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)), LogFloatCap)` |
| v4 | core | -2.52 | -0.17 | -2.52 | -1.0 | 20.0 | +0.033 | -0.07 | 未过线 | `cs_regres(sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)), LimitWidth)` |
| v14 | core | -3.48 | +0.02 | -3.48 | -1.0 | 20.0 | +0.034 | -0.02 | 未过线 | `cs_bucket_demean(sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)), cross_mean(day_std(Ret), 20))` |
| v2 | ablation | -2.27 | +0.13 | -2.27 | -1.0 | 20.0 | +0.032 | -0.07 | 未过线 | `cross_sum(ts_delta(sub(log(day_last(Close)), LogTotalCap), 1), 241)` |
| v5 | ablation | — | — | — | — | — | — | — | 门槛废品 | `neg(sub(sub(LogTotalCap, sub(LogFloatCap, LogFloatShares)), cross_mean(sub(LogTotalCap, sub(LogFloatCap, LogFloatShares)), 241)))` |
| v6 | ablation | -0.85 | -0.85 | +0.23 | -1.0 | 20.0 | +0.053 | +0.00 | 未过线 | `sub(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 241))` |
| v7 | ablation | -0.27 | -0.27 | +0.16 | 1.0 | 20.0 | +0.041 | +0.01 | 未过线 | `sub(sub(log(day_last(Close)), LogFloatCap), cross_mean(sub(log(day_last(Close)), LogFloatCap), 241))` |
| v8 | ablation | — | — | — | — | — | — | — | 门槛废品 | `neg(cross_min(ts_delta(sub(LogTotalCap, sub(LogFloatCap, LogFloatShares)), 1), 241))` |
| v9 | ablation | -3.16 | -0.52 | -3.16 | -1.0 | 20.0 | +0.039 | -0.07 | 未过线 | `sub(sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)), mul(0.1, less(ListAge, 250)))` |
| v10 | ablation | — | — | — | — | — | — | — | 门槛废品 | `sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 60))` |
| v16 | ablation | -3.78 | -0.09 | -3.78 | -1.0 | 20.0 | +0.030 | +0.10 | 未过线 | `cs_bucket_demean(sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)), cross_mean(day_sum(Amt), 30))` |
| v17 | ablation | -3.02 | -0.14 | -3.02 | -1.0 | 20.0 | +0.041 | +0.03 | 未过线 | `cs_regres(sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)), sub(log(day_last(Close)), cross_mean(log(day_last(Close)), 241)))` |
| v11 | control | -0.99 | -0.91 | -0.99 | 1.0 | 20.0 | +0.083 | -0.36 | 未过线 | `sub(log(day_last(Close)), cross_mean(log(day_last(Close)), 241))` |
| v12 | control | -1.36 | -0.85 | -1.36 | 1.0 | 20.0 | +0.080 | -0.36 | 未过线 | `sub(LogTotalCap, cross_mean(LogTotalCap, 241))` |
| v13 | control | -1.11 | -1.11 | -0.94 | -1.0 | 0.0 | +0.036 | +0.47 | 未过线 | `sub(log(cross_mean(day_sum(Volume), 30)), LogFloatShares)` |

## H2_exdiv_clientele

> 谁跑赢:刚刚除息、而且年度派现水平高的股票,窗口是除息后约 2–6 周 —— 多头腿是除息后的回补方。 原料与 H1 相同(P = log(后复权收盘) − LogTotalCap),但读的是 15–30 日的变化而不是一年水平, 所以这张卡检验的是另一件事:派现效应是长期定价(H1),还是除息前后的交易(H2)。 机制:A 股差别化股息税按持股期计征(不足 1 个月 20%、1 个月至 1 年 10%、1 年以上免征), 短线持有者因此有动机在登记日前卖出、除息后买回(税务客户群效应,Elton–Gruber 一脉;先验); 叠加散户的「填权」行为。两者都在除息后形成买压,所以利润落在多头腿。 因为 P 里不含未复权价,cross_delta(P, d) 不是收益,是纯事件量 —— 这既是它的干净处,也是它的门槛风险。

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v3 | core | -2.67 | +0.19 | -2.67 | -1.0 | 20.0 | +0.034 | -0.06 | 未过线 | `add(cross_delta(sub(log(day_last(Close)), LogTotalCap), 15), sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)))` |
| v1 | core | — | — | — | — | — | — | — | 门槛废品 | `cross_delta(sub(log(day_last(Close)), LogTotalCap), 15)` |
| v2 | core | — | — | — | — | — | — | — | 门槛废品 | `cross_delta(sub(log(day_last(Close)), LogTotalCap), 30)` |
| v10 | core | -2.62 | -0.03 | -2.62 | -1.0 | 20.0 | +0.034 | -0.05 | 未过线 | `add(cross_delta(sub(log(day_last(Close)), LogTotalCap), 30), sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)))` |
| v4 | core | -2.59 | +0.16 | -2.59 | -1.0 | 20.0 | +0.034 | -0.06 | 未过线 | `add(sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 30)), sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)))` |
| v5 | ablation | -1.02 | -1.02 | +0.39 | -1.0 | 20.0 | +0.055 | +0.01 | 未过线 | `add(cross_delta(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 15), sub(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), cross_mean(sub(log(day_last(Close)), sub(LogFloatCap, LogFloatShares)), 241)))` |
| v6 | ablation | -2.69 | +0.09 | -2.69 | -1.0 | 20.0 | +0.033 | -0.05 | 未过线 | `add(cross_delta(sub(log(day_last(Close)), LogTotalCap), 60), sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241)))` |
| v7 | ablation | -2.62 | -0.09 | -2.62 | -1.0 | 20.0 | +0.030 | -0.04 | 未过线 | `cs_bucket_demean(add(cross_delta(sub(log(day_last(Close)), LogTotalCap), 15), sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241))), LogFloatCap)` |
| v8 | control | -2.47 | +0.10 | -2.47 | -1.0 | 20.0 | +0.034 | -0.06 | 未过线 | `sub(sub(log(day_last(Close)), LogTotalCap), cross_mean(sub(log(day_last(Close)), LogTotalCap), 241))` |
| v9 | control | — | — | — | — | — | — | — | 门槛废品 | `cross_delta(sub(LogTotalCap, sub(LogFloatCap, LogFloatShares)), 15)` |
| v11 | control | -2.39 | -2.39 | -2.30 | 1.0 | 20.0 | +0.207 | -0.05 | 未过线 | `cross_delta(log(day_last(Close)), 15)` |
| v12 | control | — | — | — | — | — | — | — | 门槛废品 | `cross_delta(sub(log(day_last(Close)), LogTotalCap), 3)` |

## H3_unlock_pressure_reversal

> 谁跑赢:近 60 个交易日内流通股比例明显上升(解禁)、并且这段时间股价已经跌下来的股票 —— 多头腿是「砸完了的解禁股」,不是解禁股本身。恒等式 FR = LogFloatCap − LogTotalCap = log(流通股 / 总股本): 解禁使 FR 上升,定增与股权激励授予使它下降,送转不改变它(E1 的 E-j 实测:解禁股票给出 +log(1/0.6) 并在 60 日窗内保持、 出窗归零;等比例变动的股票 ΔFR 恒为 0)。U60 = ΔFR + |ΔFR| 只留上升部分(×2), E1 的 E-k 实测它把下降一侧(定增)精确截成 0。 核心是 U60 ×(−60 日收益):解禁带来的卖压是非信息性的(锁定期到期、流动性需求), 压力兑现之后价格回补(Shleifer 1986 需求曲线向下;Field–Hanka 2001 解禁日前后的价格压力; Campbell–Gr

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v2 | core | -0.54 | -0.38 | -0.54 | -1.0 | 20.0 | +0.067 | -0.28 | 未过线 | `mul(add(add(cross_delta(sub(LogFloatCap, LogTotalCap), 60), abs_(cross_delta(sub(LogFloatCap, LogTotalCap), 60))), 0.04), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v1 | core | — | — | — | — | — | — | — | 门槛废品 | `mul(add(cross_delta(sub(LogFloatCap, LogTotalCap), 60), abs_(cross_delta(sub(LogFloatCap, LogTotalCap), 60))), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v3 | core | — | — | — | — | — | — | — | 门槛废品 | `mul(add(cross_delta(sub(LogFloatCap, LogTotalCap), 30), abs_(cross_delta(sub(LogFloatCap, LogTotalCap), 30))), neg(log(div(day_last(Close), cross_delay(day_last(Close), 30)))))` |
| v4 | core | +0.08 | +0.08 | +0.35 | -1.0 | 5.0 | +0.078 | -0.21 | 未过线 | `mul(cross_max(ts_delta(sub(LogFloatCap, LogTotalCap), 1), 60), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v5 | ablation | — | — | — | — | — | — | — | 门槛废品 | `cross_delta(sub(LogFloatCap, LogTotalCap), 60)` |
| v6 | ablation | -0.64 | -0.46 | -0.64 | -1.0 | 20.0 | +0.063 | -0.27 | 未过线 | `mul(add(add(cross_delta(LogFloatShares, 60), abs_(cross_delta(LogFloatShares, 60))), 0.04), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v7 | ablation | -0.95 | -0.81 | -0.95 | -1.0 | 20.0 | +0.072 | -0.28 | 未过线 | `mul(add(add(cross_delta(sub(LogTotalCap, sub(LogFloatCap, LogFloatShares)), 60), abs_(cross_delta(sub(LogTotalCap, sub(LogFloatCap, LogFloatShares)), 60))), 0.04), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v8 | ablation | -0.61 | -0.61 | -0.37 | -1.0 | 20.0 | +0.081 | -0.29 | 未过线 | `mul(add(mul(add(cross_delta(sub(LogFloatCap, LogTotalCap), 60), abs_(cross_delta(sub(LogFloatCap, LogTotalCap), 60))), less(ListAge, 10000)), 0.04), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v9 | ablation | -2.52 | +0.26 | -2.52 | -1.0 | 5.0 | +0.037 | -0.01 | 未过线 | `sub(sub(LogFloatCap, LogTotalCap), cross_mean(sub(LogFloatCap, LogTotalCap), 241))` |
| v10 | ablation | -0.76 | -0.36 | -0.76 | -1.0 | 20.0 | +0.060 | -0.25 | 未过线 | `mul(add(mul(2, cross_delta(sub(LogFloatCap, LogTotalCap), 60)), 0.04), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v13 | ablation | -0.59 | -0.59 | +0.07 | -1.0 | 20.0 | +0.088 | -0.21 | 未过线 | `mul(add(add(cross_delta(sub(LogFloatCap, LogTotalCap), 60), abs_(cross_delta(sub(LogFloatCap, LogTotalCap), 60))), 0.04), neg(sub(log(day_last(Close)), cross_mean(log(day_last(Close)), 60))))` |
| v14 | core | -0.73 | -0.20 | -0.73 | -1.0 | 20.0 | +0.066 | -0.27 | 未过线 | `mul(add(add(sub(sub(LogFloatCap, LogTotalCap), cross_mean(sub(LogFloatCap, LogTotalCap), 241)), abs_(sub(sub(LogFloatCap, LogTotalCap), cross_mean(sub(LogFloatCap, LogTotalCap), 241)))), 0.04), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v16 | ablation | -0.48 | -0.48 | -0.48 | -1.0 | 20.0 | +0.059 | -0.27 | 未过线 | `mul(add(add(cross_delta(sub(LogFloatCap, LogTotalCap), 60), abs_(cross_delta(sub(LogFloatCap, LogTotalCap), 60))), 0.01), neg(log(div(day_last(Close), cross_delay(day_last(Close), 60)))))` |
| v11 | control | -0.76 | -0.76 | -0.38 | -1.0 | 20.0 | +0.084 | -0.29 | 未过线 | `neg(log(div(day_last(Close), cross_delay(day_last(Close), 60))))` |
| v12 | control | -0.93 | -0.93 | -0.47 | -1.0 | 20.0 | +0.121 | -0.18 | 未过线 | `neg(log(div(day_last(Close), cross_delay(day_last(Close), 30))))` |
| v15 | control | -0.16 | -0.16 | +1.04 | 1.0 | 0.0 | +0.039 | +0.03 | 未过线 | `sub(LogFloatCap, LogTotalCap)` |

## H4_nominal_price_illusion

> 谁跑赢:同样市值下名义股价高的股票 —— 多头腿是高价股,不是低价股。 恒等式 RP = LogFloatCap − LogFloatShares = log(未复权收盘)(E1 的 E-n 实测它与直接对未复权价取对数的差在 1e-6 量级,是两条 float32 量化路径的差,不是模型误差)。 机制:名义价格幻觉 —— 投资者把低价股当作「便宜」和「有上行空间」,高估它的上行偏度并为此多付钱, 于是低价股的预期收益被压低(Birru–Wang 2016;先验)。股价的名义水平在同等市值下只反映股数这一个会计选择, 按理不该定价,所以它是一个纯粹的行为偏误度量。 为什么它适合纯多头:做多端是高名义价格股,而幸存者偏差抬高的是低价一侧(库里 5207 只股票全部存续到末日、 没有退市股),所以本卡在样本内的证据偏保守 —— 真实效应应当比读数更强,而不是更弱。 名义价格的截面排序是慢变量(

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -2.08 | -0.22 | -2.08 | 1.0 | 0.0 | +0.064 | -0.24 | 未过线 | `cross_mean(sub(LogFloatCap, LogFloatShares), 60)` |
| v2 | core | -0.27 | -0.27 | +0.26 | -1.0 | 5.0 | +0.069 | +0.20 | 未过线 | `cs_bucket_demean(cross_mean(sub(LogFloatCap, LogFloatShares), 60), LogFloatCap)` |
| v3 | core | -2.06 | -0.17 | -2.06 | 1.0 | 20.0 | +0.063 | -0.24 | 未过线 | `cs_regres(cross_mean(sub(LogFloatCap, LogFloatShares), 60), LimitWidth)` |
| v4 | ablation | +0.48 | +0.48 | +0.76 | -1.0 | 20.0 | +0.085 | -0.29 | 未过线 | `neg(LogFloatShares)` |
| v5 | ablation | -0.01 | -0.01 | +0.57 | -1.0 | 20.0 | +0.060 | -0.34 | 未过线 | `neg(sub(LogTotalCap, sub(LogFloatCap, LogFloatShares)))` |
| v6 | ablation | -2.06 | -0.21 | -2.06 | 1.0 | 0.0 | +0.064 | -0.24 | 未过线 | `cross_mean(log(div(day_sum(Amt), day_sum(Volume))), 60)` |
| v7 | ablation | -1.61 | +0.08 | -1.61 | 1.0 | 20.0 | +0.059 | -0.18 | 未过线 | `sub(cs_rank(cross_mean(sub(LogFloatCap, LogFloatShares), 60)), less(ListAge, 250))` |
| v10 | ablation | -2.18 | -0.12 | -2.18 | 1.0 | 20.0 | +0.060 | -0.26 | 未过线 | `cs_bucket_demean(cross_mean(sub(LogFloatCap, LogFloatShares), 60), cross_mean(day_std(Ret), 20))` |
| v11 | ablation | -1.94 | -0.23 | -1.94 | 1.0 | 5.0 | +0.063 | -0.20 | 未过线 | `cross_mean(sub(LogFloatCap, LogFloatShares), 241)` |
| v8 | control | -1.17 | -1.17 | -0.49 | -1.0 | 5.0 | +0.031 | +0.40 | 未过线 | `cross_mean(log(day_last(Close)), 60)` |
| v9 | control | -2.66 | -0.88 | -2.66 | -1.0 | 0.0 | +0.084 | -0.57 | 被相关度拒绝 | `cross_mean(day_zero_ratio(Ret), 30)` |

## H5_frog_in_the_pan

> 谁跑赢:过去一年累计上涨(跳过最近 15 个交易日以避开短期反转)、而且这段上涨是由许多个小幅上涨日连续累积、 不是由少数几个大跳变造成的股票 —— 多头腿是「连续慢涨」的那一端。 机制:注意力有限 —— 单日幅度小的消息不触发投资者的关注与重新定价,信息被逐步而不完全地吸收, 动量因此在「连续型」股票上更强、更持久(Da–Gurun–Warachka 2014 frog-in-the-pan; Hong–Stein 1999 的渐进信息扩散;先验)。反应不足型异象的利润在多头腿(上涨组继续涨), 这正是本轮纯多头口径需要的;长期反转那一族的利润在空头腿,所以不写。 PN 用 sign(日收益) 的一年均值度量上涨日占比:E1 Q2 实测 sign 返回 float32、NaN 输入输出 0, 可以安全喂给 cross_mean;is_gt0 / is_lt0 返回 int32,喂给 cr

| 变体 | 角色 | score | train | valid | 方向 | 半衰期 | 换手 | ρ已知 | 结果 | 表达式 |
|---|---|---|---|---|---|---|---|---|---|---|
| v1 | core | -1.31 | -1.31 | -0.85 | 1.0 | 20.0 | +0.057 | -0.26 | 未过线 | `add(cs_rank(sub(cross_sum(ts_delta(log(day_last(Close)), 1), 241), cross_sum(ts_delta(log(day_last(Close)), 1), 15))), cs_rank(cross_mean(sign(ts_delta(log(day_last(Close)), 1)), 241)))` |
| v2 | core | -1.62 | -1.62 | +0.05 | 1.0 | 20.0 | +0.050 | -0.31 | 未过线 | `add(cs_rank(sub(cross_sum(ts_delta(log(day_last(Close)), 1), 241), cross_sum(ts_delta(log(day_last(Close)), 1), 15))), cs_rank(mul(sign(sub(cross_sum(ts_delta(log(day_last(Close)), 1), 241), cross_sum(ts_delta(log(day_last(Close)), 1), 15))), cross_mean(sign(ts_delta(log(day_last(Close)), 1)), 241))))` |
| v3 | core | -1.03 | -0.60 | -1.03 | 1.0 | 20.0 | +0.067 | -0.21 | 未过线 | `add(cs_rank(sub(cross_sum(ts_delta(log(day_last(Close)), 1), 60), cross_sum(ts_delta(log(day_last(Close)), 1), 15))), cs_rank(cross_mean(sign(ts_delta(log(day_last(Close)), 1)), 60)))` |
| v4 | ablation | -2.83 | -1.19 | -2.83 | -1.0 | 20.0 | +0.045 | +0.37 | 未过线 | `sub(cross_sum(ts_delta(log(day_last(Close)), 1), 241), cross_sum(ts_delta(log(day_last(Close)), 1), 15))` |
| v5 | ablation | -1.59 | -1.23 | -1.59 | 1.0 | 20.0 | +0.055 | -0.11 | 未过线 | `cross_decay_linear(sign(ts_delta(log(day_last(Close)), 1)), 241)` |
| v7 | ablation | -2.42 | -0.74 | -2.42 | 1.0 | 20.0 | +0.073 | -0.36 | 未过线 | `sub(cross_delay(log(day_last(Close)), 15), cross_mean(log(day_last(Close)), 241))` |
| v6 | control | -0.76 | -0.76 | -0.38 | -1.0 | 20.0 | +0.084 | -0.29 | 未过线 | `neg(log(div(day_last(Close), cross_delay(day_last(Close), 60))))` |
| v8 | control | -0.80 | -0.80 | -0.78 | 1.0 | 5.0 | +0.064 | -0.39 | 未过线 | `div(sub(cross_sum(ts_delta(log(day_last(Close)), 1), 241), cross_sum(ts_delta(log(day_last(Close)), 1), 15)), add(cross_stddev(ts_delta(log(day_last(Close)), 1), 241), 0.002))` |

