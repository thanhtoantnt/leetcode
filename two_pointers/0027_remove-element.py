from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """Remove all occurrences of val in place; return the kept length.

        Reader/writer pointers (0026's skeleton with a value test):
        everything != val gets compacted to the front. O(n), O(1).
        """
        w = 0
        for r in range(len(nums)):
            if nums[r] != val:
                nums[w] = nums[r]
                w += 1
        return w


if __name__ == "__main__":
    nums = [0, 1, 2, 2, 3, 0, 4, 2]
    k = Solution().removeElement(nums, 2)
    assert k == 5 and sorted(nums[:k]) == [0, 0, 1, 3, 4]
    print("ok")
