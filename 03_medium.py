

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