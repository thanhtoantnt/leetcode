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
            