export const meta = {
  name: 'partura-tiered-studies',
  description: 'Partura 分层研究:主研(Opus 5)定思路下工单,执行(Sonnet 5)写代码跑实验读结果;每一轮都落盘,可从磁盘状态续跑',
  whenToUse: 'args = {factors:[recorder.py --state 的输出], chunk:N, models:{think,work}, max_rounds:N}',
  phases: [
    { title: 'Study', detail: '建档 → 主研/执行轮转(假设→实验→读留出段一次→成文)→ 结论' },
    { title: 'Audit', detail: '数字与流程(执行级模型)/ 机制与过拟合(主研级模型)' },
    { title: 'Revise', detail: '按审查意见修订,不再读留出段' },
  ],
}

const ROOT = '/Users/wxy/Desktop/Partura'
const factors = (args && args.factors) || []
const CHUNK = (args && args.chunk) || 4
const THINK = (args && args.models && args.models.think) || 'claude-opus-5'
const WORK = (args && args.models && args.models.work) || 'claude-sonnet-5'
const MAX_ROUNDS = (args && args.max_rounds) || 10
const MAX_REVISE_ROUNDS = (args && args.max_revise_rounds) || 4

const NUM = { type: 'number' }
const STR = { type: 'string' }
const STRS = { type: 'array', items: STR }

const LEAD_SCHEMA = {
  type: 'object',
  properties: {
    status: { type: 'string', enum: ['order', 'done'] },
    order: STR,
    kind: { type: 'string', enum: ['dossier', 'experiment', 'final', 'writeup', 'fix', 'none'] },
    summary: STR,
    state_written: { type: 'boolean' },
  },
  required: ['status', 'order', 'kind', 'summary', 'state_written'],
}
const WORK_SCHEMA = {
  type: 'object',
  properties: {
    order: STR,
    completed: { type: 'boolean' },
    result_card: STR,
    tags: STRS,
    problems: STRS,
    summary: STR,
  },
  required: ['order', 'completed', 'result_card', 'summary'],
}
const STUDY_SCHEMA = {
  type: 'object',
  properties: {
    factor_id: STR,
    one_line: STR,
    mechanism: STR,
    family: STR,
    known_exposure_r2: NUM,
    final_run: STR,
    original_id: STR,
    recommended_id: STR,
    recommended_expr: STR,
    recommended_halflife_long: NUM,
    recommended_kind: { type: 'string', enum: ['distilled', 'elevated', 'halflife_only', 'known_family', 'original_kept', 'none_robust'] },
    finalist_ids: STRS,
    long_net_train_original: NUM, long_net_test_original: NUM,
    long_net_train_recommended: NUM, long_net_test_recommended: NUM,
    long_sharpe_test_original: NUM, long_sharpe_test_recommended: NUM,
    original_at_long_halflife_is_enough: { type: 'boolean' },
    adds_over_known_family: STR,
    verdict: STR,
    established: STRS,
    unresolved: STRS,
    lab_findings: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: STR, claim: STR, evidence: STR, operators: STRS,
          confidence: { type: 'string', enum: ['low', 'medium', 'high'] }, recheck: STR,
        },
        required: ['id', 'claim', 'evidence', 'operators', 'confidence', 'recheck'],
      },
    },
    holdout_reads: { type: 'integer' },
    server_runs: { type: 'integer' },
    variants_tested: { type: 'integer' },
    report_path: STR,
    tooling_problems: STRS,
  },
  required: ['factor_id', 'one_line', 'mechanism', 'family', 'final_run', 'original_id', 'recommended_id',
    'recommended_expr', 'recommended_halflife_long', 'recommended_kind', 'finalist_ids',
    'long_net_test_original', 'long_net_test_recommended', 'adds_over_known_family', 'verdict',
    'established', 'unresolved', 'lab_findings', 'holdout_reads', 'report_path', 'tooling_problems'],
}
const AUDIT_SCHEMA = {
  type: 'object',
  properties: {
    factor_id: STR,
    lens: STR,
    issues: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          severity: { type: 'string', enum: ['critical', 'major', 'minor'] },
          where: STR, what: STR, evidence: STR, fix: STR,
        },
        required: ['severity', 'where', 'what', 'evidence', 'fix'],
      },
    },
    checked: STRS,
    refutation_attempt: STR,
    overall: STR,
  },
  required: ['factor_id', 'lens', 'issues', 'checked', 'overall'],
}

// ------------------------------------------------------------------ shared text

