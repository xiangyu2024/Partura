# 种子 2014 笔记(PROD W02L,P 组)

## 第 1 轮

**材料(只看到第 1 个结构批 B040):** 29 个成员、22 个已评分,围绕 `day_quantile_q25(F)`(一天里分钟序列的 25% 分位),F 取 Ret / Amt / High / Low / Close / Volume / Vwap。新尺子(去掉 5 个控制和两个冠军)下没有一条为正,三个「素材 head」是 −1.13 / −1.20 / −1.22,不是真 head;共性表里 `q25(Ret)` 含 / 不含 −2.44 / −3.14(p 0.16),`q25(High)` −3.38 / −2.66(p 0.89)。整批均值约 −3,和别的批一样。

**这一轮读到的事实(都已核对,写在这里给下一轮 PI,不用再查):**

1. **两个库 5583 条能解析的表达式没有一条读过六个日频叶子**(LogFloatCap / LogTotalCap / LogFloatShares / LimitWidth / BoardCode / ListAge;`struct/members.csv` 里 expression 与 leaves 两列的出现次数都是 0)。库里用到的叶子只有 Ret / Volume / Amt / Close / High / Low / Vwap / Open。库、也就是两个冠军,够不到的是:日频叶子本身,以及 `ops_ext` 的新算子(day_centroid、cross_zscore、cs_bucket_*、day_zero_ratio 等,库里几乎没有)。W01 的 head 里 86 / 260 含日频叶子,基本都是 `cs_first_low20(y, 规模或价格或 ListAge)` 的筛子写法(N 位 / E 位 / M 位都有)。
2. **分钟价格字段是后复权价**(规则 §4;`AlphaCube docs/design.md` §11.5:`Close / (Amt / Volume)` 跨股票 2.5 ~ 113,每只票内部变异系数 1% ~ 2%)。所以 `q25(High)` / `q25(Vwap)` / `q25(Low)` 量的是复权后的价格水平,不是真实价格。真实价格只能写成 `sub(LogFloatCap, LogFloatShares)` = log(流通市值 / 流通股本)。`members.csv` 里 `q25(High)`、`q25(Vwap)`、`div(sqrt(signedpower(pow_2(q25(High)))), 1)`、`add(q25(High), day_close(Ret))` 的训练段统计几乎逐位相同(rank IC −0.011,日换手 0.0137,库口径夏普 0.524),是同一张面板。
3. **三个 head 各自在量什么(读内核得到的):**
   - head 1 `ts_std(q25(Ret), 10)`:下四分位分钟收益的 10 日标准差 = 波动率的不稳定度,但取的是绝对标准差,正比于波动水平(控制)。`q25(Ret)` 被 0.01 元的 tick 量化,消融表说它单独过不了门槛(不同值占比 0.4955)。窗口 20 / 10 / 5 得 −1.19 / −1.13 / −0.88,越短越好。
   - head 2 `ts_sum(cross_fangzheng(cross_max(q25(Amt), 3), 241), 5)`:`cross_fangzheng` 在 AlphaCube 里是 `cross_mean + cross_stddev`(均值加标准差,不是方差)。承重的只有 241 日的 cross_fangzheng(拿掉它 −3.77),cross_max 与 ts_sum 不承重。这是「静默分钟成交额的一年水平」,流动性的近亲;验证段 +0.43、训练段 −1.11。
   - head 3 `ts_max(log(cross_regbeta(cs_sum(signedpower(q25(Low))), day_last(Amt), 10)), 20)`:`cs_sum` 把平方后的后复权价加成全市场的当日常数(由价格最高的少数几只票支配);`cross_regbeta(x, y, d)` 是 y 对 x 的回归斜率,y = 收盘分钟成交额,所以 beta 随 y 的幅度成比例;算子 `log` 取 |x| 且 |x| ≤ 1e-9 给缺失。整个 head 读的主要是「最近一段时间收盘分钟成交额的峰值幅度」。ts_max 窗口 10 / 20 / 40 得 −2.05 / −1.22 / −0.54,训练、验证同时单调变好,是整张表里最干净的趋势。
