class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])

        self.sum = [[0] * (COLS + 1) for _ in range(ROWS + 1)]

        for r in range(ROWS):
            for c in range(COLS):
                self.sum[r + 1][c + 1] = (
                    matrix[r][c]
                    + self.sum[r][c + 1]
                    + self.sum[r + 1][c]
                    - self.sum[r][c]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        bottomRight = self.sum[row2 + 1][col2 + 1]
        above = self.sum[row1][col2 + 1]
        left = self.sum[row2 + 1][col1]
        topLeft = self.sum[row1][col1]

        return bottomRight - above - left + topLeft