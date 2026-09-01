# Arrays & Hashing

## Core idea

Trade space for time: a hash map/set turns "have I seen this?" and "how many?" from O(n) scans into O(1) lookups. Most O(n^2) brute forces over pairs/counts collapse to O(n) with one pass + a dict.

## Recognition signals

- "Find duplicates / unique / count occurrences" -> set or Counter
- "Pair/complement that sums to target" -> dict of value->index, one pass
- "Group things that are equivalent" -> dict keyed by a canonical form (sorted string, char-count tuple)
- "Longest streak/sequence", order irrelevant -> set + only count from sequence starts
- Prefix/suffix products or sums -> precompute one direction, combine with the other

## Templates

```python
# canonical-key grouping (Group Anagrams)
groups = defaultdict(list)
for s in strs:
    key = tuple(sorted(s))          # or 26-length count tuple for O(n*k)
    groups[key].append(s)

# prefix * suffix without division (Product of Array Except Self)
res = [1] * n
for i in range(1, n):
    res[i] = res[i-1] * nums[i-1]
suf = 1
for i in range(n - 1, -1, -1):
    res[i] *= suf
    suf *= nums[i]

# sequence starts only (Longest Consecutive Sequence, O(n))
s = set(nums)
best = 0
for x in s:
    if x - 1 not in s:              # x starts a run
        y = x
        while y + 1 in s:
            y += 1
        best = max(best, y - x + 1)
```

## Complexity

Hash ops O(1) average. Full pass O(n) time, O(n) space. Bucket/counting (Top K Frequent) gives O(n) where a heap gives O(n log k).

## Pitfalls

- Keys must be hashable: lists -> tuples.
- sorted(s) per string costs O(k log k); char-count tuple is O(k). Mention the tradeoff.
- Two Sum: insert AFTER checking, else an element matches itself.
- [[0]*n]*m aliases rows.
