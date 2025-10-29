from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        counter = 0
        largest = 0

        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                loopNum = num + 1
                while loopNum in numSet:
                    count += 1
                    loopNum += 1
                
                largest = max(largest, count)

        return largest



if __name__ == "__main__":
    sol = Solution()
    print(sol.longestConsecutive([100,4,200,1,3,2]))