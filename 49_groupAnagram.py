from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_hash_table = {}
        t_hash_table = {}
        for char in s:
            if char in s_hash_table:
                s_hash_table[char] = s_hash_table[char]  + 1

            else:
                s_hash_table[char] = 1

        for char in t:
            t_hash_table[char] = t_hash_table.get(char, 0) + 1
        
        return s_hash_table == t_hash_table

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []

        for str_element in strs:
            group_found = False

            for group in results:
                if self.isAnagram(group[0], str_element):
                    group.append(str_element)
                    group_found = True
                    break
            
            if not group_found:
                results.append([str_element])

        return results

from typing import List
from collections import defaultdict

class Solution2:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_map = defaultdict(list)
        
        for word in strs:
            # Create a key that represents the character frequency
            key = ''.join(sorted(word))
            anagram_map[key].append(word)
        
        return list(anagram_map.values())

if __name__ == "__main__":
    sol = Solution2()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
    # Expected: [["bat"],["nat","tan"],["ate","eat","tea"]]

    print(sol.groupAnagrams([""]))
    # Expected: [[""]]

    print(sol.groupAnagrams(["a"]))
    # Expected: [["a"]]

    print(sol.groupAnagrams(["abc", "acb", "bac", "bca", "cab", "cba", "def", "fed"]))
    # Expected: [["abc","acb","bac","bca","cab","cba"], ["def","fed"]]