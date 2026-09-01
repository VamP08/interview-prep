# Pattern Index

Fast pre-interview review: signal -> pattern -> where it lives.

| Signal in the problem | Pattern | Notes |
|---|---|---|
| Seen before? / count / group by equivalence | Hash map / set | [01-arrays-hashing](01-arrays-hashing/notes.md) |
| Sorted + pair/triplet target | Converging two pointers | [02-two-pointers](02-two-pointers/notes.md) |
| Longest/shortest contiguous substring/subarray | Sliding window | [03-sliding-window](03-sliding-window/notes.md) |
| Nesting, matching, expression eval | Stack | [04-stack](04-stack/notes.md) |
| Next greater/smaller, spans, histogram area | Monotonic stack | [04-stack](04-stack/notes.md) |
| Sorted search, "min X such that check(X)" | Binary search (on answer) | [05-binary-search](05-binary-search/notes.md) |
| Middle / cycle / nth-from-end of list | Fast & slow pointers | [06-linked-list](06-linked-list/notes.md) |
| Reverse list (part) in place | Prev/curr reversal | [06-linked-list](06-linked-list/notes.md) |
| O(1) cache with eviction | Hash map + DLL (LRU) | [06-linked-list](06-linked-list/notes.md) |
| Height/diameter/path through node | Post-order DFS, return vs global | [07-trees](07-trees/notes.md) |
| Level-by-level tree | BFS with frozen level size | [07-trees](07-trees/notes.md) |
| BST ordering (validate, kth) | Inorder / (lo, hi) bounds | [07-trees](07-trees/notes.md) |
| K largest/closest/frequent | Size-k min-heap | [08-heap-priority-queue](08-heap-priority-queue/notes.md) |
| Running median | Two heaps | [08-heap-priority-queue](08-heap-priority-queue/notes.md) |
| All subsets/permutations/combinations | Backtracking (choose/recurse/unchoose) | [09-backtracking](09-backtracking/notes.md) |
| Prefix queries, wildcard words, multi-word grid search | Trie | [10-tries](10-tries/notes.md) |
| Regions/islands in grid | Flood fill DFS/BFS | [11-graphs](11-graphs/notes.md) |
| Spread from multiple sources, min time | Multi-source BFS | [11-graphs](11-graphs/notes.md) |
| Dependency order, cycle in DAG | Topological sort | [11-graphs](11-graphs/notes.md) |
| Dynamic connectivity, redundant edge | Union-find | [11-graphs](11-graphs/notes.md) |
| Weighted shortest path | Dijkstra | [12-advanced-graphs](12-advanced-graphs/notes.md) |
| Connect all at min cost | MST (Prim/Kruskal) | [12-advanced-graphs](12-advanced-graphs/notes.md) |
| At most K edges/stops | Bellman-Ford rounds | [12-advanced-graphs](12-advanced-graphs/notes.md) |
| Ways to reach i / take-or-skip in a line | 1-D DP | [13-dp-1d](13-dp-1d/notes.md) |
| Longest increasing subsequence | DP O(n^2) or tails + bisect | [13-dp-1d](13-dp-1d/notes.md) |
| Two strings compared (edit, common, match) | 2-D DP over prefixes | [14-dp-2d](14-dp-2d/notes.md) |
| Items x capacity/total | Knapsack DP (loop order matters) | [14-dp-2d](14-dp-2d/notes.md) |
| Provable local choice (exchange argument) | Greedy | [15-greedy](15-greedy/notes.md) |
| Max subarray | Kadane | [15-greedy](15-greedy/notes.md) |
| Overlapping ranges, rooms, merges | Sort + sweep / heap of ends | [16-intervals](16-intervals/notes.md) |
| Matrix rotate/spiral/in-place marks | Boundary bookkeeping | [17-math-geometry](17-math-geometry/notes.md) |
| Pairs cancel, appears-once, no extra space | XOR / bit tricks | [18-bit-manipulation](18-bit-manipulation/notes.md) |

If nothing matches: brute force first, state its complexity, then look for the bottleneck - the pattern usually hides in what the brute force recomputes.
