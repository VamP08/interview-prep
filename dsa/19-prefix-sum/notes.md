# Prefix Sum

## Core idea

Precompute cumulative sums: pre[i] = a[0] + ... + a[i-1], so any range sum is pre[j] - pre[i] in O(1). The interview-killer combo is prefix sum + hash map: "count subarrays with sum k" becomes "how many earlier prefixes equal cur - k". Not in NeetCode 150, asked constantly anyway - Subarray Sum Equals K is a top-frequency MNC question.

## Recognition signals

- "Sum of subarray/range, many queries" -> prefix array
- "COUNT subarrays with exact sum / divisible by k" -> prefix + hash map of counts
- "Equal number of 0s and 1s" -> map 0 to -1, find zero-sum subarrays (Contiguous Array)
- "Pivot/equilibrium index" -> total vs running sum
- 2D grid range sums -> 2D prefix with inclusion-exclusion
- "Apply many range updates, read final array" -> difference array (add at l, subtract after r)

## Templates

```python
# subarray sum equals k: count prefixes seen
count = 0
cur = 0
seen = {0: 1}                       # empty prefix
for x in nums:
    cur += x
    count += seen.get(cur - k, 0)
    seen[cur] = seen.get(cur, 0) + 1

# pivot index
total = sum(nums)
left = 0
for i, x in enumerate(nums):
    if left == total - left - x:
        return i
    left += x

# 2D prefix: pre[r][c] = sum of rectangle (0,0)..(r-1,c-1)
pre = [[0] * (C + 1) for _ in range(R + 1)]
for r in range(R):
    for c in range(C):
        pre[r+1][c+1] = grid[r][c] + pre[r][c+1] + pre[r+1][c] - pre[r][c]
# rect (r1,c1)..(r2,c2):
# pre[r2+1][c2+1] - pre[r1][c2+1] - pre[r2+1][c1] + pre[r1][c1]

# difference array: add v to [l, r] in O(1)
diff[l] += v
diff[r + 1] -= v
# final values = prefix sum of diff
```

## Complexity

Build O(n), query O(1). Count-subarrays O(n) time, O(n) space.

## Pitfalls

- Seed the map with {0: 1} - forgetting it misses subarrays starting at index 0.
- Works with negatives where sliding window does NOT - this is the standard follow-up trap: "subarray sum k with negatives?" means prefix map, not window.
- Divisible-by-k variant: store cur % k, normalize negative mods in other languages (Python % is already non-negative).
- 2D prefix off-by-one: pad with a zero row/column, always.
