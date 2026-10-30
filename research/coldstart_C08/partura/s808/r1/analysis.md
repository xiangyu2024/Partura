# 结构解剖:种子 808,P 组,第 1 轮

快照 `c07s808M1_I0_open_search`,4 个 head,83 个已评分候选,拆解 27 次付费评估,已生效 R 替换 0 个。
本文件引用的表达式都写原文。读过的源码:`partura/ops_ext.py`(`day_wmean`/`day_wstd`/`cross_*`/`cs_bucket_*`)、
AlphaCube `src/alphacube/operators/nd_ts.py`、`nd_cs.py`、`common.py`(`rolling_windows`/`nanmax_last`)、`operators/dt_day.py`、
`scripts/c05_locate.py`(控制定义、R 的替换/收录判定)、`partura/steer.py`(叶子与算子分类)。

---

## 0. 一句话结论

**四个 head 不是四个发现,是同一个「一参数族」的四个窗口取值。** 真来源是:
**对日内已实现波动(或资金加权日内收益)在约 100–150 个交易日的窗口上取「运行最大值」,也就是一个 5–7 个月回看期的「极端事件尾部统计量」,方向 -1(买没出过极端日的股票)。**
控制里只有 20 日均值的波动和 20 日反转,**没有任何一个控制覆盖「半年内有没有出现过极端日」这个时间尺度** —— 这就是 alpha 的缝隙。
附带一个必须排查的机制:运行最大值是阶梯函数,换手率极低,15 bp 的成本几乎不付;而原始日度波动换手极高(裸 `day_wstd(Ret, Volume)` 的 score 是 **-3.47**)。
所以「尾部」和「低换手」两个解释现在**还分不开**,本轮必须用 R 位把它们分开。

---

## 1. alpha 的来源

### 1.1 先修正一个读法:三层 `ts_max` 不是结构,是一个窗口参数

`rolling_windows` 左侧补 NaN、`nanmax_last` 跳过 NaN,因此嵌套的滚动最大值**精确等于**一个更宽窗口的滚动最大值:
`ts_max(ts_max(x, a), b) ≡ ts_max(x, a + b - 1)`(我用这两个算子的原语义在纯 Python 里逐点验证过:50/50/50≡148、50/50≡99、10/50≡59、50/50/25≡123,全部逐点相等,包括热身期和中途缺失)。

于是四个 head 的真实身份是:

| head | score | 等价的单算子写法 | 总窗口 W |
|---|---|---|---|
| +1.26 | `ts_max(ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50), 50)` | `ts_max(cs_demean(day_wstd(Ret, Volume)), 148)` | 148 |
| +0.99 | `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)` | `ts_max(day_wmean(Ret, Volume), 99)` | 99 |
| +0.68 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 50)` | `ts_max(cs_demean(day_wstd(Ret, Volume)), 59)` | 59 |
| +0.64 | `ts_max(ts_max(cs_normalize(day_wstd(Ret, Ret)), 50), 50)` | `ts_max(cs_normalize(day_wstd(Ret, Ret)), 99)` | 99 |

**后果(对 PI 很重要)**:
- head1 和 head3 是**同一个表达式的两个窗口**(148 与 59),库里实际只有 **2 个独立想法**(波动尾部、资金加权收益尾部),不是 4 个。共性表前 5 行(`ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)`、`cs_demean(day_wstd(Ret, Volume))`、`ts_max(cs_demean(day_wstd(Ret, Volume)), 50)`、`day_wstd(Ret, Volume)`)全都是**同一条链的前缀**,是一条证据被数了 5 遍,不是 5 条独立证据。
- 库禁令按「算子骨架(抽掉字段、常数、窗口)」判重:`ts_max(x, 148)` 与 `ts_max(ts_max(ts_max(x,50),50),50)` 骨架**不同**而面板**完全相同**。骨架禁令在这一族上是漏的,真正拦住重复的是 |ρ| ≥ 0.7 那一条。E 位设计必须按 ρ 来想,不要靠骨架。

### 1.2 窗口敏感性:真正的那条曲线

把同一个底层序列 `cs_demean(day_wstd(Ret, Volume))` 的所有已评估窗口排在一起(score = min(train, valid)):

| W | 34 | 50 | 59 | 99 | 109 | 123 | 148 | 198 |
|---|---|---|---|---|---|---|---|---|
| score | -0.51 | -0.21 | **+0.68** | +0.98 | +1.07 | +1.00 | **+1.26** | +0.74 |
| train | 0.37 | 0.79 | 0.98 | 0.98 | 1.07 | 1.00 | **1.26** | 0.74 |
| valid | -0.51 | -0.21 | 0.68 | **2.24** | **2.25** | 1.63 | 1.79 | 1.20 |

读出三件事:
1. **W < 60 这个东西不存在(score 为负),W ≥ 99 一律 ≈ +1.0,W = 198 开始衰减。** 存在性本身非常稳:连续 5 个窗口都在 +0.98 ~ +1.26。**这是「真来源」最强的一条证据 —— 不是一个窗口的运气,是一个平台。**
2. **但 W = 148 这个具体取值是挑出来的。** train 的峰在 148,valid 的峰在 99–109(2.24 / 2.25,比 148 的 1.79 高)。两段对最优窗口的看法不一致,score 取 min 时恰好 148 的 train 最幸运。**head1 的 +1.26 里大约有 0.2–0.3 是窗口挑选带来的,样本外应按 ≈ +1.0 预期。**
3. 另两族的峰都在 W ≈ 99(head2:74→0.64,99→0.99,149→0.68;head4:74→0.53,99→0.64,149→0.63)。三族合起来指向**5–7 个月**这一个时间尺度。

### 1.3 充分性 / 必要性 / 敏感性 逐条

**充分性(子树单独当因子)** —— 阶梯极其陡峭,全部集中在「窗口」这一维:

- `day_wstd(Ret, Volume)` 裸值:**-3.47**(train -2.68 / valid -3.47,sign +1,hl 20)
- `cs_demean(day_wstd(Ret, Volume))`:**-3.47**(与裸值几乎同一个数)
- 加 50 日最大值:-0.21 → 加到 99 日:**+0.98** → 148 日:**+1.26**
- `day_wmean(Ret, Volume)` 裸值:-2.49;50 日最大:-1.51;99 日最大:**+0.99**
- `day_wstd(Ret, Ret)` 裸值:-3.33;`cs_normalize` 后仍 -3.33;50 日最大:+0.22;99 日最大:**+0.64**

结论:**没有任何一个「字段 / 日内算子」的组合自己有 alpha。三族的原料单独上场都是 -2.5 ~ -3.5。alpha 完全由那一层长窗口运行最大值产生。** 这就把「真来源」钉死在一个部件上。

**必要性(knockout,= head_score − 去掉后的 score)**:

| head | 去掉的部件 | 必要性 |
|---|---|---|
| +1.26 | `cs_demean(...)` → `ts_max(ts_max(ts_max(day_wstd(Ret, Volume), 50), 50), 50)` | **+0.23** |
| +0.68 | 内层 `ts_max(..., 10)`(等于 W 59→50) | **+0.89** |
| +0.68 | `cs_demean(...)` → `ts_max(ts_max(day_wstd(Ret, Volume), 10), 50)` | **+0.03** |
| +0.64 | `cs_normalize(...)` → `ts_max(ts_max(day_wstd(Ret, Ret), 50), 50)` | **-0.15** |

只有「窗口」这一个部件必要性大(+0.89),横截面归一化那一层必要性 +0.23 / +0.03 / **-0.15**。

这里有一个容易误读的地方,值得写清楚:奖励本身每天先把值转成横截面排名,所以 `cs_demean` / `cs_normalize` **放在根上是完全无效的**(`steer.py` 里 `cs_demean` 也确实被列进 `IDEMPOTENT_OPS`)。它们**只有放在 `ts_max` 里面才有作用** —— 作用是:在沿时间取最大值之前,先把当天的**全市场波动水平**减掉,于是 `ts_max` 找的是「这只股票相对当日截面有多极端」而不是「绝对有多波动」,后者会被 2018 年底、2020 年初这种全市场高波动日统一抬高。
所以:**减去截面均值(去市场波动择时)**有一点用(+0.23);**再除以截面标准差**是纯噪声(-0.15)。这是一条干净的、可解释的结论,也直接给出了 R 的方向(见 §2)。

**敏感性(换同类字段)**:`Volume → Amt`:head1 -0.01、head3 +0.02、head2 **+0.11**,其中 head2 的 swap 与原 head 的 ρ_head = **0.9997**。
**结论:`Volume` 和 `Amt` 在这一族里是同一个字段**(`day_wstd`/`day_wmean` 里权重都走 `|w|`,成交量与成交额在分钟级上几乎共线)。任何只把 `Volume` 换成 `Amt` 的提议都是换皮,审计员应按创新度 1 处理;反过来,这也说明「用什么衡量交易强度」不是载荷部件,**「按交易强度加权」本身**才是。

**共性(enrichment)的证据强度要打折**:`cs_demean(day_wstd(Ret, Volume))` 的均值差 +2.03、p 0.000、14 个候选含它,数字很漂亮,但 `mean_without = -1.39` —— 也就是说这一批**不含它的候选平均分是 -1.4**(纯多头扣 15 bp,随机树基本都亏钱)。所以 +2.03 实际在说「这一族是这批里唯一不是垃圾的东西」,而不是「这个子树是精确的来源」。`ts_max(LogFloatShares, 50)`(效应 +0.36,p 0.22)和 `ts_min(LogFloatShares, 50)`(+0.13,p 0.42)都不显著,可以忽略。

### 1.4 真来源 vs 只是代理(对照规则 §4 的三类)

**先说清楚:按 §4,这一族没有可以据以拦截的数学问题。**

- **前视**:无。`day_*` 只用当天分钟,`rolling_windows` 是因果的(左侧补 NaN),`ts_max` 只看 t 及以前。
- **数值伪影**:无。`day_wstd` / `day_wmean` 的分母是 `sum(|w|)`,代码里 `clamp(min=1e-30)` 且 `sw > 0` 才给值,否则 NaN —— 不会出现除近零的爆点;`cs_normalize` 对零方差行显式给 0。而且奖励先转排名,重尾不可能支配排序。`distinct` 0.998–1.000、`coverage` 0.997–0.999,面板不是常数。
- **定义坏掉 / 热身期**:`day_wstd(Ret, Ret)` 在全天分钟收益全为 0 的日子(一字板、停牌)分母为 0 → NaN,这就是它 coverage 0.9973 比 Volume 版 0.9993 低的原因;`ts_max` 跳 NaN,所以锁死日沿用旧的最大值。**这不是坏掉**,但它意味着缺失本身带了「有没有一字板」的信息。

**真来源(我认为站得住的)**:一个 **5–7 个月回看期的极端事件尾部统计量**。控制集是 `liq = cross_mean(day_sum(Amt), 30)`、`vol = cross_mean(day_std(Ret), 20)`、`rev = div(day_last(Close), ts_delay(day_last(Close), 20))`、`known = cross_mean(day_std(Amt), 30)`、`size = LogFloatCap`,**全部是 20–30 日的均值或 20 日的比值**。残差只去掉了这些排名的 1/2/3 次暴露。「过去半年里有没有出现过一个极端日」与「过去 20 日的平均波动」在横截面上**不是同一个东西**(均值 vs 最大值),这个缝隙是真实存在的,方向 -1(买从没出过极端日的股票)也与极端收益 / 彩票偏好类文献的符号一致。head2 的身份更直白:`ts_max(day_wmean(Ret, Volume), 99)` 方向 -1 = 「近 5 个月里资金加权日内涨幅最大的那一天有多大」,这几乎就是日内版、量加权版的 MAX 效应。

**三个必须排除的代理(按嫌疑从大到小)**:

1. **低换手(成本代理)。** 这是最大的嫌疑,而且**和「尾部」完全缠在一起**。运行最大值是阶梯函数:只有当旧的最大值滚出窗口(每天约 1/148 ≈ 0.7% 的名字)或出现新的尖峰时才变,所以 hl=0 也几乎不付 15 bp;而裸 `day_wstd` 每天都变,换手巨大 —— 这足以解释裸值为什么是 -3.47,也足以解释「加了长窗口就从 -3.5 跳到 +1.0」。
   **判别式:把 `ts_max` 换成 `ts_mean` / `ts_med`(同样平滑、同样低换手,但测的是「水平」而不是「尾部」)。** 若 `ts_mean(cs_demean(day_wstd(Ret, Volume)), 148)` 也拿到 ≈ +1.0,那本族是「慢速波动水平 + 低成本」,不是尾部;若它掉到 0 附近,尾部就是真的。**这是本轮信息量最大的一次评估,必须做。**
2. **上市年龄(`ListAge`)。** 机制是代码层面的:`rolling_windows` 对缺失补 NaN、`nanmax_last` 跳 NaN,所以**历史短的股票是在更少的抽样里取最大值,最大值系统性偏小** → 方向 -1 → 新股被系统性推进纯多头书的头部。`ListAge` 是叶子但**不是控制**,2018-01 起的前 ~148 天以及所有中途上市的票都受影响。两股力量方向相反(新股通常波动大,会把最大值推高),净效应未知 —— **必须测**,否则 head1 的一部分 alpha 可能只是「买新股」。
3. **板块 / 涨跌幅宽度(`BoardCode`、`LimitWidth`)。** 20% 限幅的创业板 / 科创板日内波动机械地更大,`cs_demean` 只减当日全市场均值,减不掉板块差 → 极端值的最大值系统性更高 → 方向 -1 = 「空创业板科创板、买主板」的一个慢速板块倾斜。§4 明说板块信息不是缺陷,所以这不是拦截理由,但它是不是**全部**的 alpha,必须分开看。判别式:`cs_bucket_demean(…, LimitWidth)` 或 `cs_bucket_rank(…, LimitWidth)`。

---

## 2. 烂部件(适合做 R)

按必要性 ≤ 0 或换掉反而更好:

| 部件 | 在哪 | 证据 | 处置 |
|---|---|---|---|
| `cs_normalize(...)` | head +0.64 | 必要性 **-0.15**;去掉后 0.79(train 0.79 / valid **2.47**),ρ_head 0.9273 | **删**。已是现成的 R 替换候选(增益 +0.15) |
| `cs_demean(...)` | head +0.68 | 必要性 **+0.03** —— 实质为零 | 可删;但删了只有 0.6456(比原 head 低 0.035),**够不上 +0.1 的替换门槛**,只能当知识 |
| `Volume`(当权重) | 三族 | 换 `Amt`:-0.01 / +0.02 / +0.11,head2 里 ρ_head **0.9997** | 不是载荷部件。head2 换 `Amt` 增益 +0.1063,**勉强过 +0.1** |
| 内层窗口 10(head +0.68) | head +0.68 | W 59 → 109 增益 **+0.39** | 现成的最佳 R 替换候选 |
| `cs_demean(...)` | head +1.26 | 必要性 +0.23,是四个部件里唯一真有用的归一化 | **留着**,但可以试换成 `cs_rank` / `cs_robust_z` |

**可直接提交的三个已知 R 候选(分数已经付过钱,结果确定)**,按 `c05_locate.py` 的判定(`score ≥ head + 0.1` 且 `rho_head ≥ 0.5` 且 `|rho_known| < 0.5` → 替换):

| 原 head | 变体 | score | 增益 | ρ_head | 判定 |
|---|---|---|---|---|---|
| +0.68 | `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 10), 100)` | 1.066 | **+0.385** | 0.695 | 替换(余量 0.285,稳) |
| +0.64 | `ts_max(ts_max(day_wstd(Ret, Ret), 50), 50)` | 0.792 | +0.152 | 0.927 | 替换(余量 **0.052**,薄) |
| +0.99 | `ts_max(ts_max(day_wmean(Ret, Amt), 50), 50)` | 1.094 | +0.106 | 0.9997 | 替换(余量 **0.006**,几乎是硬币) |

两条从源码读到的机械规则,PI 排 R 时请直接用:
- **`todo = [...][:MAX_R]`,MAX_R = 16** —— 超出的直接截断,**所以最重要的变体要排在最前面**。
- **「一个 head 只取一个替换:合格者里分数最高的那个」** —— 所以 16 个变体**摊到 4 个 head 上**比堆在一个 head 上值钱;而且在同一个 head 上同时提交「已知的窗口赢家」和「结构探针」没有损失:探针赢了就它上,输了就窗口赢家上。
- **另外**:`c05_locate.py` 里 R 的「收录为新 head」那一支写着 `if STUDY == "C06":`,C08 走的是同一个脚本(`PARTURA_C0X=C08`,`MPFX="c07"`,与快照名 `c07s808M1_...` 一致)。按现在的代码,**C08 的 R 只会发生「替换」,不会发生「收录」**。这与 rules.md §2 的表述有出入,**请 PI 确认**;若确实如此,那么**结构性新想法不要放在 R 里**(ρ_head < 0.5 的变体会被算出来、写进 rows,但不会进库),R 只用于族内升级 + 换取 16 次廉价诊断。

**一个必须说的代价**:把 head3 从 W 59 换成 W 109 之后,库里 head1(W 148)和 head3(W 109)是同一条序列的两个最大值窗口,日度秩 ρ 几乎肯定远高于 0.7。分数上涨 +0.385,但库的有效多样性从「2 个想法」变成「1.5 个想法」,而且**今后 GP 的候选会被这两个 head 同时挡**。最终比的是库的样本外表现,所以这笔交易值不值,PI 要自己定;我的意见是**接受它**(升级是确定的),但同时要求本轮至少有一个位去做族外的东西。

---

## 3. 之前的任务

**第 1 轮,本种子没有之前的任务**:`loc.json` 的 `missions_before` 是空的,`replacements_in_force = 0`,没有 `missions_final.yaml` / `audit_record.json` / `R_prev.json`,也没有 `notebook.md`(我确认过该文件不存在)。E 没有试过任何外围、没有 heads 产出,N 没有结果,R 没有替换与收录,审计员还没有挡过任何东西,也没有上一轮的预测可以对照。

既然没有预测可查,**我在这里留下本轮的预测,供第 2 轮逐条核对**:

1. `ts_mean(cs_demean(day_wstd(Ret, Volume)), 148)` 的 score 会**明显低于** +0.9(我赌 0.0 ~ 0.6)。若它 ≥ 0.9,「尾部」解释破产,本族其实是「慢速波动水平 + 低换手」。
2. `ts_max(cs_demean(day_wstd(Ret, Volume)), 110)` 的 score 落在 **+0.95 ~ +1.15**,且 valid 高于 head1 的 1.79。
3. `cs_rank` 版本(`ts_max(cs_rank(day_wstd(Ret, Volume)), 148)`)**不差于** `cs_demean` 版本的 1.26 ± 0.2 —— 排名归一化比减均值更该稳。
4. `cs_bucket_demean(…, LimitWidth)` 版本的 score **下降不超过 0.3**。若下降超过 0.5,本族主要是板块倾斜。
5. E 位若把核心固定在 `ts_max(ts_max(cs_demean(day_wstd(Ret, Volume)), 50), 50)`(W 99),**超过一半的后代会被 |ρ| ≥ 0.7 的库禁令挡掉**(它和 head1 的 W 148 是同一序列的两个最大值),有效评估次数会远少于 96。

---

## 4. 本轮候选

### 4.1 E 的核心(≤ 3,按推荐顺序)

**全体 E 位的一条设计铁律**:这一族的核心本身就几乎是一个 head,**只要外围是「再套一层 `ts_max`」或任何单调包裹,候选与 head1 的 ρ 必然 ≥ 0.7,会被库禁令直接拒掉**(`steer.py` 的 `strip_root_monotone` 还会把根上的 `sqrt`/`pow_*` 当成同一个实验)。所以 E 的种子必须**引入第二个、不同的输入**,把 ρ 打下来。可用的外围写法(都在手写库里,我查过签名):
`sub(cs_rank(A), cs_rank(B))`、`div`、`cs_bucket_rank(y, x)`(按 x 的十分位内排名)、`cs_bucket_demean(y, x)` / `cs_bucket_zscore(y, x)`、`cs_robust_z`、`cs_winsor`、`cs_first_low20(y, x)` 一族(按 x 的分位带做字典序)、`cross_tail_mean_q75(x, d)`、`cross_valid_count(x, d)`、`cross_age(x)`、`ts_argmax(x, d)`、`ts_med` / `ts_mean`。可用的叶子:`Close/Open/High/Low/Vwap/Amt/Volume/Ret` 加 6 个日频字段 `LogFloatCap/LogTotalCap/LogFloatShares/LimitWidth/BoardCode/ListAge`。

**核心 A(首选):`ts_max(cs_demean(day_wstd(Ret, Volume)), 50)`**
核心卡第 3 项,enrichment 均值差 +1.96、p 0.000、10 个候选含它;自身 score 只有 **-0.21**,上升空间最大;它是 head1 的字面子树,合法。
*周围已经见过的外围*:∅(-0.21)、`ts_max@50`(+0.98)、`ts_max@50`+`ts_max@50`(+1.26)、`ts_max@50`+`ts_max@25`(+1.00)、`ts_max@50`+`ts_max@100`(+0.74)。另外 enrichment 说 83 个候选里有 10 个含它,**那 10 个的具体写法我在定位输出里看不到**,所以「已见过」的集合比上面这 5 个大;E 的去重由 GP 机械执行,不会出错,但有效预算会被吃掉一部分。
*建议种子方向*(都避开「再套 ts_max」):与等权波动相减 `sub(cs_rank(核心), cs_rank(ts_max(day_std(Ret), 50)))`、`cs_bucket_demean(核心, LimitWidth)`、`cs_bucket_rank(核心, ListAge)`、`cs_bucket_rank(核心, LogFloatCap)`、与 `day_gini(Ret)` / `day_es_ratio_hi(Ret)` 的尾部形状相乘或相减。
*审计风险*:E 位要求**核心与每个控制的 |ρ| < 0.8**。这个核心是 50 日最大值的波动量,与 `vol = cross_mean(day_std(Ret), 20)` 的秩相关可能逼近 0.8。**请 PI 先看相关度表再定稿**,别等退回。

**核心 B(备选,也是最安全的那个):整条 head `ts_max(ts_max(day_wmean(Ret, Volume), 50), 50)`**
理由:它是库里**第二个独立想法**,而且是唯一一个**不是波动量**的(资金加权日内收益的 5 个月最大值),所以它与 `vol` 控制的 |ρ| 应该明显低于 0.8,**E 的审计门槛最安全**;enrichment 表里连 `day_wmean` 都没出现,说明这一族在 83 个候选里只被碰了几次,**未探索的外围最多**。它的子树单独都是负分(-1.51 / -2.49),所以核心只能取整条 head(规则允许)。
*周围已经见过的外围*:∅(+0.99)、`ts_max@25`(+0.64,W 74)、`ts_max@100`(+0.68,W 149)、以及 `Volume→Amt` 的同构版(+1.09,ρ 0.9997,算同一个东西)。
*建议种子方向*:与它的「只看方向、不看幅度」的兄弟配对 —— `sub(cs_rank(核心), cs_rank(ts_max(day_signed_ratio(Ret, Amt), 99)))`;与自身的最小值配对 `sub(cs_rank(核心), cs_rank(ts_min(day_wmean(Ret, Volume), 99)))`(极端上涨日 vs 极端下跌日的不对称);`cs_bucket_rank(核心, LimitWidth)`;与 `rev` 之外的长周期动量配对。

**核心 C(第三,或留到第 2 轮):`day_wstd(Ret, Ret)`**
核心卡第 4 项,均值差 +1.88、p 0.0046、4 个候选含它。它是三族里**唯一一个不同的日内函数形式**:权重走 `|w|`(源码里 `w = _f(w).abs()`),所以 `day_wstd(Ret, Ret) = sqrt(Σ|r|(r-m)²/Σ|r|)`,是一个**尾部加权的日内波动**(大幅分钟支配),与等权的 `day_std(Ret)`(= `vol` 控制的原料)函数形式不同 —— 这正是控制覆盖不到的地方。
*周围已经见过的外围*:∅(-3.33)、`cs_normalize`(-3.33)、`cs_normalize`+`ts_max@50`(+0.22)、`cs_normalize`+`ts_max@50/50`(+0.64)、`+@25`(+0.53)、`+@100`(+0.63)、`ts_max@50/50`(+0.79,已知 R 候选)。
*审计风险*:裸日频量,与 `vol` 控制的 |ρ| 可能超 0.8 → E 位会被退回。**除非相关度表显示 < 0.8,否则不要把它放进 E,放进 N 更合适。**

### 4.2 R 目标(16 个,我建议的排序;前三个保增益,后面买知识)

前 3 位 = §2 的三个已知赢家(确定的 +0.385 / +0.152 / +0.106,**要排最前,防 MAX_R 截断**)。第 4 位起全部是判别式,摊到 4 个 head 上,门槛最低的 head3(0.681→0.781)和 head4(0.639→0.739)多放:

4. **`ts_mean(cs_demean(day_wstd(Ret, Volume)), 148)`** —— 对 head1。**本轮最重要的一次评估**:尾部 vs 水平(§1.4 代理 1)。
5. **`ts_med(cs_demean(day_wstd(Ret, Volume)), 148)`** —— 同上,稳健版。
6. **`cross_tail_mean_q75(cs_demean(day_wstd(Ret, Volume)), 148)`** —— 上四分位条件均值:是「最糟那一天」还是「尾部那一堆天」?若它 ≥ head1,说明 alpha 不靠单日,样本外更可信。
7. **`ts_argmax(cs_demean(day_wstd(Ret, Volume)), 148)`** —— 只留「尖峰离今天多久」,扔掉幅度。幅度派 vs 时机派的判别式。
8. **`ts_max(cs_rank(day_wstd(Ret, Volume)), 148)`** —— 对 head1,把 `cs_demean` 换成排名归一化(预测 3)。
9. **`ts_max(cs_robust_z(day_wstd(Ret, Volume)), 148)`** —— 中位数/MAD 版,抗重尾。
10. **`ts_max(cs_bucket_demean(day_wstd(Ret, Volume), LimitWidth), 148)`** —— 板块 / 限幅代理(§1.4 代理 3)。
11. **`ts_max(cs_bucket_demean(day_wstd(Ret, Volume), ListAge), 148)`** —— 上市年龄代理(§1.4 代理 2)。
12. **`ts_max(cs_demean(day_std(Ret)), 148)`** —— 对 head1,把量加权换成等权:**量加权到底贡献了多少?**(这是控制覆盖不到的那一半)
13. **`ts_max(cs_demean(day_wstd(Ret, Volume)), 110)`** —— 对 head1,valid 偏好的窗口(预测 2);即便够不上 +0.1 也要买这个数,它决定第 2/3 轮用哪个窗口。
14. **`ts_max(cs_normalize(day_wstd(Ret, Ret)), 148)`** —— 对 head4,把它的窗口推到 head1 的平台,顺带检验「W≈148 最优」是不是只对 Volume 族成立。
15. **`ts_max(day_topw_mean(Ret, Volume), 99)`** —— 对 head2,把「资金加权全天收益」换成「最重 10% 分钟的平均收益」(同一机制的事件化写法)。
16. **`ts_min(day_wmean(Ret, Volume), 99)`** 或 **`ts_max(day_signed_ratio(Ret, Amt), 99)`** —— 对 head2,下行不对称 / 只看方向不看幅度。

(第 4、12 项若 PI 想省,至少保 4 和 12;这两条分别钉死「尾部 vs 水平」和「量加权 vs 等权」,是我整份分析里两个还没有证据的关键环节。)

### 4.3 N 的灵感(按我的偏好排序)

**N1(首选)——「量时钟 vs 日历时钟」的波动差,而不是波动本身。**
核心观察:控制里的 `vol = cross_mean(day_std(Ret), 20)` 是**等权**分钟波动,而 head 用的是**量加权**的 `day_wstd(Ret, Volume)`。两者之差是控制集里**结构性缺失**的那一块,而且是**无标度的**(比值/秩差),天然与 `vol` 控制正交。
写法(**用秩相减,不要用除法** —— `day_std(Ret)` 在一字板日为 0,`div` 会触发 §4「除以近零的量」,审计员有权拦;秩相减没有这个问题):
`ts_max(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_std(Ret))), 110)`,以及不加 `ts_max` 的 `cross_tail_mean_q75(sub(cs_rank(day_wstd(Ret, Volume)), cs_rank(day_std(Ret))), 110)`。
机制一句话:股票的波动是发生在有量的分钟(有人在交易、有信息)还是发生在空气里(薄盘乱跳),这是两种完全不同的股票,而现有控制分不开它们。

**N2 —— 日内形状,而不是日内尺度。**
`day_es_ratio_hi(Ret)`(95% 分位以上分钟的均值 / 该分位,源码对分位近零显式给 NaN,比手写库 `erm_*` 那种 `+1e-6` 的写法干净,这点可以写进合理度理由)、`day_gini(Ret)`(全天的动都挤在几分钟还是摊开)、`day_at_max_ratio` / `day_flat_run_max`。都是无标度量,再接 5 个月的 `cross_tail_mean_q75` 或 `ts_max`。
机制:让一个波动日有预测力的,可能是「这一天的动集中在几分钟里」(跳、消息、扫单),而不是「这一天方差大」。

**N3 —— 时机,而不是幅度。**
`ts_argmax(...)`、`cross_age`、`cross_valid_count(day_last(Close), 241)`。如果 R 的第 7 项显示 argmax 自己就有分,那整族的故事就该改写成「出过事然后安静下来了」,N 位可以沿这条线建一个独立的族(例如「尖峰后已过去多少天 × 当前波动分位」)。

**N4(备选)—— 极端下跌日的镜像。** 全族都是 `ts_max`,方向 -1;`ts_min` 的那一侧(极端下跌日)在 83 个候选里完全没被碰过。`cross_semistd_neg` / `cross_semistd_pos` 可以把上行、下行的半标准差分开。不对称性是便宜的新维度。

---

## 5. 文献题目(给文献员,中英文关键词都给)

**题 1 —— 对准核心 A / head1(`ts_max(cs_demean(day_wstd(Ret, Volume)), 148)`)。**
文献里对「**在数个月的长窗口上取已实现波动(或收益)的运行最大值 / 极值**」这类结构做过哪些处理?具体想要三件事:(a) 极值统计量与**同期波动均值水平**相比,横截面预测力是独立的还是被水平吸收的;(b) 文献用的回看期是多长(1 个月?6 个月?12 个月?),有没有报告过**最优回看期在 100–150 个交易日**这个量级;(c) 效应的符号(极值大 → 未来收益低?)以及它在控制了波动水平、流动性、市值之后是否还在。
关键词:MAX effect, extreme positive return, lottery demand, idiosyncratic volatility puzzle, realized volatility tail, running maximum, long-horizon extreme event, low-volatility anomaly / 极端收益效应, 彩票偏好, 特质波动率之谜, 已实现波动尾部, 滚动最大值, 低波动异象, 回看期

**题 2 —— 对准 N1 与核心 A 的「量加权」那一层(`day_wstd(Ret, Volume)` vs `day_std(Ret)`)。**
文献里**按成交量/成交额加权的日内已实现波动**(也就是「成交量时钟 / 交易时间抽样」)与**等权(日历时间)已实现波动**相比,有哪些已知差别?特别想要:(a) 两者之差被解释成什么(信息流强度?噪声交易?流动性?);(b) 有没有人把「量加权波动 − 等权波动」直接当横截面因子用过,符号是什么;(c) 在分钟数据上这个差别主要由哪些微观结构现象驱动(开收盘集中、大单冲击、日内 U 形)。
关键词:volume clock, business-time sampling, trade-time vs calendar-time realized volatility, volume-weighted realized volatility, intraday volume-volatility relation / 成交量时钟, 交易时间抽样, 量加权已实现波动, 量价关系, 日内波动 U 形, 微观结构噪声

**题 3 —— 对准核心 B / head2(`ts_max(day_wmean(Ret, Volume), 99)`)。**
`day_wmean(Ret, Volume)` 是「成交量加权的分钟收益均值」,在量纲上接近「收盘价相对当日成交量加权均价(VWAP)的位置」。文献里对**资金加权日内收益 / VWAP 与收盘价之差 / 日内收益在成交量上的分布**这类特征,在横截面上做过哪些处理?想要:(a) 它被当作什么代理(买压?知情交易?日内动量?);(b) 已知的横截面符号与持续期(日内 → 隔日 → 月度);(c) 有没有人取它的**长窗口极值**(而不是均值)用过。
关键词:VWAP, volume-weighted average price versus close, order flow imbalance, net buying pressure, intraday momentum, close-to-VWAP reversal, money-weighted return, intraday return skewness / 成交量加权均价, 均价与收盘价之差, 买卖压力, 净主动买入, 日内动量, 资金加权收益, 日内收益偏度

**题 4 —— 对准 §1.4 的两个代理(`LimitWidth` / `BoardCode` / `ListAge`)。**
A 股的**涨跌幅限制宽度(主板 10% vs 创业板、科创板 20%)**、**板块归属**和**上市年龄**,对日内已实现波动及其**极值**有哪些**机械性**的影响?文献(含 2023-08-08 之前的中文文献)在构造日内波动类因子时**怎么中性化**这些东西 —— 是分板块排名、分组去均值、还是直接剔除?另外:一字板 / 停牌造成的「全天分钟收益恒为 0」在已实现波动类因子里通常怎么处理?
关键词:price limit, limit hit, magnet effect, 20% price limit ChiNext STAR Market, IPO age, listing age effect, new listing anomaly, trading suspension, board segmentation / 涨跌停板, 涨跌幅限制, 磁吸效应, 创业板 科创板 20% 限幅, 一字板, 上市年龄, 次新股效应, 停牌, 分板块中性化

---

## 附:本轮解剖落下的两个口子(写给第 2 轮的自己)

1. **83 个候选里那 10 个含 `ts_max(cs_demean(day_wstd(Ret, Volume)), 50)` 的候选,具体写法我看不到。** 定位输出只给了 enrichment 的汇总。这影响 E 位的「外围不得重复」的有效预算估计。若下一轮能在定位输出里看到那 10 个候选的表达式,E 的种子设计会准得多 —— 值得向 PI 提一句。
2. **四个 head 与 5 个控制的 |ρ| 在 `loc.json` 里没有**(只有 `rho_known`:-0.09 / -0.03 / +0.03 / -0.04,都很低)。E 位的审计门槛(核心与每个控制 |ρ| < 0.8)只能等相关度表。**在那张表出来之前,核心 A 和核心 C 都算「待定」,核心 B 是唯一一个我有信心能过门槛的。**
