# 127 — Word Ladder

## Problem

Shortest ladder from `beginWord` to `endWord`, changing one letter per step with every intermediate a dictionary word (word count, including both ends).

**Example:** `hit → hot → dot → dog → cog` → `5`

## Walkthrough

BFS on an **implicit wildcard graph**: each word maps to L patterns (`h*t`, `*ot`, `ho*`); words sharing a pattern are one mutation apart. BFS layers = ladder length; first arrival at endWord is optimal.

**[1] build the pattern buckets**
```text
hot → *ot, h*t, ho*     dot → *ot, d*t, do*
*ot → [hot, dot, lot]   (mutations connect through the bucket)
```

**[2] layer 1: hit's neighbors**
```text
h*t → hot ✓ (i and t match)   others empty
queue: (hot, 2)   dist counted in words: hit=1, hot=2
```

**[3] layer 2: hot fans out**
```text
*ot bucket → dot, lot   ho* empty   h*t already seen
queue: (dot,3) (lot,3)
```

**[4] layer 3 → the target**
```text
dot → do* → dog (4)   lot → lo* → log (4)
dog → *og → cog ✓ return 4+1 = 5
```

**[5] why patterns beat naive mutation**
```text
trying 26 letters × L positions per word needs word-set lookups;
buckets precompute adjacency once — each edge found in O(1) amortized
```

Why it works: mutation adjacency is an equivalence on patterns — u~v iff they share a wildcard signature for some position — so buckets materialize exactly the graph's edges, and BFS's first-arrival rule (1091/0542, this folder) gives the shortest ladder. O(n·L²) build + O(n·L) search; bidirectional BFS (from both words) halves the frontier for the same answer.
