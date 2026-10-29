# 结构解剖:种子 808,B 组,第 1 轮

快照只有 `c05s808M1_I0_open_search`:**0 个 head**、91 个已评分候选、拆解 0 次评估、R 候选 0 个。
证据等级要先说清楚:本轮**没有任何充分性 / 必要性 / 敏感性的实测**(拆解表为空,因为没有 head 可拆),
唯一的实测证据是共性(enrichment)那 7 行。下面凡是推断,都标了「推断」。

---

## 1. alpha 的来源

### 1.1 七行共性其实是一行:同一个静态字段

共性表的 7 个子树全部是 `LogFloatShares` 的单字段包装:

`inv(LogFloatShares)`、`ts_decay_linear(LogFloatShares, 50)`、`abs_(LogFloatShares)`、
`log(LogFloatShares)`、`ts_max(LogFloatShares, 50)`、`log(inv(LogFloatShares))`、`pow_2(LogFloatShares)`。

这不是 7 个发现,是 1 个。理由是机制上的,不是统计上的:

1. **奖励只看横截面秩。** `partura/steer.py` 的 `long_neutral`:每个半衰期先 `bk.smoothed(raw, hl)`,
   再 `neutral_residual(...)`,而 `neutral_residual` 第一步就是 `dg._zrank`(`partura/diagnose.py:190`,把每天的值换成 [-0.5, 0.5] 的秩),
   然后在秩空间里减掉控制的投影。`ctx.halflives=(0.0, 5.0, 20.0)`,`sign` 在 ±1 里取 train 夏普更大的那个。
   所以**当 hl=0 被选中时,任何严格单调(含单调递减)变换给出的 score 完全相同**。
2. **这 5 个一元算子在本字段上就是严格单调的。** `LogFloatShares = log(FloatShares)`(`alphacube/dailyfields.py:57`),
   A 股流通股本恒为正且远离 0(同一文件注释给的量级:cap 1e9–1e13 时 `log(cap)` 只有 ~21–30),
   所以 `inv(x)=1/x`(`operators/common.py:191`)、`abs_(x)=|x|`、`log(x)=log|x|`、`pow_(x,2)`、`log(inv(x))`
   在这段定义域上都是严格单调的 → 秩恒等或恒反 → score 相同,`sign` 自动吸收方向。
3. **两个窗口归约在静态字段上近似等于水平值。** `ts_decay_linear(·,50)` 是 50 日线性加权均值(`operators/common.py:602`),
   `ts_max(·,50)` 是 50 日最大值;流通股本只在解禁 / 增发 / 回购 / 送转这种离散事件上跳变,
   绝大多数票 50 天内不变,所以两者的横截面秩 ≈ 水平值的秩(推断,但下面的数字支持它)。

### 1.2 数字自己证明了这一点

| 子树 | n_with | mean_with | mean_without | 均值差 | p |
|---|---|---|---|---|---|
| `ts_decay_linear(LogFloatShares, 50)` | 5 | 0.4857 | −0.5154 | +1.0011 | 0.003 |
| `abs_(LogFloatShares)` | 4 | 0.4811 | −0.5037 | +0.9848 | 0.051 |
| `log(LogFloatShares)` | 4 | 0.4792 | −0.5036 | +0.9828 | 0.060 |
| `inv(LogFloatShares)` | 14 | 0.4755 | −0.6305 | +1.1060 | 0.010 |
| `log(inv(LogFloatShares))` | 4 | 0.4690 | −0.5031 | +0.9721 | 0.382 |
| `pow_2(LogFloatShares)` | 4 | 0.4686 | −0.5031 | +0.9716 | 0.442 |
| `ts_max(LogFloatShares, 50)` | 5 | 0.4653 | −0.5142 | +0.9795 | 0.596 |

三件事:

- **一致性校验**:7 行各自反推出的全档均值都是 **−0.4604**(例如 inv:(14×0.4755+77×(−0.6305))/91 = −0.4603),
  说明这张表内部自洽,n_archived=91 的口径没问题。
