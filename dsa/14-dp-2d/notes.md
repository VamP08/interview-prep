# 2-D Dynamic Programming

## Core idea

State needs two indices: position in two sequences (LCS, Edit Distance), or (index, capacity/second dimension) knapsack shapes, or a grid position. Same recipe as 1-D; the recurrence usually compares "characters match" vs "skip one side or the other".

## Recognition signals

- TWO strings/sequences compared -> dp[i][j] over prefixes (LCS, Edit Distance, Distinct Subsequences, Interleaving)
- Grid paths with counts/costs -> dp[r][c] from top/left
- "Number of ways to pick coins/items to reach total" with order irrelevant -> 2-D knapsack, item axis outer (Coin Change II, Target Sum)
- "Longest path in matrix with constraint" -> DFS + memo on cells (DP on a DAG)
- Interval problems "burst/merge, last one standing" -> interval DP dp[l][r] (Burst Balloons)
- Pattern matching with * -> dp[i][j] with the star branch (Regular Expression Matching)

## Templates

```python
# LCS
dp = [[0] * (len(b) + 1) for _ in range(len(a) + 1)]
for i in range(1, len(a) + 1):
    for j in range(1, len(b) + 1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# edit distance: replace / delete / insert
for i in range(m + 1):
    for j in range(n + 1):
        if i == 0 or j == 0:
            dp[i][j] = i + j
        elif a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

# coin change II (combinations, not permutations): coins OUTER loop
dp = [1] + [0] * amount
for c in coins:
    for a in range(c, amount + 1):
        dp[a] += dp[a - c]

# longest increasing path in matrix: memoized DFS
@lru_cache(None)
def dfs(r, c):
    best = 1
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] > grid[r][c]:
            best = max(best, 1 + dfs(nr, nc))
    return best

# interval DP (Burst Balloons): last balloon k in (l, r)
# dp[l][r] = max over k of dp[l][k] + a[l]*a[k]*a[r] + dp[k][r], padded array
```

## Complexity

Two-sequence DPs O(m * n) time; row-compress to O(n) space when dp[i] uses only dp[i-1]. Interval DP O(n^3).

## Pitfalls

- Loop order IS semantics in knapsack: items outer = combinations (Coin Change II); amount outer = permutations. Know why.
- 0-row/0-column initialization carries the empty-prefix meaning - get it right first.
- dp[i][j] indexes PREFIXES (first i chars), so compare a[i-1], b[j-1]. Off-by-one heaven.
- Stock with Cooldown: it is a small state machine (hold / sold / rest) - draw the 3 states, then code.
