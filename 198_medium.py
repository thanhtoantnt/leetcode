from typing import List

# Too slow, timeout in Leetcode
class SolutionNaive:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        if len(nums) == 1:
            return nums[0]
        
        return max(nums[0] + self.rob(nums[2:]), self.rob(nums[1:]))

class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        
        if len(nums) == 1:
            return nums[0]

        # reuse the computation
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for index in range(2, len(nums)):
            dp[index] = max(nums[index] + dp[index - 2], dp[index-1])
        
        return dp[-1]

class SolutionOpt:
    def rob(self, nums: List[int]) -> int:
        if not nums: return 0
        if len(nums) == 1: return nums[0]
        
        prev2, prev1 = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(nums[i] + prev2, prev1)
            prev2, prev1 = prev1, current
        
        return prev1

if __name__ == "__main__":
    sol = Solution()
    print(sol.rob([1,2,3,1]))     # Expected: 4
    print(sol.rob([2,7,9,3,1]))   # Expected: 12
    print(sol.rob([2,1,1,2]))     # Expected: 4
    print(sol.rob([1]))           # Expected: 1
    print(sol.rob([1,2]))         # Expected: 2