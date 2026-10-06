# F111_spearman_qclose — 交接状态

_自动生成于 2026-10-05 19:23(`python scripts/recorder.py --brief F111_spearman_qclose` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #953(批次 B01_single_factors)
- 表达式:`ts_spearman(day_quantile(Close), 10)`

## 现在到哪一步

- **阶段:研究进行中(还没有结构化结论)**
- **留出段已经读过 1 次**(10-05 12:04)—— **不许再读**。候选在留出段上的数全在 `runs/F111_spearman_qclose/final.json`(`./scripts/study.sh digest F111_spearman_qclose final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F111_spearman_qclose`:已返回结果,最后动作 10-05 11:20 → `handoff/F111_spearman_qclose/agents/synth_a763c4b39efb8321d.md`
  - `verdict:F111_spearman_qclose`:失败,最后动作 10-05 15:35 → `handoff/F111_spearman_qclose/agents/verdict_a3cee9f79f0862f8e.md`
  - `verdict:F111_spearman_qclose`:失败,最后动作 10-05 16:40 → `handoff/F111_spearman_qclose/agents/verdict_a3cea9cf2904fa486.md`

**接手的人该做什么:** 研究还没做完。先读下面的研究日志和已有的 notes,**接着做**,不要推倒重来;已经跑过的阶段不要重跑(`./scripts/study.sh list F111_spearman_qclose` 看服务器上的 tag,`./scripts/study.sh digest F111_spearman_qclose <tag>` 重看结果)。

## 研究现状(`notes/F111_spearman_qclose/state.md`,10-05 16:10 更新)—— **先读这个文件**

# F111_spearman_qclose 研究现状

> 主研每轮**覆盖重写**。最后更新:**2026-10-05,工作流第 3 轮主研**(批量扫描 **s2** 的对账与定论)。
> `ts_spearman(day_quantile(Close), 10)`,挖掘库 #953。完整论证在 `notes/F111_spearman_qclose/synthesis.md`
> —— **先读它的「## 第二轮(s2)对账与结论」**(80 行,本轮全部结论都在里面;前面 §1–§5 来自 s1 那一轮,
> 凡与 s2 冲突以 s2 为准)。假设表:第二批 `studies/F111_spearman_qclose/hypo.yaml`(34 条,已跑完 = s2);
> 第三批 `studies/F111_spearman_qclose/hypo3.yaml`(25 条,25/25 parse,**还没跑**)。
> 旧的逐轮实验文件(`04_grammar.md`、`05_hypotheses.md`、`06_baseline.md`、`07_*`、`results/R1.md`)仍在,
> 但**凡与批量扫描大表冲突,以大表为准**(用户规矩)。**留出段一个数字都没读过**(`sweepfinal_s2.json` 没打开)。

## 1. 一句话现状

**定论已下,方向性是否定的,但留了一个必须补的格子。** F111 = **秩口径的短期市场同步性**
(自身 10~20 日路径与全市场等权共识秩路径的相关)。提纯**成功但很小**:唯一站得住的改动是剔掉
「近 15 日出现过冻结盘口」的 20%(`seg_xfrozen_p` +13.5% / 2.46,ρk 0.42→**0.11**)。升华**失败**:
建在已知族上的任何用法(+15.5~15.6% / 2.32~2.35)对 `k_known`(+15.4% / 2.22)在噪声内,
对通用筛子基准 `k_known_xfrozen`(+18.5% / 3.15)**明确落后 2.9~3.0pp / 0.80~0.93 夏普**。
**唯一的缺口**:s2 的叠加全都只叠在 `k_known` 上,「叠在 `k_known_xfrozen` 上」一格都没量过 ⇒
「无增量」目前只对 `k_known` 口径成立、对正确基准**待定**,靠 `h3_xfz_plus_f` 定案。

## 2. 中间结果(全部来自 `study.sh table F111_spearman_qclose s2 --all`;噪声 ±3pp / ±0.3;ut 口径)

- **基准**:v_base +12.3% / 2.15(LTO 4.1%、ρk 0.42、空头腿毛 +23.4/+31.2%)、k_known +15.4% / 2.22、
  **k_known_xfrozen +18.5% / 3.15**(= 已知族剔掉近 15 日冻结最重的 20%,本轮才出现的通用筛子基准)。
- **自己最好的三个**:`seg_xfrozen_p` +13.5% / **2.46**(ρo 0.53、**ρk 0.11**、LTO 4.4%)>
  `h_pe_last20` = `ts_pearson(day_last(Close), 20)` +13.2% / 2.37 > `sub_A_day_last` +13.2% / 2.29。
  相对 v_base 只高 0.9~1.2pp / 0.1~0.3 夏普 —— **都在噪声边缘**,只有 ρk 0.42→0.11 是噪声解释不掉的。
- **`seg_xfrozen_p` 的收益来自哪**:填的是 f 最弱的两年(2019 +14.0% vs base +7.8%、2020 +4.4% vs +1.6%),
  代价 2022 −3.6pp ⇒ **夏普涨来自年度更平、不是整体抬升**;冻结持仓 6.5%→1.3%,五个成交额桶的桶内
  选股力全部抬高。但剩下那 1.3% 里它挑得更差(段内 −38.7% → −92.8%)⇒ **只切暴露、没修机制**。
- **六条 s1 推论的对账**:(i) 抽掉共同成分 ⇒ 塌 **支持**(`h_relpath` +0.9% / 0.12);(ii) 再乘一次市场方向 ⇒
  反转 **支持**(`h_mkt_undo` −9.1%);(iii) 显式 O(N) 等价物 **否定**(`h_mkt_explicit` −0.9%,居中点代理错了);
  (iv) 个股层面「放量才有效」**否定**(`h_act_mul` +4.0%、`h_act_add` +1.3%);(v) 冻结筛子 **想法支持 / 我的写法否定**
  (我的 `cross_mean` 版 +11.3~11.8%,通用 `cross_max` 版 +13.5%);(vi) day_last 的 0.9pp 来自少并列 **否定**
  (`h_wmean_carrier` +12.8%、ρo 0.99)。
- **四条新事实**:① `ts_pearson` 与 `ts_spearman` ρo 0.98 ⇒「秩」不承重,且能跑 d=40 ⇒ **窗口平台 10≈20>30>40**;
  ② s1「书压在低流动端是浪费」**反了** —— `h_f_excl_illiq` +6.4%、`h_stack_liq` +7.0% 都腰斩,**f 多头净超额的
  一大半是流动性倾斜本身**;③ **筛子不对称**:已知族剔掉 f 最低 20%(`scr_xhi_m`)+15.5% 等于白剔、剔掉 f 最高 20%
  (`scr_xhi_p`)塌成 **+5.3% / 0.80、LTO 11.5%** ⇒ **已知族多头腿本来就压在 f 的高分区里**,ρk 0.42 低估了多头腿重叠;
  ④ 载体换成**日收益**路径只掉 1.3pp(`h_ret_path20` +11.0% / 2.00、多空 valid 3.89 全表最高)⇒ 承重的是
  **与市场同步(秩 beta)**,不是价格路径单调。
- **空头腿的钱在哪**:三条剔除写法把空头腿 valid 从 +31.2% 打到 −8.3% / −8.4%、多头腿几乎不动 ⇒
  **+31% 全部来自那 6.5% 冻结票**;`h_excl_young` 同样打到 +14.2% ⇒ 那 6.5% 与次新高度重叠(新股一字板)。

## 3. 过程与逻辑(这一轮做了什么)

只用 `study.sh table/hypo3`,**没有起任何服务器计算**。先把 s1 综合里六条推论逐条对到 s2 的变体 id 和数字上
(含两处「大表会把人骗过去」的坑,见 synthesis §5),再用 `scr_xhi_m` / `scr_xhi_p` 的不对称和 `h_ret_path20`
补出两条 s1 没有的事实,最后发现 s2 的增量口径全建在 `k_known` 而不是本轮才出现的 `k_known_xfrozen` 上 ⇒
把这一格写成第三批里优先级最高的 `h3_xfz_plus_f`。第三批 25 条全是**只有第四批新算子才写得出**的,
或本轮结果直接指向的最小子结构替换。

## 4. 假设表(第三批 25 条,全文在 `studies/F111_spearman_qclose/hypo3.yaml`,25/25 parse)

九组:A 最好的两件事叠起来 + 筛子档位 / 窗口(`h3_best2` / `h3_xfz40` / `h3_xfz_w60`);
B 「冻结」到底是什么事件(`h3_xfz_flatmax` 单格定案 `cross_max` vs `cross_mean`、`day_at_max_ratio` /
`day_at_min_ratio` 分开涨停跌停、`cross_flat_ratio` 量日间并列、`day_distinct_ratio` 量价格格子粗细);
C 伪影单独计价(`h3_flat_iso` / `h3_f_minus_flat`);D 桶内 z 分数 / 去均值保留幅度(`h3_bkz_*` / `h3_bkd_*`);
E `cross_age` 代替饱和的 `valid_count`;F 市场状态写进表达式(`cs_state_rank` / `cs_flip_by_state` /
`select_where`)+ **`h3_xfz_plus_f`**;G day_last 那 0.9pp 的两个解释(`day_topw_mean` / `in_index`);
H 稳健标准化(`cross_madz` / `cs_robust_z`);I 收益路径线(`h3_ret_pe40` / `h3_ret_xfz`)。
**优先级**:`h3_xfz_plus_f` > `h3_best2` > `h3_xfz_flatmax` > `h3_bkz_age` > `h3_sel_dir` > `h3_robust_path` > 其余。

## 5. 候选(读留出段之前的排序,判据写死在这里)

1. **`k_known_xfrozen`** = `cs_last_high20(neg(cross_mean(day_std(Amt), 30)), cross_max(day_zero_ratio(Ret), 15))`
   +18.5% / 3.15 —— **全表最好,但它不含 f**;任何 final 都必须带它做基准,而不是只带 k_known。
2. **`seg_xfrozen_p`** +13.5% / 2.46、ρk 0.11 —— 本因子唯一站得住的提纯,价值在**低相关的备选腿**,不在业绩。
3. **`h_pe_last20`** +13.2% / 2.37 —— 便宜内核(`ts_spearman` d=50 OOM,`ts_pearson` 跑得了 d=40)。
**判据**:候选在留出段相对 **k_known_xfrozen** 的多头净超额差 < 3pp 且夏普差 < 0.3 ⇒ 判「没有增量」。
若 `h3_xfz_plus_f` 跑出来 ≈ +18.5% / 3.15,则「无增量」升级成对正确基准成立,这条因子可以收尾。

## 6. 后面的思路

一次运行的最高价值组合:**`h3_xfz_plus_f` + `h3_best2` + `h3_xfz_flatmax` + `h3_bkz_age`**(正确基准的增量 +
两件好事能不能加 + 聚合算子定案 + 把次新段的「段等权是陷阱、段内排序最强」切开),其余 21 条陪跑。
若 `h3_xfz_plus_f` ≈ k_known_xfrozen,这条因子就该收尾(结论:只是已知族 + 通用筛子的影子);
若 `h3_ret_pe40` / `h3_ret_xfz` 把收益路径载体推到 +12% 以上,**真正该立项的对象是「秩 beta / 同步性」这条线,
不是继续提纯 F111**。不要再碰叠加权重这个旋钮(0.25 / 0.5 / 1.0 已单调变差)。

## 7. 留出段

**没读过,一次都没有**(`runs/F111_spearman_qclose/sweepfinal_*.json` 从未打开)。读之前候选、排序、判据按 §5 写死;
注意 §5 的判据基准本轮**从 k_known 换成了 k_known_xfrozen**,这是和上一轮唯一不同的地方。

## 8. 给接手者的提醒

- **先读 `synthesis.md` 的「## 第二轮(s2)对账与结论」**;不要先读旧的 `07_*`(来自小样本逐轮实验)。
- 名字骗人两处:`ts_spearman` 名为时序、`arity=1`,**实为跨股票**(`nd_ts.py:483` 有 `for i in range(N)`);
  `day_quantile` 默认 q=0.5 **就是 day_median**。
- 代数事实:完整窗口上各股秩向量都是 0..d−1 的排列、**σ_j 是同一个常数** ⇒
  `mean_j corr(R_i,R_j) ∝ corr(R_i, 等权共识秩路径)`,**O(N²) 配对里没有配对信息**。
- 实现伪影:`stable=True` 排序把并列按时间先后给秩 ⇒ 10 天不动的价格路径 ≡ 完美单调上升。
  s2 已判定:**伪影不承担毛收益也不承担净超额**(`h_wmean_carrier` ρo 0.99),只承担「便宜」(低换手)。
- **大表两个坑**(本轮踩过):① `sg` 由 train 的**多空** rank IC 定、不是多头腿定 ⇒ 别把 Lnet 为负读成
  「反过来就有正的」;② `cs_first_*` / `cs_last_*` 是**词典序偏移、不产生 NaN**,外面套一个 `neg()`
  **会换掉交易的是哪一段**(`seg_hiliq_m` 的真实语义是「在流动性后 60% 里按 +f 选」)。
- **`ts_spearman` 在 d=50 OOM(exit 97)**;长窗口一律走 `ts_pearson`(与原式 ρo 0.98、同档)。
- 窗口池:`ts_*` [1,5,10,20,30,40,50];`cross_*` / `in_*` [3,5,10,15,30,60,241] —— 别写 `cross_mean(x, 20)`。
- 空头腿虚高的坑(次日封板标签 NaN)只影响多空口径;这条因子空头腿本来就大,**别拿它论证纯多头可用**。

## 研究日志(`notes/F111_spearman_qclose/journal.md`:21 条,其中研究员自己写的 11 条)

最近的 5 条(更早的和全文看文件):

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

### 2026-10-05 16:10 [主研] 批量扫描 s2 对账与结论

对账(s1 六条推论):支持 (i) 抽掉市场共同成分即塌(h_relpath +0.9%/0.12)、(ii) 再乘一次市场方向退回反转(h_mkt_undo −9.1%);
否定 (iii) 显式 O(N) 机制等价物(h_mkt_explicit −0.9%,我把「市场方向」的居中点代理错了)、(iv) 个股截面代理「放量才有效」(h_act_mul +4.0%)、
(vi) day_last 的 0.9pp 来自少并列(h_wmean_carrier +12.8%、ρo 0.99 ⇒ 伪影不承担收益);(v) 冻结筛子想法对、我的写法错 —— 只差 cross_mean→cross_max 就差 1.7pp/0.40。
四条新事实:ts_pearson 与原式 ρo 0.98 且跑得了 d=40(平台 10≈20>30>40);s1「书压在低流动端是浪费」反了(f 多头的一大半就是流动性倾斜);
scr_xhi_p 剔掉 f 最高 20% 后已知族从 +15.4% 塌到 +5.3% ⇒ 已知族多头腿本来就压在 f 的高分区里(ρk 0.42 低估多头腿重叠);载体换日收益只掉 1.3pp ⇒ 承重的是秩 beta/同步性。
定论:best_own = seg_xfrozen_p +13.5%/2.46(ρk 0.42→0.11,唯一站得住的提纯,但只切暴露没修机制);best_on_known 全部打不过 k_known_xfrozen(+18.5%/3.15),落后 2.9~3.0pp。
verdict = 提纯成功、升华失败、对 k_known 口径无增量;诚实缺口:s2 的叠加全叠在 k_known 上,「叠在 k_known_xfrozen 上」一格没量过 ⇒ 第三批 h3_xfz_plus_f 补这一格(优先级第一)。
已交:synthesis.md「第二轮(s2)对账与结论」(80 行)、state.md 覆盖重写(8 节 9.3KB)、hypo3.yaml(25 条 25/25 parse)。没起服务器,没读留出段。

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
- `sweep_s3`  10-05 18:00  142 个变体  → `./scripts/study.sh digest F111_spearman_qclose sweep_s3`
- `anatomy_s3`  10-05 18:30  0 个变体  → `./scripts/study.sh digest F111_spearman_qclose anatomy_s3`
- `sweepfinal_s3`  10-05 18:37  8 个变体  → `./scripts/study.sh digest F111_spearman_qclose sweepfinal_s3`
- `x1_identity`(自写脚本的输出)  10-04 14:23  exit 0  → `logs/F111_spearman_qclose_x1_identity.log`
- `x2_increment`(自写脚本的输出)  10-04 23:58  exit 0  → `logs/F111_spearman_qclose_x2_increment.log`

## 已写的 notes(`notes/F111_spearman_qclose/`)

`01_expression.md`(3K)、`02_operators.md`(9K)、`03_decomposition.md`(4K)、`04_grammar.md`(11K)、`05_hypotheses.md`(34K)、`06_baseline.md`(12K)、`07_S1_whatis.md`(7K)、`07x_1_identity.md`(14K)、`journal.md`(36K)、`state.md`(9K)、`synthesis.md`(22K)

## 自写的探针与分析脚本(`studies/F111_spearman_qclose/`)

- `x1_identity.py`  10-04 14:17  R1 exec script -- the identity + conditioning + known-family + tie analysis.
- `x2_increment.py`  10-04 23:51  R2 exec script (修订 R2-a) -- block A/B/C/D/E: does F1/F2 give a long-only user

## 结构化结果(`handoff/F111_spearman_qclose/results/`)

- `synthesis.json`
