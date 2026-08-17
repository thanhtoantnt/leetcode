# 56 — Merge Intervals

## Problem

Given an array of intervals `[start, end]`, merge all overlapping intervals and return the non-overlapping result.

**Example:** `[[1,3],[2,6],[8,10],[15,18]]` → `[[1,6],[8,10],[15,18]]`

## Walkthrough

Sort by start. Walk left to right: if the next interval starts before the current one ends, they overlap — extend the current end; otherwise push the current and start fresh.

**[1] sorted by start**
```text
start: 1 2 8 15
end:   3 6 10 18
       i
out=[[1,3]]  seed the output with the first interval
```

**[2] [2,6] overlaps [1,3] — extend**
```text
start: 1 2 8 15
end:   3 6 10 18
         i
out=[[1,6]]  2 ≤ 3 → overlap: current becomes [1, max(3,6)] = [1,6]
```

**[3] [8,10] is clear of [1,6] — push and start fresh**
```text
start: 1 2 8 15
end:   3 6 10 18
           i
out=[[1,6],[8,10]]  8 > 6 → no overlap: commit [1,6], carry [8,10]
```

**[4] [15,18] is clear too**
```text
start: 1 2 8 15
end:   3 6 10 18
              i
out=[[1,6],[8,10],[15,18]]  15 > 10 → commit, carry [15,18]
```

**[5] flush the last interval**
```text
start: 1 2 8 15
end:   3 6 10 18
out=[[1,6],[8,10],[15,18]]  done
```

Why it works: after sorting, any interval that overlaps the current one must start before the current end — and everything further right starts even later, so a single linear pass catches every merge. O(n log n), sort-dominated.
