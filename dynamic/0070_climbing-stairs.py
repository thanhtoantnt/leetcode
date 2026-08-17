class Solution:
    def climbStairs(self, n: int) -> int:
        """Climbing 1 or 2 steps at a time: distinct ways to reach step n.

        Fibonacci in disguise: the last move is a 1-step (from n-1)
        or a 2-step (from n-2), so ways(n) = ways(n-1) + ways(n-2).
        O(n) time, O(1) space.
        """
        a, b = 1, 1
        for _ in range(n - 1):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    assert Solution().climbStairs(2) == 2
    assert Solution().climbStairs(3) == 3
    assert Solution().climbStairs(5) == 8
    print("ok")
