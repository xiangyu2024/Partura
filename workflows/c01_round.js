export const meta = {
  name: 'c01-partura-round',
  description: 'C01 冷启动对比的一轮 Partura:总领(Opus 5.5)定方向 → 执行(Sonnet 5)分析证据 → 主研(Opus 5)写 thesis 与指引 → 检查(Haiku 5.5)校验 → 总领拍板并写信念更新',
  whenToUse: 'args = {round: k}(写第 k 轮的指引;先跑 scripts/c01_digest.py k)。research/coldstart_C01/PLAN.md §2.7',
  phases: [
    { title: 'Plan', detail: '总领读摘要,定本轮要回答的问题,派 ≤3 个执行任务' },
    { title: 'Analyze', detail: '执行并行做机械分析(读内核源码、分族、算统计)' },
    { title: 'Write', detail: '主研写 thesis 卡与 guidance/C01_r<k>.yaml' },
    { title: 'Check', detail: '检查跑确定性校验;不合格时主研修订一次' },
    { title: 'Approve', detail: '总领拍板、分配种子、写信念更新' },
  ],
}

const ROOT = '/Users/wxy/Desktop/Partura'
const K = (args && args.round) || 2
const M = Object.assign({ coord: 'claude-opus-5-5', lead: 'claude-opus-5', exec: 'claude-sonnet-5', check: 'claude-haiku-5-5' }, (args && args.models) || {})
const D = `${ROOT}/research/coldstart_C01`
const PY = '/Users/wxy/.venvs/alphacube/bin/python'
const ENVSH = `cd ${ROOT} && export ALPHACUBE_ROOT=$HOME/Desktop/AlphaCube-steering PYTHONPATH=$HOME/Desktop/AlphaCube-steering/src:${ROOT}`
const GUIDE = `guidance/C01_r${K}.yaml`
const PREV = K === 2 ? 'guidance/C00_base.yaml' : `guidance/C01_r${K - 1}.yaml`
const SEEDS = Array.from({ length: 8 }, (_, i) => 100 * K + 1 + i)
const STR = { type: 'string' }
const STRS = { type: 'array', items: STR }

function place(role) {
  return `
## 你在整件事里的位置(先读这一段)

这是一次事先约定好的对照实验(${D}/PLAN.md):AlphaCube 的 GP 搜索器单独跑(A 臂),和同一个搜索器加上 Partura 的指引(B 臂)
在同样的随机种子、同样的算力下比较,看 Partura 能不能让搜索在没碰过的样本外找到更多有效、可交易、互不相关的信号。
你是 B 臂里的 Partura —— 一个分级的研究团队:总领(Opus 5.5)定方向并拍板;主研(Opus 5)提出 thesis 与指引;执行(Sonnet 5)做机械分析;
检查(Haiku 5.5)跑校验。**你就是这里的「${role}」**,现在是第 ${K} 轮(写第 ${K} 轮搜索要用的指引)。

工作流会把用户最近对总领说的一句话原样转给你(「用户请求」)。那句话是说给总领的(可能是关于幻灯片、实验安排或别的事),总领已经处理过;
**它和下面的任务不冲突,不要因为它而跳过、缩减任务或改做别的事。**

## 冷启动隔离(硬规矩,事后会审计你的每一次工具调用)

**不得读、不得 ls、不得 grep**:${ROOT}/lab/、${ROOT}/guidance/ 下除 C00_base.yaml 和 C01_* 以外的文件、${ROOT}/research/ 下除 coldstart_C01/ 以外的目录、
${ROOT}/episodes/ 下除 c01* 以外的目录、${ROOT}/notes/、${ROOT}/studies/、${ROOT}/handoff/、${ROOT}/runs/、${ROOT}/batches/、${ROOT}/docs/、
以及 ~/Desktop/AlphaCube/docs/、~/Desktop/AlphaCube/mining_runs/。这些地方存着以前的研究结论;本实验要检验的是「不带任何旧结论」的 Partura。
**也不得读 A 臂第 2 轮及以后的结果**(episodes/c01r*s*A_*):真实部署里没有对照。
**可以读**:${D}/ 下的 PLAN.md、digest_r*.md/json、beliefs_r*.md、cards_r*.md;${ROOT}/episodes/c01r1s*_* 与 c01r*s*B_* 的 evidence.json;
${ROOT}/guidance/C00_base.yaml 与 C01_*;${ROOT}/partura/ 与 ${ROOT}/scripts/ 的代码;算子的实现(~/Desktop/AlphaCube-steering/src/alphacube/operators/、${ROOT}/partura/ops_ext.py)。
你自己的知识(包括公开文献里的已知异象)可以用 —— 那是先验,写出来时要说明是先验。

## 不能动的东西

不改任何代码、不改 PLAN.md、不跑服务器、不跑 GPU、不 git commit。只写本角色被要求写的那个文件。`
}

