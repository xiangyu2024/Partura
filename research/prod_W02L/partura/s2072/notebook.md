
## 第 1 轮

信念:本批 3 个 head 全亏(-0.8 ~ -1.45),但 ts_hurst(...) 子树单独的 sufficiency 分数(-0.78/-0.78/-1.25)比整个 head 好,而外面的 log(add(day_last(Volume), day_std(Vwap))) 水平乘子与 ts_mean@50 是拖累(knockout 必要性为正、水平子树 -1.6)。所以 alpha 来源的候选在"序列持续性(Hurst)",不在水平。

预测:
- E 位(核心 ts_hurst(day_last(Volume), 20),外围换成 cross_zscore / 桶内标准化 / 与收益 Hurst 之差 / 回归残差):预测大概率仍不出 head(约 25% 出),出的话最可能是桶内标准化或"量 Hurst 减价 Hurst"一类;因为单独的 Hurst 子树仍为负,~-0.8 离 0.5 差得远。
- N 位(成交量分钟曲线的重心 / 集中度):不确定,出 head 概率约 20%;最可能的是 cross_mean(day_gini(Volume), 60) 一带的慢聚合,但担心被成交额族吃掉。
- 上一轮:无(第 1 轮)。

## 第 2 轮

信念:第 1 轮 E(Hurst)与 N(重心/集中度)都没出 head(最好 -0.20,来自 N 位 GP 自己长的 cross_regbeta(div(pow_05(day_quantile_q25(Low)),-1),...)),说明 Hurst 与量形状都不是来源;本批真正有富集的是价位 day_quantile_q25(Low)(+0.79,p 0.001)与 pow_3(LimitWidth)(+0.64)。信念:alpha 候选在"价位/板块结构"这一块,而不是成交量序列。
预测:
- E 位(核心 day_quantile_q25(Low),外围:zscore / 比值去价位 / 桶内标准化 / 残差 / Hurst / 下尾均值):约 30% 出 head(valid 方向已为正,-0.20/+0.32 是已见最好),最可能是桶内标准化或"下沿 / 均价"比值;主要风险是与市值、反转控制共线被去掉。
- N 位(tick 摩擦 / 价格黏性 day_flat_ratio):约 15% 出 head;若出,最可能是同板块内标准化后的 cross_mean(day_flat_ratio(Vwap),60);担心被流动性/价位控制吃掉。
- 上一轮预测核对:E 预测约 25% 出 head,实际 0 个、最好 -0.58,方向对(低概率);N 预测 20%,实际 0 个,最好 -0.20(其实是 Nb 里 GP 自己长出的价位类,不是我的重心种子),说明我预测的"慢聚合重心/集中度"没成,有信息的反而是价位。
