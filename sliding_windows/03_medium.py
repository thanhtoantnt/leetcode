class SolutionOpt:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        
        Problem Understanding:
        - Given a string s
        - Find the length of the longest substring with all unique characters
        - A substring is a contiguous sequence of characters
        
        Approach:
        - Use sliding window technique with a hash map
        - Maintain a window [left, right] with no repeating characters
        - Hash map stores the most recent index of each character
        - When a duplicate is found within current window, move left pointer
        - Keep track of maximum window size seen so far
        
        Time Complexity: O(n) where n is the length of string s
        Space Complexity: O(min(m,n)) where m is the size of the character set
        
        Args:
            s: Input string
            
        Returns:
            Length of the longest substring without repeating characters
        """
        # Hash map to store the most recent index of each character
        char_map = {}
        
        # Length of the longest substring found so far
        max_length = 0
        
        # Left pointer of the sliding window
        left = 0
        
        # Expand window by moving right pointer
        for right, char in enumerate(s):
            # If current character was seen before and is within current window
            # Move left pointer to right of previous occurrence to avoid duplicates
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            # Update the most recent index of current character
            char_map[char] = right
            
            # Update the maximum length if current window is larger
            max_length = max(max_length, right - left + 1)
        
        return max_length

def run_substring_test(s, expected, test_name):
    """
    Tests the lengthOfLongestSubstring function.
    
    Args:
        s: Input string to analyze
        expected: Expected length of longest substring without repeating characters
        test_name: Name/description of the test case
    """
    solution = SolutionOpt()
    result = solution.lengthOfLongestSubstring(s)
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_substring_test("abcabcbb", 3, "Example 1: 'abcabcbb' -> 'abc' (length 3)")
run_substring_test("bbbbb", 1, "Example 2: 'bbbbb' -> 'b' (length 1)")
run_substring_test("pwwkew", 3, "Example 3: 'pwwkew' -> 'wke' (length 3)")
run_substring_test("", 0, "Edge case: Empty string")
run_substring_test(" ", 1, "Edge case: Single space")
run_substring_test("abcdef", 6, "Edge case: All unique characters")
run_substring_test("aab", 2, "Edge case: Duplicate at start")
run_substring_test("abba", 2, "Edge case: Palindrome pattern")
run_substring_test("dvdf", 3, "Edge case: 'dvdf' -> 'vdf' (length 3)")
run_substring_test("anviaj", 5, "Edge case: 'anviaj' -> 'nviaj' (length 5)")
run_substring_test("tmmzuxt", 5, "Edge case: 'tmmzuxt' -> 'mzuxt' (length 5)")
run_substring_test("abcdefghijklmnopqrstuvwxyz", 26, "Edge case: All letters")
run_substring_test("abccba", 3, "Edge case: 'abccba' -> 'abc' or 'cba' (length 3)")
run_substring_test("a", 1, "Edge case: Single character")
run_substring_test("au", 2, "Edge case: Two unique characters")