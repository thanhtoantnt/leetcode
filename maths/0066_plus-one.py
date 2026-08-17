from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """Add 1 to the big-endian digit array. Ripple the carry from
        the last digit; a leftover carry prepends a 1. O(n).
        """
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0  # 9 becomes 0, carry continues left
        return [1] + digits  # all nines: 999 → 1000


if __name__ == "__main__":
    assert Solution().plusOne([1, 2, 3]) == [1, 2, 4]
    assert Solution().plusOne([9, 9]) == [1, 0, 0]
    print("ok")
