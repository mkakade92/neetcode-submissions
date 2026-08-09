class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        


        m,n = len(matrix),len(matrix[0])

        dp = [[None for _ in range(n)] for _ in range(m)]


        


        def dfs(x,y):

            if dp[x][y]:
                return dp[x][y]
            

            MAX = 1
            for i,j in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if i>=0 and j>=0 and i<m and j<n and matrix[x][y]<matrix[i][j]:
                        MAX = max(MAX,1+dfs(i,j))
            
            dp[x][y] = MAX
            return dp[x][y]
        
        MAXIMUM = 0
        for i in range(m):
            for j in range(n):
                MAXIMUM = max(MAXIMUM,dfs(i,j))
        return MAXIMUM

