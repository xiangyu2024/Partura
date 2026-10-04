# lead:F111_spearman_qclose#1 — agent a36c37b71e6d128ea(工作流 wf_48864a04-f0a)

- 状态:**还在跑**;开始 10-04 13:38,最后一次动作 10-04 13:42;工具调用 17 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F111_spearman_qclose/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 13:38 · agent 的话**

I'll start by getting the full picture of this factor's research state.

**10-04 13:38 · Bash** — Get factor research overview

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F111_spearman_qclose 2>&1 | head -200
```

```
# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-04 13:38(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F111_spearman_qclose`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F111_spearman_qclose#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F111_spearman_qclose#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `work:F111_spearman_qclose#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:09 → `handoff/F111_spearman_qclose/agents/work_R0_a067aac26fed39d46.md`
- agent `lead:F111_spearman_qclose#1`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:26 → `handoff/F111_spearman_qclose/agents/lead_R1_ab403fe60ef06a414.md`
- agent `work:F111_spearman_qclose#1`(wf_c8c98127-70d):失败,最后动作 10-04 13:29 → `handoff/F111_spearman_qclose/agents/work_R1_aba23855eadec7a06.md`
- agent `work:F111_spearman_qclose#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)
- agent `lead:F111_spearman_qclose#1`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F111_spearman_qclose` 看服务器上的 tag,`./scripts/study.sh digest F111_spearman_qclose <tag>` 重看结果)。

## 研究现状(`notes/F111_spearman_qclose/state.md`,10-04 13:25 更新)—— **先读这个文件**

# F111_spearman_qclose 研究现状

> 本文件每轮由**主研覆盖重写**。最后更新:**第 1 轮(主研,Opus 5)**,2026-10-04。
> 表达式:`ts_spearman(day_quantile(Close), 10)`,来源 挖掘库 / #953。

---

## 1. 一句话现状

建档(R0)已完成,我(第 1 轮主研)读了源码、推出了一个把根节点**精确解掉**的恒等式、写了
`04_grammar.md` 和 `05_hypotheses.md`(H1~H10),并下了第一张工单 **R1(kind: experiment)**;
**下一步是执行去跑 R1**(1 个配置阶段 `S1_whatis` 6 变体 + 1 个 exec 脚本 `x1_identity.py` 4 段),
回来之后第 2 轮主研裁决 H1/H2/H3/H4/H5/H6/H7/H10。

---

(…全文 12849 字符,读 `notes/F111_spearman_qclose/state.md`)

## 研究日志(`notes/F111_spearman_qclose/journal.md`:3 条,其中研究员自己写的 3 条)

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

## 工单与结果卡(`notes/F111_spearman_qclose/orders/`、`notes/F111_spearman_qclose/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F111_spearman_qclose.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F111_spearman_qclose`)

- `S0_baseline`  10-04 11:54  1 个变体  → `./scripts/study.sh digest F111_spearman_qclose S0_baseline`

## 已写的 notes(`notes/F111_spearman_qclose/`)

- `01_expression.md`  3302 字节  10-04 13:01
- `02_operators.md`  9303 字节  10-04 13:02
- `03_decomposition.md`  4429 字节  10-04 13:02
- `04_grammar.md`  6581 字节  10-04 13:17
- `05_hypotheses.md`  11252 字节  10-04 13:19
- `06_baseline.md`  13257 字节  10-04 13:07
- `journal.md`  8624 字节  10-04 13:26
- `state.md`  21129 字节  10-04 13:25

## 自写的探针与分析脚本(`studies/F111_spearman_qclose/`)

(无)

## 结构化结果(`handoff/F111_spearman_qclose/results/`)

(还没有)
```

**10-04 13:38 · Bash** — List factor notes directory

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F111_spearman_qclose/ 2>&1 && echo "--- orders ---" && ls -la notes/F111_spearman_qclose/orders/ 2>&1 && echo "--- results ---" && ls -la notes/F111_spearman_qclose/results/ 2>&1
```

```
total 192
drwxr-xr-x@ 12 wxy  staff    384 Oct  4 13:25 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   3302 Oct  4 13:01 01_expression.md
-rw-r--r--@  1 wxy  staff   9303 Oct  4 13:02 02_operators.md
-rw-r--r--@  1 wxy  staff   4429 Oct  4 13:02 03_decomposition.md
-rw-r--r--@  1 wxy  staff   6581 Oct  4 13:17 04_grammar.md
-rw-r--r--@  1 wxy  staff  11252 Oct  4 13:19 05_hypotheses.md
-rw-r--r--@  1 wxy  staff  13257 Oct  4 13:07 06_baseline.md
-rw-r--r--@  1 wxy  staff   8624 Oct  4 13:26 journal.md
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:23 orders
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:06 results
-rw-r--r--@  1 wxy  staff  21129 Oct  4 13:25 state.md
--- orders ---
total 40
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:23 .
drwxr-xr-x@ 12 wxy  staff    384 Oct  4 13:25 ..
-rw-r--r--@  1 wxy  staff  16907 Oct  4 13:22 R1.md
--- results ---
total 16
drwxr-xr-x@  3 wxy  staff    96 Oct  4 13:06 .
drwxr-xr-x@ 12 wxy  staff   384 Oct  4 13:25 ..
-rw-r--r--@  1 wxy  staff  6182 Oct  4 13:06 R0.md
```

**10-04 13:38 · agent 的话**

The latest order R1 has no result card and the executor failed twice. Let me verify the state and check whether any partial work landed on the server.

**10-04 13:38 · Bash** — Read order R1

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F111_spearman_qclose/orders/R1.md
```

```
# 工单 R1(kind: experiment)

主研(第 1 轮)下。读这张工单之前,建议先扫一眼 `notes/F111_spearman_qclose/04_grammar.md`
(我从源码推出来的恒等式)和 `05_hypotheses.md`(假设 H1~H10)—— 下面每一项都标了它对应哪条假设。
**这张工单共 2 次服务器运行**:1 次 `run`(阶段 `S1_whatis`)+ 1 次 `exec`(脚本 `x1_identity.py`)。
第 1 项不用服务器。

