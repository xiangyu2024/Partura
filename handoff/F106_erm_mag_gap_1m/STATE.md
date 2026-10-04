# F106_erm_mag_gap_1m — 交接状态

_自动生成于 2026-10-04 14:21(`python scripts/recorder.py --brief F106_erm_mag_gap_1m` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 erm_mag_gap_1m(批次 B01_single_factors)
- 表达式:`sub(div(div(day_sum(select_where(is_gt(Ret, day_quantile(Ret, 0.95)), Ret, create_like(Ret, 0))), add(day_sum(is_gt(Ret, day_quantile(Ret, 0.95))), create_like(day_quantile(Ret, 0.95), 1e-06))), add(day_quantile(Ret, 0.95), create_like(day_quantile(Ret, 0.95), 1e-06))), div(div(day_sum(select_where(is_lt(Ret, day_quantile(Ret, 0.05)), abs_(Ret), create_like(Ret, 0))), add(day_sum(is_lt(Ret, day_quantile(Ret, 0.05))), create_like(day_quantile(Ret, 0.05), 1e-06))), add(abs_(day_quantile(Ret, 0.05)), create_like(day_quantile(Ret, 0.05), 1e-06))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F106_erm_mag_gap_1m`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F106_erm_mag_gap_1m#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F106_erm_mag_gap_1m#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F106_erm_mag_gap_1m`(wf_08351f46-81b):中断,最后动作 10-04 13:10 → `handoff/F106_erm_mag_gap_1m/agents/study_ad228efb5487f607c.md`
- agent `lead:F106_erm_mag_gap_1m#1`(wf_3cafb924-05e):已返回结果,最后动作 10-04 13:23 → `handoff/F106_erm_mag_gap_1m/agents/lead_R1_af04d35244a5aa63f.md`
- agent `work:F106_erm_mag_gap_1m#1`(wf_3cafb924-05e):中断,最后动作 10-04 13:36 → `handoff/F106_erm_mag_gap_1m/agents/work_R1_aee5280042fe98aa3.md`
- agent `lead:F106_erm_mag_gap_1m#1`(wf_48864a04-f0a):已返回结果,最后动作 10-04 13:57 → `handoff/F106_erm_mag_gap_1m/agents/lead_R1_a069d7be57c2c2603.md`
- agent `work:F106_erm_mag_gap_1m#1`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F106_erm_mag_gap_1m` 看服务器上的 tag,`./scripts/study.sh digest F106_erm_mag_gap_1m <tag>` 重看结果)。

## 研究现状(`notes/F106_erm_mag_gap_1m/state.md`,10-04 13:56 更新)—— **先读这个文件**

# F106_erm_mag_gap_1m — 研究现状(主研第 1 轮 · 第二个主研 agent 覆盖重写,2026-10-04)

> **这一页每轮整个覆盖重写。** 这一版由第 1 轮的**第二个**主研 agent(Opus 5,工作流 `lead:F106_erm_mag_gap_1m#1` / wf_48864a04-f0a)写。
>
> 为什么第 1 轮有两个主研 agent:上一个主研把假设裁决完、下了工单 R1,**执行 agent 跑到一半被额度打断**
> (它起的 x2 job 在服务器上跑完了、**exit 0**,但日志没拉回、结果卡没写;详见 §8)。
> 按工作流的规矩,**最新的工单还没有结果卡时不另开工单** —— 所以我这一轮**不下新工单**,
> 把 R1 原样交回给执行接着做,我自己做的是三件可以不等结果就做的事:
>
> 1. **把上一位主研采信的数字自己核对一遍**(不是转抄):S0 的每个数都对着 `runs/F106_erm_mag_gap_1m/S0_baseline.json` 验过;
>    `day_quantile` / `is_gt` 的语义自己用 `study.sh src` 从服务器内核读过。全部对得上,**结论不变**。
> 2. **把两颗雷排掉**:(i) 老版 §8 警告的 `st.control("g_max30")` 缺失是**假警报**;(ii) 「延长半衰期」这条路**由口径约定关死**,不是靠 argmax 关的。
> 3. **把 R1 的读法事前登记死**(写进 `05_hypotheses.md` 末尾的「R1 的读法预登记」)——
>    我读懂了 `x2_longonly.py` 的源码,发现它的输出里**有两类数字不能按字面读**(叠加行的 `LS`、第 5 节计数构造的多头腿),
>    而且第 2 节是 **18 个(标记, 家族)组合**的多重比较。不事前写死判据,下一轮一定会挑一行好看的讲故事。
>
> 上一位研究员(Opus 5.5)留下的 `01`~`06`、`07x_1_anatomy.md` 和两个脚本是**可靠、含量很高**的成果,全部采信并接着用。

---

## 1. 一句话现状

**事实已经查清,原样不可用已经坐实;唯一剩下的问题(对纯多头有没有排除性增量)正在服务器上算 —— 结果卡还没回来。**

这棵树不是「日内尾部形状不对称」(那部分**没有**可交易信号),而是**「最近有没有封过涨停板、那几分钟跳了多大」的一年期记忆**。
在用户的纯多头选拔口径下它**原样不可用**:多头腿净超额在**每一个**半衰期、train 和 valid、毛和净**全都是负的**。
「原式 + 多头最优半衰期」就是用户表里公布的那一行本身(hlL = hlS = 20),**没有「延长半衰期」这条免费改进**。

**下一步:执行把工单 R1 收尾。** R1 的内容是把上一位研究员写好的 `studies/F106_erm_mag_gap_1m/x2_longonly.py` 跑出来
(**0 次服务器阶段运行**,纯 numpy 分析),裁决三条假设:H10 排除性增量 / H11 记忆长度错配 / H12 被朴素的「近期涨停」替代。
**那个 job 已经跑完了(`x2` exit 0,2026-10-05_04:54:27 服务器时间)**,但**日志还没拉回本地、结果卡还没写** ——
执行要做的是 `wait`(立刻返回、顺手拉日志)然后**读日志全文**,再写 `07x_2_longonly.md` 和 `results/R1.md`。细节见 §8。

---

(…全文 24757 字符,读 `notes/F106_erm_mag_gap_1m/state.md`)

## 研究日志(`notes/F106_erm_mag_gap_1m/journal.md`:6 条,其中研究员自己写的 3 条)

最近的 12 条(完整的看文件):

### 2026-10-04 12:40 [auto] 启动 run S1_regime:阶段 S1_regime

### 2026-10-04 13:22 [主研] 第 1 轮:事实已查清(封板记忆,非尾部形状),原样不可用;唯一剩下的问题是相对已知家族的排除性增量 → 工单 R1 跑现成的 x2

看到了什么(全部来自上一位研究员留下的 S0_baseline 与 tag x1,我逐条核对后采信):
- 复现成功(多空 +2.91、多头腿毛 −4.2%)。两种口径选到同一个半衰期(hlL = hlS = 20)
  → **「原式 + 多头最优半衰期」就是公布的那一行,没有「延长半衰期」这条免费改进。**
- 多头腿在每一个半衰期下都是负的(hl 0/2/5/10/20 → −67.2/−32.5/−18.5/−10.6/−6.9%),毛超额也是负的
  → 不是成本问题。分位剖面是倒 U(train Q1 −28.4%、Q10 −5.3%),两端都负。
- 它是什么:塌缩日(上涨分钟 ≤ 12 个 → 分位数为 0 → ×10⁶)就是封板日,涨停收盘富集 50 倍;
  不是低价/不活跃(<3 元占 0.2%),也不是成交额/规模/波动/换手暴露(折叠量对五变量 R² 仅 0.068)。
- 公布的多空夏普有一半以上(train)是「次日开盘买不进」的票造成的(2.82 → 0.42);多头腿不受影响,仍为负。

判断(裁决已写进 05_hypotheses.md 的「裁决」一节和 state.md §4):
- H1、H3、H6、H8、H9 被支持;H2、H4、H5 被否定 —— 这几条都已确立,不要再查。
- **H7 要改写,而且方向反了**:事件时间说封板后的跑输只持续约 20 天、40 天归零,EMA-20 却把 10⁴ 的读数记约一年;
  标记类构造的多头最优半衰期是 hl 0~1。所以问题是**记忆太长**,不是太短 → 改写为 H11。
- 意外(也是最重要的发现):**朴素的日线涨停标记与原式秩相关只有 0.06,但 rank IC 0.0424/0.0319 是原式的 6 倍**,
  而涨停日数量是塌缩涨停日的 4 倍多,没塌缩的涨停日事后同样跑输 → 原式只抓到涨停日里「封得死」的五分之一。
  这让「它可能被一个更朴素的变量完全替代」成为最该杀的假设 → 新提 H12。
- 新提 H10:H6 之后这条因子唯一剩下的用途是**排除项**(对已知家族多头书剔除被标记的票)。
  间接证据:塌缩 0/1 标记在 hl 1 下多头腿 +2.7%/+3.5%、夏普 +0.42/+0.44,train 和 valid 同时为正 ——
  但那是并列按代码取的书、过不了 dist 门槛,不能单独交易,必须以叠加形式检验。

决定:下工单 R1(kind: experiment,**0 次服务器运行**)。
上一位研究员已经为此写好 studies/.../x2_longonly.py(211 行,带 selftest)却没来得及跑 —— 不另起炉灶,就把它跑出来,
它的五节正好裁决 H10 / H11 / H12。提醒执行:脚本用到 st.control("g_max30") / ("g_limitup30"),对不上要自己算等价量并写清定义。

决定不做的事:
- **不重跑 S1_regime**(10 变体,上次 exit 97 内存守卫让路、无结果)。它要问的 x1 已经在 numpy 里全答了,
  在「多头腿全负」已成定局时,服务器运行要留给真正的升华候选(R2)。
- 不再找「X 的单调变换」:常规/排序/clip/单侧/折叠都扫过了,多头腿 train+valid 同时为正的一个都没有,继续加变体是在挖噪声。
- 不去优化空头腿和多空夏普(用户做纯多头,且那个数字一半以上是买不进的票造成的)。

### 2026-10-04 13:26 [auto] 启动 exec x2:studies/F106_erm_mag_gap_1m/x2_longonly.py

### 2026-10-04 13:54 [主研] 第 1 轮(第二个主研 agent 接手):R1 没有结果卡 → 不另开工单,原样交回;这一轮做的是核对数字、排雷、把 R1 的读法事前登记死

上一个执行 agent 被额度打断(它在 `study.sh wait` 那一步被打断),**R1 的结果卡没有** ——
按规矩「最新的工单还没有结果卡时不另开工单」,所以这一轮我**不下新工单**,把 R1 原样交回执行接着做。
x2 的 job **还在服务器上跑着**(`634403.pt_F106_x2`,`list` 里是「还在跑 / 没有退出行」),执行要做的只是接着 `wait`,**不要起第二个**。

既然等不到结果,我把三件不依赖结果的事做了:

1. **自己核对,不转抄。**
   - S0 的每个数对着 `runs/F106_erm_mag_gap_1m/S0_baseline.json` 验过:sign −1.0、distinct 0.9933、**hl_long = hl_ls = 20.0**、
     train 多头腿净超额 −6.91% / 夏普 −2.15 / 毛 −5.09% / 换手 2.40% / 多空 +2.82 / 空头毛 +27.85%,valid −3.16% / −1.23 / −1.81% / +3.24 / +22.37%;
     半衰期 sweep(0→20)多头腿 −67.2/−45.5/−32.5/−25.8/−18.5/−10.6/−6.9%。**全部对得上,上一位主研的结论不变。**
   - `day_quantile` / `is_gt` 的语义用 `study.sh src` 从服务器内核读过:前者 = `torch.nanquantile`(线性插值,所以 0.95×240 = 228.0 恰是顺序统计量
     → 「上涨分钟 ≤ 12 个」这个阈值是对的);后者 = `(x > value).int()`(严格、NaN 为假、输出 int → 没有 NaN 传播 → cov 1.00)。
   - `ledger.json` 的 summary 只有 train/valid/utrain → **留出段 0 次读取,机会完整留着**。

2. **排掉两颗雷。**
   - 老版 state.md §8 警告「`st.control("g_max30")` / `("g_limitup30")` 可能不存在,执行要自己造等价量」—— **这是假警报**。
     `Study.control()`(partura/study_tools.py:82)先查 `external_controls` 再查 `{**controls, **gates}`,
     而这两个名字就定义在本因子配置的 `gates:` 第 50–51 行,算子和窗口 30 也都合法。已写进工单 R1 的补注,省掉执行一轮返工。
   - **「延长半衰期」这条路是由口径约定关死的,不是靠 argmax 关的**:半衰期网格 {0,1,2,3,5,10,20} 写在 playbook §1(与用户 pick_single_factors.py 一致),
     `grep halflives configs/*.yaml` 一个都搜不到 —— 没有配置项可调。**不要为这条因子扩网格**(扩了和用户表不可比 = 改了口径)。
     网格上界 hl 20 两条腿还在改善,但每翻一倍半衰期负值大致减半,而 hl→∞ 的极限是「从没封过板的股票」= 中间六档 = 超额 ≈ 0,
     扣掉成本还是负 → **翻不成正的 alpha**。这一条记作「合理但未坐实」(外推论证),不为它花服务器运行。

3. **把 R1 的读法事前登记死**(新写进 `05_hypotheses.md` 末尾「R1 的读法预登记」,state.md §4 末尾有摘要)。
   我读了 `x2_longonly.py` 的源码,发现它的输出有三处按字面读会读错、而且第 2 节是多重比较:
   - 第 2 节是 **9 张标记 × 2 个已知家族 = 18 个组合** × 2 段 = 36 行;playbook §4.6 的噪声是 ±3 个点 → 「两段同时变好」靠运气就会出现。
     所以 **H10 要四条全中**:(a) 起作用的必须是事前有动机的短记忆事件标记(近 20 日塌缩/涨停),不能是 `F106 signal decile 1`、
     `|signal| >= 5`(EMA-20 读数的换一种写法)或 `listed < 250d`(新股过滤);(b) ΔLnet > 0 在 train/valid × known30/known9 四格全中;
     (c) 被标记票占多头十分位 ≥ 2% 且其次日超额两段都差于未标记票(机制看得见);(d) ΔLnet ≥ 1 个点两段成立、四格中位数 ≥ 1 个点。
     只有 `listed < 250d` 赢 → 诚实的结论是「值钱的是排除新股,不是这条因子」。
   - **叠加行的 `LS` / `short` 不可读**:`push_down` 把被标记票压到当天所有票之下 = 推进了空头十分位,叠加后的空头腿是「做空被标记的票」。
     只读 `Lnet / Lshp / Lgross / LTO`。好消息:叠加不重拟合方向和半衰期,`Lnet` 已扣 15bp/边 → ΔLnet 可以直接读。
   - **第 5 节三条计数构造的多头腿是假的**:「近 10/20/40 日计数」绝大多数格子为 0、方向为 −,多头端就是「计数 0」那一大片并列,
     按股票代码顺序切 10% —— 和 0/1 标记同一个毛病。→ **H11 只认 rank IC**(要两段都优于 EMA-20(X) 的 0.0165 / 0.0086)和叠加表现。
   - **H12 要看完整定义那一版**:`g_limitup30`(配置 gate)只抓 ≥9.5% 的板、漏 5% 的 ST 板;`EMA20(limit-up close flag)` 才是 5/10/20% 的完整定义。
     主证据看后者和 `all four` 的残差;R² 次要,要配合「折叠量对这几组的 R²」看(playbook §6.5)。

决定不做的事(沿用并补充):不重跑 S1_regime(x1 已在 numpy 里答过它要问的事,服务器运行留给 R2);
不再找 X 的单调变换;不优化空头腿/多空夏普;**不扩半衰期网格、不量 hl 40/60**;不单独验 H9;现在**不写 10_distilled.md**(候选集合要等 R1/R2)。

### 2026-10-04 13:56 [主研] 更正上一条:x2 在我写完那条日志之后就跑完了(exit 0),执行要做的是拉回日志读全文,不是等

上一条日志里我写「x2 还在服务器上跑着」—— 13:55 复查时它**已经完成**:
`list` 显示 `x2 [partura exit 0 2026-10-05_04:54:27]`,「正在跑的」是「(无)」。

对执行的指示因此变成:
- `./scripts/study.sh wait F106_erm_mag_gap_1m x2` 仍然是要跑的那条命令 —— 对已结束的 job 它**立刻**返回,
  作用是把日志拉回 `logs/F106_erm_mag_gap_1m_x2.log`(本地现在还没有这个文件)并同步 JSON。
- ⚠️ 但 `wait` 只把日志**最后 200 行**打到屏幕上(scripts/study.sh:128,exec job 没有 JSON 就走 tail -200),
  而 x2 的输出远超 200 行(第 1 节 36 行、第 2 节 36 行,后面还有三节)
  → **必须读 `logs/F106_erm_mag_gap_1m_x2.log` 全文**,否则第 1~2 节(H10 的全部证据)会整段漏掉。
- **不要重跑 x2、不要重跑 selftest。** 只有 exit 97 才需要重跑。

工单 R1 的补注和 state.md §1、§8 都已经按这个事实改过了。
我**没有去读** x2 的输出:判据已经事前登记在 05_hypotheses.md 末尾,
结果卡该由执行按事实写、下一轮主研照登记好的判据裁决 —— 我先偷看就把预登记的意义毁掉了。

### 2026-10-04 14:21 [auto] x2 跑完(exit 0);重看结果:logs/F106_erm_mag_gap_1m_x2.log

## 工单与结果卡(`notes/F106_erm_mag_gap_1m/orders/`、`notes/F106_erm_mag_gap_1m/results/`)

- R1:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F106_erm_mag_gap_1m.yaml`)

- 标题:分钟收益右尾 ES/VaR 减左尾 ES/VaR;分母 +1e-6 在「上涨(下跌)分钟不足 5%」的日子塌掉,截面两端由这些日子决定
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_regime**(10 个变体):公布的多空夏普(和空头腿)是「塌缩日 = 封板事件」做出来的,还是「尾部形状不对称」做出来的?差的符号有没有信息?
  a_right、a_left、a_sum、a_abs、a_regular、a_eps3、a_flag、a_rankfirst、a_lockshare、a_limitup

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F106_erm_mag_gap_1m`)

