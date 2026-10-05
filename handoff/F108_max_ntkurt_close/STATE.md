# F108_max_ntkurt_close — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F108_max_ntkurt_close` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #3264(批次 B01_single_factors)
- 表达式:`day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F108_max_ntkurt_close#1`:已返回结果,最后动作 10-04 15:03 → `handoff/F108_max_ntkurt_close/agents/work_R1_a0819b08292f1d769.md`
  - `lead:F108_max_ntkurt_close#2`:失败,最后动作 10-04 15:41 → `handoff/F108_max_ntkurt_close/agents/lead_R2_aad285e161be28fc9.md`
  - `lead:F108_max_ntkurt_close#2`:失败,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F108_max_ntkurt_close` 看服务器上的 tag,`./scripts/study.sh digest F108_max_ntkurt_close <tag>` 重看结果)。

## 研究现状(`notes/F108_max_ntkurt_close/state.md`,10-04 13:58 更新)—— **先读这个文件**

# F108_max_ntkurt_close 研究现状(每次整个覆盖重写;接手先读这一页)

最后更新:第 1 轮主研读完 `x1_anatomy`、裁决假设表、下了工单 R1。表达式 `day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))`。

## 1. 一句话现状

**机制已经搞清楚了,提纯也有了结论;剩下的唯一问题是「对纯多头用户有没有增量」,而回答它的那一节实验被内存守卫掐断了。**
下一步 = 执行按工单 `orders/R1.md` 跑两次:`x2_longonly`(补齐被掐掉的「叠在已知家族上」那一节 + 落地性检验)、
`S1_nodes`(8 个变体的节点消融与显式日轴记忆)。留出段**未读**。

(…全文 13916 字符,读 `notes/F108_max_ntkurt_close/state.md`)

## 研究日志(`notes/F108_max_ntkurt_close/journal.md`:11 条,其中研究员自己写的 6 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 14:45 [执行] R1 第1次运行 x2_longonly 跑完(exit 0,全程内存 <1.9 GiB,未触发守卫):H11 核心测量做完,B1 发现一个干净的结果

看到了什么(全部数字见 results/R1.md,这里摘最关键的):
- §A2(核心测量,增量=剔除后书-同只数家族书):48 行里多数增量很小且两段不同向;表现最一致的是 K1×D_m30、
  十分位池、剔30%:增量 train+1.5pp/valid+2.1pp(净),两段同向且过了工单+1.5pt门槛;K2 系多在五分位池上增量
  为负或两段反向。不是干净的"H11成立"或"H11死",细节留给主研按口径裁决。
- §A3 自检:(w,p)=(1,1) 对 K1×D_ema20 与 x1 的 add ema20 逐位相同(Lnet+11.1%/+20.3%),公式等价性确认。
  规律:w越小、p=1(温和线性叠加)系统性地比大w或高次幂更好;K1+0.25*D_m30^1 到 Lnet+15.1%/+23.8%,
  比 K1 单独(+12.6%/+22.3%)两段都高。
- §B1(意外的干净结果):D_m30 的"剔除最差x%"(book①)随 x 从3%到20%单调改善,Lshp 到 train+3.81/valid+2.29,
  换手仅1-2%;而"十分位完整排序"(book②)几乎是零/负(Lnet train-0.3%/valid-0.2%,Lshp≈-0.04)。
  强烈支持 H14(单边剔除器,不是排序器)。
- §B2:三个语言可达代理里只有 cross_mean(day_amt,30) 两段都为正且都比不分桶好(train+2.2%/valid+3.5%);
  ctl_amt、ctl_price 两段方向不一致;ctl_cap(天花板)两段+2.5%/+6.3%最强但语言里拿不到。
- §0:utrain+固定hl10 读到 Lnet **-0.6%**(不是正的),与发布值+5.6%方向都不一致;Lgross+5.6%凑巧撞数但是毛口径。
下一步:先出 S1_nodes(固定半衰期表判 H15),再写结果卡。

### 2026-10-04 14:49 [auto] 启动 run S1_nodes:阶段 S1_nodes

### 2026-10-04 14:52 [auto] S1_nodes 跑完(exit 0);重看结果:./scripts/study.sh digest F108_max_ntkurt_close S1_nodes

### 2026-10-04 14:54 [执行] R1 第2次运行 S1_nodes 跑完(exit 0,168.8s,全程用GPU,只有6个变体真正算了新面板):n_pow3逐位复现H2改写版,n_nocube/m_mean30数字与x1替身接近但不完全相同

看到了什么(全部数字见 results/R1.md):
- 固定半衰期表(train)+分位剖面+rank相关全矩阵都拿到了。8个变体 cov 全1.00、dist 0.96~1.00,两道门槛都过,没有变体需要点名。
- n_pow3 对 v_base 交易信号 rank corr 精确 1.000(逐位同 digest 早前的 +1.00),坐实 H2 改写版(pow_2 删得掉)。
- n_nocube 实测(rank corr 0.870,train Lnet -2.6%/+2.4%,LTO 6.3%)精确匹配 x1 表里的"Kmax"行,而不是工单 why 文本引用
  的"r=max|K|"行(0.880,-1.8%,6.6%)——day_max(K) 只取 Kmax 单边,x1 的 r 取 max(Kmax,-Kmin) 双边,fold-active 只占14.46%
  时两者接近但不等。表达式照抄工单没有改动;H3 结论方向不受影响(实测降幅比预期更大)。
- m_mean30 实测 hlL2 Lnet+2.3%/+2.1%(x1 替身预测+2.6%/+2.1%);m_mean60 实测选到的半衰期是2(x1替身选的是3),
  Lnet+1.6%/+5.1%(替身预测+2.0%/+5.2%)——数字接近但非逐位相同,属engine vs numpy替身的预期内小抖动。
- k_max10 (cross_max(day_std(Amt),10)) 与 x2_longonly 里独立算的 K2=known_stdamt_max9(窗口9)几乎同号同量级,互相印证。
下一步:写结果卡 R1,交回主研裁决。

### 2026-10-04 15:01 [执行] R1 完成:结果卡 results/R1.md 写完,07_S1_nodes.md / 07x_2_x2_longonly.md 事实部分已补,交主研裁决

两次服务器运行都是 exit 0、一次性跑完,没有需要重跑或补跑的部分。结果卡里标出的几个主研可能要先看的点:
- H11(§A2 核心测量):结果不干净,只有十分位池、剔30%(尤其K1×D_m30:增量净train+1.5pp/valid+2.1pp)
  过了≥1.5pt两段同向的门槛;五分位池多数增量小且方向不稳,K2×D_ema20五分位剔30%是唯一两段都负的一行。
- H14(§B1):干净支持,剔除式随x单调改善(train Lshp到+3.81),十分位完整排序几乎是零/负。
- H9(§B2):仅cross_mean(day_amt,30)两段都为正且赢不分桶;ctl_amt/ctl_price两段方向不一致。
- H15(S1_nodes):固定半衰期表只有train(digest工具本身的限制,不是我省略);m_mean30/60在train侧
  任何固定hl下都赢四个节点消融变体,但要坐实"同一半衰期valid侧也赢"还差一次类似fixed_line的读数。
- H2改写版:n_pow3对v_base rank corr精确1.000,坐实。H3:n_nocube实测比工单why引用的数字降幅更大
  (-2.6%而非-1.8%),H3方向不受影响,但原因是n_nocube精确对应x1的"Kmax"行而非"r=max|K|"行,已在
  07_S1_nodes.md里注明。
下一步留给主研:裁决H11/H14/H9/H15的最终状态、决定要不要补一次S1固定半衰期的valid侧读数、下R2工单。

## 工单与结果卡(`notes/F108_max_ntkurt_close/orders/`、`notes/F108_max_ntkurt_close/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F108_max_ntkurt_close.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_nodes**(8 个变体):哪些节点是多余的?把软极值记忆显式写进表达式,比口径里的 EMA 好吗?
  n_pow3、n_nocube、n_pow5、n_mean、m_mean30、m_mean60、k_mean30、k_max10

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F108_max_ntkurt_close`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close S0_baseline`
- `S1_nodes`  10-04 14:52  8 个变体  → `./scripts/study.sh digest F108_max_ntkurt_close S1_nodes`
- `x1_anatomy`(自写脚本的输出)  10-04 13:13  exit 97  → `logs/F108_max_ntkurt_close_x1_anatomy.log`
- `x2_longonly`(自写脚本的输出)  10-04 14:42  exit 0  → `logs/F108_max_ntkurt_close_x2_longonly.log`

## 已写的 notes(`notes/F108_max_ntkurt_close/`)

`01_expression.md`(1K)、`02_operators.md`(5K)、`03_decomposition.md`(4K)、`04_grammar.md`(2K)、`05_hypotheses.md`(18K)、`06_baseline.md`(9K)、`07_S1_nodes.md`(10K)、`07x_1_x1_anatomy.md`(20K)、`07x_2_x2_longonly.md`(14K)、`journal.md`(13K)、`state.md`(22K)

## 自写的探针与分析脚本(`studies/F108_max_ntkurt_close/`)

- `probes.py`  10-04 12:16  Probes this tree needs:  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30)))).
- `x1_anatomy.py`  10-04 12:21  x1 -- anatomy of  day_max(pow_1_5(pow_2(nt_ts_kurt(Close, 30))))  on real data.
- `x2_longonly.py`  10-04 14:37  x2 -- the section x1 lost to the memory guard: does F108 give a pure-long user

## 结构化结果(`handoff/F108_max_ntkurt_close/results/`)

(还没有)