---

## 想回答的问题

**主问题:`ts_spearman` 那个 O(N²) 的「对全市场其他每只股票求 Spearman 相关再平均」,
到底等价于什么更简单的东西?**

我从源码推出:窗口完整时,原式的**截面排序**精确等于
`Σ_k rc_i[t,k] · M[t,k]` 的排序 —— 自己的 10 天「窗口内去均值秩路径」和**全市场平均秩路径**
的内积(推导见 `04_grammar.md`,关键一步是窗口完整时每只股票的 `rank_std` 都等于同一个常数
`sqrt((d²−1)/12)`,所以那个除法不区分股票)。再把市场路径近似成直线,就得到
**原式 ≈ (市场 10 日趋势方向) × (自己的 10 日秩动量)**,一个**条件动量**。

- **H1** 成立(恒等式在真实数据上站得住)⇒ 配对结构没有信息价值,提纯方向立刻确定。
- **H1** 被否定(rank 相关 < 0.9)⇒ 我的推导漏了东西,后面要重想,**请在结果卡里显著标出**。
- **H4**(对只能做多的用户,它是不是已知家族的另一种写法、有没有增量)是决定这条因子有没有
  价值的那一条:原式多头腿 Lnet +10.4%/+17.0%、Lshp 1.79/3.07,**已经低于**
  `known_stdamt_mean30`(+12.6%/+22.3%、1.78/3.46)和 `known_stdamt_max9`(+13.7%/+22.2%、1.99/3.59)。
  所以它唯一可能的价值在**增量**(残差 / 组合),这必须量出来。

---

## 要做的事
… (185 行略) …

---

## 约束

- **只用 train / valid。不要碰 holdout**:`st.slice("holdout")` 会直接报错,别去绕它;
  也不要跑 `study.sh final`。
- tag:阶段用 `S1_whatis`,脚本用 `x1_identity`。
- 变体数:6 个(上限 12),其中 `nt_*` 0 个(上限 6)。
- **服务器运行 2 次**:`run ... S1_whatis` 和 `exec ... x1_identity.py`。`wait` 的 Bash 超时设 600000。
  第 1 项和第 4 项不算服务器运行。两次运行**可以同时起**(阶段先起,脚本接着起,再分别 wait);
  若服务器只允许一个在跑,就串行。
- 只动 `configs/F111_spearman_qclose.yaml`、`studies/F111_spearman_qclose/`、
  `notes/F111_spearman_qclose/`。不动 `partura/`、`scripts/`、`handoff/`、别的因子的文件。
- 每看完一个结果先 `./scripts/study.sh note F111_spearman_qclose "[执行] R1:…"` 再做下一步。
- 结果卡写 `notes/F111_spearman_qclose/results/R1.md`:**只写事实和异常,不要替我下结论**
  (不要写"所以这条因子是/不是 XX")。表达式没解析、脚本某个 block 塌了、哪一项没跑完,
  都**照实写**并附错误原文 —— 这比补一个猜出来的数字有用得多。
- 我(主研)自己判断过的事,不用你再验证:`ts_spearman` 的语义、恒等式的推导、
  `cs_mean` 输出是 (D,N) 广播。你只要把数带回来。
```

**10-04 13:38 · Bash** — Check server tags and local run artifacts

```bash
cd /Users/wxy/Desktop/Partura && echo "=== list tags on server ===" && ./scripts/study.sh list F111_spearman_qclose 2>&1 | tail -40 && echo "=== runs dir ===" && ls -la runs/F111_spearman_qclose/ 2>&1 && echo "=== studies dir ===" && ls -laR studies/F111_spearman_qclose/ 2>&1 | head -30 && echo "=== logs ===" && ls -la logs/ 2>&1 | grep F111 | head -20
```

```
=== list tags on server ===
# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):
  S0_baseline            [partura exit 0 2026-10-05_02:54:02]  [有 JSON]
# 正在跑的:
  (无)
# 已把服务器上的 runs/F111_spearman_qclose/*.json 拉回本地
=== runs dir ===
total 96
drwxr-xr-x@  4 wxy  staff    128 Oct  4 11:54 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  3 17:37 ..
-rw-r--r--@  1 wxy  staff  41931 Oct  4 11:54 S0_baseline.json
-rw-r--r--@  1 wxy  staff   2370 Oct  4 11:54 ledger.json
=== studies dir ===
ls: studies/F111_spearman_qclose/: No such file or directory
=== logs ===
```

**10-04 13:39 · Bash** — Read config and journal tail

```bash
cd /Users/wxy/Desktop/Partura && echo "=== config ===" && cat configs/F111_spearman_qclose.yaml && echo "=== journal tail ===" && tail -5 notes/F111_spearman_qclose/journal.md
```

```
=== config ===
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
… (21 行略) …
diagnostics:
  decay:      [v_base]
  by_year:    [v_base]
  neutralise: [v_base]
  profile:    [v_base]
  conditional:
    - {factor: v_base, gate: ctl_cap, buckets: 5}
    - {factor: v_base, gate: ctl_amt, buckets: 5}

stages:
  - id: S0_baseline
    question: "Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?"
    variants:
      - {id: v_base, group: baseline, expr: "ts_spearman(day_quantile(Close), 10)", why: "原始表达式"}
=== journal tail ===
- 不验证 day_quantile(.,0.5) 与 day_median 逐位相同;不自己写 probes.py(R0 那个"脉冲记忆=0"的怪读数
  已被 04_grammar.md 解释掉:对全市场取平均把单只股票的脉冲摊薄了 1/N,不需要新探针)。