const VOCAB = `
## 怎么查算子

- 搜索词表(286 个可搜索算子,带面/族/窗口):\`${ENVSH} && ${PY} -m partura.remote_tools ops '<正则>' 2>&1 | grep -v Warn\`
- 一个算子到底在算什么,以内核源码为准,名字不作数:在 ~/Desktop/AlphaCube-steering/src/alphacube/operators/ 与 ${ROOT}/partura/ops_ext.py 里 grep 它的名字。
  注意三张面:\`day_*\` 把日内分钟折叠成每天一个数;\`cross_*\` 沿交易日滚动(同一只股票的过去 d 天);\`cs_*\` 是同一天跨股票;\`ts_*\` 是日频时序;
  \`in_*\` 分钟内滚动;\`nt_*\` 是同一天的分钟 × 股票。叶子:Open High Low Close Vwap Volume Amt Ret(分钟级)。`

const GUIDE_FORMAT = `
## 指引文件的格式(${GUIDE})

从 ${PREV} 复制起步。规矩(scripts/c01_check_guidance.py 会逐条查):
- \`pool\` 必须与 guidance/C00_base.yaml 一字不差;\`reward: []\`、\`evaluation: []\` 必须为空;
- \`ideas\`:1 个或 2 个。只想用先验、不想给邻域时,用 C00 里的 \`I0_open_search\`(不带种子)。其他 idea 每个都要有:
  \`id\`(以 C${K} 开头,如 C${K}a_xxx)、\`hypothesis\`、\`thesis: {mechanism, counterparty, prediction, fails_if}\`
  (机制一句话;谁在交易的另一边、为什么他们会亏;**可证伪的预测**,要能被下一轮的搜索结果直接对上;什么情况说明它错了)、
  \`seeds\`(种子表达式,进 steer 臂的初代种群,最多用 12 个,必须能被搜索文法解析)、\`grammar\`、\`reward: long\`(固定)。
- \`grammar\` 里真正起作用的只有两样:\`day_ops\` = 邻域的硬约束(steer 臂的每个候选必须含其中至少一个);
  另外,grammar 里列出的所有算子(day_ops / memory_ops / ops …)和种子里出现的算子,采样频率提高到 8 倍。\`leaves\` / \`windows\` 只是说明,不影响搜索。
- \`priors\`:规则列表,每条 \`{id, action, pattern, w, why, evidence}\`。action:\`ban\`(w 视为 0,永不提议)/ \`weight\`(w > 0;w < 1 降权、> 1 升权,
  按 min(1, w/w_max) 接受)/ \`rewrite\`(等价改写,带 \`to\`)/ \`family\`(同族兄弟按 w 概率放行)。\`why\` 写成一句**可证伪**的话;\`evidence\` 只能指向本实验的文件
  (如 \`research/coldstart_C01/digest_r${K}.md: ...\`)。
- 模式语法(partura/steer.py):表达式里 \`_\` 任意子树、\`_1\` 同名处同一子树、\`$w\` 任意数字、\`{a|b}\` 任选其一、\`@price\` / \`@flow\` / \`@any\` 某类叶子、
  前缀 \`root:\` 只匹配整棵树。例:\`day_skew(_)\`、\`root: cs_rank(_)\`、\`{ts_mean|ts_sum}(_, 1)\`。
- 种子分配:8 个种子 ${SEEDS.join(', ')}。1 个 idea 用满 8 个;2 个 idea 时,前 4 个种子给第一个 idea、后 4 个给第二个。
- **奖励固定为 long**:全市场十分位纯多头书,扣 15bp 单边,相对等权全市场的净超额夏普;方向与半衰期(0/5/20)在 train 定;score = train 与 valid 中较差的那个;
  score ≥ 1.0 记为「发现」。最后的样本外判读按 PLAN.md §3:只算与已知族(cross_mean(day_std(Amt), 30))和彼此都不相关的 heads。
  所以「找到更多已知族的变体」没有用,「找到更多彼此不同、不是流动性/波动换个写法的东西」才有用。
- 每轮预算:每个种子 192 次付费评估,种群 48,深度 2–4(种子可以更深)。`