4. **算子行为备忘:** `div` 是裸除法(没有 EPS,0/0 是缺失、x/0 是无穷);`cross_corr` 的分母是 `sqrt(var_x var_y) + 1e-9`(量级 1e-4 的输入影响 ≤ 5%);`cross_regbeta` 的方差阈值是 1e-9(`Σdx²`,不除以窗口长);`cs_mean` / `cs_sum` 返回全市场的当日常数(同一数值铺满整行);`cs_bucket_rank` 桶内并列用全局秩 × 1e-4 打破;`cross_delta(x, d)` = x[t] − x[t−d](停牌日为空时整个差为空)。
5. **本机做过的唯一数值检查:** 用 AlphaCube 自带的合成立方体(120 只票 × 300 天 × 241 分钟,与真实数据无关)把本轮全部 45 条表达式(种子 + R 变体)跑了一遍,都能算,没有无穷;只证明算子组合在数值上不爆,不证明任何 alpha。没有碰真实数据。

**目前对这个种子 alpha 来源的信念(很弱):**
- 这一批本身没有 alpha:所有已评分成员都是「波动水平」「成交额水平」「复权价格水平」三个已知东西换写法,新尺子把它们吃掉了。三个 head 的相对好,主要来自慢(窗口长、换手低)而不是来自结构。
- 值得赌的不是批里的算子骨架,而是批里反复出现却没被拆开的两个量:**价格水平**(后复权混合体)与 **tick 量化**(q25(Ret) 的 0.4955)。它们只能靠日频叶子拆开,而库和冠军都不读日频叶子。项目自己的文档(`AlphaCube docs/可交易回测.md` §21.4)给过一条旁证:未复权低价风格(原样、没中性化)的纯多头夏普,训练 +0.98,2023-08 ~ 2025-12 为 +0.44,日换手 2.0%;三个风格里只有价格不在新尺子的控制里。
- 同时要警惕的:价格水平、log F 水平都是接近常数的个股标签,样本内容易只是风格(年龄 / 规模 / 板块)的代理;train 与 valid 的符号若不一致,min 就是负数。

**本轮的任务与事先预测:**
- **槽 1(E)核心 `day_quantile_q25(High)`(后复权价格水平的代理)。** 外围 = 用日频叶子把它拆成 `log F = log(核心) − log P`(上市以来分红送转的累积)、log F 的 120 / 241 日增量(滚动股息率)、核心的 6 ~ 12 个月动量,以及它们在同规模 / 同价格十分位内的版本,14 个种子。预测:**出 head 的概率约 8%**。最可能的形态是 log F 的增量类(动态、不含个股常数)或同价格桶内的版本;最可能的失败方式:(a)水平类被「年龄 / 规模」吃掉(与市值控制的 |ρ| 偏高);(b)train 与 valid 符号相反,min 为负;(c)流通股本更新滞后造成送转日前后 log P 失真,增量类噪声大。预期最好的分数落在 −1.0 ~ 0.0。如果这一位一个 head 都没有,信息是「后复权因子这条路没有残差 alpha」,下一轮不再押它(核心 q25(High) 已用 1 个 E 位,至多再用 1 个)。
- **槽 2(N)真实价格 P 与 tick 摩擦。** 种子 = P 本身、P 在市值 / 成交额 / 波动 / 总市值 / 流通股本 / 非流通比例十分位内的秩、tick 计数 `log(|q25(Ret)|+1e-6) + log P`、以及同价格十分位内的零收益 / 同价 / 不同价位占比、q25(Ret) 及其日间标准差,16 个种子。预测:**出 head 的概率约 12%**,比 E 高,因为有一条独立旁证(低价风格样本内两段为正)。最可能成功的形态:P 在市值或成交额桶内的秩(它不再被市值控制吃掉);最可能的失败方式:(a)P 水平与市值 / 流动性控制的 |ρ| 偏高被打成同一个东西;(b)tick 统计在同价格桶内仍是流动性的近亲(与 liq 控制 |ρ| ≥ 0.8 被划掉);(c)低价端的 ST / 退市风险股拖垮 train。
- **R(15 个变体):** 烂部件是窗口(head 1、3 的趋势没到头)、尺度(head 1 的绝对标准差,head 2 的水平)、与 head 3 的幅度。预测:满足「比原 head 好 0.1 且与已知族 |ρ| < 0.5」的有 2 ~ 4 个(head 3 的长窗口版、head 1 的 5 日 / 3 日版最可能),多半是**替换**(与原 head ρ ≥ 0.5);收录新 head 的概率约 3%,没有一个能到 0.5。head 2 的均值 / 标准差拆分是信息型实验:如果「只留均值」与原 head 同分,说明 head 2 就是流动性水平;如果「只留标准差」更好,说明波动那一半承重。

