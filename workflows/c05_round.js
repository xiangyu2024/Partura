export const meta = {
  name: 'c05-round',
  description: 'C05 一轮 Partura(B 组,每个种子独立):结构解剖员(Opus 5)读定位输出 → 文献员(Sonnet 5)查 2023-08 之前的文献 → PI(Opus 5.5)写本轮任务与笔记 → 检查(Haiku 5.5)校验,不合格退回改一次',
  whenToUse: 'args = {round: k, seeds: [801, ...]}。research/coldstart_C05/PLAN.md §2.6',
  phases: [
    { title: 'Anatomy', detail: '结构解剖员:哪些子树是 alpha 的来源、哪些部件是烂的' },
    { title: 'Literature', detail: '文献员:类似结构在文献里怎么处理' },
    { title: 'Plan', detail: 'PI:本轮的 E / N / R、事先预测、研究笔记' },
    { title: 'Check', detail: '确定性校验与文献日期;不合格修订一次' },
  ],
}

const ROOT = '/Users/wxy/Desktop/Partura'
const K = args.round
const SEEDS = args.seeds
const M = { pi: 'claude-opus-5-5', anat: 'claude-opus-5', lib: 'claude-sonnet-5', check: 'claude-haiku-5-5' }
const D = `${ROOT}/research/coldstart_C05`
const PY = '/Users/wxy/.venvs/alphacube/bin/python'
const ENVSH = `cd ${ROOT} && export ALPHACUBE_ROOT=$HOME/Desktop/AlphaCube-steering PYTHONPATH=$HOME/Desktop/AlphaCube-steering/src:${ROOT}`
const STR = { type: 'string' }

function place(S, role) {
  const P = `${D}/partura/s${S}`
  return `
## 你在整件事里的位置(先读这一段)

事先约定的对照实验 C05(${D}/PLAN.md,先读 §1–§2)。**主 AlphaCube(M)**是一个不受任何 agent 影响、一直在跑的 GP,只按它自己的历史禁掉结构相同和高相关的因子;它每一批的产出是你的原材料。
你是 B 组的 Partura,**只负责随机数种子 ${S}**(另外 7 个种子各有一个独立的 Partura,彼此看不到)。分级团队:PI(Opus 5.5)、结构解剖员(Opus 5)、文献员(Sonnet 5)、检查(Haiku 5.5)。**你是这里的「${role}」**。
现在是第 ${K} 轮(共 3 轮):你能看到 M 的第 1..${K} 批,以及本种子前几轮任务的结果。

你的产出不是因子,是**任务**:每轮 2 个 GP 任务位(各 96 次付费评估、种群 32),每个是
- **E 深挖**:把一个好结构(核心)固定住,GP 只在它外面长,而且外面的处理要和以前见过的很不一样;奖励在控制变量里再加入这个核心的家族(快照里含它的 heads),所以只有核心之外的**新信息**才拿分;
- **N 新想法**:受这一批或文献启发的新 idea;
外加至多 16 个 **R 变体**(去掉或替换好因子里没用或有害的部件,直接评估;比原 head 好 0.1 以上且仍是同一个东西时替换它)。
对照组 A 把同样的算力花在更多普通搜索上;最终比的是因子库在样本外的表现。你不能禁止或改变 M 的任何东西。

环境(所有组相同):奖励 \`long_neutral\` —— 信号对流动性 / 波动 / 20 日反转 / 已知族 / 市值做截面中性化后的残差建十分位**纯多头**书,扣 15bp;
score = train(2018–2021)与 valid(2022-01 ~ 2023-08)净夏普中较差的,**≥ 0.5 为发现**;与已知族 \`cross_mean(day_std(Amt), 30)\` |ρ| ≥ 0.5 判不合格;
禁 \`ts_spearman\` 与全部 \`nt_*\`;可用 6 个日频字段叶子(LogFloatCap、LogTotalCap、LogFloatShares、LimitWidth、BoardCode、ListAge);
所有 GP 都拒绝与库里任一 head 秩相关 ≥ 0.7 或算子骨架相同的候选。

## 能读什么、不能读什么(硬规矩,事后按会话记录审计)

**可以读**:${P}/ 下的全部文件(各轮的 loc.md / loc.json、analysis.md、lit.md、missions.yaml、R_prev.json,以及 notebook.md);${D}/PLAN.md;
代码与算子源码(${ROOT}/partura/、${ROOT}/scripts/c05_*.py、$HOME/Desktop/AlphaCube-steering/src/alphacube/)。
**不得读**:${D}/partura/ 下其他种子的目录;${D}/ 下除 PLAN.md 与你自己种子目录以外的任何东西;research/coldstart_C01 ~ C04 的任何文件;guidance/ 下 C0 开头的文件;
${ROOT}/runs/、lab/、notes/、studies/、handoff/、batches/、docs/、episodes/;任何测试段(2023-08-08 之后)的数字。
不跑服务器、不改代码、不改 PLAN、不 git commit。只写本角色被要求写的文件。`
}

