# F114_q25_closeret 研究日志

只追加、不改写。[auto] 是工具自己记的(启动了什么、什么时候跑完);其余是研究员写的:
每看完一个结果,写下它说明了什么、哪条假设变了、下一步做什么。接手的人先读这里(`./scripts/study.sh brief F114_q25_closeret`)。

### 2026-10-04 13:04 [执行] R0 建档完成:读通内核源码与基线,写了 01/02/03/06 四份 notes 和结果卡

看到了什么:表达式 cross_quantile_q25(day_close(Ret), 15) 是两层直链(day_close 折叠分钟轴取当天最后一个有效分钟值,
cross_quantile_q25 在交易日轴上滚动 15 天取 0.25 分位数),整条链对 Ret 齐次度=1,没有重复子树、没有恒等节点。
S0_baseline 复现用户表:方向-1、hl=20、utrain LS=+2.36、utrain Lgross=+5.9%(与 published.ls[0]/long[0] 对上;
published.long 对应毛超额不是净超额,Partura 另算的 utrain 净超额是+3.6%)。train/valid 多头腿净超额+1.8%/+8.1%,
long_share 19%~31%(钱大部分在空头腿),分位剖面 train 不单调(Q10<Q8/Q9)、valid 单调,全控制变量中性化 R²=0.162、
残差 Lnet 掉到-20.8%但 rank IC 没变号,cov=1.00/dist=0.62 两道门槛都过,hlL 与 hlS 都选到网格上限 20(没有分化)。
holdout 未读。

判断:这一轮只建档,不提假设、不下结论(执行角色的分工)。四份事实文件(01_expression/02_operators/03_decomposition/
06_baseline)已写完整,结果卡 results/R0.md 汇总了要点和下面这些异常。

异常(写进了 R0.md 第"注意到的异常"节,不重复展开):(a) S0_baseline.json 顶层 rank_by="ls" 与当前配置的
rank_by: long 不一致,但 hlL/hlS 字段各自独立存着且数字看起来没受影响,没有验证是否需要重跑;(b) 顶部决策口径表的
rICtraded tr/va 两列展示为空,但 JSON 的 neutralise._traded_signal.rank_ic 里其实有 train 的数(+0.0070),是展示层
留空不是数据缺失;(c) Ret 字段的精确定义(简单/对数收益、基准价格)本地没有直接文档,只有旁证推断,没有另写探针验证。
errors={}、两个算子的探针表都完整,没有求值失败或读数为空的情况。

下一步:不是我(执行)该决定的 —— 留给主研读 state.md/results/R0.md 之后写假设表和第一张工单。我没有碰
scripts/、partura/、workflows/、handoff/、lab/、docs/,也没有碰 configs/F114_q25_closeret.yaml(含未填的 title 占位行,
因为"用一句话写它是什么"属于判断,没有在这一轮填)。