**上一轮预测对不对:** 第 1 轮,还没有。

**给下一轮的备忘:**
- 第 2 轮会看到 B041(`ts_cov(day_quantile_q25(F), day_close(F))` 一族,q25 与日收盘价的滚动协方差,多半仍是价格 / 波动水平),第 3 轮看到 B042(`day_std(pow_3(F))`)。如果这一轮的 E / N 都没产出,第 2 轮的 N 位应该换一条完全不同的线:下面这份「市场状态同步性」草稿已经在合成立方体上验证过都能算,骨架都不在库里:
  - `cross_corr(cs_mean(day_quantile_q25(Ret)), day_quantile_q25(Ret), 60)`(下尾分钟波动与全市场同步,AHXZ 2006 的波动 beta 的稳健版)
  - `cross_corr(cs_mean(day_sum(Ret)), day_sum(Ret), 60)`(同步性 R²;Morck-Yeung-Yu 2000),`cross_corr(ts_delay(cs_mean(day_sum(Ret)), 1), day_sum(Ret), 60)`(价格延迟;Hou-Moskowitz 2005)
  - `cross_corr(cs_mean(log(day_sum(Amt))), log(day_sum(Amt)), 60)`(流动性共同性;Chordia-Roll-Subrahmanyam 2000)
  - 注意:Amt 类分布统计(如 gini、q25/mean)与 liq 控制的 |ρ| 在别的种子的相关度表里常常 ≥ 0.8,这类不要押;Ret 类 / 相关系数类与 liq 控制的 |ρ| 一般 < 0.3。
- E 位核心的陷阱:核心必须与每个控制 |ρ| < 0.8。`day_quantile_q25(Ret)` 是波动的近亲(估计 |ρ| 0.7 ~ 0.85,可能越线),`day_last(Amt)` 是成交额水平的近亲(估计 ≥ 0.8),所以这一轮选了与控制几乎无关的 `day_quantile_q25(High)`。
- 如果第 1 轮 N 位通过审计,3 轮至少 1 个 N 的要求就满足了。

## 第 2 轮

**材料(第 1..2 批,B040 + B041):** B041 是 `ts_cov(day_quantile_q25(Ret), day_close(F), 50)` 一族(q25 分钟收益与收盘分钟收益 / 日最高价的滚动协方差,再套 ts_med / ts_stddev),loc 里 6 个 head 的得分是 −0.88 / −1.20 / −1.22 / −1.48 / −1.60 / −1.71,没有一个是真 head;新进来的 head 1 是第 1 轮 R 的替换件 `ts_std(day_quantile_q25(Ret), 5)`(train −0.43 / valid −0.88)。富集表里唯一显著的是 `day_distinct_ratio(Open)`(19 条,含 / 不含 −1.49 / −2.50,p 0.000)与几条慢变日频叶子量(`sub(LogTotalCap, LogFloatShares)` +0.92 等),都是「最不差」,不是「好」,原因是慢,不是有 alpha。

