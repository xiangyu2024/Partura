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
