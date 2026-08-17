class Solution:
    def hammingWeight(self, n: int) -> int:
        """Count 1-bits (popcount) of a 32-bit integer.

        Kernighan's trick: n &= n-1 clears the lowest set bit, so the
        loop runs once per set bit, not once per position. O(k) where
        k = number of 1s.
        """
        count = 0
        while n:
            n &= n - 1
            count += 1
        return count


if __name__ == "__main__":
    assert Solution().hammingWeight(0b1011) == 3
    assert Solution().hammingWeight(1 << 31) == 1
    print("ok")
