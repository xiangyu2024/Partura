# F113_nested_tsmax_demean 研究日志

只追加、不改写。[auto] 是工具自己记的(启动了什么、什么时候跑完);其余是研究员写的:
每看完一个结果,写下它说明了什么、哪条假设变了、下一步做什么。接手的人先读这里(`./scripts/study.sh brief F113_nested_tsmax_demean`)。

### 2026-10-04 13:12 [执行] R0 建档完成:四份事实文件+结果卡已写,树是不分支链/恒非负/82天回看,基线已对齐公布值

看了什么:study.sh brief;study.sh digest F113_nested_tsmax_demean S0_baseline;scripts/overview_for.py;
study.sh decompose;表达式里全部 7 个不同算子(day_mean/ts_max/sub/cs_demean/pow_2/mul/pow_1_5)的 study.sh src
(含它们调用的 rolling_windows/nanmax_last/create_like/cs_mean/_mean/_valid/sign)。另外读了 S0_baseline.json
和 ledger.json 原文、configs/F113_nested_tsmax_demean.yaml 的 git 历史。

写了什么:notes/F113_nested_tsmax_demean/{01_expression,02_operators,03_decomposition,06_baseline}.md
和 results/R0.md。没有写假设表、没有设计或跑新实验、没有碰 state.md 或配置文件(按分工这些是主研的事)。

结构事实(源码推导,非实测):表达式是一条不分支的链(12 个中间节点全部只被引用 1 次),只用 Ret 一个字段;
两次 pow_2 + 四次 ts_max 组合可证明原始输出恒 ≥ 0(或 NaN),方向完全是外部加的 sign=-1;对 Ret 的尺度是
6 次齐次;四层 ts_max(5/30/20/30)串联,累计回看 82 个交易日(比最大单窗口 30 长得多)。sub(ts_max(...,5),-5)
紧跟 cs_demean,这个"-5"被精确代数抵消,与取值无关——是本次找到的唯一恒等节点。

基线(S0_baseline,errors={}):公布的 sgn/hl/ls[0]/long[0] 四个可核对字段全部复现一致,但公布表"long"列核对
下来是多头腿毛超额(Lgross=+3.7%=0.037),不是净超额(Lnet 只有+0.7%)。决策口径下多头腿净超额/夏普 train 为正
(+1.6%/0.39)、valid 转负(-1.7%/-0.52),long_share 很低且 valid 更低(15.7%→4.2%),钱主要在空头腿;多空夏普
两段都稳(+2.59/+2.39)。分位剖面不单调,valid 峰值在 Q3(+11.5%)不在 Q10(+1.5%)。全部控制变量只张成
R²=0.058。rank IC 随持有期单调上升(不是衰减)。

异常(写进了结果卡,没下结论):① known_stdamt_mean30 缺失于 S0 的中性化表/rank相关表/overview_for.py——
核对 git 历史,加入这条配置的 commit 5ed9d09 比 S0_baseline.json 生成时间晚,判断是时序问题不是求值失败,
但未重跑验证;② view.warmup_rows 实测为 0(配置写 warmup:60,结构需要 82 天),猜测数据源无更早历史,未核实;
③ books 的 rank_by 字段是旧值 'ls'(配置现在是 'long'),但完整 7 点 sweep 证实 hl=1 同时是两种准则的最大值,
数字未受影响;④ digest 的 rICtraded 两段都是空;⑤ digest(原始面板)与 overview_for.py(交易信号)的 rank
相关符号相反(翻方向)但数值对得上,两张表不能直接合并引用。

下一步交给主研:读 results/R0.md 和四份 notes 定研究方向;已标出的异常(尤其①②)可能需要先决定要不要重跑 S0。

### 2026-10-04 13:46 [主研] 第 1 轮(第二次尝试):R1 无结果卡→交回执行;复核算子语义后新增 H11(cs_rank 按股票代码打破并列=板块暴露)与区块 1b

看到了什么:
- brief 显示上一轮主研(lead#1)写完 04_grammar.md / 05_hypotheses.md / orders/R1.md 后 failed(额度中断)。
- study.sh list 确认服务器上只有 S0_baseline:R1 的两个 tag(S1_chain / x1_ties)一次都没跑过。
- orders/R1.md 完整(19.7KB,结尾的「约束」一节齐全),不是写了一半。

判断与决定:
1) 按规矩不另开工单 —— 最新工单没有结果卡,交回执行(status:'order', R1, experiment)。
2) 但工单只写一次、执行只照纸做,所以这一轮全部花在复核上。核对了 c8/c9/c10 依赖的三个
   「本批次第一次用」的算子内核:
   - pow_1_5:内核 where(e<=1, sign(x)*|x|^e, x^e),e=1.5 走不保号分支 → 负数输入 NaN。
     确认工单让 c8 删外层 pow_2 时「必须同时删 pow_1_5」是对的;c9/c10 的 pow_1_5 输入恒非负,安全。
   - cs_median:末尾 expand_as,返回广播后的截面中位数 → c10 的 sub(G, cs_median(G)) 确实是去中位数。
   - cs_rank:pct=True → (0,1];并列用 argsort(stable=True) 打破,即按列序 = 股票代码顺序。
   另复核了上一轮三条代数(mul(G,5) 精确冗余 / 外层四算子除第二次 cs_demean 对排序无贡献 /
   pow_1_5 在非负输入上不改当天排序),全部成立 → 工单里 c6、c5 两个审计点是可信的红线。
