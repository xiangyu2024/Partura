# -*- coding: utf-8 -*-
import yaml
core='day_es_ratio_lo(Vwap)'
hi='day_es_ratio_hi(Vwap)'
e_seeds=[
f'cross_mean({core}, 20)',
f'cross_mean({core}, 60)',
f'cross_stddev({core}, 60)',
f'cross_zscore({core}, 60)',
f'sub(cross_mean({core}, 10), cross_mean({core}, 120))',
f'cs_bucket_zscore(cross_mean({core}, 20), LogFloatCap)',
f'cs_bucket_zscore(cross_mean({core}, 60), cross_mean(day_std(Amt), 30))',
f'cross_corr({core}, ts_delta(log(day_last(Close)), 1), 60)',
f'cross_mean(sub({core}, {hi}), 20)',
f'cross_mean(sub({core}, day_es_ratio_lo(Close)), 20)',
f'cross_mean(mul({core}, sign(ts_delta(log(day_last(Close)), 1))), 20)',
f'cross_tail_mean_q25({core}, 60)',
f'cross_autocorr({core}, 60, 1)',
f'cross_ema({core}, 30)',
f'cs_bucket_zscore(cross_stddev({core}, 60), LogFloatCap)',
]
O='sub(log(day_first(Open)), log(ts_delay(day_last(Close), 1)))'
I='sub(log(day_last(Close)), log(day_first(Open)))'
n_seeds=[
f'cross_mean({O}, 60)',
f'cross_mean({O}, 120)',
f'sub(cross_mean({O}, 60), cross_mean({I}, 60))',
f'cross_corr({O}, {I}, 120)',
f'cross_regbeta({O}, {I}, 60)',
f'cs_bucket_zscore(cross_mean({O}, 60), LogFloatCap)',
f'div(cross_stddev({O}, 60), add(cross_stddev({I}, 60), 0.0001))',
f'cross_tail_mean_q25({O}, 60)',
f'cross_corr({O}, ts_delay({I}, 1), 60)',
f'cross_ema(sub({O}, {I}), 40)',
f'cs_bucket_zscore(sub(cross_mean({O}, 60), cross_mean({I}, 60)), cross_mean(day_std(Amt), 30))',
f'cross_zscore(cross_mean({O}, 20), 120)',
]
hypE=f"""机制:核心 {core}(loc 共性表第 8 行,+1.08,p 0.000,23 个候选;含它的候选均值 -1.22,不含 -2.30)。day_es_ratio_lo 是「日内分钟 Vwap 低于当日 5% 分位的那些分钟的均值 / 该分位」:Vwap 是价格,所以它是价格尺度不变的日内下探深度(低尾比 5% 分位再低多少),接近 1 的一个小范围量;它不含任何成交量 / 成交额 / 价位水平,和已知的成交额族、流动性、市值、20 日反转都不是同一个东西。第 2 轮 N 位的最好候选(-0.21)就把它当 cross_regbeta 的右侧用,这说明它在新尺子下带信息,但那些候选的外围是 cross_regbeta + 乘积 + 日频字段 z 分数,没人单独读过它。本位的假设:日内低尾的深度是「某天被抛压打穿又被收回」的痕迹(流动性提供者的补偿 / 日内恐慌被吸收),这个痕迹按天稀疏而噪声大,只有在日轴上做累积(10 / 20 / 60 日均值、尾部均值、波动、滞后自相关、与同日收益的相关、与上尾的差)才能读出个股的慢性质,而不是某一天的偶然。
算子实现(15 个种子全部原样含核心):cross_mean 20 / 60、cross_ema 30(水平);cross_stddev 60(日内下探的不稳定度);cross_zscore 60(相对自身历史的异常);短 10 日减长 120 日(持续恶化 / 缓和);十档内 z 分数(LogFloatCap、已知成交额族),对阶跃型控制暴露是中性的;cross_corr 与同日对数收益(下探深的日子价格是涨还是跌:被吸收还是被击穿);低尾减高尾(day_es_ratio_hi)只剩下偏斜;低尾减 Close 的低尾(Close 是分钟收盘价,Vwap 含成交量权重,差来自成交量集中的位置);乘当日收益符号的 20 日均值;下 25% 尾均值;60 日滞后 1 日自相关。
和库里不同:两个库的 5583 条表达式里 day_es_ratio 出现 0 次(grep 过 members.csv),cross_* 日轴读法在这条流以前只出现在 R2 N 位的 cross_regbeta 骨架里;这里是单一对象的各种直接读法,外围算子集合(cross_mean / cross_stddev / cross_corr / cross_autocorr / cs_bucket_zscore / cross_tail_mean)与快照里含该核心的候选(cross_regbeta + mul + ts_delay + cross_zscore 外围)不同。不依赖 ts_hurst,没有 -inf 路径。
数学检查:day_es_ratio_lo 在分位近零时返回 NaN(不是 inf),价格为正所以分位 > 0,日均处理没有爆点;全部窗口尾随,无前视(分钟只用当天,t+1 交易);cross_mean 等对窗口内有限值求均值,不用 0 填充;10 日减 120 日的前 120 日估计用天数较少但不是常数;没有禁用算子。
为什么样本外还会在:来源是日内微观结构的慢性质(谁在深度处接单、谁的价格被抛压反复击穿),依赖持股结构与做市环境而不是某一段行情;60 日读数换手低,15 bp 成本下可行。诚实预期:最好分数大概在 -0.3 一带,押的是读法而不是核心的水平。"""
hypN="""新 idea:隔夜与日内收益的「拔河」。O = log(今开) - log(昨收)(隔夜收益,今开是开盘集合竞价后第一分钟的开盘价),I = log(今收) - log(今开)(日内收益)。机制(Lou, Polk & Skouras 2019;Hendershott, Livdan & Schürhoff 2015):隔夜段主要是散户 / 情绪与信息的反应,日内段是机构与做市商的执行;个股隔夜收益的持续性(过去隔夜收益高的票未来隔夜收益继续高)与日内的反转(隔夜跳空之后日内回吐)都是稳定存在的横截面性质,且它们和「总收益动量 / 20 日反转」不是同一个东西,因为总收益 = O + I,两段的符号可以相反。
算子实现(12 个种子,全是日轴上的尾随统计,没有用 ts_hurst):cross_mean(O, 60 / 120)(隔夜收益的持续水平);cross_mean(O) 减 cross_mean(I)(两个段的收益差,Lou 型);cross_corr(O, I, 120)(同日内跳空之后是回吐还是接力:个股的「跳空回补」倾向);cross_regbeta(O, I, 60)(日内收益对隔夜收益的斜率);cross_corr(O, 前一日的 I, 60);cross_stddev(O)/(cross_stddev(I) + 1e-4)(隔夜波动占比;分母加 1e-4 防近零);cross_tail_mean_q25(O, 60)(最差的 25% 隔夜跳空有多深);cross_ema(O - I, 40);cross_zscore(cross_mean(O, 20), 120);两个十档内 z 分数(LogFloatCap、已知成交额族),对阶跃型控制暴露中性。
和库里不同:库里含 day_first(Open) 的 109 条几乎全是 ts_corr / cs_rank 的成交额与价位组合,或 abs 缺口一项,没有一条把隔夜与日内两段分开做日轴累积 / 相关 / 回归;库里 0 条含 cross_corr(O, I, ·) 或 cross_regbeta 的这一对;库里 0 条含 LogFloatCap。N 位不受 R2 N 位(日频成交活跃度 / 市值字段)的重复约束,对象换成价格的两段分解。
数学检查:O、I 都是两个价格比的对数,价格(后复权)为正,无近零分母(除第 7 号分母加 1e-4);ts_delay(day_last(Close), 1) 是昨日收盘,无前视;今开是当日第一分钟,在当日收盘之后才使用,t+1 才交易;复权在分钟间不断裂(同日内同一复权因子),隔夜用后复权昨收与今开,除权日两者复权口径一致,所以不会产生除权假跳空。停牌日 Open 缺失时 O 为 NaN,被 cross_* 的有限值均值跳过,不是 0 填充。没有禁用算子。
为什么样本外还会在:隔夜 / 日内的客户群结构(散户集中在隔夜、机构集中在日内、T+1 限制隔夜风险承担)是 A 股的制度性特征,不是某一段的行情;60 ~ 120 日读数名次变化慢,换手低。风险:隔夜收益水平可能与 20 日反转 / 小盘有残余相关(已被尺子去掉线性 / U 形 / S 形暴露);我对出 head 的概率只给约 5%。"""
d={'seed':2002,'round':3,'slots':[
 {'type':'E','core':core,'hypothesis':hypE,'seeds':e_seeds},
 {'type':'N','hypothesis':hypN,'inspired_by':'本流第 3 个结构批(B006)的共性表:含 day_es_ratio_lo(Vwap)、day_var(in_delay(Low,5))、Close 隔日收益、对数换手 z 分数的候选显著好于其余(+1.0 ~ +1.3),第 2 轮 N 位最好的 -0.21 就是这些件的 cross_regbeta 组合;说明在新尺子下有残余的是价格路径的形状与日内 / 隔夜的分解,而不是 Hurst 与成交量水平。本位把价格拆成隔夜与日内两段。','seeds':n_seeds}]}
yaml.safe_dump(d,open('missions.yaml','w'),allow_unicode=True,width=10000,sort_keys=False)
