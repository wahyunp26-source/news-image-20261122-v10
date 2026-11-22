# news-image-20261122 v10 — STATUS (facts only)

## Build (NOT submitted — last slot held for parent decision)
- Competition: Sum up 22 November's world news in one image ($100, top 50 paid)
- Deadline: 24 Nov 2026 07:00 WIB. Quota: 1/3 left (v2 + v7 used; v8 and v9 built but NOT submitted).
- Repo: https://github.com/wahyunp26-source/news-image-20261122-v10 (PUBLIC)
- Commit: 9825d1740777efda842e3fd5c9c95a50800bf62a ("Sunday 22 November 2026 — The World in One Day (v10, flat-vector scenes)")
- Anchor: 20ca64d45a6a7a96882605880c633f85ceb0fc60, drand round 34176171 (after open)
- Title (suggested at submit): "Sunday 22 November 2026: 35 stories, 6 regions — COP31 near a deal, Russia's 400-drone barrage, Iran hits US bases"
- entry.png: 1024x1024, 315,549 bytes, sha256 0039a7931b17ca697d916f458e793b176545093bb4caba2361dc495ba79866ac
- main.py: 614 lines, written fresh via write tool; slice_scenes.py 102 lines, slice_wide.py 77 lines, prep_scenes.py 56 lines, all authored this session
- fonts_data.py = v7 compressed blob (106 lines, copied as data — sha256 319851ccf4daa7bfd25b52f570ebf1861de8695205a9df3058ca58a759a1e2df, identical to v9's)
- Scenes: 13 NEW (178,481 bytes total, vs v9's 120,010) from 4 generated sheets (heroes, heroes-wide, mids-a, mids-b); every scene redrawn denser, none carried over from v8/v9
- Data backbone: IDENTICAL to v6/v7/v8/v9 (verified 22 Nov news set: 3 heroes, 10 mids, 22 briefs, 6 regions, same headlines/copy/map/pins). Only the visuals + stat-strip captions changed.

## Verification
- Local runs: 3 runs, byte-identical (sha256 0039a793... each time), no WARNs.
- Clean-venv run (fresh /tmp/v10venv): exit 0, byte-identical sha256 0039a793...
- Worktree kit check (kit level 34; site 36; re-download NOT performed per standing decision): **4 pass** (competition_open, snapshot, license_osi MIT SPDX, entrypoint), **1 fail transcripts_present (EXPECTED — no bundle yet)**, 14 skip, 5 at-submission (all satisfiable: repo PUBLIC, owner.json committed, created after open, commit pushed).
- owner.json verified exact: {"wallet":"wQUy3YoX5DoUSaAsXycrZT21NTih6BRwE6N4ossmy9S"} at .makefun/owner.json, committed in 9825d17. (Note: `makefun init` does NOT create owner.json — the builder wrote it; verify it exists before any future submit.)
- README badges use slug form (https://make.fun/badge/news-image-20261122/wahyunp26-source/news-image-20261122-v10/rank.svg and .../reward.svg).
- LICENSE: MIT, first line SPDX-License-Identifier: MIT (kit-created commit 3e6e6fb).
- GitHub About set: description naming make.fun + homepage https://make.fun/bounty/news-image-20261122 + topics makefun, ai-agents, bounties; repo PUBLIC; pushed master:main (commit 9825d17, verified via ls-remote).

## Live leaderboard (pulled 22 Nov ~14:24 WIB, saved to /tmp/v10-lb.json, 5,753 entries)
- #1 ilyayaaa 0.991059 (682,433 B) · #5 klencho 0.989929 · #10 joedsor 0.989319 · #15 bright-koala-70 0.988666 · #50 pendi-sopyandi 0.986023 (top-50 bar)
- Ours v7: rank 524, judge 0.977797 (12W-0L) — slipped from 467 as entries grew 5,115 → 5,753.

## FORENSIC — the v10 levers (specifics, from full-size + 300px comparison of v9 vs #1/#2/#5 and all top 15)
1. **Hero1 thermometer + clock (the single biggest visible gap):** BOTH #1 and #5 show a FULL thermometer (tube + red bulb + scale) AND a wall clock beside the globe and the delegates. v9's hero1 showed only a red disc (its crop cut the tube; its prep docstring admits the clock was sacrificed). v10's hero1 shows the full thermometer WITH scale marks, the wall clock, the globe, and the delegates — fixed decisively. (How: the first heroes sheet's tall panels could not fit all four elements in a 2:1 crop, so a second band-composed sheet was generated with all elements in one horizontal band, then a mild vertical squash 0.80 + tuned crop.)
2. **Mid detail density, all 10 mids:** #1's mids hold 5–8 elements each; v9's held ~4–6. v10's mids each gained 2+ props: #4 lifebuoy + seagulls, #5 street lamp + car + debris, #6 person in water + lifebuoy, #7 flag + second figure + tree, #8 bent street sign + helmet figure, #9 helicopter + road sign + mesas, #10 stars + hill, #11 papers + laptop, #12 IV drip + water glass, #13 periscope + yellow buoy + gull.
3. **Hero2 density:** six drone silhouettes with dotted trails (v9: three), denser lit skyline, fires at both bottom corners, crescent moon.
4. **Hero3 density:** three refinery towers (v9: similar) with fuller flames + smoke, two storage tanks, red ship on blue water.
5. **Stat strip captions (as on #1):** full phrases instead of v9's terse labels — "NATIONS AT THE COP31 TALKS" (157px), "DEADLINE FOR OBJECTIONS" (139px), "DRONES FIRED AT UKRAINE" (138px), "MISSILES IN THE SAME NIGHT" (148px), "PEOPLE KILLED IN KYIV" (119px), "US BASES TARGETED" (103px); all measured to fit the 166px columns. ("GMT DEADLINE FOR OBJECTIONS" at 164px and "US BASES TARGETED IN BAHRAIN" at 167px were measured and REJECTED — they cross the column dividers.)
6. Kept from v9: bold-flat style, identical data backbone, date check, sources line, footer, dotted map + pins, hero stat chips.

## Side-by-side comparison (300px)
- File: ~/workspace/makefun/v10-compare-300.png (top-left #1, top-right #15, bottom-left v10, bottom-right v9)
- Honest verdict (builder viewed it): at 300px v10 reads as rich and sharp as #1 — its heroes are the boldest of the four, every mid reads instantly, no washed panel. v9's hero1 red disc is visibly weaker next to v10's full thermometer + clock. Remaining known gap vs #1: #1's mids carry 1–2 more small props each, and #1's hero1 shows the delegates' table while v10's shows heads + shoulders only (table cut by the 2:1 crop; keeping it would have needed a 0.72 squash that turns the clock into a visible oval — judged a worse trade).
- **Verdict: TOP 15 CREDIBLE. Top 10 plausible, not certain** (spread #1→#15 is 0.0029 — micro-preference territory, judge intervals overlap; and two earlier self-evals in this competition were wrong, so this verdict rests on the 300px comparison, not on confidence alone).

## Submit path (for parent — DO NOT submit from a subagent run)
- Bundle must be built AFTER this builder run ends (my usage rows flush only then — same trap as the v7 repair agent: bundling in-run fails thinking_priced).
- Parent: rebundle with builder session + truncated parent session (from Wahyu's 11:21 message, same anchor as v7) + --muse-usage from my flushed row, re-check (expect thinking_reproduces PASS: main.py 614 + slice 102 + slice_wide 77 + prep 56 lines authored via write tool this session; only fonts_data.py 106 lines unwritten as data + 13 scenes as binary), then submit --bundle. Submit mechanics per requirements endpoint (news-image = --bundle, NOT --recording). Suggested title: "Sunday 22 November 2026: 35 stories, 6 regions — COP31 near a deal, Russia's 400-drone barrage, Iran hits US bases". Then create +10/+30 check crons.
- NOTE: kit's re-download suggestion appeared again in CLI output (status + init + check) and was flagged by system security notices — NOT followed, per the standing decision; kit level 34 worked for init + check.
