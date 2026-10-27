# C01 信念 · 第 2 轮(总领,写在 R2 开跑之前)

给下一轮的自己。依据只有:本实验 R1 的 8 次共用搜索(`episodes/c01r1s101..108_I0_open_search/evidence.json`、
`research/coldstart_C01/digest_r2.md`)、`partura/` 与 `scripts/` 的代码、算子内核源码。标「先验」的是公开文献
常识,不是本实验的结论。本轮没有跑任何数据,所有数字都是在 R1 的 627 个存档候选上用搜索真正用的
`partura.steer.Guidance` 算出来的。

最终指引:`guidance/C01_r2.yaml`(检查器 ADMISSIBLE,2 ideas / 7 priors,exit 0)。
主研的 `cards_r2.md` 没改(不是我该写的文件);**它和最终 YAML 不一致的地方以本文件第 3 节为准。**

---

## 1. 现在相信什么

| # | 信念 | 证据 | 置信 |
|---|---|---|---|
| B1 | R1 的算力主要漏在 5 类原子上:成交额/量的平凡日内聚合、成交额当被加权量、pool 换外层的改写、首末分钟成交额、价格日内方差。禁掉它们打掉 189/217 个已知族通过者,一个 head 都不碰 | 627 个候选上逐条核对(C2P1–C2P5) | 高(算出来的) |
| B2 | **名义股价水平是一个「差一点过线」的吸引子**:各种拼写(day_close(Vwap)、day_max(High)、day_wmean(Low, Vwap)、day_topw_mean(Close, Close)……)都落在分数 ≈+0.5、ρ≈0.42、valid ≈+1.6,从不单独过线,却吃掉大量存档位 | 分数 0.4–0.7 且 \|ρ_known\| 0.36–0.45 的存档候选 90 个;种子 102 一次运行 33/80 个存档位是价格水平、heads 0 | 高 |
| B3 | R1 种子 104 / 107 那一族(13/18 个 head 含 `cs_mask_top_replace_mean_neg`)押的主要是**价格单位的日内离散度与低名义股价的某个内层分位带**,而不是一个单调的「低波动」:sign 全是 −1,`cs_mask_top_replace_mean_neg` 把最低 10% 换成截面均值,所以纯多头书是原信号的第 10–20%(套两层就是 20–30%)分位带;一价日 std=0 → `std^k/dr`=0 → 落在最低档 → 被 mask 挡出多头书 | 内核源码(nd_cs.py 的 mask、ops_ext 的 day_distinct_ratio);种子 107 里 `mask_neg(mask_neg(day_quantile_q75(Open)))`(纯价格水平 + 两层 mask)+1.31、ρ0.30 过线但**不是 head**,即与该次运行那个 `day_std(Open)` 双层 mask 的 head \|ρ\|≥0.7;裸价格水平只有 +0.5、单层 mask 只有 +0.60 | 机制读法:中;经济含义:低。没有在数据上核过多头书 |
| B4 | 同一族里至少有一个 head 做多的是**高**价格离散度那一侧的分位带(`mask_neg(mask_neg(inv(day_std(Vwap))))`,sign −1 → 多头书是 day_std(Vwap) 的第 70–80 分位),而 `std³/dr` 那几条做多的是低的一侧。这是 GP 用 mask 挑分位带,典型的样本内过拟合形状 | 内核语义 + 符号推导(EMA 平滑会把边界抹软,推导是近似的) | 中低 |
| B5 | `long` 奖励没有可交易性掩码(`RewardContext.untradable` 只在 long_tradable/bucket/marginal 下生效),**但标签本身做了买入可行性处理**:入场日开盘 15 分钟锁涨停的票标签置 NaN,书里这一格按 0 收益(等于持现金)计。没处理的是:出场时锁跌停卖不出、信号日一价/锁停状态、停牌(标签 NaN → 也是持现金)。主研卡里「书本身没有涨停/停牌掩码」要按这条更正 | `partura/panels.py` target():`label_buyable` → `entry_locks`;`books.long_book`:target 非有限 → 收益记 0;权重只看信号(alphacube.metrics.long_short_weights) | 高(代码) |
| B6 | 在这个奖励下,朴素反转和朴素分钟波动都不是吸引子:`day_sum(Ret)` sign −1、hl 20 → −0.40;双层 mask 的 `day_std(Ret)` → −0.52 | R1 存档 | 中(各只有一两个样本) |
| B7 | Ret 首分钟的口径**从代码里定不下来**:store 里的 Ret 是预先算好的字段;AlphaCube 的合成数据生成器用的是逐分钟 Close/Open−1(那样首分钟**不含**隔夜跳空)。所以 C2a 里用 `day_first(Ret)` 的 4 个种子读的可能是「开盘第一分钟」而不是「隔夜」;价格比值写法(种子 3)与口径无关 | alphacube/synthetic.py;store.py 只读不算 | 中 |
| B8 | 先验:A 股市场层面隔夜收益平均为负、日内为正(与美股相反),文献归因于 T+1(Qiao & Dam 2020)。主研草稿写反了,已在 YAML 里更正 | 公开文献(先验) | 中 |
| B9 | GP 里两类杠杆的作用方式:idea = 种子进初代种群 + idea 算子 8 倍提权 + `grammar.day_ops` 硬 must-contain;先验 = 在评估**之前**按模式拒掉,被拒的提议不花付费评估;weight 规则按 `min(1, w/w_ref)` 稀释,任何 w>1 的规则会把其余一切按比例降采样;`operator_weights()` 只折叠「算子 + 全是 `_` 参数」的规则(本轮 7 条都带上下文,词表不变,`operator_weights()` 为空) | `scripts/idea_search.py` guidance_accept、`partura/steer.py` | 高(代码) |
| B10 | 跨轮去重是按 score 从高到低贪心:R2 里一个比 R1 head 分数更高的同族孪生会顶掉那个 R1 head,净 head 数不变。所以「再收割 104 族」最好的情况也是零增量 | PLAN §3.1 | 高 |

