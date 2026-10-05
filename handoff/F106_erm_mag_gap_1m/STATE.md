# F106_erm_mag_gap_1m — 交接状态

_自动生成于 2026-10-05 00:42(`python scripts/recorder.py --brief F106_erm_mag_gap_1m` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_1m(批次 B01_single_factors)
- 表达式:`sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 15:35)—— **不许再读**。候选在留出段上的数全在 `runs/F106_erm_mag_gap_1m/final.json`(`./scripts/study.sh digest F106_erm_mag_gap_1m final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F106_erm_mag_gap_1m#1`:已返回结果,最后动作 10-04 23:35 → `handoff/F106_erm_mag_gap_1m/agents/work_R1_a2cc3b41af9915b6e.md`
  - `lead:F106_erm_mag_gap_1m#2`:已返回结果,最后动作 10-05 00:02 → `handoff/F106_erm_mag_gap_1m/agents/lead_R2_a6aa6ca02d7daaec3.md`
  - `work:F106_erm_mag_gap_1m#2`:中断,最后动作 10-05 00:20 → `handoff/F106_erm_mag_gap_1m/agents/work_R2_a74e3d138838a6b1a.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F106_erm_mag_gap_1m` 看服务器上的 tag,`./scripts/study.sh digest F106_erm_mag_gap_1m <tag>` 重看结果)。

## 研究现状(`notes/F106_erm_mag_gap_1m/state.md`,10-05 00:01 更新)—— **先读这个文件**

# F106_erm_mag_gap_1m — 研究现状(主研第 4 轮覆盖重写,2026-10-04)

> 每轮覆盖重写,**≤150 行 / 10 KB**:只放结论与指针。细表在 `07_S_final.md` / `07x_1` / `07x_2` / `05_hypotheses.md`;判断在 `09` / `10` / `11` / `12`。

## 1. 一句话现状

**结论已定稿:分辨 —— 原样对纯多头用户不可用,相对已知成交额家族没有可交易的增量。留出段读过一次,事前登记的 C1~C6 六条判据全部成立、一条都没被否定。**
**本轮(第 4 轮)写完了成文的判断部分**(`08`/`09`/`10` 后半节/`11`/`12` + `05` 的留出段确认表)。**只剩工单 R3(kind: writeup):执行补事实类段落、出报告、逐项核对 14 项数字,服务器运行 0 次。** 14 项全对 → 下一轮 `status: done`;有对不上的 → R4(kind: fix)。

## 2. 中间结果(只放承重的;完整表见指针)

### 2.1 留出段(= 用户测试段 20230808–20251231,581 天;**用户口径** `books_user`,方向/hl 在 utrain 拟合)

(全表在 `10_distilled.md` 后半节与 `07_S_final.md` §2b;五条 sign 全 −1、cov 全 0.967、dist ≥0.993)

| id | hlL | **Lnet** | **Lshp** | LS |
|---|---|---|---|---|
| `f_orig` 原式 | 20 | **−3.19%** | **−0.69** | +3.11 |
| `f_known30` 已知家族 | 0 | **+14.10%** | **+1.51** | +1.94 |
| `f_known30r` cs_rank 版 | 0 | +14.10%(与上行**逐项相同**,rank 相关 1.000) | +1.51 | +1.94 |
| `f_excl_blown15` 叠加 | 1 | +14.64% | +1.57 | +3.29 |
| `f_excl_lu15` 朴素涨停叠加 | 1 | +14.85% | +1.60 | +3.52 |

- 逐年 Lnet(2018→2025,全表在 `07_S_final.md` §7;**holdout 干净整年只有 2024/2025**):`f_orig` **八年全负**(−9.2%~−0.4%;2024 −5.13、2025 −0.43);`f_known30` **八年全正**(+6.6%~+24.6%;2024 +9.2、2025 +14.3)。
- **用户公布的 test 列被精确复现**:公布 LS 3.11 / 多头腿毛 −1.4%,实测 **+3.108 / −1.38%** → 「原样不可用」不是口径差异。
- rank 相关(train,交易信号):`f_orig`↔`f_known30` **+0.0055**(近乎正交);叠加↔基准 +0.923;两张标记互相 +0.893。

