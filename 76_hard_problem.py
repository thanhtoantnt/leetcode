from collections import defaultdict

# Pass tests but time limit exceeded
class Solution1:
    def includedSubstr(self, s:str, t:str):
        if len(s) < len(t):
            return False
        
        htbl_t = {}

        for char in t:
            htbl_t[char] = htbl_t.get(char, 0) + 1
        
        for char in s:
            if char in htbl_t:
                htbl_t[char] = htbl_t.get(char) - 1
                if htbl_t[char] == 0:
                    htbl_t.pop(char)

        ret = len(htbl_t) == 0
        # print(f"s = {s}, t = {t}, ret = {ret}")
        return ret

    def minWindow(self, s: str, t: str) -> str:
        substr = ""
        # first find the window
        start = 0
        index = 0
        while index < len(s):
            if not self.includedSubstr(s[start:(index+1)], t):
                index = index + 1
                continue
            
            # a window is found
            # minimize the windows

            # print(f"substr: {s[start:(index+1)]}")
            start = start + 1
            while self.includedSubstr(s[start:(index+1)], t):
                # print(f"substr loop: {s[start:(index+1)]}")
                start = start + 1
            
            if substr == "" or index + 1 - (start - 1) < len(substr):
                substr = s[(start - 1):(index+1)]
            
            index = index + 1
        
        return substr

# pass Leetcode
class Solution:
    def check_included(self, hash_table):
        return all(value <= 0 for value in hash_table.values())

    def minWindow(self, s: str, t: str) -> str:
        substr = ""
        htbl_t = {}

        for char in t:
            htbl_t[char] = htbl_t.get(char, 0) + 1

        # first find the window
        start = 0
        for index, char in enumerate(s):
            if char in htbl_t:
                htbl_t[char] = htbl_t.get(char) - 1
            
            if not self.check_included(htbl_t):
                continue
            
            # print(f"start = {start}, index = {index}")
            start = start + 1
            if s[start - 1] in htbl_t:
                htbl_t[s[start - 1]] = htbl_t.get(s[start - 1]) + 1

            while self.check_included(htbl_t):
                # print(f"loop: start = {start}, index = {index}")

                start = start + 1
                if s[start - 1] in htbl_t:
                    htbl_t[s[start - 1]] = htbl_t.get(s[start - 1]) + 1
            
            if substr == "" or index + 1 - (start - 1) < len(substr):
                substr = s[(start - 1):(index+1)]
                # print(f"substr = {substr}")
            
            index = index + 1
        
        return substr

# optimal solution
class SolutionOpt:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t:
            return ""
        
        # Frequency count for characters in t
        t_count = defaultdict(int)
        for char in t:
            t_count[char] += 1
        
        # Variables to track the window
        left = 0
        min_left = 0
        min_len = float('inf')
        required = len(t_count)  # Number of unique characters we need to match
        formed = 0  # Number of unique characters currently matched
        
        # Frequency count for current window
        window_count = defaultdict(int)
        
        for right, char in enumerate(s):
            # Add current character to window
            window_count[char] += 1
            
            # Check if current character completes a requirement
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Try to shrink the window while it's still valid
            while left <= right and formed == required:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # Remove left character from window
                left_char = s[left]
                window_count[left_char] -= 1
                
                # Check if removing broke a requirement
                if left_char in t_count and window_count[left_char] < t_count[left_char]:
                    formed -= 1
                
                left += 1
        
        return "" if min_len == float('inf') else s[min_left:min_left + min_len]

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
    # print(sol.minWindow("a", "a"))                # Expected: "a"
    # print(sol.minWindow("a", "aa"))               # Expected: ""
    # print(sol.minWindow("ab", "a"))               # Expected: "a"
    # print(sol.minWindow("abc", "ac"))             # Expected: "abc"