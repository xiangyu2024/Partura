# lead:F111_spearman_qclose#2 — agent af0c892fdf47993a9(工作流 wf_48864a04-f0a)

- 状态:**已返回结果**;开始 10-04 14:55,最后一次动作 10-04 15:24;工具调用 44 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F111_spearman_qclose/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 14:55 · agent 的话**

I'll start by getting the full picture of this factor's research state.

**10-04 14:55 · Bash** — Get overview brief for factor F111

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F111_spearman_qclose 2>&1 | head -200
```

```
# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-04 14:55(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F111_spearman_qclose#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `work:F111_spearman_qclose#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:09 → `handoff/F111_spearman_qclose/agents/work_R0_a067aac26fed39d46.md`
- agent `lead:F111_spearman_qclose#1`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:26 → `handoff/F111_spearman_qclose/agents/lead_R1_ab403fe60ef06a414.md`
- agent `work:F111_spearman_qclose#1`(wf_c8c98127-70d):失败,最后动作 10-04 13:29 → `handoff/F111_spearman_qclose/agents/work_R1_aba23855eadec7a06.md`
- agent `work:F111_spearman_qclose#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)
- agent `lead:F111_spearman_qclose#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 13:55 → `handoff/F111_spearman_qclose/agents/lead_R1_a36c37b71e6d128ea.md`
- agent `work:F111_spearman_qclose#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 14:36 → `handoff/F111_spearman_qclose/agents/work_R1_a4f4276b792511fca.md`
- agent `lead:F111_spearman_qclose#2`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F111_spearman_qclose` 看服务器上的 tag,`./scripts/study.sh digest F111_spearman_qclose <tag>` 重看结果)。

## 研究现状(`notes/F111_spearman_qclose/state.md`,10-04 13:54 更新)—— **先读这个文件**

# F111_spearman_qclose 研究现状

> 本文件每轮由**主研覆盖重写**。最后更新:**第 1 轮(主研,Opus 5,重启的那一次)**,2026-10-04。
> 表达式:`ts_spearman(day_quantile(Close), 10)`,来源 挖掘库 / #953。

---

## 1. 一句话现状

**R1 工单已写好但一个字都还没执行**(上一个执行 agent 在动手前就因对话额度耗尽失败;额度现已重置)。
我这一轮(第 1 轮的重启)按工作流规矩**没有另开工单**,而是:
**自己把 R1 的第 1 项做掉了(H5 ⇒ 已确立)**、从同一个恒等式里推出一条和 H2 竞争的新假设 **H11**
并写进 `05_hypotheses.md`、给 R1 加了一个零成本的判别小项 **(c4)**。
**下一步仍然是执行去跑 R1**(阶段 `S1_whatis` 6 变体 + 脚本 `x1_identity.py` 的 4 个 block + (c4)),
回来之后由第 2 轮主研裁决 H1/H2/H3/H4/H6/H7/H10/H11。

---

(…全文 15797 字符,读 `notes/F111_spearman_qclose/state.md`)

## 研究日志(`notes/F111_spearman_qclose/journal.md`:9 条,其中研究员自己写的 5 条)

最近的 12 条(完整的看文件):

### 2026-10-04 12:46 [总领] 分层工作流接手:建档(执行)→ 主研/执行轮转

### 2026-10-04 13:06 [执行] R0 建档完成:四份 notes 和结果卡写完,主要发现 ts_spearman 实为跨股票横截面平均相关

看到了什么:读完 day_quantile(dt_day.py:150)、ts_spearman(nd_ts.py:483)源码。day_quantile(Close) 省略 q
参数,落到默认 q=0.5(日内中位价),不是特殊分位点。ts_spearman 声明 arity=1、family=ts,但函数体内有
for i in range(N) 跨股票循环:对每只股票,算它与全市场其它每只股票同窗口的 Spearman 相关,再取平均
——不是单变量时间序列统计量,"操作数"是股票轴本身,树结构里看不出来。S0_baseline 精确复现了
published 行:sign=+1、hl_ls=10、books_user.by_rank.ls.hl10.splits.utrain 的 ls_sharpe=2.616→2.62,
long_gross_ann=0.16394→0.164,都对上,但 published.long 列是毛超额不是净超额(净超额同口径只有
11.8%),这是最容易被后续研究张冠李戴的一点。决策口径(train 定,hlL=20):Lnet train+10.4%/valid
+17.0%;多空口径 hlS=10:LS train 2.41/valid 3.20。多头腿只占 long-short 总收益 37%~39%(long_share)。
分位剖面 train/valid 都严格单调。rank 相关最高是 known_stdamt_mean30(−0.42),远低于 0.95 的同族门槛。
cov=0.99、dist=0.85 都过门槛。

记录了什么:写了 01_expression.md、02_operators.md、03_decomposition.md、06_baseline.md 和
results/R0.md(结果卡列了 12 条异常/待核对点,包括:脉冲记忆天数探针读数=0 与 10 天窗口的直觉不符;
day_median 的底层 C._median 源码读不到(工具只解析注册算子名);三套 R²〈0.276/0.253/0.287〉和两个
工具的 rank 相关〈-0.35 对 -0.34〉不是同一口径;逐年/衰减/中性化用的半衰期 hl_used=20 是靠数字反推
确认的,JSON 没有显式标注;此前 3 次 study agent 都因对话额度耗尽 0 工具调用失败,没留下任何文件)。
全部是事实陈述,没有下假设或结论。

下一步:主研可以直接基于这四份 notes 和结果卡开始定假设、下第一张工单(R1),不需要重跑 S0_baseline
或重新读算子源码。决定不做的事:没有去验证 day_quantile(Close) 和 day_median(Close) 在偶数分钟数
下是否逐位相同(需要读 C._median 或直接跑数,留给需要时再做);没有去对齐三套 R² 的口径差异。

### 2026-10-04 13:26 [主研] 第 1 轮:源码推出恒等式——原式的截面序 ≡ 对市场秩路径的投影,即条件动量;下 R1 工单

看到了什么(自己核对源码 + 读 R0 建档):
1. 自己读了 ts_spearman / ts_pearson / cs_mean / ts_corr 源码,确认 R0 的语义读法,并多读出四件事:
   (i) 秩是 argsort(argsort(x, stable=True), stable=True) 的序数秩,**相等的值按日期顺序发秩**;
   (ii) cs_mean 返回 .expand_as(x),输出是 (D,N) 广播面板,可以直接喂 ts_corr;
   (iii) ts_pearson 已重写成 chunked matmul,比还留着 for i in range(N) 的 ts_spearman 快得多;
   (iv) 实现瑕疵:cov 除以两只股票**重叠**的有效天数,而 rank_std 各自在**自己**的有效天数上算,
        缺失模式不同时分母口径不一致,"相关系数"可超出 [-1,1](影响约 1% 的停牌/新股格子)。
2. 本轮的核心产出:把根节点那个 O(N^2) 的"对全市场其他每只股票求 Spearman 再平均"**精确解掉**
   (写进 04_grammar.md)。关键一步:窗口完整时窗口内的秩必然是 {0..9} 的排列,所以每只股票的
   rank_mean=(d-1)/2、rank_var=(d^2-1)/12 都是**同一个常数**,corr=cov/(std_i*std_j) 的分母不区分股票,
   于是对 j 的平均可以换进求和号:
     B[t,i] = (N/(N-1)) * (1/(d*sigma^2)) * SUM_k rc_i[t,k]*M[t,k]  -  1/(N-1)
   M[t,.] 是全市场平均的"窗口内去均值秩路径",在第 t 天对所有股票是同一个 10 维向量;j≠i 的自排除
   精确等于一个常数项,不影响截面序。又因 ||rc_i|| 对每只股票都相同,内积序=相关序=回归 beta 序。
   再把 M 一阶近似成直线 c(t)*(k-4.5),得到 B ≈ c(t) * rho_i^time:
   **(市场 10 日趋势方向) × (自己的 10 日秩动量)= 条件动量**。

判断:
- H1(配对结构多余)、H2(条件动量)是源码推导,**不是证据**,R1 block (a)/(b) 才是实证检验。
- 推导顺手解释了基线里最别扭的读数:ctl_mom20 的 rank 相关只有 -0.08、R^2 只有 0.056。若它是条件动量,
  c(t) 时正时负,**无条件**地和动量比相关性本来就该被抵消 —— 低相关不等于"和动量无关"。
  (记在这里当反例:不要用无条件相关去排除动量。)
- 新假设 H3:stable 排序对相等值按日期发秩 ⇒ 10 天里日内中位价完全不变的股票秩路径正好是 0..9,
  一条**完美上升斜坡**,涨市里拿到接近最高的因子值。day_quantile(Close) 落在 tick 网格上,低价股容易
  并列(复权只是窗口内的常数乘子,不消除并列)。这是瑕疵型泄漏的候选,必须有答案。
- 把全局优先级定在 H4:**原式的多头腿已经输给已知家族** —— v_base +10.4%/+17.0%(Lshp 1.79/3.07)
  低于 known_stdamt_mean30 +12.6%/+22.3%(1.78/3.46)和 known_stdamt_max9 +13.7%/+22.2%(1.99/3.59)。
  所以"这条因子单独好不好"不是问题,"相对已知家族有没有增量"才是。S0 §7 的中性化已有强烈迹象:
  对 all_controls 中性化后多头腿**毛**超额从 +13.6% 掉到 +0.1%(但那是 9 个 ctl_*,**不是 known_* 家族**)。
- H5:用成本公式 2*LTO*15bp*~254 反推(在 hl=10/20 两点上吻合到 0.04pp),固定半衰期表的**毛**超额
  在 hl=0..20 上几乎是平线(≈+14%),也就是说平滑的全部功劳是省成本(换手 29.9%→4.1%),没有改变
  信号内容。推论:hl=20 已是半衰期池上界,真正的升华杠杆是**更长的窗口 d**;衰减表(rank IC 从 h=1
  的 0.0298 单调升到 h=20 的 0.0710)指向同一边。**这三行是反推的、不是实测**,R1 第 1 项零成本核实。

决定做什么:下 R1(kind: experiment),2 次服务器运行 + 1 项不花服务器的 JSON 重读:
  第 1 项(不花服务器):从本地 S0_baseline.json 读固定半衰期表的 long_gross_ann → 定 H5。
  第 2 项(run, tag S1_whatis, 6 变体):m_mktcorr=ts_corr(A, cs_mean(A),10) 测 H1;s_pearson 测 H6;
    l_mean=ts_spearman(day_mean(Close),10) 测 H3(分钟均价几乎不并列);l_last 测 H7;l_amt 测 H10;
    t_tsrank=ts_rank(A,10) 测 H2(纯动量,没有 c(t) 条件化)。
  第 3 项(exec, tag x1_identity):(a) numpy 按源码复刻秩路径、算 proj,与原式做逐日 Spearman ——
    恒等式的实证检验,**不依赖表达式语言能不能写出 m_mktcorr**;(b) 按 c(t) 符号分组的条件相关(H2);
    (c) **对 3 条 known_* 家族的残差多头腿 + 5 个权重的组合多头腿(H4,最重要)**;(d) 并列占比、
    按十分位的分布、去掉并列格子后的书(H3)。脚本开头用随机数组做自检:暴力双循环算
    mean_{j≠i} spearman 与 proj 的 rank 相关应 ≈1.0 —— 不过就说明我的推导错了。

决定不做什么:
- **不扫窗口 d**。它是最有希望的升华杠杆,但扫法取决于 H1:H1 成立就该在便宜的 ts_corr/cross_corr
  形式上扫(cross_* 窗口池到 60/241),而不是在带 Python 循环的 ts_spearman 上扫。先定身份,再扫参数。
- 不做 abs_corr=True / agg="std":取绝对值是**折叠**,会破坏 H1 的线性投影性质,也会让 playbook §6.5
  ("折叠骗过秩空间线性中性化")开始适用、H4 的检验口径得跟着换。那是另一条因子,不是这条的提纯。
- 不碰封板票对空头腿的污染(H8)、不确认 H9 的 valid 分段:多头腿不受影响,不动摇选拔结论,放 R2。
- 不对齐三套 R^2(0.276/0.253/0.287)和两个工具的 rank 相关(-0.35/-0.34):差异 0.01~0.03,无影响。
- 不验证 day_quantile(.,0.5) 与 day_median 逐位相同;不自己写 probes.py(R0 那个"脉冲记忆=0"的怪读数
  已被 04_grammar.md 解释掉:对全市场取平均把单只股票的脉冲摊薄了 1/N,不需要新探针)。

落盘:新写 04_grammar.md、05_hypotheses.md(H1~H10,每条带预测和杀死它的实验)、orders/R1.md、
state.md(8 节,覆盖重写)。服务器运行预算:R1 用掉 2 次,全研究还剩 6 次(含 final)。

### 2026-10-04 13:54 [主研] 第 1 轮(重启):R1 未执行故原样交回;自己把 H5 做成已确立(毛超额平线、hl=20 最低),并推出新假设 H11

背景:上一轮的执行 agent 两次都在动手之前就因对话额度耗尽失败。我核对过:服务器上只有
S0_baseline、studies/F111_spearman_qclose/ 不存在、配置里只有 S0_baseline 一个阶段、
两份 work:R1 动作流水显示它们只读了 playbook 和 brief 就停了。⇒ R1 一个字都没执行。
按工作流规矩**不另开工单**,把 R1 原样交回执行。本轮没有消耗任何服务器运行,预算不变
(R1 要用 2 次,全研究还剩 6 次含 final)。

既然不下新工单,我把这一轮用在**不花服务器运行、但能定事的事情**上,做了四件:

1. **把 R1 的第 1 项自己做完了 —— H5 从「反推」变成「已确立」,而且结论比上一版更强。**
   books.sweep 里确实没有 long_gross_ann 字段(上一版猜对了)。但我在 partura/books.py 里读到
   确切的成本与年化口径:long_book() 里 net_daily = gross_daily − cost_per_side × traded、
   traded = 2 ×(上报的 turnover),stats() 里 ann = mean × 252(**是 252,不是上一版用的 254**),
   于是 Lgross = Lnet + 0.756 × LTO 可以精确复原。我**先在两个实测点上验过公式**才敢用
   (有实测 long_gross_ann 的只有两处:by_rank.long 的 hl=20、by_rank.ls 的 hl=10):
   复原 13.53% vs 实测 13.558%、复原 14.83% vs 实测 14.869%,误差 ≤0.04pp。
   train 上 7 个固定半衰期的毛超额:
     hl=0  +14.07%   (LTO 29.88%, 成本 22.59pp, Lnet −8.52%)
     hl=1  +14.30%
     hl=2  +15.20%
     hl=3  +15.35%   ← 最高
     hl=5  +14.15%
     hl=10 +14.83%
     hl=20 +13.53%   ← **最低**(LTO 4.08%, 成本 3.08pp, Lnet +10.45%)
   ⇒ 毛超额**没有趋势**(13.5%~15.4%),净超额那 18.9pp 的改善**全部**来自成本。
   **EMA 平滑一点都没改善信号内容,略微还磨掉了一点。**
   硬约束(playbook §6.1):这条因子的半衰期轴不携带任何信号改善,任何"候选比原式好"
   都必须在**同一个半衰期**下比;净超额的改善归因只能写"来自平滑/省成本"。

2. **顺手改写掉上一版一个错的推论(这条很重要,免得 R2 建在错前提上)。**
   上一版从"毛超额是平线"推出"最优平滑还在更远处 ⇒ 更长的窗口 d 是最有希望的升华杠杆"。
   站不住:(i) 毛超额在 hl>3 之后是**下降**的,hl=10→20 毛超额掉 1.3pp、成本省 1.5pp、
   净只多 0.22pp —— 净超额曲线已经走平到最优平台,**半衰期轴是被耗尽了而不是没用够**;
   (ii) 衰减表(rank IC 随预测期 h 单调上升)讲的是**标签期限**,不是**平滑长度**,
   两根不同的轴不能互为证据。⇒「更长的窗口 d」降级为一个独立的、未经检验的猜想,
   R2 要扫它得自己立假设,不许引用 H5。

