# 207 — Course Schedule

## Problem

`numCourses` with prerequisites `[course, prereq]`: can all courses be finished? (Is the directed graph acyclic?)

**Example:** `n = 4`, `prereqs = [[1,0],[2,1],[3,2]]` → `true`; add `[0,3]` and the loop 0→1→2→3→0 kills it.

## Walkthrough

**Topological sort via DFS cycle detection.** Three colors: white (unvisited), gray (on the current DFS path), black (done). Hitting a **gray** node = back edge = cycle. All black at the end ⟺ a valid course order exists (that's problem 210's output).

**[1] prereq edges (prereq → course)**
```text
0 → 1 → 2 → 3
colors: all white  start DFS at 0
```

**[2] dive down the chain**
```text
0 → 1 → 2 → 3
G   G   G   G
each node grays on entry; the path is the current dependency chain
```

**[3] 3 has no out-edges — blacken and unwind**
```text
0 → 1 → 2 → 3
G   G   G   B
3 finishes; post-order blackening pops back up
```

**[4] all black — acyclic**
```text
0 → 1 → 2 → 3
B   B   B   B
return True  post-order was 3,2,1,0 — a reverse topological order
```

**[5] the failure case — add edge 3 → 0**
```text
0 → 1 → 2 → 3
 ↖__________|
DFS from 0: 0G 1G 2G 3G → 3's neighbor 0 is GRAY → back edge → cycle → False
```

Why it works: gray marks the active DFS path; any edge into gray points backward along that path — the definition of a cycle. Black is safe to re-enter: that subtree is fully explored and cycle-free. O(V+E), one pass. Kahn's algorithm (indegree-0 peeling) is the BFS twin — and its emitted order is problem 210's answer directly.
