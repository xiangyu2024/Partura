# F112_scale_spow_masktop — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F112_scale_spow_masktop` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #574(批次 B01_single_factors)
- 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F112_scale_spow_masktop#2`:已返回结果,最后动作 10-04 15:00 → `handoff/F112_scale_spow_masktop/agents/lead_R2_a1c959d6b9f32261b.md`
  - `work:F112_scale_spow_masktop#2`:失败,最后动作 10-04 15:41 → `handoff/F112_scale_spow_masktop/agents/work_R2_ac365408f6933c951.md`
  - `work:F112_scale_spow_masktop#2`:失败,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F112_scale_spow_masktop` 看服务器上的 tag,`./scripts/study.sh digest F112_scale_spow_masktop <tag>` 重看结果)。

## 研究现状(`notes/F112_scale_spow_masktop/state.md`,10-04 14:58 更新)—— **先读这个文件**

# 研究现状 · F112_scale_spow_masktop

> 第 **2** 轮主研(Opus 5)重写于 2026-10-04 下午。**每轮整个文件覆盖重写。**
> 接手的人先读这一页,再读 `journal.md` 最近的条目,再读 `results/R1.md`。
> 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`

---

## 1. 一句话现状

R1 两次运行(`S1_minimal` 10 变体 + `A1_channels` 6 节)**全部跑完**,主研已裁决:
**原式的五个节点里有三个对多头腿不是正贡献,唯一的跨日窗口也选短了** ——
删掉横截面截尾,多头腿在**每一个固定半衰期**上都变好(hl20 `+3.7% → +7.1%`,`Lshp +0.66 → +1.05`,换手不变)。
但同时发现两件扫冷水的事:① 把它「提纯」到最简形式就变成了**已知的 20 日反转**(`ctl_mom20` 自己就有 `+5.4%/+8.0%`);
② 已知家族的真实数字比上一版 state 写的高得多(`+12.6%~+13.7%` / `+22.2%~+22.3%`,`Lshp +1.78~1.99/+3.46~3.59`),
**我们最好的候选只有家族的一半**。
**下一步**:已下工单 `orders/R2.md`(kind: experiment,两次运行)—— 运行 1 `S2_combo` 测「mask 去掉 × 窗口拉长」
这个从没测过的组合 + 2×2 正交 + 遮最高一成的控制实验;运行 2 `A2_increment` 做 H8(相对已知家族的残差与合成增量),
那是本研究的决定性问题。留出段**未读**。

---

(…全文 17526 字符,读 `notes/F112_scale_spow_masktop/state.md`)

## 研究日志(`notes/F112_scale_spow_masktop/journal.md`:17 条,其中研究员自己写的 8 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 15:26 [auto] 启动 exec A2_increment:studies/F112_scale_spow_masktop/a2_increment.py

### 2026-10-04 15:30 [auto] A2_increment 跑完(exit 0);重看结果:logs/F112_scale_spow_masktop_A2_increment.log

### 2026-10-04 15:32 [执行] R2:S2_combo(10变体)+ A2_increment(§0~§4)全部跑完,exit 0,没有卡住的地方

看到了什么(全部来自 runs/F112_scale_spow_masktop/S2_combo.json 与 logs/F112_scale_spow_masktop_A2_increment.log,均 exit 0):
- 一致性检查全部通过:s2_f30 的全部字段(Lnet/Lshp/Lgross/LTO/rIC/rICtraded/cov/dist,train 与 valid)与 s1_noMask
  精确相等(diff=0.000e+00,不是近似);s2_n30 与 s1_plain30 同样精确相等。A2 §1 里 E0/E1/E2/E3 又分别与
  v_base/s1_noMask/s2_f_x60/s1_plain60 独立核对一致,K1/K2 与 S0_baseline.json 的 diagnostics.controls 逐位相同。
- S2_combo 固定半衰期表(hl0/2/5/10/20,train):s2_f30(≡s1_noMask)五档全面优于 v_base;s2_f_x60(头号候选,mask去
  掉×窗口60)五档也全面优于 v_base,hl20 +7.8%,但不是全表最高——s2_f_x241 hl20 更高(+9.7%)、s2_n_x241 五档
  反而全面走低。窗口在哪见顶没有单一答案,留给主研读表判断。
