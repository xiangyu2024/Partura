# F114_q25_closeret 研究日志

只追加、不改写。[auto] 是工具自己记的(启动了什么、什么时候跑完);其余是研究员写的:
每看完一个结果,写下它说明了什么、哪条假设变了、下一步做什么。接手的人先读这里(`./scripts/study.sh brief F114_q25_closeret`)。

### 2026-10-04 13:04 [执行] R0 建档完成:读通内核源码与基线,写了 01/02/03/06 四份 notes 和结果卡

看到了什么:表达式 cross_quantile_q25(day_close(Ret), 15) 是两层直链(day_close 折叠分钟轴取当天最后一个有效分钟值,
cross_quantile_q25 在交易日轴上滚动 15 天取 0.25 分位数),整条链对 Ret 齐次度=1,没有重复子树、没有恒等节点。
S0_baseline 复现用户表:方向-1、hl=20、utrain LS=+2.36、utrain Lgross=+5.9%(与 published.ls[0]/long[0] 对上;
published.long 对应毛超额不是净超额,Partura 另算的 utrain 净超额是+3.6%)。train/valid 多头腿净超额+1.8%/+8.1%,
long_share 19%~31%(钱大部分在空头腿),分位剖面 train 不单调(Q10<Q8/Q9)、valid 单调,全控制变量中性化 R²=0.162、
残差 Lnet 掉到-20.8%但 rank IC 没变号,cov=1.00/dist=0.62 两道门槛都过,hlL 与 hlS 都选到网格上限 20(没有分化)。
holdout 未读。

判断:这一轮只建档,不提假设、不下结论(执行角色的分工)。四份事实文件(01_expression/02_operators/03_decomposition/
06_baseline)已写完整,结果卡 results/R0.md 汇总了要点和下面这些异常。

异常(写进了 R0.md 第"注意到的异常"节,不重复展开):(a) S0_baseline.json 顶层 rank_by="ls" 与当前配置的
rank_by: long 不一致,但 hlL/hlS 字段各自独立存着且数字看起来没受影响,没有验证是否需要重跑;(b) 顶部决策口径表的
rICtraded tr/va 两列展示为空,但 JSON 的 neutralise._traded_signal.rank_ic 里其实有 train 的数(+0.0070),是展示层
留空不是数据缺失;(c) Ret 字段的精确定义(简单/对数收益、基准价格)本地没有直接文档,只有旁证推断,没有另写探针验证。
errors={}、两个算子的探针表都完整,没有求值失败或读数为空的情况。

下一步:不是我(执行)该决定的 —— 留给主研读 state.md/results/R0.md 之后写假设表和第一张工单。我没有碰
scripts/、partura/、workflows/、handoff/、lab/、docs/,也没有碰 configs/F114_q25_closeret.yaml(含未填的 title 占位行,
因为"用一句话写它是什么"属于判断,没有在这一轮填)。

### 2026-10-04 13:22 [主研] 第 1 轮:找到精确恒等式 —— 信号 = (IQR − 四分位中点)/2,把分辨与升华合成一个实验;下工单 R1(3 阶段/12 变体/2 次运行)

看到了什么(读 R0 建档 + 基线,没有新跑实验):
1. 语义上唯一骗人的地方:day_close 是 day_last 的别名,喂的是 Ret(逐分钟收益),所以这是"当天最后一个有效分钟
   那一笔分钟收益",不是收盘价也不是当日收益。因子名 q25_closeret 会误导。
2. 这棵树的"门控"和"放大"两个语法角色是空的(无逐元素二元节点、无布尔、齐次度 1)。所以唯一可问的实质问题是
   "读出的那个顺序统计量在读什么"。
3. **本轮最重要的产出 —— 一条精确恒等式**:令 loc = q75+q25(四分位中点x2,纯位置)、scl = q75-q25(IQR,纯尺度),
   则 q25 = (loc-scl)/2,可交易信号 = -q25 = (scl-loc)/2。即原式精确等于「尾盘分钟收益 15 日离散度」减「其典型水平」,
   权重 1:1 —— 而这个 1:1 是机械挖掘选到 q25 时的副产品,不是学出来的。于是"这是什么"变成两个可分别造出来、
   分别测的表达式(add/sub,两个算子都在注册表里,已核对)。
