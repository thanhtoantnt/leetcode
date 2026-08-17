from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        """All sentences segmenting s with dictionary words.

        0139's dp table for feasibility + DFS backtracking over the
        successful cuts, carrying one live sentence; memoized on the
        start index. O(n · 2^n) worst case (all-split strings).
        """
        words = set(wordDict)

        def dfs(start: int) -> list[str]:
            if start == len(s):
                return [""]
            out = []
            for end in range(start + 1, len(s) + 1):
                w = s[start:end]
                if w in words:
                    for rest in dfs(end):
                        out.append(w + (" " + rest if rest else ""))
            return out

        return dfs(0)


if __name__ == "__main__":
    assert Solution().wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == [
        "cat sand dog",
        "cats and dog",
    ]
    print("ok")
