# Greedy

## Core idea

Make the locally best choice and never revisit. Only valid when local optimum provably leads to global (exchange argument: any optimal solution can be rewritten to start with the greedy choice without getting worse). In interviews: state the greedy rule, give a one-line why, and mention what would break it (then DP is the fallback).

## Recognition signals

- "Max reach / can you get to the end" -> track furthest reachable (Jump Game)
- "Min number of steps/intervals/refuels" -> extend-window greedy (Jump Game II)
- Circular start point with net surplus -> if total >= 0 an answer exists; reset start when running sum < 0 (Gas Station)
- "Partition into groups, each as large as needed" -> track last-needed index (Partition Labels)
- Max subarray -> Kadane: drop the prefix when it goes negative

## Templates

```python
# Kadane (Maximum Subarray)
best = cur = nums[0]
for x in nums[1:]:
    cur = max(x, cur + x)        # extend or restart
    best = max(best, cur)

# jump game: furthest reach
reach = 0
for i, x in enumerate(nums):
    if i > reach:
        return False
    reach = max(reach, i + x)
return True

# jump game II: BFS-like layers, O(n)
jumps = end = far = 0
for i in range(len(nums) - 1):
    far = max(far, i + nums[i])
    if i == end:                 # current layer exhausted
        jumps += 1
        end = far

# gas station
if sum(gas) < sum(cost):
    return -1
tank = start = 0
for i in range(n):
    tank += gas[i] - cost[i]
    if tank < 0:
        start, tank = i + 1, 0   # no station in [old start..i] can work
return start

# partition labels
last = {c: i for i, c in enumerate(s)}
end = size = 0
for i, c in enumerate(s):
    size += 1
    end = max(end, last[c])
    if i == end:
        res.append(size)
        size = 0
```

## Complexity

Almost always O(n) or O(n log n) after a sort. The sort key IS the greedy insight in interval-flavored greedies.

## Pitfalls

- Say the exchange argument, even one sentence - unjustified greedy is the red flag interviewers probe.
- Gas Station reset: justify why skipping to i+1 is safe (any start between old start and i also fails).
- Valid Parenthesis String: track a RANGE [lo, hi] of possible open counts; clamp lo at 0.
- If a counterexample to the greedy exists, the problem is DP - test the rule on a tiny adversarial case before committing.
