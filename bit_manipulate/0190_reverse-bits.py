class Solution:
    def reverseBits(self, n: int) -> int:
        """Reverse the 32 bits of n.

        Build the answer bit by bit: shift acc left, OR in n's lowest bit,
        shift n right — 32 rounds. O(1) (fixed 32 iterations).
        """
        acc = 0
        for _ in range(32):
            acc = (acc << 1) | (n & 1)
            n >>= 1
        return acc


if __name__ == "__main__":
    assert Solution().reverseBits(0b00000010100101000001111010011100) == 0b00111001011110000010100101000000
    assert Solution().reverseBits(1) == 1 << 31
    print("ok")
