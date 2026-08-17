# Introduction to Algorithms (CLRS, 3rd ed.)

Local companion to [`Cormen_Introduction_to_Algorithms.pdf`](Cormen_Introduction_to_Algorithms.pdf) (gitignored). This file is an index, not the book.

- Authors: Cormen, Leiserson, Rivest, Stein
- Edition: 3rd (2009), 1313 PDF pages
- Official site / selected solutions: https://mitpress.mit.edu/9780262033848/introduction-to-algorithms/

**How to jump:** `printed page + 21 = PDF page`. Links below open the local PDF at that page (`#page=N`) in a browser.

## How this maps onto the repo

| CLRS | Pattern folder | Visualized here |
|------|----------------|-----------------|
| 2.1 Insertion sort, 2.3 Merge sort | `arrays_and_hashing/` | |
| 4.1 Maximum subarray | `dynamic/0053_maximum-subarray.py` | |
| 10.1 Stacks and queues | `stacks/`, `queue/` | |
| 10.2 Linked lists | `linked_list/` | |
| 11 Hash tables | `arrays_and_hashing/` | [3](sliding_windows/0003_longest-substring-without-repeating-characters.md) |
| 12 Binary search trees | `trees/` | |
| 15 Dynamic programming | `dynamic/` | [198](dynamic/0198_house-robber.md) |
| 15.4 Longest common subsequence | `dynamic/1143_longest-common-subsequence.py` | |
| 16 Greedy algorithms | `greedy/` | |
| 16.1 Activity selection | `intervals/`, `greedy/0435_non-overlapping-intervals.py` | |
| 21 Disjoint sets | `union-find/` | |
| 22.2 BFS | `BFS/` | [542](BFS/0542_01-matrix.md) |
| 22.3 DFS | `graphs/` | |
| 24 Shortest paths | `graphs/` | |
| 32 String matching | `strings/`, `sliding_windows/` | |
| 34 NP-completeness | (background) | |
| 35.5 Subset-sum | `dynamic/0416_partition-equal-subset-sum.py` | |

Live walkthroughs: https://thanhtoantnt.github.io/leetcode/

## Contents

### Preface

