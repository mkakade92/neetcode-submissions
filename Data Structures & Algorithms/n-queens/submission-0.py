class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        

        board = [["."]*n for i in range(n)]
        res = []

        cols = set()
        posDiag =set()
        negDiag = set()


        def backtrack(row):
            if row==n:
                res.append(["".join(r) for r in board])
                return
            
            for col in range(n):
                if col in cols or row-col in posDiag or row+col in negDiag:
                    continue
                
                cols.add(col)
                posDiag.add(row-col)
                negDiag.add(row+col)

                board[row][col] = "Q"
                backtrack(row+1)
                board[row][col]="."
                cols.remove(col)
                posDiag.remove(row-col)
                negDiag.remove(row+col)
        
        
        backtrack(0)
        return res