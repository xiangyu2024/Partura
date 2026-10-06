# 给接手这个项目的 agent

## 定位(2026-10-05 用户改定)—— 先读这一段

**Partura 不是 AlphaCube 的下游。** AlphaCube 负责高熵、可扩展的经验发现;Partura 负责从成功与失败的实验里形成并更新
研究信念,**再反过来改变 AlphaCube 的搜索**。所以一轮研究的产出有两样:

1. 对因子的结论(提纯 / 分辨 / 升华)—— `research/alpha_distillation/`;
2. **反向指引**:把结论编成对搜索的四类干预 —— 奖励函数、评估方法、动作与子结构的先验(拒绝 / 降权 / 升权 / 改写)、
   交给 AlphaCube 短搜的想法 —— `guidance/<batch>.yaml`,做法见 **`docs/reverse_guidance.md`**。

研究一个想法,不要只自己写几十个表达式:把它写成 `guidance/*.yaml` 里的一条 idea(假设 + 种子 + 邻域 + 奖励),
`./scripts/study.sh idea <id>` 让 AlphaCube 的 GP 在那个邻域里搜一小会儿,**并配一个同预算、不带干预的对照**;
证据落在 `episodes/`,信念更新之后回写 `guidance/`。要证明的是「单位算力的发现效率提高了」,不是「这次搜到了好因子」。
批量研究(`docs/study_playbook.md` 的批量流程)仍是形成结论的办法;下面的单条流程是它的细节。

**读 `docs/method.md` 之前不要开始做研究。** 最容易犯的错是把上一条因子的
`configs/*.yaml` 改个表达式就跑 —— 那不是研究,那是又一次盲搜。

一句话版本:

> 实验计划和探针集合都是**这棵树**的性质,每条表达式都要重新推;
> 唯一跨研究复用的是 `lab/findings.yaml` 里的结论,而且它是**先验**,不是证据。

拿到一条新表达式,按这个顺序走:

1. `partura decompose "<expr>"` —— 先看清楚每个算子的**实现**和**探针实测值**,
   以及实验室里与这棵树相关的既往先验。
2. **想一遍这棵树特有的问题**。内置探针答不上来的,就为这次研究写:
   `studies/<factor_id>/probes.py`,一个探针回答一个问题,声明适用范围,
   写完先在**已知答案的算子**上自检(见 `docs/method.md` §3)。
3. `partura propose "<expr>" --factor-id <fid> --out configs/<fid>.draft.yaml`
   —— 它给的是**候选**。删掉没信息量的,补上只有读了这棵树才想得到的,
   每条 `why` 写成一句可证伪的话;控制变量、门控、诊断项按这棵树的嫌疑挑。
4. `partura run` 训练段 + 验证段,一个阶段回答一个问题,看完结果再决定下一阶段。
5. `--holdout` 只用一次,在最终候选上。
6. `partura report`,然后把**可迁移**的结论写回 `lab/findings.yaml`,
   每条都要写清楚**什么情况下会失效**。

硬规矩:方向只在训练段定一次;所有钱的数字扣 15 bp 并给换手;留出段有台账;
原始结果不覆盖;判据一律实测,不写死名单。

## 接手一个做到一半的研究(或一整个批次)

**先读 `handoff/README.md`**。研究是接力做的:总领(Opus 5.5)/ 主研(Opus 5)/ 执行(Sonnet 5),彼此只靠文件传话;
agent 的推理不落盘,所以每一步都要写进 `notes/<fid>/state.md`(现状)和 `notes/<fid>/journal.md`(日志)。
`cat handoff/STATUS.md` 看全局,`./scripts/study.sh brief <fid>` 看一条因子,`docs/study_playbook.md` 是操作手册
(§0 选拔口径 = 多头腿净超额;§7 研究日志与交接)。
