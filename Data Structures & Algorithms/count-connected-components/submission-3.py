class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        


        graph = {}

        for i in range(n):
            graph[i] = []
        
        for s,d in edges:
            graph[s].append(d)
            graph[d].append(s)


        def dfs(ind,visited,graph):

            st =[]
            st.append(ind)

            while st:

                curr = st.pop()
                visited[curr]=True

                for x in graph[curr]:
                    if not visited[x]:
                        st.append(x)

        visited=[False]*n
        cnt = 0
        for i in range(n):
            if not visited[i]:
                dfs(i,visited,graph)
                cnt+=1
        return cnt
            