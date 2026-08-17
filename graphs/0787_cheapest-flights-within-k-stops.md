# 787 — Cheapest Flights Within K Stops

## Problem

Cheapest path `src → dst` using at most `k` intermediate stops (negative prices don't exist, but a **hop budget** rules out plain Dijkstra).

**Example:** `flights = [[0,1,100],[1,2,100],[0,2,500]]`, `k = 1` → `200` (0→1→2, two edges, one stop)

## Walkthrough

**Bellman-Ford with a round budget**: after round r, `dist[v]` = cheapest fare using ≤ r edges. Each round relaxes *all* edges against a **frozen copy** of last round's distances — otherwise a chain of same-round updates would sneak extra hops into one round.

**[1] round 0: only src known**
```text
dist=[0, ∞, ∞]
src=0  flights: 0→1(100), 1→2(100), 0→2(500)
```

**[2] round 1 (k+1 = 2 rounds total)**
```text
relax on a copy: 0→1 → dist[1]=100; 0→2 → dist[2]=500
dist=[0, 100, 500]  1-edge paths
```

**[3] round 2**
```text
from the frozen copy: 1→2 gives 100+100=200 < 500
dist=[0, 100, 200]  2-edge path wins — exactly the k=1 budget
```

**[4] answer**
```text
return 200 ✓  a third round could not help: no negative cycles to exploit
```

**[5] why not Dijkstra**
```text
Dijkstra finalizes a node's distance permanently — but the cheapest
path may use MORE stops than allowed, and the hop-feasible path is
longer. State must be (node, stops-left), or Bellman-Ford round caps
```

Why it works: round r's distances are exactly the r-edge optima (induction: an r-edge best path is an (r−1)-edge best to its predecessor plus one edge, all seen in the frozen copy). Stopping at k+1 rounds enforces the budget — the core of Bellman-Ford's correctness (CLRS Ch. 24.1) minus the negative-cycle detection we don't need. O(k·E).
