from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        """Largest all-1s square area in a binary matrix.

        dp[r][c] = side of the largest square whose bottom-right corner
        is (r,c) = 1 + min(up, left, up-left) when the cell is '1'.
        Area = (max side)². O(m·n) time, O(n) space with a rolling row.
        """
        n = len(matrix[0])
        prev = [0] * (n + 1)
        best = 0
        for row in matrix:
            cur = [0] * (n + 1)
            for c in range(1, n + 1):
                if row[c - 1] == "1":
                    cur[c] = 1 + min(prev[c - 1], prev[c], cur[c - 1])
                    best = max(best, cur[c])
            prev = cur
        return best * best


if __name__ == "__main__":
    m = [["1", "0", "1", "0", "0"], ["1", "0", "1", "1", "1"], ["1", "1", "1", "1", "1"], ["1", "0", "0", "1", "0"]]
    assert Solution().maximalSquare(m) == 4
    print("ok")
