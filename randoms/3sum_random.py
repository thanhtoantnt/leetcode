
def threeSum(nums):
    result = []
    
    nums.sort()
    # print(nums)

    for index in range(0, len(nums) - 2):
        if index > 0 and nums[index] == nums[index -1]:
            continue

        left = index + 1
        right = len(nums) - 1

        while left < right:
            threeSum = nums[left] + nums[right] + nums[index]
            # print(f"({index}, {nums[left]}, {right})")

            if threeSum == 0:
                result.append([nums[index], nums[left], nums[right]])
                left += 1
                right -= 1

                while left < right and nums[left - 1] == nums[left]:
                    left +=1
                
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif threeSum < 0:
                left += 1
            else:
                right -= 1
        
    return result
    
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))