**上一轮预测对不对(第 1 轮):**
- **E(核心 q25(High))。** 预测「出 head 概率约 8%、最好分数落在 −1.0 ~ 0.0」。实际:105 条评分,0 个 head,最好 −1.36(train −1.08 / valid −1.36,`cs_bucket_rank(sub(LogFloatCap, LogFloatShares), q25(High))`),**范围预测偏乐观**。更重要的是读到一个**我上轮没发现的机制性失误**:本流第 1 轮相关度表里,4 个 `cross_delta(·, 241)` 种子(log F 的 241 日增量一族)覆盖率只有 0.85,低于门槛 0.9 被判「废品」(distinct 0.99 没问题)。严格滞后 241 日在这把尺子的样本里吃掉约 14 个点,滚动窗口类(cross_sum / mean / stddev / max)有部分窗口,覆盖率 0.9995;120 日滞后 0.92 能过。所以我押的「分红 / 送转增量」这条线(假设 b)其实**从没被打过分**,E 位的失败只说明水平类和 6 ~ 12 个月动量类没有残差 alpha。
- **N(P 水平与 tick 摩擦)。** 预测「出 head 约 12%」。实际:91 条评分,0 个 head,最好 −0.86(train −0.17 / valid −0.86,`cs_last_low40(div(LogFloatCap, day_distinct_ratio(Open)), day_var(Low))`)是 GP 随机那一半长出来的,我写的 P 水平 / 同桶秩 / tick 计数种子没有一个进前 5(都在 −1.19 以下)。结论:真实价格水平与 tick 摩擦在新尺子下没有残差 alpha(被规模、流动性、已知族与两个冠军吃掉),最好的几条 train 接近 0、valid 更差。我最担心的失败方式(a)(与规模 / 流动性控制被打成同一个东西)大体对了,(c)(低价端的 ST 拖垮 train)没有证据。
- **R(15 个变体)。** 预测「2 ~ 4 个比原 head 好 0.1 且 ρ_known < 0.5,多半是替换」。实际:**只有 1 个**(`ts_std(q25(Ret), 5)`,−0.88 对 −1.13,ρ_known −0.14,ρ_head 0.82,替换);head 3 的长窗口 / 去 signedpower 变体涨到 −0.32 ~ −0.36(valid −0.02 ~ −0.20),但 ρ_known −0.80 ~ −0.83,被「已知族」门挡掉,说明 head 3 的承重量就是已知族的一个近亲(收盘分钟成交额的峰值幅度)。head 2 的拆分:只留均值是 −2.54 且符号翻转、ρ_head −0.95;只留标准差 −0.72、ρ_head 0.97、ρ_known −0.80。即「标准差那一半承重」(我写的备选解读之一),整个 head 2 也是已知族,不会有新 head。收录新 head 的概率 3%:没有发生。

