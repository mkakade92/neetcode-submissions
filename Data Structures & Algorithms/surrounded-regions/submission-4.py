class Solution:
    def solve(self, board: List[List[str]]) -> None:
        


        q = deque()
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i==0 or i==len(board)-1 or j==0 or j==(len(board[0])-1)) and board[i][j]=='O':
                    q.append((i,j))
        

        while q:
            r,c = q.popleft()
            if board[r][c]=='O':
                board[r][c] = 'T'
                for x,y in [[r+1,c],[r-1,c],[r,c+1],[r,c-1]]:
                    if x>=0 and y>=0 and x<len(board) and y<len(board[0]):
                        q.append((x,y))

        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"



            