3. **本轮的主要新理解:新假设 H11 —— 被交易的那个东西不是条件动量。**
   做法是把上一版的恒等式写成「模长 × 夹角」。因为 ‖rc_i‖ = sqrt(d)·σ 对每只股票是同一个常数:
     B[t,i] = c₁(t) · corr( rc_i[t,·], M[t,·] ) + 常数,  c₁(t) = (N/(N−1))·‖M[t,·]‖/(sqrt(d)·σ)
   c₁(t) 是一个模长,**恒为正**。所以 B 的符号只由"自己的秩路径和市场秩路径的吻合度"决定,
   **跟大盘往哪走无关** —— 涨市里跟着涨的、跌市里跟着跌的,**两种都拿到正的高值**。
   会随市场变号的是"B 与自己的动量 ρ^time 之间的关系",**不是 B 自己**。
   上一版第 3 步那个 c(t)·ρ_i^time 在代数上没错,但容易被后面的人读成"因子会翻面",
   所以我把不变量显式写进 04_grammar.md 的新第 4 步。
   这件事有可检验的后果,**而且第 1 条已经把它检验了**:如果被交易的信号真的每隔几天整本翻面,
   20 天 EMA 应该把毛超额平均掉一大块;实际只从 +14.07% 掉到 +13.53%(0.5pp),
   而换手掉了 86%。⇒ **被平滑掉的高频部分几乎不含 alpha,活下来的是跨市场方向不变的那一部分**,
   也就是"路径吻合度"= 路径干净、跟得上市场 ⇒ **特质波动低**。
   H11 还**一次解释了基线里 rank 相关的整个形状**:和低波/低活跃一族 −0.3~−0.42
   (known_stdamt_mean30 −0.42、ctl_amt −0.35、ctl_dvol20 −0.31),而**和动量几乎正交**(ctl_mom20 −0.08)。
   上一版用"条件化把无条件相关抵消了"解释了后半句,但**解释不了前半句** —— 为什么偏偏和低波
   一族有这么大的相关。H11 两句都解释。
   ⇒ 这给 H4(「对纯多头用户没有增量」)提供了**机制**而不只是相关性:用户的已知家族
   (day_std(Amt) 一族)本身就是活跃度离散度/低波,和它是**同一个暴露**。H4 的先验因此大幅升高。
   H11 的状态:**合理但未坐实** —— 预测 1 已被毛超额平线支持,预测 2 是对已有读数的事后解释
   (不算独立证据),预测 3 等 R1 block (c)。

4. **给 R1 加了一个零成本的判别小项 (c4),并标了优先级。**
   (c4):f 在 7 个 hl 下平滑后与 3 条 known_* 的 rank 相关(7×3 的表,纯 numpy,面板都已在手,
   不花额外的服务器运行)。H11 预测这条相关的**绝对值随 hl 单调上升**(平滑越久,剩下的越是那个
   不变的低波暴露);若随 hl 基本不变,H11 的"平滑把它转化成低波因子"这一步就被否定。
   同时在工单开头写明:第 1 项我已做完(别重算);**block (a) 区分不了 H2 和 H11**
   (两者都预测 proj 相关 ≈1),真正能区分的是 block (b) 的三个分组相关和 (c4) ——
   所以 (a)/(b)/(c4) 一个都不许砍,要砍先砍 block (d) 的十分位细表。
```

**10-04 14:55 · Bash** — List notes directory contents

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F111_spearman_qclose/ notes/F111_spearman_qclose/orders/ notes/F111_spearman_qclose/results/ 2>&1
```

```
notes/F111_spearman_qclose/:
total 240
drwxr-xr-x@ 12 wxy  staff    384 Oct  4 13:55 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   3302 Oct  4 13:01 01_expression.md
-rw-r--r--@  1 wxy  staff   9303 Oct  4 13:02 02_operators.md
-rw-r--r--@  1 wxy  staff   4429 Oct  4 13:02 03_decomposition.md
-rw-r--r--@  1 wxy  staff   8921 Oct  4 13:47 04_grammar.md
-rw-r--r--@  1 wxy  staff  18535 Oct  4 13:55 05_hypotheses.md
-rw-r--r--@  1 wxy  staff  13257 Oct  4 13:07 06_baseline.md
-rw-r--r--@  1 wxy  staff  17594 Oct  4 14:35 journal.md
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:48 orders
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:34 results
-rw-r--r--@  1 wxy  staff  26293 Oct  4 13:54 state.md

notes/F111_spearman_qclose/orders/:
total 40
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:48 .
drwxr-xr-x@ 12 wxy  staff    384 Oct  4 13:55 ..
-rw-r--r--@  1 wxy  staff  20225 Oct  4 13:48 R1.md

notes/F111_spearman_qclose/results/:
total 80
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:34 .
drwxr-xr-x@ 12 wxy  staff    384 Oct  4 13:55 ..
-rw-r--r--@  1 wxy  staff   6182 Oct  4 13:06 R0.md
-rw-r--r--@  1 wxy  staff  31097 Oct  4 14:34 R1.md
```

**10-04 14:55 · agent 的话**

R1 now has a result card. Let me read the state, the order, and the results.

**10-04 14:55 · Bash** — Read R1 result card

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F111_spearman_qclose/results/R1.md
```

```
<persisted-output>
Output too large (30.4KB). Full output saved to: /Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/bysbk81ag.txt

Preview (first 2KB):
# 结果卡 R1

## 做了什么

工单(`orders/R1.md`,kind: experiment)共 3 件要做的事,全部做完,**没有遇到解析不过 / 算子不存在 / 变体数超限的情况,配置和脚本都是按工单原样实现的,没有做任何偏离性修改**。

- **第 1 项(不用服务器)**:按工单补注,**由主研在第 1 轮重启时自行完成,本结果卡不重算**。结果见
  `notes/F111_spearman_qclose/05_hypotheses.md` 的 **H5** 一节 —— `books.sweep` 里没有
  `long_gross_ann` 字段(只有 `long_ann`/`long_sharpe`/`long_turnover`),毛超额是按成本公式代数复原的。
- **第 2 项(服务器运行 1/2)**:`configs/F111_spearman_qclose.yaml` 加了阶段 `S1_whatis`(6 个变体,
  表达式照抄工单),外加 top-level `corr_ids: [v_base, m_mktcorr, s_pearson, l_mean, l_last, l_amt, t_tsrank]`,
  `diagnostics.profile`/`diagnostics.neutralise` 都追加了 `m_mktcorr, t_tsrank`。`check` 一次通过
  (`18/18 OK`)。`m_mktcorr` 用的是工单给的主表达式 `ts_corr(day_quantile(Close), cs_mean(day_quantile(Close)), 10)`,
  **没有触发任何备用写法**。`run ... S1_whatis` → `wait`,tag=`S1_whatis`,exit 0,285.2s,peak anon 4.32 GiB。
- **第 3 项(服务器运行 2/2)**:新建 `studies/F111_spearman_qclose/x1_identity.py`(此前
  `studies/F111_spearman_qclose/` 目录不存在,本次新建)。按工单实现了自检 + block (a)/(b)/(c)/(c4)/(d),
  每个 block 各自 `try/except`。脚本开头先用随机数组做了工单要求的两条自检(§见下),并且我**额外加了一个
  `--mock` 模式**(合成随机面板 + 一个模拟 `Study` 接口,不连服务器)在本机先跑通一遍,确认没有 Python 级
  的形状/键错误后才提交服务器 —— 这不在工单要求之内,是我自己加的保险,没有改动工单范围之外的任何文件。
  `exec ... x1_identity.py` → `wait`,exit 0。四个 block 和 (c4) **全部跑完,没有一个触发 except**(即没有
  "某个 block 塌了"的情况);两条无害 warning 见"没人要但值得注意的"。
- **第 4 项(可选,不花服务器运行)**:跑了 `study.sh propose`,原样贴在数字 18。
- **服务器运行记账**:本工单计划 2 次,实际用了 2 次(`run S1_whatis` + `exec x1_identity`),均 exit 0,
  没有额外起新的运行。按主研 state.md 的记录,这 2 次正是"R1 要用 2 次"那笔预算,做完后"全研究还剩 6 次(含 final)"。
- 只改了 `configs/F111_spearman_qclose.yaml`(追加,未删动 S0 的任何内容)、新建
  `studies/F111_spearman_qclose/x1_identity.py`、`notes/F111_spearman_qclose/results/R1.md`(本文件)。
  没有碰 `partura/`、`scripts/`、`handoff/`、别的因子的文件。

---

## 工单要的数字

逐项对应工单"要带回来的数字"表的编号。除标明"S0 对照"外,全部是本轮两次运行的新数字。

### 数字 1 ——固定半衰期毛超额(S0 JSON)

由主研完成,不重算。照抄补注原话:"`books.sweep` 里没有 `long_gross_ann` 字段;`long_gross_ann = long_ann + 0.756 × long_turnover`,在两个实测点上误差 ≤0.04pp"。详表见 `05_hypotheses.md` H5。

...
</persisted-output>
```

**10-04 14:55 · Bash** — Read state.md

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F111_spearman_qclose/state.md
```

