
## 第 1 轮
信念:本批三个 head 全是负分(-1.1~-1.3),train/valid 同号稳定亏,推断毛超额约为 0、亏在换手;富集信号只有 day_q_stat_std(Volume)(+1.05,p 0.018)与 day_max(High)。alpha 来源猜测:分钟成交量的序列结构(执行方式聚集度),被 head 的 ts_quantile/ts_kurt 外围弄成高换手噪声。
预测:E(核心 day_q_stat_std(Volume),换成个股自比 / 与价格的长窗口滚动关系外围)——约 35% 概率出 1-2 个 head,大概率是 cross_corr/regbeta 型长窗口;N(Ret 与 Volume 的 ar1 滚动协动)——约 20% 出 head,易被流动性/波动控制吃掉或估计太吵。
上一轮:无。

## 第 2 轮
信念:第 1 轮 E(核心 day_q_stat_std(Volume),换成个股自比/滚动相关外围)最好仅 -0.88,N(ar1 协动)也只到 -0.13,没有 head;本批 6 个 head 全负。仍然相信的线索:day_mean(Volume) 子树富集 +1.18(p 0.002)、head1 的 valid 在 ts_std 窗口 25 转正(+0.56)。alpha 来源可能是量价同向协动的慢变量与上行尾部方差的长窗口波动,但没有证据支持任何一个。
本轮预测:E(核心 ts_cov(cs_normalize(day_mean(Volume)), day_close(High), 50),外围换成滚动相关/自比/平滑)——约 25% 出 head,若出则是 cross_zscore/ema 平滑型,风险是 day_close(High) 价格水平被市值/流动性控制吃掉;N(day_signed_ratio × day_centroid:买压与成交时间重心)——约 20% 出 head,最大风险是与 20 日反转控制相关;R(head1 外层窗口缩短/去 ts_sum)——约 30% 有 1 个变体比原 head 高 0.1 以上并替换,但达不到 0.5 过线。
上一轮预测:E 预计 35% 出 head,实际 0;N 预计 20%,实际 0。预测偏乐观,核心 day_q_stat_std(Volume) 整体评分在 -1 左右,外围换写法没有救回来,说明它本身不是 alpha 来源。