**第 1 轮留下的事实(核对过,下一轮不用再查):**
1. 覆盖率门槛(≥ 0.9)与 distinct 门槛(≥ 0.5,取截面上不同值占比的中位数)都在样本内的评分里;**严格滞后算子(cross_delta / cross_delay 的 d ≥ ~150)会因覆盖率被判废品**,要写滞后就改成 cross_sum / cross_mean / cross_ema 一类的滚动窗口,或用 ≤ 120 的滞后。
2. 存储文档(AlphaCube docs/steering_and_daily_fields.md §1.1)写明日频叶子「存的是收盘时点可知的东西,没有隐式 shift」;FloatShares 来自日度资本表的 `circulating_capital`(流通股数),FloatCap 来自 `circulating_market_value`;`Log*` 是在 float64 里取 log 之后降到 float32(精度约 2 ~ 4e-6)。
3. `ListAge` 对「第 1 天就在库里的老股票」给哨兵值(10000 + 天数),截面上老股票全部并列,所以 `cs_bucket_rank(·, ListAge)` 的分桶实际是按股票列序(交易所 / 板块)切的块,不是按年龄。本轮没有用 ListAge 分桶。
4. 两个库 5583 条表达式里,`ops_ext` 的新算子(day_at_max_ratio、day_centroid、day_distinct_ratio、day_flat_ratio、day_zero_ratio、cross_age、cross_valid_count、cs_state_rank、cs_flip_by_state、cross_semistd_*、cross_madz、day_signed_ratio、day_wmean、day_gini、in_madz、day_flat_run_max、day_es_ratio_*、cross_ema、cross_zscore、cs_bucket_*、day_topw_mean、day_wstd)的出现次数全是 0(逐条 grep 过 members.csv),本轮用到的 `cross_semistd_*`、`day_es_ratio_*`、`day_wmean`、`cross_ema`、`cs_bucket_*` 骨架都不在库里(本机逐条核对过)。
5. 本波 W01 的 head(研究目录 prod_W01/library.json)大量是 `day_centroid(Amt)`、开盘价跳空与首分钟成交额的 60 日相关、`cs_first_low20(·, ListAge / LogFloatCap)` 这类阶跃带,这些东西的 |ρ| ≥ 0.7 会被库禁令拒绝,所以朝那个方向写的种子大概率被拒,本轮刻意避开。
6. **distinct 门槛对「事件稀疏」的量很严**(别的流 2003 第 2 轮的相关度表里的实测,真实数据):`sub(LogTotalCap, LogFloatCap)` 水平 distinct 0.73 过;`cross_delta(sub(LogTotalCap, LogFloatCap), 241)` 覆盖率 0.852 / distinct 0.631 判废品(覆盖率);`cross_delta(·, 60)` distinct 0.29、`cross_delta(·, 120)` 类 distinct 0.22 判废品(无变化的票精确等于 0,并列太多);`sub(LogFloatCap, LogFloatShares)`(真实价格)distinct 0.68(0.01 元格点造成并列)。所以事件类的量要写成 241 日求和(约六成以上的票有事件)或连续的 cross_ema,不要写短窗口求和,也不要把事件稀疏的量塞进分桶 z 分数(无事件的票会被压成每桶一个值)。
7. 草稿目录是共享的:`scratchpad/` 下别的 PI 也在写同名文件(我的 `skel_check.py` 被覆盖过一次),自己的临时文件要放进专属子目录(本轮用 `scratchpad/pi2014_r2/`)。

**目前对这个种子 alpha 来源的信念(很弱,比第 1 轮更弱):** 这个流的批(q25 分位一族、q25 与收盘价的协方差一族)全部是「波动 / 成交额 / 后复权价格水平」的已知量换写法,新尺子把它们吃光;第 1 轮 N 位也证明价格水平与 tick 摩擦没有残差。库和冠军都读不到的、又不是水平量的,只剩日频叶子上的**事件流**(分红 / 送转 / 摊薄 / 解禁)和 ops_ext 的**新算子读出的路径形状**。本轮就押这两条,而且都选「慢、有界或无量纲、不靠严格滞后」的写法。

