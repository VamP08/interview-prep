# Backtracking

## Core idea

DFS over a decision tree: choose -> recurse -> unchoose. Generates all subsets / permutations / combinations / placements, with pruning to cut dead branches early. The three canonical shapes differ only in what the next choices are.

## Recognition signals

- "All subsets / combinations / permutations / partitions" -> enumerate everything
- "Generate all valid X" (parentheses, boards) -> build + constraint pruning
- Grid word search, N-Queens -> place, mark, recurse, unmark
- n <= ~20 in constraints -> exponential enumeration is intended

## Templates

```python
# subsets: at each index, include or skip
def bt(i, path):
    if i == len(nums):
        res.append(path[:])
        return
    path.append(nums[i]); bt(i + 1, path); path.pop()   # include
    bt(i + 1, path)                                      # skip

# combinations summing to target (reuse allowed): start index prevents duplicates
def bt(start, path, remain):
    if remain == 0:
        res.append(path[:]); return
    if remain < 0:
        return
    for j in range(start, len(nums)):
        path.append(nums[j])
        bt(j, path, remain - nums[j])       # j (not j+1): may reuse; j+1 forbids reuse
        path.pop()

# permutations: used-set
def bt(path):
    if len(path) == len(nums):
        res.append(path[:]); return
    for x in nums:
        if x in used:
            continue
        used.add(x); path.append(x)
        bt(path)
        path.pop(); used.remove(x)

# duplicates in input (Subsets II / Combination Sum II): sort, skip same value at same depth
nums.sort()
for j in range(start, len(nums)):
    if j > start and nums[j] == nums[j-1]:
        continue

# grid DFS with unmark (Word Search)
def dfs(r, c, i):
    if i == len(word):
        return True
    if not (0 <= r < R and 0 <= c < C) or board[r][c] != word[i]:
        return False
    board[r][c] = "#"                        # mark
    found = any(dfs(r+dr, c+dc, i+1) for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)))
    board[r][c] = word[i]                    # unmark
    return found
```

## Complexity

Subsets O(2^n * n), permutations O(n! * n), N-Queens O(n!)-ish with pruning. Say the tree size out loud; pruning changes constants, not the worst case.

## Pitfalls

- Append a COPY (path[:]) at the leaf, not the shared list.
- Undo EVERY mutation on the way out - the unchoose line is where bugs live.
- start index for combinations, used-set for permutations; know why each prevents duplicates.
- Duplicate-skip needs the sort AND the j > start guard together.
