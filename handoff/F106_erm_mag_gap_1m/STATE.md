# F106_erm_mag_gap_1m — 交接状态

_自动生成于 2026-10-05 11:21(`python scripts/recorder.py --brief F106_erm_mag_gap_1m` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_1m(批次 B01_single_factors)
- 表达式:`sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 15:35)—— **不许再读**。候选在留出段上的数全在 `runs/F106_erm_mag_gap_1m/final.json`(`./scripts/study.sh digest F106_erm_mag_gap_1m final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F106_erm_mag_gap_1m#2`:已返回结果,最后动作 10-05 00:02 → `handoff/F106_erm_mag_gap_1m/agents/lead_R2_a6aa6ca02d7daaec3.md`
  - `work:F106_erm_mag_gap_1m#2`:中断,最后动作 10-05 00:20 → `handoff/F106_erm_mag_gap_1m/agents/work_R2_a74e3d138838a6b1a.md`
  - `synth:F106_erm_mag_gap_1m`:已返回结果,最后动作 10-05 11:20 → `handoff/F106_erm_mag_gap_1m/agents/synth_a2e1488766b481d6b.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F106_erm_mag_gap_1m` 看服务器上的 tag,`./scripts/study.sh digest F106_erm_mag_gap_1m <tag>` 重看结果)。

## 研究现状(`notes/F106_erm_mag_gap_1m/state.md`,10-05 11:15 更新)—— **先读这个文件**

# F106_erm_mag_gap_1m — 研究现状(主研第 5 轮覆盖重写,2026-10-05:批量扫描 s1 + 市场解剖)

> 每轮覆盖重写,只放结论与指针。**本轮全文判断在 `synthesis.md`(带每个论断的变体 id 和数字);第二批假设在 `studies/F106_erm_mag_gap_1m/hypo.yaml`(37 条,已过 `study.sh hypo`)。** 前几轮细表在 `07_S_final.md` / `07x_1` / `07x_2` / `05_hypotheses.md`,判断在 `09`~`12`。

## 1. 现状

**结论类型 = 分辨,未变:原式对纯多头用户不可用(多头腿 train/valid/utrain 三段全负),相对已知成交额族 `cross_mean(day_std(Amt), 30)` 没有可交易的增量。** 留出段已读过一次(已登记,**不可再读**),C1~C6 全部成立。
本轮是**一轮制主研**:读完 152 个变体大表(`runs/.../sweep_s1.json`)+ 23 段 × 14 时段解剖(`anatomy_s1.json`),落成 `synthesis.md` + 第二批假设,服务器运行 0 次。**结论没被推翻,但「承重在哪个节点」和「在市场的哪一段有效」现在有了全市场实测证据。**

## 2. 中间结果(只放承重的;完整数字在 `synthesis.md`)

基准 `k_known` = **+12.6% / +22.3% / +15.4%**(tr/va/ut),Lshp +2.22、换手 3.4%。原式 `v_base` = **−6.9% / −3.2% / −5.8%**,Lshp −1.91、换手 2.4%、LS tr +2.82、底腿 tr −27.9%、ρk +0.01。