const COMMON = `
工作目录是 ${ROOT}(每条 Bash 命令开头都要 cd 进去,cwd 不会保留)。
**省着用轮次和阅读量(用户的额度很紧)**:不要通读 docs/study_playbook.md —— 下面的「规矩摘要」就是它的要点;
只在需要查工具用法(§2)、配置与表达式语法(§3)、notes 文件清单(§5)时翻对应那一小节。一条命令里把要看的一起打出来,
长输出用 head / grep 截,读过的文件不要重读。不要使用 Agent / Workflow 工具去派生别的 agent。写给人看的文字用中文,英文术语保留。

## 规矩摘要
- 工具只有 ./scripts/study.sh:brief <fid> / list <fid> / check <fid> / run <fid> <tag> <stage…> / wait <fid> <tag>(Bash 的 timeout 设 600000;
  没完就再 wait)/ digest <fid> <tag> / exec <fid> <tag> <script.py> / final <fid> <tag> <stage> / report <fid> / src <算子…> / note <fid> "…"。
- 只动这条因子自己的文件:configs/<fid>.yaml、studies/<fid>/、notes/<fid>/。
- 口径:train 2018–2021(fit 段)、valid 20220101–20230807、utrain = 两者 = 用户训练段、holdout 20230808 起 = 用户测试段。
  方向与半衰期只在 fit 段定。钱的数字都扣 15bp。多头口径 = 半衰期按纯多头书选(摘要里的 hlL / Lnet / Lshp);多空口径 = hlS / LS。
  门槛:cov ≥ 0.95、dist ≥ 0.5。噪声:多头腿净超额 ±3 个点、夏普 ±0.3。
- 留出段整个研究只读一次(study.sh final);读之前候选、排序、判据写进 10_distilled.md;读之后不改候选、不换推荐。
- 一个阶段回答一个问题;一个阶段 ≤ 12 个变体(含 nt_* 的 ≤ 6);全研究服务器运行 ≤ 8 次(含 final)。
- 审查反复抓到的错:把平滑(半衰期)的功劳写成结构的;「升华版」其实是已知成交额族;候选与原式 rank 相关 < 0.8 就是换了一条因子;
  读完留出段改推荐;折叠型因子(abs、平方)要用同样折叠过的控制变量去量;空头腿被「买不进的票」抬高;用内生变量分桶;数字张冠李戴。

**这项研究是接力做的**:「主研」定思路、下工单;「执行」写代码、跑实验、读结果。两者是不同的模型,而且每一轮都是
一个全新的 agent —— 彼此之间**只靠文件**传递信息,你的对话和推理不会被任何人看到。
你知道的、想到的、决定的,**不写进文件就等于没有**。`

// The harness relays the user's latest message to every subagent as "the user request", ranked above this
// script's text.  That message is about the overall arrangement, so each prompt says where the agent sits in it.
function place(role) {
  return `
## 你在整件事里的位置(先读这一段)

用户的总任务:对一批 AlphaCube 因子逐条做 Partura 研究(分辨、提纯、升华);并要求研究全程落盘、随时能换模型接手。
分工是 —— 总领(Opus 5.5)搭框架与协调;主研(Opus 5)负责单条因子的研究思路;执行(Sonnet 5)负责写代码、跑实验、读结果。

工作流会把**用户最近对总领说的一句话**原样转给你(「用户请求」)。那句话是说给总领听的 —— 可能是催进度、问状态、
要求把东西记下来、或者安排分工 —— **总领已经处理过了,下面这份任务就是总领对它的落实**。所以它和下面的任务**不冲突**:
你把这份任务完整做完(并按要求把过程写进文件),就是在执行用户的请求。**不要因为那句话而跳过、缩减任务,或改做别的事。**
如果它提到「写 state.md」「记录下来」,落到你身上就是:主研照常在本轮结束前重写 state.md;执行照常写结果卡和日志 —— 仅此而已。
记录框架、状态板、模型分工都已经由总领搭好并在运行,不需要你去搭、去改、去切换任何东西
(scripts/、partura/、workflows/、handoff/、lab/、docs/ 一律不要动;别的因子的文件也不要动)。
**你就是这个分工里的「${role}」。**`
}

const CRITERION = `
## 选拔口径(用户定的,不要改)

用户做的是 A 股纯多头,空头腿做不了。**选拔只看多头腿扣费之后能拿到多少**:第一判据是多头腿净超额与纯多头夏普,
半衰期按纯多头书在 fit 段选(rank_by: long;摘要里的 hlL / Lnet / Lshp 就是这个口径)。
- **延长半衰期带来的多头腿净超额是真的、可以交易到的改进,不是需要控制掉的伪影。**
  「原式 + 多头最优半衰期」是所有结构候选要比过的第一条基准;改进全部来自更长的半衰期也可以推荐,
  但归因要写对(写「来自平滑」;想说结构更好,就在同一个半衰期下比 —— 摘要里有固定半衰期表)。
- 多空夏普是次要信息(用户最早那张表的口径),每个变体都同时算了(hlS / LS)。
- 第二条基准是已知家族:cross_mean(day_std(Amt), 30) 与 cross_max(day_std(Amt), 9)(测试段多头腿净超额 +13%~+15%、
  纯多头夏普 1.4~1.9)。候选滑进这个家族没问题,但要说清楚它是什么,以及「对只能做多的用户,这条因子相对已知家族
  有没有增量」(残差的多头腿、或与已知家族相加之后的多头腿)。
- 结论可以是否定的:「多头腿不可用」「它就是已知家族,没有增量」都是合格的结论,只要证据在。`

function files(f) {
  return `
## 这条因子的共享记忆(都在 ${ROOT} 下)—— 接力靠的就是它们

  notes/${f.id}/state.md         研究现状,主研每轮**覆盖重写**(8 节:现状 / 中间结果 / 过程与逻辑 / 假设表 / 候选 / 后面的思路 / 留出段 / 给接手者的提醒)
  notes/${f.id}/journal.md       研究日志,**只追加**:[auto] 工具自己记;[主研] 判断与决定;[执行] 结果卡摘要;[审查] 发现的问题
  notes/${f.id}/orders/R<n>.md   第 n 张工单(主研写,执行照做)
  notes/${f.id}/results/R<n>.md  第 n 张结果卡(执行写,主研读)
  notes/${f.id}/NN_*.md          进报告的手写段落(playbook §5)
  configs/${f.id}.yaml、studies/${f.id}/、runs/${f.id}/*.json、logs/${f.id}_*.log
  handoff/${f.id}/               后台记录器自动存的:交接页 STATE.md、每个 agent 的动作流水、结构化结果(只读,不要改)

看全貌(每一轮的第一条命令):cd ${ROOT} && ./scripts/study.sh brief ${f.id}
记日志:cd ${ROOT} && ./scripts/study.sh note ${f.id} "[主研|执行|审查] R<n>:<一句话>" <<'EOF' … EOF`
}

