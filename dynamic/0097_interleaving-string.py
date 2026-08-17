class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        """
        Determines if s3 is formed by an interleaving of s1 and s2.
        
        Problem Understanding:
        - Given three strings s1, s2, and s3
        - Return True if s3 is formed by interleaving s1 and s2
        - Interleaving means s1 and s2 are split into substrings and alternately concatenated
        - For example: s1 = "aab", s2 = "axy", possible interleaving: "aaxaby", "aaaxby", etc.
        
        Approach:
        - Use dynamic programming with 2D array
        - dp[i][j] = True if s3[0:i+j] is an interleaving of s1[0:i] and s2[0:j]
        - Base case: dp[0][0] = True (empty strings form empty interleaving)
        - For first row: dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        - For first column: dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        - For other cells: dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or 
                                   (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        Time Complexity: O(m * n) where m and n are lengths of s1 and s2
        Space Complexity: O(m * n) for the DP table
        
        Args:
            s1: First input string
            s2: Second input string
            s3: Target string to check for interleaving
            
        Returns:
            True if s3 is an interleaving of s1 and s2, False otherwise
        """
        m, n, k = len(s1), len(s2), len(s3)
        
        # Check if lengths match (necessary condition)
        if m + n != k:
            return False
        
        # Create DP table: dp[i][j] = True if s3[0:i+j] is interleaving of s1[0:i] and s2[0:j]
        dp = [[False] * (n + 1) for _ in range(m + 1)]
        
        # Base case: empty strings
        dp[0][0] = True
        
        # Fill first row (s1 is empty)
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        
        # Fill first column (s2 is empty)
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        
        # Fill the rest of the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                # Check if we can form interleaving by taking character from s1 or s2
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                           (dp[i][j-1] and s2[j-1] == s3[i+j-1])
        
        return dp[m][n]

def run_interleave_test(s1, s2, s3, expected, test_name):
    """
    Tests the isInterleave function.
    
    Args:
        s1: First input string
        s2: Second input string
        s3: Target string to check
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.isInterleave(s1, s2, s3)
    
    print(f"{test_name}:")
    print(f"  Input: s1 = '{s1}', s2 = '{s2}', s3 = '{s3}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_interleave_test("aab", "axy", "aaxaby", True, "Example 1: 'aab', 'axy', 'aaxaby' -> True")
run_interleave_test("aabcc", "dbbca", "aadbbcbcac", True, "Example 2: 'aabcc', 'dbbca', 'aadbbcbcac' -> True")
run_interleave_test("aabcc", "dbbca", "aadbbbaccc", False, "Example 3: 'aabcc', 'dbbca', 'aadbbbaccc' -> False")
run_interleave_test("", "", "", True, "Edge case: All empty strings -> True")
run_interleave_test("", "a", "a", True, "Edge case: '', 'a', 'a' -> True")
run_interleave_test("a", "", "a", True, "Edge case: 'a', '', 'a' -> True")
run_interleave_test("a", "b", "ab", True, "Edge case: 'a', 'b', 'ab' -> True")
run_interleave_test("a", "b", "ba", True, "Edge case: 'a', 'b', 'ba' -> True")
run_interleave_test("a", "b", "abc", False, "Edge case: 'a', 'b', 'abc' -> False (length mismatch)")
run_interleave_test("ab", "bc", "babc", True, "Edge case: 'ab', 'bc', 'babc' -> True")
run_interleave_test("abc", "def", "adbecf", True, "Edge case: 'abc', 'def', 'adbecf' -> True")
run_interleave_test("ab", "cd", "acbd", True, "Edge case: 'ab', 'cd', 'acbd' -> True")