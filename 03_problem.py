class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:
        if string == []:
            return 0

        # windows
        start = 0
        end = 0
        longest = 0

        # hash_table of the character in the input string
        hash_table = {}

        for index, char in enumerate(string):
            if char not in hash_table:
                # end is index
                end = index

                # add to the hash table
                hash_table[char] = index
            
            else:
                # char is in the window
                if hash_table[char] >= start:
                    start = hash_table[char] + 1
                end = index

                # update the hash table
                hash_table[char] = index

            if end - start + 1 > longest:
                longest = end - start + 1
                    
           # print(f"start = {start}, end = {end}, longest = {longest}")
        return longest

class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:  # More Pythonic than s == []
            return 0

        start = 0
        longest = 0
        char_map = {}  # Slightly clearer name than hash_table
        
        for end, char in enumerate(s):
            # If duplicate found within current window, move start
            if char in char_map and char_map[char] >= start:
                start = char_map[char] + 1
            
            # Always update character's position
            char_map[char] = end
            
            # Update longest
            current_length = end - start + 1
            longest = max(longest, current_length)
        
        return longest

if __name__ == "__main__":
    # Test cases
    sol = Solution()
    # print(sol.lengthOfLongestSubstring("abcabcbb"))  # Expected: 3
    # print(sol.lengthOfLongestSubstring("bbbbbb"))     # Expected: 1
    # print(sol.lengthOfLongestSubstring("pwwkew"))    # Expected: 3
    # print(sol.lengthOfLongestSubstring(""))          # Expected: 0
    # print(sol.lengthOfLongestSubstring(" "))         # Expected: 1
    # print(sol.lengthOfLongestSubstring("dvdf"))      # Expected: 3
    print(sol.lengthOfLongestSubstring("abba"))      # Expected: 2