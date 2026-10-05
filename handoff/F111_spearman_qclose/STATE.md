# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-05 13:33(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-05 12:04)—— **不许再读**。候选在留出段上的数全在 `runs/F111_spearman_qclose/final.json`(`./scripts/study.sh digest F111_spearman_qclose final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `work:F111_spearman_qclose#1`:已返回结果,最后动作 10-05 00:09 → `handoff/F111_spearman_qclose/agents/work_R1_aae62ed0fb3b82fe7.md`
  - `lead:F111_spearman_qclose#2`:中断,最后动作 10-05 00:20 → `handoff/F111_spearman_qclose/agents/lead_R2_aeedf79bbeec0a00f.md`
  - `synth:F111_spearman_qclose`:已返回结果,最后动作 10-05 11:20 → `handoff/F111_spearman_qclose/agents/synth_a763c4b39efb8321d.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F111_spearman_qclose` 看服务器上的 tag,`./scripts/study.sh digest F111_spearman_qclose <tag>` 重看结果)。

## 研究现状(`notes/F111_spearman_qclose/state.md`,10-05 11:18 更新)—— **先读这个文件**

# F111_spearman_qclose 研究现状

> 主研每轮**覆盖重写**。最后更新:**2026-10-05,工作流第 2 轮主研**(批量扫描 s1 的综合)。
> `ts_spearman(day_quantile(Close), 10)`,挖掘库 #953。本轮的完整论证在
> `notes/F111_spearman_qclose/synthesis.md`(**先读它**);第二批假设在
> `studies/F111_spearman_qclose/hypo.yaml`(34 条,34/34 parse)。
> 旧的逐轮实验文件(`04_grammar.md`、`05_hypotheses.md`、`06_baseline.md`、`07_*`、`results/R1.md`)仍在,
> 但**凡与批量扫描 s1 的大表冲突,以大表为准**(用户规矩)。

## 1. 一句话现状

身份、承重件、市场分布**都已定清**。结论是**否定性的但有证据**:对纯多头用户,F111 **不是可单独上的因子,
也量不出相对已知成交额族的增量**(ov_m025 +15.6%/2.32 vs k_known +15.4%/2.22,全在噪声内)。
唯一还没量过、值得再花一次服务器时间的口径:**已知族定流动性倾斜 + f 只做桶内排序**(`h_ov_bk` / `h_ov_bk05`)。
留出段**一个数字都没读过**。

## 2. 中间结果(全部来自 `study.sh table F111_spearman_qclose s1`;噪声 ±3pp / ±0.3)

- **原式**:+10.4/+17.0/+12.3%(tr/va/ut),Lshp 1.79/3.07/2.15,LTO 4.1%,ρk +0.42,空头腿毛 +23.4/+31.2%
  (钱主要在空头腿,纯多头只吃到小半 —— 硬上限)。
- **承重件只有根上的 `ts_spearman`**:ts_skew +2.8 / ts_var +2.3 / ts_std +0.7 / ts_rank −3.4 / ts_argmax −11.5 /
  ts_kurt −13.0;叶子 `iso_A = day_quantile(Close)` 单独只 +5.8%、ρo 0.22。
- **多余的**:日内折叠整层(day_last/day_close **+13.2% 最好**、q25 +12.8、min +12.5、first +12.2、median=base、max +11.4,
  全在噪声内;换成非价格水平就塌:day_gini +6.1、day_skew +4.6);四个价格叶子 Open/Low/High/Vwap ρo **1.00**;
  外层日轴记忆**一条都没超过原式**(最好 decay_linear60 +12.2);`cs_winsor` 恒等(corr 本来有界)。
- **窗口**:5 → +10.2(dist ✗)、10 → +12.3、**20 → +12.7**、30 → +11.5;平台宽、峰在 20,LTO 4.1→3.0→2.6%。
- **水平承重、变化是毒药**:cross_zscore 5/10/30/60 = −14.6/−10.3/−3.0/−1.0,cross_stddev 全负,rel60 −3.9
  ⇒ 它是**持久的股票属性**,不是事件。折叠(abs_/pow_2)全塌 ⇒ 单调。
