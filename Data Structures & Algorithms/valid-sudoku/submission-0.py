class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        s = set()

        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val == '.':
                    continue

                elif (val,r) in s or (c, val) in s or (r//3,c//3,val) in s:
                    return False

                s.add((val , r))
                s.add((c,val))
                s.add((r//3,c//3,val))

        return True