```
# F111_spearman_qclose 研究现状

> 本文件每轮由**主研覆盖重写**。最后更新:**第 1 轮(主研,Opus 5,重启的那一次)**,2026-10-04。
> 表达式:`ts_spearman(day_quantile(Close), 10)`,来源 挖掘库 / #953。

---

## 1. 一句话现状

**R1 工单已写好但一个字都还没执行**(上一个执行 agent 在动手前就因对话额度耗尽失败;额度现已重置)。
我这一轮(第 1 轮的重启)按工作流规矩**没有另开工单**,而是:
**自己把 R1 的第 1 项做掉了(H5 ⇒ 已确立)**、从同一个恒等式里推出一条和 H2 竞争的新假设 **H11**
并写进 `05_hypotheses.md`、给 R1 加了一个零成本的判别小项 **(c4)**。
**下一步仍然是执行去跑 R1**(阶段 `S1_whatis` 6 变体 + 脚本 `x1_identity.py` 的 4 个 block + (c4)),
回来之后由第 2 轮主研裁决 H1/H2/H3/H4/H6/H7/H10/H11。

---

## 2. 中间结果(已经量到的事实,每条带数字和出处)

出处标记:`S0` = `./scripts/study.sh digest F111_spearman_qclose S0_baseline`(本地
`runs/F111_spearman_qclose/S0_baseline.json`);`§` 指 `06_baseline.md` 的小节。
**holdout 一个数字都没读过。**

### 2.1 原式的多头腿(选拔第一判据)

| 口径 | hl | train | valid | 出处 |
|---|---|---|---|---|
| 多头腿净超额 Lnet | **20**(hlL) | **+10.4%** | **+17.0%** | S0 §1 |
| 纯多头夏普 Lshp | 20 | **1.79** | **3.07** | S0 §1 |
… (286 行略) …
   - 年化是 **×252**(不是 254);`long_turnover` 是**单边**换手,成本按 `2×LTO×15bp` 扣。
   - §2.3 的毛超额是**代数复原**的(公式在 2 个实测点上验过,误差 ≤0.04pp),
     引用时可以当事实用,但要注明是复原值。
6. **还没看结果的任务**:R1 的两次运行(tag `S1_whatis`、`x1_identity`)—— 工单已写,执行还没跑。
   每轮先 `./scripts/study.sh list F111_spearman_qclose` 看服务器上有没有跑完没拉回的。
7. **写了一半的文件**:没有。`04_grammar.md`、`05_hypotheses.md`、`orders/R1.md`、本文件都完整。
   **还不存在**的:`07_S1_whatis.md`、`07x_1_identity.md`、`08_variants.md`、`09_diagnosis.md`、
   `10_distilled.md`、`11_risks.md`、`12_next.md`。
8. **工具的坑**:
   - `./scripts/study.sh src <算子>` 只认**注册表里的算子名**,未注册的内部辅助函数
     (如 `C._median`)查不到(R0 异常 4)。
   - `ts_spearman` / `ts_pearson` 是 O(N²) 结构,`ts_spearman` 还留着 `for i in range(N)` 的
     Python 循环 ⇒ **慢**。排队和慢都正常(playbook §2),`wait` 没完就再调一次,
     别杀任务、别动显存参数。
   - 往 `configs/*.yaml` 的 `controls:` 里加东西会改变 `all_controls` 的 R²,就和 §2.4 不可比了。
     要单独对某个家族做中性化,加到 `gates:` 里并用 exec 脚本量(R1 block (c) 就是这么做的)。
   - 服务器运行全研究控制在 8 次以内(含 final,不含 S0)。**R1 要用掉 2 次,还剩 6 次。**
     ⚠️ 本轮(重启)**一次都没用**,预算没变。
9. **此前失败的 agent**:3 个 `study:`(`wf_759ef2d3-03f`)和 2 个 `work:R1`(`wf_c8c98127-70d`)
   都因对话额度耗尽失败,`handoff/` 里那几份流水不用看。用户已重置额度,可以正常跑。
```

**10-04 14:55 · agent 的话**

R1 is done. Let me read the full result card.

10-04 14:55 · 读 `/Users/wxy/.claude/projects/-Users-wxy-Desktop-230P-hw2/a975f7b7-25eb-4993-9a81-70b3c9c381f0/tool-results/bysbk81ag.txt`

**10-04 14:59 · agent 的话**

Now let me read the hypothesis table, the grammar file, and check the R1 order's variant definitions.

**10-04 14:59 · Bash** — Read hypotheses file part 1

```bash
cd /Users/wxy/Desktop/Partura && sed -n '1,120p' notes/F111_spearman_qclose/05_hypotheses.md
```

```
# 竞争性假设表(第 1 轮写定,跑第一个实验之前)

写法:每条写**它预测什么**、**哪个实验能杀死它**。状态列每轮更新。
"出处"里 `S0` = `digest F111_spearman_qclose S0_baseline`,`§` 指 `06_baseline.md` 的小节。
`04_grammar.md` 里的恒等式是**源码推导**,不是实验证据 —— 所以 H1 这一轮仍然是"未验证"。

最后更新:第 1 轮(主研),R1 工单已下,全部待验证。

---

## A 组:它到底是什么(分辨)

### H1 ——「全市场两两配对」是多余的:原式 ≡ 对一条市场路径的投影
`04_grammar.md` 第 2 步的恒等式:窗口完整时,原式的**截面序**等于
`Σ_k rc_i[k]·M[t,k]`(自己的 10 天秩路径 · 市场平均秩路径)的序。

- **预测**:(a) 用 numpy 按源码复算的 `proj = Σ_k rc_i·M` 与原式交易信号的逐日 rank 相关
  **≈ 1.00**(窗口完整的格子上;含 NaN 的格子上明显更低);(b) `proj` 当因子跑出来的多头腿
  与原式**基本相同**;(c) 表达式语言里写得出的近似版 `ts_corr(A, cs_mean(A), 10)`
  与原式 rank 相关**高**(我的先验 0.6~0.9,不是 1.0,因为 `M` 是**秩**的截面均值〈每只股票等权〉,
  而 `cs_mean(A)` 是**价格水平**的截面均值〈高价股主导〉)。
- **杀死它的实验**:R1 的 exec 脚本 `x1`(a)(b);R1 的 `S1_whatis / m_mktcorr`(c)。
  (a) 的 rank 相关若 < 0.9,说明我的推导漏了东西(最可能是 NaN 格子的占比比想的大),H1 被否定。
- **状态**:未验证。**它是本轮的主心骨**:H1 成立 ⇒ 这条因子的 O(N²) 结构没有信息价值,
  提纯方向立刻确定;H1 被否定 ⇒ 配对结构里有我没看懂的东西,后面全部要重想。

### H2 ——它是**条件动量**:B ≈ (市场 10 日趋势方向) × (自己的 10 日秩动量)
`04_grammar.md` 第 3 步,把 `M[t,·]` 一阶近似成线性斜坡的结果。

- **预测**:(a) `rank_corr(原式, ρ^time)` 按 `c(t)` 的符号分组后**符号相反、绝对值都明显大于
… (69 行略) …
S0 §7 的中性化:对 `all_controls` 中性化后残差**毛**超额从 +13.6% → **+0.1%**,
单独对 `ctl_amt` 中性化就掉到 +4.2%,`ctl_dvol20` 掉到 +7.9%。rank 相关 §10:
`known_stdamt_mean30` −0.42、`known_amt_max9` −0.38、`ctl_amt` −0.35,方向一致(高因子值 ≈ 低成交额)。
而且已知家族**单独**就比原式好:`known_stdamt_mean30` Lnet +12.6%/+22.3%、Lshp 1.78/3.46;
`known_stdamt_max9` +13.7%/+22.2%、1.99/3.59;**原式只有 +10.4%/+17.0%、1.79/3.07**(S0 §1/§9)。

- **预测**:对已知家族中性化之后,残差的多头腿**毛**超额大幅缩水;与已知家族等权相加,
  多头腿**不优于**已知家族单独。
- **杀死它的实验**:R1 exec `x1`(c):残差多头腿(毛/净都报)+ 相加组合多头腿,对三条
  `known_*` 各做一次。残差毛超额仍有 ≥ 2/3、或组合明显超过已知家族单独,则 H4 被否定(有增量)。
- **状态**:未验证。**这是决定这条因子对用户有没有价值的那一条**。
  注:§6.5 的"折叠会骗过秩空间线性中性化"在这里**不适用** —— `abs_corr=False`,
  根节点没有取绝对值/平方这类折叠,所以线性中性化对它是公平的检验。

### H10 ——它是**活跃度**共动而不是**价格**共动
如果共动的真正载体是成交额/关注度而不是价格路径,把叶子换成 `Amt` 应该同样好或更好。

- **预测**:`ts_spearman(day_quantile(Amt), 10)` 多头腿与原式相当或更好,且与 `known_*` 家族 rank 相关更高。
- **杀死它的实验**:R1 `S1_whatis / l_amt`。它明显更差 ⇒ H10 被否定,共动的载体是价格路径。
- **状态**:未验证。(和 H4 相关但不同:H4 问"是不是已知暴露",H10 问"换个载体是不是更好"。)
```

**10-04 15:00 · Bash** — Find variant expressions in R1 order

```bash
cd /Users/wxy/Desktop/Partura && grep -n "l_amt\|l_mean\|l_last\|t_tsrank\|s_pearson\|m_mktcorr" notes/F111_spearman_qclose/orders/R1.md | head -40
```

```
93:      - {id: m_mktcorr, group: substitute,
96:      - {id: s_pearson, group: substitute,
97:         expr: "ts_pearson(day_quantile(Close), 10)",
99:      - {id: l_mean, group: field,
102:      - {id: l_last, group: ablate,
105:      - {id: l_amt, group: field,
108:      - {id: t_tsrank, group: substitute,
116:  corr_ids:   [v_base, m_mktcorr, s_pearson, l_mean, l_last, l_amt, t_tsrank]
118:  #   profile:    追加 m_mktcorr, t_tsrank
119:  #   neutralise: 追加 m_mktcorr, t_tsrank     (v_base 的已有,S0 里读过了)
127:- `m_mktcorr` 混了两个面(`cs_mean` 是 nd/cs,`ts_corr` 是 nd/ts)——我查过 `cs_mean` 的源码,
131:  2. 如果两个都不行,**就把 `m_mktcorr` 从阶段里去掉并在结果卡里报错误原文**。
135:  `ts_spearman`(`l_mean`/`l_last`/`l_amt`)。如果 `wait` 两次(约 18 分钟)还没完,
245:| 7 | 同上 | m_mktcorr, t_tsrank | — | — | 中性化表(各控制变量的 R² + 残差 rIC/Lgross/Lnet)、分位剖面 Q1..Q10 |
```

**10-04 15:00 · Bash** — Read exact variant expressions

```bash
cd /Users/wxy/Desktop/Partura && sed -n '85,120p' notes/F111_spearman_qclose/orders/R1.md
```

```
### 第 2 项(服务器运行 1/2):阶段 `S1_whatis`,6 个变体

往 `configs/F111_spearman_qclose.yaml` 的 `stages:` 后面加:

```yaml
  - id: S1_whatis
    question: "ts_spearman 的全市场两两配对平均,等价于什么更简单的东西?预测力的载体是价格路径、活跃度,还是实现细节?"
    variants:
      - {id: m_mktcorr, group: substitute,
         expr: "ts_corr(day_quantile(Close), cs_mean(day_quantile(Close)), 10)",
         why: "H1:把 O(N²) 两两配对换成「和一条市场路径做相关」。恒等式说截面序应该高度一致;若 rank 相关高且多头腿相当,配对结构就是多余的(提纯)"}
      - {id: s_pearson, group: substitute,
         expr: "ts_pearson(day_quantile(Close), 10)",
         why: "H6:同样的全市场配对结构,去掉窗口内的秩变换。秩让每只股票在市场路径上等权,Pearson 则让 10 天内价格波动大的股票主导;若 Pearson 同样好,秩就只是个实现选择"}
      - {id: l_mean, group: field,
         expr: "ts_spearman(day_mean(Close), 10)",
         why: "H3:分钟均价几乎不可能出现跨日完全并列,而日内中位价落在 tick 网格上会并列、并列按日期顺序发秩=人工上升斜坡。若与原式差异明显,原式有一部分预测力来自这个实现瑕疵"}
      - {id: l_last, group: ablate,
         expr: "ts_spearman(day_last(Close), 10)",
         why: "H7:删掉日内折叠这一步,直接用当天收盘价。若相当,日内中位价是多余的(更简单的等价写法)"}
      - {id: l_amt, group: field,
         expr: "ts_spearman(day_quantile(Amt), 10)",
         why: "H10:把共动的载体从价格换成成交额。若同样好或更好,这条因子其实是活跃度共动,更靠近已知的成交额家族"}
      - {id: t_tsrank, group: substitute,
         expr: "ts_rank(day_quantile(Close), 10)",
         why: "H2:纯粹的 10 日秩位置动量,没有「乘市场趋势方向」这个条件化。原式明显优于它=条件化有用;相当=这条因子就是个 10 日动量的写法"}
```

诊断项:请**在现有列表里追加**(不要删掉已有的 `v_base`,它的面板有缓存):

```yaml
  corr_ids:   [v_base, m_mktcorr, s_pearson, l_mean, l_last, l_amt, t_tsrank]
  # diagnostics 里:
  #   profile:    追加 m_mktcorr, t_tsrank
  #   neutralise: 追加 m_mktcorr, t_tsrank     (v_base 的已有,S0 里读过了)
```
```

**10-04 15:00 · Bash** — Read hypotheses H5-H9

```bash
cd /Users/wxy/Desktop/Partura && sed -n '120,400p' notes/F111_spearman_qclose/05_hypotheses.md
```

```
---

## B 组:预测力在结构的哪一部分(提纯)

### H5 ——EMA 平滑的功劳**全部**是省成本,不改变信号内容
**【第 1 轮(重启)主研已自己把这条做完,不需要实验了。状态:已确立。】**

`books.sweep` 里**没有** `long_gross_ann` 字段(只有 `long_ann`/`long_sharpe`/`long_turnover`),
所以读不到。但我在 `partura/books.py` 里读到了精确的成本机制,于是毛超额可以**代数地精确复原**:

```
long_book():  net_daily = gross_daily − cost_per_side × traded,  traded = 2 × (上报的 turnover)
stats():      ann = mean(daily) × 252                    ← 是 252,不是我上一版用的 ~254
⇒  long_gross_ann = long_ann + 252 × 2 × 0.0015 × long_turnover = long_ann + 0.756 × long_turnover
```

**公式先在两个实测点上验过**(有实测 `long_gross_ann` 的地方只有这两处:
`books.by_rank.long.splits.train` 的 hl=20、`books.by_rank.ls.splits.train` 的 hl=10):
复原 13.53% vs 实测 13.558%(差 0.03pp);复原 14.83% vs 实测 14.869%(差 0.04pp)。
残差来自 `turnover` 在**全部**日子上取 nanmean、而 `ann` 只在 net 有限的日子上取均值,量级 ≤0.05pp。

| hl | LTO(实测) | 成本 | Lnet(实测) | **Lgross(复原)** | Lshp(实测) |
|---|---|---|---|---|---|
| 0 | 29.88% | 22.59pp | **−8.52%** | **+14.07%** | −1.63 |
| 1 | 19.08% | 14.42pp | −0.12% | **+14.30%** | −0.02 |
| 2 | 14.11% | 10.67pp | +4.53% | **+15.20%** | 0.81 |
| 3 | 11.56% | 8.74pp | +6.61% | **+15.35%** ← 最高 | 1.15 |
| 5 | 8.87% | 6.70pp | +7.44% | **+14.15%** | 1.26 |
| 10 | 6.08% | 4.60pp | +10.23% | **+14.83%**(实测 14.87) | 1.74 |
| 20 | 4.08% | 3.08pp | **+10.45%** | **+13.53%**(实测 13.56)← **最低** | 1.79 |
… (66 行略) …
## 本轮明确决定**不**做的事(以及为什么)

1. **不扫窗口 d**(5/20/30/50)。两个理由:
   (i) 扫法取决于 H1 —— H1 成立就该在便宜的 `ts_corr(A, cs_mean(A), d)` 形式上扫
   (`cross_*` 的窗口池到 60/241,`ts_*` 的到 50),而不是在 O(N²) 的 `ts_spearman` 上扫。
   **先定身份,再扫参数。**
   (ii) ⚠️ **第 1 轮重启时的修正**:上一版在这里写的是"它是最有希望的升华杠杆(H5)"。
   **这个理由已经没有了** —— H5 确立之后恰好**否掉**了它(毛超额在 hl>3 之后是下降的,
   半衰期轴是被耗尽而不是没用够;而且衰减表讲的是标签期限、不是平滑长度,
   不能当"更长的窗口会更好"的证据,详见 H5 一节末尾)。
   「更长的窗口 d」现在只是一个**未经检验的独立猜想**,优先级低于 H11 带出来的"升华方向 F"
   (把低波/市场跟随度这个暴露直接写干净);要做也得先立新假设,**不要引用 H5 当理由**。
2. **不做 `abs_corr=True` / `agg="std"` 变体**。按 H1 的恒等式,`abs_corr` 会破坏掉
   "线性投影"这个性质(取绝对值是折叠),它是一条**不同**的因子,不是这条的提纯;
   而且一旦引入折叠,§6.5 的"秩空间线性中性化看不见非单调关系"就开始适用,
   H4 的检验也要跟着换口径。留到身份定了之后再考虑。
3. **不验证 `day_quantile(Close, 0.5)` 与 `day_median(Close)` 是否逐位相同**(R0 异常第 4 条)。
   `l_mean` / `l_last` 已经覆盖了"叶子换一个统计量会怎样"这个有信息量的版本;
   逐位相同与否对任何结论都不构成影响。
4. **不碰封板票对空头腿的污染(H8a)**。多头腿不受它影响,对选拔结论无关;放到 R2 或报告阶段。
```

**10-04 15:00 · Bash** — Check window pools

```bash
cd /Users/wxy/Desktop/Partura && grep -rn "window" configs/F111_spearman_qclose.yaml | head -20; echo "=== pools ==="; grep -rn "50\|60\|241" partura/*.py 2>/dev/null | grep -i "pool\|window" | head -20
```

```
=== pools ===
partura/probes.py:163:        # A 40-row sample is blind to a 241-day window ("impulse memory = 27 days" was 40 - 13).
```

**10-04 15:00 · Bash** — Read playbook head

```bash
cd /Users/wxy/Desktop/Partura && sed -n '1,60p' docs/study_playbook.md
```

```
# 一次研究的操作手册(给做研究的 agent)

先读 `CLAUDE.md` 和 `docs/method.md`(为什么每条表达式都要重新推计划)。这份讲**怎么干**:
口径、工具、规矩、踩过的坑、要交什么。范例是 `research/alpha_distillation/F001_dwgated_covamtlow.md`
和 `notes/F001_dwgated_covamtlow/` —— 看它的**论证方式**(每个结论后面跟着哪个实验),不要抄它的实验清单。
(F001 用的是旧口径:普通标签 + 多空夏普;**现在的口径以本文为准**。)

---

## 0. 目标:提纯、分辨、升华

| | 要回答的问题 | 算做到了 |
|---|---|---|
| **分辨** | 这东西到底是什么?是不是某个已知暴露(成交额水平、规模、换手率、波动、动量、反转)换了个写法?和这批其他因子、和已知家族是不是同一个? | 有中性化的 R² 和残差表现、有 rank 相关、有"把可疑节点换成它的朴素等价物"的直接替换实验 |
| **提纯** | 预测力在树的哪一部分?哪些节点、指数、窗口、字段是多余的? | 给出一个**更小**的结构,在 train 和 valid 上保住(或超过)原式;每删一个节点都有实验 |
| **升华** | 看懂机制之后,能不能写出一个**更好用**的版本? | 见下面的"选拔口径" |

### 选拔口径(用户 2026-10-04 明确定的,不要改)

**用户做的是 A 股纯多头,空头腿做不了。所以选拔只看一件事:多头腿扣费之后能拿到多少。**

1. **第一判据:多头腿净超额(扣 15 bp)与纯多头夏普**,半衰期按**纯多头书**在 fit 段选(`rank_by: long`)。
2. **半衰期是可以调的杠杆,它带来的多头腿净超额是真的、能交易到的。**
   第一组五条因子里,原式只是把半衰期从「为多空夏普选的」(常常 1~3)换成「为多头腿选的」(10~20),
   样本外多头腿净超额就多 1~3 个点。所以:
   - **「原式 + 多头最优半衰期」永远是候选之一**,它就是表里 `v_base` 在「半衰期(多头)」下的那一行,
     也是任何结构候选要比过的**第一条基准**;
   - 一个候选的改进如果全部来自更长的半衰期,它**照样可以被推荐**(更简单、换手更低、净超额更高就是更好用),
     但**归因要写对**:写「改进来自平滑」,不要写成「删节点的功劳」「新结构的功劳」。
3. 多空夏普是**次要**信息(用户最早那张表的口径),每个变体都会同时算出来,用来和那张表对照、以及理解空头腿。
… (10 行略) …

- **标签**:`open_vwap15` h=1 **可买入版** —— t 日收盘后决策,t+1 开盘 15 分钟 VWAP 买入,t+2 同一价卖出;
  t+1 开盘封涨停买不进的票标签是 NaN(放在多头里当天记 0,放在空头里也记 0 —— 这会抬高空头腿)。
- **数据段**:`train` 20180102–20211231、`valid` 20220101–20230807、`utrain` = 两者之和 = **用户的训练段**、
  `holdout` 20230808–20251231 = **用户的测试段**。
- **方向**:rank IC 的符号。**半衰期**:因果 EMA,在 {0,1,2,3,5,10,20} 里选;每个变体都按两种规则各选一次 ——
  **多头口径**(按纯多头书的扣费超额夏普,选拔用)和**多空口径**(按十分位多空的扣费夏普,对照用)。
  方向与半衰期都只在 fit 段上定一次,然后原样用到别的段。
- **两本书**:前/后 10% 等权多空(gross 1),每单位换手 15 bp;多头腿当成一本纯多头书,减去当天
  有信号有标签的票的等权收益。
- **两套数字,别混**:
  - *决策口径*:方向/半衰期在 `train` 上定,`valid` 是没见过的。**挑变体只看这套。**
  - *用户口径*:方向/半衰期在 `utrain` 上定,对应用户表的"训练"列;`holdout` 对应"测试"列,**只在最后读一次**。
- **诊断看的是实际交易的信号**(方向 × 面板、按选定半衰期平滑之后):中性化、条件 IC、衰减、rank 相关矩阵都是。
  很多因子原始日频面板逐日抖得厉害,平滑后才值钱;原始面板上的 rank IC(`rIC`)和交易信号的(`rICtraded`)都会打印。
  中性化的残差不再平滑,换手更高 —— 残差的**净值类指标可能只因为成本就塌掉**,alpha 还在不在看残差的 rank IC 和毛超额。

`study.sh digest` 的列:`hlL` 多头口径半衰期 · `Lnet` **多头腿净超额** · `Lshp` 纯多头夏普 · `Lgross` 多头腿毛超额 ·
`LTO` 多头日换手 ‖ `hlS` 多空口径半衰期 · `LS` 扣费多空夏普 · `short` 空头腿毛超额 ‖ `cov`/`dist` 两道门槛。
下面还有一张**固定半衰期**对照表(每个变体在 hl 0/2/5/10/20 下的多头腿)—— 判断"是结构还是平滑"就看它。
```

**10-04 15:00 · Bash** — Read ts_spearman source

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh src ts_spearman 2>&1 | head -60
```

```
### ts_spearman  face=nd family=ts category=rolling axis=D reduces_m=False lookahead=False kernel=nd_ts.ts_spearman
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_ts.py:483
@op("nd", "ts", arity=1, requires_window=True)
def ts_spearman(data: torch.Tensor, d: int, abs_corr: bool = False, agg: str = "mean") -> torch.Tensor:
    """Rolling rank (Spearman) correlation counterpart to `ts_pearson`.

    NOTE ON THE REMAINING PYTHON LOOP: this keeps the original's
    `for i in range(N)` outer loop over stocks (vectorizing only the
    `j != i` inner computation). A fully `ts_pearson`-style `(T, d, N, N)`
    all-pairs tensor is possible in principle, but ranks require an
    `argsort` per window per stock BEFORE the pairwise step, which makes
    the fully vectorized version substantially more memory (an extra
    `(T, d, N)` rank tensor broadcast to `(T, d, N, N)` pairwise products,
    same as Pearson) without a correspondingly large win, since the
    per-stock rank computation itself is already vectorized outside the
    loop. Given this task's priority is fixing outright bugs and
    dropping dead/redundant code over maximally vectorizing every exotic
    function, the loop (over stocks, i.e. `O(N)`, not `O(T)`) is kept.
    """
    if agg not in ("mean", "std"):
        raise ValueError("agg must be 'mean' or 'std'")
    D, N = data.shape
    d = int(d)
    if d <= 1 or D < d:
        return torch.full((D, N), float("nan"), device=data.device, dtype=data.dtype)

    windows = data.unfold(0, d, 1).transpose(1, 2)  # [T, d, N]
    T = windows.size(0)
    mask = ~torch.isnan(windows)

… (10 行略) …

    for i in range(N):
        rc_i = ranks_centered[:, :, i]
        std_i = rank_std[:, i]
        mask_i = mask[:, :, i]

        j_indices = [j for j in range(N) if j != i]
        if not j_indices:
            continue

        rc_j_all = ranks_centered[:, :, j_indices]
        std_j_all = rank_std[:, j_indices]
        mask_j_all = mask[:, :, j_indices]

        valid = mask_i.unsqueeze(-1) & mask_j_all
        prod = rc_i.unsqueeze(-1) * rc_j_all
        prod_masked = torch.where(valid, prod, torch.zeros_like(prod))

        sum_prod = prod_masked.sum(dim=1)
        num_valid = valid.sum(dim=1).to(windows.dtype)
```

**10-04 15:00 · Bash** — Read playbook sections 2-6

```bash
cd /Users/wxy/Desktop/Partura && sed -n '60,200p' docs/study_playbook.md
```

```
下面还有一张**固定半衰期**对照表(每个变体在 hl 0/2/5/10/20 下的多头腿)—— 判断"是结构还是平滑"就看它。

---

## 2. 工具:全部通过 `scripts/study.sh`(在 `~/Desktop/Partura` 下跑)

服务器上的 AlphaCube 才是算子实现的**唯一事实来源**(本机那份是另一个 commit,还有别人没提交的改动)。

```bash
cd ~/Desktop/Partura
./scripts/study.sh brief <fid>                   # **开工第一件事**:交接页 —— 做到哪了、研究日志、已跑的运行、已写的 notes(§7)
./scripts/study.sh note <fid> "<一句话>" <<'EOF'  # 记一条研究日志(正文走 stdin);每看完一个结果记一条(§7)
…
EOF
./scripts/study.sh ops '^cross_'                 # 有哪些算子(名字、面/族/类、可用窗口)
./scripts/study.sh src day_skew cs_demean        # 内核源码(连同它调用的底层函数)—— 每个用到的算子都要读
./scripts/study.sh decompose <fid>               # 算子档案(探针实测)+ SSA 分解 + 实验室里的相关先验
./scripts/study.sh propose <fid>                 # 从这棵树派生的候选实验 —— 草稿,要删改
./scripts/study.sh check <fid>                   # 配置里每条表达式能不能解析、是不是合法的根。run 之前必跑
./scripts/study.sh list <fid>                    # 这个研究在服务器上**已经跑过**哪些 tag(含本地还没拉回的)
./scripts/study.sh run <fid> <tag> <stage...>    # 起一个阶段(立刻返回);tag 是输出文件名
./scripts/study.sh wait <fid> <tag>              # 等它(最多 540 秒,没完就再调一次);完了自动拉回并打印摘要
./scripts/study.sh digest <fid> <tag> [base_id]  # 重看某次的摘要
./scripts/study.sh exec <fid> <tag> <script.py>  # 跑 studies/<fid>/<script.py>(自己写的分析),同样用 wait 等
./scripts/study.sh final <fid> <tag> <stage>     # 读留出段的那一次(整个研究只许一次)
./scripts/study.sh report <fid>                  # 推 notes、在服务器上拼报告、拉回 research/alpha_distillation/<fid>.md
./scripts/study.sh status                        # 服务器上现在有哪些 Partura 任务
```

- `wait` 要给 Bash 工具设 `timeout: 600000`。排队是正常的:服务器同时最多 2 个 Partura 进程,引擎求值一次只跑一个;
… (91 行略) …
8. **边做边落盘**(§7):开工先 `brief`;每看完一个结果先 `note` 再做下一步;notes 跟着进度写。
   研究随时可能被打断、由另一个模型接手 —— 没有写进文件的判断,等于没有做过。

---

## 5. 要交的东西

`notes/<fid>/` 下的手写段落(中文,英文术语保留;写法看 F001 和第一组的 notes):

| 文件 | 内容 |
|---|---|
| `journal.md` | 研究日志(§7):只追加;每看完一个结果一条。不进报告正文,是给接手的人看的 |
| `01_expression.md` | 这条因子的来历、一句话说它是什么 |
| `02_operators.md` | (可选)读源码时发现的、探针表里看不出来的事 |
| `03_decomposition.md` | 分解表之外需要说明的:关键公式、容易被名字骗的地方 |
| `04_grammar.md` | 结构语法:事件 → 记忆 → 门控 → 放大… |
| `05_hypotheses.md` | 竞争性假设表:每条写"预测什么""哪个实验能杀死它"。**在跑实验之前写** |
| `06_baseline.md` | 基线读法:多头腿在两种半衰期下各是多少、钱在多头腿还是空头腿、分位剖面是不是单调、逐年、衰减 |
| `07_<stage_id>.md` | 每个阶段的结论(问题 → 结果 → 解读),文件名里的 stage_id 要和配置一致 |
| `07_neutralise.md` / `07_conditional.md` / `07_controls.md` | 对应诊断表的解读 |
```

**10-04 15:00 · Bash** — Check operator window pools

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh ops '^ts_spearman$|^ts_pearson$|^day_last$|^day_mean$|^cross_mean$' 2>&1 | head -30
```

```
# 搜索语法内的注册表算子(带 win 的需要窗口参数,写在最后一个位置):
  cross_mean                         dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  day_last                           dt/day/unary        arity 1 axis M
  day_mean                           dt/day/unary        arity 1 axis M
  ts_pearson                         nd/ts/rolling      arity 1 axis D win [1, 5, 10, 20, 30, 40, 50]
  ts_spearman                        nd/ts/rolling      arity 1 axis D win [1, 5, 10, 20, 30, 40, 50]
# 只在完整库里的通用调用(手写因子用的;参数含字面量,签名看 src):
```

**10-04 15:00 · Bash** — Read playbook sections 6-7

```bash
cd /Users/wxy/Desktop/Partura && sed -n '200,330p' docs/study_playbook.md
```

```
| `07_neutralise.md` / `07_conditional.md` / `07_controls.md` | 对应诊断表的解读 |
| `07x_<序号>_<name>.md` | 自己写的分析(studies/ 下脚本)的结果与解读;加序号是因为报告按文件名排序拼接 |
| `08_variants.md` | 怎么读总表、哪些变体其实是同一个东西 |
| `09_diagnosis.md` | 机制诊断:已确立 / 合理但未坐实 / 未决 |
| `10_distilled.md` | **读留出段之前**:候选排序与判据;**读之后**:结果、推荐、为什么比原式好(或为什么没有更好的) |
| `11_risks.md` | 失效模式:泄漏、过拟合、尺度污染、已知暴露、容量、成本、制度依赖 |
| `12_next.md` | 只列能显著降低不确定性的下一步 |

最后 `./scripts/study.sh report <fid>`,并**把生成的报告从头读一遍**:表里有没有空的、notes 里引的数字和表对不对得上。

---

## 6. 第一组研究里,审查反复抓到的问题(开工前读;不要等审查来抓)

第一组五条因子的研究都被独立审查提了 3~6 条 major。下面这些是**重复出现**的,和具体因子无关:

1. **归因写错:把平滑的功劳记到结构头上**。原式按多空口径选到的半衰期常常很短(1~3);候选选到 10 或 20,
   换手减半,多头腿净超额自然高几个点。这个改进是**真的、可以推荐**(见 §0),但要写成「来自更长的半衰期」。
   想说「结构更好」,就必须在**同一个半衰期**下比(固定半衰期表),并且比过 `v_base` 的多头口径那一行。
2. **「升华版」其实是已知家族**。候选的多头腿好,是因为它滑向了成交额水平家族(`cross_max/mean(day_std(Amt), 9~60)`:
   第一组里它在测试段的多头腿净超额是 +13%~+15%、纯多头夏普 1.4~1.9)。推荐它没问题,但要**说清楚它是什么**:
   「对只能做多的用户,这条因子相对已知家族有 / 没有增量」。有没有增量的检验:候选对已知家族中性化后的残差
   多头腿、以及候选与已知家族相加之后的多头腿。
3. **候选与原式的 rank 相关低于约 0.8,就不是提纯,是换了一条因子**。可以推荐,但必须这么写。
4. **读完留出段之后改推荐、加「已确立」**。读完之后,推荐就是事前的第一推荐;留出段否定了它,就写「被否定」。
   读完留出段才冒出来的「规律」(尤其是只靠某一年)最多算「合理但未坐实」。
5. **秩空间的线性中性化看不见非单调关系**。因子里有 `abs_`、`cs_demean` 后取绝对值、平方这类折叠时,
   它和任何单调控制变量的 rank 相关都接近 0、R² 很低 —— 这不说明它不是已知暴露。要用**同样折叠过的控制变量**去量。
6. **空头腿被「买不进的票」抬高**。次日开盘封涨停的票标签是 NaN,在空头里记 0 收益。涨停、一字板相关的因子
   (峰度、集中度、极端收益类)空头腿和多空夏普会因此虚高 0.5 以上 —— 用 `st.target(buyable=False)` 按**收益贡献**去量。
… (30 行略) …
4. **三个必须落盘的时点**(各记一条日志):
   ① 假设表定稿(跑第一个实验之前);
   ② **读留出段之前** —— 候选、排序、判据写进 `10_distilled.md`,**然后**才 `final`;
   ③ 读完留出段 —— 每条判据是过了还是被否定,推荐是谁。
5. **收尾**:返回结构化结果之前,最后记一条「研究完成:推荐 X(半衰期 …),理由 …;未决的是 …」。
6. **研究现状 `notes/<fid>/state.md`** —— 日志是流水(只追加),这一页是「现在的理解」(每次**整个覆盖重写**),接手的人最先读它。
   每看完一个结果就更新。固定 8 节,宁可啰嗦:
   1) 一句话现状;2) 中间结果:量到的事实,每条带数字和出处(tag / 脚本 / 变体 / 哪一段 / 哪种口径);
   3) 研究过程与逻辑:做了什么、为什么这么走、源码里和名字不一样的地方;
   4) **假设表**:编号 | 假设 | 状态(未验证 / 被支持 / 被否定 / 已改写)| 证据与出处 | 还差什么才能定;
   5) 当前的候选(提纯 / 升华):表达式、train/valid 多头口径数字、为什么是它;已排除的候选与原因;
   6) **后面的研究思路**:按顺序,每步做什么、想回答什么、哪种结果意味着什么;明确决定不做的事和原因;
   7) 留出段:未读 / 已读(读前登记在哪);8) 给接手者的提醒:工具的坑、还没看结果的任务、写了一半的文件。
7. **分层接力**(用户定的分工,见 `handoff/README.md`):「主研」(Opus 5)管思路 —— 假设、裁决、设计实验、选候选、下结论,
   把要做的事写成工单 `notes/<fid>/orders/R<n>.md`;「执行」(Sonnet 5)管实现 —— 写配置和脚本、跑服务器、读结果,
   写成结果卡 `notes/<fid>/results/R<n>.md`。每一轮都是新的 agent,彼此只靠这些文件传话。工单要写到执行不需要猜
   (完整表达式、要带回来的每个数字);结果卡只写事实和异常,不替主研下结论。
8. `handoff/` 不用你管:后台记录器(`scripts/recorder.py`,不依赖任何模型和额度)会把你返回的结构化结果
   (`handoff/<fid>/results/`)、你的动作流水(`handoff/<fid>/agents/`)和交接页(`handoff/<fid>/STATE.md`)自动存下来。
   批次的总体进度在 `handoff/STATUS.md`,怎样重启在 `handoff/README.md`。
```

**10-04 15:01 · agent 的话**

Window pool for `ts_spearman` is [1,5,10,20,30,40,50]. Let me check whether the conditional-momentum form from block (b) is writable in the expression language.

**10-04 15:01 · Bash** — Search for trend/slope/rank operators

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh ops 'slope|trend|regress|linear|time|_rank|corr' 2>&1 | head -50
```

```
# 搜索语法内的注册表算子(带 win 的需要窗口参数,写在最后一个位置):
  cross_autocorr_s1                  dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_corr                         dt/cross/pair_rolling arity 2 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_decay_linear                 dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_rank                         dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cs_rank                            nd/cs/unary        arity 1 axis S
  day_autocorr_n1                    dt/day/unary        arity 1 axis M
  day_corr                           dt/day/binary       arity 2 axis M
  in_autocorr_s1                     dt/in/rolling      arity 1 axis M win [3, 5, 10, 15, 30, 60, 241]
  in_corr                            dt/in/pair_rolling arity 2 axis M win [3, 5, 10, 15, 30, 60, 241]
  in_decay_linear_rolling            dt/in/rolling      arity 1 axis M win [3, 5, 10, 15, 30, 60, 241]
  in_rank                            dt/in/unary        arity 1 axis M
  in_rank_rolling                    dt/in/rolling      arity 1 axis M win [3, 5, 10, 15, 30, 60, 241]
  nt_cs_rank                         nt/cs/unary        arity 1 axis S
  nt_ts_autocorr_s1                  nt/ts/rolling      arity 1 axis M win [3, 5, 10, 15, 30, 60]
  nt_ts_corr                         nt/ts/pair_rolling arity 2 axis M win [3, 5, 10, 15, 30, 60]
  nt_ts_decay_linear                 nt/ts/rolling      arity 1 axis M win [3, 5, 10, 15, 30, 60]
  nt_ts_rank                         nt/ts/rolling      arity 1 axis M win [3, 5, 10, 15, 30, 60]
  ts_autocorr_s1                     nd/ts/rolling      arity 1 axis D win [1, 5, 10, 20, 30, 40, 50]
  ts_corr                            nd/ts/pair_rolling arity 2 axis D win [1, 5, 10, 20, 30, 40, 50]
  ts_decay_linear                    nd/ts/rolling      arity 1 axis D win [1, 5, 10, 20, 30, 40, 50]
  ts_rank                            nd/ts/rolling      arity 1 axis D win [1, 5, 10, 20, 30, 40, 50]
# 只在完整库里的通用调用(手写因子用的;参数含字面量,签名看 src):
  column_correlation                 nd/ts  axis D reduces_m False
  cross_autocorr                     dt/cross  axis D reduces_m False
  day_autocorr                       dt/day  axis M reduces_m True
  decay_linear_last                  shared/elementwise  axis None reduces_m False
  in_autocorr                        dt/in  axis M reduces_m False
  masked_multivariate_regression     dt/in  axis M reduces_m False
  ts_autocorr                        nd/ts  axis D reduces_m False
```

**10-04 15:01 · Bash** — List cs_ and arithmetic operators

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh ops '^cs_|^mul$|^div$|^add$' 2>&1 | head -40
```

```
# 搜索语法内的注册表算子(带 win 的需要窗口参数,写在最后一个位置):
  add                                shared/elementwise/binary       arity 2 axis None
  cs_demean                          nd/cs/unary        arity 1 axis S
  cs_mask_top_replace_mean           nd/cs/unary        arity 1 axis S
  cs_mask_top_replace_mean_neg       nd/cs/unary        arity 1 axis S
  cs_mean                            nd/cs/unary        arity 1 axis S
  cs_median                          nd/cs/unary        arity 1 axis S
  cs_normalize                       nd/cs/unary        arity 1 axis S
  cs_quantile_q25                    nd/cs/unary        arity 1 axis S  [boolean_output]
  cs_quantile_q50                    nd/cs/unary        arity 1 axis S  [boolean_output]
  cs_quantile_q75                    nd/cs/unary        arity 1 axis S  [boolean_output]
  cs_rank                            nd/cs/unary        arity 1 axis S
  cs_regres                          nd/cs/binary       arity 2 axis S
  cs_scale                           nd/cs/unary        arity 1 axis S
  cs_stddev_full                     nd/cs/unary        arity 1 axis S
  cs_sum                             nd/cs/unary        arity 1 axis S
  div                                shared/elementwise/binary       arity 2 axis None
  mul                                shared/elementwise/binary       arity 2 axis None
# 只在完整库里的通用调用(手写因子用的;参数含字面量,签名看 src):
  cs_quantile                        nd/cs  axis S reduces_m False
```

**10-04 15:04 · Bash** — Read the config file

```bash
cd /Users/wxy/Desktop/Partura && cat configs/F111_spearman_qclose.yaml
```

```
# Partura study F111_spearman_qclose  (挖掘 / #953)
# 这份文件只有 S0_baseline 是生成的。后面的阶段、变体、额外控制变量、探针,都要按**这棵树**来写。
factor_id: F111_spearman_qclose
title: "(读完这棵树之后,用一句话写它是什么)"
expression: "ts_spearman(day_quantile(Close), 10)"
baseline_id: v_base

# 用户表里公布的这一行(pick_single_factors 的口径);S0 要先把它复现出来
published: {sign: 1, hl: 10, ls: [2.62, 1.1], long: [0.164, 0.075], lib: "挖掘", name: "#953"}

label: {kind: open_vwap15, horizon: 1, buyable: true,
        verify_against: /root/autodl-tmp/AlphaCube/_bench/trainto/allfac_buyable/_target.npy}
cost_per_side: 0.0015
top_frac: 0.10
rank_by: long          # 半衰期按纯多头书选(用户实际能做的那本书);多空口径每个变体也都会算
horizons: [1, 2, 3, 5, 10, 20]
warmup: 60

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
… (37 行略) …
    question: "ts_spearman 的全市场两两配对平均,等价于什么更简单的东西?预测力的载体是价格路径、活跃度,还是实现细节?"
    variants:
      - {id: m_mktcorr, group: substitute,
         expr: "ts_corr(day_quantile(Close), cs_mean(day_quantile(Close)), 10)",
         why: "H1:把 O(N²) 两两配对换成「和一条市场路径做相关」。恒等式说截面序应该高度一致;若 rank 相关高且多头腿相当,配对结构就是多余的(提纯)"}
      - {id: s_pearson, group: substitute,
         expr: "ts_pearson(day_quantile(Close), 10)",
         why: "H6:同样的全市场配对结构,去掉窗口内的秩变换。秩让每只股票在市场路径上等权,Pearson 则让 10 天内价格波动大的股票主导;若 Pearson 同样好,秩就只是个实现选择"}
      - {id: l_mean, group: field,
         expr: "ts_spearman(day_mean(Close), 10)",
         why: "H3:分钟均价几乎不可能出现跨日完全并列,而日内中位价落在 tick 网格上会并列、并列按日期顺序发秩=人工上升斜坡。若与原式差异明显,原式有一部分预测力来自这个实现瑕疵"}
      - {id: l_last, group: ablate,
         expr: "ts_spearman(day_last(Close), 10)",
         why: "H7:删掉日内折叠这一步,直接用当天收盘价。若相当,日内中位价是多余的(更简单的等价写法)"}
      - {id: l_amt, group: field,
         expr: "ts_spearman(day_quantile(Amt), 10)",
         why: "H10:把共动的载体从价格换成成交额。若同样好或更好,这条因子其实是活跃度共动,更靠近已知的成交额家族"}
      - {id: t_tsrank, group: substitute,
         expr: "ts_rank(day_quantile(Close), 10)",
         why: "H2:纯粹的 10 日秩位置动量,没有「乘市场趋势方向」这个条件化。原式明显优于它=条件化有用;相当=这条因子就是个 10 日动量的写法"}
```

**10-04 15:04 · agent 的话**

I have the full picture. Let me write the stage interpretation first.

**10-04 15:05 · 写文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/07_S1_whatis.md`(4750 字符)

**10-04 15:08 · 写文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/07x_1_identity.md`(8555 字符)

**10-04 15:08 · agent 的话**

Now updating the hypothesis table with verdicts.

**10-04 15:08 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- 最后更新:第 1 轮(主研),R1 工单已下,全部待验证。

---
+ 最后更新:**第 2 轮(主研)**,R1 的结果(`results/R1.md`)已回,下面每条都已裁决。

## 第 2 轮裁决总表(证据全在 `07_S1_whatis.md` 与 `07x_1_identity.md`)

| 编号 | 一句话 | 裁决 | 一个关键数字 |
|---|---|---|---|
| H1 | 全市场两两配对多余 ≡ 对一条市场路径的投影 | **已确立**(但提纯后果与预期相反) | 窗口完整格子上逐日 Spearman **1.0000**(p05 0.9999);`m_mktcorr` 只有 0.742 |
| H2 | 它是条件动量(市场趋势 × 自己的秩动量) | **被支持,但只描述了一半**(钱在这一半) | `f` vs `c·ρ^time` 0.5381;`ρ^time` 单独 −5.6%/−0.7% → `c·ρ^time` +9.2%/+18.6% |
| H3 | 并列值造的人工斜坡在偷预测力 | **被否定** | `l_mean`(无并列叶子)rank 相关 **0.994**、LTO 同为 4.1% |
| H4 | 对纯多头用户,相对已知家族没有增量 | **被强烈支持,差最后一步** | 组合 w=0.25 在 valid 上 −0.83 / −0.16 / +0.40 pp(噪声 ±3pp) |
| H5 | 平滑的功劳全部是省成本 | **已确立**(第 1 轮) | 毛超额 hl0→hl20:+14.07% → +13.53%(最低的一行) |
| H6 | 窗口内的**秩**变换是关键 | **被否定** | `s_pearson` rank 相关 0.978、Lnet +10.7%/+16.9% |
| H7 | 日内折叠多余,用收盘价一样好 | **成立** | `l_last` 同半衰期下差 ≤0.86pp(噪声内),rank 相关 0.961 |
| H8 | 空头腿被封板票抬高 | **未决**(没量) | `long_share` 只有 36.7%/39.0% |
… (8 行略) …
`m_mktcorr`(先对价格水平取截面均值、再归一)没有这一步,valid 多头腿塌到 +4.9%、夏普 0.74。
⇒ 市场共识路径必须**每只股票等权**。详见 `07_S1_whatis.md` 第 1 节。

---
```

10-04 15:08 · 读 `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

**10-04 15:09 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- 最后更新:第 1 轮(主研),R1 工单已下,全部待验证。

---

## A 组:它到底是什么(分辨)
+ 最后更新:**第 2 轮(主研)**,R1 的结果(`results/R1.md`)已回,下面每条都已裁决。

## 第 2 轮裁决总表(证据全在 `07_S1_whatis.md` 与 `07x_1_identity.md`)

| 编号 | 一句话 | 裁决 | 一个关键数字 |
|---|---|---|---|
| H1 | 全市场两两配对多余 ≡ 对一条市场路径的投影 | **已确立**(但提纯后果与预期相反) | 窗口完整格子上逐日 Spearman **1.0000**(p05 0.9999);`m_mktcorr` 只有 0.742 |
| H2 | 它是条件动量(市场趋势 × 自己的秩动量) | **被支持,但只描述了一半**(钱在这一半) | `f` vs `c·ρ^time` 0.5381;`ρ^time` 单独 −5.6%/−0.7% → `c·ρ^time` +9.2%/+18.6% |
| H3 | 并列值造的人工斜坡在偷预测力 | **被否定** | `l_mean`(无并列叶子)rank 相关 **0.994**、LTO 同为 4.1% |
| H4 | 对纯多头用户,相对已知家族没有增量 | **被强烈支持,差最后一步** | 组合 w=0.25 在 valid 上 −0.83 / −0.16 / +0.40 pp(噪声 ±3pp) |
| H5 | 平滑的功劳全部是省成本 | **已确立**(第 1 轮) | 毛超额 hl0→hl20:+14.07% → +13.53%(全表最低) |
| H6 | 窗口内的**秩**变换是关键 | **被否定** | `s_pearson` rank 相关 0.978、Lnet +10.7%/+16.9% |
| H7 | 日内折叠多余,用收盘价一样好 | **成立** | `l_last` 同半衰期下差 ≤0.86pp(噪声内),rank 相关 0.961 |
| H8 | 空头腿被封板票抬高 | **未决**(没量) | `long_share` 只有 36.7%/39.0% |
… (12 行略) …

---

## A 组:它到底是什么(分辨)
```

**10-04 15:09 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- - **状态**:未验证。**它是本轮的主心骨**:H1 成立 ⇒ 这条因子的 O(N²) 结构没有信息价值,
  提纯方向立刻确定;H1 被否定 ⇒ 配对结构里有我没看懂的东西,后面全部要重想。
+ - **状态(第 2 轮)**:**已确立,而且是恒等而非近似。** 窗口完整的格子(占有标签格子的 **98.70%**)上
  `proj` 与 `f` 的逐日 Spearman mean/median/p95 全是 **1.0000**、p05 **0.9999**;全部格子 0.9974。
  `proj` 自己当因子 Lnet **+10.95%/+17.09%**、Lshp 1.88/3.09(原式 +10.4%/+17.0%、1.79/3.07),
  比原式略好 0.5pp —— 因为它少了源码里分母口径不一致那个瑕疵(只影响约 1.3% 的停牌/新股格子)。
  预测 (c) 也**精确命中**:`m_mktcorr` rank 相关 **0.742**,落在事前写下的 0.6~0.9 区间里,
  塌的机制(`cs_mean` 平均价格水平、高价股主导)正是事前写下的那一条。
- **⚠️ 但提纯后果和第 1 轮的预期相反**:恒等式成立**不等于**有便宜的等价写法。
  承重件是「**等权**共识路径 `M`」,而 `cs_mean` 给不出 `M`。见上面的「新发现」一段。
  能用的便宜写法只剩 `ts_pearson`(0.978,chunked matmul,比带 Python 循环的 `ts_spearman` 快得多)。
```

**10-04 15:09 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
-   则线性斜坡近似不成立 —— H2 被否定,但 H1 可以独立地仍然成立(`M` 不是直线而是别的形状)。
- **状态**:未验证。
+   则线性斜坡近似不成立 —— H2 被否定,但 H1 可以独立地仍然成立(`M` 不是直线而是别的形状)。
- **状态(第 2 轮)**:**被支持,但只描述了一半 —— 而钱全在这一半。**
  事前的两条判据(「两边都 >0.8 = 很紧」/「两边都 <0.5 = 很松」)**都没有被干净触发**
  (实测 `c>0` 天 +0.4712、`c<0` 天 −0.5991),所以这里给出主研的裁决:
  - 预测 (a) **成立**:无条件相关 −0.0885 ≈ 0,按 `c(t)` 符号分组后变号 +0.47 / −0.60。
    这解释了 `ctl_mom20` 只有 −0.078 —— **不是和动量无关,是条件化把无条件相关抵消了**。
  - 预测 (b) **成立**:`f` vs `c·ρ^time` 0.5381,远高于 `f` vs `ρ^time` 的 −0.0885。
  - 预测 (c) **成立且很强**:`ρ^time` 单独 Lnet **−5.60%/−0.71%**(sign 还被选成 −1),
    乘上当天的全市场标量 `c(t)` 之后变成 **+9.23%/+18.62%**(毛 +14.47%/+23.75%,两段都高于原式的毛)。
    `t_tsrank` 在**全部 7 个半衰期上多头腿都是负的**、对 `ctl_mom20` 的 R² 0.420(`v_base` 只有 0.056)。
  - **但不能写成恒等**:0.5381 按 playbook §6.3 的尺度(<0.8 就是另一条因子)说明 `M` 里有大量非线性形状;
    那一半形状对多头腿**没有可测量的贡献**(`c·ρ^time` 的书已经和原式一样好)。
  - 报告里的写法:「**alpha 在与市场方向的交互里,不在自己的动量里**」(这句已确立,三条独立证据);
    「原式 ≈ 条件动量」只能写成「条件动量这一半复现了多头腿的全部收益,相关 0.54」。
```

**10-04 15:10 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- - **状态**:**合理但未坐实**。预测 1 已被本轮的毛超额平线支持;预测 2 是对已有读数的**事后解释**
  (不算独立证据);预测 3 要等 R1 block (c)。
+ - **状态(第 2 轮)——一半成立、一半被否定,措辞已改写**:
  - **成立的部分**:`c₁(t) > 0` 的不变量没有被任何数据反对,而且有两条正面证据 ——
    H5 的毛超额平线(hl 0→20 只掉 0.5pp)、以及 `c·ρ^time`(一个确实会随 `c` 翻面的量)
    在 hl=20 上毛超额仍有 +14.47%。**被 20 天 EMA 平滑的那个对象(`f` 自己)从来没有翻面**,
    所以平滑穿过变号不伤信号。预测 1 ✔。
  - **预测 3 ✔(方向)但要降格**:(c4) 的 `|rank_corr(f, known)|` 随 hl **单调上升**
    (mean30 0.2323→**0.3704**;stdamt_max9 0.3088→0.3869;amt_max9 0.2953→0.3802),
    但 hl=0 上就已经有 0.23~0.31。⇒ 正确的说法是「平滑把这个暴露**提浓**了 0.07~0.14」,
    **不是**「平滑把它转化成了低波因子」。
  - **预测 2 的机制标签被否定**:H11 原话把这个暴露叫「**反向特质波动**」,
    但 rank 相关表直接反对:`ctl_ivol` **−0.153**、`ctl_cap` −0.177、`ctl_mom20` −0.078,
    而 `ctl_amt` **−0.352**、`ctl_dvol20` −0.306、`known_stdamt_mean30` **−0.423**。
  - **改写后的 H11**:被交易的是「秩空间的市场路径吻合度」,它的截面暴露是
    **低成交额 / 低成交额离散度(安静、小、便宜的股票)**,**不是**低特质波动。
    机制读起来也更顺:安静的股票没有自己的消息,10 天路径就是市场路径的一份干净拷贝 ⇒ 高 `f`。
    block (d) 的并列剖面是一条独立的自证:并列(= 这几天估值没怎么动)占比按十分位单调升到 Q10 的 51%。
  - **它对 H4 的作用降低了**:H11 曾被当成「它和 `day_std(Amt)` 家族是同一个暴露」的机制依据。
    改写之后这个依据变弱了 —— `l_amt`(把载体直接换成 `Amt`)不但更差(+2.1%/+7.9%),
    和三条家族的相关(−0.24~−0.25)**还比 `v_base` 的(−0.37~−0.42)更低**。
    ⇒ 和家族的重叠是**副产物**(都偏爱安静的股票),不是「它本质上在量活跃度」。
    **H4 现在只能靠组合书 / 双重排序的直接证据,不能靠 H11 的机制论证。**
```

**10-04 15:10 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- - **状态**:未验证。**这条是"泄漏/瑕疵"类风险,必须有答案才能写报告**(不管结论是哪边)。
+ - **状态(第 2 轮)**:**被否定。** 决定性的一条是预测 (b) 的反面:
  `l_mean`(分钟均价,跨日完全并列几乎不可能)与原式 rank 相关 **0.994**、Lnet +10.7%/+16.5%、
  **LTO 也是 4.1%** —— 一个完全没有并列的叶子给出同一本书、同一个换手。
  预测 (a) 字面上命中了(并列占比 **44.01%**,远超 >5% 的先验,且按十分位从 Q1 的 36% 单调升到 Q10 的 **51%**),
  但那量的是「窗口里**至少有一组**并列」,而泄漏场景要的是「整窗全并列 ⇒ 完美斜坡」,前者是后者很松的上界。
  剔除并列格子后 **Lgross 基本没变**(+14.31%/+19.07% vs 原式 +13.56%/+20.01%)—— **毛 alpha 不在并列格子里**;
  净值塌掉(−3.58%/+2.52%)只是因为换手从 4.08% 跳到 23.44%,而那是**子集每天 44% 成员进出**造成的,
  不是 `f` 的换手(`l_mean` 的 4.1% 是反证)。详见 `07x_1_identity.md` 第 4 节。
  ⇒ 进 `11_risks.md` 的不是「泄漏」,而是「高因子端系统性地偏向估值不动的股票」这条**机制自证**。
```

**10-04 15:10 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- - **状态**:未验证。**这是决定这条因子对用户有没有价值的那一条**。
  注:§6.5 的"折叠会骗过秩空间线性中性化"在这里**不适用** —— `abs_corr=False`,
  根节点没有取绝对值/平方这类折叠,所以线性中性化对它是公平的检验。
+ - **状态(第 2 轮)**:**被强烈支持,差最后一步。** 三块证据:
  1. **valid 上没有可测的增量**(主要证据)。三条家族单独在 valid 上几乎一样好
     (22.18 / 21.82 / 21.72),掺进 25% 的 `f` 之后是 21.35 / 21.66 / 22.12 ——
     散布 ±0.4pp,远在 ±3pp 的噪声里,而且**最强的那条(mean30)是变差的**(−0.83pp)。
     纯多头夏普同样:valid −0.03 / +0.04 / +0.09(噪声 ±0.3)。
  2. **train 上的「增量」有一个很说明问题的形状:家族自己越弱,增量越大。**
     amt_max9 train 单独最弱(10.56%)、增量最大(+2.08pp);stdamt_max9 居中(13.37%,+1.44pp);
     mean30 train 最强(13.26%)、增量为零(−0.05pp)。这是**拟合段吸收噪声**的特征,
     真增量应该与家族的强弱无关。
  3. **残差:它不是任何「单独一条」家族的改写,但整条躺在标准控制组的联合张成里。**
     对单独一条家族中性化(R² 只有 0.068~0.109)后还剩 +3.7%~+5.2%(tr)/+6.3%~+7.8%(va) 的净多头腿;
     但 S0 §7 对 **9 个 `ctl_*` 一起**中性化(R² 0.276)后多头腿**毛**超额从 +13.6% 掉到 **+0.1%**。
     **这两句必须一起说**,只说前一句会把结论反过来。
     (两种残差口径差 8~10pp 的裁决写在 `07x_1_identity.md` §3.1:口径差本身是 (c4) 那件事 ——
     **用户真正交易的 EMA20 信号比原始面板更「像」已知家族**。H4 的裁决不靠残差。)
  - **还差的最后一步(R2 做)**:(i) 组合用的是 `v_base`,而 S1 已证明它是这一族等价写法里最弱的
    (`l_last` valid 高 1.4pp);(ii) 组合书只回答「两个因子的秩加权相加」,**没有**回答用户真正的用法
    「我已经持有家族的多头端,`f` 能不能在这个池子里再挑一遍」—— 后者要用**双重排序**量。
  - 注:§6.5 的"折叠会骗过秩空间线性中性化"在这里**不适用** —— `abs_corr=False`,
    根节点没有取绝对值/平方这类折叠,所以线性中性化对它是公平的检验。
```

**10-04 15:10 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- - **杀死它的实验**:R1 `S1_whatis / s_pearson`。若 Pearson 版同样好或更好,H6 被否定,
  秩只是个无关紧要的实现选择(而且 Pearson 版便宜得多,直接成为提纯候选)。
- **状态**:未验证。
+ - **杀死它的实验**:R1 `S1_whatis / s_pearson`。若 Pearson 版同样好或更好,H6 被否定,
  秩只是个无关紧要的实现选择(而且 Pearson 版便宜得多,直接成为提纯候选)。
- **状态(第 2 轮)**:**被否定,而且是预测的反面。** 事前预测「rank 相关 0.5~0.85、多头腿更差」;
  实测 rank 相关 **0.978**、Lnet **+10.7%/+16.9%**、Lshp 1.87/3.05(原式 +10.4%/+17.0%、1.79/3.07)。
  固定半衰期表上 `s_pearson` 在中段还**更好**(train hl5 +10.7% vs +7.44%、Lshp 1.80 vs 1.26;
  hl10 +11.0% vs +10.23%),也就是说它的净超额曲线**更早走平、对半衰期更不敏感**。
  ⇒ 秩不是承重件;承重的是「逐股归一化」这一步(秩和标准化等效)。
  **`ts_pearson` 因此是提纯候选**:同一本书 + chunked matmul 实现(`ts_spearman` 还留着 `for i in range(N)`)。
```

**10-04 15:10 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- - **杀死它的实验**:R1 `S1_whatis / l_last`。明显更差 ⇒ 日内中位价的去噪确实有用,H7 被否定
  (那时要反过来问:更强的日内去噪〈`day_mean`〉是不是更好 —— 和 `l_mean` 一起看)。
- **状态**:未验证。
+ - **杀死它的实验**:R1 `S1_whatis / l_last`。明显更差 ⇒ 日内中位价的去噪确实有用,H7 被否定
  (那时要反过来问:更强的日内去噪〈`day_mean`〉是不是更好 —— 和 `l_mean` 一起看)。
- **状态(第 2 轮)**:**成立。** `l_last` rank 相关 0.961,Lnet +11.1%/+18.4%、Lshp 1.91/3.26。
  **在同一个半衰期下比**(H5 的硬约束):train hl5 +8.3% vs +7.44%、hl10 +10.3% vs +10.23%、
  hl20 +11.1% vs +10.45%;hl0/hl2 反过来略差 0.5~0.7pp。差异 0.07~0.86pp,**全在 ±3pp 噪声里**。
  ⇒ 正确的措辞是「**日内折叠是多余的**」(一个更简单、不需要分钟数据的等价写法),
  **不是**「`l_last` 更好」。`l_mean`(更强的日内去噪)+10.7%/+16.5% 也没有更好 ⇒ 日内去噪这一维是平的。
```

**10-04 15:11 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- - **状态**:未验证。(和 H4 相关但不同:H4 问"是不是已知暴露",H10 问"换个载体是不是更好"。)
+ - **状态(第 2 轮)**:**被否定。** `l_amt` Lnet **+2.1%/+7.9%**、Lshp 0.43/1.90、rank 相关 0.612。
  共动的载体是**价格路径**。
  **而且它顺手给 H4 提了一个反证**:`l_amt` 与三条 `known_*` 的 rank 相关(−0.238~−0.252)
  **反而比 `v_base` 的(−0.365~−0.423)更低**。如果原式与成交额家族的重叠来自
  「这个结构本质上在量活跃度」,那把叶子直接换成 `Amt` 应该重叠更高、表现更好 —— **两件都没发生**。
  ⇒ 与家族的重叠是**副产物**(两者都偏爱安静的股票),不是结构性的。
  (和 H4 相关但不同:H4 问"是不是已知暴露",H10 问"换个载体是不是更好"。)
```

**10-04 15:11 · agent 的话**

Now adding the new hypothesis H12 and the second-round decisions.

**10-04 15:11 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- ## 本轮明确决定**不**做的事(以及为什么)
+ ## D 组:第 2 轮新增

### H12 ——窗口 `d` 决定它在量哪一个**频段**的共动;这是唯一一根没动过的结构轴
**这是一条独立的新假设,不是 H5 的推论**(H5 管的是平滑长度 `hl`,和 `d` 是两根不同的轴;
第 1 轮已经把「H5 ⇒ 更长的 `d` 更好」这个错推论作废,**不要再引用它**)。

立论的依据只有身份本身:`f` 量的是「你的 `d` 天秩路径和全市场等权共识路径的吻合度」。
`d` 既是**测量窗口**也是**频段选择器**:`d=5` 量的是周内共动,`d=50` 量的是季度级的秩空间 beta。
身份已经定清(H1 确立),所以现在扫 `d` 是「扫一个有明确含义的参数」,不是盲扫。

- **预测**(三种结果都有信息量,事前写死):
  1. **`d` 变长 → 多头腿变好、且与已知家族的相关上升**:说明它越长越像一个慢速的
     「安静股票」特征 ⇒ **H4 被加强**(它正在往已知家族里滑),升华版即使成立也是家族的另一种写法。
  2. **`d` 变长 → 多头腿变差**:说明效应是真正短周期的条件共动 ⇒ **H4 被削弱**
… (8 行略) …

---

## 本轮明确决定**不**做的事(以及为什么)
```

**10-04 15:11 · Bash** — Check the end of the hypotheses file

```bash
cd /Users/wxy/Desktop/Partura && tail -20 notes/F111_spearman_qclose/05_hypotheses.md
```

```
## 本轮明确决定**不**做的事(以及为什么)

1. **不扫窗口 d**(5/20/30/50)。两个理由:
   (i) 扫法取决于 H1 —— H1 成立就该在便宜的 `ts_corr(A, cs_mean(A), d)` 形式上扫
   (`cross_*` 的窗口池到 60/241,`ts_*` 的到 50),而不是在 O(N²) 的 `ts_spearman` 上扫。
   **先定身份,再扫参数。**
   (ii) ⚠️ **第 1 轮重启时的修正**:上一版在这里写的是"它是最有希望的升华杠杆(H5)"。
   **这个理由已经没有了** —— H5 确立之后恰好**否掉**了它(毛超额在 hl>3 之后是下降的,
   半衰期轴是被耗尽而不是没用够;而且衰减表讲的是标签期限、不是平滑长度,
   不能当"更长的窗口会更好"的证据,详见 H5 一节末尾)。
   「更长的窗口 d」现在只是一个**未经检验的独立猜想**,优先级低于 H11 带出来的"升华方向 F"
   (把低波/市场跟随度这个暴露直接写干净);要做也得先立新假设,**不要引用 H5 当理由**。
2. **不做 `abs_corr=True` / `agg="std"` 变体**。按 H1 的恒等式,`abs_corr` 会破坏掉
   "线性投影"这个性质(取绝对值是折叠),它是一条**不同**的因子,不是这条的提纯;
   而且一旦引入折叠,§6.5 的"秩空间线性中性化看不见非单调关系"就开始适用,
   H4 的检验也要跟着换口径。留到身份定了之后再考虑。
3. **不验证 `day_quantile(Close, 0.5)` 与 `day_median(Close)` 是否逐位相同**(R0 异常第 4 条)。
   `l_mean` / `l_last` 已经覆盖了"叶子换一个统计量会怎样"这个有信息量的版本;
   逐位相同与否对任何结论都不构成影响。
4. **不碰封板票对空头腿的污染(H8a)**。多头腿不受它影响,对选拔结论无关;放到 R2 或报告阶段。
```

**10-04 15:11 · 改文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`

```
- 4. **不碰封板票对空头腿的污染(H8a)**。多头腿不受它影响,对选拔结论无关;放到 R2 或报告阶段。
+ 4. **不碰封板票对空头腿的污染(H8a)**。多头腿不受它影响,对选拔结论无关;放到 R2 或报告阶段。

---

## 第 2 轮明确决定**不**做的事(以及为什么)

1. **第 1 轮那条「不扫窗口 d」已经作废** —— 身份已经定清(H1 确立),`d` 现在是一个有明确含义的
   频段选择器,而且是**唯一**一根没动过的结构轴。R2 按 **H12** 扫它。
   第 1 轮写的「在便宜的 `ts_corr(A, cs_mean(A), d)` 上扫」这条路**已经被堵死**:
   `m_mktcorr` 换掉了承重件(rank 相关 0.742、valid 多头腿 +4.9%),扫它扫的是另一条因子。
   ⇒ 只能在 `ts_spearman` / `ts_pearson` 上扫(窗口池 `[1,5,10,20,30,40,50]`)。
2. **不把 `c(t)·ρ^time` 做成表达式候选** —— 这是本轮最诱人、也最该说清为什么不做的一条。
   它**是写得出来的**:`cs_mean(ρ) ∝ ‖M‖·c(t)`(`‖M‖>0`,正的当天标量不改变截面序),
   所以 `mul(cs_mean(ρ), ρ)` 与 `c(t)·ρ^time` **截面序等价**,而且是 O(N)、没有 Python 循环。
… (10 行略) …
   并让 §6.5 开始适用,H4 的检验口径得跟着换)。
4. **不追那 1.3% 窗口不完整的格子**(源码分母口径不一致、相关系数可超出 [−1,1])。
   它既不改变身份(窗口完整的 98.7% 上恒等式精确成立),也不改变选拔结论
   (`proj` 修掉这个瑕疵后只好 0.5pp,在噪声内)。进 `11_risks.md` 一句话。
```

**10-04 15:12 · agent 的话**

Now the R2 order — the most important artifact of this round.

**10-04 15:14 · 写文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/orders/R2.md`(9916 字符)

**10-04 15:14 · agent 的话**

Now the full rewrite of state.md — the main handoff artifact.

**10-04 15:18 · 写文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/state.md`(21014 字符)

10-04 15:18 · 读 `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/state.md`

**10-04 15:21 · 写文件** `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/state.md`(21015 字符)

**10-04 15:21 · agent 的话**

Let me add the grammar-level correction to `04_grammar.md`, since the next lead is told to read it first.

**10-04 15:21 · Bash** — Read tail of grammar file

```bash
cd /Users/wxy/Desktop/Partura && tail -25 notes/F111_spearman_qclose/04_grammar.md
```

```
只掉 0.5pp,而换手掉掉了 86%(29.9% → 4.1%)。
⇒ **被平滑掉的高频部分几乎不含 alpha;活下来的是跨市场方向不变的那一部分。**
那一部分按上面的式子就是「路径吻合度」= 路径干净、跟得上市场 ⇒ **特质波动低**。
这正是 `05_hypotheses.md` **H11** 的内容,也是基线里
`known_stdamt_mean30` −0.42 / `ctl_dvol20` −0.31 / `ctl_amt` −0.35 这组相关的来源
—— 而动量本身几乎正交(−0.08)。

**措辞规矩**:报告里写这棵树时,"条件动量"可以作为**原始面板瞬时含义**的描述,
但必须紧跟一句"因子值本身不随大盘方向变号";而**被交易的对象**(hl=20 的平滑信号)要按 H11 的
结论来描述,不能直接叫"条件动量"。两者是不同的东西,R1 block (b) 的三个分组相关决定措辞的强弱。

---

## 这套语法立刻带出的三件事(都要实验来定,见 `05_hypotheses.md`)

1. **O(N²) 的两两配对是多余的**(如果恒等式在真实数据上站得住)。它可以被
   "和一条市场路径做相关"替掉 —— 这是这棵树上最干净的**提纯**方向,而且算得快得多。
2. **并列值会造人工趋势**。`argsort(..., stable=True)` 对**相等**的值按**窗口内位置(日期)顺序**发秩。
   所以一只 10 天里日内中位价**完全不变**的股票,秩路径正好是 `0,1,…,9`,即一条**完美上升斜坡**,
   在涨市里拿到**接近最高**的因子值。`day_quantile(Close)` 落在 tick 网格上(低价股尤其容易重复),
   这个"假趋势"不是空想。换成几乎不可能并列的 `day_mean(Close)` 就能检验它有多重要。
3. **窗口不完整时恒等式失效,而且失效的方式是个瑕疵**。源码里
   `cov = sum_prod / num_valid`(用两只股票**重叠**的有效天数),而 `rank_std` 是各自在
   **自己**的有效天数上算的。两只股票缺失模式不同时分母口径不一致,"相关系数"可以超出 [-1,1]。
   停牌/新股多的格子(`cov=0.99`,约 1% 的格子)值会被扭曲。这是实现层面的瑕疵,记录在案。
```

**10-04 15:22 · Bash** — Append grammar correction section

```bash
cd /Users/wxy/Desktop/Partura && cat >> notes/F111_spearman_qclose/04_grammar.md <<'EOF'

---

## 第 5 步(**第 2 轮主研按 R1 的实测修正**)—— 承重件是「等权」,不是「秩」

上面第 1~4 步全部是源码/代数推导。R1 回来之后,**恒等式本身被完全证实**
(窗口完整的 98.70% 格子上,numpy 复算的 `proj` 与原式面板的逐日 Spearman mean/median/p95
全是 **1.0000**、p05 0.9999),但**第 1 步末尾那句「提纯方向立刻确定」是错的**,必须改写。

把三个变体的做法并排写出来,承重件就露出来了:

```
v_base    :  mean_j spearman(x_i, x_j)  =  < x̂_i^rank ,  mean_j x̂_j^rank >      ← 先逐股归一,再平均
s_pearson :  mean_j pearson (x_i, x_j)  =  < x̂_i      ,  mean_j x̂_j      >      ← 先逐股归一,再平均
m_mktcorr :      pearson (x_i, mean_j x_j)  =  < x̂_i ,  normalize(mean_j x_j) > ← 先平均,再归一
```

实测(S1,多头口径):

| | 与 `v_base` 的 rank 相关 | Lnet tr/va | Lshp tr/va |
|---|---|---|---|
| `s_pearson`(先逐股归一再平均) | **0.978** | +10.7% / +16.9% | 1.87 / 3.05 |
| `m_mktcorr`(先平均再归一) | **0.742** | +8.7% / **+4.9%** | 1.42 / **0.74** |

⇒ **`M` 之所以是「市场共识路径」,靠的是「先把每只股票的窗口路径各自归一化、再对股票取平均」
这一步 —— 它让每只股票在共识路径里等权。** 秩只是实现这一步的一种手段,标准化是另一种,两者等效;
而 `cs_mean` 平均的是**价格水平**,高价股主导,**它根本不是 `M`**。

**语法上的归纳(这棵树真正的结构)**:

```
事件  :  每只股票 d 天窗口内的「形状」                 ← 水平被归一化掉了,只剩路径形状
共识  :  对股票轴取等权平均 ⇒ 当天唯一的一条共识路径 M   ← 承重件就在这里
门控  :  自己的形状与 M 的吻合度(内积 = 相关 = beta)   ← 恒为正系数,因子值不随大盘翻面
放大  :  EMA(hl=20)                                   ← 只省成本,不改信号(H5)
```

**三条后果,直接影响后面怎么做**:
1. **提纯的便宜路线堵死了**:`ts_corr(A, cs_mean(A), d)` 换掉了承重件,不能用,
   也不能拿它去扫窗口 `d`(扫的是另一条因子)。能用的只有 `ts_spearman` / `ts_pearson`;
   其中 `ts_pearson` 是 chunked matmul,**同一本书的便宜实现**。
2. **第 2 步里「`j≠i` 的自排除只是常数、`‖rc_i‖` 对每只股票相同」这两条是 `ts_spearman` 独有的**
   (秩让模长严格相等)。`ts_pearson` 的模长不严格相等,所以它只是"近似同一个量",
   实测 0.978 —— 够用,但不要写成恒等。
3. **第 4 步(H11)里「⇒ 特质波动低」那一步被 R1 否定了**:`ctl_ivol` 的 rank 相关只有 **−0.153**,
   而 `ctl_amt` −0.352、`ctl_dvol20` −0.306、`known_stdamt_mean30` −0.423。
   正确的读法是「**低成交额 / 低成交额离散度**(安静、小、便宜的股票)」,**不是低特质波动**。
   机制一样顺:安静的股票没有自己的消息,`d` 天路径就是共识路径的一份干净拷贝 ⇒ 高 `f`。
   详见 `05_hypotheses.md` 的 H11(已改写)与 `07x_1_identity.md` §2。
EOF
echo "ok"; wc -l notes/F111_spearman_qclose/04_grammar.md
```

```
ok
     194 notes/F111_spearman_qclose/04_grammar.md
```

**10-04 15:22 · agent 的话**

Now the journal entry.

**10-04 15:23 · Bash** — Write the lead's round-2 journal entry

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F111_spearman_qclose "[主研] 第 2 轮:R1 全部裁决——恒等式精确成立,但承重件是「每只股票等权」而不是「秩」,便宜写法堵死;H4 被强烈支持;下 R2 扫窗口 d + 双重排序" <<'EOF'
看到了什么(读 results/R1.md 两次运行的全部数字):

1. **H1 确立,而且是恒等不是近似**:窗口完整的格子(占 98.70%)上 numpy 复算的 proj 与原式面板的
   逐日 Spearman mean/median/p95 全是 1.0000、p05 0.9999;proj 自己当因子 Lnet +10.95%/+17.09%
   (原式 +10.4%/+17.0%),好的那 0.5pp 来自它少了源码分母口径不一致那个瑕疵(只影响 1.3% 的格子)。

2. **本轮最重要的发现,不在任何原假设里:承重件是「每只股票等权」,不是「秩」。**
   S1 里最有信息量的一对比较不是我事前标的主判别项,而是 m_mktcorr 和 s_pearson 这一对:
   - s_pearson(ts_pearson,保留"先逐股归一再平均",只把秩换成标准化):rank 相关 0.978,
     Lnet +10.7%/+16.9%,**完全没塌**;固定半衰期表上中段还更好(hl5 +10.7% vs 原式 +7.44%)。
   - m_mktcorr(ts_corr(A, cs_mean(A),10),改成"先平均再归一"):rank 相关只有 0.742,
     valid 多头腿从 +17.0% 塌到 **+4.9%**、夏普 3.07 → **0.74**。
   cs_mean 平均的是**价格水平**(高价股主导),给不出那条等权共识路径 M。
   ⇒ **H6 被否定**(秩不承重),而且**提纯的便宜路线被堵死** —— ts_corr(A, cs_mean(A), d) 不能用,
   也不能拿它去扫窗口 d。能用的只有 ts_pearson(chunked matmul,同一本书的便宜实现)。
   这条已经写进 04_grammar.md 新加的第 5 步(第 1 步末尾那句"提纯方向立刻确定"是错的,已改写)。
   顺便:第 1 轮 H1 的预测 (c) 写的是"先验 0.6~0.9、不是 1.0,因为 cs_mean 是价格水平的截面均值"
   —— 实测 0.742,预言连机制一起命中,这是事前写下判据的好处。

3. **alpha 在条件化里,不在动量里(三条独立证据,已确立)**:
   ρ^time 单独当因子 Lnet −5.60%/−0.71%(sign 还被选成 −1);只多乘一个当天的全市场标量 c(t),
   c·ρ^time 就变成 +9.23%/+18.62%(毛 +14.47%/+23.75%,两段都高于原式的毛)。
   外加 t_tsrank(另一种纯动量写法)在全部 7 个半衰期上多头腿都是负的、对 ctl_mom20 的 R² 0.420
   (v_base 只有 0.056)、剖面在 Q4~Q7 出峰非单调。
   备忘反例:不要用"和 ctl_mom20 无条件相关只有 −0.08"去说"它和动量无关" —— 条件化本来就会抵消。

4. **裁决了执行明确要求主研定性的两个数**:
   (i) block (b) 的 0.4712/0.5991 —— 事前两条判据("都>0.8 很紧"/"都<0.5 很松")都没干净触发。
       裁决:线性斜坡「只描述了一半、但钱全在这一半」。依据:f vs c·ρ^time 只有 0.5381
       (按 playbook §6.3 <0.8 就是另一条因子),但 c·ρ^time 的书已经和原式一样好 ⇒ M 里那一半
       非线性形状对多头腿没有可测量贡献。
   (ii) block (c) 两种残差口径差 8~10pp —— 裁决:差值本身就是 (c4) 那件事,
       **用户真正交易的 EMA20 信号比原始面板更"像"已知家族**(R² 0.068~0.109 → 0.144~0.227,
       |corr| 0.23 → 0.37)。记录在案用口径①;**并把 H4 的裁决从残差移到组合书/双重排序上**
       —— 用户的问题是"我已经在跑家族了,加上它能不能多拿到",残差回答不了这个问题。

5. **H3/H10 被否定,H7 成立,H11 改写**:
   - H3:l_mean(完全没有并列的叶子)rank 相关 0.994、LTO 也是 4.1%;剔除并列格子后 Lgross 基本
     没变(+14.31%/+19.07%)⇒ 毛 alpha 不在并列格子里。净值塌掉只是换手 4%→23%,而那是
… (44 行略) …
- 不扫 cross_* 形式的窗口(ts_corr(A, cs_mean(A), d) 已被证明换掉了承重件)。
- 不做 abs_corr / agg="std";不追那 1.3% 窗口不完整的格子;不对齐三套 R²;不自己写 probes.py。
- 不为了有个升华版去凑 —— 最可能的结论就是否定的,而那是合格的。

落盘:新写 07_S1_whatis.md、07x_1_identity.md、orders/R2.md;04_grammar.md 追加第 5 步(改写了第 1 步
末尾那句错的推论和第 4 步的"特质波动"标签);05_hypotheses.md 加了第 2 轮裁决总表 + 逐条裁决 + 新假设 H12
+ "第 2 轮明确决定不做的事";state.md 8 节覆盖重写。
服务器运行:本轮 0 次(已用 2 次 = R1;R2 要用 2 次,做完还剩 4 次含 final)。留出段未读。
EOF
echo "--- note written ---"
```

```
已记入 notes/F111_spearman_qclose/journal.md(10 条)
--- note written ---
```

**10-04 15:23 · agent 的话**

Let me verify the files are coherent and nothing stale remains.

**10-04 15:23 · Bash** — Verify statuses, files, and that holdout is unread

```bash
cd /Users/wxy/Desktop/Partura && echo "=== remaining 未验证 in 05 ===" && grep -n "状态" notes/F111_spearman_qclose/05_hypotheses.md && echo && echo "=== files ===" && ls -la notes/F111_spearman_qclose/ && echo && echo "=== holdout check ===" && ./scripts/study.sh list F111_spearman_qclose 2>&1 | tail -15
```

```
=== remaining 未验证 in 05 ===
3:写法:每条写**它预测什么**、**哪个实验能杀死它**。状态列每轮更新。
49:- **状态(第 2 轮)**:**已确立,而且是恒等而非近似。** 窗口完整的格子(占有标签格子的 **98.70%**)上
69:- **状态(第 2 轮)**:**被支持,但只描述了一半 —— 而钱全在这一半。**
125:- **状态(第 2 轮)——一半成立、一半被否定,措辞已改写**:
160:- **状态(第 2 轮)**:**被否定。** 决定性的一条是预测 (b) 的反面:
181:- **状态(第 2 轮)**:**被强烈支持,差最后一步。** 三块证据:
207:- **状态(第 2 轮)**:**被否定。** `l_amt` Lnet **+2.1%/+7.9%**、Lshp 0.43/1.90、rank 相关 0.612。
220:**【第 1 轮(重启)主研已自己把这条做完,不需要实验了。状态:已确立。】**
273:- **状态(第 2 轮)**:**被否定,而且是预测的反面。** 事前预测「rank 相关 0.5~0.85、多头腿更差」;
287:- **状态(第 2 轮)**:**成立。** `l_last` rank 相关 0.961,Lnet +11.1%/+18.4%、Lshp 1.91/3.26。
306:- **状态**:未验证。**不影响选拔结论**(多头腿不受影响),只影响报告里"为什么钱在空头腿"这一段,
315:- **状态**:**已被 S0 支持**(条件 IC 表),只差"是否同样出现在 valid 段"这一步确认。
340:- **状态**:**未验证**。注意 `ts_spearman` / `ts_pearson` 的窗口池是 `[1,5,10,20,30,40,50]`,

=== files ===
total 352
drwxr-xr-x@ 14 wxy  staff    448 Oct  4 15:21 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   3302 Oct  4 13:01 01_expression.md
-rw-r--r--@  1 wxy  staff   9303 Oct  4 13:02 02_operators.md
-rw-r--r--@  1 wxy  staff   4429 Oct  4 13:02 03_decomposition.md
-rw-r--r--@  1 wxy  staff  12059 Oct  4 15:22 04_grammar.md
-rw-r--r--@  1 wxy  staff  33900 Oct  4 15:11 05_hypotheses.md
-rw-r--r--@  1 wxy  staff  13257 Oct  4 13:07 06_baseline.md
-rw-r--r--@  1 wxy  staff   8047 Oct  4 15:05 07_S1_whatis.md
-rw-r--r--@  1 wxy  staff  14985 Oct  4 15:08 07x_1_identity.md
-rw-r--r--@  1 wxy  staff  26441 Oct  4 15:23 journal.md
drwxr-xr-x@  4 wxy  staff    128 Oct  4 15:14 orders
drwxr-xr-x@  4 wxy  staff    128 Oct  4 14:34 results
-rw-r--r--@  1 wxy  staff  33957 Oct  4 15:21 state.md

=== holdout check ===
# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):
  S0_baseline            [partura exit 0 2026-10-05_02:54:02]  [有 JSON]
  S1_whatis              [partura exit 0 2026-10-05_05:05:25]  [有 JSON]
  x1_identity            [partura exit 0 2026-10-05_05:23:46]
# 正在跑的:
  (无)
# 已把服务器上的 runs/F111_spearman_qclose/*.json 拉回本地
```

**10-04 15:23 · Bash** — Regenerate brief and sanity-check the R2 order

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F111_spearman_qclose 2>&1 | sed -n '1,30p' && echo "=== R2 order sanity ===" && grep -c "" notes/F111_spearman_qclose/orders/R2.md && grep -n "BESTW\|双重排序\|正好 2 次\|8 个变体" notes/F111_spearman_qclose/orders/R2.md | head
```

```
# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-04 15:23(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F111_spearman_qclose#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `work:F111_spearman_qclose#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:09 → `handoff/F111_spearman_qclose/agents/work_R0_a067aac26fed39d46.md`
- agent `lead:F111_spearman_qclose#1`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:26 → `handoff/F111_spearman_qclose/agents/lead_R1_ab403fe60ef06a414.md`
- agent `work:F111_spearman_qclose#1`(wf_c8c98127-70d):失败,最后动作 10-04 13:29 → `handoff/F111_spearman_qclose/agents/work_R1_aba23855eadec7a06.md`
- agent `work:F111_spearman_qclose#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)
- agent `lead:F111_spearman_qclose#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 13:55 → `handoff/F111_spearman_qclose/agents/lead_R1_a36c37b71e6d128ea.md`
- agent `work:F111_spearman_qclose#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 14:36 → `handoff/F111_spearman_qclose/agents/work_R1_a4f4276b792511fca.md`
- agent `lead:F111_spearman_qclose#2`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F111_spearman_qclose` 看服务器上的 tag,`./scripts/study.sh digest F111_spearman_qclose <tag>` 重看结果)。

## 研究现状(`notes/F111_spearman_qclose/state.md`,10-04 15:21 更新)—— **先读这个文件**

# F111_spearman_qclose 研究现状

> 本文件每轮由**主研覆盖重写**。最后更新:**第 2 轮(主研,Opus 5)**,2026-10-04。
> 表达式:`ts_spearman(day_quantile(Close), 10)`,来源 挖掘库 / #953。

---
=== R2 order sanity ===
243
39:  **「我已经持有家族的多头端了,它能不能在这个池子里再帮我挑一遍」** —— 这个要用**双重排序**量。
41:看到 **双重排序的多头腿净超额在 train 和 valid 都 ≥ +3pp** ⇒ 有真增量,H4 被否定,升华方向定为
52:### 第 1 项(服务器运行 1/2):阶段 `S2_window`,8 个变体
106:> `BESTW` = 在 `{w_last_5, w_last_20, w_last_30, w_last_50, w_q_30, p_last_30}` 这 6 个里,
108:> 把 `BESTW` 是谁、它的完整表达式、它的 train/valid 数字写进结果卡。
114:F2 = BESTW 的完整表达式                       # 由上面的规则定
143:#### block B ——双重排序(这一轮最重要的一块,R1 没做过)
187:- (d3) `BESTW` 与 `v_base`、`F1`、以及 3 条 `known_*` 的 rank 相关(交易信号口径,train)。
211:| 8 | — | — | — | `BESTW` 是谁、完整表达式、按什么规则选出来的 |
222:| 14 | D | (d1) 10×5 表;(d2) 10×2 表;(d3) `BESTW` 的 6 个 rank 相关 |
```

**10-04 15:24 · agent 的话**

All files are in place, the brief picks up the new state, and the holdout remains unread (server has only `S0_baseline`, `S1_whatis`, `x1_identity`).

**What I did this round (lead, R1 adjudication → R2 order):**

Files written, all under `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/`:
- `07_S1_whatis.md`, `07x_1_identity.md` — new, the interpretation of R1's two runs
- `05_hypotheses.md` — verdict table + per-hypothesis rulings + new H12 + round-2 "decided not to do"
- `04_grammar.md` — appended step 5, which corrects two things step 1 and step 4 got wrong
- `orders/R2.md` — new order (243 lines)
- `state.md` — full 8-section overwrite
- `journal.md` — round-2 lead entry

**The three judgments that mattered:**

1. **The load-bearing element is "每只股票等权", not "秩"** — a finding outside every pre-registered hypothesis. `s_pearson` (ts_pearson, keeps per-stock normalisation before averaging) holds at rank corr 0.978 / Lnet +10.7%/+16.9%; `m_mktcorr` (`ts_corr(A, cs_mean(A),10)`, averages price *levels* first) collapses to rank corr 0.742 / valid Lnet **+4.9%**, Lshp **0.74**. Consequence: **the cheap purification route is dead** — `ts_corr(A, cs_mean(A), d)` cannot be used, and cannot be used to scan `d` either.

2. **The alpha is in the interaction with market direction, not in own momentum** (three independent pieces): `ρ^time` alone is −5.60%/−0.71%; multiplying by the one daily market-wide scalar `c(t)` gives +9.23%/+18.62%; and `t_tsrank` is negative at all seven half-lives with R²=0.420 against `ctl_mom20` (v_base: 0.056).

3. I ruled on the two numbers the executor explicitly escalated: block (b)'s 0.4712/−0.5991 (neither pre-registered criterion fired) → "the linear ramp describes only half, but all the money is in that half"; and block (c)'s two residual calibers differing by 8–10pp → the gap *is* the (c4) effect, and **H4's verdict therefore moves off residuals onto the combination book / double sort**.

I declined the most tempting lead with reasons on record: `c(t)·ρ^time` *is* writable as `mul(cs_mean(ρ), ρ)` (cross-sectionally order-equivalent, O(N)), but rank corr to the original is only 0.5381 (§6.3 ⇒ a different factor), and its +9.23%/+18.62% still loses to the known family's +21.8%~+22.3%, so it does not change the user's answer.

**10-04 15:24 · StructuredOutput**

```json
{
 "status": "order",
 "order": "R2",
 "kind": "experiment",
 "summary": "裁决完 R1:身份已确立且是恒等——原式精确等于「自己的 10 天秩路径 · 全市场等权共识秩路径」(窗口完整的 98.7% 格子上逐日 Spearman = 1.0000)。本轮最重要的发现不在任何原假设里:承重件是「每只股票等权」而不是「秩」(s_pearson 0.978 不塌 / m_mktcorr 0.742、valid 多头腿塌到 +4.9%),这同时堵死了提纯的便宜路线。H1 确立、H3/H6/H10 被否定、H7 成立、H2 被限定为「只描述了一半但钱全在这一半」、H11 的「反向特质波动」标签被 ctl_ivol −0.153 否定并改写成「低成交额/低成交额离散度」;另确立「alpha 在与市场方向的交互里、不在自己的动量里」(ρ^time 单独 −5.6% → c·ρ^time +9.2%/+18.6%)。H4(对纯多头用户没有增量)已被强烈支持:组合 w=0.25 在 valid 上只有 −0.83/−0.16/+0.40pp,而且「家族自己越弱增量越大」= 拟合段吸收噪声。决定下 R2(2 次运行):阶段 S2_window 8 个变体扫唯一没动过的结构轴 d(新假设 H12,明确禁止引用 H5 或衰减表当理由)+ 脚本 x2_increment.py 用更强的 l_last 重做组合并新增双重排序(掩码到家族多头端后,那本书的 Lnet 天然就是「相对持有整个池子」的增量,正好是用户的问题)。明确拒掉 c(t)·ρ^time 做候选(rank 相关仅 0.54 = 另一条因子,且仍输给已知家族)。最可能的结论是否定的,而那是合格结论。",
 "state_written": true
}
```

```
Structured output provided successfully
```

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/07_S1_whatis.md`
- `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/07x_1_identity.md`
- `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/05_hypotheses.md`
- `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/orders/R2.md`
- `/Users/wxy/Desktop/Partura/notes/F111_spearman_qclose/state.md`

## 它返回给工作流的结果

```json
{
 "status": "order",
 "order": "R2",
 "kind": "experiment",
 "summary": "裁决完 R1:身份已确立且是恒等——原式精确等于「自己的 10 天秩路径 · 全市场等权共识秩路径」(窗口完整的 98.7% 格子上逐日 Spearman = 1.0000)。本轮最重要的发现不在任何原假设里:承重件是「每只股票等权」而不是「秩」(s_pearson 0.978 不塌 / m_mktcorr 0.742、valid 多头腿塌到 +4.9%),这同时堵死了提纯的便宜路线。H1 确立、H3/H6/H10 被否定、H7 成立、H2 被限定为「只描述了一半但钱全在这一半」、H11 的「反向特质波动」标签被 ctl_ivol −0.153 否定并改写成「低成交额/低成交额离散度」;另确立「alpha 在与市场方向的交互里、不在自己的动量里」(ρ^time 单独 −5.6% → c·ρ^time +9.2%/+18.6%)。H4(对纯多头用户没有增量)已被强烈支持:组合 w=0.25 在 valid 上只有 −0.83/−0.16/+0.40pp,而且「家族自己越弱增量越大」= 拟合段吸收噪声。决定下 R2(2 次运行):阶段 S2_window 8 个变体扫唯一没动过的结构轴 d(新假设 H12,明确禁止引用 H5 或衰减表当理由)+ 脚本 x2_increment.py 用更强的 l_last 重做组合并新增双重排序(掩码到家族多头端后,那本书的 Lnet 天然就是「相对持有整个池子」的增量,正好是用户的问题)。明确拒掉 c(t)·ρ^time 做候选(rank 相关仅 0.54 = 另一条因子,且仍输给已知家族)。最可能的结论是否定的,而那是合格结论。",
 "state_written": true
}
```

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  很多停止的、error的，可以继续跑了，我重置了额度

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**主研**,负责因子 F111_spearman_qclose 的研究思路:理解表达式、提出并裁决假设、设计判别性实验、决定提纯与升华的候选、下结论(分辨 / 提纯 / 升华)。
  你**不写实现代码、不跑实验**:那是「执行」的事,它照你的工单去做,把结果写成结果卡交回来。
  这一轮结束后,下一轮的主研是一个新的 agent,只看得到文件。
  
  ## 你在整件事里的位置(先读这一段)
  
  用户的总任务:对一批 AlphaCube 因子逐条做 Partura 研究(分辨、提纯、升华);并要求研究全程落盘、随时能换模型接手。
  分工是 —— 总领(Opus 5.5)搭框架与协调;主研(Opus 5)负责单条因子的研究思路;执行(Sonnet 5)负责写代码、跑实验、读结果。
  
  工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」)。那句话是说给总领听的 —— 可能是催进度、问状态、
  要求把东西记下来、或者安排分工 —— **总领已经处理过了,下面这份任务就是总领对它的落实**。所以它和下面的任务**不冲突**:
  你把这份任务完整做完(并按要求把过程写进文件),就是在执行用户的请求。**不要因为那句话而跳过、缩减任务,或改做别的事。**
  如果它提到「写 state.md」「记录下来」,落到你身上就是:主研照常在本轮结束前重写 state.md;执行照常写结果卡和日志 —— 仅此而已。
  记录框架、状态板、模型分工都已经由总领搭好并在运行,不需要你去搭、去改、去切换任何东西
  (scripts/、partura/、workflows/、handoff/、lab/、docs/ 一律不要动;别的因子的文件也不要动)。
  **你就是这个分工里的「主研」。**
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  先读 docs/study_playbook.md —— 操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西、§6 审查反复抓到的错误、
  §7 研究日志与交接。下面不重复手册里的内容。
  不要使用 Agent / Workflow 工具去派生别的 agent。所有写给人看的文字用中文,英文术语保留。
  
  **这项研究是接力做的**:「主研」定思路、下工单;「执行」写代码、跑实验、读结果。两者是不同的模型,而且每一轮都是
  一个全新的 agent —— 彼此之间**只靠文件**传递信息,你的对话和推理不会被任何人看到。
  你知道的、想到的、决定的,**不写进文件就等于没有**。
  
  ## 因子
  
  - factor_id: F111_spearman_qclose
  - 来源: 挖掘库 / #953
  - 表达式:
  ts_spearman(day_quantile(Close), 10)
  
  ## 选拔口径(用户定的,不要改)
  
  用户做的是 A 股纯多头,空头腿做不了。**选拔只看多头腿扣费之后能拿到多少**:第一判据是多头腿净超额与纯多头夏普,
  半衰期按纯多头书在 fit 段选(rank_by: long;摘要里的 hlL / Lnet / Lshp 就是这个口径)。
  - **延长半衰期带来的多头腿净超额是真的、可以交易到的改进,不是需要控制掉的伪影。**
    「原式 + 多头最优半衰期」是所有结构候选要比过的第一条基准;改进全部来自更长的半衰期也可以推荐,
    但归因要写对(写「来自平滑」;想说结构更好,就在同一个半衰期下比 —— 摘要里有固定半衰期表)。
  - 多空夏普是次要信息(用户最早那张表的口径),每个变体都同时算了(hlS / LS)。
  - 第二条基准是已知家族:cross_mean(day_std(Amt), 30) 与 cross_max(day_std(Amt), 9)(测试段多头腿净超额 +13%~+15%、
    纯多头夏普 1.4~1.9)。候选滑进这个家族没问题,但要说清楚它是什么,以及「对只能做多的用户,这条因子相对已知家族
    有没有增量」(残差的多头腿、或与已知家族相加之后的多头腿)。
  - 结论可以是否定的:「多头腿不可用」「它就是已知家族,没有增量」都是合格的结论,只要证据在。
  
  ## 这条因子的共享记忆(都在 /Users/wxy/Desktop/Partura 下)—— 接力靠的就是它们
  
    notes/F111_spearman_qclose/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
    notes/F111_spearman_qclose/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F111_spearman_qclose/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F111_spearman_qclose/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F111_spearman_qclose/NN_*.md          进报告的手写段落(playbook §5)
    configs/F111_spearman_qclose.yaml、studies/F111_spearman_qclose/、runs/F111_spearman_qclose/*.json、logs/F111_spearman_qclose_*.log
    handoff/F111_spearman_qclose/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F111_spearman_qclose
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F111_spearman_qclose "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 这一轮(第 2 轮,最多 10 轮,含读留出段和成文)
  
  1. **先看全貌**:./scripts/study.sh brief F111_spearman_qclose。然后读 notes/F111_spearman_qclose/state.md、journal.md 最近的条目、
     最新的结果卡 notes/F111_spearman_qclose/results/R<n>.md;需要核对原始数字时 ./scripts/study.sh digest F111_spearman_qclose <tag>。
     还没有 state.md、或假设表还没写(你是第一个主研)时:另读 docs/method.md(为什么每条表达式都要重新推计划),
     并读执行建的档:01_expression.md、02_operators.md、03_decomposition.md、06_baseline.md、results/R0.md。
     对关键算子的语义有疑问,自己 ./scripts/study.sh src <算子> 核对 —— 语义读错,后面全错。
     之前的研究员(可能是别的模型)留下的 notes、脚本、运行结果都是有效的工作成果:读懂、核对、接着做。
  2. **如果最新的工单还没有对应的结果卡**(上一轮的执行被打断了):不要另开工单,直接返回
     {status:'order', order:'R<n>', kind:<那张工单的 kind>},让执行接着做。
  3. **裁决**。(你是第一个主研、还没有假设表时:先把你对这棵树的理解写成 04_grammar.md(结构语法:事件 → 记忆 → 门控 → 放大…)
     和 05_hypotheses.md(竞争性假设表:每条写「它预测什么」「哪个实验能杀死它」),**先写假设,再下第一张工单**。
     想要候选实验的草稿,可以在工单里让执行跑 ./scripts/study.sh propose F111_spearman_qclose 并把输出贴进结果卡 —— 那只是草稿。)
     最新的结果说明了什么?哪条假设被支持、被杀死、要改写?有没有意外?把解读落到 notes 里:
     05_hypotheses.md(每条假设的状态和证据)、07_<stage_id>.md 的「解读」、07x_<序号>_<name>.md(自写分析的解读)。
     每个结论都要能指到一个实验;分清「已确立 / 合理但未坐实 / 未决」。
  4. **决定下一步**:
     (a) 再做实验 → 写工单(kind: experiment)。一个阶段回答一个问题;每个变体的 why 写它想证伪什么;不要套别的因子的实验清单。
         至少要认真回答过:它是不是已知暴露(成交额水平/规模/换手率/波动/动量/反转)的另一种写法;钱为什么主要在空头腿;
         分位剖面是不是单调;哪些节点多余;「原式 + 多头最优半衰期」够不够;相对已知家族有没有增量。
     (b) 读留出段 —— 只凭 train/valid 选定 ≤ 5 个最终候选(**必须含原式;必须含一条已知家族基准**,除非有证据说明无关)。
         **先**把候选排序(第一推荐是谁)和判据(留出段出现什么结果算被否定)写进 notes/F111_spearman_qclose/10_distilled.md 的
         「读留出段之前」一节,**再**写工单(kind: final)。整个研究只许读一次:brief 里显示已读过,就绝不再下 final 工单。
     (c) 成文(留出段已读)—— 你写判断类的 notes:09_diagnosis.md(已确立 / 合理但未坐实 / 未决)、10_distilled.md 的
         「读完留出段之后」(每条判据过了还是被否定;推荐就是事前的第一推荐,被否定就写被否定)、11_risks.md、12_next.md、
         08_variants.md;然后写工单(kind: writeup)让执行补齐事实类段落、出报告、逐个核对数字。
     (d) 完成 —— 报告已出、执行核对过数字、没有遗留问题 → 返回 status:'done'。
     到第 7 轮还没读留出段,就必须进入 (b);最后一轮必须是 (d)。
  5. **落盘(每一轮都必须做,在返回之前)**:
     - 覆盖重写 notes/F111_spearman_qclose/state.md。state.md 的 8 节(每轮**整个文件覆盖重写**,宁可啰嗦):
   1. 一句话现状(做到哪一步、下一步是什么)
   2. 中间结果:已经量到的事实,每条带数字和出处(tag / 脚本 / 变体 / 哪一段 / 哪种口径)
   3. 研究过程与逻辑:做了什么、按什么顺序、为什么这么走;源码里和名字不一样的地方
   4. 假设表:编号 | 假设 | 状态(未验证 / 被支持 / 被否定 / 已改写)| 证据与出处 | 还差什么才能定
   5. 当前的候选(提纯 / 升华):表达式、train/valid 多头口径数字、为什么是它;已排除的候选与原因
   6. 后面的研究思路:按顺序,每步做什么、想回答什么、哪种结果意味着什么;明确决定**不**做的事和原因
   7. 留出段:未读 / 已读(读前的候选排序与判据写在 10_distilled.md 的哪一节)
   8. 给接手者的提醒:工具的坑、还没看结果的任务(tag)、写了一半的文件
     - ./scripts/study.sh note F111_spearman_qclose "[主研] 第 2 轮:<一句话>" <<'EOF'
       这一轮看到了什么、判断是什么、决定做什么、为什么(以及决定不做什么)
       EOF
  
  工单格式(notes/<fid>/orders/R<n>.md)—— 执行是另一个模型,只看得到这张纸,写到它不需要猜:
    # 工单 R<n>(kind: experiment | final | writeup | fix)
    ## 想回答的问题(对应哪条假设;看到哪种结果意味着什么)
    ## 要做的事(逐条。配置阶段:stage id、每个变体的 id + **完整表达式** + why;分析脚本:要量什么、怎么量、用哪些面板)
    ## 要带回来的数字(逐项:哪个变体、哪一段、哪种口径、哪个指标;需要的表:固定半衰期表 / 中性化 / 条件 IC / rank 相关 / 逐年)
    ## 约束(只用 train/valid;tag 名;变体数上限)
  一张工单最多 2 次服务器运行、合计不超过 12 个变体(含 nt_* 的不超过 6 个)。
  
  返回:status('order' 或 'done')、order(工单号,如 'R3';done 时填空串)、kind、summary(两三句:这一轮的判断和决定)、
  state_written(state.md 是否已更新)。
```
