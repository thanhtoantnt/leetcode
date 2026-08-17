from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """Fill the Sudoku board in place (unique solution guaranteed).

        Backtracking over empty cells with the three conflict sets from
        0036: rows, cols, 3x3 boxes. Try digits 1-9, recurse, undo.
        """
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empties = []
        for r in range(9):
            for c in range(9):
                v = board[r][c]
                if v == ".":
                    empties.append((r, c))
                else:
                    rows[r].add(v)
                    cols[c].add(v)
                    boxes[3 * (r // 3) + c // 3].add(v)

        def fill(i: int) -> bool:
            if i == len(empties):
                return True
            r, c = empties[i]
            b = 3 * (r // 3) + c // 3
            for d in "123456789":
                if d in rows[r] or d in cols[c] or d in boxes[b]:
                    continue
                board[r][c] = d
                rows[r].add(d); cols[c].add(d); boxes[b].add(d)
                if fill(i + 1):
                    return True
                board[r][c] = "."
                rows[r].discard(d); cols[c].discard(d); boxes[b].discard(d)
            return False

        fill(0)


if __name__ == "__main__":
    b = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
         [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
         ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
         [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
         [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    Solution().solveSudoku(b)
    assert b[0] == ["5", "3", "4", "6", "7", "8", "9", "1", "2"]
    print("ok")