function head(f) {
  return `## 因子

- factor_id: ${f.id}
- 来源: ${f.lib}库 / ${f.name}
- 表达式:
${f.expr}
${f.note ? '- 特别注意: ' + f.note + '\n' : ''}`
}

// ------------------------------------------------------------------ worker: the dossier (before the first lead round)

function dossierPrompt(f) {
  return `你是 Partura 的**执行**(研究工程师)。任务:为因子 ${f.id} **建档** —— 把主研开始思考之前需要的事实全部读准、写下来。
你不提假设、不设计实验、不下结论;你的读者是主研(另一个模型),它只看你写的文件。
${place('执行')}
${COMMON}

${head(f)}
${files(f)}

配置骨架 configs/${f.id}.yaml 已生成,基线 S0_baseline 已在服务器上跑完。**先 brief**:如果下面的文件已经存在且内容完整
(之前有人做过一部分),核对后补缺,不要重写。

## 要做的事

1. 一条命令里看三样:
   ./scripts/study.sh digest ${f.id} S0_baseline                                    # 基线:两本书、半衰期扫描、分位剖面、中性化、条件 IC、逐年、衰减
   ~/.venvs/alphacube/bin/python scripts/overview_for.py ${f.id}                     # 它与本批其他因子、控制变量、已知家族的关系
   ./scripts/study.sh decompose ${f.id}                                             # 算子档案(探针实测)+ SSA 分解 + 实验室先验
2. 对表达式里出现的**每一个**算子:./scripts/study.sh src <算子名>,读内核源码(连同它调用的底层函数)。
   不许按名字猜:这个项目里 cross_* 滚的是交易日轴,nt_* 是逐分钟的截面/日轴,day_* 折叠日内分钟轴。
3. 写下面四个文件(事实,不是解读;公式写出来,数字带口径):
   - notes/${f.id}/01_expression.md:这条因子的来历、逐层拆开后它在算什么(一句话 + 公式)。
   - notes/${f.id}/02_operators.md:每个算子的**真实语义**:精确公式;沿哪条轴;窗口与回看;带不带尺度(齐次度);
     NaN / 边界 / 不足窗口时的行为;布尔或档位输出;**和名字不一样的地方单独标出来**;有没有用到当天之后的数据。
   - notes/${f.id}/03_decomposition.md:SSA 分解表之外需要说明的 —— 每个中间节点的量纲和取值范围、重复子树、
     沿路径累计的回看天数、哪些节点在数学上是恒等或近似恒等(比如窗口为 1 的滚动算子)。
   - notes/${f.id}/06_baseline.md:基线读数。原式在多头口径(hlL)和多空口径(hlS)下的 train/valid:多头腿净超额、
     纯多头夏普、多空夏普、换手;钱在多头腿还是空头腿(long_share);分位剖面是否单调(逐档列出);逐年;衰减;
     对全部控制变量的 R² 与残差表现;与控制变量、已知家族、本批其他因子的 rank 相关(最高的几个);cov / dist 门槛。
4. 写结果卡 notes/${f.id}/results/R0.md:一页的事实摘要(上面四个文件的要点 + 你注意到的任何异常:求值失败、
   覆盖率低、与公布值不一致、探针读数为空的算子)。**只写事实和异常,不写「所以它是…」。**
5. 记日志:./scripts/study.sh note ${f.id} "[执行] R0 建档完成:<一句话>" <<'EOF' … EOF

返回:order 填 'R0',result_card 填结果卡路径,completed 表示是否全部写完,problems 列出没做成的。`
}

// ------------------------------------------------------------------ lead (thinker)

const STATE_SPEC = `state.md 的 8 节(每轮**整个文件覆盖重写**;**控制在 150 行 / 10 KB 以内** —— 下一个人每轮都要读它:
 只放结论性的要点和指向 notes / 结果卡的指针,长表和推导放进对应的 07_* / 07x_* notes,过时的内容删掉):
 1. 一句话现状(做到哪一步、下一步是什么)
 2. 中间结果:已经量到的事实,每条带数字和出处(tag / 脚本 / 变体 / 哪一段 / 哪种口径)
 3. 研究过程与逻辑:做了什么、按什么顺序、为什么这么走;源码里和名字不一样的地方
 4. 假设表:编号 | 假设 | 状态(未验证 / 被支持 / 被否定 / 已改写)| 证据与出处 | 还差什么才能定
 5. 当前的候选(提纯 / 升华):表达式、train/valid 多头口径数字、为什么是它;已排除的候选与原因
 6. 后面的研究思路:按顺序,每步做什么、想回答什么、哪种结果意味着什么;明确决定**不**做的事和原因
 7. 留出段:未读 / 已读(读前的候选排序与判据写在 10_distilled.md 的哪一节)
 8. 给接手者的提醒:工具的坑、还没看结果的任务(tag)、写了一半的文件`

const ORDER_SPEC = `工单格式(notes/<fid>/orders/R<n>.md)—— 执行是另一个模型,只看得到这张纸,写到它不需要猜:
  # 工单 R<n>(kind: experiment | final | writeup | fix)
  ## 想回答的问题(对应哪条假设;看到哪种结果意味着什么)
  ## 要做的事(逐条。配置阶段:stage id、每个变体的 id + **完整表达式** + why;分析脚本:要量什么、怎么量、用哪些面板)
  ## 要带回来的数字(逐项:哪个变体、哪一段、哪种口径、哪个指标;需要的表:固定半衰期表 / 中性化 / 条件 IC / rank 相关 / 逐年)
  ## 约束(只用 train/valid;tag 名;变体数上限)
一张工单最多 2 次服务器运行、合计不超过 12 个变体(含 nt_* 的不超过 6 个)。`

