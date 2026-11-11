import yaml
T='day_sum(in_topk_masked(Ret, Volume, 20))'
Tl='day_sum(in_topk_masked(Ret, Volume, 20, False))'
A=f'signedpower({T})'
G='cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241)'
E=[
 f'cs_first_high20(day_autocorr_n1(Ret), {G})',
 f'cs_first_high20(mul(-1, cross_mean(day_sum(Ret), 20)), {G})',
 f'cs_first_high20(mul(-1, day_std(Ret)), {G})',
 f'cs_first_high20(cross_zscore(log(day_sum(Amt)), 60), {G})',
 f'cs_first_high40({A}, {G})',
 f'cs_first_low20({A}, {G})',
 f'cs_last_low20({A}, {G})',
 f'cs_last_low40(day_sum(in_topk_masked(Volume, Ret, 5)), {G})',
 f'add(cs_rank({G}), cs_rank({T}))',
 f'cs_first_high20(sub({T}, {Tl}), {G})',
 f'cs_first_high20({T}, cross_ema({G}, 5))',
 f'cs_first_high20(cs_regres({T}, day_sum(Volume)), {G})',
 f'cs_first_high20(ts_decay_linear({T}, 5), {G})',
 f'cs_first_high20(cs_bucket_zscore({T}, LogFloatCap), {G})',
 f'cs_first_high20(cross_corr(day_sum(Ret), day_sum(Volume), 60), {G})',
 f'cs_first_high20(cross_mean(div({T}, day_sum(Volume)), 20), {G})',
]
gs=[
 'cross_regbeta(cross_rank(day_sum(Volume), 30), cross_rank(day_sum(Vwap), 30), 241)',
 'cross_regbeta(day_sum(Ret), day_sum(Volume), 241)',
 'cross_corr(day_std(Ret), day_sum(Amt), 241)',
 'cross_regbeta(cross_rank(day_quantile_q75(High), 30), cs_rank(day_sum(Amt)), 241)',
 'cross_regbeta(day_std(Ret), cs_rank(day_sum(Vwap)), 241)',
 'cross_regbeta(cs_rank(LogFloatCap), cs_rank(day_sum(Vwap)), 241)',
 'cross_corr(day_sum(Ret), cs_rank(day_sum(Amt)), 241)',
 'cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_rank(day_sum(Amt)), 241)',
 'cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_rank(day_sum(Vwap)), 120)',
 'cross_corr(day_sum(Volume), day_sum(Vwap), 241)',
 'cross_regbeta(day_sum(Ret), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241)',
 'cross_regbeta(cross_rank(day_std(Ret), 30), cs_rank(day_sum(Vwap)), 241)',
]
N=[f'cs_first_high20({A}, {g})' for g in gs]
N+= [f'cs_first_high20({T}, {gs[4]})', f'cs_first_high40({A}, {gs[1]})']
def sw(s,**k):
    for a,b in k.items(): s=s.replace(a,b)
    return s
