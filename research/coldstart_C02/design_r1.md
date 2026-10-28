# C02 第 1 轮:初始种群与先验的设计说明(W2,主研)

指引文件 **`guidance/C02_r1.yaml`**(`scripts/c02_check.py guidance` → ADMISSIBLE:2 个 idea、15 条先验、24 个种子,exit 0)。
依据:`research/coldstart_C02/direct_r1.md` / `.json`(B 组直接检验 64 个表达式,已从 B 组预算里扣)、`research/coldstart_C02/prior_c01.md`、C01 的样本内材料(`beliefs_r3.md`、`episodes/c01*/evidence.json`)。

**口径**(两组相同):奖励 `long`,score = train 与 valid 较差的那个,**发现 = score ≥ 0.7**;与已知族 `cross_mean(day_std(Amt), 30)` 实测 |ρ| ≥ 0.5 判不合格;禁 `ts_spearman` 与全部 `nt_*`;终局只认与 C01 的 48 个 head 都 |ρ| < 0.7 的「新」东西。
**预算**:每个随机种子 **184 次** = 192 − ⌈64/8⌉,population 48,`--seed-share 0.5`(种子最多占初代 24 个)。
**分配**:`C2a_slow_intraday_reversal` → 401, 402, 403, 404;`C2b_return_shape_and_tug` → 405, 406, 407, 408。

## 为什么是 2 个 idea

直接检验已经把 H1/v4 `cross_ema(log(div(day_last(Close), day_first(Open))), 30)` = **+0.975** 这个发现拿到手了,再拿 8 次运行精修它,最多把这一个 head 变好。锦标赛选择下 0.8–1.0 分的种子会占掉大半繁殖位(前 8 名约 43%),弱种子得不到精修。所以 4 次运行(401–404)专门精修反转并试它的近亲,4 次(405–408)**不放反转锚**,只测正交机制。两个 idea 的 `grammar` 都留空 `{}`:C01 证明 `day_ops` 的 must-contain 会被装饰性满足(一个无关算子挂在树上就算满足)。**不放对照种子**:idea 里出现的算子被提权 ×8,对照种子只会让「已知是坏的」那一族被多抽,白花评估。

## 记号

`I` = `log(div(day_last(Close), day_first(Open)))` 盘中段对数收益;`O` = `log(div(day_first(Open), ts_delay(day_last(Close), 1)))` 隔夜;`D` = `log(div(day_last(Close), ts_delay(day_last(Close), 1)))` 整日(收盘到收盘)。

直接检验顺带定下一件事:H2/v3 与 H1/v2 读数完全相同只差方向,H2/v6、v7 因取值是常数被门槛废掉 —— 所以**首分钟 `Ret` ≡ 0、首分钟 `Close` = `Open`**(集合竞价那一笔),`Ret` 不含隔夜跳空(C01 的 B7 问题就此回答),盘中段从 `day_first(Open)` 量起是对的。分钟轴 241 根:0 = 集合竞价,1–120 = 上午,121–240 = 下午,所以 `day_last(in_delay(Close, k))` 是 15:00 前 k 分钟的价:k=30 → 14:30,k=120 → 11:30(上午收),k=180 → 10:30。

## C2a:慢的盘中反转,13 个种子(improve 4 个,4×3 = 12 ≤ 13)

