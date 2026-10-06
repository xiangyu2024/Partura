# 研究现状 · F112_scale_spow_masktop

> 第 **6** 轮(主研 Opus 5)覆盖重写于 2026-10-05。**每轮整个文件覆盖重写。**
> 读序:本页 → `synthesis.md`(§1 机制 / §2–4 s1 判读 / **末节「第二轮(s2)对账与结论」= 最新口径**)
> → `studies/F112_scale_spow_masktop/hypo3.yaml`(第三批 24 条,24/24 parse)→ 旧轮 `10_distilled.md` / `results/R3.md`。
> 表达式:`ts_scale(signedpower(cs_mask_top_replace_mean_neg(add(day_quantile(Close), day_kurt(High)))), 30)`
> 本轮证据 = `runs/F112_scale_spow_masktop/sweep_s2.json`(162 变体)+ s2 解剖。**没读测试段、没起服务器计算**,
> 只用了 `study.sh table / src / ops / hypo3 / note`。数字全是 train / valid / utrain(ut)。

## 1. 现状(一句话)

**提纯成立、升华不成立,结论仍是不纳入。** s2 把原式 ut **+4.2%/0.74** 提到 **+10.1%/1.55**、换手 6.6% → **3.2%**
(`h_csrank_cs241_ema`:删掉截尾 D 改 `cs_rank`、窗口拉到 241、`cross_ema` 10 平滑)。但解剖显示这 +10% 里**一半以上是
低价 / 低成交额段的段等权 beta**(持仓 +45.1% 压在价格最低 20%,该段段等权 +7.0%);段内 alpha 只剩 +1~+8pp。
对已知成交额族**零增量**(筛子 +11.8%、叠加 +13.5%、残差 +0.2%,全低于 `k_known` +15.4%/2.22),
而一条与本因子完全无关的通用筛子 `k_known_xfrozen`(家族剔掉近 15 日冻结盘口最重 20%)就有 **+18.5%/3.15**。

## 2. 中间结果(全部 ut `Lnet / Lshp`;逐条对账见 `synthesis.md` 末节)

- 基准:`k_known` **+15.4/2.22**(LTO 3.4%);`k_known_xfrozen` **+18.5/3.15**;`v_base` +4.2/0.74(LTO 6.6%,ρk 0.25)。
- **best_own**:`h_csrank_cs241_ema` **+10.1/1.55**(tr +9.5 / va +11.7,LTO **3.2%**,ρo 0.45 ρk 0.38);
  `h_csrank_w50` **+10.2/1.56**(+9.2/+12.5,LTO 5.7%);`h_nomask_cs241` +9.4/1.52(va 只 +7.3);
  `h_nomask_w50_ema10` +7.6/1.17;`h_masktop_mirror` +7.7/1.28;`h_div_med60` +7.3/0.85(最干净的单层比值)。
- **best_on_known:没有**。`scr_xhi_p` +11.8/1.79、`scr_xhi_m` +9.2/1.45、`ov_p025…m10` +13.5→+5.4(单调变坏)、
  `res_known` +0.2/0.03、`bk_known` +0.8/0.17、`bk_liq` +0.2/0.04 —— 全部低于 `k_known`。
- **彻底否定的三组**:流动性聚焦 `h_liq_first40` **-1.3/-0.21**、`h_liq_mul` -5.4/-0.60、`h_liq_first40_abl` -1.0/-0.19
  (只有桶内中性 `h_liq_bk` +6.1/0.75 ≈ 基线);制度代理 `h_lim_first40` -4.1/-0.44(va -15.7%);
  第二个加数 `h_kurt_z30` -17.1/-4.02、`h_gini_own30` **-28.0/-5.03**、`h_flat_own30` -18.9/-2.94。
- **干净比值族(去 nansum)天花板只有 +7.3**:`h_div_mean30` +6.4/0.72、`h_div_mean241` +5.4/0.69、`h_div_med60` +7.3/0.85、
  `h_rev_delay30` +6.1/0.73、`h_vwapish_30` +6.4/0.73 —— 全面低于保留 `ts_scale/cross_scale` 的 +10.1。
- **机制重写全败**:`h_rev_x_cv`(跌幅秩 × cv 秩)+3.2/0.35、`h_dd_max60` +2.3/0.26、`h_dd_tailq75_60` +3.9/0.43;
  状态门 `h_state_vol` +5.3/0.63、`h_state_thin` +4.9/0.58;微结构 `h_press_ema10` -5.1/-0.92、`h_press_rev` +2.2/0.34
  (tr -1.9 / va +12.4,不可用)、`h_centroid_rev` +1.1/0.16。
