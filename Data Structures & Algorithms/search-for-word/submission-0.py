class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        

        r = len(board)
        c = len(board[0])

        def dfs(i,j,ind):

            if ind==len(word):
                return True

            if i<0 or i>=r or j<0 or j>=c or word[ind] !=board[i][j] or board[i][j]=='#':
                return False

            board[i][j] = '#'
            found = False
            for x,y in [[0,1],[0,-1],[1,0],[-1,0]]:
                ni,nj = i+x,j+y
                found = found or dfs(ni,nj,ind+1)
            board[i][j] = word[ind]
            return found

        found = False
        for i in range(r):
            for j in range(c):
                found = found or dfs(i,j,0)
        return found



            