## 2. 本轮三个问题的现状

- **Q1(R1 heads 押了什么)**:部分回答(B3、B4、B5)。104/107 族像是「低名义股价 × 价格单位日内离散度」的内层分位带,mask 的一个作用是把一价/锁停名字挡在多头书外。多头书是不是仍在流动性族里、一价日是否被挡干净,要等终局的风格中性化读数或下一轮拿到的书;本轮不能跑数据,不下结论。
- **Q2(算力漏在哪)**:回答了(B1、B2)。7 条 ban 在 R1 上合计拒掉 369/627 个存档候选、0 个 head;已知族通过者打掉 189/217(全部来自 C2P1–C2P5,两条新增 ban 没有多打已知族,它们打的是 B2 那个吸引子)。幸存通过者 83 个,其中 \|ρ\|≥0.5 的 28 个(34%,R1 原来 79%)。
- **Q3(R2 押给什么)**:两个 R1 完全空白、经济学上说得通、可证伪的机制族,各 4 个种子(第 4 节)。104 族在两个邻域里不可达靠 must-contain;两条新 ban 把通往它的后门(加权价格、名义价格)也关上。

## 3. 我对主研草案改了什么,以及没改什么

主研草案的骨架是对的:两个 idea 都是机制,不是 R1 高分公式的微调;5 条 ban 都有本实验证据、零误伤 head、全是 ban(不碰 w_ref)。我改了 6 处:

