# F112_scale_spow_masktop — 交接状态

_自动生成于 2026-10-04 13:38(`python scripts/recorder.py --brief F112_scale_spow_masktop` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #574(批次 B01_single_factors)
- 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- agent `study:F112_scale_spow_masktop`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F112_scale_spow_masktop#2`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `study:F112_scale_spow_masktop#3`(wf_759ef2d3-03f):失败,几乎没做事(不用看)
- agent `work:F112_scale_spow_masktop#0`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:11 → `handoff/F112_scale_spow_masktop/agents/work_R0_af0a6582c37fdb9a7.md`
- agent `lead:F112_scale_spow_masktop#1`(wf_c8c98127-70d):已返回结果,最后动作 10-04 13:28 → `handoff/F112_scale_spow_masktop/agents/lead_R1_a180641d3dc13020d.md`
- agent `work:F112_scale_spow_masktop#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)
- agent `work:F112_scale_spow_masktop#1`(wf_c8c98127-70d):失败,几乎没做事(不用看)
- agent `lead:F112_scale_spow_masktop#1`(wf_48864a04-f0a):还在跑(如果这就是你自己,不用看它的流水)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F112_scale_spow_masktop` 看服务器上的 tag,`./scripts/study.sh digest F112_scale_spow_masktop <tag>` 重看结果)。

## 研究现状(`notes/F112_scale_spow_masktop/state.md`,10-04 13:27 更新)—— **先读这个文件**

# 研究现状 · F112_scale_spow_masktop

> 第 1 轮主研(Opus 5)写于 2026-10-04。**每轮整个文件覆盖重写**。接手的人先读这一页,再读 `journal.md` 的最近条目。
> 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`

---

## 1. 一句话现状

建档(R0)完成、假设表(H1~H9)已定稿,**第 1 张实验工单 `orders/R1.md` 已下但还没有结果卡** ——
下一步是执行照 R1 跑 `S1_minimal`(10 个节点消融/窗口变体)和 `A1_channels`(5 节分析脚本),
回来之后主研裁决 H1/H2/H2b/H3/H4/H5/H6/H7,再决定 R2(大概率是 H8「相对已知家族有没有增量」)。

---

(…全文 9996 字符,读 `notes/F112_scale_spow_masktop/state.md`)

## 研究日志(`notes/F112_scale_spow_masktop/journal.md`:2 条,其中研究员自己写的 2 条)

最近的 12 条(完整的看文件):

### 2026-10-04 13:10 [执行] R0 建档完成:四份 notes(01/02/03/06)+ 结果卡写完,6 个算子逐个读源码确认

看到了什么:
- S0_baseline 复现 sign=-1,多头/多空口径都选 hl=20。决策口径 Lnet train+3.7%/valid+5.3%,Lshp +0.66/+0.91,
  cov=1.00、dist=0.98 过门槛;空头腿毛超额占长短合计(train)约 77%。与批内因子/控制变量/已知家族(交易信号
  口径和原始面板口径分别看)rank 相关都 ≤0.49,远低于 0.95 同族门槛。留出段确认未读(ledger.json 只有 9 条
  train/valid/utrain 记录,无 holdout)。
- 与用户表出入(特别注意里预告的那个):utrain LS Partura+2.59 vs 公布+2.58,Lgross+9.1% vs 公布+8.9%。
  源码读出两个候选机制——ts_scale 左补 NaN 的窗口边界、cs_mask_top_replace_mean_neg 用 ceil 取整 + 稳定
  排序打并列——都只是列出约定,没做逐日数值 diff 去验证。
- 读源码发现两处"和名字不一样":cs_mask_top_replace_mean_neg 因为 _neg 后缀,实际遮罩当天最低 10%而不是
  字面"mask_top"的最高;ts_scale 每只股票除以自己的滚动和(不是共享分母),一般不是横截面保序的。
- 工具缺口:day_kurt 内部 `_kurt` 的源码没读到(study.sh src 解析不了 `C._kurt` 这种模块属性调用,
  `_common_rank` 这种 import 别名调用能解析),用同库另两处 kurt 实现跨证代替,非源码逐字确认。
下一步(留给主研):中间节点 A~E 的真实数据经验分布、空头腿是否被封板票抬高(day_kurt 是峰度类算子,
playbook §6.6 点名的风险)、两个候选机制要不要做数值 diff 验证——都还没做,细节见结果卡
notes/F112_scale_spow_masktop/results/R0.md。

### 2026-10-04 13:27 [主研] 第 1 轮:把全树化成一阶展开(两通道+混合权重∝1/价位),定稿假设 H1~H9,下单 R1(S1_minimal 10 变体 + A1_channels 5 节脚本)

看到了什么(全部来自 R0 的 S0_baseline,本轮没跑实验):
- 最响的一个数:原始日频面板 rank 相关里 ctl_mom20 +0.49 是最高项;ctl_mom20 单变量中性化 R²=0.091(全部控制
  变量里最高),把多头腿毛超额 +8.6%→+1.8%、空头腿 +28.5%→+5.0%,单个控制变量就拿掉约八成。而 ctl_price
  (R² 0.010)、ctl_cap(0.010)、ctl_rev1(0.008)几乎不动它。=> 它是一个 20~30 日尺度的「相对自身」量,
  不是水平量、不是规模、不是 1 日反转。
- 固定半衰期表:Lnet 从 hl0 的 −30.4% 单调升到 hl20 的 +3.7%,hl=20 就是网格上限,还在升;rank IC 随 h 单调
  升到 h=20 的 +0.0248 仍未转头。=> 起作用的是慢分量,快分量是反向噪声;真实视野可能比 30 天长。
- 分位剖面 Q1 −28.6% vs Q10 +8.6%(3.3 倍不对称),空头腿占长短合计毛超额 77%。原式多头腿 +3.7%/+5.3%,
  而已知家族 known_stdamt_max9 自己是 +9.3%/+18.5% —— 原式只有它的 1/3~1/4。

判断(本轮的主要产出是「读懂这棵树」,写进 04_grammar.md 和 05_hypotheses.md):
- 这棵树没有门控、没有重复子树、没有跨股票滚动,所以「门控 vs 两信号」那套问题在这里不存在。全树唯一的跨日
  节点 ts_scale 是唯一的信号成形动作:把水平量变成「相对自身 30 日历史的偏离」。
- 一阶展开 ★:F_t − 1/30 ≈ (2/30)·[(A_t−Ā) + (B_t−B̄)]/C̄。因为 add 把「元」和「无量纲峰度」直接相加、
  而 ts_scale 的分母 ≈ 价位水平,**峰度通道的有效权重 ∝ 1/价位** —— 低价股上它是峰度因子、高价股上是价格反转。
  这是这棵树唯一的非平凡结构(H2b),别的因子上不存在,定为头号待测对象。
- signedpower 的二阶项:F − 2F′ ≈ (1/30)(−1 + e_t² − m2),是一个「今天偏离得异常大(不分方向)」的折叠通道。
  我本想用它解释「空头腿占 77%」,**用 2 万个模拟窗口自己把这条否掉了**:spearman(F,F′)=0.9945,一阶项压倒
  折叠项。所以 signedpower 预计在秩层面近似冗余(H3,可删),空头腿的集中要从 H5(封板票)和 H6(C 的偏离
  分布右偏)去找。这条弯路写进 05 和 state 第 4 节,后面的人别再走。

决定做什么:下工单 R1,两次运行。
- S1_minimal(10 变体):四个节点消融(noK/noP/noMask/noSpow)+ 最朴素两节点等价物(plain30)+ 窗口阶梯
  (w10 / x30 / x60 / x241)+ 最简×最长的组合(plain60)。窗口阶梯用 cross_scale 是因为 ts_scale 窗口池只到 50,
  而 cross_scale 源码与 ts_scale 逐字同公式(都是 rolling_windows + scale_last_ratio);s1_x30 就是这个等价性的
  一致性检查,**不一致则整条阶梯作废**,已在工单里要求告警。
- A1_channels(5 节脚本):§1 用 numpy 重建因子并与引擎面板自检(≥0.999 才算过)、§2 搭便车查公布值出入
  (ceil vs round、29 天热身)、§3 封板票(st.target(buyable=False))+ mask 质点与并列、§4 通道分解与按滞后
  30 日均价分桶(H2b 的正题)、§5 signedpower 二阶项。授权执行在跑不动时按「先删 §2、再删 §5」砍,保住 §4。

决定不做什么:
- 不追公布值出入超过 A1_§2 那一次搭便车(0.01 夏普量级,不值得花运行次数)。
- 不做 nt_* 变体(这棵树没有分钟级截面需求,CPU 上 4 分钟一条)。
- H8(相对已知家族有没有增量)**本轮不做**,排到 R2:要先知道 R1 选出哪个结构,再对那个结构做增量检验;
  而且它必须用 exec 脚本做(往 controls 里加东西会改变 all_controls 的 R²,与 S0 那一行不再可比)。

## 工单与结果卡(`notes/F112_scale_spow_masktop/orders/`、`notes/F112_scale_spow_masktop/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F112_scale_spow_masktop.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F112_scale_spow_masktop`)

- `S0_baseline`  10-04 11:57  1 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop S0_baseline`

## 已写的 notes(`notes/F112_scale_spow_masktop/`)

- `01_expression.md`  4726 字节  10-04 13:02
- `02_operators.md`  16004 字节  10-04 13:04
- `03_decomposition.md`  6529 字节  10-04 13:06
- `04_grammar.md`  6351 字节  10-04 13:20
- `05_hypotheses.md`  11710 字节  10-04 13:22
- `06_baseline.md`  11963 字节  10-04 13:09
- `journal.md`  5876 字节  10-04 13:27
- `state.md`  16298 字节  10-04 13:27

## 自写的探针与分析脚本(`studies/F112_scale_spow_masktop/`)

(无)

## 结构化结果(`handoff/F112_scale_spow_masktop/results/`)

(还没有)
