# 981 — Time Based Key-Value Store

## Problem

A map where each key holds timestamped values. `set(key, value, timestamp)` appends; `get(key, timestamp)` returns the value with the **largest timestamp ≤ t**, or `""`.

**Example:** set `foo` at times 1, 4, 8; `get(foo, 5)` → the time-4 value.

## Walkthrough

Per key, a list that only ever grows with strictly increasing timestamps — already sorted. `get` is binary search for the **rightmost timestamp ≤ t**.

**[1] three sets on foo**
```text
foo: [(1, bar), (4, bar2), (8, bar3)]
```

**[2] get(foo, 5) — probe mid ts=4**
```text
[1, 4, 8]
 L  M     H(t=5)
lo=0 hi=2 mid=1  ts 4 ≤ 5 → candidate; answer is mid or later → lo=mid+1=2
```

**[3] probe ts=8**
```text
[1, 4, 8]
          L  H
mid=2  ts 8 > 5 → too new → hi=mid−1=1 → lo>hi, stop
```

**[4] last valid candidate**
```text
[1, 4, 8]
    ✓
return bar2  best ts ≤ 5 is 4
```

**[5] edge: get(foo, 0)**
```text
[1, 4, 8]
ts 1 > 0 → never recorded a candidate → return ""
```

Why it works: appending in timestamp order keeps the list sorted for free; "rightmost ≤ t" on a sorted list is one O(log n) binary search (`bisect_right` minus one). The candidate-tracking variant shown above (remember mid on ≤, move lo past it) is the manual version of `bisect_right(t) − 1`.
