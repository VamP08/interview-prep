# DSA Round

Pattern-first prep built on the [NeetCode 150](https://neetcode.io/practice/practice/neetcode150) (Blind 75 + 75 more, 18 categories, 28 easy / 101 medium / 21 hard).

## Why patterns, not topics

Interviewers expect you to recognize the applicable pattern within ~90 seconds, talk through the approach before coding, and state time/space complexity unprompted. ~20 recurring patterns cover the vast majority of asked questions. Each topic folder teaches the pattern (recognition signals + Python template), then lists its NeetCode problems.

## Study order (dependency roadmap)

Follow the numbering — it matches NeetCode's roadmap, each topic builds on earlier ones:

```
00 Fundamentals (Big-O, Python idioms)
01 Arrays & Hashing
├── 02 Two Pointers ──── 03 Sliding Window
├── 04 Stack
└── 05 Binary Search
06 Linked List
07 Trees ── 08 Heap/PQ ── 10 Tries
09 Backtracking
11 Graphs ── 12 Advanced Graphs
13 1-D DP ── 14 2-D DP
15 Greedy   16 Intervals   17 Math & Geometry   18 Bit Manipulation
19 Prefix Sum   20 Strings   (beyond NeetCode 150 - asked in MNC interviews and OAs)
```

## Per-topic layout

- `notes.md` — the pattern: core idea, recognition signals, Python template, complexity, pitfalls.
- `problems.md` — that topic's NeetCode 150 problems with LeetCode links.
- `solutions/` — my Python solutions, added as I solve.

## Cross-references

- [patterns.md](patterns.md) — pattern → recognition signal index (fast pre-interview review)
- [high-frequency.md](high-frequency.md) — most-asked questions at large companies
- [TRACKER.md](TRACKER.md) — all 150 problems, one table, single source of truth for progress

## Cadence

- 1–2 problems daily beats weekend cramming.
- Re-solve anything that took hints after 1 week, then 1 month (spaced repetition).
- Log every solve + mistakes in the tracker. DP and graphs need multiple passes — that's normal.
