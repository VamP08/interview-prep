# Sliding Window

## Core idea

Maintain a window [l, r] over a sequence plus O(1)-updatable state (sum, count, char freq). Grow r each step; shrink from l when the window breaks the invariant. Every element enters and leaves once -> O(n).

## Recognition signals

- "Longest/shortest SUBSTRING or SUBARRAY with property X" - contiguous is the keyword
- "At most / exactly k distinct", "k replacements", "sum >= target"
- Fixed window size k -> rolling state, slide by one
- "Max of every window" -> monotonic deque (hybrid with stack pattern)

## Templates

```python
# longest window without repeats
seen = set()
l = best = 0
for r, c in enumerate(s):
    while c in seen:
        seen.remove(s[l])
        l += 1
    seen.add(c)
    best = max(best, r - l + 1)

# longest with counts (Longest Repeating Character Replacement)
count = Counter()
l = best = maxf = 0
for r, c in enumerate(s):
    count[c] += 1
    maxf = max(maxf, count[c])          # never shrinks; window only grows or slides
    if (r - l + 1) - maxf > k:
        count[s[l]] -= 1
        l += 1
    best = max(best, r - l + 1)

# shortest window covering a requirement (Minimum Window Substring)
need = Counter(t)
missing = len(t)
l = start = 0
best = float("inf")
for r, c in enumerate(s):
    if need[c] > 0:
        missing -= 1
    need[c] -= 1
    while missing == 0:                 # valid -> shrink greedily
        if r - l + 1 < best:
            best, start = r - l + 1, l
        need[s[l]] += 1
        if need[s[l]] > 0:
            missing += 1
        l += 1
```

## Complexity

O(n) time - l and r each advance at most n times. Space O(k) window state.

## Pitfalls

- Longest-window: shrink lazily (if). Shortest-window: shrink greedily (while valid). Mixing these up is THE classic bug.
- Window length is r - l + 1.
- Breaks when windowing on sum with negative numbers - monotonicity gone; use prefix sums + hash map instead.