### 2.2 C1~C6 裁决(判据**读之前**写死在 `10_distilled.md` 前半节;裁决全文在后半节)

C1 原式多头腿仍全负(净/毛/夏普三项,八年全负)**成立** · C2 多空夏普仍为正(+3.108)**成立** · C3 F106 叠加 ΔLnet **+0.54 pp** < 门槛 +1.5 pp **成立** · C4 朴素涨停 **+0.75 pp** 反而高 0.21 pp **成立** · C5 已知家族 +14.10%/+1.51 落在用户区间 **成立** · C6 cov/dist 全过 **成立**。
→ **六条一条都没被否定,推荐不变。**

⚠ **C3/C4 的读法降级了,报告必须写明**:引擎只在拟合段算 hl 网格,**留出段没有固定半衰期表**,+0.54/+0.75 是「各自拟合 hl」下的(叠加 hl1 对基准 hl0)。
**本轮订正了上一轮的措辞**:它**不是**单方向的「上界」—— 用 utrain 的 hl 敏感性量出错配的**污染 ≲0.4 pp、符号不定**(own-hl 甚至比干净的 hl0 对照还低 0.02 pp),两个方向都远低于门槛与噪声 → 裁决不变。推导与三个数在 `09_diagnosis.md` B1;`07_S_final.md` §4 与 `results/R2.md` 写的是「上界」,**报告以 B1 为准**(R3 工单已交代)。

### 2.3 train/valid 的事实(第 1~2 轮确立,**不要重查**;每条的完整数字与出处在 `09_diagnosis.md` A1~A7)

- **它读的不是日内尾部形状,而是「最近有没有封过涨停板、那几分钟跳多大」的一年期记忆**:上涨分钟 ≤12 时分母塌成 1e-6 → 读数 ×10⁶;塌缩日 86.3%/77.8% 是涨停收盘(基准 1.59%,富集约 50 倍),不是低价股。(A1)
- 多头腿在半衰期网格 {0,1,2,3,5,10,20} **每一点、毛和净全负**(train −67.22% → −6.91%)→ **不是成本问题**;**hlL = hlS = 20 = 用户公布那一行 → 「原式 + 多头最优半衰期」就是原式本身**(网格是全局约定,不扩)。(A2)
- 剖面**倒 U**(train Q1 −28.4% / Q10 −5.3%),两端都是近期封板股 → 线性中性化看不见东西,折叠型要用**同样折叠过的**控制量。(A4)
- 不是成交额/规模/换手/波动/动量/反转的改写(折叠量对五个水平变量 R² **0.068**,对四个「近期涨停」变量 R² **0.444**)。(A5)
- 公布的多空夏普一半以上靠**次日买不进的票**(train 2.82 → 0.42);去塌缩日或 clip(±3) → 转负。多头腿不受此影响。(A3)
- **增量的天花板可以算出来**(解释力最强):ΔLnet ≈ share × 超额之差 = 2.0/0.70/1.93/0.57 对实测 +1.59/+0.52/+1.60/+0.40,**四格吻合到 25% 内**;share 低是因为**已知家族本来就在躲这些票**(相对持有频率只有全市场的 24%~64%)→ **不是清单不准,是这张「不要买」清单多余。** 相加(24 行无一取胜)与中性化残差(五行全负)也都否定。(A6/A7)

## 3. 研究过程与逻辑

读源码(不信字面)→ 要害是「分位数作分母 +1e-6」→ 探针量出三个取值区间 → 推出「截面两端一定是塌缩日」→ x1 解剖真实数据、裁决 H1~H9 → 只剩「对纯多头相对已知家族有没有增量」→ H10~H12 + 工单 R1(x2)→ 第 2 轮裁决并算出天花板,**不再做实验** → 事前登记 + final 工单 R2 → 执行跑完 `final` 被打断两次 → 第 3 轮原样交回 R2、自己裁决 C1~C6 → **第 4 轮(本轮)写判断类 notes + 工单 R3 成文**。

