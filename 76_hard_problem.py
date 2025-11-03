class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Finds the minimum window substring of s such that every character in t is included.
        
        Problem Understanding:
        - Given two strings s and t
        - Find the minimum window in s that contains all characters of t (including duplicates)
        - Return empty string if no such window exists
        - If multiple valid windows exist, return the one with leftmost starting index
        
        Approach:
        - Use sliding window technique with two pointers
        - Maintain a frequency map of characters in t
        - Expand window by moving right pointer, shrink when valid
        - Track the minimum valid window found
        - Use counter to track how many unique characters have met required frequency
        
        Time Complexity: O(|s| + |t|) where |s| and |t| are string lengths
        Space Complexity: O(|s| + |t|) for the hash maps
        
        Args:
            s: Input string to search in
            t: Pattern string containing required characters
            
        Returns:
            Minimum window substring that contains all characters of t
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        # Create frequency map for characters in t
        t_count = {}
        for char in t:
            t_count[char] = t_count.get(char, 0) + 1
        
        # Number of unique characters in t that need to be present in window
        required = len(t_count)
        
        # Left and right pointers of sliding window
        left = right = 0
        
        # Number of unique characters in current window that match required frequency
        formed = 0
        
        # Current window character count
        window_count = {}
        
        # Result tracking: (window_length, left, right)
        result = float('inf'), None, None
        
        while right < len(s):
            # Add current character to window
            char = s[right]
            window_count[char] = window_count.get(char, 0) + 1
            
            # Check if current character's frequency matches required frequency in t
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to contract window until it ceases to be valid
            while left <= right and formed == required:
                char = s[left]
                
                # Update result if current window is smaller
                if right - left + 1 < result[0]:
                    result = (right - left + 1, left, right)
                
                # Remove leftmost character from window
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
            
            # Expand window
            right += 1
        
        # Return the minimum window substring
        return "" if result[0] == float('inf') else s[result[1]:result[2] + 1]

def run_min_window_test(s, t, expected, test_name):
    """
    Tests the minWindow function.
    
    Args:
        s: Input string to search in
        t: Pattern string containing required characters
        expected: Expected minimum window substring
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.minWindow(s, t)
    
    print(f"{test_name}:")
    print(f"  Input: s = '{s}', t = '{t}'")
    print(f"  Expected: '{expected}'")
    print(f"  Got: '{result}'")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_min_window_test("ADOBECODEBANC", "ABC", "BANC", "Example 1: 'ADOBECODEBANC', 'ABC' -> 'BANC'")
run_min_window_test("a", "a", "a", "Example 2: 'a', 'a' -> 'a'")
run_min_window_test("a", "aa", "", "Example 3: 'a', 'aa' -> '' (not enough 'a's)")
run_min_window_test("ab", "b", "b", "Edge case: 'ab', 'b' -> 'b'")
run_min_window_test("abc", "cba", "abc", "Edge case: 'abc', 'cba' -> 'abc'")
run_min_window_test("bba", "ab", "ba", "Edge case: 'bba', 'ab' -> 'ba'")
run_min_window_test("", "a", "", "Edge case: Empty s -> ''")
run_min_window_test("a", "", "", "Edge case: Empty t -> ''")
run_min_window_test("abc", "def", "", "Edge case: No match -> ''")
run_min_window_test("aab", "aab", "aab", "Edge case: s equals t -> 'aab'")
run_min_window_test("abc", "a", "a", "Edge case: Single character in t")
run_min_window_test("abca", "aa", "abca", "Edge case: Multiple same characters in t")
run_min_window_test("bba", "ab", "ba", "Edge case: Repeated characters")
run_min_window_test("abcdefghijklmnopqrstuvwxyz", "cba", "abc", "Edge case: Long string with 'cba'")
run_min_window_test("mississippi", "sippi", "sippi", "Edge case: 'mississippi', 'sippi' -> 'sippi'")