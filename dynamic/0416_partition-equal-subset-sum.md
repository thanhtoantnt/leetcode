# 416 — Partition Equal Subset Sum

## Problem

Can the array be split into two subsets with equal sums? (Equivalently: is there a subset summing to `total/2`?)

**Example:** `nums = [1,5,11,5]` → `true` (`[1,5,5]` and `[11]`)

## Walkthrough

Subset-sum DP over **reachable sums**. Odd total → immediate `false`. Otherwise sweep the numbers, each extending the reachable set by its own value (only sums ≤ target matter). Reaching `target` means a partition exists.

**[1] total = 22, target = 11; sum 0 reachable**
```text
sums: 0 1 2 3 4 5 6 7 8 9 10 11
      ✓ . . . . . . . . . .  .
processing 1  empty subset only
```

**[2] take 1**
```text
sums: 0 1 2 3 4 5 6 7 8 9 10 11
      ✓ ✓ . . . . . . . . .  .
0+1=1  add {1}
```

**[3] take 5 — old set shifts by 5**
```text
sums: 0 1 2 3 4 5 6 7 8 9 10 11
      ✓ ✓ . . . ✓ ✓ . . . .  .
{0,1} + 5 → {5,6}; union → {0,1,5,6}
```

**[4] take 11 — target reached**
```text
sums: 0 1 2 3 4 5 6 7 8 9 10 11
      ✓ ✓ . . . ✓ ✓ . . . .  ✓
0+11=11 = target ✓ → True ([11] vs [1,5,5])
```

**[5] an impossible case: [1,2,5]**
```text
total=8, target=4
reach {0,1,2,3,5,6,7,8} — 4 never appears → False
```

Why it works: "some subset sums to t" is built one element at a time — each element is in or out, and the reachable-set update `R := R ∪ (R + x)` applies exactly that choice. Bitset version in Python: `bits |= bits << x` (and mask at target) — the same DP with machine-word parallelism. O(n · target) time; pseudo-polynomial, which is why the problem is NP-hard in general yet tractable at these sizes (CLRS Ch. 34/35's subset-sum discussion).
