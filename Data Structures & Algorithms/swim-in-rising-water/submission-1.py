class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        

        pq = []

        heapq.heappush(pq,(grid[0][0],0,0))
        r,c = len(grid),len(grid[0])

        dist = [[float('inf') for _ in range(c)] for _ in range(r)]

        dist[0][0] = 0
        while pq:

            time,x,y = heapq.heappop(pq)
            
            for i,j in [[x+1,y],[x-1,y],[x,y+1],[x,y-1]]:
                if i>=0 and i<r and j>=0 and j<c:
                    min_time_to_neigh = max(time,grid[i][j])
                    if  min_time_to_neigh < dist[i][j]:
                        dist[i][j] = min_time_to_neigh
                        heapq.heappush(pq,(dist[i][j],i,j))

        return dist[r-1][c-1]