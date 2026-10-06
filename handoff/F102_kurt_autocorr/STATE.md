# F102_kurt_autocorr — 交接状态

_自动生成于 2026-10-06 11:53(`python scripts/recorder.py --brief F102_kurt_autocorr` 刷新)。这一页说的是「磁盘上有什么」;判断和想法在研究日志与 notes 里。_

- 来源:挖掘 #3961(批次 B01_single_factors)
- 表达式:`cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)`

## 现在到哪一步

- **阶段:全部完成**
- **留出段已经读过 2 次**(10-03 23:15, 10-05 12:16)—— **不许再读**。候选在留出段上的数全在 `runs/F102_kurt_autocorr/final.json`(`./scripts/study.sh digest F102_kurt_autocorr final`)。
- 最近的 agent(**一般不需要读它们的流水** —— 交接的正本是 state.md、journal.md、工单和结果卡;流水很长,只在这些对不上时才查):
  - `synth:F102_kurt_autocorr`:已返回结果,最后动作 10-05 11:30 → `handoff/F102_kurt_autocorr/agents/synth_a93191635af758ebb.md`
  - `verdict:F102_kurt_autocorr`:中断,最后动作 10-05 13:53 → `handoff/F102_kurt_autocorr/agents/verdict_a628b4b5a6f89b3d1.md`
  - `verdict:F102_kurt_autocorr`:已返回结果,最后动作 10-05 15:31 → `handoff/F102_kurt_autocorr/agents/verdict_af1e2cec7e004ff15.md`

**接手的人该做什么:** 这条因子做完了。最终结论在 `handoff/F102_kurt_autocorr/results/` 里最新的那个(revised.json 优先,否则 study.json)。

## 研究现状(`notes/F102_kurt_autocorr/state.md`,10-05 15:27 更新)—— **先读这个文件**

# F102_kurt_autocorr —— 研究现状(主研,批量扫描 s2 对账之后重写)

`cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)` · sg = −1(多头 = 低值) · 挖掘库 #3961
口径:多头腿扣 15bp 净超额 + 纯多头夏普,半衰期按纯多头书选。噪声 ±3 点 / ±0.3 夏普。门槛 cov ≥ 0.95、dist ≥ 0.5。

## 1. 现状

两轮扫描都读完(s1 94 变体、s2 145 变体)+ 市场解剖两份;综合与**第二轮对账在 `synthesis.md` 末节**。
第三批 25 条假设在 `studies/F102_kurt_autocorr/hypo3.yaml`(`study.sh hypo3` **25/25 通过**),等下一轮扫描。
**留出段已被第一轮研究员读过一次(`07_S_final`,台账记着),s1 / s2 都没再读,以后也不能再读。**

**定论(提纯成功、升华失败)**:聚合器从 `cross_sum(…,15)` 换成 `cross_max(…,60)` 后,它是一条
**夏普 2.85 / 换手 3.1% / ρk 0.23 的独立低换手小因子**(原式 2.05 / 5.4%),夏普已超 `k_known` 的 2.22,净超额
+11.3% 仍低 4 点。**在已知族之上冗余**:所有筛子 / 叠加用法(2.57~2.65)都低于 `k_known_xfrozen`(+18.5% / **3.15**)
至少 0.5 夏普。它**没有桶内选股力**,收益 = 流动性倾斜 + 冻结规避。

(…全文 6693 字符,读 `notes/F102_kurt_autocorr/state.md`)

## 研究日志(`notes/F102_kurt_autocorr/journal.md`:4 条,其中研究员自己写的 4 条)

最近的 5 条(更早的和全文看文件):

### 2026-10-05 11:26 [主研] 批量扫描 s1 的综合