function leadPrompt(f, mode, k, max) {
  const study = mode === 'study'
  return `你是 Partura 的**主研**,负责因子 ${f.id} 的${study ? '研究思路' : '修订'}:${study
    ? '理解表达式、提出并裁决假设、设计判别性实验、决定提纯与升华的候选、下结论(分辨 / 提纯 / 升华)'
    : '研究已完成并经过独立审查,你要逐条裁决审查意见、决定怎么改、需要补什么实验'}。
你**不写实现代码、不跑实验**:那是「执行」的事,它照你的工单去做,把结果写成结果卡交回来。
这一轮结束后,下一轮的主研是一个新的 agent,只看得到文件。
${place('主研')}
${COMMON}

${head(f)}${CRITERION}
${files(f)}

## 这一轮(第 ${k} 轮,最多 ${max} 轮${study ? ',含读留出段和成文' : ''})

1. **先看全貌**:./scripts/study.sh brief ${f.id}。然后读 notes/${f.id}/state.md、journal.md 最近的条目、
   最新的结果卡 notes/${f.id}/results/R<n>.md;需要核对原始数字时 ./scripts/study.sh digest ${f.id} <tag>。
   ${study ? `还没有 state.md、或假设表还没写(你是第一个主研)时:读执行建的档:01_expression.md、02_operators.md、
   03_decomposition.md、06_baseline.md、results/R0.md。
   对关键算子的语义有疑问,自己 ./scripts/study.sh src <算子> 核对 —— 语义读错,后面全错。
   之前的研究员(可能是别的模型)留下的 notes、脚本、运行结果都是有效的工作成果:读懂、核对、接着做。`
    : `读审查意见:handoff/${f.id}/results/audit*.json(critical / major 的每一条);读原研究的结论 handoff/${f.id}/results/study.json;
   读报告 research/alpha_distillation/${f.id}.md 里被点到的段落。之前的修订者可能已经做了一部分(看 state.md、journal、
   ./scripts/study.sh list ${f.id} 里的 rev* / audit* tag):已有的结果直接用,不要重做。`}
2. **如果最新的工单还没有对应的结果卡**(上一轮的执行被打断了):不要另开工单,直接返回
   {status:'order', order:'R<n>', kind:<那张工单的 kind>},让执行接着做。
3. **裁决**。${study ? `(你是第一个主研、还没有假设表时:先把你对这棵树的理解写成 04_grammar.md(结构语法:事件 → 记忆 → 门控 → 放大…)
   和 05_hypotheses.md(竞争性假设表:每条写「它预测什么」「哪个实验能杀死它」),**先写假设,再下第一张工单**。
   想要候选实验的草稿,可以在工单里让执行跑 ./scripts/study.sh propose ${f.id} 并把输出贴进结果卡 —— 那只是草稿。)
   最新的结果说明了什么?哪条假设被支持、被杀死、要改写?有没有意外?把解读落到 notes 里:
   05_hypotheses.md(每条假设的状态和证据)、07_<stage_id>.md 的「解读」、07x_<序号>_<name>.md(自写分析的解读)。
   每个结论都要能指到一个实验;分清「已确立 / 合理但未坐实 / 未决」。`
    : `对每条审查意见三选一:**改正**(改 notes 的数字/措辞;把证据不足的「已确立」降级为「合理但未坐实」或「未决」)、
   **补实验**(只用 train/valid)、**有理有据地反驳**。不要为了通过审查删掉不利的事实。把裁决逐条写进
   notes/${f.id}/07x_revision.md(意见 → 处理 → 依据)。`}
4. **决定下一步**:
${study ? `   (a) 再做实验 → 写工单(kind: experiment)。一个阶段回答一个问题;每个变体的 why 写它想证伪什么;不要套别的因子的实验清单。
       至少要认真回答过:它是不是已知暴露(成交额水平/规模/换手率/波动/动量/反转)的另一种写法;钱为什么主要在空头腿;
       分位剖面是不是单调;哪些节点多余;「原式 + 多头最优半衰期」够不够;相对已知家族有没有增量。
   (b) 读留出段 —— 只凭 train/valid 选定 ≤ 5 个最终候选(**必须含原式;必须含一条已知家族基准**,除非有证据说明无关)。
       **先**把候选排序(第一推荐是谁)和判据(留出段出现什么结果算被否定)写进 notes/${f.id}/10_distilled.md 的
       「读留出段之前」一节,**再**写工单(kind: final)。整个研究只许读一次:brief 里显示已读过,就绝不再下 final 工单。
   (c) 成文(留出段已读)—— 你写判断类的 notes:09_diagnosis.md(已确立 / 合理但未坐实 / 未决)、10_distilled.md 的
       「读完留出段之后」(每条判据过了还是被否定;推荐就是事前的第一推荐,被否定就写被否定)、11_risks.md、12_next.md、
       08_variants.md;然后写工单(kind: writeup)让执行补齐事实类段落、出报告、逐个核对数字。
   (d) 完成 —— 报告已出、执行核对过数字 → 返回 status:'done'。(成文工单执行完之后会直接进入「整理结论」,一般不会再回到你这里。)
   **额度很紧:不要为了「再确认一下」多开实验轮。** 现有证据已经足够选定候选(包括否定的结论)时,这一轮就进入 (b)。
   到第 ${Math.max(2, max - 3)} 轮还没读留出段,就必须进入 (b);留出段已读的,这一轮必须是 (c)。`
    : `   判断类的文字(结论、措辞降级、归因改写)**你自己直接改 notes**;需要执行做的只有:补实验、改事实类数字、重出报告并核对。
   (a) 需要执行动手 → 写工单(kind: experiment = 要补实验;fix = 只改数字 / 重出报告。新阶段 id 用 SR_ 开头,tag 用 rev<n>)。
       fix 工单执行完之后会直接进入「整理结论」,所以下 fix 工单之前把你这边的判断类修改全部做完。
       **绝对不许再读留出段**(不许下 final 工单);final.json 里每个候选在两种口径下的留出段数字都已存着,读它不算再读。
       推荐只能从读过留出段的候选里选;按修订后的证据别的候选更好,就写「X 更值得推荐,但它没有读过留出段」。
   (b) 全部意见处理完、报告已重出、数字已核对 → 返回 status:'done'。最后一轮必须是 (b)。`}
5. **落盘(每一轮都必须做,在返回之前)**:
   - 覆盖重写 notes/${f.id}/state.md。${STATE_SPEC}
   - ./scripts/study.sh note ${f.id} "[主研] 第 ${k} 轮:<一句话>" <<'EOF'
     这一轮看到了什么、判断是什么、决定做什么、为什么(以及决定不做什么)
     EOF

${ORDER_SPEC}

返回:status('order' 或 'done')、order(工单号,如 'R3';done 时填空串)、kind、summary(两三句:这一轮的判断和决定)、
state_written(state.md 是否已更新)。`
}