| # | 角色 | 表达式 | 出处与读数 | 为什么放 | 预期它的后代 |
|---|---|---|---|---|---|
| 1 | improve | `cross_ema(I, 30)` | H1/v4:score **+0.975**(train 0.99 / valid 0.98),sign −1,hl 5,换手 0.038,ρ 0.30 | 锚与父代:唯一在样本内成立的机制,等权 30 日 0.84/0.86、等权 50/60 的 train 约 1.0 但 valid 掉到 0.42/0.44,所以平滑核要「近期权重大、无窗口截断」 | 半衰期在 {3,5,10,15,60,241} 上重试(dt 网格),与 2–8 号交叉出「换过时段的 EMA 反转」;预期本族至少 1 个 ≥ 1.05 |
| 2 | improve | `cross_ema(log(div(day_last(in_delay(Close, 30)), day_first(Open))), 30)` | H5 全盘被否:收盘 30 分钟累积收益在选中方向下 train −1.17 / −1.13,残差 −1.74,错时段对照只有 −0.37 | 收盘段对反转是噪声,剔掉它应当更干净 —— 这是 H5 的失败给 H1 的唯一可用推论 | 把截断点在分钟网格上挪(14:57…14:00),预期 ≥ 锚 −0.05;若明显高于锚,说明尾盘噪声是 H1 的主要损耗 |
| 3 | improve | `cross_ema(log(div(day_mean(Close), day_first(Open))), 30)` | H1/v1 与 v7 读数相同(0.838 / 0.838)说明口径稳;v8 按分钟波动归一 0.60/0.72 | 开盘到**日均价**:用全天均价代替一个时点,抗单点噪声,且与 H3 的「成交额加权」不同 —— 这里是等权 | 与 1、7 号组成「终点取哪个价」的一族;日均价版若赢,说明读的是全天位移而不是收盘时点 |
| 4 | improve | `cross_ema(log(div(day_last(in_delay(Close, 120)), day_first(Open))), 30)` | 同上;H6 的注意力冲击在 train 被否(−0.18 / −0.83),所以不靠量来分时段 | 只取**上午段**(9:30–11:30):散户集中下单在开盘,冲击与回吐应集中在上午 | 与 6 号一起判「回吐是不是开盘的集中下单」;预期上午段 ≥ 午后段(5 号) |
| 5 | new | `cross_ema(log(div(day_last(in_delay(Close, 30)), day_last(in_delay(Close, 120)))), 30)` | 新;时段切分的另一半 | **午后段剔收盘**(11:30–14:30):机制陈述的证伪腿,它若赢则「开盘集中下单」的说法要改写 | 与 4 号配对读;两段都 ≥ 0.7 则反转不挑时段,是全天的流动性对价 |
| 6 | new | `cross_ema(log(div(day_last(in_delay(Close, 180)), day_first(Open))), 30)` | 新 | **开盘一小时**(9:30–10:30):冲击最浓、信息最少的一段 | 窗口变异会把它拉到 dt 网格(见「已知的两处损耗」);它与 1 号的 ρ 是本轮判「时段切分有没有独立信息」的关键 |
| 7 | new | `cross_ema(log(div(day_last(Close), day_mean(Close))), 30)` | 新;H5 被否说明「尾盘绝对收益」没用,但「收盘相对日内均价」没测过 | 收盘价相对**当日均价**的位置:无量纲、与开盘价无关,把 H5 的时段问题换成位置问题 | 与 3 号互补(3 号量起点,7 号量终点);若两者都过线且互相 ρ < 0.7,是两个 head |
| 8 | new | `cross_ema(log(div(mul(day_last(Close), day_last(Close)), mul(day_max(High), day_min(Low)))), 30)` | 新;H1/v13 振幅对照被 ρ 拒(0.534),但**位置**不是**宽度** | 日内区间位置(收盘在 [Low, High] 里的几何位置,写成比值所以无量纲):振幅被拒的是水平,位置应当不含波动 | 若它过线而 12 号不过,说明反转读的是「收在哪」而不是「走了多远」 |
| 9 | new | `ts_scale(sqrt(day_mean(Low)), 30)` | **C01 的近失**:`c01r3s302A` 存档里 score +0.838(train 0.860 / valid 0.838),sign −1,hl 20,换手 0.039,**ρ已知 0.106** —— C01 门槛是 1.0 所以没成为 head,按 C02 的 0.7 它本身就是发现 | 价格相对自身 30 日水平(`ts_scale` = x[t] ÷ 窗口和):另一条慢反转路径,与 H1 的 ρ 未知,是本轮最大的不确定之一 | 与 10、11 号组成「多日价格位置」一族;若它与 1 号 ρ ≥ 0.7,则 H1 只是它的日内版本,终局只记一个 head |
| 10 | new | `log(div(day_last(Close), cross_max(day_max(High), 60)))` | 新;C01 的 104/107 族全是刻度与离散度,没有「距高点」 | 距 60 日高点的距离:52 周高点效应的短版,无量纲 | 窗口在 dt 网格上重试(3…241);与 9 号的 ρ 决定它是不是同一个读数 |
| 11 | new | `log(div(mul(day_last(Close), day_last(Close)), mul(cross_max(day_max(High), 20), cross_min(day_min(Low), 20))))` | 新;8 号的多日版 | 20 日区间位置:把 8 号的日内位置拉到一个月,检验「位置」这个量在哪个尺度上有信息 | 与 8 号配对;两者都过线说明位置效应跨尺度,只有一个过线说明尺度是机制的一部分 |
| 12 | new | `cross_ema(div(I, day_sum(abs_(Ret))), 30)` | H1 的消融留下的疑问:对振幅取残差后 v12 是 0.64/0.22、按振幅归一 v11 是 0.43/1.03、按分钟波动归一 v8 是 0.60/0.72 —— valid 段的多头表现有一块和振幅共振 | 按**日内路径长度**归一的盘中趋势(位移 ÷ 路程):去掉波动量纲的反转,正好回答 v12 留下的问题 | 它是本卡的「不是波动代理」判据:若它过线且 ρ已知 < 0.35,机制陈述里的波动倾斜就被排除;若它远低于锚,反转的那一块确实靠振幅 |
| 13 | new | `ts_skew(D, 40)` | H7/v3:train +0.47 / valid +0.54,sign −1,ρ 0.18,换手 0.049 | 正交原料,不是来精修的:让交叉能拼出「反转 × 偏度」这种 1 号自己到不了的树 | 若本卡唯一过线的新种子是它,按 `fails_if`(e) 记 C2a 不成立 —— 那是 C2b 的机制 |

