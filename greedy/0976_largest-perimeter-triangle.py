from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        """Largest perimeter of a non-degenerate triangle from 3 sticks.

        Sort descending; the first a ≥ b ≥ c with b + c > a is the
        answer — any later triple has smaller parts, any earlier triple
        with this c fails the inequality harder. One pass, O(n log n).
        """
        nums.sort(reverse=True)
        for i in range(len(nums) - 2):
            if nums[i + 1] + nums[i + 2] > nums[i]:
                return nums[i] + nums[i + 1] + nums[i + 2]
        return 0


if __name__ == "__main__":
    assert Solution().largestPerimeter([2, 1, 2]) == 5
    assert Solution().largestPerimeter([1, 2, 1, 10]) == 0
    assert Solution().largestPerimeter([3, 2, 3, 4]) == 10
    print("ok")
