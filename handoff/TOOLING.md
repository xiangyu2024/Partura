# 主研们报告的工具问题(对账轮,2026-10-05)与处置

来源:`handoff/<fid>/results/verdict.json` 的 `tooling_problems`。先是总领的处置,后面是原文。

## 处置

| 问题 | 谁报的 | 处置 |
|---|---|---|
| `cross_ema` 在成交额量级的输入上覆盖率被毁(mem_ema5 cov 0.49) | F105 | **已修**(2026-10-05):块内递推在 float32 下溢出(q^-k 到 1e30 × 输入 1e8~1e16);改在 float64 里算,和朴素递推逐位对过。缓存里 186 张含 cross_ema 的面板已清,第三轮全部重跑 |
| dist 门槛算在 EMA 之前的面板上,计数 / 占比类被机械判死 | F106(两轮都报) | **已修**:`scripts/sweep.py` 的 `dist` 现在取「原面板」与「实际交易的信号(EMA 之后)」里较大的;原值留在 `dist_raw` |
| `cs_first_*` / `cs_last_*` 的方向被 rank IC 自由翻转,「永不持有」变成「只持有」 | F101 F105 F109 | **已修**:根是这一族的变体锁定 sign = +1(`sign_locked`);docstring 仍需补一句「y 必须写成越大越想买」 |
| 注册表把 `cs_bucket_rank` / `day_zero_ratio` 等 9 个算子错标成 boolean / trivial | F101 F106 | **已修**:`partura/ops_ext.py` 在每次建注册表后清掉这批算子的错标(它们因此也进了 GP 的搜索词表) |
| 解剖表的「段内净超额」在持仓被清空的段里给出 −150% 这类退化值 | F105 F108 | 待修:持仓占比低于该段占比的 5% 时打 n/a |
| 扫描表只打印表达式前 110 字符,派生变体的「核」看不见;整行过长被截 | F101 F109 F110 F105 | 待修:加「核」字段、`--top N` / `--kind` / `--out` |
| 扫描结果没有逐日收益序列、没有变体之间的两两相关 | F102 | 部分:批次层有 `scripts/batch_cluster.py`(入选候选的两两相关与重合)和 `batch_fuse.py`(逐日序列);单因子表待加 top-N 相关矩阵 |
| 半衰期网格上限 20 是边界解 | F101 F104 | 待定:网格加 40 / 60(用户的口径是 {0…20},加了就不可比,需要用户点头) |
| 通用筛子只用原式当筛子,不用本因子最好的变体;只有 20% / 40% 两档 | F103 | 待做:下一批的通用变体里加「best_own 当筛子」;新算子 `cs_last_high10 / 05`、与方向无关的剔除 `cs_drop_*`(5 位主研要) |
| `sweepfinal_*.json`(测试段)与 `sweep_*.json` 并排放着,主研可能误开 | F106 | 待做:挪到 `runs/<fid>/holdout/` |
| `study.sh hypo3` 的纯解析检查要连服务器,网络一抖就失败 | F104 F107 F108 F110 | 待做:本地离线解析模式 |
| `study.sh table --all` 只往 stdout 打,并发时主研们重定向到了同名临时文件,差点串数据 | F107 | 待做:`--out`,默认写 `tmp/<fid>_<tag>_table.txt` |
| 数据层:流通市值 / 流通股本、板块与涨跌幅限制宽度 | 7 位主研 | **等用户决定**(要动 AlphaCube 的数据层) |

## 原文

### F101_day_shine_retstd