- **簇宽 0.02**:7 组的 mean_with 全落在 **0.4653 ~ 0.4857**。7 种不同写法、91 个候选、均值差距 0.02 —— 这是同一个因子的签名。
  而且**整簇都卡在发现门槛 0.5 之下**(最高 0.4857),这就是本种子 M 第 1 批 0 个 head 的直接原因。
- **p 值在这里不能用来排序**。表格按 mean_with 降序排,p 恰好单调递增(0.003 / 0.051 / 0.060 / … / 0.382 / 0.442 / 0.596;
  `inv` 那行 p=0.010 是因为 n=14 功效高)。原因在 `scripts/c05_locate.py` 的实现:
  `mannwhitneyu(w, wo, alternative="greater")` 的 `wo` 里**装着同簇的其他候选**(比如 `abs_` 那行的 87 个「不含」里就有 14 个含 `inv` 的)。
  所以 p 衡量的不是「这个子树好不好」,而是「这 4–5 个候选在同簇内部排第几」。
  机械核心卡按 p<0.1 筛、按均值差排,排出来的顺序没有实际含义。

  正态近似反推 U 统计量可以把簇的规模量出来(推断):score ≈ 0.4857 的候选打败约 87% 的其余候选,
  score ≈ 0.4653 的只打败约 47% —— 也就是说 **0.4653–0.4857 这条 0.02 宽的带里躺着约 35–40 个候选,占 91 个的四成左右**;
  剩下约六成的均值大约在 −1.07。M 第 1 批的 192 次预算里,大约三分之一花在反复重新发现同一个静态特征上。

### 1.3 为什么 GP 会掉进去:量纲

这不是随机的。`LogFloatShares` 的取值量级是 **~20**,而 `day_std(Ret)` 之类是 ~1e-2,`day_sum(Amt)` 是 ~1e7。
任何 `add` / `sub` 把 log 规模字段和收益类字段混在一起,结果的横截面秩就几乎完全由规模字段决定;
`mul` / `div` 里它又只是一个变化范围不到 2 倍的近似常数乘子。
所以「树里出现了 `LogFloatShares`」在加减结构里等价于「这棵树就是 `LogFloatShares`」。
**这是种子设计的第一条硬约束**:要让另一个字段真正进来,必须在秩空间里组合(`cs_rank` / `cs_normalize` / `cs_regres`),
或者用三个 log 字段**相减**把 ~20 的水平抵消掉。

### 1.4 真来源到底是什么:名义股价,还是规模的代理

奖励的控制里已经有 `LogFloatCap`(`scripts/c05_locate.py` 的 `n_size`,和 liq、`cross_mean(day_std(Ret), 20)`、
20 日反转、已知族一起进 `neutral_basis`,**秩空间线性**)。所以 `LogFloatShares` 能留下来的,只能是它正交于 `LogFloatCap` 的那部分。按定义:

- `LogFloatCap − LogFloatShares = log(未复权股价)` —— 流通市值 = 股价 × 流通股本,取 log 相减价格就显形了。
- `LogTotalCap − LogFloatCap = −log(自由流通比例)` —— 价格精确抵消,剩下总股本/流通股本。

于是本轮共性那一簇的身份有两种可能,**本轮的证据分不开**:

**(a) 名义股价(低价股效应)**:市值被中性化后,流通股本的残差主要是 −log 股价。这是 A 股一个独立且有文献的风格。
**(b) 规模的另一种写法(代理)**:中性化是**秩空间的线性**投影,挡不住规模的**非线性**暴露(例如只有最小市值那一两档才有的溢价)。
`LogFloatShares` 与 `LogFloatCap` 的秩相关很高,残差里会漏出规模的非线性部分。

