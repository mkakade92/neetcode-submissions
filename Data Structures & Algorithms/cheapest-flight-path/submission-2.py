class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        


        dist = [float('inf')]*n
        dist[src] = 0
        for _ in range(k+1):
            temp = dist[:]
            for u,v,w in flights:
                if temp[u]!=float('inf') and w+temp[u]<dist[v]:
                    dist[v] = w+temp[u]
        
        return dist[dst] if dist[dst]!=float('inf') else -1