from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        result = [1] * len(nums)

        mul = 1
        for index, num in enumerate(nums):
            result[index] = mul
            mul = mul * num

        mul = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= mul
            mul = mul * nums[index]

        return result