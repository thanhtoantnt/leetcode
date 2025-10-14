from typing import List

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        hash_table = {}
        start = 0
        max_sum = 0

        for index, num in enumerate(nums):
            if num in hash_table:
                # new subarray
                start = max(hash_table[num] + 1, start)
            
            hash_table[num] = index
            max_sum = max(max_sum, sum(nums[start: (index + 1)]))

        return max_sum


class SolutionOptimal:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        seen = {}
        start = 0
        max_sum = 0
        current_sum = 0
        
        for end, num in enumerate(nums):
            # If duplicate found, shrink window from left
            while num in seen and seen[num] >= start:
                current_sum -= nums[start]
                start += 1
            
            # Add current number to window
            seen[num] = end
            current_sum += num
            max_sum = max(max_sum, current_sum)
        
        return max_sum

if __name__ == "__main__":
    sol = Solution()
    # print(sol.maximumUniqueSubarray([4,2,4,5,6]))          # Expected: 17
    print(sol.maximumUniqueSubarray([5,2,1,2,5,2,1,2,5])) # Expected: 8
    # print(sol.maximumUniqueSubarray([1,2,3,4,5]))          # Expected: 15
    # print(sol.maximumUniqueSubarray([1,1,1,1]))     # Expected 1