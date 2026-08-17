from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        """Count ordered combinations (permutations) of nums summing to
        target, with repetition.

        The coin-change counting table (0518) with the loops SWAPPED:
        amounts outer, coins inner — each order counted separately
        (1,1,2 ≠ 1,2,1). dp[t] = Σ dp[t - coin]. O(target · n).
        """
        dp = [1] + [0] * target
        for t in range(1, target + 1):
            for coin in nums:
                if coin <= t:
                    dp[t] += dp[t - coin]
        return dp[target]


if __name__ == "__main__":
    assert Solution().combinationSum4([1, 2, 3], 4) == 7
    print("ok")