## C2b:收益形状与隔夜—盘中拉锯,11 个种子(全部 new)

| # | 表达式 | 出处与读数 | 为什么放 | 预期它的后代 |
|---|---|---|---|---|
| 1 | `ts_skew(D, 40)` | H7/v3 train +0.47 / valid +0.54,ρ 0.18,换手 0.049(拖累约 3.7%/年,毛约 6.2%) | 父代:直接检验里**唯一**方向对、两段都为正、只被成本卡住的非反转读数。MAX 本身 −0.38(ρ 0.43)、MAX/σ −0.67、波动对照被 ρ 拒 −0.95,所以形状量和波动被对照区分开了 | 窗口在 nd 网格 {1,5,10,20,30,50} 上重试;预期通过者 sign −1(做多低偏度) |
| 2 | `cross_ema(ts_skew(D, 40), 15)` | 同上 | **慢化**:0.7 的门槛下 0.049 的换手正好是差额,把换手压到 ≤ 0.04 就够过线。C01 的 B15 也说慢形式是这一族唯一的指望 | 半衰期在 dt 网格上重试;若慢化后分数不升,说明换手不是瓶颈,是信号本身弱 |
| 3 | `ts_skew(I, 40)` | 新;H1 说明盘中段与隔夜段性质不同 | 只取盘中的收益形状:分辨彩票形状来自连续竞价还是集合竞价 | 与 1、4 号三选,预期最强的那个指出形状溢价的来源 |
| 4 | `ts_skew(O, 40)` | H2 的隔夜**水平**被否(v1/v4/v5 在 train 选出的方向下 −0.6 ~ −0.9,残差 −2.79),但**形状**没测过 | 隔夜只作无量纲原料进本卡,不再测它的水平 | 若 4 号过线而 1、3 号不过,机制改写成「集合竞价里的彩票偏好」 |
| 5 | `ts_kurt(D, 40)` | 新 | 厚尾与偏度不是一件事:偏度买右尾,峰度买「两边都有尾」;放它是为了让 GP 能用 `sub`/`div` 把两者拼起来 | 与 1 号的 ρ 决定它是不是偏度的翻版 |
| 6 | `ts_corr(O, I, 40)` | 新;H2 两段相减 v2 只有 0.07、残差 −2.79,说明两段**相减**没用,但**相关**没测过 | 拉锯:长期负相关的票是被反复高开低走的情绪票,T+1 下这正是隔夜买盘被盘中修正的签名 | 窗口与两条腿的时段都会被变异;预期 ρ已知 < 0.3(两条腿都是比值) |
| 7 | `ts_corr(ts_delay(I, 1), O, 40)` | 新 | 错位一天的拉锯:今天的隔夜跟**昨天**的盘中是不是反的 —— 把「同日两段的会计恒等」与「跨日的情绪传导」分开 | 与 6 号配对;6 过 7 不过说明是同日的机械修正,两者都过说明有跨日传导 |
| 8 | `log(div(ts_std(O, 40), ts_std(I, 40)))` | 新 | 隔夜方差占比:高 = 信息集中在盘后公告,低 = 波动来自盘中交易。用比值写,两个量纲约掉 | 这是本卡里最可能撞 ρ已知 的一个(波动之比);若它被 ρ 拒,按 `fails_if`(e) 记 |
| 9 | `ts_pearson(day_skew(Ret), 50)` | **C01 的 Spearman 孪生**:`c01r2s206B` 存档里 `sub(1, ts_spearman(day_skew(Ret), 50))` score **+0.795**(train 0.795 / valid 1.919),sign −1,hl 5,换手 0.036,ρ已知 0.145;C02 禁 `ts_spearman`(逐只 Python 循环),`ts_pearson` 是向量化替身 | 同步性:日内形状跟着全市场走的票散户错价少。注意这是与彩票形状**不同的机制**(C01 的 B 组自己也这么判),所以放在 C2b 而不是当 1 号的近邻 | **必须含 `Ret` 叶子**,否则后代被 C2P5a 全挡(先验只放过含 Ret 的 `ts_pearson`);终局要专门核它与 C01 的 4 个 `ts_pearson(day_sum(Close))` head 的 ρ |
| 10 | `ts_pearson(day_sum(Ret), 30)` | 新;9 号的「水平」版 | 收益本身的同步性(β 的无量纲代理),与 9 号的「形状同步性」分开 | 同 9 号;两者 ρ ≥ 0.7 则只记一个 |
| 11 | `cross_corr(I, ts_delay(I, 1), 60)` | 新;H1 测的是盘中收益的**水平**,没测它的**持续性** | 盘中收益的日自相关:反转机制预测它为负,而「自相关有多负」本身可能是比收益水平更干净的排序量 | 它是 C2a 与 C2b 之间唯一的概念桥;若它与 1 号(C2a 的锚)ρ ≥ 0.7,按 `fails_if`(c) 记 C2b 没有独立贡献 |