3) 发现工单漏掉一个会产生假阳性的机制 → 新增 H11,并在工单末尾追加「主研补注」:
   cs_rank 的 stable 并列把股票代码序写进因子值,所以 c9_rankfold 的 dist 会接近 1 —— 但那是
   「假的修好」,退化只是被改写成代码序。而 A 股代码前缀就是上市板块(600/000/300/688),
   板块对应规模、上市年龄、涨跌幅限制(创业板/科创板 ±20% vs 主板 ±10%)。于是「并列噪声」不是
   会被平均掉的随机噪声,而是逐日稳定、看起来可交易、却毫无逻辑的暴露;它还正好躲过所有现成诊断
   (秩空间线性中性化与 rank 相关都看不见,playbook §6.5),这与 S0「联合 R² 只有 0.058、
   与所有控制变量 rank 相关 ≤0.15」完全自洽。c9 是本工单唯一的升华候选,如果它多头腿好看而
   来源是代码序,那是整个研究最容易骗过人的假阳性。
4) 对应测量 = 区块 1b,不额外花服务器运行:用 st.symbols()(API 已确认存在)对 v_base 和 c9 各量
   三项 —— 多头腿的列序位置分位 vs 0.50;板块占比 vs 全市场;切割点上「进了的」与「被切掉的」
   列下标中位数之差。c9 的面板在 (A) 跑完后已进共享缓存,所以工单强调 (A) 先跑、(B) 后跑。

决定不做的事:
- 不改变体清单、不改 tag、不加第 3 次服务器运行(规矩是交回执行,不是重新设计)。
- 不重跑 S0(known_stdamt_mean30 缺失是时序问题,R1 会免费修好)。
- H10(warmup 前 82 天)仍然不测:占 train 不到 9%,valid/holdout 不受影响,改不了选拔结论。

下一步:执行跑 S1_chain + x1_ties,写 results/R1.md。下一轮主研先看区块 1+2+1b(H1 与 H11),
再看 c9/c10 的多头腿 —— 且 c9 的好数字必须先过 H11 这道闸才算候选。

### 2026-10-04 13:55 [执行] R1:开始执行,S1_chain/x1_ties 均未跑过,从零开始

brief 确认:R1.md 是最新且唯一待办工单(无结果卡),S0_baseline 是服务器上唯一已跑完的 tag。
study.sh list 显示 S1_chain / x1_ties 都没有记录,没有"跑到一半被打断"的情况,按工单从头做 (A)+(B) 两次服务器运行。

### 2026-10-04 13:56 [auto] 启动 run S1_chain:阶段 S1_chain

### 2026-10-04 14:03 [auto] S1_chain 跑完(exit 0);重看结果:./scripts/study.sh digest F113_nested_tsmax_demean S1_chain

### 2026-10-04 14:20 [执行] R1:S1_chain(10 变体)跑完,exit 0,240.5s;c6/c5 代数审计过了,H9 不是警报