**本轮的任务与事先预测:**
- **槽 1(N):净派现 − 摊薄的事件流(后复权收盘价与流通市值的日变化之差,逐日增量求和 241 日),加解禁腿(log 总股本 / 流通股本的水平与增量)。** 种子 14 个,主种子 `cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241)`,其余是半衰期 60 / 120 日的 ema 版、四种十分位中性版、|增量| 求和版、解禁腿水平 / 增量求和 / 对规模的回归残差、两腿秩相加。预测:**出 head 的概率约 8%**(整个任务里最有机制支撑的一个:净发行异象、解禁抛压、红利风格都是持久的事件流;也是本流前面所有路径里唯一没被打过分的),最好分数落在 −0.8 ~ 0.0。最可能成功的形态:主种子按规模或按真实价格十分位中性后的版本(`cs_bucket_zscore(S1, LogFloatCap)` / `cs_bucket_rank(S1, 真实价格)`),因为分红股集中在大市值 / 低波动,不中性化时被控制吃掉。最可能的失败方式:(a)派现与大市值 / 低波动 / 低换手高度共线,被 5 个控制与两个冠军吃光残差;(b)train 与 valid 的红利风格方向相反(2023-08 以后红利大涨,2018 ~ 2023 风格混杂),min 为负;(c)事件稀疏,约三成无事件的票落在数值噪声里,若多头书取到这一端,排序会随机打转;(d)覆盖率或 distinct 门槛意外不过(本机只核对了解析、骨架不在库里与算子定义,没有算过任何真实数据)。
- **槽 2(N):已实现收益不对称(日度后复权收盘价的上行 / 下行半离差之比)与日内右 / 左尾形状差。** 种子 13 个,主种子 `(pos − neg) / (pos + neg)`,pos / neg 为 `cross_semistd_pos / neg(day_close(Close), 120)`,另有 60 / 241 日、VWAP 与开盘价版、波动 / 规模 / 成交额十分位中性版、ema 版、60 减 241 日、日内 `day_es_ratio_hi − day_es_ratio_lo` 的 60 / 241 日均值与其秩和。预测:**出 head 的概率约 4%**(彩票 / 偏度偏好是个持久的行为偏差,但这类效应在 A 股的多头腿常常被波动和反转控制吃掉,而且牛熊市里的符号可能不同)。最好分数落在 −1.2 ~ −0.3。最可能成功的形态:按波动十分位中性的 120 日版,或 60 减 241 日;最可能的失败方式:(a)A 与 20 日反转(近期大涨日)相关,被新尺子去掉;(b)train 与 valid 符号相反;(c)日内右 / 左尾那条腿在薄成交的票上大量缺失,覆盖率不够。
- **R(9 个变体,两个 head):** head 4 `ts_med(ts_cov(q25(Ret), day_close(Ret), 50), 40)` 的 4 个变体(协方差换成相关系数、窗口拉到 80 ~ 120、按波动中性),head 1 `ts_std(q25(Ret), 5)` 的 5 个变体(除以 60 日平均波动、规模 / 波动十分位 z 分数、右尾减左尾、ema)。预测:**满足「比原 head 好 0.1 且 ρ_known < 0.5」的 1 ~ 2 个**(head 4 的相关系数 / 长窗口版最可能,因为拆解表里 80 日窗口已经好 0.21);收录为新 head 的概率 < 2%,没有一个会到 0.5。head 1 的验证段(−0.88)比训练段(−0.43)差,说明尺度处理未必能救,这是信息型实验。

**给下一轮的备忘:**
- 第 3 轮会看到 B042(`day_std(pow_3(F))`,三次方的日内离散度,是尾部厚度的一个写法)。如果槽 2 的不对称线有信号(任何一个种子 score > −0.5 且 train / valid 同号),第 3 轮用 E 位,核心取本轮 A 的主表达式(它会作为快照 head 或富集表子树出现;注意核心与每个控制 |ρ| < 0.8),外围换成「尾部厚度 / 三次方离散度」一族。如果槽 1 有信号,第 3 轮 E 位核心取 S1(同样要先在 loc 里出现),外围换成 `cs_last_low10 / cs_last_high05` 一类的排除筛(把近期解禁、摊薄最重的票排除出多头书),注意不要写成 W01 head 那种 `cs_first_low20(·, ListAge)` 的写法(会被库禁令拒绝)。
- 如果两个槽都没有 head:第 3 轮 N 位换成「市场状态同步性 / 价格延迟」一条线,第 1 轮笔记里那份草稿还在(`cross_corr(cs_mean(day_quantile_q25(Ret)), day_quantile_q25(Ret), 60)`、`cross_corr(ts_delay(cs_mean(day_sum(Ret)), 1), day_sum(Ret), 60)` 等,骨架都不在库里);Amt 类分布统计不要押(与 liq 控制 |ρ| 常 ≥ 0.8)。
- E 位的核心至多再用 `day_quantile_q25(High)` 1 次;任何 E 核心都要先问自己「它会不会被 liq / known / size 控制吃到 |ρ| ≥ 0.8」。`day_distinct_ratio(Open)` 是富集表里 p 最小的核心,但它是流动性 / 价格格点的近亲,第 3 轮若没有更好的线索可以当 E 位核心试一次。