- **一条干净的反向证据**:`h_amtstd_ratio30 = div(day_std(Amt), cross_mean(day_std(Amt), 30))` **-0.5/-0.08**
  (分子 = `k_known` 的被平滑量,分母 = `k_known`)⇒ **家族就是一条流动性 / 微盘水平 beta**。
- 两个镜像实验坐实了 s1 的机制:`h_masktop_mirror`(遮**最高**一成)+7.7/1.28 ≈ `abl_D` +7.8/1.12 ≫ v_base +4.2
  ⇒ D 的损失确实是「抹掉多头腿自己的尾巴」;`h_winsor_w50_out` +4.4/0.74 vs `h_nomask_w50_ema10` +7.6/1.17
  ⇒ **收益在右尾**,缩尾把它吃光。

## 3. 过程与逻辑(本轮)

读 162 变体大表 + s2 解剖 → 把 s1 的 6 条推论和 9 组假设逐条对上数字 → 发现两处**判读错误**要改(见 §4)→
用「超配 × 段等权超额」给 best_own 做段 beta 归因,解释了「提纯了却仍无增量」→ 把还没穷尽的三件事写成第三批。
本轮只做判断,不做计算;`scripts/ partura/ workflows/ handoff/ lab/ docs/` 和别的因子一个字没动。

## 4. 假设表 / 本轮改掉的判读

**旧结论沿用**:H4(截尾有害)、H7′(窗口 50~241 是平台)、H8(相对家族无增量)—— H8 本轮由筛子 + 叠加 + 残差三条
独立路径再次支持。**H1′ 升级**:多头腿不只是「已知暴露谱上的一点」,是「低价 / 微盘段 beta + 弱 1 个月排名反转」的合成。

**两处必须改掉的 s1 判读**:
1. **「冻结盘口段 +29.6% 是富矿」是误读。** 段内净超额的基准是该段自己的等权,而该段段等权 **-67.4%** ⇒ 只做这一段仍大亏。
   同理次新段(段等权 -28.7%)。正确读法是 `段内 + 段等权`。按这个读法,s1 列的两个「被低配的富矿」都是**书本来就该回避的**,
   `ts_scale` 的 nansum 对次新的 -5.5% 低配是**有益**副产品、不是待修 bug。s2 里 `h_age_*` / `h_frozen_*` 四条全平淡,与此一致。
   真正有用的冻结盘口用法是**剔掉**:`k_known_xfrozen` 比 `k_known` 高 +3.1pp / +0.93 夏普。
2. **「应改写成 `div(day_median(Close), cross_mean(…))` 一族」作废。** 干净比值族天花板 +7.3/0.85,比保留 `ts_scale` 的
   +10.1/1.55 低 2.8pp / 0.7 夏普。nansum 暴露可去,但去掉它换不来业绩;窗口单调性在干净族里还反过来(30 +6.4 > 241 +5.4)
   ⇒ 窗口旋钮调的是 `ts_scale` 的分母稳定性 + 平滑,不是反转期长度。

**第三批 24 条**(`studies/F112_scale_spow_masktop/hypo3.yaml`,24/24 parse),九组:
A 补缺的 w50 裸版对照(1);**B `ts_rank` / `cross_rank` —— 把「相对自身近期水平」从比值换成秩,162 个变体里一次没出现(4)**;
**C `cs_bucket_zscore` / `cs_bucket_demean` 把段 beta 真正扣掉后量剩余 alpha(3)**;D 冻结盘口筛子迁移到 best_own,
三个代理(`day_zero_ratio` / `day_at_min_ratio` / `cross_flat_ratio`)并排(4);E `day_es_ratio_hi` 的 NaN 掩码当 B(1);
F `cs_flip_by_state` / `cs_state_rank` 正规状态门,含**状态加权的「反转 ⊕ 家族」混合**(3);G `cross_semistd_neg/pos`
替掉对称 cv(2);H 上一轮两条推断的正确代理 `day_distinct_ratio` / `cross_age` + `cross_madz` 裁决(3);
I `day_topw_mean` / `day_wstd` 重做微结构(3)。

## 5. 候选

1. `h_csrank_cs241_ema` = `cross_ema(cross_scale(signedpower(cs_rank(add(day_quantile(Close), day_kurt(High)))), 241), 10)`
   —— ut +10.1%/1.55,LTO 3.2%,ρk 0.38。**本条因子目前最好的版本**,但仍低于 `k_known`。
