from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """Water trapped between bars after rain. Two pointers, O(n)/O(1).

        Water above bar i = min(max height left of i, max right of i) −
        height[i]. Keep running maxes from both ends; the pointer at the
        SMALLER wall is safe to resolve — its water is capped by that
        wall (a taller wall exists on the other side already).
        """
        l, r = 0, len(height) - 1
        left_max = right_max = 0
        water = 0
        while l < r:
            if height[l] < height[r]:
                left_max = max(left_max, height[l])
                water += left_max - height[l]
                l += 1
            else:
                right_max = max(right_max, height[r])
                water += right_max - height[r]
                r -= 1
        return water


if __name__ == "__main__":
    assert Solution().trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
    assert Solution().trap([4, 2, 0, 3, 2, 5]) == 9
    print("ok")
