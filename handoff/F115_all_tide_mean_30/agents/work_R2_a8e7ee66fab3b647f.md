# work:F115_all_tide_mean_30#2 — agent a8e7ee66fab3b647f(工作流 wf_48864a04-f0a)

- 状态:**已返回结果**;开始 10-04 15:02,最后一次动作 10-04 15:38;工具调用 69 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F115_all_tide_mean_30/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 15:02 · Bash** — Check working directory and list contents

```bash
cd /Users/wxy/Desktop/Partura && pwd && ls
```

```
/Users/wxy/Desktop/Partura
CLAUDE.md
README.md
batches
configs
docs
handoff
lab
logs
notes
partura
research
runs
scripts
shared
studies
tests
tmp
workflows
```

10-04 15:02 · 读 `/Users/wxy/Desktop/Partura/docs/study_playbook.md`

**10-04 15:02 · Bash** — Get brief status for factor F115_all_tide_mean_30

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F115_all_tide_mean_30 2>&1 | head -200
```

```
# F115_all_tide_mean_30 — 交接状态

_自动生成于 2026-10-04 15:02(`python scripts/recorder.py --brief F115_all_tide_mean_30` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 all_tide_mean_30(批次 B01_single_factors)
- 表达式:`cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `work:F115_all_tide_mean_30#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:09 → `handoff/F115_all_tide_mean_30/agents/work_R0_a7273d2d90aa037a4.md`
- agent `lead:F115_all_tide_mean_30#1`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:22 → `handoff/F115_all_tide_mean_30/agents/lead_R1_a3c13ae564c521f87.md`
- agent `work:F115_all_tide_mean_30#1`(wf_c8c98127-70d):失败,最后动作 10-04 13:29 → `handoff/F115_all_tide_mean_30/agents/work_R1_afd53c65be8af464a.md`
- agent `work:F115_all_tide_mean_30#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)
- agent `lead:F115_all_tide_mean_30#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 13:56 → `handoff/F115_all_tide_mean_30/agents/lead_R1_a8335e6e80d689144.md`
- agent `work:F115_all_tide_mean_30#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 14:29 → `handoff/F115_all_tide_mean_30/agents/work_R1_ab1ea8a7172111e8e.md`
- agent `lead:F115_all_tide_mean_30#2`(wf_48864a04-f0a):已返回结果,最后动作 10-04 15:00 → `handoff/F115_all_tide_mean_30/agents/lead_R2_a7746237f816b23e1.md`
- agent `work:F115_all_tide_mean_30#2`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F115_all_tide_mean_30` 看服务器上的 tag,`./scripts/study.sh digest F115_all_tide_mean_30 <tag>` 重看结果)。

## 研究现状(`notes/F115_all_tide_mean_30/state.md`,10-04 14:59 更新)—— **先读这个文件**

# 研究现状 — F115_all_tide_mean_30

_每一轮由主研**整个覆盖重写**。最后更新:2026-10-04,**第 2 轮**(主研 = Opus 5)。
本轮做的是:裁决 R1 的结果(R1 已跑完、结果卡已交)、把解读写进 07/07x/05、下 R2 工单。本轮没有跑实验。_

---

## 1. 一句话现状

**R1 跑完了,这棵树的内部结构已经钉死;R2 工单已下,只剩两个问题没答案。**
R1(`S1_anatomy` 8 变体 + `x1_anat_mfi` 脚本,都 exit 0)把 H2、H3 杀死,H1、H5 支持,H4、H7b 改写/否定,
并给出**唯一一条确立的提纯结果**(整个 `÷M` 子树可以删掉)。
剩下的两个问题就是 R2 的全部内容:**(一) 对只做多的用户,它掺进已知家族有没有增量(H6);
(二) 潮汐定位是不是只等于一个固定子窗口(H10,新立)。**

**下一步**:执行按 `notes/F115_all_tide_mean_30/orders/R2.md` 做 ——
阶段 `S2_increment`(5 变体)+ 脚本 `studies/F115_all_tide_mean_30/increment.py`(tag `x2_increment`),
共 2 次服务器运行。

**全局判断(新接手的人先看这三句)**:
1. 这条因子**对用户没用**:valid 段多头腿净超额 +0.2%(纯多头夏普 +0.04),而用户指定的已知家族基准
   同段是 **+22.3%**(夏普 3.46)。
2. valid 的崩塌是**毛**崩塌(`Lgross` 9.4%→4.1%),**不是**成本、不是半衰期没调好 —— 而同一段
   已知家族的毛多头腿从 15.2% 升到 24.4%,所以**不是环境问题,是这条因子自己衰减**。
3. 因此本研究的归宿是**一个有证据的否定结论 + 一条提纯结果**,不是升华版。
   **R2 之后直接进入 (b) 读留出段,不要再铺第四个实验阶段。**

---

(…全文 17539 字符,读 `notes/F115_all_tide_mean_30/state.md`)

## 研究日志(`notes/F115_all_tide_mean_30/journal.md`:9 条,其中研究员自己写的 5 条)

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

### 2026-10-04 13:56 [主研] 第 1 轮(重入):R1 无结果卡→不另开工单;逐字符核对配置忠实于工单、留出段未被碰,原样让执行从 check 续跑

背景:上一位主研(同为 Opus 5)在 13:18 写完 R1 工单,13:29 执行把 8 个变体写进配置后被额度打断
(用户已重置额度)。按任务规则第 2 条:最新工单没有结果卡 → **不另开工单**,返回
{status:'order', order:'R1', kind:'experiment'} 让执行接着做。本轮没有跑任何实验,也没有新的金融结论。

这一轮我做的是核对 —— 因为上一个执行是在中途死的,半成品配置是最容易把一整轮实验做废的地方
(表达式被手改、变体漏写、controls 被加料都会让结果与 S0 那一行不可比,而这类错误在结果卡里看不出来)。
核对结果(全部写进 state.md §2.3):

1. 服务器上只有 S0_baseline(exit 0),S1_anatomy / x1_anat_mfi 都没跑过,本地 logs/ 里没有任何
   F115_* 日志 → 工单的「2 次服务器运行」额度是满的。
2. 配置里 S1_anatomy 阶段已存在,8 个变体齐全;**8/8 表达式与 orders/R1.md 代码围栏逐字符相同**
   (python 字符串相等比较),括号全部配平(每条左右括号差 0)。
3. v_base 与顶层 expression 逐字符相同(没被动过);a_win30/a_win60 确实只差末尾窗口 20→30/60。
4. a_rank_pre 用的是**首选写法** cross_mean(cs_rank(...)),工单给的备用写法 ts_mean(cs_rank(...))
   未被使用 → 说明执行根本没走到 check,check 还没跑过(这条对下一个执行很关键)。
5. 诊断项与工单一致:neutralise [v_base, a_no_rate]、profile 5 个、corr_ids 9 个、corr_with 12 个
   含 known_stdamt_mean30;controls/gates **没有被加料** → all_controls 的 R² 与 S0 可比。
6. studies/F115_all_tide_mean_30/ 目录还不存在,anat_mfi.py 还没写 —— 这是执行这一轮的主要工作量。
7. **留出段没有被偷看**:ledger.json 里只有 S0_baseline 的 train/valid/utrain,没有任何 split: holdout。

判断:R1 工单完整可执行,配置干净且忠实,**没有要修的、没有要重做的**。
决定:原样续跑 R1;执行直接从 ./scripts/study.sh check 开始,不要重写配置(唯一允许的改动是
check 若拒绝 cs_rank×cross_mean 混用,就换上工单给的 ts_mean 备用写法,并在结果卡写明用了哪条)。
决定不做:不新开工单、不改工单、不改配置、不动 R1 的实验设计;不为了「这一轮有产出」去加变体
或另起一个阶段 —— 那会把已经设计好的判别性实验冲淡,而且会越过工单的 2 次运行上限。

排期提醒(写进 state.md §6):本轮没消耗实验,但也没产出新数字,排期上要当成「R1 的结果还欠着」。
全局判断不变:原式多头腿在 valid 已经 ≈ 0(Lnet +0.2%),已知家族同段 +18.5%,半衰期已拉到顶(H7),
所以最可能的归宿是有证据的否定结论;R1 之后若 H5 被支持,尽早读留出段 + 成文,不要找升华。

### 2026-10-04 14:03 [auto] 启动 run S1_anatomy:阶段 S1_anatomy

### 2026-10-04 14:09 [auto] S1_anatomy 跑完(exit 0);重看结果:./scripts/study.sh digest F115_all_tide_mean_30 S1_anatomy

### 2026-10-04 14:18 [auto] 启动 exec x1_anat_mfi:studies/F115_all_tide_mean_30/anat_mfi.py

### 2026-10-04 14:19 [auto] x1_anat_mfi 跑完(exit 0);重看结果:logs/F115_all_tide_mean_30_x1_anat_mfi.log

### 2026-10-04 14:27 [执行] R1:S1_anatomy(8变体)+ x1_anat_mfi 都跑完(各 exit 0),结果卡 results/R1.md 已写

做了什么:配置(S1_anatomy 8 变体)上一轮已经写好且与工单逐字符一致,我没有改动;check 报 7 条
"contains a LOOKAHEAD operator"(v_base 本身 + 6/8 新变体),查到是 in_local_mean(H8 已确认的日内非
因果算子),只在 check 里提示、不影响 run/exec 的真实求值,v_base 自己已经用这个算子跑出过可信结果,
所以原样跑,没有改表达式。run S1_anatomy、exec 新写的 studies/F115_all_tide_mean_30/anat_mfi.py(D/I/F/M/L/N
六面板 + H3 直接检验),两次服务器运行都是 exit 0,8/8 变体、6/6 面板全部求值成功,服务器运行次数用满
工单给的 2 次上限。

关键数字(决策口径,train→valid 多头腿净超额):v_base +5.6%→+0.2%;a_no_rate(去掉÷M)+6.4%→+2.0%;
a_width_only(纯几何通道)-7.0%→+3.8%(但 dist=0.23,没过用户门槛);a_plain_ret(零假设,拆掉潮汐机械)
+4.8%→-0.5%,与 v_base 的 rank 相关 +0.70;a_abs(幅度通道)-8.4%→+4.8%;a_win30/60 与原式 20 相近或更好
(+5.7%/+6.8% train);k_stdamt_mean30(用户指定第二条已知家族基准)+12.6%→+22.3%,这次在两处输出里都
打印出来了(R0 的"没打印"没有重现)。rank_corr(v_base, a_no_rate)=+0.84、(v_base, a_width_only)=-0.00。

x1_anat_mfi 的 H3 直接检验(按 O 分桶,Q1/Q5/Q10 的 M 中位数):94/95/94,几乎相等;abs(N) 中位数
0.00008/0.00007/0.00012,没有随桶单调下降。M 在 train 段几乎从不小(M<=20 只占 0.61%);M==0 只有 2 个
格子,但 100% 对应 N=NaN,与 03_decomposition.md 的推导精确对上。O 与 known_stdamt_mean30/ctl_ivol/
ctl_mom20 的 rank 相关,原始面板(+0.17/+0.24/+0.44)与交易信号(-0.26/-0.21/-0.22)三项符号全部相反,
和 S1_anatomy digest 自己给的数字两位小数对得上(交叉验证通过)。

异常/没人要但值得注意的都写进了 results/R1.md 第三节(LOOKAHEAD 误报、a_width_only 的 dist 不达标、
M 几乎不小、H3 检验是平的、原始/信号相关符号相反、多个变体分位剖面不单调、N 的分位数表打印精度不够)。
没有判断任何一条假设的状态,也没有下任何结论——那是主研的事。

### 2026-10-04 15:00 [主研] 第 2 轮:裁决 R1 —— H2/H3/H7b 被否定、H1/H5 被支持、H4 改写;确立唯一的提纯结果(删整个 ÷M 子树);下 R2 工单(增量权重曲线 + 固定子窗口零假设)

看到了什么(R1 的 S1_anatomy 8 变体 + x1_anat_mfi 都 exit 0,结果卡已交):

1. ÷M 在秩空间接近恒等变换,H2 和 H3 一起死,而且 H3 的前提本身就是错的。
   x1 量到 M 的 p1/p50/p99 = 24/95/177、M<=20 只占 0.61%,根本没有 04_grammar 性质 3 预言的
   「跨三个数量级的倒数放大器」。三条独立证据:rank_corr(N,L)=+0.9582、
   rank_corr(O, cross_mean(M,20))=+0.0096、a_width_only 的 rIC 只有 +0.0024 且与 v_base 相关 -0.00、
   dist 0.23 连门槛都不过。H3 的直接检验是平的(按 O 分桶 median(M)=94/95/94)。
   机制上讲得通:argmin 找的是最低点,而日内量能曲线的最低点天然靠两头 ——
   x1 量到 I 的 p50=22(贴左端)、F 的 p50=143(贴右端),所以两谷几乎总是分得很开。
   「潮宽」不是一个有信息的量,它是被窗口两端夹出来的近常数。

2. 唯一确立的提纯结果:整个 M 子树可以删掉。a_no_rate 在同一半衰期下与原式持平
```

**10-04 15:02 · Bash** — Count lines of brief output

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F115_all_tide_mean_30 2>&1 | wc -l
```

```
     285
```

**10-04 15:02 · Bash** — Get the rest of brief output

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F115_all_tide_mean_30 2>&1 | tail -100
```

```
### 2026-10-04 15:00 [主研] 第 2 轮:裁决 R1 —— H2/H3/H7b 被否定、H1/H5 被支持、H4 改写;确立唯一的提纯结果(删整个 ÷M 子树);下 R2 工单(增量权重曲线 + 固定子窗口零假设)

看到了什么(R1 的 S1_anatomy 8 变体 + x1_anat_mfi 都 exit 0,结果卡已交):

1. ÷M 在秩空间接近恒等变换,H2 和 H3 一起死,而且 H3 的前提本身就是错的。
   x1 量到 M 的 p1/p50/p99 = 24/95/177、M<=20 只占 0.61%,根本没有 04_grammar 性质 3 预言的
   「跨三个数量级的倒数放大器」。三条独立证据:rank_corr(N,L)=+0.9582、
   rank_corr(O, cross_mean(M,20))=+0.0096、a_width_only 的 rIC 只有 +0.0024 且与 v_base 相关 -0.00、
   dist 0.23 连门槛都不过。H3 的直接检验是平的(按 O 分桶 median(M)=94/95/94)。
   机制上讲得通:argmin 找的是最低点,而日内量能曲线的最低点天然靠两头 ——
   x1 量到 I 的 p50=22(贴左端)、F 的 p50=143(贴右端),所以两谷几乎总是分得很开。
   「潮宽」不是一个有信息的量,它是被窗口两端夹出来的近常数。

2. 唯一确立的提纯结果:整个 M 子树可以删掉。a_no_rate 在同一半衰期下与原式持平
   (hl10 +5.9/+5.6、hl20 +6.4/+4.6),各自最优半衰期下 +6.4%/+2.0% 对 +5.6%/+0.2%,
   rIC 两段都更高,换手 3.7% 对 5.1%,rank_corr 0.84(>=0.8 仍是同一条因子)。
   表达式 815->539 字符(-34%)。但「严格优于原式」只算合理但未坐实(valid 的 +1.8pp 在 ±3pp 噪声带内);
   已确立的是「÷M 这个节点没有贡献」。

3. 我自己用算术补上了工具一直没打印的那一列,结果把 H7b 推翻了。主表 9 个变体的
   (Lgross-Lnet)/(LTO*252) 全落在 29.0~31.0 bp(均值 30.0 = 2 x cost_per_side),于是固定半衰期表的
   Lgross 可以反推:v_base 在 hl 0/2/5/10/20 下 Lgross = +9.7/+9.2/+9.2/+9.4/+7.6% —— 是平的。
   自检:hl10 反推 +9.4% 与主表打印值完全一致。所以平滑一点没有抬毛超额,它唯一的作用是把年化成本
   从 15.9% 压到 3.8%。上一轮写的「平滑把毛超额抬了五倍」是错的(它把 15bp 当成了单边总成本)。

4. H5 被支持并加强,而且加强的方式是新的:valid 的崩塌是毛崩塌(v_base Lgross 9.4%->4.1%),
   不是成本、不是半衰期;而同一段 k_stdamt_mean30 的毛多头腿反而 15.2%->24.4%。
   所以 valid 不是「A 股纯多头普遍难做」的时期,是这条因子自己衰减。6 个符号一致的变体
   无一例外 train +1.5~+6.8% / valid -1.8~+2.0%,没有任何结构改动能把 valid 抬到 +8% 以上。

5. H6 要问的问题被改写了。「它就是已知家族」是假的 —— 与 4 条 known_* 的相关只有 0.23~0.28。
   真正的问题是「这个基本正交、却弱得多的东西掺进已知家族有没有增量」。这只能靠权重曲线和残差量,
   R1 没有做。

6. 两个意外:(a) a_abs 的 rIC 是全表最高(tr .0407 / va .0624,都高于 v_base),但 train 多头端是
   全档最差(Q10 -6.3%)—— 折叠量的极端档是垃圾,对只做多的用户不可用,而且 rank_corr 只有 0.40
   (是另一条因子),登记进 12_next 不追。(b) 「钱在空头腿」就是剖面不对称,算术能对上:
   Q10 +9.6% / Q1 -26.4% -> 9.6/36.0 = 26.7%,与 long_share 26.5% 吻合。

判断与决定:
- 这棵树的内部已经没有值得再问的问题了。任务清单上只剩两条没认真回答过:相对已知家族有没有增量,
  以及「潮汐定位」这前三层(约 90% 的复杂度)到底有没有用 —— R1 给的边际是 +1.6pp(tr)/+2.5pp(va)
  (正确的对照是 a_plain_ret 对 a_no_rate,不是对 v_base),两段同号但都在噪声带内。
- 所以 R2 = S2_increment(5 变体:a_fixwin95 / c_pure / k_stdamt_max9 / 两个混合体)
  + 脚本 increment.py(增量权重曲线 w=0..1 / 对已知家族的残差多头腿 / 封板票对空头腿的贡献 /
  H7b 的直接确认)。2 次服务器运行。
- 新立两条假设:H9(空头腿和用户表里 LS 2.29 被次日开盘买不进的票抬高 —— 用户做不了空,
  这是对用户最有用的一句话之一)、H10(潮汐定位只是平均意义上挑了一段 95 分钟的中段;
  a_fixwin95 = 固定子窗口 in_slice(Close,66,161) 是它的判别实验)。
- 预先登记了最终候选和判据(state.md §5.3 / §6 的 J1~J4),事前第一推荐是 k_stdamt_mean30
  而不是本因子 —— 这就是否定结论的具体形态。R3 直接进 (b) 读留出段。

决定不做的事:
- 不追 a_abs(事前选不出来的东西不能当候选);不调 in_local_mean 的 d(H2 死了之后它没有信息量);
  不再铺窗口邻域(20/30/60 已经平了);不碰 nt_*;不为了有个升华版去凑。
- 不重跑任何已经 exit 0 的 tag;不往 controls 里加东西(会让 all_controls 的 R² 与 S0/S1 不可比)。
- R2 之后不再加第四个实验阶段,轮次留给读留出段和成文。

## 工单与结果卡(`notes/F115_all_tide_mean_30/orders/`、`notes/F115_all_tide_mean_30/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F115_all_tide_mean_30.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_anatomy**(8 个变体):N = L x (1/M) 的三个通道里预测力在哪一个;拆掉潮汐定位之后还剩多少?
  a_no_rate、a_width_only、a_plain_ret、a_rank_pre、a_abs、a_win30、a_win60、k_stdamt_mean30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F115_all_tide_mean_30`)

- `S0_baseline`  10-04 12:01  1 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S0_baseline`
- `S1_anatomy`  10-04 14:09  8 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S1_anatomy`
- `x1_anat_mfi`(自写脚本的输出)  10-04 14:19  exit 0  → `logs/F115_all_tide_mean_30_x1_anat_mfi.log`

## 已写的 notes(`notes/F115_all_tide_mean_30/`)

- `01_expression.md`  3095 字节  10-04 13:02
- `02_operators.md`  13227 字节  10-04 13:03
- `03_decomposition.md`  6648 字节  10-04 13:04
- `04_grammar.md`  6261 字节  10-04 13:15
- `05_hypotheses.md`  16804 字节  10-04 14:44
- `06_baseline.md`  11268 字节  10-04 13:06
- `07_S1_anatomy.md`  16143 字节  10-04 14:50
- `07x_1_anat_mfi.md`  9404 字节  10-04 14:47
- `journal.md`  16725 字节  10-04 15:00
- `state.md`  28041 字节  10-04 14:59

## 自写的探针与分析脚本(`studies/F115_all_tide_mean_30/`)

- `anat_mfi.py`  10-04 14:17  F115 R1 / x1_anat_mfi: anatomy of N = L x (1/M) on the six raw daily panels.

## 结构化结果(`handoff/F115_all_tide_mean_30/results/`)

(还没有)
```

**10-04 15:02 · Bash** — List order and result card files

```bash
cd /Users/wxy/Desktop/Partura && ls notes/F115_all_tide_mean_30/orders/ notes/F115_all_tide_mean_30/results/
```

```
notes/F115_all_tide_mean_30/orders/:
R1.md
R2.md

notes/F115_all_tide_mean_30/results/:
R0.md
R1.md
```

10-04 15:02 · 读 `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/orders/R2.md`

**10-04 15:02 · Bash** — Check config tail, studies dir, notes dir, and server-side run list

```bash
cd /Users/wxy/Desktop/Partura && echo "--- config tail ---" && tail -60 configs/F115_all_tide_mean_30.yaml && echo "--- studies dir ---" && ls -la studies/F115_all_tide_mean_30/ && echo "--- notes dir ---" && ls -la notes/F115_all_tide_mean_30/ && echo "--- server list ---" && ./scripts/study.sh list F115_all_tide_mean_30 2>&1
```

```
--- config tail ---

# train + valid = 用户的训练段(utrain);holdout = 用户的测试段,只在最后读一次
splits:
  train:   ["20180102", "20211231"]
  valid:   ["20220101", "20230807"]
  utrain:  ["20180102", "20230807"]
  holdout: ["20230808", "20251231"]
  full:    ["20180102", "20251231"]
fit_split: train
user_split: utrain

# ---- 这一批共用的控制变量(都是日频、因果、只用到 t 日收盘)。按这棵树的嫌疑增删。
controls:
  ctl_amt:    "log(add(day_sum(Amt), 1))"                                  # 成交额水平
  ctl_price:  "log(day_last(Close))"                                       # 价格水平
  ctl_ivol:   "day_std(Ret)"                                               # 日内已实现波动
  ctl_range:  "div(sub(day_max(High), day_min(Low)), day_last(Close))"     # 日内振幅
  ctl_rev1:   "div(day_last(Close), ts_delay(day_last(Close), 1))"         # 当日收益(毛比值,秩等价)
  ctl_mom20:  "div(day_last(Close), ts_delay(day_last(Close), 20))"        # 20 日动量
  ctl_dvol20: "ts_stddev(div(day_last(Close), ts_delay(day_last(Close), 1)), 20)"   # 20 日日频波动
external_controls:
  ctl_cap:      /root/autodl-tmp/Partura/shared/log_float_cap.npy        # log 流通市值 —— 把"规模"和"成交活跃"分开
  ctl_turnrate: /root/autodl-tmp/Partura/shared/log_turnover_rate.npy    # log(成交额 / 流通市值)

# ---- 既往研究里确认过的家族,用来分辨"这是不是已知的东西换了个写法"
gates:
  known_amt_max9:    "cross_max(day_sum(Amt), 9)"          # F001:成交额水平 + 极值记忆
  known_stdamt_max9: "cross_max(day_std(Amt), 9)"          # F001 的蒸馏结果
  known_ivol_max9:   "cross_max(day_var(Ret), 9)"          # F001:日内波动 + 极值记忆
  known_stdamt_mean30: "cross_mean(day_std(Amt), 30)"      # B01 第一组里纯多头最好的两算子基准之一
corr_ids: [v_base, a_no_rate, a_width_only, a_plain_ret, a_rank_pre, a_abs, a_win30, a_win60, k_stdamt_mean30]
corr_with: [ctl_amt, ctl_cap, ctl_turnrate, ctl_ivol, ctl_dvol20, ctl_price, ctl_rev1, ctl_mom20,
            known_amt_max9, known_stdamt_max9, known_ivol_max9, known_stdamt_mean30]

diagnostics:
  decay:      [v_base]
  by_year:    [v_base]
  neutralise: [v_base, a_no_rate]
  profile:    [v_base, a_no_rate, a_rank_pre, a_abs, k_stdamt_mean30]
  conditional:
    - {factor: v_base, gate: ctl_cap, buckets: 5}
    - {factor: v_base, gate: ctl_amt, buckets: 5}

stages:
  - id: S0_baseline
    question: "Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?"
    variants:
      - {id: v_base, group: baseline, expr: "cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)", why: "原始表达式"}

  - id: S1_anatomy
    question: "N = L x (1/M) 的三个通道里预测力在哪一个;拆掉潮汐定位之后还剩多少?"
    variants:
      - {id: a_no_rate, group: ablate, expr: "cross_mean(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)", why: '去掉 ÷M。H3:若 1/M 只是在制造重尾、污染多头端,去掉它应恢复 valid 段 Q10 的单调性并抬高多头腿;若多头腿反而塌掉,则 1/M 就是信息所在(H2 的放量脉冲读法)'}
      - {id: a_width_only, group: isolate, expr: "cross_mean(sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), 20)", why: '只留几何通道 M,完全不碰价格。H2:若它单独就有可观 rIC 且与 v_base rank 相关 >= 0.3,这条因子本质是成交量形状因子、是 day_std(Amt) 家族的兄弟'}
      - {id: a_plain_ret, group: substitute, expr: "cross_mean(div(day_last(in_slice(Close, 31, 211)), day_first(in_slice(Close, 31, 211))), 20)", why: '零假设:把两个成交量谷换成切片的固定两端(day_first/day_last),整套 argmax/argmin 潮汐机械全部拆掉,只剩"10:01 到 14:31 的一段收益的 20 日均值"。H1:若它接近 v_base,这棵树绝大部分复杂度是装饰,因子只是个 20 日反转'}
      - {id: a_rank_pre, group: transform, expr: "cross_mean(cs_rank(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))))), 20)", why: '先做截面排序再取 20 日均值,等于保序去尾。H3:若多头端的问题只是 1/M 的重尾,去尾应当保住经济内容同时修好 Q10;注意现在的口径是先 EMA 再排序,所以这是一个真变体不是 no-op(playbook §3)'}
      - {id: a_abs, group: magnitude, expr: "cross_mean(abs_(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))))), 20)", why: '只留幅度不留符号。H4:N ~ sigma*M^(-1/2),若起作用的是强度而不是方向,这一条应当保住甚至更好,并与 ctl_ivol/ctl_range/known_stdamt_* 的相关明显高于 v_base;这是 playbook §6.5 要求的"用同样折叠过的量去比"'}
      - {id: a_win30, group: window, expr: "cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 30)", why: '把 20 日均值换成 30 日(库名 all_tide_mean_30 说的就是 30,而表达式实际写的是 20)。检验 20 是不是调出来的,同时检验"慢变特征"读法:若更长窗口不更差,支持它是特征暴露而不是事件信号'}
      - {id: a_win60, group: window, expr: "cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 60)", why: '同上,窗口拉到 60 日。与 a_win30 一起给出窗口邻域的形状:单峰在 20 说明被调过,平坦或向右上升说明是慢变特征'}
      - {id: k_stdamt_mean30, group: known, expr: "cross_mean(day_std(Amt), 30)", why: '用户指定的第二条已知家族基准,R0 的 digest 里没有打印出来(gates 和 corr_with 里都有它,两处输出都少了它)。把它提成一等变体,拿到它自己的多头腿数字和它与本因子的 rank 相关 —— H6 要用'}
--- studies dir ---
total 24
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:18 .
drwxr-xr-x@ 17 wxy  staff    544 Oct  4 14:18 ..
drwxr-xr-x@  3 wxy  staff     96 Oct  4 14:18 __pycache__
-rw-r--r--@  1 wxy  staff  10434 Oct  4 14:17 anat_mfi.py
--- notes dir ---
total 288
drwxr-xr-x@ 14 wxy  staff    448 Oct  4 14:59 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   3095 Oct  4 13:02 01_expression.md
-rw-r--r--@  1 wxy  staff  13227 Oct  4 13:03 02_operators.md
-rw-r--r--@  1 wxy  staff   6648 Oct  4 13:04 03_decomposition.md
-rw-r--r--@  1 wxy  staff   6261 Oct  4 13:15 04_grammar.md
-rw-r--r--@  1 wxy  staff  16804 Oct  4 14:44 05_hypotheses.md
-rw-r--r--@  1 wxy  staff  11268 Oct  4 13:06 06_baseline.md
-rw-r--r--@  1 wxy  staff  16143 Oct  4 14:50 07_S1_anatomy.md
-rw-r--r--@  1 wxy  staff   9404 Oct  4 14:47 07x_1_anat_mfi.md
-rw-r--r--@  1 wxy  staff  16725 Oct  4 15:00 journal.md
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:52 orders
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:26 results
-rw-r--r--@  1 wxy  staff  28041 Oct  4 14:59 state.md
--- server list ---
# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):
  S0_baseline            [partura exit 0 2026-10-05_03:01:31]  [有 JSON]
  S1_anatomy             [partura exit 0 2026-10-05_05:09:14]  [有 JSON]
  x1_anat_mfi            [partura exit 0 2026-10-05_05:19:10]
# 正在跑的:
  (无)
# 已把服务器上的 runs/F115_all_tide_mean_30/*.json 拉回本地
```

**10-04 15:02 · Bash** — Inspect S0_baseline.json top-level structure

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F115_all_tide_mean_30/S0_baseline.json'))
print(type(d), list(d.keys()) if isinstance(d, dict) else len(d))
"
```

```
<class 'dict'> ['factor_id', 'config', 'stages', 'provenance', 'view', 'label', 'cost_per_side', 'top_frac', 'fit_split', 'user_split', 'rank_by', 'halflives', 'device', 'splits_used', 'split_dates', 'results', 'errors', 'engine_timings', 'diagnostics', 'seconds', 'peak_anon_gb']
```

**10-04 15:02 · Bash** — Inspect results structure in S0_baseline.json

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F115_all_tide_mean_30/S0_baseline.json'))
res = d['results']
print(type(res), list(res.keys()) if isinstance(res, dict) else len(res))
import pprint
if isinstance(res, dict):
    k0 = list(res.keys())[0]
    pprint.pprint(res[k0])
"
```

```
<class 'dict'> ['v_base']
{'books': {'by_rank': {'long': {'hl': 10.0,
                                'splits': {'train': {'long_ann': 0.05571977138691134,
                                                     'long_gross_ann': 0.09436048525338275,
                                                     'long_mdd': -0.06575637459487427,
                                                     'long_share': 0.26551082067306114,
                                                     'long_sharpe': 1.2062110340824914,
                                                     'long_turnover': 0.05111205537893046,
                                                     'ls_ann': 0.14218237030914097,
                                                     'ls_gross_sharpe': 3.159856221217778,
                                                     'ls_mdd': -0.04525906921202555,
                                                     'ls_sharpe': 2.529024276825985,
                                                     'ls_turnover': 0.04697585925525725,
                                                     'n_days': 973,
                                                     'short_gross_ann': 0.2610317545588481},
                                           'valid': {'long_ann': 0.0024720910931476845,
                                                     'long_gross_ann': 0.04107489501903494,
                                                     'long_mdd': -0.06320780840177617,
                                                     'long_share': 0.1317837414726888,
                                                     'long_sharpe': 0.043678178272867726,
                                                     'long_turnover': 0.05106190995487731,
                                                     'ls_ann': 0.12036522433727122,
                                                     'ls_gross_sharpe': 2.2892656727279386,
                                                     'ls_mdd': -0.04923986668093493,
                                                     'ls_sharpe': 1.7675504135422846,
                                                     'ls_turnover': 0.04692700885558922,
                                                     'n_days': 386,
                                                     'short_gross_ann': 0.2706091910451584}}},
                       'ls': {'hl': 10.0,
                              'splits': {'train': {'long_ann': 0.05571977138691134,
… (300 行略) …
                      'n_days': 973,
                      'rank_ic': 0.03735984512146503,
                      'rank_ic_t': 14.987561052352552,
                      'rank_ic_traded': 0.02977088238436819,
                      'rank_icir': 0.48047914837441746,
                      'sign': -1.0},
            'valid': {'coverage': 0.8946648005876163,
                      'coverage_labelled': 0.99953254311404,
                      'ic': 0.024086479086135607,
                      'ic_pos': 0.6036269430051814,
                      'ic_t': 5.4300714004079005,
                      'icir': 0.27638335720276846,
                      'n_days': 386,
                      'rank_ic': 0.034652893351363186,
                      'rank_ic_t': 7.276723281614222,
                      'rank_ic_traded': 0.03358254838032529,
                      'rank_icir': 0.37037546317660003,
                      'sign': -1.0}},
 'stage': 'S0_baseline',
 'why': '原始表达式'}
```

**10-04 15:03 · Bash** — Check sign and halflife for a_no_rate and k_stdamt_mean30 in S1_anatomy.json

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F115_all_tide_mean_30/S1_anatomy.json'))
res = d['results']
print(list(res.keys()))
for k in ['a_no_rate','k_stdamt_mean30']:
    r = res[k]
    print(k, 'sign=', r.get('sign'), 'sign_user=', r.get('sign_user'), 'hl_long=', r['books'].get('hl_long'), 'hl_ls=', r['books'].get('hl_ls'))
"
```

```
['a_no_rate', 'a_width_only', 'a_plain_ret', 'a_rank_pre', 'a_abs', 'a_win30', 'a_win60', 'k_stdamt_mean30']
a_no_rate sign= -1.0 sign_user= None hl_long= 20.0 hl_ls= 20.0
k_stdamt_mean30 sign= -1.0 sign_user= None hl_long= 0.0 hl_ls= 0.0
```

10-04 15:03 · 读 `/Users/wxy/Desktop/Partura/configs/F115_all_tide_mean_30.yaml`

10-04 15:03 · 读 `/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/anat_mfi.py`

**10-04 15:03 · Bash** — Locate study_tools.py source file

```bash
cd /Users/wxy/Desktop/Partura && find . -name "study_tools.py" -not -path "*/node_modules/*" 2>/dev/null
```

```
./partura/study_tools.py
```

**10-04 15:03 · Bash** — Count lines in study_tools.py

```bash
cd /Users/wxy/Desktop/Partura && wc -l partura/study_tools.py
```

```
     155 partura/study_tools.py
```

10-04 15:03 · 读 `/Users/wxy/Desktop/Partura/partura/study_tools.py`

**10-04 15:03 · Bash** — Locate books.py module

```bash
cd /Users/wxy/Desktop/Partura && find . -iname "books.py" | grep -v node_modules
```

```
./partura/books.py
```

10-04 15:03 · 读 `/Users/wxy/Desktop/Partura/partura/books.py`

**10-04 15:04 · Bash** — Read diagnose.py for rank_rows, pair_rank_corr, sign_from, ic_row

```bash
cd /Users/wxy/Desktop/Partura && wc -l partura/diagnose.py && sed -n '1,400p' partura/diagnose.py
```

```
     366 partura/diagnose.py
"""Diagnostics that turn a panel into evidence about a hypothesis.

AlphaCube already answers "how good is it" (IC, ICIR, turnover, net Sharpe).
Partura needs to answer "where does it come from", so this module adds the
discriminating measurements AlphaCube has no reason to own:

* ``neutralise``        -- daily cross-sectional residual after regressing the
  factor on control panels (size / price / volatility / reversal / momentum).
  If the alpha survives, the controls do not explain it; if it dies, they do.
* ``conditional_ic``    -- the IC of A inside quantile buckets of B.  This is
  what separates "B is a regime gate" from "B is a second, additive signal".
* ``decay``             -- IC across forward horizons: when the alpha starts,
  peaks and dies.
* ``by_year``           -- one row per calendar year, after cost.
* ``extreme_day_dependence`` -- net Sharpe after dropping the biggest P&L days.
* ``pair_rank_corr``    -- mean daily Spearman between two panels, i.e. whether
  a "variant" is actually a different factor or the same one rewritten.

Every metric that involves money is reported after cost.  The direction of a
factor is never re-chosen out of sample: ``metric_row`` takes the sign as an
argument so a sign fitted on train can be applied unchanged to valid/holdout.
"""

from __future__ import annotations

import warnings
from typing import Dict, List, Optional, Sequence, Tuple

from .bridge import ensure_alphacube_on_path
… (317 行略) …
def rank_corr_matrix(panels: Dict[str, np.ndarray]) -> Dict[str, Dict[str, float]]:
    names = list(panels)
    ranks = {n: rank_rows(np.asarray(panels[n], dtype=np.float64)) for n in names}
    out: Dict[str, Dict[str, float]] = {}
    # `out[a] = {}` used to reset a row that earlier pairs had already written
    # into, so the lower triangle came back empty (and half the report's table
    # read NaN). Build every row first, then fill both triangles.
    out = {n: {} for n in names}
    for i, a in enumerate(names):
        for b in names[i:]:
            v = nanmean_quiet(cs_pearson(ranks[a], ranks[b]))
            out[a][b] = v
            out[b][a] = v
    return out


__all__ = ["COST_PER_SIDE", "TURNOVER_CAP", "TOP_FRAC", "ic_series", "rank_ic_series", "sign_from",
           "rank_rows", "ic_row", "distinct_fraction", "nanmean_quiet",
           "metric_row", "neutralise", "conditional_ic", "decay", "by_year", "smoothing_sweep",
           "extreme_day_dependence", "pair_rank_corr", "rank_corr_matrix"]
```

**10-04 15:05 · Bash** — Inspect rank_rows implementation in alphacube.metrics

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
from partura.bridge import ensure_alphacube_on_path
ensure_alphacube_on_path()
import alphacube.metrics as m
import inspect
print(inspect.getsource(m.rank_rows))
" 2>&1 | head -60
```

```
def rank_rows(x: np.ndarray) -> np.ndarray:
    """Per-row average ranks (ties averaged) of the finite cells, NaN elsewhere.
    pandas ranks inf as a value -- the largest one -- so an inf cell used to get
    rank n here while every IC and every book in this module skips it."""
    x = np.asarray(x, dtype=np.float64)
    return pd.DataFrame(np.where(np.isfinite(x), x, np.nan)).rank(axis=1).to_numpy()
```

**10-04 15:08 · 改文件** `/Users/wxy/Desktop/Partura/configs/F115_all_tide_mean_30.yaml`

```
- corr_ids: [v_base, a_no_rate, a_width_only, a_plain_ret, a_rank_pre, a_abs, a_win30, a_win60, k_stdamt_mean30]
+ corr_ids: [v_base, a_no_rate, a_width_only, a_plain_ret, a_rank_pre, a_abs, a_win30, a_win60, k_stdamt_mean30, a_fixwin95, c_pure, k_stdamt_max9, m_blend_base_k30, m_blend_pure_k30]
```

**10-04 15:08 · 改文件** `/Users/wxy/Desktop/Partura/configs/F115_all_tide_mean_30.yaml`

```
-   by_year:    [v_base]
  neutralise: [v_base, a_no_rate]
  profile:    [v_base, a_no_rate, a_rank_pre, a_abs, k_stdamt_mean30]
+   by_year:    [v_base, c_pure, k_stdamt_mean30, m_blend_pure_k30]
  neutralise: [v_base, a_no_rate]
  profile:    [v_base, a_no_rate, a_rank_pre, a_abs, k_stdamt_mean30, a_fixwin95, c_pure, k_stdamt_max9, m_blend_base_k30, m_blend_pure_k30]
```

**10-04 15:08 · 改文件** `/Users/wxy/Desktop/Partura/configs/F115_all_tide_mean_30.yaml`

```
-       - {id: k_stdamt_mean30, group: known, expr: "cross_mean(day_std(Amt), 30)", why: '用户指定的第二条已知家族基准,R0 的 digest 里没有打印出来(gates 和 corr_with 里都有它,两处输出都少了它)。把它提成一等变体,拿到它自己的多头腿数字和它与本因子的 rank 相关 —— H6 要用'}
+       - {id: k_stdamt_mean30, group: known, expr: "cross_mean(day_std(Amt), 30)", why: '用户指定的第二条已知家族基准,R0 的 digest 里没有打印出来(gates 和 corr_with 里都有它,两处输出都少了它)。把它提成一等变体,拿到它自己的多头腿数字和它与本因子的 rank 相关 —— H6 要用'}

  - id: S2_increment
    question: "对只能做多的用户,这条因子掺进已知家族有没有增量?潮汐定位是不是只等于一个固定子窗口?"
    variants:
      - {id: a_fixwin95, group: substitute, expr: "cross_mean(div(day_last(in_slice(Close, 66, 161)), day_first(in_slice(Close, 66, 161))), 20)", why: '固定子窗口零假设(H10)。R1 量到 I 的 p50=22、F 的 p50=143、M 的 p50=95,两谷几乎总是贴着窗口两端。把两个谷换成一个固定的 95 分钟中段(全局分钟 66..161,即原切片的局部 35..130,中心 82.5 = 两谷中心的中位数、长度 95 = M 的中位数):若它追上 a_no_rate,潮汐定位是纯装饰、整棵 argmax/argmin 子树可以删;若它落回 a_plain_ret 附近,定位带来的是真的逐股票-日信息'}
      - {id: c_pure, group: distilled, expr: "cross_mean(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_me
… (1921 字符略) …
cal_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)), cs_rank(cross_mean(day_std(Amt), 30)))", why: '同上,但用提纯版(删掉 M 子树)代替原式。若两个混合体的差别可以忽略,再一次说明 ÷M 这个节点没有内容'}
```

**10-04 15:08 · Bash** — Validate config expressions for F115_all_tide_mean_30

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh check F115_all_tide_mean_30 2>&1
```

```
PROBLEM S0_baseline/v_base: contains a LOOKAHEAD operator
PROBLEM S1_anatomy/a_no_rate: contains a LOOKAHEAD operator
PROBLEM S1_anatomy/a_width_only: contains a LOOKAHEAD operator
PROBLEM S1_anatomy/a_rank_pre: contains a LOOKAHEAD operator
PROBLEM S1_anatomy/a_abs: contains a LOOKAHEAD operator
PROBLEM S1_anatomy/a_win30: contains a LOOKAHEAD operator
PROBLEM S1_anatomy/a_win60: contains a LOOKAHEAD operator
PROBLEM S2_increment/c_pure: contains a LOOKAHEAD operator
note: S2_increment/c_pure is the same tree as S1_anatomy/a_no_rate (evaluated once)
PROBLEM S2_increment/m_blend_base_k30: contains a LOOKAHEAD operator
PROBLEM S2_increment/m_blend_pure_k30: contains a LOOKAHEAD operator
15/25 OK
```

**10-04 15:09 · Bash** — Confirm S2_increment has not already been run on server

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh list F115_all_tide_mean_30 2>&1
```

```
# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):
  S0_baseline            [partura exit 0 2026-10-05_03:01:31]  [有 JSON]
  S1_anatomy             [partura exit 0 2026-10-05_05:09:14]  [有 JSON]
  x1_anat_mfi            [partura exit 0 2026-10-05_05:19:10]
# 正在跑的:
  (无)
# 已把服务器上的 runs/F115_all_tide_mean_30/*.json 拉回本地
```

**10-04 15:09 · agent 的话**

Confirmed S2_increment has not run yet. Launching it now.

**10-04 15:09 · Bash** — Launch S2_increment stage run on server

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh run F115_all_tide_mean_30 S2_increment S2_increment 2>&1
```

```
started F115_all_tide_mean_30/S2_increment: stages S2_increment
```

**10-04 15:09 · Bash** — Wait for S2_increment run to finish (up to 540s per call)

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh wait F115_all_tide_mean_30 S2_increment 2>&1
```

```
[runner] 06:11:54 diagnostics: conditional IC (of the traded signal; positive = works)
[runner] 06:12:02 diagnostics: rank correlation of traded signals (14 variants + 12 controls)
[runner] wrote /root/autodl-tmp/Partura/runs/F115_all_tide_mean_30/S2_increment.json (218.7s, peak anon 4.77 GiB)
[partura exit 0 2026-10-05_06:13:33]

===== F115_all_tide_mean_30  [S2_increment.json]  1942d x 5220s  splits ['train', 'valid', 'utrain']  fit=train  device=cuda  218.7s  peak anon 4.77G =====

决策口径(方向/半衰期在 train 上定; valid 没见过)—— 按多头腿选:
variant              sgn | hlL   Lnet tr   Lnet va  Lshp tr  Lshp va  Lgross tr  Lgross va   LTO | hlS   LS tr   LS va  short tr
a_fixwin95             - |  10     +4.3%     -9.7%    +0.74    -1.40      +8.0%      -5.9%  4.9% |  20   +2.02   +0.42    +20.2%
c_pure                 - |  20     +6.4%     +2.0%    +1.37    +0.37      +9.1%      +4.8%  3.7% |  20   +2.47   +1.74    +24.1%
k_stdamt_max9          - |   5    +13.7%    +22.2%    +1.99    +3.59     +17.1%     +25.1%  4.5% |   0   +2.47   +4.44    +37.7%
m_blend_base_k30       - |   5     +9.6%    +17.7%    +1.55    +3.26     +13.3%     +21.4%  4.9% |   1   +2.44   +3.60    +35.6%
m_blend_pure_k30       - |   5    +10.9%    +17.1%    +1.76    +3.12     +14.6%     +20.8%  4.9% |   1   +2.40   +3.55    +35.3%

variant                rIC tr   rIC va  rICtraded tr  rICtraded va    cov   dist
a_fixwin95            +0.0275  +0.0206       +0.0206       +0.0185   1.00   0.97
c_pure                +0.0388  +0.0357       +0.0286       +0.0353   1.00   1.00
k_stdamt_max9         +0.0484  +0.0671       +0.0398       +0.0609   1.00   1.00
m_blend_base_k30      +0.0457  +0.0590       +0.0360       +0.0535   1.00   0.81
m_blend_pure_k30      +0.0466  +0.0596       +0.0365       +0.0542   1.00   0.80
  (rIC = 原始日频面板的 rank IC; rICtraded = 平滑后实际交易信号的; cov ≥ 0.95、dist ≥ 0.5 是用户的两道门槛)

固定半衰期下的 train 表现(结构之间先在同一半衰期下比;Lnet = 多头腿净超额, Lshp = 纯多头夏普):
variant                hl0 Lnet   Lshp  LTO   hl2 Lnet   Lshp  LTO   hl5 Lnet   Lshp  LTO  hl10 Lnet   Lshp  LTO  hl20 Lnet   Lshp  LTO
a_fixwin95                -6.2%  -0.95  20%      +1.0%  +0.16   9%      +2.8%  +0.46   7%      +4.3%  +0.74   5%      +3.8%  +0.70   3%
c_pure                    -5.9%  -1.02  21%      +1.0%  +0.19  10%      +3.7%  +0.72   7%      +5.9%  +1.18   5%      +6.4%  +1.37   4%
k_stdamt_max9             +9.3%  +1.37  10%     +12.6%  +1.85   6%     +13.7%  +1.99   5%     +13.1%  +1.89   3%     +12.2%  +1.75   2%
m_blend_base_k30          +6.7%  +1.12  14%      +9.3%  +1.52   7%      +9.6%  +1.55   5%      +9.6%  +1.53   4%      +8.6%  +1.34   3%
m_blend_pure_k30          +6.5%  +1.08  14%     +10.3%  +1.70   7%     +10.9%  +1.76   5%      +9.9%  +1.58   4%      +8.6%  +1.35   3%
分位超额 a_fixwin95 [train] Q1..Q10(Q10 = 多头端): -21.3% -7.1% -1.5% -0.5% +1.4% +2.7% +4.2% +5.2% +8.5% +8.4%
分位超额 a_fixwin95 [valid] Q1..Q10(Q10 = 多头端): -20.5% -4.9% -1.2% +5.8% +4.0% +5.8% +8.0% +7.5% +1.7% -6.1%
分位超额 c_pure [train] Q1..Q10(Q10 = 多头端): -24.2% -7.7% -2.9% +1.6% +2.3% +4.5% +4.0% +6.2% +6.9% +9.3%
分位超额 c_pure [valid] Q1..Q10(Q10 = 多头端): -24.2% -9.6% -4.2% +1.0% +3.7% +5.5% +7.0% +7.9% +7.7% +5.3%
分位超额 k_stdamt_max9 [train] Q1..Q10(Q10 = 多头端): -26.0% -17.2% -6.5% -2.8% +1.3% +4.5% +7.6% +9.4% +12.0% +17.7%
分位超额 k_stdamt_max9 [valid] Q1..Q10(Q10 = 多头端): -39.8% -22.0% -11.0% -5.1% -0.8% +5.5% +11.2% +12.6% +22.1% +27.3%
分位超额 m_blend_base_k30 [train] Q1..Q10(Q10 = 多头端): -28.2% -8.4% -3.3% -3.3% +2.8% +2.7% +5.3% +8.1% +10.6% +13.7%
分位超额 m_blend_base_k30 [valid] Q1..Q10(Q10 = 多头端): -33.7% -17.4% -8.4% -5.2% +0.3% +2.1% +11.1% +12.3% +16.0% +22.9%
分位超额 m_blend_pure_k30 [train] Q1..Q10(Q10 = 多头端): -26.8% -10.0% -3.0% -2.2% +1.1% +3.0% +5.2% +8.6% +9.0% +15.2%
分位超额 m_blend_pure_k30 [valid] Q1..Q10(Q10 = 多头端): -34.5% -16.6% -10.4% -2.2% -1.3% +3.1% +9.2% +12.3% +17.8% +22.7%
条件 IC v_base|ctl_cap(分桶变量从低到高): Q1 +0.0328  Q2 +0.0317  Q3 +0.0368  Q4 +0.0307  Q5 +0.0189
条件 IC v_base|ctl_amt(分桶变量从低到高): Q1 +0.0167  Q2 +0.0149  Q3 +0.0184  Q4 +0.0251  Q5 +0.0391

与 v_base 的日截面 rank 相关(fit 段, 实际交易信号; |.|>=0.95 = 同一因子族): a_win30 +0.95  a_no_rate +0.84  c_pure +0.84  a_win60 +0.81  a_rank_pre +0.78  m_blend_base_k30 +0.70  a_plain_ret +0.70  m_blend_pure_k30 +0.65  a_fixwin95 +0.54  a_abs +0.40  ctl_dvol20 -0.31  known_ivol_max9 -0.28  k_stdamt_max9 +0.28  k_stdamt_mean30 +0.26  known_stdamt_mean30 -0.26  ctl_turnrate -0.26  known_stdamt_max9 -0.24  known_amt_max9 -0.23  ctl_mom20 -0.22  ctl_ivol -0.21  ctl_amt -0.20  ctl_rev1 +0.03  ctl_cap +0.02  ctl_price -0.02  a_width_only -0.00
逐年 c_pure: 2018 Lnet +7.8% LS +3.09  2019 Lnet +13.4% LS +4.47  2020 Lnet +5.2% LS +1.63  2021 Lnet -1.3% LS +1.79  2022 Lnet +0.9% LS +1.99  2023 Lnet +3.6% LS +1.44
逐年 m_blend_pure_k30: 2018 Lnet +17.4% LS +3.81  2019 Lnet +10.9% LS +2.59  2020 Lnet +1.1% LS +0.71  2021 Lnet +13.7% LS +2.28  2022 Lnet +18.0% LS +3.67  2023 Lnet +15.3% LS +2.79

📝 往下做之前先记日志(研究随时可能中断、换人或换模型接手;没落盘的判断会丢):
   ./scripts/study.sh note F115_all_tide_mean_30 "<一句话:这次看到了什么>" <<'EOF'
   这次结果说明什么(带关键数字)/ 哪条假设因此变了 / 下一步打算做什么、为什么
   EOF
   并更新 notes/F115_all_tide_mean_30/state.md(研究现状:中间结果 / 逻辑 / 假设表 / 候选 / 后面的思路;格式见 docs/study_playbook.md §7)。
```

**10-04 15:14 · Bash** — Inspect by_year diagnostics structure in S2_increment.json

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F115_all_tide_mean_30/S2_increment.json'))
diag = d.get('diagnostics', {})
print('diagnostics keys:', list(diag.keys()))
by = diag.get('by_year')
print(type(by))
if isinstance(by, dict):
    print('by_year ids:', list(by.keys()))
elif isinstance(by, list):
    print('by_year list len:', len(by))
    for item in by[:3]:
        print(item if not isinstance(item, dict) else list(item.keys()))
"
```

```
diagnostics keys: ['by_year', 'by_year_scope', 'conditional', 'rank_corr_train', 'rank_corr_on']
<class 'dict'>
by_year ids: ['c_pure', 'm_blend_pure_k30']
```

**10-04 15:14 · Bash** — Check by_year_scope and errors fields in S2_increment.json

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F115_all_tide_mean_30/S2_increment.json'))
print('by_year_scope:', d['diagnostics'].get('by_year_scope'))
print('errors:', d.get('errors'))
print()
print('results keys:', list(d.get('results', {}).keys()))
"
```

```
by_year_scope: ['20180102', '20230807']
errors: {}

results keys: ['a_fixwin95', 'c_pure', 'k_stdamt_max9', 'm_blend_base_k30', 'm_blend_pure_k30']
```

**10-04 15:14 · Bash** — Find how PanelSet stores dates

```bash
cd /Users/wxy/Desktop/Partura && grep -n "self.dates" partura/panels.py | head -20
```

```
172:        self.dates: List[str] = list(self.view.dates[self.trim:])
174:        self.years = np.asarray([d[:4] for d in self.dates])
216:        raw = f"{self.store_path}|{self.start}|{self.end}|{len(self.symbols)}|{self.dates[0]}|{self.dates[-1]}"
258:        if a.shape != (len(self.dates), len(self.symbols)):
259:            raise ValueError(f"{path}: shape {a.shape} != view {(len(self.dates), len(self.symbols))}")
417:        d = np.asarray(self.dates)
```

**10-04 15:15 · Bash** — Find where by_year diagnostic is invoked in the runner

```bash
cd /Users/wxy/Desktop/Partura && grep -rn "by_year" partura/*.py scripts/*.py 2>/dev/null | grep -v "^partura/diagnose.py"
```

```
partura/remote_tools.py:148:    for sec in ("decay", "by_year", "neutralise", "profile"):
partura/runner.py:179:        if use_holdout or vid in profile_ids or vid in (diag_cfg.get("by_year") or []):
partura/runner.py:234:        want = [v for v in ok if v in traded_full and (use_holdout or v in (diag_cfg.get("by_year") or []))]
partura/runner.py:236:            _say(f"diagnostics: by_year ({len(want)} variants)")
partura/runner.py:249:            diag["by_year"] = rows_y
partura/runner.py:250:            diag["by_year_scope"] = [ps.dates[scope.start], ps.dates[scope.stop - 1]]
partura/report_legacy.py:125:    out["by_year_scope"] = d.get("by_year_scope")
partura/report_legacy.py:134:    if d.get("by_year"):
partura/report_legacy.py:135:        for vid, rows in d["by_year"].items():
partura/report_legacy.py:141:            out[f"by_year::{vid}"] = "\n".join(lines)
partura/report_legacy.py:260:    if "by_year::" + base_id in diag:
partura/report_legacy.py:262:                  for v, rr2 in (rr.get("diagnostics", {}).get("by_year") or {}).items()
partura/report_legacy.py:265:        L += [f"**逐年({rng},方向按训练段固定)**", "", diag["by_year::" + base_id], ""]
partura/report.py:169:def by_year_table(by_year: Dict[str, list], ids: Sequence[str]) -> str:
partura/report.py:170:    ids = [i for i in ids if i in by_year and by_year[i]]
partura/report.py:173:    years = [r["year"] for r in by_year[ids[0]]]
partura/report.py:176:        rows = {r["year"]: r for r in by_year[vid]}
partura/report.py:314:    by_year = diag.get("by_year") if isinstance(diag.get("by_year"), dict) else {}
partura/report.py:315:    if base_id in by_year:
partura/report.py:316:        L += ["**逐年**(实际交易的信号)", "", by_year_table(by_year, [base_id]), ""]
partura/report.py:393:        yt = by_year_table(by_year, finals)
partura/report.py:415:__all__ = ["build", "SECTIONS", "stage_table", "user_table", "fixed_hl_table", "by_year_table"]
scripts/new_study.py:75:  by_year:    [v_base]
scripts/summarize.py:146:    for vid, rows in (diag.get("by_year") or {}).items():
```

10-04 15:15 · 读 `/Users/wxy/Desktop/Partura/partura/runner.py`

10-04 15:15 · 读 `/Users/wxy/Desktop/Partura/partura/runner.py`

10-04 15:16 · 读 `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/results/R1.md`

**10-04 15:16 · Bash** — Read the end of 05_hypotheses.md (R1 裁决 section)

```bash
cd /Users/wxy/Desktop/Partura && sed -n '1,400p' notes/F115_all_tide_mean_30/05_hypotheses.md | tail -150
```

```
  (`04_grammar.md` 性质 4)。预测力主要来自动量/反转族,潮汐定位只是给这段收益挑了个起止点。
- **预测**:(a) 零假设 `a_plain_ret`(把两个谷换成窗口两端的固定时刻)应保住相当一部分 rIC 与
  多头腿;(b) `rank_corr(v_base, ctl_mom20)` 是全部控制变量里最大的 —— **已经对上**(原始面板
  +0.44、交易信号 −0.39、单变量 R² 0.156);(c) 对 `ctl_mom20` 中性化应明显削掉 rIC 和毛超额 ——
  **部分对上**(rIC 0.0298→0.0237、Lgross 9.4%→6.4%)。
- **能杀死它的实验**:`S1_anatomy` 的 `a_plain_ret`。若 `a_plain_ret` 的 rIC 和多头腿都远弱于
  `v_base`,且 `rank_corr(v_base, a_plain_ret) < 0.5`,则 H1 不足以解释**全部**,只是一个分量。
- **状态**:**未验证**(相关性证据一致,但相关不等于「可替代」;必须靠零假设直接比)。

## H2 · 它是一个成交量形状因子,是 day_std(Amt) 家族的兄弟

- **内容**:信号主要在几何通道 `M`(两谷间隔)里,价格只是给它贴了个符号。放量脉冲让 `M` 变小,
  而放量脉冲同时就是让 `day_std(Amt)` 变大的东西(`04_grammar.md` §4)。
- **预测**:`a_width_only = cross_mean(M,20)` 单独就能拿到 `v_base` 相当比例的 rIC;
  `rank_corr(v_base, a_width_only)` 高;`a_width_only` 与 `known_stdamt_*` 的相关明显高于 `v_base` 的。
- **能杀死它**:`a_width_only` 的 rIC 接近 0、且与 `v_base` 的 rank 相关低(< 0.3)。
- **状态**:**未验证**。已知家族相关只有 ±0.24~0.25,不算高,所以这条的先验**不如 H1**;
  但它是唯一能解释「为什么一个纯位置量会和成交额族沾亲」的通道,必须量。

## H3 · 多头端是被 `1/M` 的重尾污染的(**最有建设性的一条**)

- **内容**:`M` 小的那些股票-日,`|N|` 被放大到几个数量级之上,于是因子的极端分位**不是**经济意义
  上最极端的票,而是「两谷恰好挨在一起」的退化样本。
- **预测**:(a) 因子极端分位里 `M` 的中位数显著小于全样本中位数;(b) 这正好解释 valid 段
  **Q10(+4.5%) 低于 Q9(+8.7%)、不是全档最高**,而 train 段单调(`06_baseline.md` 第 4 节)
  —— 对只买前 10% 的用户,这是致命的那一处;(c) 去掉 `÷M`(`a_no_rate`)或先截面排序去尾
  (`a_rank_pre`)应当恢复 Q10 的单调性,并抬高 valid 多头腿。
- **能杀死它**:脚本量出极端分位里 `M` 的中位数与全样本相当;且 `a_no_rate`/`a_rank_pre` 的
  Q10 仍低于 Q9。
- **状态**:**未验证**。这是 R1 里唯一可能直接改善用户关心的那个数字的假设,所以 `x1_anat_mfi`
… (100 行略) …
  而不是一个很大的正收益 → 空头腿虚高(playbook §6.6 点名的那个坑;这条因子正是「极端日内收益」类)。
- **已经确立的那一半(算术,不需要实验)**:钱在空头腿**就是**分位剖面的不对称 ——
  train Q10 +9.6% / Q1 −26.4% → 9.6/(9.6+26.4) = **26.7%**,与 digest 的 `long_share 26.5%` 吻合。
  所以「为什么钱在空头腿」= 「为什么 Q1 那么深」。
- **预测**:用 `st.target(buyable=False)` 重算,`short` 毛超额与 `LS` 明显下降,**多头腿一个数都不变**。
- **能杀死它**:两种标签下 `short`/`LS` 基本相同。
- **为什么值得测**:用户最早那张表是按多空夏普排的(这条因子 `LS 2.29` 在里面排得不低),而用户做不了空。
  若 H9 被支持,报告里必须写明「它在原表里好看的那部分是买不进的票撑的」—— 这是对用户最有用的一句话之一。
- **状态**:**未验证**(R2 脚本第 3 件)。

### H10 · 「潮汐定位」只是平均意义上挑了一个更短的子窗口(装饰),没有逐股票-日的信息

- **内容**:H1 裁决里那个未坐实的 +1.6~2.5pp。`x1` 量到 `I` 几乎总贴窗口左端(p50 = 22)、
  `F` 几乎总贴右端(p50 = 143),两谷之间几乎总是 95 分钟左右。如果定位的全部作用就是
  「平均挑了一段 95 分钟的中段」,那么把窗口**固定**成那一段应当完全复现它。
- **预测**:`a_fixwin95`(固定子窗口 `in_slice(Close, 66, 161)`,长度 95 = `M` 的中位数、中心 = 两谷中心的
  中位数)的多头腿追上 `a_no_rate`(+6.4% / +2.0%)。
- **能杀死它**:`a_fixwin95` 明显差于 `a_no_rate`、接近或低于 `a_plain_ret`(+4.8% / −0.5%)
  → 定位带来的是真的逐股票-日信息,这棵树的前三层不是纯装饰。
- **状态**:**未验证**(R2 第 1 件)。
```

**10-04 15:21 · 写文件** `/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/increment.py`(17861 字符)

**10-04 15:21 · Bash** — Check increment.py compiles without syntax errors

```bash
cd /Users/wxy/Desktop/Partura && python3 -m py_compile studies/F115_all_tide_mean_30/increment.py && echo "COMPILE OK"
```

```
COMPILE OK
```

**10-04 15:21 · Bash** — Run script locally to exercise self-checks (a)/(b) before server exec

```bash
cd /Users/wxy/Desktop/Partura && python3 studies/F115_all_tide_mean_30/increment.py 2>&1 | head -80
```

```
Traceback (most recent call last):
  File "/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/increment.py", line 20, in <module>
    from partura.bridge import PARTURA_ROOT
ModuleNotFoundError: No module named 'partura'
```

**10-04 15:21 · Bash** — Run script locally with PYTHONPATH set to exercise self-checks before server exec

```bash
cd /Users/wxy/Desktop/Partura && PYTHONPATH=/Users/wxy/Desktop/Partura python3 studies/F115_all_tide_mean_30/increment.py 2>&1 | head -100
```

```
[self-check a] 通过:O=cross_mean(div(L,M),20)、P=cross_mean(L,20) 与 configs 逐字符相同(P 就是 O 去掉外层 ÷M)
[self-check b] 通过:rank_pct 的 ties/NaN、以及 w*rpX+(1-w)*rpK 的 NaN 自动传播 == '两腿都有值才参与'
Traceback (most recent call last):
  File "/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/increment.py", line 113, in <module>
    assert _rows_syn[0]["year"] == "2000" and _rows_syn[0]["days"] == 2
IndexError: list index out of range
```

10-04 15:22 · 读 `/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/increment.py`

**10-04 15:22 · 改文件** `/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/increment.py`

```
- _sm_syn = np.array([[1.0, 2.0, 3.0, 0.5],
                    [2.0, 1.0, 0.5, 3.0],
                    [3.0, 0.5, 1.0, 2.0],
                    [0.5, 3.0, 2.0, 1.0]])
_tgt_syn = np.array([[0.01, 0.02, -0.01, -0.02]] * 4)
_years_syn = np.array(["2000", "2000", "2001", "2001"])
_rows_syn = by_year_like_engine(_sm_syn, _tgt_syn, _ye
… (242 字符略) …
inite(_v):
        assert abs(_rows_syn[0][_k] - _v) < 1e-12, (_k, _rows_syn[0][_k], _v)
say("[self-check b] 通过:by_year_like_engine 在合成数据上与直接 bk.book_row(同一切片) 逐字段相同")
+ _rng = np.random.default_rng(0)
_NDAYS, _NSYM = 40, 6                                              # >=20 天/年,过 by_year_like_engine 自己的最小天数门槛
_sm_syn = _rng.normal(size=(_NDAYS, _NSYM))
_tgt_syn = _rng.normal(size=(_NDAYS, _NSYM)) * 0.02
_years_syn = np.array(["2000"] * 20 + ["2001"] * 20)
_rows_syn = by_year_like_engine(_sm_syn, _tgt_syn, _years_syn, slice(0, _NDAYS), 0.0015, 0.5)
_direct0 = bk.book_row(_sm_syn, _tgt_syn, slice(0, 20), 0.0015, 0.5)
_direct1 = bk.book_row(_sm_syn, _tgt_syn, slice(20, 40), 0.0015, 0.5)
assert len(_rows_syn) == 2
assert _rows_syn[0]["year"] == "2000" and _rows_syn[0]["days"] == 20
assert _rows_syn[1]["year"] == "2001" and _rows_syn[1]["days"] == 20
for _k, _v in _direct0.items():
    if isinstance(_v, float) and np.isfinite(_v):
        assert abs(_rows_syn[0][_k] - _v) < 1e-9, ("y2000", _k, _rows_syn[0][_k], _v)
for _k, _v in _direct1.items():
    if isinstance(_v, float) and np.isfinite(_v):
        assert abs(_rows_syn[1][_k] - _v) < 1e-9, ("y2001", _k, _rows_syn[1][_k], _v)
say("[self-check b] 通过:by_year_like_engine 在合成数据(2 年 x 20 天)上与直接 bk.book_row(同一切片) 逐字段相同"
    "(含最小 20 天/年的门槛,与 partura/runner.py 一致)")
```

**10-04 15:22 · Bash** — Recompile and rerun local self-checks after fixing synthetic by_year test

```bash
cd /Users/wxy/Desktop/Partura && python3 -m py_compile studies/F115_all_tide_mean_30/increment.py && PYTHONPATH=/Users/wxy/Desktop/Partura python3 studies/F115_all_tide_mean_30/increment.py 2>&1 | head -100
```

```
[self-check a] 通过:O=cross_mean(div(L,M),20)、P=cross_mean(L,20) 与 configs 逐字符相同(P 就是 O 去掉外层 ÷M)
[self-check b] 通过:rank_pct 的 ties/NaN、以及 w*rpX+(1-w)*rpK 的 NaN 自动传播 == '两腿都有值才参与'
[self-check b] 通过:by_year_like_engine 在合成数据(2 年 x 20 天)上与直接 bk.book_row(同一切片) 逐字段相同(含最小 20 天/年的门槛,与 partura/runner.py 一致)
Traceback (most recent call last):
  File "/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/increment.py", line 127, in <module>
    with Study(FID) as st:
  File "/Users/wxy/Desktop/Partura/partura/study_tools.py", line 61, in __enter__
    self.ps = PanelSet(STORE, SPLITS["full"][0], SPLITS["full"][1], warmup=int(self.cfg.get("warmup", 60)),
  File "/Users/wxy/Desktop/Partura/partura/panels.py", line 157, in __init__
    f = auto_gpu_fraction() if self.auto_fraction else float(gpu_fraction)
  File "/Users/wxy/Desktop/Partura/partura/panels.py", line 129, in auto_gpu_fraction
    free, total = torch.cuda.mem_get_info()
  File "/Users/wxy/Library/Python/3.9/lib/python/site-packages/torch/cuda/memory.py", line 833, in mem_get_info
    device = torch.cuda.current_device()
  File "/Users/wxy/Library/Python/3.9/lib/python/site-packages/torch/cuda/__init__.py", line 1026, in current_device
    _lazy_init()
  File "/Users/wxy/Library/Python/3.9/lib/python/site-packages/torch/cuda/__init__.py", line 363, in _lazy_init
    raise AssertionError("Torch not compiled with CUDA enabled")
AssertionError: Torch not compiled with CUDA enabled
```

10-04 15:22 · 读 `/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/increment.py`

**10-04 15:23 · Bash** — Confirm x2_increment tag has not been run yet

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh list F115_all_tide_mean_30 2>&1
```

```
# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):
  S0_baseline            [partura exit 0 2026-10-05_03:01:31]  [有 JSON]
  S1_anatomy             [partura exit 0 2026-10-05_05:09:14]  [有 JSON]
  S2_increment           [partura exit 0 2026-10-05_06:13:33]  [有 JSON]
  x1_anat_mfi            [partura exit 0 2026-10-05_05:19:10]
# 正在跑的:
  (无)
# 已把服务器上的 runs/F115_all_tide_mean_30/*.json 拉回本地
```

**10-04 15:23 · agent 的话**

Confirmed not yet run. Launching the analysis script now (2nd of the 2 allowed server runs for this order).

**10-04 15:23 · Bash** — Launch increment.py analysis script on server

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh exec F115_all_tide_mean_30 x2_increment increment.py 2>&1
```

```
started F115_all_tide_mean_30/x2_increment: increment.py
```

**10-04 15:23 · Bash** — Wait for x2_increment script to finish

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh wait F115_all_tide_mean_30 x2_increment 2>&1
```

```
  w=0 X=P valid: ref(st.books(K30)) Lnet=+22.33% Lshp=+3.462  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000

done
[partura exit 0 2026-10-05_06:27:28]
(no runs/F115_all_tide_mean_30/x2_increment.json — an exec job prints its own output; full log: logs/F115_all_tide_mean_30_x2_increment.log)
[self-check a] 通过:O=cross_mean(div(L,M),20)、P=cross_mean(L,20) 与 configs 逐字符相同(P 就是 O 去掉外层 ÷M)
[self-check b] 通过:rank_pct 的 ties/NaN、以及 w*rpX+(1-w)*rpK 的 NaN 自动传播 == '两腿都有值才参与'
[self-check b] 通过:by_year_like_engine 在合成数据(2 年 x 20 天)上与直接 bk.book_row(同一切片) 逐字段相同(含最小 20 天/年的门槛,与 partura/runner.py 一致)

== 0 自检与环境确认
  st.ic(O,'train')['rank_ic'] = +0.0374  (对照 +0.0374,通过)
  inspect.signature(Study.books)  = (self, panel: 'np.ndarray', fit: 'str' = 'train', evals: 'Sequence[str]' = ('train', 'valid'), sign: 'Optional[float]' = None) -> 'Dict[str, object]'
  inspect.signature(Study.signal) = (self, panel: 'np.ndarray', fit: 'str' = 'train', sign: 'Optional[float]' = None, halflife: 'Optional[float]' = None) -> 'np.ndarray'
  [结论] Study.books 签名里没有 halflife/hl 参数 -> 不能直接钉住半衰期;它内部总是调 bk.books()->bk.fit_halflives(),对全部 7 个候选半衰期各跑一次再选最优,**不能**跳过这个 sweep。
  但可以绕到底层 bk 模块自己钉住:bk.smoothed(sig, 0.0) 在 halflife=0.0(假值)时直接返回原信号、不做任何 EMA;配合 bk.book_row(sm, target, days, cost, top_frac) 直接算一个单一 hl 下的 book,完全跳过 fit_halflives 的 sweep。下面 (1)(2)(4) 的'pin hl=0'都是这么做的,不是通过 Study.books。
  --- Study.books 源码 ---
    def books(self, panel: np.ndarray, fit: str = "train", evals: Sequence[str] = ("train", "valid"),
              sign: Optional[float] = None) -> Dict[str, object]:
        """Decile L/S and the long leg, in the user's convention (see partura.books)."""
        sg = self.sign(panel, fit) if sign is None else sign
        return bk.books(sg * np.asarray(panel, dtype=np.float64), self.target(), self.slice(fit),
                        {e: self.slice(e) for e in evals},
                        cost=float(self.cfg.get("cost_per_side", bk.COST)),
                        top_frac=float(self.cfg.get("top_frac", bk.TOP_FRAC)),
                        rank_by=self.cfg.get("rank_by", "long"))

  --- Study.signal 源码 ---
    def signal(self, panel: np.ndarray, fit: str = "train", sign: Optional[float] = None,
               halflife: Optional[float] = None) -> np.ndarray:
        """What would be traded: sign x panel, EMA-smoothed at the half-life fitted for the
        long book on ``fit`` (or at ``halflife``).  Full length; slice it yourself."""
        p = np.asarray(panel, dtype=np.float64)
        sg = self.sign(panel, fit) if sign is None else sign
        if halflife is None:
            halflife = bk.fit_halflives(sg * p, self.target(), self.slice(fit),
                                        float(self.cfg.get("cost_per_side", bk.COST)),
                                        float(self.cfg.get("top_frac", bk.TOP_FRAC)))[
                "hl_long" if self.cfg.get("rank_by", "long") == "long" else "hl_ls"]
        return bk.smoothed(sg * p, halflife)

  st.signal 的 sign/hl 在哪个段上定:签名默认 fit='train' -- 两者都只在 train 上拟合一次,然后对全长(含 valid)原样套用,不重新拟合。
  O: sign=-1  hl_long=10  hl_ls=10  (预期 O: -1/10,P: -1/20,K30: -1/0)
  P: sign=-1  hl_long=20  hl_ls=20  (预期 O: -1/10,P: -1/20,K30: -1/0)
  K30: sign=-1  hl_long=0  hl_ls=0  (预期 O: -1/10,P: -1/20,K30: -1/0)
  K9: sign=-1  hl_long=5  hl_ls=0  (预期 O: -1/10,P: -1/20,K30: -1/0)
  [免费自检] 现场重算 st.books(O,...) vs 主表 v_base: train Lnet=+5.57% (对照 +5.6%)  valid Lnet=+0.25% (对照 +0.2%)
  [免费自检] 现场重算 st.books(P,...) vs 主表 a_no_rate: train Lnet=+6.37% (对照 +6.4%)  valid Lnet=+1.96% (对照 +2.0%)
  [免费自检] 现场重算 st.books(K30,...) vs 主表 k_stdamt_mean30: train Lnet=+12.62% (对照 +12.6%)  valid Lnet=+22.33% (对照 +22.3%)

== 0b by_year 诊断的工具缺口(k_stdamt_mean30),以及补算
  根因(读 partura/runner.py 确认):diagnostics.by_year 只在 `for vid,v in variants.items()` 这个循环里给 traded_full[vid] 赋值,而 variants 只是**本次 run 传的 stage(S2_increment)自己的变体**;k_stdamt_mean30 属于 S1_anatomy,不在这次的 variants 里,所以即使配置的 by_year: [...] 列了它的 id,也进不了 traded_full,digest 里静默缺这一行(S2_increment.json 的 diagnostics.by_year 只有'c_pure'/'m_blend_pure_k30' 两个 key,没有 'v_base'/'k_stdamt_mean30')。corr_ids/corr_with 不受影响,因为 runner 另有一段专门把 refs(含跨阶段 id)喂给 traded(不是 traded_full)。
  [补算] k_stdamt_mean30 2018: Lnet=+17.26%  LS=+3.01  days=243
  [补算] k_stdamt_mean30 2019: Lnet=+10.23%  LS=+1.84  days=244
  [补算] k_stdamt_mean30 2020: Lnet=+6.60%  LS=+0.66  days=243
  [补算] k_stdamt_mean30 2021: Lnet=+15.96%  LS=+2.18  days=243
  [补算] k_stdamt_mean30 2022: Lnet=+24.59%  LS=+4.22  days=242
  [补算] k_stdamt_mean30 2023: Lnet=+18.27%  LS=+2.88  days=144
  补算方法与 partura/runner.py 算 by_year 的那段代码逐行一致(同一个 bk.book_row,同样按 years==y 再与 scope 取交集定下标),已经用合成数据自检过(见上面 self-check b);range 限定在 st.slice('utrain') = [20180102, 20230807],没有碰 holdout。

== 4 H7b 直接确认(可选,能做):O 在固定 hl 下的 Lgross/Lnet/LTO(train)
  能做:st.books 不能钉 hl,但 bk.smoothed(sign*O, hl) + bk.book_row(...) 可以绕过 sweep 直接钉住。
  hl=   0: Lgross=+9.79%  Lnet=-6.15%  LTO=21.09%  (反推对照 Lgross~=+9.7%)
  hl=   2: Lgross=+9.04%  Lnet=+1.58%  LTO=9.86%  (反推对照 Lgross~=+9.2%)
  hl=   5: Lgross=+9.04%  Lnet=+3.86%  LTO=6.85%  (反推对照 Lgross~=+9.2%)
  hl=  10: Lgross=+9.44%  Lnet=+5.57%  LTO=5.11%  (反推对照 Lgross~=+9.4%)
  hl=  20: Lgross=+7.31%  Lnet=+4.57%  LTO=3.62%  (反推对照 Lgross~=+7.6%)

== 3 H9:O(=v_base)在 buyable=True / False 两套标签下(train, valid)
  train buyable=True : long_gross=+9.44%  short_gross=+26.10%  long_share=0.2655  LS=+2.529  long_net=+5.57%
  train buyable=False: long_gross=+8.05%  short_gross=+27.20%  long_share=0.2283  LS=+2.497  long_net=+4.18%
  valid buyable=True : long_gross=+4.11%  short_gross=+27.06%  long_share=0.1318  LS=+1.768  long_net=+0.25%
  valid buyable=False: long_gross=+3.47%  short_gross=+26.97%  long_share=0.1141  LS=+1.710  long_net=-0.39%
  对账(buyable=True, train): long_share=0.2655(对照~0.265) LS=+2.529(对照~+2.53) short=+26.10%(对照~+26.1%)  -> 通过,下面 buyable=False 的数字可以当结论用

== 2 残差多头腿(秩空间回归,被解释变量 = rank_pct(sig_X))
  判读提醒:残差不再平滑、换手会更高,看 alpha 还在不在要看 Lgross 和 rIC,不是 Lnet(playbook §1)
  X=O grp=a(K30): meanR2=0.0725  rIC(tr/va)=+0.0225/+0.0221  sign_resid=+1  hl=10  Lgross(tr/va)=+4.21%/-4.23%  Lnet(tr/va)=+1.80%/-6.70%  Lshp(tr/va)=+0.358/-1.089  LTO=3.18%  rank_corr(resid,K30)=-0.0200
  X=O grp=b(K30+K9): meanR2=0.0756  rIC(tr/va)=+0.0214/+0.0203  sign_resid=+1  hl=10  Lgross(tr/va)=+4.49%/-4.53%  Lnet(tr/va)=+2.07%/-7.01%  Lshp(tr/va)=+0.416/-1.147  LTO=3.21%  rank_corr(resid,K30)=-0.0200
  X=O grp=c(K30+K9+mom20+dvol20): meanR2=0.1849  rIC(tr/va)=+0.0149/+0.0076  sign_resid=+1  hl=5  Lgross(tr/va)=+6.90%/-5.03%  Lnet(tr/va)=+3.56%/-8.47%  Lshp(tr/va)=+0.726/-1.619  LTO=4.32%  rank_corr(resid,K30)=-0.0235
  X=P grp=a(K30): meanR2=0.0894  rIC(tr/va)=+0.0205/+0.0219  sign_resid=+1  hl=20  Lgross(tr/va)=+2.69%/-3.56%  Lnet(tr/va)=+1.29%/-5.03%  Lshp(tr/va)=+0.262/-0.899  LTO=1.86%  rank_corr(resid,K30)=-0.0253
  X=P grp=b(K30+K9): meanR2=0.0915  rIC(tr/va)=+0.0209/+0.0215  sign_resid=+1  hl=2  Lgross(tr/va)=+4.01%/-4.42%  Lnet(tr/va)=+1.49%/-7.02%  Lshp(tr/va)=+0.277/-1.181  LTO=3.33%  rank_corr(resid,K30)=-0.0255
  X=P grp=c(K30+K9+mom20+dvol20): meanR2=0.1915  rIC(tr/va)=+0.0149/+0.0088  sign_resid=+1  hl=20  Lgross(tr/va)=+4.32%/-2.16%  Lnet(tr/va)=+2.74%/-3.77%  Lshp(tr/va)=+0.596/-0.738  LTO=2.06%  rank_corr(resid,K30)=-0.0287

== 1 增量权重曲线:blend_w = w*rank_pct(sig_X) + (1-w)*rank_pct(sig_K30)
  -- X=O  覆盖率(两腿都有值) cov_tr=0.6911 cov_va=0.8947 --
  w=0.00 sgn_auto=+1 | pin(hl=0)  Lnet +12.62%/+22.33% Lshp +1.779/+3.462 Lgross +15.18%/+24.45% LTO 3.38%/2.80% | auto(hl=0) Lnet +12.62%/+22.33% Lshp +1.779/+3.462 Lgross +15.18%/+24.45% LTO 3.38%/2.80%
  w=0.10 sgn_auto=+1 | pin(hl=0)  Lnet +12.69%/+22.02% Lshp +1.806/+3.450 Lgross +15.39%/+24.28% LTO 3.57%/2.98% | auto(hl=0) Lnet +12.69%/+22.02% Lshp +1.806/+3.450 Lgross +15.39%/+24.28% LTO 3.57%/2.98%
  w=0.25 sgn_auto=+1 | pin(hl=0)  Lnet +12.40%/+20.94% Lshp +1.832/+3.458 Lgross +15.39%/+23.67% LTO 3.95%/3.61% | auto(hl=0) Lnet +12.40%/+20.94% Lshp +1.832/+3.458 Lgross +15.39%/+23.67% LTO 3.95%/3.61%
  w=0.50 sgn_auto=+1 | pin(hl=0)  Lnet +11.32%/+17.68% Lshp +1.824/+3.290 Lgross +14.68%/+20.97% LTO 4.44%/4.35% | auto(hl=0) Lnet +11.32%/+17.68% Lshp +1.824/+3.290 Lgross +14.68%/+20.97% LTO 4.44%/4.35%
  w=0.75 sgn_auto=+1 | pin(hl=0)  Lnet +10.80%/+12.65% Lshp +2.050/+2.665 Lgross +14.52%/+16.35% LTO 4.92%/4.89% | auto(hl=0) Lnet +10.80%/+12.65% Lshp +2.050/+2.665 Lgross +14.52%/+16.35% LTO 4.92%/4.89%
  w=1.00 sgn_auto=+1 | pin(hl=0)  Lnet +5.57%/+0.25% Lshp +1.206/+0.044 Lgross +9.44%/+4.11% LTO 5.11%/5.11% | auto(hl=0) Lnet +5.57%/+0.25% Lshp +1.206/+0.044 Lgross +9.44%/+4.11% LTO 5.11%/5.11%
  -- X=P  覆盖率(两腿都有值) cov_tr=0.6911 cov_va=0.8947 --
  w=0.00 sgn_auto=+1 | pin(hl=0)  Lnet +12.62%/+22.33% Lshp +1.779/+3.462 Lgross +15.18%/+24.45% LTO 3.38%/2.80% | auto(hl=0) Lnet +12.62%/+22.33% Lshp +1.779/+3.462 Lgross +15.18%/+24.45% LTO 3.38%/2.80%
  w=0.10 sgn_auto=+1 | pin(hl=0)  Lnet +12.43%/+21.48% Lshp +1.765/+3.344 Lgross +15.03%/+23.60% LTO 3.44%/2.81% | auto(hl=0) Lnet +12.43%/+21.48% Lshp +1.765/+3.344 Lgross +15.03%/+23.60% LTO 3.44%/2.81%
  w=0.25 sgn_auto=+1 | pin(hl=0)  Lnet +12.83%/+20.39% Lshp +1.884/+3.290 Lgross +15.45%/+22.68% LTO 3.47%/3.03% | auto(hl=0) Lnet +12.83%/+20.39% Lshp +1.884/+3.290 Lgross +15.45%/+22.68% LTO 3.47%/3.03%
  w=0.50 sgn_auto=+1 | pin(hl=0)  Lnet +12.58%/+17.39% Lshp +2.009/+3.140 Lgross +15.28%/+19.96% LTO 3.58%/3.40% | auto(hl=0) Lnet +12.58%/+17.39% Lshp +2.009/+3.140 Lgross +15.28%/+19.96% LTO 3.58%/3.40%
  w=0.75 sgn_auto=+1 | pin(hl=0)  Lnet +11.98%/+13.55% Lshp +2.260/+2.747 Lgross +14.78%/+16.34% LTO 3.70%/3.69% | auto(hl=0) Lnet +11.98%/+13.55% Lshp +2.260/+2.747 Lgross +14.78%/+16.34% LTO 3.70%/3.69%
  w=1.00 sgn_auto=+1 | pin(hl=0)  Lnet +6.37%/+1.96% Lshp +1.371/+0.368 Lgross +9.15%/+4.76% LTO 3.67%/3.70% | auto(hl=0) Lnet +6.37%/+1.96% Lshp +1.371/+0.368 Lgross +9.15%/+4.76% LTO 3.67%/3.70%

  -- 两端自检(偏离量 = 这一端的 blend 数字 - 对应主表参照;就是二次平滑/覆盖率限制的代价)--
  w=1 X=O train: ref(st.books(O)) Lnet=+5.57% Lshp=+1.206  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000
  w=1 X=O valid: ref(st.books(O)) Lnet=+0.25% Lshp=+0.044  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000
  w=0 X=O train: ref(st.books(K30)) Lnet=+12.62% Lshp=+1.779  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000
  w=0 X=O valid: ref(st.books(K30)) Lnet=+22.33% Lshp=+3.462  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000
  w=1 X=P train: ref(st.books(P)) Lnet=+6.37% Lshp=+1.371  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000
  w=1 X=P valid: ref(st.books(P)) Lnet=+1.96% Lshp=+0.368  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000
  w=0 X=P train: ref(st.books(K30)) Lnet=+12.62% Lshp=+1.779  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000
  w=0 X=P valid: ref(st.books(K30)) Lnet=+22.33% Lshp=+3.462  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000

done
[partura exit 0 2026-10-05_06:27:28]

📝 往下做之前先记日志(研究随时可能中断、换人或换模型接手;没落盘的判断会丢):
   ./scripts/study.sh note F115_all_tide_mean_30 "<一句话:这次看到了什么>" <<'EOF'
   这次结果说明什么(带关键数字)/ 哪条假设因此变了 / 下一步打算做什么、为什么
   EOF
   并更新 notes/F115_all_tide_mean_30/state.md(研究现状:中间结果 / 逻辑 / 假设表 / 候选 / 后面的思路;格式见 docs/study_playbook.md §7)。
```

**10-04 15:29 · Bash** — Sanity check the full x2_increment log file head/tail

```bash
cd /Users/wxy/Desktop/Partura && wc -l logs/F115_all_tide_mean_30_x2_increment.log && echo "--- head ---" && head -5 logs/F115_all_tide_mean_30_x2_increment.log && echo "--- tail ---" && tail -5 logs/F115_all_tide_mean_30_x2_increment.log
```

```
     108 logs/F115_all_tide_mean_30_x2_increment.log
--- head ---
[self-check a] 通过:O=cross_mean(div(L,M),20)、P=cross_mean(L,20) 与 configs 逐字符相同(P 就是 O 去掉外层 ÷M)
[self-check b] 通过:rank_pct 的 ties/NaN、以及 w*rpX+(1-w)*rpK 的 NaN 自动传播 == '两腿都有值才参与'
[self-check b] 通过:by_year_like_engine 在合成数据(2 年 x 20 天)上与直接 bk.book_row(同一切片) 逐字段相同(含最小 20 天/年的门槛,与 partura/runner.py 一致)
/root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_in.py:785: FutureWarning: We've integrated functorch into PyTorch. As the final step of the integration, `functorch.vmap` is deprecated as of PyTorch 2.0 and will be deleted in a future version of PyTorch >= 2.3. Please use `torch.vmap` instead; see the PyTorch 2.0 release notes and/or the `torch.func` migration guide for more details https://pytorch.org/docs/main/func.migrating.html
  return vmap(single_row)(x).unsqueeze(-1)
--- tail ---
  w=0 X=P train: ref(st.books(K30)) Lnet=+12.62% Lshp=+1.779  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000
  w=0 X=P valid: ref(st.books(K30)) Lnet=+22.33% Lshp=+3.462  | pin 偏离 dLnet=+0.00pp dLshp=+0.000  | auto 偏离 dLnet=+0.00pp dLshp=+0.000

done
[partura exit 0 2026-10-05_06:27:28]
```

**10-04 15:30 · Bash** — Inspect rank_corr_train structure for potential m_blend vs known_stdamt_mean30 pair

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F115_all_tide_mean_30/S2_increment.json'))
rc = d['diagnostics']['rank_corr_train']
print(type(rc))
if isinstance(rc, dict):
    print('keys:', list(rc.keys()))
    for k in list(rc.keys())[:3]:
        print(k, '->', rc[k] if not isinstance(rc[k], dict) else list(rc[k].keys()))
print()
print('rank_corr_on:', d['diagnostics']['rank_corr_on'])
"
```

```
<class 'dict'>
keys: ['v_base', 'a_no_rate', 'a_width_only', 'a_plain_ret', 'a_rank_pre', 'a_abs', 'a_win30', 'a_win60', 'k_stdamt_mean30', 'a_fixwin95', 'c_pure', 'k_stdamt_max9', 'm_blend_base_k30', 'm_blend_pure_k30', 'ctl_amt', 'ctl_cap', 'ctl_turnrate', 'ctl_ivol', 'ctl_dvol20', 'ctl_price', 'ctl_rev1', 'ctl_mom20', 'known_amt_max9', 'known_stdamt_max9', 'known_ivol_max9', 'known_stdamt_mean30']
v_base -> ['v_base', 'a_no_rate', 'a_width_only', 'a_plain_ret', 'a_rank_pre', 'a_abs', 'a_win30', 'a_win60', 'k_stdamt_mean30', 'a_fixwin95', 'c_pure', 'k_stdamt_max9', 'm_blend_base_k30', 'm_blend_pure_k30', 'ctl_amt', 'ctl_cap', 'ctl_turnrate', 'ctl_ivol', 'ctl_dvol20', 'ctl_price', 'ctl_rev1', 'ctl_mom20', 'known_amt_max9', 'known_stdamt_max9', 'known_ivol_max9', 'known_stdamt_mean30']
a_no_rate -> ['v_base', 'a_no_rate', 'a_width_only', 'a_plain_ret', 'a_rank_pre', 'a_abs', 'a_win30', 'a_win60', 'k_stdamt_mean30', 'a_fixwin95', 'c_pure', 'k_stdamt_max9', 'm_blend_base_k30', 'm_blend_pure_k30', 'ctl_amt', 'ctl_cap', 'ctl_turnrate', 'ctl_ivol', 'ctl_dvol20', 'ctl_price', 'ctl_rev1', 'ctl_mom20', 'known_amt_max9', 'known_stdamt_max9', 'known_ivol_max9', 'known_stdamt_mean30']
a_width_only -> ['v_base', 'a_no_rate', 'a_width_only', 'a_plain_ret', 'a_rank_pre', 'a_abs', 'a_win30', 'a_win60', 'k_stdamt_mean30', 'a_fixwin95', 'c_pure', 'k_stdamt_max9', 'm_blend_base_k30', 'm_blend_pure_k30', 'ctl_amt', 'ctl_cap', 'ctl_turnrate', 'ctl_ivol', 'ctl_dvol20', 'ctl_price', 'ctl_rev1', 'ctl_mom20', 'known_amt_max9', 'known_stdamt_max9', 'known_ivol_max9', 'known_stdamt_mean30']

rank_corr_on: traded signals (sign x panel, smoothed at the fitted half-life); controls raw
```

**10-04 15:30 · Bash** — Extract specific pairwise rank correlations from the full matrix

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F115_all_tide_mean_30/S2_increment.json'))
rc = d['diagnostics']['rank_corr_train']
pairs = [
    ('m_blend_base_k30','known_stdamt_mean30'),
    ('m_blend_pure_k30','known_stdamt_mean30'),
    ('m_blend_base_k30','v_base'),
    ('m_blend_pure_k30','a_no_rate'),
    ('m_blend_base_k30','m_blend_pure_k30'),
    ('a_fixwin95','a_no_rate'),
    ('a_fixwin95','a_plain_ret'),
    ('c_pure','a_no_rate'),
    ('k_stdamt_max9','known_stdamt_mean30'),
    ('k_stdamt_max9','k_stdamt_mean30'),
]
for a,b in pairs:
    print(f'{a:20s} vs {b:20s} = {rc[a][b]:+.4f}')
"
```

```
m_blend_base_k30     vs known_stdamt_mean30  = -0.8287
m_blend_pure_k30     vs known_stdamt_mean30  = -0.8325
m_blend_base_k30     vs v_base               = +0.7001
m_blend_pure_k30     vs a_no_rate            = +0.6417
m_blend_base_k30     vs m_blend_pure_k30     = +0.9673
a_fixwin95           vs a_no_rate            = +0.5580
a_fixwin95           vs a_plain_ret          = +0.6110
c_pure               vs a_no_rate            = +1.0000
k_stdamt_max9        vs known_stdamt_mean30  = -0.9577
k_stdamt_max9        vs k_stdamt_mean30      = +0.9577
```

**10-04 15:31 · Bash** — Confirm ledger.json still shows no holdout reads

```bash
cd /Users/wxy/Desktop/Partura && cat runs/F115_all_tide_mean_30/ledger.json 2>&1 | python3 -c "
import json,sys
d = json.load(sys.stdin)
print(type(d))
print(d if isinstance(d, list) else list(d.keys()))
" 2>&1 | head -40
```

```
<class 'dict'>
['entries', 'summary']
```

**10-04 15:31 · Bash** — List ledger entries to confirm no holdout split was read

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d = json.load(open('runs/F115_all_tide_mean_30/ledger.json'))
for e in d['entries']:
    print(e.get('tag'), e.get('splits') or e.get('split'), e.get('use_holdout'), e.get('time') or e.get('ts'))
print('summary:', d['summary'])
"
```

```
None train None None
None valid None None
None utrain None None
None train None None
None valid None None
None utrain None None
None train None None
None valid None None
None utrain None None
None train None None
None valid None None
None utrain None None
None train None None
None valid None None
None utrain None None
None train None None
None valid None None
None utrain None None
summary: {'train': {'reads': 6, 'expressions': 17}, 'valid': {'reads': 6, 'expressions': 17}, 'utrain': {'reads': 6, 'expressions': 17}}
```

10-04 15:31 · 读 `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/07_S1_anatomy.md`

10-04 15:31 · 读 `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/07_S1_anatomy.md`

**10-04 15:31 · Bash** — List section headers in the two R1 note files

```bash
cd /Users/wxy/Desktop/Partura && grep -n "^## " notes/F115_all_tide_mean_30/07_S1_anatomy.md notes/F115_all_tide_mean_30/07x_1_anat_mfi.md
```

```
notes/F115_all_tide_mean_30/07x_1_anat_mfi.md:5:## 问题
notes/F115_all_tide_mean_30/07x_1_anat_mfi.md:11:## 结果
notes/F115_all_tide_mean_30/07x_1_anat_mfi.md:95:## 解读
notes/F115_all_tide_mean_30/07_S1_anatomy.md:3:## 问题
notes/F115_all_tide_mean_30/07_S1_anatomy.md:11:## 结果
notes/F115_all_tide_mean_30/07_S1_anatomy.md:102:## 解读
```

10-04 15:31 · 读 `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/07x_1_anat_mfi.md`

**10-04 15:33 · 写文件** `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/07_S2_increment.md`(6161 字符)

**10-04 15:34 · 写文件** `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/07x_2_increment.md`(8466 字符)

10-04 15:34 · 读 `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/results/R0.md`

**10-04 15:35 · 写文件** `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/results/R2.md`(9747 字符)

**10-04 15:36 · Bash** — Append research journal entry summarizing R2 execution results

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F115_all_tide_mean_30 "[执行] R2:S2_increment(5变体)+ x2_increment 都跑完(exit 0),结果卡 results/R2.md 已写;权重曲线在 valid 上随 w 增大严格单调下降(两条 X 都是 w=0 最高),残差 Lgross train 正 valid 全负,H9 实测方向与工单预测相反" <<'EOF'
主表(train->valid Lnet):a_fixwin95 +4.3%->-9.7%(valid 全场最差,Q10 分位剖面在这批里最烂,-6.1% vs
Q9 +1.7%);c_pure(=a_no_rate 换 id 重跑)+6.4%->+2.0%,与 a_no_rate 逐数字相同,rank_corr=+1.0000,
流水线自检通过;k_stdamt_max9 +13.7%->+22.2%(全套数字第一次拿到);m_blend_base_k30 +9.6%->+17.7%
(dist=0.81);m_blend_pure_k30 +10.9%->+17.1%(dist=0.80)。符号对齐:sign(v_base)=sign(a_no_rate)=
sign(k_stdamt_mean30)=-1,按工单用 add(cs_rank,cs_rank) 写法,未改。

增量权重曲线(H6 核心判据):X=O 和 X=P 两条曲线的 valid Lnet 都随 w 从 0 到 1 严格单调下降
(22.33%->...->0.25% / 22.33%->...->1.96%),w=0(纯 k_stdamt_mean30)始终最高,没有出现"中间某个 w
不低于 w=0"。意外:auto(自动重选半衰期)与 pin(hl=0,不加二次平滑)在全部 12 个(X,w)组合上逐数字
相同,工单担心的"二次平滑代价"这次没有出现。

残差多头腿(2 因子 x 3 组控制,6 组全部同一模式):rIC train/valid 都保持正(+0.0076~+0.0225),但
Lgross(不是 Lnet)train 全正、valid 全部转负——不是成本效应能解释的那种转负。

H9:买不进标签对调后,short 腿几乎不变(train 26.10%->27.20%,valid 27.06%->26.97%),反而是多头腿在
动(valid long_net +0.25%->-0.39%),与工单预测的方向相反;对账 buyable=True 三项(long_share 0.2655、
LS +2.529、short +26.10%)全部吻合 06 §1/§2,所以这个反向结果本身可信,只是不符合预期方向。

H7b 直接确认(不再靠反推):O 在 hl 0/2/5/10/20 的 Lgross = +9.79/+9.04/+9.04/+9.44/+7.31%,与此前反推
值逐档相差 <=0.3pp,平滑压成本不抬毛超额的结论被直接数字坐实。

工具缺口:by_year/profile 对跨阶段引用的旧变体(v_base/k_stdamt_mean30)静默跳过,只有 corr_ids 支持
跨阶段(读 partura/runner.py 确认根因:两者都只在"本次 run 自己 stage 的变体"循环里填 traded_full)。
k_stdamt_mean30 的逐年数字用脚本按 runner 同样的方法手动补算(2018~2023:+17.3/+10.2/+6.6/+16.0/
+24.6/+18.3%),没有碰 holdout。另外发现 digest 文本只打印 v_base 星形,但 JSON 的 rank_corr_train
其实是满矩阵,m_blend_* 与 known_stdamt_mean30 的相关(约 +0.83,符号因 raw/signed 不同而相反打印为
-0.83)是从满矩阵里直接查到的,不是重新计算。

留出段没有碰:runs/F115_all_tide_mean_30/ledger.json 核对过,只有 train/valid/utrain,没有 holdout
记录。服务器运行 2 次(S2_increment + x2_increment),没有超工单上限。
EOF
```

```
已记入 notes/F115_all_tide_mean_30/journal.md(14 条)
```

**10-04 15:36 · Bash** — Re-check brief output head to confirm R2 status updated

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F115_all_tide_mean_30 2>&1 | sed -n '1,40p'
```

```
# F115_all_tide_mean_30 — 交接状态

_自动生成于 2026-10-04 15:36(`python scripts/recorder.py --brief F115_all_tide_mean_30` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 all_tide_mean_30(批次 B01_single_factors)
- 表达式:`cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `work:F115_all_tide_mean_30#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:09 → `handoff/F115_all_tide_mean_30/agents/work_R0_a7273d2d90aa037a4.md`
- agent `lead:F115_all_tide_mean_30#1`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:22 → `handoff/F115_all_tide_mean_30/agents/lead_R1_a3c13ae564c521f87.md`
- agent `work:F115_all_tide_mean_30#1`(wf_c8c98127-70d):失败,最后动作 10-04 13:29 → `handoff/F115_all_tide_mean_30/agents/work_R1_afd53c65be8af464a.md`
- agent `work:F115_all_tide_mean_30#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)
- agent `lead:F115_all_tide_mean_30#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 13:56 → `handoff/F115_all_tide_mean_30/agents/lead_R1_a8335e6e80d689144.md`
- agent `work:F115_all_tide_mean_30#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 14:29 → `handoff/F115_all_tide_mean_30/agents/work_R1_ab1ea8a7172111e8e.md`
- agent `lead:F115_all_tide_mean_30#2`(wf_48864a04-f0a):已返回结果,最后动作 10-04 15:00 → `handoff/F115_all_tide_mean_30/agents/lead_R2_a7746237f816b23e1.md`
- agent `work:F115_all_tide_mean_30#2`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F115_all_tide_mean_30` 看服务器上的 tag,`./scripts/study.sh digest F115_all_tide_mean_30 <tag>` 重看结果)。

## 研究现状(`notes/F115_all_tide_mean_30/state.md`,10-04 14:59 更新)—— **先读这个文件**

# 研究现状 — F115_all_tide_mean_30

_每一轮由主研**整个覆盖重写**。最后更新:2026-10-04,**第 2 轮**(主研 = Opus 5)。
本轮做的是:裁决 R1 的结果(R1 已跑完、结果卡已交)、把解读写进 07/07x/05、下 R2 工单。本轮没有跑实验。_

---

## 1. 一句话现状

**R1 跑完了,这棵树的内部结构已经钉死;R2 工单已下,只剩两个问题没答案。**
R1(`S1_anatomy` 8 变体 + `x1_anat_mfi` 脚本,都 exit 0)把 H2、H3 杀死,H1、H5 支持,H4、H7b 改写/否定,
并给出**唯一一条确立的提纯结果**(整个 `÷M` 子树可以删掉)。
剩下的两个问题就是 R2 的全部内容:**(一) 对只做多的用户,它掺进已知家族有没有增量(H6);
(二) 潮汐定位是不是只等于一个固定子窗口(H10,新立)。**

**下一步**:执行按 `notes/F115_all_tide_mean_30/orders/R2.md` 做 ——
```

**10-04 15:36 · Bash** — Check orders/results status section of brief

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F115_all_tide_mean_30 2>&1 | sed -n '/工单与结果卡/,/配置里的实验计划/p'
```

```
## 工单与结果卡(`notes/F115_all_tide_mean_30/orders/`、`notes/F115_all_tide_mean_30/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F115_all_tide_mean_30.yaml`)
```

**10-04 15:36 · Bash** — Check runs and notes listing at the end of brief output

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F115_all_tide_mean_30 2>&1 | sed -n '/已经跑过的服务器运行/,$p'
```

```
## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F115_all_tide_mean_30`)

