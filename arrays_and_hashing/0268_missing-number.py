from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """Array holds n distinct numbers from [0, n] — which is missing?

        Sum formula: n(n+1)/2 minus the actual sum. O(n) time, O(1)
        space. (XOR with each index/value — 0136's trick — also works.)
        """
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


if __name__ == "__main__":
    assert Solution().missingNumber([3, 0, 1]) == 2
    assert Solution().missingNumber([0, 1]) == 2
    print("ok")
