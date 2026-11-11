import yaml
P='sub(LogFloatCap, LogFloatShares)'
KV='day_kurt(Vwap)'
W=f'add({KV}, add({KV}, 4))'
C=f'mul(day_sum(Ret), {W})'
m=lambda d:f'cross_mean({C}, {d})'
e1=[
f'cs_bucket_zscore(cross_delay({m(241)}, 20), {P})',
f'cross_mean(cs_bucket_zscore({C}, {P}), 241)',
f'cs_bucket_zscore(sub({m(482)}, {m(120)}), {P})',
f'cs_bucket_zscore({m(241)}, cross_mean({KV}, 241))',
f'cs_bucket_zscore(cs_bucket_zscore({m(241)}, {P}), LogFloatCap)',
f'cs_bucket_zscore({m(241)}, ListAge)',
f'cs_bucket_zscore(div({m(241)}, cross_mean({W}, 241)), {P})',
f'cs_bucket_zscore(ts_rank(cross_mean({C}, 60), 241), {P})',
f'cs_bucket_zscore(sub({m(241)}, cross_delay({m(241)}, 120)), {P})',
f'cs_bucket_zscore(cross_mean(cs_winsor({C}), 241), cross_mean(day_std(Amt), 30))',
f'cs_bucket_zscore({m(241)}, cross_mean(day_std(Ret), 241))',
f'cs_bucket_zscore(sub({m(241)}, cross_mean(cs_rank({C}), 241)), {P})',
]
def A(w): return f'cs_bucket_zscore(cross_mean(mul(day_sum(Ret), {w}), 241), {P})'
n=[A('add(day_gini(Amt), 1)'),A('sub(day_centroid(Amt), 0.5)'),A('day_es_ratio_lo(Ret)'),
A('add(day_at_max_ratio(High), 1)'),A('add(day_gini(Ret), 1)'),A('add(cs_rank(day_skew(Ret)), 1)'),
A('add(day_flat_ratio(Close), 1)'),A('day_signed_ratio(Ret, Amt)'),
f'cs_bucket_zscore(cross_mean(mul(day_wmean(Ret, Amt), {W}), 241), {P})',
f'cs_bucket_zscore(cross_mean(mul(day_topw_mean(Ret, Volume), {W}), 241), {P})',
A('add(day_distinct_ratio(Close), 1)'),
A('add(day_gini(Amt), add(day_gini(Ret), 1))')]
def R1(w=W,win=241,inner=None,b=P,agg='cross_mean',base='day_sum(Ret)'):
    c=f'mul({base}, {w})'
    if inner: c=inner.format(c)
    return f'cs_bucket_zscore({agg}({c}, {win}), {b})'
