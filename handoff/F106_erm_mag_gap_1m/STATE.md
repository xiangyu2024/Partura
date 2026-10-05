# F106_erm_mag_gap_1m — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F106_erm_mag_gap_1m` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_1m(批次 B01_single_factors)
- 表达式:`sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-04 15:35)—— **不许再读**。候选在留出段上的数全在 `runs/F106_erm_mag_gap_1m/final.json`(`./scripts/study.sh digest F106_erm_mag_gap_1m final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F106_erm_mag_gap_1m#2`:已返回结果,最后动作 10-04 15:09 → `handoff/F106_erm_mag_gap_1m/agents/lead_R2_af2bdcab5a6f74b1f.md`
  - `work:F106_erm_mag_gap_1m#2`:失败,最后动作 10-04 15:41 → `handoff/F106_erm_mag_gap_1m/agents/work_R2_a8fb391808ec1a1fd.md`
  - `work:F106_erm_mag_gap_1m#2`:失败,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F106_erm_mag_gap_1m` 看服务器上的 tag,`./scripts/study.sh digest F106_erm_mag_gap_1m <tag>` 重看结果)。

## 研究现状(`notes/F106_erm_mag_gap_1m/state.md`,10-04 15:08 更新)—— **先读这个文件**

# F106_erm_mag_gap_1m — 研究现状(主研第 2 轮覆盖重写,2026-10-04)

> **这一页每轮整个覆盖重写。** 这一版由**第 2 轮**主研(Opus 5)写。
>
> 第 1 轮发生了什么:第一个主研裁决完 H1~H9、提出 H10~H12、下了工单 R1;执行跑到一半被额度打断;
> 第二个主研按规矩**不另开工单**,把 R1 原样交回,同时做了三件事(核对数字、排雷、**把 R1 的读法事前登记死**);
> 换上来的执行把 R1 收尾,结果卡 `results/R1.md` 和事实记录 `07x_2_longonly.md` 都写完了。
>
> 这一轮(第 2 轮)我做的事:
> 1. **把 R1 的数字自己对着 `logs/F106_erm_mag_gap_1m_x2.log`(第 16~157 行)核对一遍** —— 结果卡准确,没有张冠李戴。
> 2. **照事前登记的判据裁决 H10 / H11 / H12**(写进 `05_hypotheses.md` 的「裁决(主研第 2 轮)」一节)。
> 3. **算出排除性增量的量化天花板**(新贡献,把四个格子都解释到 25% 以内,见 §2.9)—— 这是整条研究解释力最强的一块。
> 4. **决定进入 (b):读留出段。** 事前登记写进 `10_distilled.md`「读留出段之前」,工单 `orders/R2.md`(kind: final)已下。
>
> 前面两位研究员留下的 `01`~`06`、`07x_1_anatomy.md`、`07x_2_longonly.md` 和两个脚本是**可靠、含量很高**的成果,全部采信。

---

## 1. 一句话现状

**事实全部查清,三条新假设全部裁决完毕,结论是否定的:这条因子对纯多头用户不可用,相对已知家族也没有可交易的增量。
下一步是读留出段(工单 R2,kind: final,事前登记已写死),然后成文。**

这棵树不是「日内尾部形状不对称」(那部分**没有**可交易信号),而是**「最近有没有封过涨停板、那几分钟跳了多大」的一年期记忆**。
在用户的纯多头选拔口径下:

- **原样不可用**:多头腿净超额在**每一个**半衰期、train 和 valid、毛和净**全都是负的**;
  「原式 + 多头最优半衰期」就是用户表里公布的那一行本身(hlL = hlS = 20),**没有「延长半衰期」这条免费改进**。
- **没有升华候选**:这棵树派生的所有连续构造,多头腿 train+valid 同时为正的**一个都没有**。
- **作为「排除清单」也不值钱**(R1 的裁决):方向对、机制看得见,但 **valid 上只剩 +0.4~+0.5 个点**(噪声 ±3 个点);
  天花板是结构性的 —— **已知家族本来就在躲这些票**(持有被标记票的频率只有全市场的 24%~64%)。
- **和书更糟**:`rank(known) + w·rank(F106)` 24 行没有一行好于已知家族自己,随权重单调下降。

**结论类型:分辨。** 不是提纯,不是升华。这是 playbook §0 明文允许的合格结论。

**下一步(本轮已下单):工单 R2 = `study.sh final`,5 条候选(`f_orig` / `f_known30` / `f_known30r` / `f_excl_blown15` / `f_excl_lu15`),
判据 C1~C6 已写进 `10_distilled.md`。** 读完之后第 3 轮成文((c)):`09_diagnosis.md`、`10_distilled.md` 读后一节、
`11_risks.md`、`12_next.md`、`08_variants.md`,再下 writeup 工单。

---

(…全文 24998 字符,读 `notes/F106_erm_mag_gap_1m/state.md`)

## 研究日志(`notes/F106_erm_mag_gap_1m/journal.md`:10 条,其中研究员自己写的 5 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 14:21 [auto] x2 跑完(exit 0);重看结果:logs/F106_erm_mag_gap_1m_x2.log

### 2026-10-04 14:33 [执行] R1:x2 已拉回读全文,结果卡与 07x_2_longonly.md 写完

看到了什么(全部 utrain,数字见 results/R1.md 与 07x_2_longonly.md):
- x2 此前已在服务器跑完(exit 0),本轮只 wait 拉回 logs/F106_erm_mag_gap_1m_x2.log(157 行)读全文,没有重跑脚本/selftest;
  g_max30/g_limitup30 两个 control 核对后都存在,没有触发自造等价量分支;脚本无报错。
- 第1~2节(H10):9 个 flag × 2 family × 2 split 的已知家族多头十分位构成与剔除前后 dLnet 已抄全;
  "blown day within 20d"/"limit-up close within 20d"(预登记里"有动机"的两条)四格里各有一格不达标——
  known9/valid 的 share 是 0.016(<2%门槛),limit-up close within 20d 在 known9/valid 的 dLnet 是 -0.04。
- 第3节:rank(known)+w·F106 的 24 行里,没有一行 Lnet 高于已知家族自身基准,随 w 增大单调下降。
- 第4节(H12):F106 对 g_max30/g_limitup30/EMA20(limit-up)/EMA20(blown)/all four 中性化,残差 Lnet 5 行全部仍为负
  (train -5.8%~-8.6%,valid -3.4%~-7.0%);折叠量对这组变量的 R²(0.042~0.444)比带符号信号的 R²(0.017~0.164)高 2~3 倍。
- 第5节(H11):9 行里 6 行(两类计数×10/20/40日)Lnet 两段同正,但这 6 行就是主研点名的"并列书"(拟合方向-、多头端是
  计数=0的并列);唯三条连续构造(log(1+|X|)、R+L、log(1+R+L))没有一条两段同正。
- 异常:listed<250d 这一flag两段符号相反、量级一个数量级(known30 train -127.0%→valid+14.8%);其余无 NaN/脚本异常。
下一步:判据已在 05_hypotheses.md 预登记,留给下一轮主研按(a)(b)(c)(d)逐条核对后裁决 H10/H11/H12,决定是否需要 R2。

### 2026-10-04 15:08 [主研] 第 2 轮:H10 被否定/H11 被支持但不产生候选/H12 改写;算出排除增量的天花板 → 不再做实验,直接读留出段(工单 R2 kind: final)

看到了什么(R1 的 x2 五节;我自己对着 logs/F106_erm_mag_gap_1m_x2.log 第 16~157 行核对过,结果卡准确):
- H10(排除性增量)按**事前登记的四条判据被否定**:(a)(b) 过,(c)(d) 不过。
  塌缩标记 ΔLnet 四格 +1.59/+0.52/+1.60/+0.40 —— train 有一点六,**valid 只剩 0.4~0.5 个点**,噪声是 ±3 个点;
  share 在 known9/valid 只有 0.016(低于 2% 门槛,全表 36 格唯一一格)。机制那半条是过的(被标记票次日超额四格全部远差于未标记票)。
- **这一轮最重要的新结果(我自己算的,不在结果卡里):天花板可以预测出来。**
  ΔLnet ≈ (被标记票占多头十分位的比例) × (标记与未标记的超额之差) = 2.0 / 0.70 / 1.93 / 0.57,
  与实测 +1.59/+0.52/+1.60/+0.40 **四格全部吻合到 25% 以内**。
  而 share 之所以低,是因为**已知家族本来就在躲这些票**:被标记票占全市场 8.0%/6.7%,
  占 known30 多头十分位只有 5.1%/2.2%、known9 只有 4.1%/1.6% → 相对持有频率只有 24%~64%(涨停标记 15%~37%)。
  → **不是 F106 的「不要买」清单不准,是已知家族本来就没买那些票。这张清单是多余的。** 这是整条研究解释力最强的一句话。
- H11(记忆太长)**被支持**:计数构造 rank IC 是 EMA-20(X) 的 1.7~4.8 倍、两段全优;叠加里 20 日窗口四格全面优于 60 日。
  **但它不产生候选**:优势只出现在取值几乎全是 0 的计数构造(过不了 dist ≥ 0.5),三条连续构造的 rank IC 反而低于原式。
- H12 **改写**:字面版(完全被朴素涨停替代)被否定 —— 残差 rank IC 保住 0.55×/0.26×(EMA20 涨停)、0.68×/0.79×(all four),
  折叠量 R² 0.444 不是 1.0。**但残差 Lnet 五行全负**(train −5.8%~−8.6%、valid −3.4%~−
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:29 [auto] ⚠ 读留出段:final S_final,阶段 S_final(留出段只能读这一次;候选与判据应当已经写在 10_distilled.md 里)

### 2026-10-04 15:35 [auto] S_final 跑完(exit 0);重看结果:./scripts/study.sh digest F106_erm_mag_gap_1m S_final

## 工单与结果卡(`notes/F106_erm_mag_gap_1m/orders/`、`notes/F106_erm_mag_gap_1m/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 **还没有(待执行)**

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

`01_expression.md`(1K)、`02_operators.md`(2K)、`03_decomposition.md`(3K)、`04_grammar.md`(1K)、`05_hypotheses.md`(19K)、`06_baseline.md`(3K)、`07x_1_anatomy.md`(10K)、`07x_2_longonly.md`(23K)、`10_distilled.md`(7K)、`journal.md`(16K)、`state.md`(40K)

## 自写的探针与分析脚本(`studies/F106_erm_mag_gap_1m/`)

- `probes.py`  10-04 12:13  Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.
- `x1_anatomy.py`  10-04 12:19  x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.
- `x2_longonly.py`  10-04 13:02  x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

## 结构化结果(`handoff/F106_erm_mag_gap_1m/results/`)

(还没有)
