class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        


        def calcSize(i,j,visited):

            if f"{i},{j}" in visited:
                return 0
            
            if i<0 or i>=len(grid) or j<0 or j>=len(grid[0]):
                return 0
            
            if grid[i][j]==0:
                return 0

            sizeLocal = 1
            visited.add(f"{i},{j}")
            for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                sizeLocal+=calcSize(x,y,visited)
            return sizeLocal
    
        size = 0
        visited = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                size = max(size,calcSize(i,j,visited))
        return size
        

        
