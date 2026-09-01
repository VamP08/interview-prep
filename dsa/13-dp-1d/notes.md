# 1-D Dynamic Programming

## Core idea

Answer for position i built from answers of earlier positions. Recipe: (1) define state dp[i] IN WORDS, (2) write the recurrence, (3) base cases, (4) iteration order, (5) compress space if dp[i] uses only a few previous values. Start every problem with brute-force recursion + memo, convert to bottom-up after.

## Recognition signals

- "Number of ways to reach/decode/climb" -> counting DP
- "Max/min value taking or skipping items in a line" -> House Robber shape: dp[i] = max(dp[i-1], dp[i-2] + a[i])
- "Fewest coins / can it be formed" over an amount -> unbounded knapsack over amount axis
- "Break string into dict words" -> dp[i] = any(dp[j] and s[j:i] in dict)
- "Longest increasing subsequence" -> O(n^2) DP, or O(n log n) patience (tails + bisect)
- "Can we split into two equal halves" -> subset-sum over reachable sums (set works)

## Templates

```python
# climbing stairs / fibonacci with O(1) space
a, b = 1, 1
for _ in range(n - 1):
    a, b = b, a + b

# house robber
rob, skip = 0, 0
for x in nums:
    rob, skip = skip + x, max(rob, skip)
answer = max(rob, skip)
# House Robber II (circle): max(rob(nums[1:]), rob(nums[:-1]))

# coin change (min coins for amount)
dp = [0] + [float("inf")] * amount
for a in range(1, amount + 1):
    for c in coins:
        if c <= a:
            dp[a] = min(dp[a], dp[a - c] + 1)

# LIS in O(n log n): tails[k] = smallest tail of an increasing subseq of length k+1
tails = []
for x in nums:
    i = bisect.bisect_left(tails, x)
    if i == len(tails):
        tails.append(x)
    else:
        tails[i] = x
# len(tails) = LIS length

# partition equal subset sum: reachable sums as a set
target, s = divmod(sum(nums), 2)
if s:
    return False
reach = {0}
for x in nums:
    reach |= {r + x for r in reach if r + x <= target}
return target in reach

# palindromic substrings: expand around 2n-1 centers (not DP but the expected answer)
def expand(l, r):
    while l >= 0 and r < n and s[l] == s[r]:
        count += 1
        l -= 1
        r += 1
```

## Complexity

Typical O(n) or O(n * choices) time. State the space compression: "dp[i] only needs i-1 and i-2, so O(1) space."

## Pitfalls

- Define the state in words FIRST and say it: "dp[i] = min coins to make amount i." Most wrong recurrences come from a fuzzy state.
- Decode Ways: zeros are the whole problem ("06" invalid, "10" forces a pair).
- Maximum Product Subarray: track BOTH running max and min (negatives flip them).
- Off-by-one between "dp over i items" and "dp at index i" - pick one and be consistent.
