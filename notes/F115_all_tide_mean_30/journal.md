# F115_all_tide_mean_30 研究日志

只追加、不改写。[auto] 是工具自己记的(启动了什么、什么时候跑完);其余是研究员写的:
每看完一个结果,写下它说明了什么、哪条假设变了、下一步做什么。接手的人先读这里(`./scripts/study.sh brief F115_all_tide_mean_30`)。

### 2026-10-04 13:07 [执行] R0 建档完成:四份 notes(01/02/03/06)+ 结果卡写完,S0 复现用户公布值

做了什么:brief 确认此前无 notes/journal/state(从零建档);跑了 digest S0_baseline、overview_for.py、
decompose;读了表达式里全部 10 个算子(in_slice/in_local_mean/day_argmax/in_slice_to_end/day_argmin/
day_locate/in_slice_from_start/sub/div/cross_mean)及其调用的底层函数的内核源码,全部读取成功。

写了什么:01_expression.md(来历 + 逐层拆开 + 一句话)、02_operators.md(10 个算子的精确语义、轴、
窗口、齐次度、NaN/边界行为、是否布尔输出、是否跨日)、03_decomposition.md(量纲/取值范围表、
M=F-I>=0 的证明、M=0 退化情形 N=NaN 的推导、累计回看 20 天、恒等节点检查)、06_baseline.md
(两种口径下的 Lnet/Lshp/LS/long_share、分位剖面、全部控制变量中性化、条件 IC、逐年、衰减、
两套 rank 相关、cov/dist 门槛)。结果卡 results/R0.md 摘要四个文件要点 + 10 条异常。

主要异常(详见结果卡):day_locate 的 @op 装饰器 arity=1 与函数签名/注册表 arity=2 不一致;
in_slice_to_end/in_slice_from_start/day_locate 三个算子内置探针全部报错(索引型第二参数喂错形状),
只能靠读源码定性,没有实测数字;known_stdamt_mean30 这个 gate 没有出现在 digest 的两处输出里(无
报错,只是缺失);valid 段分位剖面不单调(Q10 < Q9);digest 原始面板 rank 相关与 overview_for.py
的 hl=2 平滑信号 rank 相关是两套不同口径,多数变量符号相反、绝对值接近(方向翻转),但 ctl_rev1
对不上简单翻号。S0 对用户公布值(ls[0]=2.29、long[0]≈0.08)复现吻合,没有发现求值失败或覆盖率问题
(cov=dist=1.00)。

下一步(留给主研):四个文件都是事实性建档,没有提假设、没有设计实验、没有下结论——下一步的假设表、
结构语法拆解(04_grammar.md)、实验设计都还没有人做。
