from typing import List

# Timeout
class SolutionSlow:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if s == "":
            return True

        for word in wordDict:
            if len(word) > len(s):
                continue

            if s[:len(word)] == word:
                if self.wordBreak(s[len(word):], wordDict) == True:
                    return True

        return False

class SolutionOpt:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        n = len(s)
        
        # dp[i] means s[0:i] can be segmented into words from wordDict
        dp = [False] * (n + 1)
        dp[0] = True  # empty string can be segmented
        
        for i in range(1, n + 1):
            for j in range(i):
                # Check if s[0:j] can be segmented and s[j:i] is in dictionary
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break  # no need to check other j's for this i
        
        return dp[n]

if __name__ == "__main__":
    sol = SolutionOpt()

    print(sol.wordBreak("cars", ["car","ca","rs"]))
    # # Test case 1
    # s1 = "leetcode"
    # wordDict1 = ["leet", "code"]
    # print(sol.wordBreak(s1, wordDict1))  # Expected: True
    
    # # Test case 2
    # s2 = "applepenapple"
    # wordDict2 = ["apple", "pen"]
    # print(sol.wordBreak(s2, wordDict2))  # Expected: True
    
    # # Test case 3
    # s3 = "catsandog"
    # wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    # print(sol.wordBreak(s3, wordDict3))  # Expected: False
    
    # # Test case 4
    # s4 = "aaaaaaa"
    # wordDict4 = ["aaaa", "aaa"]
    # print(sol.wordBreak(s4, wordDict4))  # Expected: True
    
    # # Test case 5
    # s5 = "abcd"
    # wordDict5 = ["a", "abc", "b", "cd"]
    # print(sol.wordBreak(s5, wordDict5))  # Expected: True