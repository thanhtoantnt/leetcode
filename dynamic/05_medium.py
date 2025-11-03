class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Finds the longest palindromic substring in the given string.
        
        Problem Understanding:
        - Given a string s
        - Find the longest contiguous substring that reads the same forwards and backwards
        - Return the actual palindromic substring (not just length)
        
        Approach:
        - Use 2D Dynamic Programming
        - dp[i][j] = True if substring s[i:j+1] is a palindrome
        - Base case: All single characters are palindromes
        - Recurrence: dp[i][j] = (s[i] == s[j]) and dp[i+1][j-1]
        - Process substrings by increasing length
        - Track the start position and length of the longest palindrome found
        
        Time Complexity: O(n²) where n is the length of string s
        Space Complexity: O(n²) for the DP table
        
        Args:
            s: Input string
            
        Returns:
            The longest palindromic substring
        """
        if len(s) == 0:
            return ""
        
        n = len(s)
        
        # 2D DP table: dp[i][j] = True if s[i:j+1] is palindrome
        dp = [[False] * n for _ in range(n)]

        # All single characters are palindromes
        for index in range(len(s)):
            dp[index][index] = True

        # Track the start position and length of longest palindrome
        start = 0
        max_len = 1
        
        # Process substrings by increasing length (2 to n)
        for length in range(2, n + 1):
            # i is the start of substrings of current length
            for i in range(n - length + 1):
                # j is the end of substring
                j = i + length - 1  # length = j + 1 - i

                # Check if current substring is palindrome
                if s[i] == s[j]:
                    # For length 2: both characters must be same
                    # For length > 2: outer chars same AND inner substring is palindrome
                    if length == 2 or dp[i+1][j-1]:
                        dp[i][j] = True

                        # Update longest palindrome if current is longer
                        if length > max_len:
                            max_len = length
                            start = i

        # Return the longest palindromic substring
        return s[start:(start+max_len)]

def run_palindrome_test(s, expected, test_name):
    """
    Tests the longestPalindrome function.
    
    Args:
        s: Input string
        expected: Expected longest palindromic substring
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.longestPalindrome(s)
    
    # Verify result is actually a palindrome
    is_palindrome = result == result[::-1]
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: '{expected}'")
    print(f"  Got: '{result}'")
    print(f"  Is palindrome: {is_palindrome}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_palindrome_test("babad", "bab", "Example 1: 'babad' -> 'bab' or 'aba'")
run_palindrome_test("cbbd", "bb", "Example 2: 'cbbd' -> 'bb'")
run_palindrome_test("a", "a", "Edge case: Single character")
run_palindrome_test("ac", "a", "Edge case: Two different characters")
run_palindrome_test("", "", "Edge case: Empty string")
run_palindrome_test("racecar", "racecar", "Edge case: Entire string is palindrome")
run_palindrome_test("abcdef", "a", "Edge case: No palindromes > 1")
run_palindrome_test("aabbaa", "aabbaa", "Edge case: Entire string is palindrome")
run_palindrome_test("abacabad", "abacaba", "Edge case: 'abacabad' -> 'abacaba'")
run_palindrome_test("noon high it is", "noon", "Edge case: 'noon high it is' -> 'noon'")
run_palindrome_test("12321", "12321", "Edge case: Numeric palindrome")
run_palindrome_test("abaxyzzyxf", "xyzzyx", "Edge case: 'abaxyzzyxf' -> 'xyzzyx'")
run_palindrome_test("abccba", "abccba", "Edge case: Even length palindrome")
run_palindrome_test("abccbx", "bccb", "Edge case: Middle palindrome")
run_palindrome_test("tattarrattat", "tattarrattat", "Edge case: Long palindrome")