源码里和名字不一样的地方(全文 `02_operators.md`):**计数分母的 1e-6 是除零保护,分位数分母的 1e-6 才是要害**(带量纲,比一个 tick 小三个数量级);树里**没有日轴算子**(真实回看 1 天,时间结构全来自口径里的因果 EMA);`cross_*` 窗口网格没有 20;**本机 torch 与服务器内核的分位数位置不一致 → 以服务器为准**。

## 4. 假设表(H1~H13 **全部已定,不要再查**;逐条证据、「还差什么」、留出段确认表都在 `05_hypotheses.md`)

- **被支持**:H1 / H3 / H6 / H8 / H9(塌缩日决定一切 / 塌缩日=封板日 / 两端都是打板股+倒 U / 两侧不对等 / 多余节点不改排序)。
- **被否定**:H2 / H4 / H5;**H10 排除性增量**(事前四判据 (a)(b) 过、(c)(d) 不过;valid +0.57、holdout +0.54 pp;天花板见 §2.3)。
- **H7 方向反了 → 改写成 H11 记忆长度错配**:**被支持但不产生候选**(计数构造 rank IC 是 EMA20(X) 的 1.7~4.8 倍,但取值几乎全 0 → 过不了 `dist`)。
- **H12 已改写**:字面版否定,**操作版被支持**(排除用途上朴素涨停标记反而更好,C4)。
- **H13 合理但未坐实**:`listed<250d`(+1.60/+1.09/+1.90/+1.95)是新股过滤器,**不是这条因子的功劳** → `12_next.md` 第 1 条。

## 5. 候选

**没有任何 F106 变体可以推荐。结论类型 = 分辨**(不是提纯、不是升华)。不是「没找到」—— 六条理由和 11 条已排除候选都在 `10_distilled.md`「为什么没有更好的」(另见 `07x_1_anatomy.md` E 表)。
事前第一推荐 = **`f_known30` = `cross_mean(day_std(Amt), 30)`**(已知家族,规则必含;holdout +14.10%/+1.51)—— **它不是这条因子的产物**。
对纯多头用户唯一可操作的输出:**F106 不进书,继续用已知成交额家族;要「别买刚封过板的票」这个排除效果,一个朴素日线涨停标记就够**(而且两者在留出段都在噪声里,连叠加本身也不推荐)。

## 6. 后面的研究思路

1. **下一轮:执行做工单 R3(kind: writeup)**,细节在 `orders/R3.md`:补事实类段落(`01`、`06`、**新建 `07_S0_baseline.md`**)、`study.sh report`、**逐项核对 14 项数字** + 单位(ΔLnet 写 pp)与口径(holdout 只来自 `books_user`)两项检查。**服务器运行 0 次。**
2. **再下一轮**:14 项全对 → `status: done`;有对不上的 → R4(kind: fix),**只改数字/措辞,不改结论、不改推荐**。
3. **明确不做**:不再下实验工单;不重跑 `S1_regime`;不找 X 的单调变换;不抢救空头腿/多空夏普;不扩半衰期网格;**不补留出段的剖面与固定半衰期表(重跑 = 第二次读留出段)**;H13 不在本研究里验;不动 `scripts/`、`partura/`、`workflows/`、`handoff/`、`lab/`、`docs/`、别的因子的文件。

## 7. 留出段

**已读,10-04 15:35,就那一次**(`ledger.json`:`holdout {reads: 1, expressions: 5}`;`S_final.json` exit 0、310.3 秒、`errors` 空)。**绝不许再下 final 工单、绝不许再跑 `final`/`run`。**
读前的候选排序与判据在 `10_distilled.md`「读留出段之前」(14:59 写,早于 15:29 启动 final,**一个字未改**);读后的裁决在同文件「读完留出段之后」。重看:`digest ... S_final` 或直接读 JSON(不算再读)。

