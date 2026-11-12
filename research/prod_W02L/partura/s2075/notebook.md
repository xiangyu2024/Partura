
## 第 1 轮

信念:本批 3 个 head 分数全为负(-0.53 / -1.12 / -1.46),没有一个过尺子,alpha 来源不明;唯一的线索是 day_last(Close) 与 day_sum(Volume) 的共性(均值差 +0.56 / +0.27,p 不显著)和 "收盘中点 vs 当日 VWAP 的符号 x 成交量" 的 5 日累计子树(sufficiency -1.49,比整个 head -0.53 之外的子树都不差)。第一个 head 的 abs_ 把方向丢了,我认为方向性资金流才是可能的来源。

预测:
- E(核心 = 符号 x 成交量的 5 日累计):外围换成自身历史归一化。预测小概率(约 20%)产出 score>=0.5 的 head;最可能是 ts_rank / cross_zscore 型,理由是去掉了水平暴露。更可能的结局是和市值 / 流动性控制过近而被尺子压成负分。
- N(量加权 vs 等权分钟收益之差、topw 均值):预测约 25% 产出 head;若有,多半是 day_wmean(Ret, Volume) 减 day_mean(Ret) 的慢平滑版本。
- R:cross_autocorr_s1 把窗口放到 482,预计只拿到 +0.2 左右,不会跨过 0.5。
上一轮:无(第 1 轮)。

## 第 2 轮

信念:6 个 head 全负(最好 -0.12),没有可信的 alpha 来源。唯一接近 0 的是 M2 的 cross_max(mul(pow_3(ts_std(day_close(Amt),50)), ts_min(...)),5):拆解里 cross_max 窗口 5->10 得 +0.00 / valid +0.05,单独 pow_3(ts_std(day_close(Amt),50)) 为 -0.52,所以我认为线索是「收盘分钟成交额的波动」(尾盘成交的不稳定性),外层取极值是噪声。Ret 的高阶矩 / 量价协方差类(第 1 批)全在 -0.8 以下,几乎是死的。第 1 轮 N 的最好 -0.44(量加权减等权收益的平滑),方向对但被控制吃掉。
预测:
- E(核心=整个 head 的内层 mul):外围换成 cross_ema / ts_decay_linear / cross_zscore 等。预测约 25% 出 score>=0.5 的 head,若有应是平滑版或 cs_rank 后平滑版;失败的主因是与 Amt 流动性控制仍过近。
- N(尾盘成交强度 CI 的波动 / 偏度 / 份额差):预测约 20% 出 head;最可能的是 ts_std(CI,50) 平滑版或末 10 分钟占比的波动。失败风险:被流动性 / 波动控制残差化后无剩余。
- R(skew/kurt head 的变体):预计无一个超过 +0.1。
上一轮预测核对:E(符号x成交量核心)预计 20%,实际 46 评估 0 过线(最好 -2.31),错;N 预计 25%,实际 0 过线(最好 -0.44,方向对但不够),错;R 预计 +0.2,实际 482 窗口 -0.86 vs -1.12,即 +0.26,对。

## 第 3 轮

信念:前两轮 heads 全负,没有可信的 alpha 来源。唯一接近线的是 Pr2a 的 cross_reg_fvalue(day_last(in_top_quantile_flag_q10(Ret)), sub(mul(day_at_min_ratio(Low), BoardCode), ...), 241)(+0.31,valid +0.48),两个富集子树都和「价格触及当日极值 / 收盘冲高」这类涨跌停机制有关,而不是 Ret 的矩或量价协方差。我的信念:本种子的可能来源是涨跌停 / 尾盘极值事件的累积频率(制度性),而非连续收益统计量。量加权减等权收益(Pr1b,-0.44)方向对但被控制吃掉。
预测:
- E(核心 = day_last(in_top_quantile_flag_q10(Ret))):外围换成时间序列频率、与 ListAge / LimitWidth 相乘、与均收益的 ts_corr。预测约 25% 出 score>=0.5 的 head;若有应是 ts_mean/cross_ema 的 60~120 日频率版或带 LimitWidth 的版本。主要失败风险:旗标稀疏,排序信息少,被已知族 / 市值控制吃掉。
- N(封涨停减封跌停的分钟占比):预测约 20% 出 head;若有多半是 cross_ema(sub(at_max_ratio(High), at_min_ratio(Low)), 20~30) 或乘 LimitWidth 的版本。失败风险:与 head 里 day_at_min_ratio 族过近被库禁令拒绝,或在 valid 上不稳。
- R(skew/kurt head 更长窗口):预计无一个超 +0.1(上轮 60 与 120 都 -0.51)。
上一轮预测核对:R 预测无增益,实际三个变体里 60 窗口 -0.51 vs 原 -0.88,有 +0.37(替换生效),预测错;E 位审计未过、降为普通 GP;N(尾盘成交强度)预计 20%,实际 99 评估 0 过线(最好 +0.31 属于 Pr2a 而非该 N;N 为 Pr2b 最好 -0.39),预测对(没出 head)。
