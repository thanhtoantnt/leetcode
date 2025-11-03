class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        htbl = {}
        start = 0
        longest_substring = 0

        for index in range(len(s)):
            if s[index] in htbl:
                start = max(start, htbl[s[index]] + 1)

            htbl[s[index]] = index
            longest_substring = max(longest_substring, index + 1 - start)

        return longest_substring

def run_length_test(s, expected, test_name):
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