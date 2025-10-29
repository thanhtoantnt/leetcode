from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        htbl = {}

        for word in strs:
            key = "".join(sorted(word))
            if key not in htbl:
                htbl[key] = []

            htbl[key].append(word)

        return list(htbl.values())

if __name__ == "__main__":
    sol = Solution()
    print(sol.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))