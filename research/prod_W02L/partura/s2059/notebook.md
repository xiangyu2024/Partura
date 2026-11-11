
## 第 1 轮

信念:本批 3 个 head 全是 nt_cs_regres(High|Ret, Low) 的日内最大值再 cross_min,score -1.9 ~ -2.4(两段同号为负),说明这一条线毛 alpha 近 0;唯一的正信号是窗口越长越好(60->120 增益 +0.85),即慢变属性。核心含被禁的 nt_*,E 位不可行(种子不得含 nt_),所以两个位都做 N。
事先预测:
- N1(日度 High/Low 截面回归残差、上下影线不对称、慢聚合):大概率与波动控制近重复,多数种子被残差去掉;可能出 head 的是影线不对称的 log 比(尺度无关)。出 head 概率约 25%。
- N2(上下尾不对称、半标准差比):尺度无关,与控制低相关;可能出 head 的是 day_skew 或半方差比的慢聚合版;概率约 25%。符号由 GP 方向决定。
上一轮预测:无(第 1 轮)。

## 第 2 轮

信念:本流 alpha 来源很弱。r1 两个 N 位 171 次评估零过线,最好 -0.43(cross_regbeta(day_max(Open), day_es_ratio_lo(Open), 60));批里的 head 全是被禁 nt_cs_regres 的日内极值,毛收益近 0。唯一的线索是 day_es_ratio_lo(Open)(价格低价端厚度,共性表富集 +0.84,p 0.009)和 ts_skew(pow_2_5(day_wmean(Vwap,Volume)),40)(r1 Nb 内含,-1.23 但两段同号偏负)。R:唯一的改善变体含 nt_,不可用,本轮不做 R。
事先预测:
- E(核心 day_es_ratio_lo(Open),外围换成 stddev / 分位尾 / 与收益成交的 corr / 上下对称):出 head 概率约 20%,若出,多半是 cross_corr 或 cross_stddev 一类读「下探与成交的耦合」;大概率仍卡在 -0.3 ~ -0.6。
- N(成交量加权的大单方向 day_topw_mean / day_signed_ratio / day_centroid):与 20 日反转 / 流动性控制可能中度相关,出 head 概率约 20%,若出,最可能是 day_signed_ratio(Ret, Amt) 的慢聚合(反转方向)。
上一轮预测对不对:r1 预测两位各约 25% 出 head,结果 0 / 0,方向对一半(Na 的区间类确实被波动吃掉,最好仅 -0.43;Nb 的尾部不对称与控制低相关但分数仍 -1.2,没有毛 alpha);三个 semistd 种子被划掉是我没核实算子定义,本轮已查过算子源码再写。
