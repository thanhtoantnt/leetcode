from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        """Stock trading with unlimited transactions, each sale paying
        a flat fee. Two-state DP: hold (own stock) / cash (free to buy)
        — 0309's machine with the fee folded into the sell edge.
        O(n), O(1).
        """
        hold = float("-inf")  # best profit while holding a share
        cash = 0              # best profit holding nothing
        for p in prices:
            hold = max(hold, cash - p)        # buy, or keep holding
            cash = max(cash, hold + p - fee)  # sell (pay fee), or stay free
        return cash


if __name__ == "__main__":
    assert Solution().maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
    assert Solution().maxProfit([1, 3, 7, 5, 10, 3], 3) == 6
    print("ok")
