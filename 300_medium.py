from typing import List

# Timeout by Leetcode
class SolutionNaive:
    def increasingSetWithMin(self, nums, min_num) -> int:
        if nums == []:
            return 0
   
        if nums[0] > min_num:
            return max(1 + self.increasingSetWithMin(nums[1:], nums[0]), self.increasingSetWithMin(nums[1:], min_num))
        else:
            return self.increasingSetWithMin(nums[1:], min_num)
        

    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.increasingSetWithMin(nums, -float('inf'))

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)

        for index_i in range(len(nums)):
            for index_j in range(index_i):
                if nums[index_j] < nums[index_i]:
                    dp[index_i] = max(dp[index_i], dp[index_j] + 1)

    
        return max(dp)

if __name__ == "__main__":
    sol = Solution()
    print(sol.lengthOfLIS([10,9,2,5,3,7,101,18]))  # Expected: 4
    print(sol.lengthOfLIS([0,1,0,3,2,3]))          # Expected: 4
    print(sol.lengthOfLIS([7,7,7,7,7,7,7]))        # Expected: 1
    print(sol.lengthOfLIS([1,3,6,7,9,4,10,5,6]))   # Expected: 6