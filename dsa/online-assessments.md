# Online Assessments (OAs)

Most MNC pipelines start with a timed OA before any human round. Different game than interviews: no clarifying questions, hidden test cases, partial scoring, time pressure across multiple problems.

## Platforms

| Platform | Used by | Format notes |
|---|---|---|
| HackerRank | Amazon, Goldman, many banks + service companies | Test-case scoring: each hidden case has points, partial credit real - submit brute force before optimizing |
| CodeSignal | Uber, Robinhood, many startups | GCA "Coding Score" is portable across companies; 4 problems / 70 min tiered easy to hard |
| Codility | Microsoft (some), European companies | Correctness + performance scored separately |
| HackerEarth / Mettl / AMCAT | Indian service companies | Aptitude sections + 1-3 coding problems |

## Common company formats (verify per drive, they shift)

- Amazon OA: 2 coding (LC medium-ish, often grid/graph/greedy dressed in logistics wording) + work-style survey. Solve both; code quality matters less than passing cases.
- TCS NQT: aptitude + verbal + 1-3 coding, easy to moderate; Prime tier hardest. Speed on basics wins.
- Infosys SP/DSE: 3 problems climbing difficulty (DSE moderate, SP hits LC-hard); heavy on arrays, string patterns, recursion, greedy allocation.
- Google: usually no OA for experienced roles; online snapshot for new grads.

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
