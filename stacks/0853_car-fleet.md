# 853 — Car Fleet

## Problem

Cars at `position` driving at `speed` toward a common `target`; a faster car catching a slower one **merges into its fleet** (both then move at the slower pace). How many fleets arrive?

**Example:** `target = 12`, `pos = [10,8,0,5,3]`, `speed = [2,4,1,1,3]` → `3`

## Walkthrough

Sort by position (front car first) and compute each car's solo arrival time: `(target − pos) / speed`. Scan from front to back: a car arrives **later** than the car ahead ⟹ it catches it before the target and joins that fleet; earlier or equal ⟹ it never catches (the one ahead is at least as fast toward the target) ⟹ new fleet. A monotonic stack of arrival times does the same check.

**[1] times sorted by position (front → back)**
```text
car:     10   8   5   3   0
time:     1   1   7   3  12
front car at 10 arrives at t=1
```

**[2] car at 8: time 1 — never catches**
```text
times: 1 1 7 3 12
fleet=2  1 ≤ 1: equal time means no catch (it'd reach exactly together) → new fleet? — equal is a catch (they meet at the line)
```

Careful with ties: time 1 vs 1 — the car at 8 would reach the point (10, t=1) exactly as the front does: fleets merge (LeetCode counts `<=` as merge).

**[3] car at 5: time 7 — blocked by the fleet ahead**
```text
times: 1 1 7 …
7 > 1 → catches the t=1 fleet before target → merges, no new fleet
```

**[4] cars at 3 and 0**
```text
times: 1 1 7 3 12
3 > 1 merges;  12 > 3 → catches the t=3 fleet → merges
```

**[5] result**
```text
fleets: {10,8}, {5}, {3,0} → return 3 ✓
```

Why it works: arrival time is a complete summary — car A catches B iff A's solo time ≤ B's (A covers the same remaining distance no slower). Scanning front-to-back with "new fleet iff time < fleet-ahead's time" counts exactly the fleets that survive catching; a stack keeping strictly decreasing times is the one-pass implementation. O(n log n), sort-dominated.
