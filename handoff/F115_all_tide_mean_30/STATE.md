# F115_all_tide_mean_30 — 交接状态

_自动生成于 2026-10-04 13:31(`python scripts/recorder.py --brief F115_all_tide_mean_30` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 all_tide_mean_30(批次 B01_single_factors)
- 表达式:`cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F115_all_tide_mean_30`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F115_all_tide_mean_30#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F115_all_tide_mean_30#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `work:F115_all_tide_mean_30#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:09 → `handoff/F115_all_tide_mean_30/agents/work_R0_a7273d2d90aa037a4.md`
- agent `lead:F115_all_tide_mean_30#1`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:22 → `handoff/F115_all_tide_mean_30/agents/lead_R1_a3c13ae564c521f87.md`
- agent `work:F115_all_tide_mean_30#1`(wf_c8c98127-70d):失败,最后动作 10-04 13:29 → `handoff/F115_all_tide_mean_30/agents/work_R1_afd53c65be8af464a.md`
- agent `work:F115_all_tide_mean_30#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F115_all_tide_mean_30` 看服务器上的 tag,`./scripts/study.sh digest F115_all_tide_mean_30 <tag>` 重看结果)。

## 研究现状(`notes/F115_all_tide_mean_30/state.md`,10-04 13:21 更新)—— **先读这个文件**

# 研究现状 — F115_all_tide_mean_30

_每一轮由主研**整个覆盖重写**。最后更新:2026-10-04,第 1 轮(主研 = Opus 5,第一个主研)。_

---

## 1. 一句话现状

建档(R0,执行做的)已完成,**我是第一个主研**:这一轮没有跑任何实验,做的是把这棵树读懂、
写出结构语法(`04_grammar.md`)和竞争性假设表(`05_hypotheses.md`,8 条 H1–H8),并下了第一张
工单 **R1(kind: experiment)**。下一步 = 执行按 R1 跑 `S1_anatomy`(8 个变体)+ 分析脚本
`x1_anat_mfi`,然后下一轮主研裁决 H1–H4 哪一条活下来。

**全局判断(新接手的人先看这一句)**:这条因子在用户口径下**多头腿基本不存在**(valid
`Lnet +0.2% / Lshp +0.04`),而用户指定的已知家族基准在同一口径同一段是 `Lnet +18.5%`。
半衰期这根杠杆在原式上**已经拉到顶**(H7,已确立)。所以本研究最可能的归宿是**一个有证据的
否定结论**,而不是一个升华版。R1 之后若 H5 被支持,应尽早进入读留出段 + 成文,不要把轮次烧在
找升华上。

---

(…全文 11078 字符,读 `notes/F115_all_tide_mean_30/state.md`)

## 研究日志(`notes/F115_all_tide_mean_30/journal.md`:2 条,其中研究员自己写的 2 条)

最近的 12 条(完整的看文件):

### 2026-10-04 13:07 [执行] R0 建档完成:四份 notes(01/02/03/06)+ 结果卡写完,S0 复现用户公布值

做了什么:brief 确认此前无 notes/journal/state(从零建档);跑了 digest S0_baseline、overview_for.py、
decompose;读了表达式里全部 10 个算子(in_slice/in_local_mean/day_argmax/in_slice_to_end/day_argmin/
day_locate/in_slice_from_start/sub/div/cross_mean)及其调用的底层函数的内核源码,全部读取成功。

写了什么:01_expression.md(来历 + 逐层拆开 + 一句话)、02_operators.md(10 个算子的精确语义、轴、
窗口、齐次度、NaN/边界行为、是否布尔输出、是否跨日)、03_decomposition.md(量纲/取值范围表、
M=F-I>=0 的证明、M=0 退化情形 N=NaN 的推导、累计回看 20 天、恒等节点检查)、06_baseline.md
(两种口径下的 Lnet/Lshp/LS/long_share、分位剖面、全部控制变量中性化、条件 IC、逐年、衰减、
两套 rank 相关、cov/dist 门槛)。结果卡 results/R0.md 摘要四个文件要点 + 10 条异常。

主要异常(详见结果卡):day_locate 的 @op 装饰器 arity=1 与函数签名/注册表 arity=2 不一致;
in_slice_to_end/in_slice_from_start/day_locate 三个算子内置探针全部报错(索引型第二参数喂错形状),
只能靠读源码定性,没有实测数字;known_stdamt_mean30 这个 gate 没有出现在 digest 的两处输出里(无
报错,只是缺失);valid 段分位剖面不单调(Q10 < Q9);digest 原始面板 rank 相关与 overview_for.py
的 hl=2 平滑信号 rank 相关是两套不同口径,多数变量符号相反、绝对值接近(方向翻转),但 ctl_rev1
对不上简单翻号。S0 对用户公布值(ls[0]=2.29、long[0]≈0.08)复现吻合,没有发现求值失败或覆盖率问题
(cov=dist=1.00)。

下一步(留给主研):四个文件都是事实性建档,没有提假设、没有设计实验、没有下结论——下一步的假设表、
结构语法拆解(04_grammar.md)、实验设计都还没有人做。

### 2026-10-04 13:21 [主研] 第 1 轮:写出结构语法+8条假设表,下 R1 工单(三通道解剖+无潮汐零假设);全局判断是多头腿基本不存在、半衰期已拉到顶

