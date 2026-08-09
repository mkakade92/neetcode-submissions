class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        
        outD ={}

        graph ={}

        path  =[]

        for src,dest in tickets:
            outD[src] = outD.get(src,0)+1
            if src not in graph.keys():
                graph[src] = []
            graph[src].append(dest)
        
        for key in graph.keys():
            heapq.heapify(graph[key])
        


        def dfs(at):
            # print(f'at={at}')
            while outD.get(at,0)!=0:

                nxt = heapq.heappop(graph[at])
                # print(f'{at}->{nxt}')
                outD[at]-=1

                dfs(nxt)
            path.append(at)
        
        # print(graph)
        # print(f'indegree={inD}')
        # print(f'outDegree={outD}')

        dfs('JFK')
        return path[::-1]
