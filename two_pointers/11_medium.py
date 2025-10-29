class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        volumn = 0
        
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                volumn = max(volumn, min(heights[i], heights[j]) * (j - i))

        
        return volumn

from typing import List

class SolutionOpt:
    def maxArea(self, heights: List[int]) -> int:
        left = 0
        right = len(heights) - 1
        max_volume = 0
        
        while left < right:
            # Calculate current volume
            height = min(heights[left], heights[right])
            width = right - left
            current_volume = height * width
            
            # Update maximum
            max_volume = max(max_volume, current_volume)
            
            # Move the pointer with the smaller height
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_volume