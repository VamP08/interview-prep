# Bit Manipulation

## Core idea

Integers as bit arrays. XOR cancels pairs, n & (n-1) clears the lowest set bit, shifts multiply/divide by 2. Small toolbox, instantly recognizable problems.

## Recognition signals

- "Every element appears twice except one" -> XOR everything
- "Count set bits" -> n & (n-1) loop, or DP on bits
- "Missing number in 0..n" -> XOR indices with values (or sum formula)
- "Add without + operator" -> XOR = sum without carry, AND << 1 = carry, loop
- "O(1) space, no extra memory" hints on counting problems

## Toolbox

```python
n & 1              # lowest bit / parity
n >> 1             # floor divide by 2
n & (n - 1)        # clear lowest set bit (Kernighan)
n & (-n)           # isolate lowest set bit
1 << k             # bit k
n ^ n == 0         # XOR self-cancels; a ^ b ^ a == b
x.bit_count()      # popcount (3.8+: bin(x).count("1"))
```

## Templates

```python
# counting bits 0..n with DP: dp[i] = dp[i >> 1] + (i & 1)
dp = [0] * (n + 1)
for i in range(1, n + 1):
    dp[i] = dp[i >> 1] + (i & 1)

# reverse 32 bits
res = 0
for _ in range(32):
    res = (res << 1) | (n & 1)
    n >>= 1

# sum without + (careful: Python ints are unbounded, mask to 32 bits)
MASK = 0xFFFFFFFF
while b:
    a, b = (a ^ b) & MASK, ((a & b) << 1) & MASK
return a if a <= 0x7FFFFFFF else ~(a ^ MASK)
```

## Complexity

O(1) per op; O(bits) loops. Kernighan's loop runs once per set bit.

## Pitfalls

- Python has no 32-bit overflow - simulate with masking when the problem assumes it (Sum of Two Integers, Reverse Integer overflow check).
- Negative numbers: Python's arbitrary-precision two's complement needs the mask-and-flip at the end.
- Operator precedence: == binds tighter than & - parenthesize (n & 1) == 1.