落盘:新写 04_grammar.md、05_hypotheses.md(H1~H10,每条带预测和杀死它的实验)、orders/R1.md、
state.md(8 节,覆盖重写)。服务器运行预算:R1 用掉 2 次,全研究还剩 6 次(含 final)。
```

**10-04 13:39 · Bash** — Inspect failed executor agent flow

```bash
cd /Users/wxy/Desktop/Partura && ls -la handoff/F111_spearman_qclose/agents/ 2>&1 && echo "=== work R1 flow ===" && cat handoff/F111_spearman_qclose/agents/work_R1_aba23855eadec7a06.md 2>&1 | head -60
```

```
total 432
drwxr-xr-x@ 10 wxy  staff    320 Oct  4 13:38 .
drwxr-xr-x@  4 wxy  staff    128 Oct  4 13:38 ..
-rw-r--r--@  1 wxy  staff  25470 Oct  4 13:38 lead_R1_a36c37b71e6d128ea.md
-rw-r--r--@  1 wxy  staff  53734 Oct  4 13:28 lead_R1_ab403fe60ef06a414.md
-rw-r--r--@  1 wxy  staff   7083 Oct  4 12:29 study_a0b074c5a7165e4c7.md
-rw-r--r--@  1 wxy  staff   7083 Oct  4 12:29 study_ad5671ea70b9d5889.md
-rw-r--r--@  1 wxy  staff   6953 Oct  4 12:29 study_af2d4d9173011a3e9.md
-rw-r--r--@  1 wxy  staff  69036 Oct  4 13:09 work_R0_a067aac26fed39d46.md
-rw-r--r--@  1 wxy  staff   9048 Oct  4 13:31 work_R1_a85840ced88464c47.md
-rw-r--r--@  1 wxy  staff  28046 Oct  4 13:31 work_R1_aba23855eadec7a06.md
=== work R1 flow ===
# work:F111_spearman_qclose#1 — agent aba23855eadec7a06(工作流 wf_c8c98127-70d)

- 状态:**失败(没有返回结果)**;开始 10-04 13:26,最后一次动作 10-04 13:29;工具调用 15 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F111_spearman_qclose/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 13:27 · Bash** — Check Partura directory exists and list contents

```bash
cd /Users/wxy/Desktop/Partura && pwd && ls
```

