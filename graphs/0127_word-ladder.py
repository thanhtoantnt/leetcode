from collections import deque
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """Shortest transformation ladder (one letter per step, every
        intermediate must be a word). BFS on the implicit wildcard graph:
        word → patterns like h*t — two words sharing a pattern are
        adjacent. O(n·L²).
        """
        if endWord not in wordList:
            return 0
        L = len(beginWord)
        adj: dict[str, list[str]] = {}
        for w in wordList:
            for i in range(L):
                adj.setdefault(w[:i] + "*" + w[i + 1:], []).append(w)
        q = deque([(beginWord, 1)])
        seen = {beginWord}
        while q:
            w, dist = q.popleft()
            for i in range(L):
                pat = w[:i] + "*" + w[i + 1:]
                for nxt in adj.pop(pat, []):
                    if nxt == endWord:
                        return dist + 1
                    if nxt not in seen:
                        seen.add(nxt)
                        q.append((nxt, dist + 1))
        return 0


if __name__ == "__main__":
    words = ["hot", "dot", "dog", "lot", "log", "cog"]
    assert Solution().ladderLength("hit", "cog", words) == 5
    assert Solution().ladderLength("hit", "cog", ["hot", "dot", "dog", "lot", "log"]) == 0
    print("ok")