// ------------------------------------------------------------------ worker: one order

function workPrompt(f, mode) {
  return `你是 Partura 的**执行**(研究工程师),负责因子 ${f.id} 最新的一张工单:把主研设计的事情实现出来、跑完、把结果读准、写成结果卡。
你**不改研究思路**:不增删假设、不换候选、不下结论。工单里有做不了的地方(表达式解析不过、算子不存在、超过变体数上限),
做**最小的、保持原意的**修改并在结果卡里写明改了什么;完全做不了就写明卡在哪。你的读者是主研(另一个模型),它只看你写的文件。
${place('执行')}
${COMMON}

${head(f)}
${files(f)}

## 要做的事

1. ./scripts/study.sh brief ${f.id};找到**最新的、还没有结果卡**的工单 notes/${f.id}/orders/R<n>.md,读它。
   (所有工单都有结果卡了:什么都不用做,返回 completed:false、summary 写「没有待办工单」。)
2. ./scripts/study.sh list ${f.id}:工单要的 tag 是不是已经跑过(上一个执行可能做到一半被打断)。跑过且 exit 0 的不要重跑,直接读结果;
   exit 97 是被内存守卫让路中止的,要重跑。
3. 实现并运行:
   - 配置阶段:在 configs/${f.id}.yaml 里加阶段(stage id、变体 id、表达式、why 照抄工单),./scripts/study.sh check ${f.id},
     通过后 ./scripts/study.sh run ${f.id} <tag> <stage…>,然后 ./scripts/study.sh wait ${f.id} <tag>(Bash 的 timeout 设 600000;没完就再 wait。
     排队是正常的)。表达式语言的坑看 playbook §3。
   - 分析脚本:studies/${f.id}/<name>.py,用 partura.study_tools.Study(playbook §2「自己写分析」);脚本开头先对一个已知答案自检;
     ./scripts/study.sh exec ${f.id} <tag> <name>.py,再 wait。
   - **只用 train / valid**。除非工单的 kind 是 final,否则绝不调用 study.sh final。
4. 把结果读准。工单「要带回来的数字」逐项回答;每个数写清口径:哪个变体、train / valid / utrain / holdout、
   多头口径(hlL)还是多空口径(hlS)、毛还是净。主动报告异常:求值失败的变体、cov < 0.95 或 dist < 0.5、符号与预期相反、
   换手异常、你做过的任何改动。
5. 写结果卡 notes/${f.id}/results/R<n>.md:
     # 结果卡 R<n>
     ## 做了什么(tag、阶段、脚本;哪些没做成、改了什么)
     ## 工单要的数字(逐项对着工单回答,用表格)
     ## 没人要但值得注意的(异常与意外)
     ## 原始输出在哪(./scripts/study.sh digest ${f.id} <tag> / logs/…)
   只写事实,不写「所以它是…」—— 那是主研的事。
6. 记日志:./scripts/study.sh note ${f.id} "[执行] R<n>:<一句话>" <<'EOF' 最关键的几个数字 EOF

## 按工单的 kind

- **final**(读留出段,整个研究只许一次):先确认 runs/${f.id}/ledger.json 里没有 split 为 holdout 的记录、
  notes/${f.id}/10_distilled.md 里已有「读留出段之前」一节;两条有一条不满足就**不要跑**,在结果卡里写明。
  S_final 的候选照抄工单(不得增删),每个变体写 group: final, final: true, profile: true(playbook §3),
  check 通过后 ./scripts/study.sh final ${f.id} final S_final,再 wait。
  结果卡里放「与用户表同口径」那张表的全部行(多头口径与多空口径各一份)和逐年表。
- **writeup**:补齐事实类段落(01、02、03、06;每个 07_<stage_id>.md 的「问题 → 结果」部分,解读是主研写的,不要改);
  ./scripts/study.sh report ${f.id};把 research/alpha_distillation/${f.id}.md 从头读一遍,notes 里引用的每个数字都到表里核对。
  明显的数字笔误直接改并列进结果卡;结论句不要动,有疑问的列进结果卡让主研裁决。
- **fix**(修订阶段):按工单改 notes 里的数字 / 措辞、补实验(阶段 id 用 SR_ 开头)、重出报告并核对。绝不读留出段。
- **experiment**:如上。

返回:order(工单号)、completed、result_card(路径)、tags(跑过的 tag)、problems、summary。`
}

