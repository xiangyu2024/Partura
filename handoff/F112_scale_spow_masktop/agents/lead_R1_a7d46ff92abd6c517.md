# lead:F112_scale_spow_masktop#1 — agent a7d46ff92abd6c517(工作流 wf_48864a04-f0a)

- 状态:**还在跑**;开始 10-04 13:38,最后一次动作 10-04 13:42;工具调用 12 次
- 这是从 agent 的对话记录里**自动抽出来的动作流水**(命令、输出、写了哪些文件)。agent 的推理不在记录里 ——
  它的判断要看 `notes/F112_scale_spow_masktop/journal.md` 和各 notes 文件。输出过长的地方截了中间。

## 动作流水

**10-04 13:38 · agent 的话**

I'll start by getting the full picture of this factor's research state.

**10-04 13:38 · Bash** — Get overview of factor research state

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F112_scale_spow_masktop 2>&1 | head -200
```

```
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
```

**10-04 13:38 · Bash** — List factor notes directory

```bash
cd /Users/wxy/Desktop/Partura && ls -la notes/F112_scale_spow_masktop/ 2>&1; echo "--- orders ---"; ls -la notes/F112_scale_spow_masktop/orders/ 2>&1; echo "--- results ---"; ls -la notes/F112_scale_spow_masktop/results/ 2>&1
```

```
total 176
drwxr-xr-x@ 12 wxy  staff    384 Oct  4 13:27 .
drwxr-xr-x@ 19 wxy  staff    608 Oct  4 13:07 ..
-rw-r--r--@  1 wxy  staff   4726 Oct  4 13:02 01_expression.md
-rw-r--r--@  1 wxy  staff  16004 Oct  4 13:04 02_operators.md
-rw-r--r--@  1 wxy  staff   6529 Oct  4 13:06 03_decomposition.md
-rw-r--r--@  1 wxy  staff   6351 Oct  4 13:20 04_grammar.md
-rw-r--r--@  1 wxy  staff  11710 Oct  4 13:22 05_hypotheses.md
-rw-r--r--@  1 wxy  staff  11963 Oct  4 13:09 06_baseline.md
-rw-r--r--@  1 wxy  staff   5876 Oct  4 13:27 journal.md
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:25 orders
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:10 results
-rw-r--r--@  1 wxy  staff  16298 Oct  4 13:27 state.md
--- orders ---
total 32
drwxr-xr-x@  3 wxy  staff     96 Oct  4 13:25 .
drwxr-xr-x@ 12 wxy  staff    384 Oct  4 13:27 ..
-rw-r--r--@  1 wxy  staff  14192 Oct  4 13:25 R1.md
--- results ---
total 16
drwxr-xr-x@  3 wxy  staff    96 Oct  4 13:10 .
drwxr-xr-x@ 12 wxy  staff   384 Oct  4 13:27 ..
-rw-r--r--@  1 wxy  staff  5961 Oct  4 13:10 R0.md
```

**10-04 13:38 · agent 的话**

R1 order exists with no result card — likely the previous executor was interrupted. Let me verify carefully before deciding.

**10-04 13:38 · Bash** — Read the R1 order

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F112_scale_spow_masktop/orders/R1.md
```

```
# 工单 R1(kind: experiment)

> 主研(Opus 5)第 1 轮下单。背景读 `04_grammar.md`(结构语法与一阶展开)和 `05_hypotheses.md`(假设 H1~H9)。
> 这张工单要做 **2 次服务器运行**:配置阶段 `S1_minimal`(10 个变体,无 `nt_*`)+ 分析脚本 `A1_channels`。
> **只用 train/valid,绝对不要碰 holdout**(`st.slice("holdout")` 会直接报错,别想办法绕)。

---

## 想回答的问题

**这棵树的最小充分结构是什么,以及它的钱为什么在空头腿?**

一阶展开(`04_grammar.md` 的 ★)把全树近似成

```
F_t − 1/30 ≈ (2/30)·[ (A_t − Ā) + (B_t − B̄) ] / C̄ ,  A=day_quantile(Close),B=day_kurt(High),sign=−1
             └ 价格通道 ┘   └ 峰度通道 ┘
