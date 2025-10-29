from typing import List
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []

        nums.sort()
        # print(nums)
        result = []
        for left in range(0, len(nums)):
            for right in range(len(nums) - 1, -1, -1):
                if right - left < 2:
                    continue

                second = left + 1

                third = right - 1

                while second < third:
                    # print(f"({nums[left]}, {nums[second]}, {nums[third]},  {nums[right]})")
                    curSum = nums[left] + nums[right] + nums[second] + nums[third]
                    if curSum == target:
                        result.append((nums[left], nums[second], nums[third], nums[right]))
                        second += 1
                        third -= 1

                    elif curSum < target:
                        second += 1
                    else:
                        third -= 1
        
        tupleSet = set(result)

        lists = []
        for element in tupleSet:
            lists.append([element[0], element[1], element[2], element[3]])

        return lists


class SolutionOpt:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        if len(nums) < 4:
            return []
        
        nums.sort()
        result = []
        n = len(nums)
        
        for i in range(n - 3):
            # Skip duplicates for first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
                
            for j in range(i + 1, n - 2):
                # Skip duplicates for second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                left = j + 1
                right = n - 1
                
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if current_sum == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        
                        # Move left pointer and skip duplicates
                        left += 1
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                            
                        # Move right pointer and skip duplicates  
                        right -= 1
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1
        
        return result

if __name__ == "__main__"
    sol = Solution()
    print(sol.fourSum([1,0,-1,0,-2,2], 0))
    # print(sol.fourSum([-2,-1,-1,1,1,2,2], 0))
