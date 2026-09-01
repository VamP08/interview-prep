# Online Assessments (OAs)

Most MNC pipelines start with a timed OA before any human round. Different game than interviews: no clarifying questions, hidden test cases, partial scoring, time pressure across multiple problems.

## Platforms

| Platform | Used by | Format notes |
|---|---|---|
| HackerRank | Amazon, Oracle, Goldman, many banks | Test-case scoring: each hidden case has points, partial credit real - submit brute force before optimizing |
| CodeSignal | Uber, Robinhood, many startups | GCA "Coding Score" is portable across companies; 4 problems / 70 min tiered easy to hard |
| Codility | Microsoft (some), European companies | Correctness + performance scored separately |
| CoderPad | Meta (live rounds, not OA) | Execution often OFF - your code must be right without running it |
| Internal platforms | Google | Plain shared-doc coding on phone screens - practice without IDE |

## Common company formats (verify per drive, they shift)

- Google: OA for new grads/interns (2 easy-medium, both visible from start); usually no OA for experienced - straight to phone screen.
- Meta: typically no OA - recruiter screen then coding phone screen. The screen IS the filter: 2 problems in ~35 min.
- Oracle: HackerRank OA for new grad pipelines, easy-medium; then 4-5 interview rounds.
- Amazon (reference point): 2 coding + work-style survey on HackerRank.
- AI startups: often a take-home or live build round instead of classic OA; Sarvam allows LLM use in its build assessment - being fast WITH AI tools is part of the test.

## Tactics

1. Read ALL problems first 2 minutes; order by points/effort, not sequence.
2. Brute force first, SUBMIT (bank partial points), then optimize.
3. No interviewer: constraints are the spec. n up to 1e5 means O(n log n); 1e9 means math not loops.
4. Hidden edge cases to always cover: empty input, single element, all same, extremes of the given range, overflow-shaped values.
5. Practice in the actual platform editor beforehand - the environment tax is real (no local IDE, weak autocomplete).
6. Time per problem budget written down at start; abandon and return, never sink 40 min into problem 1 of 4.
7. Read input format carefully on HackerRank-style raw stdin questions - parsing bugs eat scores.

## Practice

- HackerRank Interview Preparation Kit
- CodeSignal practice + a mock GCA before a real scored attempt (score is reused across companies)
- LeetCode weekly contests for timed pressure
