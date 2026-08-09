class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        


        graph={i: [] for i in range(1,n+1)}

        for src,dest,time in times:

            graph[src].append([dest,time])
        


        q = []
        distances =[float('inf')]*(n+1)
        distances[k] = 0
        q.append([k,0])
        heapq.heapify(q)
        while q:

            curr_node,curr_dist = heapq.heappop(q)

            if curr_dist > distances[curr_node]:
                continue
            
            for neighbor,weight in graph[curr_node]:

                dist = curr_dist + weight

                if dist < distances[neighbor]:
                    distances[neighbor] = dist
                    heapq.heappush(q,[neighbor,dist])
        distances =  distances[1:]
        print(distances)
        for dist in distances:
            if dist==float('inf'):
                return -1
        return max(distances)
                