- 半衰期网格上限 20 对稠密族是边界解(全部选到 20),所以「再长会不会更好」只能靠在表达式里写 cross_ema / cross_mean 绕开;而本轮又证明表达式内的平滑在这条因子上无增量,这个边界目前看不要紧,但对任何「稠密 + 持久水平」型的因子都会再撞上。
- cs_bucket_rank 的 dist 门槛已修好(s1 全部 0.20 ✗ → s2 全部 0.99~1.00),因此 s2 里那条「加 0.001·cs_rank 打破并列」的绕路变体(h_rv_fold_bk_amt20_tie,2.16 对 2.17)是多余的,可以从以后的假设表模板里删掉。
- in_sustain_stddev 在注册表里被打上 boolean_output 标签是错的:它输出的是连续的 std,真正的掩码是它的第一个操作数。这个错标签会误导任何按标签筛算子的自动生成器。
- abl_* 在触发型 / 带形状约束的算子上会产生语义意外(abl_G 的掩码变成「Δ 恰好=1」、abl_I 的根变成 0/1 掩码、abl_A / abl_H 因分钟轴宽度 236 vs 241 直接求值失败),建议扫描表把这三类单独标注,否则容易当成干净的消融读。
- 扫描表只打印表达式的前约 110 个字符,而本因子的变体表达式长 300~400 字符,派生变体的核被截在后面看不见 —— 这是本轮那条「8 条平滑/融合/overlay 全建在输掉的核上」整轮没被发现的直接原因。建议表里为每个变体额外打印一个「核」字段(最深的那个 day_* / in_* 子结构),或打印它与当轮最佳核的 diff。
- 数据层(需用户决定,六条因子都提过):缺流通市值 / 流通股本 —— 没有它只能用价格或 20 日 / 241 日成交额做规模代理,而这两个代理在本因子的解剖里给出相反答案(流通市值最低 20% 段内最强 S+2.96,20 日成交额最低 20% 段内零分辨力 S+0.15),A 组的桶内折叠只能用代理键做,结论会含糊;缺板块 / 涨跌幅限制宽度 —— 科创板是本因子唯一的失效区(段内 −19.4% S−1.01),现在只能用价格水平间接区分报价制度。

### F102_kurt_autocorr

- runs/<fid>/sweep_*.json 只存每个变体的汇总统计(long_ann / long_sharpe / long_turnover / hl_* / corr_orig / corr_known),**没有逐日的多头腿收益序列**。后果:主研在本地完全无法做任何事后融合或相关性分析 —— 这一轮用户明确要「简单融合和平滑一下大家、看样本内外」,而我既不能起服务器计算(本轮禁止),也无法用已跑完的 145 个变体在本地算一个等权 rank 融合的 train / valid 读数,只能把融合写成下一轮的假设(h3_fuse_own2 / h3_fuse_smooth5)等扫描。建议在 sweep 输出里为每个变体多存一条逐日多头腿净收益序列(约 1400 个 float,145 个变体 ≈ 1.6 MB,相对现在 430 KB 的 JSON 可接受,或单独落一个 .npz):有了它,变体之间的融合、两两相关、分段归因都能在 Mac 上零成本反复做,不必为每个组合权重再排一轮服务器扫描。
- sweep 表里只有 corr_orig(与原式)和 corr_known(与已知族)两个相关数,**没有变体之间的两两相关**。这直接影响「哪两个改良是正交的、值得融合」这类判断:本轮我只能靠 ρo 的差(h_max60 0.80 vs h_fold_csmean 0.75)和 ρk 的差(0.23 vs 0.19)去**推测**两条改良走的是不同的轴,再写成假设去验,而一张 top-N 变体的相关矩阵本来可以当场回答。建议在 digest / table 里对夏普前 15~20 的变体附一张两两 rank 相关矩阵。
- study.sh ops 的检索好用,但注册表里已有的算子容易被漏掉:上一轮的综合把「跨日边界的掩码」和若干时序能力列进了 new_operator_requests,而本轮 grep 'delay|lag|shift' 就发现 cross_delay(res[d:] = x[:-d],窗口 3/5/10/15/30/60/241)和 cross_argmax 一直都在 —— 其中 cross_delay 恰好能写出本批最关键的那条假设(h3_lagmax60,挖掉最近 5 天的事件记忆)。建议 study.sh decompose 或 propose 的输出里，对树上每个槽位列出「同 axis / 同 category 的全部可替换算子」，省得主研把假设位花在以为写不出来的问题上、或把已有算子写进 new_operator_requests。

### F103_amt_dw_decay

