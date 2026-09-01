# Trees

## Core idea

Two traversal engines: DFS (recursive, "answer for node = combine answers of children") and BFS (level order, queue). Most tree problems are: pick the traversal, decide what each call RETURNS vs what it UPDATES globally. BST adds the ordering invariant: inorder = sorted.

## Recognition signals

- Depth/height/diameter/balance -> post-order DFS returning height, updating a global
- "Level by level", "right side view", "zigzag" -> BFS with level size
- "Validate BST", "kth smallest in BST" -> inorder traversal or (lo, hi) bounds
- LCA in BST -> walk from root using ordering; general LCA -> post-order
- "Path sum through any node" -> per-node best = left gain + node + right gain, return one-sided gain
- Serialize/deserialize -> preorder with null markers

## Templates

```python
# post-order returning height, computing diameter globally
def dfs(node):
    if not node:
        return 0
    lh, rh = dfs(node.left), dfs(node.right)
    self.best = max(self.best, lh + rh)
    return 1 + max(lh, rh)

# BFS by levels
q = deque([root])
while q:
    level = []
    for _ in range(len(q)):          # freeze level size
        node = q.popleft()
        level.append(node.val)
        if node.left:  q.append(node.left)
        if node.right: q.append(node.right)
    res.append(level)

# validate BST with bounds
def valid(node, lo=float("-inf"), hi=float("inf")):
    if not node:
        return True
    if not (lo < node.val < hi):
        return False
    return valid(node.left, lo, node.val) and valid(node.right, node.val, hi)

# max path sum: return one-sided, record two-sided
def gain(node):
    if not node:
        return 0
    lg = max(gain(node.left), 0)     # clamp negatives to 0
    rg = max(gain(node.right), 0)
    self.best = max(self.best, node.val + lg + rg)
    return node.val + max(lg, rg)
```

## Complexity

Traversals O(n) time; space O(h) recursion (O(n) worst, O(log n) balanced). BFS space O(width).

## Pitfalls

- Validate BST by comparing only with parent is WRONG - must carry (lo, hi) bounds or use inorder.
- The return-vs-global split: diameter/path-sum return the one-branch value, record the through-node value on the side.
- Freeze len(q) before the level loop or levels bleed together.
- Empty tree and single node are the edge cases to state.
- Build-from-preorder+inorder: hashmap value->inorder index, recurse on index ranges - avoid list slicing (O(n^2)).