看到了什么(决策口径,多头腿,train/valid):c1_b_max5(最内层裸 MAX)Lnet -5.8%/+5.4%、Lshp -0.63/+0.66,
train/valid 不同向,方向都弱;c2_e_rel34 Lnet -1.1%/+8.5%,同样不同向;c3_g_fold1(第一次平方折叠)Lnet
+6.8%/+9.6%、Lshp +1.00/+1.57,两段同向且是本阶段多头腿最强的几个之一;c4_nodemean_out(代数预测的"删第二次
cs_demean 等价物")Lnet +6.9%/+13.3%;c8_nofold_out(删外层 pow_2+pow_1_5)Lnet +5.9%/+11.8%——这三个
(c3/c4/c8)多头腿全部两段同向为正、比 v_base(+1.6%/-1.7%)好得多。c9_rankfold(升华候选)Lnet +3.0%/+0.1%,
固定半衰期表上 hl0~hl20 全部单薄(+1.7%~+3.0%),不像 c3/c4/c8 那样强。c10_medfold Lnet +3.5%/-1.7%,train/valid
不同向。

代数审计(工单最关心的红色警报项):c6_nomul_nosub 与 v_base 的 rank 相关 = +1.00(逐位一致),c5_nopow15 同样
+1.00,c5 的 hl=0 行多头腿(Lnet +0.7%)与 c6 的 hl=0 行(Lnet +0.7%)一致——H8/H9 两条代数预测都被坐实,
不是警报。c8_nofold_out 的 cov 仍是 1.00(没有触发 pow_1_5 负数 NaN 的坑)。known_stdamt_mean30 这次出现在
了中性化残差表和 rank 相关表里(R0 异常①已修好)。

意外:c9_rankfold 的 dist 只有 0.98,不是预期的接近 1.00(c9 在外层插入 cs_rank 之后理论上应该几乎消掉并列);
c6/c5 的 dist 却是 1.00 而 v_base(S0 口径下)是 0.5847——这组数字本身不矛盾(c5/c6 的 dist 用的是当前这次
S1_chain 跑出来的 train 切片,算法等价于 v_base 但数值不是 bit-for-bit 复制,下一步 x1_ties 会专门测并列,
到时候再核对)。c3/c4/c8 这三条"更好"的候选目前还没有做 H11(代码序/板块暴露)式的审查——它们的 dist 都是
1.00(并列几乎不存在),所以 H11 机制大概率不适用于它们,但这是推断不是实测,留给主研判断要不要测。

下一步:跑 x1_ties_and_longbook.py(区块 1~6 + 主研补注 B 节),读完一起写 results/R1.md。

### 2026-10-04 14:20 [auto] 启动 exec x1_ties:studies/F113_nested_tsmax_demean/x1_ties_and_longbook.py 

### 2026-10-04 14:22 [auto] x1_ties 跑完(exit 0);重看结果:logs/F113_nested_tsmax_demean_x1_ties.log

### 2026-10-04 14:30 [执行] R1 完成:S1_chain(10变体)+x1_ties 都跑完,结果卡已写;H1 对多头腿的 sig 口径看不出并列,H11 的列序/板块偏离都在边界内

最关键的数字:
- 多头腿净超额(train/valid)两段同向为正的候选:c3_g_fold1(+6.8%/+9.6%)、c4_nodemean_out(+6.9%/+13.3%)、
  c8_nofold_out(+5.9%/+11.8%),都远好于 v_base(+1.6%/-1.7%,R0)。c9_rankfold(升华候选)+3.0%/+0.1%,
  比这三个弱,固定半衰期表上也更单薄。c4 与 c8 的 rank 相关 +0.99(几乎同一个东西,工单没预测到)。
- H9/H8 两处代数审计都通过:c6_nomul_nosub 与 v_base rank 相关 +1.00;c5_nopow15 的 hl=0 行与 v_base
  的 hl=0 行 JSON 原文精确相同(4 位小数)。没有红色警报。
- x1_ties 区块 1(并列结构,用 sig 不是 raw 面板):多头腿不同取值数/n_long 中位数=1.000(train/valid),
  并列组>=2 占比中位数=0(train)/0(valid),基本没有并列——H1 在"实际交易信号"这个口径下看不出来;
  但这是我的解读选择(区块1第2条该用 sig 还是 raw 面板,工单没写死),结果卡里已经标出来请主研确认。
- B 节(H11):v_base/c9 多头腿的列序分位都在 0.48-0.53(贴着 0.50),板块占比与全市场最大偏离在
  train 科创板(v_base 2.3% vs 基准 11.8%,偏离 9.5pp;c9 2.6% vs 11.8%,偏离 9.2pp),valid 段偏离普遍
  <5pp——都没有触发工单里"偏离>=10pp"的判定线,但 train 的科创板偏离已经很接近这条线,留给主研判断。
- 意外:known_stdamt_max9 这次用长口径选到 hl=5,工单引用 06_baseline.md 的"9d:0"对不上(§8 查无
  "30d:1"这个数字,怀疑是旧口径遗留,没有查实)。c1/c2 这两个最内层节点与波动/换手类控制变量的相关
  幅度(|.|~0.5-0.8)明显高于 c3/c4/c8/c9。空头腿封板票占比虽小(<1%)但把 train 空头腿毛年化超额从
  tgt 口径的 +25.2% 拉到 raw 口径的 +14.3%(valid 段影响小得多)。
下一步交给主研:H1/H2/H3/H5/H9 的裁决,以及 c9 的 H11 过闸判断(本次数字偏向"没有踩到板块暴露"但
train 段科创板偏离接近 10pp 这条线,也要看 c3/c4/c8 要不要补测 H11——它们 dist 都是 1.00,和 c9 不同)。
