# F110_ret_fair_log — 交接状态

_自动生成于 2026-10-04 13:38(`python scripts/recorder.py --brief F110_ret_fair_log` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 ret_fair_log(批次 B01_single_factors)
- 表达式:`mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)), day_mean(in_sustain_stddev(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F110_ret_fair_log#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F110_ret_fair_log`(wf_08351f46-81b):中断,最后动作 10-04 13:10 → `handoff/F110_ret_fair_log/agents/study_ab25579f64bc33601.md`
- agent `lead:F110_ret_fair_log#1`(wf_3cafb924-05e):已返回结果,最后动作 10-04 13:19 → `handoff/F110_ret_fair_log/agents/lead_R1_a59818aeb306ac374.md`
- agent `work:F110_ret_fair_log#1`(wf_3cafb924-05e):已返回结果,最后动作 10-04 13:24 → `handoff/F110_ret_fair_log/agents/work_R1_a837b621766f386da.md`
- agent `lead:F110_ret_fair_log#2`(wf_3cafb924-05e):已返回结果,最后动作 10-04 13:28 → `handoff/F110_ret_fair_log/agents/lead_R2_af37c713ede82119d.md`
- agent `work:F110_ret_fair_log#2`(wf_3cafb924-05e):失败,几乎没做事(不用看)
- agent `work:F110_ret_fair_log#2`(wf_3cafb924-05e):失败,几乎没做事(不用看)
- agent `lead:F110_ret_fair_log#1`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F110_ret_fair_log` 看服务器上的 tag,`./scripts/study.sh digest F110_ret_fair_log <tag>` 重看结果)。

## 研究现状(`notes/F110_ret_fair_log/state.md`,10-04 13:27 更新)—— **先读这个文件**

# F110_ret_fair_log — 研究现状(主研第 2 轮重写,2026-10-04)

> 事实类 notes(`01_expression.md`、`02_operators.md`、`03_decomposition.md`、`04_grammar.md`、`06_baseline.md`)仍然有效,照用、不要重写
> (但 02/03 里「成交量脉冲处的价格冲击」那个读法已被实测修正,见本页 2.3)。假设表全文在 `05_hypotheses.md`。
> **第 2 轮没有新的实验结果可读** —— 第 1 轮下的工单 R1 一次服务器运行都没跑成(上一位执行的会话因用户额度耗尽空转)。
> 所以这一页的科学内容 = 第 1 轮的内容,原样有效;改动只在第 1、3、8 节(把「R1 未执行」这件事写清楚)。

## 1. 一句话现状

**研究卡在「等 R1 的结果」这一步,不是卡在思路上。** 已经读过并裁决的只有 x1 的 0 段(自检)和 B 段前半
(「S 到底是什么」):**这棵树名字上像事件研究,实测是「两个几乎同一件事的日内波动估计之差」,
而且其中约四分之一到三分之一是收盘集合竞价的 241 网格版式伪影,权重还随年份翻倍**。
结构替换(C)、半衰期延长(D)、分位剖面(E)**仍然全部没有结果**:x1 被内存守卫在 B 段中途打断(exit 97),
而第 1 轮为此下的工单 **R1 的两次 exec 预算一次都没用掉**(服务器上至今只有 `S0_baseline`、`x1`,无 `x1c`/`x1d`,无正在跑的任务;
本轮第一条命令 `study.sh list` 已再次确认)。
**下一步:原样执行 R1**(`notes/F110_ret_fair_log/orders/R1.md`,kind: experiment,两次 exec = `x1c: B D`、`x1d: C E`)。
这张工单第 2 轮**没有改动、没有作废、没有被新工单取代** —— 它问的问题一个都还没被回答,其中 **D 段(半衰期 10~120)
是对用户口径最值钱的一问**(多头腿净超额在半衰期 20 处还在单调改善,而 20 只是口径网格的上限)。

(…全文 13201 字符,读 `notes/F110_ret_fair_log/state.md`)

## 研究日志(`notes/F110_ret_fair_log/journal.md`:4 条,其中研究员自己写的 3 条)

最近的 12 条(完整的看文件):

### 2026-10-04 13:08 [auto] x1 跑完(exit 97);重看结果:logs/F110_ret_fair_log_x1.log

### 2026-10-04 13:19 [主研] 第 1 轮:读 x1 的 0/B 段,否定 H3、加强 H1、把 H13(收盘竞价伪影)升级为头号嫌疑;下 R1 补 B 段剩余 + C 结构替换 + D 半衰期延长

**看到了什么。** x1 只跑到 section B 中途就被内存守卫让路(exit 97),但 0 段和 B 段前半是完整的,而且信息量很大。
之前 state.md 让接手者去 wait 的 x1b,`study.sh list` 显示**服务器上根本没有**(从没启动成功)—— 已在新 state.md 第 8 节纠正。

地基是实的:T vs D*|M−Q| rank corr 1.00000,脚本复现的基线与 S0 表逐项对齐。后面的 numpy 替换实验可以信。

**判断(三条)。**
1. **H3 被否定**:M<Q 占 16.69%(train)/ 13.53%(valid),abs_ 不是 no-op,每六七个股票-日真折叠一次。
2. **H1 大幅加强,并修正了 02/03 notes 的读法**:每侧触发占全天分钟 13.7%(中位 33 个触发点),各带 5 分钟窗,
   所以 M 和 Q 各自都近似「当天 5 分钟收益 std」,两侧只差 ~11%((M−Q)/mean p50 +0.107)。
   而「缩量紧跟放量」只占 30.7% —— 探针那个「孤立脉冲 ⇒ j 与 j+1 配对」的图景只覆盖三成,
   **不能再把这棵树读成「成交量脉冲处的价格冲击」**。正确的读法:两个几乎同一件事的日内波动估计之差。
   于是 S 的尺度是日内波动,事件内容只是 ~11% 的调制 —— 提纯的终点很可能就是 D × day_std(Ret)。
3. **H13 被支持并升级为头号嫌疑**:收盘集合竞价那一格触发放量的股票-日占 45%,而且 2018H1 24% → 2021 58% → valid 60%。
   机制探针已证(窗口剩 1 分钟 ⇒ std=0 ⇒ 往 M 里掺硬零)。算术:M 被压低 ~3%(1−1/33),而 M−Q 中位只有 0.107×mean,
   ⇒ 不对称被低估约 28% ⇒ **S 里约四分之一到三分之一是 241 网格的版式伪影,且权重随年份翻倍**。
   这是基线里「多头腿逐年飘、六年四年为负」的头号候选解释,也是报告结论段要写的东西。由此新增 H14。

**决定做什么。** 工单 R1(kind: experiment,两次 exec):
- x1c = sections `B D`:补 B 段没打出来的 rank corr(S, σ) 和 Mc/Qc(切掉最后 4 格),
  加 **D 段半衰期 5~120**。按用户口径,**H9 是这一轮最值钱的一问** —— 基线 hl 0→20 单调改善、每翻倍 +6~8 个点、
  尽头未见顶,而口径网格到 20 为止;这是唯一一条已知的能把多头腿净超额从零往上抬的路。
  判据:hl 40/60 的 Ln 在 train 和 valid 都 > +3% ⇒ 真改进(归因写「来自平滑」);都不高于 hl20 ⇒ H9 死,多头腿定性为不可用。
- x1d = sections `C E`:固定 hl20 下的 21 个结构替换(分开「结构」和「平滑」的唯一干净办法)+ 20 分位剖面。
  C/E 必须同一次跑,E 依赖 C 放进 SIG 的 6 个信号。

**决定不做什么。** (a)H12 邻域扫描(5 分钟窗 / 1σ)不做 —— 若 H1 成立,整条事件机器都要换掉,邻域不值得服务器时间;
(b)H7 可买入过滤降到最低(只影响多空口径,用户只看多头腿;且 buyable/raw 的标签 NaN 只差 0.002);
(c)G 段中性化、H 段已知家族增量留给 R2(必须在读留出段前做完,R2 还来得及);
(d)不重测 02_operators.md 的探针读数(都带自检、在服务器内核上跑过)。

**给执行的内存纪律**(上一轮被打断的原因):每段读数立刻 flush(被打断也算有效读数,照贴);
候选循环末尾 gc.collect();SIG 存 float32 但计算保持 float64;被 exit 97 打断就只重跑剩下的段,不要自己加第 3 次运行。

### 2026-10-04 13:23 [执行] R1:本轮会话因用户额度即将耗尽,未执行任何 run/exec,仅确认现状并更新 state.md

收到工单 R1(notes/F110_ret_fair_log/orders/R1.md),读完 state.md + journal.md + R1 全文。
study.sh list 确认服务器上仍只有 S0_baseline(exit 0)、x1(exit 97),无 x1c/x1d,无正在跑的任务。
本次会话未运行 study.sh run/exec/wait/final/report 中任何一个,未修改 configs/、studies/、partura/、scripts/。
results/R1.md 不存在,R1 两次 exec 预算一次都未用。已在 state.md 第 8 节补一条说明,供下一位执行接手时确认无半成品需要处理。

### 2026-10-04 13:27 [主研] 第 2 轮:R1 无结果卡(上一轮执行空转),按接力规矩不另开工单,原样把 R1 交回执行;state.md 已重写

**看到了什么。** `brief` + `./scripts/study.sh list F110_ret_fair_log` 两处确认:服务器上仍然只有 `S0_baseline`(exit 0)和
`x1`(exit 97),没有 `x1c`/`x1d`,没有正在跑的任务;`notes/F110_ret_fair_log/results/` 为空。
上一位执行读完了工单 R1 和全部 notes,但因用户额度即将耗尽,`study.sh run/exec/wait` 一条都没执行,
也没有改动 configs/、studies/、partura/、scripts/。**R1 的两次 exec 预算一次都没用掉,没有任何半成品需要清理或合并。**

**判断。** 这一轮**没有新的实验读数**,所以假设表的状态一条都不动 —— 没有证据就不改裁决。
科学上的现状仍然是第 1 轮的结论:x1 的 0 段(自检,`T vs D*|M-Q|` rank corr 1.00000,基线逐项对齐 S0)和
B 段前半已读,`S` 被判为「两个几乎同一件事的日内波动估计之差(两侧只差 ~11%)+ 一块收盘集合竞价的 241 网格版式伪影
(触发占比 0.450,2018H1 0.242 → valid 0.600)」;H3 被否定、H1 加强、H13 升级为头号嫌疑。C/D/E 全部无结果。

**决定做什么。** 按手册的接力规矩 —— **最新的工单还没有对应的结果卡,就不另开工单** —— 本轮
**不下新工单、不改 R1、不写第二张纸**,把 R1 原样交回执行(status: order / R1 / experiment)。
我复核过 R1 仍然是正确的下一步:它问的 Q1~Q4 一个都还没被回答,期间没有任何新信息会改变它的设计,
而其中 **D 段(半衰期 5~120)是对用户口径最值钱的一问** —— 基线里多头腿净超额 hl0 −62.3% → hl10 −5.9% → hl20 −0.0%
单调改善、每翻倍 +6~8 个点、到网格上限还没见顶,这是目前唯一一条已知能把多头腿净超额从零往上抬的路。
判据照旧:hl 40/60 在 train 和 valid 都 > +3% ⇒ H9 成立(归因写「来自平滑」);都不高于 hl20 ⇒ H9 死,多头腿定性为不可用。

**决定不做什么。** (a)不另开工单(理由同上:两张纸只会让执行在中间猜);(b)不改 R1 的 section、tag、变体或判据;
(c)不自己去跑 exec(主研不跑实验);(d)不动 G/H 两段的排期 —— 中性化(H8)和已知家族增量(H11)仍然留给 R2,
但**必须在读留出段之前做完**,因为用户口径明确要求回答「相对已知家族有没有增量」。

**进度风险(写给后面的主研)。** 第 2 轮结束时实验读数只有 0/B 段,而一次 exec 要按一小时算。
流程规定第 7 轮还没读留出段就必须进入读留出段那一步 —— 如果 R2 的「表达式化 + G/H」拿不到服务器时间,
就要考虑直接拿现有 train/valid 证据定候选、提前进入 (b)。已写进 state.md 第 7 节。

## 工单与结果卡(`notes/F110_ret_fair_log/orders/`、`notes/F110_ret_fair_log/results/`)

- R1:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F110_ret_fair_log.yaml`)