h1='cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))'
h2='cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(cross_rank(day_quantile_q75(Low), 30), 30), cs_last_low40(day_sum(Vwap), day_sum(Vwap)), 241))'
h3='cs_first_high20(signedpower(day_sum(in_topk_masked(Ret, Volume, 20))), cross_regbeta(cross_rank(day_quantile_q75(Low), 30), cs_last_low40(day_sum(Low), day_sum(Low)), 241))'
am=lambda s: s.replace('Ret, Volume, 20','Ret, Amt, 20')
R=[
 (h1,'Volume->Amt 把「当日涨幅最高 5% 分钟里的成交」从股数改成金额,去掉名义股价;拆解里该替换 +1.68 / +1.76 好于 +1.22',
  [am(h1), am(h1).replace(',241)',',482)'), am(h1).replace('q75(Low)','q75(High)'), h1.replace('Ret, Volume, 20','Ret, Amt, 10'),
   am(h1).replace('Low), 30)','Low), 60)'), am(h1).replace('cs_first_high20','cs_first_high40')]),
 (h2,'同上,Volume->Amt 拆解 +1.57 / +2.00',[am(h2), am(h2).replace(',241)',',482)'), am(h2).replace('q75(Low)','q75(High)')]),
 (h3,'同上,Amt 替换,并把 Low 的日内求和换成 Vwap',[am(h3), am(h3).replace('day_sum(Low), day_sum(Low)','day_sum(Vwap), day_sum(Vwap)')]),
]
d={'seed':2034,'round':3,'slots':[
 {'type':'E','core':G,'hypothesis':
 '核心 = 本流 round2 全部 head 共用的「门」:G = 241 日滚动回归斜率,自变量是 Low 日内 75 分位的 30 日截面均值排名,因变量是 cs_last_low40(Vwap,Vwap)(价格水平排名,最低 40% 压到底)。它是一个慢变的个股价格水平动态特征,不是日度信号。拆解显示去掉它分数从 +1.22 掉到 -1.52(必要性 +2.74),而内层 signedpower(放量上冲)只是单调改写(去掉 +1.17),整个 head 的 alpha 在门里。'
 '本轮不再让门只配「涨幅最高 5% 分钟里的成交」:把门换到完全不同的内层排序量(自相关、20 日反转、低波动、成交额意外、相对放量、双边差、分钟级重量收益、相关),换门宽(high40 / low20 / 排除式 last_low)、换组合方式(rank 相加而不是词典序)、对门做 EMA 平滑。库里已有候选都是 cs_first_high20(signedpower(topk 成交), G) 一种外围,这里外围算子集合完全不同。'
 '机制:A 股名义股价与价格水平相关的彩票偏好 / 散户参与度在门所刻画的慢特征上分层,门内再按短期信息排序,选出的是「慢特征 × 快信号」的交叉;门本身与流动性、波动、反转、市值控制都不是同一个量(它是年度窗口的斜率),所以不会被尺子的控制去掉;样本外还在是因为门每日变化极慢,换手低,15bp 成本吃不掉。',
  'seeds':E},
 {'type':'N','hypothesis':
 '新想法:round2 的赢家结构是「慢特征门 + 门内快信号」。本任务保持快信号 = 放量上冲(当日涨幅最高 5% 分钟里的成交量,signedpower 只是单调改写),完全不使用 round2 的那个门,而是换成其他 241 / 120 日窗口的个股特征:成交量对价格水平的斜率、收益对成交量的斜率(价格冲击弹性,Kyle lambda 思路)、波动与成交额的相关、价格水平 / 市值的共动、日内波动对价格水平的斜率、年度窗口下的收益与成交额秩相关。'
 '这些量都是一年尺度的慢变个股特征,衡量「该股票的量 / 价 / 波动是怎样联动的」:门内股票是量价联动强(信息交易占比高)或价格水平特殊的一类,其放量上冲才有信息含量,门外的放量上冲更像噪声交易,所以先分层再排序比无条件排序干净。算子上用 cross_regbeta / cross_corr 估计慢特征,cs_first_high20/40 做门,和库里所有只做单一时间序列的表达式骨架不同(库里 0 条用过 cs_first_*)。'
 '样本外还会在:慢特征变化慢,换手低;门与控制不同源;不依赖 round2 那个具体的价格水平门,若 round2 的结果只是价格水平的伪影,这里的非价格门可作对照。',
 'inspired_by':'B101 / B102 批里的放量上冲(in_topk_masked(Ret, Volume, 20))与成交额一族,加上 round2 E 位拆解里「门必要、内层只是单调改写」的现象',
 'seeds':N},
],'R':[{'head':h,'why':w,'variants':v} for h,w,v in R]}
yaml.safe_dump(d,open('../missions.yaml','w'),allow_unicode=True,width=10000,sort_keys=False)
print(len(E),len(N),sum(len(r[2]) for r in R))
