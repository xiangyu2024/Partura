import yaml
C="day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230))))"
CA="day_q_stat_std(div(in_slice(Amt, 11, 230), in_sum(in_slice(Amt, 11, 230))))"
CR="day_q_stat_std(in_slice(Ret, 11, 230))"
Es=[f"cross_ema({C}, 40)", f"cross_zscore({C}, 120)", f"cs_bucket_zscore(cross_ema({C}, 20), LogFloatCap)",
f"sub(cross_mean({C}, 10), cross_mean({C}, 60))", f"div(cross_stddev({C}, 60), cross_mean({C}, 60))",
f"cross_corr({C}, cs_mean({C}), 60)", f"cs_bucket_zscore(cross_zscore({C}, 60), ListAge)",
f"sub(cs_rank(cross_ema({C}, 40)), cs_rank(cross_ema({CA}, 40)))", f"cross_tail_mean_q75({C}, 60)",
f"cross_decay_linear({C}, 30)", f"cross_ema(cross_zscore({C}, 60), 20)", f"cs_bucket_zscore(cross_tail_mean_q25({C}, 60), LogFloatShares)",
f"cross_ema(cs_bucket_zscore({C}, LogFloatCap), 30)", f"div({C}, cross_mean({C}, 60))",
f"cross_corr({C}, {CR}, 60)", f"cross_argmax({C}, 60)"]
N=["cross_ema(day_topw_mean(Ret, Volume), 20)","cross_ema(day_topw_mean(Ret, Amt), 40)",
"cross_ema(sub(day_topw_mean(Ret, Volume), day_mean(Ret)), 20)","cross_ema(day_signed_ratio(Ret, Volume), 20)",
"cross_ema(sub(day_wmean(Ret, Volume), day_mean(Ret)), 30)","cs_bucket_zscore(cross_ema(day_topw_mean(Ret, Volume), 20), LogFloatCap)",
"cross_zscore(day_topw_mean(Ret, Volume), 60)","cross_ema(day_corr(in_index(Volume), Volume), 20)",
"cross_ema(day_centroid(Volume), 40)","cs_bucket_zscore(cross_ema(day_centroid(Amt), 30), ListAge)",
"cross_ema(day_gini(Volume), 30)","sub(cross_ema(day_topw_mean(Ret, Volume), 10), cross_ema(day_topw_mean(Ret, Volume), 60))",
"cross_ema(day_corr(in_index(Volume), Ret), 40)","cross_mean(day_topw_mean(in_slice(Ret, 11, 230), in_slice(Volume, 11, 230)), 20)",
"cross_ema(day_wstd(Ret, Volume), 20)","cs_bucket_zscore(cross_ema(day_signed_ratio(Ret, Volume), 20), LogFloatShares)"]
H1=f"ts_stddev({C}, 15)"
H2=f"add(ts_stddev({CR}, 15), ts_stddev({C}, 15))"
H1="ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15)"
H2="add(ts_stddev(day_q_stat_std(in_slice(Ret, 11, 230)), 15), ts_stddev(day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))), 15))"
R=[{"head":H1,"why":"拆解表:窗口 7 / 15 / 30 的 ts_stddev 分别是 -2.95 / -1.78 / -1.41(valid -2.66 / -1.33 / -0.85),越长越好,说明 15 日窗口对「分钟成交量份额的 Ljung-Box 节律」的波动估计仍然太噪、换手把成本吃掉;变体把窗口继续拉长到 45 / 60 并加 EMA 平滑,并换成变异系数(去掉水平)。分母 cross_mean 为日度量的均值,不近零(Q 统计量非负且有下限),无爆点。",
"variants":[f"ts_stddev({C}, 45)",f"ts_stddev({C}, 60)",f"cross_ema(ts_stddev({C}, 30), 20)",f"div(ts_stddev({C}, 30), cross_mean({C}, 30))",f"cs_bucket_zscore(ts_stddev({C}, 45), LogFloatCap)"]},
{"head":H2,"why":"拆解:Ret 一支单独(sufficiency)是 -1.34(train -1.34 / valid -0.79),比整个和式 -1.79 好 0.45;去掉 Ret 支只变 0.03,说明和式里 Ret 支没有被用上,是 Volume 支(去掉退到 -3.08)在主导并把更好的一支拖差。变体只留 Ret 支并把窗口拉长 / 加 EMA(窗口越长越好的趋势与 Volume 支一致)。无分母;窗口内常数时 ts_stddev 为 0,不爆。",
"variants":[f"ts_stddev({CR}, 30)",f"ts_stddev({CR}, 60)",f"cross_ema(ts_stddev({CR}, 30), 20)",f"cs_bucket_zscore(ts_stddev({CR}, 30), LogFloatCap)",f"cross_ema(ts_stddev({CR}, 15), 40)"]}]
hyp_e="""批里的现象(M2 批,8 个成员里 3 个 head):同一个骨架 ts_stddev(day_q_stat_std(份额序列), 15),份额序列是 in_slice(Volume 或 Amt, 11, 230) 除以其日内总和。核心 C = day_q_stat_std(div(in_slice(Volume, 11, 230), in_sum(in_slice(Volume, 11, 230)))):day_q_stat_std 是 Ljung-Box Q 统计量(各滞后阶的累计自相关)的标准差,作用在日内每分钟成交量占全天比例的序列上,读的是「当天成交量在分钟之间的节律 / 持续性有多强」(成交量被少数连续放量的时段主导,还是均匀散布)。C 单独只有 -3.43(train -3.43 / valid -2.96),而外面包一层 ts_stddev 后 -1.78(15 日)、-1.41(30 日)、-2.95(7 日),窗口越长越好:说明 alpha 若存在,存在于 C 的「慢变分布」,而 15 日窗口的波动率估计太噪,换手吃掉了成本(valid 还比 train 好,不像过拟合)。拆解里 Volume 换 Amt 几乎不变(-1.81),说明价格尺度不是关键,是份额节律本身。
本位要试的外围与批里的 ts_stddev 完全不同:不再取「节律的波动」,改成取「节律的水平 / 偏离自己常态的程度 / 与市场节律的同步度」,每个都配长窗口平滑。(1) cross_ema / cross_decay_linear / cross_mean 长半衰期读水平:机构拆单(算法单 TWAP/VWAP 切片)使一只股票的成交量节律持续、可预测,散户主导的股票节律零散,这是慢变的股票属性;(2) cross_zscore / 短减长 / 除以自己 60 日均值读「今天的节律相对自己平时是否异常」(异常放量簇 = 信息事件,Gervais-Kaniel-Mingelgrin 2001 的高成交量溢价);(3) cross_corr(C, cs_mean(C), 60) 读个股节律与全市场节律的同步度(Chordia-Roll-Subrahmanyam 2000 的成交活动共性);(4) cs_bucket_zscore 在市值 / 上市年限 / 流通股本十分位内标准化,去掉节律与规模的任意形状关系(新尺子只去线性 / 平方 / 立方的排名暴露);(5) 对 Amt 版做差 sub(cs_rank(Volume 节律), cs_rank(Amt 节律)) 提取只由价格水平变动带来的那一部分;(6) 与 Ret 的节律做 60 日相关:成交量与收益的节律是否耦合(信息驱动的成交 vs 流动性驱动的成交)。
为什么和库里已有的不同:库里 4206 条挖掘 + 1392 条手写的骨架里没有「对 day_q_stat_std 做 cross_ema / cross_zscore / cross_corr 对 cs_mean / cs_bucket_zscore」的写法;这一批的三个 head 和本流上一轮的外围都是 ts_stddev 一族(波动的波动),本位刻意不用 ts_stddev 作外层(只在变异系数种子里 cross_stddev 做分子,且被均值除掉,是比值而不是波动水平)。预计与三个 head 的日度秩相关 0.3–0.6(都含 C,但 ts_stddev 的 15 日噪声版和 40 日 EMA 水平差别大),低于 0.7 的禁令线;与 5 个控制:C 与流动性有关(小票节律更零散),但只有线性/U/S 形暴露被去掉,非线性残留由 bucket 种子检验。
为什么样本外还会在:来源是「算法执行 / 机构参与度」这类持续的股票属性(月度自相关高),不依赖于某段行情;40 日半衰期的 EMA 使名次几周内几乎不动,15 bp 成本不致吃光。可证伪:若水平类种子仍然都在 -1 以下,而 ts_stddev 版在 30 日窗口接近 -1.4,说明有用的是「变动」而不是「水平」,那就该转向更长窗口的波动。
数学检查:无前视(全部只用 t 日及以前);份额的分母 in_sum 在全天停牌时为 0,此时分子也为 0 得 NaN(日值缺失,不是爆点);Q 统计量在份额序列全相等时为 0 或有限值;cross_zscore 自带近常数窗口保护;cross_corr 在窗口内常数时得 0;窗口最长 120 日,scorer 有 lead-in 预热;无 ts_spearman / nt_*。"""
hyp_n="""机制:放量分钟的收益里有信息还是只有流动性冲击(Llorente-Michaely-Saar-Wang 2002:带信息的放量使收益延续,对冲 / 投机性放量使收益反转;Gervais 等 2001:异常放量有价格溢价)。我们有分钟数据,可以在一个节点里取出「当天成交量最大的 10% 分钟里的平均收益」day_topw_mean(Ret, Volume)(一个不用触发掩码的事件研究),再用 cross_ema 得到 20–40 日的慢变股票属性:持续地在放量时涨的股票 = 放量里带信息 / 有主动买盘的股票;持续地在放量时跌 = 被抛压 / 被砸盘。day_signed_ratio(Ret, Volume)(上涨分钟成交量占比减下跌分钟成交量占比)、sub(day_wmean(Ret, Volume), day_mean(Ret))(按成交量加权的收益减等权收益,即「收益发生在成交量重的地方还是轻的地方」)是同一机制的不同读法。第二组读法是成交量的日内「时点」:day_centroid(Volume / Amt)、day_corr(in_index(Volume), Volume)(in_index 是分钟在日内的位置,于是这是「放量是否在尾盘」;尾盘放量 = 机构调仓 / 基金申赎 / 盘尾拉抬),day_gini(Volume)(成交量集中度)。
为什么库里没有:这些算子(day_topw_mean、day_signed_ratio、day_wmean、day_centroid、in_index、day_gini、day_wstd、cross_ema)是 ops_ext 里后加的,库的 5583 条(用的是旧算子集)里一条也没有出现,我用 grep 逐个核对过;同时它们也不是本批 M1/M2(ts_pearson 的共动度、day_q_stat_std 的节律、day_last(Volume) 的尾盘占比)的任何一种写法 —— 与批里 head 比,头一个 head 用「最后一分钟成交量占比」做尾盘代理(-3.42),这里的 day_centroid / day_corr(in_index, Volume) 用的是整条日内曲线的重心,不被最后一根棒的偶然性支配。
启发来源:M1 批里 div(cross_mean(day_last(Volume), 40), cross_mean(day_sum(Volume), 40)) 的方向是 -1 且 train -2.86,而 day_close(Amt) 是共性表里均值差 +1.15(p<0.001)的子树,说明尾盘 / 收盘成交是这批里最「有东西」的度量;而它们的写法都是单点(最后一分钟),噪声大、换手大。本位把「尾盘 / 放量」改成整条日内曲线上的统计量并做 EMA 平滑。
算子怎么实现:全部先在日内轴做一个日度统计量(day_topw_mean 等),再 cross_ema 在日轴做长半衰期平滑,另一部分用 cs_bucket_zscore 在市值 / 上市年限 / 流通股本十分位内标准化,去掉与规模的非线性关系;cross_zscore 与短减长读「相对自己常态」的变化。
为什么样本外还会在:放量时的价格行为属于微观结构特征(散户 vs 机构参与的比例、算法执行、涨跌停与集合竞价制度),不依赖某一段行情;EMA 半衰期 20–40 日使排序慢变。可证伪:若 topw 一族(种子 1–7)都很差而时点一族(8–11)好,说明有用的是「什么时候成交」而不是「放量时涨跌」。
数学检查:无前视;day_signed_ratio 的分母是 sum|y|,无成交的日子为 NaN;day_topw_mean 用 90% 分位阈值,至少含 1 个分钟,有成交日才有值;day_centroid 的分母 sum|x| 同理;in_index 只是位置 t/(T-1) ∈[0,1];day_corr 在成交量日内恒定(如一字板)时分母只剩 EPS、分子为 0,得 0,不是爆点,且这样的日子占比小;day_gini 在全零日为 NaN;无近零分母爆点;无 ts_spearman / nt_*。"""
doc={"seed":2024,"round":2,"slots":[
{"type":"E","core":C,"hypothesis":hyp_e,"seeds":Es},
{"type":"N","hypothesis":hyp_n,"inspired_by":"M1 批的 div(cross_mean(day_last(Volume),40),cross_mean(day_sum(Volume),40))(尾盘成交占比,train -2.86)与共性表里均值差 +1.15 的 day_close(Amt):尾盘 / 放量是这批里最有东西的量,但只用了单点最后一分钟;M2 批里 15 日窗口的噪声问题说明要慢变平滑。","seeds":N}],
"R":R}
yaml.safe_dump(doc,open("../missions.yaml","w"),allow_unicode=True,width=10000,sort_keys=False)
