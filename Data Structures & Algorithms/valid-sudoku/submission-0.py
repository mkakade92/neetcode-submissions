class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rC = [0]*9
        cC = [0]*9
        sC = [0]*9

        for i in range(9):
            for j in range(9):
                if board[i][j]=='.':
                    continue
            
                val = int(board[i][j]) - 1 
                if (1<<val) & rC[i]:
                    return False
                if (1<<val) & cC[j]:
                    return False
                if (1<<val) & sC[(i//3)*3+(j//3)]:
                    return False
            
                rC[i] |= (1<<val)
                cC[j] |= (1<<val)
                sC[(i//3)*3+(j//3)] |= (1<<val)
        
        return True        
