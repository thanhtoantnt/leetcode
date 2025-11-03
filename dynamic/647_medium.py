class Solution:
    def countSubstrings(self, s: str) -> int:
        """
        Counts the number of palindromic substrings in the given string.
        
        Problem Understanding:
        - Given a string s, return the number of palindromic substrings
        - A palindrome is a string that reads the same forwards and backwards
        - Substrings are contiguous sequences of characters
        
        Approach:
        - Use the "expand around centers" technique
        - For each possible center position, expand outward while characters match
        - Each position can be the center of odd-length palindromes (single character)
        - Each pair of adjacent positions can be the center of even-length palindromes
        - Count all valid palindromic substrings found
        
        Time Complexity: O(n²) where n is the length of string s
        Space Complexity: O(1) - only using constant extra space
        
        Args:
            s: Input string
            
        Returns:
            Number of palindromic substrings in the string
        """
        def expand_around_center(left, right):
            """Helper function to count palindromes expanding from center"""
            count = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                count += 1
                left -= 1
                right += 1
            return count
        
        total_count = 0
        
        for i in range(len(s)):
            # Count odd-length palindromes with center at i
            total_count += expand_around_center(i, i)
            
            # Count even-length palindromes with center between i and i+1
            total_count += expand_around_center(i, i + 1)
        
        return total_count

def run_count_substrings_test(s, expected, test_name):
    """
    Tests the countSubstrings function.
    
    Args:
        s: Input string
        expected: Expected number of palindromic substrings
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.countSubstrings(s)
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_count_substrings_test("abc", 3, "Example 1: 'abc' -> 3 (a, b, c)")
run_count_substrings_test("aaa", 6, "Example 2: 'aaa' -> 6 (a, a, a, aa, aa, aaa)")
run_count_substrings_test("a", 1, "Edge case: Single character 'a' -> 1")
run_count_substrings_test("ab", 2, "Edge case: Two different 'ab' -> 2 (a, b)")
run_count_substrings_test("aa", 3, "Edge case: Two same 'aa' -> 3 (a, a, aa)")
run_count_substrings_test("aba", 4, "Edge case: 'aba' -> 4 (a, b, a, aba)")
run_count_substrings_test("abcba", 7, "Edge case: 'abcba' -> 7 (a, b, c, b, a, bcb, abcba)")
run_count_substrings_test("abccba", 9, "Edge case: 'abccba' -> 9 (a, b, c, c, b, a, cc, bccb, abccba)")
run_count_substrings_test("", 0, "Edge case: Empty string -> 0")
run_count_substrings_test("racecar", 11, "Edge case: Palindrome 'racecar' -> 11")
run_count_substrings_test("abacabad", 12, "Edge case: 'abacabad' -> 12")
run_count_substrings_test("tattarrattat", 31, "Edge case: 'tattarrattat' -> 31")