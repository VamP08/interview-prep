# Binary Search

## Core idea

Halve a MONOTONE search space each step. Two shapes: (1) search a sorted array for a value/boundary; (2) "binary search on the answer" - the condition check(x) flips from False to True exactly once over the candidate range; find the flip point.

## Recognition signals

- Sorted (or rotated-sorted) array -> direct binary search
- "Minimum X such that ..." / "maximum X such that ..." with a feasibility check -> search on answer (Koko Eating Bananas)
- O(log n) explicitly demanded
- Rotated array: one half is always properly sorted - decide which, then check if target lies in it
- Two sorted arrays + median/kth -> partition binary search (hard tier)

## Templates

```python
# exact match
l, r = 0, len(nums) - 1
while l <= r:
    m = (l + r) // 2
    if nums[m] == target:
        return m
    if nums[m] < target:
        l = m + 1
    else:
        r = m - 1
return -1

# lower bound / first True (the workhorse)
l, r = 0, n                    # r is exclusive; answer may be n (not found)
while l < r:
    m = (l + r) // 2
    if check(m):               # first index where condition holds
        r = m
    else:
        l = m + 1
return l

# binary search on answer (Koko: min speed to finish in h hours)
def hours(speed):
    return sum((p + speed - 1) // speed for p in piles)
l, r = 1, max(piles)
while l < r:
    m = (l + r) // 2
    if hours(m) <= h:
        r = m
    else:
        l = m + 1
return l

# rotated sorted array
l, r = 0, n - 1
while l <= r:
    m = (l + r) // 2
    if nums[m] == target:
        return m
    if nums[l] <= nums[m]:                       # left half sorted
        if nums[l] <= target < nums[m]:
            r = m - 1
        else:
            l = m + 1
    else:                                        # right half sorted
        if nums[m] < target <= nums[r]:
            l = m + 1
        else:
            r = m - 1
```

## Complexity

O(log n); search-on-answer is O(n log(range)) with an O(n) check.

## Pitfalls

- Pick ONE template and stick to it. The l < r exclusive-r "first True" form handles 90% of boundary problems without off-by-ones.
- Infinite loop check: does every branch shrink the range?
- Search-on-answer: verify monotonicity before searching, and get the bounds right (l = 1 not 0 for speeds).
- In interviews say "invariant: answer always in [l, r)".
