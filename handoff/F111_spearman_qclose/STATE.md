# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-04 23:02(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F111_spearman_qclose#2`:已返回结果,最后动作 10-04 15:24 → `handoff/F111_spearman_qclose/agents/lead_R2_af0c892fdf47993a9.md`
  - `work:F111_spearman_qclose#2`:失败,最后动作 10-04 15:41 → `handoff/F111_spearman_qclose/agents/work_R2_ad160550f51aa21dd.md`
  - `work:F111_spearman_qclose#2`:失败,几乎没做事

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F111_spearman_qclose` 看服务器上的 tag,`./scripts/study.sh digest F111_spearman_qclose <tag>` 重看结果)。

## 研究现状(`notes/F111_spearman_qclose/state.md`,10-04 15:21 更新)—— **先读这个文件**

# F111_spearman_qclose 研究现状

> 本文件每轮由**主研覆盖重写**。最后更新:**第 2 轮(主研,Opus 5)**,2026-10-04。
> 表达式:`ts_spearman(day_quantile(Close), 10)`,来源 挖掘库 / #953。

---

## 1. 一句话现状

**R1 已经跑完并裁决完了:身份定清了,「它是什么」这一问基本答完。**
我这一轮读完 `results/R1.md`,写了 `07_S1_whatis.md`、`07x_1_identity.md`,把 H1/H2/H3/H6/H7/H10/H11 全部裁决
(H1 确立、H3/H6/H10 被否定、H7 成立、H2 被限定、H11 改写),**并发现了一条不在任何原假设里的承重件**
(见 §2.2)。H4(「对纯多头用户没有增量」)已经**被强烈支持**,但还差最后一步。
**下一步:执行去跑 R2**(阶段 `S2_window` 8 个变体扫窗口 `d` + 脚本 `x2_increment.py` 的 5 个 block),
回来之后第 3 轮主研就应该能定 H4,然后**直接进读留出段**(研究已经可以收口了)。

---

(…全文 21014 字符,读 `notes/F111_spearman_qclose/state.md`)

## 研究日志(`notes/F111_spearman_qclose/journal.md`:13 条,其中研究员自己写的 6 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 14:35 [执行] R1:S1_whatis(6变体)+x1_identity(a/b/c/c4/d)全部跑完,结果卡 results/R1.md

两次服务器运行均 exit 0:run S1_whatis(285s)、exec x1_identity.py(4个block+c4,无一触发except)。
自检先过(完整窗口rank_var=8.25精确;暴力双循环vs proj逐日rank相关0.9998)。

H1(block a):proj与f在窗口完整格子(占98.7%)上逐日Spearman精确=1.0000(全部格子mean=0.9974);
proj自己当因子Lnet+10.95%/+17.09%几乎复刻v_base(+10.4%/+17.0%)。m_mktcorr(表达式近似版)
rank相关0.74,在工单先验0.6~0.9内。

H2/H11(block b):f vs rho_time按c(t)符号分组,|0.47|(c>0,644天)/|0.60|(c<0,706天)——
没有干净落进state.md预先定的<0.5"松"或>0.8"紧"两档(一侧压线、一侧卡在中间),待主研裁决。
(c4)|rank_corr(f,known)|随hl单调上升(3条家族都是,0.23~0.31→0.37~0.39),支持H11那一步预测。

H3(block d):tie比例44%,按十分位Q1(36%)单调升到Q10(51%);去掉并列格子后Lgross基本不变
(+14.31/+19.07%)但换手从4%涨到23%(5~6倍),净超额塌到-3.58%/+2.52%。同轮l_mean(几乎无并列
的叶子替换)整体表现(+10.7%/+16.5%)却和v_base几乎一样——两条证据有张力,留给主研取舍。

H4(block c,最重要):3条known_*家族,主口径残差多头腿净超额还剩+3.7~+5.2%(train)/+6.3~+7.8%
(valid);S0§7可比口径(残差不重新平滑)在train上三条全转负、valid接近零。组合w=0.25时
known_stdamt_max9/known_amt_max9两条家族train(+amt_max9的valid)有小幅提升(Lshp最多1.95→2.21),
known_stdamt_mean30没有看到同样提升。

H6/H7/H10:s_pearson(+10.7%/+16.9%)、l_last(+11.1%/+18.4%)和v_base打平甚至略好,ran
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:23 [主研] 第 2 轮:R1 全部裁决——恒等式精确成立,但承重件是「每只股票等权」而不是「秩」,便宜写法堵死;H4 被强烈支持;下 R2 扫窗口 d + 双重排序

看到了什么(读 results/R1.md 两次运行的全部数字):

1. **H1 确立,而且是恒等不是近似**:窗口完整的格子(占 98.70%)上 numpy 复算的 proj 与原式面板的
   逐日 Spearman mean/median/p95 全是 1.0000、p05 0.9999;proj 自己当因子 Lnet +10.95%/+17.09%
   (原式 +10.4%/+17.0%),好的那 0.5pp 来自它少了源码分母口径不一致那个瑕疵(只影响 1.3% 的格子)。

2. **本轮最重要的发现,不在任何原假设里:承重件是「每只股票等权」,不是「秩」。**
   S1 里最有信息量的一对比较不是我事前标的主判别项,而是 m_mktcorr 和 s_pearson 这一对:
   - s_pearson(ts_pearson,保留"先逐股归一再平均",只把秩换成标准化):rank 相关 0.978,
     Lnet +10.7%/+16.9%,**完全没塌**;固定半衰期表上中段还更好(hl5 +10.7% vs 原式 +7.44%)。
   - m_mktcorr(ts_corr(A, cs_mean(A),10),改成"先平均再归一"):rank 相关只有 0.742,
     valid 多头腿从 +17.0% 塌到 **+4.9%**、夏普 3.07 → **0.74**。
   cs_mean 平均的是**价格水平**(高价股主导),给不出那条等权共识路径 M。
   ⇒ **H6 被否定**(秩不承重),而且**提纯的便宜路线被堵死** —— ts_corr(A, cs_mean(A), d) 不能用,
   也不能拿它去扫窗口 d。能用的只有 ts_pearson(chunked matmul,同一本书的便宜实现)。
   这条已经写进 04_grammar.md 新加的第 5 步(第 1 步末尾那句"提纯方向立刻确定"是错的,已改写)。
   顺便:第 1 轮 H1 的预测 (c) 写的是"先验 0.6~0.9、不是 1.0,因为 cs_mean 是价格水平的截面均值"
   —— 实测 0.742,预言连机制一起命中,这是事前写下判据的好处。

3. **alpha 在条件化里,不在动量里(三条独立证据,已确立
…(这条日志还有后文,读 journal.md)

### 2026-10-04 15:35 [auto] 启动 run S2_window:阶段 S2_window

### 2026-10-04 15:39 [auto] S2_window 跑完(exit 97);重看结果:logs/F111_spearman_qclose_S2_window.log

### 2026-10-04 15:40 [auto] 启动 run S2_window:阶段 S2_window

## 工单与结果卡(`notes/F111_spearman_qclose/orders/`、`notes/F111_spearman_qclose/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 **还没有(待执行)**

