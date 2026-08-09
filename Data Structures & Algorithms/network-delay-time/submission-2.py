class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # this is not bfs because
        # a -> b cost 100
        # a -> c cost 50
        # c -> b cost 10
        # if we did bfs


        graph = {i:[] for i in range(1,n+1)}


        for u,v,w in times:
            graph[u].append([v,w])
        
        pq = []
        dist = [float('inf')]*(n+1)
        dist[k] = 0
        heapq.heappush(pq,[0,k])

        while pq:

            W, curr = heapq.heappop(pq)

            if W < dist[curr]:
                continue
            
            for v,w in graph[curr]:

                if w+W < dist[v]:
                    dist[v] = w+W
                    heapq.heappush(pq,[dist[v],v])
        
        dist =dist[1:]
        if float('inf') in dist:
            return -1
        return max(dist)