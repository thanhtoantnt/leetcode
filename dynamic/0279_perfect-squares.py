class Solution:
    def numSquares(self, n: int) -> int:
        """Fewest perfect squares summing to n (repetition allowed).

        Coin change with coin set {1, 4, 9, 16, ...}: dp[a] = 1 + min(dp[a - s])
        over squares s <= a. O(n·√n) time, O(n) space.
        (Lagrange's four-square theorem guarantees the answer is ≤ 4.)
        """
        dp = [0] + [float("inf")] * n
        for a in range(1, n + 1):
            s = 1
            while s * s <= a:
                dp[a] = min(dp[a], dp[a - s * s] + 1)
                s += 1
        return dp[n]


if __name__ == "__main__":
    assert Solution().numSquares(12) == 3  # 4 + 4 + 4
    assert Solution().numSquares(13) == 2  # 4 + 9
    print("ok")
