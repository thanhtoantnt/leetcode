# 355 — Design Twitter

## Problem

Design a feed: `postTweet`, `follow`/`unfollow`, and `getNewsFeed` = the 10 most recent tweets across a user and their followees (own tweets included).

**Example:** user 1 follows 2; both post; feed of 1 interleaves both streams by time.

## Walkthrough

Two maps: `tweets[userId]` = that user's posts in time order (append-only, so each list is already sorted), and `followees[userId]` = a set. `getNewsFeed` is the classic **merge k sorted lists** — one pointer per followee, always take the newest, 10 times. A global timestamp makes "newest" a plain integer comparison.

**[1] user 1 follows 2 (and implicitly self)**
```text
followees[1] = {1, 2}
```

**[2] posts arrive with global timestamps**
```text
tweets[2] = [t3, t1]   (user 2 posted at t1 and t3)
tweets[1] = [t2]       (user 1 posted at t2)
each list sorted ascending — newest at the tail
```

**[3] feed(1): merge pointers at the tails**
```text
ptr2 → t3  ptr1 → t2   take t3 (largest) → pop; next in list 2: t1
```

**[4] continue 10 times or until lists drain**
```text
take t2 → take t1 → feed = [t3, t2, t1]
```

**[5] unfollow(1,2) narrows the merge**
```text
followees[1] = {1}  feed(1) = [t2] only
```

Why it works: per-user lists are append-only (monotone timestamps), so feed generation is k-way merge — a heap of (timestamp, user, index) yields O(feed_size · log k) per call, exactly the K-way merge of CLRS Ch. 6/2.3 generalizing problem 21 to k lists. Follow sets are dynamic while tweet lists are immutable — the two maps split cleanly along that line.
