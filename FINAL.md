# Half Marathon Prediction: Final Report

**Question:** What half marathon finish time does this training data support for a race in late November 2026?
**Data:** `data/` (Strava export pulled 2026-11-07: 62 runs from 2026-05-17 to 2026-11-06, best efforts, and non-run activities from 2026-09-04 to 2026-11-07).
**Process:** Four subagents ran in parallel (auditor, independent estimator, case for, case against). A fifth subagent then re-ran every numeric claim in reports 2–4. The verifier's corrections are applied below.

---

## 1. Answer

**Most likely: about 2:00 (1:59–2:01). Range: 1:56–2:05.**

- **1:56** is the result if the 25:12 5k converts at the standard Riegel 1.06 exponent and the race is paced evenly.
- **2:05** is the result if the late-race fade seen on 2026-05-31 happens again, or if the efficiency trend is the true signal.
- Below 1:55 or above 2:08 is not supported by verified evidence.

The point estimate comes from three independent methods, after the verifier's corrections. It is not an average of the for and against cases.

| Method | Result | Basis |
|---|---|---|
| 1. Riegel from the 11-06 5k (1512 s), exponent 1.08 | 1:59:18 | COMPUTED. The 1.08 exponent is a judgment for ~20 mi/week volume. The same 5k gives 1:55:55 at 1.06 and 2:02:47 at 1.10. |
| 2. May half (7270 s) scaled by fitness change | ~2:01:26 | COMPUTED. Average of two inputs: the 5k ratio, rebased by the verifier to the same-day May 5k (1536 s), gives 1:59:16; the efficiency regression with the flagged 06-09 record excluded gives 2:03:36. |
| 3. Recent long-run pace (361.9 s/km) minus a 30 s/km race offset | 1:56:42 | COMPUTED. The 30 s/km offset is generic and cannot be calibrated from this data. |
| Mean of methods 1–3 | ~1:59:10 | COMPUTED |

## 2. Agreement, disagreement, and which side the evidence favors

**All four reports agreed on:**
- The current 5k and mile are the best in the data, both from 2026-11-06.
- Endurance is the limiter, not speed: the longest run since May is 12 mi, and volume is about 20 mi/week over about 3 runs/week.
- The 05-31 run is the only effort of half-marathon length, and it slowed sharply late on.
- Neither the race date nor the course is in the data.

**Disagreement 1: optimistic 1:56 (Case For) vs conservative 2:08 (Case Against). Evidence favors neither extreme; it supports about 2:00.**
- The 1:56 rests entirely on Riegel 1.06. The Case For report concedes that 1.08 gives 1:59:18 and that a realistic centre is 1:58–2:00.
- The 2:08 rests on exponents of 1.12–1.15, which the verifier found UNSUPPORTED by this data. It also leans on best efforts from training runs, which the report itself calls ceilings.
- The Case Against report had two factual errors (see below). Its own "weakest point" paragraph gives about 1:59, which the verifier confirmed.

**Disagreement 2: whether the 2:01:10 May half is a reliable benchmark. Unresolved.**
- The run was not labeled a race, and it includes 215 s of stopped time.
- On moving time it works out to 1:58:43.
- Its 10k best effort is 373 s faster than any other 10k in the data, and there are no splits or GPS stream to check it.
- The late-race fade that reports 2–4 describe was derived by subtracting best-effort windows that need not be nested. The fade is plausible, but its size is not measured.

**Disagreement 3: whether there has been any run at goal pace. The verifier resolved this against both case reports.**
- Report 3 said nothing at goal pace had been run beyond 4 mi. Report 4 said there was no race-pace run longer than 5k. Both are WRONG.
- Counterexamples:
  - 09-26: 11.28 km at 5:28/km moving.
  - 06-06: 10.6 km at 5:12/km.
  - 06-16: 10.05 km at 5:22/km.
- The 09-26 run had 938 s stopped, about 20% of elapsed time, so it was probably intervals. Its moving pace overstates what can be sustained.

## 3. Claims and their labels

