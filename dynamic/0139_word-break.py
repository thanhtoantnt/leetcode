from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        """
        Determines if the string can be segmented into a space-separated sequence of dictionary words.
        
        Problem Understanding:
        - Given a string s and a dictionary of strings wordDict
        - Return True if s can be segmented into a sequence of one or more dictionary words
        - Same word can be reused multiple times
        - Words in the dictionary don't need to be used completely
        
        Approach:
        - Use dynamic programming with dp[i] representing whether s[0:i] can be segmented
        - dp[0] = True (empty string can always be segmented)
        - For each position i, check if there's a word that ends at i and the prefix before it can be segmented
        - Use a set for faster word lookup
        - For each position, try all possible words in the dictionary
        
        Time Complexity: O(n * m * k) where n is length of s, m is number of words, k is average word length
        Space Complexity: O(n) for the dp array
        
        Args:
            s: Input string to be segmented
            wordDict: List of dictionary words
            
        Returns:
            True if string can be segmented, False otherwise
        """
        if not s or not wordDict:
            return False
        
        # Convert to set for O(1) lookup
        word_set = set(wordDict)
        
        # dp[i] = True if s[0:i] can be segmented using words in dictionary
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string can always be segmented
        
        # For each position in the string
        for i in range(1, len(s) + 1):
            # Try each word in the dictionary
            for word in word_set:
                word_len = len(word)
                
                # If current position is at least as long as the word
                # and the substring ending at current position matches the word
                # and the prefix before this word can be segmented
                if i >= word_len and s[i - word_len:i] == word and dp[i - word_len]:
                    dp[i] = True
                    break  # Found a valid segmentation, no need to check other words
        
        return dp[len(s)]

def run_word_break_test(s, wordDict, expected, test_name):
    """
    Tests the wordBreak function.
    
    Args:
        s: Input string to be segmented
        wordDict: List of dictionary words
        expected: Expected result (True/False)
        test_name: Name/description of the test case
    """
    solution = Solution()
    result = solution.wordBreak(s, wordDict)
    
    print(f"{test_name}:")
    print(f"  Input: s = '{s}', wordDict = {wordDict}")
    print(f"  Expected: {expected}")
    print(f"  Got: {result}")
    print(f"  Pass: {result == expected}")
    print()

# Run test cases
run_word_break_test("leetcode", ["leet","code"], True, "Example 1: 'leetcode', ['leet','code'] -> True")
run_word_break_test("applepenapple", ["apple","pen"], True, "Example 2: 'applepenapple', ['apple','pen'] -> True")
run_word_break_test("catsandog", ["cats","dog","sand","and","cat"], False, "Example 3: 'catsandog', ['cats','dog','sand','and','cat'] -> False")
run_word_break_test("a", ["a"], True, "Edge case: 'a', ['a'] -> True")
run_word_break_test("a", ["b"], False, "Edge case: 'a', ['b'] -> False")
run_word_break_test("", ["a"], True, "Edge case: '', ['a'] -> True (empty string)")
run_word_break_test("ab", ["a","b"], True, "Edge case: 'ab', ['a','b'] -> True")
run_word_break_test("ab", ["a"], False, "Edge case: 'ab', ['a'] -> False")
run_word_break_test("cars", ["car","ca","rs"], True, "Edge case: 'cars', ['car','ca','rs'] -> True")
run_word_break_test("cbca", ["bc","ca"], False, "Edge case: 'cbca', ['bc','ca'] -> False")
run_word_break_test("catsanddog", ["cats","dog","sand","and","cat"], False, "Edge case: 'catsanddog', ['cats','dog','sand','and','cat'] -> False")
run_word_break_test("aaaaaaa", ["aaaa","aaa"], True, "Edge case: 'aaaaaaa', ['aaaa','aaa'] -> True")