class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_hash_table = {}
        t_hash_table = {}
        for char in s:
            if char in s_hash_table:
                s_hash_table[char] = s_hash_table[char]  + 1

            else:
                s_hash_table[char] = 1

        for char in t:
            t_hash_table[char] = t_hash_table.get(char, 0) + 1

        for char, value in s_hash_table.items():
            if char not in t_hash_table:
                return False
            elif t_hash_table[char] != value:
                return False
        
        return True

# Test the solution
if __name__ == "__main__":
    sol = Solution()
    print(sol.isAnagram("anagram", "nagaram"))  # True
    print(sol.isAnagram("rat", "car"))          # False  
    print(sol.isAnagram("abc", "abcd"))         # False (length check catches this)
    print(sol.isAnagram("aacc", "ccac"))        # False (different counts)