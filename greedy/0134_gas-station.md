# 134 — Gas Station

## Problem

A circular route of gas stations: `gas[i]` to gain, `cost[i]` to reach the next. Find the unique start completing the loop, or −1.

**Example:** `gas = [1,2,3,4,5]`, `cost = [3,4,5,1,2]` → `3`

## Walkthrough

Net deltas per station: `[−2,−2,−2,3,3]`. Two facts do everything: the trip is possible iff **total ≥ 0**, and if a tank starting at A runs dry before B, **no start strictly between A and B works either** (it begins with ≤ the same fuel) — so on failure, jump the candidate to B+1.

**[1] deltas: gas − cost**
```text
station: 0   1   2   3   4
delta:  -2  -2  -2  +3  +3   total = 0 ≥ 0 → a start exists
```

**[2] try start 0 — dies at station 2**
```text
tank: -2 → -4 → -6 < 0 at station 2
candidate jumps to 3; stations 1,2 provably hopeless (they'd start deeper in the hole)
```

**[3] resume from 3**
```text
station: 3 → 4 → 0 → 1 → 2 (wrap)
tank:    +3  +6  +4  +2   0 ≥ 0 throughout → return 3 ✓
```

**[4] why skipping is safe — the killed interval**
```text
start A fails reaching B: tank at any intermediate S is tank_A(S) < 0
by construction → starting at S inherits negative balance → also fails
```

**[5] why one candidate survives**
```text
total ≥ 0 guarantees the final candidate (never tested against a
failure) completes — the last segment is the only unrefuted one
```

Why it works: the failure-skip lemma turns the O(n²) try-every-start into a single pass that discards provably-dead intervals (an exchange-argument cousin of 0055's jump reach, this folder). O(n) time, O(1) space; the wrap-around needs no special handling since the surviving candidate's prefix tank only ever grows once past its restart.