[PDF p.14](Cormen_Introduction_to_Algorithms.pdf#page=14) · printed xiii

### I — Foundations

| Ch | Title | PDF |
|----|-------|-----|
| 1 | [The Role of Algorithms in Computing](Cormen_Introduction_to_Algorithms.pdf#page=26) | 26 |
| 1.1 | Algorithms | 26 |
| 1.2 | Algorithms as a technology | 32 |
| 2 | [Getting Started](Cormen_Introduction_to_Algorithms.pdf#page=37) | 37 |
| 2.1 | Insertion sort | 37 |
| 2.2 | Analyzing algorithms | 44 |
| 2.3 | Designing algorithms | 50 |
| 3 | [Growth of Functions](Cormen_Introduction_to_Algorithms.pdf#page=64) | 64 |
| 3.1 | Asymptotic notation | 64 |
| 3.2 | Standard notations and common functions | 74 |
| 4 | [Divide-and-Conquer](Cormen_Introduction_to_Algorithms.pdf#page=86) | 86 |
| 4.1 | The maximum-subarray problem | 89 |
| 4.2 | Strassen’s algorithm for matrix multiplication | 96 |
| 4.3 | The substitution method | 104 |
| 4.4 | The recursion-tree method | 109 |
| 4.5 | The master method | 114 |
| 4.6* | Proof of the master theorem | 118 |
| 5 | [Probabilistic Analysis and Randomized Algorithms](Cormen_Introduction_to_Algorithms.pdf#page=135) | 135 |
| 5.1 | The hiring problem | 135 |
| 5.2 | Indicator random variables | 139 |
| 5.3 | Randomized algorithms | 143 |
| 5.4* | Further uses of indicator RVs | 151 |

### II — Sorting and Order Statistics

| Ch | Title | PDF |
|----|-------|-----|
| 6 | [Heapsort](Cormen_Introduction_to_Algorithms.pdf#page=172) | 172 |
| 6.1 | Heaps | 172 |
| 6.2 | Maintaining the heap property | 175 |
| 6.3 | Building a heap | 177 |
| 6.4 | The heapsort algorithm | 180 |
| 6.5 | Priority queues | 183 |
| 7 | [Quicksort](Cormen_Introduction_to_Algorithms.pdf#page=191) | 191 |
| 7.1 | Description of quicksort | 191 |
| 7.2 | Performance of quicksort | 195 |
| 7.3 | A randomized version of quicksort | 200 |
| 7.4 | Analysis of quicksort | 201 |
| 8 | [Sorting in Linear Time](Cormen_Introduction_to_Algorithms.pdf#page=212) | 212 |
| 8.1 | Lower bounds for sorting | 212 |
| 8.2 | Counting sort | 215 |
| 8.3 | Radix sort | 218 |
| 8.4 | Bucket sort | 221 |
| 9 | [Medians and Order Statistics](Cormen_Introduction_to_Algorithms.pdf#page=234) | 234 |
| 9.1 | Minimum and maximum | 235 |
| 9.2 | Selection in expected linear time | 236 |
| 9.3 | Selection in worst-case linear time | 241 |

### III — Data Structures

| Ch | Title | PDF |
|----|-------|-----|
| 10 | [Elementary Data Structures](Cormen_Introduction_to_Algorithms.pdf#page=253) | 253 |
| 10.1 | Stacks and queues | 253 |
| 10.2 | Linked lists | 257 |
| 10.3 | Implementing pointers and objects | 262 |
| 10.4 | Representing rooted trees | 267 |
| 11 | [Hash Tables](Cormen_Introduction_to_Algorithms.pdf#page=274) | 274 |
| 11.1 | Direct-address tables | 275 |
| 11.2 | Hash tables | 277 |
| 11.3 | Hash functions | 283 |
| 11.4 | Open addressing | 290 |
| 11.5* | Perfect hashing | 298 |
| 12 | [Binary Search Trees](Cormen_Introduction_to_Algorithms.pdf#page=307) | 307 |
| 12.1 | What is a binary search tree? | 307 |
| 12.2 | Querying a BST | 310 |
| 12.3 | Insertion and deletion | 315 |
| 12.4* | Randomly built BSTs | 320 |
| 13 | [Red-Black Trees](Cormen_Introduction_to_Algorithms.pdf#page=329) | 329 |
| 13.1 | Properties of red-black trees | 329 |
| 13.2 | Rotations | 333 |
| 13.3 | Insertion | 336 |
| 13.4 | Deletion | 344 |
| 14 | [Augmenting Data Structures](Cormen_Introduction_to_Algorithms.pdf#page=360) | 360 |
| 14.1 | Dynamic order statistics | 360 |
| 14.2 | How to augment a data structure | 366 |
| 14.3 | Interval trees | 369 |

### IV — Advanced Design and Analysis Techniques

| Ch | Title | PDF |
|----|-------|-----|
| 15 | [Dynamic Programming](Cormen_Introduction_to_Algorithms.pdf#page=380) | 380 |
| 15.1 | Rod cutting | 381 |
| 15.2 | Matrix-chain multiplication | 391 |
| 15.3 | Elements of dynamic programming | 399 |
| 15.4 | Longest common subsequence | 411 |
| 15.5 | Optimal binary search trees | 418 |
| 16 | [Greedy Algorithms](Cormen_Introduction_to_Algorithms.pdf#page=435) | 435 |
| 16.1 | An activity-selection problem | 436 |
| 16.2 | Elements of the greedy strategy | 444 |
| 16.3 | Huffman codes | 449 |
| 16.4* | Matroids and greedy methods | 458 |
| 16.5* | A task-scheduling problem as a matroid | 464 |
| 17 | [Amortized Analysis](Cormen_Introduction_to_Algorithms.pdf#page=472) | 472 |
| 17.1 | Aggregate analysis | 473 |
| 17.2 | The accounting method | 477 |
| 17.3 | The potential method | 480 |
| 17.4 | Dynamic tables | 484 |

### V — Advanced Data Structures

| Ch | Title | PDF |
|----|-------|-----|
| 18 | [B-Trees](Cormen_Introduction_to_Algorithms.pdf#page=505) | 505 |
| 18.1 | Definition of B-trees | 509 |
| 18.2 | Basic operations on B-trees | 512 |
| 18.3 | Deleting a key from a B-tree | 520 |
| 19 | [Fibonacci Heaps](Cormen_Introduction_to_Algorithms.pdf#page=526) | 526 |
| 19.1 | Structure of Fibonacci heaps | 528 |
| 19.2 | Mergeable-heap operations | 531 |
| 19.3 | Decreasing a key and deleting a node | 539 |
| 19.4 | Bounding the maximum degree | 544 |
| 20 | [van Emde Boas Trees](Cormen_Introduction_to_Algorithms.pdf#page=552) | 552 |
| 20.1 | Preliminary approaches | 553 |
| 20.2 | A recursive structure | 557 |
| 20.3 | The van Emde Boas tree | 566 |
| 21 | [Data Structures for Disjoint Sets](Cormen_Introduction_to_Algorithms.pdf#page=582) | 582 |
| 21.1 | Disjoint-set operations | 582 |
| 21.2 | Linked-list representation | 585 |
| 21.3 | Disjoint-set forests | 589 |
| 21.4* | Union by rank + path compression | 594 |

### VI — Graph Algorithms

| Ch | Title | PDF |
|----|-------|-----|
| 22 | [Elementary Graph Algorithms](Cormen_Introduction_to_Algorithms.pdf#page=610) | 610 |
| 22.1 | Representations of graphs | 610 |
| 22.2 | Breadth-first search | 615 |
| 22.3 | Depth-first search | 624 |
| 22.4 | Topological sort | 633 |
| 22.5 | Strongly connected components | 636 |
| 23 | [Minimum Spanning Trees](Cormen_Introduction_to_Algorithms.pdf#page=645) | 645 |
| 23.1 | Growing a minimum spanning tree | 646 |
| 23.2 | Kruskal and Prim | 652 |
| 24 | [Single-Source Shortest Paths](Cormen_Introduction_to_Algorithms.pdf#page=664) | 664 |
| 24.1 | The Bellman-Ford algorithm | 672 |
| 24.2 | DAG shortest paths | 676 |
| 24.3 | Dijkstra’s algorithm | 679 |
| 24.4 | Difference constraints | 685 |
| 24.5 | Proofs of shortest-paths properties | 692 |
| 25 | [All-Pairs Shortest Paths](Cormen_Introduction_to_Algorithms.pdf#page=705) | 705 |
| 25.1 | Shortest paths and matrix multiplication | 707 |
| 25.2 | The Floyd-Warshall algorithm | 714 |
| 25.3 | Johnson’s algorithm for sparse graphs | 721 |
| 26 | [Maximum Flow](Cormen_Introduction_to_Algorithms.pdf#page=729) | 729 |
| 26.1 | Flow networks | 730 |
| 26.2 | The Ford-Fulkerson method | 735 |
| 26.3 | Maximum bipartite matching | 753 |
| 26.4* | Push-relabel algorithms | 757 |
| 26.5* | The relabel-to-front algorithm | 769 |

### VII — Selected Topics

| Ch | Title | PDF |
|----|-------|-----|
| 27 | [Multithreaded Algorithms](Cormen_Introduction_to_Algorithms.pdf#page=793) | 793 |
| 28 | [Matrix Operations](Cormen_Introduction_to_Algorithms.pdf#page=834) | 834 |
| 29 | [Linear Programming](Cormen_Introduction_to_Algorithms.pdf#page=864) | 864 |
| 30 | [Polynomials and the FFT](Cormen_Introduction_to_Algorithms.pdf#page=919) | 919 |
| 31 | [Number-Theoretic Algorithms](Cormen_Introduction_to_Algorithms.pdf#page=947) | 947 |
| 31.7 | The RSA public-key cryptosystem | 979 |
| 32 | [String Matching](Cormen_Introduction_to_Algorithms.pdf#page=1006) | 1006 |
| 32.1 | The naive string-matching algorithm | 1009 |
| 32.2 | The Rabin-Karp algorithm | 1011 |
| 32.3 | String matching with finite automata | 1016 |
| 32.4* | The Knuth-Morris-Pratt algorithm | 1023 |
| 33 | [Computational Geometry](Cormen_Introduction_to_Algorithms.pdf#page=1035) | 1035 |
| 34 | [NP-Completeness](Cormen_Introduction_to_Algorithms.pdf#page=1069) | 1069 |
| 35 | [Approximation Algorithms](Cormen_Introduction_to_Algorithms.pdf#page=1127) | 1127 |

### VIII — Appendix: Mathematical Background

| Ch | Title | PDF |
|----|-------|-----|
| A | [Summations](Cormen_Introduction_to_Algorithms.pdf#page=1166) | 1166 |
| B | [Sets, Etc.](Cormen_Introduction_to_Algorithms.pdf#page=1179) | 1179 |
| C | [Counting and Probability](Cormen_Introduction_to_Algorithms.pdf#page=1204) | 1204 |
| D | [Matrices](Cormen_Introduction_to_Algorithms.pdf#page=1238) | 1238 |
| | [Bibliography](Cormen_Introduction_to_Algorithms.pdf#page=1252) | 1252 |
| | [Index](Cormen_Introduction_to_Algorithms.pdf#page=1272) | 1272 |

`*` = starred (graduate / extra math).
