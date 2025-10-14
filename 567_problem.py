class Solution:
    def checkInclusion(self, string1: str, string2: str) -> bool:
        find = ''.join(sorted(string1))
        # print(f"find = {find}")

        index = 0
        word_len = len(string1)
        while index + word_len <= len(string2):
            substring = string2[index:(index + word_len)]
            # print(f"substr = {substring}")
            sorted_substring = ''.join(sorted(substring))
            if sorted_substring == find:
                return True

            index = index + 1
        
        return False

class SolutionOpt:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        s1_count = [0] * 26
        s2_count = [0] * 26
        
        # Count frequencies for first window and s1
        for i in range(len(s1)):
            s1_count[ord(s1[i]) - ord('a')] += 1
            s2_count[ord(s2[i]) - ord('a')] += 1
        
        # Check first window
        if s1_count == s2_count:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character to window
            s2_count[ord(s2[i]) - ord('a')] += 1
            # Remove character that left the window
            s2_count[ord(s2[i - len(s1)]) - ord('a')] -= 1
            
            if s1_count == s2_count:
                return True
        
        return False

if __name__ == "__main__":
    sol = Solution()
    print(sol.checkInclusion("ab", "eidbaooo"))    # Expected: True
    print(sol.checkInclusion("ab", "eidboaoo"))    # Expected: False
    print(sol.checkInclusion("abc", "bbbca"))      # Expected: True
    print(sol.checkInclusion("hello", "ooolleoooleh")) # Expected: False