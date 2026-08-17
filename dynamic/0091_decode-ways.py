class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Returns the number of ways to decode a string of digits based on letter-number mapping.
        
        Problem Understanding:
        - Mapping: 'A' -> "1", 'B' -> "2", ..., 'Z' -> "26"
        - Given a string of digits, return number of ways to decode it
        - Leading zeros are not allowed (e.g., "06" is invalid, must be "6")
        - A valid decoding cannot have leading zeros except for "0" itself which is invalid
        
        Approach:
        - Use Dynamic Programming with 1D array
        - dp[i] = number of ways to decode s[0:i]
        - At each position, consider:
          1. Single digit decoding (if digit != '0')
          2. Two digit decoding (if 10 <= number <= 26)
        - Base cases: dp[0] = 1 (empty string has 1 way), dp[1] = 1 if first char is valid
        - Recurrence: dp[i] = dp[i-1] (if single valid) + dp[i-2] (if two valid)
        
        Time Complexity: O(n) where n is the length of string s
        Space Complexity: O(n) for the DP array (can be optimized to O(1))
        
        Args:
            s: String of digits to decode
            
        Returns:
            Number of ways to decode the string
        """
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        # dp[i] = number of ways to decode s[0:i]
        dp = [0] * (n + 1)
        
        # Base cases
        dp[0] = 1  # Empty string has 1 way to decode
        dp[1] = 1  # First character can be decoded if not '0'
        
        for i in range(2, n + 1):
            # Single digit decoding: s[i-1]
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            
            # Two digit decoding: s[i-2:i]
            two_digit = int(s[i-2:i])
            if 10 <= two_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]

def run_decoding_test(s, expected, test_name):
    """
    Tests the numDecodings function.
    
    Args:
        s: Input string of digits to decode
        expected: Expected number of decoding ways
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.numDecodings(s)
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_decoding_test("12", 2, "Example 1: '12' -> 2 ways (AB or L)")
run_decoding_test("226", 3, "Example 2: '226' -> 3 ways (BZ, VF, BBF)")
run_decoding_test("06", 0, "Example 3: '06' -> 0 ways (leading zero not allowed)")
run_decoding_test("123", 3, "Edge case: '123' -> 3 ways (AW, ABC, LC)")
run_decoding_test("10", 1, "Edge case: '10' -> 1 way (J)")
run_decoding_test("20", 1, "Edge case: '20' -> 1 way (T)")
run_decoding_test("27", 1, "Edge case: '27' -> 1 way (BG)")
run_decoding_test("0", 0, "Edge case: '0' -> 0 ways (invalid)")
run_decoding_test("1", 1, "Edge case: '1' -> 1 way (A)")
run_decoding_test("21", 2, "Edge case: '21' -> 2 ways (U, BA)")
run_decoding_test("11106", 2, "Edge case: '11106' -> 2 ways (AAJF, KJF)")
run_decoding_test("1111", 5, "Edge case: '1111' -> 5 ways (AAAA, KAA, AKA, AAK, KK)")
run_decoding_test("2611055971756562", 4, "Edge case: Complex string")
run_decoding_test("101", 1, "Edge case: '101' -> 1 way (JA)")
run_decoding_test("230", 0, "Edge case: '230' -> 0 ways (0 cannot be decoded alone)")