from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """Rotate the array right by k, in place.

        Three reversals: reverse everything, then reverse the first k,
        then reverse the rest. A rotation is exactly (A B) -> (B A),
        and reversal-based block swap does it with O(1) extra space.
        O(n) time.
        """
        n = len(nums)
        k %= n

        def rev(lo: int, hi: int) -> None:
            while lo < hi:
                nums[lo], nums[hi] = nums[hi], nums[lo]
                lo += 1
                hi -= 1

        rev(0, n - 1)
        rev(0, k - 1)
        rev(k, n - 1)


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    Solution().rotate(nums, 3)
    assert nums == [5, 6, 7, 1, 2, 3, 4]
    print("ok")