## 配置里的实验计划(`configs/F111_spearman_qclose.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_whatis**(6 个变体):ts_spearman 的全市场两两配对平均,等价于什么更简单的东西?预测力的载体是价格路径、活跃度,还是实现细节?
  m_mktcorr、s_pearson、l_mean、l_last、l_amt、t_tsrank
- **S2_window**(8 个变体):窗口 d 这根轴上有东西吗?10 天只是任意选择,还是 5~50 里有一个明显更好的频段?
  a_last_10、w_last_5、w_last_20、w_last_30、w_last_50、w_q_30、pl_last_10、p_last_30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F111_spearman_qclose`)

- `S0_baseline`  10-04 11:54  1 个变体  → `./scripts/study.sh digest F111_spearman_qclose S0_baseline`
- `S1_whatis`  10-04 14:05  6 个变体  → `./scripts/study.sh digest F111_spearman_qclose S1_whatis`
- `x1_identity`(自写脚本的输出)  10-04 14:23  exit 0  → `logs/F111_spearman_qclose_x1_identity.log`
- `S2_window`(自写脚本的输出)  10-04 15:41  exit 97  → `logs/F111_spearman_qclose_S2_window.log`

## 已写的 notes(`notes/F111_spearman_qclose/`)

`01_expression.md`(3K)、`02_operators.md`(9K)、`03_decomposition.md`(4K)、`04_grammar.md`(11K)、`05_hypotheses.md`(33K)、`06_baseline.md`(12K)、`07_S1_whatis.md`(7K)、`07x_1_identity.md`(14K)、`journal.md`(26K)、`state.md`(33K)

## 自写的探针与分析脚本(`studies/F111_spearman_qclose/`)

- `x1_identity.py`  10-04 14:17  R1 exec script -- the identity + conditioning + known-family + tie analysis.

## 结构化结果(`handoff/F111_spearman_qclose/results/`)

(还没有)
