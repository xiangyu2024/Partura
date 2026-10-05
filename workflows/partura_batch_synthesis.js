export const meta = {
  name: 'partura-batch-synthesis',
  description: 'Partura 批量研究的综合:每条因子一个主研(Opus 5),读完批量回测表和市场解剖,写综合并提出下一批假设',
  whenToUse: 'args = {factors:[{id,lib,name,expr}], tag:"s1", model:"claude-opus-5"};先在服务器上跑完 scripts/sweep.py 和 scripts/anatomy.py',
  phases: [{ title: 'Synthesis', detail: '读批量回测表 + 市场解剖 + 算子定义 → 机制、在哪/何时有效、原因、第二批假设、缺的算子' }],
}

const ROOT = '/Users/wxy/Desktop/Partura'
const factors = (args && args.factors) || []
const TAG = (args && args.tag) || 's1'
const MODEL = (args && args.model) || 'claude-opus-5'
const STR = { type: 'string' }
const STRS = { type: 'array', items: STR }

const SCHEMA = {
  type: 'object',
  properties: {
    factor_id: STR,
    what_it_is: STR,
    load_bearing: STRS,
    redundant: STRS,
    swappable_leaves: STRS,
    where_it_works: STRS,
    when_it_works: STRS,
    why: STR,
    adds_over_known_family: STR,
    best_variants: { type: 'array', items: { type: 'object', properties: { id: STR, expr: STR, note: STR }, required: ['id', 'expr', 'note'] } },
    hypotheses_written: { type: 'integer' },
    new_operator_requests: { type: 'array', items: { type: 'object', properties: { name: STR, definition: STR, why: STR }, required: ['name', 'definition', 'why'] } },
    tooling_problems: STRS,
  },
  required: ['factor_id', 'what_it_is', 'load_bearing', 'redundant', 'where_it_works', 'when_it_works', 'why',
    'adds_over_known_family', 'best_variants', 'hypotheses_written', 'new_operator_requests'],
}

