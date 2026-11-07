# Data export (Strava, pulled 2026-11-07)

## runs.csv
Every activity with sport_type Run/TrailRun/VirtualRun from 2025-11-01 to 2026-11-07 (62 rows; earliest returned is 2026-05-17 — no runs exist before that in the query window).
Units: distance_m meters; *_time_s seconds; elevation_gain_m meters; *_speed_mps meters/second; temp °C; wind m/s; humidity %.
- avg_cadence_spm_half: Strava cadence as reported (steps per minute per foot, i.e. half of total steps/min).
- relative_effort: Strava's heart-rate-based score (unitless); blank = not reported.
- is_trainer 1 = indoor/no GPS. tags = Strava activity tags (only "Workout" present). Weather blank where Strava returned none.
- max_speed_mps is the fastest ~5s window and can be a GPS artifact.
- avg_speed values are rounded to 4 dp; recompute from distance/moving_time if needed.

## best_efforts.csv
Strava best efforts (all-time, Run only), top 3 per distance where available. time_s seconds. activity_id joins runs.csv id.

## other_activities.csv
Non-run activities (Volleyball, Ride, Workout, WeightTraining) — ONLY covers 2026-09-04 to 2026-11-07. Walks and very short watch-logged workouts omitted. Non-run activities before 2026-09-04 were not exported.
