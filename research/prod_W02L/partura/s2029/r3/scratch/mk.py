import yaml
Z4="ts_std(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40), 40)"
Z3="ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)"
FC="LogFloatCap"
e1=[
f"cs_last_low10({FC}, {Z4})",
f"cs_last_low10(neg({FC}), {Z4})",
f"cs_last_low10(cross_semistd_neg(day_mean(Volume), 241), {Z4})",
f"cs_last_low10(neg(cross_mean(day_sum(Ret), 120)), {Z4})",
f"cs_last_low10(cross_mean(day_zero_ratio(Volume), 60), {Z4})",
f"cs_last_low05(sub({FC}, LogFloatShares), {Z4})",
f"cs_last_low20(cross_semistd_pos(day_mean(Volume), 120), {Z4})",
f"cs_last_low10({Z4}, {FC})",
f"cs_first_low40({Z4}, {FC})",
f"cs_first_low20(neg({Z4}), ts_mean(day_mean(Amt), 60))",
f"cs_bucket_rank({Z4}, {FC})",
f"cs_bucket_rank({Z4}, ts_mean(day_mean(Amt), 60))",
f"cs_last_low10(sub(log({Z4}), log(ts_mean(day_mean(Amt), 60))), {FC})",
f"cs_last_high10({Z4}, cross_mean(day_zero_ratio(Volume), 60))",
]
fl="cross_mean(day_flat_ratio(Close), 60)"
n=[
fl,
"cross_mean(day_flat_run_max(Close), 120)",
"cross_mean(day_distinct_ratio(Close), 60)",
f"cs_last_high10(neg({FC}), {fl})",
f"cs_last_high10(cross_semistd_neg(day_mean(Volume), 241), {fl})",
"cs_first_high20(cross_mean(day_sum(Ret), 120), cross_mean(day_flat_run_max(Close), 60))",
f"cs_bucket_rank({fl}, {FC})",
f"cs_regres({fl}, cross_mean(day_zero_ratio(Volume), 60))",
f"sub({fl}, cross_mean(day_flat_ratio(Close), 241))",
"ts_std(ts_std(day_std(Amt), 40), 40)",
f"cs_last_low10({FC}, ts_std(ts_std(day_std(Amt), 40), 40))",
f"cs_last_low10({fl}, ts_std(ts_std(day_max(Amt), 40), 40))",
f"cs_last_low10(ts_std(ts_std(day_std(Amt), 40), 40), {fl})",
]
head="cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))"
rv=[head.replace("LogFloatCap","LogTotalCap",1),
    head.replace("LogFloatCap","sub(LogFloatCap, LogFloatShares)",1),
    head.replace("log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))",Z4+")")[:-1]+")" if False else head[:head.rindex(", log(")]+", "+Z4+")",
    head[:head.rindex(", log(")]+", ts_std(ts_std(day_mean(Amt), 40), 40))"]
