from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        result = []
        nums.sort()

        for index in range(0, len(nums) - 2):
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                if nums[left] + nums[right] == -nums[index]:
                    result.append((nums[index], nums[left], nums[right]))
                    left += 1
                    right -= 1
                
                elif nums[left] + nums[right] < -nums[index]:
                    left += 1
                else:
                    right -= 1
        
        deduplicated = set(result)

        filtered = []
        for element in deduplicated:
            filtered.append([element[0], element[1], element[2]])
        
        return filtered

class SolutionOpt:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 3:
            return []
        
        result = []
        nums.sort()

        for index in range(0, len(nums) - 2):
            # Skip duplicate values for the first element
            if index > 0 and nums[index] == nums[index - 1]:
                continue

            left = index + 1
            right = len(nums) - 1

            while left < right:
                total = nums[index] + nums[left] + nums[right]
                
                if total == 0:
                    result.append([nums[index], nums[left], nums[right]])
                    
                    # Skip duplicates for left pointer
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    # Skip duplicates for right pointer
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    
                    left += 1
                    right -= 1
                
                elif total < 0:
                    left += 1
                else:
                    right -= 1
        
        return result

if __name__ == "__main__":
    sol = Solution()
    nums=[-1,0,1,2,-1,-4]
    print(sol.threeSum(nums))