HV=R1()
r1=[R1(w=f'add({KV}, add(day_kurt(High), 4))'),R1(win=300),R1(win=360),
R1(w=f'add({KV}, add(day_kurt(Close), 4))'),R1(w=f'add(cs_rank({KV}), 1)'),
R1(base='day_wmean(Ret, Amt)'),R1(inner='cs_winsor({})'),R1(agg='cross_ema',win=200),
R1(w=f'add({KV}, add({KV}, 8))'),R1(w=f'add(day_kurt(Vwap), add(day_kurt(High), add(day_kurt(Low), 4)))')]
H=lambda f,w,b='LogFloatCap':f'cs_bucket_zscore(ts_std({f}, {w}), {b})'
h2='cs_bucket_zscore(ts_std(day_kurt(High), 240), LogFloatCap)'
r2=[H('day_kurt(Vwap)',240),H('add(day_kurt(High), day_kurt(Vwap))',240),H('day_kurt(High)',300),
H('day_kurt(High)',200),H('day_kurt(High)',240,P),H('day_kurt(Close)',240)]
hyp_e=("核心 = 日收益 day_sum(Ret) 乘 (2*day_kurt(Vwap)+4),即本组当前最好 head(score +0.86,train +0.86 / valid +1.07)"
"cs_bucket_zscore(cross_mean(核心,241), 名义价格)的内核。拆解:去掉峰度权重 -0.29,去掉名义价格桶 -0.21,窗口 120 / 482 为 +0.25 / +0.50,"
"Vwap 换 Close +0.69,所以信号是「峰度加权日收益 → 慢平均 → 名义价格十分位内标准化」。这个核心(Vwap 版)此前没做过 E 位(前两轮 E 位的核心是 Low 版)。"
"机制假设:分钟 Vwap 路径峰度高的日子是少数分钟成交量集中成交 / 跳跃的日子,这类日子的收益带有更多信息(知情交易 / 机构冲击),"
"按它加权的 241 日平均读的是「由信息冲击日贡献的漂移」而不是普通 12 个月动量;尺子控的是 20 日反转与成交额族,没有控中期动量。"
"本轮外围刻意与 head 和已见写法不同(之前的外围都是 cross_mean/cross_ema 加 cs_bucket_zscore 的价格桶,只调窗口 / 聚合器):"
"(1)cross_delay 20 日跳过最近一个月再取 241 日均值(去掉短期反转混入);(2)先在当日名义价格桶内标准化、再时间平均(换顺序,桶按当日成分);"
"(3)482 日均值减 120 日均值(长期漂移减中期漂移,只留慢变部分);(4)桶变量换成自身 241 日平均峰度 / 上市年龄 / 成交额波动 / 收益波动,"
"即在「同样跳跃程度 / 同样新旧 / 同样流动性」的同伴里比动量;(5)除以平均权重变成加权平均收益(两个 cross_mean 之比,骨架与 head 不同);"
"(6)ts_rank 个股相对自己历史的位置;(7)动量加速度:241 日均值减 120 日前的 241 日均值;(8)两层桶 价格 → 市值。"
"其中多数种子与现 head 的日度秩相关预计 0.4 ~ 0.7,不会被库禁令挡掉,新 head 要靠骨架不同。"
"为什么样本外还会在:valid 的分数不低于 train(+1.07 对 +0.86),不是只在一段;来源是 A 股散户为主的市场里信息冲击日的慢扩散,变化慢,窗口 120 ~ 482 日、桶内相对值、换手低,15bp 下不被吃掉。"
"数学检查:无前视(只用 cross_delay / 尾随窗口,没有 cross_shift / ts_shift);day_kurt >= -2 所以权重 2k+4 >= 0,div 的分母是 241 日平均权重(>= 0 且远离 0,日均约 4 ~ 10);"
"cross_delay 取 20 日前的值是过去;ListAge 桶是日频叶子,正常叶子。")
hyp_n=("想法:峰度加权动量里起作用的可能不是「峰度」本身,而是「这一天的收益是不是由少数集中事件贡献的」;把权重换成别的、与峰度不同的日内集中度 / 事件度量,"
"检验「集中事件日的收益才有慢动量」这个更一般的机制,而不是只押峰度。机制:Chan(2003)与 Tetlock 类证据 —— 有显著信息事件的日子,价格反应不足,收益在之后数月继续漂移;没有事件的日子是噪声。"
"算子怎样实现:每个种子都是 cs_bucket_zscore(cross_mean(day_sum(Ret) × 权重, 241), 名义价格),权重分别是 成交额集中度 day_gini(Amt) / 收益集中度 day_gini(Ret) /"
"成交额重心 day_centroid(Amt)(重心偏尾盘 vs 开盘,日内资金何时进来) / 左尾平均深度 day_es_ratio_lo(Ret)(尖锐下跌事件) /"
"在日高点停留的时间占比 day_at_max_ratio(High)(涨停 / 封板事件) / 日收益偏度的截面排名 / 一价占比 day_flat_ratio(Close)(无交易分钟) /"
"净买入压力 day_signed_ratio(Ret, Amt) / 不同价位数 day_distinct_ratio(Close);另外把「日收益」本身换成成交额加权收益 day_wmean(Ret, Amt) 或最重 10% 成交分钟的收益 day_topw_mean(Ret, Volume),再乘 Vwap 峰度权重。"
"批内现象:本批的共性表里 day_sum(Ret)(+1.29,157 条)、day_wmean(Ret, Amt)(+1.13)、day_pos_ratio(Ret)(+1.07)、day_at_max_ratio(add(-5, Low))(+1.20)、day_std(Amt)(+0.75)都富集,"
"说明「收益 × 日内集中度 / 成交」这一格有东西,而且 head 靠的是 day_sum(Ret) × 峰度,而不是峰度单独。"
"和库不同:库里没有一条把 day_sum(Ret) 乘上 day_gini / day_centroid / day_es_ratio_lo / day_at_max_ratio 这类权重再做 241 日慢平均,骨架(算子集合)都不同于 head 的 kurt 骨架,也不同于库里任何一条;"
"之前的 N 位(日收益序列的形状 FIP / t 值 / MAX)不涉及日内权重。为什么样本外还会在:信息事件日的收益反应不足是行为 / 信息扩散的慢机制,窗口 241 日、名义价格桶内相对值,换手低;valid 段在 head 上比 train 好。"
"数学检查:无前视;day_gini 在 [0,1],加 1 后权重 ∈ [1,2];day_centroid 减 0.5 后是有符号权重,不会近零分母(乘法);day_es_ratio_lo 在分位数近 0 时返回 NaN 而不是爆点,乘法不爆;"
"day_at_max_ratio / day_flat_ratio / day_distinct_ratio 在 [0,1];day_signed_ratio ∈ [-1,1];所有种子全是乘法与加常数,没有除法;停牌日 NaN 被 cross_mean 跳过。")
m=dict(seed=2042,round=3,slots=[dict(type='E',core=C,hypothesis=hyp_e,seeds=e1),
 dict(type='N',hypothesis=hyp_n,inspired_by='第 1 个结构批共性表:day_sum(Ret) +1.29(157 条)、day_wmean(Ret, Amt) +1.13、day_at_max_ratio(add(-5, Low)) +1.20、day_pos_ratio(Ret) +1.07 富集;head 1 的拆解显示去掉峰度权重 -1.15 但权重换成 Vwap / High / Close 都行(+0.68 ~ +0.86)',seeds=n)],
 R=[dict(head=HV,why='拆解:权重项在 Low / High / Vwap / Close 间不挑字段(+0.66 ~ +0.86),窗口 482 为 +0.50,说明部件的字段与窗口没定型;train 是短板(+0.86 对 valid +1.07),试混合字段、窗口 300 / 360、成交额加权收益、winsor、EMA',variants=r1),
 dict(head=h2,why='拆解:ts_std 部件是必要的(去掉 -3.05),字段 High / Low 同分;上一轮 Low 的窗口越长越差,High 窗口 240 最好;试换字段 Vwap / Close / 混合、窗口 200 / 300、名义价格桶',variants=r2)])
yaml.safe_dump(m,open('missions.yaml','w'),allow_unicode=True,width=200,sort_keys=False)
