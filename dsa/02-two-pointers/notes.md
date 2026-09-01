# Two Pointers

## Core idea

Two indices moving with purpose replace a nested loop. Works when moving a pointer provably discards candidates - usually because the array is sorted or the answer is monotone in pointer position.

## Recognition signals

- Sorted array + pair/triplet sum -> converging pointers from both ends
- Palindrome / compare from both ends -> converging
- Remove/partition in place -> slow writer + fast reader
- Max area/width between ends where only moving the worse side can improve -> converging (Container With Most Water)
- Answer at i depends on max-so-far from each side -> two pointers with running maxes (Trapping Rain Water)

## Templates

```python
# converging (Two Sum II on sorted)
l, r = 0, len(nums) - 1
while l < r:
    s = nums[l] + nums[r]
    if s == target:
        return [l + 1, r + 1]
    if s < target:
        l += 1
    else:
        r -= 1

# 3Sum: sort + fix i + converging pair; skip duplicates at every level
nums.sort()
for i in range(len(nums) - 2):
    if i and nums[i] == nums[i-1]:
        continue
    l, r = i + 1, len(nums) - 1
    while l < r:
        s = nums[i] + nums[l] + nums[r]
        if s < 0:
            l += 1
        elif s > 0:
            r -= 1
        else:
            res.append([nums[i], nums[l], nums[r]])
            l += 1
            while l < r and nums[l] == nums[l-1]:
                l += 1

# Trapping Rain Water, O(1) space
l, r = 0, n - 1
lmax = rmax = water = 0
while l < r:
    if height[l] < height[r]:
        lmax = max(lmax, height[l])
        water += lmax - height[l]
        l += 1
    else:
        rmax = max(rmax, height[r])
        water += rmax - height[r]
        r -= 1
```

## Complexity

O(n) per sweep (each pointer moves at most n total). 3Sum: O(n^2) after O(n log n) sort.

## Pitfalls

- Duplicate-skipping in 3Sum: needed for the fixed index AND after recording a triplet.
- Justify the move out loud: "moving the taller side can never help, so I move the shorter one."
- while l < r vs l <= r: off-by-one on whether pointers may meet.
