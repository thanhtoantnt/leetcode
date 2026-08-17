class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        """
        Finds the length of the longest common subsequence between two strings.
        
        Problem Understanding:
        - Given two strings text1 and text2
        - Return the length of their longest common subsequence (LCS)
        - A subsequence is a sequence derived from another sequence by deleting some elements 
          without changing the order of remaining elements
        - LCS is the longest sequence that appears in both strings in the same relative order
        
        Approach:
        - Use dynamic programming with 2D array
        - dp[i][j] = length of LCS of text1[0:i] and text2[0:j]
        - If characters match: dp[i][j] = dp[i-1][j-1] + 1
        - If characters don't match: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        - Base case: dp[0][j] = 0 and dp[i][0] = 0 (empty string has LCS of 0)
        
        Time Complexity: O(m * n) where m and n are lengths of text1 and text2
        Space Complexity: O(m * n) for the DP table
        
        Args:
            text1: First input string
            text2: Second input string
            
        Returns:
            Length of the longest common subsequence
        """
        m, n = len(text1), len(text2)
        
        # Create DP table: dp[i][j] = LCS length of text1[0:i] and text2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    # Characters match, extend LCS from previous diagonal
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    # Characters don't match, take maximum from left or top
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]

def run_lcs_test(text1, text2, expected, test_name):
    """
    Tests the longestCommonSubsequence function.
    
    Args:
        text1: First input string
        text2: Second input string
        expected: Expected length of LCS
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.longestCommonSubsequence(text1, text2)
    
    print(f"{test_name}:")
    print(f"  Input: text1 = '{text1}', text2 = '{text2}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_lcs_test("abcde", "ace", 3, "Example 1: 'abcde', 'ace' -> 3 ('ace')")
run_lcs_test("abc", "abc", 3, "Example 2: 'abc', 'abc' -> 3 ('abc')")
run_lcs_test("abc", "def", 0, "Example 3: 'abc', 'def' -> 0 (no common subsequence)")
run_lcs_test("abc", "a", 1, "Edge case: 'abc', 'a' -> 1 ('a')")
run_lcs_test("", "abc", 0, "Edge case: '', 'abc' -> 0 (empty string)")
run_lcs_test("abc", "", 0, "Edge case: 'abc', '' -> 0 (empty string)")
run_lcs_test("", "", 0, "Edge case: '', '' -> 0 (both empty)")
run_lcs_test("abcdgh", "aedfhr", 3, "Edge case: 'abcdgh', 'aedfhr' -> 3 ('adh')")
run_lcs_test("pmjghexybyrgzczy", "hafcdqbgncrczhqd", 4, "Edge case: Longer strings -> 4")
run_lcs_test("ab", "ba", 1, "Edge case: 'ab', 'ba' -> 1 ('a' or 'b')")
run_lcs_test("bsbininm", "jmjkbkjkv", 1, "Edge case: 'bsbininm', 'jmjkbkjkv' -> 1 ('b' or 'j' or 'k' or 'm')")
run_lcs_test("oxcpqrsvwf", "shmtulqrypy", 2, "Edge case: 'oxcpqrsvwf', 'shmtulqrypy' -> 2")