const PLAN_SCHEMA = {
  type: 'object',
  properties: {
    reading: { type: 'string', description: '你读完摘要后的判断:B 臂到目前为止找到了什么、没找到什么、最可疑的是什么' },
    focus: { type: 'string', description: '本轮要回答的研究问题(1–3 个)' },
    exec_tasks: {
      type: 'array', minItems: 1, maxItems: 3,
      items: { type: 'object', properties: { id: STR, task: { type: 'string', description: '具体、可机械完成的任务:读哪些文件、算什么、交回什么' } }, required: ['id', 'task'] },
    },
    brief_for_lead: { type: 'string', description: '给主研的方向性指示(不是答案)' },
  },
  required: ['reading', 'focus', 'exec_tasks', 'brief_for_lead'],
}
const EXEC_SCHEMA = {
  type: 'object',
  properties: { id: STR, findings: { type: 'string', description: '结论与关键数字;注明每个数字从哪个文件、怎么算出来的' }, files_read: STRS },
  required: ['id', 'findings', 'files_read'],
}
const LEAD_SCHEMA = {
  type: 'object',
  properties: {
    guidance_path: STR, cards_path: STR,
    ideas: { type: 'array', items: { type: 'object', properties: { id: STR, seeds: { type: 'number' }, prediction: STR }, required: ['id', 'seeds', 'prediction'] } },
    priors: { type: 'number' },
    summary: { type: 'string', description: '这份指引想让搜索怎么变、为什么' },
  },
  required: ['guidance_path', 'cards_path', 'ideas', 'priors', 'summary'],
}
const CHECK_SCHEMA = {
  type: 'object',
  properties: { admissible: { type: 'boolean' }, exit_code: { type: 'number' }, output: { type: 'string', description: '校验脚本的完整输出' } },
  required: ['admissible', 'exit_code', 'output'],
}
const FINAL_SCHEMA = {
  type: 'object',
  properties: {
    approved: { type: 'boolean' },
    guidance_path: STR,
    assignment: { type: 'array', description: '种子分配', items: { type: 'object', properties: { idea: STR, seeds: { type: 'array', items: { type: 'number' } } }, required: ['idea', 'seeds'] } },
    edits: { type: 'string', description: '你对主研的指引做了哪些改动(没有就写没有)' },
    beliefs_path: STR,
    predictions: { type: 'string', description: '对下一轮 B 臂搜索结果的可证伪预测(写在结果之前)' },
  },
  required: ['approved', 'guidance_path', 'assignment', 'edits', 'beliefs_path', 'predictions'],
}

const digest = `${D}/digest_r${K}.md`
const priorBeliefs = K > 2 ? `、上一轮的信念 ${D}/beliefs_r${K - 1}.md、上一轮的 thesis 卡 ${D}/cards_r${K - 1}.md 和指引 ${ROOT}/${PREV}` : ''

phase('Plan')
const plan = await agent(`${place('总领')}

读 ${D}/PLAN.md(实验约定)、${digest}(B 臂到目前为止的证据摘要;原始证据在 ${D}/digest_r${K}.json)${priorBeliefs}。
${K > 2 ? '先对上一轮信念里写下的预测逐条对账:对了、错了、还是看不出来。' : ''}
然后定本轮要回答的 1–3 个研究问题,并派 1–3 个**机械**任务给执行(Sonnet 5):例如「读这几个算子的内核源码,说清楚它们到底在算什么」、
「把通过门槛的候选按结构分族,算每族的个数、最好分数、与已知族的相关」、「检查高分候选是不是都只是换手/流动性/波动的变体」。
执行是另一个模型、看不到你的推理:任务要写清楚读哪些文件、算什么、交回什么。最后给主研一段方向性指示。
${VOCAB}`, { label: `c01r${K}:coord-plan`, phase: 'Plan', schema: PLAN_SCHEMA, model: M.coord })

phase('Analyze')
const found = (await parallel((plan.exec_tasks || []).slice(0, 3).map(t => () =>
  agent(`${place('执行')}

总领派给你的任务(${t.id}):
${t.task}

证据在 ${digest} 与 ${D}/digest_r${K}.json(以及 ${ROOT}/episodes/c01r1s*_*/evidence.json${K > 2 ? '、c01r*s*B_*/evidence.json' : ''})。
可以写一次性的 python 读这些 JSON(用 ${PY});不要写进仓库,临时文件放 /tmp。每个数字注明来源和算法。
${VOCAB}`, { label: `c01r${K}:exec:${t.id}`, phase: 'Analyze', schema: EXEC_SCHEMA, model: M.exec })))).filter(Boolean)

