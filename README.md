# LeetCode Practice

**Live site:** https://thanhtoantnt.github.io/leetcode/

Two halves: [LeetCode problems](https://thanhtoantnt.github.io/leetcode/problems) (animated walkthroughs) and [CLRS](https://thanhtoantnt.github.io/leetcode/book) (chapter notes).

## Layout

```
<pattern>/NNNN_slug.py   # solution
<pattern>/NNNN_slug.md   # optional flipbook (frames of the algorithm running)
web/                     # Next.js site that plays those flipbooks
```

~115 solutions across 19 patterns (`arrays_and_hashing/`, `sliding_windows/`, `dynamic/`, …).

## Visualized so far

| # | Pattern | Problem |
|---|---------|---------|
| 3 | sliding window | [Longest Substring Without Repeating Characters](sliding_windows/0003_longest-substring-without-repeating-characters.md) |
| 39 | backtracking | [Combination Sum](backtracking/0039_combination-sum.md) |
| 167 | two pointers | [Two Sum II](two_pointers/0167_two-sum-ii-input-array-is-sorted.md) |
| 198 | DP | [House Robber](dynamic/0198_house-robber.md) |
| 542 | BFS | [01 Matrix](BFS/0542_01-matrix.md) |

## Add a solution

Drop `<pattern>/NNNN_slug.py` next to its siblings. Slug = the LeetCode URL slug (`two-sum`, `house-robber`).

## Add an animation

Copy one of the existing `.md` flipbooks. One fenced block per step:

````markdown
**[1] start**
```text
[2, 7, 11, 15]
 L           R
sum = 17 > 9 → R--
```
````

Same basename as the `.py`. Push to `main` — the site rebuilds itself.

## Run the site locally

```bash
cd web
npm install
npm run dev     # http://localhost:3000
```
