import yaml
Z="create_like(in_slice(Close, 1, 1), 1e-05)"
G="day_gini(High)"
e1=[f"cross_mean({G}, 20)",f"sub({G}, day_gini(Low))",f"cs_bucket_demean({G}, LogFloatCap)",
f"cs_bucket_zscore({G}, day_sum(Amt))",f"cross_zscore({G}, 20)",f"cross_stddev({G}, 20)",f"cs_robust_z({G})",
f"div({G}, add(day_gini(Volume), {Z}))",f"cross_semistd_pos({G}, 20)",f"sub({G}, cross_mean({G}, 40))",
f"cs_bucket_demean(cross_mean({G}, 10), ListAge)",f"cross_tail_mean_q75({G}, 20)",f"cs_last_high10({G}, day_gini(Volume))",
f"cross_ema({G}, 10)",f"mul({G}, LimitWidth)",f"cs_bucket_zscore(cross_mean({G}, 5), BoardCode)"]
C="day_corr(in_delta(Vwap, 5), Volume)"
e2=[f"cs_bucket_demean({C}, LogFloatCap)",f"cs_bucket_zscore({C}, LogFloatCap)",f"cross_semistd_neg({C}, 20)",
f"cross_tail_mean_q25({C}, 20)",f"cross_zscore({C}, 10)",f"sub({C}, cross_mean({C}, 60))",f"cross_stddev({C}, 20)",
f"sub({C}, day_corr(in_delta(Vwap, 5), in_shift(Volume, 5)))",f"cross_decay_linear({C}, 20)",f"cs_robust_z(cross_mean({C}, 5))",
f"cross_ema({C}, 10)",f"div({C}, add(cross_stddev({C}, 20), {Z}))",f"cs_bucket_demean(cross_mean({C}, 10), BoardCode)",
f"mul({C}, day_corr(Amt, Ret))",f"cs_first_low20(cross_mean({C}, 10), cross_valid_count({C}, 20))",f"cross_med({C}, 20)"]
P="cross_shift(day_last(Close), 1)"
up=f"div(div(sub(day_max(High), {P}), add({P}, {Z})), LimitWidth)"
dn=f"div(div(sub({P}, day_min(Low)), add({P}, {Z})), LimitWidth)"
cc=f"div(div(sub(day_last(Close), {P}), add({P}, {Z})), LimitWidth)"
n=[f"cross_mean({up}, 10)",f"cross_max({up}, 20)",f"cross_mean({dn}, 10)",f"cross_max({dn}, 20)",
f"cross_mean(sub({up}, {dn}), 20)",up,f"cross_mean({cc}, 20)",f"cross_stddev({cc}, 20)",
f"cross_sum(is_gt({up}, create_like(in_slice(Close, 1, 1), 0.9)), 20)",
f"cs_bucket_demean(cross_mean({up}, 10), LogFloatCap)",f"cs_bucket_demean(cross_mean({up}, 10), BoardCode)",
f"cross_mean(mul({up}, {dn}), 20)",f"cross_zscore({up}, 20)",f"cross_ema({cc}, 5)"]
def v(w,px="Vwap"): return f"cross_stddev(div(day_last(in_slice({px}, 1, {w})), day_first(in_slice(Open, 1, {w}))), 20)"
h30="cross_stddev(div(day_last(in_slice(Close, 1, 30)), day_first(in_slice(Open, 1, 30))), 20)"
R=[{"head":h30,"why":"Knockout of the close/open ratio raises score by only +0.32 but the Close->Vwap swap gains +0.11: the last-minute Close is a noisy single print (bid-ask bounce, closing auction) while Vwap of the same window averages it out; keep the 20-day cross-sectional stddev and open-to-window ratio, replace the noisy endpoint and try longer windows (the 40-day window was less bad on train).",
"variants":[v(30),f"cross_stddev(div(day_last(in_slice(Vwap, 1, 30)), day_first(in_slice(Open, 1, 30))), 40)",
f"cross_stddev(div(day_last(in_slice(Vwap, 1, 30)), day_first(in_slice(Vwap, 1, 30))), 20)",
f"cross_stddev(div(day_close(Vwap), day_first(Open)), 20)",f"cross_stddev(div(day_close(Vwap), day_first(Open)), 40)",
f"cross_stddev(div(day_last(in_slice(Vwap, 1, 60)), day_first(in_slice(Open, 1, 60))), 30)"]}]
plan={"seed":2041,"round":2,"slots":[
{"type":"E","core":G,"hypothesis":"Core day_gini(High): the within-day inequality of the High path (Gini of |High| across minutes). Enrichment table puts it first among structural cores (+1.31, p 0.001, 14 candidates) and the round-1 N run found cs_first_low20(day_gini(Open), ...) at -0.50, the closest to passing anything in this stream; High has not been given a different periphery. Mechanism: for a price level series the Gini is a scale-free measure of how unevenly price is spread over the day, i.e. a path-shape/range proxy that is not the level of volume (which the liquidity control kills). Previous periphery used only the lexicographic screen cs_first_low20 with a price level; this round wraps it differently: multi-day persistence/dispersion (cross_mean, cross_zscore, cross_stddev, semistd, tail mean, EMA), relative-to-own-history (minus 40-day mean), relative to the Low path (High minus Low Gini = asymmetry of upside vs downside excursions), normalised by Volume Gini (price-path inequality relative to trade-size inequality), and cross-sectional neutralisation inside deciles of Amt / float cap / listing age / board (cs_bucket_*), which removes the size and board mix the ruler only removes linearly-in-rank. Library has none of these wrappers on this core. Out of sample: intraday excursion asymmetry priced by lottery/attention demand is a persistent behavioural trait; bucket-neutral versions avoid the size regime shift. No look-ahead (same-day minutes, days earlier only); denominators guarded by 1e-5.",
"seeds":e1},
{"type":"E","core":C,"hypothesis":"Core day_corr(in_delta(Vwap, 5), Volume): correlation between the 5-minute VWAP change and same-minute volume, i.e. whether volume arrives with rising or falling price (informed/trend-chasing flow vs contrarian liquidity provision). Enrichment +1.32 (p 0.003, 9 candidates), and its 20-day skew is also enriched. Round-1 seeds tried cross_mean(core,20) only; the cores' peripheries so far are level-type. This round tests: lead-lag form (subtract the correlation with volume lagged 5 minutes: contemporaneous vs lagged flow, isolates price impact from persistence), persistence-adjusted forms (minus 60-day mean, divided by 20-day std = a stability-weighted reading), downside/upside asymmetry (semistd neg, 25% tail mean), robust z-score and decay-weighted average, and size/board-neutral versions via cs_bucket_demean on float cap or board code. Libraries only contain the raw core, its skew, and the core in the library's own sum/std wrappers; none of these normalisations/neutralisations. Why it persists: signed volume-price co-movement reflects the sign of order imbalance, which is slow-moving across days for the same stock (institutional execution programs lasting days), and the bucket-neutral versions remove the size confound. Same-day data only; no look-ahead.",
"seeds":e2},
]}
del plan["slots"][1]
plan["slots"].append({"type":"N","hypothesis":"New idea from the board-specific price limits (LimitWidth leaf, 10/20/30% boards; the library never uses it): measure how close each day's extreme comes to the stock's own limit, in units of the limit: (day high - previous close)/previous close/LimitWidth (upside proximity), the same for the day low (downside), and the close-to-close return in limit units. Mechanism: the A-share daily limit makes the extreme excursion a censored, bounded variable; stocks that routinely touch 70-100% of the limit are lottery/speculative names whose limit-chasing demand pulls the price above fair value, while repeated near-limit-down touches show forced selling; limit-normalised means over 10-20 days, counts of near-limit days (>90%), sup over 20 days (cross_max), and the up minus down asymmetry are board-comparable (a 20% board stock with a 10% move is not the same as a 10% board stock), which volatility controls (raw returns) do not do. The batch showed that raw price-bucket volume sums are pure liquidity, so the signal should be a scale-free, bounded, event-type statistic. Also bucket-demeaned by float cap and by BoardCode to test regime stability. It differs structurally from every batch member: it uses previous close via cross_shift, High/Low extremes, and LimitWidth, with no Volume or in_roll_labels. It should persist because retail attention/lottery demand for limit-touching stocks is a documented, stable A-share behaviour (limit-up chasing followed by reversal). No look-ahead: previous close is known before the day; denominator guarded.",
"inspired_by":"Batch 1-2 of stream 2041: heads are in_roll_labels(Close) tail-volume sums (liquidity, -1.5..-1.9) and cross_stddev(close/open over the window) (volatility of intraday return, -1.8..-1.9); both are unbounded return or volume levels. Enrichment of day_first(Open), day_close(Vwap) shows price-extreme/location features carry the least-bad information, so a bounded, board-normalised extreme-return statistic is the next step.",
"seeds":n})
plan["R"]=R
yaml.safe_dump(plan,open("../missions.yaml","w"),width=200,allow_unicode=True,sort_keys=False)
