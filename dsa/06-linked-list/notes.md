# Linked List

## Core idea

Pointer surgery. Three sub-patterns cover nearly everything: (1) in-place reversal with prev/curr, (2) fast & slow pointers for middles and cycles, (3) dummy head to erase edge cases at the front. Plus one design classic: LRU cache = hash map + doubly linked list.

## Recognition signals

- "Reverse (part of) a list" -> prev/curr iteration
- "Middle", "cycle?", "cycle start", "nth from end" -> fast & slow
- "Merge sorted lists" -> dummy head + tail pointer
- "Find duplicate number in array of n+1 in [1..n]" -> array AS linked list, Floyd cycle detection
- "O(1) get/put with eviction" -> hash map + DLL (LRU)

## Templates

```python
# in-place reversal
prev = None
while curr:
    nxt = curr.next
    curr.next = prev
    prev = curr
    curr = nxt
return prev

# fast & slow: middle + cycle detection
slow = fast = head
while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow is fast:                 # cycle exists (omit for middle-finding)
        break
# cycle START: reset one pointer to head, advance both by 1 until they meet

# nth from end: gap trick
lead = follow = dummy = ListNode(0, head)
for _ in range(n):
    lead = lead.next
while lead.next:
    lead = lead.next
    follow = follow.next
follow.next = follow.next.next       # removes nth from end

# merge two sorted
dummy = tail = ListNode()
while a and b:
    if a.val <= b.val:
        tail.next, a = a, a.next
    else:
        tail.next, b = b, b.next
    tail = tail.next
tail.next = a or b
return dummy.next
```

LRU Cache in Python interviews: implement with dict + DLL nodes for the real thing; mention OrderedDict / move_to_end as the pragmatic version and be ready to code either.

## Complexity

All single-pass patterns O(n) time, O(1) space. Merge K lists: heap gives O(N log k).

## Pitfalls

- Dummy head kills the "what if I delete/insert at head" special case - use it by reflex.
- Draw boxes and arrows before coding; state the pointer order (save next BEFORE overwriting).
- Cycle detection: compare with is, and guard fast AND fast.next.
- Copy with random pointer: dict old->new in pass 1, wire in pass 2 (or interleave for O(1) space).
