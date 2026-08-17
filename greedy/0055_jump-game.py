class Solution:
    def canJump(self, nums: List[int]) -> bool:
        l = r = 0
        furthest = 0

        while r < len(nums) -1 :
            for i in range(l, r + 1):
                furthest = max(furthest, i + nums[i])
            
            l = r + 1
            r = furthest

            if l > r:
                return False
        
        return True