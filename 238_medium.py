from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # left pass
        left = [1] * len(nums)

        tmp = 1
        for index in range(1, len(nums)):
            tmp = nums[index-1] * tmp
            left[index] = tmp

        right = [1] * len(nums)

        rtmp = 1
        for index in range(1, len(nums)):
            rindex = len(nums) - 1 - index
            rtmp = rtmp * nums[rindex + 1]
            right[rindex] = rtmp

        results = []
        for index in range(len(nums)):
            results.append(left[index] * right[index])

        return results

def productExceptSelfOpt(self, nums: List[int]) -> List[int]:
    n = len(nums)
    answer = [1] * n
    
    # Left pass - store prefix products in answer
    prefix = 1
    for i in range(n):
        answer[i] = prefix
        prefix *= nums[i]
    
    # Right pass - multiply with suffix products
    suffix = 1
    for i in range(n-1, -1, -1):
        answer[i] *= suffix
        suffix *= nums[i]
    
    return answer

def test_product_except_self():
    sol = Solution()
    
    # Test case 1
    nums1 = [1,2,3,4]
    print(sol.productExceptSelf(nums1))  # Expected: [24,12,8,6]
    
    # Test case 2 - with zeros
    nums2 = [-1,1,0,-3,3]
    print(sol.productExceptSelf(nums2))  # Expected: [0,0,9,0,0]
    
    # Test case 3 - two elements
    nums3 = [2,3]
    print(sol.productExceptSelf(nums3))  # Expected: [3,2]
    
    # Test case 4 - negative numbers
    nums4 = [2,-3,4,-5]
    print(sol.productExceptSelf(nums4))  # Expected: [60,-40,30,-24]

test_product_except_self()