- 标题:日内收益 × |放量后波动 − 缩量后波动|:按『成交量跳变处的价格冲击』加权的日内收益累积(方向为负 = 加权的月度日内反转)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F110_ret_fair_log`)

- `S0_baseline`  10-04 11:53  1 个变体  → `./scripts/study.sh digest F110_ret_fair_log S0_baseline`
- `x1`(自写脚本的输出)  10-04 13:07  exit 97  → `logs/F110_ret_fair_log_x1.log`

## 已写的 notes(`notes/F110_ret_fair_log/`)

- `01_expression.md`  1487 字节  10-04 12:17
- `02_operators.md`  4268 字节  10-04 12:17
- `03_decomposition.md`  3538 字节  10-04 12:17
- `04_grammar.md`  2104 字节  10-04 12:17
- `05_hypotheses.md`  11687 字节  10-04 13:18
- `06_baseline.md`  4460 字节  10-04 12:25
- `journal.md`  7443 字节  10-04 13:27
- `state.md`  23323 字节  10-04 13:27

## 自写的探针与分析脚本(`studies/F110_ret_fair_log/`)

- `probes.py`  10-04 12:14  Probes this tree needs:  D * | M - Q |
- `x1_anatomy.py`  10-04 13:10  F110 X1: anatomy of  T = D * |M - Q|  and of the signal that is actually traded, -EMA20(T).

## 结构化结果(`handoff/F110_ret_fair_log/results/`)

(还没有)
