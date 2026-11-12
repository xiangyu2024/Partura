
## 第 1 轮
信念:本批三个 head 全是负分(-1.1~-1.3),train/valid 同号稳定亏,推断毛超额约为 0、亏在换手;富集信号只有 day_q_stat_std(Volume)(+1.05,p 0.018)与 day_max(High)。alpha 来源猜测:分钟成交量的序列结构(执行方式聚集度),被 head 的 ts_quantile/ts_kurt 外围弄成高换手噪声。
预测:E(核心 day_q_stat_std(Volume),换成个股自比 / 与价格的长窗口滚动关系外围)——约 35% 概率出 1-2 个 head,大概率是 cross_corr/regbeta 型长窗口;N(Ret 与 Volume 的 ar1 滚动协动)——约 20% 出 head,易被流动性/波动控制吃掉或估计太吵。
上一轮:无。