// ------------------------------------------------------------------ conclusion (thinker; label study:/revise: -> results/*.json)

function concludePrompt(f, mode) {
  return `你是 Partura 的**主研**。因子 ${f.id} 的${mode === 'study' ? '研究' : '修订'}已经做完(上一轮主研判定完成)。
你的任务:**只凭文件**把最终结论整理成结构化结果。不要做新的实验,不要读留出段,不要改推荐。
${place('主研')}
${COMMON}

${head(f)}${CRITERION}
${files(f)}

读:./scripts/study.sh brief ${f.id};notes/${f.id}/state.md、09_diagnosis.md、10_distilled.md、11_risks.md;
./scripts/study.sh digest ${f.id} final(「与用户表同口径」表:train = utrain = 用户训练段,test = holdout = 用户测试段)。
${mode === 'revise' ? `另读 notes/${f.id}/07x_revision.md(每条审查意见的处理)。` : ''}
读留出段那次运行的 tag 不一定叫 final(看 brief 里带「读留出段」的那一行;常见的是 final 或 S_final),digest 用实际的 tag。
你也是成文之后的最后一道核对:读最新的结果卡(执行通读报告时列出的不一致);结论句与 final 的表对不上的,**直接改 notes 里的那一句**
并记进 tooling_problems;改过 notes 就再跑一次 ./scripts/study.sh report ${f.id}。以 final 的表为准。

## 输出

- final_run:读留出段那次运行的 tag(一般是 'final');original_id / recommended_id / finalist_ids:final.json 里的变体 id
  (数字由工具直接从 final.json 读,所以 id 必须准确);recommended_expr:推荐式的完整表达式;recommended_halflife_long:它的多头口径半衰期。
- recommended_kind:distilled(更小、同样好)/ elevated(结构上更好)/ halflife_only(原式换成多头最优半衰期就够)/
  known_family(最好的就是已知家族成员,这条因子没有增量)/ original_kept / none_robust(多头腿不可用)。
- long_net_*:多头口径(半衰期 hlL)下的多头腿净超额,小数(0.128 = 12.8%);long_sharpe_test_*:纯多头夏普。
- adds_over_known_family:一句话 —— 对只能做多的用户,推荐者相对已知成交额水平家族有没有增量,证据是什么。
- known_exposure_r2:原式交易信号被全部控制变量张成的 R²。family:一句话说它属于哪个家族。
- established / unresolved:各 3~6 条,每条 established 指到一个实验。
- lab_findings:对以后研究**可迁移**的结论(关于算子或结构模式,不是这条因子的业绩),每条写清证据和失效条件。
- tooling_problems:工具或接力过程中遇到的问题${mode === 'revise' ? ';以及对每条审查意见的处理(「已改」/「已补实验」/「反驳:理由」)' : ''}。

最后记一条日志:./scripts/study.sh note ${f.id} "[主研] ${mode === 'study' ? '研究' : '修订'}完成:推荐 <id>" <<'EOF' 理由与未决 EOF`
}

// ------------------------------------------------------------------ audits

function auditFiles(f) {
  return `要读的材料(都在 ${ROOT} 下;先 ./scripts/study.sh brief ${f.id},它会把研究员的结构化结论存到下面第一个文件):
  handoff/${f.id}/results/study.json           研究员自己报告的结论(待核对、待推翻)
  research/alpha_distillation/${f.id}.md       最终报告
  notes/${f.id}/*.md                            手写段落(含 state.md 与 journal.md)
  configs/${f.id}.yaml                          实验计划
  runs/${f.id}/*.json、runs/${f.id}/ledger.json   每次运行的原始结果与数据段台账
  studies/${f.id}/                              自写的探针与分析脚本
看某次运行的摘要:./scripts/study.sh digest ${f.id} <tag>。
每确认一条问题就记一条日志(审查也可能被打断):./scripts/study.sh note ${f.id} "[审查] <一句话>" <<'EOF' 证据 EOF
不要改研究员的 notes 和配置里已有的阶段。`
}

