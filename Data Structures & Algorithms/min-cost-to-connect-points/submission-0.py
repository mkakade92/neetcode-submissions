class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        

        pq = []


        heapq.heappush(pq,(0,0))
        res = 0
        visited = set()
        while pq:

            weight, ind = heapq.heappop(pq)

            if ind in visited:
                continue

            res+=weight

            visited.add(ind)
            for i in range(len(points)):

                if i!=ind:
                    if i not in visited:
                        dist = abs(points[i][0]-points[ind][0])+abs(points[i][1]-points[ind][1])
                        heapq.heappush(pq,(dist,i))
            
        return res
            


