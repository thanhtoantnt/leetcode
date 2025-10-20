from typing import List

# TooSlow
class SolutionNaive:
    def maxSubArray(self, nums: List[int]) -> int:
        assert(len(nums) > 0)

        m = len(nums)
        dp = [[0] * (m + 1) for _ in range(m + 1)]
        max_sum = nums[0]


        for i in range(m):
            index_i = m - 1 - i
            for j in range(m - 1, index_i - 1, -1):
                # index_j = m - 1 - j
                index_j = j
                if index_i == index_j:
                    dp[index_i][index_j] = nums[index_i]
                else:
                    dp[index_i][index_j] = nums[index_i] + dp[index_i + 1][index_j]
                
                # print(f"i = {index_i} j = {index_j} with dp = {dp[index_i][index_j]}")
                if dp[index_i][index_j] > max_sum:
                    max_sum = dp[index_i][index_j]

        return max_sum

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        current_sum = nums[0]
        
        for i in range(1, len(nums)):
            # Either extend the current subarray or start a new one
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))  # Expected: 6
    # print(sol.maxSubArray([1]))                       # Expected: 1
    print(sol.maxSubArray([5,4,-1,7,8]))             # Expected: 23
    # print(sol.maxSubArray([-1]))                      # Expected: -1
    # print(sol.maxSubArray([-2,-1]))                   # Expected: -1