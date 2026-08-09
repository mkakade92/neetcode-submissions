class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        



        q = deque()

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==2:
                    q.append((i,j))
        
        time = 0
        while q:
            print(f"time={time} and grid={grid}")
            for _ in range(len(q)):
                i,j = q.popleft()

                for x,y in [[i+1,j],[i-1,j],[i,j+1],[i,j-1]]:
                    if x>=0 and y>=0 and x<len(grid) and y<len(grid[0]) and grid[x][y]==1:
                        grid[x][y] = 2
                        q.append((x,y))
            if q:
                time+=1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]==1:
                    return -1
        return time