一个旁证支持 (a) 可做:`alphacube/daily.py:25` 的注释说**价格字段是后复权的,而 `Amt` / `Volume` 是原始的**
(`Amt/Volume` 的中位数只有后复权 `Close` 的 0.108 倍)。所以 `div(day_sum(Amt), day_sum(Volume))` 是**未复权均价**,
而后复权的 `day_last(Close)` 不是 —— 名义股价这条轴在本环境里只能通过 `Amt/Volume` 或者三个 log 字段相减拿到,
GP 在这 91 个候选里**一次都没有把两个字段组合起来**,所以它从来没真正试过这条轴。
顺带:`log(day_last(Close)) − (LogFloatCap − LogFloatShares)` = log 累计复权因子,是累计分红送转的痕迹,也是同一条路上的免费特征。

**结论(1):真来源是一个静态横截面特征 —— 流通股本,其中能过控制的那一部分;最可能的身份是名义股价轴 +(或)规模的非线性残差。
它不是一个新机制,属于已知风格,而且有相当的「只是代理」的风险。本轮的任务应该优先把这两者分开,而不是接着在同一个水平轴上做包装。**

---

## 2. 烂部件

本轮没有 head,**所以没有必要性数字**(跳一个算子掉多少,一次都没测)。能说的只有共性口径下的:

- **所有作用在静态字段上的单调一元包装都是烂部件**:`inv`、`abs_`、`log`、`pow_2`、`log∘inv`。
  按 §1.1 第 1–2 点,它们在 hl=0 下对 score 的贡献**精确为 0**;实测的簇宽 0.02 也只有这个量级。
- **50 日窗口归约在静态字段上同样是烂部件**,其中 `ts_max(LogFloatShares, 50)` 是全簇最差(0.4653),
  `ts_decay_linear(LogFloatShares, 50)` 最好(0.4857)—— 但这 0.02 的差距按 §1.2 不可解读,别当成信号。
- 推论给以后:**任何后来出现的 head,如果它在某个静态字段(`LogFloatCap` / `LogTotalCap` / `LogFloatShares` / `ListAge`)
  外面套了单调一元算子,那一层一定是 R 的第一目标** —— 去掉它不会掉分,却能把深度预算省给真正的外围。

### 本轮 R 在代码层面不可能,别写

- `scripts/c05_check.py`:`heads = {h["expr"] for h in loc["heads"]}` 是空集,任何 `R` 条目都会报
  `R i: the head is not in the snapshot` → NOT ADMISSIBLE。
- `scripts/c05_locate.py` 的 `direct` 模式同样会 `SystemExit("R requests name heads outside the snapshot: ...")`。

所以本轮 **R = 0**(写 `R: []` 或干脆不写)。代价要记进笔记:48 次拆解 + 16 次 R 共 **64 次评估本轮必然浪费**
(PLAN §2.3「用不完的不挪用」),B 本轮实际只花 192 次,而 A 组花满 256 次。第 1 轮 B 组是**结构性吃亏**的,
这一轮的目标不是赢,是把第 2、3 轮的拆解预算喂上 —— **本轮只要产出 1 个 head,第 2 轮的 48 次拆解就能用起来**。

---

## 3. 之前的任务

第 1 轮,`missions_before` 为空,没有可核对的东西。

**留给第 2 轮核对的预测**(本轮写下,下轮打分):

- **P1**:只在同一个静态字段上做单调包装 / 单字段窗口归约的候选,score 会继续落在 **0.46–0.49**,不会过 0.5。
  本轮若 E 位产出 head,它的表达式里**一定含第二个字段,或者一个对同一字段的差分**。
- **P2**:`sub(LogTotalCap, LogFloatCap)`(自由流通比例,价格精确抵消)单独评估的 score **低于** `sub(LogFloatCap, LogFloatShares)`(名义股价),
  且前者在 0.1–0.5 之间。—— 这条直接判定 §1.4 的 (a) 还是股本轴。
- **P3**:纯事件差分(例如 `sub(LogFloatShares, ts_decay_linear(LogFloatShares, 50))`)**会被闸门挡掉**:
  大多数票 50 天内股本不变,差分恰好为 0,`dg.distinct_fraction`(唯一值数 / 有值股票数的中位数)远低于 0.5
  → `gate=False`、无 score。必须乘进一个连续载体才能评估。
