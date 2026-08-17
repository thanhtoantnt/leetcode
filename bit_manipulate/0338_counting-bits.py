from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        """popcount(i) for every i in 0..n.

        DP on bits: i & (i-1) is i with its lowest set bit removed, so
        bits[i] = bits[i & (i-1)] + 1. O(n) time and space.
        """
        bits = [0] * (n + 1)
        for i in range(1, n + 1):
            bits[i] = bits[i & (i - 1)] + 1
        return bits


if __name__ == "__main__":
    assert Solution().countBits(5) == [0, 1, 1, 2, 1, 2]
    print("ok")
