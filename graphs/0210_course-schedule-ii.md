# 210 — Course Schedule II

## Problem

Same prerequisites as 207, but return a valid ordering of all courses — a **topological sort**.

**Example:** `n = 4`, `prereqs = [[1,0],[2,0],[3,1],[3,2]]` → `[0,2,1,3]` (or `[0,1,2,3]`)

## Walkthrough

**Kahn's algorithm (BFS peeling).** Compute indegrees; a course with indegree 0 has all prereqs met — take it, and decrement its dependents. Repeatedly take any newly-zero course. If fewer than n courses get taken, a cycle blocked the rest.

**[1] build indegrees**
```text
0 → 1, 2
1 → 3
2 → 3
indegree: 0=0  1=1  2=1  3=2
```

**[2] peel 0 — the only indegree-0 course**
```text
0 ✓  1 → 3, 2 → 3
indegree: 0=–  1=0  2=0  3=2
taking 0 releases both 1 and 2 → queue: [1, 2]
```

**[3] peel 1 (queue order decides ties)**
```text
0 → 1 ✓ → 3, 2 → 3
indegree: 3=1
3 still waits on 2
```

**[4] peel 2 — 3 releases**
```text
0 → 1 ✓ → 3, 2 ✓ → 3
indegree: 3=0  queue: [3]
```

**[5] peel 3 — done**
```text
order=[0,1,2,3]  4 = n courses taken → valid schedule
```

**[6] the cycle detector: add [0,3]**
```text
0→1→3→0 →  2 loop
peeling stalls: nothing has indegree 0 → len(order)=0 < 4 → return []
```

Why it works: an indegree-0 node has no unmet prerequisites, so putting it next is always safe; removing it updates exactly its dependents. Every acyclic graph has a source (else follow indegrees backward forever — a cycle), so peeling drains it completely. O(V+E). The DFS alternative: post-order blackening reversed (problem 207's frames) produces the same kind of order.
