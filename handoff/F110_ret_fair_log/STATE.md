# F110_ret_fair_log — 交接状态

_自动生成于 2026-10-04 23:03(`python scripts/recorder.py --brief F110_ret_fair_log` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:手写 ret_fair_log(批次 B01_single_factors)
- 表达式:`mul(sub(div(day_last(Close), day_first(Open)), 1), abs_(sub(day_mean(in_sustain_stddev(is_gt(sub(log(Volume), in_forward_valid_part(log(Volume))), add(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)), day_mean(in_sustain_stddev(is_lt(sub(log(Volume), in_forward_valid_part(log(Volume))), sub(in_mean_full(sub(log(Volume), in_forward_valid_part(log(Volume)))), in_stddev_full(sub(log(Volume), in_forward_valid_part(log(Volume)))))), Ret, 5)))))`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- 留出段:**还没读过**(只能读一次;读之前要在 `10_distilled.md` 里写下候选排序和判据)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `lead:F110_ret_fair_log#3`:失败,最后动作 10-04 15:42 → `handoff/F110_ret_fair_log/agents/lead_R3_a6bd5c7dcb41ba2f7.md`
  - `lead:F110_ret_fair_log#3`:失败,几乎没做事
  - `lead:F110_ret_fair_log#1`:还在跑(多半就是你自己)

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F110_ret_fair_log` 看服务器上的 tag,`./scripts/study.sh digest F110_ret_fair_log <tag>` 重看结果)。

## 研究现状(`notes/F110_ret_fair_log/state.md`,10-04 14:53 更新)—— **先读这个文件**

# F110_ret_fair_log — 研究现状(主研第 4 轮重写,2026-10-04)

> **轮次说明**:`journal.md` 里主研已经写过「第 1 / 2 / 3 轮」,本轮是**第 4 位主研**(工作流自己数的是「第 2 轮」——
> 工作流重启过,别被它的计数搞混;**以 `journal.md` 的条数为准**)。本轮下的工单是 **R2**。
> 事实类 notes(`01_expression.md`、`02_operators.md`、`03_decomposition.md`、`04_grammar.md`、`06_baseline.md`)仍然有效,照用、不要重写,
> 但 **02 / 03 里「成交量脉冲处的价格冲击」那个读法已经被实测彻底推翻**(见本页 2.4):
> 整条成交量事件机器不带信息。假设表全文 + 两轮裁决在 `05_hypotheses.md`;R1 结果的完整解读在 **`07x_01_x1_anatomy.md`**(先读它)。
> **本轮是第一次拿到 C/D/E 三段的结果**(R1 的两次 exec 终于跑成,exit 0),所以本轮把假设表大改了一遍:
> H9 被否定、H2/H4/H5/H6 被支持、H1/H13 被改写、H10/H14 被否定,并新增 H15/H16/H17。

## 1. 一句话现状

**原式对只能做多的用户没用,而且已经知道为什么;研究现在只剩两问 —— ①把平滑写进表达式之后新候选能不能站住
②它相对已知家族有没有增量。工单 R2 就是去拿这两样的,拿到之后下一轮就可以读留出段。**

R1 的两次运行(`x1c` = `0 B D`、`x1d` = `C E`,都 exit 0,canary 逐项对上)确立了三件事:
(a)**原式的多头腿扣费后是零,延长半衰期救不了它** —— hl20 之后毛超额掉得和换手省的一样快,hl20 本来就是最优点,
基线里「hl 0→20 每翻倍 +6~8 个点」那条曲线 100% 是成本的功劳(H9 **被否定**);
(b)**整条成交量事件机器是死重** —— 权重 `S` 换成 `|D|` 每一项都更好、换成 `σ`/`σ²` 也不差,
把波动尺度从 `S` 里除掉反而变差(H2 **被支持**);提纯的终点是 `mul(D, abs_(D))`,6 个算子,`Volume`/`Ret` 两个字段全多余;
(c)**空头腿和多头腿住在不同的持有期上** —— 空头腿是 lag 0~3 天的快反转(`sh` 从 +43.7% 掉到 lag 5 的 +6.0%),
多头腿在 lag 0~10 全为负、只有 lag 20~40 才转正(新读数,事前没想到)。这才是「多头腿为什么不行」的真正答案。

**唯一还活着的多头腿改进来源:把平滑写进表达式**(`cross_mean` 盒式 + 口径里的 `EMA`)。
R1 的 numpy 读数:`cross_mean(D,20)+EMA20` → `Ln +4.9% / +7.4%`(`Lshp +0.75 / +0.93`,`LTO 3.6%`),
全研究最高。但它只有已知家族 `cross_mean(day_std(Amt),30)` 同口径的三分之一(train `+12.6% / +1.78`,valid `+22.3% / +3.46`)。
**所以结论能不能是正面的,全看「相对已知家族有没有增量」。**

**下一步:执行 R2**(`orders/R2.md`,kind: experiment,2 次服务器运行 = `run S1_long`(8 个表达式变体)+ `exec x2`(`G H I` 三段))。

(…全文 22746 字符,读 `notes/F110_ret_fair_log/state.md`)

## 研究日志(`notes/F110_ret_fair_log/journal.md`:16 条,其中研究员自己写的 7 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 15:04 [auto] 启动 run S1_long:阶段 S1_long

### 2026-10-04 15:05 [auto] 启动 exec x2:studies/F110_ret_fair_log/x1_anatomy.py G H I

### 2026-10-04 15:09 [auto] S1_long 跑完(exit 0);重看结果:./scripts/study.sh digest F110_ret_fair_log S1_long

### 2026-10-04 15:09 [auto] x2 跑完(exit 0);重看结果:logs/F110_ret_fair_log_x2.log

### 2026-10-04 15:25 [执行] R2:两次运行(S1_long、exec x2 的 G H I)都 exit 0 无中断;Q1 canary 四项全部吻合;Q2/Q3/Q4/Q5 数字都拿到,但判据只部分满足

两次服务器运行:run S1_long(8 变体)exit 0/241.5s;exec x2(x1_anatomy.py G H I)exit 0/127s。脚本按工单
E1~E5 做了 5 处 dict 加/删改动(行号见结果卡),check 20/20 OK,无求值失败,无变体跌破 cov/dist 门槛,无变体符号异常。

Q1 canary:w_cmD20 固定 hl20 多头腿净超额 train +5.2%(numpy 预测 +4.9%)/valid +7.3%(预测 +7.4%);
w_cmT20 train +4.2%(预测 +3.6%)/valid +5.7%(预测 +5.7%);rank corr(w_cmD20,v_base)=+0.642、
rank corr(w_cmT20,v_base)=+0.896,两个 corr 与 numpy 预测精确吻合到小数点后三位。四项全部未标红,桥通。

Q2(权重):同窗口 20,四权重 train Lnet 4.2/5.2/7.5/7.9%,valid 5.7/7.3/9.5/8.1%(w_cmT20/w_cmD20/w_cmDsig20/w_cvxD20)。
S 权重(w_cmT20,原式权重)是四者中最低而不是最高,train/valid 跨度 3.7/3.8pt,略超工单说的"±3 点内"参照。

Q3(H15,砍最近10天):w_cmD20lag10 对 w_cmD20 的 Lgross 差 train -1.6pt / valid -2.0pt(都在±3点内),
但 LTO 两者完全相同(3.6%=3.6%),不是"更低"——两个子判据只满足一半。

Q4(H17,是否就是20日反转):rank corr(w_cmD20,w_cmDcc20)=+0.669(<0.9 门槛);两本书差距 train 4.1pt(超噪声带)、
valid 1.2pt(噪声带内),两段方向不一致。

Q5(H8+H11,已知家族增量):known 单独 Ln +12.6%/+22.3% Lshp +1.78/+3.46;known+0.5×cm20 Ln +13.3%/+20.0%
Lshp +1.97/+3.18 —— train 小幅升、valid 降;cm20 残差(cm20|k
…(这条日志还有后文,读 journal.md)

## 工单与结果卡(`notes/F110_ret_fair_log/orders/`、`notes/F110_ret_fair_log/results/`)

- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F110_ret_fair_log.yaml`)