- s2_masktop(遮最高一成的控制实验):固定半衰期表与 s2_f30 很接近(hl20 +7.7% vs +7.1%,其余四档都接近,不像
  v_base 那么差),条件 IC|ctl_price 的桶1 也从 v_base 的 +0.0037 回升到 +0.0305——"任一成被拉平都伤"比"专门饿
  多头端原料"更贴近这组数字,具体怎么改写 H10 留给主研。
- A2 §0 两条硬门槛自检都过:books(E0) 复现 Lnet train+3.66%/valid+5.35%、Lshp+0.66/+0.91、hl=20;手写的多头十分位
  毛超额函数复现 Lgross train+8.64%(容差内)。
- A2 §2(残差检验,H8 第一半):E0~E3 对 {K1,K2} 与 {K1,K2,ctl_mom20} 两组回归取残差后,残差 Lgross 与残差 rIC
  在 train、valid 上全部没有
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:33 [auto] 启动 exec A2_increment:studies/F112_scale_spow_masktop/a2_increment.py

### 2026-10-04 15:38 [执行] R2 补充:A2_increment 附加节算出了原始面板口径的 rank 相关(工单要带回数字第4项的后一半),再次确认两套口径符号相反这件事在 S2 变体上同样成立

看到了什么:原始日频面板口径下,10 个 s2_* 变体 vs ctl_mom20 全部是正数(+0.34~+0.90),vs K1/K2 也全部是正数
(+0.09~+0.37);而 S2_combo 主表(交易信号口径)里同一批变体 vs ctl_mom20 全部是负数(-0.11~-0.42)。这与 R1
在 S1_minimal 上已经记录的"两套口径符号相反"现象方向一致、幅度相当,不是新发现,是同一现象在 S2 上的再次确认。
vs v_base 列两套口径同号(原始面板 0.24~0.69,交易信号 0.51~0.78),幅度上原始面板普遍更低,也与 R1 的读数一致。
下一步:没有,这是补数字,不改变 R2 的任何判断;完整表格见结果卡。

## 工单与结果卡(`notes/F112_scale_spow_masktop/orders/`、`notes/F112_scale_spow_masktop/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F112_scale_spow_masktop.yaml`)

- 标题:「当天价位 + 当天 High 分钟级尖峰度」这个混合量,相对它自己过去 30 个交易日的水平偏离了多少;反向交易
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_minimal**(10 个变体):这棵树的最小充分结构是什么:删掉每个节点、把唯一的跨日窗口换档,多头腿和与原式的 rank 相关怎么变?
  s1_noK、s1_noP、s1_noMask、s1_noSpow、s1_plain30、s1_w10、s1_x30、s1_x60、s1_x241、s1_plain60
- **S2_combo**(10 个变体):mask 去掉之后,剩下的节点和窗口怎么配最好?遮最高一成会不会一样差?
  s2_f30、s2_k30、s2_p30、s2_n30、s2_f_t50、s2_f_x60、s2_f_x241、s2_n_t50、s2_n_x241、s2_masktop

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F112_scale_spow_masktop`)

- `S0_baseline`  10-04 11:57  1 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop S0_baseline`
- `S1_minimal`  10-04 13:59  10 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop S1_minimal`
- `S2_combo`  10-04 15:08  10 个变体  → `./scripts/study.sh digest F112_scale_spow_masktop S2_combo`
- `A1_channels`(自写脚本的输出)  10-04 14:21  exit 0  → `logs/F112_scale_spow_masktop_A1_channels.log`
- `A2_increment`(自写脚本的输出)  10-04 15:37  exit 0  → `logs/F112_scale_spow_masktop_A2_increment.log`

## 已写的 notes(`notes/F112_scale_spow_masktop/`)

`01_expression.md`(4K)、`02_operators.md`(15K)、`03_decomposition.md`(6K)、`04_grammar.md`(6K)、`05_hypotheses.md`(24K)、`06_baseline.md`(11K)、`07_S1_minimal.md`(7K)、`07x_01_a1_channels.md`(7K)、`journal.md`(25K)、`state.md`(26K)

## 自写的探针与分析脚本(`studies/F112_scale_spow_masktop/`)

- `a1_channels.py`  10-04 14:19  A1_channels — R1 工单第 2 件。五个小节(§1~§5)各自 try/except,互不拖累。
- `a2_increment.py`  10-04 15:33  A2_increment -- R2 工单运行 2。五节(§0 自检 → §1 独立对照 → §2 残差增量 → §3 合成增量 → §4 mask 机制),

## 结构化结果(`handoff/F112_scale_spow_masktop/results/`)

(还没有)