function auditNumbersPrompt(f) {
  return `你是 Partura 的审查员,负责**数字与流程**这一路。因子 ${f.id} 的研究刚完成;你的任务是找出报告里**不成立**的东西,
不是帮它说话。拿不准的按「有问题」处理并写明证据。
${place('审查员(数字与流程,执行级)')}
${COMMON}
${CRITERION}
因此:**不要**因为「改进来自半衰期」就判候选不成立;要查的是归因有没有写对、候选有没有和「原式 + 多头最优半衰期」
以及已知家族基准在同口径下比过。主要结论里的多头腿数字应当是多头口径(hlL)下的。

${auditFiles(f)}

## 逐项检查(每一项都要实际去查,把查过的写进 checked)

1. **数字对不对**。从 notes 里挑至少 15 个支撑主要结论的数字(优先 09_diagnosis、10_distilled、各阶段结论),逐个到
   runs/${f.id}/*.json 或 digest 输出里核对。差一位小数以上、张冠李戴(utrain 当成 valid、毛超额当成净超额、多空口径的数
   当成多头口径的、别的变体的数写到这个变体上)都算问题。study.json 里的 id 与数字也要核对。
2. **留出段纪律**。ledger.json 里 holdout 读取必须只有 1 次;S_final 候选 ≤ 5、含原式、含已知家族基准(或写明为什么不含);
   final 的 JSON 是不是最后一次阶段运行(比较 runs/${f.id}/*.json 的修改时间;rev* / audit* 除外);10_distilled.md 里有没有
   在读留出段**之前**写下的候选排序与判据(对照 journal.md 里 [auto]「读留出段」那一行的时间);最终推荐是不是事前的第一推荐
   (读后改选 = critical,除非如实写成「事前推荐被否定」)。
3. **口径**。报告里任何 valid / holdout 的数字,方向和半衰期是不是 fit 段定的;有没有把「用户口径的训练列」当成样本外来叙述。
4. **基线复现**。S0 里原式多空口径的 utrain 数字是否与配置里 published 一致(方向、半衰期、多空夏普 ±0.01、多头腿毛超额 ±0.002)。
5. **门槛**。被推荐的候选在 train 上 cov ≥ 0.95、dist ≥ 0.5 吗?
6. **报告本身**。有没有「求值失败」的变体被当成证据;表格是否有该有数却为空的;notes 的阶段文件名与配置里的 stage id 是否对得上。
7. **越界**。cd ${ROOT} && git status --short partura scripts lab docs(同时有别的研究在进行,只看这几个目录)。

issues 里每条写清 severity(critical = 结论因此不成立或流程违规;major = 需要改写或补实验;minor = 笔误级)、
where、what、evidence(你查到的具体数字)、fix。没有问题就返回空数组,不要凑数。lens 填 'numbers'。`
}

function auditMechanismPrompt(f) {
  return `你是 Partura 的审查员,负责**机制与过拟合**这一路 —— 一个多疑的量化研究员。因子 ${f.id} 的研究刚完成;
你的任务是**尝试推翻**它的机制解释和它推荐的候选。默认立场:在证据把别的解释排除掉之前,结论不成立。
${place('审查员(机制与过拟合,主研级)')}
${COMMON}
${CRITERION}
因此:**不要**因为「改进来自半衰期」就判候选不成立 —— 那是用户认可的、可交易的改进。你要推翻的是:归因写错
(把平滑的功劳写成结构的)、候选没有和「原式 + 多头最优半衰期」及已知家族基准比过、说「相对已知家族有增量」
却没有残差或合成的证据、推荐者在样本外的多头腿并不比这两条基准好。

${auditFiles(f)}

## 要回答的问题(把查过的写进 checked)

1. **每条「已确立」的结论,背后是哪个实验?** 那个实验能把它和最强的竞争解释区分开吗?把研究**没有排除**的解释写出来。
2. **算子语义读对了吗?** 用 ./scripts/study.sh src <算子> 自己读关键算子的源码,核对 02_operators.md 的描述
   (时间方向:日内向前看允许,跨日向前看不允许;NaN 与边界;带不带尺度;布尔/档位输出)。
3. **「分辨」站得住吗?** 有没有对交易信号做的中性化 R² 与残差多头腿、有没有直接替换实验?折叠型因子(abs、平方)有没有用
   折叠过的控制变量去量?overview:~/.venvs/alphacube/bin/python scripts/overview_for.py ${f.id}
4. **推荐的候选是不是挑出来的噪声?** 全研究试了多少变体;推荐者相对「原式 + 多头最优半衰期」和已知家族基准,在 valid 与
   holdout 上的多头腿净超额、纯多头夏普各差多少(噪声:净超额 ±3 个点、夏普 ±0.3);train 与 valid 是否同向;邻域稳不稳。
5. **它还是同一个因子吗?** 推荐者与原式、与已知家族的 rank 相关各是多少;低于约 0.8 就是换了一条因子,报告是否这么写了。
6. **留出段**。结果支持还是不支持 notes 的说法?有没有把不利的结果轻描淡写?

你**可以**做一次反驳实验(不是必须):在 configs/${f.id}.yaml 末尾加一个阶段 SA_audit(≤ 6 个变体,只用 train/valid,
**绝不**读留出段、绝不用 study.sh final),check 之后 ./scripts/study.sh run ${f.id} audit1 SA_audit、wait 取结果;或者写
studies/${f.id}/audit_*.py 用 exec 跑(tag 用 audit1)。只在它能直接检验你最怀疑的那一点时才做,做了就写进 refutation_attempt。

issues 里每条写清 severity(critical = 机制结论或推荐因此不成立;major = 需要降级措辞或补实验;minor)、where、what、
evidence、fix。没有问题就返回空数组,不要凑数;也不要因为报告写得流畅就放过它。lens 填 'mechanism'。`
}

// ------------------------------------------------------------------ orchestration

async function withRetry(makePrompt, opts, tries) {
  for (let k = 0; k < tries; k++) {
    const r = await agent(makePrompt(), opts)
    if (r) return r
    log(`${opts.label}: 第 ${k + 1} 次没有返回结果,${k + 1 < tries ? '接着磁盘上已有的工作重试' : '放弃,留给下次从磁盘状态续跑'}`)
  }
  return null
}

