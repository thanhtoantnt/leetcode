class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """Levenshtein edit distance: min single-char insert/delete/replace
        operations turning word1 into word2.

        dp[i][j] = distance between the first i chars of word1 and first j of
        word2. Matching tails pull from the diagonal; a mismatch is 1 plus the
        best of insert (left), delete (up), replace (diagonal).
        O(m·n) time and space.
        """
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            dp[i][0] = i  # delete all i chars
        for j in range(n + 1):
            dp[0][j] = j  # insert all j chars
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
        return dp[m][n]


if __name__ == "__main__":
    assert Solution().minDistance("horse", "ros") == 3
    assert Solution().minDistance("intention", "execution") == 5
    print("ok")