## 不放什么

- **H2 的隔夜水平、H3 的成交额加权、H4 的日内价量相关、H5 的尾盘拉升、H6 的注意力冲击**:核心变体在 train 上都为负或接近零,残差腿全为负。train 是约束条件,按失败处理。
- **被 ρ 拒的 5 个**(H1/v13 振幅 0.534、H2/v11 跳空绝对值 0.515、H4/v5 价量相关的波动 0.548、H5/v6 尾盘成交额占比 −0.504、H7/v5 日收益波动 0.512):它们全是波动或流动性的代理,放了也只会被判不合格。
- **对照变体同样过线的写法**:H3 的安慰剂(权重换成 3 日前同一分钟的成交额)在 valid 上 +0.56 / +1.34,核心的残差反而为负 —— 这一族剩下的是透过成交额看到的 H1 加流动性倾斜,不独立。
- **含 `day_first(Ret)` 的写法**:它只是 `−day_sum(Ret)` 换个写法(首分钟 Ret ≡ 0)。

## 15 条先验,各挡什么

| id | 动作 | 挡什么 |
|---|---|---|
| C2P1 | weight 0.3 `@flow` | 含 Amt/Volume 叶子的树。H3/H4/H6 共 27 个变体 0 发现、2 个被 ρ 拒;C01 含流动性叶子的通过者里低 ρ 只占 2.2%。不禁(H3/v1 量只作权重,train 0.51) |
| C2P2 | ban | `day_distinct_ratio` / `day_zero_ratio` / `day_flat_ratio` / `day_flat_run_max` —— C01 104 族的签名,48 个 C01 head 里 13 个含它,按 PLAN §3 不算新 |
| C2P3 | ban | `{day_std|day_var}(@price)` —— 名义股价 × 波动,104/107 族的第二个核。`day_std(Ret)` 不在内 |
| C2P4a/b | ban | `cs_first_*` / `cs_last_*` / `cs_mask_*` —— 已知族穿过 0.5 闸的主要洗白路径(C01 B13:去掉筛选后 ρ 0.81) |
| C2P5a–d | ban | 价格水平上的 `ts_pearson`(C01 的 head 族,1.4–2.0,会在 C2b 里抢繁殖位):a 要求树里有 `Ret`,b 直接写法,c 一层单调包装,d 嵌套或先平滑 |
| C2P6 | ban | `{day_kurt|day_skew|day_hurst|day_autocorr_n1}(@price)` —— C01 的价格路径形状 head 族。`day_skew(Ret)` 照常可用(C2b 的 9 号要用) |
| C2P7a/b | ban | 名义股价水平(裸写法与一层包装),只放过含 `div`/`ts_scale`/`cross_scale`/`ts_skew`/`ts_kurt`/`ts_rank`/`cross_rank` 的树 —— C01 那个 0.54、ρ 0.42、从不过线的吸引子 |
| C2P8 | family 0.3 | 只换价格字段的兄弟树(H1/v1 与 v7 读数完全相同就是证据) |
| C2P9a/b | ban | `div($w, _)` 与 `div(_, $w)` —— 倒数或缩放,截面排序不变,还是 1/股价穿过 C2P7a 的 unless 的写法 |