- `S0_baseline`  10-04 11:50  1 个变体  → `./scripts/study.sh digest F106_erm_mag_gap_1m S0_baseline`
- `x1`(自写脚本的输出)  10-04 12:30  exit 0  → `logs/F106_erm_mag_gap_1m_x1.log`
- `x2`(自写脚本的输出)  10-04 13:54  exit 0  → `logs/F106_erm_mag_gap_1m_x2.log`

## 已写的 notes(`notes/F106_erm_mag_gap_1m/`)

- `01_expression.md`  1323 字节  10-04 12:15
- `02_operators.md`  2769 字节  10-04 12:15
- `03_decomposition.md`  3249 字节  10-04 12:15
- `04_grammar.md`  1562 字节  10-04 12:15
- `05_hypotheses.md`  12407 字节  10-04 13:44
- `06_baseline.md`  3247 字节  10-04 12:20
- `07x_1_anatomy.md`  10386 字节  10-04 12:41
- `journal.md`  10243 字节  10-04 14:21
- `state.md`  42961 字节  10-04 13:56

## 自写的探针与分析脚本(`studies/F106_erm_mag_gap_1m/`)

- `probes.py`  10-04 12:13  Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.
- `x1_anatomy.py`  10-04 12:19  x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.
- `x2_longonly.py`  10-04 13:02  x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

## 结构化结果(`handoff/F106_erm_mag_gap_1m/results/`)

(还没有)
