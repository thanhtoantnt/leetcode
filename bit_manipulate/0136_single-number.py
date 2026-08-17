from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """Every element appears twice except one — find it.

        XOR cancels pairs: a^a = 0 and XOR is commutative/associative,
        so folding XOR over the array leaves exactly the singleton.
        O(n) time, O(1) space.
        """
        x = 0
        for n in nums:
            x ^= n
        return x


if __name__ == "__main__":
    assert Solution().singleNumber([4, 1, 2, 1, 2]) == 4
    assert Solution().singleNumber([2, 2, 1]) == 1
    print("ok")
