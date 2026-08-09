class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            st = [(i,j)]
            while st:
                x,y = st.pop()
                if x<0 or x>=rows or y<0 or y>=cols or grid[x][y]!='1':
                    continue
                grid[x][y]='#'
                st.append((x,y+1))
                st.append((x,y-1))
                st.append((x+1,y))
                st.append((x-1,y))
            return

        rows = len(grid)
        cols = len(grid[0])
        count = 0
        for i in range(rows):
            for j in range(cols):

                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)
        return count
        

        