- 读完 s1 大表 94 个变体 + 市场解剖,综合写进 notes/F102_kurt_autocorr/synthesis.md;第二批 40 条假设写进 studies/F102_kurt_autocorr/hypo.yaml(40/40 parse)。
- 它是什么:day_kurt 是**超额**峰度(nankurt_last = m4/var²−3,sub_C_pow_1_5 的 cov=0.75 直接量出 25% 的股票-日为负);nt_ts_autocorr_s1(Ret,3) 只用 4 根分钟收益算相关,窗口内收益全相等时分母的 EPS 让它**恰好吐 0**。所以整棵树 = 封板/停牌/死盘口探测器,与「自相关」无关。pow_2 是折叠(删掉 ρo=0.00、−4.0%),孔径 3 是刀尖(5→+1.5%、10→−3.1%,无平台)。
- 承重 = {3 分钟孔径, autocorr 槽位, day_kurt 槽位, pow_2 折叠, Ret 叶子};多余 = 外层 cross_sum(iso_C 单日 + hl20 已有 +8.0%,总平滑量守恒);窗口 5–60 是平台;真杠杆是换手(cross_ema/decay_linear 把 LTO 从 5.4% 压到 2.1%,净超额 +10.8/+10.9%)。
- cross_sum 把缺失日算成 0 + sg=−1 → 系统性买历史不全的票:科创板段内 −28.5%(书里压 12.3% 仓位)换 cross_mean → +3.0%;次新段 +7.1% → +23.5%。这是全表最便宜的修复。
- 「超配 × 段等权超额」点乘:原式 +5.5 个点来自跨成交额桶的倾斜(占 +8.9% 的六成),k_known +14.7(占 95%);冻结盘口段原式 +3.6、k_known +2.1。段内预测力随成交额单调上升(−2.9/−4.3/−0.3/+6.1/+12.4%)。年度极稳(5.6–11.1%,无衰减),放量 +13.3% vs 缩量 +5.4%。
- 相对已知族:ρk=0.26,但 res_known +3.7%、bk_known +4.0% → 独立上不行(8.9 vs 15.4)。小权重叠加 0.25/0.5/1.0 夏普 2.51/2.62/2.57 对 2.22,反号变坏 → 符号对、量在噪声沿。定性结论:**不是独立纯多头因子,是已知族的减波动配角(约 +0.3 夏普),最可能来源是那 1.5
…(这条日志还有后文,读 journal.md)

### 2026-10-05 13:50 [主研] 批量扫描 s2 对账与结论

