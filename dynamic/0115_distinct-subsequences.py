class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        """Count distinct subsequences of s equal to t.

        dp[i][j] = ways to form t[:j] from s[:i]. Match at the ends:
        use s[i-1] (dp[i-1][j-1]) or skip it (dp[i-1][j]); mismatch:
        only skip. O(m·n) time, O(n) space rolling.
        """
        m, n = len(s), len(t)
        dp = [1] + [0] * n  # empty t formable in exactly 1 way
        for i in range(1, m + 1):
            for j in range(n, 0, -1):  # reverse so dp[j-1] is still row i-1
                if s[i - 1] == t[j - 1]:
                    dp[j] += dp[j - 1]
        return dp[n]


if __name__ == "__main__":
    assert Solution().numDistinct("rabbbit", "rabbit") == 3
    assert Solution().numDistinct("babgbag", "bag") == 5
    print("ok")
