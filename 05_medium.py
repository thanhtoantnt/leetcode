class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return 0
        
        n = len(s)

        dp = [[False] * n for _ in range(n)]

        for index in range(len(s)):
            dp[index][index] = True

        start = 0
        max_len = 1
        
        for length in range(2, n + 1):
            # i is the start of substrings
            for i in range(n - length + 1):
                j = i + length - 1 # ending index: length = j + 1 - i

                if s[i] == s[j]:
                    if length == 2 or dp[i+1][j-1]:
                        dp[i][j] = True

                        if length > max_len:
                            max_len = length
                            start = i

        return s[start:(start+max_len)]

if __name__ == "__main__":
    sol = Solution()
    print(sol.longestPalindrome("aaaa"))  # Expected: "aaa"
    # print(sol.longestPalindrome("cbbd"))   # Expected: "bb"
    # print(sol.longestPalindrome("a"))      # Expected: "a"
    # print(sol.longestPalindrome("ac"))     # Expected: "a" or "c"
    # print(sol.longestPalindrome("racecar")) # Expected: "racecar"

                        
