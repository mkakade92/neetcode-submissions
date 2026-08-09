class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:



        graph = {i:[] for i in range(n)}

        for u,v,w in flights:

            graph[u].append([v,w])

        pq = []
        heapq.heappush(pq,(0,src,0))

        best = {}

        while pq:

            W,curr,stops = heapq.heappop(pq)

            if curr == dst:
                return W
            
            if stops > k:
                continue
            

            if curr in best and best[curr] <= stops:
                continue

            best[curr] = stops
            
            for i,w in graph[curr]:
                heapq.heappush(pq,(w+W,i,stops+1))
        return -1
            

