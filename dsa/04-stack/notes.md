# Stack

## Core idea

LIFO order matches nested structure (parentheses, expressions) and "most recent unresolved item" problems. The killer variant is the MONOTONIC stack: keep elements in increasing/decreasing order, pop when the invariant breaks - each pop resolves a "next greater/smaller element" question in O(1) amortized.

## Recognition signals

- Matching/nesting: parentheses, tags, undo -> plain stack
- Expression evaluation (RPN, calculator) -> operand stack
- "Next greater/smaller element", "days until warmer", spans -> monotonic stack
- "Largest rectangle", max area under constraint -> monotonic stack with widths
- O(1) getMin alongside push/pop -> auxiliary stack of running minimums

## Templates

```python
# matching (Valid Parentheses)
pairs = {")": "(", "]": "[", "}": "{"}
st = []
for c in s:
    if c in pairs:
        if not st or st.pop() != pairs[c]:
            return False
    else:
        st.append(c)
return not st

# monotonic decreasing stack (Daily Temperatures)
st = []                                  # indices; temps strictly decreasing
res = [0] * n
for i, t in enumerate(temps):
    while st and temps[st[-1]] < t:
        j = st.pop()
        res[j] = i - j
    st.append(i)

# largest rectangle in histogram
st = []                                  # (start_index, height), heights increasing
best = 0
for i, h in enumerate(heights + [0]):    # sentinel flushes the stack
    start = i
    while st and st[-1][1] > h:
        idx, ph = st.pop()
        best = max(best, ph * (i - idx))
        start = idx                      # extend new bar back
    st.append((start, h))
```

## Complexity

Each element pushed and popped at most once: O(n) total for any monotonic-stack sweep.

## Pitfalls

- Decide up front: stack stores indices or values? Indices when you need distances/widths.
- Strict vs non-strict comparison changes duplicate handling - check with equal elements.
- Sentinel value (append 0 / -inf) at the end saves a separate flush loop.
- Min Stack: push min AS PART of each entry (pair) - simplest correct design.
