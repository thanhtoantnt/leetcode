from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        
        rows = len(matrix)
        cols = len(matrix[0])
        modifiedRows = []
        
        for i in range(rows):
            isZero = False
            for j in range(cols):
                if matrix[i][j] == 0:
                    isZero = True
            
            nRow = []
            for j in range(cols):
                if isZero:
                    nRow.append(0)
                else:
                    nRow.append(matrix[i][j])
            
            modifiedRows.append(nRow)

        result = []
        
        # print(f"modifiedRows = {modifiedRows}")
        for i in range(cols):
            isZero = False
            for j in range(rows):
                if matrix[j][i] == 0:
                    isZero = True
            
            nCol = []
            for j in range(rows):
                if modifiedRows[j][i] == 0 or isZero:
                    nCol.append(0)
                else:
                    nCol.append(matrix[j][i])

            # print(f"newCol = {nCol}")
            result.append(nCol)

        return [list(row) for row in zip(*result)]

class Solution2:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix or not matrix[0]:
            return
        
        m, n = len(matrix), len(matrix[0])
        first_row_zero = first_col_zero = False
        
        # Check if first row has zero
        for j in range(n):
            if matrix[0][j] == 0:
                first_row_zero = True
                break
        
        # Check if first column has zero
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        
        # Use first row and column as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0  # mark row
                    matrix[0][j] = 0  # mark column
        
        # Set zeros based on markers (skip first row/col for now)
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Handle first row
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Handle first column
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0

if __name__ == "__main__":
    sol = Solution()

    matrix = [[1,1,1],[1,0,1],[1,1,1]]
    print(sol.setZeroes(matrix))

    matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
    print(sol.setZeroes(matrix))
