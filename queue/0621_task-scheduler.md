# 621 — Task Scheduler

## Problem

Tasks A–Z need running; identical tasks must be spaced at least `n` slots apart (idle or other tasks fill gaps). Minimum total time?

**Example:** `tasks = ["A","A","A","B","B","B"]`, `n = 2` → `8` (`A B _ A B _ A B`)

## Walkthrough

The **most frequent task** sets the frame: if it appears `maxCount` times, there are `maxCount−1` gaps of size `n+1` between its runs, plus its own final run. The formula `answer = (maxCount−1)·(n+1) + (number of tasks tied at maxCount)` — unless there are enough *other* tasks to fill every idle slot, in which case the total is just `len(tasks)`.

**[1] counts: A=3, B=3, n=2**
```text
A B _ A B _ A B
frame: (3−1)·(2+1) = 6 slots + final row
```

**[2] arrange — one frame per A-run**
```text
A B _ | A B _ | A B
gaps filled by B, cooldown trailing each frame
```

**[3] count tied tasks at the max**
```text
tied = 2 (A and B) → answer = 6 + 2 = 8 ✓
```

**[4] the no-idle case: A=3, B,C,D,E… many others**
```text
A B C A D E A F …  enough distinct tasks to fill every gap
answer = len(tasks)  formula would *under*count → take the max
```

**[5] final rule**
```text
return max( (maxCount−1)·(n+1) + tied, len(tasks) )
```

Why it works: the most frequent task alone forces `(maxCount−1)·(n+1)` slots plus one for each max-frequency task's last run — a hard floor; every other task fits into the gaps without ever breaking *its own* spacing (they're rarer). If total tasks exceed the frame, no idle slots remain and length wins. O(len) counting, no simulation needed — the heap + simulation version (always schedule the most-frequent remaining task) gives the same number with more machinery.
