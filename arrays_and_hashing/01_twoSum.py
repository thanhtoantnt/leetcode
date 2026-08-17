from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        
        for index, number in enumerate(nums):
            complement = target - number
            if complement in hash_table:
                return [hash_table[complement], index]
            hash_table[number] = index
        
        return []

# testing
if __name__ == "__main__":
    sol = Solution()
    print(sol.twoSum([2,7,11,15], 9))    # Expected: [0,1] or [1,0]
    print(sol.twoSum([3,2,4], 6))        # Expected: [1,2] or [2,1]
    print(sol.twoSum([3,3], 6))          # Expected: [0,1] or [1,0]
    print(sol.twoSum([-1,-2,-3,-4], -7)) # Expected: [2,3] or [3,2]