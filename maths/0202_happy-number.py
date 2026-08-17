class Solution:
    def isHappy(self, n: int) -> bool:
        """Does iterating digit-square-sum reach 1, or loop forever?

        The iteration either hits 1 or enters a cycle — detect the
        cycle with Floyd's tortoise/hare (0141's trick, O(1) space).
        """
        def step(x: int) -> int:
            total = 0
            while x:
                x, d = divmod(x, 10)
                total += d * d
            return total

        slow, fast = n, step(n)
        while fast != 1 and slow != fast:
            slow = step(slow)
            fast = step(step(fast))
        return fast == 1


if __name__ == "__main__":
    assert Solution().isHappy(19)          # 19→82→68→100→1
    assert not Solution().isHappy(2)       # 2→4→16→37→58→89→145→42→20→4 cycle
    print("ok")