- 市场解剖的「段内净超额」把上一轮 36 条假设里的 7 条(D 组)整组带偏:七条全负,而且显式限定之后的排序与解剖相反(清淡半边 2.25 > 流动半边 2.07)。建议解剖表在每一段除了段内读数,再直接给出该段的**显式限定宇宙读数**(cs_first_high40 / cs_first_low40 版的 Lnet / Lshp),两个数可以符号相反;至少把「段等权超额」和「书在该段的超/低配」放在段内读数旁边同列显示(现在要在括号里和另一列之间来回找)。
- 通用 scr_* 筛子变体只用**原式**当筛子(scr_xhi_p / scr_xhi_m),从不使用表里自家最好的变体当筛子。结果本因子的 best_on_known 只能定在 scr_xhi_p(用的是全表最差的自家版本 v_base,1.49),要等第三轮才知道真实上限 —— hypo3 为此手写了 h3_K_scr_relstd 和 h3_xfrz_then_relstd。建议 scr_* 自动再生成一组「用上一轮/本轮 best_own 当筛子」和「叠在 k_known_xfrozen 之上」的变体,这两件事每条因子都要问。
- 剔除型筛子只有 20% / 40% 两档,而要剔的段只占 6.5%(见新算子请求 2):+0.93 夏普这笔全局最大的增量,归因到现在仍是「真冻结票」还是「一道流动性下限」二者之间模糊的。
- overlay(ov_*)只有 ±0.025/0.05/0.10 三档固定权重,没有「按市场状态切换」的版本。本因子与已知族逐年近乎反相(原式跌市 +10.4%/涨市 +6.4%;k_known +6.0%/+23.0%),固定权重叠加已证明无效(h_K_plus_C 2.04 < K 2.22),而状态切换要到第三批(h3_state_switch / h3_state_flip_K)才第一次被测 —— 既然 cs_state_rank / cs_flip_by_state / select_where 已入库,建议把「状态切换 overlay」加进通用变体族。

### F104_kurt_masktop_amt

- ./scripts/study.sh hypo3 <factor> 只是解析检查,却需要连服务器:本轮第一次调用返回 `Connection closed by 36.103.198.204 port 29982`,原样重试才通过 25/25。纯语法 / 算子名检查应该能离线跑,否则网络一抖就分不清「我的 YAML 写错了」还是「连不上」。
- 大表的多头半衰期网格封在 hlL = 20,而 F104 的水平类变体几乎全部取到这个上限(h_sqrt_std / sub_C_day_std / h_mask_mean / h_pow025_kurt 全是 20),所以读不出最优半衰期是否在网格外。上一轮手工放到 30 / 40 / 60 / 120 时 train +5.5 / +5.8 / +5.0 / +3.9 而 valid −3.9 / −2.8 / −2.8 / −1.1(延长只省成本、救不活 valid),但这是单独跑出来的,大表本身不覆盖。
- hlL 不同的两行 LTO 不可直接比较,而表里没有任何提示,极易误读:h_mask_std_m30(hlL = 0)的 LTO 5.7% 高于 sub_C_day_std(hlL = 20)的 4.1%,但这不是它换手更高,而是半衰期不同。建议表头加一句,或另出一列「同半衰期下的 LTO」。
- 大表不出多头腿最大回撤。候选若要上报给用户,这是必须有的一列(净超额 + 夏普说不清 2020 / 2022 那种单段的痛感),现在只能靠逐年净超额间接推。
- 市场解剖固定只出 10 列(按 utrain 夏普自动取前十),两轮都没能把 nt_cs_rank 一族(h_rank_mean 等)放进去,所以「换成无漂移的连续标记后,放量 / 缩量的不对称是否消失」这条核心推论至今没有解剖证据 —— 这是 s1 推论 (c) 只能判「半支持」的唯一原因。建议解剖的列可由主研指定。

### F105_std_fangzheng_covamt

- 市场解剖表的「段内净超额」列在持仓被清空的段里输出退化值,而表上没有任何标记:seg_xfrozen_m 在冻结盘口段 −153.6%、seg_new_p 在次新段 −60.7%,两者的真实持仓都是 0(括号里超配 ≈ −该段占比)。建议解剖脚本在该段持仓权重低于某阈值(比如该段占比的 5%)时直接打 "—" 或 "n/a(持仓 0)",否则主研会把它读成灾难性亏损。
- cs_last_high20 / cs_first_low40 一族的词典序语义 + 对 sg 的依赖是本研究最贵的 bug(浪费 4 个变体名额、毁掉一整组预先登记的门控实验)。短期至少在 docs/new_operators.md 的定义里显式写「效果依赖 sg,y 必须写成越大越想买」;长期加 sg 无关的掩码版(见 new_operator_requests)。
- cross_valid_count(x, d) 作为筛子 / 分段变量会饱和:93% 的票卡在 d 值上,dist 只有 0.05,当筛子等于按并列随机切。它已被新加的 cross_age 替代,但仍在库里;建议在文档定义里标注「不可当筛子 / 分段变量」,否则下一位主研还会踩。
- cross_ema 在小 d 上毁覆盖:mem_ema5 cov 0.49 且 valid −92.4%,mem_ema10 cov 0.90(都没过 cov ≥ 0.95)。疑似预热 / 初始化期的 NaN 传播问题。要么在算子层修预热,要么在文档里给出最小可用 d。
- ./scripts/study.sh table <factor> s2 --all 的输出约 40 KB,超过单次工具输出限制、会被自动截断落盘,必须再读一次文件才能看全。建议加 --top N / --kind 过滤参数,或默认只打前 60 行 + 全部基准行。

