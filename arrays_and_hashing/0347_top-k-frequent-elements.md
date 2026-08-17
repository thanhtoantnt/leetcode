# 347 — Top K Frequent Elements

## Problem

Return the `k` most frequent elements of `nums`.

**Example:** `nums = [1,1,1,2,2,3]`, `k = 2` → `[1,2]`

## Walkthrough

Count occurrences, then **bucket by frequency**: bucket[f] holds every value seen exactly f times. Since frequency is at most n, buckets are indexed 0..n — walk them from high to low, collecting values until k are gathered. No heap, no sort.

**[1] count each value**
```text
[1, 1, 1, 2, 2, 3]
  i
count: 1→3, 2→2, 3→1
```

**[2] drop values into frequency buckets**
```text
[1, 1, 1, 2, 2, 3]
bucket[3]=[1]  bucket[2]=[2]  bucket[1]=[3]
```

**[3] walk buckets top-down**
```text
[1, 1, 1, 2, 2, 3]
take=1  bucket[3] gives value 1
```

**[4] collect until k**
```text
[1, 1, 1, 2, 2, 3]
take=[1,2]  bucket[2] gives value 2 → have k=2, stop
```

**[5] done**
```text
[1, 1, 1, 2, 2, 3]
return [1,2]
```

Why it works: counting is O(n), bucketing is O(n), and the final walk visits at most n buckets — O(n) total, beating the heap approach's O(n log k). The same bucket trick underlies counting sort (CLRS Ch. 8).
