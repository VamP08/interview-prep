# Heap / Priority Queue

## Core idea

Repeatedly need the min (or max) of a changing collection -> heap: O(log n) push/pop, O(1) peek. Python heapq is a MIN-heap; negate for max. Two big sub-patterns: "top K" (heap of size k) and "two heaps" (max-heap of lower half + min-heap of upper half for running median).

## Recognition signals

- "K largest / K closest / K most frequent" -> min-heap of size k (pop when > k)
- "Kth largest in a STREAM" -> keep k-size min-heap; root is the answer
- "Running median" -> two heaps balanced within 1 element
- "Schedule/merge by earliest next" -> heap of frontiers (Merge K Lists, Task Scheduler)
- Repeated "take two largest, combine, reinsert" -> max-heap (Last Stone Weight)

## Templates

```python
# top-k with size-k min-heap: O(n log k)
h = []
for x in nums:
    heapq.heappush(h, x)
    if len(h) > k:
        heapq.heappop(h)
# h holds the k largest; h[0] is kth largest

# two heaps running median
small, large = [], []           # small: max-heap (negated), large: min-heap
def add(x):
    heapq.heappush(small, -x)
    heapq.heappush(large, -heapq.heappop(small))   # order the tops
    if len(large) > len(small):                     # rebalance: small may hold 1 extra
        heapq.heappush(small, -heapq.heappop(large))
def median():
    if len(small) > len(large):
        return -small[0]
    return (-small[0] + large[0]) / 2

# heap with tie-break tuples (K Closest Points)
h = [(x*x + y*y, x, y) for x, y in points]
heapq.heapify(h)                                     # O(n)
return [(x, y) for _, x, y in heapq.nsmallest(k, h)]
```

## Complexity

Push/pop O(log n), peek O(1), heapify O(n). Top-k pattern O(n log k). Also know quickselect gives average O(n) for kth largest - name it as the alternative.

## Pitfalls

- heapq has no max-heap: negate values, and negate again on read.
- Tuples compare element-wise - if payloads are not comparable, insert a counter as tiebreak: (priority, i, item).
- Do not mutate list then rely on heap property - heapify after bulk edits.
- "Kth largest" with k-size MIN-heap (not max) is the part people flip.

## Quickselect (the heap alternative)

Kth largest without a heap: average O(n), worst O(n^2), in place. Name it when asked "can you beat O(n log k)?"

```python
import random
def quickselect(nums, k):                # kth largest = index len-k ascending
    k = len(nums) - k
    l, r = 0, len(nums) - 1
    while True:
        pivot = nums[random.randint(l, r)]
        i, j, p = l, l, r
        while j <= p:                    # 3-way partition handles duplicates
            if nums[j] < pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1; j += 1
            elif nums[j] > pivot:
                nums[j], nums[p] = nums[p], nums[j]
                p -= 1
            else:
                j += 1
        if k < i: r = i - 1
        elif k > p: l = p + 1
        else: return nums[k]
```

Random pivot is what keeps it O(n) average - say it.