### F106_erm_mag_gap_1m

- 【s1 已报,本轮证实,仍未修,最要紧】dist 门槛算在 EMA 之前的面板上(scripts/sweep.py:129 的 distinct_fraction(p[tr])),而实际交易的信号是 EMA(面板)。计数 / 占比类面板因此被机械判死。证据:bk_liq dist 0.20 ✗ → 外套 cross_mean(·,5) 的 h_bk_liq_sm5 dist 1.00(结果是干净的否定 —— 那个格子里本来就没东西,但门槛没让我们知道);s2 又死 4 条(h_blow_sgn30/60 dist 0.00、h_blow_any30 0.18、h_blown_gate 0.01、h_zero_max15 0.06)。**其中 h_zero_max15 = cross_max(day_zero_ratio(Ret),15) 正是本轮最好那条基准 k_known_xfrozen 的筛子用量:当筛子把基准抬 +3.8pp,当因子过不了门槛。** 建议 dist 改算在 bk.smoothed(signal, hl_long) 上,或对 0/1、计数、占比类面板在 hl ≥ 1 时豁免。
- 【流程安全,本轮新发现】runs/<factor>/ 目录里 sweepfinal_s2.json 与 sweep_s2.json 并排放着、命名只差四个字母,而主研被明令不许读测试段。误开一次就污染整条研究线且不可逆。建议把测试段读数移到 runs/<factor>/holdout/ 子目录,或在文件名里带 DO_NOT_OPEN,或由 study.sh 在主研角色下直接拒绝读取。
- 【s1 已报】cs_bucket_rank 在算子表里被打上 [boolean_output, trivial_boolean],而它返回 (0,1] 的桶内百分位 —— 标签错了,会误导 propose / GP。本轮 L2 的结论正好指出这个算子是「低 ρk 是不是真增量」的唯一裁决工具,被错标成 trivial 代价很大。
- 【s1 已报】打分前没有「面板全 NaN 或常数就丢掉」的过滤:s1 有三个槽位浪费在退化变体上(iso_G、iso_R、abl_R 返回全 NaN / cov 0.00)。
- 【s1 已报】表头的 rank_ic_train 存的是 abs(rank_ic)、方向在 sign 里(sweep.py:122-129)。读表的人会以为 v_base 是「IC 正而方向 −1」,建议在表头注明。

### F107_abs_demean_skew_low

- `./scripts/study.sh table <fid> <tag> --all` 只往 stdout 打印,没有 `--out`;我把它重定向到 session scratchpad 的固定文件名 `s2_table.txt`,结果**同批别的因子的主研并发写了同名文件**,我读第二段时拿到的是 F106_erm_mag_gap_1m 的 200 行表(表头和 `v_base` 的表达式都变了才发现),差一点把别人的数字写进 F107 的结论。建议:`study.sh table` 加 `--out <path>` 或默认落到 `runs/<fid>/table_<tag>.txt`;至少在 handoff/README 里写明「重定向的文件名必须带 fid 前缀」。我已把这条坑写进 `notes/F107_abs_demean_skew_low/state.md` §8。
- `state.md ≤ 10 KB` 这个约束没有任何工具校验:上一轮(同一任务模板)写出来的 state.md 是 11,454 B,超了 12%,一直没人发现。本轮重写后压到 10,236 B。建议 `scripts/recorder.py` 或 `study.sh note` 顺手检查 `notes/<fid>/state.md` 的字节数并在状态板上标红 —— 现在 15 条因子的 state.md 很可能普遍超标。
- `study.sh hypo3` 会 `rsync` 到服务器再 SSH 跑 `check_hypo.py`,一次往返约 1 分钟;本地没有离线的纯解析检查。写 25 条假设时只能一次性全推上去,改一条就要再等一轮。建议给 `check_hypo.py` 加一个只做表达式解析/算子签名校验的本地模式(不碰数据)。

