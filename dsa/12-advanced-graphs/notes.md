# Advanced Graphs

## Core idea

Weighted-graph algorithms: Dijkstra (shortest path, non-negative weights), Prim/Kruskal (minimum spanning tree), Bellman-Ford-style relaxation (K-stop constraints), Eulerian path (use every edge once), and Dijkstra-variants where "path cost" is redefined (max along path instead of sum).

## Recognition signals

- "Shortest/fastest with WEIGHTED edges" -> Dijkstra (heap of (dist, node))
- "Connect all points at min total cost" -> MST (Prim with heap, or Kruskal + union-find)
- "Cheapest with at most K stops" -> Bellman-Ford, K rounds of relaxation (Dijkstra breaks under the stop budget)
- "Minimize the MAXIMUM edge on a path" (Swim in Rising Water) -> Dijkstra with max() instead of + , or binary search + BFS
- "Use every ticket/edge exactly once, lexical order" -> Eulerian path, Hierholzer's
- "Derive letter order from sorted words" -> build precedence edges, toposort (Alien Dictionary)

## Templates

```python
# Dijkstra
dist = {src: 0}
h = [(0, src)]
while h:
    d, u = heapq.heappop(h)
    if d > dist.get(u, float("inf")):
        continue                          # stale entry
    for v, w in adj[u]:
        nd = d + w
        if nd < dist.get(v, float("inf")):
            dist[v] = nd
            heapq.heappush(h, (nd, v))

# Prim's MST from node 0
seen = set()
h = [(0, 0)]
total = 0
while h and len(seen) < n:
    w, u = heapq.heappop(h)
    if u in seen:
        continue
    seen.add(u)
    total += w
    for v, wv in adj[u]:
        if v not in seen:
            heapq.heappush(h, (wv, v))

# Bellman-Ford, at most k+1 edges (Cheapest Flights Within K Stops)
dist = [float("inf")] * n
dist[src] = 0
for _ in range(k + 1):
    nxt = dist[:]                         # relax from LAST round's values only
    for u, v, w in flights:
        if dist[u] + w < nxt[v]:
            nxt[v] = dist[u] + w
    dist = nxt

# Hierholzer's (Reconstruct Itinerary): greedy lexical DFS, post-order push
for dst in sorted(tickets_by_src[src], reverse=True):  # pop() gives smallest
    ...
def dfs(u):
    while adj[u]:
        dfs(adj[u].pop())
    route.append(u)                       # reversed at the end
```

## Complexity

Dijkstra / Prim with heap: O(E log V). Kruskal: O(E log E). Bellman-Ford K rounds: O(K * E). Hierholzer: O(E log E) with sorting.

## Pitfalls

- Dijkstra requires non-negative weights - say it before using it.
- Skip stale heap entries (the d > dist[u] guard) instead of decrease-key.
- K-stops: copying dist per round is what enforces the edge budget; in-place relaxation leaks longer paths.
- Kruskal needs union-find; reuse the one from Graphs notes.
