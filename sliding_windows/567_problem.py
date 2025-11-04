class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Checks if s2 contains a permutation of s1 as a substring.
        
        Problem Understanding:
        - Given two strings s1 and s2
        - Return True if s2 contains a permutation of s1 as a substring
        - A permutation means any rearrangement of all characters in s1
        - For example, if s1 = "ab", then "ba", "ab" are permutations
        
        Approach:
        - Use sliding window technique with fixed window size equal to length of s1
        - Maintain frequency maps for s1 and the current window in s2
        - If the frequency maps match at any point, we found a permutation
        - Use two pointers to maintain the sliding window
        - Expand window by moving right pointer, shrink when window size exceeds s1 length
        
        Time Complexity: O(|s2|) where |s2| is the length of s2
        Space Complexity: O(1) since we're using at most 26 lowercase letters
        
        Args:
            s1: String to find permutation of
            s2: String to search in
            
        Returns:
            True if s2 contains a permutation of s1, False otherwise
        """
        if len(s1) > len(s2):
            return False
        
        # Create frequency map for s1
        s1_count = {}
        for char in s1:
            s1_count[char] = s1_count.get(char, 0) + 1
        
        # Initialize sliding window and frequency map for current window
        window_size = len(s1)
        window_count = {}
        
        # Initialize the first window
        for i in range(window_size):
            char = s2[i]
            window_count[char] = window_count.get(char, 0) + 1
        
        # Check if first window is a permutation
        if window_count == s1_count:
            return True
        
        # Slide the window through the rest of s2
        left = 0
        for right in range(window_size, len(s2)):
            # Add the new character on the right
            right_char = s2[right]
            window_count[right_char] = window_count.get(right_char, 0) + 1
            
            # Remove the character on the left
            left_char = s2[left]
            window_count[left_char] -= 1
            if window_count[left_char] == 0:
                del window_count[left_char]
            
            # Check if current window is a permutation
            if window_count == s1_count:
                return True
            
            # Move the left pointer forward
            left += 1
        
        return False

def run_check_permutation_test(s1, s2, expected, test_name):
    """
    Tests the checkInclusion function.
    
    Args:
        s1: String to find permutation of
        s2: String to search in
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.checkInclusion(s1, s2)
    
    print(f"{test_name}:")
    print(f"  Input: s1 = '{s1}', s2 = '{s2}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_check_permutation_test("ab", "eidbaooo", True, "Example 1: 'ab', 'eidbaooo' -> True ('ba' is a permutation of 'ab')")
run_check_permutation_test("ab", "eidboaoo", False, "Example 2: 'ab', 'eidboaoo' -> False")
run_check_permutation_test("adc", "dcda", True, "Edge case: 'adc', 'dcda' -> True ('cda' is a permutation of 'adc')")
run_check_permutation_test("hello", "ooolleoooleh", False, "Edge case: 'hello', 'ooolleoooleh' -> False")
run_check_permutation_test("ab", "ab", True, "Edge case: 'ab', 'ab' -> True (s1 equals s2)")
run_check_permutation_test("a", "ab", True, "Edge case: 'a', 'ab' -> True")
run_check_permutation_test("ab", "a", False, "Edge case: 'ab', 'a' -> False (s1 longer than s2)")
run_check_permutation_test("", "abc", True, "Edge case: '', 'abc' -> True (empty string is permutation of empty string)")
run_check_permutation_test("abc", "", False, "Edge case: 'abc', '' -> False (non-empty in empty)")
run_check_permutation_test("abc", "bca", True, "Edge case: 'abc', 'bca' -> True ('bca' is a permutation of 'abc')")
run_check_permutation_test("abc", "def", False, "Edge case: 'abc', 'def' -> False")
run_check_permutation_test("aab", "abab", True, "Edge case: 'aab', 'abab' -> True ('aba' contains 'aab' as permutation)")