- `S0_baseline`  10-04 12:01  1 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S0_baseline`
- `S1_anatomy`  10-04 14:09  8 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S1_anatomy`
- `S2_increment`  10-04 15:13  5 个变体  → `./scripts/study.sh digest F115_all_tide_mean_30 S2_increment`
- `x1_anat_mfi`(自写脚本的输出)  10-04 14:19  exit 0  → `logs/F115_all_tide_mean_30_x1_anat_mfi.log`
- `x2_increment`(自写脚本的输出)  10-04 15:27  exit 0  → `logs/F115_all_tide_mean_30_x2_increment.log`

## 已写的 notes(`notes/F115_all_tide_mean_30/`)

- `01_expression.md`  3095 字节  10-04 13:02
- `02_operators.md`  13227 字节  10-04 13:03
- `03_decomposition.md`  6648 字节  10-04 13:04
- `04_grammar.md`  6261 字节  10-04 13:15
- `05_hypotheses.md`  16804 字节  10-04 14:44
- `06_baseline.md`  11268 字节  10-04 13:06
- `07_S1_anatomy.md`  16143 字节  10-04 14:50
- `07_S2_increment.md`  7974 字节  10-04 15:33
- `07x_1_anat_mfi.md`  9404 字节  10-04 14:47
- `07x_2_increment.md`  11071 字节  10-04 15:34
- `journal.md`  19950 字节  10-04 15:36
- `state.md`  28041 字节  10-04 14:59

