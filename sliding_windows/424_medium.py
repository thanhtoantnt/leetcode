class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        Finds the length of the longest substring that can be made with at most k replacements.
        
        Problem Understanding:
        - Given a string s and integer k
        - Choose any character and replace it with another uppercase character
        - Perform at most k replacements
        - Find the length of the longest substring containing the same letter
        
        Approach:
        - Use sliding window technique
        - Maintain a window [start, end] where we can make all characters the same with ≤ k changes
        - Track frequency of characters in current window
        - The window is valid if (window_size - max_freq_char) <= k
        - If invalid, shrink window from left until valid again
        
        Time Complexity: O(n) where n is the length of string s
        Space Complexity: O(1) - at most 26 characters in frequency map
        
        Args:
            s: Input string of uppercase English letters
            k: Maximum number of character replacements allowed
            
        Returns:
            Length of the longest substring with same characters after at most k replacements
        """
        # Frequency map to track character counts in current window
        freq = {}
        
        # Maximum frequency of any character in current window
        max_freq = 0
        
        # Start pointer of sliding window
        start = 0
        
        # Length of the longest valid substring found
        longest = 0
        
        # Expand window by moving end pointer
        for end in range(len(s)):
            # Add current character to frequency map
            freq[s[end]] = freq.get(s[end], 0) + 1
            
            # Update maximum frequency (current character might have higher frequency)
            max_freq = max(max_freq, freq[s[end]])
            
            # Shrink window while it's invalid
            # Window is invalid if we need more than k replacements
            # (window_size - max_freq_char) represents number of replacements needed
            while (end - start + 1) - max_freq > k:
                # Remove leftmost character from window
                freq[s[start]] -= 1
                # Update max_freq - we need to recalculate since we removed a character
                # This is O(26) = O(1) since at most 26 uppercase letters
                max_freq = max(freq.values())  # Recalculate max frequency
                start += 1  # Move start pointer right to shrink window
            
            # Update longest valid substring length
            longest = max(longest, end - start + 1)
        
        return longest

def run_replacement_test(s, k, expected, test_name):
    """
    Tests the characterReplacement function.
    
    Args:
        s: Input string
        k: Maximum replacements allowed
        expected: Expected longest substring length
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.characterReplacement(s, k)
    
    print(f"{test_name}:")
    print(f"  Input: s = '{s}', k = {k}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_replacement_test("ABAB", 2, 4, "Example 1: 'ABAB', k=2 -> 4 (replace both A's or both B's)")
run_replacement_test("AABABBA", 1, 4, "Example 2: 'AABABBA', k=1 -> 4 (replace B with A in AABA)")
run_replacement_test("AAAA", 2, 4, "Edge case: All same characters")
run_replacement_test("ABCD", 0, 1, "Edge case: No replacements allowed")
run_replacement_test("A", 1, 1, "Edge case: Single character")
run_replacement_test("", 1, 0, "Edge case: Empty string")
run_replacement_test("ABCDEF", 3, 4, "Edge case: All different, k=3")
run_replacement_test("AAABBBCCC", 2, 5, "Edge case: 'AAABBBCCC', k=2 -> 5 (change 2 B's to A's or A's to B's)")
run_replacement_test("ABBB", 2, 4, "Edge case: 'ABBB', k=2 -> 4 (change A to B)")
run_replacement_test("BAAAB", 2, 5, "Edge case: 'BAAAB', k=2 -> 5 (change B's to A's)")
run_replacement_test("ABCCCD", 2, 4, "Edge case: 'ABCCCD', k=2 -> 4 (change A and D to C)")
run_replacement_test("ABCDE", 4, 5, "Edge case: 'ABCDE', k=4 -> 5 (change 4 to match 1)")