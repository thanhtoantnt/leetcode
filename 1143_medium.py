class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        
        # dp[i][j] = LCS length of text1[0:i] and text2[0:j]SS
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # Characters match - extend the subsequence
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # Characters don't match - take the best of skipping one character
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestCommonSubsequence("abcde", "ace"))  # Expected: 3
    # print(sol.longestCommonSubsequence("abc", "abc"))    # Expected: 3
    # print(sol.longestCommonSubsequence("abc", "def"))    # Expected: 0
    # print(sol.longestCommonSubsequence("bsbininm", "jmjkbkjkv"))  # Expected: 1