- **P4**:E 位 32 个初代里,Partura 手写种子的 score 分布会**明显高于**机械嫁接补满的那部分(这一条检验「写种子」有没有用)。

---

## 4. 本轮候选

### 4.1 可用的核心只有 7 个

`scripts/c05_check.py` 的 `known` 集合 = {快照 heads 的全部子树 key} ∪ {`loc["enrichment"]` 的子树} ∪ {`core_cards`}。
heads 为空 → **本轮合法的核心就是共性表那 7 个表达式,一个不多**。
特别注意:**裸叶子 `LogFloatShares` 不合法** —— 共性只收 `n.operands` 非空的节点(`c05_locate.py` 里 `nodes()[1:]` + `n.operands`),
裸字段从来不会进表。这正是「7 行只是 1 行」的制度原因:工具的盲区把一个字段显示成了 7 个结构。

还有一条容易踩的:GP 自己生成的树 `max_depth=4`(`scripts/idea_search.py` 的 `gp = dict(..., min_depth=2, max_depth=4, ...)`),
`depth(Feature)=1`,所以 **深度 2 的核心只给外围留 2 层,深度 3 的核心只留 1 层**。

推荐的核心,按优先级:

**核心 1(首选):`inv(LogFloatShares)`** — 深度 2,n_with=14(样本量最大的一行),共性 +1.11 / p 0.010。
- 周围**已经见过的外围写法**:`log(inv(LogFloatShares))` 是唯一在表里露出的一层外包装;
  其余 13 个含它的候选的外围算子集合没有在 `loc.json` 里给出(工具只导出子树,不导出候选表达式)——
  但从整张共性表只有单字段单调包装这一点可以推断,**这 14 个候选的外围里没有第二个字段,也没有横截面算子**(推断)。
- 为什么选它:`periphery()` 的判定是**算子名集合**(`scripts/idea_search.py:312`,`frozenset`,忽略字段与窗口,且 `SEEN` 含空集),
  所以只要外围带上一个没见过的算子名就一定新颖;它又是唯一能把样本量撑起来的一行。
- `inv` 这层的坏处是它破坏了 `LogFloatCap − LogFloatShares` 这个干净的差。两条绕法:
  `cs_regres(LogFloatCap, inv(LogFloatShares))`(横截面 OLS 残差,`operators/nd_cs.py:254`,把核心当**条件轴**而不是信号,
  残差 ≈ 价格轴),以及 `mul(LogFloatCap, inv(LogFloatShares))` = `LogFloatCap / LogFloatShares`
  ≈ 1 + log(价格)/log(股本),分母近似常数,秩上就是价格轴。

**核心 2:`ts_decay_linear(LogFloatShares, 50)`** — 深度 2,共性 +1.00 / p 0.003(p 不可解读,见 §1.2,但它 mean_with 最高)。
- 已见外围:表里没有任何它的外包装出现(没有 `inv(ts_decay_linear(...))` 之类),5 个含它的候选的外围未知。
- 为什么选它:**7 个核心里唯一带时间维度的**,只有它能原样包含地写出股本流量
  `sub(LogFloatShares, ts_decay_linear(LogFloatShares, 50))` = 近 50 日流通股本增长 = 解禁 / 定增 / 送转的供给冲击,
  这与水平轴正交,是真正的新信息。注意 P3:它必须乘进连续载体才过闸门。

**核心 3(备选):`log(LogFloatShares)`** — 深度 2,外层是保序的 `log`,`sub` / `cs_regres` 组合时语义最干净。
只有在 PI 想用两个 E 位分别打「价格轴」和「股本流量轴」时才需要动它。

**明确不要:`log(inv(LogFloatShares))`(深度 3,GP 只剩 1 层)、`abs_` / `pow_2` / `ts_max` 三行**
(样本量 4–5、mean_with 在簇的下半、而且外层算子纯属噪声)。
每个核心整个实验只有 2 个 E 位,别花在这三个上。

