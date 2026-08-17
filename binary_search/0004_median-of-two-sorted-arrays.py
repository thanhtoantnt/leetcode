from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        """Median of two sorted arrays in O(log(m+n)).

        Binary search the partition of the SHORTER array: a cut position i
        (plus the implied j = half - i in the other) is correct when
        max-of-lefts <= min-of-rights. When found, the median reads off
        the four boundary elements.
        """
        a, b = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        m, n = len(a), len(b)
        half = (m + n + 1) // 2
        lo, hi = 0, m
        while lo <= hi:
            i = (lo + hi) // 2
            j = half - i
            aL = a[i - 1] if i > 0 else float("-inf")
            aR = a[i] if i < m else float("inf")
            bL = b[j - 1] if j > 0 else float("-inf")
            bR = b[j] if j < n else float("inf")
            if aL <= bR and bL <= aR:
                if (m + n) % 2:
                    return float(max(aL, bL))
                return (max(aL, bL) + min(aR, bR)) / 2
            if aL > bR:
                hi = i - 1
            else:
                lo = i + 1
        raise ValueError("unreachable for sorted inputs")


if __name__ == "__main__":
    assert Solution().findMedianSortedArrays([1, 3], [2]) == 2.0
    assert Solution().findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    print("ok")
