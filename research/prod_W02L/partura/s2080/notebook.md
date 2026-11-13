
## 第 1 轮
信念:本批三个 head 全是负分(-1.1~-1.3),train/valid 同号稳定亏,推断毛超额约为 0、亏在换手;富集信号只有 day_q_stat_std(Volume)(+1.05,p 0.018)与 day_max(High)。alpha 来源猜测:分钟成交量的序列结构(执行方式聚集度),被 head 的 ts_quantile/ts_kurt 外围弄成高换手噪声。
预测:E(核心 day_q_stat_std(Volume),换成个股自比 / 与价格的长窗口滚动关系外围)——约 35% 概率出 1-2 个 head,大概率是 cross_corr/regbeta 型长窗口;N(Ret 与 Volume 的 ar1 滚动协动)——约 20% 出 head,易被流动性/波动控制吃掉或估计太吵。
上一轮:无。

## 第 2 轮
信念:第 1 轮 E(核心 day_q_stat_std(Volume),换成个股自比/滚动相关外围)最好仅 -0.88,N(ar1 协动)也只到 -0.13,没有 head;本批 6 个 head 全负。仍然相信的线索:day_mean(Volume) 子树富集 +1.18(p 0.002)、head1 的 valid 在 ts_std 窗口 25 转正(+0.56)。alpha 来源可能是量价同向协动的慢变量与上行尾部方差的长窗口波动,但没有证据支持任何一个。
本轮预测:E(核心 ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50),外围换成滚动相关/自比/平滑)——约 25% 出 head,若出则是 cross_zscore/ema 平滑型,风险是 day_close(High) 价格水平被市值/流动性控制吃掉;N(day_signed_ratio × day_centroid:买压与成交时间重心)——约 20% 出 head,最大风险是与 20 日反转控制相关;R(head1 外层窗口缩短/去 ts_sum)——约 30% 有 1 个变体比原 head 高 0.1 以上并替换,但达不到 0.5 过线。
上一轮预测:E 预计 35% 出 head,实际 0;N 预计 20%,实际 0。预测偏乐观,核心 day_q_stat_std(Volume) 整体评分在 -1 左右,外围换写法没有救回来,说明它本身不是 alpha 来源。

## 第 3 轮
信念:前两轮 4 个 GP 位最好 -0.13,R 最好 -0.37(valid +0.56);没有任何 head 过线。本批 9 个 head 全是负分,仅 ts_std(上行 6.25 次幂方差的 241 日和, 25) 的 valid 为正。alpha 来源仍无证据;弱线索:(1) 订单流持续性 cross_regbeta(day_q_stat_std(Volume), day_ar1_coefficient(Ret), 40) 富集 +1.09(p 0.002);(2) 静态股数 cs_robust_z(LogFloatShares) 富集 +0.89(p 0.000,20 个候选),控制只含市值,名义价格未被控制;(3) 上行尾部方差的波动。
本轮计划:E(核心 C1 = 上述 cross_regbeta,外围改为对 C1 序列的二阶读法:ts_std / 减自己均值 / ts_rank / 极差)——约 15% 出 head,若出则是 ts_std 型或自比型;最大风险是回归斜率太吵、与波动控制相关。N(名义价格 = LogFloatCap - LogFloatShares,及市值桶内排名、与彩票需求的相互作用)——约 25% 出 head,是本流第一个用日频字段的位,换手近零,风险是被市值非线性控制与已知族吃掉或仙股风险。R(把 head1 的 pow_2_5 换保号 signedpower、缩 241 窗口、改 ts_mean)——约 25% 有变体比 -0.37 高 0.1 并替换,仍不会过 0.5 线。因只许 2 个 GP 位,放弃了「上行 vs 下行尾部不对称」的 E(核心 cross_sum(ts_sum(day_var(pow_2_5(pow_2_5(Ret))),10),241)),留给以后。
上一轮预测:E 预计 25% 出 head 实际 0(最好 -2.68,核心外围被 GP 随机树淹没);N 预计 20% 实际 0(最好 -0.69,valid 为正 +0.32 但 train 差);R 预计 30% 有替换,实际 1 个替换(-0.62 到 -0.37),但没过线。预测方向大致对,对 N 的 train/valid 不一致没预见。
