from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])

        firstRow = any(matrix[0][j] == 0 for j in range(cols))
        firstCol = any(matrix[i][0] == 0 for i in range(rows))

        # Mark rows and columns using the first row and column
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # Set marked rows to zero
        for i in range(1, rows):
            if matrix[i][0] == 0:
                for j in range(cols):
                    matrix[i][j] = 0

        # Set marked columns to zero
        for j in range(1, cols):
            if matrix[0][j] == 0:
                for i in range(rows):
                    matrix[i][j] = 0

        # Handle first row and first column
        if firstRow:
            for j in range(cols):
                matrix[0][j] = 0

        if firstCol:
            for i in range(rows):
                matrix[i][0] = 0