- 标题:日内收益 × |放量后波动 − 缩量后波动|:按『成交量跳变处的价格冲击』加权的日内收益累积(方向为负 = 加权的月度日内反转)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_long**(8 个变体):把平滑写进表达式(cross_mean 盒式 + 口径里的 EMA)之后,多头腿能不能站住?权重支路还重要吗?它是不是就是 20 日反转?
  w_cmT20、w_cmD20、w_cmDsig20、w_cvxD20、w_cmD60、w_cmD20lag10、w_cmDcc20、w_known30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F110_ret_fair_log`)

- `S0_baseline`  10-04 11:53  1 个变体  → `./scripts/study.sh digest F110_ret_fair_log S0_baseline`
- `S1_long`  10-04 15:08  8 个变体  → `./scripts/study.sh digest F110_ret_fair_log S1_long`
- `x1`(自写脚本的输出)  10-04 13:07  exit 97  → `logs/F110_ret_fair_log_x1.log`
- `x1c`(自写脚本的输出)  10-04 14:05  exit 0  → `logs/F110_ret_fair_log_x1c.log`
- `x1d`(自写脚本的输出)  10-04 14:09  exit 0  → `logs/F110_ret_fair_log_x1d.log`
- `x2`(自写脚本的输出)  10-04 15:07  exit 0  → `logs/F110_ret_fair_log_x2.log`

## 已写的 notes(`notes/F110_ret_fair_log/`)

`01_expression.md`(1K)、`02_operators.md`(4K)、`03_decomposition.md`(3K)、`04_grammar.md`(2K)、`05_hypotheses.md`(17K)、`06_baseline.md`(4K)、`07_S1_long.md`(8K)、`07x_01_x1_anatomy.md`(14K)、`07x_02_x2_GHI.md`(8K)、`journal.md`(21K)、`state.md`(34K)

## 自写的探针与分析脚本(`studies/F110_ret_fair_log/`)

- `probes.py`  10-04 12:14  Probes this tree needs:  D * | M - Q |
- `x1_anatomy.py`  10-04 15:04  F110 X1: anatomy of  T = D * |M - Q|  and of the signal that is actually traded, -EMA20(T).

## 结构化结果(`handoff/F110_ret_fair_log/results/`)

(还没有)
