# Strings

## Core idea

String manipulation and matching beyond what hashing/DP topics cover. OAs lean on direct string manipulation; product companies (Google, Meta) ask matching as a follow-up ("now do strStr better than O(nm)"). Know the naive, know one fast method (rolling hash or KMP idea), be able to say when each matters.

## Recognition signals

- "Find pattern in text" -> naive O(nm) first; follow-up wants Rabin-Karp (rolling hash) or KMP O(n+m)
- "Reverse words / compress / transform in place" -> parsing with pointers, service-company staple
- "Longest common prefix" -> vertical scan, stop at first mismatch
- "Rotation of another string?" -> s2 in s1 + s1, one line
- "At most one deletion to make palindrome" -> two pointers + one branch

## Templates

```python
# rolling hash (Rabin-Karp) - compare hashes, verify on match
BASE, MOD = 31, (1 << 61) - 1
h = 0
for c in pattern:
    h = (h * BASE + ord(c)) % MOD
cur = 0
top = pow(BASE, len(pattern) - 1, MOD)
for i, c in enumerate(text):
    cur = (cur * BASE + ord(c)) % MOD
    if i >= len(pattern):
        cur = (cur - ord(text[i - len(pattern)]) * top * BASE) % MOD
    if i >= len(pattern) - 1 and cur == h:
        start = i - len(pattern) + 1
        if text[start:i+1] == pattern:      # verify, hash can collide
            return start

# KMP failure function: lps[i] = longest proper prefix of p[:i+1] that is also suffix
lps = [0] * len(p)
k = 0
for i in range(1, len(p)):
    while k and p[i] != p[k]:
        k = lps[k - 1]
    if p[i] == p[k]:
        k += 1
    lps[i] = k
# search: walk text with same while-loop, match when k == len(p)

# reverse words in place-ish (Python: split handles runs of spaces)
" ".join(s.split()[::-1])

# valid palindrome with at most one deletion
def check(l, r, deleted):
    while l < r:
        if s[l] != s[r]:
            if deleted:
                return False
            return check(l + 1, r, True) or check(l, r - 1, True)
        l += 1
        r -= 1
    return True
```

## Complexity

Naive match O(nm). Rabin-Karp expected O(n + m). KMP worst-case O(n + m). In interviews the naive + "here is how I'd make it linear" conversation usually scores full marks.

## Pitfalls

- Rabin-Karp MUST verify on hash match - say "hashes can collide" unprompted.
- KMP: derive lps on a small example out loud; memorized-but-unexplainable KMP reads worse than clean naive.
- Python strings immutable: "in-place" problems get list(s), then join.
- strip/split cover 90% of parsing questions - do not hand-roll tokenizers.