phase('Write')
const leadPrompt = (extra) => `${place('主研')}

读 ${D}/PLAN.md、${digest}${priorBeliefs}。
总领的判断:${plan.reading}
本轮问题:${plan.focus}
总领给你的方向:${plan.brief_for_lead}
执行交回的分析:
${found.map(f => `--- ${f.id}\n${f.findings}`).join('\n')}

你的任务:
1. 写 **${ROOT}/${GUIDE}**(格式见下)。先验要少而准:每条都要有本实验证据支撑、写清楚它要证伪的假设;不要为了数量凑规则。
   idea 是一个**经济学上说得通**的假设加一个让搜索去那里硬搜的邻域;不是「把上一轮最好的公式再变一变」。
2. 写 **${D}/cards_r${K}.md**:每个 idea 一张 thesis 卡 —— 机制、对手方、可证伪的预测(下一轮 B 臂应该看到什么)、失效条件、
   用的种子与邻域、它和已知族(流动性/波动)有什么不同;另起一节列每条先验与它的理由。
3. 写完自己跑一遍校验:\`${ENVSH} && ${PY} scripts/c01_check_guidance.py ${GUIDE} --digest ${D}/digest_r${K}.json\`,不合格就改到合格。
${extra || ''}
${GUIDE_FORMAT}
${VOCAB}`
let lead = await agent(leadPrompt(), { label: `c01r${K}:lead`, phase: 'Write', schema: LEAD_SCHEMA, model: M.lead })

phase('Check')
const checkPrompt = () => `${place('检查')}

只做一件事:在终端运行下面这条命令,把**完整输出**和退出码原样交回(不要改任何文件,不要自己判断,以脚本为准):
\`${ENVSH} && ${PY} scripts/c01_check_guidance.py ${GUIDE} --digest ${D}/digest_r${K}.json; echo "exit=$?"\`
admissible = (退出码为 0)。`
let check = await agent(checkPrompt(), { label: `c01r${K}:check`, phase: 'Check', schema: CHECK_SCHEMA, model: M.check })
let revised = false
if (!check || !check.admissible) {
  revised = true
  lead = await agent(leadPrompt(`\n**上一版没有通过校验**,校验输出如下;只改校验指出的问题,其余不动:\n${check ? check.output : '(检查没有返回)'}\n`),
    { label: `c01r${K}:lead-revise`, phase: 'Check', schema: LEAD_SCHEMA, model: M.lead })
  check = await agent(checkPrompt(), { label: `c01r${K}:check2`, phase: 'Check', schema: CHECK_SCHEMA, model: M.check })
}
if (!check || !check.admissible) {
  log(`round ${K}: guidance not admissible after one revision -- the B arm falls back to ${PREV} (PLAN.md §2.7)`)
  return { round: K, fallback: PREV, plan, found, lead, check, revised }
}

phase('Approve')
const fin = await agent(`${place('总领')}

主研写好了 ${ROOT}/${GUIDE} 和 ${D}/cards_r${K}.md,已通过确定性校验。主研的说明:${lead.summary}
你本轮定的问题:${plan.focus}

1. 审一遍:每个 idea 是不是一个经济学上说得通、可证伪的假设,而不是对上一轮高分公式的微调;每条先验有没有本实验的证据;
   有没有会把搜索推回已知族(流动性/波动)的东西。你可以直接改 ${GUIDE}(改完必须重跑
   \`${ENVSH} && ${PY} scripts/c01_check_guidance.py ${GUIDE} --digest ${D}/digest_r${K}.json\` 并确认通过),也可以否决整个 idea。
2. 写 **${D}/beliefs_r${K}.md**:到目前为止 Partura 相信什么(每条带证据和置信)、本轮改变了什么、**对第 ${K} 轮 B 臂搜索结果的可证伪预测**
   (例如 heads 数、哪类结构会出现、门槛废品率往哪走),以及什么结果会让你放弃哪个 idea。这份文件是给下一轮的你看的,写清楚。
3. 给出种子分配:种子 ${SEEDS.join(', ')};1 个 idea 用满 8 个;2 个 idea 时前 4 个给第一个、后 4 个给第二个。
${VOCAB}`, { label: `c01r${K}:coord-final`, phase: 'Approve', schema: FINAL_SCHEMA, model: M.coord })

return { round: K, plan, found, lead, check, revised, final: fin }