### F108_max_ntkurt_close

- **已修,警告可以撤**:s1 §8.4 记的 `cs_bucket_rank` dist 0.20 误判已经修好 —— s2 里 `bk_liq` / `bk_known` 的 dist 都是 **1.00**。「给每条分桶变体配一条 `cs_regres` 保险」的做法可以停了(省一半变体预算)。
- **解剖表的段内净超额在仓位被剔到近零时会给出极端误导数**,而表上看不出来。本轮实例:冻结段那一行 `z_known_excl_flatrun` 段内 **−147.2%**,但它在该段的持仓占比偏离是 **−5.6pp**(6.5% 的段只剩 ~0.9%)—— 那个 −147.2% 是在残渣上算的,很容易被读成「这条筛子在病态段很差」,而事实正相反(它赢就是因为**清空了**那一段)。**建议**:段内读数在「段占比 + 持仓占比偏离 ≈ 0」时打标记或直接给 n/a;至少在表头提示「段内读数必须和括号里的持仓占比偏离一起读」。已把这条写进 state.md §8-7 以防下一位主研踩。
- `./scripts/study.sh hypo3 F108_max_ntkurt_close` 在输出结果前先打了两行 rsync 失败:`Connection closed by 36.103.198.204 port 29982` / `rsync(22952): error: unexpected end of file`,随后才正常打出 25/25 parse(重跑一次没有再出现)。语法检查本身没受影响,但失败信息在结果**前面**,容易被当成检查失败。建议把 rsync 的重试/告警与 parse 结果分开打印。
- 以下限制(R2 实测)**未变,仍然成立**,留给下一位:`by_year` / `neutralise` / `profile` 只对本次 run 的 stage 内变体生效,不能对历史 run 补算;`digest` 的固定半衰期表只有 train 一段;GPU 被占时 NT 面约 4 分钟一条、排队只能 `wait`(不要重跑);`cross_*` 的窗口池没有 9(要写 10),nt 面窗口池是 [3, 5, 10, 15, 30, 60]。

### F109_erm_mag_gap_5m_tsm20

- ./scripts/study.sh table <fid> s2 --all 的输出里 expr 列被截在约 300 字符、且不打印 SSA 节点字母表 —— 要知道某个 abl_*/sub_* 到底改了哪个节点,只能回去读 runs/<fid>/sweep_s2.json 的 results[id]['expr'](上一轮已记,仍然如此)。另外整行长达 ~700 字符,直接 head 会被输出上限截断,本轮要先用 awk 按 | 砍掉第 9 个字段才读得动 233 行。
- s2 的 sweep_s2.json 里有 243 条结果,表里只有 233 行:被过滤掉的 13 条是 cov=0.00 / dist=0.00 的完全退化件(abl_V、iso_K、iso_V、nosc_AC_cs_state_rank,以及 6 条 nosc_*_day_es_ratio_*)。过滤本身合理,但表里没有任何一行字说明「不在表里 = 已跑且退化」—— 很容易被下一位读成「这几条没跑」,从而在下一批里重复提同样的假设。建议表尾加一行「另有 N 条 cov/dist 归零的退化件,见 JSON」。
- cs_last_high20 / cs_last_low20 / cs_first_high40 / cs_first_low40 四族的 docstring 没有点明「y 的多头端必须在高值,否则方向拟合会把被平移的那一段选成多头书」。我上一轮写的三条筛子假设(h_g_fam_nofrozen / norun / nonew)就因为 y 漏了 neg() 而全部测反方向,而且不报错、数字看起来还挺合理(+9.9% / +0.5% / +3.3%)。建议在 docs/new_operators.md 的这四行里加一句话。

### F110_ret_fair_log