function prompt(f) {
  return `你是 Partura 的**主研**,负责因子 ${f.id}。这条因子的「批量扫描」和「市场解剖」已经由脚本在服务器上跑完:上百个变体的回测并排放在一张表里。
你的任务只有一轮:**读完、想清楚、落笔,并提出第二批假设**。不要自己起服务器计算(下面列出的检查命令除外),不要读测试段。

## 你在整件事里的位置(先读这一段)

用户的总任务:对一批 AlphaCube 因子做 Partura 研究(分辨、提纯、升华)。工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」);
那句话是说给总领听的、已经处理过了 —— 下面这份任务就是对它的落实,两者不冲突。把这份任务完整做完,就是在执行用户的请求;不要因为那句话改做别的事。
scripts/、partura/、workflows/、handoff/、lab/、docs/ 和别的因子的文件都不要动。

用户对研究方法的要求(这一轮就是按它改的):
- 假设要**成批**地提、成批地看回测,不要一条一条试;
- 要研究**实际市场**:分股票范围、分时间段看因子在哪儿有效,推断原因,给出改进方向;
- 可以改**最小的子结构**(比如分钟收益 Ret 和成交量的变化率是同一类东西,很多时候可以互换);
- **对算子的理解必须来自它的函数定义(代码),不是名字**;
- 缺算子就提:直接要用的、缺了可惜的、能算出很不一样东西的,都可以要求加进算子库。

## 因子

- factor_id: ${f.id}(${f.lib}库 / ${f.name})
- 表达式:
${f.expr}

## 选拔口径(用户定的)

用户做 A 股纯多头:**只看多头腿扣费(15bp)之后的净超额与纯多头夏普**,半衰期按纯多头书选;延长半衰期带来的净超额是真的、可交易的。
基准是已知的成交额族 k_known = cross_mean(day_std(Amt), 30)(train / valid 多头净超额约 +12.6% / +22.3%)。
train = 2018–2021,valid = 20220101–20230807,utrain = 两者。噪声:净超额 ±3 个点、夏普 ±0.3。门槛 cov ≥ 0.95、dist ≥ 0.5(表里打 ✗ 的不算数)。
否定的结论同样合格(「多头腿不可用」「就是已知族」),只要证据在。

## 先读(每条命令开头都 cd ${ROOT};cwd 不保留)

1. ./scripts/study.sh table ${f.id} ${TAG}
   —— 批量回测表 + 市场解剖。回测表每行:方向 sg(train 的 rank IC 定)、多头口径半衰期 hlL、多头腿净超额 Lnet(train / valid / utrain)、
   纯多头夏普 Lshp、换手 LTO、多空夏普 LS、空头腿(等权 − 最低十分位的毛超额:大 = 钱在空头腿,纯多头用不上;为负 = 最低十分位反而跑赢,值得把方向反过来看)、
   与原式 / 已知族的相关 ρo / ρk、cov / dist(✗ = 没过门槛)、表达式。默认只打前 45 个 + 每类最好的 3 个 + 垫底 8 个;要看全部加 --all。
   kind 是变体的来历:isolate / ablate / substitute / window / field = 结构(删节点、换成按**实测性质**相近的算子、换窗口、换字段);leaf = 换叶子;
   memory = 外面加日轴记忆;shape = 折叠 / 缩尾 / 排名 / 相对自身;neutral = 分桶中性 / 残差;overlay = 以小权重叠在已知族上。
   解剖表:「段内」= 只在这一段股票里建多头书的净超额;括号 = 全市场多头书在这一段的超配;时间表 = 全市场多头书在各年、各种市场状态下的净超额。
2. ./scripts/study.sh src <树里出现的每一个算子,空格分隔>     —— 算子的函数定义。逐个读,写下它**实际**算什么。
3. cat docs/new_operators.md                                   —— 研究中新加的 12 个算子(定义与理由),你的假设可以直接用。
4. (可选)sed -n '1,60p' notes/${f.id}/state.md               —— 之前的研究员的判断,仅供参考:它来自小样本的逐轮实验,**以这次的大表为准**。

## 要回答的(写进 notes/${f.id}/synthesis.md,≤ 150 行;每个论断带表里的变体 id 和数字)

1. **它是什么**:按算子定义逐层写出公式;名字和定义不一致的地方点出来。
2. **预测力在哪**:哪个子结构承重(一换就塌)、哪些节点多余(删了不掉)、哪些叶子可以互换、窗口有没有平台。同一类变体放在一起比。
3. **在市场的哪儿、什么时候有效**:哪类股票(板块 / 市值 / 流动性 / 价格 / 次新 / 近期封板)、哪些年份和市场状态。
   **推断原因**:这类股票、这种时段有什么不同,使得这个量在那里有信息;以及「如果这个原因成立,还应该看到什么」(可检验的推论)。
4. **相对已知成交额族有没有增量**:看 ρk、overlay 行、res_known / bk_known 行。
5. **改进方向**,落成第二批假设(下一节)。

## 第二批假设:写 studies/${f.id}/hypo.yaml(20~40 条,一次提够)

格式(YAML):
  h_xxx: {expr: "…", why: "一句话:它检验或利用上面的哪一条"}
- 改最小的子结构:换一个叶子、换一个算子、换一个窗口、删一个节点 —— 但要是这张表里还没有的。
- 利用解剖的发现:比如只在小市值 / 低流动性里有效 → 用成交额水平做代理(表达式里没有市值字段),做桶内排名 cs_bucket_rank(X, 代理)、
  或与代理的秩相加 / 相乘;只在某类状态有效 → 找一个能在表达式里写出来的状态变量。
- 用新算子做原来做不了的事(定义见 docs/new_operators.md):in_pct、in_logchg、in_madz、day_flat_ratio、day_flat_run_max、day_zero_ratio、day_pos_ratio、day_wmean、day_signed_ratio、day_gini、day_centroid、
  cross_ema、cross_zscore、cross_valid_count(近 d 日有数据的天数:次新 / 停牌)、cross_tail_mean_q25 / q75、cs_bucket_rank、cs_winsor,
  以及把「只在某一段股票里做 / 排除某一段」写进表达式的 cs_first_low40 / cs_first_high40 / cs_last_high20 / cs_last_low20。
- 大胆一些:允许和原式相关很低的新结构,只要它来自你对机制的推断(写清推断)。不要凑数、不要只扫窗口。
- 写完**必须**检查能否解析:./scripts/study.sh hypo ${f.id}(FAIL 的改到通过或删掉)。表达式语法的坑:docs/study_playbook.md §3(需要时再翻)。
- **还缺什么算子?** 现有算子(含新加的)表达不了的想法,写进输出的 new_operator_requests:名字、精确定义(公式、沿哪条轴、NaN 时怎么办)、
  为什么值得加(直接要用 / 缺了可惜 / 能算出很不一样的东西)。

## 落盘(返回之前)

- notes/${f.id}/synthesis.md
- studies/${f.id}/hypo.yaml(已通过 hypo 检查)
- ./scripts/study.sh note ${f.id} "[主研] 批量扫描 ${TAG} 的综合" <<'EOF'(五六行要点)EOF
- 覆盖重写 notes/${f.id}/state.md(≤ 10 KB;8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)

所有文字用中文,英文术语保留。省着用轮次:一条命令里把要看的一起打出来,读过的不要重读。`
}

