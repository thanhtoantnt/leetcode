from typing import List
from collections import Counter

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()

        result = []
        count = Counter(nums)
        perm = []
        def DFS():
            if len(perm) == len(nums):
                result.append(perm.copy())
                return

            for element in count:
                if count[element] > 0:
                    perm.append(element)
                    count[element] -= 1
                    DFS()

                    count[element] += 1
                    perm.pop()
        
        DFS()

        return result