// lead <-> worker rounds; everything they know is on disk, so an interruption anywhere resumes from the files
async function rounds(f, mode, max) {
  const phase = mode === 'study' ? 'Study' : 'Revise'
  const tag = mode === 'study' ? '' : 'revise-'
  for (let k = 1; k <= max; k++) {
    const lead = await withRetry(() => leadPrompt(f, mode, k, max),
      { label: `${tag}lead:${f.id}#${k}`, phase, schema: LEAD_SCHEMA, model: THINK }, 2)
    if (!lead) return false
    log(`${f.id} ${mode} 第 ${k} 轮(主研):${lead.status}${lead.status === 'order' ? ' ' + lead.order + ' [' + lead.kind + ']' : ''} — ${lead.summary}`)
    if (lead.status === 'done') return true
    const work = await withRetry(() => workPrompt(f, mode),
      { label: `${tag}work:${f.id}#${k}`, phase, schema: WORK_SCHEMA, model: WORK }, 2)
    if (!work) return false
    log(`${f.id} ${mode} 第 ${k} 轮(执行):${work.order} ${work.completed ? '完成' : '未完成'} — ${work.summary}`)
    // the write-up (study) / the fix (revise) is the last piece of work: conclude straight from the files
    if (work.completed && (lead.kind === 'writeup' || (mode === 'revise' && lead.kind === 'fix'))) return true
  }
  log(`${f.id}: ${mode} 用完了 ${max} 轮,按现有记录下结论`)
  return true
}

function serious(audits) {
  return audits.flatMap(a => (a.issues || []).filter(x => x.severity !== 'minor').map(x => ({ lens: a.lens, ...x })))
}

const out = []
for (let i = 0; i < factors.length; i += CHUNK) {
  const part = factors.slice(i, i + CHUNK)
  log(`第 ${Math.floor(i / CHUNK) + 1} 组: ${part.map(f => `${f.id}[${f.phase}]`).join(', ')}(主研 ${THINK},执行 ${WORK})`)
  const res = await pipeline(
    part,
    // 1. study: dossier (worker) -> lead/worker rounds -> conclusion (lead)
    async f => {
      if (f.phase !== 'study') return { from_disk: true }
      if (!f.dossier) {
        const d = await withRetry(() => dossierPrompt(f), { label: `work:${f.id}#0`, phase: 'Study', schema: WORK_SCHEMA, model: WORK }, 2)
        if (!d) return null
      }
      if (!(await rounds(f, 'study', MAX_ROUNDS))) return null
      return withRetry(() => concludePrompt(f, 'study'), { label: `study:${f.id}`, phase: 'Study', schema: STUDY_SCHEMA, model: THINK }, 2)
    },
    // 2. audit: numbers (worker-tier) + mechanism (lead-tier); audits already on disk are not redone
    async (study, f) => {
      if (!study) return null
      if (f.phase === 'revise' || f.phase === 'done') return { study, fresh: [], complete: true }
      const have = f.have_audits || []
      const todo = []
      // a negative verdict (nothing robust / it is the known family / keep the original) gets the numbers-and-process audit only
      const kind = study.from_disk ? (f.study_kind || '') : (study.recommended_kind || '')
      const positive = !['none_robust', 'known_family', 'original_kept'].includes(kind)
      if (!have.includes('audit-numbers') && !have.includes('audit')) {
        todo.push(() => withRetry(() => auditNumbersPrompt(f), { label: `audit-numbers:${f.id}`, phase: 'Audit', schema: AUDIT_SCHEMA, model: WORK }, 2))
      }
      if (positive && !have.includes('audit-mechanism') && !have.includes('audit')) {
        todo.push(() => withRetry(() => auditMechanismPrompt(f), { label: `audit-mechanism:${f.id}`, phase: 'Audit', schema: AUDIT_SCHEMA, model: THINK }, 2))
      }
      const got = await parallel(todo)
      return { study, fresh: got.filter(Boolean), complete: got.every(Boolean) }
    },
    // 3. revise: lead/worker rounds over the audit issues -> revised conclusion
    async (a, f) => {
      if (!a) return null
      if (f.phase === 'done') return { factor: f, final: null, was_revised: false, note: 'already done on disk' }
      if (!a.complete) return { factor: f, final: a.study.from_disk ? null : a.study, was_revised: false, note: '审查没有做完,留给下次续跑' }
      const n = (f.n_serious || 0) + serious(a.fresh).length
      const crit = (f.n_critical || 0) + a.fresh.flatMap(x => x.issues || []).filter(x => x.severity === 'critical').length
      if (!n || (!crit && n < 2)) return { factor: f, final: a.study.from_disk ? null : a.study, was_revised: false, audit_issues: n }
      if (!(await rounds(f, 'revise', MAX_REVISE_ROUNDS))) return { factor: f, final: null, was_revised: false, note: '修订被打断,留给下次续跑' }
      const revised = await withRetry(() => concludePrompt(f, 'revise'), { label: `revise:${f.id}`, phase: 'Revise', schema: STUDY_SCHEMA, model: THINK }, 2)
      return { factor: f, final: revised, was_revised: !!revised, audit_issues: n }
    },
  )
  res.forEach((r, k) => {
    if (!r) log(`${part[k].id}: 没有做完(留给下次从磁盘状态续跑)`)
    else log(`${part[k].id}: ${r.final ? r.final.recommended_kind + ' → ' + r.final.recommended_expr : (r.note || '见磁盘')}${r.was_revised ? '(已修订)' : ''}`)
  })
  out.push(...res.map((r, k) => r || { factor: part[k], final: null, was_revised: false, note: 'interrupted' }))
}
return out.map(r => ({
  factor_id: r.factor.id,
  recommended_kind: r.final ? r.final.recommended_kind : null,
  recommended_expr: r.final ? r.final.recommended_expr : null,
  one_line: r.final ? r.final.one_line : null,
  long_net_test_original: r.final ? r.final.long_net_test_original : null,
  long_net_test_recommended: r.final ? r.final.long_net_test_recommended : null,
  was_revised: r.was_revised,
  audit_issues: r.audit_issues || 0,
  note: r.note || '',
}))
