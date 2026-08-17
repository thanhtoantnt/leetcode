from collections import Counter
from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        """Split the multiset into groups of k consecutive values —
        0846's greedy (heap-free Counter form): the minimum card must
        start its run; peel count[min] runs upward. O(n log n).
        """
        if len(nums) % k:
            return False
        count = Counter(nums)
        for start in sorted(count):
            need = count[start]
            if need <= 0:
                continue
            for v in range(start, start + k):
                if count[v] < need:
                    return False
                count[v] -= need
        return True


if __name__ == "__main__":
    assert Solution().isPossibleDivide([1, 2, 3, 3, 4, 4, 5, 6], 4)
    assert not Solution().isPossibleDivide([1, 2, 4, 5, 6, 7], 3)  # no 3 to finish 1,2,_
    print("ok")