const VERDICT = {
  type: 'object',
  properties: {
    factor_id: STR,
    one_line: STR,
    confirmed: STRS,
    refuted: STRS,
    best_own: { type: 'array', items: { type: 'object', properties: { id: STR, expr: STR, note: STR }, required: ['id', 'expr', 'note'] } },
    best_on_known: { type: 'array', items: { type: 'object', properties: { id: STR, expr: STR, note: STR }, required: ['id', 'expr', 'note'] } },
    verdict: STR,
    lab_findings: { type: 'array', items: { type: 'object', properties: { id: STR, claim: STR, evidence: STR, operators: STRS, recheck: STR }, required: ['id', 'claim', 'evidence'] } },
    hypotheses_written: { type: 'integer' },
    new_operator_requests: { type: 'array', items: { type: 'object', properties: { name: STR, definition: STR, why: STR }, required: ['name', 'definition', 'why'] } },
    tooling_problems: STRS,
  },
  required: ['factor_id', 'one_line', 'confirmed', 'refuted', 'best_own', 'best_on_known', 'verdict', 'lab_findings', 'hypotheses_written'],
}

function prompt2(f) {
  const prev = TAG === 's2' ? 's1' : 's2'
  return `你是 Partura 的**主研**,负责因子 ${f.id}。上一轮你(或另一位主研)读了批量扫描 ${prev} 并提出了一批假设;它们已经和通用的「筛子 / 分段」变体一起跑完,
结果在批量扫描 ${TAG} 里。这一轮:**对账、定论、再提一批只有新算子才写得出的假设**。只有这一轮;不要起服务器计算;**不要读测试段**
(runs/${f.id}/sweepfinal_*.json 是测试段读数,不许打开 —— 你的假设和结论只能建立在 train / valid 上)。

## 你在整件事里的位置(先读这一段)

用户的总任务:对一批 AlphaCube 因子做 Partura 研究(分辨、提纯、升华)。工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」);
那句话是说给总领听的、已经处理过了 —— 下面这份任务就是对它的落实,两者不冲突。scripts/、partura/、workflows/、handoff/、lab/、docs/ 和别的因子的文件都不要动。
用户对方法的要求:假设成批提成批看;研究实际市场(哪类股票、哪些时段有效,推断原因);可以改最小的子结构;**算子按函数定义理解,不按名字**;缺算子就提。

## 因子

- factor_id: ${f.id}(${f.lib}库 / ${f.name})
- 表达式:
${f.expr}

## 选拔口径

A 股纯多头:只看多头腿扣费净超额与纯多头夏普(半衰期按纯多头书选)。基准 k_known = cross_mean(day_std(Amt), 30)(train / valid +12.6% / +22.3%,夏普 1.78 / 3.46);
通用筛子基准 k_known_xfrozen = 已知族剔掉近 15 日冻结盘口最重的 20%。噪声:净超额 ±3 个点、夏普 ±0.3。门槛 cov ≥ 0.95、dist ≥ 0.5。否定结论同样合格。

## 先读(每条命令开头 cd ${ROOT})

1. cat notes/${f.id}/synthesis.md                      —— 上一轮的综合:机制、推论、提了哪些假设、各自想检验什么
2. ./scripts/study.sh table ${f.id} ${TAG} --all        —— 这一轮的全表(kind = hypo 的是上一轮提的假设;screen = 已知族剔掉本因子标出的票;
   segment = 只在低 / 高流动性、次新里按本因子选,或本因子剔掉冻结盘口)+ 市场解剖
3. sed -n '/第四批/,$p' docs/new_operators.md           —— 上一轮各位主研要求、已经加进库的 23 个新算子(定义与理由)。三目选择用现成的 select_where(c, a, b)。

## 要做的

1. **对账**:上一轮综合里的每条推论 / 每组假设,结果是支持还是否定?(写变体 id 和数字;train 与 valid 都看。)
2. **定论**(只凭 train / valid):这条因子自己最好的 1~3 个版本是谁(best_own;不含已知族成分的);建在已知族上的最好用法是谁(best_on_known:筛子 / 叠加),
   它比 k_known 和 k_known_xfrozen 强不强;一句话结论(one_line)和完整判断(verdict:是提纯 / 升华 / 只是已知族 / 多头腿不可用 / 只能当筛子…)。
3. **第三批假设**:studies/${f.id}/hypo3.yaml(≤ 25 条;格式同前:h3_xxx: {expr: "…", why: "…"})。只写两类:
   (a) 上一轮想写但写不出、现在有了算子的(桶内去均值 cs_bucket_demean / cs_bucket_zscore、封在最高最低价 day_at_max_ratio / day_at_min_ratio、
       带保护的尾部比值 day_es_ratio_hi / lo、市场状态 cs_state_rank / cs_flip_by_state、上市天数 cross_age、稳健标准化 cross_madz / cs_robust_z、
       day_wstd、day_topw_mean、in_index、in_zscore_expand、cross_flat_ratio、cross_semistd_*、更多档位的 cs_first_* / cs_last_*…);
   (b) 这一轮的结果直接指向的下一步(比如某个假设意外地好,就把它周围的最小子结构再换一圈)。
   写完必须检查能否解析:./scripts/study.sh hypo3 ${f.id}(FAIL 的改到通过或删掉)。
4. **落盘**:在 notes/${f.id}/synthesis.md 末尾追加一节「## 第二轮(${TAG})对账与结论」(≤ 80 行);覆盖重写 notes/${f.id}/state.md(≤ 10 KB,8 节);
   ./scripts/study.sh note ${f.id} "[主研] 批量扫描 ${TAG} 对账与结论" <<'EOF'(五六行)EOF
5. lab_findings:对以后研究**可迁移**的结论(关于算子或结构模式,不是这条因子的业绩),每条带证据和失效条件。

所有文字用中文,英文术语保留。省着用轮次。`
}

const ROUND = (args && args.round) || 1
log(`批量综合(第 ${ROUND} 轮):${factors.length} 条因子,模型 ${MODEL},扫描 ${TAG}`)
const res = await parallel(factors.map(f => () =>
  agent(ROUND === 1 ? prompt(f) : prompt2(f), { label: `${ROUND === 1 ? 'synth' : 'verdict'}:${f.id}`, phase: 'Synthesis', schema: ROUND === 1 ? SCHEMA : VERDICT, model: MODEL })
    .then(r => { log(`${f.id}: ${r ? (r.what_it_is || r.one_line || '').slice(0, 100) + ' | 假设 ' + r.hypotheses_written + ' 条' : '没有返回'}`); return r })))
return res.map((r, i) => r || { factor_id: factors[i].id, failed: true })
