from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero_count = 0  # More descriptive than 'count'
        start = 0
        max_len = 0

        for end, num in enumerate(nums):
            if num == 0:
                zero_count += 1
            
            # Shrink window if we have too many zeros
            while zero_count > k:
                if nums[start] == 0:
                    zero_count -= 1
                start += 1
            
            max_len = max(max_len, end - start + 1)
        
        return max_len
        
if __name__ == "__main__":
    sol = Solution()
    print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2))  # Expected: 6
    print(sol.longestOnes([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3))  # Expected: 10
    print(sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 0))  # Expected: 4
    print(sol.longestOnes([0,0,0,0], 2))  # Expected: 2