lit_e=[
 dict(title="A simple model of capital market equilibrium with incomplete information",authors="Robert C. Merton",year="1987",treatment="被忽视的股票要求更高收益;成交额变异长期最低的一档是休眠度的代理,这里换成 Z4 当带,并把带内排序换成与 Z2 水平无关的变量"),
 dict(title="Asset pricing and the bid-ask spread",authors="Yakov Amihud, Haim Mendelson",year="1986",treatment="低流动性溢价;检验它是被标记集合本身,还是带内的市值 / 价位 / 休眠度排序"),
 dict(title="A new estimate of transaction costs",authors="David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka",year="1999",treatment="零成交占比作为流动性代理,用作带或带内排序"),
]
lit_n=[
 dict(title="A new estimate of transaction costs",authors="David A. Lesmond, Joseph P. Ogden, Charles A. Trzcinka",year="1999",treatment="价格不动(零收益日)占比作为交易成本 / 休眠度的代理;这里用分钟级的价格停滞占比"),
 dict(title="Liquidity and expected returns: lessons from emerging markets",authors="Geert Bekaert, Campbell R. Harvey, Christian Lundblad",year="2007",treatment="新兴市场里零收益占比定价;休眠度的价格端度量"),
 dict(title="The neglected and small firm effects",authors="Avner Arbel, Paul Strebel",year="1982",treatment="被忽视效应:休眠 / 少被关注的票的溢价"),
]
hyp_e=("事实(快照):本流唯一站得住的东西是第 1 轮 6 个 head(D 尺子下仍 +1.25)。形状是 cs_last_low10(y, x),x 是嵌套成交额标准差水平(Z2 / Z3)的最低 10%(整块并列沉底),带内 y 的 log 项数值上是死的(元量级的 Z2 与 O(1) 的 log 相减,排序由 -Z2 独占;审计在第 2 轮指出过),所以实际读的是「成交额波动的波动」的水平,外面套一个最低一档的阶跃。拆解:把 y 换成 log(Z4) 单独是 -0.10 / -0.35,去掉 -LogFloatCap 是 -1.19 / -0.14,说明水平 / 市值承重而不是去量纲。"
"本位核心 Z4 = ts_std 四层的成交额(head 1 的子树,第 1 次作核心;Z3 已用满 2 次)。设计是同时动「带」和「带外排序」:六个 head 全是 x = Z2 / Z3、带外 y = -Z2 水平。本位的种子分三类:(i) 带 = Z4 最低 10% / 5% / 20%,带外按完全不同的变量排:市值(正反两个方向)、名义价 LogFloatCap - LogFloatShares、120 日收益(反向)、60 日零成交分钟占比、一年期成交量下行半标准差(量增长「安静度」)、上行半标准差(种子 1 ~ 7);(ii) 把 Z4 放进 y,带改为「最小市值 10% / 40%」或「60 日均成交额最低 20%」(种子 8 ~ 10),检验「同样的休眠度排序,在小票内部是否仍有 alpha」;(iii) 无阶跃的连续版:Z4 在市值十档内取秩、在 60 日均成交额十档内取秩(种子 11 ~ 12),以及 log(Z4) - log(60 日均成交额)(Z4 相对水平的无量纲版本)放在最小市值带里(种子 13)和用零成交占比最高的 10% 作带(种子 14)。"
"为什么与库 / head 不同:库里 5583 条没有一条用 cs_last_* / cs_first_* / cs_bucket_*;已出 head 的带外排序都是 -Z2 水平,本位的带外排序是市值 / 价位 / 收益 / 零成交 / 量增长不对称,数值上与 -Z2 不同,所以与 head 的日度秩 |ρ| 预计只来自共享的那 10% 名字(0.2 ~ 0.6)。种子 8 ~ 12 的带不是 Z 型,Z4 只做排序变量或十档内的秩。"
"若有 alpha,最可能来自:休眠 / 被忽视的一档(Merton 1987;Lesmond 等 1999 的零交易溢价)本身,或者小票内部越稳定的成交越被忽视。为什么样本外还会在:Z4 是四层 40 日窗口,记忆约 160 个交易日,每天几乎不变,换手低;来源是慢变的参与者结构,不依赖某一段行情。"
"数学检查:Z4 是 ts_std 的叠加,非负、有限;无除法,没有近零分母;log 只作用于 Z4(正,窗内全常数时为 0 → NaN 不填充)与 60 日均成交额(正);cs_last_* / cs_first_* 的输出是 y 的截面秩加 ±1(整块并列);cs_bucket_rank 在 x 的十档内取秩;零成交占比 ∈ [0,1];没有 ts_rank / cross_rank,不触发 nanrank_last;没有用到当天收盘之后的数据;Z4 在上市不久的票上由少数点估计(滚动算子无最小样本数),这类票的带位置不稳,但不是系统性缺失。")
hyp_n=("事实(快照):已出的 head 把「休眠度」读成成交额波动的波动(Z2 / Z3 / Z4,元量级的水平)再最低一档沉底;该族与成交额水平、市值高度纠缠。第 1 轮 N 位(量增长半标准差)最好 +0.41,第 2 轮的 P120 E 位 0 个 head。B087(pow_2(ts_max(日收益)))一族在新尺子下全是负的(-0.57 ~ -1.37),彩票型 MAX 效应被尺子吃掉,不是线索。"
"本位的新想法:从价格路径一侧度量休眠度,而不是成交额一侧。分钟级价格停滞 —— day_flat_ratio(Close)(当日收盘价序列里相邻分钟不变的比例)、day_flat_run_max(Close)(最长连续不变段)、day_distinct_ratio(Close)(不同价位数 / 分钟数,低 = 休眠)—— 取 60 / 120 / 241 日均值,衡量一只票有多少时间「价格不动」。它度量的是价格发现的稀疏度(Lesmond 等 1999 的零收益占比的分钟版),不含成交额的元量纲,也不是成交额的二阶波动;库里 5583 条没有一条用 day_flat_* / day_distinct_*。"
"算子怎样实现:(i) 连续:停滞度的滚动均值本身(种子 1 ~ 3),(ii) 去掉与已知量的重叠:对市值十档内取秩(7)、对零成交占比逐日截面回归取残差(8)、短期相对长期(9);(iii) 阶跃带:最停滞的 10% 沉底 / 20% 浮顶,带外排序用市值 / 量增长下行半标准差 / 120 日收益(4 ~ 6);(iv) 另外 4 个把「成交额二阶波动」换成日内分钟成交额的离散(day_std(Amt) / day_max(Amt))再套 cs_last_low10,与停滞度互为带和排序(10 ~ 13),检验承重的是成交额一侧还是价格一侧的休眠度。"
"为什么与 head 不同:head 的底是 day_mean(Amt) 的嵌套 ts_std;本位的底是价格路径的稀疏度,以及日内成交额的分布形状,骨架不同、量纲不同(比例,无量纲)。与 head 的 |ρ| 来自共享的休眠名字(预计 0.2 ~ 0.5)。"
"若有 alpha,最可能来自价格发现稀疏的票(涨跌停板反复触板、长期无报价变化)的流动性 / 被忽视溢价。为什么样本外还会在:60 ~ 241 日的慢变量,换手低;结构来自市场微观结构(涨跌停制度、散户为主),不依赖某段行情。"
"数学检查:三个日内量都是 [0,1] 比例,有界;停滞度在涨跌停一字板日接近 1,这是真实状态不是伪影;day_distinct_ratio 在停牌日(分钟全缺失)为 NaN,滚动均值按可用日算(窗内有效点少的票不稳,不是系统性);无除法、无 log 近零;cs_regres 是逐日截面回归残差;day_std(Amt) / day_max(Amt) 有限;没有 ts_rank / cross_rank,不触发 nanrank_last;没有用到当天收盘之后的数据。")
plan=dict(seed=2029,round=3,slots=[
 dict(type="E",core=Z4,hypothesis=hyp_e,literature=lit_e,seeds=e1),
 dict(type="N",hypothesis=hyp_n,inspired_by="第 1 轮 6 个 head 的共同点(最低一档休眠度 + 成交额波动的波动,D 尺子下仍 +1.25)与 B087 一族被尺子吃掉的现象;改从价格路径度量休眠度",literature=lit_n,seeds=n)],
 R=[dict(head="cs_last_low10(sub(ts_std(log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)), 40), LogFloatCap), log(ts_std(ts_std(ts_std(day_mean(Amt), 40), 40), 40)))",
  why="拆解表:去掉 y 里的 -LogFloatCap 后 train -1.17 / valid +0.42(必要性 +2.41),换成 y 内部的其他项分数几乎不变;所以 y 里 LogFloatCap(浮动市值)是承重部件。这里检验承重的是流通市值、总市值还是价位(LogFloatCap - LogFloatShares),以及被标记集合 x 用 Z4 / Z2 代替 log(Z3) 是否更好。四个变体各只动一处,数学上都是同量纲的对数或同一族的水平,没有新引入除法。",
  variants=rv)])
yaml.safe_dump(plan,open("missions.yaml","w"),allow_unicode=True,width=10000,sort_keys=False)
