
## 第 1 轮

信念:本批 3 个 head 全亏(-0.8 ~ -1.45),但 ts_hurst(...) 子树单独的 sufficiency 分数(-0.78/-0.78/-1.25)比整个 head 好,而外面的 log(add(day_last(Volume), day_std(Vwap))) 水平乘子与 ts_mean@50 是拖累(knockout 必要性为正、水平子树 -1.6)。所以 alpha 来源的候选在"序列持续性(Hurst)",不在水平。

预测:
- E 位(核心 ts_hurst(day_last(Volume), 20),外围换成 cross_zscore / 桶内标准化 / 与收益 Hurst 之差 / 回归残差):预测大概率仍不出 head(约 25% 出),出的话最可能是桶内标准化或"量 Hurst 减价 Hurst"一类;因为单独的 Hurst 子树仍为负,~-0.8 离 0.5 差得远。
- N 位(成交量分钟曲线的重心 / 集中度):不确定,出 head 概率约 20%;最可能的是 cross_mean(day_gini(Volume), 60) 一带的慢聚合,但担心被成交额族吃掉。
- 上一轮:无(第 1 轮)。