## 8. 给接手者的提醒

- **还没看结果的任务:无。** 唯一在飞的是工单 R3(本轮刚下,还没有结果卡)。**判断类 notes(`05` 末尾 / `08` / `09` / `10` 后半节 / `11` / `12`)已经写完,不要重写。**
- **两套书别混**:`books` 在 train 拟合、只报 train/valid;`books_user` 在 utrain 拟合、报 utrain/**holdout** → holdout 一律读后者。
- **JSON 里没有的东西**(别找、别重跑):留出段的分位剖面与固定半衰期表(`profile` 只有 train/valid,`sweep` 只在拟合段);`by_year` 没标注用哪套 hl(不影响 `f_orig`/`f_known30`,两套 hl 相同)。
- **最容易张冠李戴的一处**:x2 的叠加行是**20 日窗口、hl 不重拟合**(ΔLnet +1.59/+0.52),S_final 的 `f_excl_blown15` 是**15 日窗口、引擎重拟合**(+1.63/+0.57)。接近是互相印证,**不是同一行**(`08_variants.md` §5)。
- 另外三个读表的坑都写在 `08_variants.md`:`cov` 随 split 变但五个变体相同(= 面板覆盖率,不是求值失败,§2)、0/1 计数构造的「多头腿」是假的(§7)、x2 叠加行的 `LS`/`short` 不可读(§8)。
- 服务器很挤:x2 排了 1480 秒;`S1_regime` 被内存守卫顶掉(**exit 97 = 根本没跑**);`[guard] waiting` 正常,别起第二个 job;`wait` 只打最后 200 行 → 读 `logs/` 全文。
- **一句话**:三件事都已确立并在用户测试段上按事前判据验过 —— 「它是什么」(封板记忆)、「原样不可用」(holdout 多头腿 −3.19%、八年全负)、「相对已知家族没有增量」(holdout Δ +0.54 pp,天花板可算)。**不要抢救、不要换推荐**,剩下的全是核对数字。

## 研究日志(`notes/F106_erm_mag_gap_1m/journal.md`:13 条,其中研究员自己写的 8 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 15:29 [auto] ⚠ 读留出段:final S_final,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 15:35 [auto] S_final 跑完(exit 0);重看结果:./scripts/study.sh digest F106_erm_mag_gap_1m S_final

### 2026-10-04 23:16 [主研] 第 3 轮:R2 的 final 已跑完但结果卡被打断 → 按规矩原样交回(并在工单末尾写明禁止再跑 final);我自己读 S_final.json 裁决 C1~C6,六条全部成立,结论定稿=分辨

看到了什么:
- brief 显示留出段已读(10-04 15:35),但 notes/.../results/R2.md 和 07_S_final.md 都不存在 → 上一个执行跑完 final 之后被额度打断了两次。
  磁盘事实:runs/F106_erm_mag_gap_1m/S_final.json 存在(135 KB、seconds 310、errors 空、5 个变体全部求值成功);
  ledger.json 的 summary 里 holdout {reads: 1, expressions: 5} → 那唯一一次读取已经用掉了。
- 按工作流第 2 条(最新工单没有结果卡 → 不另开工单,原样交回),本轮返回 {status: order, order: R2, kind: final}。

这一轮我做的三件事:
1. **给 R2 补了一节「补充(主研第 3 轮)」**,这是本轮最要紧的动作:工单正文第 0~3 步写的是「怎么跑 final」,已经过时;
   如果换上来的执行照着做,就会第二次读留出段 —— 这项研究唯一不可挽回的错误。补充里写明:本轮服务器运行 = 0 次,
   跳过 check/final/run,直接 digest + 写两份文件;并逐项给了 JSON 路径与字段映射(books 是 train 拟合只报 train/valid,
   books_user 是 utrain 拟合、报 utrain/holdout → holdout 一律读后者),以及三件要照实写明的事:
   (a) 用的是主版不是兜底版(f_known30r 与 f_known30 的书逐项相同、rank 相关 1.000 → cs_rank 语义与预期一致);
   (b) holdout 的分位剖面「缺」(profile 只有 train/valid,f_known30r / f_excl_lu15 的 profile 是空的),不要重跑;
   (c) C3/C4 的读法必须降级并写明降级(见下)。
2. **自己读 S_final.json,按事前登记的判据裁决 C1~C6:六条全部成立,一条都没被否定。**
   f_orig holdout(用户口径,hl 在 utrain 上拟合
…(这条日志还有后文,读 journal.md)

### 2026-10-04 23:34 [执行] R2:留出段已读(本轮服务器运行0次,只digest+读JSON),S_final五条候选的数字已带回,结果卡与07_S_final.md写完

本轮没有调用 check/final/run/exec,只重看已跑完的 S_final(exit 0,10-04 15:35)+ 直接读 JSON 核对字段;ledger.summary.holdout={reads:1,expressions:5} 确认留出段没有被第二次读取。

C1/C2(f_orig holdout,books_user 用户口径,hlL=hlS=20):Lnet −3.19%、Lshp −0.69、Lgross −1.38%、LS +3.11 —— 与用户表 test 列(LS 3.11 / Lgross −1.4%)精确复现。
C5(f_known30 holdout):Lnet +14.10%、Lshp +1.51,落在用户给的 +13~15%/1.4~1.9 区间内。
C3/C4(排除性增量 ΔLnet,holdout,引擎各自拟合半衰期下的上界):f_excl_blown15−f_known30r = +0.54pp(hl1对hl0);f_excl_lu15−f_known30r = +0.75pp(hl1对hl0)。train/valid 口径下 C3 恰好是同hl的干净对照(+1.63pp / +0.57pp),C4 始终是不同hl的上界(+2.56pp / +1.22pp)。
C6:5个变体 cov(ic_holdout.coverage)全部 0.9675,dist 全部 ≥0.9933 —— 全过门槛。

核实的三件事:(1) 主版非兜底 —— 两条叠加候选 expr 字段核对都是 cs_rank 版;f_known30 与 f_known30r 在 hl0 下书逐项相同、rank相关(train)=1.000。(2) holdout 分位剖面缺(profile 字段只有 train/valid;f_known30r/f_excl_lu15 连 profile 字段都不存在)。(3) holdout 固定半衰期表缺(sweep 只在各自拟合段算),C3/C4 已按降级读法处理并在表里标出是否同一半衰期。

异常/值得注意:无求值失败、无 NaN;5 个变体 sign/sign_user 全部 −1;cov 这个数在 train(0.691)/valid(0.895)/utrain(0.749)/holdout(0.967)差
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:02 [主研] 第 4 轮:R2 结果卡已到 → 留出段已读 ⇒ 本轮必须是 (c) 成文;写完 08/09/10后半节/11/12 + 05 留出段确认表,下工单 R3(kind: writeup,服务器运行 0 次);并订正了「上界」这个措辞

(工作流给我的轮次计数是「第 2 轮」,但磁盘上这是第 4 个主研轮次 —— state.md 和日志一律按磁盘的数走,免得接手的人对不上。)

看到了什么:
- brief 显示 R2 的结果卡已经写好(10-04 23:34,执行本轮服务器运行 0 次,只 digest + 读 JSON)。
  `ledger.summary.holdout = {reads: 1, expressions: 5}` 仍然是 1 —— 留出段没有被第二次读取。
  → 工作流第 2 条(最新工单没有结果卡就原样交回)不再适用;规矩里「留出段已读的,这一轮必须是 (c)」生效。
- 结果卡和 07_S_final.md 的数字我自己对着 07_S_final.md 的 §2b/§3/§4/§7/§8 核过,与第 3 轮我直接读 JSON 得到的 C1~C6 裁决一致,没有出入。

判断(这一轮唯一的新判断,其余都是把已有结论落成文字):
- **上一轮把 holdout 的 ΔLnet +0.54 pp 叫做「上界」,这个措辞不准,我订正了。** 理由:
  叠加候选在留出段拟合到 hl 1、基准拟合到 hl 0,所以差值里混了半衰期错配。错配有多大,可以用**有网格的 utrain** 去量
  (只借 hl 敏感性,不是把 utrain 的数当成 holdout 的数 —— 那正是「张冠李戴」):
  own-hl Δ = 16.71 − 15.40 = +1.31 pp;同 hl0 Δ = 16.73 − 15.40 = +1.33 pp;同 hl1 Δ = 16.71 − 15.00 = +1.71 pp。
  → 错配量级 ≲0.4 pp,而且 own-hl 读数比干净的 hl0 对照**还低 0.02 pp** —— 偏差方向不定,不是单方向的上界。
  这个订正让结论更稳(不再需要「只是上界」这个让步),而且两个方向都远低于 +1.5 pp 门槛与 ±3 pp 噪声 → **C3 的裁决不变、推荐不变**。
  写在 09_diagnosis.md B1,10_distilled.md 的降级说明里也指过去;R3 工单让执行在报告里按 B1 写,并把 07_S_final.md §
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F106_erm_mag_gap_1m/orders/`、`notes/F106_erm_mag_gap_1m/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有
- R3:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F106_erm_mag_gap_1m.yaml`)

- 标题:分钟收益右尾 ES/VaR 减左尾 ES/VaR;分母 +1e-6 在「上涨(下跌)分钟不足 5%」的日子塌掉,截面两端由这些日子决定
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_regime**(10 个变体):公布的多空夏普(和空头腿)是「塌缩日 = 封板事件」做出来的,还是「尾部形状不对称」做出来的?差的符号有没有信息?
  a_right、a_left、a_sum、a_abs、a_regular、a_eps3、a_flag、a_rankfirst、a_lockshare、a_limitup
- **S_final**(5 个变体):读留出段之前写死的结论(原式多头腿全负 / 排除性增量在噪声以下 / 和已知家族相加更差)在用户的测试段(20230808–20251231)上成不成立?
  f_orig、f_known30、f_known30r、f_excl_blown15、f_excl_lu15

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F106_erm_mag_gap_1m`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m S0_baseline`
- `S_final`  10-04 15:35  5 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m S_final`
- `x1`(自写脚本的输出)  10-04 12:30  exit 0  → `logs/F106_erm_mag_gap_1m_x1.log`
- `x2`(自写脚本的输出)  10-04 13:54  exit 0  → `logs/F106_erm_mag_gap_1m_x2.log`

## 已写的 notes(`notes/F106_erm_mag_gap_1m/`)

`01_expression.md`(2K)、`02_operators.md`(2K)、`03_decomposition.md`(3K)、`04_grammar.md`(1K)、`05_hypotheses.md`(21K)、`06_baseline.md`(3K)、`07_S0_baseline.md`(3K)、`07_S_final.md`(13K)、`07x_1_anatomy.md`(10K)、`07x_2_longonly.md`(23K)、`08_variants.md`(5K)、`09_diagnosis.md`(10K)、`10_distilled.md`(13K)、`11_risks.md`(6K)、`12_next.md`(4K)、`journal.md`(27K)、`state.md`(10K)

## 自写的探针与分析脚本(`studies/F106_erm_mag_gap_1m/`)

- `probes.py`  10-04 12:13  Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.
- `x1_anatomy.py`  10-04 12:19  x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.
- `x2_longonly.py`  10-04 13:02  x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

## 结构化结果(`handoff/F106_erm_mag_gap_1m/results/`)

(还没有)

报告:`research/alpha_distillation/F106_erm_mag_gap_1m.md`(10-05 00:18 生成)
