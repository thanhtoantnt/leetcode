class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        volumn = 0
        
        for i in range(len(heights) - 1):
            for j in range(i+1, len(heights)):
                volumn = max(volumn, min(heights[i], heights[j]) * (j - i))

        
        return volumn