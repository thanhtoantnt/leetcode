class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Finds the length of the longest substring without repeating characters.
        
        Approach:
        - Use sliding window technique with a hash table
        - Maintain a window [start, current_index] with no repeating characters
        - When a duplicate character is found, move start pointer to right of previous occurrence
        - Keep track of maximum window size seen so far
        
        Time Complexity: O(n) where n is the length of the string
        Space Complexity: O(min(m,n)) where m is the size of the character set
        """
        # Hash table to store the most recent index of each character
        htbl = {}
        
        # Start of the current window (left boundary)
        start = 0
        
        # Length of the longest substring found so far
        longest_substring = 0

        for index in range(len(s)):
            # If current character was seen before and is within current window
            if s[index] in htbl:
                # Move start to the right of the previous occurrence to avoid duplicates
                # Use max to ensure start doesn't move backward
                start = max(start, htbl[s[index]] + 1)

            # Update the most recent index of current character
            htbl[s[index]] = index
            
            # Update the maximum length if current window is larger
            longest_substring = max(longest_substring, index + 1 - start)

        return longest_substring

def run_length_test(s, expected, test_name):
    """
    Tests the lengthOfLongestSubstring function.
    
    Args:
        s: Input string to analyze
        expected: Expected length of longest substring without repeating characters
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.lengthOfLongestSubstring(s)
    
    print(f"{test_name}:")
    print(f"  Input: '{s}'")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_length_test("abcabcbb", 3, "Example 1: abcabcbb -> abc")
run_length_test("bbbbb", 1, "Example 2: bbbbb -> b") 
run_length_test("pwwkew", 3, "Example 3: pwwkew -> wke")
run_length_test("", 0, "Edge case: empty string")
run_length_test(" ", 1, "Edge case: single space")
run_length_test("abcdef", 6, "Edge case: all unique")
run_length_test("aab", 2, "Edge case: duplicate at start")
run_length_test("abba", 2, "Edge case: palindrome pattern")
run_length_test("dvdf", 3, "Edge case: dvdf -> vdf")
run_length_test("anviaj", 5, "Edge case: anviaj -> nviaj")
run_length_test("tmmzuxt", 5, "Edge case: tmmzuxt -> mzuxt")
run_length_test("abcdefghijklmnopqrstuvwxyz", 26, "Edge case: all letters")