1. **承重 = 「分位数当分母 + 1e-6」一个节点。** `abl_G`(A+1e-6 → A+A,结构不动、只抹平塌缩)→ LS **+2.82 → +0.06**、ρo −0.26;`abl_J`(除以 A)→ LS −1.59;`abl_V` → −1.14;`abl_R` 全 NaN(cov 0.00)。**计数侧写法相同的 1e-6 是装饰**:`abl_H` ut −5.7% / ρo **+0.98**、`abl_S` ρo +0.84。
2. **公布的多空夏普是 EMA 造的。** v_base 半衰期网格(train,[Lnet, Lshp, LS]):hl0 `[−67.2%, −19.51, −25.67]` → hl3 `[−25.8%, −8.16, +0.09]` → hl20 `[−6.9%, −2.15, +2.82]`,**LS 在 hl ≥ 3 才转正**。基准的网格单调相反(hl0 +12.6% → hl20 +8.4%)→ 基准是真的日频状态,它不是。
3. **幅度必需、形状没用。** `abl_D`/`abl_O`(分子由 Σ 幅度换成计数)ut −32.7%/−27.6%;抹掉幅度的 `rk`/`win`/`rank_X` 为 −12.9%/−9.6%/−10.4%(换手全从 2.4% 炸到 13~15%,`rank_X` 的 LS 变 −1.01)。
4. **多余节点(ρo = 1.00、逐位相同)**:`sub_U_neg`、`sub_N_neg`(`abs_`→`neg`);`sub_H_sub`、`sub_S_sub`。`abl_N` ≡ `sub_X_add` 逐行相同 → 两条腿严格镜像。**计数可整个删掉**:`only_H_R` / `sub_F_day_first/last/close` ut **+1.5%**、va **+10.4~+10.8%**、ρo +0.57(全表非 overlay 最好的一族,但 ut 仍在噪声内)。
5. **叶子互换换掉的是家族**:`in_pct(Amt,1)` / `in_pct(Volume,1)` → 方向翻正、ut +1.5%/+1.1%、ρo −0.10 而 **ρk +0.69**;`in_logchg(Volume,1)` −10.1%;`in_pct(Close,5)` ρo +0.57 同一条因子(**没有采样频率平台**)。
6. **解剖:23 个段里 22 个段内为负。** 唯一正数 =「近 15 日有冻结盘口」段内 **+18.2%**(占 6.5%、自身等权 **−67.4%**/年、书还超配 **+4.6pp**);干净段 93.5%(等权 +3.7%)段内 **−6.9%**、低配 −4.6pp。市值 / 成交额 / 价格五档**全部为负**(最差 −13.1%、−12.5%、−10.9%)→ **不是规模/流动性/低价因子**;科创板 −23.6% 最差(该段自身等权超额却是四个板块里最好的 +4.1%);次新 −15.0%。六年全负(−9.2 ~ −0.6),上涨段 −7.2 比下跌段 −3.7 更差,高/低波动、高/低离散、放量/缩量全在 −5~−6% → **没有任何状态救得了它**。
7. **增量:没有。** 六条 overlay 全部严格差于基准单独、随 |w| 单调恶化(+12.6% / +11.6% / +10.3% / +10.7% / +9.0% / +6.2%,ΔLnet −2.8 ~ −9.2pp,**两个方向都伤** → 是稀释不是方向错);`res_known` −12.2%、`bk_known` −12.3%、`res_liq` −11.7%、`bk_liq` −12.1%,换手全炸到 15.4%。
8. **对基准的新理解(对整批有用)**:`k_known` 的多头腿是**段间倾斜而非段内选股** —— 成交额五档段内 −4.1/−5.3/−8.2/−5.2/**+2.5**(四档为负),靠**超配最低档 +80.3pp**(该档自身等权 +15.1%/年)拿到 +15.4% → 要有增量得加在**低成交额桶内部**。
9. **`abl_M` 是全表唯一多头腿稳定为正的非 overlay 变体**(ut +3.4%、Lshp +0.59、换手 2.2%、ρo +0.34、ρk 只 +0.06、**六年全正**),但它在成交额五档段内**五档全负**(−11.8 ~ −2.8),靠超配最低档 +26.2pp / 次新 +16.9pp → **和基准同一个机制的更弱版本;低 ρk 在这里不等于有增量**,不做候选。

## 3. 过程与逻辑

读源码(不信字面)→ 要害是「分位数作分母 +1e-6」→ 探针量出三个取值区间 → 推出截面两端一定是塌缩日 → x1 解剖真实数据裁决 H1~H9 → 第 2 轮算出增量天花板、不再做实验 → 第 3 轮事前登记 + 读留出段、自裁 C1~C6 → 第 4 轮写成文判断 → **第 5 轮(本轮)读 152 个变体大表 + 全市场解剖,把「承重在哪个节点」「在哪一段有效」从推断升级为实测,并提第二批假设。**

机制推断(全文 `synthesis.md` §3):塌缩条件「某一侧分钟数 ≤5%」的现实对应物是**封板钉价 / 停牌前后 / 3 元以下的 tick 网格**;sg = −1 → 多头腿买的是**下跌侧塌缩**的票 = 刚封过涨停板的票 → 它是一条**彩票需求(MAX 效应)代理:对多头反、对空头对,而空头那一端次日买不进**。冻结段 +18.2% = 「在已经封过板的票里挑哪一只」它确实会;干净段 −6.9% = EMA 记忆跨约 250 天,干净段的排序由几周到几个月前的封板残留决定 → 买的是封板后的反转输家。

## 4. 假设表

- 第一批 H1~H13 **全部已定,不要再查**(逐条证据在 `05_hypotheses.md`):支持 H1/H3/H6/H8/H9,否定 H2/H4/H5/H10,H7→H11(**上一轮因 dist 门槛产不出候选**),H12 操作版支持,H13 合理未坐实。大表只是加强它们:H1/H3/H6/H8/H9 被 152 行结构实验坐实(§2 的 1/3/4/6),H10 被 overlay 单调恶化 + §2.8 的基准解剖双重坐实。
- **第二批 37 条在 `studies/F106_erm_mag_gap_1m/hypo.yaml`**,六个方向(A 有界状态量 10 / B 不会塌的尺度 + ε 阶梯 + 两区间互补门控 8 / C 新算子读日内形状 7 / D 分桶中性 4 / E 有界量做 overlay 打进低成交额桶 4 / F 承重结构最小改动 4),每条的 `why` 指向 `synthesis.md` 的具体一节。**H11 用 `cross_mean(·,30)` 救回来了**(`h_blow_sgn30/60`)。

## 5. 候选

**仍然没有任何 F106 变体可以推荐。** 事前第一推荐 = `f_known30` = `cross_mean(day_std(Amt), 30)`(留出段 +14.10% / +1.51)—— **它不是这条因子的产物**。
对纯多头用户唯一可操作的输出:**F106 不进书,继续用已知成交额家族;要「别买刚封过板的票」这个排除效果,一个朴素日线涨停标记就够**(两者在留出段都在噪声里,连叠加本身也不推荐)。
观察位(不是候选):`only_H_R` / `sub_F_day_*`(ut +1.5%、va +10.8%,只是「删掉计数」)与 `abl_M`(已被 §2.9 判为流动性倾斜)。

## 6. 后面的思路

1. **下一轮:把 37 条交给扫描**(`sweep.py --extra studies/F106_erm_mag_gap_1m/hypo.yaml`),重点看 A/B 两族能不能复现底腿而换手留在 2% 量级、`h_regular_gate` 是否接近 0;若 A/B 坐实「常规区间是空的」,分辨结论即可封板。
2. **E 族(`h_known_inlow` / `h_ov_zero_m025`)是唯一还可能产生候选的方向**,它打的是 §2.8 的新事实(基准在低成交额桶内不选股),不是 F106 自己的内容。若成功,**功劳记给「冻结状态 + 分桶」,不记给 F106**。
3. **明确不做**:不重读留出段(再跑 = 第二次读);不扩半衰期网格;不抢救空头腿/多空夏普;不找 X 的单调变换;不再扫窗口(树里没有窗口);H13 不在本研究里验;不动 `scripts/`、`partura/`、`workflows/`、`handoff/`、`lab/`、`docs/`、别的因子的文件。
4. **工具问题已上报(全文 `synthesis.md` §5)**,最要紧的是 `dist` 门槛算在 EMA 之前的面板上(`sweep.py:129`),机械判死计数/占比类面板(`iso_F/H/Q/S` 0.00、`bk_*` 0.20)——**H11 就死在这里**;另有 `cs_bucket_rank` 错标、三个全 NaN 槽位、`rank_ic_train` 存绝对值三项。
5. **缺的算子已提(同 §5)**:`day_at_max_ratio / day_at_min_ratio`、`cs_bucket_zscore`、`cross_ema_clip`、`day_tail_ratio`。

## 7. 留出段(已用掉,**不可再读**)

`study.sh final` 已跑过一次并登记(`runs/.../ledger.json`、`S_final.json`)。五条 sign 全 −1、cov 全 0.967、dist ≥0.993。`f_orig` hl20 **−3.19% / −0.69**(LS +3.11);`f_known30` hl0 **+14.10% / +1.51**(`f_known30r` 逐项相同);两条叠加 +14.64% / +14.85%。逐年 `f_orig` 八年全负、`f_known30` 八年全正。**用户公布的 test 列被精确复现**(LS 3.108、多头腿毛 −1.38%)→「原样不可用」不是口径差异。
⚠ C3/C4 的读法:留出段没有固定半衰期表,+0.54 / +0.75pp 是「各自拟合 hl」下的;错配污染 ≲0.4pp、**符号不定**(以 `09_diagnosis.md` B1 为准,不是 `07_S_final.md` §4 的「上界」说法)。

## 8. 给接手者的提醒

- **先读 `synthesis.md`**(本轮全文判断,带 id 和数字),再读本文件;不要重算 §2 里已有的数字。
- **算子按函数定义理解,不按名字**:两处 `+1e-6` 写法相同、作用相反;「mag_gap」在它有方差的地方恰好不含幅度(常规区间齐次度 0,钉在 1.254 附近);「1m」不是时间结构(树里没有日轴算子);`abs_` 是装饰;`create_like(Ret, 0)` 是 int64、`create_like(q, 1e-06)` 是 float32。
- **本机 torch 与服务器内核的分位数位置不一致 → 以服务器为准**;`cross_*` 窗口网格里没有 20;「逐位相同」不能用来判等价(引擎非分块不变),用 rank 相关。
- **写新表达式的坑**:占比/计数类 day 算子(`day_zero_ratio`/`day_flat_ratio`/`day_pos_ratio`)只有约 241 档取值,**单独当因子过不了 dist**,外面必须套 `cross_*`(`cs_bucket_rank` 同理,套 `cross_mean(·,5)`);布尔张量不能直接相减,要先 `mul(less(...), create_like(x, 1.0))` 转 float。
- **报告层面不要改结论**:C1~C6 一条都没被否定,大表只是把「为什么」说清楚、把承重位置从推断变成实测。

## 研究日志(`notes/F106_erm_mag_gap_1m/journal.md`:14 条,其中研究员自己写的 9 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-05 11:09 [主研] 批量扫描 s1 的综合

152 个变体 + 23 段 × 14 时段的解剖读完,结论不变(分辨:多头腿不可用、相对成交额族无增量),但大表给了四条前几轮没有的硬事实:
1. 承重的是「分位数当分母 + 1e-6」一个节点:abl_G(A+1e-6 → A+A,结构不动只抹平塌缩)把公布的多空夏普 +2.82 变成 +0.06、ρo 变成 −0.26;abl_J/abl_V 把 LS 变成 −1.59/−1.14;abl_R 全 NaN。计数侧的同一个 1e-6 是装饰(abl_H ρo +0.98)。半衰期网格 hl0 [−67.2%, −19.51, −25.67] → hl20 [−6.9%, −2.15, +2.82] 说明 LS 全是线性 EMA 拖出来的,不是任何一天的信号(基准 k_known 的网格单调相反)。
2. abs_ 可证明是装饰:sub_U_neg / sub_N_neg 与 v_base 逐位相同(ρo +1.00);abl_N ≡ sub_X_add 逐行相同,两腿是严格镜像。计数可以整个删掉(only_H_R / sub_F_day_* ut +1.5%、valid +10.8%,全表非 overlay 最好)。
3. 解剖:23 个段里 22 个段内为负,唯一正数是 6.5% 的冻结盘口段(段内 +18.2%,该段自身等权 −67.4%/年,书还超配 +4.6pp);干净段 93.5% 段内 −6.9%。市值/成交额/价格五档全负 → 不是规模或流动性因子。科创板 −23.6% 最差。六年全负。
4. 新增对基准的理解:k_known 的多头腿是段间倾斜而非段内选股 —— 它在成交额五档段内是 −4.1/−5.3/−8.2/−5.2/+2.5,靠超配最低成交额档 +80.3pp 拿到 +15.4%。abl_M(ut +3.4%、六年全正、ρk 只 +0.06)在成交额五档段内五档全负,靠超配最低档 +26.2pp —— 同一个机制的更弱版本,低 ρk 不等于有增量。
下一步:第二批 37 条假设已写进 studies/F106_erm_mag_gap_1m/hypo.yaml(全部通过 hypo 检查),六个方向见 synthesis.md §5;另报四个工具问题(最要紧的是 dist 门槛算在 EMA 之前,机械判死计数/占比类面板,上一轮的 H11 就死在这里)。

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
- `sweep_s1`  10-05 10:35  155 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m sweep_s1`
- `anatomy_s1`  10-05 10:45  0 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m anatomy_s1`
- `x1`(自写脚本的输出)  10-04 12:30  exit 0  → `logs/F106_erm_mag_gap_1m_x1.log`
- `x2`(自写脚本的输出)  10-04 13:54  exit 0  → `logs/F106_erm_mag_gap_1m_x2.log`

## 已写的 notes(`notes/F106_erm_mag_gap_1m/`)

`01_expression.md`(2K)、`02_operators.md`(2K)、`03_decomposition.md`(3K)、`04_grammar.md`(1K)、`05_hypotheses.md`(21K)、`06_baseline.md`(3K)、`07_S0_baseline.md`(3K)、`07_S_final.md`(13K)、`07x_1_anatomy.md`(10K)、`07x_2_longonly.md`(23K)、`08_variants.md`(5K)、`09_diagnosis.md`(10K)、`10_distilled.md`(13K)、`11_risks.md`(6K)、`12_next.md`(4K)、`journal.md`(29K)、`state.md`(9K)、`synthesis.md`(14K)

## 自写的探针与分析脚本(`studies/F106_erm_mag_gap_1m/`)

- `probes.py`  10-04 12:13  Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.
- `x1_anatomy.py`  10-04 12:19  x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.
- `x2_longonly.py`  10-04 13:02  x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

## 结构化结果(`handoff/F106_erm_mag_gap_1m/results/`)

- `synthesis.json`

报告:`research/alpha_distillation/F106_erm_mag_gap_1m.md`(10-05 00:18 生成)