- ./scripts/study.sh hypo3 F110_ret_fair_log 第一次调用整体失败:`Connection closed by 36.103.198.204 port 29982`(重复三次)+ `rsync(27078): error: unexpected end of file`,没有任何解析输出。直接重试同一条命令即成功(25/25 parse),是瞬时的 ssh/rsync 断连。建议 study.sh 的 hypo/hypo3/check 分支对 ssh 失败重试一次再报错,否则很容易被误读成「假设表写坏了」。
- ./scripts/study.sh table <fid> s2 --all 的完整输出是 272 行 / 41 KB,其中第 218 行起才是「市场解剖」那一节。用 `| head -N` 查看会把解剖整节静默截掉(我第一次就踩了,只拿到 142 条变体行、0 行解剖)。建议在表头注明总行数与解剖起始行,或给 --all 加一个 `--section anatomy` 之类的开关;下一位主研请直接重定向到文件再分段读。

### F112_scale_spow_masktop

- ts 窗口池(1/5/10/20/30/40/50)与 cross 窗口池(3/5/10/15/30/60/241)只在 5/10/30 相交。换核做对照时窗口被迫同时变,两个变量混在一条变体里 —— F112 的「窗口单调性 vs nansum 暴露」就是因此只能半定(见 new_operator_requests 的 ts_scale_mean)。
- 解剖表只打「段内净超额」和「段等权超额」两列,没有合计列(段内 + 段等权 ≈ 只做这一段相对全市场)。F112 的 s1 因此把冻结盘口段(段内 +29.6% / 段等权 -67.4%)和次新段(+11.2% / -28.7%)两块都读成「被低配的富矿」,并据此提了 4 条注定失败的假设(h_frozen_bk / h_frozen_mul / h_age_bk / h_age_first40)。建议加一列合计,或至少在表头把读法写上。
- cross_valid_count(x, 241) 在 241 处饱和,当上市时间代理时上市 300 日和 3000 日同值。s2 的 h_age_bk / h_age_first40 两条是用这个饱和版跑的,结论只能打折(新算子 cross_age 不饱和,hypo3 已换)。
- h_winsor_w50_out 这条变体缺一个「ts_scale(signedpower(add(...)), 50) 裸版」对照(表里只有 w30 裸版 abl_D 和 w50+ema 版),使「外层缩尾 -3.2pp」与「cross_ema 有益」分不开。批量扫描在加旋钮组合时应自动补齐缺的单旋钮基线;本轮只能把它写进 hypo3(h3_nomask_w50)下一轮再补。
- sub_E_sigmoid / sub_D_cs_quantile_q25/q50/q75 / sub_D_cs_mean / sub_D_cs_sum / sub_F_ts_argmin / sub_F_ts_argmax 七行 dist ≤ 0.03 被打 ✗(多头换手 0.3%~2.3%,基本是常数或接近常数的信号),它们占了全表约 4% 的算力但不可能成为候选。扫描时若能先按换手 / 有效取值数预筛掉这类退化变体,同样预算能多试七条真假设。

### F113_nested_tsmax_demean

- `./scripts/study.sh table <fid> s2 --all` 输出 72.2KB,超过工具的输出上限被截断成 2KB 预览(落盘到 tool-results/),必须重定向到文件再分段读;而 Read 工具对该文件一次最多 ~130 行(25000 token 上限),235 行的表要分 4 次读。建议 table 支持 `--cols` 或 `--kind hypo,screen,segment` 之类的子集输出,或直接提供一个紧凑格式(去掉 expr 列,expr 另出一份)。
- `./scripts/study.sh src` 一次问 17 个算子会被 SSH 直接断开(`Connection closed by 36.103.198.204 port 29982`),没有部分输出也没有错误说明;分成每次 ≤ 6 个就正常。建议 src 内部分批或在断线时提示。
- `cs_state_rank` 用 `@op("nd", "ts", arity=1, requires_window=True)` 注册,即 family = ts,窗口池是 `[1,5,10,20,30,40,50]`;但它的 docstring 举的例子是 `cs_state_rank(day_sum(Amt), 60)` —— 60 不在 ts 池里。本轮为避开只能用 30(约 1.5 个月,不是 docstring 说的「相对上一个季度」)。要么把它的窗口池改成 cross 池(含 60 / 241),要么改 docstring。
- 批量扫描里 segment 变体的 id(`seg_hiliq_*` / `seg_lowliq_*`)与它实际交易的段在拟合出的 sg = −1 时是相反的:`seg_lowliq_m` 与 `seg_hiliq_p` 的 ρo / ρk / Lshp 几乎相同(+0.42 / +0.72 / 2.09 对 1.98),是同一笔交易挂了两个相反的标签。建议扫描器在 segment / screen 这两类里固定 sg,或把实际 sg 反映到 id / 表注里,否则「只在低流动性里有效」这种结论很容易读反。
- `k_known_xfrozen` 这条通用筛子基准在 s1 的表里没有,s2 才出现,而它比 `k_known` 高 3.1pp / 0.93 夏普 —— 任何在 s1 上写的「赢了已知族」的判断(包括本研究第 5 轮的 overlay 读数)都要按新基准重算。建议把两条基准同时放进每一轮的表头,免得跨轮对账时拿错对手。

