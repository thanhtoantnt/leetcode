
class Solution:
    def diffCharsLen(self, hash_table):
        max_num = 0
        diff = 0

        for _,value in hash_table.items():
            diff = diff + value
            if value > max_num:
                max_num = value
        
        # diff now is end + 1 - start

        return diff - max_num
        # diffCharsLen is similar to (end + 1 - start) - max_num
        # because except for the character with hash_table[char] = max_num
        # other characters has the diff = end - start + 1 - max_num
        # e.g., aaabbcc => sum - max_nu

    def characterReplacement(self, string: str, k: int) -> int:
        if string == "":
            return 0
        
        start = 0
        longest = 0
        hash_table = {}

        for index, char in enumerate(string):
            hash_table[char] = hash_table.get(char, 0) + 1

            while self.diffCharsLen(hash_table) > k:
                hash_table[string[start]] = hash_table.get(string[start]) - 1
                start = start + 1
            
            longest = max(longest, index - start  + 1)
            
        return longest

class SolutionOpt:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = {}
        max_freq = 0
        start = 0
        longest = 0
        
        for end in range(len(s)):
            # Update frequency
            freq[s[end]] = freq.get(s[end], 0) + 1
            max_freq = max(max_freq, freq[s[end]])
            
            # Check if window is valid
            while (end - start + 1) - max_freq > k:
                freq[s[start]] -= 1
                start += 1
            
            longest = max(longest, end - start + 1)
        
        return longest

class Solution1:
    def diffCharsLen(self, string):
        if string == "":
            return 0

        hash_table = {}
        max_occurrent = 0

        for char in string:
            hash_table[char] = hash_table.get(char, 0) + 1
            if hash_table[char] > max_occurrent:
                max_occurrent = hash_table[char]
        
        diff = 0

        for _,value in hash_table.items():
            diff = diff + value

        diff = diff - max_occurrent
        return diff

    def characterReplacement(self, string: str, k: int) -> int:
        if string == "":
            return 0
        
        start = 0
        longest = 0

        for index, char in enumerate(string):
            if index == 0:
                longest = 1
                continue

            while self.diffCharsLen(string[start:index + 1]) > k:
                start = start + 1
            
            if index - start + 1 > longest:
                longest = index - start + 1
            
        return longest

if __name__ == "__main__":
    # Test cases
    sol = Solution()
    print(sol.characterReplacement("ABAB", 2))        # Expected: 4
    print(sol.characterReplacement("AABABBA", 1))     # Expected: 4
    print(sol.characterReplacement("AAAA", 2))        # Expected: 4
    print(sol.characterReplacement("AAAB", 0))        # Expected: 3
    print(sol.characterReplacement("AABA", 0))        # Expected: 2
                




