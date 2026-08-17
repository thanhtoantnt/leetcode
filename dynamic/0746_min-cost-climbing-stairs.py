from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        """Cheapest climb to the top (start at 0 or 1, pay the step you
        leave). 0070's Fibonacci shape with costs: the best to reach i
        is cost-to-step + min of the two ways below. O(n), O(1).
        """
        a, b = 0, 0  # best cost to reach step 0, step 1
        for i in range(2, len(cost) + 1):
            a, b = b, min(a + cost[i - 2], b + cost[i - 1])
        return b


if __name__ == "__main__":
    assert Solution().minCostClimbingStairs([10, 15, 20]) == 15
    assert Solution().minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]) == 6
    print("ok")