| Claim | Label | Source / method |
|---|---|---|
| 5k 1512 s and mile 454 s, both 2026-11-06 (id 20889980109), relative effort 124 | MEASURED | best_efforts.csv, runs.csv |
| 11-06 relative effort per minute of 3.66 is the highest in the file | COMPUTED | relative_effort / moving minutes |
| Half-marathon best effort 7270 s on 2026-05-31 (id 18732092567); 21.81 km; 7363 s moving, 7578 s elapsed | MEASURED | best_efforts.csv, runs.csv |
| May half on moving time is about 1:58:43 | COMPUTED | verifier |
| May 10k 3098 s (5:10/km); 15k 4740 s; 10 mi 5287 s | MEASURED | best_efforts.csv |
| Late fade after 15k (~6.1 km in 2530 s) | INFERRED | Subtraction of best-effort windows, not real splits; includes stopped time |
| Strava best efforts use elapsed time, not moving time | INFERRED | 10-13: 10-mile best effort 6066 s vs 6090 s elapsed and 5707 s moving |
| Weekly volume Sep 7–Nov 1: 19.0–23.1 mi; Sep 7–Oct 26 average 33.6 km | COMPUTED | Weekly sums of distance_m |
| Week of Nov 2: 13.5 mi | COMPUTED | Week incomplete at export; a taper is UNSUPPORTED |
| Longest run since May: 19.32 km (12.0 mi) on 10-22 at 9:39/mi, relative effort 251, 88% humidity | MEASURED | runs.csv |
| No run of 13.1 mi or more since 05-31 | MEASURED | runs.csv |
| Riegel predictions from the 25:12 5k: 1:55:55 (1.06), 1:59:18 (1.08), 2:02:47 (1.10) | COMPUTED | T2 = T1·(D2/D1)^k |
| VDOT 37.95, equivalent to a 1:55:59 half | COMPUTED | Daniels formulas |
| Efficiency at equal effort: Oct–Nov 2.0% slower than May–Jun (06-09 excluded) | COMPUTED | Regression of speed on relative effort per minute; May has no temperature data, so heat confounding is possible |
| Volleyball 2–3×/week, relative effort up to 109 (10-26) | MEASURED | other_activities.csv |
| "Berkeley Half Marathon Plan (Week 1/8)" note on 2026-09-25 | MEASURED | other_activities.csv id 20328041264 |
| Race date implied by the plan note: Nov 9–15 if 09-25 falls in week 1, later if week 1 started on 09-25 | INFERRED | Not in the data; see section 4 |
| Low-mileage runners need Riegel exponents of 1.12–1.15 | UNSUPPORTED | Nothing in the data calibrates it |

**Corrections from verification:**
- Report 4: max speed was not ≤4.66 m/s throughout September. The correct statement is ≤5.08 m/s from 09-12 onward.
- Report 3: the last stretch of the May run was 5.0 km at 10:38/mi (not 5.1 km at 10:26/mi). The gap between long-run pace and goal pace is 39–49 s/mi (not 40–60).
- Report 2: the 0–10k pace was 5:10/km (not 5:07). Volume was 33.6 km/week (not ~31). Method 2a should be rebased on the May 5k.

## 4. Data gaps that limit confidence

1. **Race date and course.**
   - The question says late November, and the data does not confirm it.
   - The plan note suggests the race could be as early as Nov 15, eight days from now.
   - There is no course elevation profile and no forecast.
2. **No splits, laps, or GPS streams.**
   - Without them, the size of the May fade and the 09-26 workout structure can't be checked, and neither can the outlier 05-31 best efforts.
3. **No heart-rate data.** Only Strava's relative effort score is available, which is a noisy proxy for intensity.
4. **No labeled races or workout intent.**
   - It is unknown whether the 11-06 5k or the 05-31 half were all-out.
   - The Runna plan's prescribed paces are missing.
5. **History is short.**
   - There are no runs before 2026-05-17.
   - Non-run activity before 2026-09-04 was not exported.
   - Nothing explains the 14-day gap from 06-26 to 07-11.
6. **Mixed time bases.**
   - Long-run paces use moving time and best efforts use elapsed time.
   - Every comparison between the two carries an error of a few percent.

## 5. New data that would move the answer

**Toward 1:56 or faster:**
- 8–10 km continuous at 5:30–5:40/km with no stops before the race, without high relative effort.
- An all-out 10k under about 54:30.
- Lap data showing the 05-31 slowdown was mostly stoppage rather than a fade.
- A flat course with cool race-day weather.

**Toward 2:03–2:05 or slower:**
- Lap data confirming a real fade after 15k on 05-31.
- A goal-pace tempo run that cannot be held past about 5 km.
- A hilly course, or race-day heat.
- Illness or missed runs between now and the race.
- Evidence that the 11-06 5k was a GPS-flattered or one-off effort, which the activity streams would show.

**Would narrow the range in either direction:**
- The race date and course.
- Heart-rate streams from the 11-06 run and the 10-22 long run.
- The 09-26 lap breakdown.
