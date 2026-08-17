from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """All distinct n-queens boards (no two queens share row, column,
        or diagonal). Row-by-row backtracking with three conflict sets:
        cols, positive-slope diagonals (r+c), negative-slope (r−c).
        """
        out: list[list[str]] = []
        cols: set[int] = set()
        diag1: set[int] = set()  # r + c
        diag2: set[int] = set()  # r - c
        queens: list[int] = []   # column per row

        def place(r: int) -> None:
            if r == n:
                out.append(["." * c + "Q" + "." * (n - c - 1) for c in queens])
                return
            for c in range(n):
                if c in cols or (r + c) in diag1 or (r - c) in diag2:
                    continue
                queens.append(c)
                cols.add(c); diag1.add(r + c); diag2.add(r - c)
                place(r + 1)
                queens.pop()
                cols.remove(c); diag1.remove(r + c); diag2.remove(r - c)

        place(0)
        return out


if __name__ == "__main__":
    assert len(Solution().solveNQueens(4)) == 2
    assert len(Solution().solveNQueens(1)) == 1
    print("ok")
