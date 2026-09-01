# Big-O for Interviews

State complexity unprompted, for every solution: "Time O(n log n), space O(n)."

## Ladder (fast → slow)

| Complexity | Name | Typical source | n that fits ~1s |
|---|---|---|---|
| O(1) | constant | hash lookup, math | any |
| O(log n) | logarithmic | binary search, heap push/pop | any |
| O(n) | linear | single scan, two pointers, sliding window | 10^7–10^8 |
| O(n log n) | linearithmic | sorting, n heap ops | 10^6 |
| O(n²) | quadratic | nested loops, naive pair check | ~10^4 |
| O(n³) | cubic | triple loops, Floyd-Warshall | ~500 |
| O(2^n) | exponential | subsets, unpruned recursion | ~20 |
| O(n!) | factorial | permutations | ~10 |

Constraint in the problem tells you the target: n ≤ 10^5 means O(n log n) or better; n ≤ 20 screams bitmask/backtracking.

## Rules of thumb

- Drop constants and lower-order terms: O(2n + 10) = O(n).
- Different inputs get different variables: O(n + m), O(n·m).
- Recursion: branches^depth for time; depth for stack space.
- Amortized: appending to a Python list is O(1) amortized; so is each element entering/leaving a sliding-window deque once.

## Python operation costs

| Operation | Cost |
|---|---|
| `list[i]`, `list.append`, `list.pop()` | O(1) |
| `list.pop(0)`, `list.insert(0, x)` | O(n) — use `collections.deque` |
| `x in list` | O(n) |
| `x in set` / `x in dict` | O(1) average |
| `sorted(list)` / `list.sort()` | O(n log n) — Timsort |
| `heapq.heappush/heappop` | O(log n) |
| `heapq.heapify(list)` | O(n) |
| string concat in loop `s += c` | O(n²) total — build a list, `"".join` |
| slicing `list[a:b]` | O(b−a) copy — watch this in recursion |

## Space

Count auxiliary space, not input. Recursion counts its stack. "In-place" = O(1) extra.
