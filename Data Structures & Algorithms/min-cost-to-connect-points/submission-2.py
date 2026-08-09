class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        
        pq = []

        heapq.heappush(pq,(0,0))


        visited = set()

        res = 0

        while pq:

            W,ind = heapq.heappop(pq)

            if ind in visited:
                continue
            
            visited.add(ind)
            res+=W

            for i in range(len(points)):
                if i !=ind:
                    dist = abs(points[i][0]-points[ind][0])+abs(points[i][1]-points[ind][1])
                    heapq.heappush(pq,(dist,i))
        
        return res


