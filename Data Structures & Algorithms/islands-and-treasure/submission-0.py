class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        



        def bfs(i,j):
            
            q = deque()
            q.append([i,j,0])
            visited=set()
            min_dist = float('inf')
            while q:
                x,y,dist = q.popleft()

                if x<0 or y<0 or x>=len(grid) or y>=len(grid[0]):
                    continue

                if grid[x][y]==-1:
                    continue
                
                if f"{x},{y}" in visited:
                    continue
                
                if grid[x][y]==0:
                    min_dist = min(min_dist,dist)
                    continue
                

                visited.add(f"{x},{y}")

                for neighX,neighY in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                    q.append([neighX,neighY,dist+1])
            return min_dist


        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2147483647:
                    minimum_dist = bfs(i,j)
                    if minimum_dist!=float('inf'):
                        grid[i][j] = minimum_dist


            