| 改动 | 为什么 | 核对 |
|---|---|---|
| **加 C2P6** `{day_wmean\|day_wstd\|day_topw_mean}(@price, _)` | 主研说 104 族「在两个邻域里都不可达」只对原式成立:C2b 把 day_wstd 提权 8 倍,`day_wstd(Close, Amt)` 就是 `day_std(Close)` 的加权孪生,含它的树就在邻域里;day_wmean/day_topw_mean 称价格就是名义股价水平(B2) | R1 命中 11 个、只被本条命中的 9 个最高 +0.51;0 head |
| **加 C2P7** `{day_first\|day_last\|day_open\|day_close\|day_sum\|day_mean\|day_median\|day_max\|day_quantile*}(@price)`,unless 价格作分子的 `div(...)` | C2a 把 day_first/day_last 提权 8 倍,8 个叶子里 5 个是价格,不禁就把 B2 的吸引子整个带进 C2a 邻域、占精英位。unless 放过 `div(day_first(Open), ts_delay(day_last(Close), 1))` 这类隔夜/日内收益。day_min 故意不列(一个 R1 head 用 day_min(Close)) | R1 命中 97 个、85 个只被本条命中、中位 +0.50;唯一过线的是种子 107 head 的孪生;0 head;12 个种子都不被命中 |
| C2a 的 must-contain **去掉 day_sum** | day_sum 是通用归并,不读时点;留着它,`day_sum(Close)` 这类价格水平和 `day_sum(Ret)` 这类当日收益都算「在邻域里」。day_sum 仍因出现在种子里而被提权 | C2a 邻域在 R1 上:must-contain 109 → 39,再去掉被禁 32 → 16 |
| C2a 种子 3 `day_first(Close)` → `day_first(Open)` | 原式是第一分钟收盘价,不是开盘价;改后是真正的「隔夜(开/昨收)减盘中(收/开)」,与 Ret 口径无关(B7) | parse、深度 5、在邻域内、不被禁 |
| C2b 种子 1 `day_signed_ratio(Ret, Amt)` → `sub(day_signed_ratio(Ret, Amt), day_signed_ratio(Ret, Close))` | 裸的成交额加权涨跌份额几乎就是当天涨跌方向,读到的会是短期反转;减去按时间(Close 近似常数权)加权的份额,剩下的才是「钱是否扎堆在上涨分钟」。裸形式仍在种子 4(带一价日筛选)里 | parse、深度 3、在邻域内、不被禁;同时在 C2b 加了预测与 fails_if (e) |
| C2a 先验文本更正 | B8:市场层面的符号写反了。idea 改成只押横截面,并写明竞争性先验(日内反转会让隔夜减日内写法选 +1),fails_if (c) 不动 | — |

**考虑过、没做的**:
- 禁裸 `day_wstd(Ret, _)`(分钟波动):R1 里没有证据说它是吸引子(B6),没有证据就不写。
- 把 day_open/day_close 加进 C2a 的 must-contain:那等于把首末分钟的提权翻倍,而首末分钟正是价格水平的后门。
- 任何 w>1 的 weight 规则:会把其余一切按比例稀释(B9)。
- 否决某个 idea:两个都是 R1 空白、可证伪、对手方说得清;押两个是机制上的分散。
- 主研卡里提到「E2 测过的 day_var(Low)」,我读作本轮执行角色的第二次分析;如果它指的是本实验以前的研究,那是卡片正文里的隔离疏漏,不影响 YAML(YAML 里没有这句)。

## 4. 种子分配

| idea | 种子 |
|---|---|
| C2a_when_the_return_arrives(收益在一天里什么时候到账) | 201, 202, 203, 204 |
| C2b_turnover_on_the_up_minutes(钱落在上涨还是下跌的分钟) | 205, 206, 207, 208 |

## 5. 对 R2 B 臂搜索结果的可证伪预测(写在结果之前)

口径:\|ρ\| = max(\|rho_pool\|, \|rho_known_traded\|);heads = 每次运行 evidence 里自己的 heads 列表;
「通过」= score ≥ 1。R1 基线写在括号里。

