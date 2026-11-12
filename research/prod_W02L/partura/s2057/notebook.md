
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

## 第 3 轮

信念:本种子唯一的苗头仍是 day_zero_ratio(Ret) 的多层 ts_stddev(r1 四层 train +0.32 / valid +0.80;r2 的 E 外围 cs_first_low40(LogFloatCap) 也只到 +0.20/+0.69)。train 弱、valid 强,我怀疑是板块结构(涨跌停幅度 10%/20%、新上市)抬高了截面上的冻结基线,所以本轮改成「板块/上市时长/市值十分位内中性化」。

任务位:
- 位 1 E(核心 ts_stddev^3(day_zero_ratio(Ret)) 即 ts_stddev(ts_stddev(ts_stddev(.,10),50),10)):外围用 cs_bucket_demean/rank(LimitWidth、BoardCode、ListAge、LogTotalCap)、robust z、ts_rank、与真实波动的波动之波动相减。预测:有 25% 机会出 1 个 head,最可能赢的是 LimitWidth 内中性化版本(去掉板块基线后 train 抬升);若 LimitWidth 十分位因取值很少而并列,效果可能退化为无作用(风险)。
- 位 2 N(锁价几何:day_flat_run_max(Close)、day_at_max_ratio-day_at_min_ratio、day_distinct_ratio 的水平与波动):预测 0 个 head 为主(75%);最大的机会是 flat_run_max 的嵌套波动(与 zero_ratio 同构);带符号的涨停-跌停差可能因被动量/反转控制吸收而无效。
- R:ts_quantile_q75(pow_2(day_q_stat_std(pow_2(Ret))), w) 窗口 8–20。预测会少亏但仍 <0(分数 -2 左右),只是替换式小改善,不会成为 head 过线。

上一轮预测对错:r2 预测 E 有 0–1 个 train 0.3–0.5,实际最好 train +0.20,0 个 head;预测「减去 vol-of-vol 或除水平」最可能赢,实际最好的是 cs_first_low40 嵌套(+0.20 / valid +0.69),我没想到按市值字典序排的写法最有效。N 预测 0 个 head,对(最好 -0.97)。