4. 基线里最可操作的一条线索:对 ctl_ivol 中性化后残差 rIC 反而从 +0.0070 升到 +0.0136(接近翻倍)、残差 Lgross
   +4.1%→+5.8%,而 R² 只有 0.032。即因子带着一个**不想要的**波动暴露,剥掉信号更强。恒等式刚好把这个暴露隔离成
   scl 一项、剩下的隔离成 loc 一项。
5. hlL = hlS = 20 都顶到 EMA 网格上限,固定半衰期表和衰减表都单调升到边界没掉头 → 这条因子没有"换成多头最优
   半衰期白捡几点"的空间;想加长记忆只能改窗口,而窗口是结构不是平滑(归因干净)。

判断:
- 决定**不**花运行去确认"它是不是已知暴露":all_controls R² 只有 0.162、最高单控制 0.054、最高 rank 相关 0.22,
  基线已经答了,信息量太低。
- S1_shape 同时是最锋利的"分辨"实验和最直接的"升华"线索,一次运行回答两件事,所以它是第一张工单。
- s1_q75 的引擎自选 sign 是一个不花钱的关键比特:q25 选到 -1 与"尺度驱动"和"位置驱动"两种读法都相容、区分不了;
  而 q75 对尺度的载荷符号翻转,所以 sign=+1 → 尺度,sign=-1 → 位置。
- 裁决 R0 异常 1(S0 顶层 rank_by="ls" vs 配置 rank_by: long):**不重跑 S0**。这条因子 hlL==hlS==20,两种选法
  同一个答案,顶层标量不可能影响已读到的任何数字;hl_long/hl_ls 两字段独立存着。省一次运行。但立下规矩:
  所有跨运行比较从 hlL 列和固定半衰期表读,不从可能依赖 rank_by 的表头列读。
- 事前就记下 H11(制度骑乘):valid(2022-01~2023-08)整段落在小盘/高波动占优的制度里,所以 valid Lnet +8.1%
  远高于 train +1.8% 不是"样本外更强"的证据,是制度。留出段跨过 2024 年初微盘股回撤,若 H11 成立应当见到回撤。
  这条现在写下,免得读完留出段再"发现"。
- 先验上 H12(相对已知家族没增量)和 H13(多头腿不可用)都不利:已知家族 Lnet tr/va +9.3%/+18.5% 压过原式
  +1.8%/+8.1% 一倍以上;train 分位剖面 Q8 +4.9% > Q9 +4.7% > Q10 +4.4%,最高分位不是最好的一档,Q1 -17.8% 独大。
  否定性结论是开着的,不会为了有个升华版去凑。

决定做什么:写定 04_grammar.md(结构语法 + 恒等式)、05_hypotheses.md(15 条,每条带"预测什么/哪个实验能杀死它")、
state.md(8 节),下工单 R1 = 3 个阶段 / 12 个变体 / 2 次服务器运行:
  S1_shape(6):s1_q75(sign 判据) s1_loc(纯位置,升华主线) s1_scl(纯尺度) s1_q50(单算子纯位置) s1_std s1_min
  S2_where(3):s2_daysum(≈当日收益,检验"它只是日收益下四分位数") s2_daymean s2_dayopen
  S3_window(3):s3_w5 s3_w30 s3_w60
S2_where 与 S3_window 合在第 2 次运行里跑(run 支持一次多个 stage),这样"一个阶段一个问题"和"一张工单 2 次运行"都不破。

决定**不**做什么:(a) 不跑 cross_mean(day_close(Ret),15) —— 把额度让给恒等式那一对,它只是 s1_loc/s1_q50 的
非稳健版,同一条轴已由 s1_std vs s1_scl 在尺度侧测了(列为 add() 不合法时的替补);(b) 不用 in_slice 切日内中段分钟
—— 在手写库里、参数含字面量,而 day_sum/day_mean/day_open 已能回答"位置特不特殊";(c) H9(封板票撑空头腿)、
H10(零值占比)、H15(Ret 定义)推迟到 R2 的一个自写脚本里一次量完;(d) H12(已知家族增量)故意推迟 ——
现在还不知道最终结构是谁,给一个马上要被替换的结构量增量是浪费一次运行。

### 2026-10-04 13:27 [auto] 启动 run S1_shape:阶段 S1_shape