### 4.2 杠杆在哪里:种子就是任务本身

读 `scripts/c05_round.py` 的 mission 分支 + `scripts/idea_search.py`:

- E 位:`--parts seeds --seed-share 1.0 --graft-fill 32`,所以**初代 32 个全是种子**(Partura 的 ≤16 个 + 机械嫁接补满),
  预算 96 / 种群 32 → **只有约 3 代**。也就是说 **E 位有三分之一的预算直接花在 Partura 手写的那几行上**。
- `--parts seeds` 意味着 `arm_hooks` 的 `priors` 与 `hood` **都不开**:没有算子加权、没有 guidance 的 accept。
  steer 臂除了初代种子以外和 control 臂一模一样。**初代种子是 Partura 唯一的通道** —— 不要指望 GP 去「补全」一个半成品想法。
- 种子的深度上限是 9(`seed_max_depth=9`),而 GP 自己只能长到 4。**手写种子应该写成成品、写足深度**,
  因为那是整个任务里唯一能出现深度 >4 的结构的地方。
- 本轮 E 的「核心家族」控制是**空的**(`fam = [h for h in lib if contains(...)]`,lib 无 head),
  所以 E 的奖励和 N 完全一样,E 的唯一代价就是 must-contain 与外围新颖性。E 位本轮很便宜。

### 4.3 两个闸门,写种子前先过一遍

`scripts/c05_locate.py` / `idea_search.py` 的 `gate`:`coverage ≥ 0.9`(有标签格子上有限值的比例)且
`dg.distinct_fraction ≥ 0.5`(每天唯一值数 / 有值股票数的中位数)。推论:

- **`BoardCode`(4 档)、`LimitWidth`(3–4 档,`alphacube/tradability.py:18`:主板 10%、科创 20%、创业板 2020-08-24 起 20%、北交所 30%)
  单独当因子必然被 distinct 闸门挡死**,它们只能作为**条件 / 缩放变量**乘进一个连续信号里。
- 任何「事件旗标」「差分」类部件同理(P3)。
- `log(x)` 在 |x| ≤ EPS 时返回 NaN(`operators/common.py:211`),别让 `log` 吃到可能为 0 的差。

### 4.4 R 目标

**无**(§2,代码层面不可能)。

### 4.5 N 的灵感

按「本轮快照的盲区」排序:

1. **三个 log 字段的差 —— 把价格轴和自由流通比例轴显式写出来。** 91 个候选一次都没组合两个字段。
   `sub(LogFloatCap, LogFloatShares)`(log 未复权股价)、`sub(LogTotalCap, LogFloatCap)`(−log 自由流通比例),
   以及用 `cs_regres` / `cs_rank` 做的秩空间版本。**把这两条写成分开的种子**,这样第 2 轮的共性表就能告诉我们
   alpha 在价格轴还是股本轴上(P2)—— 这是本轮能买到的最有价值的信息。
2. **未复权价与复权因子。** `div(day_sum(Amt), day_sum(Volume))` 是未复权均价(`alphacube/daily.py:25`),
   和 `day_last(Close)` 的比值 = 累计复权因子 = 累计分红送转的痕迹。这是本环境数据结构送的一个特征,
   和 §1.4 的价格轴互为旁证,而且完全没人碰过。
3. **交易约束作为缩放 / 分组变量。** PLAN §1 第 3 条记着:C01–C04 里 Partura 唯一站住的贡献是「日收益按涨跌停幅度缩放」,
   方向由 GP 从数据里定。`LimitWidth` 和 `BoardCode` 都在本轮的 6 个字段里,而 91 个候选里一个都没用。
   按 §4.3,只能乘进连续载体(例如把 `day_std(Ret)` 或 20 日收益除以 `LimitWidth`)。
   **方向一律交给 GP 的 `sign`,不要在假设里写死**(PLAN §1 第 3 条就是这么栽的)。