没有 w > 1 的规则,`w_ref = 1`。C2P1、C2P5a、C2P9a/b 都带 `unless`,因此不会被折叠成对叶子无效的算子权重(`steer.py` 的 `operator_weights` 跳过带 unless / 带上下文的规则);折叠进算子权重的只有 C2P2 和 C2P4 列出的那些算子名。

## 本机核对(主研,无数据无 GPU)

- `scripts/c02_check.py guidance guidance/C02_r1.yaml` → **ADMISSIBLE**,2 ideas / 15 priors / 24 seeds,exit 0。
- 24 个种子都能按搜索语法解析(与 `idea_search.py` 同一个 `parse(G.canonical(s), strict=True, coerce_daily=True, n_minutes=241, allow_general=True)`),**都不被本文件的先验禁掉**(weight 全 1.0),深度 4–8 ≤ `seed_max_depth` 9,`canonical` 不改写任何一条。
- 两个 idea 内 `skeleton_key` 各不相同(`gp.py` 的 `_seeded_population` 对同骨架只留一个;骨架认算子与窗口、不认字段),所以 13 和 11 个种子会全部进初代(`seed_keep = min(n, 48×0.5) = n`)。
- 400 次生成模拟(steer 臂的算子权重 + boost 8 + 本文件的 accept):每棵接受的树 **2.49–2.65** 次提议,返回的树 **0 棵**被禁,没有一次走到不经先验的回退生成;含量叶子的树 **21–25%**,同一代码不带先验的对照是 **38–41%**。
- 种子的 `mutate_subtree` / `mutate_operator` / `mutate_window` / `mutate_hoist` 各 25 次、以及种子两两交叉,产出的后代**没有一个**被先验禁掉(少数返回 None = 变异点不可用)。

