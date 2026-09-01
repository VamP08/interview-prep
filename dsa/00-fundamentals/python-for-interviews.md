# Python for Interviews

The idioms that keep solutions short and correct.

## collections

```python
from collections import Counter, defaultdict, deque

Counter("aabb")            # {'a': 2, 'b': 2}; c1 == c2 for anagram checks
Counter(nums).most_common(k)
defaultdict(list)          # graph adjacency: g[u].append(v), no key check
d = deque([1, 2, 3])       # O(1) popleft/appendleft — BFS queue, sliding window
d.popleft(); d.append(4)
```

## heapq (min-heap only)

```python
import heapq
heapq.heapify(nums)              # O(n), in place
heapq.heappush(h, x); heapq.heappop(h)
# max-heap: negate values
heapq.heappush(h, -x); largest = -heapq.heappop(h)
# tie-breaking: push tuples (priority, item)
heapq.nlargest(k, nums)          # also nsmallest
```

## bisect (binary search on sorted list)

```python
import bisect
bisect.bisect_left(a, x)   # first index i with a[i] >= x  (insertion point)
bisect.bisect_right(a, x)  # first index i with a[i] > x
bisect.insort(a, x)        # insert keeping sorted — O(n) due to shift
```

## Sorting

```python
nums.sort(key=lambda p: (p[0], -p[1]))   # multi-key, mixed direction
intervals.sort()                          # tuples/lists sort lexicographically
sorted(words, key=len)
```

## Gotchas

- Integer division: `//` floors toward −∞; `int(a/b)` truncates toward 0. Matters for negatives.
- `[[0]*n]*m` aliases rows — use `[[0]*n for _ in range(m)]`.
- Default recursion limit ~1000: `sys.setrecursionlimit(10**6)` for deep DFS, or go iterative.
- Mutable default args (`def f(x, seen=set())`) persist across calls — use `None` sentinel.
- Strings are immutable: build `parts = []`, return `"".join(parts)`.
- `nonlocal` to rebind an outer variable inside a nested DFS; reading doesn't need it.
- Infinity: `float("inf")`. Ints never overflow (mention it — it removes a whole class of edge cases).

## Micro-templates

```python
# enumerate + hash map (Two Sum shape)
seen = {}
for i, x in enumerate(nums):
    if target - x in seen: return [seen[target - x], i]
    seen[x] = i

# grid directions
for dr, dc in ((1,0), (-1,0), (0,1), (0,-1)):
    r, c = row + dr, col + dc
    if 0 <= r < rows and 0 <= c < cols: ...

# memoization
from functools import lru_cache
@lru_cache(None)
def dp(i, j): ...
```
