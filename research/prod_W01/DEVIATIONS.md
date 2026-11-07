# PROD W01 的偏差记录(agent 越出读写范围、流程例外;总领逐条判)

| 时间(EST) | 种子 / 轮 / 角色 | 发生了什么(agent 自报) | 总领判断 |
|---|---|---|---|
| 11-07 13:35–14:12 | 906 r1 审计员 | 为核对定义读了 AlphaCube-steering 的 docs、scripts 片段,grep 了 tests 与 Partura-prod/scripts | 都是代码与文档,不含样本外读数;无影响 |
| 11-07 13:35–14:12 | 909 r1 审计员 | 读了 corr_1.request.json(只有表达式),列了 partura/ 下的目录名 | 无影响 |
| 11-07 15:20 前后 | 911 r2 审计员 | 一次全库 grep,预览到 `research/alpha_distillation/B01_reverse_guidance.md` 开头几行,碰到 scripts/idea_final.py、forward_read.py | 总领看了那几行:是 B01 的**训练段**成对夏普结论,没有测试段 / 前推段的数;两个位都按宽松规则通过,打分不受影响。记录,不重审 |
| 11-07 15:25 前后 | 905 r1 PI | 在草稿脚本里加载了 `guidance/C05_base.yaml` 来规范化种子(§5 不让读),自报没看内容、没用 | 这个文件 c06_check.py 自己也加载;是 C05 的基础指引,不含样本外读数;无影响 |