### 2026-10-04 13:53 [主研] 第 1 轮(第二次接手):R1 在飞行中,按任务书第 2 条不另开工单,原样交回执行;顺手把 propose 草稿审完

看到了什么(没跑任何实验):
1. 最新工单 orders/R1.md 没有对应的结果卡 → 任务书第 2 条:不另开工单,把 R1 原样交回执行。
2. 读执行的流水 handoff/.../work_R1_ac7d2be29a60e99e6.md,确认它**不是出错**:填 title ✓ → propose ✓ →
   三个阶段写进配置 ✓ → check 24/24 OK ✓ → run S1_shape 启动成功 ✓ → **wait 这一步的工具调用被拒**,
   agent 在 13:37 停住(就是用户说的那批"停止的、error 的")。
3. ./scripts/study.sh list 显示 S1_shape **还在服务器上跑**(634794.pt_F114_S1_shape,没有退出行),
   本地还没有 logs/F114_q25_closeret_S1_shape.log —— 这是正常的(日志随运行结束拉回),不是丢了。

判断:
- **S1_shape 不能重启**。它活着,重 run 一次等于白烧一次服务器额度(R1 的上限就是 2 次),而且会把同一个 tag 覆盖掉。
  执行接手的第一条命令应该是 list 确认、然后 wait。只有 list 显示 exit 97(内存守卫让路)才需要重跑。
- **check 24/24 全过是一个实质读数,不只是流程记录**:它意味着 add / sub / cross_quantile_q75 / cross_quantile_q50 /
  cross_stddev / cross_min 以及 S2/S3 全部表达式都合法 → R1 工单里那条「兜底」条款(add/sub 不合法时改用 cross_mean)
  **不会触发**,恒等式那一对 s1_loc / s1_scl 能真的跑出来,升华主线没被语言限制挡住。已写进 state.md §2 末。
- **替执行把 propose 的 16 条草稿审了**(工单第 0 步第 2 项要的就是主研核对有没有漏兄弟算子):R1 的变体表**不改**。
  其中一条要点出来 —— propose 推荐的 sub_B_cross_max **是错的尾巴**:q25 是分布的下四分位,它的极值兄弟是
  cross_min 而不是 cross_max(max 对应 q75 那一侧),所以 R1 选 s1_min 是对的,后面的人不要照 propose 换成 max。
  其余:day_mean/day_sum/win_5/30/60 R1 已有;win_10 故意跳过(离 15 太近);durbin_watson/ar1 与"位置还是尺度"无关。
- propose 另外提醒到两条值得进 R2 候选池的**诊断**(不是候选结构,已写进 state.md §6):
  (a) iso_A = day_close(Ret) 单独跑 —— "15 日记忆层挣不挣钱"最干净的探针,看毛超额/rIC 而不是净值(它换手必然极高);
  (b) cross_argmin(day_close(Ret),15)(齐次度 0)—— 问"哪天坏"而不是"坏到什么程度",天然不带波动暴露,与 H10 同向。

决定做什么:只落盘、不下新工单。覆盖重写 state.md(新增 §8.1 一张"R1 每一步做到哪、从哪接"的表,
把"别重填 title、别重写配置、别重启 S1_shape、propose 输出在哪"四件事钉死),返回 status=order / order=R1 / kind=experiment。

决定不做什么:(a) 不新开工单、不改 R1 的任何一条变体(结果还没出来,改了就是凭空换设计);
(b) 不自己去 wait / digest / 跑任何命令 —— 那是执行的分工,主研只读不跑;(c) 不动 configs(执行正在用它跑第 2 次运行);
(d) 不碰 scripts/ partura/ workflows/ handoff/ lab/ docs/ 和别的因子。

### 2026-10-04 14:01 [执行] R1:S1_shape 已在服务器跑完(exit 0),读数完成,未重跑

list 显示 S1_shape exit 0、JSON 已拉回,未重新 run(上一个执行只是 wait 被中止,进程本身跑成功了)。
digest 读数(train/valid 多头口径 Lnet,v_base 对照 +1.8%/+8.1%):
s1_q75 sign=+(尺度驱动读数) -1.4%/+2.8%;s1_loc -0.7%/+5.9%;s1_scl +0.6%/+8.0%;s1_q50 +0.9%/+6.0%;s1_std -1.1%/+2.2%;s1_min +2.0%/+0.0%。
六个新变体 train+valid 都没有同时超过 v_base。异常:s1_q50 的 dist=0.16,跌破用户 0.5 门槛(其余 5 个变体 dist 0.63~1.00 都过);
s1_min 的 hlS=10,是本阶段唯一没顶到半衰期网格上限20的(其余 hlL/hlS 全部=20)。errors={}。
下一步:按 R1 把 corr_ids/profile 改成第2次运行版本,run S2_aperture(S2_where+S3_window),然后写 results/R1.md。

