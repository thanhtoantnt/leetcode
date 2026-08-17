from typing import List
import collections

class SolutionNaive:
    # naive solution: get max for each windows
    # Timeout when submitting to Leetcode
    def get_max(self, nums):
        assert(nums != [])
        max_num = nums[0]
        for num in nums:
            max_num = max(max_num, num)

        return max_num

    def maxSlidingWindow(self, nums, k):
        
        index = 0
        results = []
        while index + k <= len(nums):
            max_num = self.get_max(nums[index:(index + k)])
            results.append(max_num)
            index += 1
        
        return results
    
class Solution:
    def maxSlidingWindow(self, nums, k):
        results = []
        
        dq = collections.deque()

        for index, num in enumerate(nums):
            # pop an element in the head of the queue if it is smaller than the current one
            while dq and dq[0] < num:
                dq.popleft()
            
            # pop right if the element is smaller than the current one
            while dq and dq[-1] < num:
                dq.pop()

            # add to the queue
            dq.append(num)
            
            # print(dq)
            # pop the leftmost element
            if index >= k and dq and dq[0] == nums[index - k]:
                dq.popleft()

            # print(f"after pop: {dq}")
            # check for the window
            if index >= k - 1:
                results.append(dq[0])

        
        return results

class SolutionOpt:
    def maxSlidingWindow(self, nums, k):
        results = []
        dq = collections.deque()  # stores indices, not values
        
        for i, num in enumerate(nums):
            # Remove from right: elements smaller than current
            while dq and nums[dq[-1]] < num:
                dq.pop()
            
            # Add current index
            dq.append(i)
            
            # Remove from left: elements outside current window
            if dq[0] == i - k:
                dq.popleft()
            
            # Append result once we have full window
            if i >= k - 1:
                results.append(nums[dq[0]])
        
        return results

if __name__ == "__main__":
    sol = Solution()
    print(sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # Expected: [3,3,5,5,6,7]
    print(sol.maxSlidingWindow([1], 1))                   # Expected: [1]
    print(sol.maxSlidingWindow([1,-1], 1))                # Expected: [1,-1]
    print(sol.maxSlidingWindow([9,11], 2))                # Expected: [11]
    print(sol.maxSlidingWindow([4,-2], 2))                # Expected: [4]