## 第 3 轮

**材料:** B040–B042 三个批(q25 一族、q25 与收盘价协方差一族、`day_std(pow_3(F))` 一族)和第 1、2 轮任务。9 个 head 全为负(最好 -0.71),不是真 head。前两轮 8 个任务位至今 0 个过线;最接近线的是 `cross_semistd_pos(day_gini(Low), 241)`(train -0.01 / valid +0.12)和 `cross_ema(cross_delta(sub(log(day_close(Close)), LogFloatCap),1),120)`(train -0.59 / valid +0.25)。两者的短板都是 train(2018-2023),valid 已接近或为正。

**目前对 alpha 来源的信念(很弱):** 分钟统计批全是波动 / 成交额 / 价格水平的换写法,被新尺子吃光。仅剩的线索来自库与冠军都读不到的东西:日频叶子上的事件流(净派现 − 摊薄)和 ops_ext 新算子读出的日内形状(gini)。两者共同的问题是 train / valid 符号或强度不一致,可能与市场状态有关,所以本轮外围押 `cs_flip_by_state` 和『相对自身历史的异常』(cross_zscore / 短减长 ema)。

**本轮任务(都是 E,N 位已在第 2 轮通过审计):**
- 槽 1 E,核心 S1 = `cross_sum(cross_delta(sub(log(day_close(Close)), LogFloatCap), 1), 241)`(共性表第 2 位,含它的 19 个候选均值差 +0.85)。外围:状态翻转、zscore、对 ListAge / 总流通市值差中性化、减解禁腿。事先预测:出 head 概率约 8%;最可能形态是 `cs_flip_by_state` 或 ListAge 中性版;失败方式:(a)被大市值 / 低波动控制与两个冠军吃光,(b)train 仍为负,(c)事件稀疏的票被噪声排序。预期最好 -0.6 ~ +0.2。
- 槽 2 E,核心 `day_gini(Low)`。外围:zscore / madz / 短减长 ema、下行与上下半离差之差、与 gini(High) / gini(Close) 之差、状态翻转、规模 / 成交额 / 波动中性化。事先预测:出 head 概率约 6%(上轮 semistd 版已逼近 0,说明不是零,但离 0.5 很远);最可能的形态是半离差之差或 zscore 版;失败:gini 与流动性 / 波动控制 |ρ| 高,被残差化吃掉。预期最好 -0.5 ~ +0.2。
- R:不写(拆解表里唯一好 0.1 的变体仍是 -1.4 量级的假 head,没有意义)。

**上一轮预测对不对:** 第 2 轮预测『槽 1 出 head 8%、槽 2 4%』:都没出。槽 1 最好 -0.59(预测 -0.8 ~ 0.0,对),失败方式(b)(train 弱)命中;槽 2 的 A 族没有给出像样的分,反而是 Pr2b 里 `cross_semistd_pos(day_gini(Low), 241)` 的 -0.01 意外最好。R 预测『1 ~ 2 个比原 head 好 0.1』:实际 head 4 的 cross_med 长窗口版与 +80 窗口分桶版替换了原 head(与预测一致),head 1 的变体全部变差(与笔记中的怀疑一致)。