- **解剖最重要的一格(按 20 日成交额,段内净超额 / 括号=超配)**:
  最低 20% **−0.1%(+30.3%)**、20-40% −2.2%、40-60% +1.8%、60-80% +3.2%、**最高 20% +9.5%(−16.7%)**;
  已知族同一列 −4.1/−5.3/−8.2/−5.2/**+2.5%**、最低桶超配 **+80.3%**。
  ⇒ **两条因子重叠的那部分(低流动性倾斜)恰恰是 f 自己没本事的部分;f 会选股的地方正是已知族空白的地方。**
- 其他分段:市值中小更好(最高 20% 只 +2.4%);创业板 +14.4 > 深主板 +13.5 > 沪主板 +11.2 > **科创板 −3.6**;
  **次新(7.1%)段等权 −28.7% 但段内选股力最强 +16.9%**;**近 15 日有冻结盘口(6.5%)段等权 −67.4%、段内 −38.7%**(f 在那里挑到最差的)。
- 时间:2018 +16.9 / 2019 +7.8 / **2020 +1.6** / 2021 +15.7 / 2022 +16.4 / 2023H1 +18.2;
  市场上涨 +17.4 vs 下跌 +5.9;放量 +17.4 vs 缩量 +8.3;高离散 +15.1 vs 低 +9.6。
- **增量**:ov_m025 +15.6%/**2.32** vs k_known +15.4%/2.22(**噪声内**);反向掺(ov_p025 +9.4%/1.37)大幅变差 ⇒
  方向是真的、量不出增量。res_known +5.9%/1.09、res_liq +6.6%/1.22(bk_* 因并列 dist ✗,数字同档)。
  上一轮:对 9 个标准控制变量**一起**中性化后多头腿毛 +13.6% → **+0.1%**。

## 3. 过程与逻辑(这一轮做了什么)

读源码 + 代数化简把根节点解掉(§8 第 2 条)→ 对照大表把「承重 / 多余 / 可互换 / 平台」四类一次分完 →
从市场解剖读出「选股力随流动性单调上升、而持仓压在最不流动端」这条不对称 → 据此把增量问题从「加权叠加」
重新提成「倾斜 vs 桶内排序」→ 写 34 条第二批假设。**没有起任何服务器计算**(只用 `study.sh table/src/ops/hypo`)。
身份的结论与上一轮的数值结果(逐日 Spearman 1.0000、ρ^time 单独 −5.60% / 乘 c(t) 后 +18.62%)一致,互为佐证。

## 4. 假设表(第二批 34 条,全文在 `studies/F111_spearman_qclose/hypo.yaml`)

六组:A 便宜内核与最好结构的组合(h_sp_last20、h_pe_last40…);B 并列伪影与冻结盘口(h_wmean_carrier、h_excl_flat…);
C 机制 c(t)×自身趋势(**h_mkt_explicit / h_mkt_undo / h_relpath** —— 这三条一跑就能定案机制);
D 换载体 Ret↔成交额变化率(**h_ret_path** 区分 beta 与条件动量);E 把解剖写进表达式(**h_ov_bk / h_f_excl_illiq / h_act_bucket**);
F 叠加(h_stack_liq、h_stack_flat)。
**优先级**:h_ov_bk > h_mkt_explicit > h_ret_path > h_f_excl_illiq > h_excl_flat > h_sp_last20 > 其余。

## 5. 候选(读留出段之前的排序)

1. **ov_m025**(已知族 + 0.25 权重的 f)—— 全表最好,但相对 k_known 的优势在噪声内,**必须写成「没有量出增量」**。
2. **sub_A_day_last / h_sp_last20**(`ts_spearman(day_last(Close), 20)`)—— 原式的提纯版,同口径下 +0.9~+1.4pp。
3. **k_known** 本身 —— 任何 final 都必须带上它做基准。
判据:若候选在留出段相对 k_known 的多头净超额差 < 3pp 且夏普差 < 0.3,就判「没有增量」。

## 6. 后面的思路

最有价值的一次运行是把第二批里 **C 组 + E 组**一起跑(机制定案 + 增量口径),A/B/D/F 作为同一张表的陪跑。
若 h_mkt_explicit 复现 f,则这族因子脱离 O(N²),可以开更长窗口;若 h_ret_path 也成立,说明真正的对象是「秩 beta」,
应该换一条主线去做而不是继续提纯 F111。

## 7. 留出段

**没读过,一次都没有。** 读之前候选、排序、判据按 §5 写死。

## 8. 给接手者的提醒

- **先读 `synthesis.md`,不要先读旧的 07_* 文件**(它们来自小样本逐轮实验)。
- `ts_spearman` 名为时序、`arity=1`,**实为跨股票两两**(`nd_ts.py:483` 有 `for i in range(N)`);
  `day_quantile` 默认 q=0.5 **就是 day_median**。两处都会把人骗过去。
- 代数事实:完整窗口上各股秩向量都是 0..d−1 的排列、**σ_j 是同一个常数** ⇒
  `mean_j corr(R_i,R_j) ∝ corr(R_i, 等权共识秩路径)`,**两两配对里没有配对信息**。
- 实现伪影:`stable=True` 排序把**并列按时间先后给秩** ⇒ 10 天不动的价格路径 ≡ 完美单调上升,
  在上涨窗口里被打满分。上一轮量过:它不承担毛收益,但承担「低换手」(剔除并列后 LTO 4%→23%)。
- **`ts_spearman` 在 d=50 上 OOM(上一轮连挂两次 exit 97),d=30 跑得成**;长窗口一律走 `ts_pearson`(分块、峰值有预算上界)。
- `ts_*` 窗口池 [1,5,10,20,30,40,50],`cross_*`/`in_*` 是 [3,5,10,15,30,60,241] —— 别写 `cross_mean(x, 20)`。
- 空头腿虚高的坑(次日封板标签 NaN)只影响多空口径;这条因子的空头腿本来就大,**别拿它论证纯多头可用**。

## 研究日志(`notes/F111_spearman_qclose/journal.md`:20 条,其中研究员自己写的 10 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-04 23:52 [auto] 启动 exec x2_increment:studies/F111_spearman_qclose/x2_increment.py

### 2026-10-04 23:58 [auto] x2_increment 跑完(exit 0);重看结果:logs/F111_spearman_qclose_x2_increment.log

### 2026-10-05 00:06 [执行] R2:S2_window(删w_last_50后7个变体)和x2_increment(block A-E)都exit 0,结果卡见results/R2.md

第1项 S2_window:按修订R2-a删掉w_last_50(4处:variants/corr_ids/neutralise/profile)后reran,
exit 0,290.2s,peak anon 5.36GiB(此前两次exit 97的w_last_50已彻底移除)。BESTW按改动2规则选出
p_last_30(=ts_pearson(day_last(Close),30)),hlL=3,Lnet train+11.6%,5个候选里最高。

第2项 x2_increment.py(新写):F1=ts_spearman(day_last(Close),10)固定,F2=BESTW=p_last_30。
block A组合书30行:w=1时3条known家族逐位一致(F1 Lnet_tr+10.38%,F2 Lnet_tr+12.41%,PASS);
w=0行与R1数字14接近但不逐位相等,差值量级(Lnet -0.57~-0.67pp,Lshp -0.08~-0.09)落在R1自己
记录的0.3~0.9pp区间内,known_stdamt_max9这条hlL从5变2、LTO差1.6~1.9pp,比另两条家族明显大。
block B双重排序5本书:30%池覆盖率约0.29~0.30、多头端中位105~140只;10%池覆盖率约0.097、
中位35~46只,F1在两条known家族上单侧LTO都偏高(14.75%~19.44%)。block C残差(6行,主口径①):
F1对3条known家族R²=0.066/0.111/0.101(与R1的v_base版0.068/0.109/0.101高度吻合),F2对应R²=
0.127/0.126/0.129——F2的原始面板R²比F1高,但S2_window的rank_corr_train(平滑交易信号口径)显示
F1对known家族的|相关|反而比F2高(0.35~0.41 vs 0.30~0.35),两个口径排名相反,已写进结果卡"值得
注意"。block D:F1多头端(Q10)在ctl_amt/ctl_cap/ctl_ivol/ctl_dvol20/known_stdamt_mean30上全部
单调降到最低百分位(0.28~0.42),即多头端是"更不活跃更小更低波动"的票。block E:
…(这条日志还有后文,读 journal.md)

### 2026-10-05 00:07 [执行] R2 勘误:上一条日志的服务器运行计数写错了,更正如下

上一条[执行]日志里"全研究累计6次...还剩4次"这句话前后口径不一致,混用了两种计数方式,更正:

playbook §4 原文:"全研究的服务器运行控制在 8 次以内(含 final；不含预先跑好的 S0)"。按这个口径(不算
S0,S2_window 两次 exit 97 的中断重试按同一个 tag 只算一次,不是三次),已用的是:S1_whatis(1)+
x1_identity(2)+S2_window(3,本轮跑成)+x2_increment(4)= 4 次,与工单原文"都 exit 0 之后全研究还剩
4 次(含最后的 final)"的说法一致(8-4=4)。上一条日志里把 S0 和 S2_window 的两次 exit 97 也计入
"累计6次"是我自己多算的,不是这项研究的计数口径,后面不要沿用那句话里的"6次"。

### 2026-10-05 11:16 [主研] 批量扫描 s1 的综合

身份(源码+代数,已坐实):ts_spearman 名为时序实为跨股票(nd_ts.py:483 有 for i in range(N));day_quantile 默认 q=0.5 即日内中位价。
完整窗口上各股秩向量都是 0..d-1 的排列、σ_j 为同一常数 ⇒ mean_j corr(R_i,R_j) ∝ corr(R_i, 等权共识秩路径);O(N²) 配对里没有配对信息。
⇒ f ≈ (自己 10 日路径的单调趋势) × (市场 10 日路径方向),一条被市场方向翻符号的动量;与上一轮 ρ^time 单独 −5.60% / 乘 c(t) 后 +18.62% 一致。
承重件只有根上的 ts_spearman(换任何别的 ts_* 全塌:skew +2.8 / var +2.3 / rank −3.4 / kurt −13.0;叶子 iso_A 只 +5.8、ρo 0.22);
日内折叠整层多余(day_last/close/q25/min/first/max 全在噪声内,day_last +13.2 最好)、四个价格叶子 ρo=1.00 完全互换、窗口平台 10–20(峰 20:+12.7)。
水平承重变化是毒药:cross_zscore5 −14.6、stddev 全负、rel60 −3.9 ⇒ 它是持久属性不是事件。stable 排序把并列按时间给秩 ⇒ 「平」≡「完美上升」,冻结盘口段段内 −38.7%。
解剖最重要的一格:按成交额,段内选股力 −0.1/−2.2/+1.8/+3.2/+9.5%(单调升),而书在最低桶超配 +30.3% —— 与已知族重叠的流动性倾斜恰恰是 f 没本事的那一段。
增量:ρk 0.42、ov_m025 +15.6%/2.32 vs k_known +15.4%/2.22(噪声内)、res_known +5.9%/1.09 ⇒ 多头腿上没有可量出的增量;唯一没试过的口径是「已知族定倾斜 + f 只做桶内排序」(h_ov_bk)。
已交:notes/synthesis.md、studies/hypo.yaml(34 条,34/34 parse)。

## 工单与结果卡(`notes/F111_spearman_qclose/orders/`、`notes/F111_spearman_qclose/results/`)

- R0:工单 —,结果卡 有
- R1:工单 有,结果卡 有
- R2:工单 有,结果卡 有

## 配置里的实验计划(`configs/F111_spearman_qclose.yaml`)

- 标题:(读完这棵树之后,用一句话写它是什么)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_whatis**(6 个变体):ts_spearman 的全市场两两配对平均,等价于什么更简单的东西?预测力的载体是价格路径、活跃度,还是实现细节?
  m_mktcorr、s_pearson、l_mean、l_last、l_amt、t_tsrank
- **S2_window**(7 个变体):窗口 d 这根轴上有东西吗?10 天只是任意选择,还是 5~50 里有一个明显更好的频段?
  a_last_10、w_last_5、w_last_20、w_last_30、w_q_30、pl_last_10、p_last_30

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F111_spearman_qclose`)

- `S0_baseline`  10-04 11:54  1 个变体  → `./scripts/study.sh digest F111_spearman_qclose S0_baseline`
- `S1_whatis`  10-04 14:05  6 个变体  → `./scripts/study.sh digest F111_spearman_qclose S1_whatis`
- `S2_window`  10-04 23:34  7 个变体  → `./scripts/study.sh digest F111_spearman_qclose S2_window`
- `sweep_s1`  10-05 10:54  73 个变体  → `./scripts/study.sh digest F111_spearman_qclose sweep_s1`
- `anatomy_s1`  10-05 10:58  0 个变体  → `./scripts/study.sh digest F111_spearman_qclose anatomy_s1`
- `sweep_s2`  10-05 11:46  117 个变体  → `./scripts/study.sh digest F111_spearman_qclose sweep_s2`
- `anatomy_s2`  10-05 11:52  0 个变体  → `./scripts/study.sh digest F111_spearman_qclose anatomy_s2`
- `sweepfinal_s2`  10-05 12:06  8 个变体  → `./scripts/study.sh digest F111_spearman_qclose sweepfinal_s2`
- `x1_identity`(自写脚本的输出)  10-04 14:23  exit 0  → `logs/F111_spearman_qclose_x1_identity.log`
- `x2_increment`(自写脚本的输出)  10-04 23:58  exit 0  → `logs/F111_spearman_qclose_x2_increment.log`

## 已写的 notes(`notes/F111_spearman_qclose/`)

`01_expression.md`(3K)、`02_operators.md`(9K)、`03_decomposition.md`(4K)、`04_grammar.md`(11K)、`05_hypotheses.md`(34K)、`06_baseline.md`(12K)、`07_S1_whatis.md`(7K)、`07x_1_identity.md`(14K)、`journal.md`(34K)、`state.md`(6K)、`synthesis.md`(12K)

## 自写的探针与分析脚本(`studies/F111_spearman_qclose/`)

- `x1_identity.py`  10-04 14:17  R1 exec script -- the identity + conditioning + known-family + tie analysis.
- `x2_increment.py`  10-04 23:51  R2 exec script (修订 R2-a) -- block A/B/C/D/E: does F1/F2 give a long-only user

## 结构化结果(`handoff/F111_spearman_qclose/results/`)

- `synthesis.json`