我是第一个主研。本轮不跑实验,按 playbook「先写假设再下工单」的要求只做三件事:读懂这棵树、
写 04_grammar.md + 05_hypotheses.md、下第一张工单 R1。

看到了什么(都在 R0 的数据里,R0 只记录没解读):
1. 多头腿基本不存在。决策口径 v_base:train Lnet +5.6%/Lshp +1.21 → valid Lnet +0.2%/Lshp +0.04。
   同一张 digest 表里 known_stdamt_max9 = cross_max(day_std(Amt),9) 单独当因子是 +9.3%/+18.5%。
   用户只看多头腿,所以研究重心不是「怎么提纯」,而是「多头腿在不在、相对已知家族有没有增量」。
2. 半衰期这根杠杆在原式上已经拉到顶(定为 H7,已确立):固定 hl 表峰值就在 10,而 hlL=10 在 train
   和 utrain 上都被选中 —— 「原式+多头最优半衰期」就是基线那一行本身。没有第一组那种白捡几个点的空间;
   反过来,以后任何候选的改进也不能用「换了半衰期」来解释。
3. train→valid 的落差不是噪声,是时间趋势:逐年 Lnet 2019 +13.5% → 2021 −0.7%、2022 −0.6%。
   train 段含那两个好年份,valid 正好是死掉的年份。留出段 2023.08–2025 是这条趋势的延长线(定为 H5,先验很高)。
4. 结构上最可疑的是 ÷M:M∈[0,180] 跨三个数量级,随机游走标度下 N = L/M ~ σ·M^(−1/2),
   所以因子两端尾部必然被「两谷挨得很近」的退化样本占据。这正好对上 valid 段 Q10(+4.5%)低于
   Q9(+8.7%) —— 对只买前 10% 的用户这是致命的那一处(定为 H3,本轮唯一有建设性的假设)。
5. 语法上它是个 20 日反转:cross_mean(带符号日内收益,20) + 方向 −1。实测相符:ctl_mom20 是全部
   控制变量里最大的暴露(rank 相关 +0.44 / −0.39、R² 0.156)(定为 H1)。
6. 读对了一处 R0 容易被误读的地方:ctl_range/ctl_ivol 中性化后 Lnet 翻负是成本效应不是 alpha 没了
   (Lgross 9.4%→10.0%、TO 4.7%→24.0%)。按毛超额/rIC 看,真正削内容的是 dvol20/turnrate/amt/mom20;
   all_controls 砍掉约六成 rIC(0.0298→0.0110)。

自己核对的:把 01 的 A..O 节点代数重建成整条表达式,与 configs 里的 expression 逐字符相同,
所以 R1 工单里 8 条变体表达式是机器生成的、可直接用。另查到 cross_mean 的注册表窗口池不含 20
(池是 3,5,10,15,30,60,241),原式的 20 走手写库字面量路径 —— 所以窗口邻域选 30/60。

决定做什么:R1 = S1_anatomy(8 变体)+ x1_anat_mfi(分析脚本),一次把四个方向同时钉死 ——
几何通道 a_width_only=cross_mean(M,20)、带符号价格 a_no_rate(去掉 ÷M)、幅度 a_abs、
无潮汐零假设 a_plain_ret(两谷换成切片两端);搭车的有窗口邻域 a_win30/a_win60、去尾 a_rank_pre、
以及用户指定但 R0 没打印出来的第二条已知家族基准 k_stdamt_mean30。脚本量 D/I/F/M 的分布和
「极端分位里 M 的中位数」,这是 H3 的直接检验,也是绕开「三个算子内置探针全报错」的唯一办法。

决定不做什么:不查泄漏(H8 已确立);不查价格/市值污染(L 是比值,ctl_price R² 0.006);
不查成交量量级(argmax/argmin 齐次度 0,Volume 缩放对因子精确无影响);不调 in_local_mean 的 d
(二阶效应,H2 定下来之前没信息量);不碰 nt_*;不花轮次改善空头腿(long_share 只有 19~27%,
用户做不了空)。也明确写进 state.md §6:若 R1 显示所有变体 valid 多头腿都 ≈ 0(H5 被支持),
就尽早进入读留出段+成文,不要为了有个升华版去凑。

## 工单与结果卡(`notes/F115_all_tide_mean_30/orders/`、`notes/F115_all_tide_mean_30/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F115_all_tide_mean_30.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_anatomy**(8 个变体):N = L x (1/M) 的三个通道里预测力在哪一个;拆掉潮汐定位之后还剩多少?
  a_no_rate、a_width_only、a_plain_ret、a_rank_pre、a_abs、a_win30、a_win60、k_stdamt_mean30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F115_all_tide_mean_30`)

- `S0_baseline`  10-04 12:01  1 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S0_baseline`

## 已写的 notes(`notes/F115_all_tide_mean_30/`)

- `01_expression.md`  3095 字节  10-04 13:02
- `02_operators.md`  13227 字节  10-04 13:03
- `03_decomposition.md`  6648 字节  10-04 13:04
- `04_grammar.md`  6261 字节  10-04 13:15
- `05_hypotheses.md`  9832 字节  10-04 13:16
- `06_baseline.md`  11268 字节  10-04 13:06
- `journal.md`  6072 字节  10-04 13:21
- `state.md`  18792 字节  10-04 13:21

## 自写的探针与分析脚本(`studies/F115_all_tide_mean_30/`)

(无)

## 结构化结果(`handoff/F115_all_tide_mean_30/results/`)

(还没有)