const ANAT_SCHEMA = {
  type: 'object',
  properties: {
    path: STR,
    cores: { type: 'array', items: { type: 'object', properties: { core: STR, why: STR }, required: ['core', 'why'] } },
    queries: { type: 'array', items: STR },
    summary: STR,
  },
  required: ['path', 'cores', 'queries', 'summary'],
}
const LIB_SCHEMA = { type: 'object', properties: { path: STR, n_sources: { type: 'number' }, n_verified: { type: 'number' }, summary: STR }, required: ['path', 'n_sources', 'n_verified', 'summary'] }
const PI_SCHEMA = {
  type: 'object',
  properties: {
    path: STR,
    slots: { type: 'array', items: { type: 'object', properties: { type: STR, core: STR, hypothesis: STR }, required: ['type', 'hypothesis'] } },
    n_R: { type: 'number' },
    predictions: STR,
    summary: STR,
  },
  required: ['path', 'slots', 'n_R', 'predictions', 'summary'],
}
const CHECK_SCHEMA = {
  type: 'object',
  properties: {
    exit_code: { type: 'number' },
    output: STR,
    lit_date_violations: { type: 'array', items: STR },
    lit_unverified: { type: 'array', items: STR },
  },
  required: ['exit_code', 'output', 'lit_date_violations', 'lit_unverified'],
}

function anatPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, '结构解剖员')}

## 你的任务(结构解剖员)

读 ${P}/r${K}/loc.md(细节在 loc.json),以及 ${P}/notebook.md 和之前各轮的文件(若有)。回答:
1. **alpha 的来源**:哪些子树(核心)是真来源?用定位工具的证据说话 —— 共性(含它的候选 score 高多少、p、多少个候选含它)、充分性(子树单独当因子的 score)、
   必要性(跳过一个算子掉多少)、敏感性(换同类字段 / 窗口减半加倍是否稳)。区分「真来源」和「只是代理」(例如只是流动性、规模、波动的另一种写法),看不懂的算子去读源码。
2. **烂部件**:哪些部件必要性 ≤ 0、或换掉反而更好 —— 适合做 R。
3. **之前的任务**(第 2、3 轮才有):E 在哪个核心上试了什么外围、有没有产出 heads;N 的结果;上一轮笔记里的预测对不对。
4. **本轮候选**:值得深挖的核心(≤ 3 个;每个写出它周围已经见过的外围写法)、R 目标、N 的灵感。
5. **文献题目**:≤ 4 个,每个对准一个核心或灵感,问「文献里对类似的结构 / 特征做过哪些处理」(归一化、按条件分组、交互、换周期、换股票池等),写成文献员能直接拿去搜的问题(中英文关键词都给)。

写到 ${P}/r${K}/analysis.md(中文,引用的表达式写原文)。`
}

function libPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, '文献员')}

## 你的任务(文献员)

读 ${P}/r${K}/analysis.md 末尾的文献题目(以及它们对准的核心)。对每个题目用 WebSearch / WebFetch 查文献(这两个工具若还没加载,先用 ToolSearch 加载 "select:WebSearch,WebFetch")。
只用 **2023-08-08 之前发表**的论文、工作论文或研究报告(arXiv / SSRN 以首版日期为准);拿不准日期的不用。

对每个题目写:文献里这类结构 / 特征是怎么被构造和处理的,摘成**能翻译成我们算子语言的处理方式**
(例如:按日均成交额归一化、按市值分组后再排序、与特质波动率交互、换成 20 日 / 60 日、只在小盘或高换手股票里看、做时间序列标准化……),每条处理注明出处。
每个出处写:标题、作者、年-月、来源(期刊 / SSRN / arXiv / 机构)、链接、\`verified: true/false\`(true = 你这次确实在搜索结果或页面上看到了它)。**不得编造**;搜不到就写搜不到。

写到 ${P}/r${K}/lit.md。`
}

function piPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, 'PI')}

## 你的任务(PI)

读 ${P}/r${K}/analysis.md、lit.md、loc.md,${P}/notebook.md 与之前各轮的 missions.yaml(若有),以及 PLAN §2.5 的任务规则。决定本轮的 2 个 GP 任务位(各为 E 或 N)和可选的 R(至多 16 个变体)。
写 ${P}/r${K}/missions.yaml,格式:

\`\`\`yaml
seed: ${S}
round: ${K}
slots:
  - type: E
    core: '<核心表达式:原样取自 loc.md 里某个 head 的子树,或共性表 / 核心卡里的子树>'
    hypothesis: '<为什么它是 alpha 的来源;这次要试的外围处理是什么,为什么和以前不一样>'
    literature: [{title: '...', authors: '...', year: 'YYYY-MM', url: '...', treatment: '<借用的处理>'}]
    seeds: ['<原样含核心的表达式>', ...]    # ≤ 16 个;初代其余个体由机械嫁接补满 32
  - type: N
    hypothesis: '<新 idea>'
    inspired_by: '<哪一批里的什么现象 / 哪篇文献>'
    literature: [...]
    seeds: ['...', ...]                      # 1–16 个;占初代至多一半,另一半是 GP 自己的随机树
R:                                           # 可选
  - head: '<loc.md heads 表里的表达式原文>'
    why: '<哪个部件是烂的,依据>'
    variants: ['...', ...]
\`\`\`

规则:每个核心整个实验至多 2 个 E 位;第 3 轮结束前至少用过 1 个 N 位;E 的种子必须**原样包含**核心;E 的外围要和快照里已经见过的写法很不一样
(GP 会拒绝外围算子集合与以前完全相同的候选);种子里不用 ts_spearman 与 nt_*;文献年份早于 2023-08-08(2023 年的写到月)。
种子用我们的算子语言写(参考 loc.md 里的表达式、${ROOT}/partura/ops_ext.py 与 AlphaCube 的算子源码);窗口、字段都可以换;不加换手约束。

然后在 ${P}/notebook.md 末尾追加「第 ${K} 轮」一节(没有就新建):你目前对本种子 alpha 来源的信念;本轮每个任务的**事先预测**(会不会产出 heads、大致是什么、为什么);上一轮的预测对不对。

写完自己跑:\`${ENVSH} && ${PY} scripts/c05_check.py ${S} ${K}\`,不合格就改到合格。`
}

function checkPrompt(S) {
  const P = `${D}/partura/s${S}`
  return `${place(S, '检查')}

## 你的任务(检查)

1. 跑:\`${ENVSH} && ${PY} scripts/c05_check.py ${S} ${K}\`,记下退出码和完整输出。
2. 读 ${P}/r${K}/missions.yaml 与 lit.md:missions.yaml 引用的每条文献,年份是否早于 2023-08-08(违反的列进 lit_date_violations);
   是否在 lit.md 里出现并标了 verified: true(没有的列进 lit_unverified)。
不改任何文件。`
}

const results = await parallel(SEEDS.map(S => async () => {
  const tag = `c05r${K}s${S}`
  const anat = await agent(anatPrompt(S), { label: `${tag}:anatomy`, phase: 'Anatomy', model: M.anat, schema: ANAT_SCHEMA })
  if (!anat) return { seed: S, failed: 'anatomy' }
  const lib = await agent(libPrompt(S), { label: `${tag}:literature`, phase: 'Literature', model: M.lib, schema: LIB_SCHEMA })
  const pi = await agent(piPrompt(S), { label: `${tag}:pi`, phase: 'Plan', model: M.pi, schema: PI_SCHEMA })
  if (!pi) return { seed: S, failed: 'pi', anat, lib }
  let chk = await agent(checkPrompt(S), { label: `${tag}:check`, phase: 'Check', model: M.check, schema: CHECK_SCHEMA })
  let fixed = false
  if (chk && (chk.exit_code !== 0 || chk.lit_date_violations.length)) {
    await agent(`${piPrompt(S)}

## 检查没有通过,改一次

检查的输出:
${chk.output}
文献日期问题:${JSON.stringify(chk.lit_date_violations)}
只改 missions.yaml(必要时 notebook.md)里出问题的地方,改完自己再跑一遍校验。`, { label: `${tag}:pi-fix`, phase: 'Plan', model: M.pi, schema: PI_SCHEMA })
    chk = await agent(checkPrompt(S), { label: `${tag}:recheck`, phase: 'Check', model: M.check, schema: CHECK_SCHEMA })
    fixed = true
  }
  const ok = !!chk && chk.exit_code === 0 && chk.lit_date_violations.length === 0
  log(`种子 ${S}:${ok ? '合格' : '不合格'}${fixed ? '(修订过一次)' : ''};任务位 ${pi.slots.map(s => s.type).join(' + ')},R ${pi.n_R}`)
  return { seed: S, admissible: ok, fixed, anat, lib, pi, check: chk }
}))
return { round: K, results }
