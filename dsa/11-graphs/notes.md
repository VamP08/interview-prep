# Graphs

## Core idea

Model the problem as nodes + edges (often implicit: grid cells, words, courses), then pick the engine: DFS (components, flood fill), BFS (shortest path in UNWEIGHTED graphs, multi-source spread), topological sort (dependency order, cycle detection in DAGs), union-find (dynamic connectivity).

## Recognition signals

- Grid of land/water, regions, islands -> flood fill DFS/BFS
- "Minimum steps/time to reach or spread" unweighted -> BFS; "from multiple starts" (Rotting Oranges) -> multi-source BFS: seed queue with ALL sources
- Prerequisites / build order / "can finish?" -> topological sort (cycle = impossible)
- "Are these connected / count components / redundant edge" -> union-find or DFS
- Word transformation chains -> implicit graph + BFS

## Templates

```python
# grid DFS flood fill
def dfs(r, c):
    if not (0 <= r < R and 0 <= c < C) or grid[r][c] != "1":
        return
    grid[r][c] = "#"                     # mark visited in place
    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
        dfs(r + dr, c + dc)

# multi-source BFS (Rotting Oranges): all sources at distance 0
q = deque((r, c, 0) for r in range(R) for c in range(C) if grid[r][c] == 2)
while q:
    r, c, t = q.popleft()
    for dr, dc in dirs:
        nr, nc = r + dr, c + dc
        if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == 1:
            grid[nr][nc] = 2
            q.append((nr, nc, t + 1))

# topological sort (Kahn's / BFS on indegree)
indeg = [0] * n
adj = defaultdict(list)
for a, b in edges:                       # b -> a (b before a)
    adj[b].append(a)
    indeg[a] += 1
q = deque(i for i in range(n) if indeg[i] == 0)
order = []
while q:
    u = q.popleft()
    order.append(u)
    for v in adj[u]:
        indeg[v] -= 1
        if indeg[v] == 0:
            q.append(v)
# len(order) < n  <=>  cycle

# union-find with path compression + rank
parent = list(range(n))
rank = [0] * n
def find(x):
    while parent[x] != x:
        parent[x] = parent[parent[x]]    # compression
        x = parent[x]
    return x
def union(a, b):
    ra, rb = find(a), find(b)
    if ra == rb:
        return False                     # already connected (the redundant edge)
    if rank[ra] < rank[rb]:
        ra, rb = rb, ra
    parent[rb] = ra
    rank[ra] += rank[ra] == rank[rb]
    return True
```

## Complexity

DFS/BFS O(V + E). Union-find ~O(alpha) per op (say "effectively constant"). Grid: V = R*C, E = 4V.

## Pitfalls

- Mark visited WHEN ENQUEUEING, not when popping - else duplicates blow up the queue.
- Clone Graph: dict old->new created before recursing on neighbors.
- Surrounded Regions: invert the problem - flood from the BORDER, everything unreached flips.
- Course Schedule edge direction: write down "prereq -> course" before coding.
- Recursion depth on big grids: iterative DFS or raise the limit.