```
/Users/wxy/Desktop/Partura
CLAUDE.md
README.md
… (22 行略) …
```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F111_spearman_qclose 2>&1 | head -200
```

```
# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-04 13:28(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F111_spearman_qclose`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F111_spearman_qclose#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F111_spearman_qclose#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `work:F111_spearman_qclose#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:09 → `handoff/F111_spearman_qclose/agents/work_R0_a067aac26fed39d46.md`
```

**10-04 13:39 · Bash** — Inspect tails of failed executor flows

```bash
cd /Users/wxy/Desktop/Partura && echo "=== work_R1 aba tail ===" && tail -50 handoff/F111_spearman_qclose/agents/work_R1_aba23855eadec7a06.md && echo "" && echo "=== work_R1 a858 ===" && cat handoff/F111_spearman_qclose/agents/work_R1_a85840ced88464c47.md 2>&1 | tail -40
```

```
=== work_R1 aba tail ===
    notes/F111_spearman_qclose/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F111_spearman_qclose/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F111_spearman_qclose/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F111_spearman_qclose/NN_*.md          进报告的手写段落(playbook §5)
    configs/F111_spearman_qclose.yaml、studies/F111_spearman_qclose/、runs/F111_spearman_qclose/*.json、logs/F111_spearman_qclose_*.log
    handoff/F111_spearman_qclose/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F111_spearman_qclose
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F111_spearman_qclose "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 要做的事
  
  1. ./scripts/study.sh brief F111_spearman_qclose;找到**最新的、还没有结果卡**的工单 notes/F111_spearman_qclose/orders/R<n>.md,读它。
     (所有工单都有结果卡了:什么都不用做,返回 completed:false、summary 写「没有待办工单」。)
  2. ./scripts/study.sh list F111_spearman_qclose:工单要的 tag 是不是已经跑过(上一个执行可能做到一半被打断)。跑过且 exit 0 的不要重跑,直接读结果;
     exit 97 是被内存守卫让路中止的,要重跑。
  3. 实现并运行:
     - 配置阶段:在 configs/F111_spearman_qclose.yaml 里加阶段(stage id、变体 id、表达式、why 照抄工单),./scripts/study.sh check F111_spearman_qclose,
       通过后 ./scripts/study.sh run F111_spearman_qclose <tag> <stage…>,然后 ./scripts/study.sh wait F111_spearman_qclose <tag>(Bash 的 timeout 设 600000;没完就再 wait。
       排队是正常的)。表达式语言的坑看 playbook §3。
     - 分析脚本:studies/F111_spearman_qclose/<name>.py,用 partura.study_tools.Study(playbook §2「自己写分析」);脚本开头先对一个已知答案自检;
       ./scripts/study.sh exec F111_spearman_qclose <tag> <name>.py,再 wait。
     - **只用 train / valid**。除非工单的 kind 是 final,否则绝不调用 study.sh final。
  4. 把结果读准。工单「要带回来的数字」逐项回答;每个数写清口径:哪个变体、train / valid / utrain / holdout、
     多头口径(hlL)还是多空口径(hlS)、毛还是净。主动报告异常:求值失败的变体、cov < 0.95 或 dist < 0.5、符号与预期相反、
     换手异常、你做过的任何改动。
  5. 写结果卡 notes/F111_spearman_qclose/results/R<n>.md:
       # 结果卡 R<n>
       ## 做了什么(tag、阶段、脚本;哪些没做成、改了什么)
… (43 行略) …
       ## 没人要但值得注意的(异常与意外)
       ## 原始输出在哪(./scripts/study.sh digest F111_spearman_qclose <tag> / logs/…)
     只写事实,不写「所以它是…」—— 那是主研的事。
  6. 记日志:./scripts/study.sh note F111_spearman_qclose "[执行] R<n>:<一句话>" <<'EOF' 最关键的几个数字 EOF
  
  ## 按工单的 kind
  
  - **final**(读留出段,整个研究只许一次):先确认 runs/F111_spearman_qclose/ledger.json 里没有 split 为 holdout 的记录、
    notes/F111_spearman_qclose/10_distilled.md 里已有「读留出段之前」一节;两条有一条不满足就**不要跑**,在结果卡里写明。
    S_final 的候选照抄工单(不得增删),每个变体写 group: final, final: true, profile: true(playbook §3),
    check 通过后 ./scripts/study.sh final F111_spearman_qclose final S_final,再 wait。
    结果卡里放「与用户表同口径」那张表的全部行(多头口径与多空口径各一份)和逐年表。
  - **writeup**:补齐事实类段落(01、02、03、06;每个 07_<stage_id>.md 的「问题 → 结果」部分,解读是主研写的,不要改);
    ./scripts/study.sh report F111_spearman_qclose;把 research/alpha_distillation/F111_spearman_qclose.md 从头读一遍,notes 里引用的每个数字都到表里核对。
    明显的数字笔误直接改并列进结果卡;结论句不要动,有疑问的列进结果卡让主研裁决。
  - **fix**(修订阶段):按工单改 notes 里的数字 / 措辞、补实验(阶段 id 用 SR_ 开头)、重出报告并核对。绝不读留出段。
  - **experiment**:如上。
  
  返回:order(工单号)、completed、result_card(路径)、tags(跑过的 tag)、problems、summary。
```
```

**10-04 13:39 · Bash** — Check git status and previous lead flow

```bash
cd /Users/wxy/Desktop/Partura && git status --short 2>&1 | head -30 && echo "=== recent lead flow (previous main researcher, same round) ===" && head -30 handoff/F111_spearman_qclose/agents/lead_R1_a36c37b71e6d128ea.md
```

```
 D handoff/NOTICE.md
 M research/alpha_distillation/F104_kurt_masktop_amt.md
?? handoff/.recorder_cache.json
?? handoff/F101_day_shine_retstd/
?? handoff/F102_kurt_autocorr/
?? handoff/F103_amt_dw_decay/
?? handoff/F104_kurt_masktop_amt/
?? handoff/F105_std_fangzheng_covamt/
?? handoff/F106_erm_mag_gap_1m/
?? handoff/F107_abs_demean_skew_low/
?? handoff/F108_max_ntkurt_close/
?? handoff/F109_erm_mag_gap_5m_tsm20/
?? handoff/F110_ret_fair_log/
?? handoff/F111_spearman_qclose/
?? handoff/F112_scale_spow_masktop/
?? handoff/F113_nested_tsmax_demean/
?? handoff/F114_q25_closeret/
?? handoff/F115_all_tide_mean_30/
?? handoff/STATUS.md
=== recent lead flow (previous main researcher, same round) ===
# lead:F111_spearman_qclose#1 — agent a36c37b71e6d128ea(工作流 wf_48864a04-f0a)

- 状态:**还在跑**;开始 10-04 13:38,最后一次动作 10-04 13:38;工具调用 2 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F111_spearman_qclose/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 13:38 · agent 的话**

I'll start by getting the full picture of this factor's research state.

**10-04 13:38 · Bash** — Get factor research overview

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F111_spearman_qclose 2>&1 | head -200
```

```
# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-04 13:38(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
```

**10-04 13:39 · agent 的话**

Confirmed: the previous executor failed from quota exhaustion before touching anything — config unmodified, no `studies/` dir, server has only `S0_baseline`. So R1 is entirely un-executed. Per the handoff rule I must re-issue R1 rather than open a new order. Let me read the full state and verify R1 is actually executable.

**10-04 13:39 · Bash** — Read full state.md

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F111_spearman_qclose/state.md
```

```
# F111_spearman_qclose 研究现状

> 本文件每轮由**主研覆盖重写**。最后更新:**第 1 轮(主研,Opus 5)**,2026-10-04。
> 表达式:`ts_spearman(day_quantile(Close), 10)`,来源 挖掘库 / #953。

---

## 1. 一句话现状

建档(R0)已完成,我(第 1 轮主研)读了源码、推出了一个把根节点**精确解掉**的恒等式、写了
`04_grammar.md` 和 `05_hypotheses.md`(H1~H10),并下了第一张工单 **R1(kind: experiment)**;
**下一步是执行去跑 R1**(1 个配置阶段 `S1_whatis` 6 变体 + 1 个 exec 脚本 `x1_identity.py` 4 段),
回来之后第 2 轮主研裁决 H1/H2/H3/H4/H5/H6/H7/H10。

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
| 多头腿毛超额 Lgross | 20 | +13.6% | +20.0% | S0 §1 |
| 多头日换手 LTO | 20 | 4.08% | 3.98% | S0 §1 |
… (233 行略) …
   S0 的 JSON 里 `ls_sharpe` 在 `books`(决策口径)和 `books_user`(用户口径)两处都有、数值不同
   (2.41 vs 2.62),**路径别认错**。
4. **固定半衰期表(2.6)里 hl=0/2/5 的毛超额是我反推的,不是实测**。R1 第 1 项去核实。
   在核实之前,引用 H5 时必须写"反推"。
5. **还没看结果的任务**:R1 的两次运行(tag `S1_whatis`、`x1_identity`)—— 工单已写,
   执行还没跑。`./scripts/study.sh list F111_spearman_qclose` 看服务器上有没有已经跑完没拉回的。
6. **写了一半的文件**:没有。`04_grammar.md`、`05_hypotheses.md`、`orders/R1.md`、本文件都是完整的。
   **还不存在**的:`07_S1_whatis.md`、`07x_1_identity.md`、`08_variants.md`、`09_diagnosis.md`、
   `10_distilled.md`、`11_risks.md`、`12_next.md`。
7. **工具的坑**:
   - `./scripts/study.sh src <算子>` 只认**注册表里的算子名**,未注册的内部辅助函数
     (如 `C._median`)查不到(R0 异常 4)。
   - `ts_spearman` / `ts_pearson` 是 O(N²) 结构,`ts_spearman` 还留着 `for i in range(N)` 的
     Python 循环 ⇒ **慢**。排队和慢都正常(playbook §2),`wait` 没完就再调一次,
     别杀任务、别动显存参数。
   - 往 `configs/*.yaml` 的 `controls:` 里加东西会改变 `all_controls` 的 R²,就和 S0 §7 不可比了。
     要单独对某个家族做中性化,加到 `gates:` 里并用 exec 脚本量(R1 block (c) 就是这么做的)。
   - 服务器运行全研究控制在 8 次以内(含 final,不含 S0)。**R1 用掉 2 次,还剩 6 次。**
8. **此前 3 次挂在这条因子下的 `study` agent(`wf_759ef2d3-03f`)全部因对话额度耗尽、0 工具调用失败**,
   没留下任何文件(R0 异常 11)。`handoff/` 里那三份记录不用看。
```

**10-04 13:39 · Bash** — Check operator sources for R1 variants

```bash
cd /Users/wxy/Desktop/Partura && for op in ts_pearson ts_corr cs_mean ts_rank day_mean day_last; do echo "########## $op ##########"; ./scripts/study.sh src $op 2>&1 | head -40; done
```

```
########## ts_pearson ##########
### ts_pearson  face=nd family=ts category=rolling axis=D reduces_m=False lookahead=False kernel=nd_ts.ts_pearson
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/nd_ts.py:390
@op("nd", "ts", arity=1, requires_window=True)
def ts_pearson(data: torch.Tensor, d: int, abs_corr: bool = False, agg: str = "mean") -> torch.Tensor:
    """For each stock `i` and each rolling window ending at `t`: the
    Pearson correlation of `i`'s window against every OTHER stock `j`'s
    window, aggregated (`mean` or `std`) over `j`.

    Memory: the original built the pairwise products as a literal
    `(T, d, N, N)` tensor, which is quadratic in the universe AND carries the
    window length as a factor -- 2111 days x 300 stocks at window 50 wanted
    ~9.3GB for the bool mask plus ~37GB for the float products, and a full
    5215-stock market wanted ~5.4TB for a SINGLE day. It was consequently
    deferred as a resource risk (`alphamine.factor_contract`) and unusable in
    search. Two changes fix that without changing what is computed:

    1. **The `d` axis folds into a matmul.** `x_centered` is already zero
       wherever the window is NaN, so masking the pairwise product is a no-op
       (`0 * anything == 0`) and
       `sum_k [common_mask * xc_i * xc_j] == einsum('tki,tkj->tij', xc, xc)`.
       The same holds for the pairwise observation count over the float mask.
       Both reduce straight to `(T, N, N)`; the `(T, d, N, N)` intermediate
       never exists.
    2. **The remaining `(T, N, N)` term is chunked over time**, which is exact
       because each window's result depends on no other window.

    Peak working set is therefore `TS_PEARSON_PAIRWISE_BUDGET_BYTES`, not a
    function of the data size. Time is still O(T d N^2) -- the pairwise
    correlation is genuinely quadratic in the universe, and that is a property
… (126 行略) …
### day_last  face=dt family=day category=unary axis=M reduces_m=True lookahead=False kernel=dt_day.day_last
# /root/autodl-tmp/AlphaCube/src/alphacube/operators/dt_day.py:133
@op("dt", "day", arity=1)
def day_last(x: torch.Tensor) -> torch.Tensor:
    return last_valid_last(x).unsqueeze(-1)

# --- day_last 调用的: common.last_valid_last
def last_valid_last(w: torch.Tensor) -> torch.Tensor:
    """Last non-NaN value along the last dim; NaN if the slice has none.
    Shared by DT's `day_last`/`in_last`, same contract as `first_valid_last`.
    """
    d = w.shape[-1]
    idx = torch.arange(d, device=w.device).expand_as(w)
    valid = ~torch.isnan(w)
    idx_when_valid = torch.where(valid, idx, torch.full_like(idx, -1))
    last_idx = idx_when_valid.max(dim=-1, keepdim=True).values
    has_valid = last_idx >= 0
    last_idx_safe = torch.where(has_valid, last_idx, torch.zeros_like(last_idx))
    val = torch.gather(w, -1, last_idx_safe)
    return torch.where(has_valid, val, torch.full_like(val, float("nan"))).squeeze(-1)
```

**10-04 13:41 · agent 的话**

The previous main researcher's R1 is well-built and nothing of it ran. Before re-issuing it, let me verify the identity derivation it rests on and settle its zero-cost item 1 myself from the local JSON.

**10-04 13:41 · Bash** — Explore S0 baseline JSON structure

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F111_spearman_qclose/S0_baseline.json'))
def walk(o,p='',depth=0):
    if depth>4: return
    if isinstance(o,dict):
        for k,v in o.items():
            if isinstance(v,(dict,list)):
                walk(v,p+'.'+k,depth+1)
            else:
                pass
        if depth<=3:
            print(p,'->',sorted(o.keys())[:14])
walk(d)
" 2>&1 | head -60
```

```
.provenance -> ['alphacube_commit', 'alphacube_dirty', 'alphacube_root', 'host', 'numpy', 'partura_code_sha', 'partura_commit', 'partura_root', 'python', 'store', 'torch']
.view -> ['days', 'first', 'last', 'symbols', 'warmup_rows']
.label -> ['buyable', 'horizon', 'kind']
.split_dates -> ['train', 'utrain', 'valid']
.results.v_base.splits -> ['train', 'valid']
.results.v_base.books -> ['by_rank', 'hl_long', 'hl_ls', 'hl_used', 'rank_by', 'splits', 'sweep']
.results.v_base.ic_user -> ['coverage', 'coverage_labelled', 'ic', 'ic_pos', 'ic_t', 'icir', 'n_days', 'rank_ic', 'rank_ic_t', 'rank_icir', 'sign']
.results.v_base.books_user -> ['by_rank', 'hl_long', 'hl_ls', 'hl_used', 'rank_by', 'splits', 'sweep']
.results.v_base.profile -> ['train', 'valid']
.results.v_base -> ['books', 'books_user', 'distinct', 'expr', 'group', 'ic_user', 'profile', 'sign', 'sign_user', 'splits', 'stage', 'why']
.results -> ['v_base']
.errors -> []
.diagnostics.decay -> ['v_base']
.diagnostics.by_year -> ['v_base']
.diagnostics.neutralise.v_base -> ['_traded_signal', 'all_controls', 'ctl_amt', 'ctl_cap', 'ctl_dvol20', 'ctl_ivol', 'ctl_mom20', 'ctl_price', 'ctl_range', 'ctl_rev1', 'ctl_turnrate']
.diagnostics.neutralise -> ['v_base']
.diagnostics.conditional -> ['v_base|ctl_amt', 'v_base|ctl_cap']
.diagnostics.controls.ctl_amt -> ['hl', 'hl_long', 'hl_ls', 'rank_ic', 'sign', 'train_long_ann', 'train_long_gross_ann', 'train_long_sharpe', 'train_long_turnover', 'train_ls_sharpe', 'train_ls_turnover', 'valid_long_ann', 'valid_long_gross_ann', 'valid_long_sharpe']
.diagnostics.controls.ctl_price -> ['hl', 'hl_long', 'hl_ls', 'rank_ic', 'sign', 'train_long_ann', 'train_long_gross_ann', 'train_long_sharpe', 'train_long_turnover', 'train_ls_sharpe', 'train_ls_turnover', 'valid_long_ann', 'valid_long_gross_ann', 'valid_long_sharpe']
.diagnostics.controls.ctl_ivol -> ['hl', 'hl_long', 'hl_ls', 'rank_ic', 'sign', 'train_long_ann', 'train_long_gross_ann', 'train_long_sharpe', 'train_long_turnover', 'train_ls_sharpe', 'train_ls_turnover', 'valid_long_ann', 'valid_long_gross_ann', 'valid_long_sharpe']
.diagnostics.controls.ctl_range -> ['hl', 'hl_long', 'hl_ls', 'rank_ic', 'sign', 'train_long_ann', 'train_long_gross_ann', 'train_long_sharpe', 'train_long_turnover', 'train_ls_sharpe', 'train_ls_turnover', 'valid_long_ann', 'valid_long_gross_ann', 'valid_long_sharpe']
.diagnostics.controls.ctl_rev1 -> ['hl', 'hl_long', 'hl_ls', 'rank_ic', 'sign', 'train_long_ann', 'train_long_gross_ann', 'train_long_sharpe', 'train_long_turnover', 'train_ls_sharpe', 'train_ls_turnover', 'valid_long_ann', 'valid_long_gross_ann', 'valid_long_sharpe']
.diagnostics.controls.ctl_mom20 -> ['hl', 'hl_long', 'hl_ls', 'rank_ic', 'sign', 'train_long_ann', 'train_long_gross_ann', 'train_long_sharpe', 'train_long_turnover', 'train_ls_sharpe', 'train_ls_turnover', 'valid_long_ann', 'valid_long_gross_ann', 'valid_long_sharpe']
.diagnostics.controls.ctl_dvol20 -> ['hl', 'hl_long', 'hl_ls', 'rank_ic', 'sign', 'train_long_ann', 'train_long_gross_ann', 'train_long_sharpe', 'train_long_turnover', 'train_ls_sharpe', 'train_ls_turnover', 'valid_long_ann', 'valid_long_gross_ann', 'valid_long_sharpe']
.diagnostics.controls.ctl_cap -> ['hl', 'hl_long', 'hl_ls', 'rank_ic', 'sign', 'train_long_ann', 'train_long_gross_ann', 'train_long_sharpe', 'train_long_
… (3683 字符略) …
l_ivol', 'ctl_mom20', 'ctl_price', 'ctl_rev1', 'ctl_turnrate', 'known_amt_max9', 'known_ivol_max9', 'known_stdamt_max9', 'known_stdamt_mean30', 'v_base']
.diagnostics.rank_corr_train.known_amt_max9 -> ['ctl_amt', 'ctl_cap', 'ctl_dvol20', 'ctl_ivol', 'ctl_mom20', 'ctl_price', 'ctl_rev1', 'ctl_turnrate', 'known_amt_max9', 'known_ivol_max9', 'known_stdamt_max9', 'known_stdamt_mean30', 'v_base']
.diagnostics.rank_corr_train.known_stdamt_max9 -> ['ctl_amt', 'ctl_cap', 'ctl_dvol20', 'ctl_ivol', 'ctl_mom20', 'ctl_price', 'ctl_rev1', 'ctl_turnrate', 'known_amt_max9', 'known_ivol_max9', 'known_stdamt_max9', 'known_stdamt_mean30', 'v_base']
.diagnostics.rank_corr_train.known_ivol_max9 -> ['ctl_amt', 'ctl_cap', 'ctl_dvol20', 'ctl_ivol', 'ctl_mom20', 'ctl_price', 'ctl_rev1', 'ctl_turnrate', 'known_amt_max9', 'known_ivol_max9', 'known_stdamt_max9', 'known_stdamt_mean30', 'v_base']
.diagnostics.rank_corr_train.known_stdamt_mean30 -> ['ctl_amt', 'ctl_cap', 'ctl_dvol20', 'ctl_ivol', 'ctl_mom20', 'ctl_price', 'ctl_rev1', 'ctl_turnrate', 'known_amt_max9', 'known_ivol_max9', 'known_stdamt_max9', 'known_stdamt_mean30', 'v_base']
.diagnostics.rank_corr_train -> ['ctl_amt', 'ctl_cap', 'ctl_dvol20', 'ctl_ivol', 'ctl_mom20', 'ctl_price', 'ctl_rev1', 'ctl_turnrate', 'known_amt_max9', 'known_ivol_max9', 'known_stdamt_max9', 'known_stdamt_mean30', 'v_base']
.diagnostics -> ['by_year', 'by_year_scope', 'conditional', 'controls', 'decay', 'neutralise', 'rank_corr_on', 'rank_corr_train']
 -> ['config', 'cost_per_side', 'device', 'diagnostics', 'engine_timings', 'errors', 'factor_id', 'fit_split', 'halflives', 'label', 'peak_anon_gb', 'provenance', 'rank_by', 'results']
```

**10-04 13:42 · Bash** — Read fixed half-life sweep from JSON

```bash
cd /Users/wxy/Desktop/Partura && python3 -c "
import json
d=json.load(open('runs/F111_spearman_qclose/S0_baseline.json'))
v=d['results']['v_base']
print('halflives:', d.get('halflives'))
b=v['books']
print('rank_by',b['rank_by'],'hl_used',b['hl_used'],'hl_long',b['hl_long'],'hl_ls',b['hl_ls'])
print()
print('=== books.sweep type/keys ===')
sw=b['sweep']
print(type(sw), (list(sw.keys())[:10] if isinstance(sw,dict) else len(sw)))
print(json.dumps(sw, indent=1)[:3000])
"
```

```
halflives: [0.0, 1, 2, 3, 5, 10, 20]
rank_by long hl_used 20.0 hl_long 20.0 hl_ls 10.0

=== books.sweep type/keys ===
<class 'list'> 7
[
 {
  "halflife": 0.0,
  "ls_sharpe": 0.3560016198637298,
  "ls_turnover": 0.26434858393301736,
  "long_sharpe": -1.629694108934453,
  "long_ann": -0.08523351078398105,
  "long_turnover": 0.29884341164783385
 },
 {
  "halflife": 1.0,
  "ls_sharpe": 1.1404618514885043,
  "ls_turnover": 0.1859216484645096,
  "long_sharpe": -0.02191956880123775,
  "long_ann": -0.0012025813463764589,
  "long_turnover": 0.19078455959882074
 },
 {
  "halflife": 2.0,
  "ls_sharpe": 1.6625019196604574,
  "ls_turnover": 0.14433596746206312,
  "long_sharpe": 0.8140162952649699,
  "long_ann": 0.04528524183874752,
  "long_turnover": 0.14113012519342877
 },
… (13 行略) …
  "long_ann": 0.07443224744601266,
  "long_turnover": 0.08866113279149303
 },
 {
  "halflife": 10.0,
  "ls_sharpe": 2.4069655900553744,
  "ls_turnover": 0.0663397274492688,
  "long_sharpe": 1.7435359942934348,
  "long_ann": 0.10226408034080965,
  "long_turnover": 0.06083979997299115
 },
 {
  "halflife": 20.0,
  "ls_sharpe": 2.1512350543271967,
  "ls_turnover": 0.043727873095872574,
  "long_sharpe": 1.7902806314401727,
  "long_ann": 0.1044639350382888,
  "long_turnover": 0.04077510294961894
 }
]
```

**10-04 13:42 · agent 的话**

The sweep table has no gross column. Let me read the cost formula in the source so I can reconstruct gross exactly from the stored net and turnover, rather than leaving H5 on an approximation.

**10-04 13:42 · Bash** — Find gross computation in partura

```bash
cd /Users/wxy/Desktop/Partura && grep -rn "long_gross_ann" --include=*.py partura/ | head -20
```

```
(eval):1: no matches found: --include=*.py
```

**10-04 13:42 · Bash** — Find annualization and cost usage

```bash
cd /Users/wxy/Desktop/Partura && grep -rn "def book\|long_turnover\|cost_per_side\|252\|254\|ANN" --include=*.py partura/ | head -40
```

```
(eval):1: no matches found: --include=*.py
```

**10-04 13:42 · Bash** — Find gross computation

```bash
cd /Users/wxy/Desktop/Partura && grep -rn "long_gross_ann" partura/ 2>/dev/null | head -20 && echo "=== files ===" && ls partura/
```

```
partura/books.py:121:        "long_gross_ann": lg["ann"], "long_turnover": float(np.nanmean(turn)),
partura/runner.py:270:                            **{k: br[k] for k in ("ls_sharpe", "ls_gross_sharpe", "long_gross_ann",
partura/runner.py:278:                                            **{k: b0[k] for k in ("ls_sharpe", "ls_gross_sharpe", "long_gross_ann",
partura/runner.py:315:                              for m in ("ls_sharpe", "long_gross_ann", "long_ann", "long_sharpe",
partura/report.py:112:            f"| {_pair(x.get('long_gross_ann'), y.get('long_gross_ann'), pct=True)} "
partura/report.py:142:            f"| {_pair(x.get('long_gross_ann'), y.get('long_gross_ann'), pct=True)} "
partura/report.py:145:            f"| {_pair(pa.get('long_gross_ann'), pb.get('long_gross_ann'), pct=True)} "
partura/report.py:352:                         f"| {_f(rec['long_gross_ann'], pct=True)} | {_f(rec.get('long_ann'), pct=True)} "
=== files ===
__init__.py
__pycache__
books.py
bridge.py
cli.py
decompose.py
diagnose.py
guard.py
lab.py
panels.py
probes.py
propose.py
remote_tools.py
report.py
report_legacy.py
runner.py
semantics.py
splits.py
study_tools.py
```

**10-04 13:42 · Bash** — Read books.py cost and annualization

```bash
cd /Users/wxy/Desktop/Partura && sed -n '60,170p' partura/books.py
```

```
    wl = np.clip(w, 0.0, None) * 2.0
    ok = np.isfinite(sig) & np.isfinite(target)
    r = np.where(ok, target, 0.0)
    n = ok.sum(1)
    ew = np.where(n > 0, r.sum(1) / np.maximum(n, 1), np.nan)
    gross = np.where(wl.sum(1) > 0, (wl * r).sum(1) - ew, np.nan)
    traded = np.abs(np.diff(wl, axis=0, prepend=np.zeros((1, wl.shape[1])))).sum(1)
    return gross - cost * traded, gross, 0.5 * traded


def short_leg_excess(w: np.ndarray, sig: np.ndarray, target: np.ndarray) -> np.ndarray:
    """Gross daily excess EARNED by being short the bottom decile: equal-weight
    universe minus the short basket (positive = the shorts underperformed)."""
    ws = np.clip(-w, 0.0, None) * 2.0
    ok = np.isfinite(sig) & np.isfinite(target)
    r = np.where(ok, target, 0.0)
    n = ok.sum(1)
    ew = np.where(n > 0, r.sum(1) / np.maximum(n, 1), np.nan)
    return np.where(ws.sum(1) > 0, ew - (ws * r).sum(1), np.nan)


def smoothed(sig: np.ndarray, halflife: float) -> np.ndarray:
    return ema_rows(sig, halflife) if halflife else np.asarray(sig, dtype=np.float64)


def fit_halflives(sig: np.ndarray, target: np.ndarray, fit: slice, cost: float = COST,
                  top_frac: float = TOP_FRAC, halflives: Sequence[float] = HALFLIVES) -> Dict[str, object]:
    """Choose the L/S and the long-book half-life on ``fit`` only (first maximum wins)."""
    best: Dict[str, tuple] = {}
    sweep: List[dict] = []
… (61 行略) …
            continue
        sm = smoothed(sig, hl)
        views[name] = {"hl": hl, "splits": {k: book_row(sm, target, d, cost, top_frac) for k, d in evals.items()}}
    out = {"hl_ls": fitd["hl_ls"], "hl_long": fitd["hl_long"], "hl_used": views[rank_by]["hl"],
           "rank_by": rank_by, "sweep": fitd["sweep"], "splits": views[rank_by]["splits"], "by_rank": views}
    return out


def views_of(b: Dict[str, object]) -> Dict[str, dict]:
    """{"ls": {hl, splits}, "long": {hl, splits}} for a ``books`` result of ANY vintage.
    Runs from before ``by_rank`` scored at the L/S half-life and kept the long
    view under ``splits_at_hl_long`` only when the two half-lives differed."""
    if "by_rank" in b:
        return b["by_rank"]
    return {"ls": {"hl": b["hl_ls"], "splits": b["splits"]},
            "long": {"hl": b["hl_long"], "splits": b.get("splits_at_hl_long") or b["splits"]}}


def quantile_profile(sm: np.ndarray, target: np.ndarray, days: slice, n: int = 10) -> List[Dict[str, float]]:
    """Mean next-day EXCESS return (vs the equal-weight universe of scored names)
```

**10-04 13:42 · Bash** — Read stats and constants in books.py

```bash
cd /Users/wxy/Desktop/Partura && sed -n '1,60p' partura/books.py
```

```
"""The tradable-book metrics, in exactly the convention the user's tables use.

AlphaCube's current single-factor ranking (``scripts/pick_single_factors.py``)
judges a factor by two books built from a causally EMA-smoothed signal:

* a **decile long/short book** (gross 1), after 15 bp per unit turnover, and
* a **pure long book**: the long leg of that same decile book rescaled to
  weight 1, minus the equal-weight return of every stock that has both a
  signal and a label that day.  A holding whose label is missing (it opened
  locked at limit-up and could not have been bought) earns 0.

The half-life is chosen from {0, 1, 2, 3, 5, 10, 20} on the FIT period only,
by that book's own after-cost Sharpe, and then held fixed.

``stats`` and ``long_book`` are vendored from that script rather than imported
(the script lives in another session's working tree and changes under us); the
vendoring is guarded by a reproduction check against the user's published
table (``scripts/reproduce_table.py``), which is the only thing that makes a
Partura number comparable with one of theirs.

On top of that convention this module adds the two views a distillation needs:

* ``leg_anatomy`` -- how much of the spread is the long leg and how much is the
  short leg.  In A-shares the short leg cannot be traded, and a book whose
  spread is 80% short leg is a different object from one that is 80% long leg
  even when the two Sharpe ratios agree.
* ``quantile_profile`` -- mean next-day excess by signal quantile.  A decile
  book assumes "more signal is better"; the profile says whether that is true.
"""

… (10 行略) …
from alphacube.metrics import ema_rows, long_short_weights, portfolio_returns  # noqa: E402

HALFLIVES = (0.0, 1, 2, 3, 5, 10, 20)
TOP_FRAC = 0.10
COST = 0.0015


def stats(net: np.ndarray) -> Dict[str, float]:
    f = net[np.isfinite(net)]
    if f.size < 3 or f.std() == 0:
        return {"sharpe": float("nan"), "ann": float("nan"), "mdd": float("nan")}
    eq = np.cumsum(f)
    return {"sharpe": float(f.mean() / f.std() * np.sqrt(252)),
            "ann": float(f.mean() * 252),
            "mdd": float((eq - np.maximum.accumulate(eq)).min())}


def long_book(w: np.ndarray, sig: np.ndarray, target: np.ndarray, cost: float = COST):
    """(net excess, gross excess, one-sided turnover) of the long leg as a pure long book."""
    wl = np.clip(w, 0.0, None) * 2.0
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
  
  ## 这一轮(第 1 轮,最多 10 轮,含读留出段和成文)
  
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
     - ./scripts/study.sh note F111_spearman_qclose "[主研] 第 1 轮:<一句话>" <<'EOF'
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