## 自写的探针与分析脚本(`studies/F115_all_tide_mean_30/`)

- `anat_mfi.py`  10-04 14:17  F115 R1 / x1_anat_mfi: anatomy of N = L x (1/M) on the six raw daily panels.
- `increment.py`  10-04 15:22  F115 R2 / x2_increment: 增量权重曲线(H6)+ 残差多头腿 + H9(封板票)+ H7b 确认(第 2 件,见

## 结构化结果(`handoff/F115_all_tide_mean_30/results/`)

(还没有)
```

**10-04 15:36 · Bash** — Check for stray pycache files from local test run

```bash
cd /Users/wxy/Desktop/Partura && find studies/F115_all_tide_mean_30 -name "__pycache__" -o -name "*.pyc" 2>/dev/null
```

```
studies/F115_all_tide_mean_30/__pycache__
studies/F115_all_tide_mean_30/__pycache__/anat_mfi.cpython-311.pyc
```

**10-04 15:36 · Bash** — List pycache contents to check for increment-related artifacts

```bash
cd /Users/wxy/Desktop/Partura && ls -la studies/F115_all_tide_mean_30/__pycache__/
```

```
total 40
drwxr-xr-x@ 3 wxy  staff     96 Oct  4 14:18 .
drwxr-xr-x@ 5 wxy  staff    160 Oct  4 15:22 ..
-rw-r--r--@ 1 wxy  staff  17231 Oct  4 14:17 anat_mfi.cpython-311.pyc
```

**10-04 15:37 · Bash** — Search for any pycache artifacts created during this session

```bash
cd /Users/wxy/Desktop/Partura && find . -name "*.pyc" -newer configs/F115_all_tide_mean_30.yaml 2>/dev/null; find . -path "*/F115_all_tide_mean_30/__pycache__*" 2>/dev/null
```

```
./studies/F115_all_tide_mean_30/__pycache__
./studies/F115_all_tide_mean_30/__pycache__/anat_mfi.cpython-311.pyc
```

**10-04 15:37 · Bash** — Search whole repo for any increment-related pyc file

```bash
cd /Users/wxy/Desktop/Partura && find . -iname "increment*.pyc" 2>/dev/null; find . -iname "*.pyc" 2>/dev/null
```

```
./tests/__pycache__/test_partura.cpython-311-pytest-9.1.1.pyc
./partura/__pycache__/propose.cpython-311.pyc
./partura/__pycache__/lab.cpython-311.pyc
./partura/__pycache__/bridge.cpython-311.pyc
./partura/__pycache__/semantics.cpython-311.pyc
./partura/__pycache__/runner.cpython-311.pyc
./partura/__pycache__/report.cpython-311.pyc
./partura/__pycache__/probes.cpython-311.pyc
./partura/__pycache__/splits.cpython-311.pyc
./partura/__pycache__/cli.cpython-311.pyc
./partura/__pycache__/panels.cpython-311.pyc
./partura/__pycache__/decompose.cpython-311.pyc
./partura/__pycache__/__init__.cpython-311.pyc
./partura/__pycache__/diagnose.cpython-311.pyc
./studies/F105_std_fangzheng_covamt/__pycache__/longleg.cpython-311.pyc
./studies/F105_std_fangzheng_covamt/__pycache__/rev2.cpython-311.pyc
./studies/F105_std_fangzheng_covamt/__pycache__/audit_1.cpython-311.pyc
./studies/F105_std_fangzheng_covamt/__pycache__/rev1.cpython-311.pyc
./studies/F104_kurt_masktop_amt/__pycache__/rev1_review.cpython-311.pyc
./studies/F104_kurt_masktop_amt/__pycache__/x1_anatomy.cpython-311.pyc
./studies/F104_kurt_masktop_amt/__pycache__/rev2_split.cpython-311.pyc
./studies/F002_crosscov_highvar/__pycache__/probes.cpython-311.pyc
./studies/F103_amt_dw_decay/__pycache__/rev1_matched.cpython-311.pyc
./studies/F103_amt_dw_decay/__pycache__/audit_1.cpython-311.pyc
./studies/F103_amt_dw_decay/__pycache__/x3_family.cpython-311.pyc
./studies/F115_all_tide_mean_30/__pycache__/anat_mfi.cpython-311.pyc
```

**10-04 15:37 · Bash** — Check modification timestamps of partura pycache files

```bash
cd /Users/wxy/Desktop/Partura && stat -f "%Sm %N" partura/__pycache__/*.pyc 2>/dev/null | sort
```

```
Sep 30 01:42:05 2026 partura/__pycache__/decompose.cpython-311.pyc
Sep 30 01:45:17 2026 partura/__pycache__/__init__.cpython-311.pyc
Sep 30 01:46:29 2026 partura/__pycache__/splits.cpython-311.pyc
Sep 30 02:01:35 2026 partura/__pycache__/panels.cpython-311.pyc
Sep 30 02:10:35 2026 partura/__pycache__/diagnose.cpython-311.pyc
Sep 30 02:31:37 2026 partura/__pycache__/bridge.cpython-311.pyc
Sep 30 12:19:10 2026 partura/__pycache__/semantics.cpython-311.pyc
Sep 30 12:23:37 2026 partura/__pycache__/propose.cpython-311.pyc
Sep 30 12:25:11 2026 partura/__pycache__/probes.cpython-311.pyc
Sep 30 12:25:33 2026 partura/__pycache__/runner.cpython-311.pyc
Sep 30 12:25:54 2026 partura/__pycache__/cli.cpython-311.pyc
Sep 30 12:25:54 2026 partura/__pycache__/lab.cpython-311.pyc
Sep 30 12:25:54 2026 partura/__pycache__/report.cpython-311.pyc
```

**10-04 15:38 · StructuredOutput**

```json
{
 "order": "R2",
 "completed": true,
 "result_card": "/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/results/R2.md",
 "summary": "按工单 R2(kind: experiment)把两件事做完:(1) configs/F115_all_tide_mean_30.yaml 加了 S2_increment 阶段(5 个变体:a_fixwin95 固定子窗口零假设、c_pure 提纯版复核、k_stdamt_max9 第二条已知家族基准、m_blend_base_k30/m_blend_pure_k30 两个与已知家族的秩相加混合体),check 通过(除已知的 in_local_mean LOOKAHEAD 误报)后 run+wait,exit 0;符号对齐自检确认 sign(v_base)=sign(a_no_rate)=sign(k_stdamt_mean30)=-1,按工单用 add(cs_rank,cs_rank) 写法未改。(2) 新写 studies/F115_all_tide_mean_30/increment.py(三层自检后读真实数据,只用 train/valid),exec+wait,exit 0,按 (0)(0b)(4)(3)(2)(1) 顺序回答了:Study.books/signal 能否钉住半衰期(不能,但可绕 bk.smoothed/book_row 钉住)、增量权重曲线(H6 核心:X=O 和 X=P 两条曲线在 valid 上都随 w 增大严格单调下降,w=0 纯已知家族始终最高)、残差多头腿(rIC 两段为正但 Lgross train 正 valid 全负)、H9 买不进标签对照(对账通过,但实测方向与工单预测相反——short 腿几乎不变、反而是多头腿略降)、H7b 直接确认(不再靠反推,Lgross 在 hl 0~20 基本走平)。服务器运行共 2 次,在工单上限内;留出段全程未碰(ledger.json 已核对)。写了 notes/F115_all_tide_mean_30/07_S2_increment.md、07x_2_increment.md(只填问题/结果,解读留空)、results/R2.md,并记了一条 journal。过程中确认并记录了一个此前未知的工具缺口:by_year/profile 诊断对跨阶段引用的旧变体(v_base、k_stdamt_mean30)会静默跳过(只有 corr_ids/corr_with 支持跨阶段),已用与引擎相同的方法在脚本里手动补算 k_stdamt_mean30 的逐年数字;另外发现 digest 文本只打印以 v_base 为中心的相关\"星形\",但 JSON 里其实存了全部变体两两之间的满矩阵,据此直接拿到了 m_blend_* 与 known_stdamt_mean30 的相关。没有做不成的事,没有偏离工单设计的候选/判据,所有解读判断都留给主研。",
 "tags": [
  "S2_increment",
  "x2_increment"
 ],
 "problems": [
  "a_fixwin95(固定子窗口零假设)valid 段表现是目前全部变体里最差的:Lnet -9.7%、Lshp -1.40,分位剖面 Q10 大幅塌陷(-6.1%,低于 Q9 的 +1.7%),与工单给的 a_no_rate 判据(±1.5pp 内)差距很大",
  "by_year/profile 两个诊断对跨阶段引用的旧变体(v_base、k_stdamt_mean30)会静默跳过——只有 corr_ids/corr_with 支持跨阶段;k_stdamt_mean30 的逐年 Lnet/LS 改用脚本按引擎同样的方法手动补算(已用合成数据自检,范围限定在 train+valid,未碰留出段)",
  "残差多头腿(2 个因子 x 3 组控制,共 6 组)的 Lgross 在 train 全正、valid 全部转负,而残差 rIC 两段都仍为正——这不是典型的'换手推高成本'模式(那种模式下 Lgross 应该还在、只有 Lnet 转负),留给主研判断",
  "H9 的实测方向与工单预测相反:buyable=False 下空头腿(short_gross/LS)几乎不变甚至略升,反而是多头腿略降(valid long_net 从 +0.25% 变成 -0.39%);buyable=True 的对账三项(long_share/LS/short)全部吻合已知数字,所以这个反向结果本身可信,只是不是工单预期的方向",
  "权重曲线里'auto 自动重选半衰期'与'pin 钉住 hl=0'在全部 12 个 (X,w) 组合上逐数字相同,工单预期的'二次平滑代价'这次没有出现(属于意外发现,不是错误)",
  "m_blend_base_k30/m_blend_pure_k30 的 dist(0.80~0.81)明显低于这批其余变体(0.97~1.00),仍过用户 0.5 门槛但接近注意线,是两个'cs_rank 秩相加'混合体特有的现象",
  "digest 的文本输出只打印以 v_base 为中心的相关'星形',但 runs/F115_all_tide_mean_30/S2_increment.json 的 diagnostics.rank_corr_train 实际存的是全部变体/控制变量两两之间的满矩阵(已据此直接查到 m_blend_* 与 known_stdamt_mean30 的相关,约 ±0.83,正负号因 raw/交易信号方向不同而相反)"
 ]
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/configs/F115_all_tide_mean_30.yaml`
- `/Users/wxy/Desktop/Partura/studies/F115_all_tide_mean_30/increment.py`
- `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/07_S2_increment.md`
- `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/07x_2_increment.md`
- `/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/results/R2.md`

## 它返回给工作流的结果

```json
{
 "order": "R2",
 "completed": true,
 "result_card": "/Users/wxy/Desktop/Partura/notes/F115_all_tide_mean_30/results/R2.md",
 "summary": "按工单 R2(kind: experiment)把两件事做完:(1) configs/F115_all_tide_mean_30.yaml 加了 S2_increment 阶段(5 个变体:a_fixwin95 固定子窗口零假设、c_pure 提纯版复核、k_stdamt_max9 第二条已知家族基准、m_blend_base_k30/m_blend_pure_k30 两个与已知家族的秩相加混合体),check 通过(除已知的 in_local_mean LOOKAHEAD 误报)后 run+wait,exit 0;符号对齐自检确认 sign(v_base)=sign(a_no_rate)=sign(k_stdamt_mean30)=-1,按工单用 add(cs_rank,cs_rank) 写法未改。(2) 新写 studies/F115_all_tide_mean_30/increment.py(三层自检后读真实数据,只用 train/valid),exec+wait,exit 0,按 (0)(0b)(4)(3)(2)(1) 顺序回答了:Study.books/signal 能否钉住半衰期(不能,但可绕 bk.smoothed/book_row 钉住)、增量权重曲线(H6 核心:X=O 和 X=P 两条曲线在 valid 上都随 w 增大严格单调下降,w=0 纯已知家族始终最高)、残差多头腿(rIC 两段为正但 Lgross train 正 valid 全负)、H9 买不进标签对照(对账通过,但实测方向与工单预测相反——short 腿几乎不变、反而是多头腿略降)、H7b 直接确认(不再靠反推,Lgross 在 hl 0~20 基本走平)。服务器运行共 2 次,在工单上限内;留出段全程未碰(ledger.json 已核对)。写了 notes/F115_all_tide_mean_30/07_S2_increment.md、07x_2_increment.md(只填问题/结果,解读留空)、results/R2.md,并记了一条 journal。过程中确认并记录了一个此前未知的工具缺口:by_year/profile 诊断对跨阶段引用的旧变体(v_base、k_stdamt_mean30)会静默跳过(只有 corr_ids/corr_with 支持跨阶段),已用与引擎相同的方法在脚本里手动补算 k_stdamt_mean30 的逐年数字;另外发现 digest 文本只打印以 v_base 为中心的相关\"星形\",但 JSON 里其实存了全部变体两两之间的满矩阵,据此直接拿到了 m_blend_* 与 known_stdamt_mean30 的相关。没有做不成的事,没有偏离工单设计的候选/判据,所有解读判断都留给主研。",
 "tags": [
  "S2_increment",
  "x2_increment"
 ],
 "problems": [
  "a_fixwin95(固定子窗口零假设)valid 段表现是目前全部变体里最差的:Lnet -9.7%、Lshp -1.40,分位剖面 Q10 大幅塌陷(-6.1%,低于 Q9 的 +1.7%),与工单给的 a_no_rate 判据(±1.5pp 内)差距很大",
  "by_year/profile 两个诊断对跨阶段引用的旧变体(v_base、k_stdamt_mean30)会静默跳过——只有 corr_ids/corr_with 支持跨阶段;k_stdamt_mean30 的逐年 Lnet/LS 改用脚本按引擎同样的方法手动补算(已用合成数据自检,范围限定在 train+valid,未碰留出段)",
  "残差多头腿(2 个因子 x 3 组控制,共 6 组)的 Lgross 在 train 全正、valid 全部转负,而残差 rIC 两段都仍为正——这不是典型的'换手推高成本'模式(那种模式下 Lgross 应该还在、只有 Lnet 转负),留给主研判断",
  "H9 的实测方向与工单预测相反:buyable=False 下空头腿(short_gross/LS)几乎不变甚至略升,反而是多头腿略降(valid long_net 从 +0.25% 变成 -0.39%);buyable=True 的对账三项(long_share/LS/short)全部吻合已知数字,所以这个反向结果本身可信,只是不是工单预期的方向",
  "权重曲线里'auto 自动重选半衰期'与'pin 钉住 hl=0'在全部 12 个 (X,w) 组合上逐数字相同,工单预期的'二次平滑代价'这次没有出现(属于意外发现,不是错误)",
  "m_blend_base_k30/m_blend_pure_k30 的 dist(0.80~0.81)明显低于这批其余变体(0.97~1.00),仍过用户 0.5 门槛但接近注意线,是两个'cs_rank 秩相加'混合体特有的现象",
  "digest 的文本输出只打印以 v_base 为中心的相关'星形',但 runs/F115_all_tide_mean_30/S2_increment.json 的 diagnostics.rank_corr_train 实际存的是全部变体/控制变量两两之间的满矩阵(已据此直接查到 m_blend_* 与 known_stdamt_mean30 的相关,约 ±0.83,正负号因 raw/交易信号方向不同而相反)"
 ]
}
```

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  很多停止的、error的，可以继续跑了，我重置了额度

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**执行**(研究工程师),负责因子 F115_all_tide_mean_30 最新的一张工单:把主研设计的事情实现出来、跑完、把结果读准、写成结果卡。
  你**不改研究思路**:不增删假设、不换候选、不下结论。工单里有做不了的地方(表达式解析不过、算子不存在、超过变体数上限),
  做**最小的、保持原意的**修改并在结果卡里写明改了什么;完全做不了就写明卡在哪。你的读者是主研(另一个模型),它只看你写的文件。
  
  ## 你在整件事里的位置(先读这一段)
  
  用户的总任务:对一批 AlphaCube 因子逐条做 Partura 研究(分辨、提纯、升华);并要求研究全程落盘、随时能换模型接手。
  分工是 —— 总领(Opus 5.5)搭框架与协调;主研(Opus 5)负责单条因子的研究思路;执行(Sonnet 5)负责写代码、跑实验、读结果。
  
  工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」)。那句话是说给总领听的 —— 可能是催进度、问状态、
  要求把东西记下来、或者安排分工 —— **总领已经处理过了,下面这份任务就是总领对它的落实**。所以它和下面的任务**不冲突**:
  你把这份任务完整做完(并按要求把过程写进文件),就是在执行用户的请求。**不要因为那句话而跳过、缩减任务,或改做别的事。**
  如果它提到「写 state.md」「记录下来」,落到你身上就是:主研照常在本轮结束前重写 state.md;执行照常写结果卡和日志 —— 仅此而已。
  记录框架、状态板、模型分工都已经由总领搭好并在运行,不需要你去搭、去改、去切换任何东西
  (scripts/、partura/、workflows/、handoff/、lab/、docs/ 一律不要动;别的因子的文件也不要动)。
  **你就是这个分工里的「执行」。**
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  先读 docs/study_playbook.md —— 操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西、§6 审查反复抓到的错误、
  §7 研究日志与交接。下面不重复手册里的内容。
  不要使用 Agent / Workflow 工具去派生别的 agent。所有写给人看的文字用中文,英文术语保留。
  
  **这项研究是接力做的**:「主研」定思路、下工单;「执行」写代码、跑实验、读结果。两者是不同的模型,而且每一轮都是
  一个全新的 agent —— 彼此之间**只靠文件**传递信息,你的对话和推理不会被任何人看到。
  你知道的、想到的、决定的,**不写进文件就等于没有**。
  
  ## 因子
  
  - factor_id: F115_all_tide_mean_30
  - 来源: 手写库 / all_tide_mean_30
  - 表达式:
  cross_mean(div(div(sub(day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), day_locate(in_slice(Close, 31, 211), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), sub(day_argmin(in_slice_to_end(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))), day_argmin(in_slice_from_start(in_local_mean(in_slice(Volume, 31, 211), 5), day_argmax(in_local_mean(in_slice(Volume, 31, 211), 5)))))), 20)
  
  
  ## 这条因子的共享记忆(都在 /Users/wxy/Desktop/Partura 下)—— 接力靠的就是它们
  
    notes/F115_all_tide_mean_30/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
    notes/F115_all_tide_mean_30/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F115_all_tide_mean_30/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F115_all_tide_mean_30/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F115_all_tide_mean_30/NN_*.md          进报告的手写段落(playbook §5)
    configs/F115_all_tide_mean_30.yaml、studies/F115_all_tide_mean_30/、runs/F115_all_tide_mean_30/*.json、logs/F115_all_tide_mean_30_*.log
    handoff/F115_all_tide_mean_30/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F115_all_tide_mean_30
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F115_all_tide_mean_30 "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 要做的事
  
  1. ./scripts/study.sh brief F115_all_tide_mean_30;找到**最新的、还没有结果卡**的工单 notes/F115_all_tide_mean_30/orders/R<n>.md,读它。
     (所有工单都有结果卡了:什么都不用做,返回 completed:false、summary 写「没有待办工单」。)
  2. ./scripts/study.sh list F115_all_tide_mean_30:工单要的 tag 是不是已经跑过(上一个执行可能做到一半被打断)。跑过且 exit 0 的不要重跑,直接读结果;
     exit 97 是被内存守卫让路中止的,要重跑。
  3. 实现并运行:
     - 配置阶段:在 configs/F115_all_tide_mean_30.yaml 里加阶段(stage id、变体 id、表达式、why 照抄工单),./scripts/study.sh check F115_all_tide_mean_30,
       通过后 ./scripts/study.sh run F115_all_tide_mean_30 <tag> <stage…>,然后 ./scripts/study.sh wait F115_all_tide_mean_30 <tag>(Bash 的 timeout 设 600000;没完就再 wait。
       排队是正常的)。表达式语言的坑看 playbook §3。
     - 分析脚本:studies/F115_all_tide_mean_30/<name>.py,用 partura.study_tools.Study(playbook §2「自己写分析」);脚本开头先对一个已知答案自检;
       ./scripts/study.sh exec F115_all_tide_mean_30 <tag> <name>.py,再 wait。
     - **只用 train / valid**。除非工单的 kind 是 final,否则绝不调用 study.sh final。
  4. 把结果读准。工单「要带回来的数字」逐项回答;每个数写清口径:哪个变体、train / valid / utrain / holdout、
     多头口径(hlL)还是多空口径(hlS)、毛还是净。主动报告异常:求值失败的变体、cov < 0.95 或 dist < 0.5、符号与预期相反、
     换手异常、你做过的任何改动。
  5. 写结果卡 notes/F115_all_tide_mean_30/results/R<n>.md:
       # 结果卡 R<n>
       ## 做了什么(tag、阶段、脚本;哪些没做成、改了什么)
       ## 工单要的数字(逐项对着工单回答,用表格)
       ## 没人要但值得注意的(异常与意外)
       ## 原始输出在哪(./scripts/study.sh digest F115_all_tide_mean_30 <tag> / logs/…)
     只写事实,不写「所以它是…」—— 那是主研的事。
  6. 记日志:./scripts/study.sh note F115_all_tide_mean_30 "[执行] R<n>:<一句话>" <<'EOF' 最关键的几个数字 EOF
  
  ## 按工单的 kind
  
  - **final**(读留出段,整个研究只许一次):先确认 runs/F115_all_tide_mean_30/ledger.json 里没有 split 为 holdout 的记录、
    notes/F115_all_tide_mean_30/10_distilled.md 里已有「读留出段之前」一节;两条有一条不满足就**不要跑**,在结果卡里写明。
    S_final 的候选照抄工单(不得增删),每个变体写 group: final, final: true, profile: true(playbook §3),
    check 通过后 ./scripts/study.sh final F115_all_tide_mean_30 final S_final,再 wait。
    结果卡里放「与用户表同口径」那张表的全部行(多头口径与多空口径各一份)和逐年表。
  - **writeup**:补齐事实类段落(01、02、03、06;每个 07_<stage_id>.md 的「问题 → 结果」部分,解读是主研写的,不要改);
    ./scripts/study.sh report F115_all_tide_mean_30;把 research/alpha_distillation/F115_all_tide_mean_30.md 从头读一遍,notes 里引用的每个数字都到表里核对。
    明显的数字笔误直接改并列进结果卡;结论句不要动,有疑问的列进结果卡让主研裁决。
  - **fix**(修订阶段):按工单改 notes 里的数字 / 措辞、补实验(阶段 id 用 SR_ 开头)、重出报告并核对。绝不读留出段。
  - **experiment**:如上。
  
  返回:order(工单号)、completed、result_card(路径)、tags(跑过的 tag)、problems、summary。
```
