
## 第 1 轮

信念:本批 3 个 head 全是 nt_cs_quantile_q25(Amt) 的嵌套 ts_stddev,分数 -1.35 ~ -1.62(远低于 0.5),拆解里换 Volume、拉长外层窗口只是少亏;这个核心带 nt_*,E 位的种子无法使用,所以本轮没有 E、没有 R(变体都含 nt_*)。可借用的只有「成交的分布 / 稀薄程度的二阶矩」这个形状。

任务位(都是 N)与事先预测:
- 位 1:日内成交额分布的集中度与时点(day_gini / day_centroid of Amt/Volume)的日间波动与水平。预测:大概率拿不到 >= 0.5(多数与流动性控制相关,残差后留不下);有一点机会来自 centroid 波动(人群结构)。
- 位 2:死分钟占比(day_zero_ratio(Ret) / day_flat_ratio(Close))的水平与波动。预测:水平项与流动性/市值太像,可能被残差掉;波动项偶有机会。整体预期 0–1 个 head。
上一轮:无。

## 第 2 轮

信念:本种子 alpha 的唯一苗头是「盘中死分钟占比 day_zero_ratio(Ret) 的多层 ts_stddev」(第 1 轮 Pr1b 最好 train +0.32 / valid +0.80,过线 0 个);centroid 族只有 +0.13。Q25(Amt) 嵌套 head 带 nt_*,不可用,M2 的 head 为价格路径结构,分数 -2 左右,无参考价值。问题在 train 段偏弱而 valid 强,疑似 regime/流动性残余。
任务位:
- 位 1 E(核心 ts_stddev(ts_stddev(day_zero_ratio(Ret),10),50)):外围换成水平归一、减长期均值、与趋势符号 / 真实波动的波动之波动相减、与 centroid 波动相加或相除、ts_rank/ts_corr。预测:大概率仍有 0–1 个 train 能到 0.3-0.5 的候选,过 0.5 的机会约 25%;最可能的赢家是「减去真实 vol-of-vol」或「除以水平」,因为它们去掉流动性/波动残余使 train 段抬升。
- 位 2 N(价格钉住交易:day_zero_ratio(Ret)-day_zero_ratio(Amt),按上午/下午/尾盘切分):预测 0 个 head 为主(70%),差值水平项会部分被流动性残差掉;不对称与尾盘项若有则来自收盘博弈,机会小。
上一轮预测对错:预测整体 0–1 个 head,实际 0 个,方向正确;预测「centroid 波动有机会」错了(+0.13);zero_ratio 波动之波动反而是最好的(+0.32),我当时只预期偶有机会,低估了它。
