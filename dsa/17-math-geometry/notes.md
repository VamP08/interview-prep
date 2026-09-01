# Math & Geometry

## Core idea

Grab bag of matrix manipulation and number tricks. Matrix rotation/traversal is boundary bookkeeping; the number problems are about spotting the invariant (cycle detection, digit loops, fast exponentiation).

## Recognition signals

- "Rotate matrix in place" -> transpose then reverse each row (90 deg clockwise)
- "Spiral order" -> four shrinking boundaries (top, bottom, left, right)
- "Zero out row/col in place" -> use first row/col as marker storage
- "Repeated digit process, does it loop?" -> cycle detection with a set (or fast/slow)
- "x^n efficiently" -> binary exponentiation, halve n each step
- "Count points forming squares" -> hash point counts, iterate diagonal candidates

## Templates

```python
# rotate image 90 deg clockwise, in place
for r in range(n):
    for c in range(r + 1, n):
        m[r][c], m[c][r] = m[c][r], m[r][c]    # transpose
for row in m:
    row.reverse()

# spiral matrix
top, bot, left, right = 0, R - 1, 0, C - 1
while top <= bot and left <= right:
    for c in range(left, right + 1): res.append(m[top][c])
    top += 1
    for r in range(top, bot + 1): res.append(m[r][right])
    right -= 1
    if top <= bot:
        for c in range(right, left - 1, -1): res.append(m[bot][c])
        bot -= 1
    if left <= right:
        for r in range(bot, top - 1, -1): res.append(m[r][left])
        left += 1

# fast pow: x^n in O(log n)
def mypow(x, n):
    if n < 0:
        x, n = 1 / x, -n
    res = 1
    while n:
        if n & 1:
            res *= x
        x *= x
        n >>= 1
    return res

# happy number: cycle detection
seen = set()
while n != 1 and n not in seen:
    seen.add(n)
    n = sum(int(d) ** 2 for d in str(n))
return n == 1
```

## Complexity

Matrix ops O(R * C). Fast pow O(log n). Multiply Strings O(mn) with digit array of size m + n.

## Pitfalls

- Spiral: re-check top <= bot and left <= right MID-loop before the bottom/left passes, or single rows/cols double-count.
- Rotate: transpose swaps only above the diagonal (c from r+1) or you swap twice = no-op.
- Set Matrix Zeroes O(1) space: first cell of row/col as flags, plus one separate flag for column 0.
- Plus One: carry may extend length ([9,9] -> [1,0,0]).
