# 55 — Jump Game

## Problem

Each `nums[i]` is the max jump from `i`. Can you reach the last index?

**Example:** `nums = [2,3,1,1,4]` → `true`; `[3,2,1,0,4]` → `false`

## Walkthrough

Greety sweep with a **furthest-reach** frontier: walking left to right, extend `reach = max(reach, i + nums[i])`. If you ever arrive at an index *beyond* the current reach, you're stuck — no position before it could jump far enough.

**[1] i=0 — reach opens to 2**
```text
[2, 3, 1, 1, 4]
  i
reach=2  0+2=2 — indices 1,2 are live
```

**[2] i=1 — reach opens to 4**
```text
[2, 3, 1, 1, 4]
     i
reach=4  1+3=4 — the last index is now reachable
```

**[3] i=2 — nothing new, but safe**
```text
[2, 3, 1, 1, 4]
        i
reach=4  2+1=3 < 4 → frontier unchanged; i ≤ reach keeps going
```

**[4] reach covers n−1 → true**
```text
[2, 3, 1, 1, 4]
reach=4 ≥ 4  return True
```

**[5] the trap: [3,2,1,0,4]**
```text
[3, 2, 1, 0, 4]
        i  reach=3 → i=3 == reach; nums[3]=0 adds nothing
i=4 > reach  → return False — the zero is a wall no prior jump clears
```

Why it works: the set of reachable indices is exactly {i : i ≤ reach after all earlier positions} — reach is monotone and summarizes every jump option so far. One pass, O(n), O(1). Compare 0045's flipbook in this folder, which counts BFS-style *layers* to the same frontier.