### F114_q25_closeret

- `./scripts/study.sh table <fid> s2 --all` 的输出 37.6KB,超过单次工具返回上限被落盘成临时文件 —— 不是 bug,但主研读表要先 `wc -l` 再分段读,否则只能看到前 2KB 的预览(我这一轮是分三次 sed 读完的)。
- `cross_age(x)` 给「数据起点就有值」的股票从 10000 起算,于是在 2018 年起点的面板上 92.9% 的票共享同一个数值。拿它做 `cs_bucket_rank` / `cs_bucket_demean` 的分桶变量时,这个大并列块会被 `_pct_rank` 的 tie-break 任意切进多个十分位,「老票」那几个桶里的中性化实际上退化成全市场排名的随机子集。文档里没有警告,hypo3 的 T 组因此改用 `cs_first_low20`(只取最短 20%)而不是分桶。
- `cross_semistd_neg/pos` 喂有符号序列(day_close(Ret))→ 内部取对数变化,cov 掉到 0.21;`cross_madz` 喂带 0 点质量的序列 → MAD→0、cov 0.70、净 -6.8%。两个算子的 docstring 都说了「正值序列」/「稳健」,但引擎不报错、只在 cov 列里体现,很容易被当成「这个想法不对」而不是「估计量被喂错了」。建议在 digest 里对 cov < 0.95 的行直接标出触发原因。
- `study.sh table` 只 grep 本地 `logs/<fid>_sweep_<tag>.log`,而解剖那次运行会把 sweep 的日志覆盖掉 —— s1 的回测表现在已经打不出来(上一轮已记录,s2 同样的风险仍然存在)。坑在 `scripts/` 里,按规则我没有改。

### F115_all_tide_mean_30

- abl_D 两轮都跑挂:s1 报 in_slice_to_end CUDA OOM「尝试分配 280 GiB」,s2 报同一算子「40.69 GiB(GPU 总容量 31.36 GiB)」。根因是把 day_argmax 换成非 reduces_m 的算子会让 in_slice_to_end 的 pair 维度炸开。这一格两轮都没有读数,ablate 组实际上缺一条。第三批里没有这种替换。
- h_bk_amt 在 s2 表里根本不存在:它的表达式与 s1 的 bk_liq 逐字相同(cs_bucket_rank(core, cross_mean(day_sum(Amt),30))),被去重合并了,但表里和 errors 字段都没有任何提示 —— 40 条假设实际只读到 39 条,而 bk_liq 顶着 kind=neutral 混在别的组里。建议去重时在表里留一行「h_bk_amt → 同 bk_liq」。
- 同一条 bk_liq 的 dist 在 sweep_s1.json 里是 0.20、在 sweep_s2.json 里是 1.00(bk_known 同样 0.20 → 1.00),表达式没变。门槛口径在两轮之间改了,dist 不能跨轮比较;s1 综合 §6 写的「cs_bucket_rank 每桶内均匀分布必然撞 dist ≥ 0.5 门槛」这条判断在 s2 已不成立,接手的人若照着读会把 F 组整组误判。建议表头或 json 里记下门槛版本。
- s2 表仍把 cov = 0.00~0.02 的除零行按 utrain 夏普排在最前面:abl_H(+388.6%/−335.1%/+322.2%,Lshp 3.76)占据全表第一行,同类还有 abl_E、sub_D_day_autocorr_n1 / _hurst / _ar1_coefficient、only_M_R、sub_M_mul 共 7 行。已经打了 ✗,但排序没有降权,两轮都排在最显眼的位置 —— 建议把 cov < 0.95 的行排到表尾或单列一节。