## 已知的两处损耗(不改种子,先记下来)

1. `in_delay` 是 dt 面,窗口网格是 {3,5,10,15,30,60,241},**120 和 180 不在网格上**。所以 4、5、6 号的 11:30 / 10:30 切分只靠交叉与子树变异保留,窗口变异会把它们拉回网格。600 次窗口变异的模拟里有 26 次(约 4%)产出 `in_delay(_, 241)` —— 整日平移、取值全 NaN,会在覆盖率 0.9 的门槛上废掉一次评估(直接检验里 H2/v6、v7 就是这么废的)。代价小,换来的是「上午段 / 开盘一小时」这两个按机制挑的切分点。
2. C2b 的 `ts_pearson` 被提权 ×8,而 C2P5a 又挡掉不含 `Ret` 的 `ts_pearson` 树,所以 C2b 的提议里约 45% 落在禁区(被禁 446–460 / 约 1030 次提议)。这只花 CPU、不花付费评估(accept 在打分之前),是这个机制的设计代价。

## 终局要专门核的三件事

1. **9、8、4 号与 H1 锚的 ρ**:价格相对 30 日均价(C01 近失 0.838、ρ已知 0.106)、日内区间位置、上午段 —— 它们是不是独立的 head,这一轮完全未知,是本设计最大的不确定。
2. **C2b 的 `ts_pearson` 通过者与 C01 的 4 个 `ts_pearson(day_sum(Close))` head 的 ρ**:≥ 0.7 就不算新(`fails_if`(d))。
3. **H1 族与 C01 的 head `cs_first_low20(day_open(Amt), day_pos_ratio(Ret))`(+2.25)的 ρ**:那个 head 也读盘中方向,是 H1 最可能撞上的 C01 head。

## 审计自报(主研)

- 读了:`research/coldstart_C02/`(PLAN.md、prior_c01.md、direct_r1.md、C02 基线指引、总领的草案)、`guidance/C02_base.yaml`、`scripts/c02_check.py`、`scripts/c02_jobs.py`、`scripts/idea_search.py`、`partura/steer.py`、`partura/ac_plugin.py`、`partura/ops_ext.py`(cross_ema)、AlphaCube 的 `generator.py` / `gp.py` / `clustering.py` / `catalog.py` / `operators/nd_ts.py` / `operators/dt_in.py`。
- C01 的样本内材料只读了:`beliefs_r3.md`(B15、B12、B13 与对 `ts_pearson(day_skew(Ret), 50)` 的那条判断)、`episodes/c01r3s302A_*/evidence.json` 与 `episodes/c01r2s206B_*/evidence.json` 里两条具体读数(按表达式过滤,没有通读)。
- **没有**读 `research/coldstart_C01/RESULT.md`、`final*.json`、`ledger_c01.json`,也没有读 `runs/`、`lab/`、`notes/`、`studies/`、`handoff/`、`batches/`、`docs/`,没有碰任何 C02 A 组的东西(`episodes/c02r*s*A_*`)。
- 一处要如实说明:为核对两条 C01 读数,我在 `research/coldstart_C01/` 下跑过一次 `grep -rn`,它递归到了该目录下的禁读文件;两个模式都没有在那些文件里命中,返回给我的 5 行全部来自 `beliefs_r3.md` 和 `round3_workflow.json`(事后用 `grep -o '^文件名:'` 在保存的输出上核过)。之后的检索都按文件名限定在允许的材料上。
- 只写了两个文件:`guidance/C02_r1.yaml` 和本文件。没有改代码、没有改 PLAN、没有跑服务器、没有 git commit。