2. `h_csrank_w50` = `ts_scale(signedpower(cs_rank(add(day_quantile(Close), day_kurt(High)))), 50)` —— ut +10.2%/1.56,LTO 5.7%。
3. `h_div_med60` = `div(day_median(Close), cross_med(day_median(Close), 60))` —— ut +7.3%/0.85,单层、无 nansum,作模板留档。
4. 旧轮留出段候选仍有效(`results/R3.md` §1):`f_nomask30` +11.12%/1.328、`f_t50` +10.47%/1.330、`f_x241` +9.42%/1.338,
   对照 `f_known` +13.23%/1.402。**本轮没有新的留出段数字。**

## 6. 后面的思路

- 跑第三批。裁决点只有三个:(a) 秩版(B 组)能不能超过 +10.1 并把换手压到 3% 以下;(b) 段 beta 扣掉后(C 组)还剩多少;
  (c) 状态加权混合(`h3_state_w_vol`)能不能过 `k_known` +15.4%/2.22。**(a)(b) 都平淡时,这条因子可以结案**
  = 「一条被实现细节污染的弱排名反转,叠在低价 / 微盘 beta 上」,不纳入。
- **不要再做的**:扫窗口(平台已确认)、在 v_base 上加记忆(28 条 memory 最好 +5.4)、流动性聚焦(五条全塌)、
  峰度 / gini / flat 这一类日内形状当加数(-17% ~ -28%)、`cross_zscore` 短窗(四档全 -10% 量级)、重写成干净 div 族(§4.2)。
- 若第三批也没有增量,正式结案前只需读一次留出段,**≤5 条 `final`**:原式 + `h_csrank_cs241_ema` + `h_csrank_w50`
  + `k_known` + `k_known_xfrozen`,判据先写进 `10_distilled.md`。

## 7. 留出段

**本轮没有动留出段,`sweepfinal_*.json` 一个字没打开。** 第 4 轮读过一次(2024/2025,`results/R3.md` §1,
`ledger.json` 里唯一一条 `split: holdout`):候选 +9.4%~+11.1%、家族 +13.23%;家族自己在留出段衰减
(ut +16.13% → +13.23%,Lshp 2.410 → 1.402)而候选持平;但候选的优势集中在 2024 单年(候选 +19%~+21% vs 家族 +9.0%),
2025 候选只有 +3.1%~+4.7%、家族 +13.5%。**第三批跑完之前不要再读留出段。**

## 8. 给接手者的提醒

1. **段内净超额必须和「段等权超额」一起读**(`段内 + 段等权 ≈ 只做这一段相对全市场`)。单独看段内会把
   「书该回避的坑」读成「被低配的富矿」—— s1 就是这样错了两次(冻结盘口、次新),§4.1 是更正。
2. **四处名字与定义不一致**(源码为准):`day_quantile` 默认 q=0.5 = 中位数;`cs_mask_top_replace_mean_neg` 遮的是**最低**一成;
   `cross_scale ≡ ts_scale`(仅窗口池不同);`ts_scale` 分母是滚动**和**(nansum)、不保序、对窗口内缺失日敏感。
3. **`signedpower` 不是 no-op**(它改 `ts_scale` 的分母形状),但它的作用**无法被显式重写复制** —— s2 的 `h_rev_x_cv` /
   `h_dd_*` 三条都失败了。源码上的等价推导 ≠ 可替换的子结构。
4. **`ts_rank` / `cross_rank` 已经存在**(窗口池分别是 ts 的 1/5/10/20/30/40/50 和 cross 的 3/5/10/15/30/60/241),
   前两轮 162 个变体一次都没用过它们。「相对自身历史的分位」不需要新算子,第三批 B 组就是补这个洞。
5. `cs_state_rank` 在 nd 面用的是 **ts 窗口池**(1/5/10/20/30/40/50),不是 cross 池;`cs_flip_by_state` 的状态比较固定用 241 日中位数。
6. 用 `cs_first_*` / `cs_last_*` 时 `sg` 按 train 的 rank IC 自动定:**y 的 IC 为负时,被「剔到书底」的那一段会翻到书顶**。
   本因子好版本的 sg 都是 -1,所以这类假设的 y 一律写 `neg(...)`。
7. 市场状态**不能**靠「逐日常数乘子 + 日轴 EMA」写进表达式(`h_state_vol/thin` 都低于基线);正规写法是
   `cs_flip_by_state` / `cs_state_rank` + `select_where`。
8. `bk_known` / `bk_liq` 在 s1 曾因 dist 0.20 打 ✗,s2 里两行 dist 0.99 已过门槛、可作旁证;干净的增量证据仍是 `res_known`。
