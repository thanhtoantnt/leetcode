from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """Unlimited transactions: sum every positive daily rise.

        Any optimal schedule's profit decomposes into adjacent-day
        gains (sell-rebuy costs nothing), so collecting every
        price[i] - price[i-1] > 0 is exact. O(n), O(1).
        """
        return sum(max(0, prices[i] - prices[i - 1]) for i in range(1, len(prices)))


if __name__ == "__main__":
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 7  # 4 + 3
    assert Solution().maxProfit([1, 2, 3, 4, 5]) == 4
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
    print("ok")
