import sys,yaml
sys.path.insert(0,'/Users/wxy/Desktop/Partura-prod/research/prod_W02L/partura/s2034/r2/scratch')
import seeds as S
hE='''核心 `day_sum(in_topk_masked(Ret, Volume, 20))` = 每天收益最高 5% 分钟里的成交量之和(拆解 sufficiency -1.37,train -1.22 / valid -1.37,比带分母的整体 head 好)。
机制(B101 里「成交量在收益最高的那批分钟里占多大」这件事的去水平、双边改写):核心 `in_topk_masked(Ret, Volume, 20)` 是每天分钟收益排名前 5% 的分钟里的成交量(Volume 作值,Ret 作选择键)。B101 里 3 个 head(得分 -2.14 / -2.35 / -1.88)全是「这个量除以当天总成交量、再做 20 日截面均值」。拆解表给了两条事实:(1) 把除以 day_sum(Volume) 去掉后得分抬到 -1.11 到 -1.16(必要性 -0.98 到 -1.24,即分母是烂部件;分母是当天总量,它自己含分子,又带名义股价);(2) 核心只取了涨幅最大的分钟,没有对称地看跌幅最大的分钟,所以读到的是「放量上冲」和「整体放量」混在一起。
这一位要试的外围(和库里见过的 `cross_mean(div(day_sum(核心), day_sum(Volume)), 20)` / `cross_stddev(...)` 写法都不同):
(a) 双边:同一天收益最低 5% 的分钟里的成交量 `in_topk_masked(Ret, Volume, 20, False)`(库里这个骨架只出现在 Volume 作键、Open/Close 作值的写法里,收益作键的双边写法没有),取差或取对数差,度量「放量发生在上冲还是下杀」,即分钟级订单流方向的代理(买方主动推价的成交 vs 卖方主动砸价的成交;Chordia–Subrahmanyam 的订单流不平衡、Llorente 等 2002 的量价关系);差或对数比天然去掉了总成交量的水平,不需要除以当天总量;
(b) 去水平:分母换成 60 或 120 日的 cross_mean(day_sum(Volume)),即「相对自己常态」而不是「相对当天」(分母里不含分子,不会被当天放量抵消);对数后做 60 日 cross_zscore 即对自己历史标准化;cs_regres 对 Volume 基线回归;按成交额或流通市值十分位内标准化(cs_bucket_zscore / cs_bucket_demean);
(c) 关系:上冲成交量与当天收益的滚动相关 / 回归(60 日),读「价格冲击是否伴随放量」。
实现:day_sum 对掩码后的分钟面板求和(非选中分钟为 NaN,nansum);log 的输入是 20% 以内分钟的成交量之和,正常交易日 > 0,停牌日整天缺失 / 为 0 时 log 为 NaN 而不是 -inf,在滚动窗口里被配对剔除。
为什么和以前不一样:已见的 150 个候选的外围全是「同一天总量作分母 + 截面均值 / 标准差」;这里分母是自己的历史基线或根本没有分母(取差),并加入双边与回归、分桶。16 个种子的算子骨架已逐个与 struct/members.csv 的 4100 个不同骨架对照,全部不在其中。
为什么样本外还会在:读的是一天里「成交量跟着哪个方向的价格冲击走」,这是订单流不平衡的缓变特征,按月、按年稳定;种子主体是差 / 对数差 / z 分数 / 回归残差,不是水平;换手由 20 到 60 日平滑压住,15 bp 不会吃光。最可能的失败:(1) 这块与波动控制同源(涨幅最大的分钟几乎等于波动大的分钟),被尺子去掉;(2) 平局(一字板、低价股的零收益分钟)使前 5% / 后 5% 的选择变成列序,引入噪声;(3) 毛超额为 0。
数学检查:没有除以近零的量(分母是 60 / 120 日平均成交量,可交易股票 > 0;停牌日在平均里是缺失);无前视(Ret 和 Volume 都是当天分钟数据,t 日收盘后可得,t+1 才交易;所有 cross_* 只回看含当天);没有 ts_rank / cross_rank 的日轴用法。'''
hN='''机制:日内「成交最重的分钟里价格往哪个方向走」。与 B101 相反的角色分配:B101 里是「收益最大的分钟里的成交量」(Ret 作键、Volume 作值);这里是 `in_topk_masked(Volume, Ret, 5)`,成交量最大的 20% 的分钟里的收益(Volume 作键、Ret 作值),再减去成交量最小的 20% 的分钟里的收益(第 4 个参数 False)。日内重量分钟的价格推进量,是「有信息的资金推动价格」的代理(Easley–O'Hara 的知情交易与成交量、Kyle 的 lambda 的符号版本、Campbell–Grossman–Wang 1993 的放量与收益的自相关:无信息的放量之后反转,有信息的放量之后延续)。
实现:`day_sum(in_topk_masked(Volume, Ret, 5))` 是重量分钟收益之和(单位是收益,无量纲,没有成交量或成交额的水平);减去轻量分钟的那一份,等于把整体涨跌的方向去掉,只剩「重量分钟 vs 轻量分钟」的差。再用 20 到 60 日 cross_mean / cross_zscore 平滑,或除以 day_std(Ret)(把波动去掉)、除以 60 日平均 |日收益|,或在流通市值十分位内标准化,或用 60 日 cross_corr / cross_regres / cross_regbeta 读「重量分钟收益与轻量分钟收益」之间的关系。
和库里已有的不同:库里 `in_topk_masked(Volume, ·)` 的值全是价格水平(Open / Close,没有 Ret),并且都是单边;本批 B101 的 head 全是成交量在收益大的分钟里的占比,其值是成交量的水平(分数 -1.9 到 -2.4,拆解显示分母 / 水平是烂部件)。这里的值是收益,不含任何成交量水平,所以与 B101 head、与流动性控制的秩相关预计 < 0.3;与已知族 / 波动控制可能 0.2 到 0.5。16 个种子骨架已与 4100 个不同骨架对照,全部不在库里。
为什么样本外还会在:这是日内价格发现的结构性特征(重量分钟承载了大部分信息),不依赖某段风格;窗口 20 到 60 日,换手低;种子里既有差(去掉整体方向)、也有比值(去掉波动)、也有相关(读关系),真有信号时不会只在一种写法上成立。最可能的失败:(1) 重量分钟收益之和与 20 日反转 / 日内波动同源,被尺子去掉;(2) 重量分钟集中在开盘和收盘集合竞价附近,读到的主要是隔夜缺口与尾盘行为;(3) 毛超额为 0。
数学检查:种子 3 的分母 day_std(Ret) 在一字板 / 停牌日为 0,该日除法给 NaN 或 inf 由算子保护处理,已在合成立方体上验证无 inf,且该种子是 20 日均值,单日极值不会支配;无前视(都是当天分钟,t+1 交易);不用 ts_rank / cross_rank 日轴;in_topk_masked 的 k 为 (有效分钟数+1)//p,个数每天固定,不受停牌影响(停牌日全 NaN)。'''
EC='day_sum(in_topk_masked(Ret, Volume, 20))'
U='day_sum(in_topk_masked(Ret, Volume, 20))'
def R(head,why,v): return {'head':head,'why':why,'variants':v}
Rr=[
 R('cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 20)), day_sum(Volume)), 20)',
   '拆解里分母 day_sum(Volume) 是烂部件:去掉后 -1.16(必要性 -0.98),因为分母是当天总量,含分子且带名义股价;但去掉后只剩成交量水平。变体改成相对自己 60/120 日基线的分母(分母里不含当天分子)、双边取差、对数 z 分数、分桶。',
   [f'cross_mean(div({U}, cross_mean(day_sum(Volume), 60)), 20)',
    f'cross_mean(div({U}, cross_mean(day_sum(Volume), 120)), 40)',
    f'cross_mean(div(sub({U}, day_sum(in_topk_masked(Ret, Volume, 20, False))), cross_mean(day_sum(Volume), 60)), 20)',
    f'cross_zscore(log({U}), 60)',
    f'cs_bucket_zscore(cross_mean(day_sum(in_topk_masked(Ret, Volume, 20)), 20), cross_mean(day_sum(Amt), 30))']),
 R('cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), day_sum(Volume)), 20)',
   '同上:去分母后 -1.11(必要性 -1.24);窗口 20->40 也变好(+0.17),说明平滑太短也是烂的。变体用 50 分位(前 2% 分钟)的核心、更长平滑、相对自己基线的分母。',
   ['cross_mean(div(day_sum(in_topk_masked(Ret, Volume, 50)), cross_mean(day_sum(Volume), 60)), 40)',
    'cross_mean(sub(log(day_sum(in_topk_masked(Ret, Volume, 50))), log(day_sum(in_topk_masked(Ret, Volume, 50, False)))), 40)',
    'cross_zscore(log(day_sum(in_topk_masked(Ret, Volume, 50))), 120)']),
 R('cs_bucket_zscore(ts_max(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), 10), cross_mean(day_sum(Amt), 30))',
   '拆解里去掉外层 ts_max 增益 +0.18(必要性 -0.18),是烂部件;ts_std 对平滑后成交额的绝对波动与水平成正比。变体去掉 ts_max,并把绝对波动换成相对波动(对数标准差、除以水平)。',
   ['cs_bucket_zscore(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), cross_mean(day_sum(Amt), 30))',
    'cs_bucket_zscore(ts_std(log(ts_decay_linear(day_sum(Amt), 50)), 10), cross_mean(day_sum(Amt), 30))',
    'cs_bucket_zscore(div(ts_std(ts_decay_linear(day_sum(Amt), 50), 10), ts_decay_linear(day_sum(Amt), 50)), cross_mean(day_sum(Amt), 30))',
    'cs_bucket_zscore(ts_std(ts_decay_linear(day_sum(Amt), 50), 20), cross_mean(day_sum(Amt), 30))']),
]
out={'seed':2034,'round':2,'slots':[
 {'type':'E','core':EC,'hypothesis':hE,'seeds':S.E_SEEDS},
 {'type':'N','hypothesis':hN,'inspired_by':'B101:全部 head 是「收益最大的分钟里的成交量 ÷ 当天总量」,拆解显示分母(总量水平)是烂部件、去掉后分数抬高;而键与值互换(成交量最大的分钟里的收益)在库里不存在','seeds':S.N_SEEDS}],
 'R':Rr}
for s in out['slots']:
    s['hypothesis']=s['hypothesis'].strip()
yaml.safe_dump(out,open('missions.yaml','w'),allow_unicode=True,width=200,sort_keys=False)
