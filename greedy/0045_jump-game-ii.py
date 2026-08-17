from typing import List 
class Solution:
    def jump(self, nums: List[int]) -> int:
        dp = [float('inf')] * len(nums)
        dp[0] = 0

        for index in range(len(nums)):
            # update next
            for i in range(index + 1, index + 1 + nums[index]):
                if i < len(nums):
                    dp[i] = min(dp[i], dp[index] + 1)
        
        return dp[len(nums) - 1]

class SolutionOpt:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l = r = 0
        
        while r < len(nums) - 1:
            furthest = 0

            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            
            l = r + 1
            r = furthest
            res += 1
        
        return res