### 2026-10-04 14:02 [auto] 启动 run S2_aperture:阶段 S2_where S3_window

### 2026-10-04 14:08 [auto] S2_aperture 跑完(exit 0);重看结果:./scripts/study.sh digest F114_q25_closeret S2_aperture

### 2026-10-04 14:15 [执行] R1:S2_aperture 跑完(exit 0),S2_where+S3_window 读数完成

S2_where:s2_daysum 与 s2_daymean 的全部数字逐位相同(Lnet/Lshp/rIC/profile/sweep 全部一致,与v_base的rank相关都是+0.00),
两者 train/valid Lnet 都远低于v_base(-19.1%/-7.9% vs +1.8%/+8.1%),与v_base rank相关≈0,H6(等价于日收益15日下四分位数)
没有被支持。s2_dayopen 严重异常:dist=0.0003(远低于0.5门槛)、train/valid 的 rIC/rank_ic_t/rICtraded 全部是NaN(不是展示留空,
JSON里原始就是NaN),固定半衰期表5档数字完全相同(信号几乎退化为常数),与v_base的rank相关也是NaN。
S3_window:s3_w5 dist=0.4076,跌破0.5门槛(三个门槛失败变体现在是 s1_q50 dist0.16、s2_dayopen dist0.0003、s3_w5 dist0.41)。
s3_w30(hlL=20,train Lnet+2.6%/valid+8.3%/Lshp+0.47/+1.66)与s3_w60(hlL=3,train+3.5%/valid+8.6%/Lshp+0.60/+1.59)
train上Lnet都高于v_base(+1.8%),且在固定半衰期表同一列hl20上也都高于v_base的hl20(+1.8%/+0.33)——不是半衰期挑选的功劳;
valid的Lshp两者都略低于v_base(+1.78)。s3_w5两档都低于v_base。与v_base rank相关:s3_w30+0.92、s3_w60+0.76、s3_w5+0.91,
s1_loc+0.70、s1_scl+0.69(与S1轮一致,缓存值未变)。errors={}。results/R1.md 正在写。

### 2026-10-04 14:18 [执行] R1:两次服务器运行(S1_shape、S2_aperture)都已读完,results/R1.md 写完

R1 工单的 2 次运行、12 个变体全部跑完(exit 0,errors={}),没有触发工单的兜底条款,没有改表达式。
结果卡 notes/F114_q25_closeret/results/R1.md 已写完,覆盖工单要的全部7节数字(主表/固定半衰期表/rank相关/
分位剖面/逐年/中性化/异常元信息)。最关键的几个数字:
- s1_q75 引擎自选 sign=+1(尺度驱动读数)。6个新变体(S1)train+valid都没有同时超过v_base(+1.8%/+8.1%)。
- 门槛失败3个:s1_q50 dist=0.16、s2_dayopen dist=0.0003(且rIC全NaN,不是展示问题)、s3_w5 dist=0.41。
- s2_daysum与s2_daymean输出逐位相同;两者与v_base的rank相关都是+0.00,H6(=日收益15日下四分位数)缺乏支持。
- s3_w30(train+2.6%/valid+8.3%)与s3_w60(train+3.5%/valid+8.6%)是12个新变体里唯一在train+valid的Lnet
  都超过v_base的两个,且在固定半衰期表同一列hl20上也都超过v_base(+1.8%/+0.33),不是半衰期挑选的功劳。
- s1_loc的逐年long_share在2019/2020被放大到+289%/+829%(分母long_gross+short_gross接近零导致比率不稳,
  两条腿绝对数字本身正常),已在结果卡里拆开分子分母说明。
- 没有写07_*.md(工单只说"可以"贴,不是必须;留给主研或下一轮)。没有碰state.md(主研的职责)。
下一步不是我该定的:留给主研裁决H1~H8并决定R2怎么下。
