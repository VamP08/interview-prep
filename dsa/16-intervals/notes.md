# Intervals

## Core idea

Sort (usually by start; by END for max-non-overlapping), then sweep: merge when overlapping, count when not. Overlap test for [a, b] and [c, d]: a <= d and c <= b. "How many rooms/resources at once" -> sweep over start/end events or a min-heap of end times.

## Recognition signals

- "Merge / insert intervals" -> sort by start, extend current while overlapping
- "Min removals so none overlap" / "max non-overlapping" -> sort by END, greedy keep earliest-ending
- "Can attend all?" -> sort, any overlap = no
- "Min rooms / max concurrent" -> heap of end times, or +1/-1 event sweep
- "For each query, smallest covering interval" -> sort queries + intervals, heap keyed by size

## Templates

```python
# merge intervals
intervals.sort()
merged = [intervals[0]]
for s, e in intervals[1:]:
    if s <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], e)
    else:
        merged.append([s, e])

# max non-overlapping (=> min erasures), sort by END
intervals.sort(key=lambda iv: iv[1])
kept, prev_end = 0, float("-inf")
for s, e in intervals:
    if s >= prev_end:
        kept += 1
        prev_end = e
# erasures = len(intervals) - kept

# meeting rooms II: heap of end times
intervals.sort()
ends = []                                 # min-heap
for s, e in intervals:
    if ends and ends[0] <= s:
        heapq.heappop(ends)               # reuse a freed room
    heapq.heappush(ends, e)
rooms = len(ends)

# event sweep alternative
events = sorted([(s, 1) for s, e in intervals] + [(e, -1) for s, e in intervals])
# at equal time, -1 sorts before +1: end frees room before next start takes it
```

## Complexity

Sort dominates: O(n log n). Sweep O(n).

## Pitfalls

- Say which sort key and why - end-time sort is the whole insight for non-overlap problems.
- Boundary convention: does [1,2] overlap [2,3]? Meetings usually no (>= is free), merging usually yes (<= merges). Ask.
- Insert Interval without sorting: three phases - before, overlapping (merge), after.
- Event sweep tie order (ends before starts) silently changes room counts.