| # | 预测 | 失败线 |
|---|---|---|
| P1 | 8 次合并,通过者里 \|ρ\|≥0.5 的占比 ≤ 35%(点估计 ~20%;R1 79%) | ≥ 50% |
| P2 | 通过者 \|ρ\| 中位数 ≤ 0.35(R1 0.88) | > 0.5 |
| P3 | heads 总数 ≥ 6(点估计 9,80% 区间 2–20;R1 18,其中 12 个出自同一次运行);≥1 个 head 的运行 ≥ 5/8(R1 4/8);单次运行 heads ≤ 6 | 总数 < 3,或 ≥1 head 的运行 ≤ 3/8 |
| P4 | 至少一半的 R2 heads 含 Ret 叶子(R1 3/18);同时含 `cs_mask_top_replace_mean_neg` 与 `day_std(@price)` 的 head ≤ 1(R1 12) | Ret head 占比 < 1/3,或 104 族形状的 head ≥ 2 |
| P5 | 通过者总数在 20 到 273 之间(R1 273,其中 217 是已知族) | < 10 |
| P6 | 合并门槛废品率 20%–45%(R1 平均 25%);我倾向 C2b 四次高于 C2a 四次(day_es_ratio_hi 在死盘日是 NaN),这条只有 55% | 任一次运行 > 60% |
| P7 | 8 次里最好分数 < 2.72(R1 最好),点估计 1.6–2.3 | — (只记) |
| P8 | 每次运行 `sampling.banned / proposed` ≤ 30%,`outside / proposed` 在 30%–85%,`scored` ≥ 90 | 任一次 banned > 40% 且通过者 0,或 outside > 90%,或 scored < 80 |
| P9 | B2 的吸引子(分数 0.4–0.7 且 \|ρ_known\| 0.36–0.45 的存档候选)8 次合计 ≤ 15(R1 90) | > 30 |
| P10 | C2b:day_signed_ratio 写法若有通过者,方向 −1(70%);差值写法(种子 1、2 的后代)至少 1 个通过者(60%) | 方向 +1 → 主研 fails_if (c);差值写法 0 个通过者而裸写法有 → fails_if (e) |
| P11 | C2a:隔夜减日内一系若有通过者,方向 +1 与 −1 我各给 50%(主研押 −1,我不押);day_centroid/day_argmax/day_argmin 一系至少 1 个通过者(50%);种子 3 一系(价格比值)与种子 2/4 一系(Ret 首分钟)选的方向不同,就说明 Ret 首分钟不含隔夜(B7) | — (只记,用来判 B7、B8) |

## 6. 什么结果让我放弃什么

- **放弃 C2a 这个族**:种子 201–204 合计 0 个 \|ρ\|<0.5 的通过者;或 heads 只出在 `cs_first_low20` 的种子上、方向 +1(fails_if d)。
- **放弃 C2a 的机制、但保留这个族**:隔夜减日内一系选 +1(fails_if c)。这时读到的是日内反转,R3 要改写 hypothesis,不许事后改故事说它成立。
- **放弃 C2b**:种子 205–208 合计 0 个 \|ρ\|<0.5 的通过者;或通过者全是裸 signed_ratio / topw_mean、差值写法 0 个(fails_if e,归为短期反转);或 heads 与 104 族 \|ρ\|≥0.7(fails_if b)。
- **先放宽邻域、不急着放弃**:某个 idea 的运行里 outside > 90% 或 scored < 80(是邻域卡死了,不是机制错了),R3 先放宽 day_ops。
- **把 ban 改成降权**:某次运行 banned > 40% 且通过者 0(C2P7 的 unless 太窄,或 C2P1 太宽)。
- **R1 的判断要改**:如果 R2 里出现 \|ρ\|<0.5、不含任何被禁原子、却与 104 族 \|ρ\|≥0.7 的 head,说明 104 族不是价格水平/离散度能解释的,B3 降级。

## 7. 给 R3 的自己

先看(按顺序):每次运行的 `sampling` 计数(P8)→ 通过者的 \|ρ\| 分布(P1、P2)→ heads 的结构与方向(P3、P4、P10、P11)→ 存档里还有没有价格水平堆(P9)。
没解决、可能要在 R3 里设计检验的:B3/B4(104 族到底是不是低价分位带)、B7(Ret 首分钟口径)、B5(出场锁跌停没处理,对偏小盘的书是乐观偏差)。
看不到的东西:A 臂的 R2 结果按规矩不看;「坏轮次」(PLAN §3.5)只能在终局 RESULT 里判,不要在 R3 里猜。