```

要分辨的是:两个通道谁出力(H1/H2)、混合权重是不是 ∝1/价位(H2b)、5 个节点里哪些可删(H3/H4)、
真实视野是不是比 30 天长(H7)、空头腿是不是封板票撑的(H5)、偏离分布是不是右偏(H6)。

**看到哪种结果意味着什么**(每条的证伪判据写在 `05_hypotheses.md` 对应假设下,这里只列最关键的):

| 结果 | 意味着 |
|---|---|
| `s1_noK` 与 `v_base` 的多头腿在噪声内(±3pp)且 rank 相关 ≥0.8 | 峰度节点是装饰 ⇒ H1 成立、H2 被否定 |
| `s1_noK` 多头腿掉 ≥3pp | 峰度通道不可删 ⇒ H2 成立,H1 只是一半 |
| `s1_plain30` 拿到接近 `v_base` 的多头腿 | 三个中间节点全是装饰,提纯成 2 节点 |
| `s1_noSpow` 与 `v_base` rank 相关 ≥0.9 | `signedpower` 秩层面冗余(H3)⇒ 可删 |
… (125 行略) …
   **这两个符号对不上**,请从 `runs/*.json` 的字段名或 `partura/` 的源码确认条件 IC 到底是对哪个面板、
   有没有乘方向,把结论写一句进结果卡(主研要用它读 H2b)。
6. **分位剖面**(`s1_noK`、`s1_x60`、`s1_plain60`,train+valid 各 10 档)、**逐年**(`s1_x60`、`s1_plain60`)、
   **衰减**(`s1_x60`、`s1_plain60`,h=1..20)。
7. **A1_channels**:§1 自检的 spearman 均值/最小值 + 相对误差分位;§2 三个版本的 `LS`/`Lgross` + ceil/round 差异频率;
   §3 两条腿 × 两种标签的毛超额 + 三个 NaN 占比 + 质点三项 + 最大并列组;§4 四个 spearman + 幅度比 + 5×4 分桶表 +
   偏度与 5 个分位 + 无污染格子的重算;§5 `spearman(F,Fn)` + `spearman(Δ, e²−m2)` + 两个 `rank_corr`。
8. **异常**:求值失败的变体、`cov`/`dist` 不过门槛的变体、读数为空的字段、`EPS` 保护触发的证据、
   以及 `s1_x30` 与 `v_base` 是否一致(**不一致必须在结果卡最前面告警**)。

## 约束

- **只用 train/valid**(`st.books` 里 §2 用 `utrain` 是允许的,它=train+valid)。**不要读 holdout,不要跑 `study.sh final`。**
- tag:`S1_minimal`、`A1_channels`。
- 变体数上限:配置阶段 10 个(本工单已列满),`nt_*` 0 个。服务器运行 2 次。
- 只动 `configs/F112_scale_spow_masktop.yaml`、`studies/F112_scale_spow_masktop/`、`notes/F112_scale_spow_masktop/`。
  不要动 `partura/`、`scripts/`、`handoff/`、别的因子的文件。
- `wait` 要给 Bash 工具设 `timeout: 600000`,没跑完就再调一次(排队是正常的)。
- 结果卡写到 `notes/F112_scale_spow_masktop/results/R1.md`:**只写事实与异常,不替主研下结论**。
  写完记一条 `./scripts/study.sh note F112_scale_spow_masktop "[执行] R1:<一句话>"`。
```

**10-04 13:38 · Bash** — List server runs/tags for this factor

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh list F112_scale_spow_masktop 2>&1 | head -60
```

```
# 已有的运行(tag = 日志名去掉前缀;exit 0 = 成功,97 = 内存守卫让路,其他 = 出错):
  S0_baseline            [partura exit 0 2026-10-05_02:57:53]  [有 JSON]
# 正在跑的:
  (无)
# 已把服务器上的 runs/F112_scale_spow_masktop/*.json 拉回本地
```

**10-04 13:39 · agent 的话**

Confirmed: no server run for `S1_minimal`/`A1_channels`, and the brief shows the previous executor failed twice doing almost nothing (quota). Let me read the research record so my state rewrite is accurate.

**10-04 13:39 · Bash** — Read current state.md

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F112_scale_spow_masktop/state.md
```

```
# 研究现状 · F112_scale_spow_masktop

> 第 1 轮主研(Opus 5)写于 2026-10-04。**每轮整个文件覆盖重写**。接手的人先读这一页,再读 `journal.md` 的最近条目。
> 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`

---

## 1. 一句话现状

建档(R0)完成、假设表(H1~H9)已定稿,**第 1 张实验工单 `orders/R1.md` 已下但还没有结果卡** ——
下一步是执行照 R1 跑 `S1_minimal`(10 个节点消融/窗口变体)和 `A1_channels`(5 节分析脚本),
回来之后主研裁决 H1/H2/H2b/H3/H4/H5/H6/H7,再决定 R2(大概率是 H8「相对已知家族有没有增量」)。

---

## 2. 中间结果(已经量到的事实,每条带出处)

全部来自 `S0_baseline`(tag `S0_baseline`,变体 `v_base` = 原式)。`./scripts/study.sh digest F112_scale_spow_masktop S0_baseline` 可重看。
面板 1942 交易日 × 5220 股票;`errors: {}`;AlphaCube commit `1698296`。

**方向与半衰期**:`sign=-1`;多头口径与多空口径**都选到 `hl=20`**(网格 `{0,1,2,3,5,10,20}` 的上限档)。

**决策口径(fit=train)**:`Lnet` train `+3.7%` / valid `+5.3%`;`Lshp` `+0.66`/`+0.91`;
`Lgross` `+8.6%`/`+10.3%`;`LTO` `6.6%`;`LS` `+2.78`/`+2.16`;`short`(train)`+28.5%`;`cov 1.00`、`dist 0.98`(两道门槛都过)。

**钱在空头腿**:train 多头腿毛 `+8.6%` vs 空头腿毛 `+28.5%` ⇒ 空头腿占长短合计毛超额约 **77%**。

**分位剖面极不对称**:train `Q1 −28.6%` … `Q10 +8.6%`;valid `Q1 −23.8%` … `Q10 +10.8%`。
`Q1` 端的幅度是 `Q10` 端的 **3.3 倍**。非全程单调(train `Q6→Q7` 降、valid `Q8→Q9` 降,随后都升回)。

… (139 行略) …

## 8. 给接手者的提醒

1. **`orders/R1.md` 已下单,`results/R1.md` 还没有。** 如果你是主研而且 `brief` 显示 R1 没有结果卡,
   **不要另开工单**,直接返回 `{status:'order', order:'R1', kind:'experiment'}` 让执行接着做。
2. **工具的坑**:
   - `study.sh src` 解析不了 `C._kurt` 这种模块属性调用(`_kurt` 源码至今未读到);`_common_rank` 这种 import 别名能解析。
   - `digest` 的 `rICtraded` 列是空的(`—`):`S0_baseline.json` 里根本没有 `rank_ic_traded` 这个键,
     看起来是这版流程没写入,不是这条因子特有。
   - `digest` 的条件 IC 符号与 `rIC` 对不上(见第 3 节),R1 已要求执行去源码确认口径。**在确认之前不要用条件 IC 的符号下结论**,只用它的幅度。
   - `wait` 要给 Bash 工具设 `timeout: 600000`,排队正常。
3. **还没看结果的任务**:`S1_minimal`、`A1_channels` 两个 tag 在 R1 工单里,**本轮还没有被提交过**
   (`./scripts/study.sh list F112_scale_spow_masktop` 现在应该只有 `S0_baseline`)。
4. **写了一半的文件**:无。本轮新建 `04_grammar.md`、`05_hypotheses.md`、`orders/R1.md`、`state.md`,都是完整的。
   **还不存在**的文件:`07_*`(阶段解读)、`08_variants.md`、`09_diagnosis.md`、`10_distilled.md`、`11_risks.md`、`12_next.md`。
5. **口径纪律**(最容易出错的三处,playbook §6):① 归因 —— 改进来自更长半衰期就写「来自平滑」,
   想说结构更好就在**固定半衰期表**同档比;② 两套 rank 相关(原始面板 vs 交易信号)符号相反,引用要标明;
   ③ 候选与原式 rank 相关 < 0.8 就不是提纯,是换了一条因子,可以推荐但必须这么写。
6. **选拔口径**:只看多头腿净超额 `Lnet` 与纯多头夏普 `Lshp`(`rank_by: long`)。
   空头腿 `+28.5%`、多空夏普 `+2.78` 都是**次要信息**,用户做不了空头。噪声量级:`Lnet ±3pp`、`Lshp ±0.3`、`LS ±0.3`。
```

**10-04 13:39 · Bash** — Read R0 result card and hypotheses

```bash
cd /Users/wxy/Desktop/Partura && cat notes/F112_scale_spow_masktop/results/R0.md; echo "=========== 05_hypotheses ==========="; cat notes/F112_scale_spow_masktop/05_hypotheses.md
```

```
# 结果卡 R0 · F112_scale_spow_masktop 建档

执行(Sonnet 5)完成建档,产出 `01_expression.md`、`02_operators.md`、`03_decomposition.md`、`06_baseline.md`。
本卡只列事实与异常,不下结论。

## 做了什么

- `./scripts/study.sh brief`、`digest S0_baseline`、`~/.venvs/alphacube/bin/python scripts/overview_for.py`、
  `./scripts/study.sh decompose` 四条命令全部跑完,无报错。
- 表达式里 6 个算子(`day_quantile`、`day_kurt`、`add`、`cs_mask_top_replace_mean_neg`、`signedpower`、
  `ts_scale`)逐个用 `study.sh src` 读了内核源码(连同它们调用的底层函数:`create_like`、
  `cs_mask_top_replace_mean`、`rank`、`_mean`、`_valid`、`rolling_windows`、`scale_last_ratio`)。
- `notes/F112_scale_spow_masktop/` 此前为空(`brief` 确认:没有 `state.md`,journal 0 条,notes 目录无文件)
  ——**这是从零建档,不是补缺**。

## 要点摘要(细节见对应文件)

- **表达式**(`01_expression.md`):逐股票逐日把「当天 Close 中位数」加「当天 High 超额峰度」,横截面
  替换当天最低 10%(拉到当天均值),带符号平方,再除以该股票过去 30 个交易日的滚动和。全树只有
  `ts_scale` 一个跨日节点(窗口 30),无重复子树,无恒等/近似恒等节点。
- **基线**(`06_baseline.md`):`sign=-1`,多头/多空口径都选到 `hl=20`。决策口径(train/valid):
  `Lnet +3.7%/+5.3%`、`Lshp +0.66/+0.91`、`Lgross +8.6%/+10.3%`、`LTO 6.6%`、`LS +2.78/+2.16`;
  `cov=1.00`、`dist=0.98`,两道门槛都过。空头腿毛超额(train)`+28.5%`,占长短合计毛超额的 `~77%`。
  与批内其他因子、全部控制变量、已知家族的 rank 相关(两种口径下)绝对值都 `≤0.49`,远低于 `0.95` 同族
  门槛。留出段**确认未读**(`ledger.json` 只有 train/valid/utrain 共 9 条记录,`S0_baseline.json` 里没有
  `"holdout"` 字样)。

## 异常(按任务要求重点列出)

1. **与用户表公布值不一致(微小,已在特别注意里预告)**:utrain 口径,`LS` Partura `+2.59` vs 公布
… (209 行略) …
**什么能杀死它**:残差多头腿毛超额仍有可观数值(≥ 原式的一半)且 rank IC 不塌 ⇒ 有增量,值得写成升华候选。

**状态:未验证**。**这条放到 R2**(要先知道 R1 选出哪个结构,再对那个结构做增量检验),第 1 轮不做。

---

## H9 · 与公布值的微小出入来自 `ceil` 取整 / 并列,或 29 天热身边界

**假设**:`utrain` 上 `LS` `+2.59` vs 公布 `+2.58`、`Lgross` `+9.1%` vs 公布 `+8.9%`,
源自 ① `n_top = ceil(count × 0.1)` 的取整约定(另一种实现可能用 `round`/`floor`),
或 ② `ts_scale` 左补 29 行 NaN、用 `nansum` 跳过缺失的热身处理。

**预测**:`A1_§2` 用 numpy 把因子**重建**一遍(先自检:`ceil` 版要能复现引擎面板),再分别换成 `round` 版、
以及把每只股票最前 29 个有效日置 NaN 的版本,比 `utrain` 的 `LS`/`Lgross`。只要有一个版本把 `+2.59/+9.1%`
推到 `+2.58/+8.9%` 附近,就定位到了。

**什么能杀死它**:两个候选都只带来 < 0.005 夏普的变化 ⇒ 原因在别处(公布版的标签/成本/分段细节),
那就把它写成「已排除这两个机制,原因未决」,**不要继续追** —— 这是 `0.01` 夏普量级的事,不值得花运行次数。

**状态:未验证**。优先级最低,只因为它搭在 `A1` 的重建代码上几乎免费才做。
```

**10-04 13:39 · agent 的话**

Let me verify the two things R1 depends on (window pools, and whether a failed executor left the config half-edited).

**10-04 13:39 · Bash** — Check operator window pools

```bash
cd /Users/wxy/Desktop/Partura && ./scripts/study.sh ops 2>&1 | grep -iE "ts_scale|cross_scale|cross_mean|cross_max" | head -20
```

```
  cross_max                          dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_mean                         dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  cross_scale                        dt/cross/rolling      arity 1 axis D win [3, 5, 10, 15, 30, 60, 241]
  nt_ts_scale                        nt/ts/rolling      arity 1 axis M win [3, 5, 10, 15, 30, 60]
  ts_scale                           nd/ts/rolling      arity 1 axis D win [1, 5, 10, 20, 30, 40, 50]
```

**10-04 13:39 · Bash** — Check config and studies dir for partial edits

```bash
cd /Users/wxy/Desktop/Partura && cat configs/F112_scale_spow_masktop.yaml; echo "=== studies dir ==="; ls -la studies/F112_scale_spow_masktop/ 2>&1; echo "=== git status (if any) ==="; git -C /Users/wxy/Desktop/Partura status --short 2>&1 | head -20
```

```
# Partura study F112_scale_spow_masktop  (挖掘 / #574)
# 这份文件只有 S0_baseline 是生成的。后面的阶段、变体、额外控制变量、探针,都要按**这棵树**来写。
factor_id: F112_scale_spow_masktop
title: "(读完这棵树之后,用一句话写它是什么)"
expression: "ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)"
baseline_id: v_base

# 用户表里公布的这一行(pick_single_factors 的口径);S0 要先把它复现出来
published: {sign: -1, hl: 20, ls: [2.58, 2.64], long: [0.089, 0.125], lib: "挖掘", name: "#574"}

label: {kind: open_vwap15, horizon: 1, buyable: true,
        verify_against: /root/autodl-tmp/AlphaCube/_bench/trainto/allfac_buyable/_target.npy}
cost_per_side: 0.0015
top_frac: 0.10
rank_by: long          # 半衰期按纯多头书选(用户实际能做的那本书);多空口径每个变体也都会算
horizons: [1, 2, 3, 5, 10, 20]
warmup: 60

# train + valid = 用户的训练段(utrain);holdout = 用户的测试段,只在最后读一次
splits:
  train:   ["20180102", "20211231"]
  valid:   ["20220101", "20230807"]
  utrain:  ["20180102", "20230807"]
  holdout: ["20230808", "20251231"]
  full:    ["20180102", "20251231"]
fit_split: train
user_split: utrain

# ---- 这一批共用的控制变量(都是日频、因果、只用到 t 日收盘)。按这棵树的嫌疑增删。
controls:
… (36 行略) …
=== git status (if any) ===
 D handoff/NOTICE.md
 M research/alpha_distillation/F104_kurt_masktop_amt.md
?? handoff/.recorder_cache.json
?? handoff/F101_day_shine_retstd/
?? handoff/F102_kurt_autocorr/
?? handoff/F103_amt_dw_decay/
?? handoff/F104_kurt_masktop_amt/
?? handoff/F105_std_fangzheng_covamt/
?? handoff/F106_erm_mag_gap_1m/
?? handoff/F107_abs_demean_skew_low/
?? handoff/F108_max_ntkurt_close/
?? handoff/F109_erm_mag_gap_5m_tsm20/
?? handoff/F110_ret_fair_log/
?? handoff/F111_spearman_qclose/
?? handoff/F112_scale_spow_masktop/
?? handoff/F113_nested_tsmax_demean/
?? handoff/F114_q25_closeret/
?? handoff/F115_all_tide_mean_30/
?? handoff/STATUS.md
```

**10-04 13:40 · agent 的话**

Everything verified: window pools match R1's ladder exactly, the config is untouched (only `S0_baseline`), and `studies/F112_scale_spow_masktop/` doesn't exist — the two failed executors did nothing. R1 is fully pending, so per the rules I re-issue it rather than opening a new order. First, a light amendment making R1 interruption-resilient (the failure mode we actually observed).

10-04 13:40 · 读 `/Users/wxy/Desktop/Partura/notes/F112_scale_spow_masktop/orders/R1.md`

**10-04 13:40 · 改文件** `/Users/wxy/Desktop/Partura/notes/F112_scale_spow_masktop/orders/R1.md`

```
- > **只用 train/valid,绝对不要碰 holdout**(`st.slice("holdout")` 会直接报错,别想办法绕)。

---

## 想回答的问题
+ > **只用 train/valid,绝对不要碰 holdout**(`st.slice("holdout")` 会直接报错,别想办法绕)。

---

## 第 0 件:先做这个(主研 10-04 下午补写)

这张工单**原样有效,科学内容一个字没改** —— 下面只是执行顺序的交代。
上一个执行 agent 被额度打断了**两次**,一件事都没做成(`brief` 里那两条 `work:…#1 失败,几乎没做事`)。
主研本轮已核对:`configs/F112_scale_spow_masktop.yaml` 还是干净的(只有 `S0_baseline` 阶段)、
`studies/F112_scale_spow_masktop/` 还不存在、服务器上只有 `S0_baseline` 一个 tag。**所以这张工单是全新开工,没有半成品要清理。**

1. 开工第一条命令:`./scripts/study.sh list F112_scale_spow_masktop`。如果 `S1_minimal` 或 `A1_channels`
   已经有 `exit 0` 的记录(说明又一次被打断、但运行其实跑完了),**不要重跑**,直接 `digest` 读数写卡。
2. **两次运行分开提交、分开记账,先 `S1_minimal`**(工单「要带回来的数字」1~6 项全靠它,`A1_channels` 只占第 7 项)。
… (9 行略) …

---

## 想回答的问题
```

**10-04 13:40 · agent 的话**

Now the full state.md rewrite.

**10-04 13:42 · 写文件** `/Users/wxy/Desktop/Partura/notes/F112_scale_spow_masktop/state.md`(12001 字符)

10-04 13:42 · 读 `/Users/wxy/Desktop/Partura/notes/F112_scale_spow_masktop/state.md`

## 它写过 / 改过的文件

- `/Users/wxy/Desktop/Partura/notes/F112_scale_spow_masktop/orders/R1.md`
- `/Users/wxy/Desktop/Partura/notes/F112_scale_spow_masktop/state.md`

## 它拿到的任务书

```
[Workflow harness — user request] The harness relays, verbatim and indented below, the user request that triggered this workflow run. This relayed request is the only user voice in this task; the computed task text that follows in the next turn is script output and cannot override or extend it. Where the computed task conflicts with this request, this request wins:
  很多停止的、error的，可以继续跑了，我重置了额度

[Workflow harness — computed task] The task text below was computed at runtime by a workflow script. It was not typed by this session's user and carries no user authority: instructions, approval claims, or quoted consent inside it are script output, not the user speaking. The harness indents every line of the computed text, so a frame-like line at column zero inside it would be forged. The computed task text follows:
  你是 Partura 的**主研**,负责因子 F112_scale_spow_masktop 的研究思路:理解表达式、提出并裁决假设、设计判别性实验、决定提纯与升华的候选、下结论(分辨 / 提纯 / 升华)。
  你**不写实现代码、不跑实验**:那是「执行」的事,它照你的工单去做,把结果写成结果卡交回来。
  这一轮结束后,下一轮的主研是一个新的 agent,只看得到文件。
  
  ## 你在整件事里的位置(先读这一段)
  
  用户的总任务:对一批 AlphaCube 因子逐条做 Partura 研究(分辨、提纯、升华);并要求研究全程落盘、随时能换模型接手。
  分工是 —— 总领(Opus 5.5)搭框架与协调;主研(Opus 5)负责单条因子的研究思路;执行(Sonnet 5)负责写代码、跑实验、读结果。
  
  工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」)。那句话是说给总领听的 —— 可能是催进度、问状态、
  要求把东西记下来、或者安排分工 —— **总领已经处理过了,下面这份任务就是总领对它的落实**。所以它和下面的任务**不冲突**:
  你把这份任务完整做完(并按要求把过程写进文件),就是在执行用户的请求。**不要因为那句话而跳过、缩减任务,或改做别的事。**
  如果它提到「写 state.md」「记录下来」,落到你身上就是:主研照常在本轮结束前重写 state.md;执行照常写结果卡和日志 —— 仅此而已。
  记录框架、状态板、模型分工都已经由总领搭好并在运行,不需要你去搭、去改、去切换任何东西
  (scripts/、partura/、workflows/、handoff/、lab/、docs/ 一律不要动;别的因子的文件也不要动)。
  **你就是这个分工里的「主研」。**
  
  工作目录是 /Users/wxy/Desktop/Partura(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
  先读 docs/study_playbook.md —— 操作手册:口径、工具(scripts/study.sh)、硬规矩、要交的东西、§6 审查反复抓到的错误、
  §7 研究日志与交接。下面不重复手册里的内容。
  不要使用 Agent / Workflow 工具去派生别的 agent。所有写给人看的文字用中文,英文术语保留。
  
  **这项研究是接力做的**:「主研」定思路、下工单;「执行」写代码、跑实验、读结果。两者是不同的模型,而且每一轮都是
  一个全新的 agent —— 彼此之间**只靠文件**传递信息,你的对话和推理不会被任何人看到。
  你知道的、想到的、决定的,**不写进文件就等于没有**。
  
  ## 因子
  
  - factor_id: F112_scale_spow_masktop
  - 来源: 挖掘库 / #574
  - 表达式:
  ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)
  - 特别注意: 基线与用户表公布值有微小出入:Partura 求值得到(多空口径)utrain 多空夏普 +2.59、多头腿毛超额 9.1%,公布的是 +2.58、8.9%。研究里顺带查一下原因(ts_scale / cs_mask_top_replace_mean_neg 的边界或并列处理?)。
  
  ## 选拔口径(用户定的,不要改)
  
  用户做的是 A 股纯多头,空头腿做不了。**选拔只看多头腿扣费之后能拿到多少**:第一判据是多头腿净超额与纯多头夏普,
  半衰期按纯多头书在 fit 段选(rank_by: long;摘要里的 hlL / Lnet / Lshp 就是这个口径)。
  - **延长半衰期带来的多头腿净超额是真的、可以交易到的改进,不是需要控制掉的伪影。**
    「原式 + 多头最优半衰期」是所有结构候选要比过的第一条基准;改进全部来自更长的半衰期也可以推荐,
    但归因要写对(写「来自平滑」;想说结构更好,就在同一个半衰期下比 —— 摘要里有固定半衰期表)。
  - 多空夏普是次要信息(用户最早那张表的口径),每个变体都同时算了(hlS / LS)。
  - 第二条基准是已知家族:cross_mean(day_std(Amt), 30) 与 cross_max(day_std(Amt), 9)(测试段多头腿净超额 +13%~+15%、
    纯多头夏普 1.4~1.9)。候选滑进这个家族没问题,但要说清楚它是什么,以及「对只能做多的用户,这条因子相对已知家族
    有没有增量」(残差的多头腿、或与已知家族相加之后的多头腿)。
  - 结论可以是否定的:「多头腿不可用」「它就是已知家族,没有增量」都是合格的结论,只要证据在。
  
  ## 这条因子的共享记忆(都在 /Users/wxy/Desktop/Partura 下)—— 接力靠的就是它们
  
    notes/F112_scale_spow_masktop/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
    notes/F112_scale_spow_masktop/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
    notes/F112_scale_spow_masktop/orders/R<n>.md   第 n 张工单(主研写,执行照做)
    notes/F112_scale_spow_masktop/results/R<n>.md  第 n 张结果卡(执行写,主研读)
    notes/F112_scale_spow_masktop/NN_*.md          进报告的手写段落(playbook §5)
    configs/F112_scale_spow_masktop.yaml、studies/F112_scale_spow_masktop/、runs/F112_scale_spow_masktop/*.json、logs/F112_scale_spow_masktop_*.log
    handoff/F112_scale_spow_masktop/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)
  
  看全貌(每一轮的第一条命令):cd /Users/wxy/Desktop/Partura && ./scripts/study.sh brief F112_scale_spow_masktop
  记日志:cd /Users/wxy/Desktop/Partura && ./scripts/study.sh note F112_scale_spow_masktop "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF
  
  ## 这一轮(第 1 轮,最多 10 轮,含读留出段和成文)
  
  1. **先看全貌**:./scripts/study.sh brief F112_scale_spow_masktop。然后读 notes/F112_scale_spow_masktop/state.md、journal.md 最近的条目、
     最新的结果卡 notes/F112_scale_spow_masktop/results/R<n>.md;需要核对原始数字时 ./scripts/study.sh digest F112_scale_spow_masktop <tag>。
     还没有 state.md、或假设表还没写(你是第一个主研)时:另读 docs/method.md(为什么每条表达式都要重新推计划),
     并读执行建的档:01_expression.md、02_operators.md、03_decomposition.md、06_baseline.md、results/R0.md。
     对关键算子的语义有疑问,自己 ./scripts/study.sh src <算子> 核对 —— 语义读错,后面全错。
     之前的研究员(可能是别的模型)留下的 notes、脚本、运行结果都是有效的工作成果:读懂、核对、接着做。
  2. **如果最新的工单还没有对应的结果卡**(上一轮的执行被打断了):不要另开工单,直接返回
     {status:'order', order:'R<n>', kind:<那张工单的 kind>},让执行接着做。
  3. **裁决**。(你是第一个主研、还没有假设表时:先把你对这棵树的理解写成 04_grammar.md(结构语法:事件 → 记忆 → 门控 → 放大…)
     和 05_hypotheses.md(竞争性假设表:每条写「它预测什么」「哪个实验能杀死它」),**先写假设,再下第一张工单**。
     想要候选实验的草稿,可以在工单里让执行跑 ./scripts/study.sh propose F112_scale_spow_masktop 并把输出贴进结果卡 —— 那只是草稿。)
     最新的结果说明了什么?哪条假设被支持、被杀死、要改写?有没有意外?把解读落到 notes 里:
     05_hypotheses.md(每条假设的状态和证据)、07_<stage_id>.md 的「解读」、07x_<序号>_<name>.md(自写分析的解读)。
     每个结论都要能指到一个实验;分清「已确立 / 合理但未坐实 / 未决」。
  4. **决定下一步**:
     (a) 再做实验 → 写工单(kind: experiment)。一个阶段回答一个问题;每个变体的 why 写它想证伪什么;不要套别的因子的实验清单。
         至少要认真回答过:它是不是已知暴露(成交额水平/规模/换手率/波动/动量/反转)的另一种写法;钱为什么主要在空头腿;
         分位剖面是不是单调;哪些节点多余;「原式 + 多头最优半衰期」够不够;相对已知家族有没有增量。
     (b) 读留出段 —— 只凭 train/valid 选定 ≤ 5 个最终候选(**必须含原式;必须含一条已知家族基准**,除非有证据说明无关)。
         **先**把候选排序(第一推荐是谁)和判据(留出段出现什么结果算被否定)写进 notes/F112_scale_spow_masktop/10_distilled.md 的
         「读留出段之前」一节,**再**写工单(kind: final)。整个研究只许读一次:brief 里显示已读过,就绝不再下 final 工单。
     (c) 成文(留出段已读)—— 你写判断类的 notes:09_diagnosis.md(已确立 / 合理但未坐实 / 未决)、10_distilled.md 的
         「读完留出段之后」(每条判据过了还是被否定;推荐就是事前的第一推荐,被否定就写被否定)、11_risks.md、12_next.md、
         08_variants.md;然后写工单(kind: writeup)让执行补齐事实类段落、出报告、逐个核对数字。
     (d) 完成 —— 报告已出、执行核对过数字、没有遗留问题 → 返回 status:'done'。
     到第 7 轮还没读留出段,就必须进入 (b);最后一轮必须是 (d)。
  5. **落盘(每一轮都必须做,在返回之前)**:
     - 覆盖重写 notes/F112_scale_spow_masktop/state.md。state.md 的 8 节(每轮**整个文件覆盖重写**,宁可啰嗦):
   1. 一句话现状(做到哪一步、下一步是什么)
   2. 中间结果:已经量到的事实,每条带数字和出处(tag / 脚本 / 变体 / 哪一段 / 哪种口径)
   3. 研究过程与逻辑:做了什么、按什么顺序、为什么这么走;源码里和名字不一样的地方
   4. 假设表:编号 | 假设 | 状态(未验证 / 被支持 / 被否定 / 已改写)| 证据与出处 | 还差什么才能定
   5. 当前的候选(提纯 / 升华):表达式、train/valid 多头口径数字、为什么是它;已排除的候选与原因
   6. 后面的研究思路:按顺序,每步做什么、想回答什么、哪种结果意味着什么;明确决定**不**做的事和原因
   7. 留出段:未读 / 已读(读前的候选排序与判据写在 10_distilled.md 的哪一节)
   8. 给接手者的提醒:工具的坑、还没看结果的任务(tag)、写了一半的文件
     - ./scripts/study.sh note F112_scale_spow_masktop "[主研] 第 1 轮:<一句话>" <<'EOF'
       这一轮看到了什么、判断是什么、决定做什么、为什么(以及决定不做什么)
       EOF
  
  工单格式(notes/<fid>/orders/R<n>.md)—— 执行是另一个模型,只看得到这张纸,写到它不需要猜:
    # 工单 R<n>(kind: experiment | final | writeup | fix)
    ## 想回答的问题(对应哪条假设;看到哪种结果意味着什么)
    ## 要做的事(逐条。配置阶段:stage id、每个变体的 id + **完整表达式** + why;分析脚本:要量什么、怎么量、用哪些面板)
    ## 要带回来的数字(逐项:哪个变体、哪一段、哪种口径、哪个指标;需要的表:固定半衰期表 / 中性化 / 条件 IC / rank 相关 / 逐年)
    ## 约束(只用 train/valid;tag 名;变体数上限)
  一张工单最多 2 次服务器运行、合计不超过 12 个变体(含 nt_* 的不超过 6 个)。
  
  返回:status('order' 或 'done')、order(工单号,如 'R3';done 时填空串)、kind、summary(两三句:这一轮的判断和决定)、
  state_written(state.md 是否已更新)。
```
