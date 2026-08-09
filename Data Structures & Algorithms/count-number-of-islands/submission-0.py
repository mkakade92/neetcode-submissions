class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j,row,cols):
            grid[i][j]='#'
            neighbours = [[i+1,j],[i-1,j],[i,j-1],[i,j+1]]

            for x,y in neighbours:
                if x>=0 and x<row and y>=0 and y<cols and grid[x][y]=='1':
                    dfs(x,y,row,cols)
            return

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j]=='#' or grid[i][j]=='0':
                    continue
                else:
                    count+=1
                    dfs(i,j,rows,cols)
        return count
        

        