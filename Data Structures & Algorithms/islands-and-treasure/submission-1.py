class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        


            
        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==0:
                    q.append((i,j))
        dist = 0
        while q:
            dist+=1
            for _ in range(len(q)):
                i,j = q.popleft()
                for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]==2147483647:
                        grid[x][y] = dist
                        q.append((x,y))

        


            