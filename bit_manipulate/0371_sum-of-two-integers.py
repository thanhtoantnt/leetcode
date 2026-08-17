class Solution:
    def getSum(self, a: int, b: int) -> int:
        """Add two integers without + or -.

        XOR is addition ignoring carries; (a & b) << 1 is exactly the
        carries. Repeat until no carries remain. Python needs a 32-bit
        mask because its ints are unbounded — loop inside the mask,
        then sign-extend negatives at the end.
        """
        mask = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)


if __name__ == "__main__":
    assert Solution().getSum(3, 5) == 8
    assert Solution().getSum(-2, 3) == 1
    print("ok")
