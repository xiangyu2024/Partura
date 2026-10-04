# F111_spearman_qclose 研究日志

只追加、不改写。[auto] 是工具自己记的(启动了什么、什么时候跑完);其余是研究员写的:
每看完一个结果,写下它说明了什么、哪条假设变了、下一步做什么。接手的人先读这里(`./scripts/study.sh brief F111_spearman_qclose`)。

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
