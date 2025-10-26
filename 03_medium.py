class SolutionOpt:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_map = {}  # More descriptive name than htbl
        max_length = 0
        left = 0
        
        for right, char in enumerate(s):
            if char in char_map and char_map[char] >= left:
                left = char_map[char] + 1
            
            char_map[char] = right
            max_length = max(max_length, right - left + 1)
        
        return max_length

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == "":
            return 0
        
        htbl = {}
        length = 0
        left = 0

        for index, char in enumerate(s):
            if char in htbl:
                left = max(left, htbl[char] + 1)
            
            htbl[char] = index
            length = max(length, index - left + 1)

        return length

if __name__ == "__main__":
    sol = Solution()

    # print(sol.lengthOfLongestSubstring("abcabcbb"))
    # print(sol.lengthOfLongestSubstring("bbbbb"))
    # print(sol.lengthOfLongestSubstring("pwwkew"))
    print(sol.lengthOfLongestSubstring("abba"))