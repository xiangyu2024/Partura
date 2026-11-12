import yaml
M="mul(pow_3(ts_std(day_close(Amt), 50)), ts_min(signedpower(day_durbin_watson(cross_decay_linear(Amt, 30))), 1))"
e=[f"cross_ema({M}, 20)",f"ts_decay_linear({M}, 10)",f"cross_zscore({M}, 20)",f"ts_rank({M}, 40)",
f"cross_mean({M}, 30)",f"ts_max({M}, 10)",f"cs_demean(cs_rank({M}))",f"div({M}, cross_ema(day_std(Ret), 20))",
f"sub({M}, ts_mean({M}, 20))",f"ts_corr({M}, day_last(Close), 20)",f"cross_ema(cs_rank({M}), 15)",f"div({M}, ts_std(day_sum(Amt), 30))"]
CI="div(day_close(Amt), day_mean(Amt))"
n=[f"cross_ema(ts_std({CI}, 50), 20)",f"ts_std({CI}, 50)",f"ts_mean({CI}, 30)",
"div(ts_std(day_close(Amt), 50), ts_mean(day_close(Amt), 50))",f"ts_skew({CI}, 50)",
"ts_corr(day_close(Amt), day_sum(Amt), 40)",
"cross_ema(sub(div(day_close(Amt), day_sum(Amt)), div(day_open(Amt), day_sum(Amt))), 20)",
"ts_std(div(day_close(Amt), day_sum(Amt)), 50)",f"sub(ts_max({CI}, 20), ts_mean({CI}, 20))",
f"ts_corr({CI}, day_sum(Ret), 40)",
"cross_ema(div(day_sum(in_slice(Amt, 231, 240)), day_sum(Amt)), 20)",
"ts_std(div(day_sum(in_slice(Amt, 231, 240)), day_sum(Amt)), 50)"]
hE=("核心是原 head 里去掉 cross_max 的内层:(收盘一分钟成交额 50 日波动)的三次方 乘 (30 日线性衰减成交额的日内 Durbin-Watson 的 signedpower 取 1 日 ts_min)。"
"机制:收盘分钟成交额的波动衡量尾盘集中成交(指数基金 / 机构调仓、尾盘抢筹)的不稳定程度,即流动性冲击的重量;DW 刻画成交额曲线日内的自相关结构(DW 小=成交额呈连续趋势性堆积)。"
"拆解显示 cross_max 的窗口从 5 改为 10 把 score 从 -0.12 推到 +0.00(valid +0.05),去掉 ts_min 部分变化很小,说明有用的是第一因子与外层平滑;"
"上一轮的 E 没动这个核心。本轮外围与快照里 cross_max(·,k) 完全不同:不再取跨日最大值(只看极端),改为 cross_ema / ts_decay_linear / cross_mean 的慢平滑、"
"cross_zscore / ts_rank / 减自身 20 日均值的自身归一化、cs_rank 后平滑、以及除以收益波动或成交额波动去掉水平暴露。"
"与库里已有的不同:库里只有 cross_max 一种外层,取极值有很大噪声,而这里检验的是平滑后的尾盘成交波动水平;"
"样本外还会在,因为尾盘成交的波动性来自制度性的收盘定价与调仓行为,不依赖某段行情;对流动性 / 市值的线性与 U 形暴露已被尺子去掉。")
hN=("尾盘成交强度的不稳定性:CI = 收盘分钟成交额 / 全天分钟均成交额(无量纲),代表当天收盘定价阶段相对全天的参与程度;"
"它的 50 日波动 / 偏度 / 变异系数衡量一只票的尾盘参与者是否时有时无(调仓、被动资金流入流出、尾盘拉抬或砸盘),与 Ret 完全无关,和库里全部以 Ret 为输入的 skew / kurt / cov 家族不同;"
"同时用收盘份额减开盘份额、末 10 分钟成交额占比及其波动给出不同口径,用 ts_corr 观察尾盘强度与全天成交额 / 当日收益是否同向(尾盘强度的方向性)。"
"算子上全部是 day_close / day_open / in_slice 加 ts_* 或 cross_* 平滑,无前视。"
"样本外还会在,因为尾盘成交的集中度由收盘集合竞价规则与机构调仓日历这类制度性因素决定,持久;若与流动性控制过近,尺子的残差化会把水平部分去掉,留下波动部分。")
d={"seed":2075,"round":2,"slots":[
{"type":"E","core":M,"hypothesis":hE,"seeds":e},
{"type":"N","hypothesis":hN,"inspired_by":"批 2 中 cross_max(mul(pow_3(ts_std(day_close(Amt), 50)), ...), 5) 的拆解:day_close(Amt) 的 50 日波动单独留下 -0.52,窗口放宽后接近 0;共性表里 Amt 类字段的 day_close 出现频繁但不显著。这里把它去量纲并推广到开盘 / 末 10 分钟","seeds":n}],
"R":[{"head":"cross_mean(div(day_skew(Ret), day_kurt(Ret)), 20)","why":"拆解显示去掉除以 day_kurt 的分母后 score 从 -0.88 到 -1.47 更差,说明分母不是烂部件;窗口 40 把 valid 保持在 -0.78。烂的是纯 Ret 三四阶矩,换成量加权(day_wmean 与 day_mean 之差在共性表里 +1.9)版本",
"variants":["cross_mean(div(day_skew(Ret), day_kurt(Ret)), 60)","cross_ema(div(day_skew(Ret), day_kurt(Ret)), 40)","cross_mean(div(day_skew(Ret), day_std(Ret)), 40)","cross_mean(sub(day_wmean(Ret, Volume), day_mean(Ret)), 40)","cross_mean(div(day_skew(Ret), day_kurt(Ret)), 40)"]}]}
yaml.safe_dump(d,open("../r2/missions.yaml".replace("../r2/",""),"w") if False else open("missions.yaml","w"),allow_unicode=True,width=100000,sort_keys=False)