对账:A 组否定「树=已知族+封板掩码」—— 双向残差显示树严格包含掩码(h_res_zero60 +10.1%/夏普 2.41 不塌,h_res_tree_on_zero −5.2%/−0.55 塌光),而八条语义替代(zero_ratio / flat_run / centroid / gini / signed_ratio / in_madz×2 / 合成封板计)utrain 夏普 −2.48~+0.89 全废。B 组否定「更慢更好」:cross_ema 15→30→60 = 2.20→1.94→1.40 单调降,cross_max 15→60 = 2.24→2.85;q75@30 2.36 ≫ q25@30 1.52,信息在尾部、是事件标记。D 组否定跨日渗漏(h_inac3 与 sub_D_cross_mean 数字逐位相同,ρo 0.99)并确认孔径 3 是刀尖(日内版 3→5 也塌)。E 组把凸性从「1.5~2 个点」下修到 0.06 夏普(abs 2.26 vs 平方 2.32,四次方 2.17)。F / G / H 三组共 14 条基本全否定:所有桶内变体不如全市场排名,四条叠加改良全部变差。
定论:best_own = cross_max(pow_2(day_kurt(nt_ts_autocorr_s1(Ret,3))), 60),+11.3% / 夏普 2.85 / LTO 3.0% / ρk 0.23(原式 2.05 / 5.4%)—— 提纯成立,夏普已超 k_known 的 2.22。best_on_known = scr_xhi_p(+16.9%/2.57)与 h_sieve_known(+16.3%/2.65),比 k_known 好一点,但比通用筛子基准 k_known_xfrozen(+18.5%/3.15)低 0.5 以上夏普 —— 升华失败、在已知族之上冗余。
下一轮:hypo3.yaml 25 条(25/25 解析通过),重点是 h_max60 周围的窗口 / 筛子 / 配角一圈,桶内折叠中心(cs_bucket_demean/zscore),把冻结拆成涨停 vs 跌停(day_at_max_ratio/at_min_ratio)+ 纯计数版冻结日计数器(cross_valid_count(day_es_ratio_hi(Ret),60)),以及唯一可能赢过 3.15 的 h3_xfroz_max60(在 k_known_xfrozen 之上
…(这条日志还有后文,读 journal.md)

### 2026-10-05 15:12 [主研] 可读回测台账 + 补上「自己人融合与平滑」两条

本轮是上一条(s2 对账与结论)的续:对账 / 定论 / 落盘都已完成,这一次只补两件事,**没有起服务器计算、没有读测试段**。
(1) 把 s2 大表整理成一张能直接给用户看的「升级阶梯」:原式 1.84/2.79(train/valid 夏普)、LTO 5.4% → 修 NaN(cross_mean)2.15/2.99 → 折叠中心挪到截面均值 2.40/2.42、LTO 2.4% → 双层均 2.36/3.06、LTO 2.4% → 剔次新 2.57/2.97 → **cross_max@60 = 2.82/2.79、LTO 3.1%**。关键的样本内外事实:**本因子的自有改良 train ≈ valid(2.82 vs 2.79、+11.8% vs +9.2%),而已知族 k_known 是 1.78 → 3.46 / +12.6% → +22.3%** —— 已知族的「样本外更好」是 2022–2023 这段行情给的,不是稳定性;两者摆在一起看才不会被 valid 的高夏普骗。
(3) 与已知族融合的那一组(ov_p025/p05/p10 = 2.51/2.62/2.57、h_sieve_known 2.65、scr_xhi_p 2.57)全部在 k_known_xfrozen 的 3.15 之下 —— 结论不变。但看分段可知:融合把 k_known 的 **train** 夏普 1.78 抬到 2.30、valid 的 3.46 几乎没动(3.44),净超额还掉了 2.7 个点。**融合买到的是样本内稳定性,不是样本外收益**,这一条以后别反过来讲。
(3) s2 从没测过「自己人融合」—— ov_* 测的都是「与已知族融合」。补进 hypo3 的 G 组两条:h3_fuse_own2(h_max60 与 h_fold_csmean 等权 rank 相加;两条分别改聚合器形状与折叠中心,ρo 0.80/0.75、ρk 0.23/0.19,是正交轴)和 h3_fuse_smooth5(对融合后的分数再做 5 日平滑 —— rank 层平滑平的是名次抖动、不是事件幅度,所以不违反 B 组「指数衰减与事件型机制对着干」)。判据都写在 yaml 里。
为腾出位置,删掉 h3_flip_ret(与 h3_flip_amt 重复的证伪)和 h3_distinct_min60(价格桶方向已被否定);hypo3 仍是 25 条,study.sh hypo3 **
…(这条日志还有后文,读 journal.md)

### 2026-10-05 15:24 [主研] hypo3 两处换装:加 h3_lagmax60(记忆还是当期)

查算子注册表时发现 **cross_delay 早就有**(定义:`res[d:] = x[:-d]`,今天看到 d 天前的值,窗口 3/5/10/15/30/60/241)—— 上一轮以为写不出来的那一问其实写得出。
于是加 `h3_lagmax60 = cross_max(cross_delay(pow_2(K), 5), 60)`:**把最近 5 天挖掉**的事件记忆。这是本批最关键的一条,因为 `h_max60` 的 60 日极大**含今天**,
所以 2.85 可能根本不是「记忆」、只是「现在冻不冻」穿了一件 60 日的外衣 —— 这也正好解释了为什么一个 15 日的**当期**掩码(k_known_xfrozen,3.15)能赢过它 0.3 夏普。
判据:挖掉近 5 天后夏普仍 ≥ 2.6 → 冻结是**持续的烙印**(事件过后仍被定价),F102 有独立经济内容且对数据时点不敏感;≤ 2 → h_max60 = 当期掩码的一个贵写法,这条因子该退休、直接用掩码。
两处换装(都是拿低信息量的位置换高信息量的):删 `h3_flip_ret`(与 h3_flip_amt 重复的状态证伪)换 G 组融合两条;删 `h3_rz15`(cs_robust_z 全局稳健 z,与已测的 h_fold_csmean 2.40 / h_winsor_kurt 2.22 高度重叠)换 `h3_lagmax60`。
hypo3 仍 25 条、**25/25 解析通过**;state.md 第 4 节加了 H 组、第 6 节加了判据,已压到 10,234 字节(8 节)。本轮仍**没起服务器计算、没读测试段**。

## 配置里的实验计划(`configs/F102_kurt_autocorr.yaml`)

- 标题:3 对分钟收益相关的日内峰度,平方后 15 日求和:主体是 4 分钟局部形态分布的形状(水平 + 日间离散),尾部是近 15 日的涨停封板事件;两条腿要的速度不同。留出段多头腿净超额:原式 hl=1 −0.7% / 原式 hl=5 +2.5% / 记忆拉到 60 日 +7.4%(修订:60 日版本对期限匹配的控制 R² 0.45,多头腿约四成是避开近 60 日封板票)
- **S0_baseline**(1 个变体):Partura 自己求值出来的原式,能不能复现用户表里公布的那一行?它的钱在多头腿还是空头腿?
  v_base
- **S1_layers**(8 个变体):预测力在这棵树的哪一层?pow_2 的折叠、平方的凸性、15 日求和各贡献什么;D1–D9 的排序是不是分钟收益一阶自相关的另一种写法?
  l_k2_today、l_nofold_lin、l_fold_lin、l_max、l_med、l_noac、l_ac15、r_ar1
- **S2_windows**(6 个变体):15 和 3 是不是搜出来的幸运参数?(H9:真效应应该有邻域)
  w_d5、w_d10、w_d30、w_d60、w_a5、w_a10
- **S3_aggregate**(11 个变体):15 日求和这一层到底在做什么(水平 / 离散 / 缺失日),以及两条腿要的速度是不是不一样:把记忆拉长,多头腿净超额能不能在 train 和 valid 上都站住?
  a_mean_sq15、a_mean_abs15、a_level15、a_disp15、u_max30、u_max60、u_max120、u_mean_abs60、u_med60、u_max15_sm10、r_meanA15
- **S_final**(5 个变体):原式、同速度的提纯式、以及极值记忆 15 / 30 / 60 这条'速度'曲线,在 2023-08 之后从未看过的数据上还成立吗?多头腿净超额是不是仍然随记忆变长而上升?
  f_orig、f_mean_abs15、f_max15、f_max30、f_max60
- **SR_horizon**(3 个变体):把与因子同期限的朴素控制(60 日封板代理 / 日内波动 / 成交额 / 最大振幅 / 日频波动 / 最大日收益 / 最大绝对日收益)加进来之后,控制变量张成多少、残差的多头腿还剩多少?
  h_orig、h_max30、h_max60

## 已经跑过的服务器运行(本地已拉回的;服务器上可能还有没拉回的:`./scripts/study.sh list F102_kurt_autocorr`)

- `S0_baseline`  10-03 17:40  1 个变体  → `./scripts/study.sh digest F102_kurt_autocorr S0_baseline`
- `s12`  10-03 19:50  15 个变体  → `./scripts/study.sh digest F102_kurt_autocorr s12`
- `s3`  10-03 22:53  12 个变体  → `./scripts/study.sh digest F102_kurt_autocorr s3`
- `final`  10-03 23:15  5 个变体  → `./scripts/study.sh digest F102_kurt_autocorr final`
- `rev1`  10-03 23:54  3 个变体  → `./scripts/study.sh digest F102_kurt_autocorr rev1`
- `sweep_s1`  10-05 11:01  95 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweep_s1`
- `anatomy_s1`  10-05 11:05  0 个变体  → `./scripts/study.sh digest F102_kurt_autocorr anatomy_s1`
- `sweep_s2`  10-05 12:12  146 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweep_s2`
- `anatomy_s2`  10-05 12:16  0 个变体  → `./scripts/study.sh digest F102_kurt_autocorr anatomy_s2`
- `sweepfinal_s2`  10-05 12:18  8 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweepfinal_s2`
- `sweep_s3`  10-05 17:29  171 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweep_s3`
- `anatomy_s3`  10-05 18:34  0 个变体  → `./scripts/study.sh digest F102_kurt_autocorr anatomy_s3`
- `sweepfinal_s3`  10-05 18:37  8 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweepfinal_s3`
- `sweep_s4`  10-06 10:33  171 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweep_s4`
- `anatomy_s4`  10-06 11:14  0 个变体  → `./scripts/study.sh digest F102_kurt_autocorr anatomy_s4`
- `sweepfinal_s4`  10-06 11:25  8 个变体  → `./scripts/study.sh digest F102_kurt_autocorr sweepfinal_s4`
- `x1`(自写脚本的输出)  10-03 19:32  exit 0  → `logs/F102_kurt_autocorr_x1.log`
- `x2`(自写脚本的输出)  10-03 20:05  exit 0  → `logs/F102_kurt_autocorr_x2.log`
- `x3`(自写脚本的输出)  10-03 23:04  exit 0  → `logs/F102_kurt_autocorr_x3.log`
- `audit1`(自写脚本的输出)  10-03 23:33  exit 0  → `logs/F102_kurt_autocorr_audit1.log`
- `rev2`(自写脚本的输出)  10-04 00:04  exit 97  → `logs/F102_kurt_autocorr_rev2.log`

## 已写的 notes(`notes/F102_kurt_autocorr/`)

`01_expression.md`(2K)、`02_operators.md`(3K)、`03_decomposition.md`(3K)、`04_grammar.md`(1K)、`05_hypotheses.md`(11K)、`06_baseline.md`(1K)、`07_S1_layers.md`(3K)、`07_S2_windows.md`(2K)、`07_S3_aggregate.md`(5K)、`07_SA_audit.md`(1K)、`07_SR_horizon.md`(4K)、`07_S_final.md`(4K)、`07_conditional.md`(2K)、`07_controls.md`(1K)、`07_neutralise.md`(4K)、`07x_1_anatomy.md`(8K)、`07x_2_refine.md`(5K)、`07x_3_longleg.md`(8K)、`07x_4_audit.md`(6K)、`07x_5_revision.md`(11K)、`07x_anatomy.md`(1K)、`07x_longleg.md`(1K)、`07x_refine.md`(1K)、`08_variants.md`(3K)、`09_diagnosis.md`(8K)、`10_distilled.md`(12K)、`11_risks.md`(4K)、`12_next.md`(2K)、`journal.md`(7K)、`state.md`(9K)、`synthesis.md`(20K)

## 自写的探针与分析脚本(`studies/F102_kurt_autocorr/`)

- `audit_1.py`  10-03 23:29  audit_1 -- reviewer's refutation attempt (train / valid only, never the holdout).
- `probes.py`  10-03 19:37  Probes this tree needs and neither F001 nor F002 did.
- `r1_revision.py`  10-03 23:55  r1 -- revision after the two reviews (train / valid only, never the holdout; no candidate is changed).
- `x1_anatomy.py`  10-03 18:40  x1 -- what does  cross_sum(pow_2(day_kurt(nt_ts_autocorr_s1(Ret, 3))), 15)  actually measure?
- `x2_refine.py`  10-03 19:54  x2 -- three questions S1/S2 left open (train/valid only, never the holdout):
- `x3_longleg.py`  10-03 22:56  x3 -- what S3 left open about the long-memory candidates (train/valid only, never the holdout).

## 结构化结果(`handoff/F102_kurt_autocorr/results/`)

- `audit-mechanism.json`
- `audit-numbers.json`
- `revised.json`
- `study.json`
- `synthesis.json`
- `verdict.json`

报告:`research/alpha_distillation/F102_kurt_autocorr.md`(10-04 12:07 生成)
