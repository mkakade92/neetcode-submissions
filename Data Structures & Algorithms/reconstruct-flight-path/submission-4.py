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
            st =[]
            st.append(at)
            while st:
                curr = st[-1]
                if outD.get(curr,0)==0:
                    st.pop()
                    path.append(curr)
                else:
                    nxt = heapq.heappop(graph[curr])
                    outD[curr]-=1
                    st.append(nxt)

        # print(graph)
        # print(f'indegree={inD}')
        # print(f'outDegree={outD}')

        dfs('JFK')
        return path[::-1]
