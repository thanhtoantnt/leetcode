class Solution:
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
            
            if len(htbl_t) == 0:
                return True

        return False

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

            print(f"substr: {s[start:(index+1)]}")
            start = start + 1
            if self.includedSubstr(s[start:(index+1)], t):
                print(f"substr loop: {s[start:(index+1)]}")
                start = start + 1
            
            if index + 1 - (start - 1) > len(substr):
                substr = s[(start - 1):(index+1)]
            
            index = index + 1
        
        return substr

if __name__ == "__main__":
    sol = Solution()
    print(sol.minWindow("ADOBECODEBANC", "ABC"))  # Expected: "BANC"
    # print(sol.minWindow("a", "a"))                # Expected: "a"
    # print(sol.minWindow("a", "aa"))               # Expected: ""
    # print(sol.minWindow("ab", "a"))               # Expected: "a"
    # print(sol.minWindow("abc", "ac"))             # Expected: "abc"