---

## 5. 文献题目(交给文献员,只用 2023-08-08 之前发表的)

**Q1(对准核心 1 / §1.4 的价格轴)**:控制了市值之后,**名义股价(未复权的每股价格)**本身在横截面上还有没有定价能力?
文献里是怎么构造和处理这个特征的 —— 取对数还是分位、是否按板块或股龄分组、是否与波动率 / 彩票型特征(最大日收益、偏度)交互、
是否做过市值双变量排序?
中文关键词:低价股效应、名义股价、每股股价、股价幻觉、彩票型股票、A 股横截面。
English: nominal share price, low-price effect, price level and expected returns, penny stocks, lottery-like stocks, MAX effect, idiosyncratic skewness, China A-share cross-section.

**Q2(对准核心 2:股本轴与股本流量)**:**自由流通比例**(流通股本 / 总股本)和**流通股本的近期变动**
(限售解禁、定向增发、回购、送转)作为横截面特征,文献里怎么构造?
是用对数差分、事件窗口、还是解禁规模占流通市值的比例?有没有和换手率 / 波动率交互,或者按市值分组?
另外:有没有把**累计分红送转的历史**(等价于后复权因子)当横截面特征用的做法?
中文关键词:自由流通比例、限售股解禁、定向增发、股本变动、股票供给冲击、送股转增、复权因子、股息率。
English: free float ratio, lockup expiration, share supply shock, seasoned equity offering, share issuance anomaly (Pontiff-Woodgate), net share issuance, stock splits, dividend yield anomaly, payout and expected returns.

**Q3(方法论:判定「真来源」还是「规模的代理」)**:**秩空间线性市值中性化之后残留的非线性规模暴露**,
文献里用什么办法识别和处理 —— 分组内中性化(按市值分层内部排序)、双变量排序、市值平方项、
特征调整收益(characteristic-adjusted returns)?有没有比较过「正交化」与「双变量排序」给出不同结论的案例?
中文关键词:市值中性化、非线性规模效应、分层排序、双变量排序、特征调整收益、微盘股。
English: size neutralization, nonlinear size exposure, double sorting vs orthogonalization, characteristic-adjusted returns, Fama-MacBeth with size squared, microcap effect.

**Q4(对准 N 灵感 3)**:**涨跌停幅度 / 上市板块**这类交易约束,文献里怎么作为横截面变量使用 ——
用来缩放日收益或波动(按涨跌停幅度归一)、作为分组变量、还是作为事件(封板、开板)?
A 股涨跌停制度下的动量 / 反转 / 波动率因子有没有做过这种归一化处理?
中文关键词:涨跌停、价格限制、涨跌幅限制归一化、封板、创业板科创板 20% 涨跌幅、注册制。
English: price limits, limit-hit, magnet effect, price limit and momentum/reversal, volatility scaling under price limits, China ChiNext STAR 20% limit.

---

## 附:给 PI 的三句话

1. 本轮快照里只有一个因子,身份是「流通市值被中性化之后剩下的那一部分」,整簇卡在 0.465–0.486,离门槛 0.5 差一点;
   7 行共性是工具盲区(裸叶子不进表)造成的重复计数,机械核心卡的顺序和 p 值都不可解读。
2. 本轮 R 必须为 0(代码会拒),64 次评估白费;所以本轮唯一的目标是**产出第一个 head**,
   把第 2 轮的 48 次拆解预算激活。E 位本轮很便宜(家族控制为空)。
3. 真正的新信息不在「给 `LogFloatShares` 再套一层算子」,而在**把两个字段组合起来**:
   `LogFloatCap − LogFloatShares`(名义股价)、`LogTotalCap − LogFloatCap`(自由流通比例)、
   `LogFloatShares − ts_decay_linear(LogFloatShares, 50)`(股本流量)、`Amt / Volume`(未复权价)。
   91 个候选一次都没做过。写种子时注意量纲(§1.3)和两个闸门(§4.3),方向交给 GP。
