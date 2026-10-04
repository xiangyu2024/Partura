# F106_erm_mag_gap_1m — 交接状态

_自动生成于 2026-10-04 13:38(`python scripts/recorder.py --brief F106_erm_mag_gap_1m` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

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
- agent `work:F106_erm_mag_gap_1m#1`(wf_3cafb924-05e):还在跑(如果这就是你自己,不用看它的流水)
- agent `lead:F106_erm_mag_gap_1m#1`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F106_erm_mag_gap_1m` 看服务器上的 tag,`./scripts/study.sh digest F106_erm_mag_gap_1m <tag>` 重看结果)。

## 研究现状(`notes/F106_erm_mag_gap_1m/state.md`,10-04 13:20 更新)—— **先读这个文件**

# F106_erm_mag_gap_1m — 研究现状(主研第 1 轮写,2026-10-04)

> 这一页由**主研**(Opus 5,工作流 `lead:F106_erm_mag_gap_1m#1`)覆盖重写,替换了之前那份 `scripts/autostate.py` 自动汇编的版本。
> 上一位研究员(Opus 5.5)在写下判断之前被换下,但它留下的 `01`~`06`、`07x_1_anatomy.md` 和两个脚本是**可靠且含量很高**的工作成果:
> 我逐条核对了它们的数字,全部采信,下面「中间结果」的每条都带出处。
> 这一轮我做的事是:**裁决假设、补三条新假设、下第一张工单**。还没有新的实验结果 —— R1 的结果卡还没有。

---

## 1. 一句话现状

**事实基本查清了,但决定性的那一步还没做。**
这棵树已经被解剖到底:它不是「日内尾部形状不对称」(那部分没有可交易信号),而是**「最近有没有封过涨停板、以及那几分钟跳了多大」的一年期记忆**;
它在用户的纯多头选拔口径下**原样不可用**(多头腿净超额在**每一个**半衰期、train 和 valid、毛和净**全都是负的**),
而且「原式 + 多头最优半衰期」就是公布的那一行本身(两种口径都选到 hl 20),**没有这条免费改进**。

**下一步(已写成工单 R1)**:跑上一位研究员写好但没来得及跑的 `studies/F106_erm_mag_gap_1m/x2_longonly.py`,
回答整条研究唯一还没回答的问题 —— **对只能做多的用户,它相对已知家族(成交额水平族)有没有增量**,
具体是三件事:(a) 作为**排除性叠加**(把被标记的票从已知家族的多头十分位里剔除)值不值钱;
(b) 换成**显式的短记忆**(事件效应只有 20 天,EMA-20 却记一年)是不是更好;
(c) 它会不会被一个更朴素的**「近期涨停」**变量完全替代。R1 **不用服务器**(纯 numpy 分析,0 次服务器运行)。

---

(…全文 18808 字符,读 `notes/F106_erm_mag_gap_1m/state.md`)

## 研究日志(`notes/F106_erm_mag_gap_1m/journal.md`:3 条,其中研究员自己写的 1 条)

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

## 已写的 notes(`notes/F106_erm_mag_gap_1m/`)

- `01_expression.md`  1323 字节  10-04 12:15
- `02_operators.md`  2769 字节  10-04 12:15
- `03_decomposition.md`  3249 字节  10-04 12:15
- `04_grammar.md`  1562 字节  10-04 12:15
- `05_hypotheses.md`  8370 字节  10-04 13:21
- `06_baseline.md`  3247 字节  10-04 12:20
- `07x_1_anatomy.md`  10386 字节  10-04 12:41
- `journal.md`  3735 字节  10-04 13:26
- `state.md`  33038 字节  10-04 13:20

## 自写的探针与分析脚本(`studies/F106_erm_mag_gap_1m/`)

- `probes.py`  10-04 12:13  Probes this tree needs:  ES/VaR of the right tail of minute returns  minus  ES/VaR of the left tail.
- `x1_anatomy.py`  10-04 12:19  x1 -- what the ES/VaR gap tree reads on REAL data, and who sits at the ends of the traded signal.
- `x2_longonly.py`  10-04 13:02  x2 -- for a LONG-ONLY user: does this factor add anything to the known amount-level family?

## 结构化结果(`handoff/F106_erm_mag_gap_1m/results/`)

(还没有)
